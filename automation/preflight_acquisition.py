"""Read-only preflight of immutable acquisition assets; no release approval."""
import csv, hashlib, json, pathlib, re, subprocess, xml.etree.ElementTree as ET
import fitz
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'preflight-output'
OUT.mkdir(exist_ok=True)
BASE='publishing/apress/acquisition-samples/'
PINS={'13':'22ecbf572e885cad992b261fc0b3181c01e654ed','16':'441dc92902ba26666ba6615af8ae9343baf45322','atlas':'dec94ae45dbbb7ada8e67571549224952fc018ea'}
def read(ref,path):
    return subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT)
def cmd(*args):
    return subprocess.check_output(args,stderr=subprocess.STDOUT,text=True)
def digest(b):return hashlib.sha256(b).hexdigest()
def norm(s):return re.sub(r'\s+','',s).replace('\u00ad','').replace('–','-').replace('—','-')
def pdf(ref,name,expected,chapter=None):
    data=read(ref,BASE+'proofs/'+name+'.pdf')
    p=OUT/(name+'.pdf');p.write_bytes(data)
    d=fitz.open(p)
    txt=' '.join(x.get_text() for x in d)
    fonts=cmd('pdffonts',str(p))
    info=cmd('pdfinfo',str(p))
    pages=[]
    for i,page in enumerate(d):
        prefix=OUT/f'{name}-{i+1:02}'
        cmd('pdftoppm','-f',str(i+1),'-l',str(i+1),'-singlefile','-r','144','-png',str(p),str(prefix))
        spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
        outside=[s['text'] for s in spans if not page.rect.contains(fitz.Rect(s['bbox']))]
        pages.append({'page':i+1,'size_pt':list(page.rect)[2:],'spans':len(spans),'outside_trim':outside,'replacement_chars':page.get_text().count('\ufffd'),'render_sha256':digest(prefix.with_suffix('.png').read_bytes()),'fonts':sorted(set(s['font'] for s in spans))})
    result={'name':name,'sha256':digest(data),'pages':len(d),'expected_pages':expected,'page_results':pages,'fonts_report':fonts,'tagged':bool(re.search(r'^Tagged:\s+yes',info,re.M|re.I)),'language':d.xref_get_key(d.pdf_catalog(),'Lang'),'approved_fonts':all(any(f in row for f in ['SourceSerif4','SourceSans3','JetBrainsMono']) for row in fonts.splitlines()[2:] if row.strip()),'links':sum(len(x.get_links()) for x in d)}
    if chapter:
        path=BASE+'manuscripts/chapter-'+chapter+('-context' if chapter=='13' else '-gateway-control-plane')+'-acquisition-v1.md'
        md=read(ref,path).decode()
        result['source_sha256']=digest(md.encode())
        result['figure_captions']={i:('Figure '+i) in txt for i in re.findall(r'\[Place Figure (\d+-\d+)',md)}
        result['table_captions']={i:('Table '+i) in txt for i in re.findall(r'\*Table (\d+-\d+)',md)}
        result['alt_markers']=sum(x.get_text().count('Alt text:') for x in d)
        # Exact field strings may wrap inside table columns; this is a presence test, not semantic equivalence.
        result['missing_headings']=[h for h in re.findall(r'^#{1,4} (.+)$',md,re.M) if norm(h) not in norm(txt)]
    else:
        ids=['01','10','14','18','26','30'] if name.endswith('sampler') else [name[-2:]]
        result['missing_defaults']=[]
        for i in ids:
            md=read(ref,'decisions/pages/D-'+i+'.md').decode()
            default=re.search(r'^\*\*Default\.\*\* (.+)$',md,re.M).group(1)
            if norm(default) not in norm(txt):result['missing_defaults'].append(i)
    return result
def svg(n,i):
    name=f'figure-{n}-{i}'
    b=read(PINS[n],BASE+'figures/'+name+'.svg')
    p=OUT/(name+'.svg');p.write_bytes(b)
    tree=ET.fromstring(b)
    png=OUT/(name+'.png')
    cmd('rsvg-convert','--zoom','2','-o',str(png),str(p))
    ns={'s':'http://www.w3.org/2000/svg'}
    return {'name':name,'sha256':digest(b),'render_sha256':digest(png.read_bytes()),'title':tree.findtext('s:title',namespaces=ns),'desc':tree.findtext('s:desc',namespaces=ns),'role':tree.get('role'),'labelledby':tree.get('aria-labelledby'),'viewBox':tree.get('viewBox'),'text_count':len(tree.findall('.//s:text',ns))}
report={'pins':PINS,'pdfs':[pdf(PINS[n],'chapter-'+n,k,n) for n,k in [('13',12),('16',10)]],'svgs':[]}
for i in ['01','10','14','18','26','30']:report['pdfs'].append(pdf(PINS['atlas'],'atlas-D-'+i,1))
report['pdfs'].append(pdf(PINS['atlas'],'atlas-six-page-sampler',6))
for n in ['13','16']:
    for i in range(1,4):report['svgs'].append(svg(n,i))
report['limitations']=['Rendered raster images require human visual inspection; automated coordinate checks do not establish overlap absence.','PDF tagging flag is not PDF/UA certification.','Expected page counts are prior proof counts, not approved budgets.']
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

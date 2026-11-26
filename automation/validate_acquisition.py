#!/usr/bin/env python3
"""Execute acquisition checks without altering any pinned source."""
import csv, hashlib, json, pathlib, re, subprocess, sys, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
VALID=ROOT/'governance/proposals/knowledge-system/authoring-validation'
PINS={'13':'22ecbf572e885cad992b261fc0b3181c01e654ed','16':'441dc92902ba26666ba6615af8ae9343baf45322','atlas':'dec94ae45dbbb7ada8e67571549224952fc018ea','package':'31872adf82758bccf53d50a8c3f10688b5f29df7'}
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])
def read(ref,path):
    return git('show',ref+':'+path)
def run(args):
    p=subprocess.run([sys.executable,*map(str,args)],capture_output=True,text=True,cwd=ROOT)
    return {'command':[sys.executable,*map(str,args)],'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def main():
    report={'pins':PINS,'validator_commit':git('rev-parse','HEAD').decode().strip(),'tests':{},'lint':{},'atlas':[],'manifest':[]}
    for phase,name in [('phase5','test_lint.py'),('phase7','test_lint_v2.py')]:
        report['tests'][phase]=run([VALID/phase/name])
    base='publishing/apress/acquisition-samples/'
    with tempfile.TemporaryDirectory() as tmp:
        for n,name in [('13','context'),('16','gateway-control-plane')]:
            path=base+f'manuscripts/chapter-{n}-{name}-acquisition-v1.md'
            data=read(PINS[n],path)
            f=pathlib.Path(tmp)/f'chapter-{n}.md';f.write_bytes(data)
            report['lint'][n]={'source_sha256':hashlib.sha256(data).hexdigest()}
            for phase,tool in [('phase5','lint_manuscript.py'),('phase7','lint_v2.py')]:
                report['lint'][n][phase]=run([VALID/phase/tool,'CH-0'+n,f])
            report['lint'][n]['strict_negative']=run([VALID/'phase7/lint_v2.py','CH-0'+n,f,'--strict'])
    cat=list(csv.DictReader((ROOT/'decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv').open(encoding='utf-8')))
    registry=json.loads((ROOT/'meridian/fixture/authoring-registry.json').read_text())
    known=set(registry['immutable_artifact_file_map'].values())|set(registry['immutable_keys']['request'])|set(registry['immutable_keys']['action'])
    known|={x['event_id'] for x in csv.DictReader((ROOT/'meridian/fixture/event-ledger.csv').open())}
    for id in ['D-01','D-10','D-14','D-18','D-26','D-30']:
        row=next(x for x in cat if x['id']==id)
        page=read(PINS['atlas'],f'decisions/pages/{id}.md').decode()
        refs=set(re.findall(r'\bMF-(?:EVD|EVT|REQ|ACT)-[A-Z0-9-]+\b',page))
        report['atlas'].append({'id':id,'default_exact':('**Default.** '+row['default']+'\n') in page,'unknown_evidence':sorted(refs-known)})
    manifest=read(PINS['package'],'publishing/apress/submissions/acquisition-source-manifest.csv').decode()
    for row in csv.DictReader(manifest.splitlines()):
        data=read(row['source_commit'],row['source_path'])
        blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
        report['manifest'].append({'path':row['source_path'],'match':blob==row['git_blob_sha1'] and len(data)==int(row['bytes']),'sha256':hashlib.sha256(data).hexdigest()})
    failed=any(x['exit_code'] for x in report['tests'].values()) or any(v[k]['exit_code'] for v in report['lint'].values() for k in ['phase5','phase7']) or any(v['strict_negative']['exit_code']!=1 for v in report['lint'].values()) or any(not x['default_exact'] or x['unknown_evidence'] for x in report['atlas']) or any(not x['match'] for x in report['manifest'])
    report['status']='BLOCK' if failed else 'MECHANICAL_PASS_NOT_APPROVED'
    pathlib.Path('acquisition-validation-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return int(failed)
if __name__=='__main__':sys.exit(main())

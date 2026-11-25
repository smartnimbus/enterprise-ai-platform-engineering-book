from pathlib import Path
import csv, zipfile, hashlib,json,collections
D=Path('/mnt/data/phase2_intellectual')
def read(n):
 with (D/n).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def write(n,rows):
 with (D/n).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
ch=read('CHAPTER-CTO-USEFULNESS-58.csv');gap=read('MISSING-CHAPTER-CONTENT-NOT-NEW-CHAPTERS.csv');d=read('DECISION-ATLAS-30-EDITORIAL-ASSESSMENT.csv');mr=read('MERIDIAN-LIFECYCLE-COVERAGE.csv');q=read('MISSING-DECISION-QUESTIONS-NOT-NEW-IDS.csv');s=read('CHAPTER-BRIEF-SECTIONS-348.csv')
chapter_reg=[]
for r in ch:
 n=int(r['chapter']); related=[x['gap_id'] for x in gap if str(n) in [p.strip() for chunk in x['existing_chapter_placement'].replace('Ch','').split(',') for p in chunk.split(';')] ]
 # Avoid unreliable ranges inference; source audit authoring gaps are separate catalogue.
 chapter_reg.append(dict(chapter=r['chapter'],chapter_title=r['title'],new_frozen_chapter_required='NO',has_outline='YES',has_authoring_blueprint='YES' if n in [13,16] else 'NO',has_standalone_manuscript='YES' if n==16 else 'NO',manuscript_status='DRAFT_REVIEW_REQUIRED' if n==16 else 'BLUEPRINT_ONLY' if n==13 else 'NOT_WRITTEN',manuscript_completion_estimate_pct=r['manuscript_readiness_pct'],technical_review='NOT_EVIDENCED',editorial_review='NOT_EVIDENCED',publication_ready='NO',primary_next_step='Independent technical/editorial review and production edit' if n==16 else 'Author full manuscript using frozen template with evidence-linked exercises',planned_artefact=r['planned_artefact'],decision_links=r['existing_decision_ids']))
write('MISSING-CHAPTER-REGISTER-58.csv',chapter_reg)
score=[
('Enterprise architecture completeness',6,2,'Business and capability views weaker than platform; no cross-domain independent proof'),
('Reference architecture completeness',7,2,'E/T/C/L + eight responsibilities strong; physical/deployment and runtime outcomes unverified'),
('CTO utility',7,1,'Potential decision value high; no external CTO/practitioner trial'),
('Enterprise relevance',8,2,'Requirements well framed; practical adoption and measured outcomes absent'),
('Governance coverage',7,2,'Roles, rules, gates specified; executed cross-plane evidence limited to synthetic case'),
('Educational quality',5,1,'Blueprint and two chapter briefs exist; one draft and no reviewed coherent syllabus'),
('Publisher readiness',3,0,'Proposal exists; no accepted full manuscript or confirmed acquisition'),
('Methodological reproducibility',6,1,'Method inferred, no independent participant reports'),
('Synthetic evidence coherence',8,5,'Six-record Meridian links consistent; does not certify production controls')]
write('REVISED-PROGRAMME-MATURITY-SCORECARD.csv',[dict(dimension=x,specified_0_to_10=a,independently_demonstrated_0_to_10=b,principal_evidence_gap=c)for x,a,b,c in score])
assert len(ch)==58 and len(set(x['chapter'] for x in ch))==58
assert len(d)==30 and len(set(x['id'] for x in d))==30
assert len(q)==19 and all(x['new_Atlas_id'].startswith('NO') for x in q)
assert len(gap)==25 and len(mr)==12 and len(s)==348
assert 330==sum(x['section_coverage']=='SPECIFIED_BRIEF' for x in s)
assert sum(r['has_standalone_manuscript']=='YES' for r in chapter_reg)==1
assert all(r['publication_ready']=='NO' for r in chapter_reg)
files=sorted([x for x in D.iterdir() if x.is_file() and x.suffix in ('.md','.csv','.png')])
provenance={'audit_date':'2026-11-24','scope':'Intellectual completeness and publisher readiness; no canonical file modified','source_inputs':[],'generated_files':[],'verification':{'chapters':58,'atlas_decisions':30,'section_brief_records':348,'section_briefs_explicit':330,'meridian_coverage_rows':12,'existing_decision_question_gaps':19,'missing_teaching_elements':25,'top25_publication_gaps':25,'chapter_manuscripts_present':1,'publication_ready_chapters':0}}
source_names=['Enterprise_AI_Agent_Fabric_Revised_TOC.csv','Enterprise_AI_Agent_Fabric_Development_Blueprint.md','Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv','style-v1.2.md','Chapter_13_Authoring_Blueprint_v1.0.md','Chapter_16_Authoring_Blueprint_v1.0.md','chapter-16-gateway-control-plane-v1.0.md','Meridian_Evidence_Fixture_v1.0.zip','convergence/REPOSITORY-CONVERGENCE-AUDIT-v1.0.md']
for f in source_names:
 p=Path('/mnt/data')/f
 provenance['source_inputs'].append(dict(path=f,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
for p in files:provenance['generated_files'].append(dict(path=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
(D/'EVIDENCE-AND-QA-MANIFEST.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
archive=Path('/mnt/data/PHASE-2-INTELLECTUAL-COMPLETENESS-ASSESSMENT-v1.0.zip')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for f in sorted(D.iterdir()):
  if f.is_file() and f.suffix in ('.md','.csv','.png','.json'): z.write(f,arcname=f.name)
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps({'archive':str(archive),'members':len(zipfile.ZipFile(archive).namelist()),'size_bytes':archive.stat().st_size,'manifest':provenance['verification'],'report_words':len((D/'PHASE-2-INTELLECTUAL-COMPLETENESS-AND-PUBLISHER-READINESS-v1.0.md').read_text().split())},indent=2))

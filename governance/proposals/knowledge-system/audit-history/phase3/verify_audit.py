"""Validates structural invariants of Phase 3 *derived* audit only.
It is not external peer review or deployed-platform assurance.
"""
import csv,json,re,collections,zipfile
from pathlib import Path
P=Path(__file__).parent

def rows(name):
 with open(P/name,encoding='utf8',newline='') as f:return list(csv.DictReader(f))

def check():
 res=[]
 def c(name,pred,detail):res.append({'check':name,'passed':bool(pred),'detail':detail})
 d=rows('DECISION-TRACEABILITY-30.csv');ch=rows('CHAPTER-DEPENDENCY-58.csv');lay=rows('LAYER-CONTROL-CONSISTENCY-12.csv');life=rows('LIFECYCLE-CONSISTENCY-11.csv');me=rows('MERIDIAN-EVENT-INTEGRITY-15.csv');terms=rows('TERMINOLOGY-AUDIT.csv');find=rows('CONTRADICTION-AND-RISK-REGISTER.csv')
 c('30 decision unique IDs',len(d)==30 and {x['decision_id'] for x in d}=={f'D-{i:02d}' for i in range(1,31)},f'{len(d)} rows')
 c('58 chapter unique IDs',len(ch)==58 and {x['chapter_id'] for x in ch}=={f'CH-{i:03d}' for i in range(1,59)},f'{len(ch)} rows')
 c('Four layers/eight control planes',len([x for x in lay if x['kind']=='STRUCTURAL_LAYER'])==4 and len([x for x in lay if x['kind']=='CONTROL_PLANE'])==8,'12 rows')
 c('11 lifecycle stages',len(life)==11 and {x['stage'] for x in life}=={f'S{i}' for i in range(11)},'Stages 0–10')
 c('15 synthetic fixture events',len(me)==15 and {x['event_id'] for x in me}=={f'MF-EVT-{i:03d}' for i in range(1,16)},'MF-EVT-001..015')
 c('References only known chapters',all(all(x in {r['chapter_id'] for r in ch} for x in re.findall(r'CH-\d{3}',r['catalogue_chapters']+' '+r['toc_chapters_expanded'])) for r in d),'30 crosswalks')
 c('References only known decisions',all(all(x in {r['decision_id'] for r in d} for x in re.findall(r'D-\d{2}',r['decision_ids_expanded'])) for r in ch),'58 chapter rows')
 c('Fixture event crosswalk references only known fixture events',all(all(x in {r['event_id'] for r in me} for x in re.findall(r'MF-EVT-\d{3}',r['meridian_events_derived_from_fixture'])) for r in d),'30 crosswalks')
 c('No false published validation grades',all('INFERRED' in x['validation_grade'] for x in d),'All event mappings explicitly inferred')
 c('Contradiction IDs unique',len(find)==len({x['finding_id'] for x in find}),f'{len(find)} findings')
 c('Controlled vocabulary not empty',len(terms)>=20,f'{len(terms)} terms')
 g={x['chapter_id']:[t.strip() for t in x['proposed_prerequisites'].split(';') if t.strip()] for x in ch};seen=set();active=set()
 def visit(v):
  if v in active:return False
  if v in seen:return True
  active.add(v)
  if not all(visit(u) for u in g[v]):return False
  active.remove(v);seen.add(v);return True
 c('No cycle in *proposed* teaching prerequisites',all(visit(v) for v in g),'Does not certify source-defined dependencies')
 filelist=sorted([x.name for x in P.glob('*.csv')])
 c('Derived registers present',len(filelist)>=10,', '.join(filelist))
 return res
if __name__=='__main__':
 r=check();p={'test_scope':'Derived Phase 3 files only','passed':sum(x['passed'] for x in r),'total':len(r),'checks':r,'fixture_validation':'Separate original fixture validator PASS 27/27; not independently verified'}
 (P/'DERIVED-QA-RESULTS.json').write_text(json.dumps(p,indent=2)+'\n')
 print(p['passed'],'/',p['total'])
 for x in r:
  if not x['passed']:print('FAIL',x)
 raise SystemExit(0 if p['passed']==p['total'] else 1)

import csv,json,re,hashlib,pathlib,sys
from collections import Counter
ROOT=pathlib.Path('/mnt/data'); OUT=ROOT/'phase6_trial'; sys.path.insert(0,str(ROOT/'phase5_validation'))
from lint_manuscript import lint
frozen={r['id']:r for r in csv.DictReader((ROOT/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv').open())}
a=(OUT/'author-a/CH13-INDEPENDENT-OUTLINE.md').read_text();b=(OUT/'author-b/CH16-INDEPENDENT-OUTLINE.md').read_text();c=(OUT/'author-c/F1-D10-D14-D18-SPECIMENS.md').read_text()
# Source exact text checks; comparing independently produced outputs, no edited frozen sources
sections={id:{'default_exact_in_c':row['default'] in c,'label_in_a':id in a,'label_in_b':id in b} for id,row in frozen.items() if id in ['D-10','D-11','D-12','D-13','D-14','D-18']}
# Positive output self-descriptions are not independently observed outcomes; record reviewer assertion with evidence.
comparison=[
('R01','Terminology','Context is a structural layer','A/B/C','AGREE','A labels Context structural; B references Context as data input; C does not redefine layers','MINOR'),
('R02','Ownership','Context never authorises external refund','A/B/C','AGREE','A explicit exclusion; B Gateway admission; C D-10 default exact','CRITICAL'),
('R03','Ownership','Gateway does not reconcile source business truth','A/B/C','AGREE','A stewardship; B policy input; C D-14 exact default','CRITICAL'),
('R04','Atlas','D-10 signed scoped receipt required before permitted mutation','B/C','AGREE','B separates normative allowed receipt from synthetic denial; C exact frozen default','CRITICAL'),
('R05','Atlas','D-14 conflict remains explicit unresolved','A/B/C','AGREE','Both manuscript plans preserve UNRESOLVED; C frozen default','CRITICAL'),
('R06','Atlas','D-18 routing/credentials/egress prevent bypass','B/C','AGREE','B distinguishes PEP from egress; C source-exact default','CRITICAL'),
('R07','Evidence','No refund posted or tool call','A/B/C','AGREE','No actor asserts financial side effect','CRITICAL'),
('R08','Evidence','Fixture is synthetic; does not establish deployed security','A/B/C','AGREE','Explicit caveats in all outputs','CRITICAL'),
('R09','Evidence','No signed Context handoff observed','A/C','AGREE','A distinguishes D-13 normative requirement; C silent','MAJOR'),
('R10','Lifecycle','No fabricated completed stage or release','A/B/C','AGREE','Lifecycle mappings labelled editorial; B separates release event','MAJOR'),
('R11','Evidence','No executed durable-memory write','A/B/C','AGREE','A explicitly identifies planned write gate and no observed receipt','CRITICAL'),
('R12','Scope','F6 headings and F7 headings not conflated','A/B','AGREE','A F6 headings, B F7 headings; outlines not full manuscripts','MAJOR'),
('R13','Provenance','Default quotes copied exactly in chapter outlines','A/B','NOT TESTABLE','Authors defer exact default text to final drafting rather than quoting it within outline','MAJOR'),
('R14','Publishing','Full chapter completion validated','A/B/C','NOT TESTABLE','Outlines and F1 candidate excerpts, not full finished prose','MAJOR'),
('R15','Independence','Three independent human authors contributed','A/B/C','NOT MET','All outputs are simulated within one assistant environment','CRITICAL'),
('R16','Authority','Atlas F1 specimens have approved human sign-off','C','NOT MET','Author C pages are unapproved candidate excerpts','CRITICAL'),
('R17','Vocabulary','All defined terms match approved glossary in complete prose','A/B/C','NOT TESTABLE','No complete chapters or approved terminology lint in production','MAJOR'),
('R18','Evidence','Cross-author same-claim provenance alignment','A/B/C','AGREE','D10/D14/D18 link to same frozen fixture records, narrower B operational mapping','CRITICAL')]
with (OUT/'reviewer/CROSS-AUTHOR-SEMANTIC-COMPARISON.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','dimension','check','participants','verdict','evidence_and_limit','severity_if_failed']);w.writerows(comparison)

# Mutation tests: phrase-level probes, no claim of exhaustive semantic detection.
mutation=[
('T01','invalid_decision','CH-016','# Chapter 16\nD-31 is mandatory',True),
('T02','fake_event','CH-013','# Chapter 13\nMF-EVT-999 is proof of rollout',True),
('T03','context_refund_authorises','CH-013','# Chapter 13\nContext authorises refund:execute for the external mutation.',True),
('T04','gateway_reconciles','CH-016','# Chapter 16\nGateway reconciles the retail product conflict.',True),
('T05','refund_posted','CH-016','# Chapter 16\nMeridian refund was posted.',True),
('T06','request_implies_execute','CH-016','# Chapter 16\nrefund:request implies refund:execute.',True),
('T07','production_fixture_claim','CH-016','# Chapter 16\nMeridian proves production network enforcement.',True),
('T08','legacy_security_plane','CH-013','# Chapter 13\nSecurity Plane controls the Context.',True),
('T09','undocumented_meridian_ungrounded','CH-013','# Chapter 13\nMF-EVT-005 proves user eligibility.',True),
('T10','gateway_grants_refund_using_synonym','CH-016','# Chapter 16\nGateway approved the payout and released funds.',True),
('T11','semantic_newest_wins','CH-013','# Chapter 13\nThe latest CRM record is canonical truth; CLOSED wins.',True),
('T12','context_concealed_unresolved','CH-013','# Chapter 13\nContext automatically resolves conflicting product states.',True),
('T13','fabricated_meridian_evidence_id','CH-016','# Chapter 16\nMF-EVD-PAY-999 proves mutation.',True),
('T14','unsafe_signed_claim','CH-016','# Chapter 16\nThe Meridian fixture issued a cryptographically signed permission token.',True),
('T15','invented_plane','CH-016','# Chapter 16\nThe Semantic Context Control Plane owns these checks.',True),
('T16','out_of_scope_history','CH-013','# Chapter 13\nThis chapter specifies the Gateway credential rotation implementation.',True),
('T17','wrong_chapter_title','CH-013','# Chapter 13: Identity Control Plane\nD-14',True),
('T18','false_resolution_simplified','CH-013','# Chapter 13\nMF-EVD-RC-001 was reconciled.',True),
('T19','correct_synthetic_denial','CH-016','# Chapter 16\nMeridian synthetic MF-EVT-013 records a blocked direct-egress test; not production proof. D-18.',False),
('T20','negated_overclaim_with_long_range','CH-016','# Chapter 16\nThe Meridian fixture does not prove that all deployed networking rules block every route. D-18.',False),
('T21','correct_conflict','CH-013','# Chapter 13\nMeridian synthetic `MF-EVD-RC-001` remains UNRESOLVED. D-14.',False),
('T22','no_atlas_reference','CH-013','# Chapter 13\nContext is governed retrieval.',False),
]
rows=[]
for ident,kind,ch,text,should_block in mutation:
 result=lint(ch,text); blocked=result['status']=='BLOCK';rows.append([ident,kind,ch,should_block,blocked,result['counts']['WARN'], 'PASS' if should_block==blocked else 'MISS' if should_block else 'FALSE_BLOCK',';'.join(x['rule'] for x in result['diagnostics'])]);
with (OUT/'reviewer/LINT-MUTATION-BENCHMARK.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','mutation','chapter','expected_block','observed_block','warnings','assessment','triggered_rules']);w.writerows(rows)
TP=sum(r[3] and r[4] for r in rows); FN=sum(r[3] and not r[4] for r in rows); FP=sum(not r[3] and r[4] for r in rows);TN=sum(not r[3] and not r[4] for r in rows)
meta={'phase':'PHASE-6','run_kind':'single-environment role-isolated source-pack simulation; NOT independent human validation','source_files':{},'comparison':dict(Counter(r[4] for r in comparison)),'pilot':{'A':'OUTLINE_ONLY','B':'OUTLINE_ONLY','C':'F1_SOURCE_EXACT_CANDIDATE'},'lint':{'positive_cases':TP+FN,'detected':TP,'missed':FN,'negative_cases':TN+FP,'true_negative':TN,'false_blocks':FP,'recall_percent':round(TP/(TP+FN)*100,1),'specificity_percent':round(TN/(TN+FP)*100,1)},'reference_source_integrity':sections,'original_phase5_unit_test_total':18,'no_actual_independent_authors':True,'no_actual_human_review':True}
for p in [ROOT/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv',ROOT/'style-v1.2.md',ROOT/'Chapter_13_Authoring_Blueprint_v1.0.md',ROOT/'Chapter_16_Authoring_Blueprint_v1.0.md',ROOT/'Meridian_Evidence_Fixture_v1.0.zip',ROOT/'phase4_authoring/CHAPTER-AUTHORING-CONTRACTS-58.csv',ROOT/'phase5_validation/RECONCILED-ATLAS-TOC-LINKS.csv']:
 meta['source_files'][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'reviewer/TRIAL-RESULTS.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps({'comparison':meta['comparison'],'lint':meta['lint']},indent=2))

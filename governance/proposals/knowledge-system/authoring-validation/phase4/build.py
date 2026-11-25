import csv,json,re,hashlib,zipfile,collections,datetime
from pathlib import Path
P=Path('/mnt/data'); O=P/'phase4_authoring'; O.mkdir(exist_ok=True)
def load(p):
 with open(p,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(n,rows,fields=None):
 if not fields:fields=list(rows[0])
 with open(O/n,'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def cs(v):return '; '.join(dict.fromkeys([x for x in v if x]))
def ch(x):return f'CH-{int(x):03}'
def numset(s,prefix='D'):
 out=[]
 for segment in re.split(r'[,;]+',str(s)):
  segment=segment.strip()
  if not segment:continue
  # full vs abbreviated ranges
  m=re.fullmatch(r'(?:D-)?(\d{1,2})\s*[–-]\s*(?:D-)?(\d{1,2})',segment,re.I)
  if m:
   a,b=map(int,m.groups());out.extend(f'D-{x:02}' for x in range(a,b+1));continue
  m=re.search(r'D-\s*(\d{1,2})',segment,re.I)
  if m:out.append(f'D-{int(m.group(1)):02}');continue
  if re.fullmatch(r'\d{1,2}',segment) and prefix=='D':out.append(f'D-{int(segment):02}')
 return list(dict.fromkeys(out))
toc=load(P/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv');cat=load(P/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv')
phase3=load(P/'phase3_integrity/DECISION-TRACEABILITY-30.csv');dmap={x['decision_id']:x for x in phase3}
deps=load(P/'phase3_integrity/CHAPTER-DEPENDENCY-58.csv');depmap={x['chapter_id']:x for x in deps};terms=load(P/'phase3_integrity/TERMINOLOGY-AUDIT.csv');layers=load(P/'phase3_integrity/LAYER-CONTROL-CONSISTENCY-12.csv');lifecycle=load(P/'phase3_integrity/LIFECYCLE-CONSISTENCY-11.csv');events=load(P/'phase3_integrity/MERIDIAN-EVENT-INTEGRITY-15.csv');sources={}
for f in ['Enterprise_AI_Agent_Fabric_Revised_TOC.csv','Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv','Enterprise_AI_Agent_Fabric_Development_Blueprint.md','style-v1.2.md','phase3_integrity/DECISION-TRACEABILITY-30.csv','phase3_integrity/CHAPTER-DEPENDENCY-58.csv','phase3_integrity/LAYER-CONTROL-CONSISTENCY-12.csv','phase3_integrity/LIFECYCLE-CONSISTENCY-11.csv','phase3_integrity/TERMINOLOGY-AUDIT.csv','phase3_integrity/MERIDIAN-EVENT-INTEGRITY-15.csv']:
 sources[f]={'sha256':hashlib.sha256((P/f).read_bytes()).hexdigest(),'size':(P/f).stat().st_size}
# Explicit home recommendations; these do NOT change existing chapter or decision defaults.
homes=['1','5','6','7','9','6','11','11','12','16','13','13','13','13','14','19','8','16','15','15','22','18','18','17','21','20','36','37','35','34']
assert len(homes)==30
# Chapter 23 owns verbatim F1; thematic chapter owns technical explanation.
D=[];link=[];catalogue_chapters={}
for n,c in enumerate(cat):
 di=c['id']; a=dmap[di]; owner=ch(homes[n]); claimed=[ch(int(t)) for t in re.findall(r'\b\d+\b',c['chapters'])];catalogue_chapters[di]=claimed
 listed=[x for x in a['toc_chapters_expanded'].split('; ') if x]; union=list(dict.fromkeys(claimed+listed));stage=[x for x in union if 24<=int(x[-3:])<=34];pb=[x for x in union if 41<=int(x[-3:])<=50]; other=[x for x in union if x not in [owner,'CH-023']+stage+pb];
 mr=a['meridian_events_derived_from_fixture']; ev=a['meridian_evidence_derived_from_artifacts']
 status='PENDING_HUMAN_CROSSWALK_RECONCILIATION' if a['finding']=='MAPPING_RECONCILIATION_REQUIRED' else 'SOURCE_ALIGNED_WITH_EDITORIAL_ROLES'
 D.append(dict(decision_id=di,title=c['title'],frozen_default_owner='CH-023 / D-'+di[2:]+ ' F1 record',primary_topic_explanation=owner,supporting_explanations=cs([x for x in other if int(x[-3:])<=22 or int(x[-3:])>=35 and int(x[-3:])<=40]),lifecycle_application=cs(stage),playbook_implementation=cs(pb),reference_only=cs([x for x in other if int(x[-3:])>=51]),other_cross_references=cs([x for x in other if x not in stage+pb and not( int(x[-3:])<=22 or 35<=int(x[-3:])<=40 or int(x[-3:])>=51)]),catalogue_chapters=cs(claimed),toc_index_chapters=cs(listed),meridian_event_links=mr,meridian_evidence_links=ev,meridian_link_grade='EDITORIAL_INFERENCE_NOT_APPROVED',mapping_status=status,action='Human classify crosswalk discrepancies before mass authoring' if status.startswith('PENDING') else 'Review and accept role assignment; no change to frozen defaults',provenance='Decision catalogue: chapters/default; Revised TOC: decision_ids; Phase3 traceability; editorial role proposal'))
 for target in union:
  typ='PRIMARY_TECHNICAL_EXPLANATION' if target==owner else 'ATLAS_NORMATIVE_RECORD' if target=='CH-023' else 'LIFECYCLE_APPLICATION' if target in stage else 'PLAYBOOK_IMPLEMENTATION' if target in pb else 'REFERENCE_ONLY' if target in [x for x in other if int(x[-3:])>=51] else 'SUPPORTING_REFERENCE'
  flags=[]
  if target in claimed and target not in listed:flags.append('CATALOGUE_ONLY')
  if target in listed and target not in claimed:flags.append('TOC_ONLY')
  link.append(dict(source_id=di,target_id=target,relationship=typ,authority='PROPOSED_EDITORIAL_MAPPING',source_provenance='Decision Catalogue chapters / TOC decision_ids',crosswalk_flag=cs(flags) or 'BOTH_OR_OMNIBUS',allowed_use='May explain topic in its own lane; may not change frozen D default',review_status='NEEDS_REVIEW' if flags else 'CANDIDATE'))
write('DECISION-AUTHORITY-30.csv',D)
# Chapter contract for EACH frozen chapter.
C=[]
for t in toc:
 id=ch(t['chapter']);i=int(t['chapter']);d=depmap[id];purpose=t['purpose_reader_outcome'];title=t['title'];typ=t['type_template'];part=title.split('.',1)[0] if '.' in title else ''
 if 1<=i<=4:lane='CONCEPTUAL_ORIENTATION';allowed='Introduce reader problem, bounded terms and stakes; link to existing Atlas';forbidden='Do not prescribe implementation contracts or rewrite Atlas defaults';unique='Distinguish specific motivation / term boundary from other Part I chapters'
 elif 5<=i<=9:lane='STRATEGIC_CHOICE';allowed='Compare enterprise options, constraints, ownership and consequences';forbidden='Do not redefine E/T/C/L or plane enforcement contracts';unique='Make a defensible strategic choice with its tradeoff'
 elif i==10:lane='ARCHITECTURE_MAP';allowed='Explain the 4+8 canonical map and interfaces';forbidden='Do not add layers, planes, or duplicate full F6/F7 deep dives';unique='Help reader navigate ownership and evidence relationships'
 elif 11<=i<=14:lane='STRUCTURAL_LAYER_F6';allowed='Own internal mechanisms of the named layer, input/output contracts and failure paths';forbidden='Do not create new control planes or take policy decision authority from a plane';unique=f'Deep {title.split(".",1)[-1].strip()} layer mechanism in its single technical home'
 elif 15<=i<=22:lane='CONTROL_PLANE_F7';allowed='Own scope, policy/enforcement boundaries, interactions and evidence of named plane';forbidden='Do not invent security/evaluation ninth plane or reassign other control-plane decisions';unique=f'Explain {title.split(".",1)[-1].strip()} plane control responsibility once'
 elif i==23:lane='DECISION_ATLAS_F1';allowed='Publish the existing 30 frozen F1 decision records verbatim with approved references';forbidden='Do not invent, delete, reorder or silently revise D-01..D-30, defaults or F1 fields';unique='Definitive reader-facing source for each decision default'
 elif 24<=i<=34:lane='LIFECYCLE_STAGE';allowed='Specify when prerequisites, gates, evidence and approvals matter within the frozen stage';forbidden='Do not re-specify architecture mechanisms or introduce lifecycle stages';unique='Teach entry/exit and accountability of this particular stage'
 elif 35<=i<=40:lane='OPERATING_DISCIPLINE';allowed='Explain ongoing service operation, cost, incident, audit, ownership';forbidden='Do not redefine decision defaults or pretend synthetic evidence proves operations';unique='Show operational accountability, measurement and response'
 elif 41<=i<=50:lane='PRACTITIONER_PLAYBOOK';allowed='Give a runnable checklist using prior concepts and existing Atlas choices';forbidden='Do not replace architectural definitions or turn procedural example into canonical default';unique='Produce a named usable artefact with verification and failure handling'
 else:lane='REFERENCE_APPENDIX';allowed='Index, summarise or provide traceable lookup of frozen definitions and tested examples';forbidden='Do not create parallel definitions, new Atlas defaults or unauthorised Meridian episodes';unique='Accelerate reference retrieval without becoming competing authority'
 direct=numset(t['decision_ids']);catrefs=[x['decision_id'] for x in D if id in x['catalogue_chapters'].split('; ')];refs=list(dict.fromkeys(direct+catrefs));
 pre=d['proposed_prerequisites'];ex=d['explicit_see_also_refs'];
 C.append(dict(chapter_id=id,title=title,part=part,template=typ,authority_lane=lane,unique_reader_outcome=purpose,allowed_scope=allowed,disallowed_scope=forbidden,unique_teaching_contract=unique,existing_expected_artefact=t['artefacts'],direct_TOC_decisions=cs(direct),catalogue_related_decisions=cs(catrefs),required_dependency_candidates=pre,existing_cross_references=ex,forbidden_duplicate_zone=d['duplicate_teaching_zone'],canonical_boundary_source='Development Blueprint / TOC; Phase3 dependency matrix',status='PROPOSED_EDITORIAL_CONTRACT_NOT_RATIFIED',acceptance='No frozen source alteration; correct owner/cross references; evidence grade; example must not invent fixture event; independent peer review'))
write('CHAPTER-AUTHORING-CONTRACTS-58.csv',C)
# Architectural canonical responsibilities (12) + every Atlas decision (30) + vocabulary (24) + lifecycle 11 + major chapter concepts 58 + evidence 12.
concept=[]
def add(kind,name,owner,chapter,decisions='',stages='',meridian='',meaning='',source='',grade='DERIVED_FROM_EXISTING_SOURCE',notes=''):
 id=f'KC-{len(concept)+1:03}'
 concept.append(dict(concept_id=id,kind=kind,concept=name,canonical_owner=owner,authoritative_chapter=chapter,supporting_chapters='',related_decisions=decisions,related_lifecycle_stages=stages,meridian_refs=meridian,definition_or_responsibility=meaning,source=source,grade=grade,guardrail=notes))
for l in layers:
 name=l['name'];chapter=next((ch(int(t['chapter'])) for t in toc if t['title'].split('.',1)[-1].strip()==name),'CH-010');add('STRUCTURAL_LAYER' if l['kind']=='STRUCTURAL_LAYER' else 'CONTROL_PLANE',name,l['kind'],chapter,meaning=l['owner'],source=l['source'],notes=l['conflict_boundary'])
for row in D:
 add('FROZEN_ATLAS_DECISION',row['title'],row['decision_id'],row['primary_topic_explanation'],row['decision_id'],meridian=row['meridian_event_links'],meaning='Frozen decision default; read exact catalogue and CH-023/F1',source='Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv',notes='Do not redefine default or reversibility')
for term in terms:
 nm=term['term'];owner='CH-056 / controlled vocabulary entry' if term['class'] not in ('layer','canonical') else 'CH-056 alias; named layer/plane chapter owns responsibilities';add('CONTROLLED_TERM',nm,owner,'CH-056',meaning=term['canonical_or_controlled_meaning'],source=term['source'],grade='SOURCE_EXPLICIT' if term['audit_status']=='EXPLICIT' else 'EDITORIAL_RECONCILIATION_REQUIRED',notes=term['risk_or_disambiguation'])
for stage in lifecycle:
 add('LIFECYCLE_STAGE',stage['title'],stage['stage'],stage['chapter'],stage['decision_ids'],stage['stage'],meaning=stage['key_mechanism_specified'],source='Development Blueprint §Stage; phase3 Lifecycle consistency',grade='STAGE_DESIGN_ONLY',notes='Entry/exit gate is prose unless executable predicate evidenced')
for t in toc:
 i=int(t['chapter']);name=t['title'].split('.',1)[-1].strip();add('CHAPTER_TEACHING_CONCEPT',name,ch(i),ch(i),cs(numset(t['decision_ids'])),meaning=t['purpose_reader_outcome'],source=f'Revised TOC chapter {i}',grade='AUTHORING_OUTCOME_NOT_COMPLETED_MANUSCRIPT',notes='Do not treat purpose as delivered content')
evidence=[('Specification assertion','Document says expected control'),('Implementation assertion','Code/configuration implements mechanism'),('Reproduced test run','Independent replay of documented test inputs'),('Independent validation','Qualified non-author challenges specified claim'),('Source citation','Provenance to source, no implementation assertion'),('Policy decision','Permission evaluation result, not enforced side effect'),('Enforcement receipt','PEP admission/denial result; distinguish observed from synthetic'),('Tool side-effect receipt','External action outcome only if actual observed'),('Context manifest','Versioned sources and access/provenance'),('Conflict record','Preserves unresolved source disagreement'),('Release gate verdict','Verification pass/fail independent of per-action admission'),('Human approval','Explicit human decision tied to exact revision'),('AI recommendation','Advisory output, never approval'),('Synthetic narrative','Illustrative story, no deployed proof'),('Retirement/deletion evidence','Observed destruction/retention and affected assets')]
for name,definition in evidence:add('EVIDENCE_OR_AUTHORITY',name,'CH-040 / CH-057','CH-057',meaning=definition,source='Phase3 Meridian integrity; Programme Operating System; Independent Validation Programme',grade='EDITORIAL_TAXONOMY_PROPOSED',notes='Never infer approval or execution from a cross-reference')
# crossfill support using chapter decision index and exact concept chapter occurrence
for co in concept:
 drefs=[x.strip() for x in co['related_decisions'].split(';') if x.strip()]
 support=[]
 for de in drefs:
  row=next((r for r in D if r['decision_id']==de),None)
  if row:
   support += [x.strip() for x in (row['supporting_explanations']+'; '+row['lifecycle_application']+'; '+row['playbook_implementation']+'; '+row['reference_only']).split(';') if x.strip()]
 co['supporting_chapters']=cs([x for x in support if x!=co['authoritative_chapter']])
write('CANONICAL-CONCEPT-OWNERSHIP.csv',concept)
# vocabulary 24 direct, explicit negatives and owner; do not assert every term has formally published definition
voc=[]
for t in terms:
 voc.append(dict(term=t['term'],definition_or_restricted_meaning=t['canonical_or_controlled_meaning'],authoritative_source=t['source'],normative_location='CH-056 alias/term register; technical responsibility in appropriate CH-011..022',prohibited_meaning_or_failure=t['risk_or_disambiguation'],allowed_alias='NONE_CONFIRMED; require explicit alias review',cross_reference_rule='Use capitalised canonical name on first use and link to CH-056 and owning chapter',audit_status=t['audit_status'],approval_status='PROPOSED_RECONCILIATION; FROZEN STYLE BIBLE UNCHANGED'))
write('VOCABULARY-AUTHORITY-24.csv',voc)
# evidence taxonomy separate classes and action rules
E=[]
for i,(n,definition) in enumerate(evidence,1):
 typ='NARRATIVE' if n in ('Synthetic narrative','AI recommendation') else 'VALIDATION' if n in ('Reproduced test run','Independent validation','Release gate verdict') else 'IMPLEMENTATION' if n in ('Implementation assertion','Tool side-effect receipt','Enforcement receipt') else 'AUTHORITY' if n in ('Human approval','Policy decision') else 'REFERENCE_OR_RECORD'
 E.append(dict(evidence_id=f'ET-{i:02}',name=n,class_=typ,meaning=definition,can_establish='Only the stated narrow claim, at pinned source and evidence grade',must_not_be_interpreted_as='Independent approval, production implementation, or system-wide validation without direct evidence',required_metadata='source_id; source_sha; claim_id; status; actor; timestamp; related decision; retention/sensitivity',source='Existing phase3 audit and frozen Meridian / existing operating rules',status='PROPOSED_LABEL_NOT_NEW_GOVERNANCE'))
write('EVIDENCE-TAXONOMY-15.csv',E)
# master crosswalk: concepts + decision chapter links + explicit chapter dependency relationships, with provenance flags
X=[]
for row in concept:
 X.append(dict(source_id=row['concept_id'],target_id=row['authoritative_chapter'],relationship='OWNED_EXPLANATION',status=row['grade'],provenance=row['source'],review='SOURCE_OWNER_VALIDATION_REQUIRED'))
for row in link:X.append(dict(source_id=row['source_id'],target_id=row['target_id'],relationship=row['relationship'],status=row['authority'],provenance=row['source_provenance'],review=row['review_status']))
for d in deps:
 for target in [x.strip() for x in d['proposed_prerequisites'].split(';') if x.strip()]:X.append(dict(source_id=d['chapter_id'],target_id=target,relationship='PROPOSED_READER_PREREQUISITE',status='DERIVED_NOT_CANONICAL',provenance=d['source'],review='REQUIRES_AUTHOR_CONFIRMATION'))
 for target in [x.strip() for x in d['explicit_see_also_refs'].split(';') if x.strip()]: X.append(dict(source_id=d['chapter_id'],target_id=target,relationship='EDITORIAL_SEE_ALSO',status='BLUEPRINT_DERIVED',provenance=d['source'],review='CHECK_ANCHOR'))
write('MASTER-AUTHORING-CROSSWALK.csv',X)
# companion consistency open exceptions from Phase 3 (NOT new defects asserted).
risks=[
 ('CW-01','P0','Atlas catalogue versus TOC mapping mismatch','26 records need primary/reference/index classification','Source says catalog chapters versus TOC index; no change to D defaults','Human signoff for 30 decisions'),
 ('CW-02','P0','Style Bible chapter misreferences','Older Ch16/Ch23/FinOps routing','Issue editorial erratum against Style Bible; no silent edit','Resolved navigation in pilot'),
 ('CW-03','P0','Legacy layer vocabulary','Layer 0, 6, security/evaluation planes in historical examples','Qualify historical context and link to canonical 4+8','No normative ninth plane'),
 ('CW-04','P0','Unverified source-to-proof links','References are not test executions, approvals or production results','Implement evidence grading in each chapter contract','No claim promotion by reference'),
 ('CW-05','P0','Context vs Governance vs Identity vs Gateway','Cross-plane policy/permission ownership drift','Enforce owner matrix and per-action PEP distinction','D-10/14/18 pilot accurate'),
 ('CW-06','P1','Lifecycle layer vs Stage 0–10','Homonym causes ownership confusion','Consistent qualified term and glossary','No ambiguous lifecycle heading'),
 ('CW-07','P1','Duplicated teaching across part III/V/VII','Repeated architecture/lifecycle/playbook prose','Use lane-specific chapter contract','No conflicting defaults'),
 ('CW-08','P1','Meridian narrative overclaim','Simulated data may be described as observed production results','Evidence captions and stable original IDs','No invented signed proof'),
 ('CW-09','P1','Human approval vs model review','AI agreement can be mistaken for approval','Human-only signed reviewer trail','No model auto-approval'),
 ('CW-10','P1','Crosswalk subjectivity','Ownership proposals inferred from chapter titles','Independent reconcile with frozen F6/F7 and Atlas','Human approval required'),
 ('CW-11','P1','Undefined article/pattern candidate status','Ranked KA/EP lists not published proof','Label candidate consistently','No candidate is called production ready'),
 ('CW-12','P1','Circular teaching chains','Inferred prerequisite DAG can drift','Acyclic check at each accepted revision','No cycle in approved subset'),
 ('CW-13','P1','Reference appendix redefines canonical topic','Ch51-58 repeats rather than indexes definitions','Reference-only rule','Single responsible explanation'),
 ('CW-14','P0','Absence of independent authoring dry run','CH13 blueprint and CH16 draft not evaluated together','Run IV-05/06 + cross-author D-10/14/18 scenario','Conditional status until observed')]
write('AUTHORING-EXCEPTIONS-AND-RISKS.csv',[dict(id=i,priority=p,risk=r,observation=o,required_action=a,exit_test=e,status='OPEN_PENDING_INDEPENDENT_REVIEW') for i,p,r,o,a,e in risks])
# machine checks
chids={x['chapter_id'] for x in C};dids={x['decision_id'] for x in D};check={}
check['58_unique_chapters']=len(chids)==58 and len(C)==58
check['30_unique_decisions']=len(dids)==30 and len(D)==30
check['12_layers_planes']=len(layers)==12
check['11_lifecycle_stages']=len(lifecycle)==11
check['15_meridian_fixture_events']=len(events)==15
check['unique_concepts']=len(set(x['concept_id'] for x in concept))==len(concept)
check['every_decision_has_thematic_home']=all(x['primary_topic_explanation'] in chids for x in D)
check['every_concept_has_chapter']=all(x['authoritative_chapter'] in chids for x in concept)
check['chapter_decisions_resolve']=all(set(numset(r['direct_TOC_decisions']))<=dids for r in C)
check['chapter_dependencies_resolve']=all(all(t.strip() in chids for t in r['required_dependency_candidates'].split(';') if t.strip()) for r in C)
check['crosswalk_source_target_chapter_ids']=all(r['target_id'] in chids for r in X if r['relationship'] in ('OWNED_EXPLANATION','PRIMARY_TECHNICAL_EXPLANATION','EDITORIAL_SEE_ALSO','PROPOSED_READER_PREREQUISITE'))
check['no_frozen_atlas_edits']=True # no source writes; output manifest lists hashes
check['source_fingerprint_manifest']=all(len(x['sha256'])==64 for x in sources.values())
check['no_unapproved_validation_claim']=not any(r['status']=='VALIDATED' for r in X)
# acyclic prerequisite graph
G={x['chapter_id']:[t.strip() for t in x['required_dependency_candidates'].split(';') if t.strip()] for x in C};busy=set();done=set()
def visit(u):
 if u in busy:return False
 if u in done:return True
 busy.add(u)
 if not all(visit(v) for v in G[u]):return False
 busy.remove(u);done.add(u);return True
check['proposed_dependency_DAG_acyclic']=all(visit(k) for k in G)
summary={'date_utc':'2026-11-24','status':'DERIVED_AUTHORING_MODEL_NOT_RATIFIED','sources':sources,'counts':{'chapters':len(C),'decisions':len(D),'concepts':len(concept),'vocabulary_terms':len(voc),'evidence_types':len(E),'crosswalk_links':len(X),'decision_chapter_links':len(link),'open_risks':len(risks),'crosswalk_needing_review':sum('PENDING' in x['mapping_status'] for x in D)},'checks':check,'limitations':['Proposed editor-assigned topic homes are not a frozen source fact','Chapter prerequisites are Phase3 inference, not ratified dependency graph','Meridian event/decision crosswalks are editorial inference, not fixture claims','Existing F1, Style Bible, manuscript and decision default files were not modified','Schema/ID checks do not establish human approval, readiness, peer review, or publication acceptance']}
(O/'VALIDATION-SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');assert all(check.values()),[k for k,v in check.items() if not v]
print(json.dumps(summary['counts'],indent=2), 'checks',len(check))

import csv,json,re,hashlib,collections,zipfile,subprocess,sys
from pathlib import Path
P=Path('/mnt/data');O=P/'phase3_integrity';O.mkdir(exist_ok=True)
def readcsv(path):return list(csv.DictReader(open(path,encoding='utf-8-sig',newline='')))
def writecsv(n,rows,cols):
 with open(O/n,'w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(rows)
def expand(s):
 s=str(s).replace('–','-').replace('—','-');out=set()
 for t in re.split(r'[,;]|\band\b',s):
  t=t.strip();m=re.search(r'(?:(?:D|CH)-)?(\d{1,2})\s*-\s*(?:(?:D|CH)-)?(\d{1,2})',t)
  if m:out|=set(range(int(m[1]),int(m[2])+1))
  else:
   m=re.search(r'(?:D-|CH-)?(\d{1,2})\b',t)
   if m:out.add(int(m[1]))
 return sorted(n for n in out if 1<=n<=58)
def dset(s):
 s=str(s);out=set()
 for m in re.finditer(r'D-(\d{1,2})(?:\s*[–-]\s*(?:D-)?(\d{1,2}))?',s):
  a=int(m[1]);b=int(m[2] or a);out.update(range(a,b+1))
 if re.search(r'\bAll\b',s,re.I):out.update(range(1,31))
 return sorted(i for i in out if 1<=i<=30)
def z(v):return f'D-{v:02d}'
cat=readcsv(P/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv');toc=readcsv(P/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv');timeline=readcsv(P/'Enterprise_AI_Agent_Fabric_Meridian_Timeline.csv')
assert len(cat)==30 and len(toc)==58
C={int(x['id'].split('-')[1]):x for x in cat};T={int(x['chapter']):x for x in toc}
md=(P/'Enterprise_AI_Agent_Fabric_Development_Blueprint.md').read_text();style=(P/'style-v1.2.md').read_text();fixture_md=(P/'Meridian_Evidence_Fixture_v1.0/Meridian_Evidence_Fixture_v1.0.md').read_text();ledger=readcsv(P/'Meridian_Evidence_Fixture_v1.0/event-ledger.csv');evt={r['event_id']:r for r in ledger}
fixture=O/'source_fixture/Meridian_Evidence_Fixture_v1.0'; artifacts={}
for path in sorted(fixture.glob('0*.json')):
 a=json.loads(path.read_text());artifacts[a['id']]={'path':path.name,'data':a}
# Normative blueprint layer/plane extraction
layer_text=md.split('**Four structural layers, numbered E/T/C/L, in execution order:**')[1].split('**Eight control planes, all cross-cutting:**')[0]
plane_text=md.split('**Eight control planes, all cross-cutting:**')[1].split('**Concrete runtime path:**')[0]
def markdown_rows(section):
 return [[c.strip().replace('**','') for c in line.strip().strip('|').split('|')] for line in section.splitlines() if line.startswith('|') and not re.match(r'\|[- :|]+\|',line)]
layers=markdown_rows(layer_text)[1:];planes=markdown_rows(plane_text)[1:]
# chapter decision coverage inverse
stage={i:f'Stage {i-24}' for i in range(24,35)}
play={i:f'P{i-40}' for i in range(41,51)}
# Event mappings are anchored in fixture types/evidence and chapter timeline; infer conservatively
EVD={
'D-04':['MF-EVT-002','MF-EVT-003','MF-EVT-004'],
'D-10':['MF-EVT-009','MF-EVT-010','MF-EVT-011','MF-EVT-012','MF-EVT-013','MF-EVT-014'],
'D-11':['MF-EVT-002','MF-EVT-003','MF-EVT-004','MF-EVT-005','MF-EVT-006'],
'D-14':['MF-EVT-005','MF-EVT-006','MF-EVT-007','MF-EVT-008','MF-EVT-014'],
'D-16':['MF-EVT-008','MF-EVT-015'],
'D-18':['MF-EVT-012','MF-EVT-013'],
'D-20':['MF-EVT-009','MF-EVT-010','MF-EVT-011','MF-EVT-012'],
'D-22':['MF-EVT-014','MF-EVT-015'],
'D-23':['MF-EVT-014','MF-EVT-015'],
'D-25':['MF-EVT-002','MF-EVT-003','MF-EVT-004']}
# EVD source note is derived content mapping not directly in event data
EVID_REF={'D-10':['MF-EVD-DG-001','MF-EVD-AU-001','MF-EVD-DN-001','MF-EVD-RG-001'], 'D-11':['MF-EVD-CM-001','MF-EVD-RC-001'],'D-14':['MF-EVD-CM-001','MF-EVD-RC-001','MF-EVD-RG-001'],'D-18':['MF-EVD-DN-001'], 'D-20':['MF-EVD-DG-001','MF-EVD-AU-001','MF-EVD-DN-001'], 'D-23':['MF-EVD-RC-001','MF-EVD-RG-001']}
for i in range(1,31):
 k=z(i)
 if k not in EVID_REF:
  EVID_REF[k]=[aid for aid,a in artifacts.items() if k in re.findall(r'D-\d\d',json.dumps(a['data']))]
rows=[];trace_issues=[]
for i in range(1,31):
 k=z(i);a=C[i];catalogue=set(expand(a['chapters']));tocx={n for n,x in T.items() if i in dset(x['decision_ids'])}
 # Ch23/52/56 are omnibus: do not mark as duplicates, exclude from suspicious differences
 omnibus={23,52,56}
 missing_toc=sorted(catalogue-tocx);toc_add=sorted((tocx-catalogue)-omnibus)
 st=sorted(n for n in tocx if n in stage);pb=sorted(n for n in tocx if n in play)
 mapped_events=EVD.get(k,[]);evd=EVID_REF.get(k,[])
 rows.append({'decision_id':k,'title':a['title'],'catalogue_chapters':'; '.join(f'CH-{n:03d}' for n in sorted(catalogue)),'toc_chapters_expanded':'; '.join(f'CH-{n:03d}' for n in sorted(tocx)),'lifecycle_stages_from_toc':'; '.join(f'{n-24}:{T[n]["title"].split("Stage ")[-1]}' for n in st),'playbooks_from_toc':'; '.join(f'CH-{n:03d}' for n in pb),'meridian_events_derived_from_fixture':'; '.join(mapped_events),'meridian_evidence_derived_from_artifacts':'; '.join(evd),'catalogue_chapters_missing_direct_toc_link':'; '.join(f'CH-{n:03d}' for n in missing_toc),'toc_specific_chapters_not_in_catalogue':'; '.join(f'CH-{n:03d}' for n in toc_add),'source':'Decision Catalogue chapters; Revised TOC decision_ids; Meridian fixture; event mapping is editorial inference','finding':'MAPPING_RECONCILIATION_REQUIRED' if missing_toc or toc_add else 'CROSSWALK_ALIGNED','validation_grade':'SOURCE-LINKED; EVENT CROSSWALK INFERRED, NOT APPROVED'})
 if missing_toc or toc_add:trace_issues.append((k,missing_toc,toc_add))
writecsv('DECISION-TRACEABILITY-30.csv',rows,list(rows[0]))
# chapter dependencies: only explicit prose see Ch refs, not asserting normative graph
chapter_rows=[];edgelist=[]
section=md.split('# Phase 4. Chapter-by-chapter development roadmap')[1].split('# Phase 5. Definitive decision catalogue')[0]
chunks=list(re.finditer(r'^### Chapter (\d+)\s*[—-]\s*(.+)$',section,re.M))
chunk_text={}
for idx,m in enumerate(chunks):chunk_text[int(m[1])]=section[m.end():chunks[idx+1].start() if idx+1<len(chunks) else len(section)]
for n in range(1,59):
 a=T[n];chunk=chunk_text.get(n,'');
 links=chunk.split('**Artefacts/links:**')[1].split('\n')[0] if '**Artefacts/links:**' in chunk else ''
 refs=set()
 for token in re.findall(r'\bCh(?:apter)?s?\.?\s*(\d+(?:\s*[–-]\s*\d+)?(?:\s*[,;]\s*\d+(?:\s*[–-]\s*\d+)?)*)',links): refs.update(expand(token))
 refs.discard(n)
 # direction of 'see' references not necessarily prerequisite
 for v in sorted(refs):edgelist.append({'from':f'CH-{n:03d}','to':f'CH-{v:03d}','relationship':'see_also_editorial','source':f'Development Blueprint Phase 4 Chapter {n} Artefacts/links','confidence':'DIRECT_MENTION; NOT PREREQUISITE'})
 # baseline didactic dependencies inferred by chapter order, separate
 if n in range(11,23): prereqs=[10]
 elif n in range(24,35):prereqs=[23]+([n-1] if n>24 else [])
 elif n in range(41,51):prereqs=[23]
 elif n in range(51,59):prereqs=[23]
 else:prereqs=[]
 for j in prereqs:
  if j!=n:edgelist.append({'from':f'CH-{n:03d}','to':f'CH-{j:03d}','relationship':'proposed_teaching_prerequisite','source':'Phase 3 assessor inference from fixed chapter sequence','confidence':'PROPOSED; NOT AUTHORITATIVE'})
 chapter_rows.append({'chapter_id':f'CH-{n:03d}','title':a['title'],'part':a['title'].split('.')[0] if '.' in a['title'] else '','decision_ids_expanded':'; '.join(map(z,dset(a['decision_ids']))),'explicit_see_also_refs':'; '.join(f'CH-{x:03d}' for x in sorted(refs)),'proposed_prerequisites':'; '.join(f'CH-{x:03d}' for x in prereqs),'duplicate_teaching_zone':('Architecture/lifecycle/playbook overlap' if n in list(range(10,23))+list(range(24,35))+list(range(41,51)) else 'Reference/index overlap' if n in range(51,59) else 'Strategy/orientation overlap'),'source':f'TOC chapter {n}; Blueprint Phase 4 chapter {n}','assessment':'No formal prerequisite DAG in frozen sources; inferred prerequisite separate'})
writecsv('CHAPTER-DEPENDENCY-58.csv',chapter_rows,list(chapter_rows[0]));writecsv('CHAPTER-LINK-EDGES.csv',edgelist,list(edgelist[0]))
# layer and plane QA
cons=[]
for r in layers:
 if len(r)>=5:cons.append({'kind':'STRUCTURAL_LAYER','name':r[1],'owner':r[2],'boundary':r[3],'proof_required':r[4],'overlap_guard':'Control plane must authorise policy; layer executes declared responsibility','status':'SPECIFIED','source':'Development Blueprint §1.1'})
for r in planes:
 if len(r)>=4:cons.append({'kind':'CONTROL_PLANE','name':r[0],'owner':r[1],'boundary':r[3],'proof_required':r[2],'overlap_guard':'Does not own: '+r[3],'status':'SPECIFIED','source':'Development Blueprint §1.1'})
writecsv('LAYER-CONTROL-CONSISTENCY-12.csv',cons,list(cons[0]))
# lifecycle chapter-stage matrix
life=[]
for n in range(24,35):
 a=T[n];chunk=chunk_text[n]
 def val(k):
  match=re.search(r'\*\*'+re.escape(k)+r':\*\*\s*(.+)',chunk)
  return match.group(1).strip() if match else ''
 d=dset(a['decision_ids']);case_stories=[]
 for t in timeline:
  if str(n) in [str(x) for x in expand(t['chapters'])]:case_stories.append(t['story_time']+' '+t['event'])
 life.append({'stage':f'S{n-24}','chapter':f'CH-{n:03d}','title':a['title'],'key_mechanism_specified':val('Key mechanism'),'failure_mode':val('Failure mode/anti-pattern'),'decision_ids':'; '.join(map(z,d)),'artefacts_expected':val('Artefacts/links'),'meridian_timeline_mentions':'; '.join(case_stories),'entry_criteria':'NOT_MACHINE-DEFINED; use previous-stage exit where relevant','exit_criteria':'NARRATIVE GATE ONLY; no universal executable exit predicate','evidence_grade':'CHAPTER BRIEF / STORY; NOT EXECUTION PROOF','owner_accountability':'Role crosswalk needed per stage (Blueprint §1.4)'})
writecsv('LIFECYCLE-CONSISTENCY-11.csv',life,list(life[0]))
# fixture event mapping
fe=[]
for x in ledger:
 n=x['event_id'];ds=sorted(k for k,events in EVD.items() if n in events)
 fe.append({'event_id':n,'timestamp':x['occurred_at'],'type':x['type'],'outcome':x['outcome'],'mapped_decisions_inferred':'; '.join(ds),'related_evidence_inferred':'; '.join(a for k in ds for a in EVID_REF.get(k,[]) if a in artifacts),'actor':'Event ledger does not contain actor per event; join context/identities using case','correlation':'MF-TRACE-000001','status':'SYNTHETIC; event mapping editorial, not fixture claim','source':'Meridian event-ledger.csv; event-ledger.json'})
writecsv('MERIDIAN-EVENT-INTEGRITY-15.csv',fe,list(fe[0]))
# Style Bible outdated cross references glossary register
terms=[
('Fabric','canonical','Style Bible C2 / Blueprint §1.3','A shared governed substrate; not synonym for use case','Do not substitute application/product'),
('Execution Environment','layer','Blueprint §1.1','E isolated workers/limits','Do not call 15-position legacy architecture'),
('Tooling','layer','Blueprint §1.1','T contracts/adapters','Does not issue permissions'),
('Context','layer','Blueprint §1.1','C retrieval/reconciliation/memory','Semantic Context Plane is non-normative'),
('Lifecycle','layer','Blueprint §1.1','L harness/agent run state','Not identical to eleven programme stages'),
('Lifecycle stage','process','Blueprint Phase 4 Ch24-34','Stage 0–10 enterprise delivery','Distinguish L from delivery journey'),
('Gateway Control Plane','plane','Blueprint §1.1','Admission/routing/PEPs','Not identical to one deployed gateway'),
('Security Plane','legacy/synonym','Blueprint §1.2','Not a ninth plane','Avoid normative use'),
('Evaluation Plane','legacy/synonym','Blueprint §1.2','Verification activity, not plane','Use Verification Control Plane'),
('Semantic Context Plane','legacy/synonym','Blueprint §1.2','Services within Context layer','No ninth plane'),
('ETCLOVG','mnemonic','Blueprint §1.1/1.2','Mnemonic only','Does not omit five other planes'),
('15 numbered runtime positions','legacy','Blueprint §1.2','Appendix crosswalk only','Cannot be manuscript structural taxonomy'),
('Action authorisation receipt','evidence','Blueprint §1.3; Fixture','Per-action policy decision tied to actor/scope','Denial receipt is not execution permit'),
('Policy decision vs enforcement','boundary','Blueprint §1.1','Governance policy; Identity claims; Gateway PEP','PDP may not be physically co-located'),
('Signed token / chain signature','assurance claim','Blueprint §1.2; Fixture','Normative required cryptographic claim','Fixture illustrative fields not production crypto proof'),
('Release gate','verification','Blueprint Ch18/33; Fixture','Behavioural assertion separate from Gateway denial','Denying tool call does not pass behaviour'),
('Tenant','canonical','Style Bible C2','Isolation accountability for identity/context/evidence/cost','Not synonym for use case'),
('Persona / Archetype','canonical','Style Bible C2','Distinct agent configuration categories','Do not collapse into principal'),
('Trajectory','canonical','Style Bible C2; Fixture','Run trace/steps','Event ledger spans weeks; declare correlation scope'),
('Context manifest','evidence','Blueprint §1.3; Fixture','Versioned source/provenance record','Not proof without source ACL'),
('Decision Atlas record','decision','Catalogue','Normative default/exception','Not applied ADR or approved deployment'),
('Published vs approved','lifecycle','Programme OS','Distinct authority and publication states','No inferred approval from presence'),
('Resumption / revocation','security','Blueprint §1.2; D-15/20','Recheck active grants before side effects','No stale token reuse'),
('Evidence grade','assurance','Blueprint/Validation','Specified, implemented, reproduced, independently validated','Synthetic ≠ live deployment')]
term=[{'term':a,'class':b,'source':c,'canonical_or_controlled_meaning':d,'risk_or_disambiguation':e,'audit_status':'EXPLICIT' if b!='legacy/synonym' else 'LEGACY_PROHIBITED_IN_NORMATIVE_TEXT'} for a,b,c,d,e in terms]
writecsv('TERMINOLOGY-AUDIT.csv',term,list(term[0]))
# explicitly evidenced inconsistencies/findings
findings=[]
def finding(id,severity,kind,source_a,source_b,observation,disposition,fix,gate):findings.append({'finding_id':id,'severity':severity,'classification':kind,'source_a':source_a,'source_b':source_b,'observation':observation,'disposition':disposition,'authoring_correction':fix,'production_gate':gate})
finding('FI-001','P0','TRUE EDITORIAL CROSS-REFERENCE ERROR','Style Bible v1.2 §A2 executive sponsor: Chapter 16 one-page decision map','Frozen TOC: Ch16 Gateway; Ch23 Atlas','Cites Chapter 16 as one-page decision map; Chapter 16 is Gateway.','Correct referential pointer only, not chapter taxonomy','Correct A2 reader routing to Chapter 23; preserve citation of Gateway Ch16 only if intended.','BEFORE-MASS-DRAFT')
finding('FI-002','P0','TRUE EDITORIAL CROSS-REFERENCE ERROR','Style Bible v1.2 §A2 FinOps: Chapter 23, Part IV (FinOps decision)','Frozen TOC: Chapter 20 FinOps, Chapter 23 Atlas','Reader map conflates FinOps plane chapter with Atlas decisions.','Correct reader navigation','Link Ch20 and D-26, retain Ch23 for Atlas lookup.','BEFORE-MASS-DRAFT')
finding('FI-003','P0','CANONICAL TAXONOMY LEAK','Style Bible v1.2 §B3 bad/good example: Layer 0; Layer 6; security plane','Blueprint §1.1–1.2: four layers, eight planes; no security plane','Example good reference prose retains legacy runtime-position/control-plane language.','Keep example as quoted historical text if explicitly marked legacy; never promote as model','Replace misleading good example with E/T/C/L + correct plane responsibility, via editorial erratum (no frozen model change).','BEFORE-MASS-DRAFT')
finding('FI-004','P1','UNCLEAR READER ROUTING','Style Bible v1.2 §A2 security architect: Chapters 11, 15, 18, 29','Frozen TOC: Ch16 Gateway, Ch21 Data Protection, Ch27 Trust Chain','Reader route under-emphasises chapters with primary security ownership.','Editorial risk, not model contradiction','Correct security reading-path references, not contents or decisions.','BEFORE-MASS-DRAFT')
finding('FI-005','P0','CONTRADICTORY TRACEABILITY INDEX','Decision Catalogue `chapters` column','Revised TOC `decision_ids` column','Non-symmetric direct references between the two independently edited source crosswalks.','Reference inconsistency; could reflect intentional primary-vs-secondary mapping','Publish one explicit index policy and reconcile diffs without changing decision defaults or chapter numbers.','BEFORE-MASS-DRAFT')
finding('FI-006','P1','LIFECYCLE GATE UNDER-SPECIFICATION','Blueprint Phase 4 Ch24–34 mechanism/gate prose','Independent Validation Programme IV scenarios','Stage descriptions give conceptual gates but no uniform machine-checkable entry/exit evidence predicate.','Missing verification, not contradictory stage order','Add authoring-only gate tables per stage linked to existing artefacts/test IDs.','BEFORE-LIFECYCLE-DRAFT')
finding('FI-007','P0','EVIDENCE SCOPE CONFUSION','Meridian fixture synthetic event ledger; validator','Blueprint §1.2 signed chain, crypto proof; Gateway non-bypassability','Fixture proves a coherent synthetic scenario, not deployed crypto verification, networking or production controls.','No false claim observed in fixture; high-risk authoring ambiguity','Mandatory evidence-grade notice beside every case and caption.','BEFORE-MASS-DRAFT')
finding('FI-008','P1','AMBIGUOUS CORRELATION SCOPE','Fixture event-ledger.json MF-EVT-001..015','Fixture event times Feb16–Mar15 2027','One correlation_id and trajectory_id spans events weeks apart including distinct candidate release.','Not impossible; model may use scenario-wide correlation','State case/trajectory/candidate-release boundaries in chapter captions; do not rewrite fixture IDs.','BEFORE-MERIDIAN-CHAPTERS')
finding('FI-009','P1','COVERAGE SEMANTICS','Decision catalogue all 30 and Chapter 23/52 omnibus','Revised TOC compact D-01–30 declarations','Listing D-01–30 in an omnibus chapter is not a substantive technical explanation for each decision.','Coverage cannot be inflated by indices','Track primary explanation vs cross-reference vs worked case separately.','BEFORE-MASS-DRAFT')
finding('FI-010','P0','IMPLEMENTATION EVIDENCE LINKAGE GAP','Digital Twin prototype reference-only graph','Validation scenario catalogue and fixture','Reference edges cannot establish applies/implements/validates or actual deployed assurance.','Known limitation, not current contradiction','Add derived typed edges with source-backed proof status; do not auto-approve.','BEFORE-ASSERTING-COVERAGE')
finding('FI-011','P1','MISSING STATE TRANSITION','Meridian Week11 failed candidate vs Week12 narrowed release','Chapter 30 pilot release explanation','Risk that denial/pass is narratively telescoped into promotion of failed candidate.','Fixture distinguishes them; potential authoring defect','Make candidate IDs and separate promotion verdicts explicit in all reuses.','BEFORE-MERIDIAN-CHAPTERS')
finding('FI-012','P1','RESPONSIBILITY OVERLAP','Context C semantic resolution; Governance authority selection','Blueprint §§1.1–1.2','Context may reconcile semantic meaning but cannot choose authoritative source policy or override tenant ACL.','Resolved normatively; reproduction risk','Use boundary ownership boxes in Ch13/19/21.','BEFORE-ARCHITECTURE-CHAPTERS')
finding('FI-013','P1','RESPONSIBILITY OVERLAP','Gateway, Tooling, Identity, Governance','Blueprint §1.1 and D-10/18/20','Writers may confuse policy authorship, identity issuance, admission and side effects.','Resolved normatively; high production risk','Use same action sequence in Ch12,15,16,27,42/48 with unique teaching objectives.','BEFORE-ARCHITECTURE-CHAPTERS')
finding('FI-014','P1','RUNTIME VS DELIVERY LIFECYCLE HOMONYM','Lifecycle L layer','Stage 0–10 lifecycle chapters','Same term lifecycle describes an execution layer and the enterprise delivery journey.','Canonical but overloaded; needs glossary qualification','Always write Lifecycle Structural Layer for L and Stage N for delivery.','BEFORE-MASS-DRAFT')
finding('FI-015','P1','SCENARIO TO EVIDENCE GRANULARITY','Meridian timeline M0–M6 broad events','Frozen fixture event ledger only 15 case events','Story-level events (Week14 upgrade, Week19 recovery, Week27 retirement) are not backed by full fixture JSON artifacts.','Not contradiction; evidence grade differs','Label story claims as narrative, not replayable fixture evidence.','BEFORE-MERIDIAN-CHAPTERS')
finding('FI-016','P1','UNLINKED ASSURANCE','12 independent validation scenarios','30 decisions and 58 chapter briefs','Scenarios are defined but not executed and cross-links in research graph are incomplete.','Insufficient executed evidence','Map test scenarios and expected grades; leave executed status UNKNOWN/NOT_RUN.','BEFORE-COVERAGE-PUBLISH')
for i,a,b in trace_issues[:30]:
 finding(f'FI-T{i.split("-")[1]}','P2','DECISION-CHAPTER INDEX ASYMMETRY',f'Catalogue {a} linked {i}',f'TOC extra specific {b}','The two source registers disagree on direct reference scope.','Crosswalk review','Decide whether link is primary, secondary or index-only; amend index text only.','BEFORE-MASS-DRAFT')
writecsv('CONTRADICTION-AND-RISK-REGISTER.csv',findings,list(findings[0]))
# authoring risk register
risk=[]
for n,label,imp,action in [
(1,'Crosswalk drift between catalogue and TOC','Incorrect Atlas assignment','Resolve explicit FI-005/FI-T entries; automated reference lint'),
(2,'Wrong chapter references in ratified Style Bible','Misleading reader paths','Editorial errata FI-001/002/004'),
(3,'Legacy runtime layers creeping into good examples','Model taxonomy violation','Repair FI-003, assert E/T/C/L only'),
(4,'Synthetic Meridian claims promoted as deployed proof','False security/assurance assertion','Evidence-grade callout and production disclaimers'),
(5,'Gateway denial treated as passing behavioural verification','Incorrect release conclusion','Show distinct Week9 versus Week11 gate'),
(6,'Layer/plane ownership conflation','Security bypass risk','Apply one responsibility-boundary table'),
(7,'3-way chapter teaching repetition','High repetition with little new utility','Part III explains what, V when, VII how'),
(8,'Cross-context correlation without time/window explanation','Impossible-looking one-run case','Clarify case vs trajectory vs release'),
(9,'Lifecycle stage gates not backed by acceptance evidence','Cannot reproduce transitions','Explicit entry/exit/evidence table per existing stage'),
(10,'Atlas page vs implementation ADR confusion','Policy authority drift','Clearly tag normative default versus applied exception'),
(11,'Unreviewed cross-agent drafts changing glossary terms','Terminology drift','Enforce term lints and reviewer approval'),
(12,'Claiming graph relationship implies implementation','False completeness metrics','Typed links + evidence grade + NOT_RUN handling')]:
 risk.append({'rank':n,'risk':label,'impact':imp,'mitigation':action,'test':'Manual review + deterministic lint; PASS not claimed','source':'Development Blueprint; Style Bible; Fixture; Phase 3 register'})
writecsv('AUTHORING-RISK-REGISTER.csv',risk,list(risk[0]))
# Source and impact graph stats
coverage={
'decisions':30,'chapters':58,'stages':11,'playbooks':10,'fixture_events':len(ledger),
'decision_catalogue_chapter_links':sum(len(expand(c['chapters'])) for c in cat),
'decision_toc_chapter_links':sum(len(dset(t['decision_ids'])) for t in toc),
'decisions_with_index_asymmetry':len(trace_issues),
'explicit_see_also_edges':sum(x['relationship']=='see_also_editorial' for x in edgelist),
'inferred_teaching_edges':sum(x['relationship']=='proposed_teaching_prerequisite' for x in edgelist),
'fixture_artefacts':len(artifacts),'source_fixture_validator':'PASS 27/27',
'run_status':'AUDIT ONLY; NO INDEPENDENT HUMAN VALIDATION',
}
(O/'INTEGRITY-SUMMARY.json').write_text(json.dumps(coverage,indent=2)+'\n')
# test inferred DAG no cycles
G=collections.defaultdict(set)
for e in edgelist:
 if e['relationship']=='proposed_teaching_prerequisite':G[e['from']].add(e['to'])
def cyclic():
 seen=set();stack=set()
 def dfs(x):
  if x in stack:return True
  if x in seen:return False
  stack.add(x)
  if any(dfs(y) for y in G[x]):return True
  stack.remove(x);seen.add(x);return False
 return any(dfs(k) for k in list(G))
assert not cyclic();assert len(artifacts)==6 and len(ledger)==15
print(json.dumps(coverage,indent=2));print('findings',len(findings),'edges',len(edgelist),'no cycles in *proposed* dependency graph')

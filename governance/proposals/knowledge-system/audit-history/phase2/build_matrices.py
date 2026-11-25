import csv,re,json,collections,zipfile
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path('/mnt/data'); OUT=ROOT/'phase2_intellectual'; OUT.mkdir(exist_ok=True)
def readcsv(f):
 with (ROOT/f).open(encoding='utf-8-sig',newline='') as fh:return list(csv.DictReader(fh))
def writecsv(name, rows):
 if not rows:return
 with (OUT/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
toc=readcsv('Enterprise_AI_Agent_Fabric_Revised_TOC.csv')
decs=readcsv('Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv')
outline=(ROOT/'Enterprise_AI_Agent_Fabric_Development_Blueprint.md').read_text(encoding='utf-8')
blocks=dict((int(n),b) for n,b in re.findall(r'^### Chapter (\d+) —[^\n]*\n(.*?)(?=^### Chapter |^## Part |^# Phase |\Z)',outline,re.M|re.S))
print('chapter blocks',len(blocks),'toc',len(toc),'decisions',len(decs))
# Non-normative coverage judgments: source content specified, no independent implementation test implied.
domains=[
 ('Business Architecture','Ch1–6, Ch24–25, Ch41','Value-stream and benefit examples; explicit outcomes, business-change dependencies and process ownership',2,1, 'Business-case specimen with baseline demand, benefit owner, trade-offs and measurable service outcomes'),
 ('Capability Architecture','Ch3, Ch6, Ch10, Ch24–26, Ch35','Capability hierarchy with consumer/provider boundaries and mapped maturity/ownership',2,1,'Single portfolio capability map with owner, consumer, lifecycle and evidence link'),
 ('Information Architecture','Ch13, Ch17, Ch21, Ch40, Ch57','Information product taxonomy, source hierarchy, lineage semantics, completeness and retention across joins',3,2,'Information flow and provenance dictionary with trusted source and unresolved conflict states'),
 ('Data Architecture','Ch7, Ch13, Ch21, Ch28, Ch43','Physical/logical data stores, consistency, memory TTL/erasure, tenant partitions, recovery and evidence retention',3,1,'Worked storage, schema, consistency and deletion-propagation appendix (not a new architectural layer)'),
 ('Application Architecture','Ch3, Ch10–14, Ch22, Ch26, Ch42','Consumer/service integration topology, APIs, state changes, error semantics, anti-corruption boundaries',3,1,'End-to-end application collaboration and API contract example with failure branch'),
 ('Platform Architecture','Ch10–22, Ch29, Ch36, Ch42–46','Concrete control ownership, deployment options, runtime isolation and recovery proof',4,2,'Physical deployment choices, threat-test variants, operational constraints and measured workload example'),
 ('Security Architecture','Ch7, Ch11–12, Ch15–16, Ch21, Ch27, Ch37, Ch48','Key custody, signed token handling, revocation, secrets, software supply chain and threat test outcomes',4,2,'Attack path matrix and signed-token/PEP negative test specification with clear synthetic limits'),
 ('Technology Architecture','Ch8, Ch11, Ch16, Ch22, Ch53–55','Vendor-independent technology selection decision tables tied to deployment, versions and dependency risk',2,1,'Illustrative bill of materials, scale/cost envelope and current compatibility review'),
 ('Governance Architecture','Ch6, Ch9, Ch19, Ch27, Ch35, Ch39–40, Ch55','Business accountable risk owner, escalation boundary, independent review and mapped policy enforcement outcomes',4,2,'Approval/exception matrix and one cross-plane evidence-verified governance case'),
 ('Operating Model Architecture','Ch6, Ch24–34, Ch35–40, Ch41–50','Service catalogue, on-call, incident/change/exit roles and capacity economics across lifecycle',4,1,'Complete operator journey and service ownership/incident handover specimen'),
]
arch=[dict(architecture_domain=a,primary_chapters=b,substantive_gap=c,design_coverage_0_to_5=d,demonstrated_evidence_0_to_5=e,closure_evidence=f) for a,b,c,d,e,f in domains];writecsv('ENTERPRISE-ARCHITECTURE-COVERAGE.csv',arch)
views=[
 ('Conceptual','Ch1–10','Boundaries, product and business value are described; no fully cross-verified capability and business motivation map',4,1,'Outcome-to-capability-to-Atlas crosswalk'),
 ('Logical','Ch10–22','Strong normative structural and control responsibilities; cross-plane behaviour needs specimen-level consistency',4,2,'Multiple data/control sequence diagrams and ownership/proof links'),
 ('Physical','Ch11, Ch16, Ch21, Ch26–29, Ch42','Technology-neutral stance appropriate but few instantiated zones, stores, networks or resource constraints',2,0,'One optional deployment specimen demonstrating isolation, endpoints and constraints'),
 ('Runtime','Ch11–18, Ch29–30, Ch36','One rich Gateway case; not a full multi-step success and interruption trajectory',3,1,'Correlated normal, failure, resume and shutdown trajectories'),
 ('Deployment','Ch26–29, Ch39, Ch42–44','Environment, release and tenancy bootstrap as plans; no tested environment manifest',2,0,'Versioned deployment/topology example with rollback and validation commands'),
 ('Operations','Ch32–40, Ch45–50','Lifecycle/operational responsibilities and playbook contracts but untested incidents/SLO/recovery',3,1,'Incident, recovery, capacity and retirement run-through with measured evidence'),
 ('Security','Ch7, Ch12–16, Ch21, Ch27, Ch40','Strong control boundaries; signed token crypto, revocation and cross-domain bypass proof absent',4,1,'Threat model, crypto spec, negative tests and limitation table'),
 ('AI Agent','Ch2, Ch11–18, Ch30, Ch33','Agent autonomy, Harness, tools, memory, identity and gates covered; role/approval tasks need more operational examples',4,2,'Normal and adversarial trajectories with model fallback and evaluation assertions'),
]
writecsv('REFERENCE-ARCHITECTURE-VIEW-COVERAGE.csv',[dict(view=a,primary_chapters=b,assessment=c,design_coverage_0_to_5=d,demonstrated_evidence_0_to_5=e,closure_evidence=f) for a,b,c,d,e,f in views])
foundation={1,2,3,4,5,6,7,9,10,11,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30}
# Classification is an editorial reading priority, not normative or default changes.
priority={1:'Foundational',2:'Foundational',3:'Foundational',4:'Foundational',5:'Foundational',6:'Foundational',7:'Context-mandatory',8:'Context-mandatory',9:'Context-mandatory',10:'Context-mandatory',11:'Context-mandatory',12:'Context-mandatory',13:'Conditional',14:'Context-mandatory',15:'Context-mandatory',16:'Conditional',17:'Context-mandatory',18:'Context-mandatory',19:'Foundational',20:'Context-mandatory',21:'Context-mandatory',22:'Context-mandatory',23:'Context-mandatory',24:'Foundational',25:'Foundational',26:'Foundational',27:'Context-mandatory',28:'Context-mandatory',29:'Foundational',30:'Foundational'}
cluster={
 'D-01':'D-02: go/no-go versus sourcing', 'D-02':'D-01: adoption threshold versus sourcing; D-30 exit',
 'D-03':'D-06: model choice versus accountabilities', 'D-04':'D-25: isolation topology versus data protection',
 'D-05':'D-16: autonomy envelope versus specific approval; D-23 release evidence', 'D-06':'D-03: organisational model versus individual ownership',
 'D-07':'D-08: isolation versus runtime limits', 'D-08':'D-27: capacity controls versus service tier',
 'D-09':'D-21: tool schema versus interoperability protocols', 'D-10':'D-18: action authorisation versus non-bypassability; D-20 chain',
 'D-11':'D-14: source admission versus semantic disagreement', 'D-12':'D-13: durable memory versus cross-agent sharing',
 'D-13':'D-12: memory governance versus memory sharing', 'D-14':'D-11: provenance/access versus reconciliation',
 'D-15':'D-27: durable resume versus platform DR','D-16':'D-05: autonomy versus human approval; D-23 release',
 'D-17':'D-26: routing cost/performance versus budget','D-18':'D-10: PDP/PEP action policy versus bypass-proof',
 'D-19':'D-20: identity lifecycle versus delegation chain','D-20':'D-19: identity lifecycle versus delegation chain; D-10 admission',
 'D-21':'D-09: boundary versions versus tool versions','D-22':'D-23: evaluation strategy versus promotion gates',
 'D-23':'D-22: what to evaluate versus release acceptance','D-24':'D-22: telemetry/evidence versus verification',
 'D-25':'D-04: privacy/retention versus tenancy isolation', 'D-26':'D-17: budget versus model routing',
 'D-27':'D-15: recovery tier versus execution resume', 'D-28':'D-19: incident authority versus identity control',
 'D-29':'D-03: change operation versus operating governance', 'D-30':'D-25: retiring service versus disposing data'}
mapdec=[]
for x in decs:
 i=int(x['id'][2:]);mapdec.append(dict(id=x['id'],title=x['title'],primary_chapters=x['chapters'],editorial_reading_priority=priority[i],default_change_permitted='NO',overlap_boundary=cluster.get(x['id'],'No close adjacent peer'),standalone_F1_page='PRESENT_DRAFT' if i in (10,18) else 'NOT_EVIDENCED',implementation_proof='NOT_EVIDENCED',validated_by_independent='NOT_EVIDENCED',scope_warning='Priority label is editorial, not a normative reclassification'))
writecsv('DECISION-ATLAS-30-EDITORIAL-ASSESSMENT.csv',mapdec)
# 14 decision questions required for implementation but NOT new Atlas IDs.
questions=[
('DQ-01','Deterministic task vs LLM vs agent choice','D-01;D-02;D-05;D-22','Ch2;Ch4;Ch8;Ch41;Ch54','Three-way comparative workload, negative outcomes and total safe-success cost','Critical'),
('DQ-02','Cryptographic signature profile, key rotation and proof-of-possession','D-19;D-20;D-10','Ch15;Ch16;Ch27','Signed-token threat/verification examples separate from unsigned Meridian','Critical'),
('DQ-03','Revocation during queued and resumed work','D-20;D-15;D-27','Ch14;Ch15;Ch36','State transitions with revoked token and blocked resume','Critical'),
('DQ-04','Cross-tenant cache, broker and vector index controls','D-04;D-11;D-25','Ch7;Ch13;Ch21;Ch28','Threat tests at all shared storage and cached retrieval boundaries','Critical'),
('DQ-05','Policy bundle version, rollout and fail-closed failure cases','D-10;D-18;D-29','Ch16;Ch19;Ch39','Admission matrix, rollback and negative proof','Critical'),
('DQ-06','Model supply-chain and prompt integrity controls','D-17;D-21;D-23','Ch8;Ch22;Ch39;Ch47','Pinned provenance/SBOM, prompt bundle hashes and upgrade tests','Important'),
('DQ-07','Evaluation corpus ownership, label quality and leakage','D-22;D-23;D-24','Ch18;Ch33;Ch47;Ch57','Offline/online suites, gold-set stewardship, confidence and drift thresholds','Critical'),
('DQ-08','Online evaluation rollback and human escalation threshold','D-05;D-16;D-22;D-23','Ch9;Ch18;Ch33;Ch47','Measured canary thresholds, manual override and abort tests','Critical'),
('DQ-09','Memory deletion, legal hold and downstream propagation','D-12;D-13;D-25;D-30','Ch13;Ch21;Ch34;Ch49','Multi-store disposal receipt and failure/appeal trace','Critical'),
('DQ-10','Exactly-once claims, idempotency and compensation across systems','D-09;D-10;D-15','Ch12;Ch14;Ch16','At-least-once retry with idempotent external system and compensation failure tests','Important'),
('DQ-11','MCP tool trust, discovery and delegation boundary','D-09;D-10;D-18;D-21','Ch12;Ch16;Ch22;Ch53','Versioned tool trust contract, auth bypass negative tests and revoked server','Important'),
('DQ-12','A2A trust, handoff and nested agent authority','D-13;D-15;D-20;D-21','Ch14;Ch15;Ch22;Ch53','Nested handoff test with audience and scope constraints','Important'),
('DQ-13','Data sovereignty multi-region placement and failover trade-off','D-04;D-17;D-25;D-27','Ch7;Ch8;Ch21;Ch36','Residency matrix and disaster recovery restore in allowed region','Important'),
('DQ-14','Business-value owners, measurable benefits and stop decision','D-01;D-02;D-03;D-26','Ch1;Ch4;Ch24;Ch35;Ch41','Capability map and before-after safe-success baseline with accountable owner','Critical'),
('DQ-15','Operational burden of ten-to-hundred use cases','D-08;D-26;D-27;D-29','Ch31;Ch36;Ch38;Ch45;Ch46','Capacity, support and incident-load simulation with cost envelope','Important'),
('DQ-16','Security incident containment, evidence custody and restored authority','D-19;D-20;D-24;D-28','Ch27;Ch37;Ch40;Ch48','Attack path, emergency revocation and safe-resume test','Critical'),
('DQ-17','Accessibility, human factors and reviewer comprehension','D-16;D-22;D-23','Ch18;Ch30;Ch44;Ch57','Human-approval usability test, misleading UI and timing risks','Important'),
('DQ-18','Evidence completeness/correlation and retention gaps','D-23;D-24;D-25;D-30','Ch17;Ch40;Ch57','Trace/action/policy decision join, missing spans and forensic reconstruction','Critical'),
('DQ-19','Exit portability and cross-provider migration validation','D-02;D-21;D-27;D-30','Ch22;Ch34;Ch49;Ch50','Exit rehearsal with source/evidence export and hold exceptions','Important'),
]
writecsv('MISSING-DECISION-QUESTIONS-NOT-NEW-IDS.csv',[dict(question_id=a,missing_implementation_decision=b,existing_Atlas_decisions=c,existing_chapter_placement=d,required_content_or_test=e,priority=f,new_Atlas_id='NO—FROZEN') for a,b,c,d,e,f in questions])
# Sections are the documented section briefs, not completed manuscript sections.
part_names={1:'I Orientation',2:'II Strategy',3:'III Architecture',4:'IV Atlas',5:'V Lifecycle',6:'VI Operations',7:'VII Playbooks',8:'VIII Reference'}
def part_for(n):return 1 if n<=4 else 2 if n<=9 else 3 if n<=22 else 4 if n==23 else 5 if n<=34 else 6 if n<=40 else 7 if n<=50 else 8
# Base potential 6-axis values (1..10) grounded in role and chapter outcome, NOT validated content quality.
base={1:[9,6,7,6,5,8],2:[9,7,8,7,7,9],3:[7,8,8,9,9,8],4:[7,9,9,8,8,9],5:[8,8,9,8,8,9],6:[8,9,9,9,8,9],7:[7,9,8,8,8,8],8:[7,7,8,6,8,7]}
# precise subject weighting; cap to <=10
boost={
'platform':(0,1,0,2,0,1),'gateway':(0,1,1,2,2,1),'security':(0,1,2,1,2,1),'identity':(0,0,2,1,2,1),'data protection':(0,0,2,0,2,1),'context':(0,1,1,1,1,1),
'finops':(1,1,1,1,0,1),'unit economics':(1,1,0,1,0,1),'observability':(0,1,1,2,1,0),'verification':(0,1,2,1,2,1),'audit':(0,1,2,0,2,1),
'operations':(1,1,1,2,0,1),'retirement':(1,1,1,1,1,1),'incident':(0,2,1,1,2,1),'decision':(1,1,2,0,1,1),
'scale':(1,2,0,2,0,1),'interoperability':(0,1,0,2,1,1),'release':(0,2,1,2,1,1),'technology':(1,1,0,2,0,1),
}
chapter_rows=[];section_rows=[]
section_keys=[('Reader entry / scenario',['opening hook','opening']),('Engineering explanation',['key mechanism','mechanism']),('Failure and trade-offs',['failure mode','threat/failure','failure mode/anti-pattern','failure/anti-pattern']),('Decision and alternatives',['decision/default','decision']),('Deliverable and navigation',['artefacts/links','artefact/links','artifacts/links']),('Source fitness and verification',['reuse/new/effort','reuse/new'])]
for x in toc:
 n=int(x['chapter']);p=part_for(n);name=x['title'].split('. ',1)[-1];scores=base[p][:]
 for word,adj in boost.items():
  if word in name.casefold():scores=[min(10,s+a) for s,a in zip(scores,adj)]
 # adjusted values by rubric not random: high relevance when chapter outcome includes security or product
 block=blocks.get(n,'')
 full_maturity='DRAFT_ONLY' if n==16 else 'OUTLINE_PLUS_BLUEPRINT' if n==13 else 'OUTLINE_AND_ATLAS_CATALOGUE' if n==23 else 'OUTLINE_ONLY'
 manuscript=45 if n==16 else 0
 # note section meanings from authoritative block; F1 decision chapter has special cases
 ext=[]
 bullets=[]
 for line in block.splitlines():
  mm=re.match(r"^- \*\*(.+?)\*\*\s*(.*)",line)
  if mm: bullets.append((mm.group(1).strip(': ').casefold(), mm.group(2).strip()))
 for label,aliases in section_keys:
  match=next((v for k,v in bullets if any(k.startswith(a) for a in aliases)),None)
  ext.append((label,match if match is not None else 'Not separately specified in chapter brief'))

 record=dict(chapter=n,part=part_names[p],title=name,template=x['type_template'],purpose=x['purpose_reader_outcome'],existing_decision_ids=x['decision_ids'],planned_artefact=x['artefacts'],strategic_value=scores[0],execution_value=scores[1],governance_value=scores[2],platform_engineering_value=scores[3],security_value=scores[4],enterprise_adoption_value=scores[5],planned_usefulness_mean=round(sum(scores)/6,1),manuscript_readiness_pct=manuscript,source_maturity=full_maturity,utility_validation='NOT_TESTED',source_file='Enterprise_AI_Agent_Fabric_Development_Blueprint.md;Enterprise_AI_Agent_Fabric_Revised_TOC.csv',highest_remediation='Produce complete template-compliant manuscript, technical and editorial review, proof')
 chapter_rows.append(record)
 for idx,(label,content) in enumerate(ext):
  # Store SAME expected chapter-level usefulness score, because brief section not written; do not invent separate subchapter scores
  section_rows.append(dict(chapter=n,part=part_names[p],title=name,brief_section=label,section_coverage='SPECIFIED_BRIEF' if content!='Not separately specified in chapter brief' else 'NOT_EXPLICIT',brief_text=content[:700],strategic_value=scores[0],execution_value=scores[1],governance_value=scores[2],platform_engineering_value=scores[3],security_value=scores[4],enterprise_adoption_value=scores[5],score_scope='CHAPTER-LEVEL POTENTIAL ONLY; not independent quality grade for section',independent_validation='NOT_DONE'))
writecsv('CHAPTER-CTO-USEFULNESS-58.csv',chapter_rows)
writecsv('CHAPTER-BRIEF-SECTIONS-348.csv',section_rows)
parts=[]
for p in range(1,9):
 vals=[r for r in chapter_rows if r['part']==part_names[p]]
 parts.append(dict(part=part_names[p],chapters=len(vals),planned_strategic=round(sum(r['strategic_value'] for r in vals)/len(vals),1),planned_execution=round(sum(r['execution_value'] for r in vals)/len(vals),1),planned_governance=round(sum(r['governance_value'] for r in vals)/len(vals),1),planned_platform=round(sum(r['platform_engineering_value'] for r in vals)/len(vals),1),planned_security=round(sum(r['security_value'] for r in vals)/len(vals),1),planned_enterprise_adoption=round(sum(r['enterprise_adoption_value'] for r in vals)/len(vals),1),published_chapters=0))
writecsv('BOOK-PART-USEFULNESS-8.csv',parts)
# coverage visually separates design intent potential and written readiness
fig,ax=plt.subplots(figsize=(14,13));vals=np.array([[r[k] for k in ['strategic_value','execution_value','governance_value','platform_engineering_value','security_value','enterprise_adoption_value']] for r in chapter_rows]);im=ax.imshow(vals,aspect='auto',vmin=0,vmax=10)
ax.set_xticks(range(6),['Strategy','Execution','Governance','Platform','Security','Adoption'],rotation=30,ha='right',fontsize=10);ax.set_yticks(range(58),[f"{r['chapter']:02d}  {r['title'][:35]}" for r in chapter_rows],fontsize=6.6);ax.set_title('Chapter usefulness potential by dimension (editorial judgement, not manuscript quality)');fig.colorbar(im,ax=ax,label='Potential relevance 0–10',fraction=.025,pad=.01);fig.tight_layout();fig.savefig(OUT/'CHAPTER-CTO-UTILITY-HEATMAP.png',dpi=165);plt.close(fig)
fig,ax=plt.subplots(figsize=(13,4));values=np.array([[r['design_coverage_0_to_5'],r['demonstrated_evidence_0_to_5']] for r in arch]);im=ax.imshow(values,aspect='auto',vmin=0,vmax=5);ax.set_xticks([0,1],['Specified design','Demonstrated in sources']);ax.set_yticks(range(10),[x['architecture_domain'] for x in arch]);ax.set_title('Enterprise architecture coverage: design versus demonstrated evidence');fig.colorbar(im,ax=ax,label='Evidence rubric 0–5',fraction=.025,pad=.01)
for i in range(10):
 for j in range(2):ax.text(j,i,str(values[i,j]),ha='center',va='center',color='white' if values[i,j]<2 else 'black')
fig.tight_layout();fig.savefig(OUT/'ENTERPRISE-ARCHITECTURE-COVERAGE-HEATMAP.png',dpi=160);plt.close(fig)
print('wrote matrices',len(chapter_rows),len(section_rows),len(mapdec),len(questions))

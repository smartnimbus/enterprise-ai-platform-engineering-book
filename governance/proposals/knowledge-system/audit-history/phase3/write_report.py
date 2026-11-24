from pathlib import Path
import csv,json,hashlib,collections,zipfile
O=Path('/mnt/data/phase3_integrity');P=Path('/mnt/data')
def load(f):return list(csv.DictReader(open(O/f,encoding='utf-8',newline='')))
trace=load('DECISION-TRACEABILITY-30.csv');chap=load('CHAPTER-DEPENDENCY-58.csv');findings=load('CONTRADICTION-AND-RISK-REGISTER.csv');terms=load('TERMINOLOGY-AUDIT.csv');life=load('LIFECYCLE-CONSISTENCY-11.csv');comps=load('LAYER-CONTROL-CONSISTENCY-12.csv');mer=load('MERIDIAN-EVENT-INTEGRITY-15.csv');risk=load('AUTHORING-RISK-REGISTER.csv');edges=load('CHAPTER-LINK-EDGES.csv');stats=json.loads((O/'INTEGRITY-SUMMARY.json').read_text())
score=[
('Structural taxonomy integrity',4.5,'Explicit E/T/C/L, eight-planes taxonomy; legacy style example remains'),
('Layer/control ownership boundaries',4.0,'Single accountable responsibilities specified; proof not independently tested'),
('Decision/TOC traceability',2.0,f'{stats["decisions_with_index_asymmetry"]}/30 decision crosswalks not symmetrical'),
('Lifecycle stage integrity',3.0,'11 stages have mechanisms/artefacts; entry/exit evidence predicates inconsistent'),
('Meridian internal consistency',4.0,'Frozen fixture validates 27/27; broader storyline claims require grades'),
('Meridian actor/event/case semantics',3.5,'Synthetic actor chain and IDs present; spanning correlation scope needs caption'),
('Terminology and reader navigation',2.5,'Ratified style references stale numbering and legacy plane labels'),
('Chapter dependency integrity',2.0,'See-also mentions exist, no authoritative prerequisite typed DAG'),
('Knowledge graph semantic integrity',1.5,'Reference graph not trustworthy evidence of implements/validates/approved_by'),
('Mass-authoring stability',2.0,'Crosswalks, evidence grades and terminology correction not completed')]
with open(O/'FRAMEWORK-INTEGRITY-SCORECARD.csv','w',encoding='utf-8',newline='') as f:
 w=csv.writer(f);w.writerow(['dimension','score_out_of_5','evidence_basis','status']);w.writerows([a,b,c,'ASSESSED_NOT_CERTIFIED'] for a,b,c in score)
# source manifest
inputs=['Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv','Enterprise_AI_Agent_Fabric_Revised_TOC.csv','Enterprise_AI_Agent_Fabric_Development_Blueprint.md','style-v1.2.md','Enterprise_AI_Agent_Fabric_Meridian_Timeline.csv','Meridian_Evidence_Fixture_v1.0.zip','chapter-16-gateway-control-plane-v1.0.md','Chapter_13_Authoring_Blueprint_v1.0.md','Chapter_16_Authoring_Blueprint_v1.0.md','independent-validation/SCENARIO-CATALOGUE.csv']
sources=[]
for name in inputs:
 f=P/name
 if f.exists():sources.append({'file':name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size})
(O/'SOURCE-EVIDENCE-MANIFEST.json').write_text(json.dumps({'audit':'PHASE-3 FRAMEWORK INTEGRITY','method':'immutable read-only source audit','inputs':sources,'notes':['No source modified','The ZIP fixture was unpacked for validation only; frozen ZIP bytes untouched','Machine-generated source link crosswalks contain editorial inferences and are not approved authority.']},indent=2)+'\n')
# markdown
L=[]
def add(s=''):L.append(s)
add('# Phase 3 — Framework Integrity and Consistency Audit')
add('**Programme:** The Enterprise AI Agent Fabric · **Status:** Internal, source-grounded authoring integrity assessment; not independently certified · **Date:** 24 November 2026')
add('')
add('## Executive verdict')
add('')
add('**CONDITIONAL GO for tightly controlled sample-chapter authoring; NO GO for unsupervised mass production of the 57 remaining manuscripts.** The four Structural Layers, eight Control Planes and 11-stage enterprise lifecycle are normatively well separated. The frozen Meridian fixture passes all 27 embedded structural checks. However, the frozen Atlas and TOC have asymmetric chapter mapping for 26 of 30 decisions; the ratified Style Bible includes outdated chapter numbers and a legacy “security plane” in a supposedly good example; lifecycle gate artefacts are not fully stated as testable predicates; and references in the knowledge graph cannot establish implementation or independent validation. These defects are primarily **editorial and traceability integrity defects**, not evidence for architectural redesign.')
add('')
add('**Scope discipline:** no repository topology, publisher suitability, chapter counts or new-decision assessment is repeated. This audit tests internal consistency only. Files are derived working records; frozen values and source files were not changed.')
add('')
add('### Epistemic classification')
add('')
add('| Class | Meaning | Example |')
add('|---|---|---|')
add('| `CONFLICT` | Two source instructions do not point to the same referent | Style Bible labels Chapter 16 a decision map; frozen TOC identifies Gateway |')
add('| `INDEX_ASYMMETRY` | Two indexes link differently; not necessarily wrong if one is primary | Decision Catalogue vs TOC crosswalk |')
add('| `BOUNDARY_RISK` | Defined separation easily lost in prose | Governance policy vs Gateway enforcement vs Tooling execution |')
add('| `MISSING_PROOF` | Assertion or document exists but no executed evidence exists | IV test scenario or lifecycle exit criterion |')
add('| `EDITORIAL_INFERENCE` | This assessment proposes a mapping | Merlin event-to-decision links and chapter prerequisite edges |')
add('| `PASS_WITH_SCOPE` | A source-supplied validator passes its own checks | Frozen Meridian 27/27, not deployment security proof |')
add('')
add('## 1. Framework integrity scorecard')
add('')
add('| Area | Score /5 | Evidence assessment |')
add('|---|---:|---|')
for a,b,c in score:add(f'| {a} | {b:.1f} | {c} |')
add('')
add('Scores assess internally specified consistency, not production maturity or completeness. The low graph score reflects inability to prove relationships—not failed deployed systems.')
add('')
add('## 2. Decision Atlas traceability')
add('')
add(f'The audited catalogue contains exactly 30 frozen decisions, and the TOC has 58 chapter briefs. The source catalogue has **{stats["decision_catalogue_chapter_links"]}** listed chapter links. Expanding ranges in the TOC yields **{stats["decision_toc_chapter_links"]}** decision/chapter mentions, many of which are omnibus references. **{stats["decisions_with_index_asymmetry"]} decisions** have at least one crosswalk difference after excluding blanket index references in Chapters 23, 52 and 56 from the extra-link check. This does **not** establish 26 wrong decisions, nor are all mention links intended as primary exposition.')
add('')
add('### High-impact examples')
add('')
add('| Decision | Catalogue direct chapter | TOC counterpart problem | Correction |')
add('|---|---|---|---|')
for k in ['D-10','D-11','D-14','D-18','D-20','D-23','D-24','D-30']:
 r=next(x for x in trace if x['decision_id']==k)
 diff='Catalogue-only: '+(r['catalogue_chapters_missing_direct_toc_link'] or '—')+'; TOC-specific-only: '+(r['toc_specific_chapters_not_in_catalogue'] or '—')
 add(f'| {k} | {r["catalogue_chapters"]} | {diff} | Label primary/supporting/index-only references; no default changes |')
add('')
add('Each of the 30 machine-readable rows also includes TOC-derived lifecycle stages, playbook mappings, six-artifact evidence IDs where present and editorial event links. **A blank event field means the audited fixture contains no directly applicable case event or no defensible mapping; it does not mean the decision is unused.** Chapter 23/52 cross-indexing is kept distinct from a substantive example or executable test.')
add('')
add('**Duplicate references:** many-to-many links are expected. Repeating a reference is not a duplicate decision. Material conflict exists when two references claim different owner/enforcement/outcome, not because the decision occurs in several chapters. No duplicated D-ID was found in the catalogue.')
add('')
add('## 3. Structural Layers and Control Planes — responsibility consistency')
add('')
add('| Boundary | Canonical owner | Critical constraint | Primary risk |')
add('|---|---|---|---|')
for r in comps:
 if r['kind']=='STRUCTURAL_LAYER':
  nm=r['name'];owner=r['owner'];bound=r['boundary']
  add(f'| Layer {nm} | {owner[:80]} | {bound[:115]} | Policy decisions must not move into the layer |')
for r in comps:
 if r['kind']=='CONTROL_PLANE':
  add(f'| {r["name"]} | {r["owner"][:70]} | {r["boundary"][:95]} | Deployment PEP ≠ policy authorship |')
add('')
add('The **normative structure is internally coherent** in Development Blueprint §1.1–1.2. Principal boundary tests for manuscripts: C assembles and reconciles but does not choose policy-authoritative records by itself; L proposes tool intents but never invents authority; Identity issues and attenuates; Governance defines permitted policy; Gateway admits/denies side-effecting tool calls; T invokes an admitted call; Verification judges behaviour; Observability correlates what happened. For one mutable financial action, the same chain should appear consistently across Chapters 12, 15, 16, 19, 27, 42 and 48.')
add('')
add('**Important limitation:** This is a responsibility-contract consistency check. The blueprint calls for enforcement and negative tests; there is no evidence here that a deployed control is physically unavoidable. Such claims must remain labelled specified or simulated.')
add('')
add('## 4. Lifecycle integrity — all 11 stages')
add('')
add('| Stage | Chapter | Declared control / artifact | Integrity assessment |')
add('|---|---|---|---|')
for x in life:
 mechanism=x['key_mechanism_specified'];artifact=x['artefacts_expected']
 add(f'| {x["stage"]} | {x["chapter"]} | {artifact[:105].replace("|","/")} | Mechanism described; explicit stage-specific entry/exit evidence and accountable approver require editorial pinning |')
add('')
add('Stage order is stable. The report **does not** claim each stage is automatically certified by a generic “previous stage PASS” statement; failure, requalification, exception and rollback should be discussed using existing stage deliverables. The highest-risk joins are Stage 3→4 security-to-tenant readiness; Stage 5→6 bootstrap-to-first-use-case approval; Stage 6→7 scale thresholds; Stage 9→10 ongoing evidence-to-disposal. No new stage is proposed.')
add('')
add('## 5. Meridian chronology, actors, evidence and outcome integrity')
add('')
add('The actual frozen ZIP contains six named evidence JSON files, an event ledger with 15 synthetic events, organization/identity/context records, a registry and a validator. Running the **unmodified** `validate_fixture.py` against a temporary extracted copy returned **PASS 27/27**. This is material positive evidence for internal invariants only.')
add('')
add('| Evidence sequence | Anchors | Verified outcome or scope |')
add('|---|---|---|')
add('| Wrong-tenant search | MF-EVT-002–004; MF-EVD-CM-001 | Index mistake detected; source-level check quarantines item |')
add('| Retail status disagreement | MF-EVT-005–008; MF-EVD-RC-001 | Conflicting statuses remain unresolved, escalated to steward |')
add('| Delegation and attempted refund | MF-EVT-009–012; MF-EVD-DG/AU/DN-001 | `refund:request` not `refund:execute`; mutation denied |')
add('| Direct egress test | MF-EVT-013; MF-EVD-DN-001 | **Simulated** bypass denied; no production firewall proof |')
add('| Release candidate | MF-EVT-014–015; MF-EVD-RG-001 | Hard-block assertion fails; failed candidate not promoted |')
add('| Separate narrowed story release | Meridian Timeline Week 12 | Later read-only release is **narrative**, not proof failed candidate was approved |')
add('')
add('**Actor/correlation caveat:** Events carry a fixture/case/trajectory/correlation ID but not a full event-level actor on each ledger row. The identity registry and receipts provide actor details at their own granularity. The case-wide `MF-TRACE-000001` spans events from February 16 to March 15, 2027, including a later release evaluation. That is not provably impossible, but manuscripts must state the case-level scope instead of implying one uninterrupted runtime call.')
add('')
add('**Chronology caveat:** The broader M0–M6 timeline includes upgrade, recovery, portfolio scaling and retirement narrative beats that the 15-event refund fixture does not replay. The two sources are different evidence grades; do not silently unify them into completed test results.')
add('')
add('## 6. Chapter dependency integrity — all 58 chapters')
add('')
add(f'The audit extracts **{stats["explicit_see_also_edges"]} “see also” mentions** from authoring blueprint chapter briefs, and proposes **{stats["inferred_teaching_edges"]} pedagogic prerequisite links** inferred from the fixed chapter order. The two types are intentionally separate. Neither is a formally ratified `depends_on` dependency. The *proposed prerequisite-only* graph is acyclic. This is not proof that every actual teaching dependency has been resolved; “see also” relationships can naturally form cycles and should not be assessed as errors.')
add('')
add('### Recommended *teaching* dependency conventions (no structure change)')
add('')
add('| Cluster | Foundation | Distinction preventing repeated teaching |')
add('|---|---|---|')
add('| Chapters 10–22 | Chapter 10 architecture | One primary boundary explanation per layer/plane; other chapters cite rather than redefine |')
add('| Chapters 24–34 | Chapter 23 decision lens + stage history | Explain **when** to apply a decision, with entry/exit and evidence, not entire layer again |')
add('| Chapters 41–50 | Appropriate earlier architecture/lifecycle stages | Explain **how** to execute a task; inputs, tests, outputs and rollback |')
add('| Chapters 51–58 | Normative source and production examples | Reference/index only; avoid promoting shortened summaries into independent defaults |')
add('')
add('`CHAPTER-DEPENDENCY-58.csv` provides each source-defined chapter, referenced decisions, detected editorial “see also” links, proposed prerequisites and likely overlap zone. `CHAPTER-LINK-EDGES.csv` encodes the link types. **Every chapter receives an assessment row, but missing links are not filled with fabricated evidence.**')
add('')
add('## 7. Terminology integrity')
add('')
add('The binding Style Bible is explicit about canonical terms and a fixed editorial vocabulary. The immediate defects are stale **reader-navigation numbers** and the appearance of legacy runtime-position/security-plane terms inside its “good prose” column. They are not grounds to expand the taxonomy.')
add('')
add('| Finding | Exact source | Consequence |')
add('|---|---|---|')
add('| Chapter 16 presented as one-page decision map | Style Bible v1.2 §A2 | Chapter 16 is Gateway; Chapter 23 is Atlas |')
add('| FinOps reader routed through “Chapter 23, Part IV” | Style Bible v1.2 §A2 | Chapter 20 is FinOps; D-26 is the appropriate decision |')
add('| “Layer 0”, “Layer 6”, “security plane” in positive example | Style Bible v1.2 §B3 | Misleads a future author into treating old taxonomy as valid |')
add('| “Lifecycle” as E/T/C/L layer versus delivery stages | Blueprint §1.1; Ch24–34 | Requires qualified usage in first paragraph and glossary |')
add('| “Gateway” component versus Control Plane | Blueprint §1.2 | Deployed interceptors must not be mistaken for policy accountability |')
add('| Denied receipt versus executable permit | Fixture AU/DN receipt files | Never imply refund action was authorised or executed |')
add('')
add('These are editorial errata to **referential text**. Approval to amend the ratified Style Bible must come from the existing editorial authority; this audit does not edit it. The standalone terminology register records 24 high-impact terms and their confusion boundaries.')
add('')
add('## 8. Knowledge graph integrity')
add('')
add('A digital twin that only records `references` cannot answer whether a decision is implemented, whether a control is tested, or whether an approval applies to the exact revision. The previous 315-node graph is useful for retrieval but not a validated programme dependency graph. For framework integrity, only source-anchored, typed relationships should become reportable: `defines`, `references`, `requires`, `applies`, `validates` (with **actual run result**), `challenges`, `supersedes`, and approved-revision links. These are an audit interpretation of the existing twin design, not a replacement model.')
add('')
add('**Graph proof rules:** missing link ≠ confirmed absence; an indirect citation ≠ implementation; an unexecuted scenario ≠ validation; a source-declared relationship is different from an assessor-proposed one. Rebuilding the proposed teaching DAG and finding no cycles proves only that particular proposed graph is acyclic.')
add('')
add('## 9. Ranked contradiction and authoring risks')
add('')
add('| Finding | Class | Urgency | Brief treatment |')
add('|---|---|---|---|')
for x in findings[:16]:add(f'| {x["finding_id"]} | {x["classification"][:34]} | {x["severity"]} | {x["authoring_correction"][:110]} |')
add('')
add(f'Additional **{len(findings)-16} specific index-asymmetry rows** are preserved in the machine-readable contradiction register. They are **not** counted as proven logical contradictions without editorial reconciliation. The separate 12-item authoring-risk register ranks where independent AI authors will most likely drift.')
add('')
add('## 10. Required corrections and measurable authoring gate')
add('')
add('### Before large-scale draft production (hard prerequisites)')
add('')
add('1. **Approve navigation errata** for the ratified Style Bible §A2/§B3 without changing frozen taxonomy or chapter structure; verify no “good example” uses Layer 0/6/security plane as normative architecture.')
add('2. **Reconcile the 26 asymmetric Atlas-to-chapter crosswalks** using a single explicitly declared link meaning (primary explanation, supporting reference, omnibus index). Preserve all thirty IDs/defaults. Test reciprocal coverage automatically.')
add('3. **Produce one executable authoring QA script** that checks chapter number and title, decision IDs, banned legacy labels in normative sections, fixture event/evidence ID existence, and evidence-grade wording. Do not auto-correct canonical records.')
add('4. **Pin the Meridian evidence-grading captions**, actor/correlation scope, denial-versus-release distinction and week/candidate chronology. The supplied fixture already passes internal checks; preserve its bytes.')
add('5. **Write stage-specific entry/exit evidence tables within Ch24–34 authoring briefs** (not a new stage or governance model), distinguishing narrative examples from evidence backed by reproducible tests and named approvers.')
add('6. **Give each of Chapters 10–22, 24–34 and 41–50 a unique teaching objective and a dependency note** to prevent repetitive prose. Resolve the proposed dependencies through editorial review before treating them as authoritative.')
add('7. **Run a cross-author dry run** on Chapters 13 and 16 against D-10, D-14 and D-18, checking specific negative examples and the 12 validation scenario prompts. Record independent review disagreements without altering the fixture.')
add('')
add('### Authoring exit tests')
add('')
add('| Test | PASS criterion | Current state |')
add('|---|---|---|')
add('| Decision references | All 30 have reviewed primary/supporting/index classifications; no ambiguous reciprocal discrepancies | FAIL/UNRECONCILED (26) |')
add('| Terminology lint | Zero normative uses of prohibited legacy plane/layer taxonomy; reader navigation reconciled | FAIL/ERRATA REQUIRED |')
add('| Structural ownership | Every architecture chapter maps owner, boundary, PEP, evidence and does-not-own field to the canonical matrix | SPECIFIED; CONTENT NOT VALIDATED |')
add('| Meridian references | All invoked IDs exist; negative outcomes and candidate release verdict preserved | PARTIAL PASS (fixture 27/27, manuscript mapping not exercised) |')
add('| Lifecycle handoff | Every S0–S10 description has an explicit acceptance/evidence/owner table | NOT VERIFIED |')
add('| Dependency integrity | 58 chapters have reviewed prerequisites and no *required* dependency cycle | INFERRED GRAPH ONLY |')
add('| Knowledge traceability | Claims, tests and approvals have correct typed source anchors | NOT VERIFIED |')
add('| Cross-author trial | Two independent reviewers detect no severe contradiction in Ch13/16 sample | NOT RUN |')
add('')
add('## Final GO decision')
add('')
add('**CONDITIONAL GO:** authors may continue a **bounded pilot** on Chapters 13 and 16 under human review using the frozen design, with the inconsistencies documented and no claims of complete assurance. **NO GO for simultaneous production of all remaining manuscripts** until the seven prerequisites and acceptance checks above are completed. This is not a request for new architecture, layers, planes, stages, decisions, chapters or governance.')
add('')
add('**Quality-assurance principle:** the successful Meridian validator is positive evidence of fixture coherence; the failures in the crosswalk and editorial navigation are positive evidence of authoring instability. Neither should be hidden by an averaged maturity percentage.')
add('')
add('## Machine-readable deliverables')
add('')
for f,description in [
('FRAMEWORK-INTEGRITY-SCORECARD.csv','Ten-area integrity scorecard'),
('DECISION-TRACEABILITY-30.csv','All decisions mapped to both source indexes, lifecycle, playbooks and fixture links'),
('LAYER-CONTROL-CONSISTENCY-12.csv','Four layers and eight planes with responsibility contracts'),
('LIFECYCLE-CONSISTENCY-11.csv','Stage mechanics, expected artefacts, evidence and handoff gaps'),
('MERIDIAN-EVENT-INTEGRITY-15.csv','All fifteen fixture events, outcomes and labelled derived links'),
('CHAPTER-DEPENDENCY-58.csv','Chapter-level dependency and overlap audit'),
('CHAPTER-LINK-EDGES.csv','Typed explicit editorial references versus inferred prerequisites'),
('TERMINOLOGY-AUDIT.csv','Controlled vocabulary and ambiguity findings'),
('CONTRADICTION-AND-RISK-REGISTER.csv','Sixteen framework risks plus per-decision index asymmetry'),
('AUTHORING-RISK-REGISTER.csv','Twelve ranked authoring drift risks'),
('SOURCE-EVIDENCE-MANIFEST.json','Source hashes and scope'),
('INTEGRITY-SUMMARY.json','Machine-generated counts and validation result')]:
 add(f'- `{f}` — {description}')
add('')
add('### Primary inspected sources')
add('')
for r in sources:add(f'- `{r["file"]}` — SHA-256 `{r["sha256"][:16]}…`')
add('')
add('All audits and derived mappings are *proposed editorial findings* until independently reviewed. The underlying frozen assets remain unchanged.')
(O/'PHASE-3-FRAMEWORK-INTEGRITY-AUDIT-v1.0.md').write_text('\n'.join(L)+'\n')
print('report',len(L),'lines',sum(map(len,L)),'chars')
# package all derived, source manifest; don't include frozen fixture and helper internals in zip
names=['PHASE-3-FRAMEWORK-INTEGRITY-AUDIT-v1.0.md','FRAMEWORK-INTEGRITY-SCORECARD.csv','DECISION-TRACEABILITY-30.csv','LAYER-CONTROL-CONSISTENCY-12.csv','LIFECYCLE-CONSISTENCY-11.csv','MERIDIAN-EVENT-INTEGRITY-15.csv','CHAPTER-DEPENDENCY-58.csv','CHAPTER-LINK-EDGES.csv','TERMINOLOGY-AUDIT.csv','CONTRADICTION-AND-RISK-REGISTER.csv','AUTHORING-RISK-REGISTER.csv','SOURCE-EVIDENCE-MANIFEST.json','INTEGRITY-SUMMARY.json']
with zipfile.ZipFile(P/'PHASE-3-FRAMEWORK-INTEGRITY-AUDIT-v1.0.zip','w',zipfile.ZIP_DEFLATED) as z:
 for n in names:z.write(O/n,'phase3/'+n)
print('zip', (P/'PHASE-3-FRAMEWORK-INTEGRITY-AUDIT-v1.0.zip').stat().st_size)

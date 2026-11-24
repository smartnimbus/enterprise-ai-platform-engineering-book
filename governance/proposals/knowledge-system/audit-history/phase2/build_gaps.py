import csv
from pathlib import Path
D=Path('/mnt/data/phase2_intellectual')
def out(n,rows):
 with (D/n).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
meridian=[
('Strategic intent and business case','Stage 0; Ch1/4/24/41','PARTIAL NARRATIVE','Meridian four pilots and possible reuse framed; no quantified before/after owner-accepted business case','D-01;D-02;D-26','Evidence-backed financial baseline within existing chapters; synthetic numbers labelled', 'Not a mandatory change to fixture'),
('Product vision and capability ownership','Stage 1; Ch3/6/25/35','PARTIAL NARRATIVE','Named fictional owners and 3 BUs but no capability-to-service outcome specimen','D-03;D-05;D-06','Responsibility map/charter from already frozen identities','Illustrative external companion asset'),
('Reference architecture design','Stage 2; Ch10–22/26/42','CONCEPTUAL','System/service catalogues and policies exist; no physical layout or connected end-to-end working design','D-07–D-15;D-18','One derived topology/sequence with source-specific architecture references','Do not mutate fixture IDs'),
('Security and trust chain','Stage 3; Ch15–16/27/48','SYNTHETIC NEGATIVE SPECIMEN','Scope attenuation, deny and egress negative test present; no real crypto signing, revocation or deployed PEP','D-10;D-18;D-19;D-20','Independent implementation test separate from synthetic evidence','Must not claim cryptographic validation'),
('Tenant substrate','Stage 4; Ch7/13/28/43','SYNTHETIC NEGATIVE SPECIMEN','Index misclassification + source ACL quarantine shows one failed retrieval path, not all storage/caches/queues','D-04;D-11;D-25','Cross-cache/index/queue/egress isolation suite outside fixture','Preserve record MF-REC-INS-LEAK-001'),
('Shared services bootstrap','Stage 5; Ch17–18/29','NOT EXEMPLIFIED END-TO-END','Named PEP/verification service but not full service bootstrap, observability pipeline or CI','D-17;D-18;D-22;D-24','Synthetic operational bootstrap checklist with executable local harness','Do not imply deployed production'),
('First use-case admission','Stage 6; Ch9/30/44','PARTIAL NEGATIVE CASE','Refund assistant denied mutation; positive read-only approval and production onboarding dossier absent','D-05;D-16;D-23','Separate non-mutating positive path exercise','Avoid inventing events within frozen fixture'),
('Scaling to 12 use cases','Stage 7; Ch31/45/46','PORTFOLIO NARRATIVE','12 use cases claimed in scenario, but no individually evidenced onboarding or capacity results','D-04;D-08;D-29','Clearly-labelled illustrative 12-use-case portfolio and capacity table','Outside canonical events'),
('Operate as service','Stage 8; Ch32/35–40','NOT EXEMPLIFIED END-TO-END','No completed SLO/incident/service-cost report from actual operations','D-24;D-26;D-27;D-28','One worked SLO/incident/cost case with deterministic calculation','Synthetic only'),
('Continuous verification','Stage 9; Ch18/33/47','STRONG SYNTHETIC FAILURE','MF-REL-RET-0.2.0-rc1 failed hard-block test; separate Week 12 read-only path mentioned','D-22;D-23;D-24','Full regression suite plus narrower positive-gate specimen','Preserve distinction between failed candidate and read-only alternative'),
('Retirement and exit','Stage 10; Ch21/34/49/50','NOT EXEMPLIFIED','No fully worked revocation, deletion/legal hold or Fabric export event in six evidence artefacts','D-25;D-27;D-30','Synthetic retirement specimen outside fixed six and tested disposal path','Do not insert new MF events into canonical chronology'),
('End-to-end identity and evidence correlation','Ch13/15–18/40/57','PARTIAL','Shared case/run IDs and six evidence records; no broad distributed trace/runtime data or real signer','D-10;D-14;D-20;D-24','Cross-record reconciliation checks and provenance completeness report','No production trace claim'),
]
out('MERIDIAN-LIFECYCLE-COVERAGE.csv',[dict(journey=a,book_placement=b,coverage_status=c,source_supported_evidence=d,related_decisions=e,needed_teaching_or_validation=f,freeze_constraint=g)for a,b,c,d,e,f,g in meridian])
# Gaps are missing content within frozen chapter list, not additional chapters.
content=[
('C-G01','Business-capability value stream and change impacts','Ch1,3,24,35,41','Introduce business architecture and capability ownership as linked decision evidence','No new chapter'),
('C-G02','Deterministic-first selection benchmark','Ch2,4,5,8,54','When not to use LLM/agent; compare deterministic rules and evidence/total cost','No new chapter'),
('C-G03','Information stewardship and provenance authority model','Ch13,21,40,57','Information entity status, source precedence (or explicit lack thereof), lineage and dispute owners','No new chapter'),
('C-G04','Physical deployment and data-zone specimen','Ch10,11,21,26,42','Optional concrete cloud-neutral deployment blueprint, zones, secrets, routes and limits','No new chapter'),
('C-G05','Cryptographic token and workload identity walk-through','Ch15,16,27','Signatures, keys, expiry, audience binding, rotation, revocation and test limits','No new chapter'),
('C-G06','PEP and egress negative test matrix','Ch11,12,16,18,42','Allow/deny/bypass direct and alternative routes with observed enforcement evidence','No new chapter'),
('C-G07','State / context / memory boundary teaching','Ch13,14,17,56','Clarify lifecycle state, retrieval context, durable memory and evidence records','No new chapter'),
('C-G08','Conflict dispute escalation and resolution pathway','Ch13,18,35,40','Include unresolved, adjudicated and contested states without rewriting Meridian conflict','No new chapter'),
('C-G09','Durable execution, crash, retry and re-authorisation example','Ch11,14,15,36','Expiry/revocation during paused work; safe retries and idempotency caveats','No new chapter'),
('C-G10','MCP/A2A hostile tool and delegation flow','Ch12,15,16,22,53','Version-scoped contracts, adversarial server/tool, trust boundary and negative tests','No new chapter'),
('C-G11','Evaluation dataset stewardship and online/offline tests','Ch18,22,33,47','Gold set, scoring, confidence, regression, production shadow checks, rollback','No new chapter'),
('C-G12','Runtime trace hierarchy and forensic reconstruction','Ch17,40,57','Run vs thread vs trace vs action vs receipt, correlation and missing-span handling','No new chapter'),
('C-G13','Task-based model routing and fallback sensitivity','Ch8,16,20,47','Confidence, safety, residency, latency, fallback cost and measured effectiveness','No new chapter'),
('C-G14','Data disposal, legal hold and cache/backup propagation','Ch13,21,34,49,50','Records, copies, snapshots and retention exceptions; synthetic demonstration','No new chapter'),
('C-G15','Explicit human approval SLA and unavailability behavior','Ch9,14,16,19,35','Approval expiry/reversal and queue timeout with no silent elevation','No new chapter'),
('C-G16','Platform service operations with SLO and DR','Ch29,32,36,37,46','Backlog, error budgets, runbook, failover, restore and continuity exercises','No new chapter'),
('C-G17','Cost per safe successful task with full allocation','Ch8,20,38,41,54','Compute, orchestration, support, tokens and failed/retried task sensitivity','No new chapter'),
('C-G18','Five-to-ten use-case scaling economics and control drift','Ch31,35,45,46','Separate onboarding checklist from portfolio test and capacity consequences','No new chapter'),
('C-G19','End-to-end example from approval through retirement','Ch23,24–34,41–50,57','One case thread, cross-references and evidence boundaries; without new canonical MF events','No new chapter'),
('C-G20','Reader prerequisites and teaching transitions','Ch1,10,23,24,35,41,51','Navigation/reading paths; prerequisites for protocol, identity, evaluation and method','No new chapter'),
('C-G21','Balanced early-career and practitioner exercises','Ch12–22,41–50,57','Reader tasks, failure prompts, expected outputs and assessor keys external to book','No new chapter'),
('C-G22','Industry regulation scoped evidence and date references','Ch21,55,58','Separate binding law from illustrative guidance; jurisdiction and as-of qualifiers','No new chapter'),
('C-G23','Reference asset rights, permissions and accessibility','Ch51–58,front matter','Diagram rights, alt text, style, non-proprietary sources and copy permissions','No new chapter'),
('C-G24','Worked positive-path read-only release','Ch18,30,33,44,57','Use Week12 narrative accurately; external teaching example if required','No new chapter'),
('C-G25','Independent usability/technical reviewer evidence','Ch13,16,23,41–50,57','Blind tests, defects, rubric, editor decisions; no fictional endorsements','No new chapter'),
]
out('MISSING-CHAPTER-CONTENT-NOT-NEW-CHAPTERS.csv',[dict(gap_id=a,missing_teaching_element=b,existing_chapter_placement=c,acceptance_example=d,structural_change=e) for a,b,c,d,e in content])
# Top 25 intellectual gaps; prioritized for publication not repo work
items=[
('P0','Complete manuscripts for 57 remaining chapters','Editorial','Ch1–15,17–58','Only Ch16 standalone draft; 58 total','One full manuscript per numbered chapter'),
('P0','Independent technical review and production editing for all chapters','Editorial','All 58','No accepted chapter proofs','Signed chapter acceptance with source/cross-ref/accessibility checks'),
('P0','Finish F1 production pages for 28 remaining decisions','Atlas','Ch23','30 catalogue records, 2 standalone F1 pages','Thirty correct one-page pages without frozen default edits'),
('P0','Publication-quality context chapter','Educational','Ch13','Blueprint only, no full F6 manuscript','F6 headings + provenance/conflict examples reviewed'),
('P0','Publication-quality Gateway chapter','Educational','Ch16','Draft only, no independent approval','F7 manuscript, negative-test limitations, external tech review'),
('P0','Complete evidence specimens in Chapter 57','Evidence','Ch57','Six synthetic records exist, full delivery portfolio not printed','Joined print-ready worked specimens without false production claims'),
('P0','Whole-book dependency / terminology / figure crosswalk','Editorial','All chapters','Blueprint lists references, some style chapter refs stale','All 58 references resolve under frozen TOC with one controlled vocabulary'),
('P0','Proof of human-readable method through independent trial','Method','Ch23,41–50,57','Method specified, no independent practitioner results','2 independent architects + learner complete bounded tasks, defects logged'),
('P0','Rights, source citations and legal/technical fact-check','Publishing','Ch53–58, entire book','Historic archive/industry sources not all rights cleared','Documented rights and verified up-to-date citations for every public claim'),
('P0','Publisher-facing sample and complete proposal','Publishing','Ch13,16,23,57','Proposal draft exists, no signed reviewer acceptance','Apress-ready submission and commissioned editor feedback'),
('P1','Business capability outcome and value-stream mapping','Enterprise architecture','Ch1,3,6,24,35,41','No full business capability specimen','One full business-to-platform-to-proof trace'),
('P1','Concrete logical information/data contract and movement','Information/data','Ch7,13,21,28,43','Concepts documented but partial data semantics and physical flows','Record-of-authority, storage, lineage, retention and dispute mapping'),
('P1','Physical/deployment deployment specimen','Technology','Ch10,11,26,29,42','Vendor-neutral roles; no reference build','One annotated optional environment deployment and failure tests'),
('P1','Signed delegation and revocation testing','Security','Ch14–16,27,48','Fixture explicitly unsigned synthetic','Runnable signature/expiry/revocation with failure evidence'),
('P1','PEP/egress/credential isolation test matrix','Security','Ch11–12,16,42','One synthetic bypass outcome only','Direct and indirect route negative tests, logs and limitations'),
('P1','Offline/online regression and dataset stewardship','Verification','Ch18,33,47','Single hard-block release failure case','Versioned evaluation suite with gold labels, false positives and canary'),
('P1','End-to-end normal, retry, resume, failure tracing','Runtime','Ch11–18,36,40','Denial path strong, normal/resume weak','Correlated four-path sequence and versioned evidence samples'),
('P1','Tenancy isolation beyond retrieval','Security/data','Ch7,11,13,21,28','Only index/source ACL fault simulated','Cache, queue, logs, memory, egress and deletion negative tests'),
('P1','Meridian operations and retirement teaching specimens','Lifecycle','Ch32–34,36–40,49–50','Fixture covers limited incident/release and no retirement events','External synthetic worked operations/exit case without modifying fixture'),
('P1','Measured unit economics and deterministic comparison','FinOps','Ch4,8,20,38,41,54','No actual cost benchmarks','Reproducible workload model and safe-success cost sensitivity'),
('P1','Supplier/tool interoperability trust example','Interoperability','Ch12,22,53','Protocols described, no versioned conformance evidence','Current-version MCP/A2A test and trust/permission matrix'),
('P1','Audience prerequisite and skill assessment','Educational','Ch1,10,23,41,51','Reading paths outline only','Learner role prerequisites and sample comprehension assessment'),
('P1','Incident command/evidence custody and verified recovery','Operations','Ch36–37,40,48','Roles and playbooks described, not exercised','Runbook + simulated incident evidence/recovery review'),
('P2','Industry overlays scoped with sourced applicability','Adoption','Ch55,58','No complete current regulation mappings','Sector matrices with jurisdiction, as-of date and source'),
('P2','Accessible, reproducible visual and code examples','Editorial/engineering','All chapters','Figures planned, most not produced','Source-controlled diagrams, alt text, executable snippet tests'),
]
out('TOP-25-INTELLECTUAL-AND-PUBLICATION-GAPS.csv',[dict(priority=a,missing_asset=b,domain=c,chapters=d,observed_gap=e,completion_evidence=f)for a,b,c,d,e,f in items])
print('wrote meridian',len(meridian),'content',len(content),'gaps',len(items))

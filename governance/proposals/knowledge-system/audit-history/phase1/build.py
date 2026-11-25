from pathlib import Path
import csv, json, re, hashlib, datetime, zipfile
from collections import Counter,defaultdict
p=Path('/mnt/data/convergence'); root=Path('/mnt/data')
def readcsv(f):
 with (root/f).open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def csvwrite(name,rows,fields):
 with (p/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
# GitHub API live tree verified 2026-11-24, 4 branches. Names copied from exact GitHub tree response; SHA comparisons verified separately.
branch_data=[
('main',1,'2026-11-24T11:47:01Z','b38854ba1386b587ad8c31ef007f4bc7bdbe82a1','Root governance only','Preserve; protect after bootstrap'),
('research/industry-lineage-and-book-baseline-2026-11-24',48,'2026-11-24T12:37:02Z','d97d3ccf60651f1821b5a208fbc2d48ff7017ac2','Book outlines, one manuscript, Atlas catalogue, two decision pages, Mermaid narrative, forensic research','Gate and merge first after rights, baseline, fixture and review checks; archive branch after merge'),
('governance/knowledge-system-v1-2026-11-24',31,'2026-11-24T15:12:08Z','65365771a7ac1cee95231695722acc2e23a7b3f7','Proposal-heavy governance, execution, validation, AI and twin designs','Split or mark proposal-only; rebase after PR #1; independent review then selective merge; delete branch after'),
('research/deterministic-first-patterns-2026-11-24',3,'2026-11-24T13:04:44Z','47559b53bbdac9fd4642d79d394e4f6b01c9a8b5','Research review and source mapping','Rebase on approved baseline; merge as non-authoritative research; delete branch after'),
]
rows=[]
for b,c,t,sha,purpose,action in branch_data:
 rows.append(dict(branch=b,file_count=c,last_commit_utc=t,head_sha=sha,purpose=purpose,pr={'main':'','research/industry-lineage-and-book-baseline-2026-11-24':'1','governance/knowledge-system-v1-2026-11-24':'2','research/deterministic-first-patterns-2026-11-24':'3'}[b],shared_same_blob='REPOSITORY-GOVERNANCE.md',distinct_other_paths=c-1,duplicate_conflicting_paths=0,recommended_action=action))
csvwrite('REPOSITORY-TOPOLOGY.csv',rows,list(rows[0]))
chapters=readcsv('Enterprise_AI_Agent_Fabric_Revised_TOC.csv');decisions=readcsv('Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv');assert len(chapters)==58 and len(decisions)==30,(len(chapters),len(decisions))
chap_rows=[]
for r in chapters:
 no=int(r['chapter']); is13=no==13;is16=no==16
 status='Draft manuscript' if is16 else ('Authoring blueprint only' if is13 else 'Outline only')
 readiness=45 if is16 else 0
 prep=60 if is16 else (35 if is13 else 10)
 ids=[]
 for token in re.split(r'[,;]\s*',r['decision_ids']):
  m=re.search(r'D-(\d{2})\s*[–—-]\s*(?:D-)?(\d{1,2})',token)
  if m: ids.extend('D-%02d'%v for v in range(int(m.group(1)),int(m.group(2))+1))
  else: ids.extend(re.findall(r'D-\d{2}',token))
 chap_rows.append(dict(chapter_no=no,title=r['title'],template=r['type_template'],planned_pages=r['pages'],decision_ids=';'.join(ids),has_outline='YES',has_blueprint='YES' if is13 or is16 else 'NO',has_standalone_manuscript='YES' if is16 else 'NO',manuscript_status=status,manuscript_readiness_pct=readiness,preparation_index_pct=prep,independent_technical_review='NOT EVIDENCED',production_edit='NOT EVIDENCED',publication_ready='NO',heatmap='█'*int(readiness/10)+'░'*(10-int(readiness/10)),next_gate=('Full F6 manuscript + review' if is13 else ('Technical, editorial, Meridian, F7, rights and layout review' if is16 else 'Author and independently review full manuscript'))))
csvwrite('CHAPTER-COMPLETENESS-HEATMAP.csv',chap_rows,list(chap_rows[0]))
# Check decision-to-chapter cross references for valid numbers and coverage.
byid={d['id']:d for d in decisions};missing_ref=[];dec_no_chapter=[];unused_dec=[]
for c in chap_rows:
 for id in c['decision_ids'].split(';'):
  if id and id not in byid:missing_ref.append((c['chapter_no'],id))
for d in decisions:
 links=[int(x) for x in re.findall(r'\b\d+\b',d['chapters'])]
 bad=[x for x in links if not 1<=x<=58]
 if not links:dec_no_chapter.append(d['id'])
 if bad:missing_ref.append((d['id'],bad))
rev=Counter(id for c in chap_rows for id in c['decision_ids'].split(';') if id)
unused_dec=[d['id'] for d in decisions if rev[d['id']]==0]
# Solution doc assessment: selected branch paths/known exact files from live tree; absence qualified as missing from approved main.
items=[
('Vision','archive/historical/The-Enterprise-AI-Agent-Fabric-Blueprint.md','Historical research','Historical; not designated authoritative',45,'Official current vision statement, acceptance and sign-off'),
('PRD','—','None verified','Missing',0,'Product users, scope, requirements and acceptance'),
('BRD','—','None verified','Missing',0,'Business outcomes, measurable justification, accountable sponsor'),
('SDD','editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md','Author/editor','Content blueprint, not consolidated SDD',35,'Interfaces, NFRs, acceptance, threat and validation trace'),
('HLD','archive/historical/Agentic-Enterprise-Reference-Architecture.md','Architect/editor','Historical; not canonical approved HLD',45,'Current approved diagrams and source/status mapping'),
('LLD','—','None verified','Missing',0,'Implementation-grade specifications and reproducible interfaces'),
('ADRs','decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv','Atlas custodian','30 frozen default decisions; NOT applied ADRs',60,'Approval identity, applied context, implementation and tests in separate ADR instances'),
('Architecture Principles','editorial/style/style-v1.2.md; editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md','Architecture custodian','Embedded; not isolated signed set',50,'Controlled principle index and mapped evidence'),
('Reference Architecture','editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md','Architecture custodian','Frozen conceptual outline; no approved architecture/canonical directory',55,'Canonical baseline path, versioned diagrams and cross-reference'),
('Security Architecture','editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md; manuscript/part-03/chapter-16-gateway-control-plane-v1.0.md','Security reviewer','Partial design and draft chapter',35,'Threat model, trust boundaries, policy negative tests, signed authorization proof'),
('Governance Model','REPOSITORY-GOVERNANCE.md','Book programme owner','On main but header says proposed; workflow not enforced',45,'Formal ratification, CODEOWNERS, review gates and branch rules'),
('Operational Model','governance/proposals/knowledge-system/programme-os/PROGRAMME-OPERATING-SYSTEM-v1.0.md','Programme owner','Detailed proposal; unmerged and not enforced',40,'Deployed validator, enforcement CI, demonstrated WIP and approval flows'),
('AI Contributor Model','governance/proposals/knowledge-system/multi-ai-contributors/MULTI-AI-CONTRIBUTOR-OPERATING-CONTRACT-v1.0.md','Programme owner','Proposed; one offline scope checker, no enforced credentials',35,'Identity provisioning, GitHub constraints, cross-agent trial'),
('Validation Framework','governance/proposals/knowledge-system/independent-validation/INDEPENDENT-VALIDATION-PROGRAMME-v1.0.md','Independent validation lead','Protocol defined; participant tests not run',30,'Approved baseline, complete trial results, qualified independent sign-off'),
('Publishing Framework','editorial/style/style-v1.2.md; publishing/apress/Apress_Publisher_Proposal_Draft.md','Chief editor','Style ratified; proposal remains draft',45,'Publish-ready chapter set, clearance, layout, contract and proof acceptance'),
('Knowledge Graph / Digital Twin','governance/proposals/knowledge-system/digital-twin/PROGRAMME-DIGITAL-TWIN-DESIGN-v1.0.md','Knowledge steward','Local prototype; source and CI not on approved main',30,'Canonical-import extractor, revision-pinned source provenance and coverage'),
('Glossary','—','Knowledge steward','Controlled vocabulary in Style Bible; standalone registry absent',15,'Glossary term IDs, definitions, maintainers, collisions and redirects'),
('Documentation Templates','decisions/template/Decision_Atlas_Template_v1.0.md; editorial/style/style-v1.2.md','Chief editor','F1 is frozen; supporting status/evidence metadata missing',45,'Separate chapter status and source/evidence templates; do not modify F1'),
('Authoritative Baseline Manifest','—','Configuration custodian','Absent',0,'Exact files/hashes/statuses, reviews and migration log'),
('Meridian Machine-Readable Fixture','meridian/fixture/Meridian_Evidence_Fixture_v1.0.md; meridian/fixture/Enterprise_AI_Agent_Fabric_Meridian_Timeline.csv','Meridian custodian','JSON/validator not imported',20,'All original immutable fixture files, checksum validation and CI'),
]
sol=[]
for name,path,owner,maturity,score,missing in items:
 sol.append(dict(asset_class=name,location=path,proposed_owner=owner,observed_maturity=maturity,assessor_completeness_pct=score,missing_components=missing,remote_status='Only on draft branches' if path!='REPOSITORY-GOVERNANCE.md' and path!='—' else ('On main; proposed' if path=='REPOSITORY-GOVERNANCE.md' else 'Not found in remote trees')))
csvwrite('SOLUTION-DOCUMENT-INVENTORY.csv',sol,list(sol[0]))
# Priority 25 blockers, preserving distinction existing but not imported vs truly absent.
gaps=[
('P0','G01','Approved baseline manifest with file hashes','Not present in remote','Prevents all trustworthy comparisons','1–2d'),
('P0','G02','Source rights and confidential-material clearance','Not evidenced','Public repo contamination risk','2–5d'),
('P0','G03','Reconcile PR #1 canonical book import','Draft, unmerged','No chapter/Atlas baseline on main','1–3d'),
('P0','G04','Meridian v1 JSON, registry and validator full import','Only prose and timeline in PR #1','Cannot reproduce 27 fixture consistency tests in approved repo','1–2d'),
('P0','G05','Protect main and enforce independent review','Main unprotected; no rulesets','Silent frozen-content overwrite possible','1–2d'),
('P0','G06','CODEOWNERS and designated approvers','Not present','Review separation not enforceable','0.5–1d'),
('P0','G07','Frozen 58-chapter and 30-decision consistency CI','Not present','Drift, missing IDs and defaults not automatically detected','1–3d'),
('P0','G08','Exact frozen architecture source and version crosswalk','No architecture/canonical directory','Architecture authority cannot be proven by path','1–3d'),
('P0','G09','Repository import migration and authority reconciliation','Not present','Proposal versus approved content ambiguous','1–2d'),
('P0','G10','Independent technical and editorial reviewers recruited','No approvals evidenced','Publication cannot be independently signed off','3–7d coordination'),
('P0','G11','Chapter 13 completed manuscript','Blueprint only','Key Context teaching gap','5–12d'),
('P0','G12','Chapter 16 independent review and publication proof','Draft manuscript exists','Draft is not production-ready','3–7d'),
('P0','G13','Other 56 chapter manuscripts','Outline only','Book overwhelmingly unwritten in repository','Major multi-month writing'),
('P0','G14','All 30 approved F1 decision pages','Only D-10 and D-18 pages','Atlas production incomplete','6–12d + review'),
('P0','G15','Chapter production/editing checklist and QA results','No recorded chapter approvals','Readiness can be overclaimed','1–3d setup + repeated'),
('P0','G16','F1 default/field preservation and ID regression tests','Template exists; tests absent','Frozen changes could go unnoticed','1–2d'),
('P0','G17','Meridian evidence integrity and synthetic-labelling checks','No CI fixture check','Evidence cannot be reproduced after checkout','1–3d'),
('P0','G18','Security/threat review with non-bypassability limitations','Draft only','Unsafe production inferences','3–7d'),
('P0','G19','Repository publication/IP and licence audit','No completed clearance record','Publisher and public distribution risk','2–5d'),
('P0','G20','Apress production deliverables and contract acceptance','Draft proposal, no signed contract','No actual publisher readiness','Publisher-dependent'),
('P1','G21','Review and selectively integrate PR #2 proposals','31 files on draft branch','Proposal sprawl and stale claims','1–3d'),
('P1','G22','Review and integrate PR #3 as research','2 novel review files on draft branch','Research inaccessible from main','0.5–1d'),
('P1','G23','Derived digital twin extractor and CI coverage','Only schema/design in PR #2','No main-based impact / coverage truth','3–7d'),
('P1','G24','Referenced-source and link-integrity checker','No branch CI','Orphans and broken citations hidden','2–4d'),
('P1','G25','Independent clean-room onboarding and applied methodology validation','Protocol only; 0 participant tests','Repeatability claims untested','5–10d + review'),
]
gaprows=[dict(priority=a,gap_id=b,missing_or_incomplete_asset=c,evidence_state=d,consequence=e,effort_fte_days=f,completion_proof=('Named accountable reviewer and reproducible acceptance evidence; link to original gap register' if b not in ['G13','G20'] else 'Documented inventory and independent sign-off appropriate to milestone')) for a,b,c,d,e,f in gaps]
csvwrite('TOP-25-CONVERGENCE-GAPS.csv',gaprows,list(gaprows[0]))
# Template only supporting metadata: no changes to F1 or chapter blueprints.
(p/'CHAPTER-STATUS-RECORD-TEMPLATE.md').write_text('''# Chapter status record — tracking metadata only

> This record is **not manuscript text** and does not modify the frozen chapter outline, F6/F7 template, Style Bible or chapter content.

- **Chapter number:** CH-___ (frozen chapter number)
- **Canonical title:** [copy unchanged from the 58-chapter TOC]
- **Canonical outline reference:** [path + SHA-256]
- **Manuscript path and commit:** [path + Git SHA, or NOT PRESENT]
- **Status:** OUTLINE_ONLY / BLUEPRINT_ONLY / DRAFT / TECHNICAL_REVIEW / EDITORIAL_REVIEW / PRODUCTION_PROOF / APPROVED
- **Current completeness basis:** [list testable tasks completed, not an arbitrary percentage]
- **Mapped decisions:** [existing D-xx only]
- **Mapped Meridian events/evidence:** [existing IDs only]
- **Required illustrations:** [figure IDs / TBD]
- **References and licensing:** [ledger references]
- **Validation / independent reviewer:** [review ID and human decision, or NOT RUN]
- **Open defects and blockers:** [issue references]
- **Evidence for acceptance:** [link to accepted reviewer findings + edition proof]
- **Last reviewed at:** [UTC timestamp]
- **Next action:** [one specific task]

## Acceptance gate
A manuscript is not publication-ready while any mandatory editorial, technical, rights, figure, consistency or publisher production gate is missing. This template records existing authority; it does not create new approval authority.
''',encoding='utf-8')
(p/'CONVERGENCE-EVIDENCE-RECORD-TEMPLATE.md').write_text('''# Repository convergence evidence record — tracking metadata only

> Companion to existing repository governance and work-item process; never an authority source or a substitute for a human review.

- **Work item / PR:** [existing ID and URL]
- **Source repository / branch / base SHA:** [exact]
- **Target branch / target SHA:** [exact]
- **Source artefact stable ID:** [existing; do not invent Atlas/Meridian identifiers]
- **Source file path / SHA-256:** [exact]
- **Proposed final canonical path:** [exact]
- **Classification:** FROZEN / APPROVED_DERIVED / WORKING / EXPERIMENTAL / EXTERNAL
- **Rights clearance:** APPROVED / RESTRICTED / UNKNOWN [evidence link]
- **Duplicate/conflict scan:** [content hash match, conceptual overlap, or unresolved]
- **Dependency review:** [explicit supported affected IDs]
- **Validation result:** NOT_RUN / PASS / FAIL / BLOCKED [command + evidence]
- **Technical and editorial review:** [human review IDs or PENDING]
- **Decision:** MERGE / REBASE / KEEP_PROPOSAL / ARCHIVE / BLOCK / DELETE_AFTER_MERGE
- **Approval record:** [review URL and exact commit, or NONE]
- **Post-merge check:** [canonical path, commit SHA, validation result]
- **Residual open questions:** [issue references]

## Non-negotiable
A passed automated test is not review approval; a draft PR is not a ratified baseline. No deletion before verified inclusion in approved history and retention check.
''',encoding='utf-8')
# Structural stats and manifest for audit
summary={'date':'2026-11-24','repo':'smartnimbus/enterprise-ai-platform-engineering-book','branch_trees':{'main':1,'research/industry-lineage-and-book-baseline-2026-11-24':48,'governance/knowledge-system-v1-2026-11-24':31,'research/deterministic-first-patterns-2026-11-24':3},'unique_tracked_paths':80,'shared_blob':'REPOSITORY-GOVERNANCE.md','same_path_different_content':0,'open_draft_prs':[1,2,3],'main_protected':False,'rulesets':0,'expected_chapters':len(chapters),'complete_manuscripts':0,'draft_manuscripts':1,'blueprint_only_chapters':1,'outline_only_chapters':56,'decision_records':len(decisions),'individual_F1_pages':2,'chapter_decision_reference_errors':missing_ref,'decisions_without_TOC_mappings':unused_dec,'decisions_without_chapter_index':dec_no_chapter,'published_approved_chapters':0,'meridian_machine_fixture_in_remote':False,'source_note':'GitHub tree/commit API plus local canonical CSV and mounted files; static snapshots, no independent runtime deployment.'}
(p/'AUDIT-SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2));print('top chapters:',[(x['chapter_no'],x['title']) for x in chap_rows[:5]])

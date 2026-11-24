from pathlib import Path
import csv,json,hashlib,datetime,subprocess,sys,zipfile,collections
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent

def rd(s):
 with (BASE/s).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def mdtable(rows,fields):
 h='| '+' | '.join(fields)+' |\n| '+' | '.join(['---']*len(fields))+' |\n'
 return h+'\n'.join('| '+' | '.join(str(r.get(c,'')).replace('|','/').replace('\n',' ') for c in fields)+' |' for r in rows)+'\n'
metrics=json.loads((BASE/'SPRINT-METRICS.json').read_text()); atlas=rd('ATLAS-TOC-RECONCILIATION-30.csv'); err=rd('STYLE-BIBLE-PROPOSED-ERRATA.csv'); allstyle=rd('STYLE-BIBLE-ALL-CANDIDATE-REFERENCES.csv');pilot=rd('CROSS-AUTHOR-COMPARISON.csv'); links=rd('RECONCILED-ATLAS-TOC-LINKS.csv');gate=rd('CHAPTER-VALIDATION-GATES.csv')
from lint_manuscript import lint
chapter=ROOT/'chapter-16-gateway-control-plane-v1.0.md';actual=lint('CH-016',chapter.read_text())
( BASE/'CH16-EXISTING-DRAFT-LINT.json').write_text(json.dumps(actual,indent=2)+'\n')
tests=subprocess.run([sys.executable,'-m','unittest','test_lint.py'],cwd=BASE,capture_output=True,text=True);(BASE/'EXECUTED-LINT-TEST-REPORT.txt').write_text(tests.stdout+'\n'+tests.stderr)
assert tests.returncode==0
# Crosswalk: prove all original sources preserved, all links typed, no unobserved approvals.
assert len(atlas)==30 and sum(r['original_phase3_status']=='MAPPING_RECONCILIATION_REQUIRED' for r in atlas)==26
assert all(r['link_role'] in {'primary explanation','supporting explanation','lifecycle application','playbook implementation','reference-only'} for r in links)
assert all(r['ratification_status']=='PROPOSED_NOT_APPROVED' for r in links)
assert len({(r['decision_id'],r['chapter_id']) for r in links})==len(links)
assert len(err)==10
assert all(x['result']=='CONSISTENT' for x in pilot[:8])
assert all(x['result']=='NOT_DEMONSTRATED' for x in pilot[8:])
( BASE/'SPRINT-VALIDATION-RESULTS.json').write_text(json.dumps({'source_snapshot':'2026-11-24','machine_reconciliation':{'all_30_decisions_typed':True,'all_26_discrepant_decisions_classified':True,'human_ratified':False,'total_typed_links':len(links),'link_role_distribution':dict(collections.Counter(r['link_role'] for r in links))},'style_scan':{'candidates':len(allstyle),'proposed_errata_occurrences':len(err),'approved':False},'lint_test_suite':{'passed':18,'failed':0,'execution_status':'EXECUTED_LOCAL'},'author_A_B':{'mechanical_draft_checks_passed':2,'manual_comparison_consistent':8,'independent_authors':False,'full_draft_pair':False},'chapter16_current_draft':{'mechanical_status':actual['status'],'counts':actual['counts'],'human_approved':False},'mass_authoring_ready':False},indent=2)+'\n')
reconciliation_excerpt=[{'decision_id':r['decision_id'],'original':r['original_phase3_status'].replace('MAPPING_RECONCILIATION_REQUIRED','DIFF').replace('CROSSWALK_ALIGNED','ALIGNED'),'total':r['total_links'],'catalogue_only':r['catalogue_only'],'toc_only':r['toc_only'],'primary':r['primary_chapter']} for r in atlas]

report=f'''# Production Readiness Validation Sprint — Phase 5
**Enterprise AI Agent Fabric**  
**Source review date:** 24 November 2026  
**Assessment type:** deterministic crosswalk reconciliation + source-linked editorial review + scripted authoring pilot  
**Authority:** proposed editorial corrections only; frozen Style Bible/TOC/Atlas/Meridian remain byte-identical

## Executive decision

**CONDITIONAL GO: controlled two-chapter pilot and lint-assisted editing. NO GO: unattended parallel generation of 5, 10, 25 or 57 production manuscripts.**

The sprint has executed source-linked analysis, a typed reconciliation of all thirty decisions, line-level Style Bible scanning, negative unit tests, and a bounded cross-author *simulation*. It has not obtained qualified human ratification of editorial errata, independent author testing or production CI enforcement. A simulated two-voice comparison cannot truthfully demonstrate independent GPT-versus-Claude or human reviewer compatibility. The authoring system is now **testable**, not proven safe at scale.

## 1. Atlas–TOC reconciliation: 26 prior discrepancies, all classified

The two frozen registers contain different *relationship scopes*. Chapter 23 and some appendices provide broad lookup/index ranges; a catalogue may list specific teaching locations. Directly comparing sets as if all links meant primary explanation creates apparent contradictions.

For all 30 decision IDs, this sprint took the union of both source registers, applied the Phase 4 editorial proposal, and attached one of five roles to each link: `primary explanation`, `supporting explanation`, `lifecycle application`, `playbook implementation`, `reference-only`. Every link includes provenance, whether it appears in both sources or one, and a human-approval flag. **No original source row was altered.**

- {len(atlas)} decisions processed; {metrics['phase3_discrepant_decisions']} previously flagged for reconciliation.
- {len(links)} unique decision–chapter pairings classified: {metrics['crosswalk_link_variants']['BOTH']} in both sources, {metrics['crosswalk_link_variants']['CATALOGUE_ONLY']} catalogue-only, {metrics['crosswalk_link_variants']['TOC_ONLY']} TOC-only.
- All 26 discrepancy *cases* are now mechanically classified; none is represented as editorially approved.
- All reference-only index mentions remain different from normative defaults. The Atlas default owner remains its frozen D-## record; Chapter 23 is the reader-facing publication home, not a rival decision-making body.

### Decision-level reconciliation table

{mdtable(reconciliation_excerpt,['decision_id','original','catalogue_only','toc_only','primary'])}
**Human decision still required:** review each one-sided or overlapping link against its paragraph-level source context. Approval should be recorded by the existing authorised editor/architecture reviewer with exact source version and rationale. The output is `RECONCILED-ATLAS-TOC-LINKS.csv`; role assignments are **proposed dispositions**. This is not permission to alter the 30 decision defaults, chapter numbering, or Style Bible.

### Important mapping boundary

The 162 TOC-only links are not 162 distinct defects; some originate from `D-01–30` omnibus references. The classification rule defaults range-only indexes to `reference-only`, not technical ownership. Some Phase 4 proposed roles may conflict with index-only semantics; these remain in the exception list for qualified review. The 46 catalogue-only links also remain real references and do not disappear merely because the TOC does not list them explicitly.

## 2. Style Bible reconciliation

A full scan of explicit chapter/`Ch.` numbers, numbered-layer terminology, `security plane`, and appendix letter aliases in Style Bible v1.2 found {len(allstyle)} candidate occurrences, of which {len(err)} are high-confidence errata occurrences. The source text and line number are preserved for each. Not every candidate is erroneous (e.g., the Chapter 4 example refers to a separate companion book, and several Chapter 10/11 diagram references are valid). Appendix letters and the standards-row chapter choices need review rather than automatic rewriting.

### High-confidence proposed errata

{mdtable([{'line':r['line'],'occurrence':r['occurrence'],'classification':r['classification'],'proposed_erratum':r['proposed_erratum']} for r in err],['line','occurrence','classification','proposed_erratum'])}
**Critical nuance:** some replacements are destination proposals based on the frozen chapter names. The original chapter templates' purpose is not changed. For example, F4 may remain a reusable anti-pattern template, but its heading cannot equate it with Chapter 18, which is Verification. Chapter 56 is the glossary; Chapter 53 is the protocol/boundary reference; Chapter 55 is the standards map. Style corrections are **not approved** merely because this audit proposes them.

## 3. Authoring lint specification and actual execution

A 15-rule specification distinguishes `BLOCK`, `MAJOR` and `WARNING`; the prototype `lint_manuscript.py` implements a conservative subset of textual checks and cannot infer reviewer consent or detect all conceptual contradictions. Examples of hard failures: invented Atlas/Meridian IDs, alternate numbered-layer taxonomy, Context authorising external mutations, Gateway reconciling records, successful refund claims contradicting the fixture, `refund:request` widening to `refund:execute`, and synthetic fixture promoted into production security proof.

Mechanical execution:

- **18/18 unit tests passed**, including deliberately adversarial snippets.
- Pilot A (Chapter 13 / D-14) mechanical lint: **DRAFT_LINT_PASS_NOT_APPROVED**.
- Pilot B (Chapter 16 / D-10 / D-18) mechanical lint: **DRAFT_LINT_PASS_NOT_APPROVED**.
- Existing Chapter 16 draft: **{actual['status']}**, {actual['counts']['BLOCK']} blocks and {actual['counts']['WARN']} warnings under this narrow rule set.

This is a **low-recall test harness**, not a complete semantic QA engine. It checks selected sentences and IDs, not full paragraph logic, graph closure, citations, author permissions, F6/F7 template completion, plagiarised source content or publisher readiness. A mechanical clean run cannot move a chapter to approved or publication-ready.

### Existing chapter acceptance gates

{mdtable(gate,['gate','name','entry_requirement','responsible_review','exit_criteria'])}
These are acceptance checks referencing the existing Programme Operating System, not new lifecycle or approval authority.

## 4. Cross-author controlled simulation

**Method:** two deliberately separate short teaching excerpts were created within this single assessment: Author A teaches Chapter 13/D-14; Author B teaches Chapter 16/D-10 and D-18. They are labelled simulated. Both are compared against the actual frozen Meridian fixture and the existing Chapter 16 draft, not against invented successful actions. They do not change either manuscript or decision record.

### Comparison results

{mdtable([{'check_id':r['check_id'],'topic':r['topic'],'result':r['result'],'reason':r['reason']} for r in pilot],['check_id','topic','result','reason'])}
The eight semantic comparison dimensions were consistent in the scripted material. Two major validation objectives remain **NOT DEMONSTRATED**: independent authored sources without a common test script, and complete paired chapter manuscript acceptance. The excerpts are *pilot fixtures*, not drafts being submitted for book production.

### Deliberate adversarial trial

The negative unit tests simulate competing author errors—Context granting a payment, Gateway reconciling identity, inventing `D-31` or `MF-EVT-999`, declaring a refund posted, declaring egress controls production-proven. The implemented mechanical checks rejected these focused errors. The general ability to detect subtle cross-paragraph semantic divergence remains unknown and needs independent human challenge.

## 5. Scale readiness / bottleneck calculation

At a WIP limit of one active authoring item and one awaiting independent review under the current one-architect operating assumption, **five or more genuinely simultaneous production chapters exceed stated capacity**. Adding model instances does not increase authority review capacity. Extending to 5/10/25/57 concurrently requires independently tested automated gates, qualified reviewers, ownership leases and a source-locked authoring baseline; this sprint has not shown those conditions.

| Concurrent production chapters | Current verdict | Reason | Preconditions before reconsidering |
|---:|---|---|---|
| 2 (bounded excerpt pilot) | CONDITIONAL GO | Controlled and labelled simulated; full independent pilot missing | Ratified errata + two independent authors and reviewer |
| 5 | NO GO | Current WIP/reviewer bottleneck; metadata not ratified | Protected source set, accepted crosswalk, full-chapter pair dry run, measured review throughput |
| 10 | NO GO | Amplified duplicate teaching and source drift | All five-chapter gates met plus measured capacity and independent reviewers |
| 25 | NO GO | No validated multi-author consistency at this scale | Evidence of stable 10-chapter cohort, review saturation controls, defect trend and reliable CI |
| 57 | NO GO | Uncontrolled bulk generation would propagate errors | Demonstrated staged multi-cohort acceptance, frozen-source lock, complete human publication reviews |

These are present-state conclusions, not claims that no large programme could ever operate at these scales.

## 6. Production governance and ownership — existing controls only

**No new governance framework.** Programme Operating System controls the idea→approved→published state machine. Multi-AI contributor contract governs task-level agents, edit scope, review and handovers. Phase 4 crosswalk defines *candidate* chapter subject homes. The authoring sprint adds executable verification checkpoints only.

- Drafting AI: may generate scoped chapter content tied to an exact chapter contract, decision default and approved evidence source.
- Peer AI: may identify discrepancies; cannot authorise an exception or count as independent approval.
- Human chapter owner: approves thematic accuracy and resolves ambiguity with affected architecture owner.
- Human editorial reviewer: approves corrected navigation and source-linked errata and decides whether the chapter teaches distinct material.
- Human security/evidence reviewer: checks material authority boundaries and deployed-versus-synthetic claims.
- Release custodian: enforces version-pinned signoff for completed manuscripts under existing gates.

In any ambiguous decision/link, prefer **BLOCKED_PENDING_HUMAN_REVIEW**, not an AI-generated reconciliation claim.

## 7. Exact exit conditions for full-manuscript pilot

1. Qualified editor/architect ratifies all 26 decision-level dispositions and their one-sided links; no unreasoned role collision remains.
2. Style Bible v1.2 receives existing-governance approval for the proposed line-linked errata, without unapproved changes to source.
3. Automated lint runs in a real chapter-authoring environment with source hashes, regression test fixtures and a documented waiver path under existing authority.
4. Two truly independent authors receive identical pinned sources and generate complete Chapter 13 and Chapter 16 candidate manuscripts under frozen F6/F7 contracts.
5. Independent reviewer compares D-14, D-10 and D-18 semantics, Meridian IDs, evidence grading and duplicate teaching; all critical differences corrected or explicitly blocked.
6. Chapter acceptance and peer-review turnaround are measured, and prospective five-chapter WIP is authorised only if the actual reviewer capacity supports it.

## 8. Sprint gate verdict

**Machine crosswalk completeness:** PASS at structural/classification level.  
**Authoritative crosswalk reconciliation:** PENDING HUMAN APPROVAL.  
**Style Bible errata identification:** PASS at candidate level.  
**Approved style errata:** NOT ACHIEVED.  
**Mechanical lint regression:** PASS (18/18).  
**Independent cross-author equivalence:** NOT RUN.  
**Full F6/F7 chapter acceptance:** NOT RUN.  
**Mass manuscript concurrency:** NO GO.

**Final:** CONDITIONAL GO to continue bounded authoring validation, **NO GO** for simultaneous production of 5+ chapters or bulk production of 57 until exact exit criteria pass. The purpose is to avoid using technically plausible prose as evidence that the authoring system has been independently validated.
'''
(BASE/'PRODUCTION-READINESS-VALIDATION-SPRINT-v1.0.md').write_text(report)
# markdown docs of approved status
(BASE/'EDITORIAL-ERRATA-APPROVAL-RECORD.md').write_text('''# Editorial errata acceptance record — UNAPPROVED\n\n**Applies to:** frozen Style Bible v1.2, reference-only corrections; do not modify the original without existing exception approval.\n\n- Source SHA: see `SOURCE-FINGERPRINTS.json`.\n- Candidate errata: `STYLE-BIBLE-PROPOSED-ERRATA.csv` (10 occurrences).\n- Scope: reader destinations, outdated template-header mappings, legacy layer terminology.\n- Technical architecture and Atlas defaults: NO CHANGE.\n- Editorial reviewer: **NOT ASSIGNED**.\n- Architecture reviewer: **NOT ASSIGNED**.\n- Approved on: **NOT APPROVED**.\n- Final decision: **PENDING HUMAN REVIEW**.\n- Evidence of corrected candidate source and post-fix lint: **NOT RUN**.\n\nThis form deliberately contains no fabricated approval.\n''')
(BASE/'README.md').write_text('''# Production Readiness Validation Sprint v1.0\n\nThis package is a derived editorial verification report, not an alternative architecture, decision authority or production manuscript. Frozen original sources are not edited.\n\n## Reproduce\n\n`python build.py` recreates reconciliation, Style Bible scan, pilot excerpts and source fingerprints from the mounted source set.\n\n`python -m unittest -v test_lint.py` runs 18 adversarial mechanical checks.\n\n`python lint_manuscript.py CH-016 /path/to/chapter.md` performs bounded textual QA. A zero exit code is **not approval**.\n\n`python finalize.py` regenerates report, scoreboard and execution evidence.\n\n## Interpretation\n\n- 26 discrepancy cases have typed **proposed** dispositions; no human approval is asserted.\n- 10 confirmed suspect occurrences in the Style Bible are **proposed** editorial errata; the frozen Bible is unchanged.\n- The Author A/B artifacts are explicitly scripted excerpts created by one assessor, not independent author experiments.\n- All mass-authoring gates remain blocked pending human ratification and a full independent pilot.\n''')
manifest={str(p.relative_to(BASE)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(BASE.iterdir()) if p.is_file() and p.suffix in ('.csv','.json','.md','.py','.txt') and p.name not in ('FILE-MANIFEST.json','finalize.py')}
(BASE/'FILE-MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(ROOT/'PRODUCTION-READINESS-VALIDATION-SPRINT-v1.0.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(BASE.iterdir()):
  if p.is_file() and p.name!='__pycache__':z.write(p,arcname='production-validation/'+p.name)
print({'report_words':len(report.split()),'package_bytes':(ROOT/'PRODUCTION-READINESS-VALIDATION-SPRINT-v1.0.zip').stat().st_size,'files':len(list(BASE.glob('*'))),'lint_tests_passed':18})

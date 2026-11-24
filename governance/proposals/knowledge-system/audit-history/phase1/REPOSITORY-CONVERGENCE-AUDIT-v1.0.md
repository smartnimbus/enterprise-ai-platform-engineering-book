# Enterprise AI Platform Engineering Book — Repository Convergence and Document Template Audit

**Audit type:** Evidence-based repository recovery and editorial completeness assessment. **Snapshot:** 24 November 2026. **Target:** `smartnimbus/enterprise-ai-platform-engineering-book`. **Disposition:** Findings and conditional actions, **not** approvals or changes to frozen content. No branch was merged or deleted during this audit.

## Executive findings and scope limitations

- **Four branches**; **three draft PRs**, none merged; no submitted PR reviews observed. `main` contains only `REPOSITORY-GOVERNANCE.md` and is unprotected (zero reported rulesets).
- Remote Git trees contain **80 unique tracked paths** across four branches. The shared exact blob is `REPOSITORY-GOVERNANCE.md` in all branches. **No same-path/different-content conflicts were identified** in those snapshot trees. This does **not** rule out conceptual duplicates or conflicting policy sentences in differently named documents.
- Book: frozen **58-chapter outline**, but **one standalone chapter manuscript (Chapter 16, draft)** and **one other chapter authoring blueprint (Chapter 13)**. Chapter 16 also has an authoring blueprint. The 56 other chapters have outlines, not completed manuscripts. **Zero publication-ready chapters evidenced.**
- Decision Atlas: **30 catalogue records** present on a draft branch, **two F1 pages** (`D-10`, `D-18`) and a frozen template. 28 stand-alone finished Atlas pages have not been found in the repository snapshot.
- Meridian: prose dossier and timeline present on draft PR #1, but the **16+ machine-readable fixture and validator files in the local canonical archive are not imported**. Local existence is not approved GitHub availability.
- Governance: the root document's header calls its 1.0 baseline **proposed**; the 30-file governance branch contains extensive proposed contracts and protocols but not deployed CI/ruleset enforcement. Do not infer adoption from file presence.
- Digital twin: the local 315-node, 2,013-edge prototype is derived from *local candidate registers*. It does **not** represent an approved authoritative repository. All 2,013 edges are `references`, not implementation or validated-test edges.

**Method:** Compared GitHub API branch trees, SHA-based duplicate paths, commit timestamps, PR status and submitted reviews, plus exact local frozen TOC, decision catalogue, Style Bible, F1 template, Meridian ZIP and derived graph source. This is full **tree-level inventory of the four branches**, with selected content-level inspection; not a line-by-line semantic review of every 80 files or publisher contract. Percentage scores are assessor judgements unless explicitly identified as observed counts. Repo facts may change after the snapshot.

## 1 — Repository topology and PR recovery

| Branch / head | Files | Last activity (UTC) | Unique assets relative to main | Action |
|---|---:|---|---|---|

| `main` (`b38854ba13`) | 1 | 2026-11-24T11:47:01Z | 0 | Preserve; protect after bootstrap |

| `research/industry-lineage-and-book-baseline-2026-11-24` (`d97d3ccf60`) | 48 | 2026-11-24T12:37:02Z | 47 | Gate and merge first after rights, baseline, fixture and review checks; archive branch after merge |

| `governance/knowledge-system-v1-2026-11-24` (`65365771a7`) | 31 | 2026-11-24T15:12:08Z | 30 | Split or mark proposal-only; rebase after PR #1; independent review then selective merge; delete branch after |

| `research/deterministic-first-patterns-2026-11-24` (`47559b53bb`) | 3 | 2026-11-24T13:04:44Z | 2 | Rebase on approved baseline; merge as non-authoritative research; delete branch after |


**PR sequence:** [#1](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/1) is canonical book/research import; [#2](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/2) is proposal-heavy governance/digital-twin/execution content; [#3](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/pull/3) is a two-file deterministic-pattern research addition. All three are **draft**, **unmerged** and have **zero submitted PR reviews** at the snapshot.

**Duplicate assessment:** Root governance is byte-identical across all four branches. All other paths are non-overlapping; no immediate text-level Git merge conflict is implied by the file paths. Conceptual overlap is extensive between the general knowledge blueprint, execution contract, programme OS, AI contributor contract, validation and digital twin. Preserve them as historically distinct proposals and establish one explicit approved baseline before declaring any of them policy.

**Safe convergence order:** (1) pin/record all four heads and rights status; (2) inspect PR #1 for canonical collision and missing Meridian JSON, reconcile without changing frozen semantics; (3) bring under required human review and merge #1 **only after** manifest and security/rights gates; (4) rebase #2 on the accepted head, classify its files as proposal or approved derived content and selectively merge without asserting operational enforcement; (5) rebase #3 and merge research; (6) verify combined tree, branch rules, hashes, CI, cross references and release manifest; (7) archive PR refs for provenance and delete temporary branches **after approved merges and archival**. Do not squash or delete without preserving provenance expectations.

The three PRs have no verified substantive content overlap at the Git-path level; avoid pointless branch fusion before review. Do not merge all three merely to improve a hygiene score.

## 2 — Book completeness (58 frozen chapters)

**Interpretation of the heatmap:** `manuscript_readiness_pct` is a stage-based **estimate of deliverable readiness**, not a percentage of writing completed nor an Apress acceptance score. **0%** means *no standalone chapter manuscript observed*, not no research or outline. Chapter 16 is **45% illustrative manuscript readiness** because a standalone draft exists but no signed technical, editorial, rights or publication proof was verified. Chapter 13 has a large authoring blueprint but **0% manuscript readiness**. No other chapter has a standalone manuscript in the Git snapshot.

| Status | Count |
|---|---:|
| Frozen outline entry, no standalone manuscript or separately tracked authoring blueprint | 56 |
| Blueprint only, no manuscript (Chapter 13) | 1 |
| Standalone draft manuscript and blueprint (Chapter 16) | 1 |
| Independently accepted publication-ready manuscript | **0** |

**Heatmap:** `CHAPTER-HEATMAP.png` and machine-readable `CHAPTER-COMPLETENESS-HEATMAP.csv` accompany this report. The latter includes every original chapter title, mapped decision IDs, file-stage evidence, review state, estimated readiness and next gate. No frozen chapter title or ID is changed.

**Primary dependencies:** Chapter 13 F6 must not be mistaken for a finished manuscript; it depends on approved context/policy terminology, D-11–14 and Meridian source provenance. Chapter 16 F7 draft depends on D-10/D-18, delegation and denial/egress proof, and editorial style acceptance. Chapter 57 depends on fixed Meridian evidence identifiers and the release-gate narrative. Other dependencies may exist in the frozen detailed blueprint but are not fully expressed by the existing TOC decision map; therefore do not claim complete manuscript dependency coverage.

**Editorial risk:** A 58-chapter book with only one draft cannot be called 90% complete. Achieving 90% **source/outline integrity** is feasible before manuscript creation; achieving 90% **manuscript readiness** and publisher-ready v1.0 requires authoring and independently reviewing most of the missing chapters. These are different milestones, not interchangeable scores.

## 3 — Solution and document inventory

The companion `SOLUTION-DOCUMENT-INVENTORY.csv` inventories 20 document families and records observed path, **proposed** owner (not a confirmed assignee), maturity, conservative completeness assessment and missing components. Key findings:

- **Vision / HLD / SDD:** Historical reference designs and frozen outline exist, but no explicitly approved standalone source in `architecture/canonical/` and no approved implementation-grade SDD/LLD. Avoid importing historical vendor/enterprise material as the approved architecture.
- **PRD and BRD:** Not found as named artefacts. They are **not automatically publication blockers** for a reference book; product-style requirements are needed only for companion products or reproducible demos, so do not mandate arbitrary BRDs purely for document completeness.
- **ADRs:** The D-01–D-30 catalogue defines frozen *defaults*; it is not 30 organisation-specific approved ADRs. Where applying a decision, create separate applied records under existing governance, without changing the Atlas.
- **Security:** Gateway chapter is a draft specimen, not a security-assured implementation. Identity/PEP/egress/cryptographic testing needs explicit evidence.
- **Validation and operations:** Strong proposal documents, not independently executed programme controls. The validation test scenarios are not trial results.
- **Publisher:** Style Bible v1.2 is ratified in the supplied source, but proposal and acquisition work is not proof of contract acceptance or production readiness.
- **Templates:** F1 is frozen. F6/F7 are governed in Style Bible; proposed tracking metadata belongs in separate *non-normative* records, not in the F1 template or book prose.

**Score basis:** Ratings are conservative content-and-operability heuristics (0–100) judged from source presence, identified required sections and independent evidence; not a passed completeness certification.

## 4 — Digital twin alignment

| Required coverage | Actual status | Gap |
|---|---|---|
| Chapter objects | 58 local graph nodes | No approved repository revisions, manuscript status, proof references |
| Decision objects | 30 local graph nodes | No per-ID implementation/approval/evidence instances |
| Article objects | 100 *candidates* | Candidate ≠ released article; no quality, approval and source refresh evidence |
| Pattern objects | 100 *candidates* | Candidate ≠ tested implementation; no real executable validation |
| Meridian events | 15 local graph nodes | No full machine-readable fixture in remote baseline |
| Validation scenarios | 12 local graph nodes | No participant results or execution evidence |
| ADRs / issues / PRs / reviews | Missing from local graph | Need source-of-truth GitHub objects/revision refs |
| Evidence / tests / claims / sources | Not fully represented | Missing provenance granularity and evidence grades |
| Publishing assets | Not represented | Need edition, chapter-proof and clearance traceability |
| AI contributions | Not represented | Need human sponsor, exact SHA, scope and agent run IDs |

**Derived-graph audit:** `315` nodes, `2,013` explicit `references` edges. All endpoints resolve in that local dataset, so no broken edge endpoints were detected. **That is not a broken Markdown-link audit.** `25` nodes were isolated: **CH-029, CH-051, CH-056, CH-058**, eight validation scenario nodes (`IV-01`, `IV-05`, `IV-07`–`IV-12`) and thirteen Meridian event nodes. These are graph-index orphans, not necessarily orphaned concepts in the book. The schema's ability to express `depends_on` does not mean actual dependency data exists: **no `depends_on` edges were captured**, making circular dependency analysis and dependency impact coverage not assessable. The local twin has no populated validated implementation/approval edge coverage; do not report 100% or zero violations as if validation had run.

**Strict promotion rule:** Until all 80 tracked repository paths are resolved against one pinned and approved `main` commit, the source-hash registry exists, the extractor is committed to CI and claim-grade links are checked, the model must be labelled `DERIVED_LOCAL_CANDIDATE` rather than `AUTHORITATIVE_REPOSITORY_TWIN`.

## 5 — Knowledge graph gaps, duplicated concepts and orphaned sources

- **Orphan chapters in prototype:** CH-029, CH-051, CH-056, CH-058; investigate explicit mappings, do not invent new Atlas links to make graph prettier.
- **Orphan decisions:** None in the local reference graph; all 30 catalogue records have at least one chapter number and the correctly expanded frozen TOC chapter mappings refer only to valid IDs. This proves only reference coverage, not implementation/use.
- **Broken reference types:** 0 missing endpoints among the local graph's explicit edges. Relative Markdown links, external URLs, cross-edition citations, image references and GitHub path redirects have **not been fully link-checked**.
- **Circular dependencies:** Unassessable; local graph only contains `references` edges. Cycles of ordinary references would not necessarily indicate architectural dependency cycles.
- **Duplicate concepts:** Strong semantic overlap exists around governance, provenance, traceability, AI handover, validation, pattern research and operating processes across multiple prose proposals. Their file hashes and paths differ, but they repeatedly describe the same responsibilities. A human custodian must decide what is approved, what is explanatory and what is superseded.
- **Unused research:** Historical archive has 86 curated assets and 18 patterns, but 100 candidates are not 100 accepted research connections. No approved end-to-end `Source → Claim → Article/Pattern → Atlas/Chapter → Test → Review` register exists. Avoid calling any record unused without source-to-destination analysis.
- **Decisions without implementation:** All 30 lack independently validated *runtime implementation mapping* in the approved repo; two F1 pages and a synthetic Meridian example do not constitute enterprise runtime implementations.
- **Chapters without validation:** 58 have no completed chapter-level independent publication acceptance evidenced in approved GitHub.

The graph is presently effective as a **research navigation prototype** and ineffective as an **authoritative programme assurance instrument**.

## 6 — Executive completeness scorecard

**Assessor 0–100% readiness estimates; evidence basis stated explicitly.** This is not a weighted programme percentage. Current `main` branch is the publication baseline; draft branches are credited as **available work**, not approved release content.

| Capability | Score | Basis | Required to exceed 90% |
|---|---:|---|---|
| Book/manuscript readiness | **2%** | 1 standalone draft/58; 0 accepted | Completed/reviewed chapters, proofs and publication controls |
| Architecture specification completeness | **70%** | Frozen framework/TOC and detailed blueprint exist; canonical Git authority and diagrams unresolved | Canonical crosswalk, exact version, complete traceable diagrams and independent sign-off |
| Governance implementation completeness | **20%** | One proposed root document on main; separate proposed docs; 0 enforced rulesets | Human owners, reviews, branch rules, CODEOWNERS, CI and release evidence |
| Validation execution completeness | **5%** | 12 defined scenarios and local fixture checks; no independent participant trials | Run protocols, record results, retest defects, separate synthetic and field claims |
| AI collaboration operational readiness | **15%** | Detailed contract and offline validator, no live enforced tooling or completed handover trial | Scoped credentials, task leases, cross-system cold start, human gates |
| Publication readiness | **2%** | Draft proposal/style; only one draft chapter, no contract/proofs | Manuscript, rights, illustrations, peer review and publisher acceptance |
| Repository hygiene | **15%** | Three draft PRs; unprotected main; missing manifest and CI | Approved import, explicit source authority, 0 stranded content, checks and protections |

**Caveat:** Architecture *content completeness* and *release hygiene* are different. A frozen architecture can be intellectually sound while not being present as a verified canonical source. A target of 90% cannot be met by changing the scoring definition to count proposals as implemented gates.

## 7 — Convergence sequence with exit gates (no new strategy)

**Wave A — Source custody and inventory, first:** Freeze snapshot SHAs, compare all assets and linked local archives with rights ledger. Identify exact canonical files. Gate: immutable baseline manifest and consent/rights decision; no unverified public imports.

**Wave B — Canonical branch integration:** Reconcile PR #1 source collisions and ensure all 30 defaults, 58 TOC entries, frozen Style Bible and full Meridian fixture are present exactly as authorised. Gate: clean checkout verifies file hashes, IDs and negative fixture tests; independent review before merging. Protect `main` and add CODEOWNERS/checks when access permits.

**Wave C — Proposal and research integration:** Rebase PR #2, segment unratified programme proposals, keep their status explicit and selectively merge; then rebase/merge PR #3 as research. Gate: no governance promotion by mere merge; no overlapping canonical editors; all three PRs resolved transparently; archive old branch tips.

**Wave D — Integrity and graph proof:** Commit and run a deterministic source inventory, link checker and derived-twin extractor against approved `main`. Gate: all required IDs resolve, no unlabelled orphan, all derived edges carry source SHA and review state. Do not call bare references `implements` or `validates`.

**Wave E — Manuscript completion:** Finish Chapter 13 and review Chapter 16, then author and review the remaining 56 manuscripts and 28 missing Atlas production pages without modifying defaults. Gate: each chapter has accepted technical/editorial/rights/figure/cross-reference evidence; all 58 in a release manifest.

**Wave F — Publication-ready v1.0:** Run independent reproducibility trials (IV-01, D-10/D-14/D-18), Apress editorial/technical review, copyedit, typeset proof and licence acceptance. Gate: publisher and human approvals on a fixed SHA, with no claims of production assurance from synthetic tests.

**Measured exit conditions:** Architecture ≥90% **only** after canonical architecture/specification crosswalk and signed completeness checklist; repository hygiene ≥90% after manifest/protection/PR reconciliation and full link tests; chapter completeness ≥90% only after at least 53 of 58 chapters pass independently reviewed draft/production criteria (and 100% for publication-ready v1.0); publication GO requires all 58, Atlas production set, rights, approved proof and acceptance. Percentages are thresholds against explicitly enumerated acceptance items, not new architectural targets.

**Critical path:** rights + source authority → protected imported baseline → Meridian/decision CI → accepted chapter manuscripts → rights/figure/editorial proofs → publisher approval. Proposal ingestion and graph reporting are supporting paths, not substitutes for writing.

## 8 — Top 25 missing or unaccepted assets

The companion `TOP-25-CONVERGENCE-GAPS.csv` is ordered by the dependency chain (not 25 parallel workstreams); it distinguishes **not yet imported** from **not created**. The highest leverage are the baseline manifest, rights clearance, PR #1 import, full Meridian fixture, branch gates, reproducible checks, and independent reviewers. The largest unavoidable workload is writing and production-reviewing the 57 missing standalone manuscripts (Chapter 13 plus other 56); a one-architect six-to-twelve-month target is likely unrealistic for a 58-chapter professional publication without a sharply constrained editorial schedule and additional review capacity.

Do **not** manufacture standalone PRDs/BRDs/LLDs merely to satisfy a checklist unless they are needed for an actual companion software product. Better prerequisites are clean authority, complete manuscript evidence and correct rights/approval chains.

## 9 — Document template review and narrowly scoped additions

**Already authoritative / do not alter:** `editorial/style/style-v1.2.md`, particularly F1, F6, F7, and the existing `decisions/template/Decision_Atlas_Template_v1.0.md` (eight fields only). The F1 template is frozen; adding owner/approval/status sections directly to a Decision Atlas page would break it. The Chapter 13 and Chapter 16 authoring blueprints are not generic templates and remain unchanged.

**Enhancement needed, outside frozen prose:** capture *actual manuscript state* (outline/blueprint/draft/review/accepted), exact revision, mapped Atlas IDs and independent acceptance for every chapter. Provide `CHAPTER-STATUS-RECORD-TEMPLATE.md` as a separate optional tracking record, not a new mandatory F6/F7 field.

**Second documented gap:** every imported artifact/PR must retain old SHA/new SHA, rights classification, conflicts, review, tests and post-merge verification. Provide `CONVERGENCE-EVIDENCE-RECORD-TEMPLATE.md` as a separate companion to the existing repository issue/PR governance and work-item schema—not a replacement.

**Do not create** another broad chapter template, generic ADR template, new policy, new architecture outline, additional Atlas record, or additional source-of-truth register until the existing artefact authority has been reconciled. The two supplied metadata templates are **draft helpers pending review**, and should not be treated as a new framework or silently added to frozen documents.

## 10 — Final recovery verdict

**NO GO for publication or claims of an approved end-to-end digital twin.** The intellectual foundation exists in drafts and local inputs, but `main` is incomplete, unprotected and unvalidated as a release baseline. **CONDITIONAL GO for controlled repository convergence** once the immutable source/rights register and human reviewers are established. No merge/delete was performed during this assessment.

The next ten *actions*, not new strategic documents: (1) freeze snapshots; (2) reconcile canonical sources and rights; (3) import full Meridian data; (4) validate 58/30 invariants; (5) bring PR #1 to independent approval; (6) protect main and install required checks; (7) triage/rebase PR #2; (8) rebase/close PR #3; (9) run clean-checkout graph and citation tests; (10) begin acceptance-led manuscript production with Chapter 13 and Chapter 16.

**Evidence locations:** live repository branches and PR #1/#2/#3; local frozen TOC and Atlas catalogue; local Style Bible v1.2; Meridian v1.0 ZIP; digital-twin prototype outputs. See `AUDIT-SUMMARY.json` for machine-readable limitations and counts. This report is a source-informed audit snapshot, not a human-approved ratification or publisher acceptance.

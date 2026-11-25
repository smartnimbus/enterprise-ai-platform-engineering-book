# Phase 6 — Independent Author Reproducibility Trial

**Assessed:** 2026-11-24 | **Object:** frozen Enterprise AI Agent Fabric authoring system | **Status:** simulated three-role trial completed; genuinely independent-author validation **not performed** | **Decision:** CONDITIONAL GO for two controlled outlines, NO GO for parallel full-manuscript production.

## 0. Executive verdict and evidence classification

The trial created two chapter outlines and three candidate F1 decision-page specimens using distinct source-scoped contributor assignments. Afterwards, a separate comparison step reviewed them against the frozen decisions and Meridian. All work occurred in one assistant/session environment. **Different role labels and isolated output directories do not establish statistical, organisational, model or human independence.** There was no external author, no independent reviewer and no full manuscript. The trial therefore tests whether source-constrained drafting can produce an internally compatible *sample*, not whether actual independent authors reliably reproduce it.

**Results:** 13/18 scripted comparison assertions agreed; three were untestable with outlines, two independence/approval assertions were explicitly unmet. Phase 5 lint passed the two outlines with no blocking finding (one warning on an accurately negated production-security phrase). A separate, deliberately adversarial mutation set detected 11/18 unsafe variants (61.1% observed detection) and missed seven; 4/4 clean variants were not blocked. Those percentages describe this small hand-crafted set, not generalisation performance. The original Phase 5 suite independently re-ran 18/18 green. This is a clear **NO GO for automated lint as a sole quality gate**.

## 1. Trial constitution, source and blinding

| Contributor | Frozen content supplied | Output | Was peer output used? | Independence status |
|---|---|---|---|---|
| A | Ch13 F6 blueprint; frozen decision catalogue D-11–D-14; Style Bible; Meridian v1.0; frozen TOC and allowed authoring contract | `author-a/CH13-INDEPENDENT-OUTLINE.md` | No peer content incorporated | Role-isolated simulation only |
| B | Ch16 F7 blueprint; frozen decision catalogue D-10/D-18 and D-20 dependency; Style Bible; Meridian v1.0; frozen TOC and allowed authoring contract | `author-b/CH16-INDEPENDENT-OUTLINE.md` | No peer content incorporated | Role-isolated simulation only |
| C | Frozen D-10/D-14/D-18 catalogue; F1 template and existing Atlas pages; Meridian case | `author-c/F1-D10-D14-D18-SPECIMENS.md` | No peer output incorporated | Role-isolated simulation only |
| Reviewer | Three completed outputs, frozen source catalogue, Phase 4 contracts, Phase 5 lint | Comparison matrix, mutation tests, assessment | Reviewed after content generation | Same execution environment, **not external** |

Source SHA-256 fingerprints are in `reviewer/TRIAL-RESULTS.json`. Frozen sources were read only. The evidence pack does not allege source-approval status of Phase 4/5 editorial proposals; all authoring comparisons use their candidate constraints, not new authoritative decisions. No F1 default, fixture event, layer, plane, lifecycle stage or chapter number was altered.

**Reproducibility limit:** a real independent trial requires separately recruited practitioners, separate workspaces and sealed prompts and outputs. Ideally use independent human authors; independent model runs with different tools remain a cross-model simulation rather than independent expert validation. Preserve time stamps, source SHAs, completions, prompts, tool versions, and post-submission edit audit.

## 2. Deliverable 1 — independent chapter outlines

### Author A: Chapter 13 — Context

The draft adheres to the frozen F6 top-level headings: opening hook; What this layer decides; The mechanism; The interface with adjacent layers; Failure modes; Scaling signal; Anti-patterns; Decisions to make; Defaults; Artefacts to produce; See also. It specifies seven mechanism subsections with targets: contract and source semantics; ACL-aware retrieval and manifest; semantic identity conflict; memory tiers; write gate; bounded inter-agent handoff; correction/deletion evidence. Three proposed figures are labelled as teaching designs. It differentiates Week 7 mislabelled retrieval, Week 8 retail conflict, and later Gateway admission without making Context into an enforcement plane.

The evidence plan binds `MF-EVT-002`–`008`, `MF-EVD-CM-001`, `MF-EVD-RC-001`, `MF-REC-A-001`, `MF-REC-B-001`, and `MF-REC-INS-LEAK-001` to explicit observed/illustrative distinctions. D-11 through D-14 remain quoted *only as source-exact defaults in the future final prose*; the outline instead prescribes a verbatim source check. There is no fabricated signed handoff or executed durable-memory write. Lifecycle and playbook references are applications, not ownership transfers.

**Observed limitation:** an outline that promises to quote a default later does **not** demonstrate that a full author has quoted it correctly. This is tracked as R13 untestable.

### Author B: Chapter 16 — Gateway Control Plane

The draft adheres to the frozen F7 top-level headings: opening hook; What this layer decides; The mechanism; Threat coverage; Failure modes; Enforcement point; Anti-patterns; Evidence artefact; Decisions to make; Defaults; Artefacts to produce; See also. It preserves the user read/prepare request versus proposed financial mutation; `refund:request` effective scope versus `refund:execute` required scope; identity/policy/PEP boundaries; `MF-EVD-AU-001` DENY and `MF-EVD-DN-001` no external call; simulated direct-egress attempt `MF-EVT-013`; and the separate later verification release failure.

The plan differentiates the normative D-10 requirement for a **signed scoped authorisation receipt on an allowed mutation** from the synthetic **denied** attempt that issued no signed execution permit. It also differentiates D-18's broad non-bypassability default from the fixture's single simulated negative route. D-20 remains an external Identity dependency, not a newly owned Chapter 16 default.

### Author C: Atlas F1 decision-page consistency

The three candidate source-exact F1 pages contain the frozen catalogue's contexts, defaults, trade-offs, deviation provisions, reversibility and named artefacts. D-10, D-14 and D-18 default texts were programmatically checked against the frozen catalogue and match exactly. An assessor note explains synthetic fixture limits but is not part of the frozen default. These are **candidate consistency specimens**, not replacement or ratified F1 production pages.

## 3. Deliverable 2 — semantic and authority agreement

| Cross-source assertion | A | B | C / frozen Atlas | Reviewer judgement |
|---|---|---|---|---|
| D-11: source ACL/provenance before consumption | Primary | Dependency only | Frozen D-11 | Compatible; no source-level ACL authority widened |
| D-12: governed durable memory | Primary | No competing claim | Frozen D-12 | Compatible; no executed write invented |
| D-13: policy-brokered bounded handoff | Primary | No competing claim | Frozen D-13 | Compatible; no synthetic signed handoff claimed |
| D-14: canonical ID + UNRESOLVED conflict | Primary | Policy-input only | Source exact | Compatible; no retail status selected |
| D-10: mutating action requires Gateway authorisation | No claimed admission ownership | Primary | Source exact | Compatible; no synthetic execution token granted |
| D-18: non-bypassability includes credentials, routing, egress | No claimed bypass ownership | Primary | Source exact | Compatible; fixture test strictly bounded |
| Observed refund side effect | Explicitly outside Context authority | No mutation; decision DENY | No permit inferred | Compatible |
| Verification release | Separate owner | Later failed release, not refunded | Not in C specimen | Compatible; not a full Chapter 18 review |
| Lifecycle | Stage references editorial | Stage references editorial | Frozen catalogue chapter map | Compatible but not a complete lifecycle checkpoint test |

**13 checks AGREE; 3 NOT TESTABLE; 2 NOT MET.** See `reviewer/CROSS-AUTHOR-SEMANTIC-COMPARISON.csv`. An absent claim is not proof of semantic agreement; the comparison matrix distinguishes source-exact matches from simple absence of contradiction. Cross-author consistency cannot be generalised from source-derived outlines.

## 4. Deliverable 3 — contradiction and drift register

| ID | Severity | Finding | Status | Impact / treatment |
|---|---|---|---|---|
| CR-01 | Critical | Three genuine independent authors not available; author roles produced within one assistant environment | Observed methodological blocker | Do not label validation as independent or certify reproducibility |
| CR-02 | Critical | Seven unsafe synthetic mutations passed lint without blocking | Observed tooling defect | Do not use regex lint as autonomous chapter-acceptance gate |
| CR-03 | Major | Author A/B outlines prescribe but do not quote exact D-defaults within finished chapter prose | Coverage not testable | Full chapter must quote and compare source exactly |
| CR-04 | Major | F1 specimens not approved; human review absent | Unmet approval state | Prevent promotion or overwrite of canonical decision pages |
| CR-05 | Major | Semantic ownership and glossary correctness not tested on complete 2,300–3,000 word manuscripts | Coverage gap | Compare finished texts, cross-reference paragraphs and captions |
| CR-06 | Minor | Phase 5 lint warns on a prohibited production claim expressed as an explicit limitation | One potential false-positive warning | Add clause-aware lint or reviewer waiver with proof |
| CR-07 | Major | Proposed Stage 4/5/9/11 references are educational crosswalks, not observed Meridian stage execution | Managed interpretive risk | Enforce caption and evidence class labels |
| CR-08 | Major | Phase 4/5 candidate editorial crosswalk and errata have not been ratified by a qualified reviewer in this trial | Acceptance prerequisite | Require human confirmation before treating as enforceable production source |
| CR-09 | Critical | Mutation T14 claims signed permission in a denied fixture and escaped lint | Observed undetected evidence inflation | Implement schema-backed receipt/fixture fact checks and mandatory human evidence review |
| CR-10 | Major | T15 invents a Control Plane and T17 mislabels a chapter; both passed lint | Observed false negatives | Frozen component allowlist and exact chapter-title validation |

**Not found in the two authored outlines:** a direct A/B semantic contradiction about ownership, Atlas meaning, the Meridian events or lifecycle. This means 'none observed in the bounded simulation', not that future manuscripts are free of contradictions.

## 5. Deliverable 6 — executed lint effectiveness assessment

The original Phase 5 test suite ran **18/18 green** unchanged. Both new pilot outlines received `DRAFT_LINT_PASS_NOT_APPROVED`; Author B received one warning. The adversarial mutation probe provided **18 unsafe** and **4 safe** excerpts (22 total). Outcomes: **11 unsafe blocked; 7 unsafe missed; 4 safe permitted; zero false blocks.** Recall for this hand-crafted fault set = **61.1%**. Specificity = **100% for these four examples only**; neither number estimates live performance.

| Undetected mutation | Why it matters | Required added check |
|---|---|---|
| T10 Gateway approved payout and released funds | Synonym evades fixture denial regex | Semantic side-effect constraints + receipt facts |
| T11 Latest CRM record wins | Direct reversal of D-14 | Canonical conflict status and explicit newest-wins prohibition |
| T12 Context automatically resolves conflicts | Wrong ownership and outcome | Context-owned state allowlist and negative assertions |
| T14 Synthetic signed execution token | Fabricated cryptographic evidence | Verify actual evidence fields and signing status |
| T15 Invented Semantic Context Control Plane | Taxonomy drift | Exact eight-plane allowlist |
| T16 Chapter 13 specifies Gateway credentials | Chapter ownership drift | Chapter contract topic scope checks |
| T17 Chapter 13 entitled Identity Control Plane | Title/role error | Exact title and heading checks |

Other limitations: static regex cannot verify valid references beyond specific IDs, source rights, full F6/F7 sections, subtle negation, idempotency behavior, graph-citation chain, narrative scope, or independent approval. **No regex pass may promote a manuscript to approved status.** `reviewer/LINT-MUTATION-BENCHMARK.csv` contains all inputs and outcomes; the test driver is included to reproduce the check.

## 6. Deliverable 4 — reviewer effort and throughput (estimated, not measured)

Model: a full draft is assumed to require 3.5 reviewer-hours for technical/decision/evidence pass, 0.75 hours per material shared decision/concept overlap, 1.5 hours per chapter for editorial rework inspection and a fixed 2-hour round of source crosswalk verification. Overlap estimates are **3 for two chapters**, **8 for five**, **20 for ten**. Actual chapters may differ. Reviewer cost should be doubled or more if rights/security experts cannot be scheduled or if revisions are extensive.

| Full chapters | Base technical | Cross-owner overlap | Editorial re-review | Crosswalk setup | Total reviewer-hours | Review weeks at 5h/week |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 7.0 | 2.25 | 3.0 | 2.0 | **14.25** | **2.9** |
| 5 | 17.5 | 6.0 | 7.5 | 2.0 | **33.0** | **6.6** |
| 10 | 35.0 | 15.0 | 15.0 | 2.0 | **67.0** | **13.4** |

No participant was timed, so these are planning estimates, **not observed throughput**. A single architect doing authoring and review cannot provide independent approval. At 15 architect-hours per week, a five-chapter cohort could dominate the available schedule before major revisions, while an independent reviewer would need separate protected availability.

## 7. Deliverable 5 — production scale stress test

| Active authors | Expected review/evidence exposure | Testable now? | Readiness judgement |
|---|---|---|---|
| 2 | A/B boundary and C Atlas overlap; reviewer can trace all three | Only simulated outlines | Conditional pilot; no unreviewed merge/publication |
| 5 | More chapter cross-references and simultaneous owner claims | Not run | No-go for full manuscript cohort until human pilot and lint repair |
| 10 | Compounding cross-plane references, source-staleness and reviewer queues | Not run | No-go |
| 57 | Full chapter graph, publisher review bottlenecks, evidence/version drift | Not run | No-go |

The current programme controls can *specify* how authors must behave but their reliable enforcement under concurrency has not been measured. The test does not demonstrate 2, 5 or 10 simultaneous independent authors operating in separate environments. Larger author counts cannot be estimated as safe merely by multiplying draft generation speed.

## 8. Trial scores and decision rules

All scores below are **evidence-bounded editorial confidence assessments**, not a standardised psychometric scale. A score for simulated inputs cannot meet the independent author's acceptance threshold regardless of magnitude.

| Dimension | Score /10 | Basis |
|---|---:|---|
| Reproducibility | **3** | Source-exact F1 defaults, aligned scripted outlines; zero genuine independent author trials |
| Governance | **5** | Clear frozen boundaries and review contracts; human approvals not obtained and seven unsafe lint misses |
| Review throughput | **2** | Budgeted only; no timed qualified reviewer sessions |
| Scaling readiness | **1** | No parallel independent author throughput, approval or conflict-recovery measurement |

**GO** for full-production cohort requires three genuinely independent participants, no critical semantic disagreement, exact-source decision defaults, valid fixture citations, mandatory human approval and a measured successful review cycle. **CONDITIONAL GO** allows bounded non-public drafting with manual verification and no claim of independent repeatability. **NO GO** prohibits scaling or publication when controls are untested, critical claims could escape lint, or reviewer capacity is unavailable.

| Proposed workload | Final verdict | Rationale |
|---|---|---|
| 2 chapters | **CONDITIONAL GO** for human-supervised pilot only | Simulation compatible but independent manuscript trial not completed |
| 5 chapters | **NO GO** | Seven critical/major lint misses and unavailable independent reviewer capacity evidence |
| 10 chapters | **NO GO** | Same defects plus unmeasured simultaneous ownership and integration conflicts |
| 57 chapters | **NO GO** | No demonstrated reliable consistency under scale; serious evidence and reviewer bottlenecks |

## 9. Required corrections, without redesign

1. **Repair lint** for T10/T11/T12/T14/T15/T16/T17; add exact titles, eight-plane allowlist, conflict/receipt fact rules and full F6/F7 template checks. Keep human review mandatory.
2. **Ratify, do not rewrite, existing candidate authoring crosswalk/Style Bible errata** through the approved editorial steward, with source version hashes.
3. **Recruit independent author cohort:** one Chapter 13 author, one Chapter 16 author, and one Atlas/F1 author with no cross-output access; capture sealed first submissions, timestamps and source SHA manifests.
4. **Require full prose and evidence excerpts:** each author must include exact decision defaults and evidence/caption assertions; no submission may invent Merlin/Meridian event identifiers, memory writes or signed permission outcomes.
5. **Blind reviewer checks source truth**, then A/B/C pairwise semantic alignment, recording severity and labour; re-run repaired lint with held-out faults before scaling to five.
6. **Operate one controlled publication gate** only after the genuine independent trial, complete editorial checks and observable reviewer throughput.

No new architecture, Atlas record, lifecycle stage, plane, editorial framework or backlog is necessary. This is validation and repair of existing authoring controls.

## 10. Final answer to the primary question

**Can multiple independent authors produce semantically equivalent manuscripts from the current framework?** The source-constrained scripted outlines suggest that the expected concepts can be represented compatibly, but **the independent-author proposition remains unproven**. In particular, the existing mechanical lint passes several materially false statements. The evidence supports a bounded pilot, not scalable authoring approval.

**Final judgement:** **CONDITIONAL GO** for exactly two supervised pilot manuscripts; **NO GO** for 5, 10 or 57 parallel chapters. The negative lint evidence is more decision-relevant than the agreement among scripted excerpts.

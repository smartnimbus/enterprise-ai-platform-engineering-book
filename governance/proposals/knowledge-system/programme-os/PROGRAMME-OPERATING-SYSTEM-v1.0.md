# PROGRAMME OPERATING SYSTEM — Execution Contract v1.0

**Programme:** Enterprise AI Agent Fabric / Decision-to-Evidence Engineering / Engineering Knowledge MVP  
**Status:** Proposed for independent governance approval; not ratified or deployed  
**Date:** 2026-11-24  
**Scope:** Work intake, approval, publication, maintenance, challenge and retirement for the already defined programme  
**Authority:** Subordinate to `REPOSITORY-GOVERNANCE.md`, frozen Style Bible v1.2, 4 Structural Layers, 8 Control Planes, 58 chapters, 30 Decision Atlas IDs/defaults and Meridian v1.0.  
**Execution backlog:** `MASTER-EXECUTION-BACKLOG.csv` (EX-001 onward); **not replaced** by this document.  
**Capacity boundary:** One architect, 15 protected hours/week, 642 planned year-one hours, 138 hours reserve; independent review time separate. The commitments remain 15 accepted articles, 12 tested patterns, three applied decisions, a Meridian replay, a learning lab and an Apress proof-of-book—not publication of all 100+100 candidates.

## 0. Operational status and immediate adoption condition

This document describes the **rules for operating work**, not a new enterprise architecture, book, methodology, strategy or roadmap. It may be adopted only by an explicit decision of the existing repository programme/author authority and the configuration custodian; until then it is an `IN_REVIEW` governance proposal. It creates no new frozen decisions, stages, chapters or Meridian facts.

**Observed repository snapshot (verified 2026-11-24):** `main` contains only `REPOSITORY-GOVERNANCE.md`; it is not branch-protected. Three draft PRs remain open: #1 book/research import, #2 knowledge-system governance, #3 deterministic-first research. These branches and their documents are **not yet approved sources on `main`**. The operating system must not assume CI or CODEOWNERS already exists. Its first executable work is to complete existing EX-001 through EX-006 rather than perform new knowledge production.

**One system, three independent axes:** (1) *workflow phase* tells us where a work item is; (2) *artefact authority/status* tells us whether content is approved/frozen/published; (3) *evidence strength* says what claims can be supported. No rule may derive one axis from another. A published artefact can be wrong and in need of challenge; an experiment may contain a strong independent test but still lack publication rights; a frozen baseline cannot be mutated by promoting an issue.

## 1. Operating principles — concrete rules and failure consequences

| Principle | Mandatory operating test | Failure action |
|---|---|---|
| **Authority over popularity** | Every promoted item resolves to exactly one canonical path, owner, version and approval commit. | Freeze promotion; open `AUTHORITY_CONFLICT` issue. |
| **Evidence over opinion** | Material claims reference attributable sources, reproducible tests or explicitly qualified inference. | `EVIDENCE_HOLD`; no publish. |
| **Small batches** | Standard PR changes one work item or tightly coupled vertical slice; the impact matrix identifies every affected ID. | Split PR unless exception approved. |
| **Reproducibility** | Runbook, pinned inputs, exact commands/versions and expected outcomes exist for executable claims. | Cap evidence score; cannot mark `INDEPENDENT_TEST`. |
| **Independent challenge** | High-risk and publication claims require a named non-author reviewer; feedback and dissent are recorded. | `BLOCKED_REVIEW`, not self-approval. |
| **Deterministic first** | State what rule, validator, search, database or policy engine can solve without AI; compare AI only for an ambiguous need. | Remove unnecessary AI step from proposed workflow. |
| **Knowledge as code** | Source and metadata are text-based where practicable; CI checks IDs, references, schema, changed authority and rights. | Stop merge pending validated correction. |
| **Separation of source, decision and proof** | A source note is not an approved article; an F1 Atlas page is not a local ADR; an event receipt is not proof of system-wide security. | Relabel and correct lineage before promotion. |
| **No hidden AI state** | Each handoff pins branch, SHA, task, evidence and tests; AI memory cannot approve anything. | Restart from known Git baseline. |
| **Right to challenge** | Any contributor may submit counterevidence; serious defects trigger an immediate visibility warning. | Temporarily suspend affected derived publication or usage. |
| **Safe retirement** | Deprecation identifies affected consumers, replacement, preservation/rights treatment and regression checks. | Do not remove abruptly; or quarantine immediately when security/privacy requires. |
| **Time-boxed attention** | WIP and review queues have explicit owner and re-evaluation thresholds. | Pause new intake and clear blockers. |

**Non-goals:** new 4×8 component, new Atlas decision, Meridian event, independent governance framework, full 10,000-article launch, proprietary graph runtime, certification programme, automatic agent approval, guaranteed exactly-once external effects, production security guarantees based on synthetic tests.

## 2. Work-item identity, types and lifecycle

### 2.1 One work item, one record

Use **GitHub Issues** as operational work queue once repository access is verified. Existing `EX-###` task IDs remain unchanged; new working issue identifiers use GitHub issue numbers. Article candidate IDs (`KA-###`) and pattern candidate IDs (`EP-###`) remain planning identifiers from the ranked CSVs and must not be confused with frozen `D-##` Atlas IDs or `MF-...` Meridian identifiers. Record: `issue_url`, `candidate_id`, `type`, `canonical_artifact_id`, `owner_role`, `owner_identity`, `phase`, `authority_tier`, `artifact_state`, `evidence_grade`, `priority`, `effort_hours`, `acceptance_tests`, `source_refs`, `rights_status`, `baseline_sha`, `dependencies`, `reviewers`, `review_by`, `last_reviewed_utc`, `next_review_utc`, `supersedes`, `blocked_reason`, `decision`, `handover_ref`.

**Immutable historical trace:** do not reuse an ID after rejection or retirement; leave a tombstone that links the decision and successor. Publication URLs may redirect but must not silently point to different claims.

### 2.2 Workflow phase — applicable to all seven types

`IDEA → CANDIDATE → DRAFT → IN_REVIEW → APPROVED → PUBLISHED → MAINTAINED → DEPRECATED → RETIRED`

This is an **issue workflow**. It does **not** replace the distinct authority states `IMPORTED_UNVERIFIED`, `DRAFT`, `IN_REVIEW`, `APPROVED`, `FROZEN`, `SUBMITTED`, `PUBLISHED`, `SUPERSEDED`, `RETIRED` defined by repository governance. E.g. a book chapter may be `IN_REVIEW` in both axes; an operational task updating documentation for a `FROZEN` chapter is `DRAFT` while the protected chapter stays `FROZEN` until an exceptional approval. The phase `MAINTAINED` is not a separate approval state: it means a published version is monitored and receives reviewed updates.

| Transition | Minimum evidence / action | Who may authorise | Required reversible/failure outcome |
|---|---|---|---|
| `IDEA → CANDIDATE` | Owner assigned; duplicate search; relationship to backlog; measurable user value; rights precheck; estimated effort. | Programme owner / backlog custodian | Reject as duplicate, out-of-scope or not affordable, recording rationale. |
| `CANDIDATE → DRAFT` | Dependencies ready; explicit tests/definition of done; time budget; pinned source baseline; suitable working branch. | Work owner under capacity rule | Return to candidate if evidence or rights missing. |
| `DRAFT → IN_REVIEW` | Source note/artefact and metadata present; reproducibility/test results; citations; impact; known limitations; PR opened. | Author/requester | CI fail or incomplete material returns to DRAFT. |
| `IN_REVIEW → APPROVED` | Applicable reviewers actually approve exact commit; evidence, rights, technical and style checks; explicit no-op fields marked N/A. | Domain steward + designated approval authority; author cannot self-approve high-risk items | `CHANGES_REQUESTED` or `BLOCKED_REVIEW`; material PR changes reset approvals. |
| `APPROVED → PUBLISHED` | Merged authorised source; exact release SHA/tag, link checks, rights, changelog, public claims checked, rollback. | Publication owner/editor and config custodian | `HOLD_PUBLICATION`; never publish directly from personal branch. |
| `PUBLISHED → MAINTAINED` | Usage/freshness watch, next review date, incoming challenges and owner exist. | Content steward | If owner/source disappears, mark stale and suspend preferred guidance. |
| `MAINTAINED → DEPRECATED` | Recorded reason and impact, replacement or "no replacement", warning, withdrawal date/conditions. | Domain steward + configuration/rights owner | Keep historical access where lawful; restrict urgently if unsafe. |
| `DEPRECATED → RETIRED` | All consumers checked, redirects or tombstones, archive custody, retention/legal decision, build/search exclusion. | Programme authority; rights/security approval for sensitive cases | Abort retirement if dependants unresolved. |

**Non-linear transitions:** `CANDIDATE → REJECTED`, `DRAFT → REJECTED`, `IN_REVIEW → CHANGES_REQUESTED → DRAFT`, `PUBLISHED/MAINTAINED → CHALLENGED` (overlay flag, not a new artefact state), `DEPRECATED → MAINTAINED` only after a new independent review; `RETIRED → PUBLISHED` is forbidden—create a reviewed successor. `BLOCKED` and `QUARANTINED` are **hold flags** with reason and owner, not evidence of approval. Legal/security takedown may bypass the normal deprecation waiting period with an auditable emergency record.

### 2.3 Type-specific definition of done (extra gates)

| Work type | Minimum input | Required approval evidence | Publication / maintenance test |
|---|---|---|---|
| **Research topic** | Specific falsifiable question and scope; source/rights ledger | Primary-source verification, contradictory references, research librarian and domain reviewer | Each claim status dated; stale standards and disputes flagged; raw extracts restricted. |
| **Knowledge article** | Approved research or direct verified primary source; defined reader task | Fact/evidence, domain and editorial checks; glossary/link consistency | One canonical concept, executable example or concrete counterexample, 90-day/annual review based on risk. |
| **Engineering pattern** | Context, forces, deterministic baseline, trade-offs and limitations | Positive **and negative** tests where behaviour claimed; security review if authoritative boundary | Reproduce at pinned versions, record limits/anti-patterns, Atlas mapping **without modifying frozen defaults**. |
| **Decision guide** | Alternatives, criteria, assumptions, sensitivity, cost and operating burden | Independent options challenge and quantitative-claim evidence | Clear when-not-to-use; maps to existing D-## where applicable; no new frozen Atlas IDs. |
| **Learning asset** | Role, prerequisites, observable learning outcomes, permitted sources | Technical/editorial + an independent learner completes assessment | Grading rubric, feedback, accessibility and current-version checks. |
| **Reference implementation** | Scope, SBOM/licence, threat model, pinned toolchain, test plan | Clean-room build; negative tests; secrets/dependency scan; independent technical/security review | Reproducible start/stop; synthetic-only by default; evidence cannot imply production assurance. |
| **Book chapter** | Frozen chapter ID and approved blueprint, Style Bible requirements, evidence map | Developmental, technical, rights/citations, figure/accessibility and publisher-review gates | Exact TOC number, F6/F7 (as applicable), no invented Meridian events, publisher proof hash; frozen chapter changes exceptional only. |

**Existing Decision Atlas pages:** Not an eighth invented content pipeline. They remain governed by the F1 Atlas workflow and frozen D-## defaults in `REPOSITORY-GOVERNANCE.md`. An **applied** decision uses a separate work item under the decision-guide/review process and points to—but never overwrites—the Atlas recommendation.

## 3. Backlog governance and one-person WIP

**Inputs:** existing `EX-` execution backlog, `KA-` articles, `EP-` patterns; new standards, threat alerts, errata, source corrections, incidents, independent challenges and reader feedback. New items are **append-only proposals**, not automatic priority overrides. An issue without a concrete outcome, evidence requirement and owner stays `IDEA` or is closed.

**Triage once weekly (15–20 minutes):** find exact duplicate/canonical owner; classify `BUG/SECURITY/CURRENCY/RIGHTS/CONTENT/IMPLEMENTATION/EXPERIMENT`; estimate effort and deadline; identify existing EX task or candidate; decide `ACCEPT`, `DEFER`, `REJECT` or `QUARANTINE`, with rationale. Track deferred ideas in the issue system; do not maintain another editable backlog spreadsheet as competing authority. The supplied CSV remains a pinned planning baseline until explicitly migrated to issues with a reconciliation report.

**Priority without vanity scores:** `P0` = active security/privacy, canonical-source corruption, broken publication integrity or prerequisite blocking a critical existing EX deliverable; `P1` = next committed deliverable or high-impact correctness; `P2` = proven optional enhancement; `P3` = exploratory/unvalidated. Safety emergency may preempt; product enthusiasm, AI novelty and follower count do not. Within a priority choose **unblock impact per hour**, then due date, then smaller independent slice. If P0 exceeds capacity, reduce planned scope and record lost milestone explicitly.

**WIP limits at 15 hours/week:** at most **one active authoring/build item**, **one externally awaiting review**, **one small urgent maintenance item**. `IDEA` and `CANDIDATE` do not count as active. No more than **two PRs owned by the architect** open for active work; already-open PR #1/#2/#3 form a bootstrap exception to close deliberately, not a new norm. The target PR review package is ≤4 hours of reviewer attention; larger pieces split by executable outcome. A branch is temporary, not an authority silo. No standing research sprint while main is unprotected and frozen sources remain unimported.

**Capacity review:** protected weekly hours = 15. Reserve at least 2.5 hours/week for review, maintenance and surprises; 12.5 hours/week planned delivery is an upper operating average. Do not treat the existing 642-hour yearly estimate plus 138-hour reserve as guaranteed staffing; adjust task forecasts on actual time logged. Escalate if critical item is blocked >5 working days, an external review >10 working days, or the 4-week rolling planned load exceeds available time. The same person may act as interim domain steward across domains but may not invent independent approvals.

**Rejection/kill rules:** reject if not connected to a verified user task, duplicates an existing asset, requires uncleared IP, contains untestable claims, replaces deterministic software without measured benefit, cannot be maintained, conflicts with frozen authority, or consumes the reserve without removing a higher risk. Record `rejected_by`, timestamp, source, rationale, reopen condition. No quiet deletion of previously accepted work.

**Release train:** merge whenever gates pass; knowledge releases and public announcements at most monthly in the MVP; publisher submissions separately authorised. No artificial requirement to publish a knowledge item each week.

## 4. Review system — gate matrix, real approval and escalation

| Review lane | Entry checks | Exit/approval checks | Independent review required when |
|---|---|---|---|
| **Editorial** | Reader, task, structure, Style Bible and source text complete | Comprehensibility, concise definitions, diagram alt text, F1/F6/F7 as applicable | Book chapter, Atlas publication, public learning content |
| **Technical** | Mechanism, interfaces, versions, reproduction and expected failure recorded | Accuracy, alternatives, limits, runnable/inspectable evidence | Pattern, implementation, security-critical technical claim |
| **Security/privacy** | Data/tenant and identity boundaries, confidentiality, threat and licence declared | Negative tests, no secrets/unsafe guidance, rights/privacy disposition | Identity, encryption, delegation, MCP/A2A, tool mutation, multi-tenancy, real data |
| **Architecture** | Existing 4×8 ownership and frozen decision mapping | Conformance, no architectural invention, cross-boundary consequences | Any potential baseline or responsibility conflict |
| **Evidence/research** | Claim IDs, precise sources/versions, tests and counterexamples | Supported scope, negative/positive outcomes, synthetic-vs-production truth in labels | New research conclusions, commercial/benchmark/security claims |
| **Publication/IP** | Approved commit, permissions, citations, publisher restrictions, link/figure check | Public-safe output, attribution, archived submitted hash and final sign-off | Every public release, Apress package, historical source publication |
| **Community** | Contribution guide, ownership, conduct, source provenance | Reproducible review process and response to objections | External contributions and public issue/release process |

**Single-architect mode:** the architect may draft, run deterministic tests, triage and suggest disposition; a qualified **non-author human** must sign off security-sensitive claims, source-rights clearance, frozen exception and publisher release. If no independent reviewer can be obtained, the item stays `IN_REVIEW/BLOCKED_REVIEW`, and publication slips. Routine low-risk internal research notes can be merged after mechanical checks and a documented owner review under the existing repository rules; these remain T3 and must not masquerade as approved knowledge. Named GitHub approval is valid only on the exact reviewed commit; do not invent handles or infer assent from silence.

**Challenge protocol:** any person can open a linked issue marked `CHALLENGE_OPEN`, including a reproducible counterexample, affected content IDs, claim, risk, alternative hypothesis and suggested test. The author writes an evidence-based response. If disputed, a different domain expert adjudicates. Unresolved high-risk claims receive a visible warning and are blocked from new promotion. A successful challenge generates a correction, successor or withdrawal plus a graph/search dependency impact report. `Resolved by consensus` is not a substitute for a falsifiable result.

**Time objectives (targets, not promises):** triage high-risk security/rights reports within one working day; critical correctness within two; ordinary review within ten; freshness alerts within next weekly triage; published correction as soon as verified with a recorded erratum. If an immediate takedown is required, restrict distribution first, preserve permitted audit facts privately, and obtain subsequent ratification. Owners on leave must have a documented deputy or the item becomes blocked.

**Review evidence log:** record reviewer identity and role, exact commit SHA, gate, decision (`APPROVED/CHANGES_REQUESTED/BLOCKED`), concerns, evidence examined, expiry condition if relevant, and approval timestamp. Review *comments* are not equivalent to approval. Re-open a gate if the relevant file changed materially after approval.

## 5. Knowledge quality and freshness — scores with hard stops

A five-axis rubric prevents a polished article from compensating for false content. Scores are integers **0–4** assessed on a rubric rather than an LLM's self-rating.

| Axis | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **Q: factual and technical quality** | False/unsafe | Mostly unsupported | Plausible with unresolved errors | Correct within stated scope; reviewed | Independently reproduced/challenged and corrected |
| **E: evidence strength** | None/fabricated | Unattributed secondary | Cited, unverified or illustrative | Verified primary/source-specific or reproducible synthetic test, correctly labelled | Independent reproducible test or convergent high-quality primary evidence for claim |
| **F: freshness** | Withdrawn/known invalid | Overdue with breaking changes | Dated, review needed | Reviewed within risk interval | Trigger-monitored; versions and validity actively checked |
| **R: reusability** | No user task | Abstract or vendor-specific slogan | Bounded useful explanation | Portable inputs, outputs and limitations | Independent reader can apply and adapt with evidence |
| **T: traceability** | No owner/source | Broken or ambiguous links | Stable object, partial chain | Canonical source, claims, owner, decision/related assets linked | Full change lineage through approval, tests, consumers and retirement |

**Do not use a single averaged score to release risky content.** Public technical article: each Q/E/F/R/T ≥3, reviewer and rights pass. Working note: may remain below threshold but visibly T3/UNVERIFIED. Demonstrator/pattern claiming tested behaviour: Q≥3, E≥3 **with a runnable negative test**, T≥3, no critical security test failure. Publisher sample: all relevant domain gates, Style Bible, author rights, source verification, independent technical and editorial review. A critical fact error, missing licence, unknown real-data origin, confidentiality leak, source-of-truth collision, unresolved material counterevidence or missing independent high-risk approval is an unconditional `STOP`, regardless of average score. Scores are assessor judgments and must carry evidence links.

**Risk-based freshness classes:** (A) credentials, vulnerabilities, product security changes and rapidly changing vendor APIs: review on trigger, at most every 90 days while published; (B) vendor features, runtimes, MCP/A2A, pricing: review on version change, at most every 180 days; (C) stable design principles and architecture patterns: at most annually; (D) historical analysis: review provenance on correction or rights event rather than rewrite history. Review deadlines are **proposed service policies**, not claims of external standards. Missed dates flag `STALE_REVIEW_REQUIRED`, suppress preference in search and block new republication; they do not retroactively erase lawful history.

**Challenge/retirement outcomes:** `KEEP` (supported), `CORRECT` (same ID, revision and erratum), `SUPERSEDE` (new canonical version/ID with redirect), `DEPRECATE` (warning while dependants migrate), `RESTRICT` (privacy/security/rights), `RETIRE` (withdraw from active navigation with preserved tombstone). Broken links, orphaned consumers, or lost steward block ordinary retirement. Expiring vendor claims trigger review, **not** silent changes to frozen decisions.

## 6. Steward accountability and minimum separations

| Role | Owns / may do | Cannot do independently |
|---|---|---|
| **Programme owner / Author-Editorial Director** | Scope, capacity, priority, final public/publisher release, escalation | Override source facts, rights, technical/security adverse findings silently |
| **Configuration/Knowledge custodian** | IDs, canonical paths, manifests, lineage, repository controls, backups and archival | Approve own exceptional frozen-baseline change alone |
| **Domain steward** (identity, security, networking, platform, data, AI, SRE, FinOps, editorial) | Definition accuracy and risk-specific review, owner assignment, freshness | Claim cross-domain authority or waive independent high-risk review |
| **Research librarian** | Source capture, versions, citations, contradiction status and rights flags | Promote unverified sources as evidence |
| **Technical reviewer / independent challenger** | Mechanism, reproducibility, edge cases, fail/stop evidence | Rewrite author choice without a documented change |
| **Developmental editor and publisher liaison** | Reader journey, Style Bible, sample and submission release | Modify canonical decisions or fabricate technical approval |
| **Contributor / trainer** | Propose files, run experiments, submit PRs and evidence | Merge into protected baseline without required checks |
| **AI assistant** | Search public/authorised sources, draft and classify proposals, run permitted deterministic checks, produce candidate diffs | Sign review, approve or publish, override permissions, invent tests, claim a chat as canonical, make sensitive data public |

**One-person reality:** one architect may fulfil multiple drafting/custody roles provisionally, but must obtain outside review for gate outcomes needing independence. Do not fabricate stewards to populate a RACI chart. Roles are accountable lanes. Future growth adds genuine domain maintainers, verified CODEOWNERS, rotating deputies and review quotas without changing authority semantics. Identity/security stewardship applies to the *knowledge programme* and must not be confused with Meridian fictional identities.

## 7. AI operating model and portable continuity

**Tool-neutral input contract:** Every GPT, Claude, Claude Code, Copilot or successor engagement begins with repository URL, branch/commit, issue ID, target artefact, authorised source list, baseline/freeze rules, rights boundaries, last test result and a bounded deliverable. If the agent cannot fetch a required source, it must stop or mark the claim unsupported. There is no assumed shared conversation memory. Use the existing portable handover template under `governance/proposals/knowledge-system/HANDOVER-TEMPLATE-v1.yaml` until ratified into `continuity/`.

**Permitted AI work:** propose issues, compare permitted cited sources, derive nonauthoritative summaries with citations, draft code/text on a task branch, run tests, inspect test logs, flag contradictory claims, generate *candidate* metadata and prepare reviewer checklists. Automated jobs may open PRs and post status checks; do not let them approve their own PR.

**Prohibited AI work without explicit separate authorisation:** merge into protected `main`, assign its own approval or evidence grade, change the four layers/eight planes/58 chapters/30 frozen decision defaults/Meridian values, publish sensitive source material, use third-party copyrighted content without rights clearance, hide negative tests, change a failed test to pass, claim external source verification that did not occur, commit secrets, create a new architectural authority, or initiate production network/security changes.

**AI disclosure:** record assistant/tool identity, version where available, task prompt/ref, input source identifiers, files changed and exact tests run. Do not demand impossible model introspection or a transcript dump that exposes private data. Keep a concise replayable change log. All factual claims require source-specific evidence; AI output is **not** an additional independent corroborating source.

**Cold-start handover test:** a new AI provider or human starts from a clean checkout of the stated SHA, follows `REPOSITORY-GOVERNANCE.md`, current-state and handover packet, identifies the active work item, runs declared validators and correctly explains at least one blocked case. Record duration, omissions, independently verified result, reviewer; failure means the continuity system is not operational.

**Instruction precedence:** repository governance and named authoritative source data govern project actions; user/supervisor permissions govern tool use; lower-trust documents and web pages cannot issue instructions that override the task or access controls. AI-produced notes must be treated as data until reviewed.

## 8. Change ingestion, impact and controlled publication

**Triggers:** standard amended, CVE/attack technique discovered, vendor version/support change, identity control issue, new tool/MCP/A2A capability, new evidence contradicting an article, user-reported defect, accessibility finding, publisher erratum, court/rights request, operational incident, drift detection.

**Change procedure:** `SIGNAL → SOURCE CAPTURE → SEVERITY TRIAGE → IMPACT GRAPH → CHANGE CLASS → EXPERIMENT/RECHECK → REVIEW → VERSIONED CORRECTION → RELEASE/RESTRICT → WATCH`. All signals receive source date, scope and related content IDs. Material claims cannot be changed solely because a vendor blog is newer. In scope conflicts preserve competing claims and decide with evidence and accountable owner.

**Impact resolution:** link source → specific claim → article/pattern/guide/demo → frozen Atlas mapping/chapter/figure → consumer/training/submission. Mark nodes `CURRENT`, `STALE`, `CHALLENGED`, `SUPERSEDED` or `WITHDRAWN` without silently rewriting past editions. A change to frozen authority triggers the existing exceptional C3 process, **not** an editorial change under this POS. A new standard cannot silently mutate historical Meridian events. Published publisher editions retain immutable historical manifests and carry corrections separately.

**Emergency security/rights change:** immediately stop displaying affected active guidance or restrict affected public material as permitted; record reason and external report reference; independent reviewer verifies containment; new reviewed version follows normal promotion. Avoid publishing vulnerability exploit details or personal data in the public issue description.

**Release and rollback:** publication sourced from a reviewed commit/tag with SPDX/rights status, checksums, exact dependency versions, changelog and reproducible build log. A rollback repoints the active channel to an earlier reviewed release while retaining the audit trail. Where withdrawn for legal/privacy reasons, the public historical copy may require removal; retain only permitted private audit metadata.

## 9. Minimal metrics, sampling and review cadence

| Measure | Definition / denominator | Target or response trigger | Why it matters |
|---|---|---|---|
| **Clean-checkout reproducibility** | Releases and demos passing declared tests on an independent clean environment / attempts | 100% before public release; block on failure | Actual usable proof |
| **Provenance completeness** | Approved claims with precise, current source/test record / all sampled approved material claims | 100% on release sample; remediate misses | Avoid invented certainty |
| **Independent-review coverage** | High-risk releases with named eligible non-author reviewer / all high-risk releases | 100%; block otherwise | Prevent self-certification |
| **Review lead time** | Median calendar days from `IN_REVIEW` to disposition, with P90 alongside | Review weekly; investigate P90 >10 working days | Queue health |
| **Cold-start onboarding success** | New contributor/agent handovers reproducing target result unaided / attempts | At least 3 recorded pilots; fix failures | Continuity beyond individual |
| **Applied method repeatability** | Blind reviewers whose verdict matches documented case and evidence / trials | Record disagreements; cannot claim mature method before independent pilot | Methodological validity |
| **Negative test efficacy** | Critical forbidden operations demonstrably blocked / critical negative cases executed | 100% before publishing tested-control claim | Tests actual boundary |
| **Source currency** | Published active claims with in-date reviews / applicable active claims | Flag all overdue; block fresh publication of overdue material | Technical freshness |
| **Adoption with outcome** | Distinct verified teams applying one decision+evidence workflow and reporting outcome | Report observed cases only; avoid page-view proxies | Enterprise relevance |
| **Maintenance burden** | Hours spent reviewing, updating and restoring / 15 available weekly hours | Escalate if sustained >30%; reduce corpus intake | Sustainable operating cost |

**Do not optimise for:** number of articles generated, tokens spent, social followers, PR volume, number of AI agents, unchecked model-generated citations, stale download counts, or graph node count. Track usage only when it is consent-respecting and tied to a user task or independent reuse.

**Cadence:** daily only when active high-risk item; **weekly 20-minute** triage/WIP/blocker review; **monthly 45-minute** source-currency, quality sample, capacity and published corrections; **quarterly** clean-room restore and blind adoption sample; **annually** re-evaluate maintenance cost, sustainability and ownership succession. In a one-person year, combine monthly meetings with deliverable reviews rather than create a new bureaucracy.

## 10. Minimal executable operating system

### 10.1 Systems of record (avoid duplication)

| Object | One writable record | Derived view / prohibition |
|---|---|---|
| Work-in-progress/priority | GitHub Issue after controlled EX backlog import, linking original EX/KA/EP ID | GitHub Project board is a view; no competing editable plan. |
| Frozen source | Canonical imported file + approved baseline manifest and hash | Chat summaries, generated PDFs and web pages cannot overrule. |
| Source/rights | Source-and-rights ledger | Article bibliography is a projection, not new licence authority. |
| Decision | Frozen F1 D-## catalogue; local applied ADR separate | Never edit D-## to record one enterprise's choice. |
| Evidence | Versioned test/evidence record and its exact fixture/tool inputs | A diagram or model summary is not the evidence. |
| Review/approval | GitHub PR reviews linked to exact SHA; restricted publisher approvals separately stored | No "approved" tag based on comments alone. |
| Published knowledge | Versioned, rights-cleared release artefact | Website and search index regenerated from master. |
| Retirement | Change/retirement issue with redirect and impacted consumer IDs | Do not delete link history or recycle IDs. |
| AI handover | Versioned session/handover packet linked to issue/commit | Never rely on a model's conversation memory. |

### 10.2 Minimum mechanics: work item validator

A small portable JSON schema and offline Python validator accompany this contract. They verify **record structure, allowed workflow phase, ID and date shapes, hold flags and required fields**. They cannot verify human approval, evidence truth, rights permission, GitHub protection, the content's accuracy or actual publication. Automation must never conflate `schema valid` with `approved`.

**Proposed work-item location after adoption:** `continuity/work-items/<issue-id>.json` for recovery snapshots **derived from** GitHub Issues, not a parallel writable backlog. The templates and validator in this PR remain in `governance/proposals/knowledge-system/programme-os/` until independently accepted. Avoid mass-creating new issues before EX-001 reconciliation.

**Minimal PR checklist:** claim ID; stable canonical source; no frozen modifications; source/rights; baseline commit; change-class and impacted assets; test command and result; counterexample; actual reviewers; build/preview if applicable; version/retirement impact; next review date; synthetic claims labelled; AI assistance declared. Default to `not applicable—reason` rather than silent omissions.

### 10.3 Scale without a central person

At 1 owner, the critical capability is *recoverable source authority* and independent review, not committee structure. At 5–15 contributors, assign verified domain stewards, backups, review rotation, workload limits and CI owners. At 100 contributors and 10,000 assets, shard by **maintainer ownership domain and release cadence** while keeping a global canonical ID registry, source/claim lineage protocol and compatibility contract. Add search indexing only after reliable metadata and access controls; vector/LLM retrieval is derived and must expose status/conflict/rights, never launder stale claims. Every repository needs a named maintenance owner, restore drill and retirement plan. A new repository is justified by independently deployable code, access separation, release cadence or licensing—not by a new topic label.

**No single-person dependence:** two people must be able to rebuild from a clean release; all authentication, publishing and domain stewardship accounts must support documented succession and recovery through approved organisational arrangements. No personal API keys embedded in docs; signed release credentials stored in approved secret managers; external publisher rights remain in private custody.

### 10.4 First operational acceptance test (not a new roadmap)

Using the already scheduled tasks EX-001–EX-006, one independent reviewer must be able to: (1) resolve an EX issue and canonical source; (2) show the source's approved SHA and rights; (3) demonstrate a draft item being blocked by invalid provenance; (4) demonstrate one passing item reaching an independently approved PR; (5) replay the Meridian consistency/negative assertions on the frozen fixture; (6) reproduce release outputs from a clean checkout; (7) open a credible challenge that yields a visible corrective work item and dependent-asset impact; (8) deprecate a synthetic trial item and confirm redirects/tombstone; (9) hand work from one model/human to another using only the repository and handover packet. **No frozen artefact should be changed during this acceptance test.**

**Go / no-go:** `GO` only when real approvals, controls, tests and a successful clean-room handover are demonstrated; else retain `PROPOSED/NOT IMPLEMENTED`. Progress reporting separates *specified*, *committed on review branch*, *merged*, *configured*, *tested* and *independently validated*.

## Annex A — Review classes and required lanes

| Class | Typical examples | Mandatory lanes |
|---|---|---|
| C0 draft/candidate | New uncited notes, brainstorming | Work owner, source/licence precheck; cannot publish |
| C1 non-sensitive reviewed content | Low-risk editorial explanation | Editorial + evidence and link checks; independent where publication requires |
| C2 technical/security/public executable | Identity/PEP, MCP, live implementation, benchmark | Technical + security if applicable + independent reproduction + evidence + publication |
| C3 frozen authority change | Change D-## default, chapter numbers, Meridian event, 4×8 model | **Exceptional process in existing REPOSITORY-GOVERNANCE.md only** |
| C4 urgent withdrawal | Exposed secrets, rights breach, dangerously wrong security guidance | Immediate restriction plus retrospective independent approval |

## Annex B — Boundary and anti-duplication conflict rules

1. Do not create a second `CURRENT-STATE.md` or forked `BASELINE-MANIFEST.yaml` just to satisfy an AI tool; use pointers.
2. Do not give the engineering encyclopedia authority to rewrite frozen book decisions.
3. Do not mix a source research dossier, article, cheat sheet and applied ADR into one unreviewable monolith; they have distinct decision and review contracts.
4. Do not count a successful fixture validator as proof of an implemented control or successful publisher review.
5. Do not create authorisation or approval receipts from model-generated prose.
6. Do not call 100 candidates an MVP deliverable: the actual year-one acceptance remains 15 articles and 12 tested patterns.
7. Do not treat a GitHub PR being open as approval; `main` and actual tags determine ratified state.
8. Do not use public GitHub for sensitive field incidents, unreleased licensed books or personal information; use restricted storage with opaque evidence IDs.

## Annex C — Source basis and remaining implementation gap

**Read against (local copies verified 2026-11-24):** `REPOSITORY-GOVERNANCE.md` v1.0, `MASTER-KNOWLEDGE-SYSTEM-BLUEPRINT-v1.0.md`, `MASTER-EXECUTION-BACKLOG-v1.0.md` and `.csv`, ranked article/pattern candidates, `PROGRAMME-COMPLETENESS-ASSESSMENT-v1.0.md`, `MASTER-GAP-REGISTER.csv`, `WORKSTREAM-SCORECARD.csv`. Those local files may have matching review-branch counterparts but are **not all approved on main**. This contract extends their operational procedures; it does not supersede their authority.

**Implementation backlog already exists:** EX-001 reconcile draft PRs; EX-002 rights; EX-003 canonical import; EX-004 branch rules; EX-005 freeze checks; EX-006 fixture CI. Implement those before adopting a new workflow bot, graph database or knowledge platform. No new strategy documents are required.

**Not yet demonstrated:** GitHub ruleset enforcement, real CODEOWNERS approval, clean-room reproducibility on committed canonical Meridian bytes, a running publication gate, a repeatable external user test, independent approval of this POS, and any 10,000-asset performance benchmark. Do not report these as complete.
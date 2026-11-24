from pathlib import Path
import csv
D=Path('/mnt/data/phase2_intellectual')
def rd(n):
 with (D/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def table(rows,columns,limit=None):
 if limit:rows=rows[:limit]
 line='| '+' | '.join(lbl for key,lbl in columns)+' |\n| '+' | '.join('---' for _ in columns)+' |\n'
 for r in rows:
  line+='| '+' | '.join(str(r.get(key,'')).replace('|',' / ').replace('\n',' ')[:240] for key,lbl in columns)+' |\n'
 return line
EA=rd('ENTERPRISE-ARCHITECTURE-COVERAGE.csv'); RA=rd('REFERENCE-ARCHITECTURE-VIEW-COVERAGE.csv'); DEC=rd('DECISION-ATLAS-30-EDITORIAL-ASSESSMENT.csv'); DQ=rd('MISSING-DECISION-QUESTIONS-NOT-NEW-IDS.csv'); CH=rd('CHAPTER-CTO-USEFULNESS-58.csv'); SE=rd('CHAPTER-BRIEF-SECTIONS-348.csv'); PT=rd('BOOK-PART-USEFULNESS-8.csv'); ME=rd('MERIDIAN-LIFECYCLE-COVERAGE.csv'); CG=rd('MISSING-CHAPTER-CONTENT-NOT-NEW-CHAPTERS.csv'); GA=rd('TOP-25-INTELLECTUAL-AND-PUBLICATION-GAPS.csv')
body='''# Phase 2 — Intellectual Completeness and Publication Readiness Assessment

**Work:** *The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale* / Enterprise AI Platform Engineering body of knowledge  
**Assessment date:** 24 November 2026  
**Assessment posture:** adversarial developmental editor + independent enterprise architect; **not** a publisher decision or formal compliance certification.  
**Scope:** intellectual content, teaching continuity, enterprise coverage, method usefulness and publication preparedness. Repository convergence findings are treated as accepted background and are **not re-audited**.  
**Frozen:** E/T/C/L Structural Layers; eight Control Planes; Chapters 1–58 and all chapter IDs/titles/order; D-01–D-30 titles/defaults/options/roles; Meridian Fixture v1.0 and its 15 events, six evidence records, identities and claims; Style Bible v1.2.

## Evidence reviewed and provenance

Primary inputs examined directly:

1. `Enterprise_AI_Agent_Fabric_Revised_TOC.csv` — 58 numbered chapters, purpose, template, decision mappings and required artefacts.
2. `Enterprise_AI_Agent_Fabric_Development_Blueprint.md` — canonical E/T/C/L and eight-plane accountability, 58 chapter briefs, 30 F1 master decision pages, lifecycle, examples and detailed manuscript instructions.
3. `Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv` — every D-01–D-30 record, its context, frozen default, rationale, trade-off, deviations, reversibility, output artefact and chapter map.
4. `style-v1.2.md` — F1/F2/F5/F6/F7 and reference-entry norms, length, visual, terminology, reviewer and editorial rules.
5. `Meridian_Evidence_Fixture_v1.0/Meridian_Evidence_Fixture_v1.0.md` and the 18-member `Meridian_Evidence_Fixture_v1.0.zip` — fictional organisation and actors, 15 event records, six canonical evidence JSON files, complete event ledger and validation code.
6. `Chapter_13_Authoring_Blueprint_v1.0.md`, `Chapter_16_Authoring_Blueprint_v1.0.md`, `chapter-16-gateway-control-plane-v1.0.md`, `chapter-16-editorial-self-review-v1.0.md` — F6/F7 specifications and actual Gateway draft.
7. `Enterprise_AI_Agent_Fabric_Editorial_Review.md`, `Apress_Publisher_Proposal_Draft.md`, and `convergence/REPOSITORY-CONVERGENCE-AUDIT-v1.0.md` — editorial risks, publisher proposition and accepted completed manuscript/status findings.
8. Existing independent validation, hidden-method and knowledge system reports as supporting research, not implemented/approved assurance.

The broad historical archives were previously assessed; this phase does **not** reperform forensic review of every archived source. Publisher and competitor conclusions are **editorial estimates**, not confirmed acquisitions-board actions. Official publishers/standards are used only for contextual comparison and are separately cited below.

### Scoring protocol (essential to avoid false precision)

Two different things must not be averaged into a single deceptive number:

- **Design coverage (0–5)**: 0 absent; 1 named; 2 conceptual; 3 specified responsibilities and contracts; 4 coherent worked illustration; 5 independently reproduced and externally reviewed solution within scope.
- **Demonstrated evidence (0–5)**: 0 none inspected; 1 author-specified illustration; 2 coherent synthetic cross-record proof; 3 executable verified reference implementation; 4 repeated independent field use; 5 mature field evidence with independently audited outcomes.
- **Chapter usefulness (1–10)** is a **potential-relevance judgment from the frozen chapter brief**, across Strategy, Execution, Governance, Platform Engineering, Security and Enterprise Adoption. It is **not a grade for unwritten prose**. For every chapter-brief subsection, the score is inherited from the parent chapter; no individual subsection has an independently validated quality score. The section inventory records whether the brief actually supplies that element. The only standalone manuscript observed is Chapter 16, still unapproved.
- **Publication maturity (0–10)** measures inspected work plus acceptance evidence: this is different from the book concept's relevance. Zero independent pilot results are assumed unless a test report substantiates them.

Scores are conservative editorial rubrics, not empirical confidence intervals or percentages of pages typeset. `10/10` is a criterion the programme might pursue, **not a promise** that all external reviewers or enterprise sectors will agree.

---

## 1. Executive verdict

**Conditionally strong architectural reference; incomplete enterprise architecture; underdemonstrated method; not acquisition-ready as a finished manuscript.**

The architecture's technical responsibilities are coherent: Execution Environment, Tooling, Context and Lifecycle are bounded by Identity, Gateway, Observability, Verification, Governance, FinOps, Data Protection and Interoperability responsibilities. That separation supports a sophisticated enterprise agent platform book. The 30 Atlas decisions are more usable than a technology glossary because they include explicit defaults, when-to-deviate criteria, reversibility and an output artefact. The Meridian refund/Context story illustrates the distinction between tool-selection error, policy denial, network enforcement, semantic disagreement and release failure.

**But the solution is not a complete Enterprise Architecture merely because it has an architecture diagram.** The business value stream, enterprise capability map, information authority, application collaboration and deployed technology instances are not developed with the same precision as the normative runtime/control boundaries. Nor does the one synthetic refund scenario establish finance, resilience, delivery, product operations or retirement proof.

Most consequential intellectual risks:

1. **Breadth masquerading as depth.** A 58-chapter outline covers virtually every heading, but many mechanisms, diagrams, worked choices and failure exercises have yet to be written.
2. **A repeatable method not yet independently reproduced.** Decision-to-Evidence Engineering is a plausible synthesis, but no field trials show that two unrelated practitioners reliably reach correct decisions and reconstruct enforcement evidence.
3. **Layer/plane chapters, stage chapters and playbooks can repeat.** Each must teach a different question. Architecture: *what owns the control?* Lifecycle: *when must the control be established/updated?* Playbook: *what exact steps and acceptance evidence does the reader perform?*
4. **The only mature narrative path is negative.** Meridian has an impressive denied-action and failed release chain, not a comparable admitted positive workflow, operational incident, failover, budget or retired system example. Add separate clearly synthetic companion teaching specimens, **not** fabricated events within the frozen fixture.
5. **Publishing fit is unproven.** The work has an Apress-relevant professional audience but lacks a reviewed sample package and most manuscripts. The historical references have not all been cleared for quotation, figures or reproduction.

**Publication decision now: NO GO for a finished book.** A proposal conversation may be possible with clearly labelled draft status, sample content and a realistic delivery commitment; it must not claim independent method assurance or finished-manuscript readiness.

---

## 2. Enterprise Architecture completeness — ten domains

The table grades **intellectual coverage of the book as specified**, not a real enterprise implementation. The location references are frozen chapter numbers, not new architecture elements.

'''
body+=table(EA,[('architecture_domain','Domain'),('primary_chapters','Existing chapters'),('design_coverage_0_to_5','Design /5'),('demonstrated_evidence_0_to_5','Evidence /5'),('substantive_gap','Principal gap')])
body+='''
**Interpretation:** arithmetic mean design coverage = **3.10/5** (specified more fully than proven), demonstrated evidence = **1.40/5**. These are ordinal rubric summaries, not statements that the architecture is 62% deployed or 28% compliant. Business, capability and technology architecture are materially thinner than platform and security architecture. The book is an **enterprise AI platform engineering reference**, not a substitute for an enterprise's complete TOGAF architecture work.

### Enterprise-level completeness test

A convincing enterprise case should connect **business purpose → capability → business owner → information product → application/service → platform control → decision → deployment variant → operational evidence → owner-approved disposition**. The frozen chapters name almost all of these concepts, but no one end-to-end, validated specimen proves the joins. Close this gap in Ch1/3/6/10/24/35/40/41/57 using existing D-01/D-03/D-06/D-24 mappings. No additional Structural Layer is required.

### Security, privacy and governance specificity

The architecture differentiates Identity issuance from Gateway policy enforcement, Governance policy authorship from Verification test decisions, and Context semantic resolution from Data Protection retention. This is an architectural strength. The gap is *how a reviewer verifies those boundaries in a deployed system*: attested credentials, key ownership/rotation, workload token revocation, tenant-internal caches, audit-store integrity, fail-closed emergency procedures and deletion propagation. These are testable implementation contracts in the existing planes, not a missing ninth plane.

---

## 3. Reference Architecture completeness — eight views

'''
body+=table(RA,[('view','View'),('primary_chapters','Chapter evidence'),('design_coverage_0_to_5','Design /5'),('demonstrated_evidence_0_to_5','Evidence /5'),('assessment','Finding')])
body+='''
The reference views average **3.25/5 design** but **1.00/5 demonstrated evidence**. The conceptual/logical views are strongest; physical/deployment views are optional but presently too abstract to teach an implementation review. The book does not need an endorsed cloud stack. It needs one labelled, illustrative deployment with networks, data stores, workload identities, trust boundaries, service ownership, constraints, failure modes and a reader-run verification path.

The runtime narrative should contain at least four differentiated journeys (read-only success, denied mutable action, interrupted/revoked durable work, and retired/replaced use case). Meridian canonically owns the denied case; the other journeys may be separate teaching scenarios without adding events to `MF-FIX-001`.

---

## 4. Decision Atlas adequacy — preserve the thirty frozen decisions

**Finding: all major *framework-level* decision categories needed to teach the architecture are present within D-01–D-30.** There is not enough evidence to justify adding a thirty-first Atlas decision, changing a default or splitting an existing record. Several gaps are *nested implementation decisions*: crypto profile and revocation timing, online-evaluation gold sets, model supply-chain policy, cache and memory retention, MCP/A2A trust contracts, and cost/workload thresholds. They belong in existing decision applications and book sections.

### Editorial classification, not a change in normative status

- **Foundational (12):** decision pages whose question is relevant to establishing a shared enterprise context: adoption, sourcing, operating model, tenancy, risk/autonomy, ownership, identity, evidence, protection, budgets, change and exit. This label indicates **reading/review priority**, not a newly mandatory default.
- **Context-mandatory (16):** choices that become essential when their service or risk condition exists (mutable actions, model changes, tool contracts, recovery, memory, incident etc.). This is conditional editorial applicability, not a legal or normative waiver.
- **Conditional (2):** D-13 cross-agent memory and D-16 human approval, which are governed by particular use cases and action risks. Their exact existing default/deviation wording still controls.
- **Implementation-specific:** these are not extra Atlas decisions; see the 19 **DQ-xx research/engineering questions** below.

**Note:** D-16 applies when the chosen risk/action category requires human approval. Calling it 'conditional' here does **not** imply that a required approval can be skipped.

### Complete 30-decision classification and adjacency

'''
body+=table(DEC,[('id','ID'),('title','Existing frozen decision'),('editorial_reading_priority','Reader priority'),('overlap_boundary','Neighbouring boundary')])
body+='''
These neighbouring pairs are **adjacent, not necessarily duplicates**: D-03/D-06 organisational choice vs accountable owner; D-04/D-25 isolation vs data obligations; D-09/D-21 tool schema vs cross-system protocol; D-10/D-18 admission vs non-bypassability; D-11/D-14 access vs semantic correctness; D-12/D-13 memory management vs cross-agent sharing; D-19/D-20 identity vs delegation; D-22/D-23 evaluation design vs release authority; D-26/D-17 budget vs routing; D-27/D-15 DR tier vs resume correctness; D-30/D-25 exit vs data disposal. Drafting must make each boundary visible in **one sentence** or the Atlas will feel redundant.

### 19 high-priority decision questions not requiring new Atlas IDs

'''
body+=table(DQ,[('question_id','Gap'),('missing_implementation_decision','Question'),('existing_Atlas_decisions','Apply within'),('priority','Priority')])
body+='''
**Acceptance test for each:** readers should be able to state the local decision and owner, list viable alternatives and disqualifiers, name an enforcement point, identify positive/negative evidence, and explain what would make them reverse the choice. If not, the chapter describes a concept but does not teach a decision.

---

## 5. Meridian lifecycle adequacy — fixed specimen, uncovered journeys

Meridian v1.0 is a *deliberately bounded fictional case*, not an incomplete production deployment to be back-filled with invented records. It already covers three fictional business units, tenant assignments, actor identities, source records, six evidence artefacts, and 15 linked events. The Week 7 insurance result is quarantined after a source-level check; the Week 8 retail statuses remain `UNRESOLVED`; the Week 9 proposed `refund.issue` exceeds effective delegation and is denied; a separately simulated direct-route egress test is blocked; Week 11 release candidate is blocked for a **behavioural** assertion even though the Gateway prevented the side effect. The later Week 12 restricted read-only release is **not** retroactive approval of the failed candidate.

The JSON is authoritative for exact field values. The actor-chain token claims in the fixture are **illustrative and unsigned**; no 'signed authorisation receipt' or cryptographic assurance should be claimed. The denied `MF-EVD-AU-001` is not a permit, and the external ledger mutation count is zero.

### Lifecycle coverage

'''
body+=table(ME,[('journey','Journey'),('coverage_status','Observed class'),('related_decisions','Atlas mapping'),('needed_teaching_or_validation','Missing exercise')])
body+='''
**Critical editorial rule:** do not silently generate `MF-EVT-016`, a successful £125 refund, a retirement, a production firewall run or a cryptographically signed token and call it Meridian v1.0 evidence. If the existing chapter needs another demonstration, label it a separate synthetic **companion example** with separate identifiers and a clear non-canonical status. Avoid counterfeit provenance: a reader must never mistake an invented extension for frozen fixture truth.

**Meridian acceptance proof:** version-pin `MF-FIX-001`, reproduce the six canonical records and shared case/trace IDs, run its validator, have an independent reader reconstruct the correct sequence, and report which requirements the fixture cannot demonstrate. Its present 27 internal consistency checks are valuable for *internal* coherence, not operational certification.

---

## 6. Book architecture — sequencing, completeness and overlap

All **58 numbered chapters** have a planned title, reader outcome, template, mapped decision(s) and output artefact. That is a complete **construction map**, not a complete manuscript. Ch13 has a detailed F6 authoring blueprint, not a manuscript. Ch16 has an F7 blueprint and one standalone draft; no independent editorial/technical acceptance is evidenced. Ch23 includes the thirty-decision catalogue but only D-10/D-18 individually produced F1 pages. The chapter numbers remain **unchanged**.

### Sequencing review

| Transition | Risk | Repair within frozen chapter sequence |
|---|---|---|
| Ch1–4 → Ch5–9 | Reader may assume a shared Fabric is always required | Preserve negative no-build decision in Ch4 and sourcing alternatives in Ch5 |
| Ch9 → Ch10 | Sponsorship/autonomy decision may seem divorced from implementation | Add short one-page bridge from autonomy envelope to layer/plane responsibilities in Ch10 |
| Ch10 → Ch11–22 | Nine-plus structural concepts overwhelm readers | Provide one architecture-at-a-glance and an acronym/prerequisite card, not new chapters |
| Ch13 → Ch14–16 | Context state/memory, durable resume and identity delegation become blurred | Use exact boundary contract and one stop-and-resume case with stale permission denied |
| Ch22 → Ch23 | Atlas could appear as repetitions of architectural chapters | State one-page choice/output/when-to-deviate orientation; readers apply decisions, not recite |
| Ch23 → Ch24–34 | Ten stages may repeat decisions instead of progressing | Each stage: entry conditions, approval authority, evidence artefact, exit/rework outcome |
| Ch34 → Ch35–40 | Exit stage precedes general operations in reading order | Add orienting transition: Part VI is the reusable operational reference for *all* stages |
| Ch40 → Ch41–50 | Playbooks may paraphrase lifecycle and operations | Make each playbook executable with inputs, failure branches, commands/tests and sign-off |
| Ch50 → Ch51–58 | Reference entries may be a glossary masquerading as actionable appendix | Provide quick lookup, filled examples, current source dates, acceptance and navigation |

### Duplication candidates requiring editorial differentiation

| Related chapters | What must remain distinct |
|---|---|
| Ch1 and Ch4, Ch5 and Ch41 | Value case; rejection criteria; sourcing choice; **executed funding appraisal** |
| Ch3, Ch6 and Ch35 | Definitions/ownership boundary; operating-model choice; day-to-day RACI and deputies |
| Ch7, Ch21 and Ch28/43 | Isolation choice; protection obligations; tenant establishment; **tested provision** |
| Ch8, Ch20 and Ch38 | Model/provider strategy; budget control-plane accountability; showback and chargeback operations |
| Ch10, Ch26 and Ch42 | Canonical responsibilities; stage-specific approval; architecture playbook execution |
| Ch11, Ch14 and Ch36 | Worker isolation; orchestration/resume; SLO/DR and service recovery |
| Ch13, Ch17 and Ch40 | Context provenance; telemetry collection; independent audit reconstruction |
| Ch15, Ch16 and Ch20 | Issuing authority; enforcing action; financial/route constraints (no conflation) |
| Ch18, Ch33 and Ch47 | What to test; ongoing requalification; execute a model-upgrade release exercise |
| Ch19, Ch35 and Ch39 | Policies/decision rights; accountabilities; change/release implementation |
| Ch21, Ch34, Ch49 and Ch50 | Data requirements; staged retirement; use-case retirement task; Fabric exit rehearsal |
| Ch23 and Ch52 | Prescriptive Atlas pages versus **applied ADR/risk record specimens** |
| Ch53, Ch54, Ch55 and Ch58 | Boundary protocols; technology options; sourced standards; jurisdiction/industry adaptation |

**Missing chapters:** zero justified *new chapter numbers* under the freeze. **Missing full chapters:** 57 standalone manuscripts (56 with only outline, Ch13 with blueprint only), plus Ch16 needing independent production work. **Missing transitions:** nine reader-navigation bridges, all addressable by introductions, summaries and cross-references at existing boundaries.

### Missing content, placed into existing chapters (25 entries)

'''
body+=table(CG,[('gap_id','Gap'),('missing_teaching_element','Content to add'),('existing_chapter_placement','Existing home')])
body+='''
---

## 7. CTO usefulness — every chapter and every source briefing section

The key question is not whether a topic has a chapter; it is whether a CTO or platform lead can **make a better constrained decision or diagnose a real failure** after reading it. For each of the 58 chapter briefs I assessed six planned-value axes. A separate **348-row section-level register** records six content areas per chapter: opening/reader scenario; engineering mechanism; failure and trade-off; decision/default; artefact/navigation; source fitness/verification. The section values are explicitly the *parent-chapter potential relevance* because the unfinished manuscript cannot honestly be given a per-section realised-quality score.

### Scores by book part — potential value, not achieved quality

'''
body+=table(PT,[('part','Part'),('chapters','Ch'),('planned_strategic','Strategic'),('planned_execution','Execution'),('planned_governance','Governance'),('planned_platform','Platform'),('planned_security','Security'),('planned_enterprise_adoption','Adoption')])
body+='''
### Full 58-chapter usefulness scorecard

'''
body+=table(CH,[('chapter','Ch'),('title','Title'),('strategic_value','S'),('execution_value','E'),('governance_value','G'),('platform_engineering_value','P'),('security_value','Sec'),('enterprise_adoption_value','A'),('source_maturity','Source stage')])
body+='''
Legend: **S** Strategic, **E** Execution, **G** Governance, **P** Platform Engineering, **Sec** Security, **A** Enterprise Adoption (all 1–10 potential). Repeated 8s/9s are not claims of completed content. In particular the 58 chapter potential scores cannot be averaged to claim 'CTO utility 9/10': realised usefulness awaits independently completed exercises. See `CHAPTER-BRIEF-SECTIONS-348.csv` for every source section, actual brief text and exact coverage status; headings that were not separately explicit are visibly marked.

### Practical reader validation for each chapter type

- **Orientation/strategy (1–9):** a sponsor can reject an unjustified use case, select a sourcing mode and defend a funding/risk choice with numbers and conditions.
- **Architecture (10–22):** an engineer can identify the exact responsible component, data/control contract, denied path and test evidence; at least one runnable test is preferable.
- **Atlas (23):** a reader can use each of 30 F1 pages in a review without changing its original default or importing unsupported claims.
- **Lifecycle (24–34):** a reviewer can identify entry conditions, required evidence, accountable authority and a valid stop/rework/retire outcome.
- **Operating model (35–40):** a service owner can run an incident, SLO review, change, cost reconciliation or audit reconstruction with unambiguous roles.
- **Playbooks (41–50):** a non-author can complete a bounded task and state pass/fail without reading the author's original design conversation.
- **Reference (51–58):** a reader can look up a fact/term/protocol/decision safely, follow provenance and distinguish current obligation from illustrative guidance.

---

## 8. Publisher readiness — four editorial positions

The following are **likely editorial fit assessments**, not quotes or decisions from any named publisher. Acquisition may start from a proposal and sample chapters; manuscript-production readiness is a separate threshold.

| Publisher | Fit now | Attractive proposition | Probable challenge | Minimal convincing evidence |
|---|---|---|---|---|
| **Apress** | Strongest conditional fit for professional reference and practitioner atlas | Comprehensive enterprise reference plus decision pages and evidence specimens | 58 chapters too broad/expensive; one drafted chapter, unclear how much runnable proof | Scoped book proposal, rights-cleared Ch13 + Ch16 and five-to-ten F1 specimens, sample exercise, clear audience and page plan |
| **O’Reilly** | Conditional; needs compelling teachability | Durable architecture principles, explainable trade-offs, use cases, independent reader value | Book may feel like a catalogue of diagrams; needs distinctive educational progression and practical demonstrations | Cohesive multi-chapter sample, honest practitioner comparisons, reader-tested exercises and clear revision plan |
| **Packt** | Conditional but structurally weaker in current form | Runnable hands-on harness and workshops could serve engineers | This is deliberately *not* a coding tutorial; 58-chapter reference would underserve hands-on expectations | Separate practical companion/labs, runnable repository, bounded build examples |
| **Addison-Wesley Professional** | Aspirational, lower near-term fit | A coherent, durable decision-to-evidence engineering methodology | Calls for deeper argumentation, theory of practice, validation, original contribution and a tighter conceptual story | Independently trialled method, disciplined cases, durable exemplars, significant developmental edit |

Apress is within Springer Nature's professional technology publishing offerings; Springer Nature provides a book idea/proposal and author process, **not** an assurance that this specific project would be acquired. Sources: [Springer Nature author guidance](https://www.springernature.com/gp/authors/publish-a-book), [Book proposal form](https://media.springer.com/full/springer-instructions-for-authors-assets/pdf/SN_BPF_EN.pdf), [Springer Nature imprints](https://www.springernature.com/gp/authors/publish-a-book/making-your-decision). O'Reilly's [submission guidance](https://submission-guides.oreilly.com/book-submissions/) primarily concerns platform content submission; it is **not** evidence of acceptance criteria for this specific book proposal. Any AI-generated material policy and publication rights obligations must be confirmed directly with the intended publisher rather than inferred from third-party internet copies.

### Editorial non-negotiables

Original authored analysis must be distinguished from source quotation and AI-generated text; figures must be rights-cleared; all claims of real deployment/control operation must be evidence-based; numerical estimates must label assumptions; every image needs accessible alt text; frozen Style Bible v1.2 terminology and template gates apply; URLs, product support and protocol version claims require a dated fact check; code/listings and synthetic fixture must have independently runnable validation. Publication readiness cannot be inferred from a complete outline and bibliography.

---

## 9. Industry differentiation — competitors and complements

| Reference | Existing intellectual contribution | Where the book overlaps | Honest possible differentiation | What not to claim |
|---|---|---|---|---|
| TOGAF ADM | Cross-domain architecture method, governance, requirements and change | Architecture views, ownership, phased design, ADRs | Agent-specific execution boundary and connected evidence specimen | Do not claim to invent architecture lifecycle, requirements traceability or governance |
| SAFe | Portfolio funding, agile delivery, architectural runway and coordinated governance | Sponsorship, change gates, release and portfolio scaling | Proof of permission/side effects for agent actions, not agile organisational mechanics | Do not claim SAFe lacks strategic decision governance |
| Team Topologies | Platform-as-a-product, stream-aligned/enabling/platform/complicated subsystem team patterns | Hybrid control/domain ownership; cognitive load and platform products | Explicit mapping of runtime policy and evidence to platform/domain owners | Do not claim novel platform team organisational patterns |
| Platform Engineering literature | Golden paths, shared services, self-service, internal products | Reusable runtime, paved paths, cost/scale and operations | Agent-specific trust boundaries, non-bypassability and evidence-linked release | Do not claim invention of developer platforms or shared controls |
| AI Engineering literature | Retrieval, evaluation, model routing, memory, telemetry, production testing | Nearly all technical mechanisms | Join verified action admission, semantic disagreement and lifecycle obligations in one teaching case | Do not claim individual mechanisms are novel |
| Agentic AI literature | Agent harness, tools, multi-agent patterns, planning and delegated tasks | Runtime loop, models, MCP/A2A, memory, tools | Framing autonomy as continuously evidenced release privilege and explicit refusal/retirement | Do not claim generic agent coordination is original |

TOGAF's ADM is already a repeatable architecture method, while NIST AI RMF already includes Govern/Map/Measure/Manage and documentation practices; any methodological novelty claim must be narrowly framed. SAFe already includes Lean Portfolio Management and governance; Team Topologies explicitly describes four team types and three interaction modes. Sources: [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/), [SAFe](https://framework.scaledagile.com/), [Team Topologies](https://teamtopologies.com/key-concepts/).

**Differentiator that survives scrutiny:** *Decision-to-Evidence Engineering*—as a practical, joined method that asks not just what a decision recommends but how to connect its scope, owner, enforcement, negative tests, evidence record, release and retirement. This is **original synthesis in the book**, not proof the individual ideas were invented here or already validated professionally. The 30 F1 pages and Meridian evidence should be the method's most compact teaching objects.

---

## 10. Missing intellectual assets and remediation priorities

The missing-asset list is restricted to assets needed for a coherent publishable reference and trustworthy teaching—not a new architecture, new governance system or new product roadmap.

'''
body+=table(GA,[('priority','Priority'),('missing_asset','Missing intellectual or publication asset'),('domain','Concern'),('completion_evidence','Acceptance evidence')])
body+='''
### Proposed shortest remediation order — no changes to frozen structure

**Gate A — Prove editorial contract, before high-volume authoring.** Confirm 58 chapter plan, source and permission policy, Style Bible v1.2 production templates, six-axis audience acceptance criteria and F1 one-page restrictions. Repair stale chapter cross-reference **pointers** under editor control without rewriting frozen chapter IDs/defaults. Complete Ch13 F6 and technically rework Ch16 F7, with an independent review and a Meridian source/claim validation run. Deliver a coherent sample before spending months generating manuscripts.

**Gate B — Prove one full explanatory chain.** Complete 30 F1 production pages by transcription/production checks; finish Ch23's application instructions and Ch57's joined specimens. Demonstrate separate policy enforcement success versus behavioural release failure; add a labelled outside-fixture positive read-only case; perform cold-reader testing. This is where technical credibility is won or lost.

**Gate C — Complete intellectual breadth with focused deep dives.** Fill the 25 missing teaching elements inside the appropriate frozen chapters. Prioritise business capability outcomes, physical deployment example, cryptographic delegation/revocation, durable execution, Context and reconciliation, evaluation data, cost per safe task, operations/retirement. Finish the source/citation map and technical comparative examples, with no new layers or decision IDs.

**Gate D — Produce the book.** Write and review all remaining manuscripts to template; finish the ten executable F2/F5 playbooks and reference chapters; obtain independent technical and instructional assessments and full rights/standards fact-check; complete the illustrations, index, cross-references, accessible layout and final publisher proofs.

**Gate E — Submission/acceptance.** Submit a truthful proposal/package and respond to an actual editor's criteria. '10/10 publisher readiness' exists only when the agreed contracted deliverables have passed the publisher's actual process—not when internal reviewers award the work a score.

### Definition of a claimed 10/10

| Dimension | Minimum evidence for a credible 10/10 claim | Present state |
|---|---|---|
| Architecture completeness | All in-scope business, capability, information, data, app, platform, security, technology, governance and operations views explicitly joined; necessary variants and threat/scale tests; independent architectural sign-off | Not met; conceptual/logical stronger than business and physical |
| CTO utility | Non-author CTO/platform leads independently reach defensible build/no-build, sourcing, release, incident and exit decisions using the materials | Not tested |
| Enterprise relevance | Multiple sector/organisation constraints and real/practitioner use, with economics and support outcomes measured | Partly planned; no independent sector adoption evidence |
| Governance coverage | Decisions, approval authority, enforcement, evidence, exception, audit, withdrawal covered with verifiable case studies; rights/standards scoped and reviewed | Design described; independent operational proof absent |
| Educational quality | Complete chapters, prerequisites, progressive exercises, independent novice and expert reader tasks, accessibility and editorial acceptance | Not met; one draft chapter |
| Publisher readiness | Complete contract-compliant manuscript, proofs, permissions, peer reviews and publisher-specific approvals | Not met; no finished manuscript package |

The ambition to reach 10/10 in every dimension is not realistic within a short delivery window. **Near-term success should be defined by passed review gates, not self-assessed perfection.** A high-quality reference book may be publishable without independent production deployments, provided claims are explicitly bounded and examples reproducible.

---

## 11. Revised programme maturity scorecard

These ratings evaluate the **body of knowledge and actual written artefacts**, not the repository branch situation. Numbers are ordinal editorial judgements, with observed evidence shown. A 7/10 conceptual design is not a 7/10 verified implementation.

| Dimension | Specified content /10 | Independently demonstrated /10 | Why it cannot claim 10 now |
|---|---:|---:|---|
| Enterprise architecture completeness | **6** | **2** | Thin business/capability/technology instances and cross-domain proof |
| Reference architecture completeness | **7** | **2** | Coherent E/T/C/L + 8 planes; physical and operational variants not validated |
| CTO utility | **7** potential | **1** | Excellent decisions proposed, but no non-author CTO trial |
| Enterprise relevance | **8** potential | **2** | Enterprise risks and ownership well represented; few independent use cases |
| Governance coverage | **7** | **2** | Role/policy boundaries defined; functioning approvals and negative proofs unverified |
| Educational quality | **5** | **1** | Strong writing plan, one draft, no complete formative assessment series |
| Publisher readiness | **3** | **0** | Proposal draft exists; no accepted manuscript/production proof |
| Methodological reproducibility | **6** | **1** | Applied decision method inferred, independent reproduction not evidenced |
| Synthetic evidence coherence | **8** | **5** | Internally checked six-record Meridian chain, but no production assurance |

**Score discipline:** 'specified' indicates planned intellectual content; 'demonstrated' means inspected source evidence, not external certification. Values should not be added or averaged into an overall readiness percentage. A publisher can commission a proposal ahead of a finished manuscript, but this programme cannot honestly claim a completed v1.0 now.

---

## 12. Final verdict and editorial decision

**Retain the complete frozen architecture, Atlas and 58-chapter plan. Do not add a control plane, make up new decisions, extend Meridian's canonical event chain or start another strategy exercise.** The main intellectual failure risk is *execution*: a technically rich overview that has not yet become a demonstrably usable, evidence-led professional reference.

The programme has three real advantages: explicit control/authority boundaries, an unusually concrete prescriptive decision catalogue, and a single consistent synthetic case that exposes the gap between a denied action and a failed behaviour/release assertion. Those are valuable. They are not sufficient by themselves to claim a standard, a new industry category, assurance certification or a definitive reference book.

**A commissioning editor should proceed only on a carefully scoped, conditional proposal**, with two genuinely strong sample chapters, a sample of the F1 decision pages, print-ready Meridian evidence, and an independent practitioner trial. The most important manuscript question is whether readers can use the Atlas and evidence to make a technically correct decision **without needing the author to interpret the material for them**.

**The next decisive deliverable is a proof-of-book package, not another reference architecture.**

---

## Companion files and audit crosswalk

- `ENTERPRISE-ARCHITECTURE-COVERAGE.csv` — ten domain-level evidence gaps and closure tests.
- `REFERENCE-ARCHITECTURE-VIEW-COVERAGE.csv` — eight views and design/evidence separation.
- `DECISION-ATLAS-30-EDITORIAL-ASSESSMENT.csv` — all thirty frozen IDs, adjacency and non-normative classification.
- `MISSING-DECISION-QUESTIONS-NOT-NEW-IDS.csv` — 19 missing practical decision applications mapped to existing D-IDs.
- `MERIDIAN-LIFECYCLE-COVERAGE.csv` — eleven lifecycle stages plus traceability/evidence completeness.
- `CHAPTER-CTO-USEFULNESS-58.csv` — all 58 chapters with six reader-value dimensions.
- `CHAPTER-BRIEF-SECTIONS-348.csv` — six brief elements per frozen chapter, their source text and assessment scope.
- `BOOK-PART-USEFULNESS-8.csv` — aggregate part-level planned utility; not achieved manuscript quality.
- `MISSING-CHAPTER-CONTENT-NOT-NEW-CHAPTERS.csv` — 25 missing teaching elements placed into existing chapters.
- `TOP-25-INTELLECTUAL-AND-PUBLICATION-GAPS.csv` — ranked critical gaps and acceptance evidence.
- `ENTERPRISE-ARCHITECTURE-COVERAGE-HEATMAP.png`, `CHAPTER-CTO-UTILITY-HEATMAP.png` — visual assessment (judgement scores only).

**No normative document, Decision Atlas item or Meridian event was changed.**
'''
(D/'PHASE-2-INTELLECTUAL-COMPLETENESS-AND-PUBLISHER-READINESS-v1.0.md').write_text(body,encoding='utf-8')
print('Report words:',len(body.split()),'bytes:',len(body.encode()),'tables:',body.count('|---'))

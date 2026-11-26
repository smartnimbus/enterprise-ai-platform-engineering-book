# Chapter 14 — pinned source handoff

State: SOURCE_PREPARATION_COMPLETE / AUTHORING_BLOCKED. Not a new blueprint, ratification or manuscript. Source baseline cc728dbec56190276eb3f25b5f10729c9959ab95. Prompt 5 from 1d7699d1b3f4abc8fe8c2d8e477697c8be2ecc3e.

## Existing contract (verbatim)
```csv
chapter_id,title,part,template,authority_lane,unique_reader_outcome,allowed_scope,disallowed_scope,unique_teaching_contract,existing_expected_artefact,direct_TOC_decisions,catalogue_related_decisions,required_dependency_candidates,existing_cross_references,forbidden_duplicate_zone,canonical_boundary_source,status,acceptance
CH-014,III. Lifecycle,III,Structural/F6,STRUCTURAL_LAYER_F6,Own the Harness and trajectory → design interruption/resume and multi-agent coordination,"Own internal mechanisms of the named layer, input/output contracts and failure paths",Do not create new control planes or take policy decision authority from a plane,Deep Lifecycle layer mechanism in its single technical home,"Harness contract, transition model",D-15; D-16,D-08; D-13; D-15; D-16; D-20; D-27,CH-010,CH-011; CH-012; CH-015; CH-016; CH-036,Architecture/lifecycle/playbook overlap,Development Blueprint / TOC; Phase3 dependency matrix,PROPOSED_EDITORIAL_CONTRACT_NOT_RATIFIED,No frozen source alteration; correct owner/cross references; evidence grade; example must not invent fixture event; independent peer review
chapter,title,purpose_reader_outcome,type_template,narrative_allocation,pages,decision_ids,artefacts
14,III. Lifecycle,Own the Harness and trajectory → design interruption/resume and multi-agent coordination,Structural/F6,5%; ≤150,8,"D-15, D-16","Harness contract, transition model"
```
8 planned pages; Part III narrative 5%, opening only, maximum 150 words. No independently approved Chapter 14 word count found in these pins; do not infer a frozen Ch13 word target. Resolve word budget with editor before drafting. Proposed contract status remains PROPOSED_EDITORIAL_CONTRACT_NOT_RATIFIED.

## Normative decisions — verbatim
- D-15: Default to a single Harness owning the trajectory, checkpoint and bounded step policy, with renewed authorisation on resume.
- D-16: Default to explicit approval for irreversible, financial or sensitive external mutations unless Governance has approved a narrower low-risk envelope.

Required Atlas artefacts: `harness-state-machine.md` and `approval-envelope-and-sla.yaml`. Existing contract: Harness contract, transition model. Development Blueprint adds restart assertions. D-08/D-13/D-20/D-27 are related references only.

## F6 structure
### F6. Layer Chapter Template (Part III structural core)

```
## Chapter N: [Layer name]

[Opening hook — a failure scene.]

### What this layer decides
[One sentence.]

### The mechanism
[The layer's components, in a table, with one paragraph per component group.]

### The interface with adjacent layers
[One paragraph per adjacent layer, naming the boundary and the contract.]

### Failure modes
[Table: failure, cause, symptom, control.]

### Scaling signal
[The metric that drives autoscaling, with the threshold.]

### Anti-patterns
[Two to four anti-patterns using the F4 template.]

### Decisions to make
[Bulleted.]

### Defaults
[Bulleted, matched.]

### Artefacts to produce
[Bulleted.]

### See also
[Cross-references.]
```

## Ownership and boundaries
Lifecycle owns the Harness event loop, trajectory, bounded step policy, checkpoints, pause/resume, multi-agent coordination and escalation. Execution Environment supplies isolated execution and observations; Tooling owns invocation; Context owns permitted inputs and memory; Identity establishes current actor and delegation; Governance owns policy and exceptions; Gateway owns mutable-action admission; Verification owns behavioural assertions and release; Observability owns correlated telemetry. Checkpoint progress does not confer authority. Use C2 Harness and Trajectory definitions; do not use trace as a synonym except OTel trace. Cross-reference CH-010 prerequisite, CH-011/012/015/016/036, Ch13 Context, Ch18 Verification and Ch56 vocabulary. Do not duplicate Part V lifecycle-stage or playbook material.

## Evidence constraints
- MF-REQ-REF-001 / MF-EVT-001: review/prepare only.
- MF-EVT-005–008 / MF-EVD-RC-001: unresolved conflict and escalation.
- MF-EVD-DG-001 / MF-EVT-009: synthetic attenuated chain, no real cryptographic verification.
- MF-EVT-010–012 / MF-EVD-AU-001 / MF-EVD-DN-001: proposed mutation denied, no call or financial mutation; MF-EVT-013 separate synthetic bypass test.
- MF-EVT-014/015 / MF-EVD-RG-001: failed behavioural assertion, blocked promotion, no production deployment, retest not in fixture. Later separate read-only story is not successful retest.
- Machine-readable chronology ends 2027-03-15T14:00:03Z. Development Blueprint's interrupted workflow opening and M4 Week 19 recovery drill are story/design material, not observed fixture events. Restart, stale approval, checkpoint, replay or interruption illustrations must be explicitly hypothetical; no invented fixture ID, completed side effect or recovery receipt.
- Use BP13 teaching lessons as working editorial guidance (consequence, mechanism, authority, evidence interpretation, trade-off), not ratified architecture.

## Exact source pins
- [editorial/style/style-v1.2.md](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/editorial/style/style-v1.2.md) — blob `868b5ff6d4cc9b48ef79bf97a3cfe3e98eac5138`
- [editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md) — blob `0e13eb830819165a3d15218f4b1e8ae235cd6392`
- [publishing/apress/v2/FROZEN-TOC-58.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/publishing/apress/v2/FROZEN-TOC-58.csv) — blob `d5d2553d073eea292f25640877ec89049422d6f8`
- [governance/proposals/knowledge-system/authoring-validation/phase4/CHAPTER-AUTHORING-CONTRACTS-58.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/governance/proposals/knowledge-system/authoring-validation/phase4/CHAPTER-AUTHORING-CONTRACTS-58.csv) — blob `9a5206bae7765824472cb67dada6eaa373222214`
- [governance/proposals/knowledge-system/authoring-validation/phase4/CANONICAL-CONCEPT-OWNERSHIP.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/governance/proposals/knowledge-system/authoring-validation/phase4/CANONICAL-CONCEPT-OWNERSHIP.csv) — blob `7e1a53375309320d0aae9aacf5e6b6900433e705`
- [governance/proposals/knowledge-system/authoring-validation/phase4/VOCABULARY-AUTHORITY-24.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/governance/proposals/knowledge-system/authoring-validation/phase4/VOCABULARY-AUTHORITY-24.csv) — blob `e92ec98ae0e1873b0b337f6a9f825e0cef5d47d2`
- [decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv) — blob `64f5ea77ee6e76ae211149f1ae389f1d38cea729`
- [meridian/fixture/authoring-registry.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/authoring-registry.json) — blob `50e4b38e15e0d3d006f35aef8d24a6f065be0760`
- [meridian/fixture/event-ledger.csv](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/event-ledger.csv) — blob `842d51fd3d768c721dd884c70ee440f0425eb609`
- [meridian/fixture/03-delegation-record.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/03-delegation-record.json) — blob `53fce18c081e75ea2112557bab52fe2a0aea3ea5`
- [meridian/fixture/04-authorisation-receipt.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/04-authorisation-receipt.json) — blob `1aaa8af31a9ab0fa7613b6a8ec95662d39e9b88f`
- [meridian/fixture/05-denied-action-receipt.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/05-denied-action-receipt.json) — blob `2446137413a816794bb968090ac1cfce219f2286`
- [meridian/fixture/06-release-gate-report.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/06-release-gate-report.json) — blob `13829febaa8af01705d1a4937b0e8faaa5e8e050`
- [meridian/fixture/02-reconciliation-record.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/02-reconciliation-record.json) — blob `54854860c550c1a1e7544e115bcb8ca77859ed3a`
- [meridian/fixture/original-request.json](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/cc728dbec56190276eb3f25b5f10729c9959ab95/meridian/fixture/original-request.json) — blob `a4343d45fdeb51af1aa4452fdf103e472792ad52`

Cross-sample continuity: [Ch13 production](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/tree/22ecbf572e885cad992b261fc0b3181c01e654ed/publishing/apress/acquisition-samples), [Ch16 production](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/tree/441dc92902ba26666ba6615af8ae9343baf45322/publishing/apress/acquisition-samples), [working acquisition package](https://github.com/smartnimbus/enterprise-ai-platform-engineering-book/blob/31872adf82758bccf53d50a8c3f10688b5f29df7/publishing/apress/submissions/acquisition-submission-index.md).

## Authoring entry condition
Author/editorial director ratifies CH-014 contract and word budget; independent pilot acceptance recorded for exact sample revisions; qualified orchestration/distributed systems reviewer appointed (role only, no named acceptance). PR7/9/13 open without recorded reviews. Formal lint and proof preflight remain open. Therefore no Chapter 14 manuscript created. Once authorised, canonical target `manuscript/part-03/chapter-14/chapter-14.md`; use existing F6 and evidence map, one chapter in progress.

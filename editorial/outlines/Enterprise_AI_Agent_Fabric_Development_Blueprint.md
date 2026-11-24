# The Enterprise AI Agent Fabric
## Publisher-ready manuscript construction blueprint

**Editorial baseline:** Style Bible `style-v1.2.md`, ratified. **Working edition:** 2026-11-09. **Status:** implementation specification for the book, not a second review.

**Source key:** `B` = `The-Enterprise-AI-Agent-Fabric-Blueprint.md`; `R` = `Agentic-Enterprise-Reference-Architecture.md`; `S` = `style-v1.2.md`; `T` = `transcript.md`. The transcript is a research prompt/inspiration source, not an authoritative account of enterprise deployments or vendor implementations. All proposed Meridian events and quantitative outcomes below are **fictional design specifications**, not observed results.

**Deliverables locked by this plan:** eight parts; 58 numbered chapters; four F6 layer chapters; eight F7 control-plane chapters; 30 individually paginated F1 decisions; 11 lifecycle-stage chapters; ten F2/F5 playbooks; one Meridian narrative spanning the book; complete worked artefacts and reference library. The three promises remain, in order: decision surface, reference architecture, practitioner journey (S A1). The book remains a reference architecture with a narrative spine, not a coding tutorial (S A3–A4).

**Page budget:** approximately 478 pages including about 30 pages of front matter and index. Page estimates below are editorial allocation, not a guaranteed typeset count. The Style Bible's page and narrative ceilings remain production gates.

# Phase 1. Canonical architecture reconciliation

## 1.1 The single normative model

The architecture contains **four structural layers** and **eight control planes**. There is no third architectural tier, ninth control plane, or separate numbered layer stack. ETCLOVG is a mnemonic covering E/T/C/L plus Observability/Verification/Governance, not an additional taxonomy.

**Four structural layers, numbered E/T/C/L, in execution order:**

| Code | Structural layer | Owns | Boundary contract | Evidence |
|---|---|---|---|---|
| E | Execution Environment | Isolated workers, compute, sandboxing, resource limits, filesystem/network constraints, teardown, resumption infrastructure | Accepts an authorised workload envelope from L; returns execution result and measured usage | Workload attestation, quota/termination log, isolation test |
| T | Tooling | Tool catalogue, schema binding, protocol adapters, idempotency contract, invocation adapter and result normalisation | Receives a tool intent from L and an authorisation decision from Gateway; calls only registered tools | Tool-schema version, request/response receipt, side-effect receipt |
| C | Context | Intake normalisation, ACL-filtered retrieval implementation, context assembly, canonical entity IDs, semantic reconciliation, working/episodic/semantic memory, provenance | Reads or writes context under Identity and Data Protection policy; passes provenance-bearing context to L | Context manifest, source lineage, reconciliation and memory-write ledger |
| L | Lifecycle | Harness, event loop, plan/step budget, agent and persona lifecycle, checkpoints, multi-agent coordination, escalation, interruption and resume | Invokes E/T/C; cannot create authorisation; supplies execution intent and delegation references to the control-plane enforcement points | Trajectory, step budget report, checkpoint transitions, completion record |

**Eight control planes, all cross-cutting:**

| Control plane | Singular design accountability | Runtime enforcement / evidence | Does not own |
|---|---|---|---|
| Identity | Human, agent, tenant and delegated identities; claims issuance and attenuation | Issued actor-chain token; entitlement decision inputs; expiry/revocation | Application business approval or gateway transport |
| Gateway | Admission, model/tool/agent routing policy, protocol termination, egress and mandatory side-effect enforcement | Tool/model/A2A policy enforcement point; decision receipt; deny-path test | Credential issuance, enterprise policy authorship, tool business logic |
| Observability | Collection and correlation of telemetry; trajectories, metrics and incident signals | Correlated event stream, SLO report, retention-class metadata | Release-quality verdict, policy decision |
| Verification | Behavioural assertions, evaluations, integrity checks, release and runtime verification gates | Assertion report, evidence grade and signed release-gate result | Business risk appetite, audit retention policy |
| Governance | Autonomy classes, accepted risk, exception and approval authority, ownership, review and change policy | Policy bundle, approval record, waiver/expiry, attestation | Inline routing, token minting, evaluator implementation |
| FinOps | Cost allocation rules, budgets, unit economics, pricing assumptions and financial exceptions | Budget decision, cost ledger and forecast/reconciliation | Gateway execution of routing or resource metering |
| Data Protection | Data classification, consent handling, residency, retention, deletion and encryption rules | Classification decision, access/write/delete proofs, residency verification | Identity issuance, semantic conflict resolution |
| Interoperability | Protocol selection, version contract, compatibility and event semantics across boundaries | Versioned protocol registry, conformance report, mapping record | Gateway network proxy operation, Context's business entity resolution |

**Concrete runtime path:** user/channel → Identity tenant and delegation resolution → Governance policy and Data Protection classification → L Harness → C context read/assembly → model route and Gateway policy → E isolated work when required → T tool invocation via Gateway enforcement → C governed memory write → Verification behavioural assertions → Observability correlated evidence → completed or escalated outcome. Control decisions are enforced at multiple policy enforcement points; the Gateway must be unavoidable for *mutable external actions*, not a physically central process through which every internal memory read flows.

**Separation of duties:** Governance decides *which action is permitted in principle*; Identity establishes *who may request it and under what delegation*; Gateway admits/denies the specific call; Tooling performs the authorised call; Verification establishes *whether the behaviour met its assertions*; Observability records *what happened*. Evidence joins on `run_id`, `tenant_id`, `actor_chain_id`, `policy_decision_id`, `action_id` and `artefact_version`.

## 1.2 ETCLOVG and semantic-context disposition

| Existing label | Canonical meaning | Rule for manuscript |
|---|---|---|
| ETCLOVG E/T/C/L | Four structural layers | Capitalise the named Structural Layer; use F6 for each |
| ETCLOVG O/V/G | Observability, Verification, Governance Control Planes | Use F7; the mnemonic does not exclude the other five planes |
| Semantic Context Plane | Semantic context **services within C** | Not a ninth plane. C owns entity resolution, conflict handling, and provenance-bearing context; Interoperability owns inter-system schema compatibility; Governance owns authoritative-source selection; Verification validates reconciliation behaviour |
| Security Plane | Security controls distributed among Identity, Gateway, Governance, Data Protection, E and T | Security is an assurance perspective and threat model, **not** a ninth plane |
| Evaluation Plane | Verification Control Plane | `Evaluation` names a verification activity or method, never a ninth plane |
| Agent Gateway, MCP gateway, model gateway, network gateway | Enforcement components governed by the Gateway Control Plane | Distinguish configured policy/control plane from deployed gateways and proxies |
| Delegation chain | Identity-issued, audience-bound, attenuated chain | Gateway validates chain at each external action; Governance defines required approval; Observability records chain; L can request delegation but cannot extend privilege |
| 15 numbered runtime positions (-1 to 13) | Legacy engineering inventory, not normative architecture | Retain as appendix crosswalk only; remove “Layer -1” and “Layer 13” as first-class structural terms |

**Identity proof contract:** `human_subject`, `agent_workload_id`, `tenant_id`, `persona_id`, `archetype_id`, `delegator`, `delegatee`, `purpose`, `allowed_actions`, `resource_scope`, `audience`, `issued_at`, `expires_at`, `parent_chain_hash`, `chain_signature`. No hop expands `allowed_actions` or `resource_scope`; the effective scope is the intersection of all prior grants and the current tenant policy. Revocation must propagate to queued and resumed work. Tokens are checked before side effects, not only at session creation.

**Mutable-action gate:** a side-effecting tool declares `risk_class`, `side_effect_type`, `idempotency_key`, `approval_required`, `resource_scope` and `compensation_strategy`. Gateway rejects calls without a valid scoped actor chain and live policy receipt. A tool adapter cannot send traffic directly to an external endpoint. Enforce through credentials, egress rules, service identities, and negative bypass tests. Failed or unavailable policy decision paths fail closed; low-risk read-only queries can use an explicitly approved degraded mode.

## 1.3 Terminology lock

The C2 definitions are mandatory: **Fabric, Use case, Agent, Persona, Archetype, Structural layer, Control plane, Tenant, Harness, Trajectory, Behavioural assertion**. Use these terms precisely; avoid prohibited synonyms in normative prose. The following are supplemental defined terms, not C2 replacements.

| Additional term | Controlled definition |
|---|---|
| Workload envelope | Signed input to L/E containing tenant, actor chain, budgets, risk class and deadline |
| Action authorisation receipt | Gateway decision tied to an action, policy version, actor chain and expiry |
| Context manifest | Versioned index of retrieved sources, entity IDs, timestamps and policy classes |
| Memory write receipt | Provenance and retention record for one durable context mutation |
| Evidence envelope | Correlated records proving authorisation, execution and verification for one trajectory |
| Autonomy envelope | Allowed tools, risk classes, approvals, limits, and escalation conditions for one use case |
| Policy enforcement point (PEP) | A deployed interceptor that executes decisions issued by the owning Control Plane |
| Fabric product | The independently owned business-facing capability that uses the shared Fabric; it is not a synonym for the Fabric |
| Tenant substrate | Isolation implementation for identity, context, state, evidence and cost attribution |

## 1.4 Ownership and escalation model

| Deliverable or decision | Accountable role | Responsible delivery | Required counter-sign |
|---|---|---|---|
| Fabric product strategy and funded service catalogue | Sponsor / Fabric product owner | Platform lead | Domain lead, FinOps lead |
| E, T, C, L implementation | Platform lead | Layer engineering owners | Security for risk-bearing boundaries |
| Human, workload, and delegation identity | Security architect | IAM/workload identity team | Platform lead |
| Gateway enforcement and bypass-proof | Security architect | Gateway/platform engineering | SRE lead |
| Semantic context contract and source-of-truth decisions | Platform lead | Context engineer and domain data owner | Domain lead; Data Protection for personal data |
| Verification assertion thresholds and release gates | Domain lead for task correctness; Security architect for safety controls | Evaluation engineers | Platform lead; Governance if autonomy increases |
| Governance policy and autonomy exceptions | Sponsor-delegated risk authority | Governance/risk team | Security architect; domain owner |
| Telemetry, SLOs, continuity and incident command | SRE lead | Operations team | Security architect on security incidents |
| Cost allocation and budget exceptions | FinOps lead | Finance operations | Sponsor for exceptional spend |
| Protocol contract and version acceptance | Platform lead | Interoperability engineer | Security architect where trust boundaries change |
| Retirement, retention and deletion evidence | Business owner | Platform and Data Protection teams | Security architect; records owner |

**Escalation:** unresolved semantic ownership → domain data owner → governance forum; disputed policy exception → security architect and sponsor-delegated risk authority; exceeded budget → FinOps lead then sponsor; release-gate failure → Verification owner blocks promotion; on-call incidents → SRE incident commander. No sponsor waiver silently bypasses statutory retention or security controls.

## 1.5 Old-to-new architecture crosswalk

| Legacy R section | Old heading | New primary location | Cross-cutting owner / retained material |
|---|---|---|---|
| R 11 | User, channel and intent | Ch14 L / Ch3 | Identity; intake/auth/session |
| R 12 | Identity, consent, policy context | Ch15 Identity | Governance; Data Protection; tenant proof |
| R 13 | Model interface and transport | Ch12 T | Ch16 Gateway; model adapter and retry controls |
| R 14 | Input normalisation and ingestion | Ch13 C | Ch21 Data Protection; source validation |
| R 15 | Knowledge and retrieval | Ch13 C | Ch21 ACL/retention; retrieval evidence |
| R 16 | Prompt and context assembly | Ch13 C | Ch18 Verification; context-budget contract |
| R 17 | Reasoning and planning | Ch14 L | Ch19 Governance; autonomy envelope |
| R 18 | Tool and action interface | Ch12 T | Ch16 Gateway; idempotent actions |
| R 19 | Execution sandbox | Ch11 E | Ch21 Data Protection; isolation evidence |
| R 20 | Reflection and guardrail | Ch14 L | Ch18 Verification; pre-commit assertions |
| R 21 | Memory and state; 21.1 | Ch13 C | Ch21 Data Protection; Ch17 Observability; retain full memory-depth material |
| R 22 | Multi-agent orchestration | Ch14 L | Ch15 Identity; signed handoff and attenuation |
| R 23 | Output composition and grounding | Ch13 C | Ch18 Verification; citation correctness |
| R 24 | Evaluation and feedback | Ch18 Verification | Ch39 release and Ch33 improvement |
| R 25 | Operations and lifecycle | Ch14 L and Ch36–40 | Ch17 Observability; operational procedures |
| R 25A | Identity and Delegation Plane | Ch15 Identity | Normative identity-control chapter |
| R 25B | Agent Gateway Plane | Ch16 Gateway | Normative gateway-control chapter |
| R 25C | Semantic Context Plane | Ch13 C | Rename to `Semantic context services`; no plane |
| R 26 | Security Plane | Ch15/16/19/21 | Threat coverage integrated across eight planes |
| R 27 | Governance Plane | Ch19 Governance | Authoritative policies and approvals |
| R 28 | Observability Plane | Ch17 Observability | Metrics, telemetry and evidence correlation |
| R 29 | Evaluation Plane | Ch18 Verification | Test method and runtime/release gates |
| R 30 | Cost and FinOps Plane | Ch20 FinOps | Cost policy and allocation |
| R 31–32 | Interoperability/standards | Ch22 + Ch53 | Normative protocol choice and versioned reference entries |
| R 33 | Data Protection and Compliance Plane | Ch21 Data Protection | Protection controls, separate governance authority |
| R 34–40 | Trust, threat and RAG | Ch13, 15–22, 27 | Explicit threat mapping, RAG lifecycle and proof |
| R 41–50 | Operating lifecycle/build choices | Ch5–9, 24–40 | Merge into lifecycle, business and change chapters |
| R 51–59 | Playbooks, checks, matrices, evidence | Ch41–58 | Populate rather than list matrices only |
| B Ch1–9 | Orientation and strategy | Ch1–9 | Preserve initial progression; expand decisions |
| B Ch10–15 | Tiered architecture | Ch10–22 | Split F6/F7 chapters; remove tier-3 taxonomy |
| B Ch16–18 | Decision map, ADR and anti-patterns | Ch23 + relevant chapters/Ch52 | Thirty one-page F1 entries; anti-patterns in F4 |
| B Ch19–29 | Stages 0–10 | Ch24–34 | One E1 chapter per stage |
| B Ch30–35 | Operating model | Ch35–40 | Six operational chapters |
| B Ch36–45 | P1–P10 | Ch41–50 | F2/F5 chapters |
| B Ch46–53, Appendix A | References and memory | Ch51–58 + Ch13 | Concise reference entries; memory in normative C chapter |

**Editorial renumbering instruction:** every hard-coded chapter reference in S A2, H1, F9–F11 and I3 must be regenerated against this final TOC before typesetting. This does not change an architectural/style rule. Record the cross-reference renumbering in the editorial decisions log as `ED-018`, with a source-to-destination map and editor approval. Protocol examples in S C5 are illustrative, not permission to invent an unverified version.

**Affected new chapters:** Ch10–22 directly; Ch2, 5–9, 23, 26–29, 32–40 and 41–58 by dependency. No chapter may use a superseded ninth plane.

# Phase 2. Revised complete table of contents

## Front matter

Title and subtitle; copyright and fictional-scenario disclaimer; practitioner promise; audience/reading paths; Figure 0-1 chapter dependency map; terminology quick card; how the decision pages work; architecture-at-a-glance; list of figures/tables. The index follows Part VIII.

**Template key:** `O` = E1 adapted to conceptual opening/closing; `S` = E1 strategy; `F6` = exact structural-layer template; `F7` = exact control-plane template; `F1×30` = thirty identical decision pages; `L` = E1 lifecycle plus stage contract; `OP` = E1 operating chapter; `F2/F5` = exact playbook/war-story templates; `REF` = F3/F8/F9/F10/F11 as applicable. Every non-F1 chapter retains E4 closing blocks. In Part IV each decision page follows F1, not a generic E1 chapter. `Narrative` gives the E5 part allocation and the absolute per-chapter ceiling; the ceiling wins during editing. The stated percentage is the Style Bible's compositional intent, not permission to exceed its vignette cap.

| Ch | Part and chapter title | Purpose → reader outcome | Type/template | Narrative | Pages | Key decisions | Key artefacts |
|---|---|---|---|---|---:|---|---|
| 1 | I. The Case for a Shared Fabric | Establish the repeat-use-case problem → identify shared economics/control triggers | O | 40%; ≤400 words | 9 | D-01 | Fabric opportunity brief |
| 2 | I. Agent Capability, Autonomy and Risk | Tie capabilities to permitted actions → classify autonomy envelope | O | 40%; ≤400 | 9 | D-05, D-16 | Autonomy classification card |
| 3 | I. Fabric, Product, Use Case and Tenant | Draw ownership boundaries → assign responsibility without ambiguity | O | 40%; ≤400 | 9 | D-06, D-04 | Responsibility boundary map |
| 4 | I. When Not to Build a Fabric | Identify disqualifying conditions → choose an alternative | O | 40%; ≤400 | 9 | D-01, D-02 | No-fabric decision memo |
| 5 | II. Build, Buy, Embed or Partner | Compare acquisition patterns → defend a reversible choice | S | 30%; ≤300 | 11 | D-02 | Sourcing option appraisal |
| 6 | II. Central, Federated or Hybrid Ownership | Allocate authority → choose team structure and exception path | S | 30%; ≤300 | 11 | D-03, D-06 | Operating-model ADR |
| 7 | II. Tenant Isolation and Sovereignty | Select isolation model → name mandatory data and identity boundaries | S | 30%; ≤300 | 11 | D-04, D-25 | Tenant isolation ADR |
| 8 | II. Model Strategy and Unit Economics | Design route and fallback policy → justify spend/performance bounds | S | 30%; ≤300 | 11 | D-17, D-26 | Routing policy and cost model |
| 9 | II. Earned Autonomy and Sponsorship | Specify promotion criteria → fund only evidenced autonomy | S | 30%; ≤300 | 11 | D-05, D-16, D-23 | Autonomy promotion charter |
| 10 | III. The Canonical Fabric Architecture | Lock E/T/C/L plus eight planes → trace a request and its evidence | Architecture overview/E1 | 5%; ≤150 | 8 | D-07, D-18 | Layer stack, ownership diagram |
| 11 | III. Execution Environment | Isolate work → specify sandbox and quota contracts | Structural/F6 | 5%; ≤150 | 8 | D-07, D-08 | Workload envelope and isolation profile |
| 12 | III. Tooling | Make tool invocation typed and bounded → implement action contracts | Structural/F6 | 5%; ≤150 | 8 | D-09, D-10 | Tool contract and invocation receipt |
| 13 | III. Context | Govern retrieval, memory and meaning → specify provenance and contradiction handling | Structural/F6 | 5%; ≤150 | 8 | D-11–14 | Context manifest, memory policy |
| 14 | III. Lifecycle | Own the Harness and trajectory → design interruption/resume and multi-agent coordination | Structural/F6 | 5%; ≤150 | 8 | D-15, D-16 | Harness contract, transition model |
| 15 | III. Identity Control Plane | Constrain actors/delegation → verify non-expanding authority | Control/F7 | 5%; ≤150 | 6.5 | D-19, D-20 | Actor-chain schema and tests |
| 16 | III. Gateway Control Plane | Enforce each mutable external action → prove non-bypassability | Control/F7 | 5%; ≤150 | 6.5 | D-10, D-18 | Policy receipt and bypass test |
| 17 | III. Observability Control Plane | Correlate events and outcomes → reconstruct trajectories | Control/F7 | 5%; ≤150 | 6.5 | D-24 | Evidence envelope and telemetry map |
| 18 | III. Verification Control Plane | Gate behaviours and releases → specify assertions/evidence | Control/F7 | 5%; ≤150 | 6.5 | D-22, D-23 | Evaluation suite and gate report |
| 19 | III. Governance Control Plane | Establish risk decision rights → govern exceptions and autonomy | Control/F7 | 5%; ≤150 | 6.5 | D-05, D-29 | Risk charter and policy ledger |
| 20 | III. FinOps Control Plane | Govern budgets/chargeback → attribute cost per successful task | Control/F7 | 5%; ≤150 | 6.5 | D-26 | Allocation ledger and unit-economics card |
| 21 | III. Data Protection Control Plane | Protect personal/regulated data → prove retention and deletion | Control/F7 | 5%; ≤150 | 6.5 | D-25, D-30 | Data classification and deletion proof |
| 22 | III. Interoperability Control Plane | Version boundary contracts → accept or reject protocol changes | Control/F7 | 5%; ≤150 | 6.5 | D-21 | Versioned boundary map, conformance record |
| 23 | IV. The Fabric Decision Atlas | Make every major choice reproducible → complete 30 decision pages | F1×30 | 0% | 30 | D-01–30 | Thirty F1 pages and ADR links |
| 24 | V. Stage 0: Strategic Intent | Establish demand and alternatives → authorise or stop discovery | Lifecycle/L | 50%; ≤600 | 5 | D-01–03 | Strategic intent brief |
| 25 | V. Stage 1: Fabric Vision | Define product and success criteria → approve measurable scope | Lifecycle/L | 50%; ≤600 | 5 | D-05–06 | Vision charter |
| 26 | V. Stage 2: Reference Architecture | Specify topology/control contracts → approve baseline | Lifecycle/L | 50%; ≤600 | 5 | D-07–15, D-18 | Baseline architecture pack |
| 27 | V. Stage 3: Trust Chain and Security | Threat-model runtime and delegation → accept bounded risk | Lifecycle/L | 50%; ≤600 | 5 | D-10, D-19–21, D-25 | Threat register and abuse tests |
| 28 | V. Stage 4: Tenant Substrate | Build isolation and context partitions → evidence no cross-tenant leak | Lifecycle/L | 50%; ≤600 | 5 | D-04, D-11–14 | Tenant readiness certificate |
| 29 | V. Stage 5: Shared Services Bootstrap | Stand up gateway, observability and verification → pass control smoke tests | Lifecycle/L | 50%; ≤600 | 5 | D-17–18, D-22, D-24 | Platform smoke-test bundle |
| 30 | V. Stage 6: First Use Case | Onboard a bounded use case → make a go/no-go decision | Lifecycle/L | 50%; ≤600 | 5 | D-05, D-16, D-23 | Pilot release dossier |
| 31 | V. Stage 7: Scale to Twelve Use Cases | Enforce onboarding archetypes → expand without policy drift | Lifecycle/L | 50%; ≤600 | 5 | D-04, D-29 | Onboarding catalogue and exceptions |
| 32 | V. Stage 8: Operate as a Product | Institute SLOs/on-call/chargeback → evidence service ownership | Lifecycle/L | 50%; ≤600 | 5 | D-26–28 | Product service contract |
| 33 | V. Stage 9: Continuous Verification | Detect regression and requalify → sustain earned autonomy | Lifecycle/L | 50%; ≤600 | 5 | D-22–23 | Requalification report |
| 34 | V. Stage 10: Retirement | Retire a use case and plan Fabric exit → preserve/delete records correctly | Lifecycle/L | 50%; ≤600 | 5 | D-30 | Retirement certificate |
| 35 | VI. Team Design and Responsibility Matrix | Name owners and deputies → resolve every handoff | Operational/OP | 10%; ≤200 | 9 | D-03, D-06, D-29 | RACI and service catalogue |
| 36 | VI. Reliability, Service Levels and Continuity | Define error budgets and recovery → test a service tier | Operational/OP | 10%; ≤200 | 9 | D-27 | SLO book, recovery drill |
| 37 | VI. Incident Command and Security Response | Contain bad actions → assign incident command and evidence custody | Operational/OP | 10%; ≤200 | 9 | D-28 | Incident runbook and case record |
| 38 | VI. Unit Economics, Showback and Chargeback | Attribute usage and value → reconcile unit economics | Operational/OP | 10%; ≤200 | 9 | D-26 | Chargeback rules and forecast |
| 39 | VI. Release, Change and Version Control | Control prompts/tools/models/policies → prevent unreviewed production change | Operational/OP | 10%; ≤200 | 9 | D-21–23, D-29 | Change record, rollback plan |
| 40 | VI. Audit Evidence and Assurance Reviews | Reconstruct permission, action and outcome → produce audit-ready evidence | Operational/OP | 10%; ≤200 | 9 | D-20, D-24, D-30 | Evidence chain and review pack |
| 41 | VII. P1: Build the Business Case | Execute sourcing and financial appraisal → obtain funding gate | F2/F5 | 25%; 150–300 | 7 | D-01–03, D-26 | Business case + ADR |
| 42 | VII. P2: Design the Reference Architecture | Apply structural/control contracts → obtain design approval | F2/F5 | 25%; 150–300 | 7 | D-07–22 | Architecture baseline + threat map |
| 43 | VII. P3: Stand Up the Tenant Substrate | Provision and test tenant partitions → sign isolation proof | F2/F5 | 25%; 150–300 | 7 | D-04, D-11–14, D-25 | Tenant readiness dossier |
| 44 | VII. P4: Onboard the First Use Case | Register/verify/release use case → approved production pilot | F2/F5 | 25%; 150–300 | 7 | D-05, D-16, D-23 | Pilot release record |
| 45 | VII. P5: Scale from One to Ten Use Cases | Template onboarding and cost policy → controlled portfolio | F2/F5 | 25%; 150–300 | 7 | D-06, D-26, D-29 | Onboarding factory report |
| 46 | VII. P6: Plan for Ten to One Hundred-Plus | Capacity and isolation stress-test → scale/no-scale plan | F2/F5 | 25%; 150–300 | 7 | D-08, D-27, D-29 | Scale stress-test report |
| 47 | VII. P7: Execute a Model Upgrade | Compare candidate with baseline → gated canary or rollback | F2/F5 | 25%; 150–300 | 7 | D-17, D-22–23 | Upgrade approval or rollback report |
| 48 | VII. P8: Handle a Security Incident | Contain, preserve and recover → verified safe resumption | F2/F5 | 25%; 150–300 | 7 | D-10, D-20, D-28 | Incident evidence packet |
| 49 | VII. P9: Retire a Use Case | Revoke access and dispose data → audited use-case retirement | F2/F5 | 25%; 150–300 | 7 | D-30 | Use-case retirement certificate |
| 50 | VII. P10: Retire or Replace the Fabric | Move/terminate tenants and preserve obligations → executable exit | F2/F5 | 25%; 150–300 | 7 | D-02, D-27, D-30 | Fabric exit plan and rehearsal evidence |
| 51 | VIII. Layer and Control-Plane Checklists | Enable evidenced inspection → verify all 12 architecture units | Reference/F3 | 0% | 7 | D-07–25 | Twelve C-X checklists |
| 52 | VIII. Architecture Decision and Risk Records | Supply accepted templates → produce a complete ADR and exception | Reference/F8 | 0% | 7 | D-01–30 | ADR-001, risk record |
| 53 | VIII. Protocol and Boundary Reference | Locate versioned protocols → choose and check contracts | Reference/F10 | 0% | 7 | D-09, D-21 | Protocol registry and boundary map |
| 54 | VIII. Technology Decision Matrix | Compare implementation categories without endorsement → evaluate alternatives | Reference/matrix | 0% | 7 | D-02, D-07, D-17 | Scoring matrix and evidence register |
| 55 | VIII. Standards and Regulatory Map | Map named standards to controls → prepare compliance crosswalk | Reference/F11 | 0% | 7 | D-19, D-25, D-28 | Standards mapping table |
| 56 | VIII. Glossary and Controlled Vocabulary | Find exact meanings → eliminate synonym drift | Reference/F9 | 0% | 7 | All | Indexed glossary |
| 57 | VIII. Worked Evidence and Delivery Artefacts | Inspect full specimens → reproduce usable records | Reference/specimens | 0% | 7 | D-20, D-23, D-30 | Release, incident, delegation, deletion specimens |
| 58 | VIII. Industry Adoption Overlays | Translate constraints to sectors → adapt risk and data choices | Reference/overlay | 0% | 7 | D-01, D-04, D-25 | Banking, insurance, health, public, retail, manufacturing overlays |

**Budget calculation:** Parts I–VIII = 36 + 55 + 92 + 30 + 55 + 54 + 70 + 56 = **448 pages**. Front matter, endnotes, index and production allowances = **about 30 pages**. Total **about 478 pages**. The 30 F1 decision pages are exactly one page each. The twelve F6/F7 architecture units remain within D2 depth ceilings and floors.

# Phase 3. Meridian Financial story design

## 3.1 Fictional setting and cast

Meridian Financial is fictional: 12,000 employees in retail banking, insurance and wealth management; a UK-regulated group with FCA/PRA responsibilities and GDPR-scoped data. Its beginning is four uncoordinated agent pilots and no shared tenant substrate. Its ending is one running Fabric, 12 live use cases across three tenant-isolation types, and one external SaaS pilot connected under policy. All dates, characters, incidents, dialogue and results are invented for the book. Never portray simulated evidence as a real bank's production results.

| Character | Role / responsibility | Motivation | Recurring conflict | Decisions influenced |
|---|---|---|---|---|
| Eleanor Price | Group COO, executive sponsor; investment, risk appetite and go/no-go decisions | Reduce duplicated work without taking unbounded regulatory exposure | Speed versus verifiable control; funding a shared service without owning domain outcomes | D-01–03, D-05–06, D-26, D-29 |
| Maya Shah | Platform lead; architecture, team, tenancy and Fabric product lifecycle | Replace fragmented pilots with a supportable substrate | Domain autonomy versus shared contracts; urgency versus architecture debt | D-03–04, D-07–18, D-21, D-29 |
| Ruth Mercer | Security architect; identity, threat model, control-plane enforcement and incident approval | Prevent privilege expansion and data egress | Central visibility versus domain-specific exceptions; rapid release versus proof | D-05, D-10, D-16, D-18–21, D-25, D-28 |
| Tomas Reed | Retail banking domain lead; use-case owner, task assertions and operational outcomes | Deliver accurate, timely customer-service outcomes | Customer-service speed versus approvals and retrieval quality | D-05–06, D-11–16, D-22–23, D-29 |
| Samir Khan | SRE lead; on-call, SLOs, queues, recovery and incidents | Make agent workloads bounded and recoverable | Latency/cost targets versus safe shutdown and checkpoint integrity | D-07–08, D-15, D-24, D-27–28 |
| Priya Nair | FinOps lead; budget policy, cost allocation, forecast and value case | Show cost per successful task and funded growth | Sponsor's portfolio growth versus hidden model/tool costs | D-02, D-17, D-26–27 |

No vignette names more than three characters. Conflict is between legitimate duties, never a villain. Use third-person past for vignettes and end with the named artefact. The external SaaS pilot is not credited with controls Meridian has not verified.

## 3.2 Timeline and chapter placement

| Story time | Event, consequence and decision | Architecture evolution | Chapters | Artefact anchor |
|---|---|---|---|---|
| M0 / Week 1 | Four pilots produce inconsistent answers and unowned tool credentials; Eleanor requests inventory | No Fabric yet | 1, 3, 24, 41 | Fragmentation register |
| M0 / Week 2 | Retail domain proposes a fifth custom pilot; Maya requires alternative appraisal | D-01/D-02 go/no-go | 4–6, 24, 41 | Sourcing ADR |
| M1 / Week 4 | Finance finds duplicate model subscriptions and no per-use-case costs | Showback defined before routing | 8, 20, 38 | Cost baseline |
| M1 / Week 5 | Ruth discovers a tool credential usable outside the submitting use case | Actor-chain and Gateway gate become mandatory | 2, 15–16, 27, 42 | Identity threat record |
| M2 / Week 7 | A sample retail case retrieves an insurance record after an incorrect tenant tag | Three tenant types; ACL negative test | 7, 13, 21, 28, 43 | Tenant boundary proof |
| M2 / Week 8 | Two sources disagree on a customer's product status; the agent cannot choose safely | Semantic context services; unresolved conflict escalates | 13, 18, 28 | Reconciliation case record |
| M2 / Week 9 | A pilot's delegated agent tries to expand a refund permission | Signed scope attenuation and gateway refusal | 12, 14–16, 27 | Denied-action receipt |
| M3 / Week 11 | Pilot release misses its behavioural assertion on conflicting documents | Verification gate blocks promotion | 9, 18, 30, 44 | Gate-failure report |
| M3 / Week 12 | Tomas narrows pilot to read-only payment-dispute triage; the new gate passes | First bounded production use case | 30, 44 | Pilot release dossier |
| M3 / Week 14 | A vendor model change degrades tool argument selection | Version-pinned canary and rollback | 18, 22, 33, 39, 47 | Model upgrade ADR |
| M4 / Week 16 | Work queue grows but CPU remains stable; retries amplify provider cost | Queue-age scaling and step budgets | 11, 14, 20, 32, 36 | Saturation and cost report |
| M4 / Week 18 | A poisoned knowledge item requests an unauthorised external call; it is denied, but memory is quarantined | Context write gate, egress denial and incident evidence | 13, 16–18, 21, 37, 48 | Security incident packet |
| M4 / Week 19 | An outage interrupts long-running work; stale delegation is revoked before resume | Checkpoint integrity plus renewed actor chain | 14–15, 32, 36 | Recovery drill report |
| M5 / Week 22 | Five domain teams demand divergent onboarding rules | Archetype catalogue and exception expiry | 6, 19, 31, 35, 45 | Onboarding standard |
| M5 / Week 24 | Ten use cases live; Priya reports cost per successful task rather than token spend alone | Portfolio service and cost governance | 20, 31, 38, 45 | Unit-economics ledger |
| M6 / Week 26 | Two further use cases and a SaaS pilot pass control gates | 12 live use cases, three tenant types, one external SaaS pilot | 22, 31, 46, 53 | Portfolio attestations |
| M6 / Week 27 | Legacy pilot replaced; source memory and credentials must be disposed of | Use-case retirement with deletion proof | 21, 34, 40, 49 | Retirement certificate |
| M6 / Week 28 | Sponsor asks whether the Fabric itself could be replaced; team runs a rehearsal, not a shutdown | Documented exit route, Fabric remains live | 34, 36, 50 | Fabric exit rehearsal |

**Story-state continuity rules:** the 12-use-case endpoint counts only live use cases; the retired legacy pilot is outside that number. The Fabric does not shut down by the end. The 100-plus scale playbook is a *capacity design exercise*, not a claim that Meridian reached 100 uses. Time labels are relative to the fictional case chronology, not a claim about the manuscript's six-month writing schedule.

## 3.2.1 Meridian's end-state portfolio (synthetic)

**Tenant profiles:** `TP-A` = pooled compute with strictly scoped identity, context and evidence; `TP-B` = pooled compute with separate data, key and audit domains; `TP-C` = dedicated execution/data boundary with explicit cross-system admission. These are isolation profiles, not three actual customer tenants. Individual tenant IDs and data-owner assignments remain mandatory.

| Use-case ID | Business unit | Governed task | Tenant profile | Autonomy limit at book end |
|---|---|---|---|---|
| MF-UC01 | Retail banking | Payment-dispute triage | TP-B | Read-only triage and human-reviewed recommendation |
| MF-UC02 | Retail banking | Branch procedure retrieval | TP-A | Read-only response with citations |
| MF-UC03 | Retail banking | Customer-letter drafting | TP-B | Draft only; human sends |
| MF-UC04 | Retail banking | Transaction-query summarisation | TP-B | Read-only with customer data access checks |
| MF-UC05 | Retail banking | Internal service-ticket categorisation | TP-A | Automated internal categorisation; no external mutation |
| MF-UC06 | Insurance | Claims-document intake | TP-B | Classification and human-reviewed submission |
| MF-UC07 | Insurance | Policy coverage search | TP-A | Read-only source-backed lookup |
| MF-UC08 | Insurance | Non-sensitive document classification | TP-A | Bounded internal metadata write |
| MF-UC09 | Insurance | Renewal case preparation | TP-C | Case draft only; no binding decision |
| MF-UC10 | Wealth management | Approved research summarisation | TP-A | Research summary, not personalised advice |
| MF-UC11 | Wealth management | Compliance document extraction | TP-A | Internal extraction; human verifies |
| MF-UC12 | Wealth management | External SaaS client-service pilot | TP-C | Read-only pilot, external protocol gateway controls |

**Portfolio reconciliation:** twelve live use cases, split `TP-A = six`, `TP-B = four`, `TP-C = two`; five retail, four insurance, three wealth. The external SaaS pilot (MF-UC12) is *included* within the twelve. The legacy fragmented pilot retired in P9 is not one of the twelve. Every figure and table involving totals must use this register.


## 3.3 Narrative distribution and production rules

- **Part I:** four short openings. Start with failed inventory, autonomy ambiguity, ownership dispute and the stop-build decision; name an artefact in each closing sentence.
- **Part II:** five decision vignettes. Different decisions, the same six-person cast; no reset of company maturity.
- **Part III:** one failure hook per architecture chapter, 150 words maximum; the body is mechanism-first. Reuse the same incident from different technical viewpoints without repeating the same prose.
- **Part IV:** no narrative. Decision D-01–D-30 stay one page each.
- **Part V:** one restrained opening and one brief closing for each stage; 600 words maximum total per stage. End each transition with the stage exit artefact.
- **Part VI:** only occasional war-story hooks; each ends with an operational record.
- **Part VII:** an F5 150–300-word war story precedes the exact F2 procedure.
- **Part VIII:** no narrative. Cross-reference Meridian artefacts but do not dramatise them.

**Vignette acceptance:** stakes visible within two sentences; no more than three named characters; no more than four dialogue exchanges; at most one sentence of interiority per character; no villain; decision consequence visible; final sentence names the artefact. End each narrative transition with the E5 bold `The mechanism.` lead-in.

# Phase 4. Chapter-by-chapter development roadmap

Each chapter has a drafting contract below. `R` and `B` references mean the specified *source content* can be mined and rewritten; they are not instructions to paste existing prose. `New` names material that must be authored and proved. `Effort` is estimated **lead-author working days for a complete first draft**, with fact checking, diagrams, developmental editing and copyediting budgeted separately. Every numbered chapter must receive the E4 closing blocks in the exact order `Decisions to make`, `Defaults`, `Artefacts to produce`, `See also`, except the individually templated F1 decision pages of Ch23. For F6/F7, insert all mandatory template headings verbatim.

## Part I. Orientation

### Chapter 1 — The Case for a Shared Fabric
- **Opening hook:** Eleanor asks which of four existing pilots can prove who approved its tools; nobody produces a complete record.
- **Key mechanism:** compare duplicate identity, integrations, verification and evidence against the fixed cost of a shared Fabric; distinguish repeated demand from one-off work.
- **Failure mode:** a central service is funded without repeatable use-case demand. **Anti-patterns:** fleet-wide Fabric as a default; counting demonstrations as production adoption.
- **Decision/default:** D-01; default to no shared Fabric until at least two production use cases need the same governed capabilities and the incremental business case is positive.
- **Artefacts/links:** opportunity register, shared-control map, business-case assumptions; see Ch4, 5, 24, 41.
- **Reuse/new/effort:** B1–4; R1–8, 47. New measured comparison, demand inventory, Meridian opening, and worked decision; **2 days**.

### Chapter 2 — Agent Capability, Autonomy and Risk
- **Opening hook:** a team calls a read-only draft assistant “autonomous” and requests the same permission as a payment workflow.
- **Key mechanism:** separate persona from archetype, classify permitted side effects, assign an autonomy envelope and approval threshold.
- **Failure mode:** authority is inferred from vendor/product labels. **Anti-patterns:** capability spectrum mistaken for maturity; privilege determined by prompt.
- **Decision/default:** D-05, D-16; start at read-only or human approval for writes; promote only after behavioural and security evidence.
- **Artefacts/links:** classification card, action risk matrix, autonomy envelope; see Ch9, 15, 18, 30.
- **Reuse/new/effort:** B2, 9; R5–7, 37. New action-risk rubric and testable promotion thresholds; **2 days**.

### Chapter 3 — Fabric, Product, Use Case and Tenant
- **Opening hook:** two business owners claim the same adapter; neither owns its incident queue.
- **Key mechanism:** show the Fabric, product, use case, persona, archetype and tenant as different ownership/isolation entities.
- **Failure mode:** the Fabric team inherits domain decisions. **Anti-patterns:** use case equated with Agent; tenant equated with department by default.
- **Decision/default:** D-04, D-06; domain owns outcomes and assertions, Fabric team owns shared contracts and controls.
- **Artefacts/links:** system context, responsibility map, ownership registry; see Ch6–7, 35, 44.
- **Reuse/new/effort:** B3, 7; R42, 57. New canonical diagram and two competing ownership examples; **2 days**.

### Chapter 4 — When Not to Build a Fabric
- **Opening hook:** a vendor-native workflow passes every policy test but the architecture board still insists on rebuilding it.
- **Key mechanism:** explicit exclusion tests for single-use-case demand, hard isolation, platform lock-in risk and integration cost.
- **Failure mode:** sunk-cost funding overrides the stop decision. **Anti-patterns:** Fabric-first dogma; false equivalence between embed and custom orchestration.
- **Decision/default:** D-01, D-02; embed or keep domain-local when shared-controls value is not demonstrated.
- **Artefacts/links:** stop-build memo and negative decision record; see Ch1, 5, 23, 41.
- **Reuse/new/effort:** B4–5; R47–50. New quantitative stop thresholds and Meridian declined-option vignette; **2 days**.

## Part II. Strategy

### Chapter 5 — Build, Buy, Embed or Partner
- **Opening hook:** a provider meets the demo criteria but cannot export the authorisation trail.
- **Key mechanism:** compare ownership, risk, portability, contracts, costs, evidence, and exit conditions across four delivery choices.
- **Failure mode:** procurement chooses interface convenience over enforceability. **Anti-patterns:** buy-versus-build binary; unsupported vendor rating.
- **Decision/default:** D-02; embed for bounded SaaS-native tasks, extend for shared governed multi-system work; require exit terms.
- **Artefacts/links:** options appraisal, exit-terms list, ADR; see Ch4, 8, 22, 54.
- **Reuse/new/effort:** B5; R47–49. New four-option worked example with defensible synthetic numbers and sensitivity analysis; **3 days**.

### Chapter 6 — Central, Federated or Hybrid Ownership
- **Opening hook:** security wants central sign-off while Tomas refuses central ownership of customer outcomes.
- **Key mechanism:** RACI, policy-versus-implementation delegation, funding, exception approval and support escalation.
- **Failure mode:** shared team becomes a ticket queue. **Anti-patterns:** all decisions centralised; federated teams exempt from controls.
- **Decision/default:** D-03, D-06; use hybrid, central controls and domain-owned use cases, with a named accountable owner.
- **Artefacts/links:** organisation map, exception path, RACI; see Ch3, 19, 35, 45.
- **Reuse/new/effort:** B6, 30–31; R42. New accountability test cases and dispute-resolution example; **2 days**.

### Chapter 7 — Tenant Isolation and Sovereignty
- **Opening hook:** one insurance document appears in a retail retrieval result during a staging run.
- **Key mechanism:** isolation dimensions, pooled/hard-isolated profiles, data residency, identity scoping and negative tests.
- **Failure mode:** storage separation without shared cache isolation. **Anti-patterns:** `tenant_id` tagging as the only boundary; blanket dedicated clusters.
- **Decision/default:** D-04, D-25; pooled compute with isolated identity/data unless contract, regulation or threat model requires hard isolation.
- **Artefacts/links:** tenant ADR, isolation tests, residency record; see Ch11, 13, 21, 28.
- **Reuse/new/effort:** B7; R10, 33, 40. New three tenant types, data-flow contract and bypass tests; **3 days**.

### Chapter 8 — Model Strategy and Unit Economics
- **Opening hook:** a cheap model route sends repeated retries and raises cost per successful case.
- **Key mechanism:** route by task/risk, measure success-adjusted unit economics, define provider failure and fallback conditions.
- **Failure mode:** token costs improve while task failures worsen. **Anti-patterns:** cheapest-model-first without quality gates; undeclared provider failover.
- **Decision/default:** D-17, D-26; route within verified provider/residency bounds and spend against successful outcomes.
- **Artefacts/links:** router ADR, routing matrix, budget forecast; see Ch16, 20, 38, 47.
- **Reuse/new/effort:** B8, 34; R13, 30. New scenario-level cost model, quality-band constraints and failover worksheet; **3 days**.

### Chapter 9 — Earned Autonomy and Sponsorship
- **Opening hook:** the sponsor asks for autonomous refunds before the pilot can account for denied actions.
- **Key mechanism:** evidence-gated progression from read-only to approved writes, limited autonomous writes and periodic requalification.
- **Failure mode:** higher autonomy persists after quality degrades. **Anti-patterns:** one-time approval; “human in loop” without approval SLA.
- **Decision/default:** D-05, D-16, D-23; set task-specific envelopes, approvals for financial mutations, and revocation triggers.
- **Artefacts/links:** autonomy charter, promotion rubric, rollback trigger; see Ch2, 18–19, 33.
- **Reuse/new/effort:** B9, 28; R6, 37. New worked progression and sponsor decision; **3 days**.

## Part III. Architecture

### Chapter 10 — The Canonical Fabric Architecture
- **Opening hook:** a mutable action cannot be attributed to one policy decision across two pilots.
- **Key mechanism:** draw E/T/C/L, eight planes, three logical paths, evidence joins and enforcement boundaries; demonstrate a read and a write trajectory.
- **Failure mode:** control ownership follows diagram boxes instead of responsibilities. **Anti-patterns:** tier proliferation; a single gigantic architecture image.
- **Decision/default:** D-07, D-18; design four layers and eight planes with mandatory side-effect interception.
- **Artefacts/links:** Figures 10-1/10-2, execution/ownership crosswalk; see Ch11–22, 23.
- **Reuse/new/effort:** B10–15; R10.1, 25A–33. New normative diagrams and worked flow; **3 days**.

### Chapter 11 — Execution Environment
- **Opening hook:** a long-running code action shares a worker with another tenant after a failed teardown.
- **Key mechanism:** F6; worker allocation, isolation tiers, warm pool identity-neutrality, quotas, egress policy, checkpoint resume and teardown contracts.
- **Failure mode:** state leakage and retry exhaustion. **Anti-patterns:** pod per agent persona; CPU-only scale trigger.
- **Decision/default:** D-07/D-08; default ephemeral sandbox for risk-bearing execution, fixed step/runtime budget; scale on queue age and saturation.
- **Artefacts/links:** isolation profile, quota sheet, teardown proof; see Ch14, 16, 21, 36.
- **Reuse/new/effort:** B11.1; R19 and scale/HA material. New interface and test data for worker reuse; **3 days**.

### Chapter 12 — Tooling
- **Opening hook:** a tool schema changes `amount` semantics; the agent sends a valid but unintended request.
- **Key mechanism:** F6; tool registry, typed schemas, risk labelling, idempotency, approval handle, adapter retries and error normalisation.
- **Failure mode:** correct JSON still performs an unauthorised business action. **Anti-patterns:** prompt-only permissions; unversioned tool descriptions.
- **Decision/default:** D-09/D-10; register and pin schemas; require action receipt for every mutable call.
- **Artefacts/links:** tool manifest, request/receipt schemas, negative tests; see Ch16, 18, 22, 39.
- **Reuse/new/effort:** B11.2; R18, 32. New version-change example and explicit data contract; **3 days**.

### Chapter 13 — Context
- **Opening hook:** two source records disagree about a product status and memory replays the stale statement.
- **Key mechanism:** F6; source ingestion, ACL retrieval, context manifest, canonical entity resolution, contradiction states, memory tiers, write-path provenance, TTL and deletion.
- **Failure mode:** tenant leak, stale source promoted into durable memory, or unresolved conflicts silently merged. **Anti-patterns:** vector similarity as truth; shared mutable memory without lineage.
- **Decision/default:** D-11–14; ACL before retrieval and again before use; no durable write without provenance and policy class; escalate unresolved conflicts.
- **Artefacts/links:** context contract, memory-write receipt, conflict state machine; see Ch15, 18, 21, 28.
- **Reuse/new/effort:** R15–16, 21.1, 38–40; B Appendix A. New memory write/read sequence, deletion tests and data examples; **5 days**.

### Chapter 14 — Lifecycle
- **Opening hook:** an interrupted workflow resumes with an expired permission and repeats a side effect.
- **Key mechanism:** F6; Harness-owned loop, trajectory, checkpoint, delegation, retries, idempotency, pause/resume, approval expiry and retirement.
- **Failure mode:** duplicate mutation or privilege retained across restart. **Anti-patterns:** unbounded agent loops; checkpoint as authorisation.
- **Decision/default:** D-15/D-16; use one Harness for task control, bounded steps and re-authorisation before resumed actions.
- **Artefacts/links:** Harness contract, state machine, restart assertions; see Ch11–12, 15–16, 36.
- **Reuse/new/effort:** R17, 20, 22, 25, 41–45; B11.4. New sequence for resumable action; **4 days**.

### Chapter 15 — Identity Control Plane
- **Opening hook:** a delegated refund action asks for broader permissions than the human originator held.
- **Key mechanism:** F7; identity broker, workload attestation, actor-chain issuance, attenuation, audience binding, revocation and policy-checked reissue.
- **Threat/failure:** stolen delegation token or missing tenant binding. **Anti-patterns:** permanent agent superuser; forwarding user JWT unchanged.
- **Decision/default:** D-19/D-20; short-lived, signed, attenuated identity chain per action and delegation hop.
- **Artefacts/links:** chain schema, security tests and revocation ledger; see Ch16, 19, 27, 40.
- **Reuse/new/effort:** R12/25A; B12. New signer/verifier examples, threat coverage and evidence artefact; **3 days**.

### Chapter 16 — Gateway Control Plane
- **Opening hook:** a tool sends traffic directly from a worker and avoids the policy proxy.
- **Key mechanism:** F7; configuration policy versus deployed PEPs, model/tool/A2A admission, routing and egress, fail-closed side-effect path and bypass testing.
- **Threat/failure:** network and credential bypass, inconsistent policy cache. **Anti-patterns:** gateway as single logical choke without network enforcement; model route selected solely by price.
- **Decision/default:** D-10/D-18; enforce external mutations at verified PEPs; deny if scope or policy proof is absent.
- **Artefacts/links:** PEP map, test matrix, authorisation receipt; see Ch12, 15, 19, 27.
- **Reuse/new/effort:** R13/25B; B13. New non-bypass proof design and availability failure handling; **4 days**.

### Chapter 17 — Observability Control Plane
- **Opening hook:** on-call sees a cost anomaly but cannot correlate retries to the original task.
- **Key mechanism:** F7; join trajectories across steps, redact sensitive payload, measure queue/latency/cost, and emit coherent evidence envelopes.
- **Threat/failure:** missing correlation or excess sensitive logging. **Anti-patterns:** token logs as full audit; collecting prompts without data classification.
- **Decision/default:** D-24; use mandatory correlation IDs, bounded retention and separately controlled evidence stores.
- **Artefacts/links:** event schema, telemetry map, incident query; see Ch18, 20–21, 36–40.
- **Reuse/new/effort:** R28; B32–33. New end-to-end trace exemplar and evidence retrieval exercise; **3 days**.

### Chapter 18 — Verification Control Plane
- **Opening hook:** a release passes benchmark averages while failing one high-risk forbidden-action assertion.
- **Key mechanism:** F7; offline/online sets, behavioural assertions, trajectory scoring, contract tests, canary, runtime checks and versioned stop gates.
- **Threat/failure:** benchmark overfit, untested schema drift and false confidence. **Anti-patterns:** aggregate success metric only; unreviewed model upgrade.
- **Decision/default:** D-22/D-23; all mutable-risk releases require explicit negative tests and hard-blocking assertions.
- **Artefacts/links:** assurance matrix, assertion bundle, signed gate report; see Ch9, 12–13, 33, 47.
- **Reuse/new/effort:** R24/29; B18, 28. New assertion fixtures and measurable acceptance policy; **4 days**.

### Chapter 19 — Governance Control Plane
- **Opening hook:** a high-impact domain exception has no owner or expiry date.
- **Key mechanism:** F7; risk categories, policy authority, approval workflow, waivers, recertification and actor accountability.
- **Threat/failure:** silent policy override or unapproved autonomy drift. **Anti-patterns:** governance by committee without accountable decision maker; permanent exception.
- **Decision/default:** D-05/D-29; set named approval authority, bounded exception expiry and risk-specific evidence.
- **Artefacts/links:** risk charter, approval and waiver ledgers; see Ch6, 9, 15, 35.
- **Reuse/new/effort:** R27/42; B9, 31. New policy evaluation worked case and threat coverage; **3 days**.

### Chapter 20 — FinOps Control Plane
- **Opening hook:** provider unit costs fall but failed/retried tasks raise total spend.
- **Key mechanism:** F7; invoice reconciliation, budgets, forecast, usage dimensions and cost per successful task.
- **Threat/failure:** cost allocated to a shared tenant rather than the invoking use case. **Anti-patterns:** tokens as sole unit; quotas without business criticality.
- **Decision/default:** D-26; meter by tenant/use case/trajectory and reconcile each unit to invoices.
- **Artefacts/links:** allocation dimensions, chargeback policy, forecast; see Ch8, 17, 32, 38.
- **Reuse/new/effort:** R30; B34. New synthetic invoice reconciliation and stop/exception case; **3 days**.

### Chapter 21 — Data Protection Control Plane
- **Opening hook:** a discontinued pilot's memory remains searchable after consent withdrawal.
- **Key mechanism:** F7; classification, regional controls, access, retention, legal hold, encrypted stores and deletion verification.
- **Threat/failure:** untracked copy in retrieval cache or evidence store. **Anti-patterns:** deletion of application table treated as complete erasure; logging sensitive prompts indiscriminately.
- **Decision/default:** D-25/D-30; default explicit retention/erasure schedule with per-store proof, subject to legal hold.
- **Artefacts/links:** data-flow map, retention matrix, deletion certificate; see Ch7, 13, 34, 49.
- **Reuse/new/effort:** R33, 38–40; B7, 23. New complete data inventory and legal-hold example; **3 days**.

### Chapter 22 — Interoperability Control Plane
- **Opening hook:** an agent peer changes a protocol version and silently removes delegation metadata.
- **Key mechanism:** F7; transport versus semantics, boundary-specific protocols, compatibility tests, version pinning and retirement.
- **Threat/failure:** a syntactically valid request loses security intent. **Anti-patterns:** protocol compatibility assumed to guarantee shared meaning; unpinned standards.
- **Decision/default:** D-21; version and test every protocol boundary; use C for semantic entity reconciliation.
- **Artefacts/links:** protocol registry, compatibility matrix, boundary conformance report; see Ch12–13, 15–16, 53.
- **Reuse/new/effort:** R31–32; B15. New standards evidence verification and an incompatibility worked example; **3 days**.

## Part IV. Decisions

### Chapter 23 — The Fabric Decision Atlas
- **Opening hook:** none. Open with a one-paragraph instruction on using the 30 one-page decisions and a link to the chapter-dependency map.
- **Key mechanism:** reproduce F1 exactly for D-01–D-30, one printable page each. Include context, default, why, trade-off, deviation, reversibility, artefact and see also.
- **Failure mode:** decision without an evidence threshold. **Anti-patterns:** option lists without a recommendation; unexplained deviations. These are checked editorially, not added as decorative text to F1.
- **Decision/default:** all thirty; no generic default can override its own deviation clause.
- **Artefacts/links:** the full catalogue in Phase 5, with links to Ch1–22, 24–58.
- **Reuse/new/effort:** B16–17 and implicit source decisions throughout R; new F1 pages, case evidence and traceability; **10 days**.

## Part V. Lifecycle

### Chapter 24 — Stage 0: Strategic Intent
- **Opening hook:** Eleanor requests a funding decision after seeing four overlapping pilots.
- **Key mechanism:** demand classification, option appraisal, explicit stop criteria, investment gate and sponsor ownership.
- **Failure mode/anti-pattern:** strategic approval based on demonstrations; defaulting to a Fabric before calculating shared controls.
- **Decision/default:** D-01–03; require an evidence-backed use-case portfolio and funded governance owner before authorising design.
- **Artefacts/links:** strategic intent brief, demand register, Stage 0 gate; see Ch1, 4–6, 41.
- **Reuse/new/effort:** B19; R47–49. New dated Meridian decision notes and exit criteria; **1.5 days**.

### Chapter 25 — Stage 1: Fabric Vision
- **Opening hook:** the sponsor asks what exactly will be shared and what remains domain-owned.
- **Key mechanism:** service catalogue, use-case boundaries, outcome metrics, autonomy cap, product roadmap and exclusions.
- **Failure mode/anti-pattern:** vision measured as agent count; scope without a named owner.
- **Decision/default:** D-05–06; define product outcomes and risk envelopes before implementation choices.
- **Artefacts/links:** vision charter, use-case register, benefit hypothesis; see Ch2–3, 6, 35.
- **Reuse/new/effort:** B20; R42, 44. New signed-off vision example and synthetic KPIs; **1.5 days**.

### Chapter 26 — Stage 2: Reference Architecture
- **Opening hook:** Maya must explain which service enforces a tool permission during a multi-agent run.
- **Key mechanism:** baseline diagrams, interface contracts, tenant model, threat boundary and decision-page linkage.
- **Failure mode/anti-pattern:** two conflicting canonical diagrams; control plane with no PEP.
- **Decision/default:** D-07–15, D-18; adopt Ch10–22 model and record deviations in ADRs.
- **Artefacts/links:** HLD, trust boundaries, architecture baseline, ADR index; see Ch10–22, 42, 52.
- **Reuse/new/effort:** B21; R10 and trust-chain mapping. New complete baseline example; **2 days**.

### Chapter 27 — Stage 3: Trust Chain and Security
- **Opening hook:** Ruth proves a delegated call can cross a tenant boundary through a raw service token.
- **Key mechanism:** threat modelling of intake, context, delegation, tools, memory, output and evidence; map threat to owner and negative test.
- **Failure mode/anti-pattern:** “secure model” substituted for tool-level controls; audit only after execution.
- **Decision/default:** D-10, D-19–21, D-25; use per-boundary enforcement and deny privilege expansion.
- **Artefacts/links:** threat register, trust diagram, abuse-case results; see Ch15–16, 19, 21, 48.
- **Reuse/new/effort:** R34–37; B22. New traceable threat-to-test crosswalk; **2 days**.

### Chapter 28 — Stage 4: Tenant Substrate
- **Opening hook:** a staging isolation run reveals a shared vector index returns the wrong tenant's reference.
- **Key mechanism:** provision tenants, partition context, control identity and cost keys, run negative isolation tests, attest readiness.
- **Failure mode/anti-pattern:** namespace names mistaken for security proof; pooled cache without access filter.
- **Decision/default:** D-04, D-11–14; block tenant launch until end-to-end isolation tests pass.
- **Artefacts/links:** tenant manifest, context partition proof, go/no-go certificate; see Ch7, 13, 21, 43.
- **Reuse/new/effort:** B23; R21, 33. New test script specification and example findings; **2 days**.

### Chapter 29 — Stage 5: Shared Services Bootstrap
- **Opening hook:** the new gateway comes online, but one connector can still call an endpoint directly.
- **Key mechanism:** deploy PEP, set model/tool routes, wire telemetry, install assertions and run smoke/bypass tests.
- **Failure mode/anti-pattern:** green infrastructure status mistaken for control effectiveness.
- **Decision/default:** D-17–18, D-22, D-24; require direct-bypass negative test and evidence correlation before onboarding.
- **Artefacts/links:** bootstrap checklist, red-path tests, baseline telemetry; see Ch16–18, 20, 42.
- **Reuse/new/effort:** B24; R25B, 28–29. New staged bootstrap workflow with rollback; **2 days**.

### Chapter 30 — Stage 6: First Use Case
- **Opening hook:** the payment-dispute-triage pilot fails a contradiction assertion and is narrowed to read-only scope.
- **Key mechanism:** business acceptance, security review, evaluation, canary, rollback and promotion decision.
- **Failure mode/anti-pattern:** handpicked demonstrations become release evidence; unowned domain assertions.
- **Decision/default:** D-05, D-16, D-23; pilot with bounded read-only actions unless explicit write approval is evidenced.
- **Artefacts/links:** gate report, release dossier, post-pilot review; see Ch9, 18, 44, 47.
- **Reuse/new/effort:** B25; R45 and checklists. New full pilot case and assertion outcomes; **2 days**.

### Chapter 31 — Stage 7: Scale to Twelve Use Cases
- **Opening hook:** five teams ask for unique onboarding exceptions, overwhelming the platform team.
- **Key mechanism:** approved archetypes, repeatable registration, tenant profile, exception expiry, budget and readiness gates.
- **Failure mode/anti-pattern:** every new use case becomes a bespoke control architecture.
- **Decision/default:** D-04, D-29; reuse approved archetypes; permit deviations only through dated ADRs.
- **Artefacts/links:** onboarding catalogue, 12-use-case portfolio, exception register; see Ch6, 35, 45–46.
- **Reuse/new/effort:** B26; R44 and scale materials. New three-tenant portfolio table and capacity progression; **2 days**.

### Chapter 32 — Stage 8: Operate as a Product
- **Opening hook:** backlog increases while infrastructure health dashboards remain green.
- **Key mechanism:** define user-centred SLO, error budget, on-call escalation, service support, cost attribution and continuity.
- **Failure mode/anti-pattern:** infrastructure availability equated with successful tasks.
- **Decision/default:** D-26–28; measure cost and reliability per successful task and maintain tested recovery paths.
- **Artefacts/links:** service contract, incident classification, SLO report; see Ch17, 20, 36–38.
- **Reuse/new/effort:** B27; R25 and scale/DR. New week-by-week operating example; **2 days**.

### Chapter 33 — Stage 9: Continuous Verification
- **Opening hook:** a previously accepted use case degrades after a tool-description update.
- **Key mechanism:** changed-asset fingerprint, replay set, behavioural assertions, trajectory comparison, rollback and reaccreditation.
- **Failure mode/anti-pattern:** one-time risk approval becomes permanent; “model upgrade” exempted from release control.
- **Decision/default:** D-22–23; any changed model, prompt, retrieval or tool contract requires impact-based verification.
- **Artefacts/links:** evaluation history, drift report, recertification; see Ch18, 39, 47.
- **Reuse/new/effort:** B28; R24, 45. New regression test ledger and requalification case; **2 days**.

### Chapter 34 — Stage 10: Retirement
- **Opening hook:** an unused pilot is switched off, but its long-term memory and access tokens remain live.
- **Key mechanism:** retirement approval, dependency export, revocation, data disposal/legal hold, audit export and outcome verification.
- **Failure mode/anti-pattern:** disabling UI treated as retirement; deletion proof without all stores.
- **Decision/default:** D-30; demand explicit disposal evidence and continuity plan; separately rehearse Fabric exit.
- **Artefacts/links:** retirement certificate, deletion ledger, exit rehearsal; see Ch21, 40, 49–50.
- **Reuse/new/effort:** B29; R41, 43, 46. New disposition matrix and hypothetical full-Fabric exit case; **2 days**.

## Part VI. Operating model

### Chapter 35 — Team Design and Responsibility Matrix
- **Opening hook:** an incident reaches three teams and none acknowledges ownership.
- **Key mechanism:** service catalogue, RACI, delegated control-plane authority, escalation and cost-centre mapping.
- **Failure mode/anti-pattern:** split accountability; central team owns business decisions it cannot validate.
- **Decision/default:** D-03, D-06, D-29; one accountable owner per service and risk decision; named deputy and escalation.
- **Artefacts/links:** RACI, service registry, escalation tree; see Ch6, 19, 31, 40.
- **Reuse/new/effort:** B30–31; R42. New filled six-role RACI and handoff examples; **2 days**.

### Chapter 36 — Reliability, Service Levels and Continuity
- **Opening hook:** a model dependency slows but no alert fires until the queue misses its business deadline.
- **Key mechanism:** latency/quality/error-budget contracts, saturation signals, tiered HA/DR, RTO/RPO and recovery drills.
- **Failure mode/anti-pattern:** uptime-only SLO and unverified failover; CPU-only scaling.
- **Decision/default:** D-27; assign SLO and RTO/RPO per use-case risk and proof through drills.
- **Artefacts/links:** SLO contract, DR exercise, capacity model; see Ch11, 14, 17, 32.
- **Reuse/new/effort:** B32; R scale/HA/DR. New numbers as fictional targets with test method; **3 days**.

### Chapter 37 — Incident Command and Security Response
- **Opening hook:** memory contamination is detected after a denied external-call attempt.
- **Key mechanism:** severity, containment, evidence preservation, source quarantine, access revocation, restore and post-incident review.
- **Failure mode/anti-pattern:** continuing an affected queue; deleting evidence before investigation.
- **Decision/default:** D-28; containment authority sits with the incident commander; safety-sensitive resume requires security sign-off.
- **Artefacts/links:** incident command record, evidence custody, safe-resume decision; see Ch16–18, 21, 48.
- **Reuse/new/effort:** B33; R46. New fully worked security incident timeline; **3 days**.

### Chapter 38 — Unit Economics, Showback and Chargeback
- **Opening hook:** the forecast looks favourable until retry and failure expenses are allocated.
- **Key mechanism:** unit cost formula, charge dimensions, shared overhead, forecasting and reconciliation to bills.
- **Failure mode/anti-pattern:** chargeback based only on tokens; budgets lack owners.
- **Decision/default:** D-26; publish cost per successful task, with failed-run cost allocated explicitly.
- **Artefacts/links:** chargeback policy, synthetic month-end reconciliation; see Ch8, 20, 32, 41.
- **Reuse/new/effort:** B34; R30. New numerical example and sensitivity scenarios; **3 days**.

### Chapter 39 — Release, Change and Version Control
- **Opening hook:** a tool schema changes between two model canaries without a new verification run.
- **Key mechanism:** change classification, dependency inventory, versioned prompt/model/tool/index/policy bundles, promotion and rollback.
- **Failure mode/anti-pattern:** silent SaaS update; rollback incompatible with migrated state.
- **Decision/default:** D-21–23, D-29; no mutable-risk production release without a signed gate and reversal plan.
- **Artefacts/links:** change record, release manifest, rollback drill; see Ch12, 18, 22, 47.
- **Reuse/new/effort:** B35; R45. New exact change workflow and safe version-drift example; **3 days**.

### Chapter 40 — Audit Evidence and Assurance Reviews
- **Opening hook:** a reviewer asks who approved a tool call and whether it executed; the logs show a response but no authorisation receipt.
- **Key mechanism:** join identity, policy, action, context, verification and retention records into one evidence envelope.
- **Failure mode/anti-pattern:** telemetry used as permission evidence; evidence export loses provenance.
- **Decision/default:** D-20, D-24, D-30; one correlated and access-controlled evidence packet per risk-bearing trajectory.
- **Artefacts/links:** end-to-end evidence packet, reviewer checklist, attestation; see Ch15–18, 21, 52, 57.
- **Reuse/new/effort:** B31–33, 52; R34, 54. New realistic audit specimen and verification queries; **3 days**.

## Part VII. Playbooks

### Chapter 41 — P1: Build the Business Case
- **Opening hook:** Eleanor declines a budget request that lacks duplicate-cost and risk assumptions.
- **Mechanism:** P1 seven-step appraisal; failure/anti-pattern: unsupported ROI and Fabric-first assumption.
- **Decision/default:** D-01–03, D-26; fund only where shared controls and outcomes justify recurring cost.
- **Artefacts/links:** business case, option ADR, benefits register; see Ch1, 5, 8, 24.
- **Reuse/new/effort:** B36, B19; R47. New F2 procedure, F5 vignette, fully filled case; **2 days**.

### Chapter 42 — P2: Design the Reference Architecture
- **Opening hook:** Maya is asked which service owns a side effect across one tool and two agents.
- **Mechanism:** architecture baseline and control proof; failure/anti-pattern: ambiguous ownership or unverifiable PEP.
- **Decision/default:** D-07–22; select canonical E/T/C/L and eight planes; document exceptions.
- **Artefacts/links:** 12-unit map, actor chain and threat diagram; see Ch10–22, 26.
- **Reuse/new/effort:** B37, B21. New F2 steps and detailed handover pack; **2 days**.

### Chapter 43 — P3: Stand Up the Tenant Substrate
- **Opening hook:** staging retrieval crosses from insurance to retail banking.
- **Mechanism:** provision and negative-test the identity/context/evidence/cost partitions; failure/anti-pattern: tenant-tag-only isolation.
- **Decision/default:** D-04, D-11–14, D-25; deny live onboarding until cross-tenant tests pass.
- **Artefacts/links:** tenant manifest, leak-test proof, sign-off; see Ch7, 13, 21, 28.
- **Reuse/new/effort:** B38, B23. New F2 steps, synthetic isolation examples; **2 days**.

### Chapter 44 — P4: Onboard the First Use Case
- **Opening hook:** Tomas's payment-dispute triage fails a mandatory conflict test.
- **Mechanism:** register, assert, pilot, remediate and release; failure/anti-pattern: demo-only acceptance and unbounded writes.
- **Decision/default:** D-05, D-16, D-23; read-only first with explicit promotion gate.
- **Artefacts/links:** release dossier, domain assertions and rollback; see Ch9, 18, 30.
- **Reuse/new/effort:** B39, B25. New full release transcript and handoff evidence; **2 days**.

### Chapter 45 — P5: Scale from One to Ten Use Cases
- **Opening hook:** five teams submit incompatible tool access requests.
- **Mechanism:** archetype templates, onboarding automation, cost/service gate; failure/anti-pattern: bespoke authorisation per domain.
- **Decision/default:** D-06, D-26, D-29; approved reusable onboarding packages with expiring exceptions.
- **Artefacts/links:** onboarding catalogue, portfolio gate report; see Ch6, 19, 31, 35.
- **Reuse/new/effort:** B40, B26. New F2 onboarding steps and portfolio metrics; **2 days**.

### Chapter 46 — P6: Plan for Ten to One Hundred-Plus
- **Opening hook:** service growth outpaces the proposed gateway capacity model.
- **Mechanism:** capacity scenario, contract sharding, queue and failure drills; failure/anti-pattern: extrapolating from healthy average CPU.
- **Decision/default:** D-08, D-27, D-29; scale against queue age, policy latency, error budgets and cost limits.
- **Artefacts/links:** synthetic 100-plus stress report, not a claim of deployment; see Ch11, 17, 31, 36.
- **Reuse/new/effort:** B41, B26. New capacity worksheet and drill plan; **3 days**.

### Chapter 47 — P7: Execute a Model Upgrade
- **Opening hook:** a model change selects the wrong tool argument while preserving answer quality.
- **Mechanism:** pinned baseline, shadow replay, hard assertions, canary and rollback; failure/anti-pattern: benchmark-only acceptance.
- **Decision/default:** D-17, D-22–23; block if any critical behavioural assertion fails.
- **Artefacts/links:** comparison report, signed gate and rollback receipt; see Ch8, 18, 33, 39.
- **Reuse/new/effort:** B42, B28. New F2 procedure and test dataset card; **2 days**.

### Chapter 48 — P8: Handle a Security Incident
- **Opening hook:** a poisoned context item requests external exfiltration; the Gateway denies the action.
- **Mechanism:** incident trigger, scope assessment, containment, forensics, correction, resumption; failure/anti-pattern: deleting logs or assuming denial means no breach.
- **Decision/default:** D-10, D-20, D-28; preserve evidence and suspend affected authority until proven safe.
- **Artefacts/links:** incident evidence packet, containment and re-entry gate; see Ch16, 21, 37, 40.
- **Reuse/new/effort:** B43, B33; R35–36, 46. New F2 escalation matrix and worked packet; **3 days**.

### Chapter 49 — P9: Retire a Use Case
- **Opening hook:** the old pilot's tool token works after its interface is removed.
- **Mechanism:** dependency cut, actor revocation, memory disposition, archive and outcome review; failure/anti-pattern: deleting the dashboard only.
- **Decision/default:** D-30; no closure without verified revocation and per-store disposition.
- **Artefacts/links:** retirement certificate, deletion receipts; see Ch21, 34, 40.
- **Reuse/new/effort:** B44, B29. New per-store evidence checklist and fictional example; **2 days**.

### Chapter 50 — P10: Retire or Replace the Fabric
- **Opening hook:** Eleanor requires an exit option while the Fabric remains in service.
- **Mechanism:** tenant export, contract exit, parallel-run, decommission rehearsal and evidence handover; failure/anti-pattern: irreversible proprietary state or incomplete legal hold.
- **Decision/default:** D-02, D-27, D-30; retain an annually tested exit plan; do not pretend the fictional Fabric is shut down.
- **Artefacts/links:** exit rehearsal and migration decision; see Ch5, 22, 34, 36.
- **Reuse/new/effort:** B45, B29. New complete rehearsal procedure and acceptance criteria; **3 days**.

## Part VIII. Reference library

### Chapter 51 — Layer and Control-Plane Checklists
- **Opening hook:** direct instruction to inspect the evidence field for each checklist answer.
- **Mechanism:** F3 templates for four layers and eight planes; failure/anti-pattern: subjective “is it secure?” checks.
- **Decision/default:** D-07–25; make every yes/no question auditable and record evidence ID or failure.
- **Artefacts/links:** 12 checklists, completed example; see Ch10–22, 40.
- **Reuse/new/effort:** B46; R52. New at least eight evidenced questions per unit; **3 days**.

### Chapter 52 — Architecture Decision and Risk Records
- **Opening hook:** record the decision before a vendor or implementation is chosen.
- **Mechanism:** exact F8 ADR, governance exception and decision-to-artefact index; failure/anti-pattern: undocumented default deviations.
- **Decision/default:** D-01–30; no deviation without owner, evidence threshold and review date.
- **Artefacts/links:** ADR-001, exception record, traceability map; see Ch23, 35, 40.
- **Reuse/new/effort:** B47 and B17. New filled ADR and audit trail; **2 days**.

### Chapter 53 — Protocol and Boundary Reference
- **Opening hook:** identify the trust boundary before naming a protocol.
- **Mechanism:** F10 entries for model transport, tool invocation, agent-to-agent, events, identity, telemetry and schemas; failure/anti-pattern: “protocol supported” treated as version compatibility.
- **Decision/default:** D-09, D-21; specify exact revision and source-backed capability at each boundary.
- **Artefacts/links:** protocol reference register, contract test cards; see Ch12, 15–16, 22.
- **Reuse/new/effort:** B48, B15; R32. New dated protocol evidence and conformance cases; **3 days**.

### Chapter 54 — Technology Decision Matrix
- **Opening hook:** replace a “top ten tools” list with boundary requirements and vendor-neutral acceptance tests.
- **Mechanism:** compare category options by evidence, security, cost, reversibility and fit; failure/anti-pattern: unversioned claims or product endorsements.
- **Decision/default:** D-02, D-07, D-17; weigh a product only within a documented use-case requirement.
- **Artefacts/links:** matrix, evidence register and scoring worksheet; see Ch5, 8, 11, 22.
- **Reuse/new/effort:** B49; R53–57. New independently cited examples and as-of dates; **3 days**.

### Chapter 55 — Standards and Regulatory Map
- **Opening hook:** show a control obligation, its source and the evidence that satisfies it.
- **Mechanism:** F11 table and obligation-to-implementation map; failure/anti-pattern: equating a standard citation with compliance.
- **Decision/default:** D-19, D-25, D-28; cross-map only sourced versions and actual in-scope obligations.
- **Artefacts/links:** standards crosswalk, evidence register; see Ch15–21, 27, 40.
- **Reuse/new/effort:** B50; R35–37. New version-verified legal/standards research, editor review; **4 days**.

### Chapter 56 — Glossary and Controlled Vocabulary
- **Opening hook:** an alphabetical lookup entry with exact term and cross-reference.
- **Mechanism:** F9 entries for every C2 term and defined technical concept; failure/anti-pattern: synonyms expanding the architecture.
- **Decision/default:** all; use C2 exact terms and one owning chapter per term.
- **Artefacts/links:** glossary, forbidden-synonym sweep, index hints; see Ch10–23, 53.
- **Reuse/new/effort:** B51; R terminology. New controlled glossary and automated term scan; **2 days**.

### Chapter 57 — Worked Evidence and Delivery Artefacts
- **Opening hook:** show a reviewer the complete evidence envelope rather than merely listing its field names.
- **Mechanism:** print filled ADR, context manifest, actor-chain receipt, evaluation release report, incident packet and retirement certificate; failure/anti-pattern: empty templates passed off as reference value.
- **Decision/default:** D-20, D-23, D-30; every specimen must reconcile identifiers and demonstrate approval or denial.
- **Artefacts/links:** six completed specimens, cross-reference map; see Ch13–18, 40, 47–49.
- **Reuse/new/effort:** B52, R54. New synthetic but consistent records and worked joins; **4 days**.

### Chapter 58 — Industry Adoption Overlays
- **Opening hook:** state which decision flips because of sector requirements, rather than repeat the architecture.
- **Mechanism:** six sector tables with regulation scope, data class, autonomy, tenancy, evidence and exception; failure/anti-pattern: one-size-fits-all regulatory labels.
- **Decision/default:** D-01, D-04, D-25; adapt only specific constraints with sourced authority.
- **Artefacts/links:** banking, insurance, healthcare, public sector, retail and manufacturing overlays; see Ch4, 7, 19, 55.
- **Reuse/new/effort:** B53, R8. New researched overlays and scope notes; **3 days**.

**Drafting capacity ledger:** work estimates above are for first drafts only. The writer-day sum must be tracked against editorial, research, review and illustration allocations. For execution, maintain a chapter tracker with: `chapter_id`, `template`, `word_budget`, `page_budget`, `source_sections`, `opening_event`, `decision_ids`, `artefact_ids`, `diagram_ids`, `writer`, `reviewer`, `due_date`, `M2_status`, `source_evidence_status`, `final_edit_status`. Every chapter advances through S M3's 12 stages and cannot skip fact-check or accessibility sign-off.


# Phase 5. Definitive decision catalogue (Chapter 23)

The following thirty entries are the **drafting masters** for 30 printed F1 pages. Each entry uses every F1 field in S F1 and is tied to real chapter destinations. At typesetting, each must occupy exactly one page; expand only the evidence and worked examples needed to reach one-page density. The default is a proposed **book recommendation**, not a claim that a named production organisation has implemented it. Cite standards, public examples and quantitative claims during M3 fact-checking.

| Decision | Title | Reversibility | Artefact | Main chapters |
|---|---|---|---|---|
| D-01 | Adopt a shared Fabric | Two-way door | `fabric-adoption-adr.md` | Ch1, Ch4, Ch5, Ch24, Ch41 |
| D-02 | Select build, buy, embed or partner | Two-way door | `sourcing-options-adr.md` | Ch4, Ch5, Ch24, Ch41, Ch50, Ch54 |
| D-03 | Choose a central, federated or hybrid model | Two-way door | `operating-model-adr.md` | Ch3, Ch6, Ch24, Ch35, Ch41 |
| D-04 | Choose tenant isolation | Two-way door | `tenant-isolation-adr.md` | Ch3, Ch7, Ch11, Ch13, Ch21, Ch28, Ch43 |
| D-05 | Set the autonomy envelope | Two-way door | `autonomy-envelope.yaml` | Ch2, Ch9, Ch19, Ch25, Ch30, Ch44 |
| D-06 | Allocate Fabric and domain ownership | Two-way door | `ownership-raci.md` | Ch3, Ch6, Ch25, Ch35, Ch45 |
| D-07 | Select execution isolation | Two-way door | `execution-isolation-profile.yaml` | Ch10, Ch11, Ch26, Ch42 |
| D-08 | Set runtime limits and scaling signals | Two-way door | `workload-budget-and-capacity.yaml` | Ch11, Ch14, Ch36, Ch46 |
| D-09 | Version tool contracts | Two-way door | `tool-contract-registry.yaml` | Ch12, Ch22, Ch39, Ch53 |
| D-10 | Authorise mutable tool actions | Two-way door | `action-authorisation-contract.json` | Ch12, Ch15, Ch16, Ch27, Ch48 |
| D-11 | Control retrieval access | Two-way door | `retrieval-policy-and-test-suite.md` | Ch7, Ch13, Ch21, Ch28, Ch43 |
| D-12 | Govern durable memory | Two-way door | `memory-write-contract.json` | Ch13, Ch21, Ch34, Ch49 |
| D-13 | Enable cross-agent memory | Two-way door | `cross-agent-handoff-schema.json` | Ch13, Ch14, Ch15, Ch21 |
| D-14 | Reconcile semantic identities | Two-way door | `semantic-reconciliation-record.json` | Ch13, Ch18, Ch22, Ch28 |
| D-15 | Choose orchestration and resume strategy | Two-way door | `harness-state-machine.md` | Ch11, Ch14, Ch15, Ch36 |
| D-16 | Require human approval | Two-way door | `approval-envelope-and-sla.yaml` | Ch2, Ch9, Ch14, Ch19, Ch30 |
| D-17 | Route and fail over models | Two-way door | `model-routing-policy.yaml` | Ch8, Ch16, Ch20, Ch39, Ch47 |
| D-18 | Prove Gateway non-bypassability | One-way door | `gateway-bypass-proof.md` | Ch10, Ch12, Ch16, Ch27, Ch42 |
| D-19 | Manage human and agent identity | Two-way door | `identity-registry-and-claims.yaml` | Ch15, Ch19, Ch27, Ch40 |
| D-20 | Control delegation chains | One-way door | `delegation-chain-proof.json` | Ch14, Ch15, Ch16, Ch40 |
| D-21 | Version interoperability contracts | Two-way door | `protocol-boundary-registry.md` | Ch12, Ch22, Ch39, Ch53 |
| D-22 | Select verification strategy | Two-way door | `verification-matrix-and-fixtures.md` | Ch9, Ch13, Ch18, Ch33, Ch47 |
| D-23 | Set release and autonomy gates | Two-way door | `release-gate-report.md` | Ch9, Ch18, Ch30, Ch33, Ch39, Ch47 |
| D-24 | Design telemetry and evidence retention | Two-way door | `evidence-envelope-schema.json` | Ch17, Ch21, Ch36, Ch40, Ch57 |
| D-25 | Choose data residency and protection | One-way door | `data-protection-and-residency-record.md` | Ch7, Ch13, Ch21, Ch27, Ch55 |
| D-26 | Allocate cost and budgets | Two-way door | `cost-allocation-policy.xlsx` | Ch8, Ch20, Ch32, Ch38, Ch41 |
| D-27 | Set reliability and DR tier | Two-way door | `service-tier-and-dr-contract.md` | Ch11, Ch14, Ch32, Ch36, Ch46 |
| D-28 | Define incident containment authority | Two-way door | `incident-command-and-resume-runbook.md` | Ch16, Ch21, Ch37, Ch40, Ch48 |
| D-29 | Standardise onboarding and changes | Two-way door | `onboarding-contract-and-exception-ledger.md` | Ch6, Ch19, Ch31, Ch35, Ch39, Ch45 |
| D-30 | Retire use cases and the Fabric | One-way door | `retirement-certificate-and-exit-plan.md` | Ch21, Ch34, Ch40, Ch49, Ch50, Ch57 |

## F1 master pages

### D-01: Adopt a shared Fabric

**Context.** Multiple use cases are requesting overlapping tool, identity and verification controls, but a shared service creates recurring operational obligations.

**Default.** Default to domain-local delivery until at least two funded production use cases need the same control contracts and a positive shared-cost case is evidenced.

**Why.** A shared Fabric introduces support cost before it creates benefit. Count duplicated controls and onboarding time, then compare measured or labelled synthetic unit costs against operating overhead.

**Trade-off.** This buys coherent controls and reuse at the cost of platform operations.

**When to deviate.**
- One isolated use case.
- Hard contractual segregation.
- No confirmed shared-control demand.

**Reversibility.** Two-way door.

**Artefact.** `fabric-adoption-adr.md`.

**See also.** Chapter 1; Chapter 4; Chapter 5; Chapter 24; Chapter 41.

### D-02: Select build, buy, embed or partner

**Context.** An enterprise must choose which capability it owns and which risks a provider may carry.

**Default.** Default to embedding bounded SaaS-native tasks and extending governed shared integration only where cross-system control warrants it.

**Why.** The sourcing choice follows the location of control and evidence requirements. A provider must support access, audit export, testability and exit before it can replace the shared substrate.

**Trade-off.** This buys faster delivery for bounded tasks at the cost of supplier dependence.

**When to deviate.**
- Cross-domain side effects require custom admission.
- Provider cannot export audit evidence.
- Hard residency constraint prevents embedding.

**Reversibility.** Two-way door.

**Artefact.** `sourcing-options-adr.md`.

**See also.** Chapter 4; Chapter 5; Chapter 24; Chapter 41; Chapter 50; Chapter 54.

### D-03: Choose a central, federated or hybrid model

**Context.** Shared controls and domain outcomes need distinct accountable owners.

**Default.** Default to a hybrid model with central control contracts and domain-owned use cases.

**Why.** Domain owners can validate business correctness; central teams can enforce common security and SLO contracts. Neither competence eliminates the need for a formal escalation path.

**Trade-off.** This buys reuse without removing domain ownership at the cost of coordination overhead.

**When to deviate.**
- Tiny portfolio with one domain.
- Legal segregation requires fully independent operating entities.
- No central service funding.

**Reversibility.** Two-way door.

**Artefact.** `operating-model-adr.md`.

**See also.** Chapter 3; Chapter 6; Chapter 24; Chapter 35; Chapter 41.

### D-04: Choose tenant isolation

**Context.** A use case must not read, write, bill or audit another tenant's work.

**Default.** Default to pooled compute with isolated identities, context, memory, evidence and policy partitions, subject to negative tests.

**Why.** Isolation must be verified at retrieval, cache, queue and tool boundaries. Dedicated compute is not automatically equivalent to end-to-end data isolation.

**Trade-off.** This buys resource efficiency at the cost of more demanding logical-isolation proof.

**When to deviate.**
- Contract requires dedicated infrastructure.
- Threat model shows unmitigated co-residency.
- Residency boundaries cannot be enforced within a pool.

**Reversibility.** Two-way door.

**Artefact.** `tenant-isolation-adr.md`.

**See also.** Chapter 3; Chapter 7; Chapter 11; Chapter 13; Chapter 21; Chapter 28; Chapter 43.

### D-05: Set the autonomy envelope

**Context.** Business impact varies by action, data and reversibility rather than product marketing labels.

**Default.** Default to read-only or human-approved side effects until task-specific evidence supports greater autonomy.

**Why.** Autonomy is permission to select and perform actions within limits. Promotion needs behavioural assertions, owner approval and requalification after relevant change.

**Trade-off.** This buys bounded blast radius at the cost of review latency.

**When to deviate.**
- Verified reversible low-risk actions qualify for unattended execution.
- Regulation requires stricter approval.
- New tool increases action risk.

**Reversibility.** Two-way door.

**Artefact.** `autonomy-envelope.yaml`.

**See also.** Chapter 2; Chapter 9; Chapter 19; Chapter 25; Chapter 30; Chapter 44.

### D-06: Allocate Fabric and domain ownership

**Context.** A shared Fabric cannot be accountable for every domain's task outcome.

**Default.** Default to shared Fabric ownership of reusable controls and domain ownership of use-case outcomes and assertions.

**Why.** The boundary matches who has technical control and who can judge business correctness. Shared tooling remains a service with an owner and documented escalation.

**Trade-off.** This buys clear responsibility at the cost of negotiated interface contracts.

**When to deviate.**
- Single team owns Fabric and one use case.
- Joint regulated product needs a formally shared accountable owner.

**Reversibility.** Two-way door.

**Artefact.** `ownership-raci.md`.

**See also.** Chapter 3; Chapter 6; Chapter 25; Chapter 35; Chapter 45.

### D-07: Select execution isolation

**Context.** Agents may run code, handle untrusted content or trigger work with different impacts.

**Default.** Default to ephemeral, policy-constrained workers for execution with side effects or untrusted code.

**Why.** The isolation level follows risk, not the agent's label. Worker identity and files must be cleared before reuse; escape and reuse tests prove the contract.

**Trade-off.** This buys stronger containment at the cost of worker start and operating overhead.

**When to deviate.**
- Pure read-only routing needs no sandbox.
- Contract requires dedicated tenant worker.
- Trusted deterministic job permits a restricted process.

**Reversibility.** Two-way door.

**Artefact.** `execution-isolation-profile.yaml`.

**See also.** Chapter 10; Chapter 11; Chapter 26; Chapter 42.

### D-08: Set runtime limits and scaling signals

**Context.** Unbounded retries can exhaust budget while queue delays evade CPU alarms.

**Default.** Default to explicit step, wall-time, token and tool limits, with autoscaling driven by queue age and saturation.

**Why.** The Harness can stop work only if the execution envelope contains limits. A queue-aware signal reflects user impact that CPU alone may not show.

**Trade-off.** This buys predictable resource exposure at the cost of rejecting some long-running requests.

**When to deviate.**
- Long-horizon job requires approved checkpointing.
- Batch processing has a different queue-time objective.
- Provider quota is the immediate bound.

**Reversibility.** Two-way door.

**Artefact.** `workload-budget-and-capacity.yaml`.

**See also.** Chapter 11; Chapter 14; Chapter 36; Chapter 46.

### D-09: Version tool contracts

**Context.** A tool request can remain syntactically valid after its meaning changes.

**Default.** Default to registered, version-pinned input/output schemas and explicit side-effect classifications.

**Why.** Descriptions influence tool selection, while schemas constrain invocation. A contract change therefore needs both argument tests and behavioural assertions.

**Trade-off.** This buys repeatable integration at the cost of version maintenance.

**When to deviate.**
- Emergency vendor patch requires a short-lived compatibility adapter.
- Legacy protocol has no schema but can be wrapped.

**Reversibility.** Two-way door.

**Artefact.** `tool-contract-registry.yaml`.

**See also.** Chapter 12; Chapter 22; Chapter 39; Chapter 53.

### D-10: Authorise mutable tool actions

**Context.** A generated tool intent is not permission to change an external system.

**Default.** Default to Gateway-enforced action authorisation with a signed, scoped receipt and idempotency key before every external mutation.

**Why.** The PEP checks tenant, actor chain, resource scope, risk and approval. Tooling may execute only after successful validation and must log the resulting side effect.

**Trade-off.** This buys defensible action boundaries at the cost of policy-check latency.

**When to deviate.**
- A read-only call has an approved reduced policy path.
- Bulk action uses a separately authorised bounded batch.
- Emergency operations require recorded break-glass review.

**Reversibility.** Two-way door.

**Artefact.** `action-authorisation-contract.json`.
**See also.** Chapter 12; Chapter 15; Chapter 16; Chapter 27; Chapter 48.

### D-11: Control retrieval access

**Context.** Retrieved context can expose records the original user could not open.

**Default.** Default to ACL-aware retrieval, source-level provenance and policy rechecks before context is consumed.

**Why.** Retrieval is an access decision as well as a relevance operation. Cache and index results must preserve tenant and data-class constraints.

**Trade-off.** This buys enforceable access at the cost of additional filtering and missed matches.

**When to deviate.**
- A public knowledge corpus carries no personal data.
- An explicit data-sharing contract authorises a limited cross-tenant lookup.

**Reversibility.** Two-way door.

**Artefact.** `retrieval-policy-and-test-suite.md`.

**See also.** Chapter 7; Chapter 13; Chapter 21; Chapter 28; Chapter 43.

### D-12: Govern durable memory

**Context.** Persisted facts can become stale, contradictory or subject to deletion obligations.

**Default.** Default to no durable memory write without provenance, policy classification, owner, retention and verification status.

**Why.** A successful answer is not itself evidence that a fact is correct. Each write must carry its source and allow correction or deletion across derived stores.

**Trade-off.** This buys accountable recall at the cost of write-path verification and maintenance.

**When to deviate.**
- Transient task state does not warrant long-term retention.
- Statutory record must be retained under an explicit legal policy.

**Reversibility.** Two-way door.

**Artefact.** `memory-write-contract.json`.

**See also.** Chapter 13; Chapter 21; Chapter 34; Chapter 49.

### D-13: Enable cross-agent memory

**Context.** Shared context can transmit another agent's authority or unverified conclusions.

**Default.** Default to signed, policy-brokered handoff packets with bounded sharing; do not share unrestricted mutable memory.

**Why.** Agents need the provenance and intended audience of a fact, not another agent's credentials. Handoffs reference data under the receiving tenant's policy.

**Trade-off.** This buys controlled collaboration at the cost of handoff validation and duplication.

**When to deviate.**
- A public read-only mission blackboard is sufficient.
- Hard tenant separation forbids cross-agent sharing.

**Reversibility.** Two-way door.

**Artefact.** `cross-agent-handoff-schema.json`.

**See also.** Chapter 13; Chapter 14; Chapter 15; Chapter 21.

### D-14: Reconcile semantic identities

**Context.** Different sources may name the same entity or disagree on its status.

**Default.** Default to canonical IDs with source lineage and explicit unresolved-conflict states; never silently choose the newest record as truth.

**Why.** Context owns the entity match and conflict record. The domain data owner defines precedence, while Verification tests that a blocked conflict does not lead to a side effect.

**Trade-off.** This buys consistent meaning at the cost of stewardship and escalations.

**When to deviate.**
- Authoritative source has published precedence rules.
- A disposable unlinked context item needs no canonical entity.

**Reversibility.** Two-way door.

**Artefact.** `semantic-reconciliation-record.json`.

**See also.** Chapter 13; Chapter 18; Chapter 22; Chapter 28.

### D-15: Choose orchestration and resume strategy

**Context.** Multi-step work must survive retries and interruption without duplicating actions.

**Default.** Default to a single Harness owning the trajectory, checkpoint and bounded step policy, with renewed authorisation on resume.

**Why.** Execution engines return observations; they do not own the task's permission state. Checkpoints capture progress, not an everlasting grant.

**Trade-off.** This buys recoverability at the cost of checkpoint and idempotency design.

**When to deviate.**
- Single deterministic request needs no durable checkpoint.
- Business workflow engine already supplies a governed process boundary.

**Reversibility.** Two-way door.

**Artefact.** `harness-state-machine.md`.

**See also.** Chapter 11; Chapter 14; Chapter 15; Chapter 36.

### D-16: Require human approval

**Context.** High-impact actions need an authorised human decision at the correct time.

**Default.** Default to explicit approval for irreversible, financial or sensitive external mutations unless Governance has approved a narrower low-risk envelope.

**Why.** A human must see the proposed action, target, context and expiry. Approval is bound to one action or bounded batch; an expired approval cannot be replayed.

**Trade-off.** This buys accountability at the cost of queue delay and operational staffing.

**When to deviate.**
- Reversible low-value action passes an approved autonomous limit.
- Emergency break-glass is required with enhanced logging.

**Reversibility.** Two-way door.

**Artefact.** `approval-envelope-and-sla.yaml`.

**See also.** Chapter 2; Chapter 9; Chapter 14; Chapter 19; Chapter 30.

### D-17: Route and fail over models

**Context.** Model providers differ in quality, cost, latency, location and availability.

**Default.** Default to risk- and quality-constrained routing, with provider failover only inside preapproved data and evaluation boundaries.

**Why.** A cheaper route can cost more after retries. Model changes may also alter tool selection and must pass the same assertion gates as other changes.

**Trade-off.** This buys resilience and cost control at the cost of more comparison tests and routing policy.

**When to deviate.**
- Residency or contract restricts to one provider.
- High-risk task requires pinned model and no silent failover.

**Reversibility.** Two-way door.

**Artefact.** `model-routing-policy.yaml`.

**See also.** Chapter 8; Chapter 16; Chapter 20; Chapter 39; Chapter 47.

### D-18: Prove Gateway non-bypassability

**Context.** A gateway control plane is ineffective if tools can call external targets directly.

**Default.** Default to mandatory PEP checks on mutable external actions, enforced by credentials, routing policy and egress controls.

**Why.** Architecture diagrams are insufficient proof. A denial and direct-bypass negative test must show that unapproved side effects cannot succeed.

**Trade-off.** This buys enforceable admission at the cost of proxy dependencies and outage planning.

**When to deviate.**
- Restricted offline worker cannot reach external systems.
- An explicitly approved trusted path implements equivalent PEP controls.

**Reversibility.** One-way door.

**Artefact.** `gateway-bypass-proof.md`.

**See also.** Chapter 10; Chapter 12; Chapter 16; Chapter 27; Chapter 42.

### D-19: Manage human and agent identity

**Context.** A user session and an agent workload are distinct actors with different lifecycles.

**Default.** Default to separate authenticated identities, short-lived workload credentials and tenant-bound claims.

**Why.** Workload credentials must not inherit all permissions from an interactive user. Attestation and revocation bind the work to a recognised executable.

**Trade-off.** This buys scoped, auditable authority at the cost of token issuance and identity infrastructure.

**When to deviate.**
- Fully offline no-action experiment.
- Legacy non-interactive integration requires temporary wrapper and dated migration.

**Reversibility.** Two-way door.

**Artefact.** `identity-registry-and-claims.yaml`.

**See also.** Chapter 15; Chapter 19; Chapter 27; Chapter 40.

### D-20: Control delegation chains

**Context.** An agent may ask another agent or tool to act on its behalf.

**Default.** Default to signed, audience-bound, expiring delegation with monotonically narrowing permissions at each hop.

**Why.** The next actor receives no more authority than the originator and intermediaries permit. Gateway verifies the effective scope and Observability retains the actor chain reference.

**Trade-off.** This buys traceable collaboration at the cost of token validation and handoff latency.

**When to deviate.**
- No delegation exists in a single-agent read-only task.
- Contract prohibits delegated execution and requires direct user approval.

**Reversibility.** One-way door.

**Artefact.** `delegation-chain-proof.json`.

**See also.** Chapter 14; Chapter 15; Chapter 16; Chapter 40.

### D-21: Version interoperability contracts

**Context.** Messages can be valid at transport level while omitting authorisation or business meaning.

**Default.** Default to boundary-specific, version-pinned protocol contracts with conformance and downgrade tests.

**Why.** Interoperability owns protocol compatibility; Context owns business meaning. Gateway enforces protocol admission, but a successful handshake is not a semantic guarantee.

**Trade-off.** This buys controlled provider portability at the cost of compatibility testing and registry maintenance.

**When to deviate.**
- Legacy endpoint requires versioned adapter.
- Regulation bars a proposed transport.
- New specification is unverified.

**Reversibility.** Two-way door.

**Artefact.** `protocol-boundary-registry.md`.

**See also.** Chapter 12; Chapter 22; Chapter 39; Chapter 53.

### D-22: Select verification strategy

**Context.** A model can appear helpful while violating a required business or security action rule.

**Default.** Default to task and risk-specific behavioural assertions, trajectory checks and negative tests before approval.

**Why.** Aggregate answer quality cannot prove that a prohibited action never occurs. Evaluation evidence must tie dataset version, test runner, model and tool schema to the result.

**Trade-off.** This buys stronger release confidence at the cost of dataset upkeep and execution time.

**When to deviate.**
- Read-only low-risk task uses reduced regression set.
- Regulated mutation requires independent expert review.

**Reversibility.** Two-way door.

**Artefact.** `verification-matrix-and-fixtures.md`.

**See also.** Chapter 9; Chapter 13; Chapter 18; Chapter 33; Chapter 47.

### D-23: Set release and autonomy gates

**Context.** Production changes can invalidate prior evaluation and accepted autonomy.

**Default.** Default to fail-closed promotion for failed critical assertions, with signed gate evidence and an executable rollback plan.

**Why.** The release gate inspects changed prompts, models, tools, context and policy. Passing a mean score never overrides a failing hard-block assertion.

**Trade-off.** This buys bounded change risk at the cost of release lead time.

**When to deviate.**
- Emergency rollback to last verified version.
- Safety patch follows documented emergency path with post-release evidence.

**Reversibility.** Two-way door.

**Artefact.** `release-gate-report.md`.

**See also.** Chapter 9; Chapter 18; Chapter 30; Chapter 33; Chapter 39; Chapter 47.

### D-24: Design telemetry and evidence retention

**Context.** An audit must connect who requested an action, why it was allowed, what executed and how it ended.

**Default.** Default to shared correlation identifiers and access-controlled evidence envelopes with explicit retention classes.

**Why.** Observability captures events; it does not make policy decisions. Sensitive payload logging needs minimisation, redaction and retention rules.

**Trade-off.** This buys reconstructable trajectories at the cost of storage and privacy governance.

**When to deviate.**
- Low-risk read-only use case can use sampled diagnostics.
- High-risk regulated action requires complete action evidence.

**Reversibility.** Two-way door.

**Artefact.** `evidence-envelope-schema.json`.

**See also.** Chapter 17; Chapter 21; Chapter 36; Chapter 40; Chapter 57.

### D-25: Choose data residency and protection

**Context.** Data moves through retrieval, model calls, tools, memories, logs and backups.

**Default.** Default to classification-led location and retention rules that cover every derived store and provider boundary.

**Why.** A storage-region setting is not proof of end-to-end residency. Data Protection must identify processors, temporary caches, legal holds and deletion obligations.

**Trade-off.** This buys defensible handling of regulated data at the cost of processing restrictions and lifecycle work.

**When to deviate.**
- Anonymised public corpus has reduced obligations.
- Contract mandates stricter location or encryption.
- Legal hold suspends normal deletion.

**Reversibility.** One-way door.

**Artefact.** `data-protection-and-residency-record.md`.

**See also.** Chapter 7; Chapter 13; Chapter 21; Chapter 27; Chapter 55.

### D-26: Allocate cost and budgets

**Context.** Multi-tenant model and tool charges must be allocated to outcomes and owners.

**Default.** Default to tenant, use-case and trajectory-level showback based on cost per successful task, with budgets and invoice reconciliation.

**Why.** Token charges omit retries, tool calls, compute and shared overhead. Finance needs visibility into failed tasks as well as successful ones.

**Trade-off.** This buys unit-economic accountability at the cost of attribution engineering.

**When to deviate.**
- Small pilot uses temporary showback only.
- Regulated contract prescribes a fixed-cost recovery model.

**Reversibility.** Two-way door.

**Artefact.** `cost-allocation-policy.xlsx`.

**See also.** Chapter 8; Chapter 20; Chapter 32; Chapter 38; Chapter 41.

### D-27: Set reliability and DR tier

**Context.** Different use cases tolerate different interruption, recovery and data-loss windows.

**Default.** Default to risk-tiered SLOs, queue-age/quality signals, tested RTO/RPO and approved degradation modes.

**Why.** A model call that returns HTTP 200 may still fail the business task. Recovery must preserve checkpoints without reusing expired authorisation.

**Trade-off.** This buys continuity matched to need at the cost of standby capacity and testing.

**When to deviate.**
- Non-critical batch allows delayed recovery.
- Irreversible task requires tighter proof.
- Outsourced SaaS constrains achievable RTO.

**Reversibility.** Two-way door.

**Artefact.** `service-tier-and-dr-contract.md`.

**See also.** Chapter 11; Chapter 14; Chapter 32; Chapter 36; Chapter 46.

### D-28: Define incident containment authority

**Context.** Bad actions or compromised context demand immediate but accountable containment.

**Default.** Default to SRE-led incident command with Security authority for containment of risk-bearing credentials, egress and tainted memory.

**Why.** The on-call commander must be able to suspend execution and preserve evidence. Restart occurs only after risk owner sign-off and a safe-resume test.

**Trade-off.** This buys rapid containment at the cost of occasional service interruption.

**When to deviate.**
- Low-severity quality defect uses ordinary rollback.
- Regulatory notification obligations impose additional legal steps.

**Reversibility.** Two-way door.

**Artefact.** `incident-command-and-resume-runbook.md`.

**See also.** Chapter 16; Chapter 21; Chapter 37; Chapter 40; Chapter 48.

### D-29: Standardise onboarding and changes

**Context.** The portfolio grows faster than bespoke approval and deployment processes can scale.

**Default.** Default to approved archetypes, automated contract tests, named domain owners and time-limited exceptions.

**Why.** Repeatable onboarding should reuse verified controls without granting extra permissions. Changes that alter a boundary renew the relevant approval and regression set.

**Trade-off.** This buys faster, consistent onboarding at the cost of a managed template catalogue.

**When to deviate.**
- Novel regulated use case requires a new archetype.
- Vendor-native pilot requires separate but equivalent gate.

**Reversibility.** Two-way door.

**Artefact.** `onboarding-contract-and-exception-ledger.md`.

**See also.** Chapter 6; Chapter 19; Chapter 31; Chapter 35; Chapter 39; Chapter 45.

### D-30: Retire use cases and the Fabric

**Context.** Stopping execution leaves credentials, memory, evidence, vendor contracts and legal obligations behind.

**Default.** Default to a formal retirement gate proving token revocation, data disposition, preserved obligations and tested export or migration.

**Why.** The identity, context and telemetry stores do not share one deletion command. Each owner must record disposal, archival or legal hold against a common inventory.

**Trade-off.** This buys safe closure and portability at the cost of exit rehearsals and retention administration.

**When to deviate.**
- Legal hold prevents a specified deletion.
- Phased migration requires dual running.
- Decommission is delayed by unresolved data ownership.

**Reversibility.** One-way door.

**Artefact.** `retirement-certificate-and-exit-plan.md`.

**See also.** Chapter 21; Chapter 34; Chapter 40; Chapter 49; Chapter 50; Chapter 57.

**Decision-page production gate:** validate thirty unique IDs, thirty artefacts, thirty exact F1 heading sequences, one-to-many decision-to-chapter cross-references and thirty actual one-page print proofs. Attach a unique ADR owner and decision review date to each completed use-case example even though those fields are not part of F1 itself.

# Phase 6. Ten immediately writable playbooks

The following is the *full authoring contract* for Chapters 41–50. Each procedure uses S F2, its story uses F5, and its action table specifies owner, input, output and indicative execution time. Times are **planning assumptions**, not observed Meridian operating data. Each owner can complete the step without consulting another chapter; chapter links provide explanation, not missing instructions. Every playbook includes an abort or escalation branch. In final prose, write the F5 war story at 150–300 words, third-person past, with no more than three named characters and a closing artefact connection.

## P1. Build the Business Case — Chapter 41

**Objective.** Decide whether a shared Fabric deserves funding and specify its commercial exit criteria.

**When to use.** Before authorising a shared Fabric or when an existing portfolio seeks material growth funding. **Trigger:** repeated use-case demand or high duplicated control spend. **Actors:** Eleanor (decision), Maya (delivery), Priya (economics), Ruth (risk), Tomas (demand owner).

**Preconditions.** Inventory at least four candidate use cases; obtain spend assumptions and provider terms; identify data/risk owners; distinguish actual observations from synthetic scenario data.

**War story.** Week 2: Eleanor refuses to approve the fifth pilot on a demo slide. Maya returns with duplicate integration costs, and Priya separates fixed control costs from model variable costs. The incident ends with the sourcing-option ADR on the approval agenda. Target 180–220 words. **Meridian event:** M0 Week 2.

**Steps.**

| # | Action | Owner | Input | Output | Planning time |
|---|---|---|---|---|---|
| 1 | Register use cases, owners, risk classes and shared control needs | Maya | Demand interviews | Use-case inventory | 1 day |
| 2 | Quantify baseline and target cost, including evaluation, on-call, security and retirement | Priya | Spend, usage, support assumption | Three-scenario total-cost workbook | 2 days |
| 3 | Compare build, buy, embed and partner against enforceability, evidence and portability | Maya | Contract terms, controls | Options appraisal | 1 day |
| 4 | Record threats and supplier obligations, including failure to export evidence | Ruth | Options appraisal | Risk and sourcing exclusions | 1 day |
| 5 | Run break-even and downside sensitivities; identify the stop-build case | Priya | Cost workbook | Finance decision note | 1 day |
| 6 | Record funding decision, owner, evidence threshold and review date | Eleanor | Complete pack | Approved or rejected D-01/D-02/D-03 | 1 meeting |

**Failure modes.** Demand forecast unsupported → reject appraisal; hidden support costs → return to step 2; evidence-export impossible → remove provider option; no accountable service owner → stop before step 6.

**The artefact you now have.** `business-case-v1.xlsx`, `sourcing-options-adr.md`, `risk-exclusions.md`, `funding-decision.md`.

**The decision you must record.** Approve, defer or reject the shared Fabric, with a reversibility class and a funded operating owner.

## P2. Design the Reference Architecture — Chapter 42

**Objective.** Convert approved requirements into one enforceable, versioned design with no ambiguous owner.

**When to use.** After P1 approval or before a major Fabric redesign. **Trigger:** signed scope and risk envelope. **Actors:** Maya, Ruth, Samir, Tomas; Priya signs cost constraints.

**Preconditions.** Accepted D-01–06, use-case risk cards, tenant profiles, candidate interfaces and accepted business SLAs.

**War story.** Maya draws the first action path. Ruth asks who can verify that the tool cannot bypass a delegated user's scope. The meeting shifts from component labels to one end-to-end denial receipt. The result is the policy-enforcement map. Target 180–220 words. **Meridian event:** M1 Week 5.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Allocate E/T/C/L and eight control-plane owners | Maya | Scope, Ch10 contract | Responsibility map | 0.5 day |
| 2 | Draw context, container, layer-stack and trust-boundary diagrams under H2 | Maya | Data/use-case flows | Versioned figures | 2 days |
| 3 | Define actor-chain, action receipt, context manifest and trajectory schemas | Ruth and Maya | Risk decisions | Interface contracts | 2 days |
| 4 | Mark each PEP and write direct-bypass denial tests | Ruth | Call paths | Threat-to-PEP map | 1 day |
| 5 | Specify SLO, unit-economics assumptions and recovery classes | Samir and Priya | Service targets | NFR sheet | 1 day |
| 6 | Conduct architecture and risk review; record exceptions and baseline versions | Maya | Complete design | Accepted design baseline | 1 meeting |

**Failure modes.** A new ninth plane appears → reject diagram; bypass path lacks a PEP → block sign-off; revocation not testable → return to step 3; unowned evidence → return to step 1.

**The artefact you now have.** `fabric-hld.md`, `boundary-map.svg`, `control-contracts/`, `architecture-adrs/`, `security-tests.md`.

**The decision you must record.** Accept the canonical design baseline and all explicit deviations from D-07–22.

## P3. Stand Up the Tenant Substrate — Chapter 43

**Objective.** Make tenant identity, context, state, evidence and cost partitions provable before the first production use case.

**When to use.** Before onboarding a tenant or moving a tenant into pooled infrastructure. **Trigger:** approved tenant isolation ADR. **Actors:** Maya, Ruth, Samir, Priya, domain data steward.

**Preconditions.** Tenant ID, risk class, data locations, retention schedule, scoped identities, test fixtures and isolation-profile owner.

**War story.** A staging retrieval returns an insurance record to a retail test session. The team does not reclassify the incident as a harmless search error. The tenant readiness certificate is withheld until the full cache path is corrected. Target 180–220 words. **Meridian event:** M2 Week 7.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Select pooled, segmented or hard-isolated tenant profile | Ruth | Risk/contract | Isolation ADR | 0.5 day |
| 2 | Create tenant identities, namespaces, encryption and data-store scopes | Maya | Profile | Tenant manifest | 1 day |
| 3 | Provision memory, retrieval, queues, evidence and budget partitions | Maya and Priya | Manifest | Partition inventory | 1 day |
| 4 | Run positive/negative tests across retrieval, caches, tools, telemetry and worker reuse | Ruth | Synthetic fixtures | Test result pack | 1 day |
| 5 | Verify retention, residency, revocation and fail-closed behaviour | Ruth | Protection rules | Protection proof | 0.5 day |
| 6 | Accept tenant for pilot or quarantine it with remediation owner | Samir | Evidence pack | Readiness certificate | 0.5 day |

**Failure modes.** Mixed-tenant retrieval → block; logs contain raw personal data → quarantine evidence; worker retains prior identity → deny reuse; charge cannot be attributed → block production accounting.

**The artefact you now have.** `tenant-manifest.yaml`, `isolation-test-results.json`, `retention-matrix.md`, `tenant-readiness-certificate.md`.

**The decision you must record.** Accept the tenant isolation profile and required tests, or refuse onboarding.

## P4. Onboard the First Use Case — Chapter 44

**Objective.** Release one bounded use case with business, technical and security acceptance.

**When to use.** When a pilot requests production access. **Trigger:** signed domain owner and tenant readiness certificate. **Actors:** Tomas, Maya, Ruth, Samir, verification engineer.

**Preconditions.** Approved use-case owner, persona/archetype, tool list, autonomy envelope, baseline dataset, approval SLA and rollback route.

**War story.** Tomas presents payment-dispute triage as ready. The hidden test finds a contradictory policy record and the agent proceeds anyway. Tomas accepts read-only restriction; the narrower use case passes the next gate. The signed pilot dossier closes the story. Target 180–220 words. **Meridian event:** M3 Weeks 11–12.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Register use-case objective, ownership, action risk and data use | Tomas | Business process | Use-case contract | 0.5 day |
| 2 | Bind approved persona, archetype, tenant, tools and budgets | Maya | Contract | Deployment manifest | 0.5 day |
| 3 | Write task and forbidden-action behavioural assertions | Tomas and Ruth | Scenarios | Evaluation fixtures | 1 day |
| 4 | Run negative tests, business acceptance and cost/latency checks | Verification owner | Fixtures | Signed gate result | 1 day |
| 5 | Canary with bounded authority and explicit stop trigger | Samir | Approved gate | Canary observation | 1–3 days |
| 6 | Approve production, narrow autonomy, or roll back | Tomas and Ruth | Canary results | Release decision | 1 meeting |

**Failure modes.** Critical assertion fails → no promotion; tenant isolation fails → stop; action approval expires → deny action; business owner absent → release withheld.

**The artefact you now have.** `use-case-registration.yaml`, `evaluation-report.md`, `canary-report.md`, `pilot-release-dossier.md`.

**The decision you must record.** Record production go/no-go and the accepted autonomy envelope.

## P5. Scale from One to Ten Use Cases — Chapter 45

**Objective.** Convert successful pilot onboarding into a governed repeatable service.

**When to use.** When the second funded domain use case enters the pipeline. **Trigger:** P4 completed and cross-domain demand evidenced. **Actors:** Maya, Tomas, Ruth, Priya, Samir.

**Preconditions.** Passing pilot evidence, reusable identity/context/tool contracts, published pricing and on-call SLO.

**War story.** Five teams request five approval methods. Maya refuses to add five bypass paths and instead maps the requests to two approved archetypes. The onboarding catalogue becomes the authority for the next five use cases. Target 180–220 words. **Meridian event:** M5 Week 22.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Group incoming cases by action risk, tenant class and interfaces | Maya | Demand register | Archetype candidates | 1 day |
| 2 | Publish default persona, tool, tenant, verification and observability contracts | Maya | Pilot baseline | Onboarding package | 2 days |
| 3 | Implement automated negative tests and evidence collection for each package | Ruth | Contracts | Admission tests | 2 days |
| 4 | Define cost/SLO tiers and owner acknowledgement | Priya and Samir | Usage and SLO | Service catalogue | 1 day |
| 5 | Onboard in cohorts and measure time, quality and exception rate | Maya | Packages | Cohort results | Per cohort |
| 6 | Retire one-off exceptions and update standard | Ruth | Cohort results | Versioned catalogue | 0.5 day |

**Failure modes.** Template expands permissions → withdraw; exceptions have no expiry → reject; gateway saturation grows → freeze cohort; unallocated cost → stop scale claim.

**The artefact you now have.** `approved-archetypes/`, `onboarding-admission-tests/`, `service-catalogue.md`, `portfolio-report.md`.

**The decision you must record.** Approve the first standard onboarding catalogue and its exception authority.

## P6. Plan for Ten to One Hundred-Plus — Chapter 46

**Objective.** Prove whether the Fabric design can scale without weaker control or unaffordable costs.

**When to use.** At portfolio scale, before a large growth approval. **Trigger:** ten live use cases, measured saturation or strategic growth demand. **Actors:** Maya, Samir, Ruth, Priya, Eleanor.

**Preconditions.** Measured service patterns, queue/error budgets, budget forecast, tenant distribution and representative synthetic 100-plus use-case load.

**War story.** Twelve Meridian use cases are live. A proposed expansion to 100 is modelled, not deployed. Samir's load test exposes Gateway policy latency under burst conditions, so Eleanor approves capacity engineering rather than automatic expansion. Target 180–220 words. **Meridian event:** M6 Week 26.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Profile use-case classes and design peak/burst workloads | Samir | Metrics | Workload catalogue | 1 day |
| 2 | Load-test queues, Gateway PEP, identity issuance, stores and verification | Samir | Synthetic load | Capacity report | 2 days |
| 3 | Test tenant leakage, revocation and denial under saturation | Ruth | Load scenario | Security stress results | 1 day |
| 4 | Simulate cost, error budget, failover and budget caps | Priya | Capacity report | Finance sensitivity | 1 day |
| 5 | Model sharding, scale-out and policy-cache resilience | Maya | Bottlenecks | Scale architecture ADR | 2 days |
| 6 | Decide staged growth, redesign or reject expansion | Eleanor | Complete evidence | Scale decision | 1 meeting |

**Failure modes.** Bypass appears under failure → block; unbounded retries → correct Harness budget; policy cache stale → invalidate design; cost exceeds funded cap → stage expansion.

**The artefact you now have.** `scale-workload-model.csv`, `stress-test-report.md`, `capacity-adr.md`, `investment-gate.md`.

**The decision you must record.** Approve the next scale tier only with proven control latency, reliability and unit economics.

## P7. Execute a Model Upgrade — Chapter 47

**Objective.** Replace or reroute a model without losing approved behaviour or control evidence.

**When to use.** Before model/version/routing change or when provider deprecates a required route. **Trigger:** proposed provider, model or parameter change. **Actors:** Maya, verification engineer, Tomas, Ruth, Samir.

**Preconditions.** Pinned current route and datasets, complete prompt/tool/index versions, rollback image, canary limits and change owner.

**War story.** A vendor update answers faster but supplies the wrong tool argument under a cancellation scenario. The average score still looks positive. Ruth points to the one failed hard assertion, and Maya rolls the canary back. The gate report carries the decision. Target 180–220 words. **Meridian event:** M3 Week 14.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Freeze baseline and define candidate differences | Maya | Release manifest | Diff record | 0.5 day |
| 2 | Replay representative, adversarial and forbidden-action trajectories | Verification owner | Golden fixtures | Comparison matrix | 1 day |
| 3 | Check cost, latency, data locality and side-effect changes | Priya and Ruth | Comparison | Control impact | 0.5 day |
| 4 | Execute bounded canary with stop thresholds | Samir | Signed offline gate | Canary report | 1–2 days |
| 5 | Review hard assertions and revoke candidate on failure | Tomas and Ruth | Canary | Go/rollback verdict | 1 meeting |
| 6 | Update routing policy, catalogue and rollback proof | Maya | Verdict | Accepted release manifest | 0.5 day |

**Failure modes.** Critical assertion fails → block; provider residency differs → block; rollback schema incompatible → do not canary; telemetry incomplete → stop and restore baseline.

**The artefact you now have.** `model-upgrade-diff.md`, `regression-results.json`, `canary-report.md`, `release-gate-report.md`.

**The decision you must record.** Accept the exact route/version or restore the last verified baseline.

## P8. Handle a Security Incident — Chapter 48

**Objective.** Contain a suspected security breach while preserving the evidence needed to scope and safely resume.

**When to use.** On unauthorised action, context poisoning, identity misuse, tenant leak or suspected egress. **Trigger:** telemetry incident signal or verified report. **Actors:** Samir (incident commander), Ruth (security authority), Maya (technical), domain owner and records officer.

**Preconditions.** On-call roster, containment permissions, immutable evidence path, actor and tenant correlation, legal notification guidance and rehearsal history.

**War story.** An altered retrieved document instructs a tool to send customer data to an external domain. The Gateway denies the request, but Ruth does not declare the incident closed: the source record might have reached other trajectories. Samir quarantines the queue. The incident packet is the bridge to the procedure. Target 180–220 words. **Meridian event:** M4 Week 18.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Declare incident and record time, scope hypothesis and severity | Samir | Alert | Incident ID and commander | 15 min target |
| 2 | Suspend affected actions, credentials, routes and memory writes | Ruth and Maya | Incident scope | Containment receipts | Immediate once validated |
| 3 | Preserve actor chains, policy receipts, tool outcomes and context versions | Samir | Correlation IDs | Evidence custody bundle | 1 hour target |
| 4 | Determine impacted tenants, trajectories and obligations; notify authorised teams | Ruth | Evidence | Impact assessment | Risk-dependent |
| 5 | Correct source/policy/code; replay abuse and negative tests | Maya | Root cause | Recovery test report | Risk-dependent |
| 6 | Approve safe resume, close actions and schedule post-incident review | Ruth and Samir | Recovery evidence | Resume decision, PIR | After acceptance |

**Failure modes.** Evidence compromised → preserve alternate logs; scope uncertain → broaden containment; legal notice threshold reached → engage legal; test still fails → do not resume.

**The artefact you now have.** `incident-command-log.md`, `evidence-custody.json`, `scope-assessment.md`, `safe-resume-decision.md`.

**The decision you must record.** Who authorised containment and safe resumption, on which evidence.

## P9. Retire a Use Case — Chapter 49

**Objective.** Eliminate a use case's action authority while honouring data, evidence and legal obligations.

**When to use.** On product withdrawal, replacement or cessation of value. **Trigger:** domain owner-approved retirement request. **Actors:** Tomas, Maya, Ruth, Samir, data owner/records officer.

**Preconditions.** Use-case inventory, downstream dependencies, exported records, legal-hold classification and validated successor or stop plan.

**War story.** The old pilot's interface is removed, but a service account can still query a knowledge store. Tomas withholds closure until its credentials, memories and schedules are accounted for. The retirement certificate becomes the completion signal. Target 180–220 words. **Meridian event:** M6 Week 27.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Approve business cessation and identify dependent workflows | Tomas | Retirement request | Dependency inventory | 0.5 day |
| 2 | Stop ingress, queued work and scheduled triggers | Samir | Runbook | Stop proof | 0.5 day |
| 3 | Revoke actor credentials, permissions, tool routes and delegation chains | Ruth | Identity inventory | Revocation receipts | 0.5 day |
| 4 | Export or delete memory, context, logs and backups by retention class | Data owner | Retention schedule | Disposition receipts | 1–3 days |
| 5 | Run negative access and orphan-work tests; check successor continuity | Maya | Receipts | Closure tests | 1 day |
| 6 | Sign retirement, preserve legal holds and update catalogue | Tomas and Ruth | Evidence | Retirement certificate | 1 meeting |

**Failure modes.** Hidden integration remains → block; retained evidence is deleted → restore from protected archive if lawful; legal hold exists → suspend specified deletion; successor depends on old endpoint → defer closure.

**The artefact you now have.** `dependency-export.csv`, `credential-revocations.json`, `disposition-ledger.csv`, `use-case-retirement-certificate.md`.

**The decision you must record.** Confirm complete authority removal and lawful disposition, or record explicit unresolved obligations.

## P10. Retire or Replace the Fabric — Chapter 50

**Objective.** Demonstrate an executable plan to move or close all tenants without untracked authority, lost obligations or hidden dependence.

**When to use.** During strategic sourcing review, supplier exit, major contract change or full closure. **Trigger:** approved exit scenario. **Actors:** Eleanor, Maya, Ruth, Samir, Priya and domain representatives.

**Preconditions.** Current tenant inventory, provider contracts, provenance/export contracts, identity mapping, continuity obligations and funded rehearsal window.

**War story.** Eleanor asks for an exit path before renewing a major service contract. Maya does not close the running Fabric. Instead, the team runs one synthetic tenant through a parallel destination, verifies the action and audit record, and reports what cannot yet be moved. Target 180–220 words. **Meridian event:** M6 Week 28.

**Steps.**

| # | Action | Owner | Input | Output | Time |
|---|---|---|---|---|---|
| 1 | Inventory every live tenant, route, credential, state store and contract | Maya | Fabric inventory | Exit dependency register | 2 days |
| 2 | Classify retention, legal-hold, portability and successor obligations | Ruth | Records/contracts | Disposition and export rules | 2 days |
| 3 | Design tenant migration order and rollback, including actor identity transition | Samir | Dependency register | Migration runbook | 2 days |
| 4 | Rehearse one synthetic tenant, validate behaviour and audit continuity | Maya and Tomas | Test tenant | Rehearsal evidence | 2 days |
| 5 | Compare transition cost and residual risk with continue option | Priya | Tests/contracts | Exit appraisal | 1 day |
| 6 | Choose continue, migrate in cohorts or close; record go/no-go gates | Eleanor | Exit pack | Signed exit decision | 1 meeting |

**Failure modes.** Cannot export memory provenance → stop migration; successor cannot enforce delegations → block; retained records lack legal owner → leave source in controlled archive; rollback cannot reconcile queued mutations → redesign sequence.

**The artefact you now have.** `fabric-exit-register.md`, `export-mapping.json`, `migration-rehearsal-report.md`, `fabric-exit-decision.md`.

**The decision you must record.** Select an exit route with tenant order, legal obligations, continuity thresholds and a proven rollback.

## Playbook completion gate

All ten must pass these checks before manuscript lock: one F5 war story of 150–300 words; preconditions; named owner/input/output/time for every step; at least one abort path; completed Meridian artefact; one explicit F2 final decision. A step is incomplete if its action cannot be performed without unexplained knowledge from elsewhere in the book. Each playbook's specimen outputs are printed in Ch57 or cross-referenced to an equally complete appendix.

# Phase 7. The first two chapters to write

## 7.1 Exact sequence and acquisition purpose

**Write first: Chapter 16, Gateway Control Plane.** This is the first publisher sample. Its reader promise is concrete: determine whether the Fabric can prevent an unauthorised external mutation, rather than merely log one. It demonstrates enforceable control-plane ownership, a failure path, a threat-to-PEP mapping, a denial receipt and a reusable decision page. It can stand alone with a two-page prerequisite summary of the canonical E/T/C/L model. The differentiation is a *testable authorisation boundary*, not a list of protocols.

**Write second: Chapter 13, Context.** This is the companion publisher sample. Its reader promise is equally concrete: reconcile disagreeing evidence, keep memory and retrieval under tenant policy, and prove that a durable context write can be traced or deleted. It demonstrates the deeper semantic/memory architecture without inventing an extra control plane. Together, the samples cover the two most distinctive enterprise problems: **authority over action** and **authority over knowledge**. Ch16 should be structurally accepted before Ch13 is drafted so the Context chapter can reference the locked actor-chain and action-gate contract.

**Selection criteria:** architectural mechanism, portable design, actual failure and recovery, an immediately usable artefact, a credible fictional scenario, clear linkage to F1 decision pages, and minimal dependency on vendor-specific implementation. Do not use the transcript as proof of any commercial vendor's internal memory implementation.

### Sample publication package

- Sample A: Ch16, 6–7 typeset pages, F7 exact headings, two diagrams, one action receipt, three F4 anti-patterns, D-10/D-18 excerpts and a compact Meridian evidence trail.
- Sample B: Ch13, eight typeset pages, F6 exact headings, three diagrams, two policy-bearing data examples, conflict resolution and memory retention/erasure sequence, D-11–14 excerpts.
- Submission preface: one page defining Fabric, use case, agent, persona, archetype and the four layers/eight planes. This is context for the samples, not a substitute chapter.
- Technical reviewer question: after these chapters, can a reader identify who has authority, where it is enforced, how failure is contained and which proof to retain?

## 7.2 Chapter 16 full subsection-level writing outline (F7)

**Title:** Chapter 16 — Gateway Control Plane. **Target:** 6.5 pages, approximately 2,100–2,500 finished words subject to actual typesetting. **Register:** mechanism-first third person. **Narrative:** one failure hook, no more than 150 words, preferably 90–120. **Primary decision records:** D-10 and D-18; secondary D-17, D-20 and D-21. **Principal source sections:** R13, 18, 25A–25B, 26, 31–32, 34–37; B13, 15.

### Opening hook (90–120 words)

- Meridian Week 5. Ruth learns that an agent with an apparently limited persona can call a tool using a shared technical credential.
- Show the operational consequence: no reliable association between requesting human, agent, risk approval and external mutation.
- Close on the artefact: the team must produce a non-bypassable action-authorisation contract.
- Keep dialogue to one brief exchange and end with the named contract; no explanations of MCP or token internals in the vignette.

### What this layer decides (one sentence; retain the exact F6 heading inherited by F7)

- The Gateway Control Plane decides whether a model, tool, agent-to-agent or egress request may cross an enforced boundary, using policy and identity claims owned elsewhere.

### The mechanism (two pages)

#### 16.1 The distinction between control plane and policy enforcement point
- Define policy authoring (Governance), actor claims (Identity), admission decision (Gateway), and operation execution (Tooling).
- Separate logical Gateway Control Plane from deployable model proxy, tool proxy, A2A router and network egress PEP.
- Figure 16-1: Gateway enforcement topology. Limit to ten nodes and at most 16 labelled edges. Nodes: user, Harness, Identity, policy decision, tool PEP, model PEP, egress PEP, Tooling adapter, external system, evidence store. Show authorisation and evidence flows.
- Table 16-1: component; owns; input; rejects; emits. Every row maps to one named owner.

#### 16.2 The action-authorisation receipt
- Present a **synthetic** JSON example: `tenant_id`, `run_id`, `actor_chain_hash`, `action_id`, `tool_id`, `resource_scope`, `policy_version`, `approval_ref`, `issued_at`, `expires_at`, `idempotency_key`, `decision`, `receipt_signature`.
- Define which fields the Tooling adapter must bind to the physical external request.
- Show allowed, denied, expired and revoked states; deny any missing signature or wrong audience.
- Table 16-2: condition → Gateway decision → evidence record.

#### 16.3 Write-path and read-path separation
- Use a read-only knowledge lookup to show a reduced-risk admission path; ACL and data protection still apply.
- Use a payment/refund mutation to show mandatory human approval where configured, tool risk class and idempotency.
- Explain why a preapproved model response is not an authorisation for a tool call.

#### 16.4 Enforcing non-bypassability
- Define technical controls: tool credentials are reachable only through authorised adapters; outbound routes cannot avoid network PEP; side-effect endpoints reject unbound service identity.
- Negative tests: direct endpoint call, forged receipt, expired token, changed resource ID, cross-tenant target, delayed queue replay and unavailable policy service.
- Show a fail-closed write and a separately approved degraded read path.

#### 16.5 Model and agent-to-agent routing
- Route within preapproved model region, price and verification policy; do not silently move data across regions.
- On A2A handoff, check protocol compatibility and delegated chain. Model/protocol routers do not own the delegation token.
- State which protocol facts require date/version research before publication; avoid claiming that a transport standard supplies authorisation semantics absent in its published contract.

### Threat coverage (approximately half a page)

#### 16.6 Trust-chain points covered
- Map identity intake, delegated action, tool invocation, egress and tool response to named PEPs.
- OWASP/other standards are added only after the research editor verifies their current version and actual category definitions.
- Table 16-3: threat → enforcement point → negative test → retained evidence; include a bypass and policy-cache-staleness case.

### Failure modes (approximately half a page)

#### 16.7 Failure table
- Columns: failure, cause, symptom, control, safe mode, evidence owner.
- Rows: policy service unavailable; scope mismatch; identity revocation; external side effect executes but response times out; duplicate retry; connector bypass; stale policy cache.
- Show one nontrivial point: tool failure after an external mutation requires reconciliation, not blind retry.

### Enforcement point (approximately half a page)

#### 16.8 Request sequence and load signals
- Figure 16-2: sequence of Harness intent → Identity proof → Gateway verdict → Tooling invocation → receipt → Observability evidence. Eight actors maximum.
- Set example *proposed* SLO targets as design variables, not industry facts; `policy_decision_latency_p99`, `denial_completeness`, `bypass_test_pass_rate`, `stale_policy_decisions`, `revocation_propagation_time`.
- Distinguish scaling signals from authorisation criteria. If a PEP is overloaded, it may deny requests; it may never silently omit checking them.

### Evidence artefact (approximately a quarter page)

#### 16.9 Verifying one denied action
- Reconstruct a single synthetic action using `run_id`, `actor_chain_id`, `action_id`, policy version and deny receipt.
- Show sample audit rows for request, rejection, attempted direct bypass, network refusal and closure.
- Figure/table requirement: evidence report must reconcile to the same tenant and action IDs as Chapter 15.

### Anti-patterns (approximately half a page; exact F4 entries)

#### 16.10 AP-16-01: Gateway only in the diagram
- Direct endpoint bypass succeeds; detection signal is any successful side effect without a Gateway receipt; fix with identity/egress enforcement and a negative test.

#### 16.11 AP-16-02: Policy in prompts
- Prompt requests restraint but tool credentials permit mutation; detection signal is unbound side-effect receipt; fix with Gateway policy and tool-scoped identity.

#### 16.12 AP-16-03: Gateway as permanent superuser
- Proxy forwards an overprivileged service token; detection signal is privilege beyond actor-chain intersection; fix with short-lived action-bound credentials.

### Decisions to make (3–7 bullets; mandatory closing block)
- Select the PEP placement for each mutable external action, D-18.
- Define the authorisation receipt and failure modes, D-10.
- Define the approved model route and fallback envelope, D-17.
- Define the protocol version contract for Gateway boundaries, D-21.

### Defaults (matched one-to-one)
- Every mutable external action crosses verified PEP enforcement.
- Deny absent, invalid or expired action receipts.
- Route only within approved risk, quality and residency limits.
- Pin and test every relevant protocol version.

### Artefacts to produce (mandatory closing block)
- `gateway-enforcement-map.svg`; `action-authorisation-contract.json`; `gateway-negative-tests.md`; `gateway-denial-evidence.json`.

### See also (2–5 exact references)
- Chapter 12, Tooling: tool contract and side-effect adapter.
- Chapter 15, Identity Control Plane: signed actor and delegation chain.
- Chapter 18, Verification Control Plane: deny-path behavioural assertions.
- Chapter 27, Stage 3: trust-chain verification.
- Chapter 48, P8: incident containment when the Gateway denies suspicious egress.

**Sample chapter acceptance checks:** every mutable action path has a PEP; actor-chain owner is Identity, not Gateway; every test has an expected denied or permitted result; two diagrams pass H2/H7; all claims have source status; no protocol version is guessed; section ordering matches F7, including `Evidence artefact` and the last four blocks.

## 7.3 Chapter 13 full subsection-level writing outline (F6)

**Title:** Chapter 13 — Context. **Target:** eight pages, approximately 2,600–3,000 finished words. **Register:** mechanism-first third person. **Narrative:** one failed-reconciliation hook, no more than 150 words. **Primary decisions:** D-11, D-12, D-13, D-14. **Principal source sections:** R14–16, 21/21.1, 23, 38–40; B11.3 and Appendix A. The CoLab transcript can be used to generate *questions* to research, but its claims about specific vendors are never treated as facts without independent evidence.

### Opening hook (90–120 words)

- Meridian Week 8. Two authorised records disagree on whether a retail product remains active.
- The Agent's retrieval is functioning correctly; the business status cannot be decided from the retrieved evidence.
- A previous pilot silently selects one value. Maya requires a recorded conflict instead of a guessed answer.
- Close with the artefact: the context reconciliation record.

### What this layer decides

- Context decides which governed evidence, context state, memory and semantic entities are available to the Harness, including how conflicting claims are handled.

### The mechanism (3.5–4 pages)

#### 13.1 Context contracts at the Fabric boundary
- Separate incoming data, retrieval, assembly, working state, durable memory and business semantic meaning.
- Define schema fields: `context_id`, `source_id`, `source_version`, `tenant_id`, `subject_id`, `data_class`, `valid_from`, `observed_at`, `authority`, `confidence`, `retention_class`, `provenance_hash`.
- Figure 13-1: Context component diagram, ten nodes maximum. Show ingestion, ACL filter, retrieval, assembly, entity map, memory write gate, conflict queue and evidence ledger.

#### 13.2 Retrieval access and citation provenance
- Show tenant-filtered retrieval and source-level ACL enforcement before any content enters model context.
- Explain cache invalidation, stale index metadata and redaction prior to external model use.
- Synthetic example 13-1: one authorised and one denied source document; show the effective context manifest.

#### 13.3 Semantic entity reconciliation
- Define canonical ID, alias, temporal validity and source precedence; precedence is approved by the domain data owner, not inferred from similarity.
- Define conflict states: `candidate`, `accepted`, `disputed`, `superseded`, `rejected`.
- Figure 13-2: semantic claim state machine with approved transitions and owner labels.
- Synthetic example 13-2: retail product record contradicts historical CRM event. No silent overwrite; escalation preserves both claims with timestamps.

#### 13.4 Memory tiers with different obligations
- Distinguish working/session state, episodic facts, semantic facts and immutable evidence archive. The archive is *evidence*, not automatically retrievable memory.
- Define purpose, tenant scope, owner, TTL and deletion path for each tier.
- State why an embedding index does not create business authority or temporal truth.

#### 13.5 Governed memory write-path
- Figure 13-3: sequence from candidate extraction to classification, source verification, contradiction check, approval if needed, tier placement, receipt and index update.
- Require `source`, `policy_class`, `tenant_id`, `validity`, `retention`, `writer_actor_chain` and idempotency key.
- A write that fails verification is held in `disputed`, not quietly accepted.

#### 13.6 Cross-agent context sharing
- Signed handoff packets reference authoritative content and a bounded audience; no blind copying of full histories or credentials.
- Show receiving agent verifies context policy and scope independently.
- Define replay and staleness behaviour when the source is deleted or permission revoked.

#### 13.7 Retention, decay and deletion
- State what is eligible for decay, what is fixed by records policy and how verification refreshes validity.
- Trace deletion through primary store, indexes, caches, replicas and backups subject to lawful constraints; preserve an erasure receipt without retaining deleted content.
- Give one example of expired memory being blocked before retrieval.

### The interface with adjacent layers

#### 13.8 With Lifecycle
- Harness requests context and receives a manifest. Context never supplies action authorisation.

#### 13.9 With Tooling and Execution Environment
- Tool results enter through typed adapters; E worker state is ephemeral, while Context persists only approved data.

#### 13.10 With control planes
- Identity provides actor/tenant proof; Data Protection governs data class and retention; Interoperability governs schema version; Verification checks conflicts; Observability captures provenance without unrestricted content.

### Failure modes (approximately one page)

#### 13.11 Failure table
- Columns: failure, mechanism, symptom, owning control, test and evidence.
- Include cross-tenant retrieval, forged source, stale index, false alias match, contradictory authoritative sources, memory poisoning, deleted-source replay and incomplete data erasure.
- For each, name the safe result: deny, quarantine, mark disputed, request human clarification or erase.

### Scaling signal (approximately half a page)

#### 13.12 Scale and degradation
- Measure ACL-filter latency, retrieval freshness lag, conflict queue age, memory-write verification backlog and deletion completion age.
- Explicit proposed thresholds belong in the service tier; do not imply universal industry thresholds.
- Demonstrate separation between retrieval service availability and correctness of evidence.

### Anti-patterns (F4 entries)

#### 13.13 AP-13-01: Similarity equals truth
- Highest embedding score becomes authoritative. Detect conflicts resolved without source precedence or steward review; fix with semantic claims and explicit authority.

#### 13.14 AP-13-02: Shared memory by convenience
- Multiple tenants write to a shared mutable collection. Detect cross-tenant source IDs in one context manifest; fix with scope and brokered handoffs.

#### 13.15 AP-13-03: Delete the row, not the copies
- Primary record removed but index/cache still serves content. Detect post-deletion retrieval; fix with a store-by-store disposition ledger.

### Decisions to make (3–7 bullets)
- Select source ACL and retrieval-proof contract, D-11.
- Define durable write gate, tiers and retention, D-12.
- Choose allowable handoff content and recipient scope, D-13.
- Define canonical-ID and conflict escalation policy, D-14.

### Defaults (matched one-to-one)
- Enforce ACL at retrieval and before consumption.
- Require policy-bearing provenance for durable memory.
- Exchange only signed, bounded handoffs.
- Preserve disputed claims until authoritative reconciliation.

### Artefacts to produce
- `context-manifest-schema.json`; `memory-write-contract.json`; `semantic-claim-reconciliation.json`; `context-negative-tests.md`; `context-deletion-receipts.csv`.

### See also
- Chapter 7, Tenant Isolation and Sovereignty: tenant profile.
- Chapter 14, Lifecycle: checkpoint and handoff consumer.
- Chapter 15, Identity Control Plane: actor scope.
- Chapter 18, Verification Control Plane: behavioural assertions.
- Chapter 21, Data Protection Control Plane: retention and deletion.

**Sample chapter acceptance checks:** C is the sole home for semantic context services; legal ownership does not move to C; memory and audit evidence are distinguished; each example carries source and tenant IDs; one conflict is deliberately unresolved; three diagrams pass H2; all memory heuristics are represented as policies subject to verification, not vendor facts.

## 7.4 Writing handoff checklist for both samples

| Check | Chapter 16 | Chapter 13 |
|---|---|---|
| Opening consequence | Unauthorised mutation path | Disputed source facts |
| Main mechanism | Inline action admission and PEP | Retrieval, entity resolution, memory and provenance |
| Hard failure demonstration | Forged or bypassed receipt denied | Conflicting source held as disputed |
| Reusable reader artefact | Authorisation schema + denial test | Context manifest + conflict record |
| Distinctive diagram | Gateway request sequence | Memory write sequence |
| Mandatory template | F7 | F6 |
| External fact-check focus | Protocol versions, identity/security claims | Retrieval/retention claims and cited memory patterns |
| First editorial gate | Correct eight-plane ownership | No ninth Semantic Context Plane |

# Phase 8. Six-month manuscript build plan

## 8.1 Staffing and delivery assumptions

**Duration:** 26 working weeks, six calendar months. The chapter briefs total **161 estimated first-draft author-days**; this excludes developmental editing, source verification, illustrations and proofs. **Writing model:** lead author about 0.9 FTE plus technical co-author about 0.7 FTE; developmental editor about 0.4 FTE; research/fact-check support about 0.3 FTE; diagrammer about 0.3 FTE; copyeditor and accessibility reviewer intensify in Months 5–6. A single author doing all production and technical review is not the assumed capacity. This is an aggressive parallel schedule, not a promise that editorial sign-off takes no time.

**Production order:** canonical architecture → sample chapters → Parts I–III → decisions → lifecycle/operations → playbooks → reference library → full-book edit/production. Writing, fact checking and art progress in parallel only after governing contracts are locked. No diagram is accepted without its source file, caption, version, alt text and greyscale proof.

**Editorial release gates:**
- **G0 (end Week 2):** architecture definitions, all 58 titles, chapter-to-decision matrix, six-character cast, source crosswalk and ED-018 renumbering accepted.
- **G1 (end Month 1):** Ch16 and Ch13 technically signed off and editorially line-edited; proposal pitch verified against both.
- **G2 (end Month 3):** all architecture chapters, 30 F1 pages and source evidence links accepted; no missing plane ownership.
- **G3 (end Month 5):** lifecycle, operating chapters and ten executable playbooks structurally complete, with Meridian continuity and working specimens.
- **G4 (end Month 6):** every chapter passes M2/M3; no unverified claims or unapproved figures; publisher proposal and two samples ready to query.

## 8.2 Month-by-month production schedule

| Month | Chapters completed as first drafts | Decision pages | Playbooks | Figures, tables, artefacts | Reviews and exit gate |
|---|---|---|---|---|---|
| **1 — Foundation and samples** | Ch1, Ch5, Ch10, **Ch16**, **Ch13** | Catalogue D-01–30 locked; complete D-10/11/12/13/14/18 first | P2 outline and initial test run | Figures 0-1, 10-1/10-2, 13-1/13-2/13-3, 16-1/16-2; action receipt and context manifest | Canonical ownership review; 2 sample technical reviews; S M2 sample audit; G0 and G1 |
| **2 — Strategic argument and layer contract** | Ch2–4, Ch6–9, Ch11–12, Ch14–15 (11 chapters) | D-01–09, D-15–17, D-19–20 complete; normalised F1 production masters | P1, P3, P4 story and step outlines | Structural component diagrams; tenant trust boundary; actor-chain sequence; business case model | Narrative/terminology continuity check; architecture integration review; no source claim without register |
| **3 — Complete architecture and decisions** | Ch17–22 plus Ch23 (seven chapters, including 30 decision pages) | Finalise all D-01–30; one-page pagination proof; ADR crosswalk | Complete P5–P10 step contracts; peer tabletop for P7/P8 | Eight Control Plane evidence maps; 30 decision artefact IDs; gateway/verification end-to-end path | G2; independent security review; F6/F7 completeness; 12-unit ownership trace; protocol/standard research |
| **4 — Meridian lifecycle and first operations** | Ch24–34, Ch35–36 (13 chapters) | No new IDs; verify decision references in each stage | P1–P4 first complete F2/F5 drafts | Eleven lifecycle state diagrams/tables within H1 taxonomy; complete pilot, recovery and retirement records | Story continuity read, incident chronology, RACI/SLO review; every Stage 0–10 has entry/exit gates |
| **5 — Operations and procedural book** | Ch37–40, Ch41–50 (14 chapters) | Decision pages reconciled to playbook actual outputs | P1–P10 complete; two dry-run tabletop exercises | Incident, FinOps, audit, release and retirement specimens; playbook input/output forms | G3; SRE/security/FinOps peer review; revise M3 stages 1–7 chapters in rolling batches |
| **6 — Reference, fact checking and publisher pack** | Ch51–58 (eight chapters); revisions to Ch1–50 | D-01–30 page proof, cross-link and index QA | Final F2/F5 verification and no-missing-step proof | Twelve F3 checklists; F8/F9/F10/F11 references; standards sources; all figure SVG/alt text and print proofs | Copyedit, anti-slop edit, fact check, technical review, accessibility, index and layout proof; G4 |

**Review capacity:** release drafts in weekly batches of two to five chapters, never as a single Month 6 handoff. The developmental editor reviews every part after its first two chapters; the technical reviewer signs architecture, security and standards claims at first-draft time. The copyeditor begins on locked chapters in Month 4. Reserve the final two weeks of Month 6 for proof correction and proposal refinement, not first drafts of critical architecture.

**Milestone quantities:** 58 chapters; 30 decisions; 10 playbooks; 11 lifecycle stages; 12 F6/F7 architecture units; at least twelve F3 checklists; six worked evidence specimens. Maintain a figure register rather than promising a diagram count beyond what the H1 taxonomy and H2 density rules permit. A major state machine may be divided into several figures to satisfy H2.

## 8.3 Writing and QA operating system

### Recommended manuscript directory structure

```text
book/
  style/style-v1.2.md
  governance/canonical-architecture.md
  governance/terminology-lock.md
  governance/editorial-decisions.md
  governance/source-to-chapter-crosswalk.csv
  governance/decision-to-chapter-matrix.csv
  governance/claims-evidence-register.csv
  narrative/meridian-characters.md
  narrative/meridian-events.csv
  manuscript/part-01/ch01.md ... ch04.md
  manuscript/part-02/ch05.md ... ch09.md
  manuscript/part-03/ch10.md ... ch22.md
  manuscript/part-04/ch23-decision-atlas.md
  manuscript/part-05/ch24.md ... ch34.md
  manuscript/part-06/ch35.md ... ch40.md
  manuscript/part-07/ch41.md ... ch50.md
  manuscript/part-08/ch51.md ... ch58.md
  decisions/D-01.md ... D-30.md
  playbooks/P1.md ... P10.md
  artefacts/meridian/
  diagrams/source/
  diagrams/svg/
  diagrams/alt-text/
  production/figure-register.csv
  production/tables-register.csv
  production/chapter-tracker.csv
  production/index-terms.csv
  submission/proposal.md  submission/comp-titles.md
  submission/query-tracker.csv
```

A chapter links to a decision by ID; it does not embed another independently edited copy. The built book compiles Ch23 from `decisions/D-XX.md` in numerical order and Ch41–50 from the corresponding playbook master files. Build tooling verifies exact heading sequence, links, figure IDs and one-page pagination. The companion site republishes verified artefacts without replacing the print book's examples (S SD-010).

### Definition of done for an individual chapter

1. Identified chapter reader outcome and template, with E2 page allocation.
2. Completed opening hook, mechanism, failure, anti-pattern, exact matched decision/default lists, named artefacts and two to five cross-references.
3. Attached cited primary evidence or explicitly labelled fictional/synthetic examples for each empirical assertion.
4. Locked diagrams within H1's eight types, H2's 12-node/20-edge maximum, H7 accessibility and greyscale rules.
5. Applied S C2 terms, British spelling, exact protocol versioning, 30-word sentence/6-sentence paragraph maxima, and C10/Part O edits.
6. Validated story chronology against `meridian-events.csv` and fictitious case attributes against J1–J3.
7. Completed structural edit, author second draft, line edit, anti-slop edit, copyedit, technical fact-check, diagram review and accessibility review (S M3).
8. Tested artefact validity and reader reproducibility; for a decision, rendered exactly one page; for a playbook, confirmed every step has owner/input/output/time.

### Global consistency test matrix

| Test ID | Gate | Method | Required result |
|---|---|---|---|
| ED-QA-01 | Canonical architecture | Search normative prose for `Security Plane`, `Evaluation Plane`, `Semantic Context Plane` used as independent planes | Zero unauthorised ninth-plane instances |
| ED-QA-02 | Vocabulary | Compare text to S C2 exact definitions and forbidden synonym contexts | Zero unexplained term substitutions |
| ED-QA-03 | Decision coverage | Join 30 IDs to chapter and artefact registers | Thirty defined, each referenced, no orphan decision |
| ED-QA-04 | Template order | Parse Parts III and VII headings against F6/F7/F2 | All required headings and order present |
| ED-QA-05 | Chapter closing | Parse Ch1–22 and Ch24–58 against E4 | Matched decisions/defaults, artefacts, then see also |
| ED-QA-06 | Narrative allocation | Count words, speakers and characters in each vignette | E5 caps and J5 ethics satisfied |
| ED-QA-07 | Evidence quality | Audit source citation and effective version/date for every factual claim | No unverified, unsourced current technical claim |
| ED-QA-08 | Diagram accessibility | Check figure-source export, counts, captions and alt text | All diagrams pass H2/H7 and greyscale |
| ED-QA-09 | Operational procedures | Validate every playbook step and abort gate | Ten complete executable F2 procedures |
| ED-QA-10 | Book promise | Sample reader can complete a decision, trace a control and run a playbook without the site | Standalone print book passes |

## 8.4 Publisher submission package

Produce the following **publisher-facing artefacts** after the manuscript has passed G1 and the proposal facts are verified. The complete manuscript and proof library continue through G4; the query package can be prepared in Month 3 and dispatched only with the approved samples and market positioning.

| Component | Exact content | Responsible owner |
|---|---|---|
| Proposal | 2-page promise and differentiator; 1-page market/personal audience; full 58-chapter annotated contents; 1-page author's authority and platform; estimated 478-page specification; 6-month production history; sample chapters and companion-site statement | Lead author and editor |
| Publisher sample A | Finished Ch16 with figures, action receipt, decision links and technical evidence notes | Lead author, security reviewer |
| Publisher sample B | Finished Ch13 with figures, reconciliation record and memory-write receipt | Lead author, data/privacy reviewer |
| Comparative title analysis | Four researched comparables, publication date/edition, reader level, differentiator, areas of overlap and unaddressed decision need | Research editor |
| Demonstration artefacts | One F1 decision page, one fully executed F2 playbook excerpt, one complete audit packet, three labelled synthetic data records | Technical co-author |
| Sample graphics | Figure 10-1 plus one diagram from each sample chapter, source SVG and accessibility text | Diagrammer |
| Market/author evidence | Actual speaking, training, readership, practitioner testimony or distribution only if supported; do not invent sales forecasts or endorsements | Author |
| Query tracker | Publisher, imprint, current submission policy, appropriate editor/channel, date sent, reply, exclusivity terms and next step | Editor |

### Comparative titles for the proposal

These are positioning comparables, **not asserted competitors with identical scope**. The titles below were checked through public publisher/author pages available on 9 November 2026; final proposal metadata must be rechecked before sending.

| Comparable book | Verified publishing context | What its reader seeks | Distinction claimed for this project |
|---|---|---|---|
| *AI Engineering*, Chip Huyen | O'Reilly, official listing at https://www.oreilly.com/library/view/ai-engineering/9781098166298/ | Build applications with foundation models and evaluate model-powered products | This book centres multi-tenant authority, governance, decision records and enterprise operating responsibilities, not foundation-model application engineering alone |
| *AI Agents in Action, Second Edition*, Micheal Lanham | Manning, 2026 edition, official listing at https://www.manning.com/books/ai-agents-in-action-second-edition | Implement agent workflows, tools, knowledge, evaluation and deployment using code | This book is implementation-agnostic and decision/assurance-first; it must contain more complete architecture and operational artefacts rather than compete on programming examples |
| *LLM Engineer's Handbook*, Paul Iusztin and Maxime Labonne | Packt, official 2024 publisher listing at https://www.packtpub.com/en-gb/product/llm-engineers-handbook-9781836200079 | Deliver model/RAG pipelines and LLMOps deployment | This book addresses enterprise-wide Fabric ownership, control-plane proof, tenancy and retirement, not just application delivery |
| *Designing Machine Learning Systems*, Chip Huyen | O'Reilly, May 2022, official listing at https://www.oreilly.com/library/view/designing-machine-learning-systems/9781098107956/ | Design dependable ML systems and operational trade-offs | This book focuses specifically on delegated action, agentic context/memory, eight Control Planes and risk-tiered autonomy |

### Target publisher and query strategy

| Publisher | Proposal angle | Suggested initial action | Submission emphasis |
|---|---|---|---|
| O'Reilly | Durable, vendor-neutral Fabric architecture and enforceable security contracts | Verify current proposal route and submit concise expert-led pitch with Ch16 and Ch13 | Control-plane model, evidence, technical longevity |
| Manning | Distinct reader journey through Meridian and usable decisions | Check proposal process; pitch annotated progression and complete examples | Hands-on conceptual tasks, repeatable playbooks, reader outcomes |
| Apress | Practical enterprise implementation/architecture reference | Verify acquisitions process and target relevant enterprise/cloud imprint | Fully populated architecture, RACI, templates and operational detail |
| Packt | Directly usable guide for platform and security leads | Verify current author proposal channel and word-length constraints | Decision cards, production playbooks, low-level contracts |
| Wiley | Enterprise leadership and architecture governance | Confirm eligible imprint and current proposal process | Executive business case plus credible technical and risk-operating structure |

**Query sequence:** begin with a short tailored proposal to O'Reilly and Manning after both samples pass G1. If either publisher requests exclusivity, follow the stated policy before contacting others. Prepare the Apress/Packt technical package and the Wiley leadership package from the same master proposal, but modify the synopsis and sample emphasis rather than sending identical messages. Track each actual reply; do not assume acceptance or claim a relationship with an editor. If unsolicited submissions are restricted, use the publisher's current documented channel or a legitimate agent introduction. No editor contact details are fabricated.

### Suggested proposal positioning statement

> Enterprise AI agents do not become an enterprise service simply because they can call tools. Their operators must decide who may delegate authority, where each external action is enforced, how context becomes trusted, what evidence proves a release safe, and how a shared Fabric is run and retired. *The Enterprise AI Agent Fabric* gives enterprise architects and platform leads thirty one-page decisions, a four-layer/eight-plane reference architecture, and ten end-to-end operational playbooks. A single fictional financial-services case links each decision to its operational consequences without depending on a specific AI framework or vendor.

### Publisher proposal acceptance checklist

- The book's distinctive promise is demonstrated in both sample chapters; nothing essential requires downloading a companion.
- The source-derived architecture and editorially designed additions are labelled; unverified industry claims are not disguised as production facts.
- The TOC, estimated pages, staffing and sample materials are internally consistent.
- Comparative titles are edition-accurate and sourced; author platform statements and endorsements are real or omitted.
- The two sample chapters follow F6 and F7 verbatim and pass the full S M2 checklist.
- The proposal leads with the decision surface, then the architecture, then the Meridian narrative, in S A1 priority order.

# Final production handoff

**Authoritative work order:** (1) lock ED-018 cross-reference decisions and architecture; (2) write Ch16; (3) write Ch13; (4) reconcile sample-related F1 decisions; (5) follow the Month 2–6 chapter schedule; (6) run the M2/M3, narrative and diagram gates; (7) release the submission package. A chapter that cannot pass its evidence gate does not advance by adding explanatory prose.

**Never infer that a fictional Meridian decision or metric is a real bank's experience.** The final disclaimer and every worked artefact must identify the scenario as fictional and data as synthetic. The printed book must remain self-sufficient even if its companion site disappears.

# Chapter 13 — Context: Definitive Authoring Blueprint v1.0

**Book:** *The Enterprise AI Agent Fabric: Designing, Governing and Operating AI Agents at Scale*  
**Document class:** Binding developmental-editor authoring contract; **not manuscript prose**  
**Chapter:** 13, Part III — Context Structural Layer  
**Status:** Draft-ready, subject to editorial acceptance of this contract  
**Baseline:** Style Bible v1.2; frozen 58-chapter developmental blueprint; frozen Decision Atlas D-11–D-14; Meridian Evidence Fixture v1.0.0 (`MF-FIX-001`); Chapter 16 (cross-reference only).  
**Change discipline:** Do not modify frozen IDs, decision defaults, chapter order, actor roles, policy versions, event timestamps, conflict outcome, or other fixture records. Distinguish an authoring recommendation from an observed fixture result.

## Author's single-sentence mandate

Explain **how Context converts authorised source records into provenance-bearing, policy-scoped inputs without falsely declaring conflicting claims true or persisting unverified facts**. Make the difference between retrieval success, evidence authority, semantic reconciliation and durable memory impossible to miss.

---

## Part 1 — Chapter objectives and reader outcomes

| Dimension | Exact problem the text must resolve | Observable proof in chapter |
|---|---|---|
| Reader | “My retrieval finds relevant answers; which ones can the agent use or trust?” | Reader distinguishes index retrieval from source authorisation, source claim from confirmed business truth, context from memory |
| Enterprise | A retail service function depends on multiple source systems with different owners and update schedules | Reader traces one coherent request across retrieval, conflicting claims, escalation, and downstream action restrictions |
| Data | `MF-REC-A-001` states `ACTIVE`; `MF-REC-B-001` states `CLOSED` for the same product and effective date | Both preserved; no source timestamp treated as precedence; `MF-EVD-RC-001.status=UNRESOLVED` |
| Governance | Source access rules, business precedence, retention and data stewardship have different decision authorities | Policy ownership stays with Identity/Data Protection/Governance and the Retail Data Steward, while Context enforces its data contract |
| Architecture | Context is one of four Structural Layers, **not a ninth control plane** | Clear interface contracts to Lifecycle, Tooling, Execution Environment, and cross-cutting control planes |

**What Chapter 13 must prove:** A successful retrieval can still be unsafe or indecisive; the Context layer must recheck access before consumption, carry provenance, preserve conflicting claims, escalate semantic uncertainty, and refuse unsupported durable-memory assertions. In the frozen case the insurance item is returned by a mislabelled index but excluded from context; two authorised retail records are included but remain disputed. This is the proof, not an imagined resolved account.

**Measurable reader outcomes:** By the final page, a reader can (1) identify Context's responsibilities and boundaries on the frozen 4+8 model; (2) inspect `MF-EVD-CM-001` and explain why two records were included but an insurance record was quarantined; (3) reproduce the comparison logic behind `MF-EVD-RC-001` using source, tenant, product, effective time and values; (4) specify which human owner decides source precedence; (5) describe working context versus governed durable memory versus immutable audit evidence; (6) state the D-11, D-12, D-13, D-14 defaults verbatim; (7) identify safe failure outcomes and scale signals; and (8) explain why the Chapter 16 Gateway denial and Chapter 18 release failure are separate from Context's reconciliation result.

**Non-goals:** No RAG framework tutorial, embedding benchmark, product/vendor recommendation, new architecture plane, new policy, live memory-write demonstration, real customer record, or implied successful resolution. No claim of cryptographically signed handoffs within Meridian unless a frozen artefact explicitly supports it.

---

## Part 2 — Complete Style Bible F6 chapter structure

**Editorial target:** eight typeset pages, approximately **2,600–3,000 finished words** excluding Mermaid/source diagram files. Working assignment: **2,830 words**, with three compact figures and short evidence extracts. Page allocations are editorial planning, not guaranteed typesetting measurements. **Part III narrative:** opening hook only, ≤150 words and approximately 5% of chapter; no dialogue scenes later in the chapter. Mechanism-first, third-person register; British spelling; sentence ≤30 words; no paragraph >6 sentences. For F6, use the exact heading text in the left column; the opening hook is unheaded.

| Fixed F6 order/heading | Purpose and mandatory content | Target words | Page allowance* | Required fixture evidence | Figure placement |
|---|---|---:|---:|---|---|
| **Opening hook** | Week 8 failure: both authorised product-status sources disagree; close by naming the reconciliation artefact | 115 | 0.30 | `MF-EVT-005`–`008`; `MF-EVD-RC-001` | None |
| **What this layer decides** | One sentence defining governed retrieval, context assembly, semantic identity, provenance and memory boundary | 35 | 0.10 | D-11–D-14 | None |
| **The mechanism** | Context contracts; retrieval ACL; manifest assembly; semantic identity and conflict; memory tiers, write gate, bounded handoff, expiry/deletion | 1,640 | 4.35, including diagrams | `MF-REC-A-001`, `MF-REC-B-001`, `MF-EVD-CM-001`, `MF-EVD-RC-001`, `MF-EVT-005`–`008`; earlier `MF-EVT-002`–`004` as retrieval negative case | Figures **13-1, 13-2, 13-3** |
| **The interface with adjacent layers** | Contracts with Lifecycle, Tooling, Execution Environment, and relevant Control Planes without ownership transfer | 205 | 0.55 | `MF-SVC-CTX-001`, actor/tenant references and context manifest | None |
| **Failure modes** | F6 table: failure, cause, symptom, control. Cover tenant mislabel, stale index, alias collision, contradiction, poisoning, replay, incomplete deletion | 245 | 0.65 | `MF-EVT-002`–`008`; manifest and reconciliation record | None |
| **Scaling signal** | Workload/quality metrics, threshold ownership, degradation mode; distinguish fast retrieval from trustworthy context | 140 | 0.35 | Fixture events are *examples only*, no measured production SLO | None |
| **Anti-patterns** | Three complete F4 cards, each with detection signal and exact correction | 240 | 0.65 | A/B conflict and insurance quarantine; deletion as design requirement, not observed event | None |
| **Decisions to make** | Four bullets D-11–D-14, preserving frozen names and purpose | 65 | 0.15 | Frozen decision catalogue | None |
| **Defaults** | Four bullets, one-to-one with preceding decisions, verbatim frozen defaults | 105 | 0.25 | Frozen decision catalogue | None |
| **Artefacts to produce** | 3–5 authorable outputs; distinguish canonical example records from prospective contracts | 35 | 0.10 | Manifest, reconciliation, memory/handoff/deletion contracts | None |
| **See also** | 4–5 specific cross-references and purpose | 25 | 0.10 | Ch7/14/15/18/21 | None |
| **Total** | Guide for composition | **2,850** | **~7.5–8.0** |  | **3 figures** |

*Page budget is shared between figures and paragraphs. If the three figures force overflow, shorten duplicated exposition; do not omit evidence or exceed the narrative ceiling. Keep full JSON in Chapter 57 or the fixture, not inline.*

### Exact F6 heading order for the eventual manuscript

```text
# Chapter 13: Context
[Opening hook: unheaded]
### What this layer decides
### The mechanism
### The interface with adjacent layers
### Failure modes
### Scaling signal
### Anti-patterns
### Decisions to make
### Defaults
### Artefacts to produce
### See also
```

**Mandatory material within “The mechanism” (subsections, not new top-level F6 headings):**

1. **13.1 Context contract and semantic boundary (~180 words).** Separate input data, retrieval results, context assembly, semantic claims, session state, durable memory, and immutable evidence. Define candidate fields (`context_id`, `source_id`, `source_version`, `tenant_id`, `subject_id`, `data_class`, `valid_from`, `observed_at`, `authority`, `confidence`, `retention_class`, `provenance_hash`) as **proposed schema fields**, not fields asserted to exist in the frozen JSON. The fixture's actual names are authoritative (`id`, `source_system`, `classification`, `recorded_at`, `effective_as_of`).
2. **13.2 Access-aware retrieval and manifest (~250 words).** Distinguish index result from source-authorised content and final consumption. Week 7: `MF-REC-INS-LEAK-001` indexed with an incorrect retail tag, actual insurance tenant `MF-TEN-INS-001`, `source_acl_check=DENY`, `context_included=false`. Week 8: `MF-EVT-005`/`006` permit A/B and `MF-EVD-CM-001` records both `acl_check=ALLOW`, `consumer_recheck=ALLOW`, `context_included=true`. Include a compact 3-row audit table. **Figure 13-1** after this explanation.
3. **13.3 Semantic identity and authority (~310 words).** Both records map to `MF-CUST-SYN-0042`, `MF-PROD-0091`, `MF-TEN-RET-001`, `effective_as_of=2027-02-22T00:00:00Z`; Record A at `09:00Z` states `ACTIVE`, Record B at `09:10Z` states `CLOSED`. Same referent/effective date is necessary to expose a conflict. `MF-POL-CTX-CONFLICT-v1.0`, owner `MF-HUM-RET-OWN-001`; `effective_precedence_rule=NONE_DEFINED`. Show `MF-EVT-007` BLOCKED and `MF-EVT-008` ESCALATED. **Figure 13-2** must depict `UNRESOLVED` as the *only observed case state*; a proposed state model is design guidance, not an event that happened.
4. **13.4 Working context, memory and audit evidence (~260 words).** Define: assembled context is a bounded read-time input; working/task state is transient; governed durable memory is a distinct future write; immutable evidence is not automatically an agent-readable memory store. Explain hot/working, episodic and semantic tiers only as frozen conceptual model; avoid claiming Meridian populated them. Explain why embedding proximity is not a truth or temporal-authority rule.
5. **13.5 Governed memory write decision (~280 words).** Name mandatory provenance, owner, tenant, policy classification, verification status, retention, effective time, writer actor chain, idempotency and correction/deletion paths. `MF-EVD-RC-001.blocked_effect` explicitly states **no durable memory assertion of eligibility**. **Figure 13-3** models the *required write-path decision*, not a recorded memory-write transaction; include a clearly marked denied/hold path for the unresolved claim. Do not mint a memory-write event ID or receipt ID.
6. **13.6 Cross-agent context sharing (~170 words).** D-13 uses signed, policy-brokered bounded handoff packets by default. Describe audience, tenant, provenance, retention and receiving-side revalidation. No signed handoff exists in the frozen Meridian case, so this remains a normative description; do not claim `MF-EVD-DG-001` is a Context handoff or that it contains a signed context packet.
7. **13.7 Retention, refresh and deletion (~190 words).** Explain TTL/decay and verification, retention/erasure propagation through source stores, indexes and caches, and lawful backup holds. No actual deletion took place in this fixture. Describe required tests and erasure receipts as chapter artefacts, not retrospective evidence.
8. **13.8 Worked mechanism summary (~100 words).** One compact chain: retrieved → rechecked → manifested → reconciled as unresolved → not promoted as authoritative memory → eligibility cannot authorise refund. Cross-reference Chapter 16 only; do not re-explain its action admission.

## Part 3 — Context responsibility and ownership model

### Context functions and decisions

| Function | What Context owns | Boundary and owner of authority | Output or evidence |
|---|---|---|---|
| **Retrieval** | Context retrieval contract, filtered candidate set, before-use recheck, exclusion/quarantine | Identity establishes actor/tenant identity; Data Protection provides classification constraints; policy owner `MF-HUM-SEC-001` | `MF-EVD-CM-001` and retrieval-negative evidence |
| **Provenance** | Source lineage, timestamps, tenant association, policy references and included/excluded status | Source system owns its record; Observability correlates events without unrestricted customer payload | Manifest with A/B, source ACL results and quarantined record |
| **Semantic identity** | Entity matching and canonical referent linkage; preserve original source IDs | Domain data owner approves precedence, not vector score or retrieval order | `MF-CUST-SYN-0042`, `MF-PROD-0091`, claim links |
| **Reconciliation** | Detect incompatible claims at same effective time; record dispute state; block unsafe use | Retail data owner `MF-HUM-RET-OWN-001` decides subsequent business resolution; **none recorded** | `MF-EVD-RC-001`, `UNRESOLVED` |
| **Memory** | Write/read contracts, validation and placement, provenance and correction hooks | D-12 retention/classification requirements from Data Protection and Governance; no actual fixture durable write | Prospective `memory-write-contract.json`; *no executed write receipt* |
| **Escalation** | Signal unresolved state and route stewardship work item | `MF-HUM-RET-OWN-001` accountable for resolution, `MF-TASK-STEWARDSHIP-001` already recorded | `MF-EVT-008`, reconciliation record |

**Control-plane separation:**

- **Identity:** determines who the actor is, effective tenant and delegation. Context *consumes* that verified context, never originates permission or increases scopes.
- **Gateway:** controls external mutable action admission. Context supplies `UNRESOLVED` as a policy input, never permits or denies `refund.issue` on behalf of Gateway. See Chapter 16 for `MF-EVT-009`–`013`.
- **Verification:** tests behavioural assertions and release readiness; Context records data conflicts. The later `MF-EVD-RG-001` is a Verification artefact, not a Context reconciliation result.
- **Governance:** determines acceptable business policy, owners and exceptions. The Context layer makes governed data usable but does not claim policy authority.
- **Data Protection:** governs class, residency, retention and deletion obligations. Context implements storage/retrieval behaviour and provides evidence of enforcement where available.
- **Observability:** captures correlation and trajectories; Context records source lineage. Do not copy raw confidential context into unrestricted logs.
- **Interoperability:** governs cross-boundary schema/contract versioning, not source-of-truth precedence.

**Adjacent Structural Layer interfaces required by F6:**

| Boundary | Contract to describe | Forbidden ownership transfer |
|---|---|---|
| **Lifecycle → Context** | Harness requests bounded context for `MF-AGT-RET-004`; Context returns manifest + inclusion/uncertainty status; Harness chooses whether to continue or escalate | Context does not own step limits, workflow state machine, approval transitions |
| **Tooling → Context** | Typed read/tool observations are reclassified and traced before potential context inclusion | Tool output does not automatically become trusted fact or durable memory |
| **Execution Environment ↔ Context** | Isolated workers receive approved scoped inputs; task-local scratch state is ephemeral | Runtime scratch files do not become a durable governed store by accident |

**Decision ownership:** D-11 retrieval controls and D-12 durable-memory gate are expressed as Context contracts under the applicable control policies; D-13 cross-agent sharing must respect the receiving identity and tenant; D-14 semantic dispute is referred to the Retail Data Steward. The chapter must never call Context a “Semantic Context Control Plane.”

---

## Part 4 — Immutable Meridian fixture mapping

| Frozen reference | Exact timestamp, fact or status | Required chapter placement | Do not say |
|---|---|---|---|
| `MF-REC-A-001` | Retail Product Registry `MF-SYS-PROD-001`; `2027-02-22T09:00:00Z`; `ACTIVE`; `CONFIDENTIAL_CUSTOMER`; owner `MF-HUM-RET-OWN-001` | Opening/semantic comparison/manifest/figure 13-2 | “Verified truth”; authoritative merely because source is Product Registry |
| `MF-REC-B-001` | Retail CRM `MF-SYS-CRM-001`; `2027-02-22T09:10:00Z`; `CLOSED`; same owner, tenant, product and effective time | Opening/semantic comparison/manifest/figure 13-2 | “Latest wins”; product definitively closed |
| `MF-EVD-CM-001` | ContextManifest, created `2027-02-22T09:12:03Z`; both records included, insurance candidate quarantined; `cryptographic_signature=NOT_APPLIED_SYNTHETIC_FIXTURE` | Figure 13-1; retrieval table and referenced context contract | Signed proof, a complete memory record, or conflict resolution |
| `MF-EVD-RC-001` | Reconciliation, created `2027-02-22T09:12:03Z`; `status=UNRESOLVED`, `resolution=ESCALATE_TO_DOMAIN_DATA_OWNER`, `effective_precedence_rule=NONE_DEFINED` | Figure 13-2; conflict table; memory hold; escalation | Approved override, resolved status, authorisation to pay |
| `MF-EVT-005` | `2027-02-22T09:12:00Z`, `RECORD_A_RETRIEVED`, `ALLOWED` | Retrieval example and chronological miniature | All business facts in A verified |
| `MF-EVT-006` | `2027-02-22T09:12:01Z`, `RECORD_B_RETRIEVED`, `ALLOWED` | Retrieval example and chronological miniature | B supersedes A merely by later record time |
| `MF-EVT-007` | `2027-02-22T09:12:02Z`, `CONTEXT_CONFLICT`, `BLOCKED` | Reconciliation and Figure 13-2 | Both records denied for retrieval; source truth settled |
| `MF-EVT-008` | `2027-02-22T09:12:03Z`, `ESCALATED_TO_STEWARD`, `ESCALATED` | Closing of technical mechanism; stewardship step | Steward approved a resolution |
| `MF-REC-INS-LEAK-001` | Week 7 insurance document, actual tenant `MF-TEN-INS-001`; incorrect retail index tag; source ACL DENY and not in final context | Negative retrieval proof and Figure 13-1 | Insurance content was consumed by the retail agent |
| `MF-EVT-002`–`004` | `2027-02-16`; index mislabel detected, record quarantined; cross-tenant negative test PASS | Background example in mechanism, failure table | Real production leak or confirmed breach |
| `MF-POL-RET-ACCESS-v1.0`, `MF-POL-TENANT-v1.0` | Access and tenant policies in manifest | Retrieval explanation | Context independently invented these policies |
| `MF-POL-CTX-CONFLICT-v1.0` | Semantic conflict policy; retail data owner `MF-HUM-RET-OWN-001` | Reconciliation explanation | Automatic newest-record precedence |
| `MF-TASK-STEWARDSHIP-001` | Follow-up ticket in reconciliation record | Escalation explanation | Ticket closed or approved |
| `MF-EVD-RG-001` | Later Week 11 release failure | One forward cross-reference to Chapter 18, no retelling | Evidence of a Context memory-write failure or revised fixture |

**Chronology lock:** Week 7 `2027-02-16` mislabel/quarantine; Week 8 `2027-02-22` A/B retrieval and unresolved dispute; Week 9 `2027-03-01` downstream Gateway denied attempt; Week 11 `2027-03-15` candidate release blocked. This chapter **stays in Week 7/8** except concise consequence links. Never promote a dispute into an executed payment or a recorded durable-memory write.

**Recommended short evidence table for manuscript:** 3 rows: A (`ALLOW/ALLOW/included`), B (`ALLOW/ALLOW/included`), insurance item (`source_acl_check=DENY`, excluded). Maintain distinction between `index_returned=true` and `context_included=false` for insurance.

---

## Part 5 — Production-ready diagram briefs

All figures follow Style Bible H1–H8: one idea each; maximum 12 nodes and 20 edges; sentence-case labels, ≤4 words per node, verb-phrase arrows; greyscale legibility, no colour-only meaning; caption with figure ID, version and source; 2–3-sentence alt text; editable source and SVG export. Component/context graphics use draw.io or Excalidraw; state machine/sequence use Mermaid. Illustrators must not turn proposed contracts into evidence of actual events. The figures are **specifications, not illustrations**.

### Figure 13-1 — Context Manifest Assembly

**Approved type:** Component diagram. **Reader question:** Which index results reached the agent context, and on what authority?

**Components (maximum ten):** Retail Product Registry (`MF-SYS-PROD-001`); Retail CRM (`MF-SYS-CRM-001`); Insurance Policy Repository (`MF-SYS-INS-001`); Retrieval index (logical component, no new fixture ID); Context Retrieval Service (`MF-SVC-CTX-001`); source-ACL recheck (logical); context assembler (logical); Context Manifest (`MF-EVD-CM-001`); restricted/quarantine lane (logical); Context consumer (`MF-AGT-RET-004`). The logical nodes are diagram abstractions, **not newly declared registered services**.

**Directed, labelled edges:** sources supply indexed candidates; index returns A/B and wrongly tagged insurance candidate; recheck permits A/B and excludes insurance; assembler records inclusion/denial and delivers scoped context to agent; manifest records provenance and policy refs. No insurance-content arrow into consumer. Draw a separate visually distinguished quarantine path. Exact policy identifiers in caption/legend, not overly long node labels.

**Required annotations:** `MF-REC-A-001` (included), `MF-REC-B-001` (included), `MF-REC-INS-LEAK-001` (excluded); `MF-POL-RET-ACCESS-v1.0`; `MF-POL-TENANT-v1.0`; `source_acl_check=DENY` on insurance; `cryptographic_signature=NOT_APPLIED_SYNTHETIC_FIXTURE`. Clearly distinguish index return from context consumption. Avoid implying a cryptographically proven manifest.

**Caption:** “Figure 13-1. A source-level access recheck admits two retail claims but excludes an incorrectly tagged insurance result (v1.0; synthetic `MF-EVD-CM-001`).”

**Alt text:** “Two retail records pass source authorisation and are included in the Context Manifest. An insurance record returned by a mislabelled retrieval index fails the source-tenant recheck and never enters the agent's context.”

**One-sentence reader takeaway:** *A relevant index hit is not an authorised context input.*

**QA:** Reconcile all three inclusion flags against JSON; no accidental connection of insurance to the agent; no invented signatures. Use the figure after §13.2.

### Figure 13-2 — Semantic Reconciliation Workflow

**Approved type:** State machine (Mermaid source) showing a compact claim-workflow; use no more than 8 states, 12 edges. **Reader question:** What happens after two authorised sources disagree?

**States:** Candidate claims → Identity matched → Time aligned → Conflict detected → Unresolved → Steward escalation. Optional conceptual future states “Accepted” and “Superseded” may be shown as **design-state possibilities only**, separated from the observed Meridian path; simpler figure with only six states is preferable. No line to “Resolved” on the Meridian observed path.

**Transitions/guards:** A/B records retrieved (`MF-EVT-005/006`); same `MF-PROD-0091` and `effective_as_of`; `ACTIVE` vs `CLOSED`; no precedence; `MF-EVT-007` records blocked conflict; `MF-EVT-008` escalates to `MF-HUM-RET-OWN-001`. Add a visible `UNRESOLVED` annotation and “No durable eligibility assertion”. The figure must not imply that record B is newer *in business-effective time*: both have the same effective date.

**Caption:** “Figure 13-2. Both retail claims remain available as evidence while their incompatible product statuses are preserved as unresolved (v1.0; `MF-EVD-RC-001`).”

**Alt text:** “Two authorised records resolve to the same product and date but disagree on status. The reconciliation path stops at an unresolved conflict and escalates to the Retail Data Steward instead of choosing either value.”

**Reader takeaway:** *Matching an entity is not deciding its truth.*

**QA:** Confirm `effective_precedence_rule=NONE_DEFINED`; no unrecorded steward decision; use the figure immediately after §13.3.

### Figure 13-3 — Governed Memory Write Decision

**Approved type:** Sequence diagram (Mermaid source). **Reader question:** Why does a retrieved or generated assertion not automatically become durable memory?

**Participants:** Agent (`MF-AGT-RET-004`); Context write gate (logical); provenance verifier (logical); classification/retention policy (logical); reconciliation checker (logical); durable memory store (logical); stewardship queue (`MF-TASK-STEWARDSHIP-001`, existing task reference). No new service or evidence IDs.

**Nominal sequence:** candidate memory claim proposed → provenance and scope checked → policy class/owner/retention checked → contradiction checked → conditional outcome. **Observed synthetic case:** eligibility claim remains unresolved; write gate **does not persist** the assertion; reference existing `MF-EVD-RC-001` and stewardship ticket. **Hypothetical alternate path** for verified, approved claims may show a conditional write and receipt, labelled **“design contract only; not observed in Meridian”**. If visual density compromises clarity, omit the alternate path.

**Required annotation:** “No durable memory assertion of eligibility” (exact `MF-EVD-RC-001.blocked_effect` meaning). Do not invent a memory-write event, completed erasure, signature or durable-memory receipt. Record reference `MF-EVD-RC-001` in caption rather than pretending it is a memory-write receipt.

**Caption:** “Figure 13-3. The proposed memory write path holds an eligibility assertion when the source claims remain unresolved (v1.0; required decision process, not a recorded memory transaction).”

**Alt text:** “An agent proposes retaining an eligibility assertion, but provenance, policy and contradiction checks must complete before durable storage. The unresolved Meridian claim follows the hold/escalation route; no durable memory write is shown as having occurred.”

**Reader takeaway:** *A retrieved fact requires separate justification before becoming durable memory.*

**QA:** The hold line must be explicit; durable store never receives the disputed claim; distinguish conceptual design nodes from registered runtime identities. Use after §13.5.

---

## Part 6 — Technical explanation standards and misunderstandings

| Concept | Must explain | Common misunderstanding to correct | Required anchored example | Forbidden simplification |
|---|---|---|---|---|
| **Provenance** | Source identity, ownership, tenant, effective time versus observation time, policy context and lineage through manifest; digest is not truth | “A citation guarantees accuracy” | A/B source and timestamp columns in `MF-EVD-CM-001` / context records | Calling `context_digest_sha256` proof of business truth or signature verification |
| **Retrieval filtering** | Two-stage access: preselect/ACL and before-consumption source recheck; why index tenancy may be stale or wrong | “The vector index checked tenancy, so it is safe” | Insurance candidate `MF-REC-INS-LEAK-001` returned by index but quarantined (`MF-EVT-002`–`004`) | Calling an index return a confidential-data exposure to agent context |
| **Context assembly** | Include authorised sources with traceable inclusion status; preserve both values and uncertainty labels | “Everything retrieved goes into the prompt” | `MF-EVD-CM-001`: A and B included; insurance excluded | Equating assembly with agent memory or with a verified knowledge base |
| **Semantic identity** | Same customer/product/effective time can be matched without deciding value correctness | “Same identifier means same true status” | `MF-CUST-SYN-0042`, `MF-PROD-0091`; status mismatch | Deducing precedence from recency or similarity score |
| **Reconciliation** | Dispute state, no established source precedence, named steward, explicit escalation | “Newest wins, so CRM CLOSED is correct” | `MF-EVD-RC-001.status=UNRESOLVED`, `MF-EVT-007/008` | Fabricating approved resolution or hiding one source |
| **Escalation** | Work item and role handoff; permissible use of disputed evidence for review | “Escalation automatically resolves the record” | `MF-HUM-RET-OWN-001`, `MF-TASK-STEWARDSHIP-001` | Reporting ticket as closed or authority as transferred to agent |
| **Governed memory** | Write-path gate vs retrieval; consent/legal class, provenance, verification, retention, change and deletion; evidence archive separate | “Chat context, vector index and memory are the same store” | `MF-EVD-RC-001.blocked_effect`: no durable eligibility memory assertion | Claiming a completed memory write, deletion, cryptographic handoff or actual retention outcome |
| **Cross-agent context** | Bound recipient/audience, source references, re-evaluation, no credential copying | “Shared memory means copying all histories” | D-13 default; **conceptual only** for this case | Claiming Meridian supplied a signed Context handoff packet |

**Required technical sequence for the prose:** retrieval is shown before Context terminology; provenance before conflict; conflict before memory; memory before lifecycle/operating consequences. Introduce mechanisms only when their failure has been established. A brief Chapter 16 forward pointer is allowed for the financial mutation; the Gateway discussion itself remains in Chapter 16.

### Scaling signal contract

Show *three* distinct dimensions: (a) throughput/latency of authorised retrieval, (b) correctness/freshness/age of source and conflict queues, and (c) verification and deletion backlogs. Candidate measures: `p95 source-ACL recheck latency`, `p95 context assembly latency`, index freshness lag, unresolved-conflict age, memory-write review queue age, deletion propagation age, source recheck failure rate. **No fixture-derived performance numbers exist.** If the final chapter includes example thresholds, label them as illustrative operator-set thresholds and provide an owner and deviation condition; do not invent a Meridian SLO. Describe degradation: preserve denial/quarantine, report insufficient evidence, pause unsafe mutation dependency, and continue only permitted read/review work.

### F4 anti-pattern assignment (three complete cards)

1. **AP-13-01 — Similarity equals truth.** What it looks like: top-ranked claim becomes product truth; why it happens: relevance conflated with authority; why it fails: conflicting status for identical effective time; correct pattern: D-14 explicit dispute plus steward; detection: unresolved inputs merged without a `MF-EVD-RC-001`-like record.
2. **AP-13-02 — Shared memory by convenience.** What it looks like: tenant data written into common mutable context; why it happens: cross-agent reuse optimisation; why it fails: context crosses authorisation boundary; correct pattern: D-11 and D-13 controlled source access and bounded sharing; detection: cross-tenant source ID in final manifest (the insurance fixture is *excluded*, not a real leak).
3. **AP-13-03 — Delete the row, not the copies.** What it looks like: primary record deleted while cache/index still retrieves it; why it happens: retention treated as single-store operation; why it fails: derived stores remain accessible; correct pattern: D-12, Data Protection rules, store-by-store deletion verification; detection: post-deletion retrieval. **Hypothetical design anti-pattern, not an event in Meridian fixture.**

Each anti-pattern follows F4's exact five fields: **What it looks like; Why it happens; Why it fails; The correct pattern; Detection signal.** Avoid a new taxonomy or additional named controls.

### Mandatory F6 ending, frozen decision alignment

**Decisions to make** (same order as defaults):

- **D-11 — Control retrieval access:** specify the retrieval access and consumer recheck contract.
- **D-12 — Govern durable memory:** specify provenance, classification, ownership, retention and verification before durable write.
- **D-13 — Enable cross-agent memory:** specify bounded, policy-brokered transfer conditions.
- **D-14 — Reconcile semantic identities:** specify canonical identity matching and unresolved escalation to owner.

**Defaults** (must be copied without paraphrase in final manuscript):

- **D-11:** “Default to ACL-aware retrieval, source-level provenance and policy rechecks before context is consumed.”
- **D-12:** “Default to no durable memory write without provenance, policy classification, owner, retention and verification status.”
- **D-13:** “Default to signed, policy-brokered handoff packets with bounded sharing; do not share unrestricted mutable memory.”
- **D-14:** “Default to canonical IDs with source lineage and explicit unresolved-conflict states; never silently choose the newest record as truth.”

**Artefacts to produce** (five frozen development-brief outputs; do not present prospective documents as completed Meridian artefacts):

- `context-manifest-schema.json` — contract for included/quarantined sources (fixture sample `MF-EVD-CM-001`).
- `memory-write-contract.json` — normative durable-write policy and receipt fields (no actual Meridian write recorded).
- `semantic-claim-reconciliation.json` — conflict representation (fixture sample `MF-EVD-RC-001`).
- `context-negative-tests.md` — tenant, stale index, conflict and poison-control negative assertions.
- `context-deletion-receipts.csv` — deletion verification format (no actual Meridian deletion recorded).

**See also** (five links and purpose): Ch7 tenant isolation; Ch14 Harness consumer and checkpoints; Ch15 identity and tenant proof; Ch18 behavioural assertion and release gate; Ch21 data protection, retention and erasure. Optionally mention Chapter 16 in body prose for Gateway consumer of unresolved status, but do not displace these frozen F6 links.

---

## Part 7 — Editorial failure-mode catalogue

| Failure | How it appears in draft | Correction / editorial test |
|---|---|---|
| **RAG tutorial drift** | Installation commands, vector DB comparisons, chunk-size advice | Replace with source access, evidence, conflict and policy consequence; cite Ch13 contract, not framework API |
| **AI hype language** | “Transformative”, “revolutionary” or unsupported safety promises | Delete adjective, name mechanism and observed simulated result; apply Style Bible C10/Part O |
| **Context equals memory** | Included A/B records described as persisted long-term facts | Define separate read context, working state, governed durable memory and evidence archive; show no write |
| **Silent conflict resolution** | CRM `CLOSED` overwrites Registry `ACTIVE` because recorded later | Quote `effective_precedence_rule=NONE_DEFINED` and `status=UNRESOLVED`; show steward escalation |
| **Provenance ambiguity** | Generic “the system says” with no record/time/tenant | Include actual A/B source IDs, timestamps, class, owner and manifest reference |
| **False cross-tenant breach** | Insurance content said to have entered the agent prompt | State `index_returned=true`, `context_included=false`; demonstrate source ACL denial |
| **Invented memory event** | A new memory write, memory receipt or deletion result is presented as observed | Remove unsupported event; explain conceptual D-12 contract and existing `blocked_effect` only |
| **Signed-context overclaim** | Digest or handoff depicted as a verified signature | `cryptographic_signature=NOT_APPLIED_SYNTHETIC_FIXTURE`; describe signed handoffs as default design |
| **Control-plane confusion** | Context creates permissions, owns final business truth or blocks external tool directly | Assign Identity/owner/Gateway/Verification the respective decisions; Context supplies evidence and status |
| **Temporal confusion** | Week 7 event placed on Week 8 date; Week 9 refund issued | Use exact event ledger and UTC; no payment made |
| **Wrong vocabulary** | “Semantic Context Plane” introduced or `agent` used for use case | Enforce frozen four-layer/eight-plane and Style Bible C2 terms |
| **Vague scaling advice** | “Scale when needed”; invented production latency | Specify measurable indicators and service-owned thresholds; label numbers illustrative if given |
| **Diagram overload** | More than 12 nodes; unlabeled edges; colours alone carry deny/allow | Split or simplify; H2/H7 check, grey-scale proof, explicit caption/alt text |
| **Narrative overrun** | Multiple dialogue scenes or a fictitious steward resolution | Opening ≤150 words; all further references analytical and fixture-grounded |
| **Unsubstantiated external facts** | Named framework behaviour, vendor memory mechanism or compliance assurance asserted without proof | Cite authoritative evidence if researched; otherwise omit; never use `transcript.md` as independent authority |
| **Chapter-as-specification** | Long schema blocks and rules without explanation of consequence | Mechanism-first prose, short tables, one worked example per idea; full JSON to Ch57 |

**Anti-slop edit:** read aloud for mechanical rhythm; eliminate generic conclusions and filler transitions; restrict overused em dashes, superficial `-ing` clauses and synonym cycling. Keep exact controlled vocabulary even if unusual. Vignette must end with the reconciliation artefact, not a generic moral.

---

## Part 8 — Final professional author brief and acceptance contract

### Author assignment

Write a finished **Chapter 13: Context** in approximately 2,600–3,000 words with **all F6 headings in the fixed order**. Explain the contrast between (i) relevant but excluded insurance index result, (ii) authorised but contradictory retail records, and (iii) a durable assertion that must not be accepted. Frame the chapter around Context as the **C Structural Layer**, not a new Control Plane. The chapter's core teaching payoff is that an agent may receive a coherent, attributable context containing unresolved claims without being permitted to act as though those claims were resolved.

### Required drafting sequence

1. **Freeze source extracts** from `context-records.json`, `01-context-manifest.json`, `02-reconciliation-record.json`, and `event-ledger.json`. Create a private fact table before drafting; copy reference values exactly.
2. **Write the evidence-led opening** from `MF-EVT-005`–`008` (90–120 words). No unrecorded event, conclusion or approved source precedence.
3. **Draft “What this layer decides” and the mechanism** in the §13.1–13.8 order. Introduce terms after their practical need appears. Put three figures at the specified points.
4. **Draft adjacent-layer contracts** without granting Context the decision authorities of Gateway, Identity, Verification or business stewards.
5. **Draft failure and scale tables** tied to a symptom, control and measurement. Distinguish actual fixture evidence from future operational targets.
6. **Write three complete F4 anti-pattern entries**, with detection signals and the required references.
7. **Copy the four frozen defaults verbatim**, match decisions in one-to-one order, list the five required artefacts, close with the five prescribed See also links.
8. **Run source validation and editorial QA** against the fixture, Style Bible and chapter production register; produce a fact-check report. No claim of approval without review evidence.

### Evidence citation and text integrity

- First use of the case must identify **fictional Meridian Financial** and the synthetic fixture. Later evidence can use compact exact IDs.
- Every factual case statement must match the fixture; if the JSON lacks a value, do not invent it. Place conceptual architecture guidance in a distinct normative voice.
- Context Manifest and Reconciliation Record were created at `2027-02-22T09:12:03Z`. The different `recorded_at` values of A/B do not establish source precedence.
- The cross-tenant item was **quarantined before use**. No personal customer record or actual finance operation exists.
- A canonical hash illustrates integrity of included IDs and event references; it neither signs the manifest nor certifies truth.
- The case has **no performed durable-memory write, deletion or cross-agent context handoff**. Do not claim outcomes for those absent events.
- Subsequent denial and release-gate outcomes may be cross-referenced without repeating Chapter 16 or Chapter 18 narratives.

### Required author deliverables

| Deliverable | Production content | Acceptance |
|---|---|---|
| `chapter-13-context-v1.0.md` | Complete chapter prose, 3 figure references, all F6 sections | Chapter is readable independently |
| `figure-13-1.*` | Editable component diagram + SVG | Manifest source paths and excluded item correct |
| `figure-13-2.*` | Mermaid state-machine source + SVG | No invented resolution; matches `MF-EVD-RC-001` |
| `figure-13-3.*` | Mermaid sequence source + SVG | No invented memory-write event/receipt |
| `chapter-13-evidence-crosswalk.csv` | Claim → exact fixture reference → manuscript section | Every assertion traceable or labelled normative |
| `chapter-13-editorial-self-review.md` | F6, voice, diagrams, facts, anti-slop, reader test | All checks explicitly reported |

### Quality gate

**PASS only if all are true:**

1. Exactly the F6 section headings appear in order, with one opening hook and correct closing-block order.
2. Chapter length is within ~2,600–3,000 words before production pagination; Part III narrative is ≤150 words and confined to the hook.
3. Figures 13-1/13-2/13-3 each have source, caption, alt text, version, greyscale proof and ≤12 nodes/20 edges.
4. `MF-REC-A-001`, `MF-REC-B-001`, `MF-EVD-CM-001`, `MF-EVD-RC-001`, and `MF-EVT-005`–`008` appear with accurate dates, values, tenants and outcomes.
5. Insurance candidate is explicitly **not included** in agent context; both retail records are **included but disputed**.
6. `MF-EVD-RC-001.status=UNRESOLVED`, the steward escalation and `NONE_DEFINED` precedence survive intact.
7. No memory-write/erasure success or Context handoff is invented; prospective D-12/D-13 mechanisms are labelled appropriately.
8. Identity, Gateway, Verification, Governance and Data Protection maintain their frozen ownership boundaries.
9. D-11–D-14 defaults are unchanged, all four paired with their decisions, and all required output artefacts are named.
10. An independent enterprise data architect can reconstruct the conflict; an AI platform lead can explain the difference between retrieval, context, memory and evidence without author assistance.

**Escalate rather than silently repair:** missing source data, diagram contradictions, pressure to create new event IDs, scope ambiguity, an inconsistent frozen decision default, or typesetting changes that would remove required content. Record the issue for the custodian; this authoring blueprint does not authorise fixture edits.

### Final handoff statement

This document is **Chapter 13 Authoring Blueprint v1.0**. Its job is to ensure that one professional writer can draft the chapter without redesigning the architecture, inventing a memory event, or silently deciding the conflicting retail records. The definitive source for example values remains the six-record Meridian Evidence Fixture v1.0.0; the Style Bible v1.2 governs all editorial form and language.
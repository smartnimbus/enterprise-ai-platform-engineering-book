# Chapter 13: Context

On 22 February 2027, two systems at fictional Meridian Financial reported incompatible statuses for the same retail product. The Retail Product Registry said ACTIVE. The customer relationship management (CRM) system said CLOSED. Both records described the product as of the same date.

On 16 February, an incorrectly labelled insurance index entry had failed a source access check. The retail records presented a different problem: the agent could read both, but neither established eligibility for the requested GBP 125 refund. The synthetic Meridian fixture preserves the disagreement and records its escalation in the Semantic Reconciliation Record, `MF-EVD-RC-001`.

### What this layer decides

Context determines which information an agent may consume, how source claims retain their identity and authority, and whether assertions qualify for durable reuse under the governing policies.

### The mechanism

#### From retrieved information to usable evidence

A retrieval engine ranks candidate information against a query. Context determines which candidates may become inputs to a particular agent. The distinction matters because the retrieval service may possess broader source access than the agent on whose behalf it operates.

The Context Structural Layer separates admission, interpretation, and persistence. Admission concerns access; interpretation concerns the meaning and authority of claims; persistence concerns their reuse beyond the current task.

*Table 13-1. Context responsibilities and inspectable outputs.*

| Component group | Responsibility | Output |
|---|---|---|
| Retrieval | Find candidates and check source access | Authorised observations |
| Assembly | Bound inputs to the consumer and purpose | Context Manifest |
| Reconciliation | Match entities and preserve disagreements | Reconciliation Record |
| Memory | Evaluate proposed retention and reuse | Write disposition |
| Handoff | Broker information sharing under receiving policy | Bounded context packet |

A proposed context schema uses `context_id` to identify an assembly and `source_id` with `source_version` to identify its inputs. The `tenant_id`, `subject_id`, and `data_class` delimit their applicability. Fields such as `valid_from` and `observed_at` distinguish business-effective time from observation time. The `authority`, `confidence`, `retention_class`, and `provenance_hash` describe separate properties, not interchangeable measures of trust.

These are design fields, not additions to Meridian's JSON. The fixture uses names including `id`, `source_system`, `classification`, `recorded_at`, and `effective_as_of`.

#### Admission, consumption, and the Context Manifest

Under D-11, retrieval begins with verified actor and tenant assertions supplied by Identity. The index applies relevance ranking and preliminary access control list (ACL) filters. Context then checks each candidate against applicable source permissions, tenant constraints, and classification rules before assembly.

The retrieval service's credential must not substitute for the consumer's authority. A service account may read an entire collection to maintain an index, while an individual agent may consume only a subset. Source admission establishes access to the record; the consumer recheck establishes whether that record remains permitted in the assembled context for the intended recipient and purpose.

A permission change between indexing and consumption can invalidate an earlier decision. Cached payloads therefore require current policy validation before reuse. Where access cannot be established, Context excludes the affected material and reports insufficient evidence if the remaining inputs cannot support the task. It does not treat an unavailable permission service as approval.

Meridian illustrates why both checks matter. Request `MF-REQ-REF-001` permits review and preparation, not refund execution. On 16 February 2027, the index returns `MF-REC-INS-LEAK-001` under the incorrect retail tenant tag `MF-TEN-RET-001`. The actual tenant is `MF-TEN-INS-001`.

The source check rejects the item with reason `SOURCE_TENANT_MISMATCH`. Events `MF-EVT-002` and `MF-EVT-003` record detection and quarantine; `MF-EVT-004` records the passing synthetic negative test. The insurance payload never enters the retail agent's context. Filtering a generated answer would occur after disclosure to the model.

*Table 13-2. Inclusion decisions from synthetic Context Manifest MF-EVD-CM-001.*

| Record | Source | ACL | Consumer recheck | Included |
|---|---|---|---|---|
| MF-REC-A-001 | MF-SYS-PROD-001 | ALLOW | ALLOW | true |
| MF-REC-B-001 | MF-SYS-CRM-001 | ALLOW | ALLOW | true |
| MF-REC-INS-LEAK-001 | MF-SYS-INS-001 | DENY | Not recorded | false |

For the retail records, the ACL column represents `acl_check`; for the insurance result, it represents `source_acl_check`. The quarantined result has `index_returned=true` and `context_included=false`.

[Place Figure 13-1 here: Context Manifest Assembly.]

*Figure 13-1. A source-level access recheck admits two retail claims but excludes an incorrectly tagged insurance result (v1.0; synthetic MF-EVD-CM-001).*

*Alt text:* Retail records A and B pass source and consumer checks and enter context. The incorrectly tagged insurance result fails the source check and follows a quarantine path that cannot deliver its payload to the agent.

An investigator starts with manifest `MF-EVD-CM-001`, rather than reconstructing the agent's inputs from its final answer. The record identifies agent `MF-AGT-RET-004`, retail tenant `MF-TEN-RET-001`, retrieval request `MF-RETR-001`, and trajectory `MF-TRJ-001`. It references policies `MF-POL-RET-ACCESS-v1.0` and `MF-POL-TENANT-v1.0`.

The investigator follows the admitted record IDs to their source observations and the quarantine reference to the exclusion reason. The manifest's `conflict_ref` leads to `MF-EVD-RC-001`, which limits the use of the admitted claims. Thus, the record explains both selection and the unresolved condition affecting subsequent decisions.

The manifest itself requires controlled access. Quarantine metadata can support investigation without exposing the rejected payload to the consumer. Its SHA-256 digest covers canonical JSON containing included record IDs and event references. The field `cryptographic_signature` reads `NOT_APPLIED_SYNTHETIC_FIXTURE`; the digest neither authenticates the record's origin nor verifies the entire source payload.

D-11 incurs additional source checks, filtering, and possible missed matches. The relevant performance measure is authorised retrieval, not unrestricted recall. A higher recall score achieved by exposing another tenant's documents measures the wrong outcome.

#### Semantic identity, authority, and reconciliation

Permission to read a source does not establish its authority over a business attribute. Retrieval relevance ranks potential evidence; confidence estimates uncertainty. Authority identifies who may establish a particular business fact, while precedence determines which applicable source governs a disputed attribute. Verified truth requires evidence meeting the relevant verification conditions.

A reconciliation mechanism first establishes whether claims concern the same entity. It retains source record identifiers alongside canonical identifiers so that a match remains reversible and investigable. An ambiguous entity match warrants further investigation rather than merging unrelated records.

It then aligns business-effective times and compares the claims. Two different statuses can represent successive valid states. In Meridian, however, both sources describe the same product at the same effective instant.

The records identify customer `MF-CUST-SYN-0042`, product `MF-PROD-0091`, and retail tenant `MF-TEN-RET-001`. Both carry classification `CONFIDENTIAL_CUSTOMER` and owner `MF-HUM-RET-OWN-001`.

*Table 13-3. Source claims from context-records.json; times in UTC.*

| Field | Record A | Record B |
|---|---|---|
| Record ID | MF-REC-A-001 | MF-REC-B-001 |
| Source | Retail Product Registry | Retail CRM |
| Recorded at (2027-02-22) | 09:00 | 09:10 |
| Effective as of (2027-02-22) | 00:00 | 00:00 |
| product_status | ACTIVE | CLOSED |
| eligible_for_refund_review | true | false |
| verified_truth | false | false |

The CRM recording time is ten minutes later, but neither record describes a later effective state. Choosing CRM on recency would manufacture a business transition that the evidence does not establish. Choosing the Product Registry on its name would make an equally unsupported authority decision.

Under D-14, the domain data owner defines applicable precedence. A published rule can identify a governing source for a specific attribute and effective period. Context applies that rule and retains its reference; absent an applicable rule, it preserves the incompatible claims. A model's confidence cannot replace the owner's decision.

On 22 February 2027, events `MF-EVT-005` and `MF-EVT-006` record allowed retrieval at 09:12:00 and 09:12:01 UTC. Event `MF-EVT-007` records BLOCKED at 09:12:02; `MF-EVT-008` records escalation at 09:12:03.

The manifest and reconciliation record share the creation time 09:12:03 UTC. Under policy `MF-POL-CTX-CONFLICT-v1.0`, the latter records `UNRESOLVED` and `ESCALATE_TO_DOMAIN_DATA_OWNER`. Its precedence field reads `NONE_DEFINED; explicit unresolved state retained`. The Retail Data Steward, `MF-HUM-RET-OWN-001`, receives follow-up ticket `MF-TASK-STEWARDSHIP-001`.

[Place Figure 13-2 here: Semantic Reconciliation Workflow.]

*Figure 13-2. Both retail claims remain available as evidence while their incompatible product statuses are preserved as unresolved (v1.0; MF-EVD-RC-001).*

*Alt text:* Two authorised records match the same product and effective time but disagree on status. The reconciliation workflow retains UNRESOLVED and escalates to the Retail Data Steward without selecting either value.

The record permits presentation of conflicting evidence to a human reviewer. It does not settle eligibility. D-14 trades automatic completion for accountable interpretation, including the cost of stewardship and outstanding disputes.

#### Working context, memory, and evidence

Working context contains bounded inputs for the present task. Task-local state contains progress and intermediate results; a checkpoint may preserve that state for resumption without making it general-purpose memory. The conceptual hot or working tier supports this active work.

Episodic memory retains selected experiences for later tasks. Semantic memory retains assertions intended for reuse as knowledge. Neither tier removes the need to check provenance, current access, effective time, and verification status on recall. Similarity between episodes cannot establish that the earlier circumstances still apply.

Consider a hypothetical agent that retains a generated eligibility conclusion after completing a disputed case. Later trajectories retrieve that conclusion instead of the underlying source claims. Each reuse can compound the error, even if the original source conflict remains unchanged. D-12 constrains this propagation at the write boundary.

Audit evidence has a different purpose. It preserves an attributable account of decisions, including rejected claims and failed actions, for authorised investigation. A retained record of disagreement is not a verified business assertion or an unrestricted memory entry. These distinctions describe conceptual storage obligations, not deployed Meridian memory services.

#### Governed memory writes

A proposed durable write requires a claim, source lineage, writer actor chain, tenant, owner, classification, effective time, verification status, and retention conditions. Under D-12, those attributes inform the write decision rather than merely satisfying schema validation.

Verification status describes the available assurance. Verification policy determines whether that assurance permits the intended reuse. An unverified claim can carry every required field and still be unsuitable for durable retention as knowledge. The memory contract records the disposition and its basis, including a hold or rejection where prerequisites fail.

A retry-safe write uses an idempotency key to distinguish repeated submission from a new claim. That does not prevent a different failure: the source or reconciliation state may change after validation but before commitment.

A conditional write can bind commitment to the validated version. Atomic version validation or an equivalent consistency mechanism prevents an obsolete decision from being committed after a concurrent change. Where the storage boundary cannot provide that guarantee, the design needs an equivalent guard before publishing the claim for reuse.

These are implementation options, not additional Atlas defaults. The memory owner also needs dependency references to invalidate or correct derived entries when supporting evidence changes.

Meridian's reconciliation record specifies the blocked effect: "No refund.issue and no durable memory assertion of eligibility". The recorded dispute may support human review; an eligibility conclusion cannot qualify on that basis.

[Place Figure 13-3 here: Governed Memory Write Decision.]

*Figure 13-3. The proposed memory write path holds an eligibility assertion when the source claims remain unresolved (v1.0; required decision process, not a recorded memory transaction).*

*Alt text:* A proposed write undergoes provenance, ownership, policy, retention, and contradiction checks. The unresolved eligibility claim follows the hold path; no completed memory write or receipt is shown.

No performed durable-memory write appears in the fixture. The design explains how D-12 would enforce the restriction, at the cost of verification effort, storage management, and correction work.

#### Bounded cross-agent sharing

D-13 defaults to signed, policy-brokered handoff packets. The sender supplies bounded information or source references; the broker evaluates the permitted sharing conditions. The recipient receives only the information allowed for its own identity, tenant, and purpose.

A handoff contract identifies its audience, classification, source lineage, retention limits, expiry, and verification or conflict status. The recipient validates the signature and rechecks applicable access before consumption. A signature authenticates the signed content under the applicable trust assumptions; it does not establish source truth or current permission.

The recipient may possess less authority than the sender. Passing a reference enables an independent access decision without copying the sender's credential. A summary of the disputed retail claims must preserve UNRESOLVED and their lineage; dropping either changes the information's permitted interpretation.

Expiry limits the period of use but does not prevent repeated submission inside that period. Where repetition matters, recipient-bound packet identifiers and replay tracking can supplement expiry checks. These are design options. Bounded sharing incurs validation overhead and sometimes repeated retrieval, but avoids unrestricted mutable memory across agents.

Meridian records no signed Context handoff. Its delegation record belongs to Identity and is not evidence of information sharing.

#### Refresh, retention, and deletion

Refresh re-evaluates a retained claim against current sources; expiry requires renewed justification for reuse. Invalidation stops use of an affected assertion while correction or deletion proceeds. A time-to-live cannot renew an assertion whose source access has been revoked.

Deletion requires lineage across primary records, indexes, embeddings, caches, and handoff copies. A deletion receipt identifies the affected representations, verified outcomes, and outstanding exceptions. Where lawful retention applies, the applicable policy determines restricted retention or disposition rather than promising immediate removal.

Restoring a backup does not restore permission to consume its contents. Recovery procedures reapply applicable restrictions before exposing restored information to ordinary retrieval. Negative retrieval tests then establish whether prohibited copies remain accessible. The fixture records no deletion or restoration outcome.

The Context Manifest and Reconciliation Record supply the downstream precondition. In Week 9, Gateway denies the proposed mutation. In Week 11, Verification's `MF-EVD-RG-001` records failure of assertion `MF-ASSERT-CTX-001`: the candidate selected `refund.issue` instead of abstaining and escalating. Zero side effects do not make that behaviour acceptable. Chapters 16 and 18 explain the separate admission and release decisions.

### The interface with adjacent layers

The Lifecycle Structural Layer owns task progression through the Harness. Its request identifies the actor, task, and required information. Context returns scoped inputs, the manifest, and uncertainty or permitted-use conditions. The Harness uses those conditions to continue authorised review or escalate; Context does not own workflow transitions.

Tooling supplies typed source observations. Context applies governing classification rules, attaches lineage, and evaluates inclusion. Execution Environment isolates consumption and task-local state; persistence beyond the task requires the appropriate contract.

Identity supplies verified actor and tenant assertions. Governance governs policy ownership, approval, and exceptions; the domain data owner defines business precedence. Data Protection determines applicable classification, retention, and deletion constraints.

Observability correlates Context evidence with trajectories without unrestricted payload logging. Interoperability preserves schema compatibility and the meaning of exchanged claims. FinOps accounts for the cost of retrieval, storage, and verification capacity.

Gateway evaluates mutable external action admission using the relevant Context preconditions and independent authority evidence. Verification evaluates behavioural assertions and release suitability. A correctly recorded conflict grants neither execution permission nor release approval.

### Failure modes

*Table 13-4. Context failure modes, diagnostic signals, and controls; design guidance.*

| Failure | Cause | Observable symptom | Control |
|---|---|---|---|
| Tenant mislabel | Incorrect index metadata | Source and index tenants differ | Quarantine before consumption (D-11) |
| Stale access | Revocation missed by cache | Formerly allowed payload remains accessible | Recheck; exclude when authority is unavailable |
| Alias collision | Ambiguous canonical mapping | Unrelated customer claims merge | Preserve source IDs; defer uncertain match (D-14) |
| Silent contradiction | Recency substitutes for precedence | Incompatible value disappears | Record unresolved status; escalate |
| Context poisoning | Retrieved text treated as instructions | Source content changes tool selection | Separate data from instructions; enforce authority independently |
| Unverified memory | Status recorded without policy evaluation | Recalled assertion lacks eligible evidence | Validate write and reuse conditions (D-12) |
| Handoff replay | Valid packet repeatedly submitted | Unexpected duplicate processing | Check audience, expiry, and replay constraints where applicable |
| Incomplete deletion | Derived or restored copies omitted | Prohibited result remains retrievable | Verify disposition across stores |

Retrieval operators own index defects; domain stewards own disputed business attributes. Memory owners investigate invalid retained assertions with the relevant policy authorities. Negative tests should inspect actual consumer inputs and side effects, not rely on answer wording.

### Scaling signal

Context capacity depends on both local workers and source dependencies. Consider an illustrative service objective of 800 ms for context assembly, with 200 ms allocated to queue wait. Sustained p95 queue delay above that allowance can trigger worker scaling if source capacity remains available. These are example budgets, not Meridian measurements.

The service owner monitors recheck latency, source failures, and index freshness. Provenance completeness and cross-tenant exclusions measure different properties from throughput. Stewardship queue age, memory verification backlog, and deletion propagation age require owner-specific limits.

Additional workers cannot settle disputed business facts. During permission-service failure, Context preserves exclusions and reports insufficient evidence. It must not relax access controls to recover a latency objective.

### Anti-patterns

#### AP-13-01: Similarity equals truth

**What it looks like.** The highest-ranked or newest claim becomes the accepted product status.

**Why it happens.** Retrieval optimisation substitutes for domain authority.

**Why it fails.** Matching the question does not establish the claim's validity.

**The correct pattern.** Apply D-14 with canonical identity, explicit precedence, and steward escalation.

**Detection signal.** Incompatible values merge without a Reconciliation Record.

#### AP-13-02: Shared memory by convenience

**What it looks like.** Agents write retrieved information and generated assertions into a common mutable store.

**Why it happens.** Teams avoid repeated retrieval and handoff validation.

**Why it fails.** An agent can inherit information outside its permissions or reuse an unsupported conclusion.

**The correct pattern.** Apply D-11 admission checks, D-12 write policy, and D-13 bounded handoffs.

**Detection signal.** A recalled claim lacks verification provenance or an unauthorised source enters context.

#### AP-13-03: Delete the row, not the copies

**What it looks like.** A primary entry disappears but its derived index remains searchable.

**Why it happens.** The implementation treats retention as a single-store obligation.

**Why it fails.** Subsequent retrieval can recover information that policy prohibits.

**The correct pattern.** Apply D-12 disposition requirements and Chapter 21 Data Protection controls across derived stores.

**Detection signal.** A post-deletion negative retrieval test returns the prohibited representation.

### Decisions to make

- D-11: Control retrieval access. Specify source admission and consumer rechecks.
- D-12: Govern durable memory. Establish verification and retention conditions for reuse.
- D-13: Enable cross-agent memory. Define bounded sharing and receiving-side policy checks.
- D-14: Reconcile semantic identities. Establish matching, precedence ownership, and unresolved escalation.

### Defaults

- D-11: Default to ACL-aware retrieval, source-level provenance and policy rechecks before context is consumed.
- D-12: Default to no durable memory write without provenance, policy classification, owner, retention and verification status.
- D-13: Default to signed, policy-brokered handoff packets with bounded sharing; do not share unrestricted mutable memory.
- D-14: Default to canonical IDs with source lineage and explicit unresolved-conflict states; never silently choose the newest record as truth.

### Artefacts to produce

- `context-manifest-schema.json`: reconstruct admission and quarantine decisions.
- `memory-write-contract.json`: establish eligibility for retention and reuse.
- `semantic-claim-reconciliation.json`: preserve incompatible claims and accountable escalation.
- `context-negative-tests.md`: verify exclusion, conflict handling, and unsafe-recall restrictions.
- `context-deletion-receipts.csv`: track verified disposition and exceptions.

### See also

- Chapter 7: Tenant Isolation and Sovereignty (data boundaries).
- Chapter 14: Lifecycle (Harness consumption and checkpoints).
- Chapter 15: Identity Control Plane (actor and tenant claims).
- Chapter 18: Verification Control Plane (behavioural assertions).
- Chapter 21: Data Protection Control Plane (retention and erasure).

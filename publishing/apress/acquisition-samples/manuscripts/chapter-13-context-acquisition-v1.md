# Chapter 13: Context

On 22 February 2027, two systems at fictional Meridian Financial reported different statuses for the same retail product. The Product Registry said ACTIVE. The customer relationship management (CRM) system said CLOSED. Both records were accessible to the retail agent, and both described the product as of the same date. A week earlier, an incorrectly labelled insurance index entry had failed a source access check. This time, access was not the problem. The agent needed to prepare a recommendation concerning a £125.00 refund, but the evidence did not establish eligibility. In the synthetic Meridian fixture, the disagreement was retained and escalated in the Semantic Reconciliation Record, `MF-EVD-RC-001`.

### What this layer decides

Context determines which source material may enter an agent's working inputs, how claims retain their provenance and semantic identity, and which information qualifies for governed memory under applicable policies.

### The mechanism

#### Retrieval and the context contract

A retrieval system can return a document because its contents match a question. That match says nothing about whether the requesting actor may read the document or whether its contents establish a business fact. Context has to preserve these distinctions throughout assembly, consumption and subsequent reuse.

The Context Structural Layer has separate contracts for the operations in Table 13-1. Each operation produces information that the next operation can inspect without assuming that a previous check settled a different question.

*Table 13-1. Context components and their respective outputs.*

| Component group | Responsibility | Output |
|---|---|---|
| Retrieval | Find candidates and enforce applicable access constraints | Authorised source observations |
| Assembly | Select and bound inputs for a consumer | Context Manifest |
| Semantic reconciliation | Match referents and detect incompatible claims | Reconciliation Record |
| Memory | Validate retention and future reuse | Governed write decision |
| Handoff | Transfer bounded information under receiving policy | Context packet |

A context contract binds information to the task and the actor consuming it. An implementation might use fields such as `context_id`, `source_id`, `source_version`, `tenant_id`, `subject_id`, `data_class`, `valid_from`, `observed_at`, `authority`, `confidence`, `retention_class` and `provenance_hash`. These are proposed schema fields, not a transcription of Meridian's records. The fixture uses names including `id`, `source_system`, `classification`, `recorded_at` and `effective_as_of`.

The distinction between source authority and confidence matters. A relevance score expresses how closely a result matches a query; it cannot establish the authority of the system that supplied the result. Provenance makes that authority inspectable. It does not confer it.

#### Access-aware retrieval and manifest assembly

The first failure in Meridian's case occurs before any disagreement about product status. On 16 February 2027, request `MF-REQ-REF-001` permits reading records, assessing eligibility and preparing a recommendation for an authorised human reviewer. It does not permit issuing the refund.

The retrieval index returns insurance item `MF-REC-INS-LEAK-001` with the incorrect tenant tag `MF-TEN-RET-001`. Its actual tenant is `MF-TEN-INS-001`. The source access check returns DENY, and the item is quarantined before consumption. Events `MF-EVT-002` and `MF-EVT-003` record detection and exclusion; `MF-EVT-004` records the passing synthetic negative test.

An access control list (ACL) attached to an index entry can reduce the candidate set. It cannot be the sole access decision because indexing and source permission changes may occur independently. A document may move between classifications, its reader permissions may change, or the indexing process may associate it with the wrong tenant.

D-11 therefore requires a policy recheck before context is consumed. The Context Retrieval Service, `MF-SVC-CTX-001`, must work within the actor's identity, tenant and applicable source permissions. A candidate that fails the check cannot be passed to the model for summarisation or interpretation. Filtering its generated answer would occur too late.

The Context Manifest records which candidates survive admission. Meridian's `MF-EVD-CM-001` names the access policies `MF-POL-RET-ACCESS-v1.0` and `MF-POL-TENANT-v1.0`. Its two included records and one quarantined result are shown in Table 13-2.

*Table 13-2. Synthetic Context Manifest inclusion and exclusion results; source: MF-EVD-CM-001.*

| Record | Source | ACL result | Consumer recheck | Included |
|---|---|---|---|---|
| MF-REC-A-001 | MF-SYS-PROD-001 | ALLOW | ALLOW | true |
| MF-REC-B-001 | MF-SYS-CRM-001 | ALLOW | ALLOW | true |
| MF-REC-INS-LEAK-001 | MF-SYS-INS-001 | DENY | Not recorded | false |

[Place Figure 13-1 here: Context Manifest Assembly.]

*Figure 13-1. A source-level access recheck admits two retail claims but excludes an incorrectly tagged insurance result (v1.0; synthetic MF-EVD-CM-001).*

*Alt text:* Two retail records pass source authorisation and enter the assembled context. An insurance record returned by a mislabelled index fails the source-tenant check and never reaches the agent.

The manifest is evidence of the selection process, not an unrestricted copy of everything encountered. A quarantine reference can identify the reason for exclusion without exposing the rejected document's contents to the consumer. Access to the manifest itself must respect the applicable classification rules.

The Meridian manifest contains a SHA-256 digest of canonical JSON comprising included record IDs and event references. Its signature field is `NOT_APPLIED_SYNTHETIC_FIXTURE`. The digest illustrates integrity checking over that defined representation; it neither authenticates the origin of the manifest nor establishes the truth of either included claim.

#### Semantic identity and reconciliation

Access checks establish whether the agent may inspect the two retail records. The next question is whether they refer to the same business entity and describe compatible states.

A source identifier identifies a record within a system. A canonical identifier identifies the entity that the record describes across systems. Keeping both allows a reconciliation process to compare claims without discarding their origins. Replacing source identifiers with a canonical identifier alone would make subsequent investigation unnecessarily difficult.

Matching also needs a temporal boundary. A product described as ACTIVE yesterday and CLOSED today may have undergone a legitimate transition. A contradiction arises when incompatible claims concern the same referent, attribute and effective time.

Meridian's Record A and Record B identify customer `MF-CUST-SYN-0042`, product `MF-PROD-0091` and retail tenant `MF-TEN-RET-001`. Both have classification `CONFIDENTIAL_CUSTOMER` and the same owner, `MF-HUM-RET-OWN-001`.

*Table 13-3. Comparison of the two authorised retail claims; source: context-records.json. All times UTC, 22 February 2027.*

| Field | Record A | Record B |
|---|---|---|
| Record ID | MF-REC-A-001 | MF-REC-B-001 |
| Source | Retail Product Registry | Retail CRM |
| Recorded at | 09:00 | 09:10 |
| Effective as of | 00:00 | 00:00 |
| product_status | ACTIVE | CLOSED |
| eligible_for_refund_review | true | false |
| verified_truth | false | false |

The CRM record was recorded ten minutes later. Its business-effective time, however, is identical to that of the Product Registry record. The later timestamp cannot establish that a change of status occurred between the two observations. Nor does the name Product Registry establish precedence without a published rule assigning that authority.

D-14 separates entity matching from the decision about which claim governs a business process. Context owns the match and records the disagreement. The domain data owner defines any applicable precedence rule. Where a valid rule exists, the reconciliation process can apply it and retain the basis for the decision. Where no rule exists, the conflict remains explicit.

On 22 February, `MF-EVT-005` at 09:12:00 and `MF-EVT-006` at 09:12:01 record allowed retrieval of A and B. At 09:12:02, `MF-EVT-007` records the conflict with outcome BLOCKED. At 09:12:03, `MF-EVT-008` records escalation to the steward.

The reconciliation record, created at 09:12:03 UTC, references policy `MF-POL-CTX-CONFLICT-v1.0`. Its status is `UNRESOLVED`, its resolution is `ESCALATE_TO_DOMAIN_DATA_OWNER`, and its effective precedence field reads `NONE_DEFINED; explicit unresolved state retained`. The accountable Retail Data Steward is `MF-HUM-RET-OWN-001`; the follow-up ticket is `MF-TASK-STEWARDSHIP-001`.

[Place Figure 13-2 here: Semantic Reconciliation Workflow.]

*Figure 13-2. Both retail claims remain available as evidence while their incompatible product statuses are preserved as unresolved (v1.0; MF-EVD-RC-001).*

*Alt text:* Two authorised records match the same product and effective date but disagree on status. The reconciliation workflow retains the unresolved state and escalates to the Retail Data Steward without selecting either claim.

A useful result can contain uncertainty. The agent can present the conflicting evidence to a human reviewer, but it cannot report a settled eligibility conclusion. Preserving both records also allows the steward to investigate the systems responsible for the disagreement. The fixture records escalation, not the completion of that investigation.

#### Working context, memory and evidence

The distinction between a claim and a verified fact becomes more consequential when information survives the current task. A wrong conclusion in working context may affect one recommendation. A wrong conclusion in durable memory may influence many later tasks without repeating the original retrieval checks.

Working context is the bounded set of inputs assembled for a particular consumer and purpose. Task-local state holds intermediate computations and progress. The hot or working tier supports the active task; its existence does not imply permission to retain the information indefinitely.

Episodic memory represents selected prior experiences or task episodes. Semantic memory retains knowledge intended for reuse across tasks. These are conceptual memory tiers, not evidence that Meridian populated separate stores. Each durable entry needs a retention and verification decision appropriate to its intended use.

An audit record has a different purpose. It allows an authorised investigator to reconstruct what happened, including unsuccessful actions and rejected claims. It may require retention even when the information is unsuitable for future agent recall. An evidence archive must not become an agent-readable memory store by default.

These distinctions affect retrieval design. A semantic search over previous conversations may return a confident statement about eligibility, although that statement originated in a disputed case. The similarity of the previous and current questions does not establish that the earlier conclusion is valid. Recall requires inspection of provenance, verification status and effective time under current access policy.

#### Governed memory write decisions

D-12 places a separate gate on durable memory writes. A write contract identifies the proposed claim, its source lineage, tenant, owner, classification, retention period and verification status. It also records the effective time, writer actor chain and an idempotency key where retries could create duplicate entries.

Verification should be appropriate to the claim. A task outcome might be established by an attributable execution receipt. A customer eligibility assertion requires evidence and authority suitable for that business decision. A generated answer, even one accepted by a user, does not automatically satisfy either requirement.

The write gate evaluates these conditions before persistent storage. It must preserve the link between a retained claim and the evidence supporting it. If the supporting record is corrected, withdrawn or superseded, that link enables the memory owner to identify affected derived entries.

For Meridian, the reconciliation record's blocked effect is explicit: “No refund.issue and no durable memory assertion of eligibility”. The allowed effect is to show conflicting evidence to a human reviewer. Recording the existence of a dispute as evidence is different from persisting a conclusion that the customer is eligible.

[Place Figure 13-3 here: Governed Memory Write Decision.]

*Figure 13-3. The proposed memory write path holds an eligibility assertion when the source claims remain unresolved (v1.0; required decision process, not a recorded memory transaction).*

*Alt text:* A proposed memory assertion passes through provenance, classification, ownership, retention and contradiction checks before any durable write. The unresolved Meridian eligibility claim follows the hold path; no completed write or receipt is shown.

A deployed implementation needs to handle concurrent changes between validation and storage. For example, a write request can carry the version of the reconciliation record on which it depends. If that version changes before commitment, the gate can require re-evaluation rather than persist a claim under obsolete conditions. This is a design mechanism, not a recorded Meridian event.

The synthetic case contains no performed durable-memory write. Its evidence establishes the blocked effect, not the operation of a deployed memory service.

#### Bounded cross-agent sharing

Agents collaborating on a task often need information produced by another agent. Sharing an unrestricted mutable store makes the receiving agent dependent on every contributor's access checks, retention decisions and interpretation of source claims.

D-13 instead defaults to signed, policy-brokered handoff packets with bounded sharing. A packet identifies its intended audience, tenant, purpose, source references, applicable classification and expiry. The receiving agent revalidates access and relevant policy before consuming the contents. A valid signature supports verification of packet origin and integrity; it does not establish business truth.

The packet must not transfer the sender's credentials or expand the receiver's delegated authority. If a disputed claim is shared, its unresolved status and lineage must travel with it. A summary that drops those attributes changes the meaning of the handoff.

This is the prescribed design approach. Meridian records no signed Context handoff. Its later delegation record belongs to the Identity Control Plane and cannot substitute for such a packet.

#### Refresh, retention and deletion

Durable memory does not remain valid simply because a write was permitted. A source may change, an access grant may expire or the business purpose for retention may end. The Context layer needs refresh and invalidation behaviour that respects Data Protection policy.

A time-to-live can require a claim to be rechecked before reuse. Expiry does not establish that the claim became false; it establishes that continued reliance needs justification. A freshness check must not silently renew a claim whose source is inaccessible.

Deletion must account for derived representations, including embeddings, indexes, caches and handoff copies. Removing a primary row while leaving its searchable representation available defeats the intended access restriction. Where lawful retention or backup holds apply, the policy owner determines the permitted disposition and access restrictions.

A deletion verification procedure should enumerate affected stores, record completion or outstanding exceptions, and test that prohibited retrieval no longer succeeds. Restoration procedures also need to prevent deleted information from becoming accessible again. Meridian records no completed deletion; these are prospective engineering requirements.

The resulting Context contract admits authorised evidence, preserves disagreement and prevents unsupported durable assertions. It supplies unresolved status to downstream consumers. Chapter 16 explains how the Gateway separately enforces external action admission; Chapter 18 explains why a denied action can still accompany a failed behavioural assertion.

### The interface with adjacent layers

The Lifecycle Structural Layer owns the Harness and task progression. It requests bounded context for a particular actor and receives the assembled inputs, manifest and uncertainty status. An unresolved result permits escalation or other authorised review work, rather than silently advancing a task that requires settled eligibility. Context does not own workflow transitions or approval state.

The Tooling Structural Layer supplies typed observations from source reads. Context classifies those observations, attaches lineage and determines their suitability for inclusion. A successful tool response does not by itself establish a verified fact or permission for durable retention.

The Execution Environment provides isolated runtime resources. Workers receive scoped inputs and keep intermediate state within the task boundary. Runtime scratch files and checkpoints require explicit treatment before they become persistent, reusable information.

Identity establishes actor and tenant claims. Governance defines policy and accountable owners, while Data Protection determines classification, retention and deletion obligations. Context applies those constraints to its own data operations. Observability preserves correlated evidence without requiring unrestricted logging of confidential payloads. Interoperability maintains exchange contracts rather than determining source precedence.

Gateway owns external mutable action admission; Verification owns behavioural assertions and release decisions. Neither responsibility transfers to Context when it reports a conflict.

### Failure modes

Context failures can propagate through caches, model inputs and later tasks. The first visible symptom may therefore occur well after the original retrieval or write. Table 13-4 identifies the failure at the boundary where an operator can investigate it.

*Table 13-4. Context failure modes and required controls; design guidance, not a production incident inventory.*

| Failure | Cause | Observable symptom | Control |
|---|---|---|---|
| Tenant mislabel | Incorrect index metadata | Candidate tenant differs from source tenant | Source ACL recheck; quarantine (D-11) |
| Stale access | Index or cache misses a permission change | Previously permitted record remains retrievable | Revalidate before consumption (D-11) |
| Alias collision | Different entities mapped to one identifier | Claims combine unrelated customers or products | Preserve source IDs; verify canonical mapping (D-14) |
| Silent contradiction | Recency used as precedence | One incompatible value disappears | Explicit conflict state and steward escalation (D-14) |
| Context poisoning | Untrusted content treated as instructions or verified facts | Retrieved text changes task behaviour | Separate data from instructions; test hostile inputs |
| Unverified memory | Generated conclusion persisted without evidence | Later recall lacks attributable verification | Governed write gate (D-12) |
| Handoff replay | Expired packet accepted | Old data enters a new task under obsolete policy | Validate audience, expiry and policy (D-13) |
| Incomplete deletion | Derived stores omitted | Deleted information remains retrievable | Verify propagation across stores (D-12) |

The remediation depends on which contract failed. An index defect belongs with the retrieval operator and relevant source owner. A disputed business attribute belongs with its steward. Adding more retrieval capacity does not resolve either kind of failure.

### Scaling signal

Scale authorised retrieval workers against queue depth and source recheck latency, rather than raw index-hit volume. An illustrative operator-set trigger is p95 queue wait above 200 ms for five minutes, provided the source systems have spare capacity. The Context service owner must calibrate that threshold against workload objectives and source rate limits; it is not a Meridian measurement.

Quality signals include provenance coverage, source recheck failures, cross-tenant exclusion rate, index freshness lag and unresolved-conflict age. Memory owners also track write rejection, verification backlog and deletion propagation age. The relevant policy and data owners set acceptable limits.

If rechecks become unavailable, the service preserves quarantine and reports insufficient evidence. It does not relax tenant restrictions to meet a latency target. Stewardship backlog requires owner capacity or revised business processes, not simply more retrieval workers.

### Anti-patterns

#### AP-13-01: Similarity equals truth

**What it looks like.** The highest-ranked claim, or the most recently recorded claim, becomes the product's accepted status.

**Why it happens.** Retrieval relevance and recording time are used as substitutes for business authority.

**Why it fails.** Two authorised records can describe the same entity at the same effective time and disagree.

**The correct pattern.** Apply D-14, retain source lineage and route unresolved conflicts to the domain data owner.

**Detection signal.** Incompatible claims are merged without a corresponding Reconciliation Record.

#### AP-13-02: Shared memory by convenience

**What it looks like.** Agents write retrieved information and generated conclusions into a common mutable store.

**Why it happens.** Reuse avoids repeated retrieval and handoff validation.

**Why it fails.** Readers can acquire information outside their tenant or purpose, and unverified conclusions can survive the originating task.

**The correct pattern.** Use D-11 access rechecks, D-12 write controls and D-13 bounded sharing.

**Detection signal.** An unauthorised cross-tenant source appears in a consumer manifest, or a recalled claim lacks verification provenance.

#### AP-13-03: Delete the row, not the copies

**What it looks like.** A primary memory entry is removed while its indexed or cached representations remain available.

**Why it happens.** Retention is implemented as a single-store operation.

**Why it fails.** A later retrieval can recover information that policy requires to be inaccessible.

**The correct pattern.** Apply D-12 correction and deletion requirements with the Data Protection controls in Chapter 21.

**Detection signal.** A negative retrieval test returns a prohibited representation after deletion.

### Decisions to make

- D-11: Control retrieval access. Specify source access and consumer rechecks.
- D-12: Govern durable memory. Define the evidence and policy requirements for persistence.
- D-13: Enable cross-agent memory. Define bounded, policy-brokered sharing conditions.
- D-14: Reconcile semantic identities. Establish canonical matching, precedence ownership and unresolved escalation.

### Defaults

- D-11: Default to ACL-aware retrieval, source-level provenance and policy rechecks before context is consumed.
- D-12: Default to no durable memory write without provenance, policy classification, owner, retention and verification status.
- D-13: Default to signed, policy-brokered handoff packets with bounded sharing; do not share unrestricted mutable memory.
- D-14: Default to canonical IDs with source lineage and explicit unresolved-conflict states; never silently choose the newest record as truth.

### Artefacts to produce

- `context-manifest-schema.json`: inclusion and quarantine contract (example: `MF-EVD-CM-001`).
- `memory-write-contract.json`: durable write and correction requirements.
- `semantic-claim-reconciliation.json`: explicit conflict representation (example: `MF-EVD-RC-001`).
- `context-negative-tests.md`: access, conflict and unsafe-recall assertions.
- `context-deletion-receipts.csv`: deletion verification format.

The D-11–D-14 Atlas pages provide the associated retrieval policy, handoff schema and reconciliation specifications.

### See also

- Chapter 7: Tenant Isolation and Sovereignty (data boundaries).
- Chapter 14: Lifecycle (Harness consumption and checkpoints).
- Chapter 15: Identity Control Plane (actor and tenant claims).
- Chapter 18: Verification Control Plane (behavioural assertions).
- Chapter 21: Data Protection Control Plane (retention and erasure).

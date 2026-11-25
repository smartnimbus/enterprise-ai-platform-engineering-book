# Chapter 13: Context

On 22 February 2027, the retail agent at fictional Meridian Financial had two records for a GBP 125 refund review and no established basis for deciding eligibility. The Retail Product Registry reported the product as ACTIVE. The customer relationship management (CRM) system reported it as CLOSED. Both described the same effective date.

Six days earlier, an insurance record had appeared among retail search results but failed the source access check. The agent could not consume it. The retail records presented a different problem: both could be read, but neither settled the decision. The synthetic Meridian fixture preserves that disagreement in the Semantic Reconciliation Record, `MF-EVD-RC-001`.

### What this layer decides

**The mechanism.** Context determines which information an agent may consume, how source claims retain their identity and authority, and whether assertions qualify for durable reuse under the governing policies.

### The mechanism

#### From retrieved information to usable evidence

The insurance record fails admission. The retail records pass admission but disagree. Neither admission nor a generated interpretation justifies retaining an eligibility conclusion. The Context Structural Layer separates admission, interpretation, and persistence rather than treating retrieval success as knowledge.

*Table 13-1. Context responsibilities and inspectable outputs.*

| Component group | Responsibility | Output |
|---|---|---|
| Retrieval | Find candidates and check source access | Authorised observations |
| Assembly | Bound inputs to the consumer and purpose | Context Manifest |
| Reconciliation | Match entities and preserve disagreements | Reconciliation Record |
| Memory | Evaluate proposed retention and reuse | Write disposition |
| Handoff | Broker information sharing under receiving policy | Bounded context packet |

An investigator needs to identify which observations entered a particular assembly. A proposed schema uses `context_id`, `source_id`, and `source_version` for that purpose. The `tenant_id`, `subject_id`, and `data_class` delimit their applicability; `valid_from` and `observed_at` distinguish effective and observation time. The fields `authority` and `confidence` remain separate because ranking a claim cannot confer business precedence. The `retention_class` and `provenance_hash` support disposition and integrity checks.

These are design fields, not additions to Meridian's JSON. The fixture uses names including `id`, `source_system`, `classification`, `recorded_at`, and `effective_as_of`.

#### Admission, consumption, and the Context Manifest

D-11 treats preliminary index filtering as candidate selection, not final authorisation. Identity supplies verified actor and tenant assertions. Retrieval ranks candidates and applies access control list (ACL) filters; Context checks applicable source permissions and classification before assembly.

An indexing service may read a collection that the consuming agent cannot read in full. Its credential cannot answer the consumer's permission question. Source admission establishes access to the record; the consumer recheck establishes whether the assembled observation remains permitted for the intended recipient and purpose.

A permission change between indexing and consumption can invalidate an earlier decision. Cached payloads therefore require current policy validation before reuse. Where access cannot be established, Context excludes the affected material and reports insufficient evidence if the remaining inputs cannot support the task. It does not treat an unavailable permission service as approval.

Request `MF-REQ-REF-001` permits review and preparation, not refund execution. On 16 February 2027, the index returns `MF-REC-INS-LEAK-001` under the incorrect retail tenant tag `MF-TEN-RET-001`. The actual tenant is `MF-TEN-INS-001`.

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

An investigator starts with the Context Manifest, not the generated answer. Manifest `MF-EVD-CM-001` identifies agent `MF-AGT-RET-004`, retail tenant `MF-TEN-RET-001`, retrieval request `MF-RETR-001`, and trajectory `MF-TRJ-001`. It references policies `MF-POL-RET-ACCESS-v1.0` and `MF-POL-TENANT-v1.0`. These anchors identify the assembly under examination rather than all information the retrieval service could access.

The investigator follows the admitted record IDs to their source observations and the quarantine reference to the exclusion reason. The manifest's `conflict_ref` leads to `MF-EVD-RC-001`, which limits the use of the admitted claims. The investigator can identify both admitted records without mistaking either for a settled eligibility decision.

The manifest itself requires controlled access. Quarantine metadata can support investigation without exposing the rejected payload to the consumer. Its SHA-256 digest covers canonical JSON containing included record IDs and event references. The field `cryptographic_signature` reads `NOT_APPLIED_SYNTHETIC_FIXTURE`; the digest neither authenticates the record's origin nor verifies the entire source payload.

D-11 incurs additional source checks, filtering, and possible missed matches. The relevant performance measure is authorised retrieval, not unrestricted recall. A higher recall score achieved by exposing another tenant's documents measures the wrong outcome.

#### Semantic identity, authority, and reconciliation

Both retail records are relevant and accessible. Neither property establishes which status governs eligibility. Relevance ranks evidence; confidence expresses uncertainty. Authority identifies who may establish the business attribute, while precedence identifies the governing source under an applicable rule. A more confident interpretation cannot replace that rule or establish verified truth without sufficient evidence.

Context first establishes whether the claims concern the same entity. The canonical product identifier establishes their common referent; separate source record IDs let the steward inspect both observations instead of an aggregated value. An ambiguous match warrants investigation rather than a merge.

ACTIVE followed by CLOSED may describe a legitimate transition. In Meridian, both sources describe the product at the same effective instant. The comparison therefore needs business-effective time as well as source recording time.

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

The record permits presentation of conflicting evidence to a human reviewer. It does not settle eligibility. D-14 leaves the dispute visible and incurs stewardship work rather than concealing it behind a guessed status.

#### Working context, memory, and evidence

An unresolved claim does not acquire authority when the task ends. A checkpoint can preserve the progress of the refund review without making its provisional conclusions reusable knowledge. Working context supplies bounded read-time inputs; task-local state retains intermediate results for continuation. The conceptual hot or working tier supports the active task.

Episodic memory could retain the experience of handling a dispute; semantic memory could retain an assertion intended for reuse. Retaining the former does not justify accepting the latter. On recall, both require applicable provenance, access, effective-time, and verification checks. Embedding proximity cannot establish that an earlier conclusion still applies.

Consider a hypothetical agent that retains a generated eligibility conclusion after completing a disputed case. Later trajectories retrieve that conclusion instead of the underlying source claims. Each reuse can compound the error, even if the original source conflict remains unchanged. D-12 constrains this propagation at the write boundary.

The Reconciliation Record may preserve a dispute for authorised investigation without making either disputed value available as established knowledge. Audit evidence retains attributable decisions, including rejected claims and failed actions. It is not an unrestricted agent memory store. These distinctions describe conceptual storage obligations, not deployed Meridian memory services.

#### Governed memory writes

A memory assertion can satisfy its schema and still fail its write policy. Both retail observations carry `verified_truth=false`. Supplying a verification-status field does not establish that an eligibility claim qualifies for durable reuse.

Under D-12, the proposed write carries the claim and source lineage, writer actor chain, tenant, owner, classification, effective time, verification status, and retention conditions. The memory owner applies the governing verification and retention policy, including consent or legal-class restrictions where applicable. The disposition records whether those conditions justify persistence and intended reuse.

A retry key cannot make an invalid claim valid. Idempotency distinguishes repeated submission from a new assertion; it does not protect against a change in source state between validation and commitment.

If a writer validates an assertion against one reconciliation version, a concurrent change can invalidate that decision before storage. A conditional write can bind commitment to the validated version. Where atomic version validation is unavailable, another consistency mechanism must prevent publication under obsolete validation. Dependency references allow later correction or invalidation of derived entries.

Meridian's reconciliation record specifies the blocked effect: "No refund.issue and no durable memory assertion of eligibility". The recorded dispute may support human review; an eligibility conclusion cannot qualify on that basis.

[Place Figure 13-3 here: Governed Memory Write Decision.]

*Figure 13-3. The proposed memory write path holds an eligibility assertion when the source claims remain unresolved (v1.0; required decision process, not a recorded memory transaction).*

*Alt text:* A proposed write undergoes provenance, ownership, policy, retention, and contradiction checks. The unresolved eligibility claim follows the hold path; no completed memory write or receipt is shown.

No performed durable-memory write appears in the fixture. The design explains how D-12 would enforce the restriction, at the cost of verification effort, storage management, and correction work.

#### Bounded cross-agent sharing

A second agent could receive an accurate summary of the retail dispute without possessing the first agent's source permissions. Removing UNRESOLVED from that summary would also change the claim's meaning. Information transfer establishes neither receiving authority nor truth.

D-13 defaults to signed, policy-brokered handoff packets. The sender supplies bounded information or references; the broker evaluates sharing under the recipient's identity, tenant, and purpose.

A handoff contract identifies its audience, classification, source lineage, retention limits, expiry, and verification or conflict status. The recipient validates the signature and rechecks applicable access before consumption. A signature authenticates the signed content under the applicable trust assumptions; it does not establish source truth or current permission.

A reference allows the recipient to make an independent access decision without copying the sender's credential. Both lineage and unresolved status must survive the transfer.

Expiry limits the period of use but does not prevent repeated submission inside that period. Where repetition matters, recipient-bound packet identifiers and replay tracking can supplement expiry checks. Bounded sharing incurs validation overhead and sometimes repeated retrieval, but avoids unrestricted mutable memory across agents.

Meridian records no signed Context handoff. Its delegation record belongs to Identity and is not evidence of information sharing.

#### Refresh, retention, and deletion

Restoring a backup does not restore permission to consume its contents. A retained assertion may have been corrected, expired, or become inaccessible since the backup was made. Refresh rechecks its sources; expiry ends reliance without renewed justification. Invalidation stops use pending correction or disposition. A time-to-live cannot renew revoked permission.

The lineage required by D-12 also defines the deletion investigation. A deletion receipt distinguishes primary records, indexes, embeddings, caches, and handoff copies, recording verified outcomes and outstanding exceptions. Where lawful retention applies, the applicable policy determines restricted retention or disposition rather than promising immediate removal.

Recovery procedures reapply disposition restrictions before restored information enters retrieval. Negative tests inspect whether prohibited representations can enter Context, not whether the agent omits them from its answer. The fixture records no deletion or restoration outcome.

#### What the evidence establishes

The manifest establishes the recorded admission outcomes; reconciliation establishes an unresolved disagreement and its referral. Neither establishes eligibility. The two records supply the downstream precondition. In Week 9, Gateway denies the proposed mutation. In Week 11, Verification's `MF-EVD-RG-001` records failure of assertion `MF-ASSERT-CTX-001`: the candidate selected `refund.issue` instead of abstaining and escalating. Zero side effects do not make that behaviour acceptable. Chapters 16 and 18 explain the separate admission and release decisions.

### The interface with adjacent layers

The Harness receives more than retrieved text. Its request identifies the actor, task, and required information; Context returns admitted observations, the manifest, and unresolved status. Lifecycle owns progression and escalation. Removing the uncertainty removes information necessary to that decision.

A typed Tooling response becomes an input only after Context applies classification and access rules and attaches lineage. Execution Environment isolates consumption and task state; a checkpoint does not authorise durable reuse.

Identity supplies verified actor and tenant assertions. Governance manages policy ownership, approval, and exceptions; the domain data owner defines business precedence. Data Protection determines applicable classification, retention, and deletion constraints.

An investigator correlates the manifest with its trajectory through Observability without unrestricted payload logging. Interoperability preserves the meaning of exchanged claims and their schemas; FinOps accounts for retrieval, storage, and verification capacity.

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

Inspect the consumer inputs and side effects, not only the answer. Retrieval operators investigate admission defects; domain stewards investigate disputed attributes, and memory owners investigate invalid retained assertions.

### Scaling signal

Context capacity depends on both local workers and source dependencies. Consider an illustrative service objective of 800 ms for context assembly, with 200 ms allocated to queue wait. Sustained p95 queue delay above that allowance can trigger worker scaling if source capacity remains available. These are example budgets, not Meridian measurements.

The service owner monitors recheck latency, source failures, and index freshness. Provenance completeness and cross-tenant exclusions measure different properties from throughput. Stewardship queue age, memory verification backlog, and deletion propagation age require owner-specific limits.

Additional workers cannot settle disputed business facts. Retrieval delay consumes a latency budget; unresolved claims consume stewardship capacity. During access-check failure, Context preserves exclusions and reports insufficient evidence rather than relaxing policy.

### Anti-patterns

#### AP-13-01: Similarity equals truth

**What it looks like.** The highest-ranked or newest claim becomes the accepted product status.

**Why it happens.** A team optimises relevance but has no approved precedence rule.

**Why it fails.** Both retail observations match the query and still disagree.

**The correct pattern.** Apply D-14 with canonical identity, explicit precedence, and steward escalation.

**Detection signal.** Incompatible values merge without a Reconciliation Record.

#### AP-13-02: Shared memory by convenience

**What it looks like.** A later agent inherits a generated eligibility conclusion without its original evidence.

**Why it happens.** Reuse substitutes for retrieval and receiving-policy checks.

**Why it fails.** The recipient cannot establish permission or the claim's verification status.

**The correct pattern.** Apply D-11 admission checks, D-12 write policy, and D-13 bounded handoffs.

**Detection signal.** A recalled claim lacks verification provenance or an unauthorised source enters context.

#### AP-13-03: Delete the row, not the copies

**What it looks like.** A primary entry disappears but its derived index remains searchable.

**Why it happens.** The deletion operation changes one store and leaves derived representations untouched.

**Why it fails.** A later assembly can admit a prohibited copy.

**The correct pattern.** Apply D-12 disposition requirements and Chapter 21 Data Protection controls across derived stores.

**Detection signal.** A negative retrieval test exposes the prohibited representation in actual Context inputs.

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

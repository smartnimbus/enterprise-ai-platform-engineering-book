# Chapter 13: Context

On 22 February 2027, the retail agent at fictional Meridian Financial had two records for a GBP 125 refund review and no established basis for deciding eligibility. The Retail Product Registry reported the product as ACTIVE. The customer relationship management (CRM) system reported it as CLOSED. Both described the same effective date.

Six days earlier, an insurance record had appeared among retail search results but failed the source access check. The agent could not consume it. The retail records presented a different problem: both could be read, but neither settled the decision. The synthetic Meridian fixture preserves that disagreement in the Semantic Reconciliation Record, `MF-EVD-RC-001`.

### What this layer decides

**The mechanism.** Context determines which information an agent may consume, how source claims retain their identity and authority, and whether assertions qualify for durable reuse under the governing policies.

### The mechanism

#### From retrieved information to usable evidence

The insurance record fails admission. The retail records pass admission but disagree. Neither admission nor a generated interpretation justifies retaining an eligibility conclusion. Context, a Structural Layer, records separate decisions for admission, reconciliation, and durable reuse.

*Table 13-1. Context responsibilities and inspectable outputs.*

| Component group | Responsibility | Output |
|---|---|---|
| Retrieval | Find candidates and check source access | Authorised observations |
| Assembly | Bound inputs to the consumer and purpose | Context Manifest |
| Reconciliation | Match entities and preserve disagreements | Reconciliation Record |
| Memory | Evaluate proposed retention and reuse | Write disposition |
| Handoff | Broker information sharing under receiving policy | Bounded context packet |

A product identifier alone cannot reconstruct the inputs to the refund review. In a proposed Context schema, `context_id` identifies the assembly; `source_id` and `source_version` identify the observation it used. The `tenant_id`, `subject_id`, and `data_class` delimit who and what it concerns.

The pair `valid_from` and `observed_at` prevents a later observation from masquerading as a later business state. Separate `authority` and `confidence` fields preserve the difference between precedence and uncertainty. A `retention_class` governs disposition; a `provenance_hash` supports an integrity check, not a truth determination.

These proposed fields are not Meridian's JSON. The fixture uses `id`, `source_system`, `classification`, `recorded_at`, and `effective_as_of`. Its first question is whether a returned record enters the assembly at all.

#### Admission, consumption, and the Context Manifest

D-11 treats preliminary index filtering as candidate selection, not final authorisation. Identity supplies verified actor and tenant assertions. Retrieval ranks candidates and applies access control list (ACL) filters; Context checks applicable source permissions and classification before assembly.

An indexing service may read a collection that the consuming agent cannot read in full. Its credential cannot answer the consumer's permission question. Source admission checks source permissions. Consumer rechecks evaluate the assembled input for its actual recipient and purpose.

A cached ALLOW result can outlive the permission it records. A later assembly must recheck that permission, not inherit the previous manifest's decision. If access cannot be established, Context excludes the material and reports insufficient evidence when the remaining inputs cannot support the task.

Request `MF-REQ-REF-001` permits review and preparation, not refund execution. On 16 February 2027, the index returns `MF-REC-INS-LEAK-001` under the incorrect retail tenant tag `MF-TEN-RET-001`. The actual tenant is `MF-TEN-INS-001`.

The source check rejects the item with reason `SOURCE_TENANT_MISMATCH`. Events `MF-EVT-002` and `MF-EVT-003` record detection and quarantine; `MF-EVT-004` records the passing synthetic negative test. The fixture records no insurance payload in the retail agent's Context. Filtering a generated answer would occur after disclosure to the model.

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

The investigator follows the admitted record IDs to their source observations and the quarantine reference to the exclusion reason. The `allowed_use` field restricts the assembly to review, and `conflict_ref` leads to the disputed status. Two ALLOW results establish recorded admission, not eligibility.

The manifest and the negative-test event answer different questions. One records admission; the other records a passing synthetic exclusion test. Neither independently demonstrates that every component of a deployed system prevented disclosure.

Quarantine metadata supports investigation without exposing the rejected payload; the manifest itself requires controlled access. Its SHA-256 digest covers canonical JSON containing included record IDs and event references. The field `cryptographic_signature` reads `NOT_APPLIED_SYNTHETIC_FIXTURE`; the digest neither authenticates the record's origin nor verifies the entire source payload.

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

An unresolved claim does not acquire authority when the task ends. The working Context supplies the observations for the refund review. Task-local state preserves progress for resumption. A checkpoint can retain the outstanding review without qualifying its provisional conclusions for durable reuse. The hot or working tier serves this active task.

Episodic memory could preserve the experience of escalating a dispute. Semantic memory would retain an assertion intended for reuse as knowledge. The distinction changes the next trajectory: recalling that a dispute occurred supports investigation, whereas recalling that the customer qualifies for a refund could affect a financial recommendation.

Neither memory tier bypasses access, provenance, effective-time, or verification checks on recall. Embedding proximity cannot establish that a previous claim remains applicable. Later recall could propagate unsupported eligibility without either source observation.

The Reconciliation Record serves a different purpose. Immutable audit evidence preserves the disagreement, its attribution, and the decision to escalate, including failed or rejected actions where relevant. Retaining that evidence for authorised investigation does not make either status established knowledge. These are conceptual storage obligations, not deployed Meridian memory services.

#### Governed memory writes

A memory assertion can satisfy its schema and still fail its write policy. Both retail observations carry `verified_truth=false`. A proposed assertion that the customer qualifies for a refund would need evidence sufficient for that intended reuse, not merely a recorded verification status.

D-12 requires a justified write. The writer actor chain, tenant, and owner identify who proposes and owns the claim. Source lineage, effective time, and verification status identify the justification; policy classification and retention conditions constrain use. The memory owner applies the governing verification policy and records the disposition. Consent or legal-class restrictions apply where required.

A hold or rejection preserves the difference between review evidence and reusable eligibility. A write contract must expose the justification, not just metadata completeness.

Retries introduce a separate problem. Idempotency distinguishes repeated submission from a new assertion; it cannot make an invalid claim valid. Suppose a writer validates a claim against one reconciliation version, then the source changes before commitment. Reusing the earlier validation could publish an obsolete claim even if duplicate detection works.

A conditional write can bind commitment to the validated version. Atomic version validation or equivalent consistency protection prevents publication under obsolete validation. Dependency references allow correction or invalidation when the source changes.

Meridian's reconciliation record specifies the blocked effect: "No refund.issue and no durable memory assertion of eligibility". This is a restriction, not a transaction.

[Place Figure 13-3 here: Governed Memory Write Decision.]

*Figure 13-3. The proposed memory write path holds an eligibility assertion when the source claims remain unresolved (v1.0; required decision process, not a recorded memory transaction).*

*Alt text:* A proposed write undergoes provenance, ownership, policy, retention, and contradiction checks. The unresolved eligibility claim follows the hold path; no completed memory write or receipt is shown.

No performed durable-memory write appears in the fixture. D-12 incurs write-path verification and maintenance rather than transferring the cost of correcting an unsupported assertion to every later consumer. A qualified assertion still needs a separate decision before another agent can use it.

#### Bounded cross-agent sharing

A second agent could receive an accurate summary of the retail dispute without possessing the first agent's source permissions. Removing UNRESOLVED from that summary would also change the claim's meaning. Information transfer establishes neither receiving authority nor truth.

D-13 defaults to signed, policy-brokered handoff packets with bounded sharing. The sender provides information or references; the broker evaluates sharing for the recipient's identity, tenant, and purpose. Audience and classification delimit the transfer. Lineage and conflict status preserve its meaning; expiry and retention delimit continuing use.

The recipient checks the signature and revalidates access. Authentic content does not establish business truth or current permission. A receiving-policy denial need not invalidate the sender's access.

Expiry alone cannot distinguish a repeated handoff from a new one. Where repeated acceptance could duplicate processing or reintroduce a disputed claim, recipient-bound packet identifiers and replay tracking can supplement expiry checks. Repeated retrieval has a cost, but unrestricted shared memory would obscure whose authority permitted the input.

Meridian records no signed Context handoff. Its delegation record belongs to Identity.

#### Refresh, retention, and deletion

Restoring a backup does not restore permission to consume its contents. Suppose a retained assertion's source changes or access is revoked. Refresh checks whether the evidence still supports the claim. Expiry ends reliance without renewed justification; invalidation stops use while correction or disposition proceeds. A time-to-live cannot renew revoked permission.

The lineage required by D-12 identifies the representations affected by a deletion decision: primary records, indexes, embeddings, caches, and handoff copies. A deletion receipt identifies addressed representations, verified outcomes, and outstanding exceptions. Lawful retention may require restricted access to a backup rather than immediate removal.

A receipt and a negative retrieval test answer different questions. The receipt accounts for disposition; the test checks whether a prohibited representation can still enter Context. Recovery reapplies restrictions before exposing restored information to retrieval. Meridian records no deletion or restoration outcome.

#### What the evidence establishes

The manifest records admission; reconciliation records the unresolved conflict and referral. Neither establishes eligibility. On 1 March 2027 (Week 9), Gateway denies the proposed mutation. On 15 March (Week 11), Verification's `MF-EVD-RG-001` records failure of behavioural assertion `MF-ASSERT-CTX-001`. The candidate selected `refund.issue` instead of abstaining and escalating.

Zero side effects do not make that behaviour acceptable. Promotion is blocked; no production deployment occurs. Chapters 16 and 18 explain the separate decisions.

### The interface with adjacent layers

A typed Tooling response is not yet a Context input. Identity establishes actor and tenant assertions, Governance owns policy approval and exceptions, and Data Protection determines classification, retention, and deletion constraints. Context applies those constraints before assembly and records source lineage. The domain data owner, not Context, establishes business precedence.

The Harness receives more than retrieved text. It requests information for an actor and task; Context returns the admitted observations, manifest, and unresolved status. Without that status, Lifecycle loses the basis for escalation. Execution Environment isolates the consumer and its task-local state; resumption does not confer durable-memory authority.

Interoperability governs schema and contract versioning; Observability correlates the assembly with its trajectory without unrestricted payload logging. FinOps accounts for retrieval, storage, and verification costs.

Gateway evaluates mutable action admission using the unresolved precondition and independent authority evidence. Verification evaluates the behaviour that proposed the action. A correctly recorded conflict grants neither execution permission nor release approval.

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

If source checks stall while workers remain idle, adding workers will not restore the budget. Source failures and index freshness help diagnose that constraint. Provenance completeness and cross-tenant exclusions assess admission quality; memory verification backlog, stewardship queue age, and deletion propagation age need separate limits.

Additional workers cannot settle disputed business facts. Retrieval delay consumes a latency budget; unresolved claims consume stewardship capacity. During access-check failure, Context preserves exclusions and reports insufficient evidence rather than relaxing policy.

### Anti-patterns

#### AP-13-01: Similarity equals truth

**What it looks like.** The highest-ranked or newest claim becomes the accepted product status.

**Why it happens.** A team optimises relevance but has no approved precedence rule.

**Why it fails.** Optimising the ranking cannot supply a missing precedence rule.

**The correct pattern.** Apply D-14 with canonical identity, explicit precedence, and steward escalation.

**Detection signal.** Incompatible values merge without a Reconciliation Record.

#### AP-13-02: Shared memory by convenience

**What it looks like.** A later agent inherits a generated eligibility conclusion without its original evidence.

**Why it happens.** Reuse substitutes for retrieval and receiving-policy checks.

**Why it fails.** The recipient inherits an assertion without the evidence needed to establish permission or verification status.

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

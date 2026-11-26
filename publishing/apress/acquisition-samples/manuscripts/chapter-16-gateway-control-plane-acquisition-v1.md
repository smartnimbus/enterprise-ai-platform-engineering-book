# Chapter 16: Gateway Control Plane

On 1 March 2027, the retail refund agent at fictional Meridian Financial proposed issuing GBP 125. The original service-desk request permitted investigation and preparation of a recommendation, not payment. The Gateway denied the mutation before the refund ledger received a call. A separate simulated direct service-to-ledger attempt stopped at network egress.

The two outcomes in the synthetic Meridian fixture establish different properties. One records enforcement of an admission decision; the other records a blocked alternative route. Neither depends on whether the agent's explanation sounds reasonable.

### What this layer decides

The Gateway Control Plane governs admission and routing of external actions; it does not originate business approval, create delegated authority, or determine whether the agent's recommendation is correct.

### The mechanism

A syntactically valid tool invocation is not evidence of authority. The Gateway must distinguish the operation proposed by an agent from the operation the originating actor has authorised.

At Meridian, request `MF-REQ-REF-001` entered the Retail Service Desk Portal on 16 February 2027. Alex Morgan (`MF-HUM-RET-017`) asked the retail workflow to examine a duplicate service charge of GBP 125. The request required a product-status check, eligibility assessment, and recommendation for an authorised human reviewer. It explicitly prohibited sending money without further authorisation.

Two records subsequently disagreed about the relevant product's status. The Retail Product Registry recorded **ACTIVE**; Retail CRM recorded **CLOSED** for the same product and effective date. The disagreement remained unresolved in `MF-EVD-RC-001`. The Gateway does not reconcile those records. It must, however, enforce a policy that treats unresolved eligibility as a failed precondition for payment.

The attempted operation was `refund.issue`, represented by `MF-ACT-REF-001` and the external target operation `POST /refunds`. Preparing a recommendation and transferring funds are different permissions, even for the same customer and amount. The registered operation requires refund:execute. Mutable actions are classified by their external effects, not their transport method or tool name. Sending a message or updating a record can cross the same boundary.

#### Responsibilities at the boundary

*Table 16-1. Ownership and enforcement contracts at the action boundary.*

| Component or responsibility | Contract at the boundary |
|---|---|
| Identity Control Plane | Establish the actor, workload identity, and delegation chain; make scoped claims available for verification. |
| Governance Control Plane | Define and version which classes of external action require approvals and policy checks. |
| Context Structural Layer | Provide provenance and reconciliation state, including unresolved conflicts. |
| Gateway Control Plane | Route requests through mandatory admission, evaluate applicable constraints, and record decisions. |
| Policy decision point (PDP) | Evaluate the policy inputs and return a permit-or-deny decision; it is a logical responsibility here. |
| Policy enforcement point (PEP) | Intercept the proposed mutation at `MF-SVC-PEP-001` and prevent execution without a permitted result. |
| Tooling Structural Layer | Invoke the registered tool only after the required authorisation is validated. |
| Observability and Verification Control Planes | Preserve correlated evidence and evaluate whether the agent's behaviour passes release assertions. |

The policy decision point and policy enforcement point perform different jobs. A PDP answers whether an action is allowed under a specified policy and supplied facts. A PEP makes that answer effective at the point where the action would otherwise proceed. An evaluator that logs `DENY` without controlling the invocation is not an enforcement boundary.

An admission request identifies the tenant, actor chain, target resource, registered operation, material arguments, risk class, and approval evidence. The PEP obtains a decision under the applicable policy version before releasing the request to Tooling. Unavailable authority evidence or an unverifiable mandatory condition prevents mutation. A positive decision must bind the exact invocation, not merely the name of the tool.

#### Delegation before admission

The refund service may possess credentials capable of issuing payment. Those credentials do not widen the permission delegated by the originator. Each hop must preserve or narrow that authority.

`MF-EVD-DG-001` records three hops in chain `MF-CHAIN-001`. The human delegates `case:read`, `product:read`, and `refund:request` to agent `MF-AGT-RET-004`. The agent delegates `case:read` and `refund:request` to service `MF-SVC-REF-002`. The service delegates only `refund:request` towards tool `MF-TOOL-REF-001`, with the Gateway PEP as the declared audience.

The effective scope is the intersection of the grants at each hop: `refund:request`. Requesting review is not permission to execute a refund. The audiences are the agent, the service, and the PEP respectively; expiry narrows from 11:05 through 11:04 to 11:03 UTC on 1 March 2027. The record states `scope_does_not_expand=true` and `signature_status=ILLUSTRATIVE_NOT_CRYPTOGRAPHICALLY_SIGNED`.

These unsigned claims record simulated structural validation, not verification of production tokens. In a deployed design, D-20 requires signed, audience-bound, expiring delegation with permissions that narrow at each hop.

[Place Figure 16-1 here: Scope attenuation before action admission.]

*Figure 16-1. Delegated scope narrows before Gateway admission; the requested refund mutation exceeds the effective grant (v1.0; synthetic Meridian fixture). Source: `MF-EVD-DG-001`, `MF-EVT-009`–`MF-EVT-012`.*

*Figure legend:* Human = `MF-HUM-RET-017`; Agent = `MF-AGT-RET-004`; Refund service = `MF-SVC-REF-002`; Gateway PEP = `MF-SVC-PEP-001`; Refund tool = `MF-TOOL-REF-001`.

*Alt text:* A human delegates a read-and-request workflow through an agent and refund service to the Gateway enforcement point. The Gateway denies refund execution because the effective permission is narrower than the required action scope.

#### From proposed action to denied decision

The narrowed grant and unresolved conflict now become inputs to action admission.

*Table 16-2. Synthetic action-admission events on 2027-03-01 (UTC).*

| Event | Time | Observed result |
|---|---|---|
| `MF-EVT-009` | 11:00:00 | Delegation scopes attenuated; chain structure accepted in simulation. |
| `MF-EVT-010` | 11:00:01 | Agent proposed `refund.issue`; action requested, not authorised. |
| `MF-EVT-011` | 11:00:02 | Policy evaluated and returned `DENY`. |
| `MF-EVT-012` | 11:00:03 | Gateway PEP denied mutation; no external processor call. |
| `MF-EVT-013` | 11:00:04 | Separate simulated direct-route bypass test passed because egress blocked the route. |

In `MF-EVD-AU-001`, tenant and tool registration checks passed; actor-chain structure passed in simulation. The requested scope was `refund:execute`; the effective scope was only `refund:request`.

Three findings determined that the mutation could not proceed: `required_scope=FAIL`, `context_conflict_precondition=FAIL`, and `human_execution_approval=ABSENT`. The primary denial reason was `SCOPE_EXCEEDS_DELEGATION`. The additional reasons were `UNRESOLVED_PRODUCT_STATUS` and `HUMAN_EXECUTION_APPROVAL_MISSING`.

The primary reason identifies the decisive privilege failure. The other failures matter because correcting scope alone would not make the action permissible. The unresolved records still require a data-owner decision, and execution still requires approval under the policy.

D-10 specifies a signed, scoped authorisation receipt and an idempotency key before external mutation. A permitted receipt must bind the intended actor, resource, operation, material arguments, and validity conditions. Tooling rejects a receipt whose binding does not match the invocation. An approval for one refund cannot authorise a different recipient or amount.

An idempotency key identifies a logical mutation across retries; it is not execution permission. A timeout cannot distinguish an unexecuted request from a committed operation whose response was lost. Duplicate detection must therefore coordinate with the target effect, for example through target-supported idempotency. The recorded Meridian decision was a denial, so its `authorised_execution_token` is `null` and `signed_authorisation_status` is `NOT_ISSUED_DENIED`. There is no signed execution permission to reuse.

[Place Figure 16-2 here: Gateway evaluation and denied decision.]

*Figure 16-2. The Gateway PEP records a denied policy decision before any call reaches the refund ledger (v1.0; synthetic Meridian fixture). Source: `MF-EVD-AU-001`, `MF-EVD-DN-001`.*

*Figure legend:* Agent = `MF-AGT-RET-004`; Refund service = `MF-SVC-REF-002`; Gateway PEP = `MF-SVC-PEP-001`; Refund ledger = `MF-SYS-LEDGER-001`. The policy evaluator represents a logical PDP responsibility, not a separately registered Meridian service.

*Alt text:* The refund service proposes a mutation, but the Gateway enforcement point receives a denial from the policy evaluator and records the decision. No execution token or external ledger request is issued.

### Threat coverage

The Gateway protects the service-to-action boundary. OWASP's **Top 10 for Agentic Applications (2026)** identifies **ASI02: Tool Misuse and Exploitation** and **ASI03: Identity and Privilege Abuse** as relevant risks. The proposed `refund.issue` without execution authority illustrates why tool intent and delegated privilege must be checked independently. These are threat mappings, not claims that Meridian suffered an attack. [OWASP Agentic Top 10, 2026 edition](https://genai.owasp.org/top-10-for-agentic-applications-2026/).

The chain crosses five relevant interfaces: originator to agent, agent to service, service to PEP, PEP to external target, and PEP to evidence store. Identity owns the delegation claims. Gateway evaluates action admission and enforces the result. Observability preserves the corresponding trajectory evidence.

**ASI01: Agent Goal Hijack** and **ASI06: Memory & Context Poisoning** remain relevant upstream threats. The Gateway cannot repair poisoned records or agent goals. Context preserves unresolved evidence; Verification tests the agent's response. The Gateway's contribution is to prevent a prohibited side effect even when a request reaches its boundary.

### Failure modes

*Table 16-3. Failure modes, observable symptoms, and required controls.*

| Failure | Cause | Observable symptom | Required control |
|---|---|---|---|
| Privilege expansion | Requested scope exceeds delegated grant | `required_scope=FAIL` | Deny at PEP and retain actor-chain reference. |
| Direct bypass | Service can reach external target without mediation | Mutation traffic lacks PEP decision | Restrict egress and test the forbidden route. |
| Stale policy | PEP uses an obsolete policy version | Receipt version differs from approved bundle | Version validation and controlled policy distribution. |
| PEP unavailable | Admission service or policy evaluator fails | No trustworthy decision returned | Fail closed for mutable actions; define recovery separately. |
| Replayed permission | An old approval is presented again | Duplicate attempt or stale binding | Validate audience, expiry, action binding, and applicable reuse constraints. |
| Duplicate retry | A timed-out request is submitted twice | Repeated mutation attempts | Carry an idempotency key through admission and execution. |
| Unresolved context | Eligibility records contradict each other | `context_conflict_precondition=FAIL` | Block mutation and escalate reconciliation. |

The controls add latency, dependencies, and recovery obligations. They also prevent a failure in the agent's planning from becoming an irreversible external operation. Removing the Gateway check may improve the measured response time while transferring risk to the ledger and its operators.

### Enforcement point

At Meridian, `MF-SVC-PEP-001` is the named enforcement point for the permitted action route. It must deny before the Tooling Structural Layer invokes `MF-TOOL-REF-001` against `MF-SYS-LEDGER-001`. The recorded `MF-EVT-012` outcome is **DENIED**, not a rollback after execution.

That alone does not prove non-bypassability. A service with direct credentials and network access could call the ledger without using the approved route. D-18 therefore requires independent controls over credentials, routing, and egress, plus a negative test. Target-side identity restrictions provide another enforcement boundary where supported. The design covers all applicable mutation routes, including alternate integrations and maintenance paths. A credential inventory and a route inventory define the scope of the negative tests.

`MF-EVT-013` records a controlled, synthetic direct-route attempt from `MF-SVC-REF-002` to `MF-SYS-LEDGER-001`. Network egress returned `DENIED_BY_NETWORK_EGRESS`; `target_received_request=false`. The result records the intended negative outcome for this simulated route, not proof of a deployed firewall, real payment processor, or every possible bypass.

[Place Figure 16-3 here: Direct-route negative bypass test.]

*Figure 16-3. The synthetic direct service-to-ledger bypass test is blocked at network egress (v1.0; not production control evidence). Source: `MF-EVT-013`, `MF-EVD-DN-001`.*

*Figure legend:* Refund service = `MF-SVC-REF-002`; Gateway PEP = `MF-SVC-PEP-001`; Refund ledger = `MF-SYS-LEDGER-001`; direct-route result = `DENIED_BY_NETWORK_EGRESS`. There is deliberately no connection into the ledger: the simulated direct-route attempt stops at the blocking boundary.

*Alt text:* The refund service has an approved architectural route through the Gateway enforcement point and a separately tested direct network route. The direct route terminates at the blocking egress boundary; the external refund ledger receives no request.

Non-bypassability requires renewed evidence after routing, credential, or deployment changes. Target-side observations should corroborate the negative tests. D-18 trades enforceable admission for mediation dependencies and outage planning; recovery must restore enforcement rather than open an unreviewed direct path.

### Anti-patterns

#### Gateway drawn, not enforced

**What it looks like.** Every architecture arrow passes through the Gateway, but service credentials still reach the ledger directly.  
**Why it happens.** Teams treat the documented route as proof of exclusivity.  
**Why it fails.** An unmediated call avoids policy admission.  
**The correct pattern.** Apply mandatory PEP checks and independent egress enforcement as defined in D-18 and Chapter 12.  
**Detection signal.** A direct-route negative test reaches the target or produces an external mutation.

#### Shared execution credential

**What it looks like.** Agents with different delegated scopes share a credential that can issue refunds.  
**Why it happens.** A single integration credential simplifies initial onboarding.  
**Why it fails.** Effective privilege exceeds the actor's delegated rights.  
**The correct pattern.** Bind identity, audience, scope, and permitted action as described in Chapter 15 and D-20.  
**Detection signal.** The tool accepts `refund:execute` without a matching actor-chain permission.

#### Decision receipt as execution permission

**What it looks like.** An application interprets any authorisation receipt as evidence that the action was approved.  
**Why it happens.** Decision logging and execution authorisation are collapsed into one field.  
**Why it fails.** A receipt containing `DENY` can be mistaken for a permit.  
**The correct pattern.** Require an explicit permit, valid scoped execution authority, and bound action attributes under D-10.  
**Detection signal.** A denied receipt produces an execution token or target call.

### Evidence artefact

`MF-EVD-AU-001` records the policy decision. `MF-EVD-DN-001` records the enforcement outcome and links the separate bypass test. The distinction is operationally important: a PDP decision does not independently prove that a PEP stopped the side effect.

*Table 16-4. Linked decision and enforcement receipt fields (synthetic fixture).*

| Evidence field | Recorded value |
|---|---|
| Request / action | `MF-REQ-REF-001` / `MF-ACT-REF-001` |
| Correlation | `MF-TRACE-000001` |
| Attempt / idempotency | `MF-PEP-ATT-001` / `MF-IDEMP-REF-001` |
| Delegation | `MF-EVD-DG-001` |
| Policy | `MF-POL-ACTION-v1.0` |
| policy_evaluation.decision | `DENY` |
| policy_evaluation.primary_reason | `SCOPE_EXCEEDS_DELEGATION` |
| policy_evaluation.required_scope | `FAIL` |
| policy_evaluation.context_conflict_precondition | `FAIL` |
| policy_evaluation.human_execution_approval | `ABSENT` |
| authorised_execution_token | `null` |
| signed_authorisation_status | `NOT_ISSUED_DENIED` |
| reason_code | `SCOPE_EXCEEDS_DELEGATION` |
| enforcement_point | `MF-SVC-PEP-001` |
| external_tool_called | `false` |
| financial_mutation_count | `0` |
| negative_bypass_test.result | `DENIED_BY_NETWORK_EGRESS` |
| negative_bypass_test.target_received_request | `false` |
| negative_bypass_test.proof_type | `SIMULATED_CONTROLLED_NEGATIVE_TEST` |

Both receipts belong to `MF-FIX-001`, case `MF-CASE-REFUND-001`, tenant `MF-TEN-RET-001`, and trajectory `MF-TRJ-001`. An investigator follows delegation_id to the original scope grants, reconciliation_id in the authorisation receipt to the disputed claims, and authorisation_receipt_id in the denial receipt back to the policy decision. The bypass record identifies a separate test. Neither receipt independently establishes production enforcement; invocation telemetry and target-side evidence must corroborate the no-effect claim. See Chapter 57 for the full specimen.

The operational response is to retain the denial, expose it to the responsible support and security processes, and escalate the unresolved eligibility record. These are different obligations: denial protects the financial boundary, while reconciliation addresses the underlying business-data conflict.

A later candidate, `MF-REL-RET-0.2.0-rc1`, exposed a separate defect. On **15 March 2027**, `MF-EVT-014` recorded a failed behavioural assertion because the candidate selected `refund.issue` despite unresolved context. `MF-EVT-015` blocked promotion. The Gateway denied the simulated mutation, but the candidate failed `MF-ASSERT-CTX-001`, which expects abstention and escalation. A stopped action is not a correct action selection. Report `MF-EVD-RG-001` records `assertion.assertion_result=FAIL`, `gate_verdict=BLOCK_PROMOTION`, and `production_deployment=false`. No retest outcome appears in the fixture. Chapter 18 develops that release-gate distinction.

### Decisions to make

- **D-10 — Authorise mutable tool actions:** determine the mandatory authorisation contract before an external mutation.
- **D-18 — Prove Gateway non-bypassability:** determine which independent controls and tests prevent unmediated actions.
D-20 remains the Identity-owned dependency for the actor and scope evidence.

### Defaults

- **D-10:** Default to Gateway-enforced action authorisation with a signed, scoped receipt and idempotency key before every external mutation.
- **D-18:** Default to mandatory PEP checks on mutable external actions, enforced by credentials, routing policy and egress controls.
**D-20 dependency:** Default to signed, audience-bound, expiring delegation with monotonically narrowing permissions at each hop. The Meridian example does not claim production signature verification.

D-10 permits an approved reduced path for read-only calls, separately authorised bounded batches, and recorded break-glass review. D-18 permits an isolated offline worker or an explicitly approved trusted path with equivalent PEP controls. Neither exception creates an unreviewed route for refund mutations.

### Artefacts to produce

- `action-authorisation-contract.json` — D-10's required decision and execution binding.
- `gateway-bypass-proof.md` — D-18's negative-route evidence and limits.
- `delegation-chain-proof.json` — D-20's Identity-owned prerequisite.
- `MF-EVD-AU-001` and `MF-EVD-DN-001` — the case's linked decision and denial receipts.

### See also

- **Chapter 12 — Tooling:** tool contracts, permitted invocation and side-effect handling.
- **Chapter 15 — Identity Control Plane:** actor chains, delegation and scope attenuation.
- **Chapter 18 — Verification Control Plane:** behavioural assertions and release decisions.
- **Chapter 19 — Governance Control Plane:** policy authority, ownership and review.
- **Chapter 57 — Worked Evidence and Delivery Artefacts:** complete Meridian evidence specimens.

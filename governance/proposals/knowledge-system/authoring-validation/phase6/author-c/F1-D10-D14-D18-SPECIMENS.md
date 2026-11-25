# Author C — F1 decision-page consistency specimens

**Assignment:** D-10, D-14, D-18 only. **Source boundary:** frozen catalogue and existing F1 template; Meridian v1.0 primary records. No Chapter 13 or Chapter 16 author outputs used. **Authority:** source-exact candidate excerpt, not an approved new F1 production page.

### D-10: Authorise mutable tool actions

**Context.** A generated tool intent is not permission to change an external system.

**Default.** Default to Gateway-enforced action authorisation with a signed, scoped receipt and idempotency key before every external mutation.

**Why.** The PEP checks tenant, actor chain, resource scope, risk and approval. Tooling may execute only after successful validation and must log the resulting side effect.

**Trade-off.** This buys defensible action boundaries at the cost of policy-check latency.

**When to deviate.** A read-only call has an approved reduced policy path; Bulk action uses a separately authorised bounded batch; Emergency operations require recorded break-glass review

**Reversibility.** Two-way door

**Artefact.** `action-authorisation-contract.json`.

**See also.** Existing catalogue chapter map: 12; 15; 16; 27; 48.

**Teaching/fixture boundary (non-normative assessor note).** `MF-EVD-DG-001`, `MF-EVD-AU-001`, `MF-EVD-DN-001`, `MF-ACT-REF-001`. A `DENY` is not a signed action permit. In this synthetic case effective scope remained `refund:request`, no refund:execute permit was issued and no external mutation occurred.

### D-14: Reconcile semantic identities

**Context.** Different sources may name the same entity or disagree on its status.

**Default.** Default to canonical IDs with source lineage and explicit unresolved-conflict states; never silently choose the newest record as truth.

**Why.** Context owns the entity match and conflict record. The domain data owner defines precedence, while Verification tests that a blocked conflict does not lead to a side effect.

**Trade-off.** This buys consistent meaning at the cost of stewardship and escalations.

**When to deviate.** Authoritative source has published precedence rules; A disposable unlinked context item needs no canonical entity

**Reversibility.** Two-way door

**Artefact.** `semantic-reconciliation-record.json`.

**See also.** Existing catalogue chapter map: 13; 18; 22; 28.

**Teaching/fixture boundary (non-normative assessor note).** `MF-REC-A-001`, `MF-REC-B-001`, `MF-EVD-RC-001`, `MF-EVT-007`–`008`. Conflict remains `UNRESOLVED`; the retail steward was escalated but no canonical business truth was selected or durable verified eligibility written.

### D-18: Prove Gateway non-bypassability

**Context.** A gateway control plane is ineffective if tools can call external targets directly.

**Default.** Default to mandatory PEP checks on mutable external actions, enforced by credentials, routing policy and egress controls.

**Why.** Architecture diagrams are insufficient proof. A denial and direct-bypass negative test must show that unapproved side effects cannot succeed.

**Trade-off.** This buys enforceable admission at the cost of proxy dependencies and outage planning.

**When to deviate.** Restricted offline worker cannot reach external systems; An explicitly approved trusted path implements equivalent PEP controls

**Reversibility.** One-way door

**Artefact.** `gateway-bypass-proof.md`.

**See also.** Existing catalogue chapter map: 10; 12; 16; 27; 42.

**Teaching/fixture boundary (non-normative assessor note).** `MF-EVT-013`, `MF-EVD-DN-001.negative_bypass_test`. Direct-egress blocked is a synthetic negative test, not exhaustive evidence of deployed network or credential enforcement.


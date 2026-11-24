# Author B — Chapter 16: Gateway Control Plane (F7 authoring outline)

**Trial assignment:** Chapter 16, D-10, D-18. **Input boundary:** frozen Chapter 16 blueprint, catalogue, Style Bible, Meridian v1.0 and frozen TOC. Other contributor drafts excluded. **Status:** independently scoped simulation; not a finished F7 manuscript.

## Unique reader outcome
Explain how proposed mutable intent becomes a Gateway admission decision and enforced side-effect boundary, why a DENY receipt cannot confer execution authority, and why a Gateway PEP check and a direct-egress bypass negative test are distinct. Identify accountable upstream and downstream owners; separate synthetic evidence from deployment proof.

## Required F7 structure and section specification

### Opening hook (unheaded; ~95 words)
Week 9: an action originally described as read/prepare is translated into a proposed `POST /refunds` for GBP 125.00. The applicant's effective scope does not permit the mutation. Gateway denies; a separate direct route is denied by simulated network egress. Both outcomes must be independently evidenced rather than inferred from diagrams. Name `MF-EVD-AU-001` and `MF-EVD-DN-001`.

### What this layer decides (~35 words)
Gateway coordinates policy evaluation and mandatory runtime admission for external mutations. It does not create identity, select business facts, execute target transactions, or approve a release.

### The mechanism (~940 words)
1. **16.1 Propose is not permit.** `MF-REQ-REF-001` is a read/prepare request; `MF-ACT-REF-001` is an attempted mutation. The agent's emitted intent has no independent authority.
2. **16.2 Delegation to effective scope.** Use `MF-EVD-DG-001`: Human→Agent→Service→Tool chain; effective `refund:request` remains bounded. D-20 is a related Identity control, not redefined here. Fixture signature status must not be promoted to a production signed delegation.
3. **16.3 Policy ownership, PDP and PEP.** Governance defines/risk-approves policy, Identity establishes chain, Gateway evaluates proposed action and enforces at `MF-SVC-PEP-001`. Data Protection/classification and Context's `UNRESOLVED` state are inputs; neither is an execution permit. Tooling is the mediated caller only after positive authorisation. Do not invent a physically distinct PDP service.
4. **16.4 Denial path.** `MF-EVD-AU-001` decision `DENY`; `required_scope=FAIL` is central; conflict and human execution approval are additional failed/missing preconditions. No signed execution token is emitted. `MF-EVD-DN-001` records no external tool call and zero financial mutations. **Figure 16-1** actor/delegation/PEP trust chain; **Figure 16-2** decision inputs and denied side-effect.
5. **16.5 Separate bypass path.** `MF-EVT-013` shows a simulated direct service→ledger request blocked by egress controls. That is not the same as the PEP evaluation nor evidence that every deployment path is non-bypassable. **Figure 16-3** alternate-route denial.
6. **16.6 Release separation.** `MF-EVD-RG-001` later failed behavioural release assertion: verification/release failure is separate from the original Week 9 denial. Do not suggest later promotion went to production.

### Threat coverage (~190 words)
Discuss illegitimate mutable tool calls, confused deputy, token replay, bypass and overbroad credentials. Verify any standards references and edition before claiming a crosswalk. Report both preventative controls and untested attack surfaces; design requirement ≠ observed proof.

### Failure modes (~220 words)
Table: scope mismatch, missing business approval, Context unresolved, policy unavailable, PEP fail-open, replay/idempotency duplication, direct egress, wrong target. Include primary evidence, secondary conditions, fail-closed expectation and accountable control owner.

### Enforcement point (~245 words)
The PEP at `MF-SVC-PEP-001` rejects mutation lacking appropriate scope/approval, while credential and network policy block alternative calls to the target. Distinguish middleware policy logic from tested routing and target enforcement. D-18's normative requirement is broader than this synthetic example.

### Anti-patterns (~180 words)
F4 cards: policy diagram treated as enforcement, shared unrestricted tool credential, DENY receipt treated as signed permission. For each specify exploit path, detection, correction and whether Meridian actually exercises it.

### Evidence artefact (~265 words)
Compact field-mapped excerpt from `MF-EVD-DG-001`, `MF-EVD-AU-001`, `MF-EVD-DN-001` and `MF-EVT-013`. Distinguish authorisation decision receipt, denial proof, signed allowed-action receipt (not issued here), attempted bypass and tool target acknowledgment (no request received). Preserve correlation identifiers and event ordering.

### Decisions to make (~55 words)
D-10 Authorise mutable tool actions; D-18 Prove Gateway non-bypassability. D-20 signed delegation is a dependency owned by the Identity explanation, not a third Chapter 16 decision default.

### Defaults (~65 words)
Quote D-10 and D-18 defaults **verbatim** from the catalogue. Do not say the denied fixture issued a signed authorisation token or executed a mutation.

### Artefacts to produce (~55 words)
`action-authorisation-contract.json`, `gateway-bypass-proof.md`, decision/denial receipt example, and negative-test result; only the existing fixture records count as observed synthetic artefacts.

### See also (~35 words)
Chapter 12 for Tooling contract, Chapter 13 for unresolved source quality, Chapter 15 for Identity, Chapter 18 for Verification and Chapter 57 for specimen; lifecycle authorisation and incident/playbook use are cross-references, not authority transfers.

## Evidence usage plan
| Claim | Frozen evidence | Interpretation boundary | Prohibited overclaim |
|---|---|---|---|
| Effective scope insufficient | `MF-EVD-DG-001` | Scope intersection yields request only | `refund:execute` granted |
| Normal mutable action DENY | `MF-EVD-AU-001`, `MF-EVD-DN-001`, `MF-EVT-009`–`012` | No signed allow token, no external call | Refund posted or signed permission observed |
| Context conflict is policy input | `MF-EVD-RC-001` | Data disagreement remains unresolved | Gateway chose source truth |
| Direct bypass blocked | `MF-EVT-013`, `MF-EVD-DN-001.negative_bypass_test` | Synthetic egress negative test | All production bypass routes proven blocked |
| Later release failed | `MF-EVD-RG-001` | Verification gate independently failed | Original denial reversed or release promoted |

## Lifecycle / playbook application
Apply the authorisation control during the trust-chain stage, tenant integration and first-use-case acceptance; revisit in incident handling and release requalification. Link D-10 and D-18's existing catalogue and crosswalk chapters; do not copy the playbook's operational instructions into Chapter 16. All stage references are teaching crosswalks, not claims of Meridian stage-execution completeness.

## Author B self-check before comparison
Gateway enforces a proposed action; Governance owns policy; Identity owns effective authority; Context supplies unresolved state; Tooling calls only with positive permission; Verification controls release readiness. Synthetic receipts are not production certificates.

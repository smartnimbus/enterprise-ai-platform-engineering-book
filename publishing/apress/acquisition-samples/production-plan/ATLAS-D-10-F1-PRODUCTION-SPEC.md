# D-10 — Authorise mutable tool actions: acquisition F1 page production specification

**Editorial status:** page build instruction; not a finished F1 print proof. **Authority:** frozen Decision Atlas catalogue entry `D-10`. **Placement:** Chapter 23, Part IV. **Related chapters:** Ch 12, 15, 16, 27, 48. **Target:** one publisher-typeset page per decision, subject to layout proof. Do not add a new decision or reword the default.

## Exact frozen Default (paste verbatim)

> Default to Gateway-enforced action authorisation with a signed, scoped receipt and idempotency key before every external mutation.

## Full F1 content source — keep the canonical meaning

**Context.** A generated tool intent is not permission to change an external system.

**Why.** The PEP checks tenant, actor chain, resource scope, risk and approval. Tooling may execute only after successful validation and must log the resulting side effect.

**Trade-off.** This buys defensible action boundaries at the cost of policy-check latency.

**When to deviate.** A read-only call has an approved reduced policy path; Bulk action uses a separately authorised bounded batch; Emergency operations require recorded break-glass review. Render as separate conditions in the final one-page layout; these are exceptions, not overriding defaults.

**Reversibility.** Two-way door.

**Artefact.** `action-authorisation-contract.json`.

## Required evidence / reproducible reader deliverable

- Primary decision record: `action-authorisation-contract.json` with option selected, owner, approver, verification criterion, evidence pointer and conditions for re-evaluation.
- Reader-facing worked illustration: Meridian MF-EVD-DG-001 → MF-EVD-AU-001 DENY → MF-EVD-DN-001; authorised refund:request, not refund:execute; no external call or mutation.
- Layout or illustration: Four-step request → authority → PEP DENY → zero side effects strip; excerpt exact receipt fields.
- Citation discipline: exact Atlas source is normative; Mermaid/Meridian evidence is synthetic; any cost or adoption statistics must carry separate, dated references.
- Sample artefact must show required fields and the limits of what the worked illustration proves. Do not manufacture a signed token, approved payout, source-precedence rule, production egress test, paid unit-cost outcome or completed retirement.

## Final F1 page structure and production test

1. Exact heading `D-10: Authorise mutable tool actions`.
2. **Context.** Canonical problem in a short paragraph.
3. **Default.** The source-exact frozen sentence above.
4. **Why.** Two to four sentences grounded in the source rationale.
5. **Trade-off.** The one-sentence source trade-off.
6. **When to deviate.** Source conditions in concise bullets.
7. **Reversibility.** `Two-way door`; no change to one-way/two-way classification.
8. **Artefact.** `action-authorisation-contract.json` and captioned illustrative snippet or tiny diagram if layout permits.

**Acceptance:** Source-exact default/title/reversibility/artefact; no assertion beyond the available source; one-page PDF proof with readable type, caption and accessible figure alt text; reviewer can explain the decision from the page alone. Atlas custodian checks source matching; technical reviewer checks mechanism and illustration; editor checks one-page clarity.

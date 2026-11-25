# Editorial and publication review — D-10 and D-18

## Completeness
Both pages contain all eight required F1 fields, retain the frozen decision identifiers and choices, and include source-checked Meridian evidence within the **Why** field. The examples distinguish a policy denial from enforcement and distinguish the simulated bypass test from real deployed proof.

## Usability
D-10 guides an architect to require authorisation before mutation; D-18 guides them to test whether approved control paths can be bypassed. Their exception criteria and artefact names allow immediate use in an architecture review. Readers must still adapt these decisions to their organisation's policy and implementation.

## Independence
Both can be read without Chapter 16 because Context identifies the problem, Default states the answer, Why includes the Meridian observation, and Trade-off/When to deviate identify limits. Chapter links are supporting references rather than prerequisites.

## Enterprise applicability
D-10 applies to external mutations, subject to the frozen reduced-read, bounded-batch and emergency deviations. D-18 applies to mutable routes that might bypass the policy enforcement point, with the frozen offline/equivalent-control deviations. Neither page asserts that all enterprise technologies already implement these controls.

## Publication readiness
- **Apress sample package:** Suitable as substantive samples, pending a final typeset proof with the prescribed fonts, editorial sign-off and independent technical review.
- **Proposal appendix:** Suitable now as clearly labelled production drafts. Include both with Chapter 16, and retain the synthetic-data disclosure.
- **Chapter 23:** Content-ready under F1; final-ready only after house layout and cross-reference checks.

## Residual weaknesses and fixes
1. **The evidence is simulated.** The pages correctly qualify this. For a production-backed claim, add independent implementation results elsewhere without changing the frozen records.
2. **The signed authorisation default is not exercised on the denied path.** This is not a defect in the fixture. The pages must not claim a signed execution token was issued. An approved-action example elsewhere may demonstrate that separate aspect.
3. **Technical shorthand:** A first-time reader may not know PEP. Expand in surrounding proposal copy, or introduce "policy enforcement point (PEP)" inside the Why field if the final copyedit permits it without altering the frozen intent.
4. **Proof geometry and font:** The preview is on A4 with substitute fonts because the prescribed Source family was unavailable. Verify page count, greyscale, typography and trim after production fonts are supplied.
5. **D-18 one-way door:** Reviewers may dispute how a design decision about non-bypassability is classified. The classification is frozen; do not change it without explicit editorial governance approval.

## Technical checks
- `MF-EVD-AU-001` is a denial receipt at the policy-decision layer; it has `authorised_execution_token: null`.
- `MF-EVD-DN-001` records `external_tool_called: false`, `financial_mutation_count: 0`, and a blocked negative route.
- `MF-EVT-013` is a simulated direct-route negative test, not a real attack or observed firewall test.
- All references are taken from frozen Meridian Evidence Fixture v1.0; no records were changed.

## Verdict
Strong draft sample pages for an Apress proposal. Not yet final press proofs until production-font/typesetting and independent reviewer gates pass.

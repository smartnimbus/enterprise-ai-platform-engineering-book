# Independent validation pack

This pack implements the **test protocol**, not the controls or the independent participant tests.

## Distribution split

- **Participant-visible:** approved repository + approved Programme Operating System + approved handover; for assigned case, a case brief taken from the master protocol *without* assessor-key sections. Include only permitted fixture source JSON and frozen decisions.
- **Assessor restricted:** `ASSESSOR-KEY-RESTRICTED.md`, scored rubrics, raw unredacted answers, protocol pre-registration and participant consent information. Do **not** publish these alongside live participant assignments.
- **Public results:** aggregate redacted results after approvals, with failures, confidence limits and explicit `NOT_RUN/BLOCKED` entries.

## Source integrity

Meridian test cases refer to existing fixture v1.0 and must never rewrite its data. Every execution records protocol hash, fixture checksum and Git SHA.

## Running

1. Establish approved baseline and recruited independent reviewers.
2. Copy the run template for each assigned case.
3. Log raw response, times, mistakes, access and assistance.
4. Score from pre-registered rubric; adjudicate without overwriting original.
5. Issue scope-specific GO/CONDITIONAL GO/NO GO/INSUFFICIENT EVIDENCE.

## Package files

- `INDEPENDENT-VALIDATION-PROGRAMME-v1.0.md` — exact 10-part protocol and criteria.
- `SCENARIO-CATALOGUE.csv` — 12 cases with roles, inputs, timeboxes and expected limits.
- `SCORING-RUBRIC.csv` — explicitly weighted dimensions.
- `VALIDATION-RUN-TEMPLATE.json` — unexecuted evidence record.
- `ASSESSOR-KEY-RESTRICTED.md` — case key, controlled distribution.
- `validate_pack.py` — structural consistency validator; *not a substitute for participants*.

# Programme Operating System — Proposed Execution Package

**Status:** governance proposal on an existing review branch. This package does not replace the approved `REPOSITORY-GOVERNANCE.md`; it neither changes frozen architecture nor claims implementation of branch protection, publishing or independent review.

## Files

- `PROGRAMME-OPERATING-SYSTEM-v1.0.md`: ten-part operational contract covering lifecycle, intake/WIP, review, stewardship, AI, change, quality, retirement and minimal metrics.
- `WORK-ITEM-CONTRACT-v1.schema.json`: proposed structural JSON schema for a task recovery snapshot, not a second issue tracker.
- `WORKFLOW-TRANSITIONS-v1.json`: allowed normal phase transitions, no implicit human approval.
- `WORK-ITEM-EXAMPLE-DRAFT.json`: **fictional** non-publishable draft illustrating valid structure, not a real GitHub Issue.
- `validate_work_item.py`: Python stdlib-only structural validator; checks shape, holds, promotion prerequisites and optional transitions.
- `test_work_item.py`: small positive/negative unit tests, not platform or security assurance.
- `VALIDATION-REPORT.json`: reproducible test snapshot and explicit limitations.

## Review-branch scope

The full source and test harness are contained in the attached ZIP. The GitHub review branch initially contains the operating contract and README; until all harness files are uploaded and the actual repository baseline is ratified, do **not** treat the test commands below as available from a clean checkout of that branch. The commands work after extracting the ZIP to the proposed path.

## Run from a clean checkout or extracted package

```sh
python3 governance/proposals/knowledge-system/programme-os/test_work_item.py
python3 governance/proposals/knowledge-system/programme-os/validate_work_item.py governance/proposals/knowledge-system/programme-os/WORK-ITEM-EXAMPLE-DRAFT.json
python3 governance/proposals/knowledge-system/programme-os/validate_work_item.py --from-phase CANDIDATE governance/proposals/knowledge-system/programme-os/WORK-ITEM-EXAMPLE-DRAFT.json
```

The optional `candidate_id` and GitHub example issue link are illustrative. New items may have no `candidate_id`; their real GitHub issue number is the work identity. No source/right/reviewer validation can be inferred from these commands. Human reviewers must verify actual commits, authority and rights. Schema is documentation; stdlib validator deliberately implements only an explicitly described subset rather than pretending to be a complete JSON Schema engine.

## Deployment rule

Do not create new live issues or automation yet. First complete existing EX-001–EX-006 and obtain explicit approval to adopt this contract; then exercise one vertical slice and verify rollback/retirement behaviour.
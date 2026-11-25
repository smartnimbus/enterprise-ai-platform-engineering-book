# Multi-AI Contributor Contract — Proposal, Not Adopted Policy

- [Operating contract](MULTI-AI-CONTRIBUTOR-OPERATING-CONTRACT-v1.0.md): ten parts, grounded in existing programme governance, and not a replacement authority.
- `validate_ai_change.py`: offline demonstration of path checks, frozen-path denials and active claim collisions, **not** a GitHub permission, identity, PR-review or approval enforcement system.
- `assignment-example.json`: fictional task claim, not an actually active agent registration.
- `test_ai_change.py`: unit tests for bounded path and claim inputs.

## Local check

```bash
python test_ai_change.py
printf 'automation/tests/test.py\n' > changed-files.txt
python validate_ai_change.py assignment-example.json changed-files.txt
```

For actual integration, CI must generate `changed-files.txt` from a protected, exact-base Git diff; fetch active work claims from the already authoritative work-item system; compare frozen-source hashes against the ratified manifest; and require independently reviewed GitHub protection rules. Path globs are advisory in this local tool and cannot grant or revoke GitHub permissions. The validator alone is insufficient for production or multi-user security.

**Status:** proposed, pending independent review and controlled EX-001–EX-006 implementation. Frozen architecture, Atlas and fixture were not modified.

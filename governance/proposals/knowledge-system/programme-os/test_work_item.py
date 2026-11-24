#!/usr/bin/env python3
"""Negative and positive control tests for proposed work-item validator."""
from pathlib import Path
import json
from validate_work_item import validate, validate_transition

base=Path(__file__).resolve().parent
clean=json.loads((base/'WORK-ITEM-EXAMPLE-DRAFT.json').read_text())
assert validate(clean)==[], validate(clean)

v=dict(clean,phase='APPROVED',rights_status='PENDING')
assert 'Promotion without rights clearance' in validate(v)
assert 'Promotion without actual reviewer identity' in validate(v)
assert 'Promotion without reviewed commit' in validate(v)

v=dict(clean,baseline_sha='not-a-sha')
assert 'Invalid baseline_sha' in validate(v)

v=dict(clean,hold_flags=['BLOCKED'],blocked_reason=None)
assert 'Blocked item requires reason' in validate(v)

v=dict(clean,phase='RETIRED')
assert 'Retirement requires record of disposition' in validate(v)

v=dict(clean,authority_tier='T9')
assert 'Invalid authority_tier' in validate(v)

v=dict(clean,candidate_id='D-10')
assert 'Invalid candidate_id' in validate(v)

v=dict(clean,source_refs=['a','a'])
assert 'Invalid list source_refs' in validate(v)

assert validate_transition('DRAFT','IN_REVIEW') == []
assert validate_transition('DRAFT','PUBLISHED')
assert validate_transition('RETIRED','PUBLISHED')
print('PASS: 11 structural/transition positive/negative checks (no external approval validation)')

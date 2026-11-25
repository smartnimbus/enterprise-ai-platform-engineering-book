#!/usr/bin/env python3
"""Check the independent validation document's internal structure only."""
from pathlib import Path
import csv,json,hashlib,re,sys
D=Path(__file__).parent
rows=list(csv.DictReader((D/'SCENARIO-CATALOGUE.csv').open()))
rub=list(csv.DictReader((D/'SCORING-RUBRIC.csv').open()))
run=json.load((D/'VALIDATION-RUN-TEMPLATE.json').open())
book=(D/'INDEPENDENT-VALIDATION-PROGRAMME-v1.0.md').read_text()
assert len(rows)==12, len(rows)
ids=[x['test_id'] for x in rows]
assert ids==[f'IV-{i:02d}' for i in range(1,13)],ids
assert len(ids)==len(set(ids))
assert all(r['test_id'] in ids for r in rub)
for id in sorted(set(r['test_id'] for r in rub)):
 assert sum(int(r['max_points']) for r in rub if r['test_id']==id)==10,id
for i in ids: assert i in book,i
for h in [f'## Part {i}' for i in range(1,11)]: assert h in book,h
for name in ['MF-EVD-CM-001','MF-EVD-RC-001','MF-EVD-DG-001','MF-EVD-AU-001','MF-EVD-DN-001','MF-EVD-RG-001','MF-EVT-013','MF-REQ-REF-001','MF-ACT-REF-001']:
 assert name in book,name
assert run['assessor_verdict']=='INSUFFICIENT_EVIDENCE'
assert run['test_eligibility']=='BLOCKED'
assert 'not an actual run' in run['notes']
print('PASS: 12 unique scenarios, 10 sections, weighted rubric totals, fixture IDs and blocked run template')
print('SHA256 protocol',hashlib.sha256((D/'INDEPENDENT-VALIDATION-PROGRAMME-v1.0.md').read_bytes()).hexdigest())

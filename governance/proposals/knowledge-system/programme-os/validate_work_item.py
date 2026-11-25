#!/usr/bin/env python3
"""Offline structural work-item validation. Does not check actual GitHub approval or evidence truth."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from datetime import datetime

BASE=Path(__file__).resolve().parent
ALLOWED = {
 'phase': ['IDEA','CANDIDATE','DRAFT','IN_REVIEW','APPROVED','PUBLISHED','MAINTAINED','DEPRECATED','RETIRED','REJECTED'],
 'artifact_state':['IMPORTED_UNVERIFIED','DRAFT','IN_REVIEW','APPROVED','FROZEN','SUBMITTED','PUBLISHED','SUPERSEDED','RETIRED'],
 'type':['research-topic','knowledge-article','engineering-pattern','decision-guide','learning-asset','reference-implementation','book-chapter'],
 'authority_tier':['T1','T2','T3','T4','T5'],
 'priority':['P0','P1','P2','P3'],
 'evidence_grade':['PRIMARY_VERIFIED','SECONDARY_CORROBORATED','INDEPENDENT_TEST','SYNTHETIC_TEST','HISTORICAL_DOCUMENTED','DESIGN_ONLY','INFERRED','UNVERIFIED'],
 'rights_status':['PENDING','CLEARED_PUBLIC','CLEARED_RESTRICTED','BLOCKED','NOT_APPLICABLE'],
}
ALLOWED_FLAGS={'BLOCKED','QUARANTINED','CHALLENGE_OPEN','EVIDENCE_HOLD','STALE_REVIEW_REQUIRED','BLOCKED_REVIEW','AUTHORITY_CONFLICT'}
REQUIRED=['issue_url','type','title','phase','artifact_state','authority_tier','evidence_grade','priority','owner_role','owner_identity','baseline_sha','rights_status','source_refs','acceptance_tests','dependency_ids','last_updated_utc']

def validate(data):
    errors=[]
    if not isinstance(data,dict): return ['Root must be an object']
    schema=json.loads((BASE/'WORK-ITEM-CONTRACT-v1.schema.json').read_text())
    extra=set(data)-set(schema['properties'])
    if extra:errors.append('Unknown fields: '+', '.join(sorted(extra)))
    for x in REQUIRED:
        if x not in data: errors.append('Required field missing: '+x)
    for field, vals in ALLOWED.items():
        if field in data and data[field] not in vals: errors.append('Invalid '+field)
    for name,pat in [('candidate_id',r'^(EX|KA|EP)-\d{3}$'),('baseline_sha',r'^[0-9a-f]{40}$'),('issue_url',r'^https://github\.com/[^/]+/[^/]+/issues/\d+$')]:
        if name in data and data[name] is not None and (not isinstance(data[name],str) or not re.fullmatch(pat,data[name])): errors.append('Invalid '+name)
    for f in ['title','owner_role','owner_identity']:
        if f in data and (not isinstance(data[f],str) or not data[f].strip()): errors.append('Invalid '+f)
    for f in ['source_refs','acceptance_tests','dependency_ids','reviewer_identities','hold_flags']:
        if f in data and (not isinstance(data[f],list) or not all(isinstance(x,str) for x in data[f]) or len(data[f])!=len(set(data[f]))): errors.append('Invalid list '+f)
    for flag in data.get('hold_flags',[]):
        if flag not in ALLOWED_FLAGS:errors.append('Invalid hold flag '+str(flag))
    for f in ['last_updated_utc','next_review_utc','approved_at_utc']:
        if f in data and data[f] is not None:
            try:
                if not isinstance(data[f],str) or not data[f].endswith(('Z','+00:00')): raise ValueError('expected UTC')
                datetime.fromisoformat(data[f].replace('Z','+00:00'))
            except (ValueError,TypeError):errors.append('Invalid UTC date '+f)
    if data.get('phase') in ['APPROVED','PUBLISHED','MAINTAINED']:
        if data.get('rights_status') not in ['CLEARED_PUBLIC','CLEARED_RESTRICTED','NOT_APPLICABLE']:errors.append('Promotion without rights clearance')
        if not data.get('reviewer_identities'):errors.append('Promotion without actual reviewer identity')
        if not data.get('review_commit_sha'):errors.append('Promotion without reviewed commit')
        if data.get('hold_flags'):errors.append('Promoted work item has hold flags')
    if data.get('phase') in ['PUBLISHED','MAINTAINED'] and not data.get('approved_at_utc'):errors.append('Published work item has no approval timestamp')
    if 'BLOCKED' in data.get('hold_flags',[]) and not data.get('blocked_reason'):errors.append('Blocked item requires reason')
    if data.get('phase')=='RETIRED' and not data.get('changelog_ref'):errors.append('Retirement requires record of disposition')
    # No content-approval inference: claims still require independent human inspection.
    return errors

def validate_transition(old, new):
    """Shape-check an intended workflow change, not an authorisation to perform it."""
    transitions=json.loads((BASE/'WORKFLOW-TRANSITIONS-v1.json').read_text())['transitions']
    if old not in transitions: return [f'Unknown starting phase: {old}']
    if new not in transitions[old]: return [f'Forbidden normal phase transition: {old} -> {new}']
    return []

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files',nargs='+')
    parser.add_argument('--from-phase',dest='from_phase',help='Check a proposed normal workflow transition from this phase')
    args=parser.parse_args()
    fail=False
    for name in args.files:
        try:
            data=json.loads(Path(name).read_text())
            errors=validate(data)
            if args.from_phase and isinstance(data,dict):
                errors += validate_transition(args.from_phase, data.get('phase'))
        except (OSError,ValueError) as e:errors=[str(e)]
        if errors:fail=True
        print(('FAIL' if errors else 'PASS')+': '+name)
        for e in errors:print('  - '+e)
    return 1 if fail else 0
if __name__=='__main__':sys.exit(main())

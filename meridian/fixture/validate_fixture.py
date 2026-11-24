import json,pathlib,datetime,sys
p=pathlib.Path(__file__).resolve().parent
load=lambda f:json.loads((p/f).read_text(encoding='utf-8'))
files=['organization.json','identities.json','original-request.json','context-records.json','event-ledger.json','authoring-registry.json','01-context-manifest.json','02-reconciliation-record.json','03-delegation-record.json','04-authorisation-receipt.json','05-denied-action-receipt.json','06-release-gate-report.json']
x={f:load(f) for f in files}; issues=[]; checks=[]
def ck(name, cond):
 checks.append({'check':name,'status':'PASS' if cond else 'FAIL'});
 if not cond:issues.append(name)
rg=x['authoring-registry.json']; org=x['organization.json']; ids=x['identities.json']; ev=x['event-ledger.json']['events']; request=x['original-request.json']; ctx=x['01-context-manifest.json']; rec=x['02-reconciliation-record.json']; deleg=x['03-delegation-record.json']; auth=x['04-authorisation-receipt.json']; deny=x['05-denied-action-receipt.json']; rel=x['06-release-gate-report.json']
ck('12,000 employees and 3 business units',org['employees_synthetic']==12000 and len(org['business_units'])==3)
ck('profile definitions remain 3',set(org['tenant_profiles'])=={'TP-A','TP-B','TP-C'})
ck('six fixed human cast members present',{'Eleanor Price','Maya Shah','Ruth Mercer','Tomas Reed','Samir Khan','Priya Nair'} <= {h['name'] for h in ids['humans']})
ck('six distinct evidence IDs',len({ctx['id'],rec['id'],deleg['id'],auth['id'],deny['id'],rel['id']})==6)
ck('evidence IDs match registry',set(rg['immutable_keys']['artifact'])=={ctx['id'],rec['id'],deleg['id'],auth['id'],deny['id'],rel['id']})
ck('all artifacts share same case ID',len({o['case_id'] for o in [ctx,rec,deleg,auth,deny,rel]})==1)
ck('all artifacts share same fixture ID',len({o['fixture_id'] for o in [ctx,rec,deleg,auth,deny,rel]})==1)
ck('same tenant throughout action evidence',len({o['tenant_id'] for o in [ctx,rec,deleg,auth]})==1)
ck('same request through action',auth['request_id']==deleg['request_id']==deny['request_id']==request['id'])
ck('same action, attempt and idempotency',auth['action_id']==deny['action_id'] and auth['attempt_id']==deny['attempt_id'] and auth['idempotency_key']==deny['idempotency_key'])
ck('same trace ID for action',auth['correlation_id']==deny['correlation_id'])
ck('the two retail product records conflict',len(x['context-records.json']['records'])==2 and len({r['attributes']['product_status'] for r in x['context-records.json']['records']})==2 and len({r['product_id'] for r in x['context-records.json']['records']})==1)
ck('both records are included and attributed',set(r['id'] for r in x['context-records.json']['records'])==set(r['id'] for r in ctx['retrieved_records']))
ck('insurance result quarantined and not consumed',ctx['quarantined_result']['context_included'] is False and ctx['quarantined_result']['source_acl_check']=='DENY')
ck('conflict unresolved and never resolved by timestamp',rec['status']=='UNRESOLVED' and rec['effective_precedence_rule'].startswith('NONE_DEFINED'))
ck('delegation scopes monotonically attenuate',all(set(b['granted_scopes']) <= set(a['granted_scopes']) for a,b in zip(deleg['hops'],deleg['hops'][1:])))
ck('refund execute not delegated',all('refund:execute' not in h['granted_scopes'] for h in deleg['hops']))
ck('Gateway denies and issues no permission token',auth['policy_evaluation']['decision']=='DENY' and auth['authorised_execution_token'] is None)
ck('zero external side effect',not deny['external_tool_called'] and deny['financial_mutation_count']==0)
ck('direct bypass denied in simulated test',deny['negative_bypass_test']['result']=='DENIED_BY_NETWORK_EGRESS' and deny['negative_bypass_test']['target_received_request'] is False)
ck('critical failed assertion blocks candidate',rel['assertion']['critical'] and rel['assertion']['assertion_result']=='FAIL' and rel['gate_verdict']=='BLOCK_PROMOTION' and rel['production_deployment'] is False)
ck('candidate failure is not an executed refund',rel['assertion']['observed_side_effects']==0)
ck('time-ordered events with unique IDs',len({e['event_id'] for e in ev})==len(ev) and [e['occurred_at'] for e in ev]==sorted(e['occurred_at'] for e in ev))
ck('all original event weeks represented',set({7,8,9,11})==set(((datetime.date.fromisoformat(e['occurred_at'][:10])-datetime.date(2027,1,4)).days//7+1) for e in ev))
ck('decision links frozen',{'D-10','D-11','D-14','D-18','D-20','D-23'}<=set(sum([x['decision_refs'] for x in [ctx,rec,deleg,auth,deny,rel]],[])))
ck('refund review is not payment instruction',request['requested_task']=='review and prepare, not execute')
ck('evidence cross-link integrity',rec['context_manifest_id']==ctx['id'] and auth['delegation_id']==deleg['id'] and auth['reconciliation_id']==rec['id'] and deny['authorisation_receipt_id']==auth['id'] and rel['evidence_refs']==[ctx['id'],rec['id'],deleg['id'],auth['id'],deny['id']])
result={'fixture_version':'1.0.0','status':'PASS' if not issues else 'FAIL','checks':checks,'errors':issues,'source_type':'synthetic_consistency_tests_only; not a software or deployed PEP verification','checked_files':files}
(p/'validation-report.json').write_text(json.dumps(result,indent=2)+'\n')
print(f"{result['status']}: {len(checks)-len(issues)}/{len(checks)} validation checks")
if issues:print('\n'.join(issues));sys.exit(1)

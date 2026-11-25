import csv
from pathlib import Path
p=Path('/mnt/data/phase3_integrity');a=list(csv.DictReader(open(p/'LAYER-CONTROL-CONSISTENCY-12.csv')))
mapping={
'Execution Environment':('Lifecycle','Gateway, Identity, Data Protection','E performs isolated compute; no permission minting','Tenant boundaries; compute and egress resource ceilings'),
'Tooling':('Lifecycle','Gateway, Interoperability, Identity','T uses registered versioned adapters after admission','Tool schema drift and direct external bypass'),
'Context':('Lifecycle','Identity, Data Protection, Governance, Verification','C retrieves, reconciles and carries provenance','Cannot override source ACL or authoritative policy'),
'Lifecycle':('External request','Identity, Gateway, Verification, Observability','L orchestrates; no grants created','Checkpoint-resume must recheck delegation'),
'Identity':('Human/service IAM','Gateway, Governance, Data Protection','Scope attenuation and identity assertions','Not business approval or Gateway PEP'),
'Gateway':('Identity, Governance, Lifecycle','Tooling, Execution Environment, Observability','Mandatory action admission','Do not assume central proxy physically intercepts every context read'),
'Observability':('All layers/planes','Verification, Governance','Logs measurement and correlation','Telemetry ≠ test pass or policy permit'),
'Verification':('Events/test fixtures','Gateway, Governance, Observability','Behavioural and release verdict','Gateway blocked action ≠ agent behaved acceptably'),
'Governance':('Domain risk policy','Identity, Gateway, Verification','Risk acceptance and owner rules','Does not author tool execution or issue tokens'),
'FinOps':('Budgets and ledger','Gateway, Observability, Execution Environment','Financial constraints and chargeback','Does not meter resources or enforce network routes'),
'Data Protection':('Classification/consent','Context, Identity, Gateway','Source access/write/delete constraints','Does not resolve business semantic identity'),
'Interoperability':('Protocol/version registry','Tooling, Gateway, Context','Interface compatibility and event contract','No business entity mastership or proxy runtime ownership')}
for x in a:
 key=x['name'];
 if key in mapping:x['input_from'],x['interacts_with'],x['ownership_test'],x['conflict_boundary']=mapping[key]
 else:print('missing',key)
with open(p/'LAYER-CONTROL-CONSISTENCY-12.csv','w',newline='',encoding='utf8') as f:
 cols=list(a[0]);w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(a)

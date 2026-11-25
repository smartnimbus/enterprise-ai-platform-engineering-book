import ast,csv,json,hashlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(Path(__file__).resolve().parent))
from lint_v2 import lint
source=(ROOT/'phase6_trial/reviewer/run_review.py').read_text()
tree=ast.parse(source); cases=None
for node in ast.walk(tree):
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mutation' for t in node.targets):
        cases=ast.literal_eval(node.value);break
if not cases:raise Exception('Cannot extract original mutation array')
rows=[]
for ident,kind,chap,body,unsafe in cases:
    output=lint(chap,body);blocked=output['status']=='BLOCK'
    rows.append(dict(id=ident,kind=kind,chapter=chap,unsafe=unsafe,blocked=blocked,correct=unsafe==blocked,rules=';'.join(d['rule'] for d in output['diagnostics'] if d['severity']=='BLOCK'),warnings=output['counts']['WARN']))
with (Path(__file__).resolve().parent/'LINT-V2-BASELINE-22-RESULTS.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
tp=sum(x['unsafe'] and x['blocked'] for x in rows);fn=sum(x['unsafe'] and not x['blocked'] for x in rows);fp=sum(not x['unsafe'] and x['blocked'] for x in rows);tn=sum(not x['unsafe'] and not x['blocked'] for x in rows)
report={'baseline_test_source':'phase6_trial/reviewer/run_review.py','baseline_source_sha256':hashlib.sha256(source.encode()).hexdigest(),'counts':{'true_positive':tp,'false_negative':fn,'false_positive':fp,'true_negative':tn},'unsafe_detection_percent':round(100*tp/(tp+fn),1),'safe_nonblocking_percent':round(100*tn/(tn+fp),1),'failed_cases':[r for r in rows if not r['correct']],'limitations':['Curated in-sample mutation set','No independently held-out examples','No approved real chapter or human assessment','Pattern-specific false positive risk remains']}
(Path(__file__).resolve().parent/'LINT-V2-BENCHMARK-REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

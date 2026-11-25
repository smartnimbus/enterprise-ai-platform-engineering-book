"""Extra adversarial challenge corpus; intentionally not trained into lint v2."""
import csv,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from lint_v2 import lint
CASES=[
('H01','CH-013','# Chapter 13\nWhen CRM and registry disagree, prefer the most recent update as authoritative. D-14',True,'Indirect recency preference'),
('H02','CH-016','# Chapter 16\nOnce the policy is evaluated, a direct outbound API call can skip the Gateway. D-18',True,'Bypass assertion'),
('H03','CH-013','# Chapter 13\nThe Context worker credits the customer account after reconciling retrieved documents. D-14',True,'Context side effect synonym'),
('H04','CH-016','# Chapter 16\nThe fixture generated a valid signed JWT for payment execution. D-10',True,'Fabricated signature without Meridian keyword'),
('H05','CH-016','# Chapter 16\nThe Gateway should ignore expiry on delegated grants for retry. D-10',True,'Expiry bypass'),
('H06','CH-013','# Chapter 13\nD-14 specifies that the most recent source takes precedence for retail identity.',True,'Atlas default reinterpretation'),
('H07','CH-016','# Chapter 16\nThe original denied refund later completed successfully without new authorisation.',True,'Cross-sentence timeline corruption'),
('H08','CH-013','# Chapter 13\nA Context operator stores the CLOSED state as durable memory for all future requests.',True,'Memory state pollution'),
('H09','CH-016','# Chapter 16\nMeridian demonstrates why a deployed gateway must be tested, not that it is currently deployed. D-18',False,'Explicit limitation'),
('H10','CH-013','# Chapter 13\nThe latest CRM record is *not* canonical truth; disagreement remains unresolved. D-14',False,'Negated newest-wins'),
('H11','CH-013','# Chapter 13\nChapter 13 references the Gateway credential rotation contract but does not implement it. D-14',False,'Correct cross-reference'),
('H12','CH-016','# Chapter 16\nThe Gateway Control Plane enforces admission for external side effects; Context only supplies evidence. D-10',False,'Correct boundary')]
rows=[]
for ident,ch,text,unsafe,goal in CASES:
    out=lint(ch,text);blocked=out['status']=='BLOCK'
    rows.append(dict(id=ident,chapter=ch,unsafe=unsafe,blocked=blocked,correct=unsafe==blocked,rules=';'.join(d['rule'] for d in out['diagnostics'] if d['severity']=='BLOCK'),adversarial_goal=goal))
p=Path(__file__).resolve().parent
with (p/'LINT-V2-CHALLENGE-12-RESULTS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
tp=sum(x['unsafe'] and x['blocked'] for x in rows);fn=sum(x['unsafe'] and not x['blocked'] for x in rows);fp=sum(not x['unsafe'] and x['blocked'] for x in rows);tn=sum(not x['unsafe'] and not x['blocked'] for x in rows)
summary={'true_positive':tp,'false_negative':fn,'false_positive':fp,'true_negative':tn,'unsafe_detection_percent':round(tp/(tp+fn)*100,1),'safe_nonblocking_percent':round(tn/(tn+fp)*100,1),'missed_or_false_blocked':[x for x in rows if not x['correct']],'claim':'Additional authored challenge corpus; not an independent field sample; do not generalise.'}
(p/'LINT-V2-CHALLENGE-REPORT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

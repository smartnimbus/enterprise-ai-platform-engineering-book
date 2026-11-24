#!/usr/bin/env python3
"""Conservative Phase 5 draft lint. Structural checks only; never approves a chapter.
Usage: python lint_manuscript.py CH-013 chapter.md [--json OUTPUT]
"""
from __future__ import annotations
import argparse,csv,json,re,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
ALLOW_D={f'D-{i:02}' for i in range(1,31)}
ALLOW_CH={f'CH-{i:03}' for i in range(1,59)}
MERIDIAN_KNOWN={'MF-EVD-RC-001','MF-EVD-CM-001','MF-EVD-AU-001','MF-EVD-DN-001','MF-EVD-DG-001','MF-ACT-REF-001','MF-REQ-REF-001','MF-EVT-013'}

def readcsv(path):
 with open(path,encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

def lint(chapter,text):
 problems=[]
 def add(rule,severity,message,excerpt='',line=0):
  problems.append({'rule':rule,'severity':severity,'message':message,'line':line,'excerpt':excerpt[:160]})
 if chapter not in ALLOW_CH:add('L001','BLOCK','Invalid chapter ID',chapter)
 contracts={r['chapter_id']:r for r in readcsv(BASE.parent/'phase4_authoring'/'CHAPTER-AUTHORING-CONTRACTS-58.csv')}
 if chapter not in contracts:add('L009','BLOCK','Chapter has no frozen authoring contract',chapter)
 title_match=re.search(r'(?m)^#\s+(.+)$',text)
 if not title_match:add('L009','BLOCK','Missing top-level chapter title')
 for i,line in enumerate(text.splitlines(),1):
  lower=line.lower();strip=line.strip();
  if strip.startswith(('```','>')):continue
  for match in re.finditer(r'\bD-\d{2,3}\b',line):
   if match.group() not in ALLOW_D:add('L001','BLOCK','Unknown decision identifier',match.group(),i)
  for match in re.finditer(r'\bCH-\d{3}\b',line):
   if match.group() not in ALLOW_CH:add('L001','BLOCK','Unknown chapter identifier',match.group(),i)
  for match in re.finditer(r'\bMF-EVT-\d{3}\b',line):
   if match.group() not in {f'MF-EVT-{j:03}' for j in range(1,16)}:
    add('L010','BLOCK','Meridian fixture event not in v1.0 ledger',match.group(),i)
  if re.search(r'(?i)\b(?:layers?\s+[0-9]+(?:[–-][0-9]+)?|security plane)\b',line) and 'legacy' not in lower and 'incorrect' not in lower:
   add('L006','BLOCK','Legacy layer/control-plane taxonomy in normative prose',line,i)
  if re.search(r'(?i)\b(?:context|retrieval|vector(?:\s+search)?)\b.{0,75}\b(?:authori[sz]es?|permits?|grants?)\b.{0,75}\b(?:refund|external|payment|mutation)',line):
   if not re.search(r'(?i)\b(?:not|cannot|never|must not|does not|without)\b',line):add('L002','BLOCK','Context appears to authorise external mutation',line,i)
  if re.search(r'(?i)\b(?:gateway|pep)\b.{0,55}\b(?:reconcil(?:e|es|ed)|resolv(?:e|es|ed))\b.{0,60}\b(?:product|identity|record|conflict)',line):
   if not re.search(r'(?i)\b(?:not|cannot|never|must not|does not|without)\b',line):add('L002','BLOCK','Gateway appears to reconcile source identity',line,i)
  if re.search(r'(?i)\b(?:Meridian|refund|MF-ACT-REF-001)\b.{0,140}\b(?:refund (?:was )?posted|payment (?:was )?sent|refund:execute was permitted|refund issued successfully)',line):
   if not re.search(r'(?i)\b(?:not|no|never|denied|false|hypothetical|separately|counterfactual)\b',line):add('L003','BLOCK','Misrepresents denied Meridian refund as posted',line,i)
  if re.search(r'(?i)(?:Meridian|fixture).{0,140}(?:proves?|verified|demonstrates?).{0,55}(?:production|deployed|cryptographic|signed receipt|network enforce)',line):
   if not re.search(r'(?i)\b(?:not|does not|cannot|no|only synthetic)\b',line):add('L004','BLOCK','Synthetic evidence is promoted to production assurance',line,i)
  if re.search(r'(?i)\b(?:MF-EVD-RC-001|Retail Product Registry|Retail CRM)\b.{0,85}\b(?:resolved|reconciled|merged)\b',line):
   if not re.search(r'(?i)\b(?:unresolved|not|cannot|never|must not|no)\b',line):add('L003','BLOCK','Reconciliation conflict might be shown as resolved',line,i)
  if re.search(r'(?i)\b(?:refund:request).{0,50}\b(?:implies|equates to|grants|authori[sz]es)\b.{0,60}(?:refund:execute)',line):
   if not re.search(r'(?i)\b(?:not|does not|cannot|never)\b',line):add('L003','BLOCK','Delegated authority appears widened',line,i)
  if re.search(r'(?i)\b(?:production|deployed)\b.{0,30}\b(?:proven|validated|certified)\b',line) and ('Meridian' in text):
   add('L004','WARN','Check deployment validation claim against independent evidence',line,i)
 if re.search(r'\bMF-(?:EVT|EVD|ACT|REQ)-',text) and not re.search(r'(?i)\b(?:synthetic|illustrative|fixture)\b',text):add('L008','BLOCK','Meridian claims require synthetic evidence grading')
 if not re.search(r'\bD-\d{2}\b',text):add('L007','WARN','No direct Atlas reference')
 # cannot infer an approved editorial link or reviewer signature from chapter prose.
 return {'chapter':chapter,'status':'BLOCK' if any(x['severity']=='BLOCK' for x in problems) else 'DRAFT_LINT_PASS_NOT_APPROVED','diagnostics':problems,'counts':dict((s,sum(x['severity']==s for x in problems)) for s in ['BLOCK','WARN']), 'limits':['Mechanical scanning cannot detect every semantic contradiction','No review, rights or approval is inferred','Frozen source bytes must be checked separately']}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('chapter');ap.add_argument('file',type=Path);ap.add_argument('--json',type=Path);arg=ap.parse_args()
 r=lint(arg.chapter,arg.file.read_text(encoding='utf-8'));payload=json.dumps(r,indent=2)
 if arg.json:arg.json.write_text(payload+'\n')
 print(payload);return 1 if r['status']=='BLOCK' else 0
if __name__=='__main__':sys.exit(main())
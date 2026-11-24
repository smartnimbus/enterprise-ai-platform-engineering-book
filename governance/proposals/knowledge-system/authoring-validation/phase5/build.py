from pathlib import Path
import csv,re,json,hashlib,collections,datetime,textwrap
ROOT=Path('/mnt/data'); OUT=ROOT/'phase5_validation'; OUT.mkdir(exist_ok=True)
P3=ROOT/'phase3_integrity';P4=ROOT/'phase4_authoring'

def rows(p):
 with open(p,encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def save(name, data, fields=None):
 p=OUT/name
 if fields is None:fields=list(data[0])
 with open(p,'w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
 return p

def spl(s):return sorted(set(re.findall(r'CH-\d{3}',s or '')))

def role(ch):
 n=int(ch[3:]);return 'lifecycle application' if 24<=n<=34 else 'playbook implementation' if 41<=n<=50 else 'reference-only' if n in (23,51,52,53,54,55,56,57,58) else 'supporting explanation'

a={r['decision_id']:r for r in rows(P4/'DECISION-AUTHORITY-30.csv')}; p3={r['decision_id']:r for r in rows(P3/'DECISION-TRACEABILITY-30.csv')}; out=[]; exceptions=[]
for did,d in a.items():
 src=p3[did]; ca=set(spl(src['catalogue_chapters'])); toc=set(spl(src['toc_chapters_expanded']))
 category={};provenance={}
 for field,cat in [('primary_topic_explanation','primary explanation'),('supporting_explanations','supporting explanation'),('lifecycle_application','lifecycle application'),('playbook_implementation','playbook implementation'),('reference_only','reference-only')]:
  for ch in spl(d[field]):
   if ch in category and category[ch]!=cat:
    exceptions.append({'id':did+'-'+ch,'severity':'P1','kind':'MULTIPLE_PROPOSED_ROLES','subject':did,'details':f'{ch}: {category[ch]} versus {cat}','resolution':'Human verify intended single authoritative role','status':'OPEN'})
   category.setdefault(ch,cat)
 allchs=ca|toc|set(category)
 for ch in sorted(allchs):
  tag='BOTH' if ch in ca and ch in toc else 'CATALOGUE_ONLY' if ch in ca else 'TOC_ONLY' if ch in toc else 'PHASE4_EDITORIAL_ONLY'
  prior=category.get(ch)
  guess=prior or role(ch)
  # Avoid pretending a TOC omnibus range is specific technical coverage
  if ch in ('CH-023','CH-052','CH-056','CH-058') and guess!='reference-only':
   if ch in ('CH-023','CH-052','CH-056','CH-058'):
    exceptions.append({'id':did+'-'+ch+'-omni','severity':'P1','kind':'OMNIBUS_ROLE_CONFLICT','subject':did,'details':'Omnibus chapter assigned '+guess,'resolution':'Reference-only except record is physically printed in Chapter 23','status':'OPEN'})
    guess='reference-only'
  reviewer='REVIEW_REQUIRED' if tag!='BOTH' or (prior is None) else 'CONFIRM_EDITORIAL_ROLE'
  out.append({'decision_id':did,'decision_title':d['title'],'chapter_id':ch,'link_role':guess,'source_presence':tag,'source_classification':'SOURCE_EXPLICIT_REFERENCE' if tag!='PHASE4_EDITORIAL_ONLY' else 'PHASE4_PROPOSED_ONLY','phase4_proposed_role':prior or '', 'reason':('frozen catalogue and TOC' if tag=='BOTH' else 'catalogue direct reference only' if tag=='CATALOGUE_ONLY' else 'TOC reference or range only' if tag=='TOC_ONLY' else 'Phase 4 editorial routing only'), 'ratification_status':'PROPOSED_NOT_APPROVED','review_action':reviewer,'decision_default_changed':'NO','resolution_note':'Role assigned for authoring crosswalk; requires editorial ratification; no frozen source changed'})
  if tag!='BOTH':
   exceptions.append({'id':did+'-'+ch,'severity':'P1','kind':'ATLAS_TOC_REFERENCE_ASYMMETRY','subject':did,'details':f'{ch} is {tag}; proposed {guess}','resolution':'Ratify role as primary/supporting/lifecycle/playbook/reference or drop explicitly with reason; do not edit frozen default','status':'CLASSIFIED_PENDING_APPROVAL'})

discrepant={d for d in a if p3[d]['finding']=='MAPPING_RECONCILIATION_REQUIRED'}
assert len(a)==30 and len(discrepant)==26
save('RECONCILED-ATLAS-TOC-LINKS.csv',out)
summary=[]
for did in sorted(a):
 rr=[r for r in out if r['decision_id']==did];types=collections.Counter(r['source_presence'] for r in rr)
 summary.append({'decision_id':did,'title':a[did]['title'],'original_phase3_status':p3[did]['finding'],'total_links':len(rr),'both_sources':types['BOTH'],'catalogue_only':types['CATALOGUE_ONLY'],'toc_only':types['TOC_ONLY'],'editorial_only':types['PHASE4_EDITORIAL_ONLY'],'primary_chapter':a[did]['primary_topic_explanation'],'classification_status':'ALL_LINKS_TYPED_PROPOSED','approval_status':'PENDING_QUALIFIED_EDITORIAL_AND_ARCHITECT_REVIEW','frozen_catalogue_edited':'NO','frozen_toc_edited':'NO'})
save('ATLAS-TOC-RECONCILIATION-30.csv',summary)

style=(ROOT/'style-v1.2.md').read_text(encoding='utf-8');lines=style.splitlines()
pat=re.compile(r'(?i)\b(?:chapter|ch\.)\s*(\d{1,2})(?!\d)|\blayers?\s*\d+(?:[–-]\d+)?\b|\bsecurity plane\b|\bappendix\s*[A-Z]\b')
found=[]
for lno,l in enumerate(lines,1):
 for m in pat.finditer(l):
  token=m.group(0); n=m.group(1); clas='REVIEW_CONTEXT';repl='';reason=''
  if lno==31 and n=='16':clas='CONFIRMED_MISROUTE';repl='Chapter 23 (the Decision Atlas)';reason='Chapter 16 is the Gateway Control Plane'
  elif lno==36 and n=='23':clas='CONFIRMED_MISROUTE';repl='Chapter 20 (FinOps Control Plane); Chapter 23/D-26 for the Atlas default';reason='FinOps owner is Chapter 20'
  elif lno==108 and ('Layer' in token or 'security plane' in token):clas='CONFIRMED_LEGACY_IN_POSITIVE_EXAMPLE';repl='Execution/Tooling/Context/Lifecycle; Identity, Gateway and Data Protection planes as applicable';reason='Incorrect layer numbers/ninth security plane'
  elif lno==519 and n=='18':clas='CONFIRMED_STALE_TEMPLATE_HEADING';repl='Template F4: Anti-pattern template; chapter use by approved brief, not Chapter 18';reason='Chapter 18 is Verification, not generic anti-pattern home'
  elif lno==614 and n=='30':clas='CONFIRMED_STALE_TEMPLATE_HEADING';repl='Chapter 56 (Glossary)';reason='Chapter 30 is First Use Case'
  elif lno==622 and n=='14':clas='CONFIRMED_STALE_TEMPLATE_HEADING';repl='Chapter 53 (Protocol and Boundary Reference)';reason='Chapter 14 is Lifecycle Structural Layer'
  elif lno==635 and n=='29':clas='CONFIRMED_STALE_TEMPLATE_HEADING';repl='Chapter 55 (Standards and Regulatory Map)';reason='Chapter 29 is Stage 5 bootstrap'
  elif lno==772 and ('Layer' in token or n=='15'):clas='CONFIRMED_LEGACY_DIAGRAM_GUIDANCE' if 'Layer' in token else 'REVIEW_CONTEXT';repl='E/T/C/L Structural Layers; runtime Gateway Chapter 16, Identity Chapter 15';reason='No numbered layers 6–8'
  elif lno==73 and n=='4':clas='EXEMPT_COMPANION_EXAMPLE';reason='Explicit reference to a different companion book'
  elif lno==640 and n in ('15','18'):clas='REVIEW_STANDARDS_ROW';reason='Verify standards coverage chapter 55 versus chapter 15/18 usages'
  elif lno in (773,775):clas='VALID_NAVIGATION' if n in ('10','11','15') else 'REVIEW_CONTEXT';reason='Actual architecture chapter named'
  elif 'Appendix' in token:clas='APPENDIX_ALIAS_REVIEW';reason='Appendix letter may be legacy; check frozen TOC appendix mapping; no automatic replacement'
  found.append({'line':lno,'occurrence':token,'classification':clas,'context':l.strip()[:650],'proposed_erratum':repl,'rationale':reason,'source':'Style Bible v1.2','approval_status':'PENDING_HUMAN_APPROVAL' if clas.startswith('CONFIRMED') else 'REVIEW_OR_EXEMPT','frozen_source_changed':'NO'})
save('STYLE-BIBLE-ALL-CANDIDATE-REFERENCES.csv',found)
errors=[r for r in found if r['classification'].startswith('CONFIRMED')]
save('STYLE-BIBLE-PROPOSED-ERRATA.csv',errors)

# Preserve a separate display explanation for source-evidence and generated exercises.
clauses=[
('L001','CRITICAL','FROZEN_ID','Use only exact D-01..D-30 IDs, CH-001..058, original Meridian IDs','Reject unknown D-31, fabricated IDs, invented event reference'),
('L002','CRITICAL','WRONG_AUTHORITY','Do not let Context authorize action or Gateway reconcile source disagreements','Block canonical boundary inversion'),
('L003','CRITICAL','FORBIDDEN_SIDE_EFFECT','No text may claim refund posted/execute permitted when describing the Meridian denied case','Block false outcome'),
('L004','CRITICAL','FALSE_VALIDATION','Synthetic fixture cannot substantiate production deployment or cryptographic verification','Block false assurance'),
('L005','CRITICAL','FROZEN_CHANGE','Reject edits to frozen TOC/Atlas/fixture unless separately approved existing exception process','Fail source digest comparison'),
('L006','MAJOR','TERMINOLOGY','Do not use numbered structural layers or ninth security plane as normative','Block legacy taxonomy outside explicit quotations'),
('L007','MAJOR','CROSSWALK','Cite valid decision IDs with typed role and canonical primary owner','Fail invalid decision role and unresolved review status for production'),
('L008','MAJOR','EVIDENCE_STATE','Explicitly grade synthetic/demo/pending/implemented/tested/reproduced/approved','Fail ungraded consequential evidence'),
('L009','MAJOR','CHAPTER_SCOPE','No chapter can redefine another chapter technical authority or Atlas default','Reject scope-boundary violations'),
('L010','MAJOR','PROVENANCE','Every asserted observed event has an exact source file/event/evidence ID','Fail unverifiable material claim'),
('L011','MAJOR','IDEMPOTENCY','Keep authorisation and idempotency distinct from side effect','Flag mutation without permit'),
('L012','MAJOR','RELEASE_CANDIDATE','Distinguish failed release candidate from later revised candidate','Flag collapse of release timeline'),
('L013','WARNING','DUPLICATE_TEACHING','Use one explanation owner; link, do not replicate material without new reader task','Manual review of similarity'),
('L014','WARNING','NAVIGATION','Resolve old chapter references and glossary destinations','Warn for review unless clearly invalid'),
('L015','WARNING','PILOT_COVERAGE','D-10/D-14/D-18 have linked source claims, but not independent authoring pass','Visible limitation on pilot results'),
]
save('AUTHORING-LINT-SPECIFICATION.csv',[dict(rule_id=i,severity=s,category=k,rule=rule,acceptance=accept,mode='PARTIAL_AUTOMATION; HUMAN REVIEW FOR SEMANTICS') for i,s,k,rule,accept in clauses])
gates=[
('G0','SOURCE_PIN','Frozen fixture/Atlas/TOC hashes and candidate crosswalk pinned','Human editorial owner verifies source manifest; provenance','BLOCKED until reviewer accepts candidate authoring baseline'),
('G1','SCOPE','Chapter scope/contract and typed references complete','Validator + human owner','Reject missing chapter owner and known map contradictions'),
('G2','AUTOMATED_LINT','Critical and major mechanical checks pass','CI / local deterministic run','0 critical; 0 unwaived major'),
('G3','SEMANTIC_REVIEW','Security, authority, claim grade and fixture narrative independently checked','Qualified technical reviewer','0 material authority or evidence contradictions'),
('G4','CROSS_CHAPTER','Paired authors compare overlapping concepts and explicitly record deltas','Two reviewers, one independent','No unexplained semantic divergence'),
('G5','EDITORIAL','Template, teaching uniqueness, figures, citations and rights accepted','Human editorial reviewer','Chapter acceptance signed under existing operating system'),
('G6','PUBLICATION','Reproducible evidence package, immutable source versions and approved release','Existing publication gate / human approval','Never approve from AI-to-AI consensus')]
save('CHAPTER-VALIDATION-GATES.csv',[{'gate':i,'name':n,'entry_requirement':e,'responsible_review':who,'exit_criteria':x,'current_status':'NOT_EXECUTED_ON_PRODUCTION_MANUSCRIPTS'} for i,n,e,who,x in gates])

# Two deliberately bounded author simulations using exact fixture distinctions.
a_text='''# Simulated Author A — Chapter 13 / D-14 (training excerpt)
The Context Structural Layer retrieves evidence and records semantic disagreement; it does not grant permission to mutate a financial system. In the frozen Meridian v1.0 synthetic fixture, the Retail Product Registry reports **ACTIVE** while Retail CRM reports **CLOSED**. Record `MF-EVD-RC-001` preserves the conflict as **UNRESOLVED**. The source-level access decision belongs to the documented policy and authority boundary, not to vector similarity. Context may surface candidate sources with provenance; it must not silently select the convenient record, rewrite the product state or infer that payment was authorised. This is synthetic fixture evidence, not proof of a deployed reconciliation engine.

**Atlas linkage:** D-14 (semantic identity reconciliation), with the immutable default sourced from the frozen Atlas. **Handoff to Chapter 16:** the Gateway Control Plane must treat unresolved eligibility as a policy input, not as a new authorisation granted by Context.
'''
b_text='''# Simulated Author B — Chapter 16 / D-10 and D-18 (training excerpt)
The Gateway Control Plane intercepts a proposed mutable tool call. Governance defines the policy; Identity provides the constrained delegation chain; the Gateway policy decision and enforcement points evaluate and block the proposed action; Tooling may invoke an external processor only following validated permission. In the frozen Meridian v1.0 synthetic fixture, `MF-EVD-DG-001` retains effective `refund:request`, not `refund:execute`. `MF-EVD-AU-001` records **DENY** for proposed action `MF-ACT-REF-001`; `MF-EVD-DN-001` records that no refund was posted. The Context record `MF-EVD-RC-001` remains **UNRESOLVED**; Gateway does not reconcile it. A separate direct-egress attempt `MF-EVT-013` is blocked in the synthetic fixture. This is not proof of deployed network egress controls or cryptographic receipt validation.

**Atlas linkage:** D-10 owns action authorisation, D-18 owns non-bypassability. **Handoff to Chapter 13:** Context produces provenance and unresolved state; it cannot grant `refund:execute` or change the policy.
'''
(OUT/'PILOT-A-CH13-D14.md').write_text(a_text)
(OUT/'PILOT-B-CH16-D10-D18.md').write_text(b_text)

pilot=[
('A/B-01','Context owner','Context retains evidence and unresolved semantic state','CONSISTENT','Both attribute reconciliation state to Context; neither claims identity issuance'),
('A/B-02','Gateway owner','Gateway controls action admission, not semantic reconciliation','CONSISTENT','Both authors reserve action enforcement for Gateway'),
('A/B-03','Policy and identity','Governance defines policy; Identity constrains delegation','CONSISTENT','B explicitly names both; A does not conflict'),
('A/B-04','D-14 result','Product state remains UNRESOLVED','CONSISTENT','Both preserve disagreement'),
('A/B-05','D-10 result','DENY; refund:request does not imply refund:execute','CONSISTENT','B uses exact fixture; A refrains from asserting permit'),
('A/B-06','D-18 bypass','Simulated direct-egress block; no deployed guarantee','CONSISTENT','B explicitly grades evidence; A does not make egress claims'),
('A/B-07','Canonical terms','Context Structural Layer; Gateway Control Plane','CONSISTENT','Correct taxonomy; no numbered layers'),
('A/B-08','Cross-chapter navigation','Chapter 13 not authorisation; Chapter 16 not reconciliation','CONSISTENT','Explicit reciprocal handoffs'),
('A/B-09','Independent authoring','Authors independently draft from no shared written test script','NOT_DEMONSTRATED','Both synthetic excerpts authored as a controlled exercise within one assistant, not independent models'),
('A/B-10','Full manuscript integration','Complete Chapters 13 and 16 obey all F6/F7 instructions','NOT_DEMONSTRATED','Only short synthetic excerpts tested; Chapter 13 is still a blueprint'),
]
save('CROSS-AUTHOR-COMPARISON.csv',[dict(check_id=i,topic=t,expected=e,result=result,reason=why,evidence_grade='SIMULATED_NOT_INDEPENDENT') for i,t,e,result,why in pilot])

# manifest
sources=[ROOT/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv',ROOT/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv',ROOT/'style-v1.2.md',ROOT/'chapter-16-gateway-control-plane-v1.0.md',ROOT/'Chapter_13_Authoring_Blueprint_v1.0.md',ROOT/'Chapter_16_Authoring_Blueprint_v1.0.md',P3/'DECISION-TRACEABILITY-30.csv',P3/'CONTRADICTION-AND-RISK-REGISTER.csv',P4/'DECISION-AUTHORITY-30.csv',P4/'CHAPTER-AUTHORING-CONTRACTS-58.csv']
manifest={str(p.relative_to(ROOT)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size_bytes':p.stat().st_size} for p in sources}
(OUT/'SOURCE-FINGERPRINTS.json').write_text(json.dumps({'snapshot_date':'2026-11-24','sources':manifest},indent=2)+'\n')
metrics={'decision_records':len(a),'phase3_discrepant_decisions':len(discrepant),'classified_links':len(out),'crosswalk_link_variants':dict(collections.Counter(x['source_presence'] for x in out)),'style_candidates':len(found),'style_confirmed_occurrences':len(errors),'lint_rules':len(clauses),'pilot_consistent':sum(x[3]=='CONSISTENT' for x in pilot),'pilot_not_demonstrated':sum(x[3]=='NOT_DEMONSTRATED' for x in pilot)}
(OUT/'SPRINT-METRICS.json').write_text(json.dumps(metrics,indent=2)+'\n'); print(metrics)

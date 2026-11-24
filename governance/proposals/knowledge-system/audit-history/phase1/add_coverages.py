import csv
from pathlib import Path
p=Path('/mnt/data/convergence');root=Path('/mnt/data')
def read(path):return list(csv.DictReader(path.open(encoding='utf-8-sig',newline='')))
def save(name,items):
 with (p/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(items[0]));w.writeheader();w.writerows(items)
toc=read(root/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv')
cat=read(root/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv')
rows=[]
for d in cat:
 pages='PRESENT_IN_DRAFT_PR_1' if d['id'] in ('D-10','D-18') else 'MISSING_STANDALONE_PAGE'
 rows.append({'id':d['id'],'title':d['title'],'mapped_chapters_from_catalogue':d['chapters'],'catalogue_status':'PRESENT_DRAFT_PR_1_FROZEN_SOURCE','F1_standalone_page':pages,'canonical_main_status':'ABSENT','approved_applied_ADR':'NONE_EVIDENCED','verified_implementation':'NONE_EVIDENCED','independent_validation':'NOT_RUN','required_action':'Preserve frozen default; create F1 production page without changing meaning' if pages!='PRESENT_IN_DRAFT_PR_1' else 'Import unchanged, verify F1 template and proof'})
save('DECISION-COVERAGE-30.csv',rows)
A=read(root/'execution-mvp'/'100-ARTICLE-MVP-CANDIDATES.csv'); B=read(root/'execution-mvp'/'100-ENGINEERING-PATTERN-CANDIDATES.csv')
out=[]
for d in A:out.append({'asset_id':d['article_id'],'type':'article','rank':d['rank'],'title':d['title'],'domain':d['domain'],'priority':d['priority'],'planned_wave':d['publication_wave'],'mapped_chapters':d['frozen_chapters'],'mapped_decisions':d['frozen_decisions'],'source_register':'100-ARTICLE-MVP-CANDIDATES.csv','current_state':'CANDIDATE_ONLY_NOT_PUBLISHED','independent_review':'NOT_EVIDENCED','published_main':'NO'})
for d in B:out.append({'asset_id':d['pattern_id'],'type':'pattern','rank':d['rank'],'title':d['pattern'],'domain':d['group'],'priority':d['priority'],'planned_wave':d['publication_wave'],'mapped_chapters':d['fabric_chapters'],'mapped_decisions':d['atlas_decisions'],'source_register':'100-ENGINEERING-PATTERN-CANDIDATES.csv','current_state':'CANDIDATE_ONLY_NOT_TESTED','independent_review':'NOT_EVIDENCED','published_main':'NO'})
save('ARTICLE-AND-PATTERN-STATUS-200.csv',out)
print('covered',len(rows),'decisions',len(out),'knowledge candidates')

from pathlib import Path
import csv,json,zipfile,hashlib
p=Path('/mnt/data/book-completion'); src=Path('/mnt/data')
rows=list(csv.DictReader(open(src/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv',encoding='utf-8-sig')))
pilot={13,16,23}; intensive={10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,28,30,32,33,34,36,37,38,39,40,42,43,44,47,48,49,50,52,57}
compress={46,51,53,54,55,58}
# pragmatic sequence, no change to publication order
waves={
'W0 Controlled pilot': [13,16,23],
'W1 Concept, authority and architecture': [1,2,3,4,5,6,7,8,9,10,11,12,14,15,17,18,19,20,21,22],
'W2 Lifecycle and operating story': list(range(24,41)),
'W3 Practitioner proof': list(range(41,51)),
'W4 Reference and final integration': list(range(51,59))}
# Chapter 23 treated as 30 atlas-page composition not single author redefinition
waveby={n:w for w,ns in waves.items() for n in ns}
# add any missing
assert len(waveby)==58
status={int(r['chapter']):r for r in csv.DictReader(open(src/'phase2_intellectual/MISSING-CHAPTER-REGISTER-58.csv',encoding='utf-8-sig'))}
fields=['chapter_id','title','part','planned_pages','existing_manuscript_state','wave','six_month_treatment','authoring_mode','specialist_review','dependencies','human_work_hours_estimate','publication_exit']
output=[]
for r in rows:
 n=int(r['chapter']); part=r['title'].split('.',1)[0]; pages=float(r['pages']); prev=status[n]
 mode='Human technical lead + AI-assisted drafting' if n in intensive else 'AI-assisted first draft + human substantive rewrite'
 if n in (13,16,23):mode='Human-led proof-of-book; independent technical editor'
 if n==23: mode='F1 exact-source composition with manual decision-page review'
 reviewer='Security/identity + audit' if n in [7,13,15,16,18,21,27,37,40,48] else 'SRE/platform operations' if n in [11,12,14,17,29,30,31,32,33,34,36,39,43,44,45,46,47,49,50] else 'Economics/FinOps' if n in [5,8,20,38,41] else 'Editorial/source-rights and technical peer'
 treatment='Keep concise within frozen contract' if n in compress else 'Complete at scoped page budget'
 deps='Ch13, Ch16, F1 specimen approved before mass cohort' if n not in pilot else 'Approved source pack, independent human reviewer, lint+semantic QA'
 # AI-assisted *combined human* planning hours: less for reference, more for specialty; includes drafting and specialist review
 base=pages*(2.1 if n in intensive else 1.55)
 if n==16:base=max(12,base-8) # draft exists
 if n==13:base=max(12,base-5) # blueprint not manuscript
 output.append({'chapter_id':f'CH-{n:03d}','title':r['title'].split('.',1)[-1].strip(),'part':part,'planned_pages':r['pages'],'existing_manuscript_state':prev['manuscript_status'],'wave':waveby[n],'six_month_treatment':treatment,'authoring_mode':mode,'specialist_review':reviewer,'dependencies':deps,'human_work_hours_estimate':str(round(base,1)),'publication_exit':'F template compliant; source-linked claims; tech+copy review; human acceptance'})
with open(p/'MANUSCRIPT-PRODUCTION-58.csv','w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerows(output)
hours=round(sum(float(r['human_work_hours_estimate']) for r in output),1);overhead=round(.22*hours+75);total=round(hours+overhead)
summary={'planned_manuscript_pages':448,'proposal_total_estimate_including_front_index':478,'draft_manuscripts':1,'authoring_blueprints':2,'unwritten_standalone_manuscripts':57,'estimated_direct_human_hours':hours,'integration_qa_rights_rework_and_buffer_hours':overhead,'estimated_total_human_hours':total,'available_single_author_15h_week_26weeks':390,'full_6month_team_hours_week':round(total/26,1),'assumptions':'2.1 h/page architecture/high-risk, 1.55 h/page others incl technical review and edit; 22% reserve +75 integration; scenario not measurement'}
(p/'EFFORT-ASSUMPTIONS.json').write_text(json.dumps(summary,indent=2))
print(summary)

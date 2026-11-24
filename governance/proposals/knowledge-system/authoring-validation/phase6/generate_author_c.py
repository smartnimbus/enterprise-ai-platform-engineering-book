import csv, pathlib, json
root=pathlib.Path('/mnt/data'); out=root/'phase6_trial/author-c'; out.mkdir(exist_ok=True)
rows={r['id']:r for r in csv.DictReader((root/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv').open())}
head='''# Author C — F1 decision-page consistency specimens\n\n**Assignment:** D-10, D-14, D-18 only. **Source boundary:** frozen catalogue and existing F1 template; Meridian v1.0 primary records. No Chapter 13 or Chapter 16 author outputs used. **Authority:** source-exact candidate excerpt, not an approved new F1 production page.\n\n'''
for did in ['D-10','D-14','D-18']:
 r=rows[did]
 evidence={'D-10':'`MF-EVD-DG-001`, `MF-EVD-AU-001`, `MF-EVD-DN-001`, `MF-ACT-REF-001`','D-14':'`MF-REC-A-001`, `MF-REC-B-001`, `MF-EVD-RC-001`, `MF-EVT-007`–`008`','D-18':'`MF-EVT-013`, `MF-EVD-DN-001.negative_bypass_test`'}[did]
 boundary={'D-10':'A `DENY` is not a signed action permit. In this synthetic case effective scope remained `refund:request`, no refund:execute permit was issued and no external mutation occurred.','D-14':'Conflict remains `UNRESOLVED`; the retail steward was escalated but no canonical business truth was selected or durable verified eligibility written.','D-18':'Direct-egress blocked is a synthetic negative test, not exhaustive evidence of deployed network or credential enforcement.'}[did]
 txt=f'''### {did}: {r['title']}\n\n**Context.** {r['context']}\n\n**Default.** {r['default']}\n\n**Why.** {r['why']}\n\n**Trade-off.** {r['tradeoff']}\n\n**When to deviate.** {r['deviations']}\n\n**Reversibility.** {r['reversibility']}\n\n**Artefact.** `{r['artifact']}`.\n\n**See also.** Existing catalogue chapter map: {r['chapters']}.\n\n**Teaching/fixture boundary (non-normative assessor note).** {evidence}. {boundary}\n\n'''
 head+=txt
(out/'F1-D10-D14-D18-SPECIMENS.md').write_text(head,encoding='utf-8')
(out/'FROZEN-DEFAULTS.json').write_text(json.dumps({k:{'title':rows[k]['title'],'default':rows[k]['default'],'reversibility':rows[k]['reversibility'],'chapters':rows[k]['chapters']} for k in ['D-10','D-14','D-18']},indent=2)+'\n')
print('Author C source-exact specimen bytes',len(head.encode()))

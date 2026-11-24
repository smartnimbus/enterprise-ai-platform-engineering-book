from pathlib import Path
import csv
p=Path('/mnt/data/convergence')
raw='''README.md
archive/historical/Agentic-Enterprise-Reference-Architecture.md
archive/historical/The-Enterprise-AI-Agent-Fabric-Blueprint.md
decisions/catalogue/Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv
decisions/pages/D-10.md
decisions/pages/D-18.md
decisions/template/Decision_Atlas_Template_v1.0.md
editorial/authoring-blueprints/Chapter_13_Authoring_Blueprint_v1.0.md
editorial/authoring-blueprints/Chapter_16_Authoring_Blueprint_v1.0.md
editorial/outlines/Enterprise_AI_Agent_Fabric_Development_Blueprint.md
editorial/outlines/Enterprise_AI_Agent_Fabric_Revised_TOC.csv
editorial/reviews/Enterprise_AI_Agent_Fabric_Editorial_Review.md
editorial/reviews/chapter-16-editorial-self-review-v1.0.md
editorial/style/style-v1.2.md
knowledge-mining/RESEARCH-IMPORT-STATUS.md
knowledge-mining/briefs/industry-comparison-v2-research-brief.md
knowledge-mining/cross-project-analysis/fabric-hidden-methodology-research-notes-v1.md
knowledge-mining/cross-project-analysis/fabric-industry-comparison-v2.md
knowledge-mining/forensic-review/Archive_Custody_Register.csv
knowledge-mining/forensic-review/Book_Relevance_Matrix_PUBLIC.csv
knowledge-mining/forensic-review/Cross_Project_Patterns.csv
knowledge-mining/forensic-review/Cross_Project_Synthesis.md
knowledge-mining/forensic-review/Forensic_Methodology_and_Limitations.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/AEGIS.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/Kollab.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/MemOS-2026-05-21-09-53-51.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/agentic-enterprise-reference-architecture-complete-v2.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/agentic-enterprise-reference-architecture-final-V2.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/estate-pulse-main.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/estate-pulse.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/uaf.md
knowledge-mining/forensic-review/Individual_Project_Dossiers/workshop-2026-05-21-09-50-32.md
knowledge-mining/forensic-review/Intellectual_Asset_Register_PUBLIC.csv
knowledge-mining/forensic-review/Knowledge_Graph_Edges.csv
knowledge-mining/forensic-review/Knowledge_Graph_Nodes.csv
knowledge-mining/forensic-review/MASTER_FORENSIC_REPORT.md
knowledge-mining/forensic-review/Master_Knowledge_Graph_Guide.md
knowledge-mining/forensic-review/Modernisation_Assessment.md
knowledge-mining/forensic-review/README.md
knowledge-mining/forensic-review/Repository_Import_Plan.md
knowledge-mining/forensic-review/Timeline_and_Concept_Evolution.md
manuscript/part-03/chapter-16-gateway-control-plane-v1.0.md
meridian/fixture/Enterprise_AI_Agent_Fabric_Meridian_Timeline.csv
meridian/fixture/Meridian_Evidence_Fixture_v1.0.md
publishing/apress/Apress_Acquisition_Competitive_Dossier.md
publishing/apress/Apress_Publisher_Proposal_Draft.md
publishing/thought-leadership/Enterprise_AI_Agent_Fabric_IP_and_Thought_Leadership_Playbook.md'''
gov='''governance/proposals/knowledge-system/CRITICAL-MISSING-ASSETS.csv
governance/proposals/knowledge-system/HANDOVER-TEMPLATE-v1.yaml
governance/proposals/knowledge-system/MASTER-GAP-REGISTER.csv
governance/proposals/knowledge-system/MASTER-KNOWLEDGE-SYSTEM-BLUEPRINT-v1.0.md
governance/proposals/knowledge-system/PRODUCT-OPPORTUNITY-REGISTER.csv
governance/proposals/knowledge-system/PROGRAMME-COMPLETENESS-ASSESSMENT-v1.0.md
governance/proposals/knowledge-system/README.md
governance/proposals/knowledge-system/RESEARCH-DOSSIER-CATALOGUE.csv
governance/proposals/knowledge-system/WORKSTREAM-SCORECARD.csv
governance/proposals/knowledge-system/digital-twin/PROGRAMME-DIGITAL-TWIN-DESIGN-v1.0.md
governance/proposals/knowledge-system/digital-twin/PROTOTYPE-TEST-REPORT.json
governance/proposals/knowledge-system/digital-twin/README.md
governance/proposals/knowledge-system/digital-twin/twin-schema-v1.json
governance/proposals/knowledge-system/execution-mvp/100-ARTICLE-MVP-CANDIDATES.csv
governance/proposals/knowledge-system/execution-mvp/100-ENGINEERING-PATTERN-CANDIDATES.csv
governance/proposals/knowledge-system/execution-mvp/MASTER-EXECUTION-BACKLOG-v1.0.md
governance/proposals/knowledge-system/execution-mvp/MASTER-EXECUTION-BACKLOG.csv
governance/proposals/knowledge-system/execution-mvp/README.md
governance/proposals/knowledge-system/independent-validation/INDEPENDENT-VALIDATION-PROGRAMME-v1.0.md
governance/proposals/knowledge-system/independent-validation/README.md
governance/proposals/knowledge-system/independent-validation/SCENARIO-CATALOGUE.csv
governance/proposals/knowledge-system/independent-validation/SCORING-RUBRIC.csv
governance/proposals/knowledge-system/independent-validation/VALIDATION-RUN-TEMPLATE.json
governance/proposals/knowledge-system/multi-ai-contributors/MULTI-AI-CONTRIBUTOR-OPERATING-CONTRACT-v1.0.md
governance/proposals/knowledge-system/multi-ai-contributors/README.md
governance/proposals/knowledge-system/multi-ai-contributors/assignment-example.json
governance/proposals/knowledge-system/multi-ai-contributors/test_ai_change.py
governance/proposals/knowledge-system/multi-ai-contributors/validate_ai_change.py
governance/proposals/knowledge-system/programme-os/PROGRAMME-OPERATING-SYSTEM-v1.0.md
governance/proposals/knowledge-system/programme-os/README.md'''
res='''knowledge-mining/reviews/enterprise-ai-platform-engineering-patterns-03-research-mapping-v1.csv
knowledge-mining/reviews/enterprise-ai-platform-engineering-patterns-03-research-review-v1.md'''
A=raw.splitlines();B=gov.splitlines();C=res.splitlines();assert (len(A),len(B),len(C))==(47,30,2),(len(A),len(B),len(C))
def class_asset(path):
 if path=='REPOSITORY-GOVERNANCE.md':return 'Root governance','proposed governance record','Preserve root authority; ratify and enforce separately'
 if '/historical/' in path:return 'Historical architecture/reference','historical not authoritative','Keep labelled historical; rights/attribution check'
 if path.startswith('decisions/catalogue/'):return 'Frozen Decision Atlas catalogue','frozen candidate on PR #1','Merge verbatim after hash/default checks'
 if path.startswith('decisions/pages/'):return 'Decision Atlas F1 page','frozen candidate on PR #1','Merge verbatim after F1/style review'
 if path.startswith('decisions/template/'):return 'Frozen F1 template','frozen candidate on PR #1','Merge verbatim, no new fields'
 if path.startswith('editorial/style/'):return 'Style Bible','ratified locally, unmerged','Import original SHA/contents verbatim'
 if path.startswith('editorial/outlines/'):return 'Frozen editorial outline','frozen candidate on PR #1','Import exact source, verify 58 chapters'
 if path.startswith('editorial/authoring-blueprints/'):return 'Chapter blueprint','frozen/approved locally','Preserve; track separately from chapter manuscripts'
 if path.startswith('editorial/'):return 'Editorial assessment','working review','Merge after source/version verification'
 if path.startswith('manuscript/'):return 'Chapter manuscript','draft; frozen substantive baseline','Import original; independent tech/editorial proof'
 if path.startswith('meridian/'):return 'Meridian prose/timeline','frozen related source; fixture incomplete','Preserve, add missing machine-readable fixture and validate'
 if path.startswith('publishing/'):return 'Publishing/research','draft','Keep proposal status; verify rights/market claims'
 if path.startswith('knowledge-mining/forensic-review/'):return 'Historical forensic research','derived, unapproved','Rights/security gate, import as research'
 if path.startswith('knowledge-mining/'):return 'Research and programme metadata','working derived','Import as research, not authority'
 if path.startswith('governance/proposals/knowledge-system/digital-twin/'):return 'Digital-twin design/prototype metadata','proposal/offline result','Keep proposal status; CI extractor still absent'
 if path.startswith('governance/proposals/knowledge-system/independent-validation/'):return 'Validation protocol/tool','proposal, no completed trial','Keep test definitions separate from run evidence'
 if path.startswith('governance/proposals/knowledge-system/multi-ai-contributors/'):return 'AI contribution contract/tool','proposal, offline check','Keep proposal status; no inference of GitHub enforcement'
 if path.startswith('governance/proposals/knowledge-system/execution-mvp/'):return 'Execution planning/candidate register','proposed plan, not completed asset','Keep candidate rankings distinct from published assets'
 if path.startswith('governance/proposals/knowledge-system/programme-os/'):return 'Programme OS proposal','proposed/unratified','Keep distinct from root governance, test enforcement'
 return 'Knowledge-system programme proposal','unmerged working','Review authority classification; selectively merge'
branchA='research/industry-lineage-and-book-baseline-2026-11-24';branchB='governance/knowledge-system-v1-2026-11-24';branchC='research/deterministic-first-patterns-2026-11-24'
rows=[]
for path,branch in [('REPOSITORY-GOVERNANCE.md','ALL_BRANCHES')]+[(x,branchA) for x in A]+[(x,branchB) for x in B]+[(x,branchC) for x in C]:
 kind,status,act=class_asset(path)
 rows.append(dict(path=path,source_branch=branch,asset_type=kind,authority_state=status,duplication='Exact SHA duplicate in four branches' if branch=='ALL_BRANCHES' else 'Unique Git path / semantic overlap review may be required',recommended_action=act,approval_status='No submitted PR review evidenced' if branch!='ALL_BRANCHES' else 'Root bootstrap on main, self-labelled proposed'))
with (p/'ALL-TRACKED-ASSETS-80.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),'assets',len(A),len(B),len(C))

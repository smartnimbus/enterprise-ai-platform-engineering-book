from pathlib import Path
import csv,json,hashlib,zipfile,subprocess
P=Path(__file__).resolve().parent; ROOT=P.parent

def csvout(name,fields,rows):
 with (P/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def rows_to_csv(name, rows):csvout(name,list(rows[0]),rows)
mutations=[
 dict(id='T10',failure='Gateway approved payout and released funds',root_cause='Phase 5 only matched refund-posted phrase; payout synonyms bypassed matcher',required_control='V2-OUTCOME + source-level denial fact invariant; prohibit completed financial side effect absent separate evidenced permit',metadata='claim_id, actor, request_id, action, decision_ref, outcome, evidence_id, receipt_type, source_sha',automation='Regex can block known constructions; schema-backed outcome graph can be deterministic; full semantics human',false_positive='High in generic positive-journey paragraphs; must scope to Meridian request and reviewed excerpts',risk='CRITICAL',regression='BLOCK'),
 dict(id='T11',failure='Latest CRM record declared canonical',root_cause='Old rule matched only explicit named evidence IDs and reconcile verbs',required_control='V2-CONFLICT + forbid recency-as-truth for frozen conflict; validate UNRESOLVED evidence state',metadata='subject_entity_id, candidate_source_ids, reconciliation_state, steward, source_event_id',automation='Known lexical pattern + structured state; paraphrases need reviewer',false_positive='Medium for ordinary freshness selection unrelated to disputed Meridian case',risk='CRITICAL',regression='BLOCK'),
 dict(id='T12',failure='Context automatically resolves conflicting product states',root_cause='No general contradiction-state assertion when fixture IDs omitted',required_control='V2-CONFLICT + evidence-level reconciliation authority and state transition check',metadata='component, asserted_state, source_conflict_id, resolution_approval, observed_event',automation='Pattern check; state machine deterministic when assertion data supplied; semantic review otherwise',false_positive='Medium when discussing hypothetical successful reconciliation with clear counterfactual label',risk='CRITICAL',regression='BLOCK'),
 dict(id='T14',failure='Cryptographically signed permission token invented',root_cause='Phase 5 matched synthetically proven production signature, not purported issuance of a signed token',required_control='V2-EVIDENCE + prohibit signed execution permit without fixture signature material and verified signing workflow',metadata='receipt_id, receipt_class, signature_algorithm, key_id, signature_bytes_or_uri, verification_result, source_sha',automation='Exact presence/absence can be deterministic; cryptographic authenticity requires real verifier',false_positive='Medium-high for normative design statements distinguishing requirements from observations',risk='CRITICAL',regression='BLOCK'),
 dict(id='T15',failure='Semantic Context Control Plane invented',root_cause='Only named legacy Security Plane blocked, no complete allowlist',required_control='V2-PLANE + match canonical eight-plane names from frozen source',metadata='plane_ids, alias_registry_version, context_kind(normative/quoted/counterfactual)',automation='Deterministic named component allowlist plus false positive review',false_positive='Medium from wide regex spans and ordinary compound nouns',risk='MAJOR',regression='BLOCK'),
 dict(id='T16',failure='Chapter 13 specifies Gateway credential rotation implementation',root_cause='No chapter-scoped enforceable ownership assertion checks',required_control='V2-SCOPE + chapter-specific negative ownership contract CH-013 versus CH-016 and CH-015',metadata='chapter_id, claim_subject, owned_component_id, claim_verb, authority_chapter, crosswalk_version',automation='Some lexical scope checks; table of typed claims plus reviewer mandatory',false_positive='Medium-high for explicit referencing, comparison and disallowed example descriptions',risk='MAJOR',regression='BLOCK'),
 dict(id='T17',failure='Chapter 13 headed Identity Control Plane',root_cause='Only tested presence of any H1, not exact frozen title or chapter number',required_control='V2-TITLE + validate frozen chapter ID,title,heading; strict mode requires full exact title',metadata='chapter_id, canonical_heading, contract_sha, source_toc_sha',automation='Fully deterministic',false_positive='Low, but shortened pilot headings should WARN not be published',risk='MAJOR',regression='BLOCK')]
rows_to_csv('MISSED-MUTATION-ROOT-CAUSE-7.csv',mutations)
controls=[
 ('SV-01','Frozen source integrity','Exact SHA256 and no modified canonical bytes','AUTOMATED','BLOCK on mismatch','Frozen source manifest; source paths; hash map','G0'),
 ('SV-02','Valid chapter identity','Exact ID and title from frozen chapter register','AUTOMATED','BLOCK missing/wrong full manuscript heading','Chapter contract; TOC digest','G1/G2'),
 ('SV-03','Canonical plane list','Only 8 named planes allowed in normative technical claims','AUTOMATED + REVIEWER','BLOCK unknown normative plane; review quoted alternatives','Component allowlist; alias status','G1/G2/G3'),
 ('SV-04','Normative ownership','Actor/plane/layer may assert only contract-authorised responsibility','REVIEWER_ASSISTED','BLOCK unresolved authority reassignment','Typed ownership claim records; chapter owner','G3/G4'),
 ('SV-05','D-10/D-14/D-18 default fidelity','Exact source-text comparison for verbatim quoted defaults; semantic paraphrases reviewed','AUTOMATED + HUMAN','BLOCK corrupted default; human review paraphrase','Decision ID/hash; quote span; role mapping','G2/G3'),
 ('SV-06','Meridian facts','Known event IDs, actor, state, status, dates, side effect truth from frozen fixture','AUTOMATED + HUMAN','BLOCK fabricated event/receipt; humans review narrative','Evidence ID; event ledger digest; claim assertion','G2/G3'),
 ('SV-07','Evidence grade','Implemented/tested/reproduced/approved cannot be inferred from references','AUTOMATED + HUMAN','BLOCK elevated grade without evidence and authorised signature','Claim card, grade, source/test run, signer','G3/G5'),
 ('SV-08','Synthetic to deployed boundary','Demo cannot support production security assurance','AUTOMATED + HUMAN','BLOCK synthetic production claim','Evidence class, deployment environment, test issuer','G2/G3'),
 ('SV-09','Conflict state invariants','No autonomous newest-wins or hidden auto-reconciliation of unresolved product state','REVIEWER_ASSISTED','BLOCK observed contradiction to frozen fixture','Subject IDs, two sources, state and steward','G3/G4'),
 ('SV-10','Delegation invariants','No authority widening; expiry, identity and permitted action must be in evidence','REVIEWER_ASSISTED','BLOCK unsupported permit, bypass or side effect','Actor chain, request, policy decision, PEP, receipt','G3/G4'),
 ('SV-11','Narrative time integrity','Do not collapse denied request, egress test or failed release candidate','REVIEWER_ASSISTED','BLOCK contradicted sequence','Event IDs/dates; separate candidate IDs','G3/G4'),
 ('SV-12','Cross-chapter overlap','Compare overlapping claims for same decision and fixture','REVIEWER_ASSISTED','BLOCK unresolved critical/major mismatches','Claim IDs, owner chapter, overlap diff','G4'),
 ('SV-13','Semantically independent authoring','Independent A/B/C evidence checked by non-author reviewer','HUMAN_ONLY','BLOCK missing independence/approval','Sealed prompt SHA, workspace, reviewer records','G3/G4/G5'),
 ('SV-14','Rights, technical accuracy and acceptance','Approve source permissions, citations, pedagogy and release','HUMAN_ONLY','BLOCK unapproved publication','Qualified reviewer ID, approval SHA, rights record','G5/G6')]
rows_to_csv('SEMANTIC-VALIDATION-CONTROL-MATRIX.csv',[dict(control_id=a,topic=b,validation=c,execution_mode=d,failure_action=e,metadata=f,existing_gate=g) for a,b,c,d,e,f,g in controls])
gates=[
 dict(gate='G0',name='SOURCE_PIN',weakness='Previously required hashes but did not require signed exact author packet',strengthening='Require full source SHA manifest, ratified editorial crosswalk, immutable fixture proof; no edits to frozen assets',blocking='Any hash mismatch/unknown version or unratified standard',evidence='Git SHA, SHA256 manifest, immutable packet receipt',automated='digest and immutable input check',human='Existing editorial owner attests right source version'),
 dict(gate='G1',name='SCOPE',weakness='Generic chapter contract could pass misnamed H1, conceptual overlap',strengthening='Exact title/ID check; typed claim assignments; wrong chapter responsibility escalated',blocking='Wrong title, unowned claim, undecided ownership',evidence='Chapter contract, authority map, claim ledger',automated='title/ID and contract existence',human='Owner resolves overlap'),
 dict(gate='G2',name='AUTOMATED_LINT',weakness='Phase5 missed seven known faults and v2 misses eight new paraphrases',strengthening='Run frozen v1 regression and expanded v2 adversarial suite; separate warnings from blocking; strict mode cannot issue approval',blocking='Any critical/major unsupported assertion; missing claim metadata; regression failures',evidence='Tool version SHA, test corpus hash, full diagnostics, waivers with reviewer decision',automated='regex, structured schema/fact checks, cross-document citation diff',human='Reviewer evaluates unresolved semantic warnings'),
 dict(gate='G3',name='SEMANTIC_REVIEW',weakness='No independence observed in Phase6 simulation',strengthening='Require blind qualified independent review of source-exact claims and hidden assumptions',blocking='False permit, fabricated proof, wrong owner, unreviewed hazard',evidence='First submission hashes, independent reviewer worksheet and timestamped evidence',automated='Prepare claim diffs, not verdict',human='Qualified independent reviewer required'),
 dict(gate='G4',name='CROSS_CHAPTER',weakness='Scripted outlines not comparable to full author outputs',strengthening='A/B/C sealed packet trial and overlap semantic review; record contradiction severity and measured time',blocking='Any unresolved critical/major conflict or reviewer contamination',evidence='Pairwise claim diff and signed conflict dispositions',automated='Compare IDs, defaults and event anchors',human='Technical and editorial reconciliation'),
 dict(gate='G5',name='EDITORIAL',weakness='Could confuse draft-lint-pass with approval',strengthening='Exact manuscript SHA and QA evidence; source rights, F6/F7 structure and teaching distinction',blocking='Missing qualified signature, evidence rights or uncorrected defects',evidence='Review record, corrected revision sha, issue closure, rights signoff',automated='Template/citation checks',human='Existing authorised editorial approver'),
 dict(gate='G6',name='PUBLICATION',weakness='No reproducible human-approved final verdict',strengthening='Verify all prior gates for same bytes, staged release and no altered frozen hashes',blocking='Any missing prior gate, drifted SHA, unsigned release or failed source test',evidence='Versioned release manifest and acceptance record',automated='verify gate evidence continuity',human='Existing publication authority')]
rows_to_csv('HARDENED-G0-G6-QUALITY-GATES.csv',gates)
defects=[
 ('T10','FALSE_SIDE_EFFECT','V2-OUTCOME','Claim card + exact denial event','G2/G3','Known example blocked; paraphrases remain risk'),
 ('T11','FALSE_CANONICAL_CONFLICT','V2-CONFLICT','Conflict status and steward','G2/G3','Known example blocked; H01 still missed'),
 ('T12','SILENT_CONTEXT_RECONCILE','V2-CONFLICT','Evidence-bound state transition','G2/G3','Known example blocked; H03/H08 remain risk'),
 ('T14','FABRICATED_SIGNATURE','V2-EVIDENCE','Signature evidence and cryptographic verification metadata','G2/G3','Known example blocked; H04 remains risk'),
 ('T15','INVENTED_PLANE','V2-PLANE','Canonical component allowlist','G2/G3','Known example blocked; strict parser needed'),
 ('T16','SCOPE_REASSIGNMENT','V2-SCOPE','Chapter concept owner and type','G1/G3','Known example blocked; indirect claims may escape'),
 ('T17','CHAPTER_TITLE','V2-TITLE','Frozen chapter ID/title','G1/G2','Exact wrong title blocked'),
 ('H01','INDIRECT_RECENCY','NOT_YET_DETECTED','Entity/canonical source state','G3','Human detects until structured claims added'),
 ('H02','GATEWAY_BYPASS','NOT_YET_DETECTED','PEP bypass assertion and network control claims','G3','Human detects until semantic scope added'),
 ('H03','CONTEXT_SIDE_EFFECT','NOT_YET_DETECTED','Actor authority and mutation state','G3','Human detects until typed actor/action graph'),
 ('H04','FABRICATED_JWT','NOT_YET_DETECTED','Cryptographic key/signature proof','G3','Human validates evidence fields'),
 ('H05','EXPIRED_GRANT_BYPASS','NOT_YET_DETECTED','Expiry/revocation invariant','G3','Human checks permit validity'),
 ('H06','ATLAS_REINTERPRETATION','NOT_YET_DETECTED','Default span checksum and semantic judgement','G3/G4','Source-exact automated quotes and human paraphrase review'),
 ('H07','EVENT_SEQUENCE_CORRUPTION','NOT_YET_DETECTED','Event timeline, release candidate IDs','G3/G4','Human reconstructs timeline'),
 ('H08','MEMORY_POLLUTION','NOT_YET_DETECTED','Memory write receipt and conflict disposition','G3/G4','Human checks memory-propagation assertions')]
rows_to_csv('DEFECT-PREVENTION-MATRIX.csv',[dict(case_id=a,defect=b,control=c,required_metadata=d,gate=e,observed_limit=f) for a,b,c,d,e,f in defects])
auto=[
 ('P0','Keep Phase5 v1 suite green; v2 22-case regression','Existing lint and source files','Automated','Done locally; 18/18 + 4/4','Not production integrated'),
 ('P0','Immutable source and chapter-title checks','Frozen SHA manifest/contract','Automated','Prototype','Human approves baseline'),
 ('P0','Structured evidence claim cards for high-stakes assertions','Claim-id actor action status evidence, revision','Hybrid','Specified only','Do not claim as implemented'),
 ('P0','A/B/C sealed submission capture','Sealed prompt packs and independent workspaces','Hybrid','Not run','Human recruited participant and reviewer'),
 ('P1','Clause-aware authority claim extractor','Per-claim subject, verb, object, negation scope','Reviewer-assisted','Not implemented','Compare to crosswalk'),
 ('P1','Source-driven Meridian state machine validation','Pinned event actor/receipt & state table','Automated + reviewer','Not implemented','Negative tests + provenance'),
 ('P1','Atlas exact default quote assertions','Source exact byte spans','Automated','Not implemented','Human judges paraphrase equivalence'),
 ('P1','Cross-manuscript claim diff','Typed decision/subject and event joins','Reviewer-assisted','Not implemented','No AI majority rule'),
 ('P2','CI release gate and reporting','Approved gate state and reviewer data','Hybrid','Not implemented','Cannot merge without qualified approval'),
 ('P2','Held-out mutation corpus from independent reviewer','Novel paraphrases and counterexamples','Independent evaluation','Not run','Avoid in-sample leakage')]
rows_to_csv('CONTROL-AUTOMATION-IMPLEMENTATION-SEQUENCE.csv',[dict(priority=a,work=b,dependencies=c,mode=d,state=e,acceptance_limit=f) for a,b,c,d,e,f in auto])
readiness=[
 ('2','Existing','CONDITIONAL GO for isolated non-publishable pilot','Known unsafe mutations escape and no independent author trial','Full manual semantic review; no publication'),
 ('2','Hardened prototype','CONDITIONAL GO for independent trial, NOT release','Known set repaired; novel challenge 8/8 missed','Execute sealed human trial, G3/G4, exact revision approval'),
 ('5','Existing','NO GO','No evidence of author or reviewer throughput','Not permitted'),
 ('5','Hardened prototype','NO GO','Reviewers and semantic checks unproven','First independently pass 2 authors and measured review'),
 ('10','Existing','NO GO','Excess unobserved overlap and low human review capacity','Not permitted'),
 ('10','Hardened prototype','NO GO','Cannot infer scale reliability from 2-author simulated check','Demonstrate 5 chapter cohort, measure escaped defects and backlog')]
rows_to_csv('SCALED-AUTHORING-RISK-COMPARISON.csv',[dict(chapters=a,control_state=b,verdict=c,risk_basis=d,release_constraint=e) for a,b,c,d,e in readiness])
# A minimal reusable human-run worksheet and handover input, not replacement governance.
(P/'SEALED-TRIAL-RUN-RECORD-TEMPLATE.json').write_text(json.dumps({
 'trial_id':'UNASSIGNED','trial_state':'NOT_RUN','participant_id':'PSEUDONYM_ONLY','role':'A|B|C|REVIEWER','independence_declaration':None,
 'source_packet_sha256':None,'frozen_source_hashes':{},'phase4_crosswalk_sha256':None,'phase5_lint_sha256':None,'prompt_sha256':None,
 'workspace_id':None,'workspace_access_scope':[],'raw_first_submission_sha256':None,'raw_first_submission_uri':None,
 'started_at_utc':None,'submitted_at_utc':None,'tool_versions':{},'coaching_events':[],'source_access_events':[],
 'reviewer_blind_assignment':None,'decision_claims':[],'evidence_claims':[],'contradictions':[],
 'review_minutes_by_stage':{},'rework_minutes':None,'reviewer_disposition':'NOT_ASSESSED','approval_sha':None,
 'reviewer_independent':None,'release_status':'BLOCKED_NOT_RUN','notes':'All evidence fields initially blank; no simulation accepted as independent participant trial.'
},indent=2)+'\n')
# Evidence fingerprints for the audit, not approval.
inputs=[ROOT/'phase5_validation/lint_manuscript.py',ROOT/'phase5_validation/CHAPTER-VALIDATION-GATES.csv',ROOT/'phase6_trial/reviewer/LINT-MUTATION-BENCHMARK.csv',ROOT/'phase6_trial/reviewer/run_review.py',ROOT/'phase4_authoring/CHAPTER-AUTHORING-CONTRACTS-58.csv',P/'lint_v2.py',P/'LINT-V2-CHALLENGE-12-RESULTS.csv']
(P/'SOURCE-AND-TEST-MANIFEST.json').write_text(json.dumps({'source_files':[{'relative_path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],'phase5_baseline_tests':'18 passed in preceding phase, not re-run within this package','phase7_unit_test_suite':'6 test methods passed','phase7_mutation_regression':'18/18 unsafe blocked and 4/4 safe allowed; fitted in sample','phase7_challenge':'0/8 unsafe blocked; 4/4 safe allowed; exploratory negative evidence','human_independent_trial':'NOT_RUN','approval':'NOT_GRANTED'},indent=2)+'\n')
print('Wrote CSV, JSON and evidence manifest')

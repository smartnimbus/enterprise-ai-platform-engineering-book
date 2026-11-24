#!/usr/bin/env python3
"""Build a conservative, *derived* inventory from named, local source CSVs.
No network/LLM calls. Does not write or mutate any source record. Python stdlib.
Usage: python build_twin.py --source /mnt/data --output /mnt/data/programme-digital-twin/generated
"""
import argparse,csv,hashlib,json,re,collections,datetime
from pathlib import Path

ID_FORMAT={"decision":r"D-\d{2}","chapter":r"CH-\d{3}","article":r"KA-\d{3}","pattern":r"EP-\d{3}","validation":r"IV-\d{2}","meridian_event":r"MF-EVT-\d{3}"}
REL={"references","depends_on","implements","validates","challenges","supersedes","approved_by","tested_by","published_in","retired_by","teaches","maps_to","uses_evidence","produced_by","derived_from","reviews","blocks","has_source","affects"}

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):
    if not p.is_file(): raise FileNotFoundError(p)
    with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def add_node(nodes,id,typ,name,source,status="OBSERVED_LOCAL_CANDIDATE",**meta):
    if id in nodes: raise ValueError(f"duplicate ID {id}")
    if not re.fullmatch(ID_FORMAT[typ],id):raise ValueError(f"invalid {typ} ID {id}")
    nodes[id]={"id":id,"type":typ,"title":name,"status":status,"source_path":str(source),"source_sha256":digest(source),"metadata":meta}
def add_edge(edges,src,dst,typ,source,reason):
    if typ not in REL:raise ValueError(typ)
    edges.append({"from":src,"to":dst,"type":typ,"source_path":str(source),"source_sha256":digest(source),"basis":reason,"evidence_state":"EXPLICIT_SOURCE_MAPPING","review_state":"UNREVIEWED_DERIVATION"})
def ids(value,kind):
    patt={"chapter":r"\b\d{1,2}\b","decision":r"\bD-\d{2}\b"}[kind]
    seen=[]
    for t in re.findall(patt,value or ''):
        item=(f"CH-{int(t):03d}" if kind=="chapter" else t)
        if item not in seen:seen.append(item)
    return seen

def build(source):
    nodes={};edges=[];sources={}
    locations={
      'decision':source/'Enterprise_AI_Agent_Fabric_Decision_Catalogue.csv',
      'chapter':source/'Enterprise_AI_Agent_Fabric_Revised_TOC.csv',
      'article':source/'execution-mvp/100-ARTICLE-MVP-CANDIDATES.csv',
      'pattern':source/'execution-mvp/100-ENGINEERING-PATTERN-CANDIDATES.csv',
      'validation':source/'independent-validation/SCENARIO-CATALOGUE.csv',
      'meridian_event':source/'Meridian_Evidence_Fixture_v1.0/event-ledger.csv'}
    for typ,p in locations.items():sources[typ]={"path":str(p),"sha256":digest(p),"authority":"LOCAL_INPUT_NOT_APPROVED_REPOSITORY"}
    for r in load(locations['decision']):add_node(nodes,r['id'],'decision',r['title'],locations['decision'],chapters=r['chapters'],recommended_default=r['default'])
    for r in load(locations['chapter']):add_node(nodes,f"CH-{int(r['chapter']):03d}",'chapter',r['title'],locations['chapter'],template=r['type_template'])
    for r in load(locations['article']):add_node(nodes,r['article_id'],'article',r['title'],locations['article'],rank=int(r['rank']),priority=r['priority'],publication_wave=r['publication_wave'])
    for r in load(locations['pattern']):add_node(nodes,r['pattern_id'],'pattern',r['pattern'],locations['pattern'],rank=int(r['rank']),priority=r['priority'],publication_wave=r['publication_wave'])
    for r in load(locations['validation']):add_node(nodes,r['test_id'],'validation',r['scenario'],locations['validation'],purpose=r['primary_measure'])
    for r in load(locations['meridian_event']):add_node(nodes,r['event_id'],'meridian_event',r['type'],locations['meridian_event'],event_outcome=r['outcome'],fixture_is_synthetic=True)
    # Only explicit crosswalks. None of these assert runtime implementation, test pass or human approval.
    for r in load(locations['decision']):
        for target in ids(r['chapters'],'chapter'):add_edge(edges,r['id'],target,'references',locations['decision'],'Decision catalogue chapters field')
    for typ,pk,cp,dp in [('article','article_id','frozen_chapters','frozen_decisions'),('pattern','pattern_id','fabric_chapters','atlas_decisions')]:
        for r in load(locations[typ]):
            for target in ids(r[cp],'chapter'):add_edge(edges,r[pk],target,'references',locations[typ],cp)
            for target in ids(r[dp],'decision'):add_edge(edges,r[pk],target,'references',locations[typ],dp)
    # Validation scenario input_sources column includes explicit source identifiers. Do not infer test execution.
    for r in load(locations['validation']):
        for target in re.findall(r'\bD-\d{2}\b|\bMF-EVT-\d{3}\b',r.get('input_sources','')):
            add_edge(edges,r['test_id'],target,'references',locations['validation'],'Scenario input_sources (reference, not a completed validation)')
    return nodes,edges,sources

def assess(nodes,edges):
    dangling=[e for e in edges if e['from'] not in nodes or e['to'] not in nodes]
    triples=collections.Counter((e['from'],e['to'],e['type']) for e in edges)
    duplicates=[{"from":k[0],"to":k[1],"type":k[2],"count":v} for k,v in triples.items() if v>1]
    inbound=collections.Counter(e['to'] for e in edges)
    outbound=collections.Counter(e['from'] for e in edges)
    # isolated nodes are normal in candidate inventories, a diagnostic only.
    isolated=[n for n in nodes if not inbound[n] and not outbound[n]]
    bytype=collections.Counter(n['type'] for n in nodes.values())
    referenced={n for e in edges for n in (e['from'],e['to'])}
    # A reference or proposed test scenario never counts as completed validation.
    reports={"total_nodes":len(nodes),"total_edges":len(edges),"nodes_by_type":dict(sorted(bytype.items())),"orphan_links":len(dangling),"duplicate_edge_triplets":len(duplicates),"isolated_candidates":len(isolated),"isolated_ids":isolated[:100],"dangling_edges":dangling[:50],"duplicates":duplicates[:50],"reference_coverage_pct":round(100*len(referenced)/max(1,len(nodes)),2),"completed_validation_coverage":"NOT_MEASURABLE_WITH_SOURCE_FILES","independent_review_coverage":"NOT_MEASURABLE_WITH_SOURCE_FILES","staleness":"NOT_MEASURABLE_WITHOUT_PINNED_APPROVED_BASELINE","source_authority":"LOCAL_INPUT_NOT_APPROVED_REPOSITORY","limitations":["All source files are local research inputs; no claims of approval, merged main or independent validation", "No reviewer, claim or publication records in these input CSVs", "A reference edge is not implements/validates/tested_by", "Missing traceability is not inferred from text similarities", "Path renames require explicit ID and revision manifest rather than heuristic identity", "Any missing citation target remains a dangling edge, not silently created"]}
    return reports

def impact(nodes,edges,target):
    # reverse reachability: who references/depends on affected target
    parents=collections.defaultdict(list)
    for e in edges:
        if e['type'] in {"references","depends_on","implements","validates","derived_from","teaches","maps_to","uses_evidence"}:
            parents[e['to']].append((e['from'],e['type']))
    seen={target};queue=collections.deque([(target,0)]);affected=[]
    while queue:
        cur,depth=queue.popleft()
        for dependent,relationship in parents[cur]:
            if dependent in seen:continue
            seen.add(dependent);affected.append({"id":dependent,"type":nodes.get(dependent,{}).get('type','MISSING_TARGET'),"depth":depth+1,"via":cur,"relation":relationship,"impact":"REVIEW_REQUIRED_NOT_AUTOMATIC_INVALIDATION"});queue.append((dependent,depth+1))
    return {"changed_asset":target,"dependent_candidates":affected,"count":len(affected),"release_impact":"UNKNOWN_UNTIL_APPROVED_SOURCE_AND_REVIEW"}

def write_csv(path,rows,fields):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--impact-id',default='D-10');args=ap.parse_args(argv)
    nodes,edges,sources=build(args.source);args.output.mkdir(parents=True,exist_ok=True)
    report=assess(nodes,edges)
    data={"schema_version":"1.0","generation_mode":"offline_explicit_crosswalk","authority":"DERIVED_NON_AUTHORITATIVE","snapshot_scope":"LOCAL_PROVIDED_FILES_NOT_GITHUB_MAIN","sources":sources,"nodes":list(nodes.values()),"edges":edges}
    (args.output/'twin.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    (args.output/'coverage-report.json').write_text(json.dumps(report,indent=2)+'\n')
    (args.output/'impact-D-10.json').write_text(json.dumps(impact(nodes,edges,args.impact_id),indent=2)+'\n')
    write_csv(args.output/'nodes.csv',({"id":x['id'],"type":x['type'],"title":x['title'],"status":x['status'],"source_path":x['source_path'],"source_sha256":x['source_sha256']} for x in nodes.values()),['id','type','title','status','source_path','source_sha256'])
    write_csv(args.output/'edges.csv',edges,['from','to','type','source_path','source_sha256','basis','evidence_state','review_state'])
    if report['orphan_links'] or report['duplicate_edge_triplets']:print(json.dumps(report,indent=2));return 1
    print(f"OK nodes={len(nodes)} edges={len(edges)} explicit; isolated={len(report['isolated_ids'])}; approved_validations=unknown")
    return 0
if __name__=='__main__':raise SystemExit(main())

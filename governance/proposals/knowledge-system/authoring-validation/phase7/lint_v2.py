#!/usr/bin/env python3
"""Phase 7 additive manuscript lint. NOT an approval engine.
Usage: python lint_v2.py CH-013 draft.md [--strict] [--metadata claims.json]
Reads frozen chapter contracts but never writes to frozen inputs.
"""
import argparse,csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CONTRACTS={r['chapter_id']:r for r in csv.DictReader((ROOT/'phase4_authoring/CHAPTER-AUTHORING-CONTRACTS-58.csv').open(encoding='utf-8'))}
PLANE_NAMES=['Identity','Gateway','Observability','Verification','Governance','FinOps','Data Protection','Interoperability']
KNOWN_EVD={'MF-EVD-RC-001','MF-EVD-CM-001','MF-EVD-AU-001','MF-EVD-DN-001','MF-EVD-DG-001','MF-ACT-REF-001','MF-REQ-REF-001','MF-EVT-013'}
NEG=re.compile(r'\b(?:not|no|never|cannot|does not|did not|without|false|incorrect|denied|prohibited|reject(?:ed)?|unsupported|rather than|isn.t|wasn.t)\b',re.I)

def negated(s):
    # Clause-local negation, not arbitrary elsewhere in the document.
    return bool(NEG.search(s))

def lint(chapter,text,metadata=None,strict=False):
    diag=[]
    def add(rule,severity,message,line=0,evidence=''):
        if not any(x['rule']==rule and x['line']==line and x['message']==message for x in diag):
            diag.append(dict(rule=rule,severity=severity,message=message,line=line,evidence=evidence[:180]))
    if chapter not in CONTRACTS:
        add('V2-ID','BLOCK','Unregistered chapter')
        return result(chapter,diag)
    row=CONTRACTS[chapter]; chapter_no=int(chapter[-3:]);title=row['title'].split('. ',1)[-1].strip()
    lines=text.splitlines()
    heading=next(((i,l[2:].strip()) for i,l in enumerate(lines,1) if l.startswith('# ')),None)
    if not heading: add('V2-TITLE','BLOCK','Missing H1 chapter heading')
    else:
        number,actual=heading
        # Specific claim of a chapter title is testable. Generic outline titles remain non-releasable drafts.
        if re.match(r'^Chapter\s+\d+\s*:',actual,re.I):
            declared=re.match(r'^Chapter\s+(\d+)\s*:\s*(.+)$',actual,re.I)
            if declared and (int(declared.group(1))!=chapter_no or declared.group(2).strip().casefold()!=title.casefold()):
                add('V2-TITLE','BLOCK','Chapter number/title disagrees with frozen contract',number,actual)
        elif re.match(r'^Chapter\s+\d+$',actual,re.I):
            if int(re.search(r'\d+',actual).group())!=chapter_no:add('V2-TITLE','BLOCK','Wrong chapter number',number,actual)
            elif strict:add('V2-TITLE','BLOCK','Release requires exact canonical chapter title',number,actual)
            else:add('V2-TITLE','WARN','Outline heading lacks canonical chapter title',number,actual)
        elif actual.casefold()!=title.casefold():
            add('V2-TITLE','BLOCK' if strict else 'WARN','H1 must be canonical chapter title for release',number,actual)
    # Use an intentionally conservative text-only allowlist. Table/quotes/negations may be false positives.
    for number,line in enumerate(lines,1):
        if line.strip().startswith(('```','>')):continue
        low=line.lower()
        for m in re.finditer(r'\bD-\d{2,3}\b',line):
            if m.group() not in {f'D-{i:02}' for i in range(1,31)}:add('V2-ID','BLOCK','Invented decision ID',number,m.group())
        for m in re.finditer(r'\bMF-(?:EVT|EVD|ACT|REQ)-[A-Z0-9-]+\b',line):
            val=m.group().strip('.,;:')
            if re.fullmatch(r'MF-EVT-\d{3}',val):
                if val not in {f'MF-EVT-{n:03}' for n in range(1,16)}:add('V2-ID','BLOCK','Invented event ID',number,val)
            elif val not in KNOWN_EVD: add('V2-PROVENANCE','BLOCK','Unregistered Meridian reference; require pinned source manifest',number,val)
        # Novel plane proposals are not accepted in normative chapter text.
        for m in re.finditer(r'\b([A-Za-z][A-Za-z -]{1,65}?)\s+Control Plane\b',line):
            name=' '.join(m.group(1).split()).strip(' .,:;')
            # Greedy matches can capture surrounding prose. Check exact candidate suffixes.
            if not any(name.endswith(p) for p in PLANE_NAMES) and not negated(line):
                add('V2-PLANE','BLOCK','Unrecognised Control Plane name; use frozen eight-plane allowlist',number,m.group())
        if re.search(r'\bsecurity plane\b|\bevaluation plane\b|\blayer\s+[0-9]+(?:[-–][0-9]+)?\b',line,re.I) and not re.search(r'\blegacy|historical|incorrect|not a\b',line,re.I):
            add('V2-TAXONOMY','BLOCK','Legacy taxonomy in normative prose',number,line)
        # Preserve Phase 5 regression coverage (T05, T09, T18) in additive v2.
        if re.search(r'\b(?:meridian\s+)?refund\s+(?:was\s+)?(?:posted|issued|settled|paid)\b',line,re.I) and not negated(line):
            add('V2-OUTCOME','BLOCK','Fixture denial cannot be described as a completed refund',number,line)
        if re.search(r'\bMF-EVD-(?:RC|CM)-001\b.{0,90}\b(?:reconciled|resolved|merged)\b',line,re.I) and not negated(line):
            add('V2-CONFLICT','BLOCK','Frozen contradictory source records remain unresolved',number,line)
        if re.search(r'\bMF-EVT-\d{3}\b.{0,65}\b(?:proves|certifies|establishes)\b.{0,70}\b(?:eligibility|permission|authorization|authorisation|success)\b',line,re.I) and not negated(line):
            add('V2-PROVENANCE','BLOCK','Event cited as proof of an unsupported business/authority fact',number,line)
        # T10 outcome synonym: limited to the concrete Meridian financial case or if a payout is asserted outright.
        if re.search(r'\b(?:gateway|meridian)\b.{0,100}\b(?:approved|authori[sz]ed|permitted|granted)\b.{0,45}\b(?:payout|refund|funds|payment)\b',line,re.I) and not negated(line):
            add('V2-OUTCOME','BLOCK','Potential assertion of payout approval in denied Meridian example',number,line)
        if re.search(r'\b(?:gateway|meridian)\b.{0,110}\b(?:released|disbursed|transferred|paid|posted)\b.{0,35}\b(?:funds|refund|payout|payment)\b',line,re.I) and not negated(line):
            add('V2-OUTCOME','BLOCK','Potential false completed payment in Meridian case',number,line)
        # T11; T12 retail conflicts are unresolved, not "newest wins".
        if re.search(r'\b(?:latest|newest|most recent)\b.{0,75}\b(?:crm|record|canonical|truth|wins|closed)\b|\bclosed wins\b',line,re.I) and not negated(line):
            add('V2-CONFLICT','BLOCK','Newest-wins canonicalisation contradicts unresolved fixture conflict',number,line)
        if re.search(r'\bcontext\b.{0,100}\b(?:automatically|silently|implicitly)\s+(?:resolves?|reconciles?|merges?)\b.{0,70}\b(?:conflict|product|record|state)',line,re.I) and not negated(line):
            add('V2-CONFLICT','BLOCK','Context presented as silently resolving disputed source state',number,line)
        # T14 only claims involving fixture; unsupported claims outside fixture become reviewer-assisted.
        if re.search(r'\b(?:meridian|fixture)\b.{0,110}\b(?:cryptograph\w*\s+signed|signed\s+(?:permission|execution|authori[sz]ation)|signature|signed\s+token)\b',line,re.I) and not negated(line):
            add('V2-EVIDENCE','BLOCK','Synthetic fixture does not prove cryptographically signed execution permit',number,line)
        if re.search(r'\b(?:meridian|fixture)\b.{0,100}\b(?:proves|certifies|validates)\b.{0,70}\b(?:deployed|production|network|cryptograph)',line,re.I) and not negated(line):
            add('V2-EVIDENCE','BLOCK','Synthetic evidence promoted to deployed assurance',number,line)
        # T16 Chapter 13 owns Context, not Gateway credential rotation implementation.
        if chapter=='CH-013' and re.search(r'\b(?:this chapter|chapter 13)\b.{0,70}\b(?:specifies?|implements?|defines?|owns?)\b.{0,95}\b(?:gateway|identity)\b.{0,65}\b(?:credential|rotation|policy enforcement|pdp|pep)',line,re.I) and not negated(line):
            add('V2-SCOPE','BLOCK','Chapter 13 claims another chapter\'s technical implementation responsibility',number,line)
        if re.search(r'\bcontext\b.{0,70}\b(?:authori[sz]es?|grants?|permits?)\b.{0,65}\b(?:refund|mutation|payout|payment)',line,re.I) and not negated(line):
            add('V2-AUTHORITY','BLOCK','Context is not a payment authorisation PEP',number,line)
        if re.search(r'\bgateway\b.{0,65}\b(?:reconciles?|resolves?)\b.{0,60}\b(?:product|source|record|conflict)',line,re.I) and not negated(line):
            add('V2-AUTHORITY','BLOCK','Gateway cannot choose business truth',number,line)
        if re.search(r'\brefund:request\b.{0,70}\b(?:implies|grants|equals|permits)\b.{0,70}\brefund:execute\b',line,re.I) and not negated(line):
            add('V2-AUTHORITY','BLOCK','Delegation scope illegally widened',number,line)
        if chapter=='CH-016' and re.search(r'\b(?:this chapter|chapter 16)\b.{0,100}\b(?:owns|defines)\b.{0,65}\b(?:context reconciliation|durable memory)',line,re.I) and not negated(line):
            add('V2-SCOPE','BLOCK','Gateway chapter redefines Context ownership',number,line)
    metadata=metadata or {}
    if strict:
        for key in ('source_sha256','decision_default_hashes','evidence_claims','review_record','crosswalk_status','style_errata_status'):
            if key not in metadata:add('V2-METADATA','BLOCK',f'Missing release-required metadata: {key}')
        if metadata.get('crosswalk_status')!='RATIFIED':add('V2-CROSSWALK','BLOCK','Candidate crosswalk cannot be treated as ratified')
        if metadata.get('style_errata_status')!='APPROVED':add('V2-STYLE','BLOCK','Style errata need authorised sign-off')
        for claim in metadata.get('evidence_claims',[]):
            if claim.get('grade') in ('VALIDATED','APPROVED','IMPLEMENTED','TESTED') and not claim.get('evidence_uri'):
                add('V2-CLAIMS','BLOCK',f'Claim {claim.get("id", "?")} lacks evidence for claimed grade')
        if not metadata.get('review_record',{}).get('qualified_human_approved'):
            add('V2-APPROVAL','BLOCK','No qualified human approval for exact revision')
    else:
        if re.search(r'\b(?:meridian|MF-EVD|MF-EVT)\b',text,re.I) and not re.search(r'\b(?:synthetic|fixture|illustrative|not production)\b',text,re.I):
            add('V2-EVIDENCE','WARN','Fixture evidence grade not explicit in draft')
    return result(chapter,diag)

def result(chapter,diag):
    return {'chapter':chapter,'status':'BLOCK' if any(x['severity']=='BLOCK' for x in diag) else 'DRAFT_LINT_PASS_NOT_APPROVED','counts':{s:sum(x['severity']==s for x in diag) for s in ['BLOCK','WARN']},'diagnostics':diag,'limits':['No exact Atlas semantic equivalence without frozen-text extraction and human review','Source manifest/approval never inferred from prose','No arbitrary prose regex proves absence of contradictions']}

def main():
    p=argparse.ArgumentParser();p.add_argument('chapter');p.add_argument('file',type=Path);p.add_argument('--strict',action='store_true');p.add_argument('--metadata',type=Path);a=p.parse_args()
    m=json.loads(a.metadata.read_text()) if a.metadata else None
    x=lint(a.chapter,a.file.read_text(),m,a.strict);print(json.dumps(x,indent=2));return int(x['status']=='BLOCK')
if __name__=='__main__':sys.exit(main())

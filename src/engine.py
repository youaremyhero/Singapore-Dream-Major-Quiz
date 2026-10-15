"""Exploratory university-neutral interest scorer; NOT validated for student advising."""
import json,csv,re,collections,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parent
Q=json.load(open(ROOT/'question_bank_20.json'))
T=json.load(open(ROOT/'taxonomy.json'))
FOLLOW=json.load(open(ROOT/'followup_bank.json'))['followups']
AREAS={
 'physical_sciences':['Natural, Mathematical & Life Sciences'],
 'life_health':['Health & Allied Health','Natural, Mathematical & Life Sciences'],
 'computing':['Computing, Data & Digital Technology'],
 'engineering':['Built Environment & Engineering'],
 'business':['Business, Finance & Management'],
 'society':['Society, Behaviour & Public Service'],
 'humanities':['Humanities, Language & Cultural Studies'],
 'creative':['Media, Design & Creative Arts'],
 'law_policy':['Society, Behaviour & Public Service'],
 'applied':['Aviation, Maritime & Transport','Education & Early Childhood','Hospitality, Tourism & Service','Sports, Exercise & Human Performance','Food Science & Technology'],
 'environment':['Environmental & Sustainability Studies','Built Environment & Engineering']}
ELIGIBLE={'Undergraduate degree / programme','Primary major','Named degree or business major pathway','Cross-disciplinary degree'}
DISCIPLINES={
 'information_security':('computing',{'cybersecurity'}),
 'software_development':('computing',{'software_creation'}),
 'artificial_intelligence':('computing',{'ai_methods'}),
 'data_science':('computing',{'statistics','data_reasoning'}),
 'physics':('physical_sciences',{'physics'}),
 'chemistry':('physical_sciences',{'chemistry'}),
 'biomedical_research':('life_health',{'biomedical_research'}),
 'patient_care':('life_health',{'person_care'}),
 'rehabilitation':('life_health',{'rehabilitation'}),
 'environmental_engineering':('engineering',{'environmental_engineering'}),
 'mechanical_engineering':('engineering',{'mechanical_systems'}),
 'civil_engineering':('engineering',{'civil_infrastructure'}),
 'economics':('business',{'economics'}),
 'accounting':('business',{'accounting'}),
 'psychology':('society',{'psychology'}),
 'history':('humanities',{'historical_inquiry'}),
 'literature':('humanities',{'literature_language'}),
 'law':('law_policy',{'law_policy'}),
 'design':('creative',{'visual_design','inclusive_design'}),
}

def gather(answers, questions):
    """One question contributes at most 1 unit per field; two choices never double-count."""
    evidence=collections.defaultdict(set)
    for q in questions:
        ans=answers.get(q['id'])
        if q.get('type')=='likert':
            if isinstance(ans,int) and ans>=4:
                for s in q['signals']: evidence[s].add(q['id'])
        else:
            choices=[ans] if isinstance(ans,str) else (ans or [])
            if not isinstance(choices,list) or len(set(choices))>q.get('maxSelections',2): continue
            valid={v['id']:v for v in q['options']}
            for a in set(choices):
                if a in valid:
                    for s in valid[a]['signals']:evidence[s].add(q['id'])
    return evidence

def score(core,follow=None):
    core_e=gather(core,Q)
    extras=gather(follow or [],FOLLOW) if isinstance(follow,dict) else collections.defaultdict(set)
    # Family interest derived ONLY from the core: optional choices cannot rewrite the core.
    family={k:len(set().union(*(core_e.get(sig,set()) for sig in vals))) for k,vals in T.items()}
    ranked=sorted(family,key=lambda k:(-family[k],k))
    promoted=[];explore=[]
    detail={}
    for name,(fam,signals) in DISCIPLINES.items():
        direct_core=set().union(*(core_e.get(s,set()) for s in signals))
        direct_optional=set().union(*(extras.get(s,set()) for s in signals))
        direct=direct_core|direct_optional
        detail[name]={'family':fam,'questions':sorted(direct),'count':len(direct)}
    for name,(fam,signals) in DISCIPLINES.items():
        count=detail[name]['count']
        peer_max=max((detail[peer]['count'] for peer,(peer_fam,_) in DISCIPLINES.items() if peer_fam==fam and peer!=name),default=0)
        # Candidate only if 2 independent direct signals AND a conservative two-question lead over tested peers.
        # Not a validated numerical ranking margin; this is a conservative gating check.
        status='candidate_for_catalogue_review' if count>=2 and count-peer_max>=2 else ('explore_only' if count else 'not_supported')
        detail[name]['status']=status
        detail[name]['peer_max']=peer_max
        if status=='candidate_for_catalogue_review':promoted.append(name)
        elif status=='explore_only':explore.append(name)
    return {'core_family_scores':family,'core_family_order':ranked,'eligible_discipline_signals':promoted,'explore_only_discipline_signals':explore,
            'discipline_evidence':detail,'core_evidence':{k:sorted(v) for k,v in core_e.items()},'optional_evidence':{k:sorted(v) for k,v in extras.items()}}

def browse_catalogue(catalogue, family, limit=12):
    """Category browsing, not recommendation matching: catalogue categories unverified."""
    targets=set(AREAS.get(family,[])); eligible=[]; other=[]
    for row in catalogue:
        if not targets.intersection(set(x.strip() for x in row['Discovery Areas (PROVISIONAL)'].split(';'))):continue
        v={'id':row['Record ID'],'university':row['University'],'programme':row['Programme / Major'],
           'record_type':row['Record Type'],'admission_pathway':row['Parent Degree / Pathway'],
           'source_url':row['Source URL'],'verification_status':row['Verification Status']}
        (eligible if row['Record Type'] in ELIGIBLE else other).append(v)
    return {'family':family,'primary_candidate_records':eligible[:limit], 'other_opportunities':other[:limit],
            'total_primary_candidate_records':len(eligible),'total_other_opportunities':len(other),
            'warning':'Browsable provisional category associations. NOT ranked programme matches, eligibility or official admissions guidance.'}

def load_catalogue():
    with open(ROOT/'six_au_catalogue.csv',encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

if __name__=='__main__':
    c=load_catalogue()
    for fam in T:
        print(fam,browse_catalogue(c,fam,0)['total_primary_candidate_records'])

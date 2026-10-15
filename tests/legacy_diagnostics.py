import csv,json,sys,collections
from pathlib import Path
from engine import *
PROFILES={
 'software':['software_creation','digital_problem_solving'],
 'cybersecurity':['cybersecurity','digital_problem_solving'],
 'AI/data':['ai_methods','statistics','data_reasoning'],
 'civil engineering':['civil_infrastructure','engineering_design'],
 'environmental engineering':['environmental_engineering','engineering_design','environmental_inquiry'],
 'environmental science':['environmental_inquiry','scientific_inquiry'],
 'physics':['physics','quantitative_modelling'],
 'chemistry':['chemistry','scientific_inquiry'],
 'biomedical research':['biomedical_research','living_systems'],
 'patient care':['person_care','community'],
 'economics':['economics','business_strategy'],
 'accounting':['accounting','business_strategy'],
 'history':['historical_inquiry','cultural_studies'],
 'law':['law_policy','ethical_reasoning'],
 'psychology':['psychology','people_research'],
 'creative design':['visual_design','creative_expression'],
 'sports explorer':['sport_science'],
 'undecided':[],
 'mixed computing humanities':['software_creation','historical_inquiry','digital_problem_solving','cultural_studies']}

def simulate(signals):
 s=set(signals);answer={}
 for q in Q:
    if q['type']=='likert': answer[q['id']]=5 if s.intersection(q['signals']) else 3
    else:
      opts=sorted(q['options'],key=lambda v:(-len(s.intersection(v['signals'])),v['id']))
      picks=[v['id'] for v in opts if s.intersection(v['signals'])][:2]
      answer[q['id']]=picks
 return answer

rows=[];all_answers={};cat=load_catalogue()
for name,signals in PROFILES.items():
 a=simulate(signals);all_answers[name]=a;r=score(a)
 top=r['core_family_order']; maxscore=max(r['core_family_scores'].values())
 ties=[x for x in top if r['core_family_scores'][x]==maxscore] if maxscore else []
 expected=[f for f,sigs in T.items() if set(signals)&set(sigs)]
 rows.append({'profile':name,'expected_relevant_families':'|'.join(expected),'top_family_ties':'|'.join(ties),
 'top_family_score':maxscore,'positive_question_count':len([v for v in a.values() if v and v!=3]),
 'eligible_disciplines':'|'.join(r['eligible_discipline_signals']),
 'explore_disciplines':'|'.join(r['explore_only_discipline_signals']),
 'expected_family_in_top_ties':bool(set(expected)&set(ties)) if expected else 'not_applicable',
 'note':'Synthetic answers select matching signals; not independent validation'})

# strict assertions incl optional immutability, optional single cannot promote, duplicate choices capping, skip, catalogue independence
checks=[]
def check(name,expr):
 checks.append({'test':name,'passed':bool(expr)})
 assert expr,name
all_ids=[q['id'] for q in Q];check('20 unique questions',len(all_ids)==len(set(all_ids))==20)
check('chapters 7-6-7',[sum(q['stage']==s for q in Q) for s in (1,2,3)]==[7,6,7])
check('each chapter mixes types',all({'scenario','likert'}==set(q['type'] for q in Q if q['stage']==s) for s in (1,2,3)))
check('no unsupported taxonomy tags',all(sig in set().union(*map(set,T.values())) or sig=='evidence_reasoning' for q in Q for sig in (q.get('signals',[]) if q['type']=='likert' else [s for opt in q['options'] for s in opt['signals']])))
base=score(all_answers['software']);opt=score(all_answers['software'],{'F01':['A']});check('optional keeps core scores fixed',base['core_family_scores']==opt['core_family_scores'])
check('optional keeps core evidence fixed',base['core_evidence']==opt['core_evidence'])
empty=score({}, {'F01':['A']});check('one optional question not sufficient for promotion','information_security' not in empty['eligible_discipline_signals'])
check('two selections same follow-up not two independent questions','software_development' not in score({}, {'F01':['A','B']})['eligible_discipline_signals'])
check('no answers yields no named disciplines',not score({})['eligible_discipline_signals'])
check('unanswered remains neutral',score({})==score({q['id']:None for q in Q}))
check('catalogue browses classifications',browse_catalogue(cat,'computing',5)['total_primary_candidate_records']>0)
check('minors not presented as primary',all(v['record_type'] in ELIGIBLE for v in browse_catalogue(cat,'computing',500)['primary_candidate_records']))
check('primary excludes admission choices',not ELIGIBLE.intersection({'OAM admission choice'}))

out=Path(__file__).parent
with open(out/'profiles.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
with open(out/'test_results.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=checks[0].keys());w.writeheader();w.writerows(checks)
json.dump(all_answers,open(out/'synthetic_answers.json','w'),indent=2)
examples={}
for name in ['software','cybersecurity','environmental engineering','history','mixed computing humanities','sports explorer','undecided']:
 examples[name]=score(all_answers[name]);
 examples[name]['category_browser']=browse_catalogue(cat,examples[name]['core_family_order'][0],3) if examples[name]['core_family_scores'][examples[name]['core_family_order'][0]] else None
json.dump(examples,open(out/'worked_results.json','w'),indent=2)
print('passed',len(checks),'profile top families:')
for r in rows:print(r['profile'],r['top_family_ties'],r['eligible_disciplines'])

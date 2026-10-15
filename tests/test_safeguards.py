import unittest,sys,tempfile,csv,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"src"))
from engine import score,Q
from programme_matcher import load_approved,shortlist
class Tests(unittest.TestCase):
 def test_20_questions_three_mixed_chapters(self):
  self.assertEqual(len(Q),20)
  self.assertEqual([sum(q['stage']==i for q in Q) for i in (1,2,3)],[7,6,7])
  for i in (1,2,3): self.assertEqual(set(q['type'] for q in Q if q['stage']==i),{'scenario','likert'})
 def test_optional_does_not_change_family(self):
  core={q['id']:4 for q in Q if q['type']=='likert'}
  base=score(core);with_extra=score(core,{'F01':['A']})
  self.assertEqual(base['core_family_scores'],with_extra['core_family_scores'])
 def test_no_approved_mappings_no_programme_recommendations(self):
  p=pathlib.Path(__file__).resolve().parents[1]/'data'/'approved_programme_mappings.csv'
  self.assertEqual(shortlist(score({}),load_approved(p)),[])
 def test_no_made_up_specificity(self):
  self.assertEqual(score({})['eligible_discipline_signals'],[])
if __name__=='__main__': unittest.main()

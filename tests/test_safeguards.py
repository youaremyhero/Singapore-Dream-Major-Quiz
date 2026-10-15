import unittest, sys, pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"src"))
from engine import score, Q
from programme_matcher import shortlist, explore_other_opportunities, load_current_catalogue, PRIMARY_TYPES

class Tests(unittest.TestCase):
    def test_20_questions_three_mixed_chapters(self):
        self.assertEqual(len(Q),20)
        self.assertEqual([sum(q["stage"]==i for q in Q) for i in (1,2,3)],[7,6,7])
        for i in (1,2,3):
            self.assertEqual({q["type"] for q in Q if q["stage"]==i},{"scenario","likert"})

    def test_optional_does_not_change_family(self):
        core={q["id"]:4 for q in Q if q["type"]=="likert"}
        self.assertEqual(score(core)["core_family_scores"],score(core,{"F01":["A"]})["core_family_scores"])

    def test_no_made_up_specificity(self):
        self.assertEqual(score({})["eligible_discipline_signals"],[])

    def test_empty_answers_not_forced_into_recommendations(self):
        self.assertEqual(shortlist(score({})),[])

    def test_current_catalogue_is_enabled(self):
        rows=load_current_catalogue()
        self.assertGreater(len(rows),0)
        # A family match is available without manually approving every catalogue row.
        example={"core_family_scores":{"computing":4},"core_family_order":["computing"],
                 "eligible_discipline_signals":[]}
        self.assertTrue(shortlist(example,rows))
        self.assertTrue(all(r["display_status"]=="prototype_catalogue_match"
                            for r in shortlist(example,rows)))

    def test_secondary_offerings_not_primary_matches(self):
        rows=load_current_catalogue()
        example={"core_family_scores":{"computing":4},"core_family_order":["computing"],
                 "eligible_discipline_signals":[]}
        self.assertTrue(all(r["record_type"] in PRIMARY_TYPES for r in shortlist(example,rows)))
        self.assertTrue(all(r["record_type"] not in PRIMARY_TYPES for r in explore_other_opportunities(rows)))

    def test_top_five_are_unique_and_grounded(self):
        example={"core_family_scores":{"computing":4,"business":3},
                 "core_family_order":["computing","business"],
                 "eligible_discipline_signals":[]}
        result=shortlist(example,load_current_catalogue(),limit=5)
        self.assertEqual(len(result),5)
        self.assertEqual(len({r["programme_id"] for r in result}),5)
        self.assertTrue(all(r["source_url"] and r["family_score"]>0 for r in result))

    def test_five_results_not_all_from_one_university_when_alternatives_exist(self):
        example={"core_family_scores":{"computing":4},
                 "core_family_order":["computing"],
                 "eligible_discipline_signals":[]}
        result=shortlist(example,load_current_catalogue(),limit=5)
        self.assertGreaterEqual(len({r["university"] for r in result}),2)

    def test_original_interest_scores_unchanged(self):
        core={q["id"]:4 for q in Q if q["type"]=="likert"}
        original=score(core)["core_family_scores"]
        shortlist(score(core),load_current_catalogue(),limit=5)
        self.assertEqual(original,score(core)["core_family_scores"])

    def test_no_catalogue_size_effect_on_core_scores(self):
        answers={q["id"]:4 for q in Q if q["type"]=="likert"}
        before=score(answers)["core_family_scores"]
        shortlist(score(answers),load_current_catalogue())
        self.assertEqual(before,score(answers)["core_family_scores"])

if __name__=="__main__":
    unittest.main()

"""Run existing synthetic answer profiles through the active top-five matcher."""
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from engine import score
from programme_matcher import recommendation_report,load_current_catalogue
from discipline_mapping import coverage_summary
from programme_matcher import PRIMARY_TYPES

profiles=json.loads((ROOT/"tests"/"synthetic_answers.json").read_text(encoding="utf-8"))
catalogue=load_current_catalogue()
print("Working catalogue coverage:",coverage_summary(catalogue,PRIMARY_TYPES))
print("PROFILE | LEADING FAMILIES | TOP FIVE (university: programme [level])")
for name,answers in profiles.items():
    sc=score(answers)
    report=recommendation_report(sc,catalogue,limit=5)
    families=", ".join("%s=%s"%(f,n) for f,n in
        sorted(sc["core_family_scores"].items(),key=lambda t:(-t[1],t[0]))[:3] if n>0)
    recs=" ; ".join("%s: %s [%s]"%(x["university"],x["programme_title"],x["recommendation_level"])
                   for x in report["top_matches"])
    print("%s | %s | %s"%(name,families or "no positive evidence",recs or "explore more"))

"""Prototype catalogue matcher: current six-AU list is enabled for discovery.

This is an editorial/product decision, not an independent verification of official
programme status, university admission routes, or source links.
"""
import csv
from pathlib import Path

PRIMARY_TYPES = {
    "Undergraduate degree / programme", "Primary major",
    "Named degree or business major pathway", "Cross-disciplinary degree",
}
FAMILY_AREAS = {
    "physical_sciences": {"Natural, Mathematical & Life Sciences"},
    "life_health": {"Health & Allied Health", "Natural, Mathematical & Life Sciences"},
    "computing": {"Computing, Data & Digital Technology"},
    "engineering": {"Built Environment & Engineering"},
    "business": {"Business, Finance & Management"},
    "society": {"Society, Behaviour & Public Service"},
    "humanities": {"Humanities, Language & Cultural Studies"},
    "creative": {"Media, Design & Creative Arts"},
    "law_policy": {"Society, Behaviour & Public Service"},
    "applied": {"Aviation, Maritime & Transport", "Education & Early Childhood", "Hospitality, Tourism & Service", "Sports, Exercise & Human Performance", "Food Science & Technology"},
    "environment": {"Environmental & Sustainability Studies", "Built Environment & Engineering"},
}
ROOT = Path(__file__).resolve().parents[1]
# Derived solely from the interest taxonomy; no catalogue frequency weighting.
import json
FAMILY_SIGNALS = {k:set(v) for k,v in json.loads((ROOT/"data"/"taxonomy.json").read_text(encoding="utf-8")).items()}

def load_current_catalogue(path=None):
    path = Path(path) if path is not None else ROOT / "data" / "programmes_provisional.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

def load_review_suggestions(path=None):
    """Non-authoritative discipline hints, never a statement of approval."""
    path = Path(path) if path is not None else ROOT / "data" / "mapping_review_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return {r["record_id"]: set(filter(None, r["suggested_discipline_ids"].split(";")))
                for r in csv.DictReader(fh)}

def load_approved(path):
    """Keep the stricter ledger available for future independently reviewed data."""
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))

def shortlist(scoring_result, catalogue_rows=None, review_hints=None, limit=5):
    """Select explainable prototype matches without alphabetical or catalogue-size bias.

    Direct signals are *suggestions*, not verified discipline assignments.
    Prefer supported academic families; diversify universities and family areas.
    Keep tied scores tied in metadata rather than inventing percentage matches.
    """
    catalogue_rows = load_current_catalogue() if catalogue_rows is None else catalogue_rows
    review_hints = load_review_suggestions() if review_hints is None else review_hints
    scores = scoring_result.get("core_family_scores", {})
    order = scoring_result.get("core_family_order") or sorted(scores, key=lambda f: (-scores[f],f))
    positive = [f for f in order if scores.get(f,0)>0]
    if not positive or limit <= 0:
        return []
    direct_signals = set(scoring_result.get("eligible_discipline_signals", []))
    candidates = []
    for row in catalogue_rows:
        if row.get("Record Type") not in PRIMARY_TYPES: continue
        title = row.get("Programme / Major","").strip()
        if not title: continue
        categories = {x.strip() for x in row.get("Discovery Areas (PROVISIONAL)","").split(";") if x.strip()}
        matched = [f for f in positive if categories & FAMILY_AREAS.get(f,set())]
        hints = review_hints.get(row.get("Record ID"),set())
        direct = sorted(direct_signals & hints)
        if not matched: continue
        primary_family = matched[0]
        main_score = scores[primary_family]
        candidates.append({
            "programme_id":row.get("Record ID"),"programme_title":title,
            "university":row.get("University"),"record_type":row.get("Record Type"),
            "admission_pathway":row.get("Parent Degree / Pathway"),
            "family_id":primary_family,"family_score":main_score,
            "direct_discipline_signals":direct,
            "source_url":row.get("Source URL"),
            "source_verification_note":row.get("Verification Status"),
            "display_status":"prototype_catalogue_match",
            "match_basis":"direct_discipline_hint" if direct else "broad_academic_family",
            "why_this_fits_basis":{
                "academic_family":primary_family,
                "independent_core_questions":main_score,
                "supporting_question_ids":sorted(set().union(*(set(scoring_result.get("core_evidence", {}).get(signal, [])) for signal in scoring_result.get("core_evidence", {}) if signal in FAMILY_SIGNALS.get(primary_family,set())))),
                "direct_discipline_hints":direct,
                "claim_strength":"exploratory_not_verified"
            },
            "_matched":len(matched),
        })
    # Rank interest strength first; direct evidence only resolves competition
    # among candidates associated with equally supported core families.
    candidates.sort(key=lambda r:(-r["family_score"],-bool(r["direct_discipline_signals"]),
                                  -r["_matched"],r["university"],r["programme_title"].casefold()))
    selected=[]
    used_ids=set()
    university_count={}
    family_count={}
    while len(selected)<limit:
        remaining=[r for r in candidates if r["programme_id"] not in used_ids]
        if not remaining: break
        highest=max(r["family_score"] for r in remaining)
        tier=[r for r in remaining if r["family_score"]==highest]
        tier.sort(key=lambda r:(
            -bool(r["direct_discipline_signals"]),
            family_count.get(r["family_id"],0),
            university_count.get(r["university"],0),
            -r["_matched"],
            r["university"],r["programme_title"].casefold(),r["programme_id"]))
        picked=tier[0]
        selected.append(picked)
        used_ids.add(picked["programme_id"])
        family_count[picked["family_id"]]=family_count.get(picked["family_id"],0)+1
        university_count[picked["university"]]=university_count.get(picked["university"],0)+1
    for r in selected:
        r.pop("_matched",None)
        r["family_tied_with"]=[f for f in positive if f!=r["family_id"] and scores[f]==r["family_score"]]
    return selected

def explore_other_opportunities(catalogue_rows=None, limit=100):
    """Second majors, minors and other offerings remain explorable, not core top matches."""
    rows = load_current_catalogue() if catalogue_rows is None else catalogue_rows
    return [{"programme_id":r.get("Record ID"),"university":r.get("University"),
             "programme_title":r.get("Programme / Major"),"record_type":r.get("Record Type"),
             "source_url":r.get("Source URL"),"display_status":"additional_opportunity"}
            for r in rows if r.get("Record Type") not in PRIMARY_TYPES][:limit]

def recommendation_report(scoring_result, catalogue_rows=None, review_hints=None, limit=5):
    """Result format for a future UI: explicit family ties and honest specificity.

    Family scores come only from student answers; the number of catalogue records
    never contributes to the score. A broad catalogue association is not evidence
    for that *individual* degree. Specific results require independent direct hints.
    """
    scores=scoring_result.get("core_family_scores",{})
    positive=[(f,v) for f,v in scores.items() if v>0]
    positive.sort(key=lambda x:(-x[1],x[0]))
    groups=[]
    for value in sorted({v for _,v in positive},reverse=True):
        families=[f for f,v in positive if v==value]
        groups.append({"evidence_count":value,"families":families,"is_tie":len(families)>1})
    matches=shortlist(scoring_result,catalogue_rows,review_hints,limit)
    for m in matches:
        if m["direct_discipline_signals"]:
            m["recommendation_level"]="specific_candidate"
            m["why_this_fits"]="Your answers support the {} academic area. Additional responses support exploring {}. This is an interest-based suggestion, not an admissions assessment.".format(
                m["family_id"].replace("_"," "),", ".join(x.replace("_"," ") for x in m["direct_discipline_signals"]))
        else:
            m["recommendation_level"]="family_exploration"
            m["why_this_fits"]="Your answers show interest in {}. This programme belongs to a related discovery area, but your answers do not yet distinguish it from other programmes in that area.".format(
                m["family_id"].replace("_"," "))
        m["why_this_fits_basis"]["supporting_question_ids"]=m["why_this_fits_basis"].get("supporting_question_ids",[])
    return {"status":"explore_more" if not positive else "ready",
            "core_family_groups":groups,"top_matches":matches,
            "note":"Tied academic families are equally supported. Catalogue links and programme routes have not all been independently verified."}

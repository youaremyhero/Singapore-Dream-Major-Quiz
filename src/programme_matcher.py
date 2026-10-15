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
    """Display prototype matches without treating unreviewed records as verified.

    Family ordering comes only from the core questionnaire. Optional Dive Deeper
    can expose specialist matches but does not replace the original family scores.
    """
    catalogue_rows = load_current_catalogue() if catalogue_rows is None else catalogue_rows
    review_hints = load_review_suggestions() if review_hints is None else review_hints
    scores = scoring_result.get("core_family_scores", {})
    order = scoring_result.get("core_family_order") or sorted(scores, key=lambda f: -scores[f])
    signals = set(scoring_result.get("eligible_discipline_signals", []))
    candidates = []
    for row in catalogue_rows:
        if row.get("Record Type") not in PRIMARY_TYPES:
            continue
        title = row.get("Programme / Major", "").strip()
        if not title:
            continue
        categories = {x.strip() for x in row.get("Discovery Areas (PROVISIONAL)", "").split(";") if x.strip()}
        matches = [f for f in order if categories & FAMILY_AREAS.get(f,set()) and scores.get(f,0)>0]
        suggested = review_hints.get(row.get("Record ID"),set())
        direct = sorted(signals & suggested)
        if not matches and not direct:
            continue
        family = matches[0] if matches else None
        family_score = scores.get(family,0) if family else 0
        candidates.append({
            "programme_id":row.get("Record ID"), "programme_title":title,
            "university":row.get("University"), "record_type":row.get("Record Type"),
            "admission_pathway":row.get("Parent Degree / Pathway"),
            "family_id":family,"direct_discipline_signals":direct,
            "source_url":row.get("Source URL"),
            "source_verification_note":row.get("Verification Status"),
            "display_status":"prototype_catalogue_match",
            "match_basis":"direct_discipline_hint" if direct else "broad_academic_family",
            "_rank":(1 if direct else 0,family_score,len(matches)),
        })
    # Stable ordering without using catalogue size to alter core interest scores.
    candidates.sort(key=lambda r:(-r["_rank"][0],-r["_rank"][1],-r["_rank"][2],
                                  r["programme_title"].casefold(),r["university"]))
    for r in candidates: r.pop("_rank")
    return candidates[:limit]

def explore_other_opportunities(catalogue_rows=None, limit=100):
    """Second majors, minors and other offerings remain explorable, not core top matches."""
    rows = load_current_catalogue() if catalogue_rows is None else catalogue_rows
    return [{"programme_id":r.get("Record ID"),"university":r.get("University"),
             "programme_title":r.get("Programme / Major"),"record_type":r.get("Record Type"),
             "source_url":r.get("Source URL"),"display_status":"additional_opportunity"}
            for r in rows if r.get("Record Type") not in PRIMARY_TYPES][:limit]

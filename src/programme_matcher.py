"""Conservative recommendations: ONLY approved mappings may be ranked."""
import csv
from pathlib import Path

def load_approved(path):
    with open(path,encoding="utf-8",newline="") as fh:
        rows=list(csv.DictReader(fh))
    required={"record_id","programme_id","university","programme_title","record_type","discipline_id","family_id","official_url","reviewer","approved_on"}
    if rows and not required.issubset(rows[0]): raise ValueError("Missing mapping columns")
    for r in rows:
        if any(not r[k].strip() for k in required): raise ValueError("Approved mapping lacks required review data")
        if not r["official_url"].startswith("https://"): raise ValueError("Official URL required")
        if r["record_type"] not in {"Primary major","Undergraduate degree / programme","Named degree or business major pathway","Cross-disciplinary degree"}: raise ValueError("Not primary programme")
    return rows

def shortlist(scoring_result, approved_rows):
    # Candidates can only come from independently supported discipline evidence.
    eligible=set(scoring_result.get("eligible_discipline_signals", []))
    return [{"programme_id":r["programme_id"],"programme_title":r["programme_title"],
             "university":r["university"],"discipline_id":r["discipline_id"],
             "official_url":r["official_url"],"display_status":"reviewed_candidate_not_ranked"}
            for r in approved_rows if r["discipline_id"] in eligible]

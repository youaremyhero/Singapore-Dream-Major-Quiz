"""Conservative title-level discipline mappings for the *current working catalogue*.

Editorial classification, not university verification. Only narrow programme names
are mapped. Broad admissions choices and combined degrees need separate review.
"""
import re

# Case-insensitive patterns anchored to whole programme title or the named
# specialisation of an explicit degree. This avoids arbitrary keyword substring
# promotions (e.g. 'security' in 'public safety and security').
RULES = [
 ("information_security", r"(information security|information and communications technology \(information security\))"),
 ("software_development", r"(software engineering|information and communications technology \(software engineering\))"),
 ("artificial_intelligence", r"(artificial intelligence|applied artificial intelligence|design and artificial intelligence)"),
 ("data_science", r"(data science and applied ai|data science and artificial intelligence|data science and economics)"),
 ("civil_engineering", r"(civil engineering)"),
 ("mechanical_engineering", r"(mechanical engineering)"),
 ("environmental_engineering", r"(environmental engineering)"),
 ("rehabilitation", r"(physiotherapy|occupational therapy)"),
 ("patient_care", r"(nursing|nursing \(pre-registration and specialty training\))"),
 ("biomedical_research", r"(biomedical science|biomedical sciences)"),
 ("physics", r"(physics|physics and applied physics)"),
 ("chemistry", r"(chemistry|chemistry and biological chemistry)"),
 ("economics", r"(economics|bachelor of science \(economics\))"),
 ("accounting", r"(accountancy|bachelor of accountancy)"),
 ("psychology", r"(psychology|bachelor of science in psychology)"),
 ("history", r"(history)"),
 ("literature", r"(english literature|literature)"),
 ("law", r"(law|bachelor of laws)"),
]
COMPILED = [(discipline,re.compile(r"^(?:"+pattern+r")$",re.I)) for discipline,pattern in RULES]

def infer_discipline(row):
    """None when title is too broad, interdisciplinary or ambiguous."""
    title=(row.get("Programme / Major") or "").strip()
    hits=[name for name,pattern in COMPILED if pattern.fullmatch(title)]
    return hits[0] if len(hits)==1 else None

def coverage_summary(rows,primary_types):
    primary=[r for r in rows if r.get("Record Type") in primary_types]
    mapped=[r for r in primary if infer_discipline(r)]
    return {"primary_records":len(primary),"narrowly_mapped_records":len(mapped),
            "unmapped_records":len(primary)-len(mapped)}

# Singapore Dream Major Quiz — New project starter

**Status: offline research prototype, not a live or official university admissions service.**

A new, standalone project for Singapore pre-university students to explore undergraduate academic fields and programmes across NUS, NTU, SMU, SUTD, SIT and SUSS. **Not affiliated with or endorsed by these universities.**

## Product decisions
- 20 core questions across three mixed-format chapters (7 + 6 + 7).
- Retain Top Qualities, Top Matches, Why This Fits, Explore Similar Majors conceptually; no existing-site design copied into this starter.
- Optional Dive Deeper for specialised programmes, without rewriting core family scores.
- University-neutral discipline scoring; strict family/specific-major distinction.
- Octopus experience and UI are future work; no AI API is needed at runtime.
- No QS rankings in suitability scores.

## Important data limitation
The 375 catalogue records are provisional, mixed types (including minors and admission choices), unevenly verified, and **not 375 directly available degrees**. `mapping_review_queue.csv` has machine-generated *suggestions*, not approvals. The approved ledger is intentionally empty. **The current 375-record catalogue is nonetheless ENABLED as the project's working list**, by project decision, to provide useful initial recommendations. Matches show their source verification notes and are explicitly labelled prototype matches; they are not independently confirmed admissions offerings.

## Files
- `data/questions.json` — selected twenty core question definitions.
- `data/dive_deeper.json` — optional question bank (older metadata may mention 12Q; only follow-ups applicable).
- `data/programmes_provisional.csv` — unverified six-AU catalogue, for research only.
- `data/mapping_review_queue.csv` — review triage; never directly use for rankings.
- `data/approved_programme_mappings.csv` — empty, approved records only.
- `src/engine.py` — exploratory evidence collection and conservative specialty gate.
- `src/programme_matcher.py` — enables working-catalogue prototype matching, keeps minors and second majors out of primary top matches, and retains source caveats.
- `tests/test_safeguards.py` — reproducible structural/safety checks.

## Tests
Run from the project root:
```bash
python -m unittest discover -s tests -p 'test_safeguards.py' -v
```
No external Python dependencies. Tests are structural; they do not establish recommendation accuracy.

## Development roadmap
1. Use the current six-AU catalogue as the working discovery list; refine programme title, degree/admission pathways, discipline ID and source links iteratively.
2. Resolve weak evidence (patient care vs rehab, cyber vs software, environment overlap) using answer evidence, not popularity.
3. Test top-five programme shortlist against diverse synthetic then real student responses.
4. Build accessible 20-question, 3-chapter standalone front end and optional Dive Deeper.
5. Implement yearly catalogue refresh workflow with change review.

## GitHub
Create a **new repository** such as `Singapore-Dream-Major-Quiz` and upload these files. Do not push to the existing `NUS-Dream-Major` repository. Suggest starting private while the catalogue is being verified, then publishing when ready.

## Working-catalogue policy (October 2026)
The existing provisional programme records are **included in prototype recommendations now**, as requested by the project owner. `shortlist()` selects eligible primary record types using university-neutral family scores and optional direct discipline hints. Named programme suggestions are exploratory rather than admission advice. The original source verification status is retained for display; neither a guessed programme-level URL nor a verified entry route is inferred from an index page. Minors and second majors are explored separately. The scoring framework is exploratory and unvalidated on real students.

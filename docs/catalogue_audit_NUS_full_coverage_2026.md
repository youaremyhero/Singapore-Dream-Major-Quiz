# NUS catalogue — full record coverage and remaining verification, 20 October 2026

## Scope and status

**Inventory reconciliation completed for all 256 current NUS working-catalogue records (NUS-0001 through NUS-0256). Detailed programme-link verification is NOT complete.** This distinction is important. The source-list match is not proof of every programme's current cohort eligibility.

Primary cross-reference file: `data/official_audit/NUS_full_record_reconciliation_2026.csv`.

Statuses across the 256 records:
- 54: AY2026/27 academic Bulletin listing established; **individual detail URL / exact admissions/cohort route pending**.
- 145: Registrar second-major/minor index listing established; **faculty detail page and current-cohort applicability pending**.
- 10: supplemented/current through specific official departmental evidence.
- 11: official OAM programme choice that is **itself a primary degree and valid main quiz recommendation**.
- 9: admission-pathway-only records, not independently scored as subject majors.
- 1: computer engineering shared SoC / CDE application record.
- 1: Computer Engineering duplicate to suppress in display.
- 12: historical language-track entries hidden in favour of one Language Studies minor.
- 2: current independently validated entries (Geospatial Intelligence and Music).
- 1: Criminal Justice minor effective from Semester 2 AY2026/27, not treated as generally active earlier.
- 10: double-degree combinations reserved for Explore More pending exact programme and eligibility verification.

## Applied source policies
- Official school and faculty pages take precedence over inconsistent central Registrar lists. Conflicts retained in notes.
- Primary majors/degree entries can be recommended; application-choice parent rows cannot manufacture standalone academic majors.
- NUS Music represented as **one Bachelor of Music (Honours)** primary recommendation (new catalogue ID NUS-0256).
- Computer Engineering represented **once**, with SoC / CDE joint school.
- Language Studies minor represented once as NUS-0255; 12 individual language tracks archived.
- FASS China Studies minor: discontinued for Cohort 2026 and later. NUS College China Studies remains unverified, excluded pending confirmation.
- Physics in Technology minor: older cohorts only, exclude from new student catalogue.
- Double degrees and special tracks belong in Explore More; other AUs' minors excluded.
- The NUS 2026/27 OAM page is an authoritative admission-choice index, not an independent degree record list.

## Official baseline sources
- NUS OAM: https://www.nus.edu.sg/oam/undergraduate-programmes
- NUS AY2026/27 Bulletin: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/
- NUS Registrar second majors: https://www.nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/double-major-programmes
- NUS Registrar minors: https://www.nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/minor-programmes
- FASS undergraduate list: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/faculty-of-arts-and-social-sciences/undergraduate-education/
- Science undergraduate list: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/faculty-of-science/undergraduate-education/
- CDE undergraduate list: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/college-of-design-and-engineering/undergraduate-education/
- Business undergraduate list: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/school-of-business/undergraduate-education/
- Music undergraduate degree: https://www.nus.edu.sg/nusbulletin/ay202627/programmes/yong-siew-toh-conservatory-of-music/undergraduate-education/

## Outstanding verification issues — do not silently resolve
1. **199 source-list-only entries need direct programme-page links and, where applicable, current cohort and eligibility verification.** University listing-level source URLs should not be presented as programme-specific details.
2. **Ten double-degree combination records are generic or broad descriptions**, not necessarily exact current direct-entry routes. Keep in internal ledger / Explore More pending an official per-combination check.
3. **Registrar second majors count vs OAM promotional count:** our earlier Registrar transcription has 52 lines whereas OAM promotes 54 second majors. Grouping, cohorts and host duplication complicate reconciliation. Do not claim either figure is the total number of eligible student-facing programmes without an exact comparison.
4. **NUS College China Studies minor** remains separately indexed while FASS discontinued its minor for Cohort 2026 onwards. Pending direct NUS College evidence, exclude both new-student display entries.
5. **Data Science and Applied AI vs Data Science and Analytics:** Faculty of Science AY2026/27 Bulletin uses inconsistent labels; check the host department's current programme title and cohort-specific degree award.
6. **Minor Criminal Justice** has Semester 2 AY2026/27 effective date: prevent pre-effective-date misrepresentation.
7. **Some active degrees are stored as OAM admission-choice records** for historical data-model reasons. Student-facing export must treat the 11 verified direct degree choices as main recommendation programmes, rather than excluding all `OAM admission choice` records indiscriminately.
8. **Degree-count completeness:** an audit of existing 256 entries does not prove every newly introduced NUS programme is represented. Check admissions choices and faculty current prospectuses again before declaring full NUS inventory complete.
9. **Main quiz code does not yet implement all status/visibility rules.** Catalogue records and audit ledger have been updated, but runtime suppression needs a separate implementation and testing phase.

## Release rule
Do not mark this NUS dataset fully verified or ready for unrestricted use in the quiz until the above source and eligibility checks are closed. Never fill in a guessed URL, rename or status to improve completeness figures. Do not modify original `youaremyhero/NUS-Dream-Major` repo.

## Next work
Continue per-programme links and cohort verification from the 199 flagged rows in the master ledger, then reconcile the 10 double degrees and check for previously omitted 2026 majors. Present unresolved policy questions together at the end, and only then proceed to NTU.

## Final unmatched-name review
The main catalogue has **54 second-major rows and 114 minor rows**, but their totals are **not independently validated current programme counts**. An exact-name comparison against the Registrar audit yields:
- Second-major differences: Chinese Languages and Cultures, Chinese Studies (Bilingual), Environmental Science for Sustainability, Forensic Science, Marine and Freshwater Ecology. These are supported by official departmental evidence from earlier NUS batches; do **not** delete because of absent exact Registrar wording.
- Minor differences: two current Chinese cohort names, twelve archived language tracks (suppressed), and Multilingual Communication (separately supported by CLS). This explains the working-list differences without inventing programme discontinuations.
- The official Registrar names Chinese Language and Chinese Studies in places where FASS shows newer cohort names. Faculty cohort data takes precedence.
- Catalogue row counts include archive tracks, OAM application choices and double degrees. Do not compare the raw catalogue count directly with NUS publicity totals.

## Checks completed
- Main NUS catalogue contains 256 distinct NUS IDs, all 15 expected CSV columns per row.
- The record-level audit ledger contains the same 256 distinct IDs, with none missing.
- Primary Music degree was missing; added NUS-0256 (one Music entry).
- No scoring/frontend files modified.

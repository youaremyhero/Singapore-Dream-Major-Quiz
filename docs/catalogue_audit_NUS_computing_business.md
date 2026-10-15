# NUS Catalogue Audit — Computing and Business (AY2026/27)

Completed 15 October 2026. This is an **official-source audit snapshot**, not a replacement for the working catalogue.

## Official evidence
- [NUS School of Computing AY2026/27 Bulletin](https://www.nus.edu.sg/nusbulletin/ay202627/programmes/school-of-computing/undergraduate-education/) identifies six undergraduate degrees (five Computing School programmes and jointly offered Computer Engineering).
- [NUS Business School AY2026/27 Bulletin](https://www.nus.edu.sg/nusbulletin/ay202627/programmes/school-of-business/undergraduate-education/) identifies three Bachelor of Business Administration honours degree labels.
- [NUS BBA AY2026/27 curriculum](https://bba.nus.edu.sg/curriculum-ay2026-2027-onwards/) specifies the nine BBA major tracks.
- [NUS Office of Admissions undergraduate programmes](https://nus.edu.sg/oam/undergraduate-programmes) differentiates Computing admission choices (including Common Computer Science Programmes) from constituent degrees and lists Business Administration as the Business admission choice.

## Important reconciliation outcomes
1. **Artificial Intelligence and Computer Science** are separate undergraduate degree programmes, but both are presented under the OAM **Common Computer Science Programmes** choice. Preserve both degree entries linked to the shared OAM pathway, not as invented standalone admissions choices.
2. **Computer Engineering** is jointly offered with CDE. Existing NUS-0148 and NUS-0157 both describe an OAM Computer Engineering choice. These must be checked and reconciled into a single canonical programme/admission pathway with shared offering schools, not represented as two unrelated degrees.
3. **Business Artificial Intelligence Systems** is explicitly described by OAM as formerly known as Information Systems; keep the former name as an alias, not a second current degree.
4. **Business** has three degree labels in the Bulletin, while its AY2026/27 curriculum identifies nine major tracks. These are different entities; do not create nine distinct direct OAM choices.
5. Computing Bulletin mentions a **Computer Science – Turing Programme** as a special programme within Computer Science. Do not promote it into another standard degree without further official entry/eligibility verification.

## Verified output
`data/official_audit/NUS_Computing_Business_AY2026_27.csv` — six SoC/joint degrees, three BBA degree labels, nine BBA majors. All named URLs lead to official NUS-controlled sites. Blank programme-specific URLs signify that a direct page has **not** been verified. The school Bulletin and curriculum links are supporting sources, not guarantees of direct admissions pathways.

## Pending decisions from project owner
- Should student-facing results display the **specific academic major first**, followed by the actual **application pathway** (recommended), or show just the admission-choice name until the student opens the card?
- Should **double degrees and limited-entry special tracks** be part of the separate Explore More library, or omitted during the first release? They should not inflate primary match rankings.

## Still to review
FASS and the remaining NUS schools, NUS second majors and minors, record-level URLs and cohort restrictions. NTU, SMU, SUTD, SIT and SUSS not yet audited.

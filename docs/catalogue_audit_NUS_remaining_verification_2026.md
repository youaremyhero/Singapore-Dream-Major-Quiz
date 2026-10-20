# NUS official catalogue — reconciliation status and outstanding decisions (20 October 2026)

This is a truthful *interim* verification status, not a declaration that all NUS programme links are individually verified. University-controlled sources only.

## Integrity check
- Working NUS catalogue: **257 unique records** (NUS-0001 through NUS-0257), all 15-column CSV rows.
- NUS reconciliation ledger: **257 matching records**, no missing IDs.
- Academic first-majors, admissions choices, second majors, minors, double-degree records, and one Music degree are not equivalent counts of unique degree awards.

## Evidence state (257)
- 75 official individual faculty/programme detail pages.
- 77 names on current official faculty supplementary indexes, but direct per-programme pages remain pending.
- 37 names currently supported at official Registrar index level only; departmental confirmation/direct links remain pending.
- 9 BBA majors verified on one official AY2026/27 curriculum page.
- 11 direct-entry programme records verified on official OAM/host pages.
- Remaining records: 8 other supplementary confirmed; 1 restricted MBBS minor; 1 other restricted current minor; 2 current independently validated programmes; 1 future-effective minor; 12 language tracks hidden; 9 pathway-only records; 1 shared Computer Engineering record; 1 duplicate Computer Engineering suppressed; 2 historical Business supplements hidden; 10 double degrees reserved for Explore More pending application-route check.
- **The quiz UI / scoring engine has not been updated** to enforce these decisions. Do not claim runtime filtering complete.

## New verifications in this continuation
1. Six current NUS Conservatory secondary programme links were updated to YST programme and admissions pages. Continue showing only one primary Music degree; second majors/minors are supplementary.
2. Official FASS discovery list confirms 21 second majors and its current named minor options. Faculty evidence assigned to the matching 38 previously Registrar-only minor records, and 18 previously Registrar-only second-major records.
3. Faculty of Science's cohort-specific second-major/minor list is the official faculty listing source for 21 previously Registrar-only records.
4. The ten existing double-degree rows are divided into 7 named combinations and 3 grouped umbrella descriptions. These are not automatically direct-application choices and remain Explore More only. File: `data/official_audit/NUS_double_degree_exactness_2026.csv`.
5. NUS Medicine confirms the **Biomedical Informatics minor is currently only open to MBBS students**; NUS-0239 is marked restricted, with a department link.
6. Current FASS offers individual language-named minors while CLS supports the umbrella **Language Studies** minor. Under the owner's presentation decision, show *Language Studies* once, and preserve language names internally; record the difference for final discussion.
7. Official NUS AY2026/27 registrar overview, faculty cohort details and admissions FAQ need not have identical groupings or older cohort labels. Prioritise host faculty where contemporary evidence differs.

## Exact official sources
- FASS second majors and minors: https://fass.nus.edu.sg/discover/second-majors-minors/
- Science second majors and minors: https://www.science.nus.edu.sg/undergraduates/academic-programmes/second-majors-and-minors/
- NUS double degrees: https://www.nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/double-degree-programmes
- NUS double-degree admissions FAQ: https://nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/faqs-for-ddp-cdp-and-dmp
- YST secondary offerings: https://www.ystmusic.nus.edu.sg/programmes-electives-minors-second-majors-for-nus-students-second-majors/
- YST minors: https://www.ystmusic.nus.edu.sg/programmes-electives-minors-second-majors-for-nus-students-minors/
- Biomedical Informatics minor: https://medicine.nus.edu.sg/dbmi/education-3/minor-in-biomedical-informatics/

## Pending for NUS final sign-off
- Validate remaining 37 Registrar-index-only records on host school pages (principally CDE, Computing, Medicine, Business and community programmes).
- For 77 faculty-index-listed offerings, verify individual detail pages where a distinct page exists, and their eligibility where this matters. An *official faculty-level index URL* is a legitimate fallback but should be labelled as such, never disguised as a specific programme page.
- Resolve whether the 7 historical NUS Music second-major labels in our working file correspond to currently selectable secondary programmes; YST's current page principally names 4 second-major streams and lists instrumental pathways under the BMus. Historical second-major labels should not surface as current without dedicated source confirmation.
- Resolve the NUS College China Studies minor status without assuming it is the discontinued FASS programme; existing conservative exclusion applies.
- Check 2026 direct-entry status of all double-degree combinations, especially the Registrar's historical **Information Systems** wording.
- Consider the FASS-versus-CLS language-minor **classification** conflict only at final user clarification; do not override the user's decision.
- Validate the 2026 freshman programme admissions list against canonical programme entries for omissions.
- After official inventory sign-off, implement and test student-facing availability filter across sources; not part of this source-audit task.

## Non-negotiable rules
Faculty/department current pages take precedence over conflicting Registrar pages; legacy cohorts in archival metadata; no unsupported claims; minor entries only for NUS (none for other AUs); the original NUS-Dream-Major repository remains untouched.

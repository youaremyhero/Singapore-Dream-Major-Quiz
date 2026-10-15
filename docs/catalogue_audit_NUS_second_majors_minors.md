# NUS second-major and minor reconciliation — official Registrar audit

Review date: 2026-10-15. **NUS only**. University sources only.

## Sources
- Second majors: https://www.nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/double-major-programmes
- Minors: https://www.nus.edu.sg/registrar/academic-information-policies/undergraduate-students/special-programmes/minor-programmes

## Committed audit files
- `data/official_audit/NUS_second_majors_registrar_2026.csv` — earlier 52-row initial listing, includes music group labels; do not construe its count as total current majors.
- `data/official_audit/NUS_minors_registrar_2026_27.csv` — 99 distinct index-listed names, deduplicating jointly hosted programmes like Data Engineering and Interactive Media Development. Retains Open / Restricted classification, cohort notes and official Registrar listing URLs.
- `data/official_audit/NUS_second_major_minor_reconciliation_queue.csv` — 171 reconciliation rows combining the two lists with existing NUS catalogue IDs. 142 matched exact normalized names, 9 source-list entries lack exact old names, 20 old records lack exact matches; these are **review flags, not demonstrated deletions**.

## Important qualifications
- Minors listed on the Registrar page include **Criminal Justice** (effective Semester 2 AY2026/27) and **Human-AI Systems** (AY2026/27). The former is not yet assumed currently available at the October 2026 audit date; status is `not_yet_effective` in our file.
- The index includes **Chinese Language** and **Chinese Studies**, but the contemporary cohort's primary majors were renamed/reorganised. Do not infer that all corresponding *minors* have the same new titles; check department-level pages before renaming.
- The second-major index still includes **Civil Infrastructure** specifically for cohorts AY2019/20 and AY2020/21. Preserve history, do not offer to new pre-university students.
- NUS music is **one primary Music degree** in quiz results. Any music-related second major/minor is supplementary and not a separate Music primary recommendation.
- Registrar links here are **official listing URLs**. A unique direct detail page has NOT yet been verified for every individual offering. Do not label them as per-programme links.

## Matching problems to resolve
1. Names not matching exactly can be true programme additions, renamed titles or different cohort labels. Inspect official department pages before categorising.
2. Some 113 old NUS minor catalogue rows may be legacy/duplicates or simply different labels; 99 current Registrar index entries should not trigger automatic deletion.
3. Jointly offered subjects must be one student-facing record, not multiple because host schools list them independently.
4. Restricted offerings require approval; do not imply every NUS student can declare them freely.
5. Main recommendation priorities remain degrees and first majors; second majors and NUS minors are separately browsable additional opportunities.

## Next concrete step
Review the 29 flagged reconciliation rows, in order: new effective AY2026/27 offerings; cohort-specific names; current direct university pages; potential duplicate records. Then merge vetted updates into the canonical working catalogue, keeping stable IDs and archival notes. For NTU/SMU/SUTD/SUSS/SIT, **do not collect minors**.

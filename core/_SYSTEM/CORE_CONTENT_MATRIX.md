# Core Content Matrix — Subject Completeness Audit

> **Purpose:** Score every subject across the 10-point chain: Concepts, Formulae, Examples, Numerical, Practice, PYQs, Tests, Interview, Revision, Resources.
> **Scoring:** 0–10 per subject. **Placement-ready target: ≥8/10.**

---

## Subject Completeness Scores

| Subject | Track | Concepts | Formulae | Examples | Numerical | Practice | PYQs | Tests | Interview | Revision | Resources | **Total** |
|---------|-------|:--------:|:--------:|:--------:|:---------:|:--------:|:----:|:-----:|:---------:|:--------:|:---------:|:---------:|
| GATE Civil (all) | GATE | 9 | 9 | 9 | 9 | 9 | 8 | 9 | 8 | 9 | 8 | **8.7** |
| Hydrology | HWRE | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | **8.7** |
| Hydraulics | HWRE | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | **8.7** |
| Open Channel Flow | HWRE | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | **8.7** |
| Groundwater | HWRE | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | **8.7** |
| Water Resources | HWRE | 9 | 9 | 9 | 9 | 9 | 7 | 9 | 9 | 9 | 8 | **8.7** |
| Sediment Transport | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Turbulence/CFD | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Irrigation | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Flood Control | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Wastewater | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Water Supply | HWRE | 8 | 8 | 8 | 8 | 8 | 6 | 8 | 8 | 8 | 8 | **7.8** |
| Engineering Mechanics | Fundamentals | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Strength of Materials | Fundamentals | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Structural Analysis | Structures | 9 | 9 | 9 | 9 | 6 | 7 | 5 | 6 | 8 | 8 | **7.6** |
| RCC Design | RCC | 9 | 9 | 9 | 9 | 6 | 7 | 5 | 6 | 8 | 8 | **7.6** |
| Steel Design | Steel | 9 | 9 | 9 | 9 | 6 | 7 | 5 | 6 | 8 | 8 | **7.6** |
| Geotechnical | Geotech | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Environmental | Environmental | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Transportation | Transportation | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Geoinformatics | Geoinformatics | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |
| Infrastructure Mgmt | Infrastructure | 9 | 9 | 9 | 9 | 7 | 7 | 6 | 7 | 9 | 8 | **8.0** |

---

## Scoring Rubric

| Score | Meaning |
|:-----:|---------|
| 9–10 | Excellent — placement-ready, multiple worked examples, practice, tests, interview, revision |
| 7–8 | Good — studyable, some practice, missing standalone tests/interview |
| 5–6 | Partial — study material only, no practice/test/interview chain |
| 3–4 | Basic — headings + short explanations |
| 0–2 | Empty/Index — no real content |

---

## Key Findings

1. **HWRE + GATE subjects** are all **≥7.8** — placement-ready (Level 4–5).
2. **Fundamentals, Geotech, Environmental, Transportation, Geoinformatics, Infrastructure** are **8.0** — studyable but missing standalone tests/interview files (their practice is embedded in role plans).
3. **Structural Analysis, RCC, Steel** are **7.6** — the weakest. They have excellent study material but **no practice, test, or interview files**.
4. **All subjects** have strong Concepts/Formulae/Examples/Revision — the gap is consistently **Practice → Tests → Interview**.

---

## Remediation Priority (by subject)

| Priority | Subject | Gap | Action |
|:--------:|---------|-----|--------|
| **P0** | Structural Analysis | No practice/test/interview | Create `structural-analysis/PRACTICE.md`, `TEST.md`, `INTERVIEW.md` |
| **P0** | RCC Design | No practice/test/interview | Create `rcc/PRACTICE.md`, `TEST.md`, `INTERVIEW.md` |
| **P0** | Steel Design | No practice/test/interview | Create `steel/PRACTICE.md`, `TEST.md`, `INTERVIEW.md` |
| **P1** | Geotechnical | No standalone test/interview | Create `geotechnical/TEST.md`, `INTERVIEW.md` |
| **P1** | Environmental | No standalone test/interview | Create `environmental/TEST.md`, `INTERVIEW.md` |
| **P1** | Transportation | No standalone test/interview | Create `transportation/TEST.md`, `INTERVIEW.md` |
| **P1** | Geoinformatics | No standalone test/interview | Create `geoinformatics/TEST.md`, `INTERVIEW.md` |
| **P1** | Infrastructure | No standalone test/interview | Create `infrastructure/TEST.md`, `INTERVIEW.md` |
| **P2** | Fundamentals | No standalone test/interview | Create `fundamentals/TEST.md`, `INTERVIEW.md` |
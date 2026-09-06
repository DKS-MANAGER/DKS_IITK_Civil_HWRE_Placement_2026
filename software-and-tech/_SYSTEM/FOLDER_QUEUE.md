# FOLDER_QUEUE.md — First-Pass Folder Queue for `software-and-tech/`

> **Purpose:** Ordered processing queue for the folder-by-folder audit + fix.
> **Rule:** Process strictly in queue order. Never partially modify multiple folders simultaneously.
> **Status legend:** `NOT STARTED` · `AUDITING` · `FIXING` · `VERIFYING` · `COMPLETE`

---

## Queue (Priority Order)

| # | Folder | Purpose | Target Role | Files | Status |
|:-:|:-------|:--------|:------------|:-----:|:-------|
| 01 | [`tools/`](../tools/) | Canonical P0/P1 tool pages (AutoCAD, Excel, ETABS, STAAD, QGIS, Primavera, Revit, SAP2000) | Structural, Construction, GIS, Water Resources, All | 8 | `COMPLETE` |
| 02 | [`deep-dives/`](../deep-dives/) | Hands-on step-by-step walkthroughs (HEC-RAS, HEC-HMS, SWMM, EPANET, PLAXIS, SLOPE/W, OpenFOAM) | Water Resources, Hydrology, Geotech, CFD | 8 | `COMPLETE` |
| 03 | [`programming/`](../programming/) | Programming languages (Python, MATLAB, SQL, C/C++, Git) | All roles, Research, Data, Tech | 6 | `COMPLETE` |
| 04 | [`structural/`](../structural/) | Structural engineering software roadmap | Structural Engineer, Consultant, BIM | 1 | `COMPLETE` |
| 05 | [`hwre/`](../hwre/) | HWRE / Hydraulics software roadmap | Water Resources Engineer | 1 | `COMPLETE` |
| 06 | [`geotechnical/`](../geotechnical/) | Geotechnical software roadmap | Geotechnical Engineer | 1 | `COMPLETE` |
| 07 | [`hydrology/`](../hydrology/) | Hydrology software roadmap | Hydrologist | 1 | `COMPLETE` |
| 08 | [`gis/`](../gis/) | GIS / Remote Sensing roadmap | GIS Engineer | 1 | `COMPLETE` |
| 09 | [`environmental/`](../environmental/) | Environmental engineering software | Environmental Engineer | 1 | `COMPLETE` |
| 10 | [`sediment/`](../sediment/) | Sediment / River engineering software | River Engineer | 1 | `COMPLETE` |
| 11 | [`transportation/`](../transportation/) | Transportation software roadmap | Transportation Engineer | 1 | `COMPLETE` |
| 12 | [`construction/`](../construction/) | Construction / PM software roadmap | Construction Engineer, PM | 1 | `COMPLETE` |
| 13 | [`bim/`](../bim/) | BIM software (Revit, Navisworks) | BIM Engineer | 3 | `COMPLETE` |
| 14 | [`cfd/`](../cfd/) | CFD / Computational roadmap | CFD Engineer | 1 | `COMPLETE` |
| 15 | [`research/`](../research/) | Research / M.Tech tech stack | Researcher | 1 | `COMPLETE` |
| 16 | [`data/`](../data/) | Data / Analytics stack | Data Analyst, BA | 1 | `COMPLETE` |
| 17 | [`consulting/`](../consulting/) | Consulting tech stack | Consultant | 1 | `COMPLETE` |
| 18 | [`product/`](../product/) | Product / PM tech stack | Product Analyst, PM | 1 | `COMPLETE` |
| 19 | [`operations/`](../operations/) | Operations / Supply Chain stack | Operations | 1 | `COMPLETE` |
| 20 | [`technology-careers/`](../technology-careers/) | Tech / software-adjacent careers | SWE-adjacent | 1 | `COMPLETE` |
| 21 | [`developer-tools/`](../developer-tools/) | Linux / shell / dev tools | Research, CFD | 1 | `COMPLETE` |
| 22 | [`computing/`](../computing/) | Cloud / HPC stack | Research, CFD | 1 | `COMPLETE` |
| 23 | [`automation/`](../automation/) | Python/MATLAB/Bash automation | All | 1 | `COMPLETE` |
| 24 | [`comparisons/`](../comparisons/) | Tool-vs-tool decision tables | All | 1 | `COMPLETE` |
| 25 | [`practice/`](../practice/) | Practice exercise system | All | 1 | `COMPLETE` |
| 26 | [`tests/`](../tests/) | Test / assessment system | All | 1 | `COMPLETE` |
| 27 | Top-level system files | Navigation, matrices, linkage, strategy | All | 18 | `COMPLETE` |

---

## Top-Level System Files (Processed Last)

| File | Purpose | Status |
|:-----|:--------|:-------|
| [`README.md`](../README.md) | System hub | `COMPLETE` |
| [`software-template.md`](../software-template.md) | Tool page template | `COMPLETE` |
| [`priority-system.md`](../priority-system.md) | L1–L4 proficiency levels | `COMPLETE` |
| [`role-roadmaps.md`](../role-roadmaps.md) | Role → tool map | `COMPLETE` |
| [`branch-roadmaps.md`](../branch-roadmaps.md) | Branch → tool map | `COMPLETE` |
| [`software-interview-questions.md`](../software-interview-questions.md) | Question bank | `COMPLETE` |
| [`resume-positioning.md`](../resume-positioning.md) | Resume strategy | `COMPLETE` |
| [`learning-roadmaps.md`](../learning-roadmaps.md) | Timeline plans | `COMPLETE` |
| [`anti-overload.md`](../anti-overload.md) | Strategy | `COMPLETE` |
| [`project-first-learning.md`](../project-first-learning.md) | Project strategy | `COMPLETE` |
| [`mtech-advantage.md`](../mtech-advantage.md) | Research path | `COMPLETE` |
| [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) | Role → tool matrix | `COMPLETE` |
| [`TOOLS_INDEX.md`](../TOOLS_INDEX.md) | Tool index | `COMPLETE` |
| [`SOFTWARE_ROADMAP.md`](../SOFTWARE_ROADMAP.md) | Learning roadmap | `COMPLETE` |
| [`SOFTWARE_COMPLETENESS_MATRIX.md`](../SOFTWARE_COMPLETENESS_MATRIX.md) | Readiness scores | `COMPLETE` |
| [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) | Resume strategy | `COMPLETE` |
| [`SOFTWARE_COMPANY_LINKAGE.md`](../SOFTWARE_COMPANY_LINKAGE.md) | Company → tool linkage | `COMPLETE` |
| [`SOFTWARE_THEORY_LINKAGE.md`](../SOFTWARE_THEORY_LINKAGE.md) | Theory → tool linkage | `COMPLETE` |

---

## Processing Rule

```
SELECT FOLDER → INVENTORY → AUDIT → IDENTIFY GAPS → FIX PLAN → FIX CONTENT
→ FIX NAVIGATION → VERIFY → SCORE → MARK COMPLETE → NEXT FOLDER
```

> **Last Updated:** 2026-09-06
> **Status:** ALL FOLDERS COMPLETE — cross-folder audit done, 825 links verified, 5/5 user journeys pass.
> **Next Folder:** None (all folders processed)
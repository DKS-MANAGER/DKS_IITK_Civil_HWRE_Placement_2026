# 🎯 Master Software Role Matrix (Canonical Decision Engine)

> **The single authoritative decision engine answering: "What software should I learn for my target role?"**
> Distinguishes empirical company evidence (`[VERIFIED]`, `[SOURCE-DERIVED]`, `[INFERRED]`) from repository preparation priorities (`[PREPARATION HEURISTIC]`: P0, P1, P2, P3).

---

## 1. Information Architecture: Canonical Decision Path

To prevent decision fatigue across multiple roadmap files, use this canonical hierarchy:

```
                      WHAT SOFTWARE SHOULD I LEARN?
                                    │
                                    ▼
                 ┌──────────────────────────────────────┐
                 │    SOFTWARE_ROLE_MATRIX.md           │  ◄── PRIMARY CANONICAL DECISION ENGINE
                 │    (This Document: Role + Tools)     │
                 └──────────────────┬───────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌──────────────┐            ┌──────────────┐            ┌──────────────┐
│  BY BRANCH   │            │ BY TIMELINE  │            │ ANTI-OVERLOAD│
│  DISCIPLINE  │            │ (7/30/90 d)  │            │ (1+1+1 RULE) │
│branch-road   │            │learning-road │            │anti-overload.│
│maps.md       │            │maps.md       │            │md            │
└──────────────┘            └──────────────┘            └──────────────┘
```

- **Specialized Supporting Views:**
  - Need a pure branch view? See [`branch-roadmaps.md`](branch-roadmaps.md).
  - Need a 7-day, 30-day, or 90-day plan? See [`learning-roadmaps.md`](learning-roadmaps.md) and [`SOFTWARE_ROADMAP.md`](SOFTWARE_ROADMAP.md).
  - Feeling overwhelmed? Read the Rule of 1+1+1 in [`anti-overload.md`](anti-overload.md).
  - Writing your resume? Follow [`SOFTWARE_RESUME_STRATEGY.md`](SOFTWARE_RESUME_STRATEGY.md).

---

## 2. Evidentiary Taxonomy & Priority Legend

- **Preparation Priority `[PREPARATION HEURISTIC]`:**
  - **P0 — Placement Required:** Essential screening or interview filter for this role.
  - **P1 — High Value:** Significant competitive advantage; commonly tested in technical rounds.
  - **P2 — Useful / Niche:** Situational advantage or secondary project capability.
  - **P3 — Optional:** Specialized tool; skip if preparation time is constrained.
- **Evidence Provenance Tag:**
  - `[VERIFIED]`: Confirmed by primary SPO placement job descriptions, company tests, or verified candidate debriefs.
  - `[SOURCE-DERIVED]`: Directly derived from industry-standard role requirements or consultancy specifications.
  - `[INFERRED]`: Reasoned from underlying engineering workflows and design code standards.

---

## 3. Core Civil & Computational Engineering Roles

### 3.1 Structural Design Engineer

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **AutoCAD** | L3 Proficient | [`tools/AutoCAD.md`](tools/AutoCAD.md) | `[VERIFIED]` L&T, SPECTRUM, Thornton Tomasetti, Hilti, ASC |
| **P0** | **STAAD.Pro** | L3 Proficient | [`tools/STAAD.md`](tools/STAAD.md) | `[VERIFIED]` L&T, SPECTRUM, ASC Infratech, BPCL |
| **P0** | **ETABS** | L3 Proficient | [`tools/ETABS.md`](tools/ETABS.md) | `[VERIFIED]` Thornton Tomasetti, SPECTRUM, Hilti, Smarttrak |
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` Universal requirement across all engineering firms |
| **P1** | **SAP2000** | L2–L3 Working | [`tools/SAP2000.md`](tools/SAP2000.md) | `[VERIFIED]` Thornton Tomasetti, Hilti, L&T |
| **P1** | **Revit (Structure)**| L2 Working | [`tools/Revit.md`](tools/Revit.md) | `[VERIFIED]` Thornton Tomasetti, Godrej Properties |
| **P2** | **Python** | L2 Basic | [`programming/python.md`](programming/python.md) | `[INFERRED]` Structural optimization and automated batch calculation |

---

### 3.2 Water Resources & Hydraulics (HWRE) Engineer

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **HEC-RAS** | L3 Proficient | [`deep-dives/hec-ras-walkthrough.md`](deep-dives/hec-ras-walkthrough.md) | `[VERIFIED]` Vassar Labs (explicit placement criteria) |
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` Universal hydrological calculations & data analysis |
| **P1** | **HEC-HMS** | L2–L3 Working | [`deep-dives/hec-hms-tutorial.md`](deep-dives/hec-hms-tutorial.md) | `[VERIFIED]` Vassar Labs, watershed modeling roles |
| **P1** | **QGIS / ArcGIS** | L2–L3 Working | [`tools/QGIS.md`](tools/QGIS.md) | `[VERIFIED]` Vassar Labs, GIST |
| **P1** | **Python** | L2–L3 Working | [`programming/python.md`](programming/python.md) | `[VERIFIED]` Vassar Labs, hydroinformatics roles |
| **P2** | **EPANET** | L2 Basic | [`deep-dives/epanet-walkthrough.md`](deep-dives/epanet-walkthrough.md) | `[SOURCE-DERIVED]` Rodic Consultants (water distribution networks) |

---

### 3.3 CFD & Fluid Dynamics Simulation Engineer

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **OpenFOAM** | L3 Proficient | [`deep-dives/openfoam-case-study.md`](deep-dives/openfoam-case-study.md) | `[SOURCE-DERIVED]` TuTr Hyperloop, AgniKul Cosmos, aerospace R&D |
| **P0** | **Python** | L3 Proficient | [`programming/python.md`](programming/python.md) | `[VERIFIED]` AgniKul, TuTr Hyperloop, automated meshing scripts |
| **P0** | **Linux / Shell** | L2–L3 Working | [`developer-tools/linux-dev-tools.md`](developer-tools/linux-dev-tools.md) | `[INFERRED]` Essential CFD cluster & HPC execution environment |
| **P1** | **ParaView** | L2–L3 Working | [`developer-tools/linux-dev-tools.md`](developer-tools/linux-dev-tools.md) | `[INFERRED]` Standard CFD post-processing and vector visualization |
| **P1** | **ANSYS / Fluent** | L2 Working | [`cfd/cfd-tech.md`](cfd/cfd-tech.md) | `[VERIFIED]` TuTr Hyperloop, Smarttrak AI |
| **P2** | **MATLAB** | L2 Basic | [`programming/matlab.md`](programming/matlab.md) | `[SOURCE-DERIVED]` Numerical discretization and matrix math |

---

### 3.4 Geotechnical Engineer

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **PLAXIS 2D** | L2–L3 Working | [`deep-dives/plaxis-2d-tutorial.md`](deep-dives/plaxis-2d-tutorial.md) | `[VERIFIED]` Reliance New Energy, geotechnical consultancy JDs |
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` Universal bearing capacity & settlement models |
| **P1** | **GeoStudio SLOPE/W**| L2 Working | [`deep-dives/geostudio-slopew-tutorial.md`](deep-dives/geostudio-slopew-tutorial.md) | `[SOURCE-DERIVED]` Reliance New Energy, embankment slope checks |
| **P1** | **AutoCAD** | L2 Working | [`tools/AutoCAD.md`](tools/AutoCAD.md) | `[INFERRED]` Soil profile and foundation drafting |
| **P2** | **QGIS** | L2 Basic | [`tools/QGIS.md`](tools/QGIS.md) | `[INFERRED]` Terrain and borehole spatial interpolation |

---

### 3.5 Construction Management & EPC Engineer

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **AutoCAD** | L3 Proficient | [`tools/AutoCAD.md`](tools/AutoCAD.md) | `[VERIFIED]` L&T, Godrej Properties, BPCL |
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` BOQ preparation, rate analysis, site billing |
| **P0** | **Primavera P6**| L2–L3 Working | [`tools/Primavera.md`](tools/Primavera.md) | `[VERIFIED]` L&T, Godrej, ITC, BPCL, HPCL |
| **P1** | **STAAD.Pro** | L2 Basic | [`tools/STAAD.md`](tools/STAAD.md) | `[VERIFIED]` L&T, BPCL |
| **P1** | **Revit (BIM)** | L2 Basic | [`tools/Revit.md`](tools/Revit.md) | `[SOURCE-DERIVED]` Godrej Properties, EPC site coordination |

---

## 4. Non-Core, Analytics & Technology-Adjacent Roles

### 4.1 Data Analyst

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` Axis Bank, Mu Sigma, EXL |
| **P0** | **SQL** | L3 Proficient | [`programming/sql.md`](programming/sql.md) | `[VERIFIED]` Accenture, Blitz, Battery Smart |
| **P0** | **Python** | L3 Proficient | [`programming/python.md`](programming/python.md) | `[VERIFIED]` Accenture, Barclays, Tiger Analytics |
| **P1** | **Power BI** | L2 Working | [`data/data-analytics-stack.md`](data/data-analytics-stack.md) | `[SOURCE-DERIVED]` Axis Bank, business intelligence teams |

---

### 4.2 Business Analyst & Management Consultant

| Priority `[PREPARATION HEURISTIC]` | Tool | Target Level | Canonical Study Source | Evidence Provenance & Visiting Companies |
|:---:|:---|:---:|:---|:---|
| **P0** | **Excel** | L3 Proficient | [`tools/Excel.md`](tools/Excel.md) | `[VERIFIED]` McKinsey, BCG, Bain, universal financial models |
| **P0** | **PowerPoint** | L3 Proficient | [`consulting/consulting-tech.md`](consulting/consulting-tech.md) | `[VERIFIED]` Executive presentations, MECE storyline decks |
| **P1** | **SQL** | L2 Working | [`programming/sql.md`](programming/sql.md) | `[SOURCE-DERIVED]` Battery Smart, data-driven consulting caselets |
| **P2** | **Python / BI** | L1–L2 Basic | [`programming/python.md`](programming/python.md) | `[INFERRED]` Exploratory analytics and scenario sensitivity |

---

## 5. Candidate Action Summary: Primary Stack by Target

```
┌──────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Candidate Target Profile             │ Primary Core Stack (P0/P1 Essentials)                  │
├──────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Core HWRE / Water Resources          │ HEC-RAS + QGIS + Python + Excel                        │
│ CFD & Fluid Mechanics R&D            │ OpenFOAM + ParaView + Linux Shell + Python             │
│ Structural Engineering               │ AutoCAD + ETABS or STAAD.Pro + Excel (+ SAP2000)       │
│ Construction EPC / Management        │ AutoCAD + Primavera P6 + Excel                         │
│ Data Analytics                       │ Excel + SQL + Python (Pandas/NumPy)                    │
│ Management Consulting                │ Advanced Excel + Executive PowerPoint (+ Basic SQL)    │
└──────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

> **Related Navigation:**
> [SOFTWARE_COMPANY_LINKAGE.md](SOFTWARE_COMPANY_LINKAGE.md) · [SOFTWARE_COMPLETENESS_MATRIX.md](SOFTWARE_COMPLETENESS_MATRIX.md) · [TOOLS_INDEX.md](TOOLS_INDEX.md) · [anti-overload.md](anti-overload.md)
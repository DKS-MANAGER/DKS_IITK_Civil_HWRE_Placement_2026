# Core Track Inventory

> **Purpose:** Identify all preparation tracks inside `core/`, their roles, subjects, existing material, and completeness.
> **Completeness:** Level 0–5 (0=empty, 1=index, 2=basic, 3=studyable, 4=placement-ready, 5=excellent)

---

## Track Inventory

| # | Track | Purpose | Roles | Subjects | Existing Material | Completeness |
|---|-------|---------|-------|----------|-------------------|:------------:|
| 1 | **GATE** | GATE Civil exam prep | GATE aspirant | All 15 GATE subjects | Notes, formulas, practice, mock, PYQ, revision, roadmap, 30/60/90 | **Level 5** |
| 2 | **HWRE** | Water resources / hydrology / hydraulics | Water Resources Engineer, Hydrologist, Hydraulic Engineer, Flood Modeller | Hydrology, Hydraulics, Fluid Mech, Groundwater, WRE, Irrigation, Flood Control, Wastewater, Water Supply, Sediment, Turbulence | 11 subject guides, formulas, practice, mock, interview, modelling, traps, roadmap, 30/60/90 | **Level 5** |
| 3 | **Fundamentals** | General Civil foundation | General Civil Engineer (PSU) | Mechanics, SOM, cross-domain | Mechanics, SOM, foundations, role plan | **Level 4** |
| 4 | **Structures** | Structural design | Structural Engineer, Design Engineer | SOM, RCC, Steel, Structural Analysis | structures.md, role plan, revision | **Level 3** |
| 5 | **RCC** | Reinforced concrete design | Structural Engineer, Design Engineer | RCC design (IS 456) | rcc-design.md | **Level 3** |
| 6 | **Steel** | Steel structure design | Structural Engineer, Design Engineer | Steel design (IS 800) | steel-design.md | **Level 3** |
| 7 | **Structural Analysis** | Structural analysis | Structural Engineer, Design Engineer | Determinacy, ILD, moment distribution, matrix methods | structural-analysis.md | **Level 3** |
| 8 | **Geotechnical** | Soil mechanics & foundations | Geotechnical Engineer | Soil mechanics, foundations, slope stability | geotechnical.md, role plan, revision | **Level 3** |
| 9 | **Environmental** | Environmental engineering | Environmental Engineer | Water/air quality, wastewater, solid waste, EIA | environmental-engineering.md, role plan, revision | **Level 3** |
| 10 | **Transportation** | Transportation engineering | Transportation Engineer | Highway, traffic, pavement, railway, airport | transportation-engineering.md, software, role plan, revision | **Level 3** |
| 11 | **Geoinformatics** | GIS / remote sensing | GIS/Survey Engineer | GIS, RS, GNSS, spatial analysis | geoinformatics.md, role plan, revision | **Level 3** |
| 12 | **Infrastructure** | Construction & project management | Project Manager, Construction Engineer, Planning Engineer | PMBOK, CPM/PERT, construction, estimation | infrastructure-engineering-management.md, role plan, revision | **Level 3** |

---

## Track Completeness Summary

| Track | Study | Formula | Examples | Practice | Test | Interview | Revision | Role Plan | Company Map |
|-------|:-----:|:-------:|:--------:|:--------:|:----:|:---------:|:--------:|:---------:|:-----------:|
| GATE | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | △ |
| HWRE | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | △ |
| Fundamentals | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| Structures | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| RCC | ✅ | ✅ | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Steel | ✅ | ✅ | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Structural Analysis | ✅ | ✅ | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Geotechnical | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| Environmental | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| Transportation | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| Geoinformatics | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |
| Infrastructure | ✅ | ✅ | ✅ | △ | ✗ | △ | ✅ | ✅ | ✗ |

**Legend:** ✅ = present · △ = partial (embedded in role plan, no standalone file) · ✗ = missing

---

## Key Insight

- **GATE + HWRE** are the only two **Level 5** tracks (complete LEARN→UNDERSTAND→PRACTICE→TEST→INTERVIEW→REVISE chain).
- **All 10 other tracks** have strong **study material (Level 3)** but are **missing the practice → test → interview chain** that would make them Level 4.
- The **biggest structural gap** is `rcc/`, `steel/`, `structural-analysis/` — they have no role plan, practice, test, or interview files at all.
- **B-tier roles** (geotech, enviro, transport, GIS, infra) have role plans with embedded practice but **no standalone test/interview files**.
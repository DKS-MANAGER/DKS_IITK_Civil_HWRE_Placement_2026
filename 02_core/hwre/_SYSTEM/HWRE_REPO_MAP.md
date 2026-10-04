# HWRE — Repository Map

> Dependency and navigation map for the complete HWRE placement preparation system.

## Directory Structure

```
02_02_02_02_core/hwre/
├── README.md                      ← Hub (rewritten)
├── MASTER_INDEX.md                ← Entry point (1–2 click navigation)
├── HWRE_ROADMAP.md                ← Syllabus → Roadmap → Learn → Practice → Test → Revise
├── HWRE_30_60_90_DAY_PLAN.md      ← Realistic 30/60/90-day schedule
├── ERROR_ANALYSIS.md              ← Error tracking + reattempt system
├── RAPID_REVISION.md              ← 30-min / 2-hr / 1-day revision
├── TRAPS.md                       ← Common GATE/interview mistakes
├── INTERVIEW.md                   ← HWRE interview Q&A bank
├── MODELLING.md                   ← HEC-HMS → HEC-RAS → GIS workflow
├── _SYSTEM/
│   ├── HWRE_AUDIT_STATE.md        ← Context-limit tracker
│   ├── HWRE_REPO_MAP.md           ← This file
│   ├── HWRE_FILE_INVENTORY.md     ← File inventory + status
│   └── HWRE_COMPLETENESS_MATRIX.md← 0–10 completeness scores
├── formulas/
│   └── hwre-formulas.md           ← Canonical formula sheet (P0–P3)
├── practice/
│   └── hwre-practice.md           ← Verified solved problems
├── mocks/
│   └── hwre-mock-1.md             ← Full HWRE mock test
├── hydraulics/
│   ├── hydraulics.md              ← P0 Fluid mechanics & hydraulics
│   ├── turbulence-modeling.md     ← P0 CFD / turbulence
│   ├── hydraulics-rapid-revision.md
│   └── role-study-plan.md
├── open_channel_flow/
│   └── open-channel-flow.md       ← P0 Open channel flow
├── hydrology/
│   ├── hydrology.md               ← P0 Hydrology
│   ├── sediment-transport.md      ← P0 Sediment transport
│   ├── hydrology-rapid-revision.md
│   └── role-study-plan.md
├── water_resources/
│   └── water-resources-engineering.md ← P0 Water resources
├── irrigation/
│   └── irrigation-engineering.md  ← P1 Irrigation
├── flood_control/
│   └── flood-control.md           ← P1 Flood control
├── wastewater/
│   └── wastewater-engineering.md  ← P1 Wastewater
├── water_supply/
│   ├── groundwater.md             ← P1 Groundwater
│   └── water-supply.md            ← P1 Water supply
└── exam_notes/
    └── hwre-exam-notes.md         ← One-page cheat sheet
```

## External Dependencies

| Resource | Location | Used By |
|----------|----------|---------|
| HEC-RAS walkthrough | `02_02_02_02_02_core/hwre/software-deep-dives/hec-ras-walkthrough.md` | MODELLING, README |
| HEC-HMS tutorial | `02_02_02_02_02_core/hwre/software-deep-dives/hec-hms-tutorial.md` | MODELLING, README |
| EPANET walkthrough | `02_02_02_02_02_core/hwre/software-deep-dives/epanet-walkthrough.md` | README |
| SWMM guide | `02_02_02_02_02_core/hwre/software-deep-dives/swmm-guide.md` | README |
| OpenFOAM case study | `02_02_02_core/cfd/openfoam-case-study.md` | README |
| GeoStudio SLOPE/W | `02_02_02_core/civil-engineering/geotechnical/software-deep-dives/geostudio-slopew-tutorial.md` | README |
| PLAXIS 2D | `02_02_02_core/civil-engineering/geotechnical/software-deep-dives/plaxis-2d-tutorial.md` | README |
| GATE Civil formula sheet | `02_02_02_02_02_02_core/gate/formulas/gate-civil-formulas.md` | README, RAPID_REVISION |
| Technical interview bank | `01_common/interview-fundamentals/technical/technical-interview-bank.md` | INTERVIEW, README |
| Project defense guide | `01_common/interview-fundamentals/technical/project-defense-guide.md` | README |
| Behavioral guide | `01_common/behavioral/behavioral-interview-guide.md` | README |
| HWRE tech roadmap | `02_02_02_02_02_core/hwre/hwre-tech-roadmap.md` | README |

## Navigation Graph

```
MASTER_INDEX
  ├── HWRE_ROADMAP → subject guides → formulas → practice → mock
  ├── HWRE_30_60_90_DAY_PLAN → weekly breakdown
  ├── FORMULAS (canonical) ← subject guides link back
  ├── PRACTICE → verified problems
  ├── MOCK TESTS → scoring + error analysis
  ├── ERROR_ANALYSIS → reattempt loop
  ├── RAPID_REVISION → 30-min/2-hr/1-day
  ├── TRAPS → mistake prevention
  ├── INTERVIEW → Q&A bank
  └── MODELLING → HEC-HMS → HEC-RAS → GIS
```

## Canonical Source Principle

- **Formulas**: `formulas/hwre-formulas.md` is canonical. Subject guides link to it rather than duplicating.
- **Software workflows**: `MODELLING.md` is canonical. Deep-dives in `02_02_02_core/hwre/software-deep-dives/` provide detail.
- **Interview Q&A**: `INTERVIEW.md` is canonical for HWRE-specific questions. General bank in `01_common/interview-fundamentals/technical/`.
# 02_CORE — Technical Engineering Preparation Hub

> **Directory Focus**: Complete technical engineering preparation layer covering Civil Engineering, Hydraulics & Water Resources Engineering (HWRE), Computational Fluid Dynamics (CFD), and GATE Civil.  
> **Target Audience**: M.Tech HWRE / Civil Engineering students preparing for technical interviews, design roles, and core engineering companies.

---

## 1. Core Technical Architecture & Canonical Boundaries

```text
02_core/
├── README.md                      # Core engineering dashboard & cross-discipline routing
├── civil-engineering/             # Classical civil sub-disciplines
│   ├── fluid-mechanics/           # Canonical Home: Fundamental Fluid Mechanics
│   ├── fundamentals/              # Engineering Mechanics & Strength of Materials (SOM)
│   ├── structural-analysis/       # Indeterminate structures, stiffness & flexibility methods
│   ├── rcc/                       # IS 456 concrete design & limit state method
│   ├── steel/                     # IS 800 steel design & plastic analysis
│   ├── geotechnical/              # Soil mechanics, effective stress, foundations & slope stability
│   ├── transportation/            # IRC 37 pavement design, geometric design, traffic
│   ├── environmental/             # Water/wastewater treatment, BOD, air pollution
│   ├── geoinformatics/            # Remote sensing, GIS, photogrammetry & GPS
│   └── infrastructure/            # Construction technology & BIM workflows
├── hwre/                          # Major Specialization: Hydraulics, OCF, Hydrology, Rivers
├── cfd/                           # Computational Fluid Dynamics & OpenFOAM simulation
└── gate/                          # Dedicated GATE Civil syllabus, PYQs, tests & formula revision
```

---

## 2. Canonical Fluid Mechanics Ownership Rule

To eliminate conceptual duplication across Civil, HWRE, and CFD:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 CANONICAL FLUID MECHANICS OWNERSHIP RULE                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 02_core/civil-engineering/fluid-mechanics/                               │
│    └──► Fundamental Fluid Mechanics (Properties, Statics, Kinematics,       │
│         Euler/Bernoulli Dynamics, Pipe Flow, Boundary Layer, Similitude)    │
│                                                                             │
│ 2. 02_core/hwre/                                                            │
│    └──► Applied Hydraulics, Open Channel Flow (Specific Energy, Hydraulic   │
│         Jumps, GVF Profiles), Hydrology, Groundwater, Sediment Transport    │
│                                                                             │
│ 3. 02_core/cfd/                                                             │
│    └──► Numerical Fluid Mechanics, Navier-Stokes Discretization, Turbulence │
│         Modeling (k-ε, k-ω SST), OpenFOAM Case Studies & Meshing            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Master Navigation & Quick Links

| Technical Domain | Directory Link | Core Subjects & Tools Covered |
| :--- | :--- | :--- |
| **Fundamental Fluid Mechanics** | [`civil-engineering/fluid-mechanics/README.md`](civil-engineering/fluid-mechanics/README.md) | Fluid Statics, Bernoulli, Navier-Stokes, Pipe flow losses, Boundary layer growth, Buckingham Pi theorem. |
| **Civil Engineering Sub-Disciplines** | [`civil-engineering/`](file:///e:/DKS_IITK_Civil_HWRE_Placement_2026/02_core/civil-engineering/) | Engineering Mechanics, SOM, RCC, Steel, Geotech, Highway, Environment, Geoinformatics, Infrastructure, and tools (STAAD, ETABS, Revit). |
| **HWRE Specialization** | [`hwre/README.md`](hwre/README.md) | Open Channel Flow, Hydrology, Groundwater, Sediment Transport, Flood Modeling, and modeling software (HEC-RAS, HEC-HMS, EPANET, SWMM). |
| **CFD & Simulation** | [`cfd/cfd-tech.md`](cfd/cfd-tech.md) | Finite Volume discretization, $k$-$\epsilon$ / $k$-$\omega$ SST turbulence, OpenFOAM case studies, ParaView, and mesh generation. |
| **GATE Civil** | [`gate/README.md`](gate/README.md) | Complete topic-wise GATE notes, comprehensive formula sheets, previous years' questions (PYQ), and mock tests. |

---

## 4. Recommended Study Paths

```text
Core Civil Track:
01_common/aptitude ──► 02_core/civil-engineering ──► 04_company-prep/core-companies ──► 05_interview/technical/civil ──► 06_revision

HWRE & Water Resources Track:
01_common/aptitude ──► 02_core/civil-engineering/fluid-mechanics ──► 02_core/hwre ──► 08_projects ──► 04_company-prep/hwre-companies ──► 05_interview/technical/hwre ──► 06_revision

CFD / Fluids Specialization Track:
01_common/aptitude ──► 02_core/civil-engineering/fluid-mechanics ──► 02_core/cfd ──► 08_projects/bridgerisk ──► 05_interview/technical/cfd ──► 06_revision
```

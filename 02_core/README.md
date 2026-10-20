# 02_CORE — Technical Engineering Preparation Hub

> **Target Audience**: Civil Engineering students and M.Tech Hydraulics & Water Resources Engineering (HWRE) candidates preparing for campus recruitment assessments, technical screening rounds, core design interviews, and PSU/GATE assessments.  
> **Scope & Syllabus Basis**: Curated curriculum mapped to core undergraduate Civil Engineering foundations, postgraduate water resources engineering, and standard Indian campus placement technical assessments.  
> **Placement Variance Notice**: Campus recruitment formats, question patterns, weightages, and interview depth vary significantly by company, hiring division, and recruitment season. Do not assume fixed test patterns without verified placement-cell circulars or confirmed past papers from the IIT Kanpur Students' Placement Office (SPO).

---

## 1. Core Technical Architecture & Directory Layout

```text
02_core/
├── README.md                      # Core engineering curriculum dashboard & topic matrix
├── civil-engineering/             # Classical civil engineering sub-disciplines
│   ├── fundamentals/              # Engineering Mechanics & Strength of Materials (SOM)
│   ├── structural-analysis/       # Indeterminate structures, stiffness & flexibility methods
│   ├── rcc/                       # IS 456:2000 concrete design & limit state method
│   ├── steel/                     # IS 800:2007 steel design & plastic analysis
│   ├── geotechnical/              # Soil mechanics, effective stress, foundations, slope stability
│   ├── fluid-mechanics/           # Canonical Home: Fundamental Fluid Mechanics & pipe flow
│   ├── environmental/             # Water/wastewater treatment, BOD, air pollution & standards
│   ├── transportation/            # IRC pavement design, highway geometric design, traffic & airport
│   ├── geoinformatics/            # Remote sensing, GIS, photogrammetry, surveying & GNSS/NavIC
│   ├── infrastructure/            # Construction management, CPM/PERT, cost estimation & BIM
│   ├── structures/                # Structural role study plans & tech overviews
│   └── tools/                     # Structural analysis & CAD software references
├── hwre/                          # Major Specialization: Hydraulics, OCF, Hydrology, Rivers, Modeling
├── cfd/                           # Computational Fluid Dynamics & OpenFOAM simulation
└── gate/                          # Dedicated GATE Civil syllabus, PYQs, tests & formula revision
```

---

## 2. Canonical Fluid Mechanics Ownership Rule

To eliminate redundancy and cross-file contradictions across Civil, HWRE, and CFD:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 CANONICAL FLUID MECHANICS OWNERSHIP RULE                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 02_core/civil-engineering/fluid-mechanics/                               │
│    └──► Fundamental Fluid Mechanics (Properties, Statics, Kinematics,       │
│         Euler/Bernoulli Dynamics, Pipe Flow Losses, Boundary Layer, Similitude)│
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

## 3. Four Balanced Placement Study Routes

Candidates should tailor their study sequence according to their target roles:

```text
Route 1: General Placement Aptitude & Screening Track
[01_common/aptitude] ──► [01_common/logical-reasoning] ──► [02_core/civil-engineering/fundamentals] ──► Section Mocks

Route 2: Broad Civil Technical Assessment Track
[fundamentals] ──► [structural-analysis] ──► [rcc & steel] ──► [geotechnical] ──► [environmental & highway] ──► Full Mocks

Route 3: Technical Design & Whiteboard Interview Track
[First-principles derivations] ──► [IS 456 / IS 800 / IRC 37 Code Provisions] ──► [Failure Modes & Shear Stress Profiles] ──► Viva

Route 4: HWRE & Water Resources Specialization Track
[fluid-mechanics] ──► [hwre/open_channel_flow] ──► [hwre/hydrology] ──► [Software: HEC-RAS / EPANET] ──► Project Defenses
```

1. **Route 1 — General Placement Screening**: Focuses on quantitative aptitude, logical reasoning, and rapid fundamental Civil MCQs for multi-disciplinary screening rounds. Routing and general aptitude practice are maintained centrally in [`01_common/aptitude`](../01_common/aptitude/README.md).
2. **Route 2 — Broad Civil Technical Assessment**: Systematically covers all core undergraduate Civil subjects required by EPC contractors, infrastructure developers, consultancies, and public sector assessments.
3. **Route 3 — Technical Interview & Design Viva**: Deep dives into code assumptions, failure modes, sign conventions, moment distributions, and whiteboard derivations commonly asked by senior technical panelists.
4. **Route 4 — HWRE Specialization**: Targeted at specialized water resource consultancies, environmental engineering firms, hydraulics research laboratories, and CFD teams.

---

## 4. Master Civil Placement Topic Matrix

The following matrix provides topic-by-topic guidance, priority levels, practice locations, and external practice references adapted from standard question patterns (such as [IndiaBIX Civil Engineering](https://www.indiabix.com/civil-engineering/questions-and-answers/)):

| Subject | Fundamentals to Master | Typical Question Formats | Local Study & Practice Files | Priority | Prerequisites | Practice & Reference Link |
| :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **Engineering Mechanics** | Free-body diagrams, Lami's theorem, dry friction, trusses (method of joints/sections), virtual work, kinematics/kinetics. | Conceptual MCQs, truss force calculations, friction equilibrium problems. | [`fundamentals/engineering-mechanics.md`](civil-engineering/fundamentals/engineering-mechanics.md)<br>[`fundamentals/civil-engineering-foundations.md`](civil-engineering/fundamentals/civil-engineering-foundations.md) | **P0** | Basic Calculus & Vector Algebra | [IndiaBIX Applied Mechanics](https://www.indiabix.com/civil-engineering/applied-mechanics/) |
| **Strength of Materials (SOM)** | Stress-strain relationships, Mohr’s circle sign conventions, beam bending ($M/I = \sigma/y$), shear stress distribution, torsion ($T/J = \tau/r$), Euler buckling columns. | Numerical derivations, principal stress MCQs, maximum deflection calculations. | [`fundamentals/strength-of-materials.md`](civil-engineering/fundamentals/strength-of-materials.md)<br>[`fundamentals/civil-rapid-revision.md`](civil-engineering/fundamentals/civil-rapid-revision.md) | **P0** | Engineering Mechanics | [IndiaBIX Strength of Materials](https://www.indiabix.com/civil-engineering/strength-of-materials/) |
| **Structural Analysis** | Static & kinematic indeterminacy, moment distribution method, slope deflection, three-hinged parabolic arches, matrix stiffness method $[K]\{u\} = \{F\}$. | Matrix assembly, end-moment calculations, influence line diagrams, shape factors. | [`structural-analysis/structural-analysis.md`](civil-engineering/structural-analysis/structural-analysis.md)<br>[`structural-analysis/PRACTICE.md`](civil-engineering/structural-analysis/PRACTICE.md)<br>[`structural-analysis/INTERVIEW.md`](civil-engineering/structural-analysis/INTERVIEW.md) | **P0** | Strength of Materials | [IndiaBIX Theory of Structures](https://www.indiabix.com/civil-engineering/theory-of-structures/) |
| **RCC Design (IS 456:2000)** | Limit state method, under- vs. over-reinforced failure modes, singly/doubly reinforced beams, one-way vs. punching shear, column interaction curves, detailing. | Code clause MCQs, limiting moment of resistance, stirrup design, bar curtailment. | [`rcc/rcc-design.md`](civil-engineering/rcc/rcc-design.md)<br>[`rcc/PRACTICE.md`](civil-engineering/rcc/PRACTICE.md)<br>[`rcc/INTERVIEW.md`](civil-engineering/rcc/INTERVIEW.md) | **P0** | SOM & Structural Analysis | [IndiaBIX RCC Structures](https://www.indiabix.com/civil-engineering/rcc-structures-design/) |
| **Structural Steel (IS 800:2007)** | Limit state design of tension/compression members, plastic hinge mechanisms & shape factors, bolted/welded connections, lateral torsional buckling. | Plastic collapse load, weld shear capacity, slenderness ratio limits. | [`steel/steel-design.md`](civil-engineering/steel/steel-design.md)<br>[`steel/PRACTICE.md`](civil-engineering/steel/PRACTICE.md)<br>[`steel/INTERVIEW.md`](civil-engineering/steel/INTERVIEW.md) | **P1** | SOM & Structural Analysis | [IndiaBIX Steel Design](https://www.indiabix.com/civil-engineering/steel-structure-design/) |
| **Geotechnical Engineering** | 3-phase soil system, USCS / IS 1498 classification, Terzaghi effective stress, Darcy seepage velocity vs. flux, 1D consolidation, Mohr-Coulomb shear, bearing capacity. | Phase diagram calculations, $C_c$ settlement, factor of safety against sliding, active/passive earth pressure. | [`geotechnical/geotechnical.md`](civil-engineering/geotechnical/geotechnical.md)<br>[`geotechnical/PRACTICE.md`](civil-engineering/geotechnical/PRACTICE.md)<br>[`geotechnical/INTERVIEW.md`](civil-engineering/geotechnical/INTERVIEW.md) | **P0** | SOM & Fluid Statics | [IndiaBIX Soil Mechanics](https://www.indiabix.com/civil-engineering/soil-mechanics-and-foundation-engineering/) |
| **Fluid Mechanics** | Fluid properties, hydrostatic pressure & center of pressure, Bernoulli equation with head losses, boundary layer separation, Darcy-Weisbach friction factor, similitude. | Manometer problems, venture/orifice discharge, laminar vs. turbulent pipe flow, Pi theorem. | [`fluid-mechanics/README.md`](civil-engineering/fluid-mechanics/README.md)<br>[`fluid-mechanics/01_fluid-properties-and-statics.md`](civil-engineering/fluid-mechanics/01_fluid-properties-and-statics.md)<br>[`fluid-mechanics/03_pipe-flow-and-losses.md`](civil-engineering/fluid-mechanics/03_pipe-flow-and-losses.md) | **P0** | Engineering Mechanics | [IndiaBIX Hydraulics](https://www.indiabix.com/civil-engineering/hydraulics/) |
| **Hydraulics & OCF (HWRE)** | Specific energy & critical flow ($F_r = 1$), hydraulic jump energy dissipation, gradually varied flow (GVF) profiles, choking in contractions, channel transitions. | Jump sequent depth ratio, channel choke limiting width, backwater profile identification. | [`hwre/open_channel_flow/open-channel-flow.md`](hwre/open_channel_flow/open-channel-flow.md)<br>[`hwre/practice/hwre-practice.md`](hwre/practice/hwre-practice.md)<br>[`hwre/INTERVIEW.md`](hwre/INTERVIEW.md) | **P0 (HWRE)** | Fluid Mechanics | [IndiaBIX Hydraulics & OCF](https://www.indiabix.com/civil-engineering/hydraulics/) |
| **Hydrology & Water Resources** | Hydrologic water budget, unit hydrograph theory, Muskingum flood routing, infiltration models, well hydraulics (Theis/Thiem equations). | UH convolution, S-curve derivation, unconfined/confined aquifer drawdown. | [`hwre/hydrology-tech.md`](hwre/hydrology-tech.md)<br>[`hwre/sediment-tech.md`](hwre/sediment-tech.md)<br>[`hwre/hwre-rapid-revision.md`](hwre/hwre-rapid-revision.md) | **P0 (HWRE)** | Fluid Mechanics | [IndiaBIX Water Resources](https://www.indiabix.com/civil-engineering/water-resources-engineering/) |
| **Environmental Engineering** | Water quality standards (IS 10500:2012), 4-phase breakpoint chlorination, sedimentation kinetics, activated sludge BOD kinetics, air quality indices. | $\text{BOD}_5$ dilution calculations, settling velocity (Stokes law), chlorine dosage, air dispersion. | [`environmental/environmental-engineering.md`](civil-engineering/environmental/environmental-engineering.md)<br>[`environmental/PRACTICE.md`](civil-engineering/environmental/PRACTICE.md)<br>[`environmental/INTERVIEW.md`](civil-engineering/environmental/INTERVIEW.md) | **P1** | Chemistry & Fluid Mechanics | [IndiaBIX Water Supply](https://www.indiabix.com/civil-engineering/water-supply-engineering/) & [Wastewater](https://www.indiabix.com/civil-engineering/waste-water-engineering/) |
| **Transportation & Highway** | Geometric design (SSD, OSD, superelevation $e + f = v^2/127R$), IRC 37:2018 pavement design, traffic flow ($q = ku$), ICAO runway length corrections. | Superelevation balance, runway temperature/elevation correction, traffic capacity. | [`transportation/transportation-engineering.md`](civil-engineering/transportation/transportation-engineering.md)<br>[`transportation/PRACTICE.md`](civil-engineering/transportation/PRACTICE.md)<br>[`transportation/INTERVIEW.md`](civil-engineering/transportation/INTERVIEW.md) | **P1** | SOM & Surveying | [IndiaBIX Highway Engineering](https://www.indiabix.com/civil-engineering/highway-engineering/) |
| **Geoinformatics & Surveying** | Traverse balancing (Bowditch), leveling, UTM projection & EPSG datum coordinates, GNSS/NavIC multi-frequency signals, remote sensing sensors. | Error propagation, RL computation, scale factor & coordinate zone transformation. | [`geoinformatics/geoinformatics.md`](civil-engineering/geoinformatics/geoinformatics.md)<br>[`geoinformatics/PRACTICE.md`](civil-engineering/geoinformatics/PRACTICE.md)<br>[`geoinformatics/INTERVIEW.md`](civil-engineering/geoinformatics/INTERVIEW.md) | **P1** | Trigonometry & Basic Physics | [IndiaBIX Surveying](https://www.indiabix.com/civil-engineering/surveying/) & [Remote Sensing](https://www.indiabix.com/civil-engineering/elements-of-remote-sensing/) |
| **Construction & Infrastructure** | CPM/PERT network analysis, critical path, crash cost slope, contract escalation (CPWD Cl. 10CA/10CC, FIDIC index ratio), BIM LOD levels. | Total/free float, expected project duration, cost optimization, cash flow curves. | [`infrastructure/infrastructure-engineering-management.md`](civil-engineering/infrastructure/infrastructure-engineering-management.md)<br>[`infrastructure/PRACTICE.md`](civil-engineering/infrastructure/PRACTICE.md)<br>[`infrastructure/INTERVIEW.md`](civil-engineering/infrastructure/INTERVIEW.md) | **P2** | Basic Probability & Finance | [IndiaBIX Construction Management](https://www.indiabix.com/civil-engineering/construction-management/) |

---

## 5. Verification Policy & Citation Standards

In accordance with technical editorial integrity:
1. **Physical Laws & First Principles**: Verified from standard engineering mechanics, fluid dynamics, and thermodynamics principles (Euler, Navier-Stokes, Darcy, Bernoulli, Hooke).
2. **Design Standards & Codes of Practice**: Explicitly dated and cited by publishing authority:
   - Concrete: Bureau of Indian Standards, **IS 456:2000** (Reaffirmed 2021).
   - Steel: Bureau of Indian Standards, **IS 800:2007** (Reaffirmed 2017).
   - Drinking Water: Bureau of Indian Standards, **IS 10500:2012** (Amendment No. 2, 2018).
   - Soil Classification: Bureau of Indian Standards, **IS 1498:1970** / ASTM D2487.
   - Pavement Design: Indian Roads Congress, **IRC:37-2018** & **IRC:73-1980**.
   - Aerodromes: International Civil Aviation Organization, **ICAO Doc 9157 Part 1** / DGCA CAR Section 4.
   - Public Works Contracts: Central Public Works Department, **CPWD General Conditions of Contract (GCC 2020)**.
3. **External References & Practice Inspiration**: Question patterns and conceptual diagnostics are adapted with attribution to standard engineering question repositories (including [IndiaBIX](https://www.indiabix.com/)). Verbatim copying of proprietary question blocks is strictly prohibited; all examples are independently formulated, solved, and dimensionally checked.
4. **Corporate & Recruiter Data**: Specific compensation numbers, recruitment history, and selection round formats are treated as unconfirmed unless verified against official placement brochures or Students' Placement Office (SPO) releases.

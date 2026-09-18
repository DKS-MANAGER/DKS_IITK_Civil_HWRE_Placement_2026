# Topic Map — DKS IITK Civil / HWRE Placement 2026

> **Repository Provenance & Consolidation Mapping Registry**  
> **Target Audience:** IIT Kanpur M.Tech Civil / HWRE (DEEC 2026 Batch)  
> **Last Updated:** 2026-09-17  
> **Core Architecture Principle:** Clear separation between **Historical Source Provenance** (where content originated during initial ingestion) and **Current Canonical Destination** (the live, active file in the repository tree).

---

## 1. Architectural Model

```
┌──────────────────────────────────────────────┐
│ HISTORICAL SOURCE PROVENANCE                 │
│ (10 Ingested Repositories + Primary Codes)   │
└──────────────────────┬───────────────────────┘
                       │ Content Paraphrasing, Verification & Expansion
┌──────────────────────▼───────────────────────┐
│ CURRENT CANONICAL DESTINATION                │
│ (Active repository file with live hyperlinks)│
└──────────────────────────────────────────────┘
```

---

## 2. Topic → Source Provenance → Canonical Destination

### Core Civil & Structural Engineering

- **Civil Engineering Foundations**
  - **Canonical Destination:** [`core/fundamentals/civil-engineering-foundations.md`](../core/fundamentals/civil-engineering-foundations.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/README.md`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Merged, expanded with IITK course linkage

- **Engineering Mechanics**
  - **Canonical Destination:** [`core/fundamentals/engineering-mechanics.md`](../core/fundamentals/engineering-mechanics.md)
  - **Source Provenance:** `GATE_Civil_Study_Material_2027.md`, `Civil_Placement_IITK/README.md`
  - **Best Source:** `GATE_Civil_Study_Material_2027.md`
  - **Consolidation Status:** Comprehensive guide with worked examples

- **Strength of Materials**
  - **Canonical Destination:** [`core/fundamentals/strength-of-materials.md`](../core/fundamentals/strength-of-materials.md)
  - **Source Provenance:** `GATE_Civil_Study_Material_2027.md`, Gere & Timoshenko standards
  - **Best Source:** `GATE_Civil_Study_Material_2027.md`
  - **Consolidation Status:** Comprehensive guide with Mohr's circle & beam deflection

- **Structural Analysis**
  - **Canonical Destination:** [`core/structural-analysis/structural-analysis.md`](../core/structural-analysis/structural-analysis.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Merged, slope deflection & plastic analysis

- **Reinforced Cement Concrete (RCC)**
  - **Canonical Destination:** [`core/rcc/rcc-design.md`](../core/rcc/rcc-design.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, BIS IS 456:2000
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Full limit-state design guide with code provisions

- **Steel Structures**
  - **Canonical Destination:** [`core/steel/steel-design.md`](../core/steel/steel-design.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, BIS IS 800:2007
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Connection & member design with code provisions

- **Geotechnical Engineering**
  - **Canonical Destination:** [`core/geotechnical/geotechnical.md`](../core/geotechnical/geotechnical.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Merged, soil mechanics & bearing capacity

- **Environmental Engineering**
  - **Canonical Destination:** [`core/environmental/environmental-engineering.md`](../core/environmental/environmental-engineering.md)
  - **Source Provenance:** `awesome-civil-engineering/data/resources.json`, `Civil_Placement_IITK/README.md`
  - **Best Source:** `awesome-civil-engineering/data/resources.json`
  - **Consolidation Status:** Comprehensive environmental guide

- **Transportation Engineering**
  - **Canonical Destination:** [`core/transportation/transportation-engineering.md`](../core/transportation/transportation-engineering.md)
  - **Source Provenance:** `awesome-civil-engineering/README.md`, `Civil_Placement_IITK/README.md`
  - **Best Source:** `awesome-civil-engineering/README.md`
  - **Consolidation Status:** Enhanced guide with geometric & pavement design

- **Geoinformatics & Remote Sensing**
  - **Canonical Destination:** [`core/geoinformatics/geoinformatics.md`](../core/geoinformatics/geoinformatics.md)
  - **Source Provenance:** `awesome-civil-engineering/data/resources.json`, `resources/gis-tools.md`
  - **Best Source:** `resources/gis-tools.md`
  - **Consolidation Status:** GIS, RS, and GPS spatial modeling guide

- **Infrastructure Engineering & Management**
  - **Canonical Destination:** [`core/infrastructure/infrastructure-engineering-management.md`](../core/infrastructure/infrastructure-engineering-management.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `campus-placement-prep/README.md`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** CPM/PERT, cost estimation & construction management guide

---

### Hydraulics & Water Resources Engineering (HWRE)

- **Hydraulics**
  - **Canonical Destination:** [`core/hwre/hydraulics/hydraulics.md`](../core/hwre/hydraulics/hydraulics.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Bernoulli, pipe friction, pumps, and momentum theorems

- **Turbulence Modeling**
  - **Canonical Destination:** [`core/hwre/hydraulics/turbulence-modeling.md`](../core/hwre/hydraulics/turbulence-modeling.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, Wilcox / Pope turbulence literature
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** RANS ($k$-$\epsilon$, $k$-$\omega$ SST), LES, and wall functions

- **Open Channel Flow**
  - **Canonical Destination:** [`core/hwre/open_channel_flow/open-channel-flow.md`](../core/hwre/open_channel_flow/open-channel-flow.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, Chow OCF standards
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** GVF backwater curves, hydraulic jumps, and channel controls

- **Hydrology**
  - **Canonical Destination:** [`core/hwre/hydrology/hydrology.md`](../core/hwre/hydrology/hydrology.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Hydrograph analysis, unit hydrograph, and Muskingum flood routing

- **Sediment Transport & Scour**
  - **Canonical Destination:** [`core/hwre/hydrology/sediment-transport.md`](../core/hwre/hydrology/sediment-transport.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, Shields / Rouse / Garcia literature
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Shields threshold, suspended sediment Rouse profiles, and bridge pier scour

- **Water Resources Engineering**
  - **Canonical Destination:** [`core/hwre/water_resources/water-resources-engineering.md`](../core/hwre/water_resources/water-resources-engineering.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Reservoir capacity, dam stability, and water budgeting

- **Irrigation Engineering**
  - **Canonical Destination:** [`core/hwre/irrigation/irrigation-engineering.md`](../core/hwre/irrigation/irrigation-engineering.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `Aptitude-For-Placements/`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Duty-delta, canal design (Kennedy/Lacey), and irrigation methods

- **Groundwater Hydrology**
  - **Canonical Destination:** [`core/hwre/water_supply/groundwater.md`](../core/hwre/water_supply/groundwater.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Darcy's law, Theis exponential integral $W(u)$, Cooper-Jacob method

- **Wastewater Engineering**
  - **Canonical Destination:** [`core/hwre/wastewater/wastewater-engineering.md`](../core/hwre/wastewater/wastewater-engineering.md)
  - **Source Provenance:** `awesome-civil-engineering/data/resources.json`, `Civil_Placement_IITK/README.md`
  - **Best Source:** `awesome-civil-engineering/data/resources.json`
  - **Consolidation Status:** Sewer design, activated sludge, and anaerobic digestion

- **Water Supply Engineering**
  - **Canonical Destination:** [`core/hwre/water_supply/water-supply.md`](../core/hwre/water_supply/water-supply.md)
  - **Source Provenance:** `awesome-civil-engineering/data/resources.json`
  - **Best Source:** `awesome-civil-engineering/data/resources.json`
  - **Consolidation Status:** Water distribution networks, Hardy Cross method, and water treatment

- **Flood Control & Management**
  - **Canonical Destination:** [`core/hwre/flood_control/flood-control.md`](../core/hwre/flood_control/flood-control.md)
  - **Source Provenance:** `awesome-civil-engineering/data/resources.json`, `Civil_Placement_IITK/README.md`
  - **Best Source:** `awesome-civil-engineering/data/resources.json`
  - **Consolidation Status:** Flood plain delineation, levees, and drainage engineering

---

### Aptitude & Assessment Battery

- **Quantitative Aptitude**
  - **Canonical Destination:** [`aptitude/quant/percentages.md`](../aptitude/quant/percentages.md)
  - **Source Provenance:** `Aptitude/README.md`, `Aptitude-For-Placements/README.md`
  - **Best Source:** `Aptitude/README.md`
  - **Consolidation Status:** Modular topic series with 10 topic diagnostic tests

- **Logical Reasoning**
  - **Canonical Destination:** [`aptitude/reasoning/seating-arrangement.md`](../aptitude/reasoning/seating-arrangement.md)
  - **Source Provenance:** `Aptitude/README.md`, `Aptitude-For-Placements/`
  - **Best Source:** `Aptitude/README.md`
  - **Consolidation Status:** Complete analytical puzzle battery

- **Verbal Ability & Reading Comprehension**
  - **Canonical Destination:** [`aptitude/verbal/README.md`](../aptitude/verbal/README.md)
  - **Source Provenance:** `Aptitude/README.md`
  - **Best Source:** `Aptitude/README.md`
  - **Consolidation Status:** Grammar, sentence correction, and RC passage bank

- **Data Interpretation**
  - **Canonical Destination:** [`aptitude/di/README.md`](../aptitude/di/README.md)
  - **Source Provenance:** `Aptitude/README.md`
  - **Best Source:** `Aptitude/README.md`
  - **Consolidation Status:** Multi-tier datasets, caselets, radar charts, and tables

- **Standardized Assessment Suite (54 Tests)**
  - **Canonical Destination:** [`docs/TESTING_GUIDE.md`](../docs/TESTING_GUIDE.md) & [`prep/READINESS_SCORECARD.md`](../prep/READINESS_SCORECARD.md)
  - **Source Provenance:** Primary creation calibrated against IITK OA papers
  - **Best Source:** Repository Original Testing Engine
  - **Consolidation Status:** 17 Topic Diagnostics + 5 Sectionals + 7 Full Mocks + 25 Role Tests

---

### Software & Technology

- **OpenFOAM CFD Case Study**
  - **Canonical Destination:** [`software-and-tech/deep-dives/openfoam-case-study.md`](../software-and-tech/deep-dives/openfoam-case-study.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, OpenFOAM Foundation v10 Guide
  - **Best Source:** OpenFOAM Official Documentation
  - **Consolidation Status:** Complete end-to-end tutorial with `nutkWallFunction` and PIMPLE setup

- **HEC-RAS River Hydraulics**
  - **Canonical Destination:** [`software-and-tech/deep-dives/hec-ras-walkthrough.md`](../software-and-tech/deep-dives/hec-ras-walkthrough.md)
  - **Source Provenance:** USACE HEC-RAS User Manual
  - **Best Source:** USACE Official Technical Documentation
  - **Consolidation Status:** 1D steady and 2D unsteady flow modeling walkthrough

- **EPANET Water Distribution**
  - **Canonical Destination:** [`software-and-tech/deep-dives/epanet-walkthrough.md`](../software-and-tech/deep-dives/epanet-walkthrough.md)
  - **Source Provenance:** US EPA Documentation
  - **Best Source:** EPA Technical Manual
  - **Consolidation Status:** Pipe network calibration, pump head curves, water quality tracking

- **SWMM Urban Stormwater**
  - **Canonical Destination:** [`software-and-tech/deep-dives/swmm-guide.md`](../software-and-tech/deep-dives/swmm-guide.md)
  - **Source Provenance:** US EPA SWMM Reference Manual
  - **Best Source:** EPA Technical Manual
  - **Consolidation Status:** Catchment discretization, hydrograph routing, LID controls

---

### Interview Preparation & Career Hub

- **Technical Interview Oral Bank (30 Trees)**
  - **Canonical Destination:** [`prep/interview/technical/technical-interview-bank.md`](../prep/interview/technical/technical-interview-bank.md)
  - **Source Provenance:** `Civil_Placement_IITK/README.md`, `interview-handbook-2026/README.md`
  - **Best Source:** `Civil_Placement_IITK/README.md`
  - **Consolidation Status:** Branching question trees with literature references

- **Behavioral & HR Interview Bank**
  - **Canonical Destination:** [`prep/behavioral/hr_questions/hr-questions-bank.md`](../prep/behavioral/hr_questions/hr-questions-bank.md)
  - **Source Provenance:** `awesome-behavioral-interviews/README.md`, `Placement_Preparation/INTERVIEW EXPERIENCES/`
  - **Best Source:** `awesome-behavioral-interviews/README.md`
  - **Consolidation Status:** STAR framework, 50 curated questions with corporate rubric

- **Consulting Case Bank & Frameworks**
  - **Canonical Destination:** [`non-core/01_roles/consulting/case-bank.md`](../non-core/01_roles/consulting/case-bank.md) & [`non-core/01_roles/consulting/case-frameworks.md`](../non-core/01_roles/consulting/case-frameworks.md)
  - **Source Provenance:** Case in Point, Victor Cheng LOMS, IITK Casebook
  - **Best Source:** IITK Consulting Casebook
  - **Consolidation Status:** 12 worked case simulations with quantitative math verification

---

## 3. Historical Migration Reference

For candidates or developers auditing original file movements from the initial 10-repository consolidation (September 3, 2026), refer to the historical migration ledger:
- [`index/SOURCE_MIGRATION_MAP.csv`](SOURCE_MIGRATION_MAP.csv)


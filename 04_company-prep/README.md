# 04_COMPANY_PREP — Company Intelligence & Targeting Hub

> **Directory Focus**: Target corporate profiles, hiring process insights, selection criteria, eligibility rules, and dedicated company-specific preparation packs for IIT Kanpur M.Tech Civil (Hydraulics and Water Resources Engineering) placement candidates.  
> **Core Architectural Rule**: Company preparation does NOT duplicate technical chapters. It answers: *"Given this specific company and role, what exact modules should I study from the repository, and how are candidate skills evaluated?"*

---

## 1. Seven-Tier Architecture Overview

The `04_company-prep/` layer is organized into seven modular directories:

```text
04_company-prep/
├── README.md                      # Master navigation hub, evidentiary guidelines, and directory index
├── company-directory/             # Recruiter registries, historical CTC trends, and eligibility profiles
├── role-matrix/                   # Cross-company software matrices, role-to-tool linkages & priority tiers
├── core-companies/                # Core Civil, structural, EPC & materials majors (L&T, Godrej, Hilti, JSW)
├── hwre-companies/                # Water resources, hydrology, GIS & fluid modeling firms (Vassarlabs, SLB)
├── consulting-companies/          # Strategy, management & technical advisory consultancies (Mu Sigma, KBR, TCE)
├── software-companies/            # Technology, SaaS & software systems firms (Darwinbox, DeltaX, Expeditor)
└── company-specific-prep/         # High-yield end-to-end deep-dive preparation packages
    ├── accenture-japan/           # Accenture Japan — Digital Consultant (Analyst Entry) Package
    ├── citicorp-aim-analytics/    # Citicorp (CSIPL) — Business Analytics (SBS) AIM Package
    ├── deloitte-analyst-ai-analytics/ # Deloitte US-India — Analyst (AI, Analytics & Tech Consulting) Pack
    ├── exxonmobil-engineer/       # ExxonMobil (EMSTPL) — Engineer (Civil, HWRE, Energy & Facilities) Pack
    ├── hilti-get-value-engineering/ # Hilti (HTSI) — GET (Global Value Engineering Hub, Pune) Pack
    ├── larsen-toubro-pget-civil/  # Larsen & Toubro — PGET (Civil Engineering & EPC Infrastructure) Pack
    ├── vantage-research-scientist-modeler/ # Vantage Research — Scientist Modeler (QSP & Mechanistic PK/PD) Pack
    └── kla-applications-engineer/ # KLA Corporation — Customer Applications Engineer (Semiconductor Yield) Pack
```

---

## 2. Evidentiary Standards & Factual Integrity

All facts in this directory are governed by strict provenance tags to distinguish empirical records from pedagogical preparation heuristics:

| Provenance Tag | Definition & Evidentiary Standard | Usage in Profiles |
| :--- | :--- | :--- |
| `[IITK PLACEMENT SOURCE]` | Directly derived from an accessible official campus placement proforma, SPO circular, or verified portal listing. | Confirmed CTC components, service bonds, verified role titles. |
| `[OFFICIAL COMPANY SOURCE]` | Confirmed via active primary corporate documentation, official career portals, or published regulatory filings. | Corporate structure, business divisions, core technologies. |
| `[OTHER CREDIBLE SOURCE]` | Supported by verified public industry databases, peer-reviewed engineering standards, or documented alumni debriefs. | Historical interview rounds, compensation ranges, market presence. |
| `[PREPARATION INFERENCE]` | A reasoned pedagogical recommendation, study curriculum, or simulated practice problem. | Practice cases, SQL questions, recommended priority tiers (P0–P3). |
| `[UNVERIFIED]` | Data point currently pending official confirmation or blank on active proformas. | Unconfirmed branch cutoffs, unstated test durations, tentative locations. |

> [!IMPORTANT]
> **Cycle Qualification**: Prior-year compensation and selection processes are historical indicators (`[OTHER CREDIBLE SOURCE]`), not guaranteed rules for the 2026–27 Phase 1 placement cycle. Official proformas take precedence for confirmed details.

---

## 3. Directory Navigation & Core Reference Links

| Category | Primary Directory / Index | Scope & Focus | Verified Key Targets |
| :--- | :--- | :--- | :--- |
| **Master Recruiter Directory** | [`company-directory/`](company-directory/README.md) · [`company-profiles.md`](company-directory/company-profiles.md) | Recruiter profiles, placement trends, eligibility summaries, and past interview debriefs. | 50+ recorded recruiters across core, analytics, tech, and consulting. |
| **Software & Role Matrices** | [`role-matrix/`](role-matrix/SOFTWARE_ROLE_MATRIX.md) · [`SOFTWARE_COMPANY_LINKAGE.md`](role-matrix/SOFTWARE_COMPANY_LINKAGE.md) | Maps specific job profiles (Core Design, Water Modeling, Consulting, Tech) to required software and priority tiers. | AutoCAD, STAAD, HEC-RAS, QGIS, OpenFOAM, SQL, Python, Power BI. |
| **Core Civil & Infrastructure** | [`core-companies/`](core-companies/) | Structural consulting, EPC infrastructure, materials R&D, and industrial mechanics. | [L&T](core-companies/civil-lt.md), [Thornton Tomasetti](core-companies/civil-thornton-tomasetti.md), [Hilti](core-companies/07_structural-civil-consulting/008_hilti.md), [TuTr Hyperloop](core-companies/civil-tutr-hyperloop.md). |
| **HWRE & Water Resources** | [`hwre-companies/`](hwre-companies/README.md) | 121-company corporate target directory across 13 sector clusters (Water Consulting, GIS, EPC, Hydro, Pumps, Water Treatment, Energy Fluids). | [Vassarlabs](hwre-companies/02_water-resources-gis/001_vassarlabs.md), [AECOM](hwre-companies/01_water-consulting/022_aecom.md), [Mott MacDonald](hwre-companies/01_water-consulting/023_mott-macdonald.md), [SLB](hwre-companies/09_energy-fluids-rnd/006_slb-schlumberger.md). |
| **Consulting & Advisory** | [`consulting-companies/`](consulting-companies/) | Strategic problem solving, analytics consulting, multidisciplinary engineering, and risk advisory. | [Mu Sigma](consulting-companies/mu-sigma.md), [KBR](consulting-companies/11_multidisciplinary-consulting/010_kbr.md), [TCE](consulting-companies/11_multidisciplinary-consulting/025_tata-consulting-engineers.md). |
| **Software, Tech & SaaS** | [`software-companies/`](software-companies/) | Enterprise software, data analytics, cloud platforms, and supply chain technologies. | [Darwinbox](software-companies/darwinbox.md), [DeltaX](software-companies/deltax.md), [Tech Mahindra](software-companies/tech-mahindra.md), [CEI America](software-companies/cei-american.md). |
| **Dedicated Prep Packs** | [`company-specific-prep/`](company-specific-prep/) | Comprehensive, multi-module interview preparation packages built for high-priority hiring drives. | [Accenture Japan](company-specific-prep/accenture-japan/README.md) (Digital Consultant)<br>[Citi AIM Analytics](company-specific-prep/citicorp-aim-analytics/README.md) (Business Analytics SBS)<br>[Deloitte USI Analyst](company-specific-prep/deloitte-analyst-ai-analytics/README.md) (AI, Analytics & Tech Consulting)<br>[ExxonMobil Engineer](company-specific-prep/exxonmobil-engineer/README.md) (Engineer — Civil & HWRE)<br>[Hilti GET](company-specific-prep/hilti-get-value-engineering/README.md) (Global Value Engineering Hub)<br>[Larsen & Toubro PGET](company-specific-prep/larsen-toubro-pget-civil/README.md) (Post Graduate Engineer Trainee — Civil)<br>[Vantage Research Scientist Modeler](company-specific-prep/vantage-research-scientist-modeler/README.md) (Scientist 1 & 2 — QSP & PK/PD)<br>[KLA Corporation Applications Engineer](company-specific-prep/kla-applications-engineer/README.md) (Customer Applications Engineer — Semiconductor Yield). |

---

## 4. End-to-End Dedicated Preparation Packs

For flagship campus opportunities with verified job descriptions or placement proformas, comprehensive deep-dive preparation suites are maintained in a consolidated **6 Topic-Wise Master Modules** architecture:

### 4.1 Accenture Japan — Digital Consultant (Analyst Entry)
* **Target Package**: [`company-specific-prep/accenture-japan/`](company-specific-prep/accenture-japan/README.md)
* **Core Profile**: Technology-agnostic digital transformation (DX), Enterprise Architecture, Cloud Migration, and Industry X smart systems.
* **Master Architecture**:
  * [`01_QUANTITATIVE_APTITUDE_AND_COMMERCIAL_MATH.md`](company-specific-prep/accenture-japan/01_QUANTITATIVE_APTITUDE_AND_COMMERCIAL_MATH.md) — Commercial economics, SaaS metrics, and 20 solved math problems.
  * [`02_PYTHON_ALGORITHMIC_LOGIC_AND_CODE_PUZZLES.md`](company-specific-prep/accenture-japan/02_PYTHON_ALGORITHMIC_LOGIC_AND_CODE_PUZZLES.md) — Python runtime internals, memory model, and 20 verified algorithms.
  * [`03_SQL_DATABASE_ARCH_AND_ENTERPRISE_ANALYTICS.md`](company-specific-prep/accenture-japan/03_SQL_DATABASE_ARCH_AND_ENTERPRISE_ANALYTICS.md) — 10-step SQL execution, 3VL logic, and 20 production analytics queries.
  * [`04_DIGITAL_TECHNOLOGIES_CLOUD_AI_AND_SECURITY.md`](company-specific-prep/accenture-japan/04_DIGITAL_TECHNOLOGIES_CLOUD_AI_AND_SECURITY.md) — OS, networking, cloud systems, Generative AI/RAG, and Zero Trust security.
  * [`05_CONSULTING_CASES_JAPAN_CULTURE_AND_BEHAVIORAL.md`](company-specific-prep/accenture-japan/05_CONSULTING_CASES_JAPAN_CULTURE_AND_BEHAVIORAL.md) — 6 enterprise transformation cases, Japan business culture (Hou-Ren-So), and STAR interview mastery.
  * [`06_MOCK_TESTS_QUESTION_BANK_AND_RAPID_REVISION.md`](company-specific-prep/accenture-japan/06_MOCK_TESTS_QUESTION_BANK_AND_RAPID_REVISION.md) — 90-min online mock assessment, 15-question diagnostic, and rapid revision handbook.
  * Governance: [`PLACEMENT_FACTS.md`](company-specific-prep/accenture-japan/PLACEMENT_FACTS.md), [`STUDY_GUIDE.md`](company-specific-prep/accenture-japan/STUDY_GUIDE.md), [`READINESS_SCORECARD.md`](company-specific-prep/accenture-japan/READINESS_SCORECARD.md).

### 4.2 Citicorp Services India — Business Analytics (SBS), Citi AIM
* **Target Package**: [`company-specific-prep/citicorp-aim-analytics/`](company-specific-prep/citicorp-aim-analytics/README.md)
* **Core Profile**: Analytics and Information Management (AIM) global community delivering financial insights, predictive scoring, and data manipulation.
* **Master Architecture**:
  * [`01_STATISTICS_PROBABILITY_AND_BANKING_RISK.md`](company-specific-prep/citicorp-aim-analytics/01_STATISTICS_PROBABILITY_AND_BANKING_RISK.md) — Distributions, hypothesis testing (Welch's t, ANOVA, Chi-Square), and 30 solved problems.
  * [`02_SQL_DATABASE_ARCH_AND_BANKING_DATA_MANIPULATION.md`](company-specific-prep/citicorp-aim-analytics/02_SQL_DATABASE_ARCH_AND_BANKING_DATA_MANIPULATION.md) — Window functions, join fan-out mechanics, and 30 production banking SQL queries.
  * [`03_PREDICTIVE_MODELING_ML_AND_CREDIT_RISK.md`](company-specific-prep/citicorp-aim-analytics/03_PREDICTIVE_MODELING_ML_AND_CREDIT_RISK.md) — Credit scorecard development, WoE, IV, KS statistic, and Population Stability Index (PSI).
  * [`04_BANKING_CASES_VISUALIZATION_AND_EXECUTIVE_STORYTELLING.md`](company-specific-prep/citicorp-aim-analytics/04_BANKING_CASES_VISUALIZATION_AND_EXECUTIVE_STORYTELLING.md) — 10 end-to-end banking cases, MECE issue trees, and visualization traps.
  * [`05_BANKING_COMPLIANCE_BEHAVIORAL_AND_HWRE_DEFENSE.md`](company-specific-prep/citicorp-aim-analytics/05_BANKING_COMPLIANCE_BEHAVIORAL_AND_HWRE_DEFENSE.md) — SR 11-7 model governance, AML/ECOA compliance, and engineering thesis defense.
  * [`06_MOCK_TESTS_QUESTION_BANK_AND_RAPID_REVISION.md`](company-specific-prep/citicorp-aim-analytics/06_MOCK_TESTS_QUESTION_BANK_AND_RAPID_REVISION.md) — Diagnostic mock, 3 sectional mocks, 75-min full mock, and multi-tier question bank.
  * Governance: [`PLACEMENT_FACTS.md`](company-specific-prep/citicorp-aim-analytics/PLACEMENT_FACTS.md), [`STUDY_GUIDE.md`](company-specific-prep/citicorp-aim-analytics/STUDY_GUIDE.md), [`READINESS_SCORECARD.md`](company-specific-prep/citicorp-aim-analytics/READINESS_SCORECARD.md).

### 4.3 Deloitte US-India — Analyst (AI, Analytics & Technology Consulting)
* **Target Package**: [`company-specific-prep/deloitte-analyst-ai-analytics/`](company-specific-prep/deloitte-analyst-ai-analytics/README.md)
* **Core Profile**: Technology consulting, applied artificial intelligence, enterprise lakehouse data engineering, business process transformation (S2P/O2C), and consultative problem solving.
* **Master Architecture**:
  * [`01_APTITUDE_AND_ENGLISH_PREP.md`](company-specific-prep/deloitte-analyst-ai-analytics/01_APTITUDE_AND_ENGLISH_PREP.md) — Quantitative aptitude, logical reasoning, and verbal comprehension.
  * [`02_CODING_DSA_AND_SOFTWARE_ENGINEERING.md`](company-specific-prep/deloitte-analyst-ai-analytics/02_CODING_DSA_AND_SOFTWARE_ENGINEERING.md) — Python data structures, algorithms, and software design principles.
  * [`03_DATA_SQL_AND_ANALYTICS.md`](company-specific-prep/deloitte-analyst-ai-analytics/03_DATA_SQL_AND_ANALYTICS.md) — Advanced SQL, lakehouse data engineering, and PySpark fundamentals.
  * [`04_ARTIFICIAL_INTELLIGENCE_AND_MACHINE_LEARNING.md`](company-specific-prep/deloitte-analyst-ai-analytics/04_ARTIFICIAL_INTELLIGENCE_AND_MACHINE_LEARNING.md) — Machine learning models, LLMs, enterprise RAG, and agentic workflows.
  * [`05_CONSULTING_BUSINESS_AND_INTERVIEW_PREP.md`](company-specific-prep/deloitte-analyst-ai-analytics/05_CONSULTING_BUSINESS_AND_INTERVIEW_PREP.md) — Business cases, enterprise ERP processes, and behavioral interview mastery.
  * [`06_MOCK_TESTS_QUESTION_BANK_AND_REVISION.md`](company-specific-prep/deloitte-analyst-ai-analytics/06_MOCK_TESTS_QUESTION_BANK_AND_REVISION.md) — 4 timed mock tests, 200-question multi-tier question bank, and rapid revision cheat sheet.
  * Governance: [`PLACEMENT_FACTS.md`](company-specific-prep/deloitte-analyst-ai-analytics/PLACEMENT_FACTS.md), [`STUDY_GUIDE.md`](company-specific-prep/deloitte-analyst-ai-analytics/STUDY_GUIDE.md), [`READINESS_SCORECARD.md`](company-specific-prep/deloitte-analyst-ai-analytics/READINESS_SCORECARD.md).

### 4.4 ExxonMobil — Engineer (Civil, HWRE, Energy & Facilities)
* **Target Package**: [`company-specific-prep/exxonmobil-engineer/`](company-specific-prep/exxonmobil-engineer/README.md)
* **Core Profile**: Energy infrastructure, technical engineering consulting, pipeline hydraulics, flow assurance, facilities engineering, and operational integrity management (OIMS).
* **Master Architecture**:
  * [`01_COMMON_ENGINEERING_APTITUDE_AND_PSYCHOMETRIC.md`](company-specific-prep/exxonmobil-engineer/01_COMMON_ENGINEERING_APTITUDE_AND_PSYCHOMETRIC.md) — Engineering quantitative aptitude, numerical reasoning, and psychometric/situational judgment.
  * [`02_CIVIL_CORE_ENGINEERING_AND_WORKBOOK.md`](company-specific-prep/exxonmobil-engineer/02_CIVIL_CORE_ENGINEERING_AND_WORKBOOK.md) — Broad civil engineering core: SOM, structural steel, RCC, geotech, and 56 graded non-HWRE workbook problems.
  * [`03_FLUID_MECHANICS_AND_HWRE_HYDRAULIC_SYSTEMS.md`](company-specific-prep/exxonmobil-engineer/03_FLUID_MECHANICS_AND_HWRE_HYDRAULIC_SYSTEMS.md) — Pipe networks, water hammer, pumps, cavitation, open-channel flow, sediment transport, and 17 multi-step numerical derivations.
  * [`04_ENERGY_FACILITIES_FLOW_ASSURANCE_AND_SAFETY_OIMS.md`](company-specific-prep/exxonmobil-engineer/04_ENERGY_FACILITIES_FLOW_ASSURANCE_AND_SAFETY_OIMS.md) — Flow assurance (hydrates, wax, asphaltenes), pressure piping, OIMS safety framework, HAZOP, and LOPA.
  * [`05_BEHAVIORAL_INTERVIEW_AND_HWRE_THESIS_DEFENSE.md`](company-specific-prep/exxonmobil-engineer/05_BEHAVIORAL_INTERVIEW_AND_HWRE_THESIS_DEFENSE.md) — M.Tech HWRE CFD thesis defense, oral technical problems, STAR safety behaviors, and Stop-Work Authority.
  * [`06_MOCK_ASSESSMENTS_QUESTION_BANK_AND_RAPID_REVISION.md`](company-specific-prep/exxonmobil-engineer/06_MOCK_ASSESSMENTS_QUESTION_BANK_AND_RAPID_REVISION.md) — 4 timed 90-question full mocks (360 questions), multi-tier question bank, and high-density formula matrix.
  * Governance: [`PLACEMENT_FACTS.md`](company-specific-prep/exxonmobil-engineer/PLACEMENT_FACTS.md), [`STUDY_GUIDE.md`](company-specific-prep/exxonmobil-engineer/STUDY_GUIDE.md), [`READINESS_SCORECARD.md`](company-specific-prep/exxonmobil-engineer/READINESS_SCORECARD.md).

### 4.5 Hilti (HTSI) — Graduate Engineer Trainee (Global Value Engineering Hub, Pune)
* **Target Package**: [`company-specific-prep/hilti-get-value-engineering/`](company-specific-prep/hilti-get-value-engineering/README.md)
* **Core Profile**: Energy & Industry (E&I) business unit, structural engineering design, post-installed anchorages (CCD method), modular MEP support conversion, and design optimization for global mega-projects.
* **Master Architecture (16-File Suite)**:
  * [`COMPANY_AND_ROLE_FACTS.md`](company-specific-prep/hilti-get-value-engineering/COMPANY_AND_ROLE_FACTS.md) — Verified facts, Pune hub mission, structured 8–12 mo training, salary benchmarks (`NOT VERIFIED`).
  * [`SELECTION_PROCESS_AND_EVIDENCE.md`](company-specific-prep/hilti-get-value-engineering/SELECTION_PROCESS_AND_EVIDENCE.md) — 4-stage recruitment pipeline, candidate profiles, and evidence classification.
  * [`STUDY_ROADMAP.md`](company-specific-prep/hilti-get-value-engineering/STUDY_ROADMAP.md) — 4-week structured preparation schedule, P0/P1/P2 priorities, and daily tracking.
  * [`01_STRUCTURAL_ENGINEERING_FUNDAMENTALS.md`](company-specific-prep/hilti-get-value-engineering/01_STRUCTURAL_ENGINEERING_FUNDAMENTALS.md) — 3D equilibrium, Mohr's circle, Euler buckling, deflection theorems, and 25 worked problems.
  * [`02_STEEL_RCC_AND_CONNECTION_DESIGN.md`](company-specific-prep/hilti-get-value-engineering/02_STEEL_RCC_AND_CONNECTION_DESIGN.md) — IS 800:2007, AISC 360, EN 1993, base plates, prying forces, welds, and 25 worked problems.
  * [`03_ANCHORS_SUPPORT_SYSTEMS_AND_FAILURE_MODES.md`](company-specific-prep/hilti-get-value-engineering/03_ANCHORS_SUPPORT_SYSTEMS_AND_FAILURE_MODES.md) — CCD method (ACI 318-19 / EN 1992-4), 8 failure modes, SafeSet, and 30 worked problems.
  * [`04_VALUE_ENGINEERING_AND_DESIGN_OPTIMISATION.md`](company-specific-prep/hilti-get-value-engineering/04_VALUE_ENGINEERING_AND_DESIGN_OPTIMISATION.md) — SAVE 6-phase plan, FAST diagram, modular channel vs welded steel, and 20 detailed VE cases.
  * [`05_ENGINEERING_CALCULATIONS_AND_NUMERICALS.md`](company-specific-prep/hilti-get-value-engineering/05_ENGINEERING_CALCULATIONS_AND_NUMERICALS.md) — 20 rigorous multi-step numerical calculation suites with step-by-step math.
  * [`06_HILTI_PRODUCTS_APPLICATIONS_AND_INDUSTRY_AWARENESS.md`](company-specific-prep/hilti-get-value-engineering/06_HILTI_PRODUCTS_APPLICATIONS_AND_INDUSTRY_AWARENESS.md) — MT/MQ modular channels, HST3, HUS4, HIT-RE 500 V4, PROFIS CBFEM, and competitors.
  * [`07_TECHNICAL_INTERVIEW_AND_CASE_STUDIES.md`](company-specific-prep/hilti-get-value-engineering/07_TECHNICAL_INTERVIEW_AND_CASE_STUDIES.md) — 25 deep technical interview prompts, 15 STAR behavioral scenarios, and ethics dilemmas.
  * [`08_APTITUDE_AND_ANALYTICAL_REASONING.md`](company-specific-prep/hilti-get-value-engineering/08_APTITUDE_AND_ANALYTICAL_REASONING.md) — Quantitative speed, spatial reasoning, pulleys/gears, and 30 solved problems.
  * [`09_MOCK_TESTS_AND_SOLUTIONS.md`](company-specific-prep/hilti-get-value-engineering/09_MOCK_TESTS_AND_SOLUTIONS.md) — 4 full-length calibrated technical mock tests (130 questions total) with worked solutions.
  * [`RAPID_REVISION.md`](company-specific-prep/hilti-get-value-engineering/RAPID_REVISION.md) — High-yield 60-minute formula cheatsheet, code matrices, and anchor sanity checks.
  * [`SOURCES_AND_VERIFICATION.md`](company-specific-prep/hilti-get-value-engineering/SOURCES_AND_VERIFICATION.md) — Provenance index, audit methodology, and verified recruitment sources.
  * [`READINESS_SCORECARD.md`](company-specific-prep/hilti-get-value-engineering/READINESS_SCORECARD.md) — 10-dimension evaluation rubric, benchmark metrics, and gap tracker.

### 4.6 Larsen & Toubro (L&T) — Post Graduate Engineer Trainee (PGET — Civil Engineering)
* **Target Package**: [`company-specific-prep/larsen-toubro-pget-civil/`](company-specific-prep/larsen-toubro-pget-civil/README.md)
* **Core Profile**: India's flagship engineering, procurement, and construction (EPC) multinational conglomerate. Intake spans 6 operational Independent Companies (ICs): Buildings & Factories (B&F), Transportation Infrastructure (TI), Heavy Civil Infrastructure (HCI), Water & Effluent Treatment (WET), Power Transmission & Distribution (PT&D), and Minerals & Metals Handling (MMH).
* **Compensation & Eligibility**:
  * **Office Postings**: CTC ₹6,25,360 (₹6.25 LPA).
  * **Site Postings**: CTC ₹6,80,000 (₹6.80 LPA).
  * **Post-Confirmation (Year 2)**: Office ₹8,00,000 (₹8.00 LPA) / Site ₹8,60,000 (₹8.60 LPA).
  * **Eligibility**: Minimum 65.0% or 6.50 CGPA across 10th, 12th, B.Tech, and M.Tech; strictly zero standing backlogs; mandatory PAN-India site mobility.
* **Master Architecture (18-File Comprehensive Suite)**:
  * [`README.md`](company-specific-prep/larsen-toubro-pget-civil/README.md) — Master syllabus roadmap, 6 IC operational guide, and evidentiary taxonomy.
  * [`COMPANY_AND_ROLE_FACTS.md`](company-specific-prep/larsen-toubro-pget-civil/COMPANY_AND_ROLE_FACTS.md) — Corporate facts, IC footprint, compensation breakdowns, and mobility obligations.
  * [`SELECTION_PROCESS_AND_EVIDENCE.md`](company-specific-prep/larsen-toubro-pget-civil/SELECTION_PROCESS_AND_EVIDENCE.md) — 4-stage recruitment pipeline, 120-Q / 120-min OA test mechanics, and evidence classification.
  * [`STUDY_ROADMAP.md`](company-specific-prep/larsen-toubro-pget-civil/STUDY_ROADMAP.md) — 1-day emergency, 3-day accelerated, 7-day complete, and 14-day foundation revision schedules.
  * [`RAPID_REVISION.md`](company-specific-prep/larsen-toubro-pget-civil/RAPID_REVISION.md) — 60-minute formula handbook, IS code tables, open-channel hydraulics, and CPM float matrices.
  * [`SOURCES_AND_VERIFICATION.md`](company-specific-prep/larsen-toubro-pget-civil/SOURCES_AND_VERIFICATION.md) — Statutory standards (IS, IRC, SP), corporate disclosures, and placement proforma audits.
  * [`READINESS_SCORECARD.md`](company-specific-prep/larsen-toubro-pget-civil/READINESS_SCORECARD.md) — 12-competency diagnostic rubric, scoring benchmark, and gap remediation tracks.
  * [`01_APTITUDE_AND_REASONING.md`](company-specific-prep/larsen-toubro-pget-civil/01_APTITUDE_AND_REASONING.md) — 100 fully solved aptitude, commercial math, logical deduction, and DI problems.
  * [`02_STRUCTURAL_ENGINEERING_AND_RCC.md`](company-specific-prep/larsen-toubro-pget-civil/02_STRUCTURAL_ENGINEERING_AND_RCC.md) — 30 solved problems (IS 456, IS 800, IS 1893, IS 13920, prestressing).
  * [`03_GEOTECHNICAL_AND_FOUNDATION_ENGINEERING.md`](company-specific-prep/larsen-toubro-pget-civil/03_GEOTECHNICAL_AND_FOUNDATION_ENGINEERING.md) — 25 solved problems (bearing capacity, pile load tests, settlement, earth pressures).
  * [`04_FLUID_MECHANICS_HYDRAULICS_AND_WATER_RESOURCES.md`](company-specific-prep/larsen-toubro-pget-civil/04_FLUID_MECHANICS_HYDRAULICS_AND_WATER_RESOURCES.md) — 25 solved problems (pipe networks, open canals, hydraulic jump, pumps NPSH, unit hydrographs).
  * [`05_ENVIRONMENTAL_AND_TRANSPORTATION_ENGINEERING.md`](company-specific-prep/larsen-toubro-pget-civil/05_ENVIRONMENTAL_AND_TRANSPORTATION_ENGINEERING.md) — 25 solved problems (sedimentation overflow, BOD kinetics, IRC superelevation, SSD, Westergaard).
  * [`06_CONSTRUCTION_MATERIALS_SURVEYING_AND_QS.md`](company-specific-prep/larsen-toubro-pget-civil/06_CONSTRUCTION_MATERIALS_SURVEYING_AND_QS.md) — 25 solved problems (IS 10262 mix design, reciprocal leveling, BBS bar schedules, prismoidal earthwork).
  * [`07_CONSTRUCTION_PLANNING_SAFETY_AND_QUALITY.md`](company-specific-prep/larsen-toubro-pget-civil/07_CONSTRUCTION_PLANNING_SAFETY_AND_QUALITY.md) — CPM/PERT floats, crashing, HIRA safety, PTW protocols, IS 456 Table 11 testing frequencies.
  * [`08_LNT_AND_EPC_INDUSTRY_AWARENESS.md`](company-specific-prep/larsen-toubro-pget-civil/08_LNT_AND_EPC_INDUSTRY_AWARENESS.md) — Landmark mega-projects (Statue of Unity, Atal Setu, Coastal Road, MAHSR), EPC lifecycle, and BIM Level 2/3.
  * [`09_TECHNICAL_INTERVIEW_AND_PROJECT_DISCUSSION.md`](company-specific-prep/larsen-toubro-pget-civil/09_TECHNICAL_INTERVIEW_AND_PROJECT_DISCUSSION.md) — M.Tech thesis EPC defense framework, 30 technical prompts + follow-ups, 20 site troubleshooting scenarios.
  * [`10_HR_BEHAVIOURAL_AND_COMMUNICATION.md`](company-specific-prep/larsen-toubro-pget-civil/10_HR_BEHAVIOURAL_AND_COMMUNICATION.md) — "Why L&T" strategic positioning, site resilience, PAN-India mobility, and 25 STAR behavioral prompts.
  * [`11_MOCK_TESTS_AND_SOLUTIONS.md`](company-specific-prep/larsen-toubro-pget-civil/11_MOCK_TESTS_AND_SOLUTIONS.md) — 4 complete mock assessments (Mock 1 Core Civil 60 Qs, Mock 2 Aptitude 60 Qs, Mock 3 Integrated 120 Qs, Mock 4 Site Scenarios 30 Qs; 270 total questions with full worked solutions).

### 4.7 Vantage Research — Scientist Modeler (Scientist 1 & Scientist 2 — QSP & PK/PD)
* **Target Package**: [`company-specific-prep/vantage-research-scientist-modeler/`](company-specific-prep/vantage-research-scientist-modeler/README.md)
* **Core Profile**: Contract Research Organization (CRO) specializing in Quantitative Systems Pharmacology (QSP), mechanistic PK/PD mathematical modeling, ODE/PDE dynamical systems, and pharmaceutical simulation.
* **Selection & Governance**: MSQ Assessment $\rightarrow$ Technical Interview R1 $\rightarrow$ Research & Problem-Solving R2; evaluated jointly for Scientist 1 and Scientist 2.

### 4.8 KLA Corporation — Applications Engineer (Semiconductor Yield / CAE Benchmark)
* **Target Package**: [`company-specific-prep/kla-applications-engineer/`](company-specific-prep/kla-applications-engineer/README.md)
* **Core Profile**: Market leader in Semiconductor Process Diagnostics & Control Equipment (~50% to >55% global market share per Gartner Market Share Analysis 2022/2023 and KLA SEC Form 10-K / Investor Day disclosures). Role centers on high-volume fab on-site yield troubleshooting, optical inspection recipe sensitivity tuning, killer defect elimination, BKM documentation, and Python/Perl fab data analytics.
* **Compensation & Travel**: CTC ₹28,50,000 (INR 28.50 LPA, fixed/variable breakdown unspecified in proforma); base location unspecified in proforma (KLA India centers in Chennai & Bengaluru); >80% international and domestic travel to semiconductor fabs worldwide.
* **Master Architecture (16-File Suite)**:
  * [`README.md`](company-specific-prep/kla-applications-engineer/README.md) — Master navigation hub, executive overview, directory map & 3-minute pivot narrative.
  * [`PLACEMENT_FACTS.md`](company-specific-prep/kla-applications-engineer/PLACEMENT_FACTS.md) — Audited proforma records, CTC ₹28.5L factsheet, >80% travel obligations, 5-tier taxonomy.
  * [`01_COMPANY_AND_ROLE_RESEARCH.md`](company-specific-prep/kla-applications-engineer/01_COMPANY_AND_ROLE_RESEARCH.md) — Corporate profile, semiconductor ecosystem, KLA product families (BPO, Surfscan, Archer, eSL10, Klarity), CAE day-to-day duties.
  * [`02_RECRUITMENT_PROCESS_AND_EVIDENCE.md`](company-specific-prep/kla-applications-engineer/02_RECRUITMENT_PROCESS_AND_EVIDENCE.md) — Selection workflow audit, proforma facts vs. reconstructed benchmarks, candidate interview reports, evidence ledger.
  * [`03_SEMICONDUCTOR_FUNDAMENTALS_AND_YIELD.md`](company-specific-prep/kla-applications-engineer/03_SEMICONDUCTOR_FUNDAMENTALS_AND_YIELD.md) — Wafer fabrication flow (FEOL/BEOL), Rayleigh litho equations, Preston CMP law, Poisson & Negative Binomial yield models.
  * [`04_INSPECTION_METROLOGY_AND_PROCESS_CONTROL.md`](company-specific-prep/kla-applications-engineer/04_INSPECTION_METROLOGY_AND_PROCESS_CONTROL.md) — Brightfield vs. Darkfield optics, overlay metrology, Shewhart charts ($\bar{X}-R$), Western Electric rules, $C_p / C_{pk}$ capability indices, RCA 5-Whys.
  * [`05_STATISTICS_DATA_ANALYTICS_AND_PYTHON.md`](company-specific-prep/kla-applications-engineer/05_STATISTICS_DATA_ANALYTICS_AND_PYTHON.md) — Statistical testing (t-test, ANOVA), KLARF inspection file standard, production Python KLARF parser class, ROC sensitivity tuning.
  * [`06_MACHINE_LEARNING_AND_PERL_SCRIPTING.md`](company-specific-prep/kla-applications-engineer/06_MACHINE_LEARNING_AND_PERL_SCRIPTING.md) — Automated Defect Classification (ADC) with XGBoost, imbalanced learning, SHAP explainability, 50-line fab Perl log parser.
  * [`07_ENGINEERING_PROBLEM_SOLVING_AND_CFD_PIVOT.md`](company-specific-prep/kla-applications-engineer/07_ENGINEERING_PROBLEM_SOLVING_AND_CFD_PIVOT.md) — Navier-Stokes transport to CMP slurry lubrication analogy, project defense (OpenFOAM, BridgeRisk), 3-minute pivot pitch.
  * [`08_CUSTOMER_FACING_SCENARIOS_AND_HR.md`](company-specific-prep/kla-applications-engineer/08_CUSTOMER_FACING_SCENARIOS_AND_HR.md) — Cleanroom fab operations, 5-phase escalation management, BKM template, >80% travel defense, STAR behavioral models.
  * [`09_SIMULATED_ASSESSMENT_AND_QUESTION_BANK.md`](company-specific-prep/kla-applications-engineer/09_SIMULATED_ASSESSMENT_AND_QUESTION_BANK.md) — 15 rigorous practice questions with complete mathematical derivations, distractor refutations, and concepts.
  * [`10_TECHNICAL_INTERVIEW_AND_CASE_STUDIES.md`](company-specific-prep/kla-applications-engineer/10_TECHNICAL_INTERVIEW_AND_CASE_STUDIES.md) — 4 deep fab engineering troubleshooting case studies + comprehensive Q&A bank across three difficulty tiers.
  * [`11_PRACTICE_PROJECTS_PORTFOLIO.md`](company-specific-prep/kla-applications-engineer/11_PRACTICE_PROJECTS_PORTFOLIO.md) — 4 end-to-end reproducible projects (Wafer clustering, ADC XGBoost/SHAP, SPC engine, CMP fluid dynamics).
  * [`READINESS_SCORECARD.md`](company-specific-prep/kla-applications-engineer/READINESS_SCORECARD.md) — Competency matrix, gap analysis, and 10-point pre-interview verification checklist.
  * [`STUDY_GUIDE.md`](company-specific-prep/kla-applications-engineer/STUDY_GUIDE.md) — 4-week structured preparation timeline, daily milestones, and revision strategy.
  * [`SOURCES.md`](company-specific-prep/kla-applications-engineer/SOURCES.md) — Complete research evidence ledger with citations, source tiers, access dates, and confidence ratings.

---

## 5. Maintenance & Quality Control Workflow

To preserve documentation integrity throughout the placement season:
1. **Link Verification**: Every relative link must resolve to a valid existing file. Verify using automated scripts before committing changes.
2. **Personal Data Isolation**: Keep project defense frameworks candidate-adaptable and generic. Do not hardcode individual thesis titles or private repo paths.
3. **No Speculative Scaffolding**: Never commit empty files or placeholder lists. Every document must contain substantive, actionable study guidance.
4. **Source Attribution**: Always cite source documents (`[IITK PLACEMENT SOURCE]`, `[OFFICIAL COMPANY SOURCE]`) when adding newly announced campus recruitment drives.

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
    └── exxonmobil-engineer/       # ExxonMobil (EMSTPL) — Engineer (Civil, HWRE, Energy & Facilities) Pack
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
| **Dedicated Prep Packs** | [`company-specific-prep/`](company-specific-prep/) | Comprehensive, multi-module interview preparation packages built for high-priority hiring drives. | [Accenture Japan](company-specific-prep/accenture-japan/README.md) (Digital Consultant)<br>[Citi AIM Analytics](company-specific-prep/citicorp-aim-analytics/README.md) (Business Analytics SBS)<br>[Deloitte USI Analyst](company-specific-prep/deloitte-analyst-ai-analytics/README.md) (AI, Analytics & Tech Consulting)<br>[ExxonMobil Engineer](company-specific-prep/exxonmobil-engineer/README.md) (Engineer — Civil & HWRE). |

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

---

## 5. Maintenance & Quality Control Workflow

To preserve documentation integrity throughout the placement season:
1. **Link Verification**: Every relative link must resolve to a valid existing file. Verify using automated scripts before committing changes.
2. **Personal Data Isolation**: Keep project defense frameworks candidate-adaptable and generic. Do not hardcode individual thesis titles or private repo paths.
3. **No Speculative Scaffolding**: Never commit empty files or placeholder lists. Every document must contain substantive, actionable study guidance.
4. **Source Attribution**: Always cite source documents (`[IITK PLACEMENT SOURCE]`, `[OFFICIAL COMPANY SOURCE]`) when adding newly announced campus recruitment drives.

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
    └── citicorp-aim-analytics/    # Citicorp (CSIPL) — Business Analytics (SBS) AIM Package
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
| **Dedicated Prep Packs** | [`company-specific-prep/`](company-specific-prep/) | Comprehensive, multi-module interview preparation packages built for high-priority hiring drives. | [Accenture Japan](company-specific-prep/accenture-japan/README.md) (Digital Consultant)<br>[Citi AIM Analytics](company-specific-prep/citicorp-aim-analytics/README.md) (Business Analytics SBS). |

---

## 4. End-to-End Dedicated Preparation Packs

For flagship campus opportunities with verified job descriptions or placement proformas, comprehensive deep-dive preparation suites are maintained:

### 4.1 Accenture Japan — Digital Consultant (Analyst Entry)
* **Target Package**: [`company-specific-prep/accenture-japan/`](company-specific-prep/accenture-japan/README.md)
* **Core Profile**: Technology-agnostic digital transformation (DX), Enterprise Architecture, Cloud Migration, and Industry X smart systems.
* **Key Components**:
  * [`ROLE.md`](company-specific-prep/accenture-japan/ROLE.md) & [`PLACEMENT_FACTS.md`](company-specific-prep/accenture-japan/PLACEMENT_FACTS.md) — Role identity, 3 career tracks, verified JPY 8.21M compensation breakdown.
  * [`TECHNICAL_TEST.md`](company-specific-prep/accenture-japan/TECHNICAL_TEST.md) — 30 SQL queries, 20 Python algorithms, and 20 business math drills.
  * [`CONSULTING_CASES.md`](company-specific-prep/accenture-japan/CONSULTING_CASES.md) — 15 structured DX/Industry X business cases, 15 issue trees, and 10 Tokyo market-sizing guesstimates.
  * [`QUESTION_BANK.md`](company-specific-prep/accenture-japan/QUESTION_BANK.md) & [`INTERVIEW.md`](company-specific-prep/accenture-japan/INTERVIEW.md) — Manager (R1) vs Director (R2) interview strategies with model answers.
  * [`PROJECT_STRATEGY.md`](company-specific-prep/accenture-japan/PROJECT_STRATEGY.md) — Defensible quantitative engineering project defense across 3 adaptable archetypes.
  * [`JAPAN_RELOCATION_AND_LANGUAGE.md`](company-specific-prep/accenture-japan/JAPAN_RELOCATION_AND_LANGUAGE.md) — Relocation roadmap and 18-month JLPT Japanese progression plan.

### 4.2 Citicorp Services India — Business Analytics (SBS), Citi AIM
* **Target Package**: [`company-specific-prep/citicorp-aim-analytics/`](company-specific-prep/citicorp-aim-analytics/README.md)
* **Core Profile**: Analytics and Information Management (AIM) global community delivering financial insights, predictive scoring, and data manipulation.
* **Key Components**:
  * [`PLACEMENT_FACTS.md`](company-specific-prep/citicorp-aim-analytics/PLACEMENT_FACTS.md) — Verified Phase 1 proforma breakdown (₹15.29L CTC + ₹2L relocation).
  * [`01_STATISTICS_PROBABILITY.md`](company-specific-prep/citicorp-aim-analytics/01_STATISTICS_PROBABILITY.md) — Probability distributions, hypothesis testing (Z/t/Chi-Square/ANOVA), and heavy-tailed risk metrics.
  * [`02_SQL_DATA_MANIPULATION.md`](company-specific-prep/citicorp-aim-analytics/02_SQL_DATA_MANIPULATION.md) — 30 banking SQL queries covering window functions, CTEs, roll rates, and data quality diagnostics.
  * [`03_PREDICTIVE_MODELING_ML.md`](company-specific-prep/citicorp-aim-analytics/03_PREDICTIVE_MODELING_ML.md) — Credit scoring, logistic regression, KS statistic, PSI, RFM, and K-Means segmentation.
  * [`04_INTERVIEW_AND_CASES.md`](company-specific-prep/citicorp-aim-analytics/04_INTERVIEW_AND_CASES.md) — 10 end-to-end retail banking analytics cases, analytical deduction puzzles, and guesstimates.
  * [`07_PROJECT_AND_RESUME_DEFENCE.md`](company-specific-prep/citicorp-aim-analytics/07_PROJECT_AND_RESUME_DEFENCE.md) — Grounded mapping of quantitative engineering research to banking analytics.

---

## 5. Maintenance & Quality Control Workflow

To preserve documentation integrity throughout the placement season:
1. **Link Verification**: Every relative link must resolve to a valid existing file. Verify using automated scripts before committing changes.
2. **Personal Data Isolation**: Keep project defense frameworks candidate-adaptable and generic. Do not hardcode individual thesis titles or private repo paths.
3. **No Speculative Scaffolding**: Never commit empty files or placeholder lists. Every document must contain substantive, actionable study guidance.
4. **Source Attribution**: Always cite source documents (`[IITK PLACEMENT SOURCE]`, `[OFFICIAL COMPANY SOURCE]`) when adding newly announced campus recruitment drives.

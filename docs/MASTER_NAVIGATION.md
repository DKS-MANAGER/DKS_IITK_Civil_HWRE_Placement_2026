# Master Navigation

> **Single routing document.** Find any resource in ≤3 clicks (Design Target) across tracks, roles, testing layers, or companies.

---

## 1. The Three Structural Dimensions

The repository organizes placement preparation along three orthogonal dimensions (see [architecture.md](architecture.md)):

```
       DOMAIN (What subject?)
         ├── Core Civil & HWRE
         ├── Quantitative & Logical Aptitude
         ├── Non-Core Business & Strategy
         └── Software, Data & Computing
                   ↓
       CAREER TARGET (What corporate role?)
         ├── Core HWRE / Water Resources / Infrastructure
         ├── CFD / Hydrodynamics / Thermal Fluids R&D
         ├── Public Sector Undertakings (PSUs)
         ├── Management Consulting & Corporate Strategy
         ├── Data Science, BI & Quantitative Analytics
         └── Product Management & Technology Operations
                   ↓
       PREPARATION STAGE (What are you doing today?)
         ├── Learn: Deep conceptual notes & governing equations
         ├── Practice: Granular topic drills, sectionals & full mocks
         ├── Interview: Branching question trees, case dialogues, STAR-L stories
         └── Revise: Rapid revision sheets, formula cards & cheat sheets
```

---

## 2. Route by Preparation Track

| Track | Core Coverage Scope | Primary Entry Point |
|:------|:---|:------------|
| **Core Civil Engineering** | Structures, Geotechnical, Transportation, Environmental | [`02_core/README.md`](../README.md) |
| **HWRE & Hydrodynamics** | Open Channel Flow, Hydrology, CFD, Coastal, Groundwater | [`02_core/hwre/README.md`](../02_core/hwre/README.md) |
| **Aptitude & Reasoning** | 720 Quant Qs, 10 DI Chapters, 9 Verbal Modules, 17 Topic Tests, 5 Sectionals, 7 Full Mocks | [`01_common/aptitude/README.md`](../01_common/aptitude/README.md) |
| **Non-Core & Consulting** | Consulting Cases, Business Fundamentals, Guesstimates, Finance, Product | [`03_non_core/README.md`](../03_non_core/README.md) |
| **Software & Analytics** | Python, SQL, Git, Linux, C++, Data Structures & Algorithms | [`archive/legacy_software/README.md`](../archive/legacy_software/README.md) |
| **Central Execution Hub** | Master Plan, Readiness Scorecard, Technical Bank, Company Profiles | [`archive/legacy_archive/legacy_prep/README.md`](../archive/legacy_prep/README.md) |

*Full detail → [TRACKS.md](TRACKS.md) · [IITK_PLACEMENT_MAP.md](IITK_PLACEMENT_MAP.md)*

---

## 3. Route by Preparation Stage

| Stage | What You Need | Primary Entry Points |
|:------|:--------------|:---------------------|
| **Learn** | Concept notes, derivations, IS codes | [`02_core/`](../02_core/) · [`01_common/aptitude/quantitative/`](../01_common/aptitude/quantitative/README.md) · [`01_common/placement-math/`](../01_common/placement-math/) |
| **Practice (L1–L2)** | Topic diagnostics & pure domain sectionals | [`01_common/aptitude/mocks/section-tests/`](../01_common/aptitude/mocks/section-tests/README.md) · [`01_common/aptitude/mocks/section-tests/section/`](../01_common/aptitude/mocks/section-tests/section/README.md) |
| **Mock (L3–L5)** | Full placement mocks & company OAs | [`01_common/aptitude/mocks/`](../01_common/aptitude/mocks/README.md) · [`05_interview/mock-interviews/mock-tests/`](../05_interview/mock-interviews/mock-tests/README.md) |
| **Interview (L6–L7)**| Technical branching trees & case simulations | [`01_common/interview-fundamentals/technical/`](../05_interview/technical/technical-interview-bank.md) · [`05_interview/case-interview/case-interviews/`](../05_interview/case-interview/case-interviews/case-simulation-suite.md) |
| **Simulate (L8)** | 45-min end-to-end interview & scorecard | [`05_interview/mock-interviews/MOCK_INTERVIEW.md`](../05_interview/mock-interviews/MOCK_INTERVIEW.md) · [`05_interview/mock-interviews/READINESS_SCORECARD.md`](../05_interview/mock-interviews/READINESS_SCORECARD.md) |
| **Revise** | Formula sheets & rapid revision | [RAPID_REVISION_GUIDE.md](../06_revision/RAPID_REVISION_GUIDE.md) · [`01_common/aptitude/rapid-revision/FORMULA_SHEET.md`](../01_common/aptitude/rapid-revision/FORMULA_SHEET.md) |

---

## 4. Route by Placement Role & Recruiter Target

| Role Target | Target Companies at IITK | Core Prep Pathway | Testing & Interview Assets |
|:---|:---|:---|:---|
| **HWRE / Water Resources** | Vassarlabs, Rodic Consultants, DHI, AECOM | [`02_core/hwre/`](../02_core/hwre/) · [`07_resources/reference-material/gis-tools.md`](../07_resources/reference-material/gis-tools.md) | [Test Water Resources OA](../05_interview/mock-interviews/mock-tests/mock-test-water-resources.md) · [Tech Bank](../05_interview/technical/technical-interview-bank.md) |
| **CFD / Hydrodynamics R&D** | TuTr Hyperloop, Dimension Renewables, ANSYS | [`02_core/hwre/hydraulics/`](../02_core/hwre/hydraulics/) · [`01_common/interview-fundamentals/technical/project-defense-guide.md`](../05_interview/project-defense/project-defense-guide.md) | [Test Hydraulics CFD](../05_interview/mock-interviews/mock-tests/mock-test-hydraulics-cfd.md) · [Navier-Stokes Tree](../05_interview/technical/technical-interview-bank.md) |
| **Core Civil Infrastructure** | L&T, Godrej Properties, Tata Projects, Afcons | [`02_core/civil-engineering/structures/`](../02_core/civil-engineering/structures/) · [`02_core/civil-engineering/geotechnical/`](../02_core/civil-engineering/geotechnical/) | [Test Civil General OA](../05_interview/mock-interviews/mock-tests/mock-test-civil-general.md) · [Civil Core Sectional](../01_common/aptitude/mocks/section-tests/section/sectional-civil-core-01.md) |
| **PSU Engineering** | BPCL, HPCL, IOCL, ONGC, GAIL | [`02_core/`](../02_core/) · [`04_company-prep/core-companies/civil-bpcl.md`](../04_company-prep/core-companies/civil-bpcl.md) | [GATE Question Engine](../05_interview/technical/questions-bank-overview.md) · [Technical Interview Bank](../05_interview/technical/technical-interview-bank.md) |
| **Management Consulting** | McKinsey, BCG, Bain, Kearney, Strategy& | [`03_non_core/consulting/`](../03_non_core/consulting/) · [`05_interview/case-interview/case-interviews/`](../05_interview/case-interview/case-interviews/) | [Full Mock 03/04](../01_common/aptitude/mocks/README.md) · [Case Simulation Suite](../05_interview/case-interview/case-interviews/case-simulation-suite.md) |
| **Data Analytics / Tech PM** | Google, Amazon, Flipkart, Tiger Analytics | [`03_non_core/analytics/data-analyst/`](../03_non_core/analytics/data-analyst/) · [`03_non_core/product/product-management/`](../03_non_core/product/product-management/) | [Role Mock Tests](../05_interview/mock-interviews/mock-tests/README.md) · [DI Sectional Test](../01_common/aptitude/mocks/section-tests/section/sectional-di-01.md) |

*Full role profiles → [ROLES.md](..\03_non_core\README.md) · [COMPANIES.md](..\04_company-prep\README.md)*

---

## 5. Master Navigation Index

| Quick Link | Destination Document | Functional Purpose |
|:-----------|:---------------------|:-------------------|
| **Getting Started** | [GETTING_STARTED.md](GETTING_STARTED.md) | Onboarding orientation (first 15 minutes) |
| **Daily How-To** | [HOW_TO_USE.md](HOW_TO_USE.md) | Daily study workflows by time & goal |
| **IITK Placement Map** | [IITK_PLACEMENT_MAP.md](IITK_PLACEMENT_MAP.md) | Dedicated operational guide for IITK M.Tech candidates |
| **Assessment Ladder** | [ASSESSMENT_ARCHITECTURE.md](../05_interview/mock-interviews/ASSESSMENT_ARCHITECTURE.md) | Complete 8-level testing framework & score heuristics |
| **Testing Guide** | [TESTING_GUIDE.md](../05_interview/mock-interviews/TESTING_GUIDE.md) | Testing directory & error triage protocols |
| **Readiness Control Panel** | [`05_interview/mock-interviews/READINESS_SCORECARD.md`](../05_interview/mock-interviews/READINESS_SCORECARD.md) | 100-point composite readiness dashboard & mock logger |
| **End-to-End Workflow** | [PREPARATION_WORKFLOW.md](PREPARATION_WORKFLOW.md) | 6-stage lifecycle from Learn to Offer Letter |
| **Technical Interview Bank**| [`01_common/interview-fundamentals/technical/`](../05_interview/technical/technical-interview-bank.md) | 10 branching technical question trees |
| **Consulting Simulations** | [`05_interview/case-interview/case-interviews/`](../05_interview/case-interview/case-interviews/case-simulation-suite.md) | Full dialogue case interview simulation suite |
| **Content Standards** | [content-standards.md](content-standards.md) | 8 quality gates & definition of done |
| **Source Provenance** | [SOURCE_POLICY.md](SOURCE_POLICY.md) · [`07_resources/reference-material/source-registry.md`](../07_resources/reference-material/source-registry.md) | 6-level canonical evidence taxonomy |

---

> **Back to:** [README](README.md) · [Main README](../README.md)


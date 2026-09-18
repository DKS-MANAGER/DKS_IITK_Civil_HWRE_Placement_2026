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
| **Core Civil Engineering** | Structures, Geotechnical, Transportation, Environmental | [`core/README.md`](../core/README.md) |
| **HWRE & Hydrodynamics** | Open Channel Flow, Hydrology, CFD, Coastal, Groundwater | [`core/hwre/README.md`](../core/hwre/README.md) |
| **Aptitude & Reasoning** | 720 Quant Qs, 10 DI Chapters, 9 Verbal Modules, 17 Topic Tests, 5 Sectionals, 7 Full Mocks | [`aptitude/README.md`](../aptitude/README.md) |
| **Non-Core & Consulting** | Consulting Cases, Business Fundamentals, Guesstimates, Finance, Product | [`non-core/README.md`](../non-core/README.md) |
| **Software & Analytics** | Python, SQL, Git, Linux, C++, Data Structures & Algorithms | [`software-and-tech/README.md`](../software-and-tech/README.md) |
| **Central Execution Hub** | Master Plan, Readiness Scorecard, Technical Bank, Company Profiles | [`prep/README.md`](../prep/README.md) |

*Full detail → [TRACKS.md](TRACKS.md) · [IITK_PLACEMENT_MAP.md](IITK_PLACEMENT_MAP.md)*

---

## 3. Route by Preparation Stage

| Stage | What You Need | Primary Entry Points |
|:------|:--------------|:---------------------|
| **Learn** | Concept notes, derivations, IS codes | [`core/`](../core/) · [`aptitude/quant/`](../aptitude/quant/README.md) · [`non-core/03_common-skills/`](../non-core/03_common-skills/) |
| **Practice (L1–L2)** | Topic diagnostics & pure domain sectionals | [`aptitude/tests/`](../aptitude/tests/README.md) · [`aptitude/tests/section/`](../aptitude/tests/section/README.md) |
| **Mock (L3–L5)** | Full placement mocks & company OAs | [`aptitude/mocks/`](../aptitude/mocks/README.md) · [`prep/mock-tests/`](../prep/mock-tests/README.md) |
| **Interview (L6–L7)**| Technical branching trees & case simulations | [`prep/interview/technical/`](../prep/interview/technical/technical-interview-bank.md) · [`non-core/02_interview-preparation/case-interviews/`](../non-core/02_interview-preparation/case-interviews/case-simulation-suite.md) |
| **Simulate (L8)** | 45-min end-to-end interview & scorecard | [`prep/MOCK_INTERVIEW.md`](../prep/MOCK_INTERVIEW.md) · [`prep/READINESS_SCORECARD.md`](../prep/READINESS_SCORECARD.md) |
| **Revise** | Formula sheets & rapid revision | [RAPID_REVISION_GUIDE.md](RAPID_REVISION_GUIDE.md) · [`aptitude/FORMULA_SHEET.md`](../aptitude/FORMULA_SHEET.md) |

---

## 4. Route by Placement Role & Recruiter Target

| Role Target | Target Companies at IITK | Core Prep Pathway | Testing & Interview Assets |
|:---|:---|:---|:---|
| **HWRE / Water Resources** | Vassarlabs, Rodic Consultants, DHI, AECOM | [`core/hwre/`](../core/hwre/) · [`resources/gis-tools.md`](../resources/gis-tools.md) | [Test Water Resources OA](../prep/mock-tests/mock-test-water-resources.md) · [Tech Bank](../prep/interview/technical/technical-interview-bank.md) |
| **CFD / Hydrodynamics R&D** | TuTr Hyperloop, Dimension Renewables, ANSYS | [`core/hwre/hydraulics/`](../core/hwre/hydraulics/) · [`prep/interview/technical/project-defense-guide.md`](../prep/interview/technical/project-defense-guide.md) | [Test Hydraulics CFD](../prep/mock-tests/mock-test-hydraulics-cfd.md) · [Navier-Stokes Tree](../prep/interview/technical/technical-interview-bank.md) |
| **Core Civil Infrastructure** | L&T, Godrej Properties, Tata Projects, Afcons | [`core/structures/`](../core/structures/) · [`core/geotechnical/`](../core/geotechnical/) | [Test Civil General OA](../prep/mock-tests/mock-test-civil-general.md) · [Civil Core Sectional](../aptitude/tests/section/sectional-civil-core-01.md) |
| **PSU Engineering** | BPCL, HPCL, IOCL, ONGC, GAIL | [`core/`](../core/) · [`prep/company-profiles/civil-bpcl.md`](../prep/company-profiles/civil-bpcl.md) | [GATE Question Engine](../questions/README.md) · [Technical Interview Bank](../prep/interview/technical/technical-interview-bank.md) |
| **Management Consulting** | McKinsey, BCG, Bain, Kearney, Strategy& | [`non-core/01_roles/consulting/`](../non-core/01_roles/consulting/) · [`non-core/02_interview-preparation/case-interviews/`](../non-core/02_interview-preparation/case-interviews/) | [Full Mock 03/04](../aptitude/mocks/README.md) · [Case Simulation Suite](../non-core/02_interview-preparation/case-interviews/case-simulation-suite.md) |
| **Data Analytics / Tech PM** | Google, Amazon, Flipkart, Tiger Analytics | [`non-core/01_roles/data-analyst/`](../non-core/01_roles/data-analyst/) · [`non-core/01_roles/product-management/`](../non-core/01_roles/product-management/) | [Role Mock Tests](../prep/mock-tests/README.md) · [DI Sectional Test](../aptitude/tests/section/sectional-di-01.md) |

*Full role profiles → [ROLES.md](ROLES.md) · [COMPANIES.md](COMPANIES.md)*

---

## 5. Master Navigation Index

| Quick Link | Destination Document | Functional Purpose |
|:-----------|:---------------------|:-------------------|
| **Getting Started** | [GETTING_STARTED.md](GETTING_STARTED.md) | Onboarding orientation (first 15 minutes) |
| **Daily How-To** | [HOW_TO_USE.md](HOW_TO_USE.md) | Daily study workflows by time & goal |
| **IITK Placement Map** | [IITK_PLACEMENT_MAP.md](IITK_PLACEMENT_MAP.md) | Dedicated operational guide for IITK M.Tech candidates |
| **Assessment Ladder** | [ASSESSMENT_ARCHITECTURE.md](ASSESSMENT_ARCHITECTURE.md) | Complete 8-level testing framework & score heuristics |
| **Testing Guide** | [TESTING_GUIDE.md](TESTING_GUIDE.md) | Testing directory & error triage protocols |
| **Readiness Control Panel** | [`prep/READINESS_SCORECARD.md`](../prep/READINESS_SCORECARD.md) | 100-point composite readiness dashboard & mock logger |
| **End-to-End Workflow** | [PREPARATION_WORKFLOW.md](PREPARATION_WORKFLOW.md) | 6-stage lifecycle from Learn to Offer Letter |
| **Technical Interview Bank**| [`prep/interview/technical/`](../prep/interview/technical/technical-interview-bank.md) | 10 branching technical question trees |
| **Consulting Simulations** | [`non-core/02_interview-preparation/case-interviews/`](../non-core/02_interview-preparation/case-interviews/case-simulation-suite.md) | Full dialogue case interview simulation suite |
| **Content Standards** | [content-standards.md](content-standards.md) | 8 quality gates & definition of done |
| **Source Provenance** | [SOURCE_POLICY.md](SOURCE_POLICY.md) · [`resources/source-registry.md`](../resources/source-registry.md) | 6-level canonical evidence taxonomy |

---

> **Back to:** [README](README.md) · [Main README](../README.md)


# 03_NON_CORE — Non-Core Placement Preparation Hub

> **Target Audience**: IIT Kanpur students—specifically Civil Engineering and M.Tech Hydraulics & Water Resources Engineering (HWRE) candidates—preparing for non-core campus recruitment.  
> **Scope & Purpose**: A structured, self-contained curriculum covering role selection, domain fundamentals, analytical frameworks, worked case studies, coding patterns, and full mock assessments across 7 major non-core job families.  
> **Placement Variance Notice**: Campus recruitment processes, shortlisting criteria, test formats, and compensation terms vary significantly by company, role, and recruitment season. Eligibility for non-core roles depends strictly on employer proformas submitted to the IIT Kanpur Students' Placement Office (SPO). Treat all company listings, test patterns, and historical salary figures as indicative preparation references, not as official guarantees.

---

## 1. Non-Core Preparation Architecture & Directory Layout

```text
03_non_core/
├── README.md                      # Non-core master dashboard & role-selection strategy
├── ROLE_DIRECTORY.md              # Detailed profile breakdowns, competencies & syllabus index
├── ROLES.md                       # High-level role-to-resource quick reference
├── consulting/                    # Management & Strategy Consulting (MECE, Issue Trees, Cases, Guesstimates)
│   ├── strategy/                  # Corporate Strategy, Market Entry, M&A & Growth
│   ├── worked_cases/              # Deep-dive business case walkthroughs
│   └── lessons/                   # Structured problem solving & consulting math
├── analytics/                     # Core Business & Data Analytics Tracks
│   ├── analytics/                 # Full Analytics curriculum (SQL, Python, Statistics, ML)
│   ├── business-analyst/          # Requirements gathering, BPMN, dashboards, metrics
│   └── data-analyst/              # Exploratory data analysis, SQL window functions, BI reporting
├── data-science/                  # Machine Learning, Statistical Inference & Data Analytics Stack
├── finance/                       # Corporate Finance & Quantitative Risk Analytics
│   ├── finance/                   # 3-Statement financial modeling, DCF, WACC, Capital Budgeting
│   └── risk/                      # Credit Risk, Market Risk (VaR), Basel III & Stress Testing
├── operations/                    # Operations Research & Execution Management
│   ├── operations/                # Plant operations, Little's Law, EOQ, Line Balancing, Six Sigma
│   ├── business-operations/       # BizOps, unit economics, dark store scaling, SLA governance
│   ├── supply-chain/              # SCM, multi-echelon networks, Bullwhip effect, logistics
│   └── program-management/        # CPM/PERT scheduling, EVM tracking, RACI governance
├── product/                       # Product Management & Product Telemetry
│   ├── product-management/        # Product sense (CIRCLES), PRDs, feature prioritization (RICE)
│   └── product-analyst/           # Telemetry schemas, funnel conversion, A/B testing (SRM, CUPED)
└── software-engineering/          # Software Development & Systems Engineering
    ├── programming/               # Python, C++, SQL, Algorithms, Data Structures
    └── developer-tools/           # Git, Linux, Docker, CI/CD, APIs & System Design
```

---

## 2. Master Navigation & Role Directory Matrix

The table below maps each non-core job family to its canonical study track, core practice modules, and comprehensive mock assessments:

| Role Family | Canonical Study Track | Practice & Cases Module | Mock Assessment | Primary Skills Evaluated |
| :--- | :--- | :--- | :--- | :--- |
| **Management Consulting** | [`consulting/README.md`](consulting/README.md) | [`consulting/07_practice-and-cases.md`](consulting/07_practice-and-cases.md) | [`consulting/12_mock-assessment.md`](consulting/12_mock-assessment.md) | Structured Problem Solving, MECE Issue Trees, Market Sizing, Profitability Diagnostics |
| **Business Analyst (BA)** | [`analytics/business-analyst/01_role-overview.md`](analytics/business-analyst/01_role-overview.md) | [`analytics/business-analyst/07_case-practice.md`](analytics/business-analyst/07_case-practice.md) | [`analytics/business-analyst/12_mock-assessment.md`](analytics/business-analyst/12_mock-assessment.md) | Business Requirements, SQL Data Extraction, KPI Dashboards, Process Mapping (BPMN) |
| **Data Analyst (DA)** | [`analytics/data-analyst/01_role-overview.md`](analytics/data-analyst/01_role-overview.md) | [`analytics/data-analyst/07_practice-and-cases.md`](analytics/data-analyst/07_practice-and-cases.md) | [`analytics/data-analyst/12_mock-assessment.md`](analytics/data-analyst/12_mock-assessment.md) | Advanced SQL (Window Functions), Descriptive Statistics, Tableau/Power BI, Cohorts |
| **Analytics & Data Science** | [`analytics/analytics/01_role-overview.md`](analytics/analytics/01_role-overview.md) | [`data-science/data-analytics-stack.md`](data-science/data-analytics-stack.md) | [`analytics/analytics/12_mock-assessment.md`](analytics/analytics/12_mock-assessment.md) | Python (Pandas/Scikit-Learn), Statistical Modeling, Hypothesis Testing, ML Algorithms |
| **Corporate Finance & FP&A** | [`finance/finance/01_role-overview.md`](finance/finance/01_role-overview.md) | [`finance/finance/07_practice-and-cases.md`](finance/finance/07_practice-and-cases.md) | [`finance/finance/12_mock-assessment.md`](finance/finance/12_mock-assessment.md) | 3-Statement Linking, DCF Valuation, WACC, Working Capital, Ratio Analysis |
| **Risk Management & Quant** | [`finance/risk/01_role-overview.md`](finance/risk/01_role-overview.md) | [`finance/risk/07_practice-and-cases.md`](finance/risk/07_practice-and-cases.md) | [`finance/risk/12_mock-assessment.md`](finance/risk/12_mock-assessment.md) | Value-at-Risk (VaR), Credit Risk Scorecards, Basel III Capital, Stress Testing |
| **Business Operations (BizOps)** | [`operations/business-operations/01_role-overview.md`](operations/business-operations/01_role-overview.md) | [`operations/business-operations/07_practice-and-cases.md`](operations/business-operations/07_practice-and-cases.md) | [`operations/business-operations/12_mock-assessment.md`](operations/business-operations/12_mock-assessment.md) | Unit Economics (CM1/CM2/CM3), SLA Governance, Dark Store Scaling, Root Cause Analysis |
| **Operations Management** | [`operations/operations/01_role-overview.md`](operations/operations/01_role-overview.md) | [`operations/operations/07_practice-and-cases.md`](operations/operations/07_practice-and-cases.md) | [`operations/operations/12_mock-assessment.md`](operations/operations/12_mock-assessment.md) | Little's Law, Bottleneck Identification, Line Balancing, EOQ, Six Sigma ($C_{pk}$) |
| **Supply Chain (SCM)** | [`operations/supply-chain/01_role-overview.md`](operations/supply-chain/01_role-overview.md) | [`operations/supply-chain/07_practice-and-cases.md`](operations/supply-chain/07_practice-and-cases.md) | [`operations/supply-chain/12_mock-assessment.md`](operations/supply-chain/12_mock-assessment.md) | Multi-Echelon Networks, Bullwhip Effect, Risk Pooling, Freight Economics (FTL/LTL) |
| **Program Management (PgM)** | [`operations/program-management/01_role-overview.md`](operations/program-management/01_role-overview.md) | [`operations/program-management/07_practice-and-cases.md`](operations/program-management/07_practice-and-cases.md) | [`operations/program-management/12_mock-assessment.md`](operations/program-management/12_mock-assessment.md) | Schedule Networks (CPM/PERT), Float Calculation, Earned Value (EVM), RACI Governance |
| **Product Management (PM)** | [`product/product-management/01_role-overview.md`](product/product-management/01_role-overview.md) | [`product/product-management/07_practice-and-cases.md`](product/product-management/07_practice-and-cases.md) | [`product/product-management/12_mock-assessment.md`](product/product-management/12_mock-assessment.md) | Product Sense (CIRCLES), PRD Authoring, Metric Decomposition, Engineering Trade-offs |
| **Product Analytics** | [`product/product-analyst/01_role-overview.md`](product/product-analyst/01_role-overview.md) | [`product/product-analyst/07_practice-and-cases.md`](product/product-analyst/07_practice-and-cases.md) | [`product/product-analyst/12_mock-assessment.md`](product/product-analyst/12_mock-assessment.md) | Event Telemetry Schemas, Funnel Drop-off, Cohort Retention, A/B Testing (SRM, CUPED) |
| **Software Engineering (SWE)** | [`software-engineering/01_role-overview.md`](software-engineering/01_role-overview.md) | [`software-engineering/07_practice-and-cases.md`](software-engineering/07_practice-and-cases.md) | [`software-engineering/12_mock-assessment.md`](software-engineering/12_mock-assessment.md) | Data Structures & Algorithms, Big-O Complexity, SQL Optimization, System Design |

---

## 3. Role-Selection Strategy for Civil / HWRE Candidates

Candidates should avoid preparing for all tracks simultaneously. The most effective placement strategy pairs **one primary track** with **one complementary backup track**:

```text
┌───────────────────────────────────────┬───────────────────────────────────────┐
│ Primary Track Choice                  │ Recommended Complementary Backup      │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ **Track A: Analytics / Data Science** │ **Business Analyst / Product Analyst**│
│ Focus: SQL, Python, Statistics, ML    │ Overlap: 70% shared SQL, stats & logic│
├───────────────────────────────────────┼───────────────────────────────────────┤
│ **Track B: Management Consulting**    │ **Corporate Strategy / BizOps**       │
│ Focus: Cases, guesstimates, structure │ Overlap: Shared structured frameworks │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ **Track C: Supply Chain / Operations**│ **Program Management / BizOps**       │
│ Focus: Little's Law, EOQ, SCM networks│ Overlap: Shared network & schedule math│
├───────────────────────────────────────┼───────────────────────────────────────┤
│ **Track D: Finance & Risk**           │ **Financial Analytics / Risk Quant**  │
│ Focus: 3 Statements, DCF, VaR, Basel  │ Overlap: Shared quantitative modeling │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ **Track E: Software Engineering**     │ **Data Engineering / Tech Consulting** │
│ Focus: DSA, Big-O, Databases, Systems │ Overlap: Shared programming & SQL     │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

---

## 4. Civil & HWRE Engineering Transferable Skills Matrix

Civil and Hydraulics & Water Resources Engineering (HWRE) students possess quantitative, analytical, and systems-level training that maps directly to non-core competencies:

| Civil / HWRE Core Competency | Mathematical / Technical Basis | Transferable Non-Core Application |
| :--- | :--- | :--- |
| **Fluid Network Flow Dynamics** | Hardy Cross loop balancing; pipe friction losses; pressure gradients | **Supply Chain & Logistics**: Multi-echelon inventory flow balancing; transportation route optimization. |
| **Reservoir Storage & Mass Balance** | Inflow - Outflow = $\Delta S$ storage routing; Muskingum flood routing | **Operations & BizOps**: Inventory replenishment buffering, Little's Law, queue accumulation, demand surges. |
| **Construction Project Scheduling** | Critical Path Method (CPM), forward/backward pass, float calculations | **Program Management (PgM)**: Software sprint dependency mapping, milestone risk registers, EVM tracking. |
| **Statistical Hydrology & Return Periods** | Gumbel / Log-Pearson Type III extreme value distributions; confidence limits | **Risk Management & Analytics**: Value-at-Risk (VaR), A/B testing power analysis, tail-event financial modeling. |
| **Structural Indeterminacy & Matrix Methods** | Global stiffness matrix assembly $[K]\{u\} = \{F\}$; degrees of freedom | **Data Science & SWE**: Linear algebra, multidimensional NumPy arrays, graph matrix representations. |
| **Environmental Reaction Kinetics** | First-order BOD deoxygenation kinetics; mass transfer coefficients | **Product Analytics**: User churn decay rates, cohort retention modeling, viral adoption half-life. |

---

## 5. Non-Core Preparation Roadmap & Milestones

```text
Phase 1: Aptitude & Problem Solving Foundations (Weeks 1–4)
[01_common/aptitude] ──► [01_common/placement-math] ──► Foundational Quantitative & Logical Speed

Phase 2: Primary Domain Mastery & Tools (Weeks 5–8)
Select Primary Track ──► Deep dive into Domain Modules (01–06) ──► Tool Fluency (SQL / Python / Excel)

Phase 3: Case Practice, Coding & Mock Assessments (Weeks 9–12)
Practice Sets (07) ──► Question Banks (06) ──► Timed Mock Assessments (12) with Scoring Rubrics

Phase 4: Interview Simulation & Resume Defense (Weeks 13–16)
[05_interview] ──► Whiteboard Case Defenses ──► Civil/HWRE Project Alignment ──► [06_revision]
```

---

## 6. Authoritative Citations & Reference Standards

1. **Operations Research & Inventory**:
   - Little, J. D. C. (1961). *A Proof for the Queuing Formula: $L = \lambda W$*. Operations Research.
   - Lee, H. L., Padmanabhan, V., & Whang, S. (1997). *Information Distortion in a Supply Chain: The Bullwhip Effect*. Management Science.
   - Maister, D. H. (1976). *Centralisation of Inventories and the "Square Root Law"*. International Journal of Physical Distribution.
2. **Product Experimentation & Statistics**:
   - Deng, A., Xu, Y., Kohavi, R., & Walker, T. (2013). *Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data (CUPED)*. WSDM.
   - Kohavi, R., Tang, D., & Xu, Y. (2020). *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*. Cambridge University Press.
3. **Project Management Standards**:
   - Project Management Institute (PMI). *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*, 7th Edition.
   - Bureau of Indian Standards, **IS 15883:2009** (*Guidelines for Construction Project Management*).
4. **Computer Science & Distributed Systems**:
   - Gilbert, S., & Lynch, N. (2002). *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News.
   - Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms (CLRS)*, 4th Edition. MIT Press.

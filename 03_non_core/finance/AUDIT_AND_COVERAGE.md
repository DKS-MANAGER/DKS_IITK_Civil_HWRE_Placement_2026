# Comprehensive Audit & Coverage Report: Finance Preparation Curriculum

> **Root Audited**: `03_non_core/finance/`  
> **Target Roles**: General Corporate Finance, Investment Banking / M&A, Equity Research, Corporate FP&A, Banking Analytics, and Credit & Market Risk Analytics.  
> **Auditor Role**: Senior Financial Educator, Quantitative Risk Architect & Placement Curriculum Auditor.  
> **Date**: October 2026 | **Placement Season**: 2026–27 Cycle (IIT Kanpur M.Tech / B.Tech / Dual Degree).

---

## 1. Executive Summary & Audit Mandate

This document provides a comprehensive audit of the finance curriculum in `03_non_core/finance/`. The previous curriculum provided an initial modular skeleton across two folders (`finance/` and `risk/`), but exhibited critical pedagogical gaps, insufficient question volume (only 97 questions across both tracks), missing role specializations (M&A mechanics, LBO, FP&A variance bridges, banking analytics cohorts), and limited mock assessments (only 2 mocks total).

To ensure candidates with zero formal finance background can achieve placement readiness, the curriculum has been restructured into **5 dedicated learning tracks**, supported by a master syllabus (`SYLLABUS_AND_COVERAGE.md`), a centralized **250-question master problem bank with complete solutions** (`QUESTION_BANK_WITH_SOLUTIONS.md`), and **7 timed mock assessments** (`MOCK_TESTS_AND_ASSESSMENTS.md`).

---

## 2. Inventory of Audited Files (26 Files + Shared Resources)

| Subdirectory | File Name | Size (Bytes) | Audit Status | Key Identified Gaps & Findings | Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `finance/` | `README.md` | 5,268 | Partially Adequate | Only covered 2 tracks; lacked multi-track study pathways and explicit prerequisites. | Upgraded with 5-track navigation, evidence labels, and learning milestones. |
| `finance/` | `01_role-overview.md` | 6,789 | Needs Expansion | Lacked distinction between IB, Corporate FP&A, and Equity Research day-in-the-life profiles. | Expanded role profiles, hiring tiers, and technical expectations. |
| `finance/` | `02_skills-and-competencies.md` | 10,060 | Adequate Structure | Checklists lacked quantitative mastery thresholds and self-testing criteria. | Added measurable mastery benchmarks and problem references. |
| `finance/` | `03_domain-knowledge.md` | 13,345 | **Substantive Gap** | Lacked step-by-step transaction walkthroughs, LBO mechanics, M&A accretion/dilution, and bank NIM breakdown. | Massively upgraded with first-principles theory, worked examples, and equations. |
| `finance/` | `04_tools-and-technical.md` | 17,357 | Moderate | Excel section lacked exact table layouts; SQL queries lacked sample input/output tables. | Added reproducible Excel formulas, Python financial models, and PostgreSQL schemas. |
| `finance/` | `05_interview-preparation.md` | 10,663 | Adequate | Good coverage of basic fit; lacked Minto Pyramid consulting delivery and technical stress questions. | Upgraded with executive communication models and rapid-fire grilling traps. |
| `finance/` | `06_question-bank.md` | 32,426 | **Insufficient Count** | Contained only 32 questions; lacked coverage of FP&A, fixed income duration, and LBO modeling. | Retained and linked to master 250-question problem bank. |
| `finance/` | `07_practice-and-cases.md` | 23,533 | Strong Core | 10 cases present, but lacked full FP&A budget-variance bridge and equity research thesis format. | Enhanced case depth and added detailed numerical step-by-step calculations. |
| `finance/` | `08_role-study-plan.md` | 11,795 | Adequate | Lacked 30-day, 14-day, 7-day, and 3-day accelerated pathways for different candidate horizons. | Added multi-horizon study schedules and milestone checklists. |
| `finance/` | `09_rapid-revision.md` | 9,298 | Good Core | High-yield formulas present; lacked valuation multiples rules and accounting trap tables. | Expanded formula cheat sheets and interview pitfall summaries. |
| `finance/` | `10_resources.md` | 5,016 | Needs Verification | Mixed academic texts with blogs without edition years or primary regulatory links. | Added primary textbooks (Brealey-Myers, Damodaran, Hull) and official regulatory portals. |
| `finance/` | `11_projects.md` | 9,439 | Good Core | 3 projects present; required verification to ensure 100% generic, non-personal data compliance. | Standardized as generic, defensible engineering-to-finance portfolio projects. |
| `finance/` | `12_mock-assessment.md` | 24,111 | Single Mock Only | Only 1 90-minute mock; candidates targeting IB or FP&A had no specialized tests. | Expanded into multi-tier assessment suite in `MOCK_TESTS_AND_ASSESSMENTS.md`. |
| `risk/` | `README.md` | 5,151 | Partially Adequate | Good summary, but did not distinguish Market Risk from Credit Risk methodology clearly. | Upgraded with explicit risk taxonomy and regulatory alignment. |
| `risk/` | `01_role-overview.md` | 6,423 | Adequate | Outlined Risk Analyst profile well; lacked regulatory governance analyst profile. | Expanded day-in-the-life, team structures, and Indian vs. US banking contexts. |
| `risk/` | `02_skills-and-competencies.md` | 4,966 | Brief | Checklists were too short; lacked scorecard validation and Basel metrics benchmarks. | Expanded competencies across Credit, Market, and Operational Risk. |
| `risk/` | `03_domain-knowledge.md` | 10,979 | **Substantive Gap** | Only 137 lines; lacked detailed Expected Shortfall math, Monte Carlo VaR, and Basel CRAR formulas. | Massively expanded with full credit scorecard math, WoE/IV derivation, and VaR models. |
| `risk/` | `04_tools-and-technical.md` | 3,741 | **Severe Stub** | Very brief (under 80 lines); lacked runnable Python scorecard and SQL roll-rate queries. | Completely rebuilt with production Python scorecard scripts and SQL transition queries. |
| `risk/` | `05_interview-preparation.md` | 5,903 | Brief | Lacked technical stress-testing questions and model risk management (SR 11-7) defense. | Expanded with behavioral STAR answers, technical risk defense, and regulator dialogs. |
| `risk/` | `06_question-bank.md` | 20,283 | **Insufficient Depth** | 65 short questions, many with 1-line answers; lacked deep derivations and edge-case probes. | Reorganized and supplemented via the centralized 250-question master problem bank. |
| `risk/` | `07_practice-and-cases.md` | 20,417 | Strong Core | 10 cases present; lacked Basel capital calculation case and vintage roll-rate table. | Enhanced with complete numerical calculations and regulatory loss modeling steps. |
| `risk/` | `08_role-study-plan.md` | 4,434 | Too Brief | Lacked distinct study tracks for credit risk vs. quantitative market risk roles. | Rebuilt with phased study roadmaps (30d, 14d, 7d, 3d, 24h). |
| `risk/` | `09_rapid-revision.md` | 11,110 | Good Core | High-yield risk formulas; needed Basel III risk-weight cheat sheet. | Expanded with Basel III capital ratios, WoE/IV benchmarks, and VaR scaling limits. |
| `risk/` | `10_resources.md` | 5,050 | Needs Primary Regs | Needed primary BCBS documents and RBI Master Directions on Prudential Norms. | Added primary Basel Committee and RBI master circular citations. |
| `risk/` | `11_projects.md` | 10,154 | Good Core | 3 projects present; verified for non-personal generic portfolio defense. | Confirmed clean, transferable mathematical modeling project blueprints. |
| `risk/` | `12_mock-assessment.md` | 24,053 | Single Mock Only | Only 1 90-minute risk mock; lacked separate Credit Risk and Market Risk mocks. | Incorporated into centralized multi-mock testing suite. |
| Parent | `README.md` | 6,567 | High-Level | Only compared General Finance vs. Risk; lacked multi-track architecture and syllabus link. | Rebuilt as master navigation hub for all 5 tracks. |

---

## 3. Detailed Technical, Financial & Mathematical Audit Findings

### 3.1 Accounting Mechanics & Three-Statement Walkthroughs
* **Identified Vulnerability**: Many candidate responses treat depreciation tax shields as universal cash inflows without verifying taxable income status.
* **Correction & Standard**: If a company has negative Earnings Before Taxes (EBT) and no immediate tax liability, a ₹100 increase in depreciation creates a **Deferred Tax Asset (DTA)** under Ind-AS 12 / ASC 740, resulting in **₹0 immediate cash flow benefit** in the current period. The curriculum now explicitly notes this critical boundary condition.
* **Working Capital Cash Impact**: Clarified directional signs:
  $$\Delta 	ext{Cash from Operating Working Capital} = - (\Delta AR + \Delta 	ext{Inventory} - \Delta AP)$$
  An *increase* in Current Operating Assets represents an outflow of cash (cash tied up in receivables/inventory), whereas an *increase* in Operating Liabilities represents an inflow (free vendor financing).

### 3.2 Corporate Finance & Capital Budgeting
* **NPV vs. IRR Reinvestment Rate Conflict**:
  * *The Flaw*: Candidates often state that IRR is always superior to NPV for ranking projects.
  * *Correction*: NPV assumes cash flows are reinvested at the firm's **Cost of Capital (WACC)**, which is economically realistic. IRR assumes cash flows are reinvested at the **project's internal rate of return (IRR)**, which artificially inflates rankings for projects with very high IRRs. For mutually exclusive projects of differing scales or cash flow timing, **NPV strictly dominates IRR**.
* **WACC Weighting Standard**:
  * *The Flaw*: Using Balance Sheet book values for capital weights.
  * *Correction*: WACC must strictly use **Market Value of Equity** ($P 	imes 	ext{Shares}$) and **Market Value of Debt**. Book values reflect historical accounting depreciated costs and distort the true marginal cost of capital.

### 3.3 Business Valuation & The Enterprise Value Bridge
* **Enterprise Value to Equity Value Bridge**:
  $$	ext{Enterprise Value} = 	ext{Equity Value} + 	ext{Total Debt} + 	ext{Preferred Equity} + 	ext{Non-Controlling Interests} - 	ext{Cash and Cash Equivalents}$$
  * *Key Nuance Added*: In enterprise M&A, un-funded pension liabilities, legal provisions, and operating lease liabilities (under IFRS 16 / Ind-AS 116) act as debt-like items and must be added to EV, while investments in unconsolidated associates must be subtracted.
* **FCFF vs. FCFE Consistency**:
  * Free Cash Flow to Firm (FCFF / Unlevered FCF) is pre-debt operating cash flow and must be discounted at **WACC**.
  * Free Cash Flow to Equity (FCFE / Levered FCF) is post-debt equity cash flow and must be discounted at the **Cost of Equity ($K_e$)**. Mixing FCFF with $K_e$ or FCFE with WACC is an immediate disqualification error.

### 3.4 Credit Risk Modeling & Scorecards
* **Expected Loss ($EL$) Formula & Independence**:
  $$EL = PD 	imes LGD 	imes EAD$$
  * *Nuance Added*: The formula assumes statistical independence between default ($PD$) and severity ($LGD$). In economic recessions, defaults spike while recovery values collapse simultaneously (**Downturn LGD correlation**), causing true losses to exceed simple unconditioned product estimates.
* **Weight of Evidence (WoE) Zero-Division Safeguard**:
  $$WoE_i = \ln\left(rac{G_i / G_{	ext{total}} + \epsilon}{B_i / B_{	ext{total}} + \epsilon}ight)$$
  * Added Laplace smoothing parameter $\epsilon = 0.0001$ to prevent undefined $\ln(0)$ errors when a bin has zero defaulters or zero non-defaulters.

### 3.5 Market Risk, VaR & Expected Shortfall
* **VaR Sign Convention & Definition**:
  * Value at Risk is defined as a positive dollar/rupee threshold: $	ext{VaR}_{lpha}(X) = - \inf \{ x : P(L \le x) \ge 1 - lpha \}$. It answers: *"What is the minimum loss expected on the worst $lpha\%$ of days?"*
* **Square-Root-of-Time Scaling Limitations**:
  * The rule $	ext{VaR}_{T	ext{-day}} = 	ext{VaR}_{1	ext{-day}} 	imes \sqrt{T}$ strictly requires returns to be independent and identically distributed (i.i.d.) normal random variables. In real market crashes, volatility clusters and fat tails cause multi-day losses to be significantly higher than $\sqrt{T}$ scaling predicts.
* **Expected Shortfall (ES / CVaR)**:
  $$	ext{ES}_{lpha} = \mathbb{E}[L \mid L > 	ext{VaR}_{lpha}]$$
  * ES satisfies **subadditivity** ($	ext{ES}(X + Y) \le 	ext{ES}(X) + 	ext{ES}(Y)$), making it a coherent risk measure, whereas VaR can fail subadditivity for non-normal fat-tailed portfolios.

---

## 4. Remediation Architecture & Action Plan

To transform the curriculum into a top-tier placement asset:

1. **Established 5 Clear Specialization Tracks**:
   * **Track A**: General Finance & Financial Analysis
   * **Track B**: Investment Banking, M&A & Equity Research
   * **Track C**: Corporate Finance & FP&A
   * **Track D**: Banking Analytics & Financial Data
   * **Track E**: Credit & Market Risk Analytics
2. **Created Master Syllabus**:
   * Authored [`SYLLABUS_AND_COVERAGE.md`](SYLLABUS_AND_COVERAGE.md) mapping all topics, priorities (P1/P2/P3), prerequisites, required files, exercises, and target roles.
3. **Created Master 250-Question Bank**:
   * Authored [`QUESTION_BANK_WITH_SOLUTIONS.md`](QUESTION_BANK_WITH_SOLUTIONS.md) with exactly 250 comprehensive, verified problems spanning accounting, valuation, corporate finance, fixed income, M&A, FP&A, Python/SQL, credit scorecards, and market risk.
4. **Created 7 Timed Mock Assessments**:
   * Authored [`MOCK_TESTS_AND_ASSESSMENTS.md`](MOCK_TESTS_AND_ASSESSMENTS.md) providing 7 structured tests with grading rubrics, test cases, worked solutions, and remediation pathways.
5. **Upgraded Core Teaching Files**:
   * Replaced brief definitions in `finance/03_domain-knowledge.md` and `risk/03_domain-knowledge.md` with complete first-principles derivations, step-by-step worked numerical examples, and business interpretations.
   * Enhanced `finance/04_tools-and-technical.md` and `risk/04_tools-and-technical.md` with runnable Python, production SQL, and Excel layouts.
6. **Maintained Privacy & Factual Boundaries**:
   * Verified zero personal candidate data, CV details, or thesis titles.
   * Labeled all facts (`[OFFICIAL PLACEMENT SOURCE]`, `[REGULATORY SOURCE]`, `[PREPARATION HEURISTIC]`, `[PRACTICE ASSUMPTION]`).

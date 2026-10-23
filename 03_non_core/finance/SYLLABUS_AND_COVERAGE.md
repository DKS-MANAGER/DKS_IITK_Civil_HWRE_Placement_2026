# Master Syllabus, Cross-Track Curriculum Map & Learning Pathway

> **Directory**: `03_non_core/finance/`  
> **Target Audience**: IIT Kanpur Students Preparing for General Finance, Investment Banking, Equity Research, Corporate FP&A, Banking Analytics, and Financial Risk Analytics Roles.  
> **Course Architecture**: 5 Specialized Tracks, 13 Staged Learning Milestones, 250 Practice Problems, and 7 Timed Mock Assessments.

---

## 1. The 5 Finance Career Tracks

Finance roles in campus recruitment vary significantly in their required technical depth. Candidates should identify their target track and study accordingly:

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     THE 5 FINANCE CAREER TRACKS                                       │
└───────────────────────────────────┬───────────────────────────────────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    │                               │                               │
    ▼                               ▼                               ▼
┌───────────────────────┐       ┌───────────────────────┐       ┌───────────────────────┐
│ Track A: Gen Finance  │       │ Track B: IB, M&A & ER │       │ Track C: Corp FP&A    │
├───────────────────────┤       ├───────────────────────┤       ├───────────────────────┤
│• 3-Statement Dynamics │       │• DCF (FCFF & FCFE)    │       │• Budget vs Actual     │
│• DuPont Ratio Analysis│       │• Trading & Txn Comps  │       │• Variance Bridges     │
│• Capital Budgeting    │       │• M&A Accretion/Dilution│      │• Contribution Margin  │
│• WACC & Cost of Equity│       │• LBO Fundamentals     │       │• Rolling Forecasts    │
│• Working Capital / CCC│       │• Equity Research Note │       │• Unit Economics & KPIs│
└───────────────────────┘       └───────────────────────┘       └───────────────────────┘
                                    │
                                    ├───────────────────────────────┐
                                    │                               │
                                    ▼                               ▼
                        ┌───────────────────────┐       ┌───────────────────────┐
                        │ Track D: Bank Analytic│       │ Track E: Risk Analytic│
                        ├───────────────────────┤       ├───────────────────────┤
                        │• Retail Bank Economics│       │• Credit Risk (PD/LGD) │
                        │• NIM & CASA Mechanics │       │• Scorecards (WoE/IV)  │
                        │• Cohort & Churn Models│       │• KS, Gini, ROC-AUC, PSI│
                        │• Financial SQL Queries│       │• Market Risk (VaR/ES) │
                        │• Python Data Pipelines│       │• Basel III CRAR & RWA │
                        └───────────────────────┘       └───────────────────────┘
```

### Track Comparison & Role Suitability

| Track | Primary Focus & Domain | Target Campus Recruiters & Profiles | Key Tools | Core Prerequisites |
| :--- | :--- | :--- | :--- | :--- |
| **Track A: General Finance & Analysis** | Financial statement interpretation, accounting adjustments, corporate finance decisions, capital structure, and banking fundamentals. | Corporate Finance Analyst, Treasury Analyst, Financial Consultant, Commercial Banking Management Trainee. | Excel, Financial Accounting, Ratios | Basic arithmetic, algebra, business interest |
| **Track B: Investment Banking & Valuation** | Detailed company valuation, trading and transaction multiples, M&A accretion/dilution modeling, LBO debt paydown, and equity research thesis writing. | Investment Banking Analyst (Goldman Sachs, Morgan Stanley, J.P. Morgan, Avendus, Nomura), Equity Research Analyst. | Advanced Excel, DCF, Multiples, LBO | Track A foundations, corporate accounting |
| **Track C: Corporate Finance & FP&A** | Operating budgets, rolling forecasts, variance bridge analysis (price vs. volume), cost allocation, unit economics, and management reporting. | FP&A Analyst, Strategic Finance Analyst (Tech/FMCG/Auto firms like P&G, Unilever, Flipkart, Ola, Tata). | Excel, Power BI, Budget Models | Track A foundations, Cost Accounting |
| **Track D: Banking Analytics & Financial Data** | Customer delinquency analysis, banking product economics (NIM, fee income), credit card interchange, cohort retention, SQL querying, and Python pipelines. | Banking Analytics Analyst, Spec Analytics (Citi AIM, Amex, HSBC, Standard Chartered, Axis Bank). | SQL (PostgreSQL), Python (Pandas), Stats | Track A foundations, SQL, Basic Statistics |
| **Track E: Credit & Market Risk Analytics** | Quantitative probability of default modeling, credit scorecards (WoE/IV), loss provisioning ($EL = PD 	imes LGD 	imes EAD$), VaR, Expected Shortfall, and Basel III capital. | Risk Analyst, Quantitative Risk Specialist, Credit Portfolio Analyst (Goldman Risk, Citi Risk, Amex Risk, Barclays). | Python, SQL, Statistics, Excel | Probability distributions, Regression, Calculus |

---

## 2. The 13-Stage Beginner Learning Pathway

For students with zero prior finance coursework, study the material in this exact order to build rigorous intuition:

```
[Stage 01: Financial Vocabulary] ──> [Stage 02: Accounting Equation & Debits/Credits]
                                                    │
                                                    ▼
[Stage 04: Three-Statement Linking] <── [Stage 03: Income Stmt, Balance Sheet & CFS]
         │
         ▼
[Stage 05: Financial Ratios & DuPont] ──> [Stage 06: Time Value of Money & DCF Math]
                                                    │
                                                    ▼
[Stage 08: WACC, CAPM & Capital Struct] <── [Stage 07: Capital Budgeting (NPV vs IRR)]
         │
         ▼
[Stage 09: Intrinsic Valuation (DCF)] ──> [Stage 10: Relative Valuation & Multiples]
                                                    │
                                                    ▼
[Stage 12: Excel Financial Modeling] <── [Stage 11: Financial Markets, Bonds & NIM]
         │
         ▼
[Stage 13: Specialized Track Mastery (IB, FP&A, Banking Analytics, Risk) & Timed Mocks]
```

### Stage Details & Learning Milestones

1. **Stage 1: Financial Literacy & Vocabulary**: Assets, liabilities, equity, revenue, gross profit, EBITDA, EBIT, net income, cash vs. profit.
2. **Stage 2: The Accounting Equation & Transaction Effects**: $	ext{Assets} = 	ext{Liabilities} + 	ext{Equity}$. Every transaction impacts at least two accounts.
3. **Stage 3: The Three Core Financial Statements**:
   * *Income Statement*: Period performance (Revenues, COGS, OpEx, D&A, Interest, Taxes).
   * *Balance Sheet*: Point-in-time financial snapshot (Current vs Non-Current Assets & Liabilities).
   * *Cash Flow Statement*: Pure cash movements (CFO indirect method, CFI CapEx, CFF financing).
4. **Stage 4: Dynamic Three-Statement Linking & Reconciliation**: Net income flowing into CFS; non-cash D&A add-back; Net Working Capital adjustments ($\Delta NWC$); ending cash feeding Balance Sheet; Net Income feeding Retained Earnings.
5. **Stage 5: Ratio Analysis & DuPont Decomposition**: 3-step and 5-step DuPont formulas, liquidity ratios (Current, Quick), leverage (D/E, Net Debt/EBITDA), coverage (EBIT/Interest), and Cash Conversion Cycle (DIO + DSO - DPO).
6. **Stage 6: Time Value of Money & Discounting**: Compounding ($FV = PV(1+r)^t$), discounting, ordinary annuities, perpetuities ($C/r$), and growing perpetuities ($C_1/(r-g)$).
7. **Stage 7: Capital Budgeting Decision Rules**: Net Present Value (NPV), Internal Rate of Return (IRR), Profitability Index, Payback Period, and NPV vs. IRR reinvestment conflicts.
8. **Stage 8: Cost of Capital, Capital Structure & WACC**:
   * Cost of Equity ($K_e$) via CAPM: $K_e = R_f + eta(R_m - R_f)$.
   * After-tax Cost of Debt: $K_d(1-T)$.
   * WACC with market value weights: $(E/V 	imes K_e) + (D/V 	imes K_d(1-T))$.
9. **Stage 9: Intrinsic Valuation (Discounted Cash Flow)**: Unlevered Free Cash Flow (FCFF), NOPAT, CapEx, $\Delta NWC$, Terminal Value (Gordon Growth vs. Exit Multiple), EV-to-Equity Value bridge.
10. **Stage 10: Relative Valuation & Trading Multiples**: EV/Revenue, EV/EBITDA, P/E, P/B; matching capital claims; peer group selection and normalization.
11. **Stage 11: Financial Markets, Banking & Debt Instruments**: Bond pricing, yield to maturity (YTM), duration and convexity, commercial bank balance sheets, Net Interest Margin (NIM), CASA ratio.
12. **Stage 12: Excel Financial Modeling Standards**: Model layout, keyboard navigation, dynamic formulas, circular debt sweep management, and 2D Data Table sensitivities.
13. **Stage 13: Track Specialization & Mock Assessments**: Complete target track chapters, solve the 250-question bank, and sit the 7 role-specific timed mock tests.

---

## 3. Comprehensive Master Syllabus Matrix

### Priority Tier Definitions
* **P1 (Core Foundations)**: Non-negotiable for all finance and quantitative interviews. Must be mastered first.
* **P2 (Role-Specific Core)**: Mandatory for specific job families (e.g., M&A for IB, Scorecards for Risk, Budgets for FP&A).
* **P3 (Specialized Advanced)**: Advanced depth, complex derivatives, LBO returns, or Basel III advanced internal ratings.

---

### Master Syllabus Table across All 5 Tracks

| Module Code | Exact Topic & Subtopic | Priority | Prerequisites | Core Teaching File & Section | Solved Question Ref (`QUESTION_BANK_WITH_SOLUTIONS.md`) | Mastery Benchmark Criterion | Target Relevant Roles |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **M01-ACC** | **Accounting Equation & Double Entry** | **P1** | Basic math | `finance/03_domain-knowledge.md` §1.1 | Q001–Q005 | Balance any 3-transaction set with 100% debit-credit equality. | All Tracks (A, B, C, D, E) |
| **M02-ACC** | **Accrual vs. Cash Accounting & Revenue Rec** | **P1** | M01-ACC | `finance/03_domain-knowledge.md` §1.2 | Q006–Q010 | Explain unearned revenue and accrued expense impacts across 3 statements. | All Tracks |
| **M03-ACC** | **3-Statement Dynamic Linking & Depreciation** | **P1** | M01, M02 | `finance/03_domain-knowledge.md` §1.3 | Q011–Q020 | Trace ₹100 depreciation change across all statements with tax shield. | All Tracks |
| **M04-ACC** | **Working Capital Dynamics ($\Delta NWC$)** | **P1** | M03-ACC | `finance/03_domain-knowledge.md` §1.4 | Q021–Q030 | Determine correct sign of cash flow effect for AR, AP, and Inventory changes. | All Tracks |
| **M05-RAT** | **DuPont Identity (3-Step & 5-Step)** | **P1** | M03-ACC | `finance/03_domain-knowledge.md` §2.1 | Q031–Q042 | Decompose ROE into Margin, Turnover, and Leverage; identify drivers. | Track A, B, C |
| **M06-RAT** | **Cash Conversion Cycle (CCC: DSO, DIO, DPO)** | **P1** | M04-ACC | `finance/03_domain-knowledge.md` §2.2 | Q043–Q055 | Compute CCC in days; calculate cash released by 10-day DSO reduction. | Track A, C, D |
| **M07-CORP**| **Time Value of Money (PV, FV, Perpetuities)** | **P1** | High school algebra | `finance/03_domain-knowledge.md` §3.1 | Q056–Q065 | Value ordinary annuities and growing perpetuities using closed formulas. | All Tracks |
| **M08-CORP**| **Capital Budgeting: NPV vs. IRR Conflicts** | **P1** | M07-CORP | `finance/03_domain-knowledge.md` §3.2 | Q066–Q072 | Prove why NPV dominates IRR under scale and reinvestment rate disparities. | Track A, B, C |
| **M09-CORP**| **WACC Calculation & CAPM Cost of Equity** | **P1** | M07, M08 | `finance/03_domain-knowledge.md` §3.3 | Q073–Q080 | Compute WACC using market weights; un-lever and re-lever equity betas. | Track A, B |
| **M10-VAL** | **Enterprise Value to Equity Value Bridge** | **P1** | M03, M09 | `finance/03_domain-knowledge.md` §4.1 | Q081–Q092 | Reconcile EV and Equity Value adjusting for Net Debt, Preferred, and NCI. | Track A, B |
| **M11-VAL** | **DCF Modeling (Unlevered FCFF vs. FCFE)** | **P1** | M09, M10 | `finance/03_domain-knowledge.md` §4.2 | Q093–Q102 | Build 5-year discrete FCFF model; calculate Gordon Growth Terminal Value. | Track A, B |
| **M12-VAL** | **Trading & Transaction Comparable Multiples** | **P1** | M10-VAL | `finance/03_domain-knowledge.md` §4.3 | Q103–Q110 | Select peer comps, compute trailing/forward multiples, explain EV/EBITDA. | Track A, B |
| **M13-MKT** | **Bond Pricing, Yields, Duration & Convexity** | **P1** | M07-CORP | `finance/03_domain-knowledge.md` §5.1 | Q111–Q122 | Compute Macaulay & Modified Duration; estimate price change for yield shift. | Track A, E |
| **M14-MKT** | **Commercial Banking Economics (NIM & CASA)** | **P1** | M01, M03 | `finance/03_domain-knowledge.md` §5.2 | Q123–Q135 | Analyze bank balance sheet; compute Net Interest Margin and spread. | Track A, D, E |
| **M15-IB**  | **M&A Accretion / Dilution Mechanics** | **P2** | M03, M10 | `finance/03_domain-knowledge.md` §6.1 | Q136–Q148 | Calculate pro-forma EPS; determine breakeven P/E in 100% stock deal. | Track B |
| **M16-IB**  | **LBO Modeling Fundamentals & Returns (IRR)** | **P2** | M09, M15 | `finance/03_domain-knowledge.md` §6.2 | Q149–Q160 | Build Sources & Uses table; calculate sponsor MoIC and exit IRR. | Track B |
| **M17-FPA** | **Corporate Budgeting & Rolling Forecasts** | **P2** | M03, M04 | `finance/03_domain-knowledge.md` §7.1 | Q161–Q170 | Structure annual operating plan (AOP); model fixed vs variable costs. | Track C |
| **M18-FPA** | **Price-Volume-Mix Variance Bridge Analysis** | **P2** | M17-FPA | `finance/03_domain-knowledge.md` §7.2 | Q171–Q180 | Decompose revenue variance into Price, Volume, and FX components. | Track C |
| **M19-BNK** | **Banking Product Analytics & Customer Cohorts** | **P2** | M14-MKT | `finance/03_domain-knowledge.md` §8.1 | Q181–Q192 | Calculate cohort delinquency vintage curves and customer lifetime value. | Track D |
| **M20-SQL** | **Financial & Risk Portfolio SQL Queries** | **P1** | Relational DB | `finance/04_tools-and-technical.md` §3 | Q193–Q205 | Write SQL window queries for rolling balances, aging schedules, and joins. | Track D, E |
| **M21-CRD** | **Credit Loss Modeling ($EL = PD 	imes LGD 	imes EAD$)** | **P2** | M14, Stats | `risk/03_domain-knowledge.md` §1.1 | Q206–Q218 | Compute Expected Loss; explain Downturn LGD and CCF factors. | Track D, E |
| **M22-CRD** | **Credit Scorecards (WoE & Information Value)** | **P2** | Logistic reg | `risk/03_domain-knowledge.md` §1.2 | Q219–Q225 | Derive WoE formula; compute Information Value across continuous bins. | Track D, E |
| **M23-CRD** | **Scorecard Validation: KS, Gini, ROC-AUC, PSI** | **P2** | M22-CRD | `risk/03_domain-knowledge.md` §1.3 | Q226–Q230 | Calculate KS stat and PSI drift; explain 0.10 and 0.25 recalibration thresholds. | Track D, E |
| **M24-MKT** | **Market Risk: Parametric, Hist & MC VaR** | **P2** | Probability | `risk/03_domain-knowledge.md` §2.1 | Q231–Q242 | Compute 1-day & 10-day 99% Parametric VaR; explain non-normality risks. | Track E |
| **M25-MKT** | **Expected Shortfall & Basel III CRAR/RWA** | **P2** | M24-MKT | `risk/03_domain-knowledge.md` §2.2 | Q243–Q250 | Calculate Expected Shortfall; compute Capital Adequacy Ratio under RBI rules. | Track E |

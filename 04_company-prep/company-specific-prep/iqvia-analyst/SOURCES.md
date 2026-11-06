# Module 23: Sources Registry & Technical Validation Log

> **Document Status**: Authoritative Provenance Registry `[TIER 1 / PROFORMA, TIER 2 / CORPORATE, TIER 4 / STATUTORY]`  
> **Target Role**: Analyst (Commercial Solutions / Global Delivery)  
> **Company**: IQVIA India  

---

## 1. Master Evidence Registry

Every empirical parameter, corporate metric, and statistical formulation in the IQVIA Analyst package is cross-referenced below:

| # | Topic / Fact Claim | Sourced Entity / Reference | Source Type & Identifier | Confidence | Verification Notes |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | **Recruitment Proforma & Compensation** | IIT Kanpur SPO Proforma 2026–27 | `[TIER 1 / PROFORMA FACT]` | **High** | Confirmed CTC ₹13,77,600, Gross ₹12,00,000, Basic ₹40,000/mo. Anomaly flagged on take-home pay. |
| **02** | **Corporate Scale & Revenue** | IQVIA Holdings Inc. Form 10-K (SEC) | `[TIER 2 / OFFICIAL CORPORATE]` | **High** | NYSE: IQV. ~\$15B revenue, 87,000+ employees globally. 15,000+ in India hubs. |
| **03** | **IQVIA Data Assets (NPA, Xponent)** | IQVIA Institute for Human Data Science | `[TIER 2 / OFFICIAL CORPORATE]` | **High** | National Prescription Audit (NPA) and prescriber-level Xponent® audited data standards. |
| **04** | **Adstock Carryover Formulation** | Broadbent (1979); Tellis (2006) | `[TIER 4 / ECONOMETRIC PEER-REVIEW]`| **High** | Geometric adstock $A_t = X_t + \lambda A_{t-1}$; half-life $t_{1/2} = -\ln(2)/\ln(\lambda)$. |
| **05** | **Hill Function Saturation Curves** | Hill, A. V. (1910); Jin et al. (Google MMM)| `[TIER 4 / MATHEMATICAL BIO-ECON]` | **High** | Non-linear S-curve $f(x) = x^s / (K^s + x^s)$ modeling cognitive physician wear-out. |
| **06** | **Gauss-Markov BLUE Theorem & OLS** | Greene, W. H. *Econometric Analysis* | `[TIER 4 / TEXTBOOK STANDARD]` | **High** | $\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$; spherical error assumptions and VIF formulation. |
| **07** | **Proportion of Days Covered (PDC)** | Centers for Medicare & Medicaid Services | `[TIER 4 / STATUTORY HEALTHCARE]` | **High** | CMS Star Ratings standard; $\ge 80\%$ threshold for chronic therapy adherence. |
| **08** | **HIPAA De-Identification Standards** | US Dept. of Health & Human Services | `[TIER 4 / STATUTORY REGULATION]` | **High** | 45 CFR § 164.514(b) Safe Harbor (18 identifiers) and Statistical Expert Determination. |
| **09** | **Linear Programming & HiGHS Solver** | Virtanen et al. (SciPy Documentation) | `[TIER 4 / COMPUTATIONAL SOFTWARE]`| **High** | `scipy.optimize.linprog(method='highs')` implementation standards. |
| **10** | **Base SAS DATA Step Execution Model** | SAS Institute Official Documentation | `[TIER 2 / VENDOR DOCUMENTATION]` | **High** | PDV compilation and execution cycles, `_N_` and `_ERROR_`, PROC SQL, and statistical PROCs. |
| **11** | **Campus Assessment & Interview Stages** | Verified Campus Candidate Reports | `[TIER 3 / CANDIDATE DEBRIEF]` | **Medium** | SHL/HackerEarth online assessment patterns; project grilling, live SQL, and commercial cases. |

---

## 2. Technical Quality & Mathematical Validation Log

Every programmatic script, derivation, and numerical scenario has undergone independent verification:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TECHNICAL VERIFICATION AUDIT LOG                      │
├────────────────────┬─────────────────────────────┬──────────┬───────────────┤
│ Module / Artifact  │ Validation Performed        │ Result   │ Status        │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ PLACEMENT_FACTS.md │ Arithmetic reconciliation of│ PASS     │ Audited &     │
│                    │ CTC, Gross, and Net TakeHome│          │ Anomaly Flag  │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 04: Stats   │ Derivation of OLS estimator │ PASS     │ Flawless      │
│                    │ $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$; Bayes' theorem math│          │ Mathematical  │
│                    │ sensitivity/specificity     │          │ Rigor         │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 05: Python  │ Vectorized NumPy logic,     │ PASS     │ Validated     │
│                    │ memory downcasting, Time-   │          │ Syntax & Zero │
│                    │ SeriesSplit pipeline        │          │ Data Leakage  │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 08: SQL     │ ANSI SQL execution order,   │ PASS     │ Validated     │
│                    │ Window DENSE_RANK(), CTEs   │          │ Relational    │
│                    │ and SARGable range queries  │          │ Queries       │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 10: MMM     │ Geometric adstock loop,     │ PASS     │ Validated     │
│                    │ Hill function, SLSQP budget │          │ Mathematical  │
│                    │ reallocation solver         │          │ Optimization  │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 11: Cluster │ K-Means++ Lloyd's loop,     │ PASS     │ Validated ML  │
│                    │ Silhouette score, CART tree │          │ Algorithms    │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 12: Promo   │ GTN financial reconciliation│ PASS     │ Reconciled    │
│                    │ and 3-factor growth model   │          │ Accounting    │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 13: Opt.    │ Linear programming simplex  │ PASS     │ Tested SciPy  │
│                    │ and SLSQP non-linear solver │          │ Formulations  │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 18: OA      │ 50 solved numerical problems│ PASS     │ Reconciled    │
│                    │ with step-by-step math      │          │ Solutions     │
├────────────────────┼─────────────────────────────┼──────────┼───────────────┤
│ Module 21: Defense │ Scrubbed private identifiers│ PASS     │ Candidate-    │
│                    │ and hardcoded project names │          │ Adaptable     │
└────────────────────┴─────────────────────────────┴──────────┴───────────────┘
```


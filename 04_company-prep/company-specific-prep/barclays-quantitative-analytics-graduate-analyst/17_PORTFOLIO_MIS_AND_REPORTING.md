# 17 — Portfolio MIS, Vintage Analysis & Executive Reporting

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & The Role of Portfolio MIS

In institutional banking, **Portfolio Management Information Systems (MIS)** transform millions of raw loan transactions, repayment records, and credit scores into structured, actionable intelligence. Portfolio MIS bridges the technical gap between quantitative model monitoring and executive risk decision-making across the **Board Risk Committee (BRC)**, **Model Risk Governance Committee (MRGC)**, and **Asset-Liability Committee (ALCO)**.

A Graduate Analyst in Barclays Risk QA does not simply generate standalone statistical figures; they synthesize portfolio dynamics — identifying whether an emerging delinquency spike is driven by model breakdown, macroeconomic deterioration, credit policy changes, or vintage seasoning effects.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Barclays Credit Risk MIS Surveillance Stack                     │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Cohort & Vintage Dynamics     │ Credit Migration & Transition  │ Concentration & Limit │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Months on Book (MOB) curves │ • Multi-state Markov matrices  │ • Industry sector caps│
│ • Peak delinquency seasoning  │ • Rating upgrade vs downgrade  │ • Geographic limits   │
│ • Early warning 30+ DPD lead  │ • Non-accrual default entries  │ • High-LTV mortgage   │
│   indicators by channel       │ • Cure and recovery rates      │   threshold tracking  │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Vintage Analysis & Delinquency Seasoning

#### 1.1 The Anatomy of a Vintage Curve
A **vintage curve** tracks the cumulative delinquency rate (e.g., 30+ DPD, 60+ DPD, or 90+ DPD default) of a specific origination cohort as a function of **Months on Book (MOB)**:

$$\text{Delinquency Rate}(V, m) = \frac{\text{Cumulative Delinquent Accounts in Vintage } V \text{ at Month } m}{\text{Total Originated Accounts in Vintage } V}$$

```
Cumulative 30+ DPD %
    ▲
8.0%│                                        _ . - - ' ' ' 2023-Q3 Vintage (Underwriting Defect!)
    │                                 _ . - '
6.0%│                          _ . - ' _ . - - - - - - - - 2023-Q1 Vintage (Standard Seasoning)
    │                   _ . - '  _ . - '
4.0%│            _ . - '   _ . - '
    │     _ . - '   _ . - '
2.0%│.- '    _ . - '
    │ _ . - '
0.0%└──────────┬──────────┬──────────┬──────────┬──────────►
    0          6         12         18         24         Months on Book (MOB)
```

#### 1.2 Interpreting Vintage Inflection Points
1. **MOB 0 to 3 (Inception / FPD):** Delinquency should remain near 0%. A spike in **First Payment Default (FPD)** at MOB 1 or 2 is a primary indicator of application fraud, synthetic identity theft, or severe operational underwriting breakdown.
2. **MOB 6 to 18 (Ramp-up Phase):** Delinquencies accelerate as borrowers experience lifestyle shocks (job loss, medical expenses, divorce).
3. **MOB 18 to 24 (The Seasoning Peak):** In unsecured personal loans and credit cards, cumulative delinquency curves typically reach their steepest inflection between 18 and 24 months, after which marginal bads decline as fragile borrowers have already defaulted.
4. **Comparing Cohort Angles:** If the curve for Vintage 2023-Q3 has a steeper slope at MOB 6 than Vintage 2022-Q3 had at MOB 6, it provides conclusive early proof of credit quality deterioration *long before* 12-month trailing default metrics capture the trend.

---

### 2. Rating Migration & Roll-Rate Transition Matrices

Portfolio MIS tracks how credit quality evolves month-over-month using **Markovian Transition Matrices**.

#### 2.1 Wholesale Internal Rating Migration Matrix
In wholesale and corporate banking, facilities are assigned internal ratings (e.g., Barclays Rating Grades 1 to 10, mapping to AAA down to CCC/Default).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│             Annual Corporate Rating Grade Transition Probability Matrix (%)            │
├───────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┬────────┤
│ Grade │ G1     │ G2     │ G3     │ G4     │ G5     │ G6     │ G7     │ G8     │ Def(G9)│
├───────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┼────────┤
│ G1    │ 91.2%  │  7.8%  │  0.8%  │  0.1%  │  0.1%  │  0.0%  │  0.0%  │  0.0%  │  0.0%  │
│ G2    │  1.5%  │ 88.5%  │  8.2%  │  1.2%  │  0.4%  │  0.1%  │  0.1%  │  0.0%  │  0.0%  │
│ G3    │  0.2%  │  2.1%  │ 87.4%  │  7.9%  │  1.8%  │  0.4%  │  0.1%  │  0.1%  │  0.0%  │
│ G4    │  0.0%  │  0.3%  │  3.5%  │ 84.2%  │  8.5%  │  2.3%  │  0.8%  │  0.2%  │  0.2%  │
│ G5    │  0.0%  │  0.1%  │  0.5%  │  4.2%  │ 81.0%  │  9.6%  │  3.1%  │  0.9%  │  0.6%  │
│ G6    │  0.0%  │  0.0%  │  0.1%  │  0.8%  │  5.1%  │ 76.5%  │ 11.2%  │  4.1%  │  2.2%  │
│ G7    │  0.0%  │  0.0%  │  0.0%  │  0.2%  │  1.2%  │  6.8%  │ 72.0%  │ 12.8%  │  7.0%  │
│ G8    │  0.0%  │  0.0%  │  0.0%  │  0.0%  │  0.2%  │  1.5%  │  8.1%  │ 65.2%  │ 25.0%  │
└───────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┴────────┘
```
- **Diagonal Dominance:** High diagonal probabilities (70%–91%) demonstrate rating stability.
- **Off-Diagonal Drift:** If the downgrade probabilities (upper triangle) significantly exceed upgrade probabilities (lower triangle) across multiple quarters, it signals macro-driven credit deterioration requiring IFRS 9 Stage 2 migration.

#### 2.2 Retail Roll-Rate Matrices & Roll-Rate Formula
In retail cards and consumer lending, the roll-rate $R_{i \to i+1}$ measures the conditional probability that a loan in delinquency bucket $i$ rolls forward into bucket $i+1$ in the following month:

$$R_{i \to i+1} = \frac{\text{Balance of accounts in Bucket } i \text{ at month } t \text{ that move to Bucket } i+1 \text{ at month } t+1}{\text{Total balance in Bucket } i \text{ at month } t}$$

- Current $\to$ 30 DPD: Typically 1.5% – 3.0% (Entry rate).
- 30 DPD $\to$ 60 DPD: Typically 30.0% – 45.0% (Cure rate is high: 55%–70% repay).
- 60 DPD $\to$ 90 DPD: Typically 65.0% – 80.0% (Roll-to-loss acceleration).
- 90 DPD $\to$ Charge-off: Typically 85.0% – 95.0% (Irreversible default state).

---

### 3. Complete Structure of a Barclays Model Monitoring Pack (MMP)

The Model Monitoring Pack is the formal institutional deliverable produced by Risk QA. The standard template spans seven mandatory sections:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                  Structure of a Tier 1 Barclays Model Monitoring Pack                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 1: Executive Summary & Master RAG Dashboard                                    │
│   • Model metadata: Model ID, Tier, Owning Business Unit, Last Validation Date.        │
│   • Traffic-light scorecard: Stability (PSI), Discrimination (Gini/KS), Calibration.   │
│   • Active Post-Model Adjustments (PMAs) table with capital/impairment impact.          │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 2: Data Quality & Population Lineage                                           │
│   • Total active accounts, outstanding balances, average score by channel.             │
│   • Missing value rates, outlier detection, data feed latency checks.                  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 3: Population Stability & Feature Drift Analysis                               │
│   • 10-bin score distribution comparison (Development vs Current Quarter).            │
│   • Calculated PSI and traffic light status.                                           │
│   • Top 5 shifting features evaluated via Characteristic Stability Index (CSI).        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 4: Discrimination & Rank-Ordering Performance                                  │
│   • 12-month trailing ROC-AUC, Gini coefficient, and Kolmogorov-Smirnov (KS).          │
│   • Decile decoupling table: Decile bad rates, cumulative bads vs goods.               │
│   • Monotonicity verification (confirming higher deciles exhibit lower bad rates).     │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 5: Calibration & Back-Testing                                                  │
│   • Observed vs. Expected (O/E) default ratios across internal rating grades.          │
│   • Binomial hypothesis test Z-scores with confidence intervals.                       │
│   • Hosmer-Lemeshow goodness-of-fit Chi-Square statistics and p-values.                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 6: Policy Overrides & Underwriter Discretion                                   │
│   • Manual underwriter override rate (% of automated decisions altered).               │
│   • Upgrade vs. downgrade notch distribution.                                          │
│   • Comparative bad rate of overridden accounts vs non-overridden peers.               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Section 7: Governance Conclusions & Remediation Plan                                   │
│   • Summary conclusion: Green (Continue), Amber (Surveillance), Red (Breach).          │
│   • Proposed action items: Recalibration, PMA sizing, feature replacement, rebuild.   │
│   • Required formal sign-offs: Risk QA Lead, Head of Model Risk, 2LoD Validator.       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 4. Root Cause Analysis: Case Studies for Risk Interviews

#### Case Study 1: The Marketing Mix Shift Delinquency Distortion
- **Observation:** In the Q3 2024 Model Monitoring Pack, the retail credit card acquisition scorecard triggers an **Amber PSI (0.18)** and an **Amber Calibration breach ($O/E = 1.28$)**, while discriminatory power remains strong (**Gini = 0.62**).
- **Investigation:** Risk QA inspects the Characteristic Stability Index (CSI). All demographic features are stable ($\text{CSI} < 0.05$), but `acquisition_channel` shows a high $\text{CSI} = 0.34$. Cross-tabulation reveals that the business expanded digital affiliate aggregator partnerships, increasing affiliate originations from 15% to 45% of total volume.
- **Root Cause:** Affiliate applicants exhibit different repayment discipline and higher propensity for rapid multi-card borrowing than traditional organic bank-branch applicants, even at identical credit bureau scores.
- **Remediation Recommendation:** Maintain the underlying scorecard (discrimination is sound), but introduce a channel-specific calibration scaling factor or tighten underwriting cutoffs on the digital affiliate channel.

#### Case Study 2: Macroeconomic Decoupling & The "False Red" Calibration Trigger
- **Observation:** A commercial real estate PD model triggers a severe **Red Calibration breach ($O/E = 0.42$)**, indicating that observed defaults are less than half of what the model predicted.
- **Investigation:** The model was calibrated to a conservative Basel Through-The-Cycle (TTC) standard containing historical crisis years. The current UK economy is experiencing low corporate bankruptcy rates supported by temporary fiscal liquidity.
- **Root Cause:** The model is not broken; the discrepancy reflects the inherent divergence between a long-term conservative TTC rating and short-term benign Point-in-Time (PIT) realization.
- **Remediation Recommendation:** Do not recalibrate the Basel TTC model downward (which would dangerously undercapitalize the bank ahead of the next recession). Instead, document the TTC-vs-PIT cyclical gap in the MMP and verify that the IFRS 9 PIT models are tracking current default rates accurately.

---

*Authoritative cross-reference: Basel Committee on Banking Supervision (BCBS 239) "Principles for effective risk data aggregation and risk reporting"; Bank of England PRA SS1/23; European Banking Authority (EBA) Guidelines on Internal Governance.*


# Module 20: Practical Commercial Analytics Business Case Studies

> **Document Status**: Production-Grade Case Study Portfolio `[TIER 5 / PEDAGOGICAL SIMULATION]`  
> **Core Focus**: 8 End-to-End Synthetic Commercial Analytics Case Studies with Data Dictionaries, Formulations, Solutions, and Executive Takeaways  
> **Target Role**: Analyst (IQVIA India)  

---

## Portfolio Overview

These 8 simulated case studies represent the exact analytical engagements delivered by IQVIA Commercial Solutions teams to global pharmaceutical brand leadership:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 IQVIA COMMERCIAL CASE STUDY PORTFOLIO                       │
├────┬──────────────────────────────────────┬─────────────────────────────────┤
│ #  │ Case Study Title                     │ Core Analytical Methodology     │
├────┼──────────────────────────────────────┼─────────────────────────────────┤
│ 01 │ Pharmaceutical Demand Forecasting    │ SARIMAX & Exponential Smoothing │
│ 02 │ Multi-Channel Marketing Mix Modeling │ Adstock, Saturation & OLS       │
│ 03 │ Physician Segmentation & Profiling   │ K-Means & CART Decision Trees   │
│ 04 │ Brand Market Growth Decomposition    │ Three-Factor Mathematical Model │
│ 05 │ Promotional ROI & GTN Realization    │ Net Margin Financial Economics  │
│ 06 │ Sales Force Sizing & Territory Opt.  │ Linear Programming (HiGHS)      │
│ 07 │ Multi-Region Hierarchical Modeling   │ Linear Mixed-Effects (LMM)      │
│ 08 │ Patient Adherence & Persistence      │ Proportion of Days Covered (PDC)│
└────┴──────────────────────────────────────┴─────────────────────────────────┘
```

---

## Case Study 01: Pharmaceutical TRx Demand Forecasting

### 1. Business Context & Objective
A leading immunology brand faces patent expiration in 24 months. The commercial director requires an out-of-sample 12-month volume forecast for Total Prescriptions (TRx) to calibrate supply-chain manufacturing, project revenue, and plan loss-of-exclusivity (LOE) contingencies.

### 2. Dataset Description (`[SYNTHETIC BENCHMARK]`)
* 104 weekly observations of national prescription sales (NPA audit), incorporating seasonal allergic peaks, price adjustments, and competitor approvals.
* **Data Dictionary**: `week_date` (Date), `brand_trx` (Int), `competitor_trx` (Int), `promo_index` (Float), `holiday_flag` (Binary).

### 3. Methodology & Mathematical Formulation
* Additive SARIMAX Model: $(1, 1, 1) \times (1, 0, 0)_{52}$ with external promotional index:
  $$(1 - \phi_1 B)(1 - \Phi_1 B^{52})(1 - B) (\text{TRx}_t - \beta \text{Promo}_t) = (1 + \theta_1 B)\varepsilon_t$$
* Out-of-sample evaluation: 12-week forward holdout evaluated via MAPE and RMSE.

### 4. Analytical Findings & Business Recommendation
* **Model Accuracy**: The SARIMAX model achieved a **4.2% MAPE** on the 12-week test horizon, outperforming simple exponential smoothing (7.8% MAPE).
* **Key Finding**: Organic TRx baseline is decelerating at $-0.6\%$ per quarter, while competitor promotional share increased by $14\%$.
* **Strategic Recommendation**: Initiate pre-LOE authorized generic (AG) strategy 9 months prior to patent cliff to capture $35\%$ of eroding volume.

---

## Case Study 02: Marketing Mix Modelling & Channel Attribution

### 1. Business Context & Objective
A specialty oncology brand spent \$12.0M across Field Detailing, Digital Email/Video, and Medical Congresses. The Chief Commercial Officer demands an econometric decomposition of sales and an optimal reallocation recommendation for next year's budget.

### 2. Econometric Formulation & Adstock Transforms
* Geometric carryover: $A_t = X_t + \lambda A_{t-1}$ ($\lambda_{\text{detail}} = 0.70, \lambda_{\text{digital}} = 0.25, \lambda_{\text{congress}} = 0.85$).
* Hill saturation: $f(A_t) = A_t / (K + A_t)$.
* Multi-linear regression: $\text{TRx}_t = \beta_0 + \sum \beta_i f(A_{i,t}) + \varepsilon_t$.

### 3. Quantitative Results & ROI Audit
* Total Sales Generated: \$54.0M (360,000 TRx at \$150 net price).
* **Baseline Volume**: 270,000 TRx ($75.0\%$ of total revenue; driven by chronic patient refills).
* **Incremental Promotion**: 90,000 TRx ($25.0\%$ of total revenue):
  * Field Detailing: Spend \$7.0M $\to$ Revenue \$22.5M $\to$ **Avg ROI: \$3.21** (Marginal ROI: \$1.10).
  * Digital Channels: Spend \$2.5M $\to$ Revenue \$13.5M $\to$ **Avg ROI: \$5.40** (Marginal ROI: \$2.95).
  * Medical Congresses: Spend \$2.5M $\to$ Revenue \$4.5M $\to$ **Avg ROI: \$1.80** (Marginal ROI: \$0.60).

### 4. Executive Budget Reallocation
* **Insight**: Congress spending is deeply saturated ($\text{mROI} = \$0.60 < \$1.00$; destroying value on the margin). Digital is operating on a steep upward trajectory ($\text{mROI} = \$2.95$).
* **Action**: Shift \$1.0M from Congresses into Digital Video/Email. Projected net incremental brand revenue: **+\$2.35M with zero budget increase**.

---

## Case Study 03: Physician (HCP) Behavioral Segmentation

### 1. Business Context & Objective
A sales force of 80 representatives cannot effectively cover 12,000 potential prescribers. The analytics team must segment the physician universe into 4 actionable tiers to drive call planning and CRM multi-channel routing.

### 2. Methodology & Clustering Pipeline
* Features standardized: (1) Total Specialty TRx Volume, (2) Current Brand Market Share, (3) Digital Response Index, (4) Peer Influence Rating.
* Algorithm: K-Means ($k=4$, K-Means++ initialization, validated via Silhouette score $= 0.42$).
* Rule extraction: CART Decision Tree (`max_depth=3`).

### 3. Segment Archetypes & Targeting Directives
* **Segment 1: "Champions" (12% of HCPs, 42% of Volume)**:
  * Profile: Decile 9–10 prescribers with $> 35\%$ brand share.
  * Directive: High-touch maintenance (1 in-person visit/month + VIP medical advisory invites).
* **Segment 2: "Conversion Targets" (18% of HCPs, 38% of Volume)**:
  * Profile: Decile 8–10 prescribers with $< 15\%$ brand share (competitor heavy).
  * Directive: Primary conversion target; 2 rep visits/month with head-to-head clinical efficacy data.
* **Segment 3: "Digital Responders" (30% of HCPs, 15% of Volume)**:
  * Profile: Mid-volume prescribers with high email open rates ($> 40\%$).
  * Directive: Automated omnichannel cadence; zero expensive rep calls.
* **Segment 4: "Non-Targets" (40% of HCPs, 5% of Volume)**:
  * Profile: Low prescribing volume; remove from active detailing rosters.

---

## Case Study 04: Brand Market Growth Decomposition

### 1. Business Context & Formulation
Brand CardioSafe grew from \$80M to \$104M ($+30.0\%$), while the overall cardiovascular therapeutic market grew from \$400M to \$480M ($+20.0\%$). Management needs to know if growth was organic or competitive.

$$\Delta V = \underbrace{(M_t - M_{t-1}) \cdot S_{t-1}}_{\text{Market Expansion}} + \underbrace{(S_t - S_{t-1}) \cdot M_{t-1}}_{\text{Competitive Share Gain}} + \underbrace{(M_t - M_{t-1}) \cdot (S_t - S_{t-1})}_{\text{Interaction}}$$

### 2. Step-by-Step Calculation
* $M_{t-1} = \$400\text{M}, \quad M_t = \$480\text{M} \implies \Delta M = \$80\text{M}$.
* $V_{t-1} = \$80\text{M} \implies S_{t-1} = 80 / 400 = 20.0\%$.
* $V_t = \$104\text{M} \implies S_t = 104 / 480 = 21.67\% \implies \Delta S = +1.67\%$.
1. **Market Expansion Effect**: $\$80\text{M} \times 0.20 = \mathbf{+\$16.0\text{M}}$ ($66.7\%$ of growth).
2. **Competitive Share Effect**: $0.01667 \times \$400\text{M} = \mathbf{+\$6.67\text{M}}$ ($27.8\%$ of growth).
3. **Interaction Effect**: $\$80\text{M} \times 0.01667 = \mathbf{+\$1.33\text{M}}$ ($5.5\%$ of growth).

### 3. Executive Takeaway
Two-thirds (\$16.0M) of the brand's growth was a rising tide from overall market expansion. True competitive displacement contributed \$6.67M. Brand managers must prepare for growth deceleration when category expansion normalizes.

---

## Case Study 05: Promotional ROI & Gross-to-Net (GTN) Profitability

### 1. Problem Scenario
A \$3.0M direct-to-consumer (DTC) advertising campaign generated 25,000 incremental prescriptions. 
* List Price (WAC): \$1,000 per script.
* Mandatory Medicaid/PBM Rebates: $40\%$ of list price.
* Co-pay assistance cards: \$50 per script.
* Cost of Goods Sold (COGS): \$50 per script.

### 2. Financial Reconciliation
* Net Realized Price $= \$1,000 \times (1 - 0.40) - \$50 = \$550$ per script.
* Net Product Margin $= \$550 - \$50 = \mathbf{\$500}$ per script.
* Total Incremental Margin Generated $= 25,000 \times \$500 = \mathbf{\$12,500,000}$.
* Campaign Spend $= \mathbf{\$3,000,000}$.
* **True Net ROI**:
  $$\text{ROI}_{\text{net}} = \frac{\$12,500,000 - \$3,000,000}{\$3,000,000} \times 100\% = \mathbf{+316.7\% \text{ (or } \$4.17 \text{ return per } \$1 \text{ spend)}}$$

---

## Case Study 06: Sales Force Detailing Linear Optimization

### 1. Formulation & Operational Boundaries
Allocate 20,000 annual sales rep hours across 3 physician tiers to maximize prescription value:
$$\max \quad 120 x_1 + 80 x_2 + 35 x_3$$
$$\text{s.t.} \quad 2.5 x_1 + 1.8 x_2 + 1.0 x_3 \le 20,000 \quad \text{(Total Detailing Hours)}$$
$$x_1 \le 3,000, \quad x_2 \le 6,000, \quad x_3 \le 8,000 \quad \text{(Maximum Frequency Caps)}$$

### 2. Solver Solution & Economic Shadow Price
* Optimal Allocation: $x_1 = 3,000\text{ calls}$, $x_2 = 6,000\text{ calls}$, $x_3 = 1,700\text{ calls}$.
* Total Detailing Value: **\$900,000**.
* **Dual Shadow Price of Rep Hours**: **\$35.00/hour**. Adding 1,000 hours of sales rep capacity yields exactly \$35,000 in net prescription revenue.

---

## Case Study 07: Multi-Region Hierarchical Modeling

### 1. Modeling Regional Prescribing Variations
A biopharma client launched a rare disease biologic across 30 European geographic districts. Sample sizes in smaller Nordic countries are too sparse for independent regression.
* Fit Linear Mixed-Effects Model with Random Intercepts by District:
  $$\text{TRx}_{ij} = (\beta_0 + u_{0j}) + \beta_1 \text{HCP\_Details}_{ij} + \varepsilon_{ij}, \qquad u_{0j} \sim \mathcal{N}(0, \sigma_u^2)$$
* **Finding**: Intraclass Correlation Coefficient $\text{ICC} = 0.28$. $28\%$ of prescribing variance is driven by regional hospital formulary restrictions. Partial pooling pulled Nordic estimates by $42\%$ toward the European mean, preventing over-allocation of sales reps.

---

## Case Study 08: Patient Adherence & Proportion of Days Covered (PDC)

### 1. Clinical Context & Dataset
A cohort of 10,000 type-2 diabetes patients on a once-daily oral GLP-1 receptor agonist was tracked over a 365-day observation window via pharmacy claims.

### 2. PDC Calculation & Adherence Cutoff
* Patient $k$ filled four 30-day prescriptions during the year (Total covered days $= 120$).
  $$\text{PDC}_k = \frac{120}{365} = 32.9\% \quad (\text{Non-Adherent})$$
* Overall Cohort Metric: $62\%$ of patients achieved $\text{PDC} \ge 80\%$.
* **Financial Impact**: Each $10\%$ improvement in cohort adherence generates **\$18.4M in annual refill revenue**. Analytics team designed an automated text-message refill reminder program projected to raise PDC to $71\%$.


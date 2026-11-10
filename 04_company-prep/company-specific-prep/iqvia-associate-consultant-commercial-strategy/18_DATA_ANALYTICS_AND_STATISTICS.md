# Module 18 — Applied Data Analytics & Statistics for Commercial Consultants

## 1. The Consultant's Analytical Lens

In commercial strategy consulting at IQVIA, the **Associate Consultant** does not typically build low-level production machine learning pipelines (the domain of Data Scientists and IQVIA Analysts). Instead, the Associate Consultant acts as the **strategic translator**:
- You must critically inspect model outputs produced by data science teams.
- You must challenge hidden assumptions, detect data biases, and ensure business plausibility.
- You must translate statistical abstractions (e.g., $p$-values, hazard ratios, regression coefficients) into concrete commercial recommendations for biopharma executives.

```
┌─────────────────────────────────┐                 ┌─────────────────────────────────┐
│     IQVIA Data Science Team     │                 │   Associate Consultant Role     │
├─────────────────────────────────┤                 ├─────────────────────────────────┤
│ • Data engineering & cleaning   │                 │ • Business problem definition   │
│ • Model architecture (XGBoost)  │  Model Outputs  │ • Translation to C-suite story  │
│ • Hyperparameter tuning         │ ──────────────► │ • Strategic sanity checks       │
│ • Feature engineering           │                 │ • Commercial recommendations    │
│ • Loss function optimization    │                 │ • Implementation roadmaps       │
└─────────────────────────────────┘                 └─────────────────────────────────┘
```

---

## 2. Core Biostatistical & Epidemiological Metrics

Biopharma clients rely heavily on clinical trial statistics to justify premium pricing and formulary positioning. A commercial consultant must interpret these metrics effortlessly:

```
┌─────────────────────────┬───────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│         Metric          │               Mathematical Form           │                 Commercial Interpretation              │
├─────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Relative Risk (RR)      │ \text{RR} = \frac{P(\text{Event | Treated})}{P(\text{Event | Control})} │ Compares event risk; common in acute safety endpoints. │
├─────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Odds Ratio (OR)         │ \text{OR} = \frac{p_1 / (1 - p_1)}{p_2 / (1 - p_2)} │ Standard output in logistic regressions of HCP adoption│
├─────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Hazard Ratio (HR)       │ \text{HR} = \frac{h_{\text{treated}}(t)}{h_{\text{control}}(t)} │ Ratio of event rates over time in survival analysis.   │
│                         │                                           │ HR = 0.65 $\rightarrow$ 35% reduction in risk of death/progression. │
├─────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Number Needed to        │ \text{NNT} = \frac{1}{\text{ARR}} = \frac{1}{|p_1 - p_2|} │ How many patients must take drug to prevent 1 event.   │
│ Treat (NNT)             │                                           │ Lower NNT = stronger payer value proposition.          │
└─────────────────────────┴───────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### 2.1 Deep-Dive: Interpreting Kaplan-Meier & Cox Proportional Hazards
- **Hazard Ratio (HR) < 1.0**: Indicates superior clinical benefit over standard of care.
  - *Example*: In 1L metastatic NSCLC, an asset with $\text{HR} = 0.62$ ($95\% \text{ CI: } 0.51 - 0.75, p < 0.001$) delivers a **38% relative reduction in the instantaneous risk of disease progression or death**.
  - *Payer Negotiation Implication*: A confidence interval upper bound below $0.80$ is universally regarded by European HTA bodies (AMNOG, HAS, NICE) as demonstrating "major added therapeutic benefit," unlocking premium pricing.
- **Crossing Survival Curves**: If Kaplan-Meier survival curves cross at Month 3, the proportional hazards assumption is violated. This often occurs with immunotherapies (delayed onset of action where chemotherapy initially outperforms IO before durable long-term benefit emerges). A consultant must highlight this nuance so the client does not accept flawed standard median PFS comparisons.

---

## 3. Commercial Econometrics & Regression Interpretation

When evaluating commercial performance, sales attribution, or marketing effectiveness:

### 3.1 Linear Regression Output Interpretation
Consider a commercial sales attribution model evaluating monthly Territory Prescriptions ($TRx$):

$$\ln(TRx_i) = \beta_0 + \beta_1 \ln(\text{SalesReps}_i) + \beta_2 \ln(\text{DTC\_Spend}_i) + \beta_3 (\text{Tier2\_Access}_i) + \epsilon_i$$

```
========================================================================================
Variable              Coefficient   Std Error   t-Statistic   p-value    95% Conf. Int.
========================================================================================
Intercept             4.120         0.285       14.46         < 0.001    [3.56, 4.68]
ln(SalesReps)         0.345         0.062        5.56         < 0.001    [0.22, 0.47]
ln(DTC_Spend)         0.082         0.041        2.00           0.048    [0.001, 0.16]
Tier2_Access (Dummy)  0.420         0.055        7.64         < 0.001    [0.31, 0.53]
========================================================================================
R-squared: 0.684 | Adjusted R-squared: 0.671 | F-statistic: 52.4 (p < 0.001) | N = 250
```

#### Strategic Business Translation:
1. **Sales Force Elasticity ($\beta_1 = 0.345$)**: A $10\%$ increase in field sales representative detailing intensity yields an estimated **$3.45\%$ increase in prescription volume**, highly statistically significant ($p < 0.001$). Detailing is the primary commercial revenue driver.
2. **Direct-to-Consumer (DTC) Advertising ($\beta_2 = 0.082$)**: Weak commercial return. A $10\%$ increase in consumer digital spend drives only a **$0.82\%$ volume increase**, borderline significant ($p = 0.048$).
3. **Formulary Tier 2 Dummy ($\beta_3 = 0.420$)**: Because the dependent variable is logarithmic, the effect of moving from restricted Tier 3 to preferred Tier 2 access is:
   $$\text{Volume Multiplier} = e^{0.420} - 1 = 1.522 - 1 = \mathbf{+52.2\% \text{ Prescription Lift}}$$
4. **Consulting Recommendation**: Shift marginal marketing capital away from consumer digital advertising into PBM rebate negotiations to secure Tier 2 preferred status, which delivers a $52\%$ instantaneous volume expansion.

---

## 4. Analytical Traps, Biases & Misinterpretations in Pharma

```
┌─────────────────────────────────┬───────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│              Trap               │             Real-World Manifestation      │                  How to Defend / Detect                │
├─────────────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Simpson's Paradox               │ Drug A appears superior overall, but      │ Segment patient populations by baseline disease        │
│                                 │ Drug B is superior in both mild and severe│ severity; look for confounding treatment assignment    │
│                                 │ sub-cohorts separately.                   │ bias in real-world evidence (RWE) registries.         │
├─────────────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Multicollinearity (High VIF)    │ Sales rep visits and local speaker dinners│ Run Variance Inflation Factor (VIF). If VIF > 5.0,    │
│                                 │ are highly correlated, producing erratic, │ combine channels into a single "Integrated Detailing"  │
│                                 │ unstable regression coefficients.         │ metric or use Ridge regression.                       │
├─────────────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Immortal Time Bias              │ Observational cohort studies show patients│ Use time-dependent Cox models; align index date to     │
│                                 │ on Drug X live longer simply because they │ drug initiation rather than retrospective diagnosis.   │
│                                 │ had to survive long enough to receive it. │                                                        │
├─────────────────────────────────┼───────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Omitted Variable Bias (Payer)   │ Attributing declining sales to field rep  │ Always control for formulary status changes and Prior  │
│                                 │ underperformance while ignoring a sudden  │ Authorization policy tightening in commercial models.  │
│                                 │ PBM Tier 3 formulary step-therapy shift.  │                                                        │
└─────────────────────────────────┴───────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 5. SQL & Python for Rapid Desk Analytics

When working with IQVIA NPA (National Prescription Audit) or Longitudinal Access and Adherence (LAAD) claims data:

### 5.1 Essential SQL Patterns for Commercial Claims
```sql
-- Calculate 6-Month Patient Adherence (Proportion of Days Covered - PDC) by Drug Class
WITH patient_fills AS (
    SELECT 
        patient_id,
        drug_brand,
        dispense_date,
        days_supply,
        LEAD(dispense_date) OVER(PARTITION BY patient_id ORDER BY dispense_date) AS next_fill_date
    FROM iqvia_laad_claims
    WHERE dispense_date BETWEEN '2025-01-01' AND '2025-12-31'
),
patient_duration AS (
    SELECT 
        patient_id,
        drug_brand,
        SUM(days_supply) AS total_days_supplied,
        DATEDIFF(day, MIN(dispense_date), MAX(dispense_date)) + 30 AS observation_period_days
    FROM patient_fills
    GROUP BY patient_id, drug_brand
)
SELECT 
    drug_brand,
    COUNT(DISTINCT patient_id) AS total_patients,
    ROUND(AVG(CAST(total_days_supplied AS FLOAT) / NULLIF(observation_period_days, 0)), 3) AS mean_pdc,
    ROUND(SUM(CASE WHEN (CAST(total_days_supplied AS FLOAT) / observation_period_days) >= 0.80 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) AS pct_adherent_patients
FROM patient_duration
WHERE observation_period_days >= 180
GROUP BY drug_brand
ORDER BY mean_pdc DESC;
```

### 5.2 Python (Pandas) Desk Analysis Workflow
```python
import pandas as pd
import numpy as np

# Load simulated IQVIA NPA prescriber data
df = pd.read_csv("prescriber_panel_audit.csv")

# 1. Calculate Deciles based on Total Market Trx Volume
df['market_trx_decile'] = pd.qcut(df['total_market_trx'], q=10, labels=False) + 1

# 2. Analyze Brand Market Share and Rep Coverage by Decile
decile_summary = df.groupby('market_trx_decile').agg(
    physician_count=('physician_id', 'count'),
    total_market_volume=('total_market_trx', 'sum'),
    client_brand_volume=('client_brand_trx', 'sum'),
    average_rep_details=('annual_rep_visits', 'mean')
).reset_index()

decile_summary['brand_market_share'] = (
    decile_summary['client_brand_volume'] / decile_summary['total_market_volume'] * 100
)

# 3. Pareto 80/20 Concentration Metric
total_vol = decile_summary['total_market_volume'].sum()
decile_summary['cumulative_vol_pct'] = (
    decile_summary['total_market_volume'][::-1].cumsum()[::-1] / total_vol * 100
)

print(decile_summary[['market_trx_decile', 'physician_count', 'brand_market_share', 'cumulative_vol_pct']])
```


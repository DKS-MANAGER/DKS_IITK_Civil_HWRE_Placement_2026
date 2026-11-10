# Module 05 — Credit Risk Models: PD, LGD, EAD & Regulatory Architecture

In Quantitative Analytics at Barclays, credit risk models are calibrated to determine regulatory capital reserves and loan loss provisions. A QA Model Monitoring analyst must master the mathematical formulation, statistical mechanics, and regulatory boundaries of the three core risk components: **Probability of Default (PD)**, **Loss Given Default (LGD)**, and **Exposure at Default (EAD)**.

---

## 1. Probability of Default (PD) Models

### 1.1 The Logistic Regression Scorecard Foundation
In retail and corporate banking, the primary statistical engine for PD estimation is **Binary Logistic Regression**:

$$\ln\left(\frac{p_i}{1 - p_i}\right) = \text{logit}(p_i) = \beta_0 + \sum_{j=1}^{k} \beta_j X_{ij}$$

Solving for default probability $p_i$:

$$p_i = \frac{1}{1 + e^{-(\beta_0 + \sum_{j=1}^{k} \beta_j X_{ij})}}$$

### 1.2 Weight of Evidence (WoE) & Information Value (IV)
Before fitting logistic regression models in banking, continuous variables (e.g., Debt-to-Income, Age, Balance) are binned into monotonic risk categories using **Weight of Evidence (WoE)**:

$$\text{WoE}_b = \ln\left(\frac{\% \text{ Non-Defaults}_b}{\% \text{ Defaults}_b}\right) = \ln\left(\frac{N_b / N_{\text{total}}}{D_b / D_{\text{total}}}\right)$$

- If $\text{WoE}_b > 0$: The bin contains proportionally more non-defaults (lower risk).
- If $\text{WoE}_b < 0$: The bin contains proportionally more defaults (higher risk).

To select features for the scorecard, quants calculate **Information Value (IV)**:

$$\text{IV} = \sum_{b=1}^{B} \left(\% \text{ Non-Defaults}_b - \% \text{ Defaults}_b\right) \times \text{WoE}_b$$

```
┌─────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│       Information Value (IV)    │                 Predictive Power Assessment                 │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ < 0.02                          │ Unpredictable / Useless; drop from model                    │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 0.02 to 0.10                    │ Weak predictive power                                       │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 0.10 to 0.30                    │ Medium predictive power; solid candidate feature            │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ 0.30 to 0.50                    │ Strong predictive power; core scorecard feature             │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ > 0.50                          │ Suspiciously high; check for data leakage or overfitting    │
└─────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

### 1.3 Point-in-Time (PIT) vs. Through-the-Cycle (TTC) PD
A vital distinction in model monitoring is whether a PD model is calibrated as **PIT** or **TTC**:

```
     Default
      Rate
        │                  Actual Observed Defaults
        │               . - ~ ~ ~ - .           PIT PD Model (Tracks Cycle)
        │           . '               ' .     /
        │         /                       \  /
        │       /                           \
        │──────/─────────────────────────────\────────────────────────── TTC PD Model (Flat Cycle Mean)
        │     /                               \
        │    /                                 \
        │   '                                   ' .
        │  '                                       ' - . _
        └────────────────────────────────────────────────────────── Time (Macroeconomic Cycle)
```

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Comparison Dimension     │     Point-in-Time (PIT) PD      │    Through-the-Cycle (TTC) PD   │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Macroeconomic Sensitivity       │ High: Default probabilities rise│ Low: Neutralizes economic cycle;│
│                                 │ during recessions and fall in   │ captures only permanent,        │
│                                 │ economic expansions.            │ idiosyncratic borrower risk.    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Primary Regulatory Purpose      │ **IFRS 9 Impairment & ECL**     │ **Basel III/IV Regulatory       │
│                                 │ Stress Testing (CCAR/PRA).      │ Capital (IRB) / RWAs**.         │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Monitoring Implication          │ Expected to vary with macro data│ Should remain completely stable │
│                                 │ if macro moves, model adjusts.  │ over time; drift triggers alert.│
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 2. Loss Given Default (LGD) Models

**Loss Given Default (LGD)** is the economic percentage loss incurred by the bank if an obligor defaults:

$$\text{LGD} = 1 - \text{Recovery Rate}$$

### 2.1 The Workout LGD Methodology (Discounted Cash Flows)
In commercial and retail banking, LGD is calculated empirically using the **Workout LGD** approach:

$$\text{Workout LGD} = 1 - \frac{\sum_{t=1}^{T} \frac{\text{Recoveries}_t - \text{Workout Costs}_t}{(1 + \text{EIR})^t}}{\text{EAD}}$$

- $\text{Recoveries}_t$: Direct cash collections, collateral liquidation proceeds, guarantee payouts received in period $t$.
- $\text{Workout Costs}_t$: Legal fees, asset repossession expenses, third-party collection agency commissions.
- $\text{EIR}$: The **Effective Interest Rate** of the loan, used to discount recoveries back to the date of default to reflect the time value of money.

### 2.2 Downturn LGD (Basel Requirement)
Under Basel Internal Ratings-Based (IRB) rules, banks cannot simply use average historical LGD. They must calibrate **Downturn LGD**:
- Reflects the severe losses observed during a severe economic recession (when asset/property prices collapse and liquidation haircuts widen).
- *Regulatory Floor*: Under Basel III/IV reforms, residential mortgages face a mandatory **minimum LGD floor of 10%**, while unsecured consumer credit faces an LGD floor of **50%**.

### 2.3 Cure Rates
A critical driver in retail LGD monitoring is the **Cure Rate**:
- The percentage of defaulted accounts (90 DPD) that successfully rehabilitate and resume full payments without the bank incurring a permanent financial loss.
- In mortgages, cure rates can reach 20% to 40%; in unsecured credit cards, cure rates are typically under 5%.

---

## 3. Exposure at Default (EAD) & Credit Conversion Factors

For fixed-term amortizing loans (e.g., an auto loan), EAD is simply the outstanding balance plus accrued unpaid interest: $\text{EAD} = \text{Drawn Balance}$.

However, for **revolving facilities** (Credit Cards, Overdrafts, Corporate Revolving Credit Facilities [RCF]), borrowers have the legal right to draw down additional funds up to their approved limit. Borrowers facing distress typically draw down their lines aggressively before defaulting:

$$\mathbf{EAD = \text{Drawn Balance} + \text{CCF} \times \text{Undrawn Commitment}}$$

Where **Credit Conversion Factor (CCF)** represents the percentage of currently undrawn available credit that the borrower will draw down before the default date:

$$\text{CCF} = \frac{\text{EAD}_{\text{actual}} - \text{Drawn Balance}}{\text{Credit Limit} - \text{Drawn Balance}}$$

```
┌─────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│        Facility Type            │            Regulatory / Monitored CCF Benchmark             │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Credit Cards (Retail Revolving) │ Typically 50% to 80% (Higher for subprime, lower for prime) │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Corporate Committed Facilities  │ Basel Foundation IRB mandates 75%; Advanced IRB uses models │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ Uncommitted / Cancelable Lines  │ Basel IV mandates 10% floor (historical 0% removed)         │
└─────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 4. Machine Learning vs. Traditional Statistical Scorecards

While machine learning (XGBoost, Random Forests) has revolutionized data science, its deployment in regulated credit risk is governed by strict supervisory constraints:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Evaluation Dimension     │   Logistic Regression Scorecard │   Machine Learning (XGBoost)    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Predictive Discrimination (AUC) │ Good (AUC ~ 0.72 – 0.80)        │ Superior (AUC ~ 0.82 – 0.88)    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Interpretability / Explainability│ Completely transparent; linear  │ Complex non-linear interactions;│
│                                 │ log-odds score allocation       │ requires SHAP / TreeExplainer   │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Regulatory Compliance           │ Universally approved by PRA,    │ Challenged by regulators over   │
│                                 │ EBA, Fed; easy adverse action   │ "black box" risks & unfair bias │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Monotonicity                    │ Enforced via monotonic WoE bins │ Risk of non-monotonic artifacts │
│                                 │ (higher score = strictly lower p│ (requires monotonic constraints)│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Primary Banking Role            │ **Production Decision Models**  │ **Challenger Models**, Fraud,   │
│                                 │ Regulatory Capital & IFRS 9     │ Marketing response & Collections│
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

> [!IMPORTANT]
> **Key Interview Takeaway**: In credit risk, **explainability and stability trumps marginal AUC gains**. A bank will happily choose a logistic scorecard with 0.76 AUC that is stable and explainable over an XGBoost model with 0.81 AUC that exhibits unstable feature interactions under macroeconomic stress.


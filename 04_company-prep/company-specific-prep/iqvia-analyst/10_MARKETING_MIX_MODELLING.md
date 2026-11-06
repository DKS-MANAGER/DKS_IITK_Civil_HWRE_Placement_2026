# Module 10: Marketing Mix Modelling (MMM) & Econometric Attribution

> **Document Status**: Authoritative Technical & Commercial Guide `[TIER 2 / IQVIA CORE ANALYTICS & TIER 4 / ECONOMETRIC STANDARDS]`  
> **Core Focus**: Econometric Formulation, Adstock Carryover Physics, Hill Saturation, Bayesian vs Frequentist MMM, Contribution Decomposition, and Complete End-to-End Python Project  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. What is Marketing Mix Modelling in Biopharma?

Marketing Mix Modelling (MMM) is an advanced econometric technique that quantifies the past impact and predicts the future return of multi-channel promotional investments on pharmaceutical brand sales (TRx, NRx, or Net Sales Revenue).

In life sciences, MMM answers three non-negotiable executive questions:
1. **Attribution**: *"Out of \$50M in annual brand revenue, how many dollars were driven by field-force detailing vs digital physician emails vs medical conferences vs baseline patient inertia?"*
2. **Efficiency (ROI)**: *"What was the return on investment (ROI) and marginal ROI (mROI) for each individual promotional dollar spent across channels?"*
3. **Budget Optimization**: *"If our brand budget is \$10M next year, how should we reallocate spend across channels to maximize top-line revenue?"*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PHARMACEUTICAL SALES DECOMPOSITION                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ TOTAL BRAND SALES = BASELINE VOLUME (70–85%) + INCREMENTAL PROMOTION (15–30%)│
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 1. BASELINE SALES (Organic Inertia)  │ 2. INCREMENTAL PROMOTIONAL SALES     │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ • Chronic patient repeat refills     │ • Field sales rep detailing visits   │
│ • Longstanding brand equity          │ • Virtual e-detailing & video calls  │
│ • Underlying disease prevalence      │ • Digital programmatic banners       │
│ • Formulary Tier 1/2 insurance access│ • Sponsored medical congresses & symp│
│ • Organic word-of-mouth adoption     │ • Product sampling & co-pay cards    │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. The Twin Non-Linear Pillars of MMM: Adstock & Saturation

Standard linear regression ($\text{Sales} = \beta \times \text{Spend}$) fails catastrophically in commercial marketing because it violates two fundamental laws of human psychology: **Memory Decay** and **Diminishing Returns**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE TWIN NON-LINEAR MARKETING TRANSFORMS                 │
│                                                                             │
│ 1. ADSTOCK (Memory Carryover)              2. SATURATION (Diminishing Return)│
│    Spend ▲                                    Sales ▲                        │
│          │    Peak                                  │       Saturating       │
│          │    ┌───┐                                 │       Plateau          │
│          │   /     \ Exponential                    │      .─────────────    │
│          │  /       \ Decay                         │    .─                  │
│          │ /         \                              │  .─                    │
│          └─────────────┴─────► Time                 └─┴──────────────────►   │
│                                                          Promotional Spend   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Adstock Transformation (Memory Carryover Effect)
When a sales representative details a physician today, the doctor does not forget the drug tomorrow. Prescribing impact lingers across subsequent weeks with geometric decay:

#### Geometric Adstock Formulation
$$A_t = X_t + \lambda A_{t-1}, \qquad \lambda \in [0, 1)$$
where:
* $X_t$: Raw promotional activity (spend, details, impressions) at week $t$.
* $\lambda$: Decay parameter (retention rate).
* $A_t$: Cumulative adstocked promotional stock available at week $t$.

#### Half-Life Derivation
The half-life ($t_{1/2}$) is the time required for promotional impact to decay to $50\%$ of its initial intensity:
$$\lambda^{t_{1/2}} = 0.5 \iff t_{1/2} \ln(\lambda) = \ln(0.5) \iff \boxed{t_{1/2} = \frac{-\ln(2)}{\ln(\lambda)}}$$

* *Benchmark Values in Pharma*:
  * Field sales rep detailing: $\lambda \approx 0.60\text{–}0.80$ ($t_{1/2} \approx 1.4\text{ to } 3.1\text{ weeks}$).
  * Digital display ads / banners: $\lambda \approx 0.15\text{–}0.35$ ($t_{1/2} \approx 0.4\text{ to } 0.7\text{ weeks}$).
  * Major Medical Congresses (ASCO/AHA): $\lambda \approx 0.85\text{–}0.92$ ($t_{1/2} \approx 4.3\text{ to } 8.3\text{ weeks}$).

### 2.2 Diminishing Returns & Saturation Curves (Hill Function)
Doubling promotional spend does not double prescription response. After a certain threshold, physicians experience cognitive wear-out and reach prescribing capacity:

#### The Hill Saturation Function
$$f(A_t; K, S) = \frac{A_t^S}{K^S + A_t^S}$$
where:
* $K > 0$: Half-saturation parameter (the adstock level at which response reaches $50\%$ of maximum potential).
* $S > 0$: Shape / slope parameter:
  * $S \le 1$: Pure concave diminishing returns curve (standard in mature pharmaceutical markets).
  * $S > 1$: Sigmoidal S-curve (initial inflection / threshold effect before saturation, typical in new therapy launches).

---

## 3. Econometric Model Specification: Multiplicative vs Additive

### 3.1 Log-Log (Multiplicative) Specification
In commercial analytics, multiplicative formulations are widely favored because promotional channels interact synergistically:
$$\ln(\text{TRx}_t) = \beta_0 + \sum_{i=1}^{p} \beta_i \ln\left(f(A_{i,t}) + 1\right) + \gamma \text{Trend}_t + \sum_{m=1}^{11} \delta_m \text{Month}_{m,t} + \varepsilon_t$$
* **Key Advantage**: Coefficients $\beta_i$ represent **direct constant elasticities**: a $1\%$ increase in channel $i$ spend produces a $\beta_i\%$ increase in brand prescriptions.

### 3.2 Frequentist vs Bayesian MMM
* **Frequentist OLS Limitations**: Marketing variables are inherently multicollinear (spend across detailing, digital, and conferences spikes simultaneously in Q1 and Q3). OLS yields unstable, inverted negative coefficients ($\beta_{\text{detailing}} < 0$).
* **Bayesian Advantage**: By encoding domain priors (e.g., specifying that detailing elasticity must be strictly positive via $\beta_{\text{detail}} \sim \text{HalfNormal}(\sigma)$), Bayesian MCMC (via Stan or PyMC) stabilizes parameter estimation and yields full posterior probability distributions for ROI.

---

## 4. Decomposition, Channel Contribution & ROI Mechanics

### 4.1 Channel Volume Contribution
For an additive model:
$$\hat{Y}_t = \text{Baseline}_t + \sum_{i=1}^{p} \text{Contrib}_{i,t}$$
$$\text{Percentage Contribution of Channel } i = \frac{\sum_{t=1}^{T} \text{Contrib}_{i,t}}{\sum_{t=1}^{T} \hat{Y}_t} \times 100\%$$

### 4.2 Return on Investment (ROI) and Marginal ROI (mROI)
* **Average ROI**: Total incremental profit generated divided by total promotional spend:
  $$\text{ROI}_i = \frac{\text{Incremental Brand Margin}_i}{\text{Total Channel Spend}_i} = \frac{\left(\sum_t \text{Contrib}_{i,t} \times \text{Net Margin per TRx}\right)}{\sum_t \text{Spend}_{i,t}}$$
* **Marginal ROI (mROI)**: The incremental revenue generated by the *very next dollar* allocated:
  $$\text{mROI}_i = \frac{\partial (\text{Incremental Revenue})}{\partial (\text{Spend}_i)}$$
* **The Golden Optimization Theorem**: Under a constrained marketing budget, total portfolio revenue is maximized when **marginal ROIs are equalized across all channels**:
  $$\text{mROI}_1 = \text{mROI}_2 = \dots = \text{mROI}_p$$

---

## 5. End-to-End Production Python Project: Simulated MMM & Optimization

```python
"""
Module 10: Complete End-to-End Pharmaceutical Marketing Mix Model
1. Generates 104 weeks of synthetic biopharma commercial data.
2. Applies Geometric Adstock and Hill Saturation transformations.
3. Fits econometric regression model.
4. Computes baseline vs incremental contributions, ROI, and optimal budget reallocation.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize

# ==============================================================================
# STEP 1: MATHEMATICAL TRANSFORMATION ENGINES
# ==============================================================================
def geometric_adstock(x: np.ndarray, decay_rate: float) -> np.ndarray:
    """Applies geometric adstock carryover transformation: A_t = X_t + decay * A_{t-1}."""
    adstocked = np.zeros_like(x, dtype=float)
    adstocked[0] = x[0]
    for t in range(1, len(x)):
        adstocked[t] = x[t] + decay_rate * adstocked[t - 1]
    return adstocked

def hill_saturation(x: np.ndarray, k: float, s: float) -> np.ndarray:
    """Applies Hill function saturation: f(x) = x^s / (k^s + x^s)."""
    return (x ** s) / (k ** s + x ** s)

# ==============================================================================
# STEP 2: SYNTHESIZE PHARMACEUTICAL COMMERCIAL DATASET (104 WEEKS)
# ==============================================================================
np.random.seed(42)
n_weeks = 104
dates = pd.date_range(start='2024-01-01', periods=n_weeks, freq='W-MON')

# Raw Weekly Spends ($)
detailing_raw = np.random.gamma(shape=8, scale=5000, size=n_weeks)    # Rep Details
digital_raw = np.random.gamma(shape=5, scale=3000, size=n_weeks)      # Digital Ads
congress_raw = np.zeros(n_weeks)                                      # Medical Congresses
congress_raw[np.random.choice(n_weeks, size=8, replace=False)] = np.random.uniform(40000, 80000, 8)

# Apply Known True Physics
adstocked_detail = geometric_adstock(detailing_raw, decay_rate=0.70)
adstocked_digital = geometric_adstock(digital_raw, decay_rate=0.30)
adstocked_congress = geometric_adstock(congress_raw, decay_rate=0.85)

sat_detail = hill_saturation(adstocked_detail, k=50000, s=1.0)
sat_digital = hill_saturation(adstocked_digital, k=25000, s=1.0)
sat_congress = hill_saturation(adstocked_congress, k=80000, s=1.0)

# True Brand Sales DGP (TRx Units)
base_sales = 8000 + 15 * np.sin(2 * np.pi * np.arange(n_weeks) / 52)  # Organic Baseline
true_coefs = {'Detail': 12000, 'Digital': 6500, 'Congress': 9500}
noise = np.random.normal(0, 300, size=n_weeks)

brand_trx = (base_sales + 
             true_coefs['Detail'] * sat_detail + 
             true_coefs['Digital'] * sat_digital + 
             true_coefs['Congress'] * sat_congress + noise)

df = pd.DataFrame({
    'Week': dates,
    'Brand_TRx': brand_trx,
    'Spend_Detail': detailing_raw,
    'Spend_Digital': digital_raw,
    'Spend_Congress': congress_raw,
    'Transformed_Detail': sat_detail,
    'Transformed_Digital': sat_digital,
    'Transformed_Congress': sat_congress
}).set_index('Week')

# ==============================================================================
# STEP 3: FIT ECONOMETRIC REGRESSION MODEL
# ==============================================================================
X = df[['Transformed_Detail', 'Transformed_Digital', 'Transformed_Congress']]
X_reg = sm.add_constant(X)
y = df['Brand_TRx']

mmm_model = sm.OLS(y, X_reg).fit()

# ==============================================================================
# STEP 4: SALES DECOMPOSITION & CONTRIBUTION AUDIT
# ==============================================================================
net_price_per_trx = 150.0  # $150 net revenue per prescription

predicted_total_trx = mmm_model.fittedvalues.sum()
baseline_trx = mmm_model.params['const'] * n_weeks
detail_trx = (mmm_model.params['Transformed_Detail'] * df['Transformed_Detail']).sum()
digital_trx = (mmm_model.params['Transformed_Digital'] * df['Transformed_Digital']).sum()
congress_trx = (mmm_model.params['Transformed_Congress'] * df['Transformed_Congress']).sum()

total_spend_detail = df['Spend_Detail'].sum()
total_spend_digital = df['Spend_Digital'].sum()
total_spend_congress = df['Spend_Congress'].sum()

# Compute Total Revenue & ROI
detail_revenue = detail_trx * net_price_per_trx
digital_revenue = digital_trx * net_price_per_trx
congress_revenue = congress_trx * net_price_per_trx

roi_detail = detail_revenue / total_spend_detail
roi_digital = digital_revenue / total_spend_digital
roi_congress = congress_revenue / total_spend_congress

print("="*75)
print("             IQVIA COMMERCIAL MARKETING MIX MODEL RESULTS")
print("="*75)
print(f"Model R-squared: {mmm_model.rsquared:.4f} | Adj. R-squared: {mmm_model.rsquared_adj:.4f}")
print("\n--- SALES VOLUME DECOMPOSITION ---")
print(f"Baseline (Organic) Prescriptions: {baseline_trx:10.0f} ({baseline_trx/predicted_total_trx*100:5.1f}%)")
print(f"Field Detailing Contribution:     {detail_trx:10.0f} ({detail_trx/predicted_total_trx*100:5.1f}%)")
print(f"Digital Channel Contribution:     {digital_trx:10.0f} ({digital_trx/predicted_total_trx*100:5.1f}%)")
print(f"Medical Congress Contribution:    {congress_trx:10.0f} ({congress_trx/predicted_total_trx*100:5.1f}%)")
print(f"Total Predicted Brand TRx:        {predicted_total_trx:10.0f} (100.0%)")

print("\n--- PROMOTIONAL RETURN ON INVESTMENT (ROI) ---")
print(f"Field Sales Detailing ROI: ${roi_detail:.2f} revenue per $1.00 spend")
print(f"Digital Advertising ROI:   ${roi_digital:.2f} revenue per $1.00 spend")
print(f"Medical Congresses ROI:    ${roi_congress:.2f} revenue per $1.00 spend")

# ==============================================================================
# STEP 5: EXECUTIVE BUDGET OPTIMIZATION (SCIPY CONSTRAINED OPTIMIZATION)
# ==============================================================================
current_total_budget = total_spend_detail + total_spend_digital + total_spend_congress

def negative_revenue_objective(weights):
    """Negative revenue to be minimized."""
    spend_det, spend_dig, spend_cong = weights
    # Average weekly spend
    w_det = spend_det / n_weeks
    w_dig = spend_dig / n_weeks
    w_cong = spend_cong / n_weeks
    
    # Estimate steady-state transformed response
    steady_adstock_det = w_det / (1 - 0.70)
    steady_adstock_dig = w_dig / (1 - 0.30)
    steady_adstock_cong = w_cong / (1 - 0.85)
    
    resp_det = hill_saturation(steady_adstock_det, 50000, 1.0)
    resp_dig = hill_saturation(steady_adstock_dig, 25000, 1.0)
    resp_cong = hill_saturation(steady_adstock_cong, 80000, 1.0)
    
    total_rev = (mmm_model.params['Transformed_Detail'] * resp_det + 
                 mmm_model.params['Transformed_Digital'] * resp_dig + 
                 mmm_model.params['Transformed_Congress'] * resp_cong) * n_weeks * net_price_per_trx
    return -total_rev

# Constraints & Bounds
budget_constraint = {'type': 'eq', 'fun': lambda w: sum(w) - current_total_budget}
bounds = [(current_total_budget * 0.1, current_total_budget * 0.7) for _ in range(3)]
initial_guess = [total_spend_detail, total_spend_digital, total_spend_congress]

opt_result = minimize(negative_revenue_objective, initial_guess, method='SLSQP', bounds=bounds, constraints=budget_constraint)

print("\n" + "="*75)
print("             EXECUTIVE PORTFOLIO REALLOCATION RECOMMENDATION")
print("="*75)
print(f"Current Spend Allocation   : Detail: ${total_spend_detail:,.0f} | Digital: ${total_spend_digital:,.0f} | Congress: ${total_spend_congress:,.0f}")
print(f"Optimized Spend Allocation : Detail: ${opt_result.x[0]:,.0f} | Digital: ${opt_result.x[1]:,.0f} | Congress: ${opt_result.x[2]:,.0f}")
print(f"Projected Incremental Gain : ${( -opt_result.fun - (detail_revenue + digital_revenue + congress_revenue) ):,.0f} net brand revenue")
```


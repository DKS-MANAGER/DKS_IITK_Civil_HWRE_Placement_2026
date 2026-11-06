# Module 14: Hierarchical & Bayesian Modelling in Biopharma Analytics

> **Document Status**: Production-Grade Advanced Modeling Reference `[TIER 2 / ADVANCED PROFORMA SPECIFICATION & TIER 4 / BAYESIAN STANDARDS]`  
> **Core Focus**: Multilevel Regression, Partial Pooling Shrinkage, Mixed-Effects Models, MCMC Mechanics (NUTS/HMC), Convergence Diagnostics, and Python Implementation  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Why Hierarchical Models are Essential in Commercial Healthcare

Healthcare commercial data exhibits an intrinsically nested, multilevel hierarchical structure:
* Individual Patients are nested within Prescribing Physicians.
* Physicians are nested within Zip Codes and Sales Territories.
* Sales Territories are nested within Geographic Regions.
* Products are nested within Therapeutic Classes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 NESTED HIERARCHICAL STRUCTURE IN PHARMA DATA                │
│                                                                             │
│ [ National Brand Performance ]                                              │
│       │                                                                     │
│       ├── [ Region 1: US Northeast ]        ├── [ Region 2: US South ]      │
│       │        │                                     │                      │
│       │        ├── Territory 101                     ├── Territory 201      │
│       │        │       │                                     │              │
│       │        │       └── Dr. Smith (Oncologist)            └── Dr. Davis  │
│       │        │                 │                                          │
│       │        │                 └── Patient Claims A, B, C                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Complete Pooling vs No Pooling vs Partial Pooling

When estimating physician detailing response across 50 territories, standard analytics approaches fail at the extremes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     THE THREE POOLING PARADIGMS                             │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ COMPLETE POOLING         │ NO POOLING               │ PARTIAL POOLING       │
│ (One Single Model)       │ (50 Separate Models)     │ (Hierarchical Model)  │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ • Combines all data into │ • Fits an isolated linear│ • Estimates territory-│
│   a single regression.   │   model for each region. │   specific effects    │
│ • Assumes all territories│ • Treats each territory  │   drawn from a shared │
│   respond identically.   │   as totally independent.│   prior distribution. │
│ ⚠️ Ignores genuine local  │ ⚠️ Overfits small regions │ ✅ **SHRINKAGE EFFECT**:│
│   payer and demographic  │   with few physicians;   │   Borrow statistical  │
│   heterogeneity.         │   massive variance.      │   strength safely.    │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

### 2.1 The Shrinkage Principle
In partial pooling, estimates for territories with **small sample sizes** or high noise are pulled strongly toward the national population mean. Conversely, territories with **large sample sizes** and rich data retain their localized estimates.

---

## 3. Linear Mixed-Effects Models (LMM)

### 3.1 Mathematical Matrix Specification
$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \mathbf{Z}\mathbf{u} + \boldsymbol{\varepsilon}$$
where:
* $\mathbf{y} \in \mathbb{R}^{N \times 1}$: Observed dependent variable (e.g., Physician Brand TRx).
* $\mathbf{X} \in \mathbb{R}^{N \times p}$: Design matrix for **Fixed Effects** (population-level averages).
* $\boldsymbol{\beta} \in \mathbb{R}^{p \times 1}$: Fixed-effects regression coefficients.
* $\mathbf{Z} \in \mathbb{R}^{N \times q}$: Design matrix for **Random Effects** (group/territory-level deviations).
* $\mathbf{u} \in \mathbb{R}^{q \times 1}$: Vector of random effects, assumed $\mathbf{u} \sim \mathcal{N}(\mathbf{0}, \mathbf{G})$.
* $\boldsymbol{\varepsilon} \in \mathbb{R}^{N \times 1}$: Residual error vector, assumed $\boldsymbol{\varepsilon} \sim \mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I})$.

### 3.2 Random Intercept vs Random Slope Models
1. **Random Intercept Model**: Assumes promotional responsiveness ($\beta_1$) is constant nationally, but baseline prescribing volume varies by territory ($u_{0j}$):
   $$y_{ij} = (\beta_0 + u_{0j}) + \beta_1 x_{ij} + \varepsilon_{ij}, \qquad u_{0j} \sim \mathcal{N}(0, \sigma_u^2)$$
2. **Random Slope Model**: Allows both baseline volume and promotional detailing effectiveness to vary by territory:
   $$y_{ij} = (\beta_0 + u_{0j}) + (\beta_1 + u_{1j}) x_{ij} + \varepsilon_{ij}, \qquad \begin{bmatrix} u_{0j} \\ u_{1j} \end{bmatrix} \sim \mathcal{N}\left(\mathbf{0}, \begin{bmatrix} \sigma_0^2 & \sigma_{01} \\ \sigma_{01} & \sigma_1^2 \end{bmatrix}\right)$$

### 3.3 Intraclass Correlation Coefficient (ICC)
The ICC ($\rho$) measures the proportion of total variance attributable to clustering between territories:
$$\rho = \frac{\sigma_{\text{between}}^2}{\sigma_{\text{between}}^2 + \sigma_{\text{within}}^2} = \frac{\sigma_{u0}^2}{\sigma_{u0}^2 + \sigma_\varepsilon^2}$$
* $\rho > 0.05\text{–}0.10$ indicates that hierarchical multilevel modeling is strictly necessary; ignoring it leads to artificially deflated standard errors and severe Type I errors.

---

## 4. Bayesian Inference & MCMC Sampling

### 4.1 Bayes' Theorem for Continuous Parameter Vectors
$$P(\boldsymbol{\theta} | \mathcal{D}) = \frac{P(\mathcal{D} | \boldsymbol{\theta}) P(\boldsymbol{\theta})}{P(\mathcal{D})} = \frac{\mathcal{L}(\boldsymbol{\theta}; \mathcal{D}) \pi(\boldsymbol{\theta})}{\int \mathcal{L}(\boldsymbol{\theta}'; \mathcal{D}) \pi(\boldsymbol{\theta}') d\boldsymbol{\theta}'} \propto \mathcal{L}(\boldsymbol{\theta}; \mathcal{D}) \pi(\boldsymbol{\theta})$$
$$\text{Posterior} \propto \text{Likelihood} \times \text{Prior}$$

### 4.2 Modern MCMC: Hamiltonian Monte Carlo (HMC) & NUTS
High-dimensional Bayesian models cannot be integrated analytically. The **No-U-Turn Sampler (NUTS)** simulates physical Hamiltonian dynamics across the posterior probability surface, taking vector gradients ($\nabla \ln P(\boldsymbol{\theta}|\mathcal{D})$) to explore complex, correlated parameter spaces thousands of times faster than random-walk Metropolis-Hastings.

### 4.3 MCMC Convergence Diagnostics
Before accepting Bayesian estimates, commercial analysts verify four convergence criteria:
1. **Gelman-Rubin Statistic ($\hat{R}$)**: Compares variance between independent MCMC chains to variance within chains. **Must satisfy $\hat{R} < 1.05$** (ideally $\le 1.01$).
2. **Effective Sample Size (ESS)**: Number of independent, un-autocorrelated posterior draws. Target $\text{ESS}_{\text{bulk}} > 400$ and $\text{ESS}_{\text{tail}} > 400$.
3. **Divergent Transitions**: Energy conservation errors in the HMC leapfrog integrator indicating high-curvature posterior geometry. **Must be 0**.
4. **Posterior Predictive Checks (PPC)**: Simulating synthetic datasets from the fitted posterior ($\mathbf{y}^{\text{rep}} \sim P(\mathbf{y}|\mathcal{D})$) and verifying that observed distributions match model predictions.

---

## 5. Python Implementation: Fitting Hierarchical Mixed Models

```python
"""
Module 14: Production Hierarchical Linear Mixed-Effects Model
Fits a random-intercept model across sales territories using statsmodels.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 1. Generate Synthetic Multilevel Commercial Dataset
np.random.seed(42)
n_territories = 25
physicians_per_territory = 40
total_n = n_territories * physicians_per_territory

# Territory-level baseline differences (Random Intercepts)
true_territory_effects = np.random.normal(loc=0, scale=15.0, size=n_territories)
territory_ids = np.repeat(np.arange(n_territories), physicians_per_territory)

# Physician-level detailing calls
detailing_calls = np.random.poisson(lam=6, size=total_n)

# Fixed coefficients
beta_0 = 45.0  # National baseline prescriptions
beta_1 = 4.2   # Detailing response slope
residual_noise = np.random.normal(loc=0, scale=8.0, size=total_n)

# Dependent Variable: Physician TRx
brand_trx = (beta_0 + 
             true_territory_effects[territory_ids] + 
             beta_1 * detailing_calls + 
             residual_noise)

df = pd.DataFrame({
    'Territory_ID': pd.Categorical(territory_ids),
    'Detailing_Calls': detailing_calls,
    'Brand_TRx': brand_trx
})

# 2. Fit Linear Mixed-Effects Model (Random Intercept by Territory)
mixed_model = smf.mixedlm(
    "Brand_TRx ~ Detailing_Calls", 
    data=df, 
    groups=df["Territory_ID"]
).fit()

print("="*75)
print("             HIERARCHICAL MIXED-EFFECTS MODEL SUMMARY")
print("="*75)
print(mixed_model.summary())

# Extract Variance Components & Intraclass Correlation (ICC)
var_between = mixed_model.cov_re.iloc[0, 0]  # Territory variance sigma_u^2
var_within = mixed_model.scale               # Residual variance sigma_e^2
icc = var_between / (var_between + var_within)

print("\n--- VARIANCE DECOMPOSITION & ICC ---")
print(f"Between-Territory Variance (sigma_u^2) : {var_between:8.2f}")
print(f"Within-Territory Residual  (sigma_e^2) : {var_within:8.2f}")
print(f"Intraclass Correlation (ICC / rho)     : {icc:8.4f} ({icc*100:.1f}% variance at territory level)")
```


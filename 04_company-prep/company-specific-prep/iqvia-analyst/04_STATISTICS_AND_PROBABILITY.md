# Module 04: Statistics & Probability for Commercial Analytics

> **Document Status**: High-Yield Theoretical & Practical Reference `[TIER 4 / STATISTICAL THEORY & NIST BENCHMARKS]`  
> **Core Focus**: Descriptive Statistics, Probability Distributions, Hypothesis Testing, OLS Regression, Diagnostics, and Logistic Regression with Healthcare Examples  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Descriptive Statistics & Summary Metrics

### 1.1 Measures of Central Tendency
* **Sample Mean ($\bar{x}$)**: Arithmetic average, sensitive to extreme outliers:
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$
* **Median**: Middle value in an ordered dataset. Robust to extreme skewness (e.g., physician prescription counts where the top 10% of specialists write 80% of scripts).
  $$\text{Median} = \begin{cases} x_{(n+1)/2} & \text{if } n \text{ is odd} \\ \frac{1}{2}\left(x_{(n/2)} + x_{(n/2)+1}\right) & \text{if } n \text{ is even} \end{cases}$$
* **Mode**: Most frequently occurring observation. Useful for categorical variables (e.g., most common physician specialty or payer plan).

### 1.2 Measures of Dispersion & Shape
* **Sample Variance ($s^2$) & Standard Deviation ($s$)**: Utilizing Bessel's correction ($n-1$) to yield an unbiased estimator of population variance:
  $$s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar{x})^2, \qquad s = \sqrt{s^2}$$
* **Interquartile Range (IQR)**: Difference between the 75th percentile ($Q_3$) and 25th percentile ($Q_1$). Tukey's fence defines outliers as points outside:
  $$[Q_1 - 1.5 \times \text{IQR}, \quad Q_3 + 1.5 \times \text{IQR}]$$
* **Skewness ($\gamma_1$)**: Degree of asymmetry around the mean:
  $$\gamma_1 = \frac{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^3}{\left(\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2\right)^{3/2}}$$
  * $\gamma_1 > 0$: Positive / right-skewed (tail extends right; Mean > Median; typical for healthcare sales and prescribing volumes).
  * $\gamma_1 < 0$: Negative / left-skewed (tail extends left; Mean < Median).
* **Kurtosis ($\gamma_2$)**: Measure of peakedness and tail fatness relative to a normal distribution:
  $$\text{Excess Kurtosis} = \frac{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^4}{\left(\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2\right)^2} - 3$$
  * Leptokurtic ($\gamma_2 > 0$): Fat tails, higher outlier risk than Gaussian.

---

## 2. Probability Fundamentals & Bayes' Theorem

### 2.1 Core Axioms & Conditional Probability
* **Joint Probability**: $P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$
* **Independence**: Events $A$ and $B$ are independent iff $P(A \cap B) = P(A)P(B) \iff P(A|B) = P(A)$.
* **Law of Total Probability**: If $B_1, B_2, \dots, B_k$ partition the sample space:
  $$P(A) = \sum_{j=1}^{k} P(A|B_j)P(B_j)$$

### 2.2 Bayes' Theorem in Commercial Healthcare
Updating prior beliefs with new empirical evidence:
$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^{k} P(A|B_j)P(B_j)}$$

#### Worked Numerical Problem: Diagnostic Test Sensitivity & Specificity
* A rare oncology condition has a prevalence of $0.5\%$ ($P(D) = 0.005$).
* A companion diagnostic assay exhibits **$98\%$ sensitivity** ($P(+|D) = 0.98$) and **$95\%$ specificity** ($P(-|\neg D) = 0.95 \implies P(+|\neg D) = 0.05$).
* A randomly selected patient tests positive ($+$). What is the true probability that the patient has the disease (Positive Predictive Value / PPV)?

$$\begin{aligned}
P(D|+) &= \frac{P(+|D)P(D)}{P(+|D)P(D) + P(+|\neg D)P(\neg D)} \\
&= \frac{0.98 \times 0.005}{(0.98 \times 0.005) + (0.05 \times 0.995)} \\
&= \frac{0.0049}{0.0049 + 0.04975} = \frac{0.0049}{0.05465} \approx \mathbf{0.0897 \text{ (or } 8.97\%)}
\end{aligned}$$

> **Key Commercial Insight**: Even with a 98% sensitive and 95% specific test, a positive result indicates less than a 9% probability of actual disease because the base rate prevalence is low. In commercial pharmaceutical targeting, failing to account for base rates leads to massive misallocation of diagnostic detailing resources.

---

## 3. Parametric Probability Distributions

| Distribution | Probability Mass / Density Function (PMF / PDF) | Mean ($\mu$) | Variance ($\sigma^2$) | Primary Pharma / Commercial Application |
| :--- | :--- | :---: | :---: | :--- |
| **Bernoulli($p$)** | $P(X=k) = p^k (1-p)^{1-k}, \quad k \in \{0, 1\}$ | $p$ | $p(1-p)$ | Physician conversion event (converts to brand or does not). |
| **Binomial($n, p$)** | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | Number of physicians who adopt a new therapy out of $n$ detailed. |
| **Poisson($\lambda$)** | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0,1,2,\dots$ | $\lambda$ | $\lambda$ | Number of adverse event reports received per week; rare disease arrivals. |
| **Exponential($\lambda$)** | $f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Time between consecutive patient prescription refills (adherence modeling). |
| **Normal($\mu, \sigma^2$)** | $f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$ | $\mu$ | $\sigma^2$ | Log-transformed sales volume; sampling distribution of estimators (CLT). |
| **Student's $t$($\nu$)** | $f(t) = \frac{\Gamma((\nu+1)/2)}{\sqrt{\nu\pi}\Gamma(\nu/2)}\left(1 + \frac{t^2}{\nu}\right)^{-(\nu+1)/2}$ | $0$ (for $\nu > 1$) | $\frac{\nu}{\nu-2}$ (for $\nu > 2$) | Hypothesis testing with unknown population variance on small samples. |

---

## 4. Sampling Theory, CLT & Hypothesis Testing

### 4.1 Central Limit Theorem (CLT) & Standard Error
Let $X_1, X_2, \dots, X_n$ be an independent and identically distributed (i.i.d.) random sample from any population with mean $\mu$ and finite variance $\sigma^2$. As $n \to \infty$:
$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$
* **Standard Error of the Mean (SEM)**: $\text{SE} = \frac{s}{\sqrt{n}}$.
* **Confidence Interval (95%)**:
  $$\text{CI}_{95\%} = \bar{x} \pm t_{\alpha/2, \, n-1} \left(\frac{s}{\sqrt{n}}\right)$$

### 4.2 Hypothesis Testing Framework & Error Matrix
* **Null Hypothesis ($H_0$)**: Baseline assumption of no effect or no difference (e.g., *"Digital detailing has zero impact on NRx"*).
* **Alternative Hypothesis ($H_1$)**: Operational claim to be validated.
* **$p$-value**: Probability of observing a test statistic as extreme as, or more extreme than, the observed value under the assumption that $H_0$ is true.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       HYPOTHESIS TESTING ERROR MATRIX                       │
├──────────────────────────┬────────────────────────┬─────────────────────────┤
│ DECISION TAKEN           │ $H_0$ IS ACTUALLY TRUE │ $H_0$ IS ACTUALLY FALSE │
├──────────────────────────┼────────────────────────┼─────────────────────────┤
│ Reject $H_0$             │ **Type I Error ($\alpha$)**│ Correct Decision        │
│ (Claim effect exists)    │ False Positive         │ **Power ($1 - \beta$)** │
├──────────────────────────┼────────────────────────┼─────────────────────────┤
│ Fail to Reject $H_0$     │ Correct Decision       │ **Type II Error ($\beta$)**│
│ (Do not claim effect)    │ Confidence ($1-\alpha$)│ False Negative          │
└──────────────────────────┴────────────────────────┴─────────────────────────┘
```

### 4.3 Common Statistical Test Formulations
1. **Two-Sample Independent $t$-Test (Equal Variances)**:
   $$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \qquad s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}$$
2. **One-Way Analysis of Variance (ANOVA)**:
   Tests whether means across $k$ promotional channels are equal ($H_0: \mu_1 = \mu_2 = \dots = \mu_k$).
   $$F = \frac{\text{MS}_{\text{between}}}{\text{MS}_{\text{within}}} = \frac{\text{SSB} / (k - 1)}{\text{SSW} / (N - k)}$$
   $$\text{SSB} = \sum_{j=1}^{k} n_j (\bar{x}_j - \bar{x}_{\text{grand}})^2, \qquad \text{SSW} = \sum_{j=1}^{k}\sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2$$
3. **Chi-Square Test of Independence ($\chi^2$)**:
   $$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}, \qquad E_{ij} = \frac{(\text{Row Total}_i)(\text{Column Total}_j)}{N}$$

---

## 5. Linear Regression (OLS) & Mathematical Derivation

### 5.1 Ordinary Least Squares Formulation
Consider the multiple linear regression model:
$$\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$
where $\mathbf{y} \in \mathbb{R}^{n \times 1}$, $\mathbf{X} \in \mathbb{R}^{n \times (p+1)}$, $\boldsymbol{\beta} \in \mathbb{R}^{(p+1) \times 1}$, and $\boldsymbol{\varepsilon} \in \mathbb{R}^{n \times 1}$.

OLS minimizes the Sum of Squared Residuals ($S(\boldsymbol{\beta})$):
$$S(\boldsymbol{\beta}) = \boldsymbol{\varepsilon}^T \boldsymbol{\varepsilon} = (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^T (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = \mathbf{y}^T\mathbf{y} - 2\boldsymbol{\beta}^T\mathbf{X}^T\mathbf{y} + \boldsymbol{\beta}^T\mathbf{X}^T\mathbf{X}\boldsymbol{\beta}$$

Taking the partial derivative with respect to $\boldsymbol{\beta}$ and setting to zero:
$$\frac{\partial S}{\partial \boldsymbol{\beta}} = -2\mathbf{X}^T\mathbf{y} + 2\mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{0}$$
$$\mathbf{X}^T\mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}^T\mathbf{y} \implies \boxed{\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}}$$

### 5.2 Gauss-Markov Theorem & OLS Assumptions
OLS produces the **Best Linear Unbiased Estimator (BLUE)** if:
1. **Linearity**: The relationship between regressors and dependent variable is linear in parameters.
2. **Strict Exogeneity**: $\mathbb{E}[\boldsymbol{\varepsilon}|\mathbf{X}] = \mathbf{0}$ (no correlation between errors and features; no omitted variable bias).
3. **No Multicollinearity**: $\mathbf{X}$ has full column rank ($\text{rank}(\mathbf{X}) = p+1$); $\mathbf{X}^T\mathbf{X}$ is invertible.
4. **Spherical Errors (Homoscedasticity & No Autocorrelation)**:
   $$\text{Var}(\boldsymbol{\varepsilon}|\mathbf{X}) = \sigma^2 \mathbf{I}_n$$
   * Homoscedasticity: Constant error variance $\text{Var}(\varepsilon_i) = \sigma^2$.
   * No Autocorrelation: $\text{Cov}(\varepsilon_i, \varepsilon_j) = 0$ for all $i \neq j$.

### 5.3 Goodness of Fit & Variance Decomposition
$$\text{SST} = \text{SSR} + \text{SSE} \iff \sum(y_i - \bar{y})^2 = \sum(\hat{y}_i - \bar{y})^2 + \sum(y_i - \hat{y}_i)^2$$
$$R^2 = 1 - \frac{\text{SSE}}{\text{SST}} = \frac{\text{SSR}}{\text{SST}}$$
* **Adjusted $R^2$**: Penalizes addition of non-informative regressors:
  $$R^2_{\text{adj}} = 1 - \left[\frac{\text{SSE} / (n - p - 1)}{\text{SST} / (n - 1)}\right] = 1 - (1 - R^2)\frac{n - 1}{n - p - 1}$$

---

## 6. Regression Diagnostics in Commercial Modeling

### 6.1 Multicollinearity & Variance Inflation Factor (VIF)
In pharmaceutical Marketing Mix Modeling, sales-rep detailing, digital display ads, and email campaigns frequently co-vary (heavy campaigns run simultaneously across channels).
$$VIF_j = \frac{1}{1 - R_j^2}$$
where $R_j^2$ is the $R^2$ obtained from regressing feature $x_j$ on all other regressors.
* **Interpretation**:
  * $\text{VIF} = 1$: Perfectly orthogonal (no collinearity).
  * $\text{VIF} > 5$: Moderate collinearity requiring attention.
  * $\text{VIF} > 10$: Severe collinearity; standard errors of $\hat{\beta}_j$ are inflated by $\sqrt{\text{VIF}} > 3.16$, destabilizing channel ROI attribution.
* **Remedies**: Ridge regression ($\ell_2$ penalty), PCA dimensionality reduction, or combining collinear channels.

### 6.2 Heteroscedasticity & Autocorrelation
* **Heteroscedasticity**: Non-constant variance across observations (e.g., high-prescribing tier physicians exhibit much wider prescription variance than low prescribers).
  * *Test*: **Breusch-Pagan test** or **White's test**.
  * *Remedy*: Logarithmic transformation ($\ln(y)$) or Huber-White robust standard errors (`HC3`).
* **Autocorrelation**: Error terms correlate across sequential time periods ($\text{Cov}(\varepsilon_t, \varepsilon_{t-1}) \neq 0$).
  * *Test*: **Durbin-Watson statistic**:
    $$d = \frac{\sum_{t=2}^{T} (e_t - e_{t-1})^2}{\sum_{t=1}^{T} e_t^2} \approx 2(1 - \rho)$$
    * $d \approx 2$: No autocorrelation.
    * $d < 1.5$: Positive autocorrelation (typical in sales time-series; inflates $t$-statistics and creates false significance).

---

## 7. Logistic Regression & Binary Classification

When modeling whether a physician becomes an adopter ($y_i \in \{0, 1\}$), linear probability models ($y = \mathbf{x}^T\boldsymbol{\beta}$) predict probabilities outside $[0, 1]$. Logistic regression maps the linear predictor to probabilities via the **logit link / sigmoid function**:

$$p_i = P(y_i = 1 | \mathbf{x}_i) = \sigma(\mathbf{x}_i^T\boldsymbol{\beta}) = \frac{1}{1 + e^{-\mathbf{x}_i^T\boldsymbol{\beta}}}$$

### 7.1 Odds and Log-Odds (Logit)
$$\text{Odds} = \frac{p_i}{1 - p_i} = e^{\mathbf{x}_i^T\boldsymbol{\beta}}$$
$$\text{Logit}(p_i) = \ln\left(\frac{p_i}{1 - p_i}\right) = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip}$$

* **Interpreting Odds Ratios (OR)**:
  For a unit increase in $x_j$, the odds of adoption multiply by $e^{\beta_j}$:
  $$\text{OR}_j = \frac{\text{Odds}(x_j + 1)}{\text{Odds}(x_j)} = e^{\beta_j}$$
  * If $\beta_j = 0.405$, $\text{OR} = e^{0.405} \approx 1.50$ (a 1-unit increase in detailing visits increases the odds of therapy adoption by $50\%$).

### 7.2 Maximum Likelihood Estimation (MLE)
Parameters $\boldsymbol{\beta}$ are estimated by maximizing the log-likelihood function (solved numerically via Newton-Raphson / IRLS):
$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^{n} \left[ y_i \ln(p_i) + (1 - y_i)\ln(1 - p_i) \right]$$

---

## 8. Python Code Implementation: Rigorous OLS & Diagnostics Pipeline

```python
"""
Module 04: Production Statistical Regression & Diagnostics Pipeline
Executable script demonstrating OLS estimation, VIF calculation,
Durbin-Watson test, and Breusch-Pagan heteroscedasticity check.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan

# 1. Generate Synthetic Pharmaceutical Commercial Dataset
np.random.seed(42)
n_weeks = 104  # 2 years of weekly brand data

detailing_spend = np.random.gamma(shape=5, scale=2000, size=n_weeks)
digital_spend = np.random.gamma(shape=3, scale=1500, size=n_weeks)
# Inject moderate collinearity between detailing and conferences
conference_spend = 0.4 * detailing_spend + np.random.normal(2000, 500, size=n_weeks)

# True data generating process with known coefficients
true_beta = [5000, 1.8, 0.9, 1.2]  # Intercept, Detail, Digital, Conf
noise = np.random.normal(0, 1200, size=n_weeks)

trx_sales = (true_beta[0] + 
             true_beta[1] * detailing_spend + 
             true_beta[2] * digital_spend + 
             true_beta[3] * conference_spend + noise)

df = pd.DataFrame({
    'TRx_Sales': trx_sales,
    'Detailing_Spend': detailing_spend,
    'Digital_Spend': digital_spend,
    'Conference_Spend': conference_spend
})

# 2. Fit OLS Model via Statsmodels
X = df[['Detailing_Spend', 'Digital_Spend', 'Conference_Spend']]
X_with_const = sm.add_constant(X)
y = df['TRx_Sales']

model = sm.OLS(y, X_with_const).fit()
print("="*60)
print("             OLS REGRESSION MODEL SUMMARY")
print("="*60)
print(model.summary().tables[1])
print(f"\nR-squared: {model.rsquared:.4f} | Adj. R-squared: {model.rsquared_adj:.4f}")
print(f"F-statistic: {model.fvalue:.2f} (p-value: {model.f_pvalue:.2e})")

# 3. Multicollinearity Audit: VIF Calculation
vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print("\n" + "="*60)
print("             VARIANCE INFLATION FACTOR (VIF)")
print("="*60)
print(vif_data.to_string(index=False))

# 4. Residual Diagnostics: Autocorrelation & Heteroscedasticity
dw_stat = durbin_watson(model.resid)
bp_stat, bp_pvalue, _, _ = het_breuschpagan(model.resid, model.model.exog)

print("\n" + "="*60)
print("             RESIDUAL DIAGNOSTICS")
print("="*60)
print(f"Durbin-Watson Statistic: {dw_stat:.4f} (Ideal ~ 2.0)")
print(f"Breusch-Pagan LM Stat:   {bp_stat:.4f} (p-value: {bp_pvalue:.4f})")
if bp_pvalue > 0.05:
    print("Interpretation: Fail to reject homoscedasticity (Errors are homoscedastic).")
else:
    print("Interpretation: Heteroscedasticity detected! Apply Huber-White robust SE.")
```


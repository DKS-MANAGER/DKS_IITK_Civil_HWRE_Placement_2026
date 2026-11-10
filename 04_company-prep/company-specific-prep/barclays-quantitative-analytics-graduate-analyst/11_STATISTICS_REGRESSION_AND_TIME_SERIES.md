# 11 — Statistics, Regression & Time-Series for Risk QA

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview

Quantitative Analytics in credit risk monitoring requires a rigorous foundation in classical probability theory, inferential statistics, generalized linear models (GLMs), and macro-econometric time-series analysis. Whether deriving the asymptotic distribution of a calibration test, fitting a logistic scorecard via Maximum Likelihood Estimation (MLE), or modeling portfolio default rates against GDP cycles, statistical rigor ensures that model monitoring flags genuine structural degradation rather than sample noise.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Risk QA Mathematical & Statistical Stack                        │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Probability & Distributions   │ Inferential Hypothesis Testing │ Econometric Modeling  │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Latent asset returns:       │ • Calibration tests:           │ • Credit scorecards:  │
│   Gaussian & Student-t        │   Binomial Z-test, Chi-Square  │   Logistic Regression │
│ • Default event counts:       │ • Distribution divergence:     │ • Satellite models:   │
│   Binomial & Poisson          │   Two-sample KS, Jeffrey's PSI │   ARIMA, VAR, ADL     │
│ • Loss Given Default (LGD):   │ • Hypothesis error control:    │ • Stationarity:       │
│   Beta distribution [0, 1]    │   Type I vs. Type II trade-off │   ADF test, KPSS      │
│ • Extreme loss tails:         │ • Multicollinearity:           │ • Regime shifts:      │
│   Gumbel & Generalized Pareto │   Variance Inflation Factor    │   Chow test, CUSUM    │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Probability Distributions in Credit Risk Modeling

#### 1.1 Bernoulli & Binomial Distribution
The credit status of a single borrower over a fixed 1-year window is a Bernoulli random variable $Y \sim \text{Bernoulli}(p)$, where $Y = 1$ (default) with probability $p$ and $Y = 0$ (non-default) with probability $1 - p$.

For a homogeneous cohort of $N$ independent borrowers with identical default probability $p$, the total number of defaults $K = \sum_{i=1}^N Y_i$ follows a Binomial distribution:

$$P(K = k) = \binom{N}{k} p^k (1 - p)^{N - k}, \quad k \in \{0, 1, \dots, N\}$$
$$\mathbb{E}[K] = Np, \quad \text{Var}(K) = Np(1 - p)$$

When $N$ is large ($N > 100$) and $Np > 10$, the Binomial distribution converges to a Gaussian distribution by the Central Limit Theorem:
$$K \xrightarrow{d} \mathcal{N}(Np, \; Np(1 - p))$$

#### 1.2 Poisson Distribution for Rare Default Events
For high-grade corporate portfolios (e.g., AAA/AA-rated exposures where $p \to 0$ and $N \to \infty$ such that $\lambda = Np$ remains constant), the default count follows a Poisson distribution:

$$P(K = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad \mathbb{E}[K] = \lambda, \quad \text{Var}(K) = \lambda$$

#### 1.3 Beta Distribution for Loss Given Default (LGD)
Because Loss Given Default represents a percentage loss bounded strictly between 0% and 100% ($LGD \in [0, 1]$), the standard normal distribution is mathematically invalid. Risk QA models empirical recovery rates using the **Beta distribution**:

$$f(x; \alpha, \beta) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}, \quad 0 \le x \le 1$$

where $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}$ is the Beta function.
$$\mathbb{E}[X] = \frac{\alpha}{\alpha + \beta}, \quad \text{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}$$

Given sample mean $\bar{x}$ and sample variance $s^2$, the shape parameters $\alpha$ and $\beta$ are estimated via Method of Moments:
$$\alpha = \bar{x} \left( \frac{\bar{x}(1 - \bar{x})}{s^2} - 1 \right), \quad \beta = (1 - \bar{x}) \left( \frac{\bar{x}(1 - \bar{x})}{s^2} - 1 \right)$$

#### 1.4 Extreme Value Theory (EVT) & Gumbel Distribution
In catastrophic stress testing and extreme tail loss modeling, standard Gaussian distributions severely underestimate tail thickness (the "fat-tail" problem). Under the Fisher-Tippett-Gnedenko theorem, the maximum of a sequence of independent and identically distributed random variables converges to the **Generalized Extreme Value (GEV)** distribution:

$$F(x; \mu, \sigma, \xi) = \exp\left( -\left[ 1 + \xi \left(\frac{x - \mu}{\sigma}\right) \right]^{-1/\xi} \right)$$

When the tail index $\xi = 0$, it simplifies to the **Type I (Gumbel) distribution**:
$$F(x; \mu, \sigma) = \exp\left( -\exp\left( -\frac{x - \mu}{\sigma} \right) \right)$$

> **Interview Bridge to Candidate's Background:**  
> In hydrological engineering, extreme value distributions (Gumbel, Log-Pearson Type III) model 100-year and 500-year flood peak discharges. In banking, the exact same mathematical formalism models regulatory 99.9% Value at Risk (1-in-1,000-year credit loss events) and tail default clustering.

---

### 2. Inferential Hypothesis Testing in Model Monitoring

In model monitoring, statistical tests evaluate whether deviations between predicted metrics and realized monitoring data are attributable to random sampling variation or structural model failure.

```
┌─────────────────────────────────┬─────────────────────────────────┐
│ Type I Error (Producer Risk, α) │ Type II Error (Consumer Risk, β)│
├─────────────────────────────────┼─────────────────────────────────┤
│ • Null Hypothesis H0:           │ • Null Hypothesis H0:           │
│   Model is functioning correctly│   Model is functioning correctly│
│ • Reality: Model is sound.      │ • Reality: Model is degraded.   │
│ • Decision: Test rejects H0     │ • Decision: Test fails to       │
│   (False Alarm).                │   reject H0 (Missed Detection). │
│ • Banking Consequence:          │ • Banking Consequence:          │
│   Costly, unnecessary model     │   Severe under-provisioning,    │
│   rebuild and diversion of quant│   hidden insolvency, regulatory │
│   resources.                    │   enforcement fines.            │
└─────────────────────────────────┴─────────────────────────────────┘
```

#### 2.1 The Two-Sided Binomial Calibration Test
Let $N$ be the number of active facilities in a given rating band with predicted default probability $PD_0$. Let $K$ be the observed number of defaults over 12 months.
- Null Hypothesis $H_0: p = PD_0$ (Model is accurately calibrated)
- Alternative Hypothesis $H_1: p \ne PD_0$ (Model is miscalibrated)

Using the standard normal approximation test statistic:
$$Z = \frac{K - N \cdot PD_0}{\sqrt{N \cdot PD_0 (1 - PD_0)}} \sim \mathcal{N}(0, 1)$$

Decision Rules at 5% significance level ($\alpha = 0.05$):
- If $|Z| < 1.96$: Fail to reject $H_0$ $\implies$ **GREEN (Calibrated)**.
- If $1.96 \le |Z| < 2.58$: Reject at 5% level $\implies$ **AMBER (Warning: slight drift)**.
- If $|Z| \ge 2.58$: Reject at 1% level $\implies$ **RED (Breach: significant miscalibration)**.

#### 2.2 Chi-Square ($\chi^2$) Goodness-of-Fit Test
Used to test whether an entire categorical frequency distribution matches theoretical expectations across $k$ bins:

$$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} \sim \chi^2_{k - 1 - p}$$

where $O_i$ is observed count, $E_i$ is expected count, and $p$ is the number of estimated parameters.

---

### 3. Logistic Regression & Generalized Linear Models (GLMs)

Logistic regression is the foundational workhorse for credit scoring models due to its monotonic interpretability, direct probabilistic output, and compliance transparency.

#### 3.1 Latent Variable Derivation
Assume an unobservable (latent) continuous variable $y_i^*$ representing the financial distress propensity of borrower $i$:

$$y_i^* = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} + \epsilon_i$$

where $\epsilon_i$ is an idiosyncratic error term following a **Standard Logistic distribution** with cumulative distribution function:
$$F(\epsilon) = \frac{1}{1 + e^{-\epsilon}}$$

A default event occurs ($y_i = 1$) if the borrower's distress exceeds a critical threshold (normalized to 0):
$$P(y_i = 1 \mid \mathbf{x}_i) = P(y_i^* > 0) = P(\mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i > 0) = P(\epsilon_i > -\mathbf{x}_i^T \boldsymbol{\beta})$$

By the symmetry of the logistic distribution ($P(\epsilon > -z) = F(z)$):
$$P(y_i = 1 \mid \mathbf{x}_i) = \frac{1}{1 + e^{-\mathbf{x}_i^T \boldsymbol{\beta}}} = \sigma(\mathbf{x}_i^T \boldsymbol{\beta})$$

#### 3.2 Maximum Likelihood Estimation (MLE)
Given a sample of $N$ independent observations $\{( \mathbf{x}_i, y_i )\}_{i=1}^N$, the likelihood function is:

$$L(\boldsymbol{\beta}) = \prod_{i=1}^{N} p_i^{y_i} (1 - p_i)^{1 - y_i}, \quad \text{where } p_i = \frac{1}{1 + e^{-\mathbf{x}_i^T \boldsymbol{\beta}}}$$

The log-likelihood function $\ell(\boldsymbol{\beta}) = \ln L(\boldsymbol{\beta})$ is:
$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^{N} \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]$$

Since $\ln\left(\frac{p_i}{1 - p_i}\right) = \mathbf{x}_i^T \boldsymbol{\beta}$ and $\ln(1 - p_i) = -\ln(1 + e^{\mathbf{x}_i^T \boldsymbol{\beta}})$:
$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^{N} \left[ y_i \mathbf{x}_i^T \boldsymbol{\beta} - \ln(1 + e^{\mathbf{x}_i^T \boldsymbol{\beta}}) \right]$$

To maximize $\ell(\boldsymbol{\beta})$, we compute the **Gradient vector (Score function)**:
$$\mathbf{g}(\boldsymbol{\beta}) = \nabla_{\boldsymbol{\beta}} \ell(\boldsymbol{\beta}) = \sum_{i=1}^{N} (y_i - p_i) \mathbf{x}_i = \mathbf{X}^T (\mathbf{y} - \mathbf{p})$$

Setting $\mathbf{g}(\boldsymbol{\beta}) = \mathbf{0}$ yields a system of non-linear equations with no closed-form analytical solution. It is solved numerically using the **Newton-Raphson algorithm** or **Iteratively Reweighted Least Squares (IRLS)**.

The **Hessian matrix** of second partial derivatives is:
$$\mathbf{H}(\boldsymbol{\beta}) = \nabla_{\boldsymbol{\beta}}^2 \ell(\boldsymbol{\beta}) = -\sum_{i=1}^{N} p_i (1 - p_i) \mathbf{x}_i \mathbf{x}_i^T = -\mathbf{X}^T \mathbf{W} \mathbf{X}$$

where $\mathbf{W} = \text{diag}(p_1(1 - p_1), \dots, p_N(1 - p_N))$ is a diagonal weighting matrix.
Because $p_i(1 - p_i) > 0$ for all $p_i \in (0, 1)$, $\mathbf{H}$ is strictly negative definite, guaranteeing that the log-likelihood is concave and has a unique global maximum.

The Newton-Raphson parameter update step is:
$$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} - \left[ \mathbf{H}(\boldsymbol{\beta}^{(t)}) \right]^{-1} \mathbf{g}(\boldsymbol{\beta}^{(t)}) = \boldsymbol{\beta}^{(t)} + (\mathbf{X}^T \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^T (\mathbf{y} - \mathbf{p}_t)$$

#### 3.3 Logit, Odds & Odds Ratios
The **odds of default** is defined as the ratio of default probability to non-default probability:

$$\text{Odds} = \frac{p}{1 - p} = e^{\beta_0 + \beta_1 x_1 + \dots + \beta_k x_k}$$
$$\text{Logit} = \ln(\text{Odds}) = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k$$

If feature $x_j$ increases by 1 unit while all other features remain constant:
$$\text{Odds}_{\text{new}} = e^{\beta_j} \times \text{Odds}_{\text{old}}$$
$$\text{Odds Ratio (OR)}_j = \frac{\text{Odds}(x_j + 1)}{\text{Odds}(x_j)} = e^{\beta_j}$$
- If $\beta_j > 0 \implies \text{OR}_j > 1$: Higher values increase default odds.
- If $\beta_j < 0 \implies \text{OR}_j < 1$: Higher values decrease default odds.

#### 3.4 Multicollinearity & Variance Inflation Factor (VIF)
When independent variables are highly correlated with each other, parameter estimates become unstable with inflated standard errors:

$$\text{VIF}_j = \frac{1}{1 - R_j^2}$$

where $R_j^2$ is the coefficient of determination obtained from regressing feature $x_j$ against all remaining explanatory features.
- $\text{VIF} < 3$: Low collinearity (safe).
- $3 \le \text{VIF} \le 5$: Moderate collinearity (monitor coefficients).
- $\text{VIF} > 5$: Severe multicollinearity; drop or combine features to prevent scorecard instability.

---

### 4. Time-Series Analysis & Macroeconomic Satellite Modeling

Credit risk default rates exhibit persistent cyclicality driven by macroeconomic business cycles. Risk QA builds **Satellite Models** to forecast portfolio default rates under stress testing scenarios.

#### 4.1 Weak Stationarity (Covariance Stationarity)
A time series $\{Y_t\}$ is covariance stationary if:
1. Constant Mean: $\mathbb{E}[Y_t] = \mu$ for all $t$.
2. Constant Finite Variance: $\text{Var}(Y_t) = \sigma^2 < \infty$ for all $t$.
3. Lag-dependent Autocovariance: $\text{Cov}(Y_t, Y_{t-k}) = \gamma_k$, depending only on lag length $k$, not on absolute time $t$.

#### 4.2 Unit Root Testing: Augmented Dickey-Fuller (ADF)
Most macroeconomic variables (e.g., GDP levels, House Price Indices) are non-stationary $I(1)$ series that must be differenced:

$$\Delta Y_t = \alpha + \beta t + \gamma Y_{t-1} + \sum_{p=1}^{P} \delta_p \Delta Y_{t-p} + \epsilon_t$$

- $H_0: \gamma = 0$ (Unit root present; series is non-stationary).
- $H_1: \gamma < 0$ (Series is stationary).

If the test fails to reject $H_0$, the variable must be transformed into percentage changes or first differences: $\Delta Y_t = Y_t - Y_{t-1}$.

#### 4.3 Autoregressive Distributed Lag (ADL) Satellite Models
A standard credit portfolio satellite model relates the quarterly logit-transformed default rate $DR_t$ to macroeconomic variables:

$$\text{logit}(DR_t) = c + \sum_{i=1}^{p} \phi_i \text{logit}(DR_{t-i}) + \sum_{j=0}^{q} \boldsymbol{\beta}_j^T \mathbf{X}_{t-j} + \epsilon_t$$

where $\mathbf{X}_t = [\Delta \text{GDP}_t, \; \text{Unemployment}_t, \; \Delta \text{HPI}_t, \; \text{BaseRate}_t]^T$.

#### 4.4 Structural Breaks & Chow Test
During macroeconomic shocks (e.g., the 2008 Financial Crisis or COVID-19 pandemic), historical regression relationships can experience structural breaks. The **Chow Test** partitions the sample into two sub-periods ($N_1$ and $N_2$) at break-point $T_B$:

$$F = \frac{\frac{\text{RSS}_P - (\text{RSS}_1 + \text{RSS}_2)}{k}}{\frac{\text{RSS}_1 + \text{RSS}_2}{N_1 + N_2 - 2k}} \sim F(k, \; N_1 + N_2 - 2k)$$

where $\text{RSS}_P$ is the pooled residual sum of squares, and $k$ is the number of parameters. If $F > F_{\text{critical}}$, the model parameters have shifted structurally, indicating that historical satellite elasticities cannot be applied without recalibration.

---

### 5. Numerical Worked Examples

---

#### Worked Example 1: Logistic Scorecard Log-Odds, Odds Ratio & Probability
A retail credit card default model produces the following estimated parameters:
- Intercept: $\beta_0 = -3.50$
- Feature 1 ($x_1$, Debt-to-Income ratio as decimal): $\beta_1 = +2.40$
- Feature 2 ($x_2$, Delinquency in last 12 months, binary flag): $\beta_2 = +1.10$
- Feature 3 ($x_3$, Normalized Bureau Score $[0, 1]$): $\beta_3 = -2.80$

Evaluate the credit risk for Borrower A and Borrower B:
- **Borrower A:** $\text{DTI} = 0.25$, Delinquency $= 0$, Bureau $= 0.80$
- **Borrower B:** $\text{DTI} = 0.50$, Delinquency $= 1$, Bureau $= 0.30$

##### Calculation for Borrower A:
$$\text{Logit}_A = -3.50 + 2.40(0.25) + 1.10(0) - 2.80(0.80) = -3.50 + 0.60 + 0 - 2.24 = \mathbf{-5.14}$$
$$\text{Odds}_A = e^{-5.14} \approx \mathbf{0.005858}$$
$$\text{PD}_A = \frac{1}{1 + e^{-(-5.14)}} = \frac{1}{1 + e^{5.14}} = \frac{1}{1 + 170.71} = \mathbf{0.00582} \quad (0.582\%)$$

##### Calculation for Borrower B:
$$\text{Logit}_B = -3.50 + 2.40(0.50) + 1.10(1) - 2.80(0.30) = -3.50 + 1.20 + 1.10 - 0.84 = \mathbf{-2.04}$$
$$\text{Odds}_B = e^{-2.04} \approx \mathbf{0.1300}$$
$$\text{PD}_B = \frac{1}{1 + e^{-(-2.04)}} = \frac{1}{1 + e^{2.04}} = \frac{1}{1 + 7.6906} = \mathbf{0.11506} \quad (11.51\%)$$

##### Marginal Effect of Delinquency Flag:
$$\text{Odds Ratio for Delinquency} = e^{\beta_2} = e^{1.10} \approx \mathbf{3.004}$$
Having a past delinquency multiplies a borrower's default odds by **3.00x** (a 200% increase in odds), holding all other variables constant.

---

#### Worked Example 2: Binomial Calibration Z-Test for Rating Band 3
In a quarterly monitoring cycle, Barclays QA audits internal Rating Band 3:
- Number of active accounts: $N = 4,000$
- Benchmark expected default probability: $PD_0 = 1.20\% = 0.012$
- Realized defaults over trailing 12 months: $K = 64$

##### Step 1: Compute Expected Defaults and Standard Error
$$\mathbb{E}[K] = N \cdot PD_0 = 4,000 \times 0.012 = 48.0 \text{ defaults}$$
$$\text{SE} = \sqrt{N \cdot PD_0 (1 - PD_0)} = \sqrt{4,000 \times 0.012 \times (1 - 0.012)} = \sqrt{4,000 \times 0.012 \times 0.988} = \sqrt{47.424} \approx \mathbf{6.8865}$$

##### Step 2: Compute Test Statistic $Z$
$$Z = \frac{K - \mathbb{E}[K]}{\text{SE}} = \frac{64 - 48.0}{6.8865} = \frac{+16.0}{6.8865} = \mathbf{+2.323}$$

##### Step 3: Governance Triaging
- Standard two-tailed 95% critical value: $Z_{0.025} = 1.96$.
- Standard two-tailed 99% critical value: $Z_{0.005} = 2.58$.
- Since $1.96 \le Z = 2.323 < 2.58$, the two-tailed $p$-value is:
  $$p = 2 \times (1 - \Phi(2.323)) = 2 \times (1 - 0.9899) = \mathbf{0.0202} \quad (2.02\%)$$
- **Governance Result:** **AMBER TRIGGER**.  
  Observed defaults (64) significantly exceed model expectations (48) at the 5% level, but do not exceed the 1% emergency breach threshold.
- **Analyst Action:** Flag Rating Band 3 in the quarterly MMP, launch a feature-level CSI investigation to identify the origin of the underestimation, and evaluate the necessity of a conservative Post-Model Adjustment (PMA).

---

*Authoritative cross-reference: Greene, W. H. (2018), "Econometric Analysis", 8th Edition; Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013), "Applied Logistic Regression", 3rd Edition; BCBS Studies on the Validation of Internal Rating Systems (Working Paper 14).*


# 06. Risk Analyst: Comprehensive 65+ Question Bank

> High-yield interview questions across Probability & Statistics, Credit Risk, Market Risk, Quantitative Modeling, SQL, and Behavioral Fit.

---

## 📑 Question Bank Index
- **Section 1**: Probability, Statistics & Mathematics (Q1 - Q15)
- **Section 2**: Credit Risk Modeling & Scorecards (Q16 - Q30)
- **Section 3**: Market Risk, VaR & Portfolio Math (Q31 - Q42)
- **Section 4**: SQL & Risk Portfolio Querying (Q43 - Q52)
- **Section 5**: Risk Business Cases & Trade-offs (Q53 - Q60)
- **Section 6**: Behavioral & Civil-to-Risk Fit (Q61 - Q65)

---

## Section 1: Probability, Statistics & Mathematics

### Q1 [P0][PROBABILITY]: A disease has 0.1% prevalence in a population. A test has 99% sensitivity and 98% specificity. If a patient tests positive, what is the probability they actually have the disease?
- **Solution (Bayes' Rule)**:
  $$P(D) = 0.001, \quad P(T^+ \mid D) = 0.99, \quad P(T^+ \mid D^c) = 1 - 0.98 = 0.02$$
  $$P(T^+) = (0.001 	imes 0.99) + (0.999 	imes 0.02) = 0.00099 + 0.01998 = 0.02097$$
  $$P(D \mid T^+) = rac{0.00099}{0.02097} pprox \mathbf{4.72\%}$$
  *(Even with a 99% accurate test, a positive result only indicates a 4.72% chance of disease due to low baseline prevalence).*

### Q2 [P0][STATS]: What is the difference between Probability of Default ($PD$) and Hazard Rate?
- $PD$ is the cumulative probability of default over a fixed discrete time horizon (e.g. 1 year).
- Hazard Rate ($\lambda(t)$) is the instantaneous conditional default rate at time $t$, given survival up to time $t$: $PD(t) = 1 - e^{-\int_0^t \lambda(u)du}$.

### Q3 [P0][PROBABILITY]: If X and Y are independent standard normal variables $\mathcal{N}(0,1)$, what is the distribution of $Z = 2X - 3Y$?
- $E[Z] = 2(0) - 3(0) = 0$.
- $	ext{Var}(Z) = 2^2 	ext{Var}(X) + (-3)^2 	ext{Var}(Y) = 4(1) + 9(1) = 13$.
- $Z \sim \mathcal{N}(0, 13)$.

### Q4 [P1][PROBABILITY]: In a credit card fraud detection system, fraud events arrive according to a Poisson process with $\lambda = 4$ per hour. What is the probability of observing exactly 2 fraud events in a 30-minute window?
- For 30 mins ($0.5	ext{ hr}$), $\mu = \lambda 	imes t = 4 	imes 0.5 = 2$.
- $P(X = 2) = rac{e^{-2} \cdot 2^2}{2!} = rac{4 e^{-2}}{2} = 2 e^{-2} pprox 2 	imes 0.1353 = \mathbf{27.06\%}$.

### Q5 [P0][STATS]: Explain Central Limit Theorem and its limitation in financial risk modeling.
- CLT states that sample means of independent and identically distributed variables converge to a normal distribution. Limitation: Financial asset returns have fat tails, excess kurtosis, and volatility clustering (non-i.i.d.), making normal CLT assumptions dangerously underestimate tail losses.

### Q6 [P1][STATS]: What is the difference between parametric and non-parametric hypothesis tests?
- Parametric tests (t-test, ANOVA) assume an underlying theoretical distribution (e.g. normality) and evaluate distribution parameters ($\mu, \sigma^2$).
- Non-parametric tests (Mann-Whitney U, Kolmogorov-Smirnov, Wilcoxon) make no distribution assumptions and evaluate ranks or empirical CDFs.

### Q7 [P0][PROBABILITY]: You roll two fair 6-sided dice. What is the probability that the sum is $\ge 9$ given that the first die shows an odd number?
- Possible outcomes with odd first die ($1, 3, 5$): $3 	imes 6 = 18$ outcomes.
- Outcomes with sum $\ge 9$:
  - First die = 3: $(3,6) \implies 1$ outcome.
  - First die = 5: $(5,4), (5,5), (5,6) \implies 3$ outcomes.
- Total favorable = $1 + 3 = 4$. $P = rac{4}{18} = \mathbf{rac{2}{9} pprox 22.22\%}$.

### Q8 [P1][STATS]: Explain Copulas and why Gaussian copulas failed during the 2008 Global Financial Crisis.
- A Copula couples individual marginal distributions into a joint multivariate distribution. The Gaussian copula assumed zero tail dependence between mortgage defaults, severely underestimating the probability of simultaneous nationwide housing defaults.

### Q9 [P0][STATS]: Differentiate between Type I error, Type II error, and Power of a test.
- Type I ($lpha$): Rejecting null hypothesis when it is true (False Positive).
- Type II ($eta$): Failing to reject null hypothesis when it is false (False Negative).
- Power ($1 - eta$): Probability of correctly detecting a true effect.

### Q10 [P1][PROBABILITY]: What is the memoryless property of the Exponential distribution?
- $P(X > s + t \mid X > s) = P(X > t)$. The remaining time until an event occurs does not depend on how much time has already elapsed.

### Q11 [P2][STATS]: Explain Extreme Value Theory (EVT) and the Generalized Extreme Value (GEV) distribution.
- EVT models the distribution of sample maxima/minima (Block Maxima) or threshold exceedances (Peaks Over Threshold - POT using Generalized Pareto Distribution), vital for estimating 1-in-100 year financial crashes and hydrological flood events.

### Q12 [P0][PROBABILITY]: What is the expected number of coin flips to get two consecutive Heads ($HH$)?
- Let $E$ be expected flips: $E = 6$ flips. (Equation: $E = rac{1}{2}(1 + E_{H}) + rac{1}{2}(1 + E)$, where $E_H = rac{1}{2}(1) + rac{1}{2}(1 + E) \implies E = 6$).

### Q13 [P1][STATS]: Why is Maximum Likelihood Estimation (MLE) preferred over Ordinary Least Squares (OLS) for binary classification?
- Binary outcomes have non-normal, heteroscedastic Bernoulli error distributions bounded $[0,1]$, violating Gauss-Markov OLS assumptions. MLE maximizes the log-likelihood of Bernoulli probabilities.

### Q14 [P0][STATS]: Explain the bias-variance tradeoff in predictive risk models.
- High bias $\implies$ Underfitting (model too simple, misses risk patterns). High variance $\implies$ Overfitting (model memorizes noise, fails out-of-time validation). Controlled via regularization ($L_1/L_2$), pruning, and cross-validation.

### Q15 [P1][PROBABILITY]: If correlation $ho(X, Y) = 0$, does it mean X and Y are independent?
- No. Zero correlation only implies absence of a *linear* relationship. Non-linear dependencies (e.g. $Y = X^2$ where $X \sim \mathcal{N}(0,1)$) have $ho=0$ but are completely dependent.

---

## Section 2: Credit Risk Modeling & Scorecards

### Q16 [P0][CREDIT]: Define PD, LGD, EAD, and calculate Expected Loss for a 10 Cr INR credit facility with 2% PD, 45% LGD, and 8 Cr drawn + 2 Cr undrawn (Credit Conversion Factor = 50%).
- $PD = 0.02, \quad LGD = 0.45$.
- $EAD = 	ext{Drawn} + (	ext{CCF} 	imes 	ext{Undrawn}) = 8 + (0.50 	imes 2) = 9	ext{ Cr INR}$.
- $EL = 0.02 	imes 0.45 	imes 9	ext{ Cr} = \mathbf{0.081	ext{ Cr INR} = 8.1	ext{ Lakh INR}}$.

### Q17 [P0][CREDIT]: Why is Logistic Regression preferred over XGBoost for regulatory credit scoring scorecards?
- Interpretability, strict regulatory compliance (Basel / FCRA adverse action notices requiring explainable score deductions), monotonic risk relationships enforced via WoE binning, and robust stability over economic cycles.

### Q18 [P0][CREDIT]: How do you calculate Weight of Evidence (WoE) and Information Value (IV)?
- $WoE_i = \ln \left(rac{G_i / G_{	ext{total}}}{B_i / B_{	ext{total}}}ight)$.
- $IV = \sum (Dist\_Good_i - Dist\_Bad_i) 	imes WoE_i$.

### Q19 [P1][CREDIT]: What is the Kolmogorov-Smirnov (KS) statistic and how is it used in credit scorecards?
- Maximum vertical divergence between the cumulative distribution of good loans and bad loans. It indicates the scorecard's ability to separate defaulters from non-defaulters. Typical industry cutoff is $KS \ge 40$.

### Q20 [P1][CREDIT]: Explain Population Stability Index (PSI) and the action thresholds.
- Quantifies distribution shift between baseline development data and current production portfolio. Thresholds: $PSI < 0.10$ (Stable), $0.10 \le PSI < 0.25$ (Moderate drift), $PSI \ge 0.25$ (Significant drift $ightarrow$ recalibrate model).

### Q21 [P0][CREDIT]: What is Through-the-Cycle (TTC) vs Point-in-Time (PIT) PD?
- **PIT PD**: Estimates probability of default over the next 12 months given current macroeconomic conditions (used for IFRS 9 / CECL loss accounting).
- **TTC PD**: Estimates long-run average default rate across an entire economic cycle (used for Basel regulatory capital calculation).

### Q22 [P1][CREDIT]: What is Reject Inference in credit scoring?
- Technique used to infer the repayment behavior of applicants who were rejected by historical underwriting rules, preventing selection bias when training new scorecard models.

### Q23 [P0][CREDIT]: Differentiate between Gini coefficient and ROC-AUC.
- $	ext{Gini} = 2 	imes AUC - 1$. While ROC-AUC measures area under the true positive vs false positive curve (ranging $0.5$ to $1.0$), Gini rescales this to range between $0$ and $1.0$.

### Q24 [P1][CREDIT]: What are Roll Rates and how are they used in credit risk?
- The percentage of delinquent balances or accounts that transition ("roll") from one delinquency bucket (e.g. 30 DPD) to the next severe bucket (e.g. 60 DPD) within a monthly billing cycle.

### Q25 [P1][CREDIT]: What is a Vintage Analysis in retail credit portfolios?
- Tracking loss and delinquency curves of loan cohorts originated in the same month/quarter over their seasoned lifecycle (e.g. 6, 12, 24 months on book).

### Q26 [P2][CREDIT]: Explain IFRS 9 / CECL 3-Stage Expected Credit Loss (ECL) classification.
- **Stage 1**: Performing loans with no significant increase in credit risk (SICR) $ightarrow$ 12-month ECL provisioned.
- **Stage 2**: Underperforming loans with significant credit risk deterioration $ightarrow$ Lifetime ECL provisioned.
- **Stage 3**: Credit-impaired / defaulted loans $ightarrow$ Lifetime ECL provisioned with interest recognized on net carrying amount.

### Q27 [P1][CREDIT]: How does fine binning differ from coarse binning in scorecard development?
- Fine binning splits continuous variables into 10-20 granular bins (quantiles/equal-width). Coarse binning merges adjacent fine bins to ensure monotonic WoE trends and minimum sample size ($\ge 5\%$ per bin).

### Q28 [P0][CREDIT]: What is the Credit Conversion Factor (CCF)?
- Factor used to convert off-balance-sheet contingent liabilities and undrawn credit lines (credit card limits, letters of credit) into on-balance-sheet Exposure at Default.

### Q29 [P1][CREDIT]: Why can a high Gini coefficient model still perform poorly in production?
- If the model is poorly calibrated (predicts relative risk ranking well but underestimates absolute default probabilities), or if population drift ($PSI > 0.25$) occurs due to changing applicant demographics.

### Q30 [P2][CREDIT]: How do macroeconomic variables (GDP, Interest rates) enter stress-testing credit models?
- Via Satellite Models: Linking historical log-odds of default ($\ln rac{PD}{1-PD}$) to macroeconomic indicators using autoregressive distributed lag (ARDL) or linear regression models.

---

## Section 3: Market Risk, VaR & Portfolio Math

### Q31 [P0][MARKET]: A portfolio has daily volatility $\sigma = 1.5\%$ and value $V = 50	ext{ Cr INR}$. Calculate the 1-day 99% Parametric VaR.
- $Z_{99\%} = 2.326$.
- $	ext{VaR}_{1	ext{d}, 99\%} = 2.326 	imes 0.015 	imes 50	ext{ Cr} = \mathbf{1.7445	ext{ Cr INR}}$.

### Q32 [P0][MARKET]: Convert the 1-day VaR of 1.74 Cr INR into a 10-day Basel regulatory VaR.
- $	ext{VaR}_{10	ext{d}} = 	ext{VaR}_{1	ext{d}} 	imes \sqrt{10} = 1.7445 	imes 3.1623 = \mathbf{5.516	ext{ Cr INR}}$.

### Q33 [P0][MARKET]: What are the 3 major methods for calculating Value at Risk (VaR), and their trade-offs?
1. *Parametric (Variance-Covariance)*: Fast, simple; assumes normal returns (underestimates tail risk).
2. *Historical Simulation*: Non-parametric, captures fat tails; completely constrained by historical lookback sample.
3. *Monte Carlo Simulation*: Flexible, models non-linear derivatives; computationally intensive and model-parameter dependent.

### Q34 [P1][MARKET]: Why is Expected Shortfall ($ES$) preferred over Value at Risk ($VaR$)?
- VaR is not sub-additive ($	ext{VaR}(A+B) > 	ext{VaR}(A) + 	ext{VaR}(B)$ can occur), meaning it does not consistently reward portfolio diversification. Expected Shortfall is a coherent risk measure that quantifies the average loss severity in the tail.

### Q35 [P0][MARKET]: What is the formula for the variance of a 2-asset portfolio?
$$\sigma_p^2 = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 ho \sigma_1 \sigma_2$$

### Q36 [P1][MARKET]: How does Kupiec's POF (Proportion of Overlapping Failures) test evaluate VaR model backtesting?
- It performs a likelihood-ratio test comparing observed VaR exceedances ($x$) over $N$ days against expected exceedances ($p 	imes N$, e.g. $1\% 	imes 250 = 2.5$). If exceedances fall into the Basel "Red Zone" ($\ge 10$ exceedances), the model is rejected.

### Q37 [P1][MARKET]: Define Option Greeks: Delta, Gamma, Vega, Theta.
- **Delta ($\Delta$)**: First derivative of option price w.r.t. underlying asset price ($rac{\partial V}{\partial S}$).
- **Gamma ($\Gamma$)**: Second derivative w.r.t. underlying asset price ($rac{\partial^2 V}{\partial S^2}$).
- **Vega ($
u$)**: Sensitivity w.r.t. implied volatility ($rac{\partial V}{\partial \sigma}$).
- **Theta ($\Theta$)**: Time decay of option value per day ($rac{\partial V}{\partial t}$).

### Q38 [P0][MARKET]: What is Duration and DV01 of a fixed-income bond?
- **Macaulay Duration**: Weighted average time until cash flows are received.
- **Modified Duration**: Percentage change in bond price per 100 bps change in yield ($rac{	ext{MacDur}}{1 + y/k}$).
- **DV01 (Dollar Value of an 01)**: Absolute dollar price change for a 1 basis point ($0.01\%$) shift in yield.

### Q39 [P1][MARKET]: What happens to portfolio diversification when correlation $ho$ jumps from $0.2$ to $0.9$ during a financial crisis?
- The diversification benefit collapses; portfolio variance surges toward the weighted average of individual asset variances, creating liquidity crunches and margin calls.

### Q40 [P2][MARKET]: Explain Marginal VaR vs Incremental VaR vs Component VaR.
- **Marginal VaR**: Partial derivative of portfolio VaR w.r.t. the weight of asset $i$.
- **Incremental VaR**: Exact change in portfolio VaR from adding or removing an entire position.
- **Component VaR**: Decomposition of portfolio VaR attributable to asset $i$ such that $\sum 	ext{Component VaR}_i = 	ext{Portfolio VaR}$.

### Q41 [P1][MARKET]: What is Volatility Clustering and how does GARCH(1,1) model it?
- Periods of high volatility are followed by high volatility, and tranquil periods by tranquility. GARCH(1,1) models variance as: $\sigma_t^2 = \omega + lpha \epsilon_{t-1}^2 + eta \sigma_{t-1}^2$.

### Q42 [P0][MARKET]: If an asset has an annualized volatility of 32%, what is its daily volatility assuming 256 trading days?
- $\sigma_{	ext{daily}} = rac{\sigma_{	ext{annual}}}{\sqrt{256}} = rac{32\%}{16} = \mathbf{2.0\% 	ext{ per day}}$.

---

## Section 4: SQL & Risk Portfolio Querying

### Q43 [P0][SQL]: Write a query to calculate the overall default rate (defined as $	ext{DPD} \ge 90$) grouped by credit score decile.
```sql
SELECT 
    NTILE(10) OVER (ORDER BY credit_score DESC) AS score_decile,
    MIN(credit_score) AS min_score,
    MAX(credit_score) AS max_score,
    COUNT(*) AS total_accounts,
    SUM(CASE WHEN days_past_due >= 90 THEN 1 ELSE 0 END) AS default_count,
    ROUND(100.0 * SUM(CASE WHEN days_past_due >= 90 THEN 1 ELSE 0 END) / COUNT(*), 2) AS bad_rate_pct
FROM CustomerLoans
GROUP BY 1
ORDER BY score_decile;
```

### Q44 [P0][SQL]: Query to identify accounts that transitioned from "Current" to "30 DPD" for the first time in January 2026.
```sql
WITH RankedStatus AS (
    SELECT 
        customer_id,
        statement_date,
        days_past_due,
        LAG(days_past_due, 1) OVER (PARTITION BY customer_id ORDER BY statement_date) as prev_dpd
    FROM LoanStatements
)
SELECT DISTINCT customer_id
FROM RankedStatus
WHERE statement_date >= '2026-01-01' AND statement_date < '2026-02-01'
  AND days_past_due BETWEEN 1 AND 30
  AND (prev_dpd = 0 OR prev_dpd IS NULL);
```

### Q45 [P1][SQL]: Calculate total portfolio Exposure at Default (EAD) assuming CCF = 0.50 on undrawn limits.
```sql
SELECT 
    product_type,
    COUNT(account_id) AS total_accounts,
    SUM(drawn_balance) AS total_drawn,
    SUM(credit_limit - drawn_balance) AS total_undrawn,
    SUM(drawn_balance + 0.50 * (credit_limit - drawn_balance)) AS total_ead
FROM CreditCards
GROUP BY product_type;
```

### Q46 [P1][SQL]: Calculate 30-day cumulative roll rate from 30 DPD to 60 DPD across origination cohorts.
```sql
WITH Cohorts AS (
    SELECT 
        account_id,
        DATE_TRUNC('quarter', origination_date) as orig_quarter
    FROM LoanAccounts
),
MonthlyDPD AS (
    SELECT 
        c.orig_quarter,
        s.statement_date,
        COUNT(CASE WHEN s.dpd BETWEEN 1 AND 30 THEN 1 END) as count_30dpd,
        COUNT(CASE WHEN s.dpd BETWEEN 31 AND 60 THEN 1 END) as count_60dpd
    FROM Cohorts c
    JOIN LoanStatements s ON c.account_id = s.account_id
    GROUP BY 1, 2
)
SELECT 
    orig_quarter,
    statement_date,
    count_30dpd,
    count_60dpd,
    ROUND(100.0 * count_60dpd / NULLIF(count_30dpd, 0), 2) as roll_rate_pct
FROM MonthlyDPD;
```

---

## Section 5: Risk Business Cases & Trade-offs

### Q53 [P0][CASE]: "Our credit card approval rate was increased by 8%, resulting in 25 Cr INR incremental interest income, but 90-day defaults rose by 14 Cr INR and collection costs rose by 4 Cr INR. Was this policy change value-accretive?"
- **Analysis**:
  - Incremental Gross Revenue = $+25	ext{ Cr INR}$.
  - Incremental Credit Losses = $-14	ext{ Cr INR}$.
  - Incremental Operating / Collection Costs = $-4	ext{ Cr INR}$.
  - Net Profit Contribution = $25 - 14 - 4 = +\mathbf{7	ext{ Cr INR}}$.
  - *Follow-up*: Check Capital Charge: If incremental RWA requires 5 Cr INR additional regulatory capital at a 15% cost of equity ($5 	imes 0.15 = 0.75	ext{ Cr}$), net economic profit is $+6.25	ext{ Cr INR}$. The expansion was value-accretive.

### Q54 [P1][CASE]: "A peer-to-peer lending startup has 12% default rates. They want to cut defaults in half by eliminating the bottom 3 score deciles. What is the risk?"
- **Analysis**: Severe adverse selection and volume collapse. Cutting 30% of applicants reduces revenue by ~30%, but defaults may not fall by 50% if the model has low discrimination ($KS < 25$). Furthermore, fixed customer acquisition costs (CAC) spent on rejected applicants are unrecoverable.

---

## Section 6: Behavioral & Civil-to-Risk Fit

### Q61 [P0][FIT]: "Why are you interested in Quantitative Risk Management coming from a Civil / Water Resources Engineering background?"
- (See verbatim high-conviction answer in [05_interview-preparation.md](05_interview-preparation.md)).

### Q62 [P0][FIT]: "Tell me about a time your mathematical model predicted an outcome that contradicted conventional team opinion."
- Use STAR framework. Detail how data-driven sensitivity analysis or extreme value modeling revealed a vulnerability others overlooked, and how you presented the evidence to build consensus.

### Q63 [P1][FIT]: "How do you handle the ethical trade-off between strict risk controls (rejecting marginal borrowers) and financial inclusion?"
- Explain how alternative data sources (utility payments, cash flow telemetry) and graduated credit lines with risk-based pricing enable expanding credit access safely without reckless balance sheet exposure.

### Q64 [P0][FIT]: "Describe a high-pressure situation where a calculation error could have caused severe project consequences."
- Detail rigorous verification protocols, unit tests, and cross-checks developed during numerical engineering research at IIT Kanpur.

### Q65 [P0][FIT]: "Do you have any questions for our Quantitative Risk team?"
- Ask about how the firm is integrating machine learning scorecards alongside traditional Basel regulatory models, or how real-time alternative data is transforming intraday risk monitoring.

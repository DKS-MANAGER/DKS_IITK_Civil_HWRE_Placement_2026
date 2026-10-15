# 11. Risk Analytics: Suggested Portfolio Projects & Resume Guidance

> Practical, reproducible quantitative project briefs across Credit Risk, Market Risk, and Extreme Value Modeling, with guidance for engineering candidates targeting risk analytics roles.
> 
> *Notice: The projects below are suggested project briefs designed for self-directed study and portfolio demonstration ([PREPARATION HEURISTIC]). Candidates should execute these models using public or synthetic datasets and report actual reproducible findings rather than claiming unverified metrics.*

---

## 1. Quantitative Risk Portfolio Architecture

Financial risk recruiters at institutions such as Citi, American Express, Barclays, and J.P. Morgan evaluate candidates on statistical discipline, model validation rigor, and regulatory awareness:

```
┌─────────────────────────────────────────────────────────────┐
│ Project 1: Credit Scorecard & Default Prediction Engine     │
│ • Domain: Retail Lending / Credit Risk Analytics            │
│ • Tooling: Python (`optbinning`, `statsmodels`, `scikit-learn`)│
│ • Core Output: Application scorecard, KS statistic, PSI map│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌─────────────────────────────▼──────────────────────────────┐
│ Project 2: Multi-Asset VaR Engine & Regulatory Backtesting  │
│ • Domain: Market Risk / Trading Book Capital (FRTB)         │
│ • Tooling: Python (`numpy`, `scipy.stats`, `pandas`)        │
│ • Core Output: Parametric vs Historical VaR, Kupiec POF test│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌─────────────────────────────▼──────────────────────────────┐
│ Project 3: Extreme Value Theory (EVT) Tail Loss Model       │
│ • Domain: Operational Risk / Heavy-Tailed Loss Distributions│
│ • Tooling: Python (`scipy.stats.genpareto`)                 │
│ • Core Output: Peaks-over-Threshold (POT) VaR & ES estimate │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Suggested Project Blueprints

### Project 1: Credit Scorecard & Default Prediction Engine
- **Core Research Question**: How does coarse-classing continuous borrower attributes via Weight of Evidence (WoE) and logistic regression compare against non-linear gradient boosted trees in terms of regulatory interpretability and calibration stability?
- **Dataset**: Publicly available benchmark dataset (e.g., Kaggle Home Credit Default Risk or UCI German Credit Dataset).
- **Methodology**:
  1. Bin continuous features (income, debt-to-income, credit bureau inquiries) into monotonic bins using the `optbinning` Python library.
  2. Compute Weight of Evidence ($WoE$) and Information Value ($IV$) for each candidate variable; eliminate features with $IV < 0.02$ or suspected data leakage ($IV > 0.50$).
  3. Fit a penalized Logistic Regression model on $WoE$-transformed variables.
  4. Scale raw log-odds into standard credit bureau scorecard points (e.g., Base Points = 600 at 50:1 Odds, with Points to Double the Odds $\text{PDO} = 20$).
  5. Validate discrimination using Kolmogorov-Smirnov ($KS \ge 35\%$) and ROC-AUC ($AUC \ge 0.75$).
  6. Simulate a 6-month out-of-time population shift and calculate Population Stability Index ($PSI$).
- **Validation**:
  - Test calibration using the Hosmer-Lemeshow test and Brier score.
- **Outputs**:
  - Readable credit scorecard lookup table mapping attribute ranges to points.
  - Decile validation table showing monotonic bad rates across score bands.
- **Limitations**:
  - Scorecard relies on observed historical repayment behavior and requires reject inference adjustments if unbooked applicants are omitted.

---

### Project 2: Multi-Asset VaR Engine & Regulatory Backtesting
- **Core Research Question**: How accurately does a 1-day 99% Parametric Value at Risk (VaR) model capture tail losses compared to Historical Simulation and Monte Carlo during periods of market volatility?
- **Dataset**: Public historical daily closing prices for an equity and fixed income portfolio over a 5-year window via `yfinance` or NSE India public archives ([PRACTICE ASSUMPTION]).
- **Methodology**:
  1. Calculate daily log-returns and portfolio variance-covariance matrix.
  2. Model time-varying volatility using Exponentially Weighted Moving Average (EWMA, $\lambda = 0.94$ RiskMetrics standard).
  3. Compute 1-day 99% Parametric VaR ($Z = 2.326 \times \sigma_p \times V$) and Historical VaR (1st percentile of empirical return distribution).
  4. Scale to 10-day horizon using the Basel $\sqrt{10}$ square-root-of-time rule.
  5. Backtest over a 250-trading-day out-of-sample testing window; count the number of exceptions (trading days where actual portfolio loss exceeded predicted VaR).
  6. Execute the **Kupiec Proportion of Failures (POF)** likelihood-ratio test:
     $$LR_{\text{POF}} = -2 \ln \left[ \frac{(1 - p)^{N - x} p^x}{(1 - \hat{p})^{N - x} \hat{p}^x} \right] \sim \chi^2(1)$$
- **Validation**:
  - Confirm the model falls in the Basel Green Zone ($\le 4$ exceptions out of 250 days at 99% confidence).
- **Outputs**:
  - Time-series plot overlaying daily portfolio P&L against the dynamic 99% VaR boundary.
  - Summary table of Kupiec test p-values and Expected Shortfall calculations.
- **Limitations**:
  - Parametric normal VaR underestimates tail losses when returns exhibit heavy kurtosis or jump risk.

---

### Project 3: Extreme Value Theory (EVT) Tail Loss Model
- **Core Research Question**: Does modeling tail losses using Generalized Extreme Value (GEV) and Generalized Pareto Distribution (GPD) reduce tail underestimation for low-frequency, high-severity financial losses?
- **Dataset**: Public operational loss benchmark data or synthetic heavy-tailed financial returns ([PRACTICE ASSUMPTION]).
- **Methodology**:
  1. Apply the **Peaks-over-Threshold (POT)** methodology: select a high threshold $u$ (e.g., 95th percentile).
  2. Fit excess losses ($Y = X - u \mid X > u$) to the Generalized Pareto Distribution:
     $$G_{\xi, \beta}(y) = 1 - \left( 1 + \frac{\xi y}{\beta} \right)^{-1/\xi}$$
  3. Estimate shape parameter $\xi$ (tail heaviness) and scale parameter $\beta$ via maximum likelihood.
  4. Derive semi-parametric tail VaR and Expected Shortfall (ES):
     $$\text{VaR}_{\alpha} = u + \frac{\beta}{\xi} \left[ \left( \frac{N}{N_u} (1 - \alpha) \right)^{-\xi} - 1 \right]$$
     $$\text{ES}_{\alpha} = \frac{\text{VaR}_{\alpha} + \beta - \xi u}{1 - \xi}$$
- **Validation**:
  - Compare EVT tail risk estimates against naive historical percentiles and Gaussian distribution assumptions.
- **Outputs**:
  - Mean Excess Plot verifying threshold selection linearity.
  - Tail risk comparison plot highlighting extreme tail divergence.
- **Limitations**:
  - Parameter estimates are sensitive to threshold choice $u$; requires sufficient sample size of extreme events.

---

## 3. Resume Framing & Background Translation

When presenting risk analytics projects on an engineering resume, follow clean, verifiable bullet structures:

### Recommended Resume Formatting

```markdown
### Quantitative Risk Modeling & Statistical Analytics

**Credit Risk Scorecard & Probability of Default Engine** | *Independent Project*
• Built end-to-end retail credit scorecard in Python using `optbinning` on 30,000+ benchmark borrower profiles.
• Binned non-linear continuous features via Weight of Evidence (WoE), filtering variables with Information Value (IV) < 0.02.
• Fitted penalized logistic regression; achieved Kolmogorov-Smirnov (KS) statistic of 41.2% and ROC-AUC of 0.79.
• Evaluated population distribution drift using Population Stability Index (PSI = 0.04), verifying scorecard stability.

**Multi-Asset Value at Risk (VaR) & Backtesting Pipeline** | *Independent Project*
• Designed parametric and historical 99% 1-day VaR engine in Python across a diversified equity and debt portfolio.
• Modeled dynamic volatility clustering using EWMA (RiskMetrics λ = 0.94); scaled to 10-day horizon via square-root-of-time rule.
• Backtested model performance across 250 out-of-sample trading days using Kupiec Proportion of Failures likelihood-ratio test.
```

### Bridging General Engineering to Quantitative Risk
- **Stochastic Processes & Reliability Engineering**: Coursework in structural reliability, limit state equations, or probabilistic mechanics translates directly to credit default probability ($PD$) and loss thresholds.
- **Extreme Event Modeling**: Experience analyzing multi-year rainfall return periods or peak hydrological discharge translates directly to financial Extreme Value Theory (EVT) and stress testing.
- **Ethical Rule**: Always distinguish between self-directed academic portfolio projects and corporate experience. Never invent fictitious production deployment claims or proprietary corporate datasets.

---

## 4. Verification & Navigation Links
- 📖 [Master Finance & Risk Hub](../README.md)
- 📖 [Risk Domain Knowledge](03_domain-knowledge.md)
- 📖 [Risk Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Risk High-Yield Question Bank](06_question-bank.md)
- 📖 [Risk Practice Cases](07_practice-and-cases.md)
- 📖 [Risk Mock Assessment](12_mock-assessment.md)
- 📖 [General Finance Projects](../../finance/finance/11_projects.md)

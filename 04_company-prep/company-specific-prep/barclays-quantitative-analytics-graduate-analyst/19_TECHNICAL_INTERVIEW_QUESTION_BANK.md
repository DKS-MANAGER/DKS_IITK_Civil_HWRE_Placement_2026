# 19 — Technical Interview Question Bank (60 Comprehensive Questions)

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Interview Architecture

The technical interview rounds for the **Barclays Quantitative Analytics Graduate Analyst (BA4) — QA Model Monitoring** role in Noida evaluate candidates across three structured tiers:
1. **Tier 1: Foundational Banking & Statistical Concepts (Q01–Q20):** Core mathematics, probability distributions, hypothesis testing, credit risk parameters ($PD, LGD, EAD$), and basic regulatory definitions.
2. **Tier 2: Applied Model Monitoring, Metrics & Coding (Q21–Q40):** Detailed mechanics of Discrimination (Gini, ROC, KS), Calibration ($O/E$, Hosmer-Lemeshow), Stability (PSI, CSI), SQL extraction, and Python/SAS implementation.
3. **Tier 3: Advanced Regulatory Frameworks, Governance & Case Scenarios (Q41–Q60):** IFRS 9 staging, Basel A-IRB capital derivation, SR 11-7 and PRA SS1/23 compliance, Post-Model Adjustments (PMAs), and live model crisis debugging.

Below is an exhaustive bank of **60 original technical questions with model institutional answers and interviewer trap alerts**.

---

### Tier 1: Foundational Banking & Statistical Concepts (Q01–Q20)

#### Q01. What is the fundamental difference between Expected Loss (EL) and Unexpected Loss (UL)?
- **Key Concepts:** Credit risk decomposition, IFRS 9 vs. Basel capital.
- **Model Answer:**  
  *Expected Loss (EL)* is the anticipated, statistical average loss a bank expects to incur from a credit portfolio over a defined period (typically 12 months). It is treated as an operational cost of doing business and is covered directly through accounting provisions on the balance sheet and loan pricing ($EL = PD \times LGD \times EAD$).  
  *Unexpected Loss (UL)* represents the potential volatility or standard deviation of credit losses around the expected mean, up to an extreme statistical confidence limit (99.9% under Basel). UL is not covered by loan pricing or provisions; it must be absorbed by the bank's equity capital buffer (CET1) to prevent insolvency during severe systemic crises.
- **Interviewer Trap:** Don't say "EL is for normal times and UL is for bad times." EL exists *always* as a mathematical expectation; UL is the extreme tail spread that capital absorbs.

#### Q02. Why is default defined at 90 Days Past Due (DPD) rather than 30 or 60 DPD?
- **Key Concepts:** Basel definition of default, cure rates, operational friction.
- **Model Answer:**  
  Empirical research across global retail and wholesale lending shows that 30 DPD and 60 DPD exhibit high "cure rates" (50% to 70% of borrowers with temporary cash-flow friction repay and return to performing status). At 90 DPD, empirical cure rates collapse below 5%–10%, marking a structural transition where full repayment without collateral liquidation or legal recovery becomes highly unlikely. The Basel Committee and EBA therefore codified 90 DPD (alongside qualitative "unlikeliness to pay") as the objective international default standard.
- **Interviewer Trap:** Remember to mention "unlikeliness to pay" (UTP) indicators (e.g., bankruptcy or distressed restructuring), which trigger default *even before* 90 DPD is reached.

#### Q03. Explain the mathematical intuition of the Odds Ratio in Logistic Regression.
- **Key Concepts:** Logit link function, relative odds.
- **Model Answer:**  
  In a logistic regression model, the dependent variable is the log-odds of default: $\ln\left(\frac{p}{1 - p}\right) = \beta_0 + \sum \beta_j X_j$. The odds ratio for a one-unit increase in feature $X_j$ is given by $OR_j = e^{\beta_j}$. If $\beta_j = +0.693$, then $OR = e^{0.693} = 2.0$. This means that a one-unit increase in $X_j$ doubles the odds of default, holding all other explanatory variables constant.
- **Interviewer Trap:** Do not confuse *odds* ($\frac{p}{1-p}$) with *probability* ($p$). An odds ratio of 2.0 does *not* mean the probability doubles, except when probabilities are extremely close to zero ($p < 0.01$).

#### Q04. What is Point-in-Time (PIT) PD versus Through-The-Cycle (TTC) PD?
- **Key Concepts:** Cyclical sensitivity, IFRS 9 vs. Basel IRB.
- **Model Answer:**  
  A *Point-in-Time (PIT) PD* measures default probability over the next 12 months conditioned on current macroeconomic conditions and near-term borrower characteristics. It fluctuates significantly across the business cycle (spikes during recessions, falls during expansions). PIT PD is required for **IFRS 9 financial accounting** to capture timely provisions.  
  A *Through-The-Cycle (TTC) PD* measures the average default rate of a credit risk grade across a full economic cycle (smoothing out cyclical fluctuations). It reflects long-term structural risk and is utilized in **Basel IRB regulatory capital** to prevent destabilizing pro-cyclical capital requirements.
- **Interviewer Trap:** Always state which regulatory framework requires which: IFRS 9 = PIT; Basel = TTC.

#### Q05. What is the difference between Model Validation (IMR) and Model Monitoring (QA)?
- **Key Concepts:** 3 Lines of Defense, pre-deployment vs. post-deployment surveillance.
- **Model Answer:**  
  *Model Validation* is an independent, Second Line of Defense (2LoD) activity performed by Independent Model Review (IMR). It provides pre-implementation challenge, audits mathematical conceptual soundness, inspects development code, builds challenger models, and re-validates models annually or during major rebuilds.  
  *Model Monitoring* is an ongoing, First Line of Defense (1LoD) surveillance activity conducted by Risk QA. It tracks the live performance, stability, and calibration of deployed models on a continuous monthly or quarterly basis, generating Model Monitoring Packs (MMPs) to detect degradation early.

#### Q06. What is the Central Limit Theorem (CLT), and why is it critical in credit risk back-testing?
- **Key Concepts:** Asymptotic normality, sample means, Binomial approximation.
- **Model Answer:**  
  The CLT states that the sum (or mean) of a sufficiently large number of independent and identically distributed random variables with finite variance converges in distribution to a normal distribution, regardless of the underlying population distribution. In credit risk back-testing, while individual defaults are binary Bernoulli trials, the aggregated default count in a rating band ($N > 500$) converges to a normal distribution, enabling the use of standard normal $Z$-tests for calibration checks.

#### Q07. Why cannot Ordinary Least Squares (OLS) regression be used directly to model probability of default?
- **Key Concepts:** Linear Probability Model (LPM) failure modes.
- **Model Answer:**  
  Using OLS to model a binary default indicator (the Linear Probability Model, $P(Y=1) = \mathbf{X}^T \boldsymbol{\beta}$) introduces three critical flaws:
  1. *Unbounded Predictions:* OLS can generate predicted probabilities outside $[0, 1]$ ($< 0$ or $> 1$), which is mathematically nonsensical.
  2. *Heteroskedasticity:* The error variance $\text{Var}(\epsilon_i \mid \mathbf{X}) = p_i(1 - p_i)$ is not constant, violating Gauss-Markov assumptions and invalidating standard error inference.
  3. *Non-normal Errors:* Residuals are strictly bimodal ($-\mathbf{X}^T \boldsymbol{\beta}$ or $1 - \mathbf{X}^T \boldsymbol{\beta}$), invalidating $t$-tests in finite samples.  
  Logistic regression resolves these issues via the non-linear sigmoid link function.

#### Q08. What is Exposure at Default (EAD) and how does it differ for a term loan versus a credit card?
- **Key Concepts:** Amortization vs. revolving facilities, Credit Conversion Factor (CCF).
- **Model Answer:**  
  EAD is the total gross exposure expected to be outstanding when a borrower defaults. For a fixed-rate term loan, EAD equals the amortized principal balance plus accrued interest. For revolving facilities (credit cards, overdrafts), EAD includes the currently drawn balance plus a modeled percentage of the currently undrawn credit limit that the borrower is anticipated to draw down prior to formal default: $\text{EAD} = \text{Drawn} + (\text{CCF} \times \text{Undrawn Limit})$.

#### Q09. Explain Type I and Type II errors in the context of credit underwriting decisions.
- **Key Concepts:** Confusion matrix, business loss vs. opportunity cost.
- **Model Answer:**  
  - *Type I Error (False Positive in default prediction):* The bank predicts a good borrower will default and erroneously rejects their loan. The business impact is **opportunity cost** (lost interest revenue and customer dissatisfaction).  
  - *Type II Error (False Negative in default prediction):* The bank predicts a bad borrower is safe and approves the loan, after which the borrower defaults. The business impact is **direct credit write-off loss** ($LGD \times EAD$).  
  Because credit default losses are asymmetric (a write-off of 50%–100% of balance vastly exceeds the 4%–8% annual interest margin), underwriting systems prioritize minimizing Type II errors over Type I errors.

#### Q10. What is Downturn LGD in Basel IRB, and why is it higher than average historical LGD?
- **Key Concepts:** Economic cycle correlation, collateral haircut.
- **Model Answer:**  
  Basel A-IRB rules mandate that LGD estimates must reflect economic downturn conditions rather than long-term historical averages. During severe economic recessions, asset prices (real estate, commercial machinery, vehicles) deflate, driving down liquidation recovery proceeds. Furthermore, corporate debtor insolvency queues lengthen, increasing legal and workout costs. Downturn LGD ensures that bank capital reserves are sufficient to absorb losses under worst-case historical recovery environments.

#### Q11. Define Multicollinearity and explain how it is diagnosed using the Variance Inflation Factor (VIF).
- **Key Concepts:** Feature correlation, standard error inflation.
- **Model Answer:**  
  Multicollinearity occurs when two or more independent variables in a regression model are highly linearly correlated. While it does not bias coefficient point estimates, it inflates parameter variances ($\text{SE}(\hat{\beta}_j) \to \infty$), making the model unstable and sensitive to minor data perturbations. It is diagnosed via $VIF_j = \frac{1}{1 - R_j^2}$. A $VIF > 5$ indicates severe collinearity requiring variable dropping or principal component reduction.

#### Q12. What is an Adverse Action Notice, and why does it constrain machine learning models?
- **Key Concepts:** FCRA, ECOA, Consumer Duty, explainability.
- **Model Answer:**  
  Under the US Fair Credit Reporting Act (FCRA) and Equal Credit Opportunity Act (ECOA), a lender that rejects a credit application or offers less favorable terms must provide the applicant with the **top 4 key reasons** for the decision. In complex machine learning models (e.g., deep neural networks), individual decision logic is opaque, preventing legal compliance unless post-hoc local attribution methods (such as TreeSHAP) are engineered to extract auditable reason codes.

#### Q13. What is the difference between a Parametric and Non-Parametric statistical test?
- **Key Concepts:** Distributional assumptions, robustness.
- **Model Answer:**  
  A *parametric test* (e.g., Student's $t$-test, ANOVA) assumes that the underlying population data follows a specific mathematical distribution (typically Gaussian) governed by parameters ($\mu, \sigma^2$). A *non-parametric test* (e.g., Mann-Whitney U, Kolmogorov-Smirnov, Wilcoxon signed-rank) makes no distributional assumptions, evaluating data ranks or empirical cumulative distributions. Non-parametric tests are preferred in credit risk when distributions exhibit heavy tails or extreme skewness.

#### Q14. Explain what Stationarity means in macroeconomic time-series modeling.
- **Key Concepts:** Covariance stationarity, mean-reversion, unit roots.
- **Model Answer:**  
  A time series is weakly (covariance) stationary if its mean $\mathbb{E}[Y_t] = \mu$ and variance $\text{Var}(Y_t) = \sigma^2$ are constant over time, and its autocovariance $\text{Cov}(Y_t, Y_{t-k}) = \gamma_k$ depends only on the lag length $k$, not on time $t$. Non-stationary series (such as un-differenced GDP or price indices) generate spurious regressions with invalid statistical inference when regressed against credit default rates.

#### Q15. What is the Brier Score, and how is it decomposed?
- **Key Concepts:** Mean squared probability error, Murphy decomposition.
- **Model Answer:**  
  The Brier Score is the mean squared difference between predicted probabilities $\hat{p}_i$ and observed binary outcomes $y_i \in \{0, 1\}$: $\text{BS} = \frac{1}{N}\sum(y_i - \hat{p}_i)^2$. Under Murphy's decomposition, it splits into: $\text{BS} = \text{Reliability} - \text{Resolution} + \text{Uncertainty}$. Reliability measures calibration error (ideal = 0), Resolution measures discriminatory separation (higher is better), and Uncertainty measures the intrinsic variance of the portfolio.

#### Q16. What is a Credit Scorecard Alignment / Scaling formula?
- **Key Concepts:** PDO (Points to Double the Odds), Base Score, Base Odds.
- **Model Answer:**  
  Credit scorecards convert log-odds into integer scores using linear scaling:  
  $\text{Score} = \text{Offset} + \text{Factor} \times \ln(\text{Odds})$.  
  The scaling constants are governed by two business parameters: Base Score at Base Odds, and Points to Double the Odds (PDO):  
  $\text{Factor} = \frac{\text{PDO}}{\ln(2)}$, $\text{Offset} = \text{Base Score} - \text{Factor} \times \ln(\text{Base Odds})$.  
  Common industry standard: 600 points at 50:1 odds, with 20 PDO.

#### Q17. What is a Markov Transition Matrix in banking?
- **Key Concepts:** State migration, memoryless property, rating drift.
- **Model Answer:**  
  A Markov transition matrix is a square matrix $P \in \mathbb{R}^{K \times K}$ where entry $P_{ij}$ represents the conditional probability that a borrower in credit state $i$ (e.g., Rating Grade $i$ or Delinquency Bucket $i$) transitions to state $j$ over a discrete time step $\Delta t$ (e.g., 1 month or 1 year), satisfying $\sum_j P_{ij} = 1.0$.

#### Q18. What is the difference between In-Sample, Out-of-Sample, and Out-of-Time validation?
- **Key Concepts:** Overfitting detection, temporal validation.
- **Model Answer:**  
  - *In-Sample (Train):* The dataset used to estimate model parameters.
  - *Out-of-Sample (OOS / Test):* Randomly held-out data from the *same time period* as the training data; tests cross-sectional generalizability.
  - *Out-of-Time (OOT):* Data collected from a *subsequent, chronologically distinct observation window* (e.g., model trained on 2021–2022; tested on 2023). OOT validation is critical in banking to evaluate how the model withstands temporal population drift and macroeconomic shifts.

#### Q19. What is the role of the Bank of England Prudential Regulation Authority (PRA)?
- **Key Concepts:** UK prudential supervision, SS1/23, capital adequacy.
- **Model Answer:**  
  The PRA is the prudential regulator of banks, building societies, credit unions, and major investment firms in the UK. Operating as part of the Bank of England, it enforces statutory capital and liquidity standards, approves internal IRB models, conducts annual stress testing (ACS), and issues regulatory standards such as **PRA SS1/23** governing model risk management.

#### Q20. What is a Workout LGD versus a Market LGD?
- **Key Concepts:** Economic recovery tracking vs. secondary bond pricing.
- **Model Answer:**  
  *Workout LGD* tracks actual cash recoveries (repayments, asset liquidations, guarantees) minus legal and collection expenses discounted back to default date using the Effective Interest Rate (EIR). It is used for non-traded retail and commercial loans.  
  *Market LGD* observes the secondary market trading price of defaulted bonds or syndicated loans shortly (30 to 60 days) after the default event. It is utilized in wholesale investment banking portfolios.

---

### Tier 2: Applied Model Monitoring, Metrics & Coding (Q21–Q40)

#### Q21. Derive the mathematical relationship between the Gini Coefficient and ROC-AUC.
- **Key Concepts:** Somers' D, Cumulative Accuracy Profile.
- **Model Answer:**  
  The ROC curve plots Sensitivity ($TPR$) against 1-Specificity ($FPR$). A random model has $\text{AUC} = 0.50$, and a theoretically perfect model has $\text{AUC} = 1.00$. The total area under the unit square is 1.0, and the area under the diagonal is 0.50. The area between the model ROC curve and the diagonal line is $A = \text{AUC} - 0.50$. The Gini coefficient scales this area relative to the maximum possible area above the diagonal ($A_{\text{max}} = 0.50$):  
  $$\text{Gini} = \frac{A}{A_{\text{max}}} = \frac{\text{AUC} - 0.50}{0.50} = \mathbf{2 \times \text{AUC} - 1}$$
- **Interviewer Trap:** Always state that Gini in credit risk is mathematically identical to Somers' $D$ rank correlation.

#### Q22. How is the Kolmogorov-Smirnov (KS) statistic calculated across 10 deciles?
- **Key Concepts:** Cumulative separation, maximum vertical distance.
- **Model Answer:**  
  Accounts are ranked from lowest score (highest risk) to highest score (lowest risk) and divided into 10 equal deciles. For each decile $k \in \{1, \dots, 10\}$, we compute:
  1. Cumulative percentage of total bad accounts: $F_{\text{bad}, k} = \frac{\sum_{i=1}^k \text{Bads}_i}{\text{Total Bads}}$.
  2. Cumulative percentage of total good accounts: $F_{\text{good}, k} = \frac{\sum_{i=1}^k \text{Goods}_i}{\text{Total Goods}}$.
  3. Absolute vertical distance: $D_k = |F_{\text{bad}, k} - F_{\text{good}, k}|$.  
  The KS statistic is the maximum distance across all deciles: $\text{KS} = \max_{k} D_k \times 100\%$. In strong retail scorecards, KS exceeds 40% and typically peaks at deciles 2, 3, or 4.

#### Q23. Why does the Population Stability Index (PSI) use symmetrized Kullback-Leibler divergence?
- **Key Concepts:** Relative entropy, symmetry requirement.
- **Model Answer:**  
  Standard Kullback-Leibler (KL) divergence $D_{\text{KL}}(A \parallel E) = \sum A_i \ln\left(\frac{A_i}{E_i}\right)$ is asymmetric: $D_{\text{KL}}(A \parallel E) \ne D_{\text{KL}}(E \parallel A)$. In statistical governance, a divergence metric comparing two populations should not depend arbitrarily on which sample is labeled "baseline" versus "current". Jeffreys (symmetrized) divergence sums both directions:  
  $$\text{PSI} = D_{\text{KL}}(A \parallel E) + D_{\text{KL}}(E \parallel A) = \sum (A_i - E_i) \ln\left(\frac{A_i}{E_i}\right)$$
  This guarantees $\text{PSI}(A, E) = \text{PSI}(E, A) \ge 0$ with $\text{PSI} = 0$ if and only if $A_i = E_i$ for all $i$.

#### Q24. What are the regulatory traffic light thresholds for PSI, and what actions are required at each?
- **Key Concepts:** Green, Amber, Red governance triggers.
- **Model Answer:**  
  - **$\text{PSI} < 0.10$ (GREEN):** Population is stable. Routine monitoring continues.
  - **$0.10 \le \text{PSI} < 0.25$ (AMBER):** Moderate population drift. The analyst must conduct Characteristic Stability Index (CSI) analysis on individual features to identify root causes and evaluate whether credit policy or marketing shifts explain the change.
  - **$\text{PSI} \ge 0.25$ (RED):** Significant population shift. The scorecard is operating on a materially different population than designed. Risk QA must escalate to the Model Risk Governance Committee, size a Post-Model Adjustment (PMA), and trigger an algorithmic recalibration or rebuild.

#### Q25. How do you handle zero-count bins in PSI calculation without distorting results?
- **Key Concepts:** Division by zero, log of zero, epsilon smoothing.
- **Model Answer:**  
  If a bin has zero actual or expected accounts, $\frac{A_i}{E_i}$ results in division by zero or $\ln(0) = -\infty$. In production code, we apply small-value smoothing: replacing zero counts with a minute epsilon value (e.g., $\epsilon = 10^{-6}$ or $0.0001\%$) and re-normalizing the distribution to sum to 1.0. Alternatively, if the development sample had sparse bins, bins should be combined (coarse-binned) prior to calculating PSI.

#### Q26. Why does the Hosmer-Lemeshow test almost always fail on large retail banking datasets?
- **Key Concepts:** Sample size sensitivity of $\chi^2$ test, economic vs. statistical significance.
- **Model Answer:**  
  The Hosmer-Lemeshow test statistic $H = \sum \frac{(O_g - E_g)^2}{N_g \bar{\pi}_g(1 - \bar{\pi}_g)}$ scales linearly with sample size $N$. In modern retail banking datasets where $N = 500,000$ accounts, the standard error becomes infinitesimally small. Even an economically trivial calibration error (e.g., predicting $PD = 1.02\%$ when actual default rate is $1.00\%$) yields a massive $H$ value that rejects the null hypothesis at $p < 0.0001$. Risk QA supplements HL with effect-size metrics: decile $O/E$ ratios, calibration slopes, and Binomial $Z$-scores.

#### Q27. What does a Calibration Slope of $\beta < 1.0$ indicate in a logistic recalibration regression?
- **Key Concepts:** Overfitting, extreme probability shrinkage.
- **Model Answer:**  
  In the recalibration regression $\text{logit}(P(Y=1)) = \alpha + \beta \cdot \text{logit}(\hat{p})$, a slope $\beta < 1.0$ indicates **overfitting**. The model's predicted probabilities are too extreme: high-risk accounts are assigned predicted probabilities that are too high, and low-risk accounts are assigned probabilities that are too low. In monitoring, an out-of-time $\beta < 0.85$ triggers an investigation into model variance and potential shrinkage recalibration.

#### Q28. How does Characteristic Stability Index (CSI) differ from PSI?
- **Key Concepts:** Feature-level drift vs. score-level drift.
- **Model Answer:**  
  PSI evaluates the distribution shift of the **final credit score** output. CSI applies the identical mathematical formula to **individual input characteristics** (e.g., Bureau Score, Debt-to-Income, Age, Account Utilization). When a scorecard triggers an Amber or Red PSI, the analyst computes CSI across all input features; the features with the highest CSI indicate the exact upstream root cause of the score drift.

#### Q29. Write a Python snippet to compute the Kolmogorov-Smirnov (KS) statistic using SciPy.
- **Key Concepts:** `scipy.stats.ks_2samp`.
- **Model Answer:**  
  ```python
  from scipy.stats import ks_2samp
  # Separate continuous predicted scores for Goods and Bads
  scores_goods = scores[y_actual == 0]
  scores_bads = scores[y_actual == 1]
  ks_stat, p_value = ks_2samp(scores_bads, scores_goods)
  print(f"KS Statistic: {ks_stat * 100:.2f}% (p-value: {p_value:.4e})")
  ```

#### Q30. In SQL, why is `ROWS BETWEEN 1 FOLLOWING AND 12 FOLLOWING` preferred over `RANGE BETWEEN` for default windowing?
- **Key Concepts:** SQL window framing, execution performance.
- **Model Answer:**  
  `ROWS BETWEEN` specifies physical row offsets, whereas `RANGE BETWEEN` evaluates logical value intervals across the order column. In large partitioned banking tables, `ROWS` execution requires significantly less memory and does not require the database engine to maintain variable logical window buffers, eliminating expensive temp-space disk spills in Teradata and Snowflake.

#### Q31. What is the Weight of Evidence (WoE) and Information Value (IV) formula?
- **Key Concepts:** Non-linear binning, feature selection.
- **Model Answer:**  
  For bin $i$:
  $$\text{WoE}_i = \ln\left( \frac{\text{Distribution Goods}_i}{\text{Distribution Bads}_i} \right) = \ln\left( \frac{G_i / G_{\text{total}}}{B_i / B_{\text{total}}} \right)$$
  Information Value (IV) evaluates the overall predictive power of the feature:
  $$\text{IV} = \sum_{i=1}^k \left( \frac{G_i}{G_{\text{total}}} - \frac{B_i}{B_{\text{total}}} \right) \times \text{WoE}_i$$
  Rule of thumb: $\text{IV} < 0.02$ (unpredictive), $0.10 \le \text{IV} \le 0.30$ (strong predictor), $\text{IV} > 0.50$ (suspicious; check for look-ahead bias).

#### Q32. Explain the difference between Concordant, Discordant, and Tied pairs in credit scoring.
- **Key Concepts:** Rank correlation, Mann-Whitney U.
- **Model Answer:**  
  Pairing every default (Bad) account with every non-default (Good) account:
  - *Concordant:* The Bad account has a higher predicted risk score than the Good account (correct rank-order).
  - *Discordant:* The Good account has a higher predicted risk score than the Bad account (inverted error).
  - *Tied:* Both accounts share the exact same predicted score.  
  $\text{AUC} = \frac{\text{Concordant} + 0.5 \times \text{Tied}}{\text{Total Pairs}}$.

#### Q33. What is the impact of manual underwriter overrides on model calibration?
- **Key Concepts:** Policy overrides, adverse selection.
- **Model Answer:**  
  When human credit underwriters override model recommendations (e.g., approving an applicant that the scorecard flagged for rejection), they introduce selection bias. Empirically, overridden accounts exhibit default rates **1.5x to 3.0x higher** than non-overridden peers within the same score band. QA Model Monitoring must track override frequency and isolate overridden accounts in back-testing to prevent human policy errors from contaminating baseline scorecard calibration.

#### Q34. How do you detect data leakage (look-ahead bias) during model monitoring?
- **Key Concepts:** Feature timestamp integrity, impossible discrimination.
- **Model Answer:**  
  Data leakage occurs when an input feature incorporates information generated *after* the scoring date (e.g., using "delinquency status at month 3" as an input to predict default at month 12). It is detected by:
  1. Exceptionally high IV ($IV > 0.80$) or near-perfect AUC ($AUC > 0.95$) on retail unsecured products.
  2. Sudden collapse in performance when tested on out-of-time production feeds.
  3. Auditing SQL joins to ensure all feature tables strictly filter: `feature_timestamp <= scoring_date`.

#### Q35. What is the purpose of monotonic binning in scorecard development?
- **Key Concepts:** Monotonic WoE, business logic compliance.
- **Model Answer:**  
  Monotonic binning groups continuous variables into discrete buckets such that the resulting Weight of Evidence (WoE) increases or decreases monotonically with risk. This ensures that the transformed variable has a strictly linear relationship with the log-odds in the logistic regression, guaranteeing that the final score behaves predictably and satisfies regulatory explainability requirements.

#### Q36. Write an ANSI SQL query to identify accounts that experienced an internal rating downgrade of $\ge 2$ notches.
- **Key Concepts:** SQL LAG / LEAD window functions.
- **Model Answer:**  
  ```sql
  WITH rating_changes AS (
      SELECT
          account_id,
          snapshot_month,
          internal_rating_grade,
          LAG(internal_rating_grade, 1) OVER (
              PARTITION BY account_id ORDER BY snapshot_month
          ) AS prior_grade
      FROM fact_model_score
  )
  SELECT *
  FROM rating_changes
  WHERE (internal_rating_grade - prior_grade) >= 2; -- Higher numeric grade = worse risk
  ```

#### Q37. What is the Brier Skill Score (BSS)?
- **Key Concepts:** Relative benchmark accuracy.
- **Model Answer:**  
  The Brier Skill Score measures the relative accuracy of a model compared to a naive reference forecast (such as predicting the historical portfolio average default rate $\bar{y}$ for all accounts):  
  $$\text{BSS} = 1 - \frac{\text{BS}_{\text{model}}}{\text{BS}_{\text{reference}}}$$
  $\text{BSS} = 1$ indicates a perfect model; $\text{BSS} = 0$ indicates no skill beyond the base rate; $\text{BSS} < 0$ indicates the model performs worse than naive guessing.

#### Q38. How does XGBoost handle missing values during prediction?
- **Key Concepts:** Default split direction, sparsity-aware split finding.
- **Model Answer:**  
  XGBoost features an automated "sparsity-aware split finding" algorithm. During training, when a feature has missing values, the algorithm evaluates placing all missing instances into the left child node and then the right child node, choosing whichever direction maximizes the gain metric. This optimal branch is designated as the **default path**. During live monitoring, any new record with a missing value is automatically routed down that pre-learned default path without requiring imputation.

#### Q39. What is the difference between Marginal PD and Cumulative PD?
- **Key Concepts:** Survival probability, discrete hazard rate.
- **Model Answer:**  
  - *Cumulative PD ($PD_{\text{cum}}(t)$):* The probability that a borrower defaults at *any time* between origination $t = 0$ and period $t$: $PD_{\text{cum}}(t) = 1 - S(t)$.
  - *Marginal PD ($d_t$):* The probability that a borrower defaults specifically *in period $t$*, having survived up to period $t - 1$: $d_t = S(t - 1) - S(t) = S(t - 1) \times h_t$.
  Under IFRS 9, 12-month ECL uses $d_t$ for periods $1 \le t \le 12$, and Lifetime ECL sums discounted losses using $d_t$ across all periods up to contractual maturity $T$.

#### Q40. Why must Effective Interest Rate (EIR) be used for IFRS 9 discounting rather than WACC?
- **Key Concepts:** IFRS 9 accounting standard, amortized cost.
- **Model Answer:**  
  IFRS 9 paragraph 5.5.17 mandates discounting cash shortfalls using the contractual **Effective Interest Rate (EIR)** established at loan origination because credit impairment provisions represent the reduction in the present value of contractual cash flows owed to the bank. Using WACC or market risk-free rates would conflate credit losses with the bank's own funding cost fluctuations or general interest rate duration risk.

---

### Tier 3: Advanced Regulatory Frameworks, Governance & Case Scenarios (Q41–Q60)

#### Q41. State the mathematical formula for the Basel IRB Capital Requirement ($K$) and explain each component.
- **Key Concepts:** Vasicek 1-factor model, Unexpected Loss.
- **Model Answer:**  
  $$K = \left[ LGD \times \Phi\left( \frac{\Phi^{-1}(PD) + \sqrt{\rho} \, \Phi^{-1}(0.999)}{\sqrt{1 - \rho}} \right) - (PD \times LGD) \right] \times \text{Maturity Adjustment}(M)$$
  - $\Phi(\cdot)$: Standard normal cumulative distribution function.
  - $\Phi^{-1}(PD)$: Latent default threshold for the borrower.
  - $\sqrt{\rho} \, \Phi^{-1}(0.999)$: Shift in default threshold under a 99.9% worst-case macroeconomic shock.
  - $\sqrt{1 - \rho}$: Idiosyncratic risk normalization factor.
  - $\left[ LGD \times \text{Conditional PD}_{99.9\%} \right]$: Total 99.9% Value at Risk loss.
  - $(PD \times LGD)$: Subtraction of Expected Loss (covered by provisions).
  - $\text{Maturity Adjustment}(M)$: Accounts for potential credit migration downgrade prior to maturity $M$ for wholesale facilities.

#### Q42. Why is Risk-Weighted Assets (RWA) defined as $K \times 12.5 \times EAD$? Why 12.5?
- **Key Concepts:** Basel 8% minimum capital standard.
- **Model Answer:**  
  Under Basel II/III, the minimum total regulatory capital ratio is set to **8.0%**:  
  $$\text{Minimum Capital} = 0.08 \times \text{RWA}$$
  Since $K$ represents the required capital percentage per unit of exposure ($K = \frac{\text{Required Capital}}{\text{EAD}}$), we have:  
  $$\text{Required Capital} = K \times \text{EAD} = 0.08 \times \text{RWA} \implies \text{RWA} = \frac{K \times \text{EAD}}{0.08} = K \times 12.5 \times \text{EAD}$$
  The multiplier **12.5** is exactly the mathematical reciprocal of the 8.0% capital requirement ($\frac{1}{0.08} = 12.5$).

#### Q43. What is the Basel 3.1 Aggregate Output Floor, and why was it introduced?
- **Key Concepts:** Model variability, Standardized vs. IRB RWAs.
- **Model Answer:**  
  The Basel 3.1 Output Floor mandates that total RWAs calculated using advanced internal models (A-IRB) cannot fall below **72.5%** of the RWAs calculated under the supervisory Standardized Approach:  
  $$\text{RWA}_{\text{Reported}} = \max\left(\text{RWA}_{\text{IRB}}, \; 0.725 \times \text{RWA}_{\text{Standardized}}\right)$$
  It was introduced by the Basel Committee to curb excessive variability in RWAs across global banks, preventing institutions from aggressively optimizing internal models to artificially minimize capital reserves.

#### Q44. Explain the quantitative and qualitative criteria for Significant Increase in Credit Risk (SICR) under IFRS 9.
- **Key Concepts:** Staging triggers, Lifetime PD delta, 30 DPD backstop.
- **Model Answer:**  
  An account moves from Stage 1 to Stage 2 if it triggers:
  1. *Quantitative Criterion:* Lifetime PD at the reporting date increases significantly compared to origination lifetime PD (e.g., Barclays dual test: Lifetime PD ratio $\ge 2.5\times$ and absolute increase $\ge 100$ bps).
  2. *Qualitative Indicators:* Placement on credit watchlist, concession/forbearance restructuring, or external credit bureau distress.
  3. *Regulatory Backstop:* Contractual payments are $> 30$ Days Past Due (mandatory hard floor).

#### Q45. Why is IFRS 9 ECL calculated across multiple probability-weighted macroeconomic scenarios rather than a single baseline forecast?
- **Key Concepts:** Jensen's Inequality, non-linear convex loss response.
- **Model Answer:**  
  ECL is a non-linear, strictly convex function of macroeconomic deterioration ($\frac{\partial^2 \text{ECL}}{\partial \text{Macro}^2} > 0$). In a severe recession, defaults spike exponentially, recovery collateral deflates, and large volumes of loans cross SICR thresholds into Lifetime ECL. By **Jensen's Inequality**:  
  $$\mathbb{E}[\text{ECL}(\text{Macro})] > \text{ECL}(\mathbb{E}[\text{Macro}])$$
  Evaluating ECL solely on a consensus "Baseline" scenario systematically underestimates expected losses by ignoring tail asymmetry. Probability-weighting (e.g., 50% Baseline, 15% Upside, 25% Downside, 10% Severe Downside) captures this non-linear loss distribution.

#### Q46. What constitutes a "Material Model Change" under Bank of England PRA SS1/23?
- **Key Concepts:** Materiality thresholds, pre-implementation regulatory approval.
- **Model Answer:**  
  Under PRA SS1/23 and European banking regulations, a model change is classified as *Material* if:
  1. It alters group-wide credit Risk-Weighted Assets (RWAs) or IFRS 9 provisions by more than 5%.
  2. It introduces a fundamental change in mathematical architecture (e.g., replacing a logistic regression with an ensemble tree model).
  3. It changes the core definition of default or rating scale structure.  
  *Governance Consequence:* Material changes cannot be deployed into production without prior formal review, independent validation (2LoD), and **written pre-approval from the PRA**. Minor changes require internal validation sign-off and post-implementation notification.

#### Q47. What is a Post-Model Adjustment (PMA), and what are the PRA SS1/23 regulatory requirements for PMAs?
- **Key Concepts:** Management overlays, sunset clauses, model remediation.
- **Model Answer:**  
  A PMA is a manual, quantitative adjustment added to or subtracted from model-generated provisions or capital figures when the model cannot adequately capture unprecedented events (e.g., COVID furlough distortions, UK energy price shocks).  
  Under **PRA SS1/23 Principle 5**, PMAs must:
  1. Be quantitatively justified using transparent satellite models or empirical benchmarks (no arbitrary expert guesses).
  2. Be independently reviewed by 2LoD and approved by the Model Risk Committee.
  3. Have an explicit **sunset clause** (expiration timeline). If a PMA persists for more than 4 consecutive quarters, Risk QA must initiate a formal model rebuild to absorb the adjustment into the code.

#### Q48. Case Scenario: A retail mortgage PD model reports an Amber PSI (0.16) and a Red Gini decline (from 0.65 to 0.44). Observed default rates remain low. How do you triage this?
- **Key Concepts:** Triaging workflow, root-cause isolation, policy vs. model failure.
- **Model Answer:**  
  1. *Immediate Assessment:* The model's rank-ordering capacity has collapsed (Gini fell 21 points), but benign macroeconomic conditions are masking credit losses (observed default rate is low). This is a dangerous leading indicator: when the macro cycle turns, the model will fail to separate safe from risky borrowers.
  2. *Execute Characteristic Stability Index (CSI):* Run CSI across all mortgage inputs. Check Loan-to-Value (LTV), Debt-to-Income (DTI), and Bureau Score.
  3. *Investigate Score Decoupling:* Check if underwriting loosened credit policies or if mortgage brokers found a loophole in documentation.
  4. *Governance Action:* Declare an Amber/Red monitoring alert in the quarterly MMP, advise the credit committee to freeze automated cutoffs and tighten manual underwriting, and submit an emergency model recalibration proposal.

#### Q49. What is the difference between CCAR Stress Testing in the US and PRA Annual Cyclical Scenario (ACS) in the UK?
- **Key Concepts:** Dodd-Frank DFAST/CCAR vs. BoE ACS.
- **Model Answer:**  
  Both frameworks project bank capital depletion under severe hypothetical 3-to-5 year macroeconomic recessions. However:  
  - *US Fed CCAR:* Applies to Barclays US Intermediate Holding Company (IHC). It features quantitative capital hurdles (CET1 must remain above minimums throughout the shock) and a qualitative assessment of the bank's internal risk governance and data infrastructure, with statutory authority to veto capital distributions (dividends/share buybacks).  
  - *BoE PRA ACS:* Applies to Barclays Group / UK bank. It tests resilience against simultaneous UK housing collapse, sharp unemployment spikes, and global trading market shocks, setting firm-specific **Pillar 2B PRA Buffers**.

#### Q50. How does Shapley value attribution satisfy the "Efficiency" (Additivity) axiom?
- **Key Concepts:** Local feature attribution, cooperative game theory.
- **Model Answer:**  
  The Efficiency axiom guarantees that the sum of the feature Shapley values across all $M$ inputs equals the difference between the model's prediction for applicant $x$ and the unconditional expected prediction across the training population:  
  $$\sum_{i=1}^M \phi_i(x) = f(x) - \mathbb{E}[f(X)]$$
  This ensures that feature contributions account for 100% of the prediction shift without unexplained residual variance.

#### Q51. What is the "Low Credit Risk Exemption" (LCRE) under IFRS 9?
- **Key Concepts:** Practical expedients, investment grade carve-out.
- **Model Answer:**  
  IFRS 9 allows lenders to presume that an asset has not experienced a Significant Increase in Credit Risk (SICR) if it is determined to have "low credit risk" at the reporting date (typically external investment grade: AAA down to BBB-). These assets are permitted to remain in Stage 1 with 12-month ECL without tracking historical origination PD. Barclays restricts LCRE strictly to sovereign bonds, central bank deposits, and select prime corporate counterparties.

#### Q52. Why is LGD modeled using a Workout approach rather than simply taking the collateral value at default?
- **Key Concepts:** Realization costs, time value of money, legal delays.
- **Model Answer:**  
  Collateral value at default does not equal cash recovered. Liquidating physical collateral (e.g., foreclosed commercial real estate) incurs:
  1. Liquidation haircuts (fire-sale price discounts).
  2. Legal, workout, and asset-maintenance fees.
  3. Time delay (often 18 to 36 months in judicial bankruptcy regimes), which erodes recovery value through discounting at the Effective Interest Rate. Workout LGD accounts for all post-default cash inflows and outflows discounted to the default timestamp.

#### Q53. Explain the term "Model Drift" and differentiate between Concept Drift and Covariate Shift.
- **Key Concepts:** Machine learning monitoring, population drift taxonomy.
- **Model Answer:**  
  - *Covariate Shift (Data Drift):* The distribution of input features $P(\mathbf{X})$ changes over time, while the conditional probability of default given features $P(Y \mid \mathbf{X})$ remains unchanged. (Measured via PSI / CSI). Example: The bank begins marketing to younger digital borrowers.
  - *Concept Drift:* The underlying relationship between input features and default $P(Y \mid \mathbf{X})$ changes over time, while input feature distributions $P(\mathbf{X})$ may remain unchanged. Example: Rapid interest rate hikes make previously affordable DTI levels default-prone.

#### Q54. In Basel IRB, what is the Asset Correlation ($\rho$) formula for Residential Mortgages versus Qualifying Revolving Retail Exposures (QRRE)?
- **Key Concepts:** Regulatory correlation constants.
- **Model Answer:**  
  - *Residential Mortgages:* Basel fixes $\rho = 0.15$ (15%). Mortgages exhibit moderate systematic risk linked to housing prices and national interest rate cycles.
  - *Qualifying Revolving Retail Exposures (Credit Cards):* Basel fixes $\rho = 0.04$ (4%). Consumer card defaults are driven primarily by idiosyncratic personal life events (job loss, illness, divorce) rather than nationwide systemic shocks, justifying lower asset correlation and lower capital requirements.

#### Q55. What is the role of a Challenger Model in Model Risk Management?
- **Key Concepts:** Benchmark testing, independent model review (IMR).
- **Model Answer:**  
  A challenger model is an independently developed alternative model built to solve the identical business problem using different mathematical architectures, functional forms, or data assumptions (e.g., building a LightGBM challenger to benchmark a legacy logistic scorecard). By comparing predictions, Risk QA quantifies model capability frontiers, isolates regions where the champion model exhibits weakness, and ensures conceptual soundness.

#### Q56. How do you evaluate whether an underwriting score threshold should be adjusted?
- **Key Concepts:** Marginal default rate, Risk-Reward optimization, NPV.
- **Model Answer:**  
  Score cutoffs are evaluated by analyzing the **marginal bad rate** and Net Present Value (NPV) curve at each score band:
  $$\text{Expected Profit}(s) = (1 - PD(s)) \times \text{Net Revenue} - PD(s) \times (LGD \times EAD)$$
  The optimal cutoff is the score where marginal revenue equals marginal credit loss ($\text{Expected Profit} = 0$). If portfolio monitoring reveals that macroeconomic stress has inflated $PD(s)$, the cutoff must be shifted higher (tightening credit) to preserve portfolio profitability.

#### Q57. What is an Asymptotic Single Risk Factor (ASRF) model, and why is it used in Basel?
- **Key Concepts:** Gordy (2003), portfolio invariance, capital additivity.
- **Model Answer:**  
  The ASRF framework (formalized by Michael Gordy, 2003) assumes that borrower defaults are driven by a single systematic macroeconomic factor $X$ and an idiosyncratic factor $\epsilon_i$. As the portfolio grows large ($N \to \infty$), idiosyncratic risks diversify away entirely, leaving only systematic risk. This achieves **portfolio invariance**: the capital required for a loan depends only on the borrower's individual characteristics ($PD, LGD, EAD, \text{asset class}$), not on the specific composition of the bank holding it.

#### Q58. Case Scenario: An automated monitoring script reveals that 12-month trailing Gini dropped from 0.62 to 0.38 in Wholesale Commercial Banking. The senior developer claims the script has a bug. How do you investigate?
- **Key Concepts:** Quantitative troubleshooting, code vs data verification.
- **Model Answer:**  
  1. *Sanity Check on Input Data:* Verify upstream SQL extracts for data feed pipeline issues: check missing values, duplicate account IDs, or corrupted score fields.
  2. *Replicate Manually on Subsample:* Extract a clean sample of 1,000 accounts and recalculate Gini using an alternative validated library (`scikit-learn` in Python and `pROC` in R) to eliminate script software bug hypotheses.
  3. *Inspect Rating Migration & Monotonicity:* Plot the decile bad-rate chart. Check if specific rating grades had unexpected default clusters (e.g., high defaults among Grade 2 borrowers due to an unrated corporate collapse).
  4. *Rule Out Software Bug:* If data and code are verified correct, confirm the Gini decline as a genuine Red breach and notify the Technical Approval Committee immediately.

#### Q59. What is the difference between a Model Limitation and a Model Deficiency under PRA SS1/23?
- **Key Concepts:** Regulatory taxonomy of model defects.
- **Model Answer:**  
  - *Model Limitation:* An inherent constraint arising from data availability, theoretical modeling approximations, or behavioral assumptions that are well-understood, documented, and mitigated through ongoing controls or PMAs (e.g., an inability to model unprecedented zero-interest-rate regimes).
  - *Model Deficiency:* A flaw, error, or operational failure in model design, implementation, code, or governance that renders the model non-compliant or inaccurate, requiring immediate remediation, code correction, or formal rebuild.

#### Q60. Why is Barclays committed to the RISES values, and how does Stewardship apply to Quantitative Analytics?
- **Key Concepts:** Barclays RISES values, ethics in risk management, Stewardship.
- **Model Answer:**  
  Barclays operates under five core values: **Respect, Integrity, Service, Excellence, and Stewardship**.  
  In Quantitative Analytics Model Monitoring, **Stewardship** means taking personal responsibility for the long-term safety, solvency, and ethical integrity of the bank. A quant analyst exhibits stewardship by refusing to obscure statistical model degradation, resisting pressure from business lines to artificially lower capital provisions, and ensuring that every model monitoring pack provides transparent, reproducible, and mathematically rigorous evidence that protects depositors and the wider financial system.

---

*Authoritative cross-reference: Barclays Quantitative Analytics Interview Protocols; Bank of England PRA SS1/23; US Federal Reserve SR 11-7; Gordy, M. B. (2003), "A risk-factor model foundation for ratings-based bank capital rules", Journal of Financial Intermediation.*


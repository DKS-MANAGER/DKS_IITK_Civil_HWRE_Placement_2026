# Module 19: Technical Interview Question Bank

> **Document Status**: Production-Grade Interview Preparation Bank `[TIER 3 / CANDIDATE DEBRIEFS & TIER 5 / EXPERT QUESTIONS]`  
> **Structure**: Three Rigorous Difficulty Tiers (Fundamentals, Applied Commercial Analytics, Advanced Systems) with Ideal Answers, Mathematical Formulations, and Follow-Up Traps  
> **Target Role**: Analyst (IQVIA India)  

---

## Level 1: Core Fundamentals & Programming (Python, SQL, SAS, Statistics)

### Q1.01: Handling Extreme Class Imbalance in Healthcare Models
* **Question**: *"In a rare oncology screening model, only 0.3% of records are positive. How do you evaluate and optimize this classifier?"*
* **Ideal Answer**:
  > *"When classes are severely imbalanced, conventional accuracy and ROC-AUC are fundamentally misleading. Standard accuracy achieves 99.7% by predicting the majority class for all rows, and ROC-AUC is artificially inflated because its denominator includes True Negatives, which dwarfs False Positives.*
  > 
  > *I optimize for **Precision-Recall AUC (PR-AUC)** and calibrate probability thresholds using the **F-beta score** ($F_\beta$, with $\beta = 2$ if minimizing false negatives / missing true patients is critical). During model training, I apply:*
  > 1. *Algorithm-level cost weighting: Setting `scale_pos_weight = 333` in XGBoost or using balanced class weights in logistic regression.*
  > 2. *Validation integrity: Using `StratifiedKFold` to ensure identical positive ratios across all training and holdout folds.*
  > 3. *Threshold tuning: Selecting the decision boundary that balances high clinical recall with acceptable clinical precision."*
* **Follow-Up Grilling**: *"Why not just run SMOTE (Synthetic Minority Over-sampling) on the entire dataset?"*
* **Trap Avoidance**: *"Applying SMOTE to the entire dataset before train-test splitting causes catastrophic data leakage. If used, SMOTE must be confined strictly within training cross-validation folds. However, in high-dimensional tabular claims data, synthetic interpolation frequently generates clinically impossible feature combinations."*

### Q1.02: SQL Window Functions vs GROUP BY
* **Question**: *"Explain the fundamental difference between a `GROUP BY` aggregation and a Window Function (`OVER (...)`). When must you use a window function in pharma commercial analytics?"*
* **Ideal Answer**:
  > *"`GROUP BY` collapses multiple individual records into a single summarized row per group, destroying row-level granularity. A Window Function computes an aggregate, rank, or offset across a defined partition of rows while **preserving individual row identity and original row counts**.*
  > 
  > *In commercial analytics, window functions are indispensable for:*
  > 1. *Top-$N$ Prescribers: `DENSE_RANK() OVER (PARTITION BY territory ORDER BY brand_trx DESC)`.*
  > 2. *Temporal Dynamics: Computing rolling 4-week moving averages (`AVG(trx) OVER (ORDER BY week ROWS BETWEEN 3 PRECEDING AND CURRENT ROW)`).*
  > 3. *Conversion Lag: Finding the date difference between a rep detail and first script using `LAG()` or `LEAD()` without expensive self-joins."*

### Q1.03: Multicollinearity Diagnostics & Treatment
* **Question**: *"In our brand marketing regression, why does high correlation between detailing spend and digital advertising cause problems, and how do you diagnose it?"*
* **Ideal Answer**:
  > *"When two marketing channels are highly collinear, the matrix $\mathbf{X}^T\mathbf{X}$ approaches singularity, causing $(\mathbf{X}^T\mathbf{X})^{-1}$ to explode. This does not degrade the overall model fit ($R^2$ remains high), but it drastically inflates the standard errors of individual channel coefficients:*
  > $$\text{Var}(\hat{\beta}_j) = \frac{\sigma^2}{\sum(x_{ji} - \bar{x}_j)^2} \times \text{VIF}_j$$
  > *As a result, coefficients become wild, unstable, or switch to clinically absurd negative signs (e.g., negative detailing ROI).*
  > 
  > *I diagnose it using the **Variance Inflation Factor (VIF)**. If $\text{VIF}_j > 5\text{–}10$, I address it by:*
  > 1. *Applying Ridge Regression ($\ell_2$ shrinkage) to condition the matrix: $(\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}$.*
  > 2. *Incorporating informative Bayesian priors to constrain coefficients to positive domains.*
  > 3. *Combining overlapping digital tactics into a composite digital engagement index via PCA."*

---

## Level 2: Applied Commercial Analytics & Econometrics

### Q2.01: Formulating Adstock & Diminishing Returns in MMM
* **Question**: *"Walk me through the exact mathematical equations you use to transform raw weekly promotional spend into an input suitable for Marketing Mix Modeling."*
* **Ideal Answer**:
  > *"I apply two sequential transformations: Geometric Adstock followed by Hill Saturation.*
  > 
  > *1. **Geometric Adstock (Carryover)**:*
  > $$A_t = X_t + \lambda A_{t-1}, \qquad \lambda \in [0, 1)$$
  > *where $\lambda$ governs the retention rate. The carryover half-life is $t_{1/2} = -\ln(2)/\ln(\lambda)$. For field detailing, $\lambda \approx 0.70$ (half-life $\approx 2$ weeks); for digital media, $\lambda \approx 0.25$ (half-life $\approx 0.5$ weeks).*
  > 
  > *2. **Hill Function Saturation (Diminishing Returns)**:*
  > $$S(A_t) = \frac{A_t^s}{K^s + A_t^s}$$
  > *where $K$ is the half-saturation point where response reaches 50% of maximum potential, and $s$ controls curvature.*
  > 
  > *The transformed variable $S(A_t)$ is then entered into a log-log or additive regression model, guaranteeing that promotional elasticities behave realistically without unbounded linear extrapolation."*

### Q2.02: Average ROI vs Marginal ROI & The Reallocation Theorem
* **Question**: *"If Channel A has an average ROI of \$4.00 per \$1.00 spent, and Channel B has an average ROI of \$2.50 per \$1.00 spent, should we automatically shift budget from Channel B to Channel A?"*
* **Ideal Answer**:
  > *"No, absolutely not. Reallocating budget based solely on **Average ROI** is a major commercial error. Spending decisions must be governed by **Marginal ROI (mROI)**:*
  > $$\text{mROI} = \frac{\partial (\text{Incremental Revenue})}{\partial (\text{Spend})}$$
  > *Channel A may have high historical average ROI, but if it has already passed its saturation threshold, its marginal return on the next dollar could be \$0.80 (losing money). Meanwhile, Channel B might be operating on the steep upward slope of its Hill response curve, where its marginal ROI is \$3.20.*
  > 
  > *Optimal portfolio reallocation occurs when **marginal ROIs are equalized across all channels** ($\text{mROI}_A = \text{mROI}_B$), subject to operational constraints."*

### Q2.03: Diagnosing Flat NRx Despite High Sales Rep Detailing
* **Question**: *"A brand manager notices that despite a 25% increase in field sales calls to Cardiologists in Q3, overall New-to-Brand Prescriptions (NRx) remained completely flat. How would you systematically investigate this using data?"*
* **Ideal Answer**:
  > *"I structure the investigation across four data-driven hypotheses:*
  > 1. *Reach vs Frequency Saturation: Check if reps were detailing the same already-converted doctors 8 times instead of expanding reach to new prescribers.*
  > 2. *Formulary & Access Barriers: Cross-reference pharmacy claims to check if a major health plan moved the drug to Tier 3 or added Prior Authorization restrictions in Q3 (preventing written scripts from being dispensed).*
  > 3. *Competitive Counter-Promotion: Check IQVIA Promotrak data to verify if a competitor launched an aggressive detailing or co-pay card campaign in the same period.*
  > 4. *Quality & Execution: Analyze CRM detailing notes to check whether details were delivered in primary position (Position 1) or relegated to secondary/tertiary positions."*

---

## Level 3: Advanced Systems, Bayesian & Case Strategy

### Q3.01: Bayesian Hierarchical Modeling for Small-Market Forecasting
* **Question**: *"How does a Bayesian Hierarchical Model enable robust demand forecasting across European countries with vastly different population sizes (e.g., Germany vs Slovenia)?"*
* **Ideal Answer**:
  > *"In a multi-country launch, fitting independent regressions (No Pooling) overfits small countries like Slovenia due to limited transaction volume and high noise. Conversely, combining all countries into a single regression (Complete Pooling) obliterates local pricing, reimbursement, and healthcare infrastructure differences.*
  > 
  > *A **Bayesian Hierarchical Model applies Partial Pooling**: country-specific parameters $\boldsymbol{\beta}_j$ are modeled as draws from a shared global hyperdistribution:*
  > $$\mathbf{y}_j \sim \mathcal{N}(\mathbf{X}_j \boldsymbol{\beta}_j, \sigma^2 \mathbf{I}), \qquad \boldsymbol{\beta}_j \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$$
  > *This creates **shrinkage**: small-market estimates borrow statistical strength from large-market priors, stabilizing parameter estimation while preserving genuine country-level variation."*

### Q3.02: Why Deep Learning is Rarely Used in Marketing Mix Modeling
* **Question**: *"Can we replace traditional Marketing Mix Modeling with a Deep LSTM or Transformer model?"*
* **Ideal Answer**:
  > *"In production biopharma commercial analytics, Deep Learning is fundamentally unsuitable for MMM due to four mathematical and business constraints:*
  > 1. *Data Volume: MMM is conducted on weekly brand sales over 2 to 3 years ($N \approx 104\text{ to } 156$). Deep networks have tens of thousands of weights and overfit small sample sizes instantly.*
  > 2. *Interpretability & Governance: Brand leaders will not reallocate \$20M in field-force spend based on opaque black-box weights. They require audited carryover half-lives and saturation plateaus.*
  > 3. *Causal Counterfactuals: Neural networks fit correlational associations; they cannot evaluate counterfactual policy scenarios ('What if we reduce detailing by 30%?') without structural econometric bounds.*
  > 
  > *Where deep learning genuinely excels at IQVIA is in large-scale patient journey mapping from unstructured electronic health records, automated clinical pathology image analysis, and processing millions of raw medical claims."*


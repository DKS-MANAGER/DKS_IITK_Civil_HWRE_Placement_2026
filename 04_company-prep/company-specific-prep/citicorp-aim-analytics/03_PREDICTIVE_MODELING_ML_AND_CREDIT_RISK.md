# Topic Master 03: Machine Learning, Predictive Modeling & Credit Risk Analytics

> **Consolidated Module**: CITI-TOPIC-03 (Predictive Modeling & Credit Risk)  
> **Target Assessment**: Technical Machine Learning Interview & Credit Risk Analytics Evaluations  
> **Scope**:
> - **SECTION A**: Supervised Learning for Credit Scoring (Linear vs Logistic Regression, Sigmoid Mechanics, Log-Odds & Coefficients)
> - **SECTION B**: Data Leakage Prevention & Temporal Train-Test Splitting in Banking Time-Series
> - **SECTION C**: Model Evaluation & Discriminatory Power (Confusion Matrix, Precision/Recall, ROC-AUC vs PR-AUC, Kolmogorov-Smirnov / KS Statistic)
> - **SECTION D**: Credit Risk Scorecard Development: Binning, Weight of Evidence (WoE) & Information Value (IV)
> - **SECTION E**: Model Stability & Monitoring: Population Stability Index (PSI) Calculation & Thresholds
> - **SECTION F**: Unsupervised Segmentation: K-Means Clustering & RFM (Recency, Frequency, Monetary) Customer Segmentation
> - **SECTION G**: 10 Technical ML & Credit Risk Grilling Q&As

---

# 03. Predictive Modeling & Machine Learning — Banking Analytics Module

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Explicitly required by the job description ("Statistical mind set – Familiarity in basic statistics, hypothesis testing, segmentation, and predictive modeling").  
> **Evidence Policy**: Specialized banking scorecards and industry benchmarks are classified as `[PREPARATION RECOMMENDATION — Supplementary Banking Context]`. All numerical examples are `[PRACTICE CASE ASSUMPTION]`.

---

## 1. End-to-End Analytics & Modeling Workflow

In banking analytics, a model is not an isolated piece of code; it is an analytical pipeline that drives a commercial decision:

```
[1. Business Question] ──────► "Can we predict which credit cardholders will default within 90 days?"
        │
[2. Data Extraction]   ──────► Query enterprise data warehouse via SQL (join accounts, txns, bureau)
        │
[3. EDA & Cleaning]    ──────► Inspect distributions, handle missing values, cap outliers
        │
[4. Feature Pipeline]  ──────► Construct behavioral ratios, lag features, utilization indicators
        │
[5. Train/Val/Test]    ──────► Time-based out-of-time (OOT) partition to prevent temporal leakage
        │
[6. Model Training]    ──────► Logistic regression baseline $\rightarrow$ Tree-based ensemble
        │
[7. Calibration]       ──────► Ensure predicted score represents true empirical probability
        │
[8. Threshold & Metric]──────► Set decision cutoff balancing charge-off loss vs customer friction
        │
[9. Synthesis & Rec]   ──────► Translate technical outputs into executive presentation
        │
[10. Monitor Drift]    ──────► Track Population Stability Index (PSI) and feature decay post-launch
```

---

## 2. Data Cleaning & Feature Engineering

### 2.1 Managing Missing Data
* **Missing Completely at Random (MCAR)**: Missingness is unrelated to any observed or unobserved variable (e.g., occasional network packet drop). Imputation via median or mode is mathematically valid.
* **Missing at Random (MAR)**: Missingness depends on observed features (e.g., younger applicants less likely to report home phone numbers). Conditional imputation via regression or iterative models.
* **Missing Not at Random (MNAR)**: Missingness depends directly on the unobserved value (e.g., high-wealth clients refusing to state annual income). **Do not simply impute the mean.** Create an explicit binary indicator `is_income_missing = 1` and preserve the signal.

### 2.2 Feature Scaling
* **Standardization ($Z$-Score)**: $X_{scaled} = \frac{X - \mu}{\sigma}$. Required for distance-based algorithms (K-Means, KNN, PCA) and gradient-descent models (Logistic Regression with regularization).
* **Robust Scaling**: $X_{robust} = \frac{X - \text{median}}{\text{IQR}}$. Uses median and interquartile range; resistant to extreme financial transaction outliers.
* **Tree Invariance**: Decision Trees and Random Forests split on ordered thresholds and are **invariant to monotonic feature scaling**.

### 2.3 Critical Data Leakage Traps
Data leakage occurs when information from outside the training dataset is used to create the model, producing artificially high validation metrics that collapse in production:
1. **Preprocessing Leakage**: Calculating imputation means or scaling parameters across the *entire* dataset before splitting. **The Rule**: Split into Train and Test *first*; fit scalers/imputers *only* on the training split, then transform validation/test sets using training parameters.
2. **Temporal Leakage**: Randomly splitting time-series financial transactions into $80/20$ train/test. Future customer transactions leak backward to predict earlier events. **The Rule**: Always use chronological splits (e.g., Train on Jan–June 2026, Test on July–Sept 2026).
3. **Target Leakage**: Including features that are populated *after* the target event occurs (e.g., using `collection_call_assigned` as a feature to predict loan default).

---

## 3. Linear Regression for Financial Forecasting

### 3.1 Mathematical Formulation & Ordinary Least Squares (OLS)
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
OLS minimizes the Sum of Squared Residuals (SSR):
$$\min_{\beta} \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \min_{\beta} (Y - X\beta)^T(Y - X\beta)$$
Normal equations solution:
$$\hat{\beta} = (X^T X)^{-1} X^T Y$$

### 3.2 The Gauss-Markov Theorem & Assumptions
For OLS estimators to be **BLUE** (Best Linear Unbiased Estimator):
1. **Linearity in Parameters**: $Y$ is a linear combination of coefficients $\beta_j$.
2. **Strict Exogeneity**: $E[\epsilon | X] = 0$. Regressors are uncorrelated with the error term.
3. **No Multicollinearity**: Regressors are linearly independent ($\text{det}(X^T X) \neq 0$).
4. **Homoscedasticity**: Error variance is constant across all levels of $X$: $\text{Var}(\epsilon_i | X) = \sigma^2$.
5. **No Autocorrelation**: Residuals are uncorrelated across observations: $\text{Cov}(\epsilon_i, \epsilon_j) = 0$ for $i \neq j$.

### 3.3 Multicollinearity & Variance Inflation Factor (VIF)
* **Impact**: Inflates coefficient variance, making parameter estimates unstable and p-values unreliable.
* **Formula**:
  $$\text{VIF}_j = \frac{1}{1 - R_j^2}$$
  Where $R_j^2$ is the $R^2$ from regressing feature $X_j$ against all other predictors.
* **Standard Thresholds**:
  * $\text{VIF} < 5$: Acceptable collinearity.
  * $\text{VIF} \ge 5 \text{ to } 10$: Severe collinearity; remove redundant features or combine via PCA.

### 3.4 Goodness-of-Fit: $R^2$ vs Adjusted $R^2$
* **$R^2$**: Proportion of variance explained:
  $$R^2 = 1 - \frac{\text{SS}_{res}}{\text{SS}_{tot}}$$
  * Limitation: Adding any feature (even pure random noise) strictly increases $R^2$.
* **Adjusted $R^2$**: Penalizes model complexity:
  $$\text{Adjusted } R^2 = 1 - \left[\frac{(1 - R^2)(n - 1)}{n - k - 1}\right]$$
  Where $n$ is sample size and $k$ is the number of predictors.

---

## 4. Logistic Regression: Classification & Credit Scoring

### 4.1 Derivation from Odds to Sigmoid
Linear regression can predict values $< 0$ or $> 1$, which cannot represent probabilities. Logistic regression models the **log-odds** as a linear function:

1. **Odds Ratio**:
   $$\text{Odds} = \frac{p}{1 - p}$$
2. **Log-Odds (Logit Link Function)**:
   $$\ln\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k = Z$$
3. **Inverting for Probability $p$ (Sigmoid Function)**:
   $$\frac{p}{1 - p} = e^Z \implies p = e^Z(1 - p) \implies p(1 + e^Z) = e^Z$$
   $$p = \frac{e^Z}{1 + e^Z} = \frac{1}{1 + e^{-Z}} = \sigma(Z)$$

```
     Probability p
        1.0 ┼                                    ╭──────────
            │                                 ╭──╯
        0.5 ┼────────────────────────────────● (Default Threshold 0.5)
            │                            ╭───╯
        0.0 ┼────────────╮───────────────╯
            └────────────┴───────────────────┴──────────
                        -∞                   0          +∞
                                             Z
```

### 4.2 Interpreting Logistic Coefficients & Worked Probability Calculation
* $\beta_i$ represents the change in the **log-odds** of the outcome per 1-unit increase in $X_i$, holding all other features constant.
* $e^{\beta_i}$ represents the multiplicative change in the **odds ratio**:
  * If $\beta_{\text{delinquencies}} = 0.693$, then $e^{0.693} \approx 2.0$. Each additional past delinquency **doubles the odds of default**.
  * If $\beta_{\text{income}} = -0.05$, then $e^{-0.05} \approx 0.951$. Each unit increase in income reduces the odds of default by $\approx 4.9\%$.

#### Fully Worked Example: Credit Card Default Probability
Suppose a retail bank's credit risk scorecard models 90-day delinquency risk using the logit equation:
$$\ln\left(\frac{p}{1 - p}\right) = -2.50 - 0.005 \cdot (\text{FICO} - 600) + 0.04 \cdot \text{DTI} + 0.35 \cdot \text{Inquiries}$$
A customer applies with:
* $\text{FICO} = 680$
* Debt-to-Income ($\text{DTI}$) $= 35\%$
* Recent Bureau Inquiries $= 2$

**Step 1: Compute the Linear Predictor ($Z$)**:
$$Z = -2.50 - 0.005(680 - 600) + 0.04(35) + 0.35(2)$$
$$Z = -2.50 - 0.005(80) + 1.40 + 0.70$$
$$Z = -2.50 - 0.40 + 1.40 + 0.70 = \mathbf{-0.80}$$

**Step 2: Calculate the Odds**:
$$\text{Odds} = e^Z = e^{-0.80} \approx \mathbf{0.4493}$$

**Step 3: Convert Odds to Predicted Probability ($p$)**:
$$p = \frac{\text{Odds}}{1 + \text{Odds}} = \frac{0.4493}{1 + 0.4493} = \frac{0.4493}{1.4493} \approx \mathbf{0.3100} \quad (31.0\%)$$

**Step 4: Interpretation & Sensitivity**:
* If the applicant had recorded 1 additional inquiry (3 instead of 2):
  * New linear predictor: $Z_{new} = -0.80 + 0.35 = -0.45$.
  * New odds: $e^{-0.45} \approx 0.6376$ ($0.4493 \times e^{0.35} = 0.4493 \times 1.419 = 0.6376$).
  * New probability: $p_{new} = \frac{0.6376}{1.6376} \approx \mathbf{38.9\%}$.
  * The odds increased by **$41.9\%$**, driving default probability up from $31.0\%$ to $38.9\%$.

### 4.3 Loss Function: Binary Cross-Entropy (Log-Loss)
Because least-squares produces a non-convex surface for sigmoid outputs, logistic regression is optimized using Maximum Likelihood Estimation via Binary Cross-Entropy:
$$\mathcal{L}(\beta) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \ln(\hat{p}_i) + (1 - y_i) \ln(1 - \hat{p}_i) \right]$$

---

## 5. Model Evaluation on Imbalanced Financial Datasets

In retail banking, target events are inherently rare: credit default rates are typically $2\%\text{ to }5\%$, while transaction fraud is $<0.1\%$.

### 5.1 Confusion Matrix

| Actual \ Predicted | Predicted Negative ($\hat{Y} = 0$) | Predicted Positive ($\hat{Y} = 1$) |
| :--- | :--- | :--- |
| **Actual Negative ($Y = 0$)** | **True Negative (TN)** | **False Positive (FP)** (Type I error) |
| **Actual Positive ($Y = 1$)** | **False Negative (FN)** (Type II error) | **True Positive (TP)** |

### 5.2 Metric Definitions & Business Trade-offs

1. **Accuracy**: $\frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$.
   * *Critical Flaw*: If $99\%$ of transactions are legitimate, a dumb model predicting all zeros achieves $99\%$ accuracy while catching zero fraud. **Never rely on accuracy alone.**
2. **Precision**: $\frac{\text{TP}}{\text{TP} + \text{FP}}$.
   * Fraction of predicted positives that are true positives.
   * *Business Cost*: Low precision means many false alarms (annoying cardholders with false transaction blocks).
3. **Recall (Sensitivity / True Positive Rate)**: $\frac{\text{TP}}{\text{TP} + \text{FN}}$.
   * Fraction of actual positives caught by the model.
   * *Business Cost*: Low recall means letting fraudsters escape or approving bad borrowers who charge off.
4. **Specificity (True Negative Rate)**: $\frac{\text{TN}}{\text{TN} + \text{FP}}$.
5. **$F_1$-Score**: Harmonic mean of Precision and Recall:
   $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$

### 5.3 Asymmetric Cost Matrix & Threshold Optimization Worked Example
In banking analytics, **the cost of a False Negative rarely equals the cost of a False Positive**.

#### Worked Commercial Problem: Selecting the Optimal Underwriting Cutoff
A portfolio consists of $10,000$ personal loan applicants. The true default rate is $4\%$ ($400$ defaults, $9,600$ non-defaulters).
* **Cost of False Negative (FN)**: Approving a borrower who defaults $= \mathbf{\$5,000}$ (unrecoverable charge-off loss).
* **Cost of False Positive (FP)**: Denying a creditworthy borrower $= \mathbf{\$200}$ (lost net lifetime interest margin).

We compare two classification thresholds:

```
Threshold A: τ = 0.50 (Standard Textbook Default)
┌──────────────────────┬──────────────────────┬──────────────────────┐
│                      │ Predicted Good (0)   │ Predicted Bad (1)    │
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Actual Good (0)      │ TN = 9,500           │ FP = 100             │
│ Actual Bad (1)       │ FN = 250             │ TP = 150             │
└──────────────────────┴──────────────────────┴──────────────────────┘
Metrics:
- Accuracy  = (150 + 9500) / 10000 = 96.5%
- Precision = 150 / (150 + 100) = 60.0%
- Recall    = 150 / (150 + 250) = 37.5%
Total Business Cost:
Cost = (250 × $5,000) + (100 × $200) = $1,250,000 + $20,000 = $1,270,000

Threshold B: τ = 0.20 (Risk-Tuned Cutoff)
┌──────────────────────┬──────────────────────┬──────────────────────┐
│                      │ Predicted Good (0)   │ Predicted Bad (1)    │
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Actual Good (0)      │ TN = 9,000           │ FP = 600             │
│ Actual Bad (1)       │ FN = 50              │ TP = 350             │
└──────────────────────┴──────────────────────┴──────────────────────┘
Metrics:
- Accuracy  = (350 + 9000) / 10000 = 93.5% (Lower accuracy!)
- Precision = 350 / (350 + 600) = 36.8% (Lower precision!)
- Recall    = 350 / (350 + 50) = 87.5% (High recall!)
Total Business Cost:
Cost = (50 × $5,000) + (600 × $200) = $250,000 + $120,000 = $370,000
```

**Interview Synthesis**:
* Despite lower accuracy ($93.5\%$ vs $96.5\%$) and lower precision ($36.8\%$ vs $60.0\%$), Threshold B saves the bank:
  $$\text{Net Annual Savings} = \$1,270,000 - \$370,000 = \mathbf{\$900,000}$$
* **Core Takeaway**: In high-stakes financial risk environments with asymmetric loss functions, **optimize for minimum financial loss or maximum expected utility, never raw accuracy or balanced F1 alone**.

---

## 6. Supplementary Banking Context: KS Statistic, Gini & PSI

> **Evidence Note**: The following credit risk scorecard methodologies represent standard industry context (`[PREPARATION RECOMMENDATION — Supplementary Banking Context]`), not official Citi assessment standards.

### 6.1 The Kolmogorov-Smirnov (KS) Statistic
The KS statistic measures the maximum vertical distance between the cumulative distribution of "Goods" (non-defaulters) and "Bads" (defaulters) across risk score deciles:
$$\text{KS} = \max_{d \in [1, 10]} \left| F_{bad}(d) - F_{good}(d) \right|$$

#### Decile Scorecard Validation Table (`[PRACTICE CASE ASSUMPTION]`):

| Decile (High $\to$ Low Risk) | Total Accounts | Defaulters (Bads) | Cum Bads (%) | Non-Defaulters (Goods) | Cum Goods (%) | KS Separation (%) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1 (Highest Risk)** | 10,000 | 2,000 | 40.0% | 8,000 | 8.4% | **31.6%** |
| **2** | 10,000 | 1,400 | 68.0% | 8,600 | 17.5% | **50.5%** |
| **3** | 10,000 | 750 | **83.0%** | 9,250 | 27.2% | **55.8% (Peak KS)**|
| **4** | 10,000 | 400 | 91.0% | 9,600 | 37.3% | 53.7% |
| **5** | 10,000 | 200 | 95.0% | 9,800 | 47.6% | 47.4% |
| **...** | ... | ... | ... | ... | ... | ... |
| **10 (Lowest Risk)** | 10,000 | 10 | 100.0% | 9,990 | 100.0% | 0.0% |

* **Standard Interpretation**:
  * **$\text{KS} > 40\%$**: Strong separation capability.
  * **Location**: Peak KS should occur in Deciles 2, 3, or 4. If peak KS occurs late (e.g. Decile 8), the model fails to isolate bads in the top risk tiers.

### 6.2 Gini Coefficient
$$\text{Gini} = 2 \times \text{ROC-AUC} - 1$$
Measures discriminatory power over a random baseline. An $\text{AUC} = 0.75 \implies \text{Gini} = 0.50$ ($50\%$).

### 6.3 Population Stability Index (PSI) Step-by-Step Worked Calculation
Quantifies whether the distribution of credit scores in production has drifted away from the development baseline:
$$\text{PSI} = \sum_{i=1}^B \left( \text{Actual}_i - \text{Expected}_i \right) \times \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$$

#### Worked Calculation Table (`[PRACTICE CASE ASSUMPTION]`):

| Score Bin | Expected % ($E_i$) [Dev] | Actual % ($A_i$) [Prod] | $(A_i - E_i)$ | $\ln(A_i / E_i)$ | Contribution $(A_i - E_i) \times \ln(A_i / E_i)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Bin 1 (300–550)** | 0.10 (10%) | 0.18 (18%) | +0.08 | $\ln(1.8) \approx +0.5878$ | $+0.08 \times 0.5878 = \mathbf{0.0470}$ |
| **Bin 2 (551–650)** | 0.25 (25%) | 0.32 (32%) | +0.07 | $\ln(1.28) \approx +0.2469$| $+0.07 \times 0.2469 = \mathbf{0.0173}$ |
| **Bin 3 (651–750)** | 0.40 (40%) | 0.35 (35%) | -0.05 | $\ln(0.875) \approx -0.1335$| $-0.05 \times (-0.1335) = \mathbf{0.0067}$ |
| **Bin 4 (751–850)** | 0.25 (25%) | 0.15 (15%) | -0.10 | $\ln(0.60) \approx -0.5108$| $-0.10 \times (-0.5108) = \mathbf{0.0511}$ |
| **TOTAL PSI** | **1.00** | **1.00** | — | — | $\mathbf{0.1221}$ |

**Interpretation & Governance Action**:
* Calculated $\text{PSI} = \mathbf{0.1221}$.
* **Industry Heuristic Benchmarks (`[INDUSTRY HEURISTIC BENCHMARK]` — Not Statutory Law or Citi Policy)**:
  * $\text{PSI} < 0.10$: Minor shift / stable; continue routine monitoring.
  * $\mathbf{0.10 \le \text{PSI} < 0.25}$: **Moderate Shift**. Investigate underlying feature movements or applicant sourcing changes; heightened monitoring without automated shutdown.
  * $\text{PSI} \ge 0.25$: **Significant Shift**. Indicates substantial population drift; triggers formal model risk review, potential threshold recalibration, or model retraining.

> [!NOTE]
> **Enterprise Model Risk Management (SR 11-7) Context**:  
> In modern banking analytics, model-risk decisions are **never executed based on a single scalar metric in isolation**. Under regulatory frameworks (Federal Reserve SR 11-7 / OCC 2011-12) and institutional risk governance:
> 1. **Model Materiality Tier**: High-impact Tier 1 models (e.g. automated capital adequacy, large-exposure credit approval) have stricter governance thresholds than low-impact marketing propensity models.
> 2. **Sample Volume & Sampling Noise**: In small portfolios or low-volume segments, elevated PSI can be driven by binomial sampling variance rather than genuine population drift.
> 3. **Portfolio Economic Performance**: PSI measures distributional shape, not model accuracy. If PSI is elevated but default roll-rates and rank-ordering (AUC / Gini) remain stable, the model may simply require cutoff recalibration rather than decommissioning.
> 4. **Scope Distinction**: Core hiring requirements for Citi AIM emphasize SQL, exploratory data analysis, business statistics, hypothesis testing, and machine learning fundamentals. Metrics like WoE, IV, KS, and PSI are valuable supplementary extensions for candidates targeting specialized credit risk and scorecard modeling teams.

---

## 7. Customer Segmentation & Unsupervised Learning

### 7.1 K-Means Clustering & Centroid Math
* **Objective**: Partition $n$ observations into $K$ clusters by minimizing the Within-Cluster Sum of Squares (WCSS / Inertia):
  $$\arg\min_S \sum_{i=1}^K \sum_{x \in S_i} \| x - \mu_i \|^2$$
* **Algorithm Lifecycle**:
  1. Initialize $K$ centroids randomly (or via K-Means++ to maximize distance between seeds).
  2. Assign each observation to the nearest centroid using Euclidean distance.
  3. Recompute each cluster centroid as the component-wise mean of assigned points:
     $$\mu_k = \frac{1}{|S_k|} \sum_{x_j \in S_k} x_j$$
  4. Repeat until centroid movement falls below convergence threshold $\epsilon$.
* **Determining Optimal $K$**:
  * **Elbow Method**: Plot Inertia vs $K$; identify the point of diminishing marginal gain.
  * **Silhouette Score**: Measures cohesion vs separation:
    $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, +1]$$
    Where $a(i)$ is mean intra-cluster distance and $b(i)$ is mean nearest-cluster distance.

### 7.2 RFM Segmentation in Banking Analytics
* **R (Recency)**: Days since last card swipe or digital banking login.
* **F (Frequency)**: Total transaction count per quarter.
* **M (Monetary Value)**: Total spend volume or average daily deposit balance.
* **Portfolio Action Mapping**:
  * **Champions ($R \uparrow, F \uparrow, M \uparrow$)**: Upsell to bespoke Wealth Management; exclusive lounge access.
  * **At-Risk High Spenders ($R \downarrow, F \downarrow, M \uparrow$)**: Dedicated relationship manager outreach, fee waivers, premium retention incentives.
  * **Dormant Accounts ($R \downarrow, F \downarrow, M \downarrow$)**: Automated re-engagement push notification, or reduce credit limits to free regulatory capital.

---

## 8. Decision Trees & Ensemble Methods

### 8.1 Splitting Criteria & Worked Gini Impurity Gain Calculation
* **Gini Impurity**:
  $$I_G(p) = 1 - \sum_{i=1}^C p_i^2$$

#### Worked Calculation: Information Gain on Loan Underwriting Split
* **Parent Node ($N = 100$ applicants)**:
  * $60$ Approved Loans (Goods, $p_1 = 0.60$)
  * $40$ Defaulted Loans (Bads, $p_2 = 0.40$)
  * Parent Impurity:
    $$I_G(\text{Parent}) = 1 - (0.60^2 + 0.40^2) = 1 - (0.36 + 0.16) = \mathbf{0.4800}$$

* **Proposed Split on Feature $\text{Credit Score} \ge 650$**:
  * **Left Child ($\text{Score} \ge 650$, $N_L = 60$)**: $50$ Goods, $10$ Bads.
    $$I_G(\text{Left}) = 1 - \left[\left(\frac{50}{60}\right)^2 + \left(\frac{10}{60}\right)^2\right] = 1 - \left[\frac{25}{36} + \frac{1}{36}\right] = 1 - \frac{26}{36} \approx \mathbf{0.2778}$$
  * **Right Child ($\text{Score} < 650$, $N_R = 40$)**: $10$ Goods, $30$ Bads.
    $$I_G(\text{Right}) = 1 - \left[\left(\frac{10}{40}\right)^2 + \left(\frac{30}{40}\right)^2\right] = 1 - \left[\frac{1}{16} + \frac{9}{16}\right] = 1 - \frac{10}{16} = \mathbf{0.3750}$$

* **Weighted Child Impurity**:
  $$I_G(\text{Children}) = \left(\frac{60}{100}\right) \times 0.2778 + \left(\frac{40}{100}\right) \times 0.3750 = 0.1667 + 0.1500 = \mathbf{0.3167}$$

* **Gini Impurity Gain**:
  $$\Delta I_G = I_G(\text{Parent}) - I_G(\text{Children}) = 0.4800 - 0.3167 = \mathbf{0.1633}$$
  * The split reduces impurity by **$0.1633$**, isolating good applicants on the left and defaults on the right.

---

## 9. 10 High-Yield Technical Interview Questions & Model Answers

#### Q01: How do you handle extreme class imbalance in credit default prediction?
* **Answer**:
  1. **Evaluation Metrics**: Never rely on accuracy. Use PR-AUC, Recall at fixed Top 5% alert volume, or dollarized cost-loss curves.
  2. **Algorithm Level**: Use cost-sensitive loss functions (`scale_pos_weight` in XGBoost, `class_weight='balanced'` in scikit-learn Logistic Regression) which penalize misclassifications of the minority class proportional to class prevalence.
  3. **Resampling Techniques**: Downsample the majority class or apply SMOTE on the *training split only* (never on validation/test data).
  4. **Threshold Tuning**: Lower decision threshold $\tau$ from default $0.5$ to match the empirical optimal operating point based on charge-off vs interest margins.

#### Q02: Explain the difference between L1 (Lasso) and L2 (Ridge) regularization. When would you prefer L1 in risk analytics?
* **Answer**:
  * **L1 Regularization (Lasso)**: Adds penalty $\lambda \sum |\beta_j|$. Drives non-essential feature coefficients to exactly zero, performing automatic feature selection and producing sparse, highly interpretable models.
  * **L2 Regularization (Ridge)**: Adds penalty $\lambda \sum \beta_j^2$. Shrinks coefficients toward zero without eliminating them; effective when features are collinear.
  * **Preference in Banking**: L1 is preferred when building transparent credit risk scorecards that must undergo regulatory and internal audit scrutiny, ensuring only statistically vital features remain in the scoring equation.

#### Q03: What is the difference between Bagging and Boosting?
* **Answer**:
  * **Bagging (Bootstrap Aggregation - Random Forest)**: Trains independent, deep trees in parallel on bootstrap samples and averages their outputs. Primarily **reduces variance** without increasing bias.
  * **Boosting (Gradient Boosting / XGBoost)**: Trains shallow trees sequentially, where each tree fits the residual errors of prior trees. Primarily **reduces bias** and variance, but is more vulnerable to overfitting if hyperparameters are not tuned.

#### Q04: What is data leakage and how do you prevent it in banking models?
* **Answer**:
  * Data leakage occurs when test or future information contaminates the model training process.
  * Common forms:
    1. Fitting scalers/imputers before train/test splitting.
    2. Using random splits instead of chronological (time-based) out-of-time splits on transactional datasets.
    3. Target leakage: incorporating downstream operational flags (e.g. `collection_agency_assigned`) into upfront underwriting models.

#### Q05: Why is ROC-AUC sometimes misleading on imbalanced datasets?
* **Answer**:
  * ROC-AUC plots TPR (Recall) against FPR ($\frac{\text{FP}}{\text{FP} + \text{TN}}$). When the negative class is massive (e.g. $99.9\%$ legitimate transactions), even a huge number of False Positives yields a tiny FPR because the denominator is dominated by TN. Consequently, ROC-AUC can exceed $0.95$ while the model's Precision is abysmal ($<5\%$). The Precision-Recall (PR) curve directly contrasts Precision and Recall without TN dilution, exposing weak models.

#### Q06: What is the KS (Kolmogorov-Smirnov) statistic and how is it used in scorecard validation?
* **Answer**:
  * The KS statistic represents the maximum vertical separation between the cumulative percentage of non-defaulters (goods) and defaulters (bads) across risk-score deciles.
  * In commercial banking, a model with $\text{KS} \ge 40\%$ is considered to have strong discriminative power.
  * Crucially, the peak KS must occur within the top 3 or 4 highest-risk deciles. If peak separation occurs in decile 7 or 8, the model fails to isolate bad borrowers early in the portfolio ranking.

#### Q07: How do you detect and remediate model drift in a deployed credit underwriting scorecard?
* **Answer**:
  * **Detection**: Calculate the Population Stability Index (PSI) monthly comparing the score and feature distributions of new applicants against the development baseline. Also monitor default roll-rates (early payment defaults / 30+ DPD in first 6 months).
  * **Remediation**:
    * If $\text{PSI} < 0.10$: Model is stable; continue monitoring.
    * If $0.10 \le \text{PSI} < 0.25$: Investigate which specific features shifted (e.g. bureau inquiry surge due to macro inflation); adjust underwriting cutoffs without retraining if underlying risk relationship holds.
    * If $\text{PSI} \ge 0.25$: Recalibrate scorecard intercept or retrain model on recent vintage cohorts.

#### Q08: How do you explain a black-box model (like XGBoost) to bank regulators or compliance auditors?
* **Answer**:
  * 1. **SHAP (SHapley Additive exPlanations)**: Use TreeSHAP to calculate the exact additive marginal contribution of each feature to an individual applicant's predicted score, based on cooperative game theory.
  * 2. **Adverse Action Reason Codes**: Under FCRA/ECOA regulatory requirements, banks must provide the top 4 reasons an applicant was rejected. Rank individual negative SHAP values to generate clear, legally compliant customer reason notices (e.g. "High revolving credit utilization", "Too many recent inquiries").
  * 3. **Global Interpretability**: Inspect Partial Dependence Plots (PDP) and SHAP summary plots to confirm monotonic, intuitive risk relationships (e.g. higher income decreases predicted default risk).

#### Q09: In K-Means clustering of retail bank customers, how do you handle features measured on radically different scales?
* **Answer**:
  * K-Means relies on Euclidean distance: $d(x, y) = \sqrt{\sum (x_i - y_i)^2}$.
  * If features such as `annual_income` ($\$50,000$) and `credit_card_count` ($3$) are unscaled, income will completely dominate the distance metric, rendering card count irrelevant.
  * **Solution**: Apply $Z$-score standardization ($Z = \frac{X - \mu}{\sigma}$) or Robust Scaler ($\frac{X - \text{median}}{\text{IQR}}$) to all numerical features before clustering, ensuring each dimension has equal variance weight.

#### Q10: Why can't we use Ordinary Least Squares (OLS) for credit card default probability prediction?
* **Answer**:
  * 1. **Unbounded Predictions**: OLS predicts $\hat{y} = X\beta \in (-\infty, +\infty)$, yielding nonsense probabilities $< 0$ or $> 1$.
  * 2. **Heteroscedasticity**: For a binary outcome $Y \in \{0, 1\}$, the error variance is $\text{Var}(\epsilon | X) = p(X)(1 - p(X))$, which directly violates OLS's constant-variance assumption.
  * 3. **Non-Normal Residuals**: The residuals $\epsilon_i = y_i - X_i\beta$ take only two discrete values ($1 - X_i\beta$ or $-X_i\beta$), violating the normality assumption required for valid hypothesis testing in small samples.


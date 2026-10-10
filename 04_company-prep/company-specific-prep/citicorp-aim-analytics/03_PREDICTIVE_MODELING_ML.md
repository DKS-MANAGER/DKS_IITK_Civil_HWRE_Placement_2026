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

### 4.2 Interpreting Logistic Coefficients
* $\beta_i$ represents the change in the **log-odds** of the outcome per 1-unit increase in $X_i$, holding all other features constant.
* $e^{\beta_i}$ represents the multiplicative change in the **odds ratio**:
  * If $\beta_{\text{delinquencies}} = 0.693$, then $e^{0.693} \approx 2.0$. Each additional past delinquency **doubles the odds of default**.
  * If $\beta_{\text{income}} = -0.05$, then $e^{-0.05} \approx 0.951$. Each unit increase in income reduces the odds of default by $\approx 4.9\%$.

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

### 5.3 Asymmetric Cost Matrix
In banking analytics, **the cost of a False Negative rarely equals the cost of a False Positive**:
* In Credit Default: $\text{Cost}(\text{FN}) = \text{Loan Charge-off Loss} \approx \$10,000$. $\text{Cost}(\text{FP}) = \text{Lost Interest on Denied Good Customer} \approx \$600$.
* Optimal threshold $\tau^*$ is selected to minimize total expected business loss:
  $$\min_\tau \left[ \text{Cost}(\text{FP}) \cdot \text{FP}(\tau) + \text{Cost}(\text{FN}) \cdot \text{FN}(\tau) \right]$$

### 5.4 ROC-AUC vs Precision-Recall Curves
* **ROC Curve**: True Positive Rate (Recall) vs False Positive Rate ($1 - \text{Specificity}$) across all cutoffs $\tau \in [0, 1]$.
  * **ROC-AUC**: Represents the probability that a randomly chosen positive instance receives a higher predicted score than a randomly chosen negative instance.
* **Precision-Recall (PR) Curve**: Precision vs Recall. **Superior to ROC-AUC on severely imbalanced datasets** ($<1\%$ prevalence), because ROC-AUC can remain deceptively high ($>0.90$) due to large true negative counts diluting the False Positive Rate.

---

## 6. Supplementary Banking Context: KS Statistic, Gini & PSI

> **Evidence Note**: The following credit risk scorecard methodologies represent standard industry context (`[PREPARATION RECOMMENDATION — Supplementary Banking Context]`), not official Citi assessment standards.

### 6.1 The Kolmogorov-Smirnov (KS) Statistic
The KS statistic measures the maximum vertical distance between the cumulative distribution of "Goods" (non-defaulters) and "Bads" (defaulters) across risk score deciles.

$$\text{KS} = \max_{d \in [1, 10]} \left| F_{bad}(d) - F_{good}(d) \right|$$

#### Decile Scorecard Validation Table (`[PRACTICE CASE ASSUMPTION]`):

| Decile (Sorted High $\to$ Low Risk) | Total Accounts | Defaulters (Bads) | Cum Bads (%) | Non-Defaulters (Goods) | Cum Goods (%) | KS Separation (%) |
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

### 6.3 Population Stability Index (PSI)
Quantifies whether the distribution of scores or features in production has drifted away from the baseline training distribution:
$$\text{PSI} = \sum_{i=1}^{10} \left( \text{Actual}_i - \text{Expected}_i \right) \times \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$$
* Industry Heuristics:
  * $\text{PSI} < 0.10$: Minimal shift; model stable.
  * $0.10 \le \text{PSI} < 0.25$: Moderate drift; requires investigation.
  * $\text{PSI} \ge 0.25$: Severe population shift; scorecard requires recalibration.

---

## 7. Customer Segmentation & Unsupervised Learning

### 7.1 K-Means Clustering
* **Objective**: Partition $n$ observations into $K$ clusters by minimizing the Within-Cluster Sum of Squares (WCSS / Inertia):
  $$\arg\min_S \sum_{i=1}^K \sum_{x \in S_i} \| x - \mu_i \|^2$$
* **Determining Optimal $K$**:
  * **Elbow Method**: Plot Inertia vs $K$; identify the point of diminishing returns.
  * **Silhouette Score**: Measures cohesion vs separation:
    $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, +1]$$
    Where $a(i)$ is mean intra-cluster distance and $b(i)$ is mean nearest-cluster distance.

### 7.2 RFM Segmentation in Banking Analytics
* **R (Recency)**: Days since last card swipe or branch transaction.
* **F (Frequency)**: Total transactions per quarter.
* **M (Monetary Value)**: Total spend volume or average daily balance.
* **Portfolio Action Mapping**:
  * Champions ($R \uparrow, F \uparrow, M \uparrow$): Premium wealth management upgrade.
  * At-Risk Spenders ($R \downarrow, F \downarrow, M \uparrow$): Proactive retention calls and fee waivers.
  * Dormant Accounts ($R \downarrow, F \downarrow, M \downarrow$): Automated re-engagement or credit limit pruning to release regulatory capital reserves.

---

## 8. Decision Trees & Ensemble Methods

### 8.1 Splitting Criteria
* **Gini Impurity**:
  $$I_G(p) = 1 - \sum_{i=1}^C p_i^2$$
* **Entropy & Information Gain**:
  $$H(p) = -\sum_{i=1}^C p_i \log_2(p_i), \quad \text{Gain} = H(\text{Parent}) - \sum \frac{N_j}{N} H(\text{Child}_j)$$

### 8.2 Random Forest vs Gradient Boosting (XGBoost/LightGBM)
* **Random Forest (Bagging)**:
  * Builds $B$ deep, independent trees on bootstrap samples; selects random subsets of features at each split ($\sqrt{p}$).
  * **Reduces model variance** without increasing bias. Robust against overfitting.
* **Gradient Boosting (Boosting)**:
  * Sequentially trains shallow trees (weak learners), where each subsequent tree fits the negative gradient (pseudo-residuals) of the loss function.
  * **Reduces model bias** and variance; requires careful hyperparameter tuning (learning rate $\eta$, tree depth, subsample ratio) to prevent overfitting.

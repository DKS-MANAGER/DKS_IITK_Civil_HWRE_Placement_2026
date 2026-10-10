# 03. Predictive Modeling & Machine Learning — Banking Analytics Module

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Evaluated in Technical Round 2 and Case interviews. Bridges statistics with predictive machine learning.

---

## 1. Predictive Modeling in Financial Services

At Citigroup, predictive modeling is applied to solve four commercial challenges:
1. **Credit Scoring & Underwriting**: Estimating **Probability of Default (PD)** to decide loan approval, credit limits, and interest rates.
2. **Customer Attrition / Churn**: Identifying accounts likely to close or stop transacting within the next 90 days.
3. **Marketing Propensity / Uplift**: Identifying cardholders most likely to accept an unsecured personal loan or premium card upgrade.
4. **Transaction Fraud Detection**: Classifying live swipes as fraudulent or legitimate in $<100\text{ milliseconds}$.

---

## 2. Linear Regression for Financial Forecasting

### 2.1 The Classical Linear Model
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
Where $\epsilon \sim \mathcal{N}(0, \sigma^2)$ represents the stochastic error term.

### 2.2 The 5 Gauss-Markov Assumptions
For Ordinary Least Squares (OLS) estimators $\hat{\beta}$ to be **BLUE** (Best Linear Unbiased Estimator):
1. **Linearity in Parameters**: The dependent variable is a linear function of parameters $\beta_i$.
2. **Strict Exogeneity**: Expected value of errors given regressors is zero: $E[\epsilon | X] = 0$.
3. **No Multicollinearity**: Regressors $X$ are not linearly dependent ($\text{Rank}(X) = k + 1$).
4. **Homoscedasticity**: Error variance is constant across all observations: $\text{Var}(\epsilon_i | X) = \sigma^2$.
5. **No Autocorrelation**: Errors are uncorrelated across observations: $\text{Cov}(\epsilon_i, \epsilon_j) = 0 \text{ for } i \neq j$.

### 2.3 Multicollinearity & Variance Inflation Factor (VIF)
* **Problem**: When features are highly correlated (e.g., Annual Income and Savings Balance), OLS coefficient estimates become highly unstable with inflated standard errors.
* **Diagnostic**: Compute VIF for each regressor:
  $$\text{VIF}_j = \frac{1}{1 - R_j^2}$$
  Where $R_j^2$ is the $R^2$ obtained from regressing feature $X_j$ against all other predictors.
* **Benchmark Threshold**:
  * $\text{VIF} < 5$: Acceptable multicollinearity.
  * $\text{VIF} > 5 \text{ to } 10$: Severe multicollinearity; candidate must drop or combine variables.

### 2.4 $R^2$ vs Adjusted $R^2$
* $R^2 = 1 - \frac{\text{SS}_{res}}{\text{SS}_{tot}}$: Fraction of variance explained. **Always increases** when new features are added, even if irrelevant.
* $\text{Adjusted } R^2 = 1 - \left[\frac{(1 - R^2)(n - 1)}{n - k - 1}\right]$: Penalizes the model for adding redundant predictors $k$.

---

## 3. Logistic Regression: The Bedrock of Credit Scoring

Unlike linear regression, which can predict unphysical probabilities $< 0$ or $> 1$, **Logistic Regression** models binary outcomes ($Y \in \{0, 1\}$) by mapping linear inputs to the $(0, 1)$ probability interval via the **Sigmoid (Logit) function**.

### 3.1 Mathematical Derivation
1. **Odds Ratio**: Ratio of probability of event occurring to event not occurring:
   $$\text{Odds} = \frac{p}{1 - p}$$
2. **Log-Odds (Logit Transformation)**:
   $$\ln\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k$$
3. **Solving for Probability $p$**:
   $$p = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \dots + \beta_k X_k)}} = \sigma(Z)$$

```
     Probability p
        1.0 ┼                             ╭──────────
            │                          ╭──╯
        0.5 ┼─────────────────────────● (Decision Threshold)
            │                     ╭──╯
        0.0 ┼───────────╮─────────╯
            └───────────┴─────────────┴──────────
                       -∞             0          +∞
                                      Z
```

### 3.2 Interpretation of Coefficients $\beta_i$
* For a 1-unit increase in predictor $X_i$, the **log-odds** of the event change by $\beta_i$.
* The **odds of default** are multiplied by $e^{\beta_i}$.
  * E.g., If $\beta_{late\_payments} = 0.693$, then $e^{0.693} \approx 2.0$. Each additional late payment **doubles the odds of default**.

### 3.3 Loss Function: Binary Cross-Entropy (Log-Loss)
$$\mathcal{L}(\beta) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]$$

---

## 4. Model Evaluation on Imbalanced Financial Datasets

In credit default and fraud analytics, default rates are typically $2\%\text{ to }5\%$, while fraud rates are $<0.1\%$. Standard accuracy is useless (a model predicting $100\%$ non-default achieves $98\%$ accuracy while failing completely).

### 4.1 Confusion Matrix

| Reality \ Prediction | Predicted Negative ($\hat{Y} = 0$) | Predicted Positive ($\hat{Y} = 1$) |
| :--- | :--- | :--- |
| **Actual Negative ($Y = 0$)** | **True Negative (TN)** | **False Positive (FP)** (Type I error) |
| **Actual Positive ($Y = 1$)** | **False Negative (FN)** (Type II error) | **True Positive (TP)** |

### 4.2 Key Evaluation Metrics

1. **Precision**: Out of all accounts predicted as default, what fraction actually defaulted?
   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
2. **Recall (Sensitivity / True Positive Rate)**: Out of all actual defaults, what fraction did the model catch?
   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
3. **Specificity (True Negative Rate)**:
   $$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$$
4. **$F_1$-Score**: Harmonic mean of Precision and Recall:
   $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$

### 4.3 ROC-AUC (Receiver Operating Characteristic)
* **ROC Curve**: Plots True Positive Rate (Recall) on the $Y$-axis versus False Positive Rate ($1 - \text{Specificity}$) on the $X$-axis across all possible decision thresholds ($0.0 \le \tau \le 1.0$).
* **AUC (Area Under Curve)**:
  * $\text{AUC} = 0.50$: Equivalent to random guessing.
  * $\text{AUC} = 0.70\text{ to }0.80$: Acceptable credit scorecard.
  * $\text{AUC} > 0.85$: High-performing predictive model.
  * **Probabilistic Meaning**: AUC represents the probability that a randomly chosen defaulting borrower will be assigned a higher default risk score than a randomly chosen non-defaulting borrower.

---

## 5. Banking Specialized Metrics: KS Statistic & Gini

### 5.1 The Kolmogorov-Smirnov (KS) Statistic (Citi Standard)
The **KS Statistic** measures the maximum separation distance between the cumulative distribution of "Goods" (non-defaulters) and "Bads" (defaulters) across model score deciles.

$$\text{KS} = \max_{d \in [1, 10]} \left| F_{bad}(d) - F_{good}(d) \right|$$

```
   Cumulative %
     100% ┼                                   ╭─── Cumulative Bads (Defaulters)
          │                              ╭────╯
          │                      ┌───────●
          │                      │  KS   │
          │                      │  GAP  │
          │                      └───────●──── Cumulative Goods
          │                         ╭────╯
       0% ┼─────────────────────────╯
          └─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────
          Decile 1    2     3     4     5     6     7     8     9    10 (Score Buckets)
```

### 5.2 Decile Validation Table Interpretation

| Decile (Ranked by Risk) | Total Accounts | Defaulters (Bads) | Cumulative Bads (%) | Non-Defaulters (Goods) | Cumulative Goods (%) | KS Spread (%) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1 (Highest Risk)** | 10,000 | 1,800 | 36.0% | 8,200 | 8.6% | **27.4%** |
| **2** | 10,000 | 1,400 | 64.0% | 8,600 | 17.7% | **46.3%** |
| **3** | 10,000 | 800 | **80.0%** | 9,200 | 27.4% | **52.6% (Peak KS)** |
| **4** | 10,000 | 450 | 89.0% | 9,550 | 37.4% | 51.6% |
| **...** | ... | ... | ... | ... | ... | ... |
| **10 (Lowest Risk)** | 10,000 | 20 | 100.0% | 9,980 | 100.0% | 0.0% |

* **Industry Acceptance Standards at Citi**:
  * **$\text{KS} > 40\%$**: Statistically sound scorecard.
  * **Location of Peak KS**: Should occur in the top deciles (**Deciles 2, 3, or 4**). If peak KS occurs in Decile 8, the model is failing to concentrate bads in the top risk tiers.

### 5.3 Gini Coefficient
$$\text{Gini} = 2 \times \text{AUC} - 1$$
* Measures the model's discriminatory power compared to a random model. If $\text{AUC} = 0.80$, $\text{Gini} = (2 \times 0.80) - 1 = 0.60$ ($60\%$).

### 5.4 Population Stability Index (PSI)
Used to monitor if model population distribution has shifted over time (concept drift):
$$\text{PSI} = \sum_{i=1}^{10} \left( \text{Actual}_i - \text{Expected}_i \right) \times \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$$
* $\text{PSI} < 0.10$: No significant population shift; model stable.
* $0.10 \le \text{PSI} < 0.25$: Moderate drift; model requires monitoring.
* $\text{PSI} \ge 0.25$: Severe population shift; scorecard **must be recalibrated**.

---

## 6. Unsupervised Learning: Customer Segmentation

### 6.1 K-Means Clustering
* **Algorithm Steps**:
  1. Initialize $K$ cluster centroids randomly.
  2. Assign each customer observation to the nearest centroid (Euclidean distance).
  3. Recompute centroids as the mean of all points assigned to that cluster.
  4. Repeat until centroids converge (inertia stabilizes).
* **Selecting Optimal $K$**:
  * **Elbow Method**: Plot Within-Cluster Sum of Squares (WCSS / Inertia) vs $K$. Look for the "elbow" where incremental variance explained drops off.
  * **Silhouette Score**: Measures how close a point is to its own cluster compared to neighboring clusters (ranges from $-1$ to $+1$).

### 6.2 RFM Segmentation Framework in Retail Banking
* **R (Recency)**: Days since last transaction or card swipe.
* **F (Frequency)**: Number of transactions per month.
* **M (Monetary Value)**: Total dollar volume spent or average daily balance.
* **Banking Personas**:
  * *Champions / Whales* ($R \uparrow, F \uparrow, M \uparrow$): Offer exclusive concierge cards, wealth management cross-sell.
  * *At-Risk High Spenders* ($R \downarrow, F \downarrow, M \uparrow$): Target immediate proactive retention incentives before they churn to competitors.
  * *Low-Value Dormant* ($R \downarrow, F \downarrow, M \downarrow$): Automated digital nudge or prune credit limit to free regulatory capital.

---

## 7. Decision Trees & Ensemble Methods

### 7.1 Splitting Metrics
* **Gini Impurity**:
  $$I_G(p) = 1 - \sum_{i=1}^C p_i^2$$
* **Entropy / Information Gain**:
  $$H(p) = -\sum_{i=1}^C p_i \log_2(p_i), \quad \text{Gain} = H(\text{Parent}) - \sum \frac{N_j}{N} H(\text{Child}_j)$$

### 7.2 Why Random Forest & Gradient Boosting (XGBoost) Dominate Banking
1. **Handling Non-Linearity & Interactions**: Automatically captures complex threshold effects (e.g., Debt-to-Income $>45\%$ is high risk only when Liquidity $< \$2,000$).
2. **Handling Missing Values & Outliers**: Tree splits are invariant to monotonic transformations and insensitive to extreme outliers.
3. **Class Imbalance Control**: Use techniques like `scale_pos_weight` in XGBoost or SMOTE (Synthetic Minority Over-sampling Technique) to ensure the minority default class is learned effectively.

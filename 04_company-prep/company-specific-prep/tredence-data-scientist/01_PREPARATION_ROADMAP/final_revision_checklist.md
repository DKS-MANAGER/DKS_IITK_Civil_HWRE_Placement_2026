# 01 — Final Revision Checklist (24 Hours Pre-Interview)
## Critical Rapid-Recall Formulas, Code Patterns & Verification Benchmarks

> **Document Status**: High-Yield Pre-Interview Verification Checklist `[TIER 5 / PEDAGOGICAL TOOL]`

---

## 1. SQL Rapid-Recall Cheat Sheet

```sql
-- 1. Order of Execution: FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> WINDOW -> ORDER BY -> LIMIT

-- 2. DENSE_RANK vs RANK vs ROW_NUMBER
SELECT 
    dept_id, employee_id, salary,
    ROW_NUMBER() OVER(PARTITION BY dept_id ORDER BY salary DESC) as row_num, -- Unique 1,2,3,4
    RANK()       OVER(PARTITION BY dept_id ORDER BY salary DESC) as rnk,     -- Ties leave gaps: 1,2,2,4
    DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) as dense_rnk-- Ties no gaps: 1,2,2,3
FROM employees;

-- 3. Moving Average & Running Total
SELECT 
    store_id, sale_date, daily_revenue,
    SUM(daily_revenue) OVER(PARTITION BY store_id ORDER BY sale_date 
                            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total,
    AVG(daily_revenue) OVER(PARTITION BY store_id ORDER BY sale_date 
                            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as rolling_7d_avg,
    LAG(daily_revenue, 1) OVER(PARTITION BY store_id ORDER BY sale_date) as prev_day_revenue
FROM store_sales;
```

---

## 2. Statistical & Experimental Design Formulas

- **Bayes' Theorem**:
  $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
- **Central Limit Theorem**:
  $$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$
- **Two-Sample $z$-Test Statistic**:
  $$z = \frac{(\bar{X}_1 - \bar{X}_2) - 0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$
- **A/B Testing Sample Size (Per Variant)**:
  $$n = \frac{2 \cdot (z_{\alpha/2} + z_{\beta})^2 \cdot \sigma^2}{\delta^2} \quad \text{where } \delta = \text{Minimum Detectable Effect (MDE)}$$
  *Standard 80% Power ($\beta = 0.20 \implies z_\beta \approx 0.84$), 5% Significance ($\alpha = 0.05 \implies z_{\alpha/2} \approx 1.96$): $(1.96 + 0.84)^2 \approx 7.84 \implies 2 \times 7.84 \approx 16$.*
  $$n \approx \frac{16 \sigma^2}{\delta^2}$$
- **Variance Reduction via CUPED**:
  $$\hat{Y}_{\text{CUPED}} = Y - \theta (X - \mathbb{E}[X]), \quad \text{where } \theta = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$$
  $$\text{Var}(\hat{Y}_{\text{CUPED}}) = \text{Var}(Y) \cdot (1 - \rho_{XY}^2)$$

---

## 3. Machine Learning Loss Functions & Metrics

- **Logistic Regression Sigmoid**:
  $$p(x) = \sigma(z) = \frac{1}{1 + e^{-z}}, \quad z = w^T x + b$$
- **Binary Cross-Entropy Loss (Log-Loss)**:
  $$\mathcal{L}(w) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln p_i + (1 - y_i) \ln (1 - p_i) \right]$$
- **Gini Impurity (CART Classification)**:
  $$I_G(t) = 1 - \sum_{k=1}^K p_k^2$$
- **Gradient Boosting Step**:
  $$\tilde{y}_i = -\left[ \frac{\partial \mathcal{L}(y_i, F(x_i))}{\partial F(x_i)} \right]_{F(x) = F_{m-1}(x)}$$
  *For MSE Loss: $\mathcal{L} = \frac{1}{2}(y - F)^2 \implies \text{Pseudo-residual } \tilde{y}_i = y_i - F_{m-1}(x_i)$.*
- **Precision, Recall & F1**:
  $$\text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}, \quad F_1 = \frac{2 \cdot P \cdot R}{P + R}$$
- **When to use PR-AUC over ROC-AUC**:
  *Use PR-AUC when evaluating highly imbalanced datasets (e.g., churn < 2%, fraud < 0.1%, structural failure < 1%). ROC-AUC can be deceptively optimistic because a vast pool of True Negatives inflates the True Negative Rate ($1 - FPR$).*

---

## 4. Time-Series Rapid Checklist

- **Weak Stationarity Conditions**:
  1. Mean $\mathbb{E}[y_t] = \mu$ is constant over time.
  2. Variance $\text{Var}(y_t) = \sigma^2 < \infty$ is constant over time.
  3. Autocovariance $\text{Cov}(y_t, y_{t-k}) = \gamma_k$ depends only on lag $k$, not on calendar time $t$.
- **Augmented Dickey-Fuller (ADF) Test**:
  - $H_0$: Series possesses a unit root ($\rho = 1$, non-stationary).
  - $H_1$: Series is stationary ($\rho < 1$).
  - Decision: Reject $H_0$ if $p\text{-value} < 0.05$.
- **Forecast Error Metrics**:
  $$\text{MAE} = \frac{1}{N}\sum |y_t - \hat{y}_t|, \quad \text{RMSE} = \sqrt{\frac{1}{N}\sum (y_t - \hat{y}_t)^2}, \quad \text{WAPE} = \frac{\sum |y_t - \hat{y}_t|}{\sum y_t}$$

---

## 5. Candidate Research Defense Quick Anchor

- **The 30-Second Elevator Pitch**:
  > *"I am an M.Tech in Civil Engineering specializing in Hydraulics & Water Resources at IIT Kanpur. My work centers on mathematical modeling, stochastic time-series, and explainable machine learning under uncertainty.*  
  > *In my machine learning risk research, I trained tree-based classifiers on imbalanced failure records, achieving a ROC-AUC of 0.983 and PR-AUC of 0.854, using TreeSHAP to provide exact, legally auditable feature attributions for infrastructure managers.*  
  > *At Tredence, where the mandate is solving the 'last-mile' problem by connecting algorithms to business actions, I bring rigorous numerical computing, advanced SQL/Python skills, and a proven ability to translate complex model outputs into high-stakes decisions."*

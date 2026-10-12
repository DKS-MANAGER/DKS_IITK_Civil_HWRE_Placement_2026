# 04. Tools & Technical Stack — Risk Analytics (Python & SQL)

> **Scope**: Practical implementation guide to quantitative risk modeling in Python and production risk database querying in SQL (PostgreSQL) for credit and market risk campus placements. `[PREPARATION HEURISTIC]`

---

## 1. Quantitative Risk Modeling in Python

Python is the industry standard for credit scorecard engineering, statistical model validation, and market risk simulations across American Express, Citi, Barclays, and Goldman Sachs Risk.

### 1.1 Credit Scorecard WoE Binning, Information Value & KS Engine

The following pure-Python/Pandas script implements Weight of Evidence (WoE), Information Value (IV), and the Kolmogorov-Smirnov (KS) statistic on synthetic applicant data:

```python
"""
Retail Credit Scorecard Validation Engine: WoE, IV & KS Statistic
[PREPARATION HEURISTIC]: Standard quantitative risk analyst screening drill.
"""

import numpy as np
import pandas as pd


def compute_woe_iv(df: pd.DataFrame, feature: str, target: str, bins: int = 5):
    """
    Computes Weight of Evidence (WoE) and Information Value (IV) for a numeric feature.
    Target: 1 = Defaulter (Bad), 0 = Non-Defaulter (Good).
    """
    data = df[[feature, target]].copy()
    data['bin'] = pd.qcut(data[feature], q=bins, duplicates='drop')
    
    # Aggregate Goods and Bads
    agg = data.groupby('bin', observed=True)[target].agg(
        total='count',
        bads='sum'
    ).reset_index()
    agg['goods'] = agg['total'] - agg['bads']
    
    total_goods = agg['goods'].sum()
    total_bads = agg['bads'].sum()
    
    # Laplace smoothing to avoid division by zero
    eps = 1e-4
    agg['dist_good'] = (agg['goods'] + eps) / total_goods
    agg['dist_bad'] = (agg['bads'] + eps) / total_bads
    
    # Calculate WoE and IV
    agg['woe'] = np.log(agg['dist_good'] / agg['dist_bad'])
    agg['iv_component'] = (agg['dist_good'] - agg['dist_bad']) * agg['woe']
    total_iv = agg['iv_component'].sum()
    
    return agg, total_iv


def compute_ks_statistic(y_true: np.ndarray, y_pred_prob: np.ndarray) -> float:
    """
    Computes the Kolmogorov-Smirnov (KS) metric between predicted default probabilities.
    """
    df_eval = pd.DataFrame({'target': y_true, 'prob': y_pred_prob})
    df_eval = df_eval.sort_values(by='prob', ascending=False).reset_index(drop=True)
    
    df_eval['cum_bads'] = df_eval['target'].cumsum() / df_eval['target'].sum()
    df_eval['cum_goods'] = (1 - df_eval['target']).cumsum() / (1 - df_eval['target']).sum()
    
    df_eval['ks'] = np.abs(df_eval['cum_bads'] - df_eval['cum_goods'])
    return df_eval['ks'].max()


# Verification on synthetic credit bureau sample
if __name__ == "__main__":
    np.random.seed(42)
    n = 1000
    bureau_score = np.random.normal(700, 50, n)
    # Default probability increases as bureau score drops
    prob_default = 1 / (1 + np.exp((bureau_score - 680) / 30))
    defaults = np.random.binomial(1, prob_default)
    
    test_df = pd.DataFrame({'bureau_score': bureau_score, 'default': defaults})
    woe_table, iv_val = compute_woe_iv(test_df, 'bureau_score', 'default', bins=5)
    ks_val = compute_ks_statistic(test_df['default'].values, prob_default)
    
    print(f"Feature Information Value (IV): {iv_val:.4f}")
    print(f"Model Kolmogorov-Smirnov (KS): {ks_val * 100:.2f}%")
    assert iv_val > 0.30, "Bureau score should show strong predictive IV (>0.30)"
    assert ks_val > 0.40, "Model should achieve target KS separation (>40%)"
```

---

### 1.2 Market Risk: Parametric, Historical & Expected Shortfall (CVaR)

```python
"""
Multi-Asset Market Risk Engine: Parametric VaR, Historical VaR & Expected Shortfall
[PREPARATION HEURISTIC]: Quantitative portfolio risk simulation.
"""

import numpy as np


def compute_market_risk_metrics(portfolio_value: float,
                                returns: np.ndarray,
                                alpha: float = 0.01):
    """
    Computes 1-Day 99% Parametric VaR, Historical VaR, and Expected Shortfall.
    """
    # 1. Parametric VaR (Normal Assumption: Z = 2.326 for 99%)
    mu = np.mean(returns)
    sigma = np.std(returns)
    z_alpha = 2.3263  # standard normal quantile for 99%
    parametric_var = (z_alpha * sigma - mu) * portfolio_value
    
    # 2. Historical Simulation VaR
    # Sort returns in ascending order (worst losses at the beginning)
    sorted_returns = np.sort(returns)
    cutoff_index = int(np.floor(alpha * len(returns)))
    hist_var_pct = -sorted_returns[cutoff_index]
    historical_var = hist_var_pct * portfolio_value
    
    # 3. Expected Shortfall (Conditional VaR - Average of tail losses beyond cutoff)
    tail_losses = sorted_returns[:cutoff_index]
    expected_shortfall = -np.mean(tail_losses) * portfolio_value
    
    return {
        "Parametric_VaR_99": parametric_var,
        "Historical_VaR_99": historical_var,
        "Expected_Shortfall_99": expected_shortfall,
        "Daily_Vol": sigma
    }


# Verification
if __name__ == "__main__":
    np.random.seed(42)
    # 500 trading days of synthetic returns with fat tails (Student-t distribution)
    daily_returns = np.random.standard_t(df=4, size=500) * 0.012
    v_port = 100_000_000.0  # ₹10 Cr portfolio
    
    metrics = compute_market_risk_metrics(v_port, daily_returns, alpha=0.01)
    for k, v in metrics.items():
        print(f"{k}: ₹{v:,.2f}")
    assert metrics["Expected_Shortfall_99"] > metrics["Historical_VaR_99"], \
        "Expected Shortfall must strictly exceed VaR in the tail!"
```

---

## 2. Production SQL for Credit Risk & Portfolio Monitoring

In banking analytics screening rounds, interviewers test your ability to construct risk aggregations, aging schedules, and roll-rate matrices in ANSI SQL / PostgreSQL.

### 2.1 Delinquency Aging Schedule
Given table `loan_accounts(account_id, customer_id, outstanding_balance, days_past_due)`:

```sql
-- Production Delinquency Aging Schedule by Regulatory Buckets
SELECT 
    CASE 
        WHEN days_past_due = 0 THEN 'Current (Bucket 0)'
        WHEN days_past_due BETWEEN 1 AND 29 THEN '1-29 DPD (Bucket 1)'
        WHEN days_past_due BETWEEN 30 AND 59 THEN '30-59 DPD (Bucket 2)'
        WHEN days_past_due BETWEEN 60 AND 89 THEN '60-89 DPD (Bucket 3)'
        ELSE '90+ DPD (NPA / Default)'
    END AS delinquency_stage,
    COUNT(account_id) AS total_accounts,
    ROUND(SUM(outstanding_balance), 2) AS total_exposure,
    ROUND((SUM(outstanding_balance) * 100.0 / SUM(SUM(outstanding_balance)) OVER ()), 2) AS pct_of_portfolio
FROM loan_accounts
GROUP BY 
    CASE 
        WHEN days_past_due = 0 THEN 'Current (Bucket 0)'
        WHEN days_past_due BETWEEN 1 AND 29 THEN '1-29 DPD (Bucket 1)'
        WHEN days_past_due BETWEEN 30 AND 59 THEN '30-59 DPD (Bucket 2)'
        WHEN days_past_due BETWEEN 60 AND 89 THEN '60-89 DPD (Bucket 3)'
        ELSE '90+ DPD (NPA / Default)'
    END
ORDER BY MIN(days_past_due);
```

---

### 2.2 30-Day Roll Rate Transition Matrix Query
To measure the probability of an account rolling forward from one delinquency bucket to the next over consecutive months:

```sql
-- Monthly Delinquency Roll-Rate Transition Matrix
WITH MonthlySnapshots AS (
    SELECT 
        account_id,
        snapshot_date,
        delinquency_bucket AS current_bucket,
        LEAD(delinquency_bucket) OVER (
            PARTITION BY account_id 
            ORDER BY snapshot_date
        ) AS next_bucket
    FROM loan_monthly_snapshots
    WHERE snapshot_date IN ('2025-10-31', '2025-11-30')
)
SELECT 
    current_bucket,
    next_bucket,
    COUNT(account_id) AS transitioned_accounts,
    ROUND(
        (COUNT(account_id) * 100.0 / SUM(COUNT(account_id)) OVER (PARTITION BY current_bucket)), 
        2
    ) AS roll_rate_probability_pct
FROM MonthlySnapshots
WHERE next_bucket IS NOT NULL
GROUP BY current_bucket, next_bucket
ORDER BY current_bucket, next_bucket;
```

---

### 2.3 Portfolio Expected Loss ($EL$) Aggregation Query
To compute regulatory Expected Loss under Basel III / IFRS 9:

```sql
-- Aggregate Portfolio Expected Loss Calculation
SELECT 
    product_type,
    COUNT(loan_id) AS total_loans,
    ROUND(SUM(drawn_balance + ccf * undrawn_limit), 2) AS total_ead,
    ROUND(AVG(pd_score), 4) AS portfolio_avg_pd,
    ROUND(AVG(downturn_lgd), 4) AS portfolio_avg_lgd,
    ROUND(SUM((drawn_balance + ccf * undrawn_limit) * pd_score * downturn_lgd), 2) AS total_expected_loss,
    ROUND(
        (SUM((drawn_balance + ccf * undrawn_limit) * pd_score * downturn_lgd) * 100.0 / 
         SUM(drawn_balance + ccf * undrawn_limit)), 
        2
    ) AS el_rate_pct
FROM portfolio_exposures
GROUP BY product_type
ORDER BY total_expected_loss DESC;
```

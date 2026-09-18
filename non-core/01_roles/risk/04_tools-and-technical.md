# 04. Risk Analyst: Tools, Technical Stack & Quantitative Methods

> Comprehensive operational guide to Python risk modeling, SQL portfolio queries, Excel financial risk functions, and quantitative modeling tools.

---

## 1. Python for Risk Analytics & Modeling

Risk analysts utilize Python for probability distributions, scorecard development, Monte Carlo simulations, and extreme value analysis.

```python
import numpy as np
import pandas as pd
from scipy import stats

# 1. PARAMETRIC & HISTORICAL VALUE AT RISK (VaR)
def calculate_var_cvar(returns, portfolio_val=10_000_000, alpha=0.99):
    # Historical VaR
    hist_var = -np.percentile(returns, (1 - alpha) * 100) * portfolio_val
    tail_losses = returns[returns < -hist_var / portfolio_val]
    hist_cvar = -tail_losses.mean() * portfolio_val
    
    # Parametric VaR (Normal)
    mu, sigma = returns.mean(), returns.std()
    z_score = stats.norm.ppf(alpha)
    param_var = (z_score * sigma - mu) * portfolio_val
    param_cvar = (sigma * stats.norm.pdf(z_score) / (1 - alpha) - mu) * portfolio_val
    
    return {
        "Hist_VaR_99": hist_var, "Hist_CVaR_99": hist_cvar,
        "Param_VaR_99": param_var, "Param_CVaR_99": param_cvar
    }

# 2. WEIGHT OF EVIDENCE (WoE) & INFORMATION VALUE (IV)
def calculate_woe_iv(df, feature_col, target_col):
    eps = 1e-6
    grouped = df.groupby(feature_col)[target_col].agg(['count', 'sum'])
    grouped.columns = ['Total', 'Bads']
    grouped['Goods'] = grouped['Total'] - grouped['Bads']
    
    total_goods = grouped['Goods'].sum()
    total_bads = grouped['Bads'].sum()
    
    grouped['Dist_Good'] = grouped['Goods'] / total_goods + eps
    grouped['Dist_Bad'] = grouped['Bads'] / total_bads + eps
    
    grouped['WoE'] = np.log(grouped['Dist_Good'] / grouped['Dist_Bad'])
    grouped['IV'] = (grouped['Dist_Good'] - grouped['Dist_Bad']) * grouped['WoE']
    
    return grouped, grouped['IV'].sum()
```

---

## 2. SQL for Credit Risk & Portfolio Monitoring

Risk SQL queries center around delinquency roll-rates, vintage curve analysis, and portfolio loss aggregation.

### 1. Delinquency Roll-Rate Migration Matrix Query
```sql
WITH MonthlyStatus AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', statement_date) as month,
        CASE 
            WHEN days_past_due = 0 THEN 'Current'
            WHEN days_past_due BETWEEN 1 AND 30 THEN '30 DPD'
            WHEN days_past_due BETWEEN 31 AND 60 THEN '60 DPD'
            WHEN days_past_due BETWEEN 61 AND 90 THEN '90 DPD'
            ELSE 'Default / NPA'
        END AS dpd_bucket
    FROM LoanStatements
),
Migration AS (
    SELECT 
        m1.month as start_month,
        m1.dpd_bucket as from_bucket,
        m2.dpd_bucket as to_bucket,
        COUNT(DISTINCT m1.customer_id) as customer_count
    FROM MonthlyStatus m1
    JOIN MonthlyStatus m2 
        ON m1.customer_id = m2.customer_id 
        AND m2.month = m1.month + INTERVAL '1 month'
    GROUP BY 1, 2, 3
)
SELECT 
    from_bucket,
    to_bucket,
    customer_count,
    ROUND(100.0 * customer_count / SUM(customer_count) OVER (PARTITION BY from_bucket), 2) as transition_prob_pct
FROM Migration
ORDER BY from_bucket, to_bucket;
```

---

## 3. Excel for Financial Risk & Sensitivity Analysis

### High-Yield Risk Formulas in Excel:
1. **Parametric VaR**: `=NORM.INV(0.99, mu, sigma) * Portfolio_Value`
2. **Poisson Loss Frequency**: `=POISSON.DIST(k, lambda, cumulative)`
3. **Bond Duration & DV01**: `=DURATION(settlement, maturity, coupon, yld, frequency)`
4. **Loan Amortization & ECL**: Build dynamic schedules linking `=PMT()` with probability-weighted recovery cash flows.

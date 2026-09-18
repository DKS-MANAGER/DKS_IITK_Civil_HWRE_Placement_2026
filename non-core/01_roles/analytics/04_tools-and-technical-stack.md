# 04. Analytics: Tools, Technical Stack & Computational Methods

> Pure Analytics & Decision Science technical stack: Python (NumPy, Pandas, Scikit-learn), SQL, Applied Statistics, and Power BI / Tableau dashboard architectures.

---

## 1. Python for Data Analytics & Wrangling

Analytics professionals use Python for exploratory data analysis (EDA), data wrangling, cohort computation, and machine learning.

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report

# 1. COHORT RETENTION MATRIX COMPUTATION
def compute_cohort_retention(df):
    # df columns: ['user_id', 'order_date']
    df['order_month'] = df['order_date'].dt.to_period('M')
    df['cohort_month'] = df.groupby('user_id')['order_date'].transform('min').dt.to_period('M')
    
    cohort_data = df.groupby(['cohort_month', 'order_month']).agg(n_users=('user_id', 'nunique')).reset_index()
    cohort_data['period_number'] = (cohort_data['order_month'] - cohort_data['cohort_month']).apply(lambda x: x.n)
    
    cohort_pivot = cohort_data.pivot(index='cohort_month', columns='period_number', values='n_users')
    cohort_size = cohort_pivot.iloc[:, 0]
    retention_matrix = cohort_pivot.divide(cohort_size, axis=0) * 100
    return retention_matrix

# 2. TWO-SAMPLE PROPORTION A/B TEST EVALUATION
def evaluate_ab_test(conversions_A, visitors_A, conversions_B, visitors_B, alpha=0.05):
    p_A = conversions_A / visitors_A
    p_B = conversions_B / visitors_B
    p_pooled = (conversions_A + conversions_B) / (visitors_A + visitors_B)
    
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/visitors_A + 1/visitors_B))
    z_score = (p_B - p_A) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
    
    relative_lift = ((p_B - p_A) / p_A) * 100
    return {
        "p_A": p_A, "p_B": p_B, "lift_pct": relative_lift,
        "z_stat": z_score, "p_value": p_value,
        "is_significant": p_value < alpha
    }
```

---

## 2. Advanced SQL for Analytics & Decision Science

### 1. Complex User Funnel Conversion Query
```sql
WITH UserFunnel AS (
    SELECT 
        user_id,
        MAX(CASE WHEN event_type = 'page_view' THEN 1 ELSE 0 END) AS step_1_view,
        MAX(CASE WHEN event_type = 'add_to_cart' THEN 1 ELSE 0 END) AS step_2_cart,
        MAX(CASE WHEN event_type = 'checkout_start' THEN 1 ELSE 0 END) AS step_3_checkout,
        MAX(CASE WHEN event_type = 'purchase_success' THEN 1 ELSE 0 END) AS step_4_purchase
    FROM EventLogs
    WHERE event_timestamp >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT 
    COUNT(user_id) AS total_visitors,
    SUM(step_1_view) AS step_1_views,
    SUM(step_2_cart) AS step_2_carts,
    SUM(step_3_checkout) AS step_3_checkouts,
    SUM(step_4_purchase) AS step_4_purchases,
    ROUND(100.0 * SUM(step_2_cart) / NULLIF(SUM(step_1_view), 0), 2) AS view_to_cart_pct,
    ROUND(100.0 * SUM(step_4_purchase) / NULLIF(SUM(step_3_checkout), 0), 2) AS checkout_to_purchase_pct,
    ROUND(100.0 * SUM(step_4_purchase) / COUNT(user_id), 2) AS overall_conversion_pct
FROM UserFunnel;
```

### 2. Rolling 7-Day Active Users & Churn Prediction Query
```sql
SELECT 
    date,
    COUNT(DISTINCT user_id) as daily_active_users,
    COUNT(DISTINCT user_id) - LAG(COUNT(DISTINCT user_id), 7) OVER (ORDER BY date) as wow_change_dau
FROM DailyUserActivity
GROUP BY date
ORDER BY date;
```

---

## 3. Power BI & Tableau Executive Dashboards

### Core Dashboard Design Standards:
1. **Summary KPI Cards (Top Banner)**: Revenue, Orders, Active Users, Conversion Rate, AOV with comparison against prior period ($\Delta$ MoM / YoY).
2. **Interactive Filters (Slicers)**: Date range, Platform (iOS, Android, Web), Customer Cohort (New vs Repeat), Geographic Tier.
3. **Primary Visuals**:
   - Time-series trend (Daily / Weekly metric movement).
   - Cohort retention heatmap (Month-0 to Month-12 decay).
   - Categorical breakdown (Pareto bar chart of top revenue drivers).

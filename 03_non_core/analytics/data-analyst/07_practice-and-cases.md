# 07. Data Analyst: Practice Projects & End-to-End Case Studies

> **Document Purpose**: Real-world analytical case studies with end-to-end SQL queries, Python scripts, statistical formulations, and executive recommendation summaries.

---

## Case 1: E-Commerce Funnel Drop-off & Cart Abandonment Diagnosis

### Business Scenario
An Indian D2C fashion retailer noticed a **14% drop in Monthly Gross Merchandise Value (GMV)** despite a 10% increase in marketing ad spend and top-of-funnel website traffic.

### 1. Funnel Metric Decomposition
$$	ext{GMV} = 	ext{Sessions} 	imes 	ext{Product View Rate} 	imes 	ext{Cart Add Rate} 	imes 	ext{Checkout Start Rate} 	imes 	ext{Payment Success Rate} 	imes 	ext{AOV}$$

```sql
WITH funnel_stages AS (
    SELECT 
        session_id,
        user_id,
        device_type,
        MAX(CASE WHEN event_name = 'home_view' THEN 1 ELSE 0 END) AS step_home,
        MAX(CASE WHEN event_name = 'product_view' THEN 1 ELSE 0 END) AS step_product,
        MAX(CASE WHEN event_name = 'add_to_cart' THEN 1 ELSE 0 END) AS step_cart,
        MAX(CASE WHEN event_name = 'checkout_start' THEN 1 ELSE 0 END) AS step_checkout,
        MAX(CASE WHEN event_name = 'payment_success' THEN 1 ELSE 0 END) AS step_payment
    FROM web_events
    WHERE event_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY session_id, user_id, device_type
)
SELECT 
    device_type,
    COUNT(session_id) AS total_sessions,
    ROUND(100.0 * SUM(step_product) / COUNT(session_id), 2) AS view_rate_pct,
    ROUND(100.0 * SUM(step_cart) / NULLIF(SUM(step_product), 0), 2) AS cart_add_rate_pct,
    ROUND(100.0 * SUM(step_checkout) / NULLIF(SUM(step_cart), 0), 2) AS checkout_rate_pct,
    ROUND(100.0 * SUM(step_payment) / NULLIF(SUM(step_checkout), 0), 2) AS payment_success_rate_pct
FROM funnel_stages
GROUP BY device_type;
```

### 2. Diagnosis & Finding
* *Finding*: `payment_success_rate_pct` on **iOS App** dropped from **84% to 51%** following an iOS app update on Oct 1st, while Desktop and Android remained stable at 86%.
* *Root Cause*: A new third-party UPI intent payment gateway SDK integration had an uncaught null-pointer crash on iOS 17 devices during OTP autofill.

### 3. Executive Action Plan
1. **Immediate Hotfix**: Roll back the iOS payment SDK to version 2.4.1 within 4 hours.
2. **Monitoring**: Establish real-time Datadog/CloudWatch alert if payment gateway error rate exceeds 3% across any platform.
3. **Revenue Recovery**: Send automated WhatsApp push notifications with a 5% discount voucher to all 12,400 affected iOS users who abandoned checkout over the last 48 hours.

---

## Case 2: Multi-Touch Marketing Attribution & CAC Optimization

### Business Scenario
A FinTech company spent **INR 4.5 Crore across 4 acquisition channels** (Google Search, Meta Ads, YouTube Influencers, Affiliate Networks) and acquired 60,000 new registered users. The CFO wants to know which channel generated the highest return on ad spend (ROAS) and where to allocate next quarter's budget.

### 1. Attribution Comparison Model (Python)
```python
import pandas as pd
import numpy as np

# Load touchpoint logs
df = pd.DataFrame({
    'user_id': [101, 101, 102, 103, 103, 103],
    'touchpoint_order': [1, 2, 1, 1, 2, 3],
    'channel': ['Google', 'Meta', 'YouTube', 'Meta', 'Google', 'Affiliate'],
    'converted': [0, 1, 1, 0, 0, 1],
    'revenue': [0, 1500, 2200, 0, 0, 1800]
})

# First-Touch vs Last-Touch vs Linear Attribution
conversions = df[df['converted'] == 1].copy()

# Linear Attribution: equal weight to all touchpoints in converting journey
journey_lengths = df.groupby('user_id')['touchpoint_order'].count().rename('total_touches')
df = df.merge(journey_lengths, on='user_id')
df['linear_weight'] = 1.0 / df['total_touches']
df['attributed_rev'] = df['revenue'] * df['linear_weight']

channel_summary = df.groupby('channel')['attributed_rev'].sum().reset_index()
print(channel_summary)
```

### 2. Strategic Takeaway
* YouTube Influencer campaigns had low *last-touch* conversions (8%) but appeared in **64% of high-LTV user journeys as the *first-touch* awareness driver**. Cutting YouTube spend would collapse top-of-funnel discovery.
* Rebalance budget: Shift 20% from underperforming affiliate networks to high-intent Google Search and top-of-funnel YouTube creators.

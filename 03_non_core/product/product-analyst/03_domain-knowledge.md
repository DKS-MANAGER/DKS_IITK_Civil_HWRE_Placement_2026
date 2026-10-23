# 03. Product Analytics: Telemetry, Funnels & Statistical Experimentation

> **Track**: Product Analytics & Growth Data Science  
> **Target Audience**: IIT Kanpur students preparing for Product Analyst, Growth Analyst, and Experimentation Data Scientist roles.  
> **Methodological Focus**: Event telemetry schemas, cohort retention dynamics, A/B testing statistical rigor, Sample Ratio Mismatch (SRM) diagnostics, and variance reduction (CUPED).

---

## 1. Event Telemetry & Instrumentation Architecture

A product analyst cannot analyze what engineering has not instrumented. Modern event-driven telemetry captures every user interaction as a structured JSON object streamed to data lakes (Segment, RudderStack, Snowplow, Kafka):

### Standard Event Schema Anatomy
```json
{
  "event_name": "checkout_completed",
  "user_id": "usr_94821a",
  "anonymous_id": "anon_f8231c",
  "timestamp": "2026-10-21T08:15:30.120Z",
  "session_id": "sess_81023",
  "platform": "android",
  "app_version": "4.12.0",
  "event_properties": {
    "cart_value_inr": 850.00,
    "item_count": 3,
    "payment_method": "UPI",
    "discount_code": "DIWALI50",
    "delivery_eta_minutes": 18
  },
  "user_properties": {
    "signup_date": "2025-06-15",
    "total_lifetime_orders": 14,
    "city": "Kanpur",
    "subscription_tier": "Gold"
  }
}
```

### Client-Side vs. Server-Side Tracking Trade-Offs
- **Client-Side (SDK in App/Browser)**: Captures rich UI context (scroll depth, mouse hover, button clicks, client viewport). *Vulnerability*: $15\%\text{--}30\%$ of events are lost due to ad-blockers, mobile network disconnections, or app crashes.
- **Server-Side (Backend API Webhooks)**: 100% reliable for revenue and state changes (order placed, payment charged, invoice generated). *Limitation*: No visibility into UI interactions preceding the server call.
- *Best Practice*: Track UI intent events client-side; track financial and account state transitions strictly server-side.

---

## 2. Funnel Analytics & Cohort Retention Modeling

### A. Conversion Funnel Mechanics
A conversion funnel measures user drop-off across a sequential user journey:
$$\text{Step Conversion Rate } (S_i \to S_{i+1}) = \frac{\text{Unique Users completing } S_{i+1}}{\text{Unique Users completing } S_i} \times 100\%$$
$$\text{End-to-End Funnel Conversion} = \frac{\text{Users Reaching Final Step}}{\text{Users Starting Initial Step}} \times 100\%$$

```text
[App Open] (100,000 users) ──► 100%
   │ Drop-off: 40%
   ▼
[Search / Browse Catalog] (60,000 users) ──► 60% step conversion
   │ Drop-off: 50%
   ▼
[Add to Cart] (30,000 users) ──► 50% step conversion
   │ Drop-off: 30%
   ▼
[Initiate Checkout] (21,000 users) ──► 70% step conversion
   │ Drop-off: 20%
   ▼
[Payment Completed] (16,800 users) ──► 80% step conversion (E2E Conversion = 16.8%)
```

### B. Cohort Retention & The "Smile" Curve
A cohort is a group of users who signed up or made their first transaction during the same time window (e.g., Week 1 Cohort).
- **Day $N$ Retention**: The percentage of users from the original cohort who return and engage on exactly Day $N$.
- **Unbounded / Rolling Retention**: The percentage of users who returned on Day $N$ *or any day after Day $N$*.
- **The Retention Plateau**: Healthy product-market fit is proven when the retention curve flattens out horizontally (e.g., stabilizing at $25\%$ by Day 30). If the curve decays continuously toward zero, the product has a "leaky bucket" problem where growth is unsustainable regardless of acquisition spend.

---

## 3. A/B Testing & Statistical Experimentation

### A. Sample Size Determination
Before launching an experiment, calculate the minimum sample size ($n$ per variant) required to detect a true effect:

$$n = \frac{2 \left( Z_{\alpha/2} + Z_{\beta} \right)^2 \cdot p (1 - p)}{\delta^2}$$

Where:
- $p$ = Baseline conversion rate (e.g., $10\% = 0.10$).
- $\delta$ = **Minimum Detectable Effect (MDE)** in absolute percentage points (e.g., wanting to detect an increase from $10\%$ to $10.5\% \implies \delta = 0.005$).
- $\alpha$ = **Significance Level / Type I Error** (false positive rate, typically $5\% \implies Z_{\alpha/2} = 1.960$).
- $\beta$ = **Type II Error** (false negative rate); Statistical Power is $1 - \beta$ (typically $80\% \implies Z_{\beta} = 0.842$).

### B. Sample Ratio Mismatch (SRM): The #1 Experiment Killer
If an experiment is configured for an equal $50:50$ split between Control and Treatment, but the logged user counts are $49,150$ Control vs. $50,850$ Treatment across 100,000 users:
Does this slight imbalance matter? **Yes!** Always run a **Chi-Square Goodness-of-Fit Test**:

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} = \frac{(49,150 - 50,000)^2}{50,000} + \frac{(50,850 - 50,000)^2}{50,000} = \frac{850^2}{50,000} + \frac{850^2}{50,000} = 14.45 + 14.45 = \mathbf{28.90}$$

For 1 degree of freedom, $\chi^2_{\text{critical}} = 3.841$ at $p = 0.05$. 
Here, $\chi^2 = 28.90 \implies p < 0.000001$.
**Conclusion**: Extreme Sample Ratio Mismatch! The assignment was biased (e.g., variant crashed on older Android versions, or redirects failed). **All conversion metrics from this test are completely invalid and must be discarded.**

### C. Variance Reduction via CUPED
Controlled-experiment Using Pre-Experiment Data (CUPED, Deng et al., Microsoft Research) leverages user behavior prior to the experiment to strip out background variance:
$$\hat{Y}_{\text{cuped}} = Y - \theta (X - \bar{X})$$
Where $X$ is the pre-experiment metric (e.g., pre-experiment revenue) and $\theta = \frac{\text{Cov}(X, Y)}{\text{Var}(X)}$.
CUPED shrinks the variance of metric $Y$ by a factor of $(1 - \rho^2)$, where $\rho$ is the correlation between pre- and post-metrics. If $\rho = 0.70$, variance is slashed by **$49\%$**, equivalent to doubling the effective sample size and cutting required test duration in half!

---

## 4. Metric Hierarchy: North Star & Guardrail Metrics

```text
                [ North Star Metric ]
             (e.g., Weekly Active Subscribers)
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
[ Growth Input Metric ]     [ Quality / Engagement Input ]
(New signups completing      (Average minutes spent consuming
 onboard flow in 24 hrs)      content per active user)
        │                           │
        └─────────────┬─────────────┘
                      ▼
             [ Guardrail Metrics ]
        (App Crash-Free Sessions > 99.8%)
        (API p95 Response Latency < 250ms)
        (Unsubscribe / Spam Complaint Rate < 0.2%)
```

---

## 5. Civil & HWRE Engineering Transferable Foundations

| Civil / HWRE Fluid Dynamics Principle | Product Analytics Analogy |
| :--- | :--- |
| **Piezometric Head Loss across Pipe Contractions** | User drop-off friction across checkout and onboarding funnels. |
| **Acoustic / Pressure Sensor Telemetry Networks** | Mobile and web telemetry event streaming pipelines (Segment, Kafka). |
| **Statistical Hydrology & Return Period Confidence Intervals** | Experimentation power calculations, A/B test confidence bounds, p-values. |
| **Sediment Washload vs. Bedload Partitioning** | Cohort segmentation: organic power users vs. paid mercenary users. |

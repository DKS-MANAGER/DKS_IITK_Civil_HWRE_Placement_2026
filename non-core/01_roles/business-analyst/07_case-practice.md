# 07. Business Analyst: Case Practice

> 4 end-to-end worked Business Analyst case studies with step-by-step problem deconstruction, issue trees, data hypotheses, and executive recommendations.

---

## Case 1: Sudden Drop in Monthly Active Users (MAU)

### Problem Prompt
*"A major consumer fintech mobile app observed a 15% drop in Monthly Active Users (MAU) over the last 30 days. You are tasked with diagnosing the root cause and recommending an action plan."*

### Step 1: Clarify & Define Metric
- **Definition of 'Active'**: A user who completed at least one transaction or viewed their portfolio during the month.
- **Scope**: Did total user base shrink (churn), or did existing users simply stop transacting?

### Step 2: MECE Segmentation Tree
```text
MAU Drop (-15%)
├── Segment by Platform
│   ├── iOS App (Normal, -1%)
│   ├── Web Portal (Normal, 0%)
│   └── Android App (-26% Sharp Decline) ← Primary Driver!
├── Segment by Geography
│   ├── Tier 1 Metros (-3%)
│   └── Tier 2/3 Cities (-22%)
└── Segment by User Cohort
    ├── Power Users (>10 tx/mo) (-2%)
    └── Casual Users (1-2 tx/mo) (-28%)
```

### Step 3: Deep-Dive Root Cause
- **Finding**: Android App version v4.2 released 3 weeks ago caused crash-on-launch on budget Android OS devices (common in Tier 2/3 cities).
- **Hypothesis Confirmed**: Technical app instability rather than competitive pressure or market churn.

### Step 4: Action Plan & Executive Recommendation
1. **Immediate**: Roll back Android release v4.2 to v4.1 within 4 hours.
2. **Short-Term**: Push an emergency hotfix v4.2.1 optimized for low-RAM Android chipsets.
3. **Re-engagement**: Send personalized SMS/Push notification with a 50 INR transaction incentive to re-activate dropped users.

---

## Case 2: Revenue Growth with Margin Compression

### Problem Prompt
*"A B2B SaaS company's Topline Revenue grew 20% YoY, but Gross Margin shrank from 75% to 58%. Diagnose the underlying drivers."*

### Step 1: Mathematical Decomposition
$$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}}$$

### Step 2: Issue Tree Breakdown
- **Revenue Mix Shift**:
  - Subscription Software Revenue: Grew 5% (Margin = 85%).
  - Custom On-Premise Implementation Services: Grew 80% (Margin = 25%).
  - *Diagnosis*: Sales team heavily discounted low-margin custom engineering services to close enterprise deals, diluting overall blended margin.
- **COGS Explosion**:
  - Cloud Infrastructure (AWS/GCP): Data storage egress fees jumped 45% due to unoptimized client database querying.

### Step 3: Recommendation
1. Implement commission caps for sales reps on non-software implementation services.
2. Introduce automated SQL query caching to reduce cloud server compute costs by ~30%.

---

## Case 3: Optimizing E-Commerce Checkout Drop-Off

### Problem Prompt
*"An e-commerce platform notices that 60% of users who add items to their cart drop off before making a payment. How do you design an analytical plan to reduce cart abandonment?"*

### Step 1: Funnel Drop-off Telemetry
- Stage 1: Add to Cart $\to$ View Cart (90% transition)
- Stage 2: View Cart $\to$ Shipping Address Selection (85% transition)
- Stage 3: Address Selection $\to$ Payment Gateway (42% transition) $\leftarrow$ **Critical Drop!**
- Stage 4: Payment Gateway $\to$ Order Placed (88% transition)

### Step 2: Root Cause Analysis
- Investigating Stage 3: Surprise delivery fees ($>150$ INR) revealed only at the payment transition step.
- Delivery lead times displayed as "$>7$ days" for 40% of non-metro locations.

### Step 3: Solutions
- Implement upfront dynamic shipping fee calculators directly on the product detail page.
- Test 1-click Express Checkout with pre-saved UPI handles.

---

## Case 4: Marketing Campaign Incrementality

### Problem Prompt
*"The marketing department ran a 50 Lakh INR festive discount campaign and claims it generated 3 Crore INR in sales. How do you verify whether these sales were truly incremental?"*

### Step 1: Incrementality vs. Cannibalization
- Did the campaign bring in new buyers, or did existing loyal customers who were going to buy anyway just take advantage of the discount early?

### Step 2: Analytical Design (Difference-in-Differences / Control Group)
- **Target Group ($T$)**: Geographies exposed to campaign ads and promo codes.
- **Control Group ($C$)**: Geographies held out from marketing exposure.
- **Incremental Lift Formula**:
$$\text{Incremental Revenue} = \left( \Delta \text{Sales}_T - \Delta \text{Sales}_C \right)$$
- If incremental profit generated $>$ Campaign Cost (50 Lakh INR), the campaign was ROI positive.

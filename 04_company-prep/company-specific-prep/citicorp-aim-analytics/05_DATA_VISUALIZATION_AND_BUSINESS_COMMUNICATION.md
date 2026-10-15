# 05. Data Visualization & Business Communication

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Directly required by the job description ("Presentation & Visualization: Knowledge of data visualization techniques to design effective presentations" and "Must be able to exchange information in a concise way as well as be sensitive to audience diversity").

---

## 1. Visual Encodings & Chart Selection Framework

Selecting the right visual format is an analytical decision, not a decorative one. Every chart must answer an explicit business question without misrepresenting the underlying distribution.

```
                         WHAT TYPE OF DATA & COMPARISON?
                                       │
         ┌───────────────────┬─────────┴─────────┬───────────────────┐
         ▼                   ▼                   ▼                   ▼
    TIME-SERIES         CATEGORICAL         DISTRIBUTION        RELATIONSHIP
    • Line Chart        • Bar Chart         • Histogram         • Scatter Plot
    • Stacked Area      • Column Chart      • Box Plot          • Bubble Chart
    (Trends over time)  (Comparisons)       (Spread & Outliers) (Correlation)
```

### Chart Selection Reference Matrix

| Business Analytical Question | Recommended Visualization | Visual Encodings Used | Why It Works / What to Avoid |
| :--- | :--- | :--- | :--- |
| **Trend over Time** (e.g. Monthly debit transaction volume over 24 months) | **Line Chart** | $X$-axis: Continuous Date, $Y$-axis: Volume | Shows rate of change and seasonality clearly. Avoid connecting categorical variables with lines. |
| **Discrete Category Comparison** (e.g. Total loan disbursements across 5 customer tiers) | **Horizontal Bar Chart** or **Vertical Column Chart** | Length / Position on common scale | Humans evaluate lengths on a common axis with high perceptual accuracy. Avoid Pie charts with $>4$ slices. |
| **Distribution & Spread** (e.g. Credit score distribution of approved applicants) | **Histogram** or **Box-and-Whisker Plot** | Histogram: Binned bars; Box Plot: Median, IQR, Whiskers, Outliers | Shows skewness, bimodality, and outliers that single summary statistics (mean) hide. |
| **Correlation & Joint Variation** (e.g. Customer income vs monthly card expenditure) | **Scatter Plot** | Points plotted along continuous $X$ and $Y$ axes | Instantly reveals linear or non-linear patterns, clusters, and extreme outliers. |
| **Part-to-Whole Breakdown** (e.g. Portfolio asset allocation) | **100% Stacked Bar Chart** or **Treemap** | Area or segmented length | Avoid standard pie charts, which force visual comparison of angles rather than length. |
| **Cohort Retention Heatmap** (e.g. Percentage of users active in Month 1, 2, ..., 12 by signup cohort) | **Heatmap with Tabular Values** | Rows: Signup Cohort, Columns: Lifecycle Month, Color: Retention % | Visualizes retention degradation across time and cohort quality simultaneously. |

---

## 2. Preventing Misleading Charts & Visualization Anti-Patterns

### 2.1 The Truncated $Y$-Axis Trap
* **The Anti-Pattern**: Starting a bar chart's $Y$-axis at $₹95,000$ instead of $0$ to show a small increase from $₹96,000$ to $₹98,000$. Visually, the bar height appears to have doubled ($+100\%$), while the actual change is only $+2.08\%$.
* **The Rule**: **Bar charts must ALWAYS start at zero** because the visual encoding is the *length* of the bar. (Line charts showing trends over narrow ranges may use non-zero baselines, provided the axis scale is prominently annotated).

### 2.2 The Dual-Axis Confusion
* **The Anti-Pattern**: Plotting two unrelated metrics on two different $Y$-axes with different scales (e.g., Left axis: Total Transaction Volume in millions; Right axis: Fraud Rate in fractions of a percent).
* **The Flaw**: Adjusting either scale shifts the visual intersection point of the lines arbitrarily, implying a false causal relationship or correlation where none exists.
* **The Solution**: Split into **two stacked subplots sharing the same $X$-axis**.

### 2.3 Pie Chart Abuse
* **The Anti-Pattern**: Using a 3D pie chart with 8 slices and subtle gradient colors.
* **The Flaw**: The human visual cortex is poor at estimating angles and area ratios. Slices in the foreground of a 3D perspective appear distorted and artificially larger than background slices.
* **The Solution**: Use a sorted horizontal bar chart with explicit data labels.

---

## 3. Executive Dashboard & KPI Design

In an enterprise banking community like Citi AIM, dashboards are designed for decision support, not data dumping.

### 3.1 The 3 Dashboard Tiers

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. STRATEGIC / EXECUTIVE DASHBOARD (C-Suite / Managing Directors)      │
│ • Focus: High-level portfolio health, revenue, loss rates, Net P&L.    │
│ • Cadence: Monthly / Quarterly. Action: Strategic capital allocation.  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 2. OPERATIONAL / TACTICAL DASHBOARD (Vice Presidents / Portfolio Leads)│
│ • Focus: Delinquency roll rates, conversion funnels, campaign ROI.     │
│ • Cadence: Daily / Weekly. Action: Tactical policy threshold tuning.   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│ 3. ANALYTICAL / DIAGNOSTIC DASHBOARD (Analytics Analysts / Data Sci)   │
│ • Focus: Feature drift, score distributions, model calibration curves. │
│ • Cadence: Live / Continuous. Action: Model retraining & bug fixes.    │
└────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Visual Hierarchy: The "Z-Pattern" Layout
* **Top Left (Primary Anchor)**: 3 to 4 prominent Single-Value Metric Cards (Headline KPIs: e.g., Total Spend, 30+ DPD Delinquency Rate, Portfolio Size, Conversion Rate).
* **Center / Upper Body**: Core trend visualization (Line chart showing trailing 12-month trajectory with benchmark target lines).
* **Lower Body**: Categorical breakdowns (Segment distributions, geographic performance, product mixes).
* **Color Usage**:
  * Use a restrained, neutral palette (greys, navy).
  * Reserve bold accent colors (Red, Emerald) exclusively for status alerts (exceeding risk thresholds or hitting milestones).

---

## 4. Executive Synthesis: The Minto Pyramid Principle

The job description explicitly notes: *"Must be able to exchange information in a concise way as well as be sensitive to audience diversity."*

Business stakeholders (Directors, Managing Directors) do not have time to sit through chronological recaps of your data-cleaning steps. Apply the **Pyramid Principle**: **Lead with the recommendation (Governing Thought), followed by structured arguments, supported by data.**

```
                     [1. GOVERNING RECOMMENDATION]
       "Tighten the automated credit line increase threshold for
        sub-720 credit tier to reduce projected charge-offs by $4.2M."
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [2. EVIDENCE A]           [2. EVIDENCE B]           [2. EVIDENCE C]
   Delinquency roll rates    Top 15% risk bucket       Operational policy
   in sub-720 tier surged    accounts for 72% of       simulation shows zero
   from 1.8% to 4.1% over    total credit losses       disruption to top 80%
   the trailing 2 quarters.  in this product segment.  profitable customers.
         │                         │                         │
         ▼                         ▼                         ▼
   [3. DATA METRIC]          [3. DATA METRIC]          [3. DATA METRIC]
   Cohort analysis of        KS decile table           Financial P&L model
   Q1 vs Q3 bookings.        distribution.             sensitivity test.
```

---

## 5. Communicating Uncertainty, Limitations & Trade-Offs

A hallmark of a mature analytics candidate is the ability to present **limitations and assumptions** transparently:

### How to Frame Analytical Findings
* **Poor**: *"Our model is 85% accurate and proves that increasing marketing spend will increase revenue by $10M."*
* **Professional & Defensible**: *"Based on our regression model calibrated on 18 months of retail card data, marketing spend exhibits a positive elasticity of $+0.24$ ($p < 0.01$). With $95\%$ confidence, a $\$2\text{M}$ campaign investment is projected to yield between $\$3.8\text{M}$ and $\$5.2\text{M}$ in incremental spend, assuming competitor promotional pricing remains within historical bounds. The primary risk to this projection is macro inflation, which was not observed in the training window."*

### The 4-Part Structure for Any Analytical Presentation
1. **The Core Finding**: What did the data reveal? (One clear declarative sentence).
2. **The Commercial Implication**: What does this mean for Citi's business? (Revenue, cost, or risk impact).
3. **The Recommended Action**: What concrete operational decision should the team make?
4. **The Governance / Caveat**: What are the underlying assumptions, risks, and next monitoring milestones?

---

## 6. Worked Communication Case: Before and After

### Scenario (`[PRACTICE CASE ASSUMPTION]`):
You analyzed a pilot A/B test of a personalized fee waiver on credit cards aimed at preventing customer churn.

#### The Ineffective (Data Dump) Explanation:
> *"We pulled the data from Teradata using SQL joins on 4 tables. We had 12,410 rows and cleaned out 140 nulls. We split it into 50/50 test and control. We ran a two-sample t-test on monthly transaction counts. The t-statistic was 2.34 and the p-value was 0.019, which is less than 0.05. The mean of group B was 14.2 and group A was 12.8. We also plotted a confusion matrix and looked at the boxplots. So the test worked."*
* **Why it fails**: Bores the stakeholder with routine mechanics, buries the business outcome, speaks in abstract statistical jargon, and provides zero commercial recommendation.

#### The Effective (Senior Analyst) Explanation:
> *"The personalized fee waiver pilot successfully reduced customer attrition while increasing net portfolio profitability. Across a 60-day test of 12,000 accounts, customers receiving the waiver exhibited a statistically significant 11% increase in monthly card transactions ($14.2\text{ vs } 12.8\text{ swipes/month}, p = 0.019$).*
>
> *Commercially, the incremental swipe fee revenue of $+\$18\text{ per card}$ fully offset the waived $\$10\text{ fee}$, resulting in an estimated net profit uplift of $+\$8\text{ per account}$.*
>
> *I recommend rolling out this targeted waiver program to all 80,000 accounts in the at-risk segment, projected to generate $\$640,000$ in annual net revenue, while monitoring early 30-day delinquency rates to verify credit risk remains unchanged."*
* **Why it succeeds**: Leads with the commercial verdict, presents the statistical evidence as verification, translates transaction counts into dollar impact ($P\&L$), and concludes with a clear, actionable operational rollout and risk monitoring plan.

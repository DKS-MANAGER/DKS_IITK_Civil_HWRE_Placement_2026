# Module 12 — Business Analytics, MECE Issue Trees & Structured Problem-Solving

In private equity analytics at Accordion (Merilytics), data without structured business reasoning is useless. Analysts are evaluated on their ability to decompose ambiguous business challenges into testable hypotheses and deliver decisive, actionable recommendations.

---

## 1. The 11-Step Analytical Problem-Solving Sequence

Every case interview, analytical deliverable, and client engagement follows this disciplined 11-step sequence:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE 11-STEP ANALYTICAL SOLVING SEQUENCE                         │
├────┬─────────────────────────────┬─────────────────────────────────────────────────────┤
│ 01 │ Understand Business Problem │ Clarify scope, industry context, and constraints.   │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 02 │ Identify Target Decision    │ What specific C-suite decision does this support?   │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 03 │ Define Measurable KPIs      │ Establish quantifiable financial/operational metrics│
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 04 │ Identify Required Data      │ Determine source tables, schemas, and timestamps.   │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 05 │ Assess Data Quality         │ Check completeness, missingness, duplicates, nulls. │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 06 │ Exploratory Data Analysis   │ Summary statistics, distributions, baseline trends. │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 07 │ Identify Drivers/Anomalies  │ Isolate outliers, segment variances, margin leaks.  │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 08 │ Test Hypotheses             │ Validate root causes using quantitative models.     │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 09 │ Develop Recommendations     │ Formulate 2–3 concrete operational action levers.   │
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 10 │ Validate & Sensitivity Check│ Stress-test recommendations under downside scenarios│
├────┼─────────────────────────────┼─────────────────────────────────────────────────────┤
│ 11 │ Communicate "So-What?"      │ Present executive recommendation using Pyramid rules│
└────┴─────────────────────────────┴─────────────────────────────────────────────────────┘
```

---

## 2. MECE Issue Trees in Private Equity Analytics

**MECE (Mutually Exclusive, Collectively Exhaustive)** ensures no gaps and no overlapping categories when diagnosing performance:

```
                                  ┌────────────────────────┐
                                  │    EBITDA Shortfall    │
                                  └───────────┬────────────┘
                                              │
                    ┌─────────────────────────┴─────────────────────────┐
                    ▼                                                   ▼
        ┌───────────────────────┐                           ┌───────────────────────┐
        │   Revenue Deficit     │                           │     Cost Inflation    │
        └───────────┬───────────┘                           └───────────┬───────────┘
                    │                                                   │
          ┌─────────┴─────────┐                               ┌─────────┴─────────┐
          ▼                   ▼                               ▼                   ▼
    ┌───────────┐       ┌───────────┐                   ┌───────────┐       ┌───────────┐
    │ Price /   │       │ Physical  │                   │   COGS    │       │   OPEX    │
    │ Realiz.   │       │ Volume    │                   │ Inflation │       │ Overruns  │
    └─────┬─────┘       └─────┬─────┘                   └─────┬─────┘       └─────┬─────┘
          │                   │                               │                   │
    ┌─────┴─────┐       ┌─────┴─────┐                   ┌─────┴─────┐       ┌─────┴─────┐
    │ • Baseline│       │ • Customer│                   │ • Raw Mat.│       │ • S&M     │
    │   List Prc│       │   Churn   │                   │ • Direct  │       │ • G&A     │
    │ • Discount│       │ • New Logo│                   │   Labor   │       │ • Logist. │
    │   Leakage │       │   Deficit │                   │ • Freight │       │ • Admin   │
    └───────────┘       └───────────┘                   └───────────┘       └───────────┘
```

---

## 3. Four Solved Business Analytics Caselets

### Caselet 1: Marketing Acquisition Channel Trade-off (Merilytics Classic)
- **Problem**: An e-commerce brand is evaluating two promotional campaigns to launch a new product ($P = \$100$, Gross Margin = 60%, variable COGS = \$40).
  - *Option A (Flat Fee)*: \$100,000 upfront. Reaches 1,000,000 impressions with an expected 2.0% purchase conversion rate.
  - *Option B (Revenue Share)*: \$20,000 upfront plus a 15% net revenue royalty. Reaches 600,000 impressions with an expected 4.0% purchase conversion rate.
- **Quantitative Solution**:
  1. *Option A Calculations*:
     $$\text{Units Sold} = 1,000,000 \times 2.0\% = 20,000 \text{ units}$$
     $$\text{Gross Revenue} = 20,000 \times \$100 = \$2,000,000$$
     $$\text{Gross Contribution (before fee)} = 20,000 \times \$60 = \$1,200,000$$
     $$\text{Net Profit}_A = \$1,200,000 - \$100,000 = \mathbf{\$1,100,000}$$
  2. *Option B Calculations*:
     $$\text{Units Sold} = 600,000 \times 4.0\% = 24,000 \text{ units}$$
     $$\text{Gross Revenue} = 24,000 \times \$100 = \$2,400,000$$
     $$\text{Royalty Paid} = \$2,400,000 \times 15\% = \$360,000$$
     $$\text{Unit Margin after Royalty} = \$60 - \$15 = \$45 \text{ / unit}$$
     $$\text{Total Contribution} = 24,000 \times \$45 = \$1,080,000$$
     $$\text{Net Profit}_B = \$1,080,000 - \$20,000 = \mathbf{\$1,060,000}$$
- **Strategic Recommendation & So-What**:
  - *Base Recommendation*: Choose **Option A**, which delivers **\$40,000 higher net profit** (\$1.10M vs \$1.06M).
  - *Downside Sensitivity*: Option B has a lower fixed downside (\$20k vs \$100k). If conversion rate drops below 1.5%, Option B protects cash flow. For a well-tested product, Option A captures higher upside.

---

### Caselet 2: Product Cannibalization & Margin Dilution
- **Problem**: A software company generates \$50M annual revenue selling a Legacy On-Premise license (\$10,000/license, 90% gross margin = \$9,000 margin/unit). It introduces a Cloud SaaS subscription (\$3,000/year, 80% gross margin = \$2,400 margin/unit). In Year 1, 2,000 SaaS licenses are sold. However, 60% of SaaS buyers were existing customers who would have otherwise renewed their on-premise license. Did the SaaS launch increase or destroy gross profit dollars?
- **Quantitative Solution**:
  1. *Cannibalized Customers*: $2,000 \times 60\% = 1,200 \text{ licenses}$.
  2. *Lost On-Premise Gross Profit*:
     $$\text{Lost GP} = 1,200 \times \$9,000 = -\$10,800,000$$
  3. *Gross Profit Gained from All SaaS Sales*:
     $$\text{SaaS GP} = 2,000 \times \$2,400 = +\$4,800,000$$
  4. *Year 1 Net Change in Gross Profit*:
     $$\Delta \text{GP} = \$4,800,000 - \$10,800,000 = \mathbf{-\$6,000,000 \text{ (Net Profit Loss)}}$$
- **Consulting "So-What"**: In Year 1, the cloud launch causes a \$6.0M profit dilution. However, SaaS revenue is recurring annual revenue. Over a 5-year customer lifetime:
  $$\text{5-Year SaaS Value} = 5 \times \$2,400 = \$12,000 > \$9,000 \text{ on-premise margin}$$
  *Actionable Recommendation*: Restructure sales compensation to incentivize multi-year upfront SaaS contracts with 15% price escalators to compress the crossover breakeven from Year 4 to Year 2.

---

### Caselet 3: Credit Cutoff Optimization in Subprime Auto Finance
- **Problem**: An automotive financing portco is experiencing rising loan defaults. The portfolio consists of 10,000 loans with an average principal of \$20,000, earning 12% annual interest (\$2,400 interest revenue/year). In default, the net loss after vehicle repossession is 50% of principal (\$10,000 loss).
- **Data by Credit Score Band**:
  ```
  Score Band   Loan Count   Annual Default Rate
  650+         5,000        1.0%
  600 - 649    3,000        4.0%
  550 - 599    1,500        12.0%
  < 550          500        30.0%
  ```
- **Quantitative Solution (Profit per Loan by Band)**:
  $$\text{Net Profit / Loan} = \text{Interest Revenue} - (\text{Default Rate} \times \text{Loss Given Default})$$
  - Band 650+: $\$2,400 - (0.01 \times \$10,000) = \$2,400 - \$100 = \mathbf{+\$2,300}$ (Profitable)
  - Band 600–649: $\$2,400 - (0.04 \times \$10,000) = \$2,400 - \$400 = \mathbf{+\$2,000}$ (Profitable)
  - Band 550–599: $\$2,400 - (0.12 \times \$10,000) = \$2,400 - \$1,200 = \mathbf{+\$1,200}$ (Profitable)
  - Band < 550: $\$2,400 - (0.30 \times \$10,000) = \$2,400 - \$3,000 = \mathbf{-\$600 \text{ (Value Destructive)}}$
- **Strategic Recommendation**: Immediately eliminate loans to applicants with credit scores < 550. This cuts 500 loans, reducing volume by 5%, but increases portfolio annual profit by:
  $$500 \times \$600 = \mathbf{+\$300,000 \text{ EBITDA Expansion}}$$

---

### Caselet 4: Retail Markdown & Price Elasticity
- **Problem**: A retail apparel portco holds 50,000 excess winter jackets costing \$30 each, originally priced at \$100. At \$100, weekly sales volume is 500 units. The merchandise manager proposes two markdown alternatives:
  - *Option 1*: 20% discount (Price = \$80), expected arc price elasticity $\epsilon = -2.5$.
  - *Option 2*: 40% discount (Price = \$60), expected arc price elasticity $\epsilon = -2.0$.
- **Quantitative Solution**:
  1. *Option 1 (20% Price Cut)*:
     $$\% \Delta Q = -2.5 \times (-20\%) = +50\% \rightarrow Q_1 = 500 \times 1.50 = 750 \text{ units/week}$$
     $$\text{Weekly Gross Profit} = 750 \times (\$80 - \$30) = 750 \times \$50 = \mathbf{\$37,500 / \text{week}}$$
  2. *Option 2 (40% Price Cut)*:
     $$\% \Delta Q = -2.0 \times (-40\%) = +80\% \rightarrow Q_2 = 500 \times 1.80 = 900 \text{ units/week}$$
     $$\text{Weekly Gross Profit} = 900 \times (\$60 - \$30) = 900 \times \$30 = \mathbf{\$27,000 / \text{week}}$$
- **Strategic Recommendation**: Select **Option 1 (\$80 price point)**. It delivers \$10,500 more profit per week (\$37.5k vs \$27.0k) and prevents severe brand margin erosion.


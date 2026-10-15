# Phase 1: Business and Quantitative Foundations

> **Module Code**: `L01`  
> **Target Audience**: Beginners mastering core quantitative reasoning, commercial arithmetic, and financial exhibit interpretation for consulting interviews.  
> **Prerequisites**: [`lessons/00_orientation_and_prerequisites.md`](00_orientation_and_prerequisites.md).  
> **Estimated Study Time**: 4 hours.

---

## 1. Fractions, Percentages & Percentage-Point Changes

In consulting interviews, calculations must be executed mentally or on paper with speed and absolute conceptual precision.

### 1.1 The Crucial Distinction: Percentage Growth vs. Percentage-Point Change
A common mistake among candidates is confusing **relative percentage change** with **absolute percentage-point change**.

- **Percentage-Point Change ($\text{pp}$)**:
  - *Definition*: The simple arithmetic difference between two percentage values.
  - *Formula*: $\Delta \text{pp} = \text{Percentage}_2 - \text{Percentage}_1$.
- **Relative Percentage Change ($\%$)**:
  - *Definition*: The rate of growth or contraction of the metric relative to its starting base.
  - *Formula*: $\% \Delta = \frac{\text{Percentage}_2 - \text{Percentage}_1}{\text{Percentage}_1} \times 100\%$.

#### Fully Worked Example:
> **Scenario**: In FY24, an industrial manufacturer’s EBITDA margin was **10.0%**. In FY25, following a factory automation initiative, the EBITDA margin rose to **15.0%**.
> 
> - **Percentage-Point Change**:
>   $$\Delta \text{pp} = 15.0\% - 10.0\% = \mathbf{+5.0\text{ percentage points (or +500 basis points)}}.$$
> - **Relative Percentage Growth in Margin**:
>   $$\% \Delta = \frac{15.0\% - 10.0\%}{10.0\%} \times 100\% = \frac{5.0}{10.0} \times 100\% = \mathbf{+50.0\%}.$$
> 
> *Executive Communication*: Never say *"our margin grew by 5%"*. If you say that to a CEO, they will assume margin grew from 10% to 10.5%! Say: *"Our margin expanded by 5 percentage points, representing a 50% relative improvement in operational profitability."*

---

### 1.2 Profit Margin vs. Markup
Beginners frequently conflate markup with gross margin, leading to disastrous pricing errors in case interviews.

| Metric | Base of Calculation | Mathematical Formula | Numerical Example ($C = \$80, P = \$100$) |
| :--- | :--- | :--- | :--- |
| **Gross Margin** | Based on **Selling Price** ($P$) | $\text{Margin} = \frac{P - C}{P} \times 100\%$ | $\frac{100 - 80}{100} = \mathbf{20.0\%}$ |
| **Markup** | Based on **Unit Cost** ($C$) | $\text{Markup} = \frac{P - C}{C} \times 100\%$ | $\frac{100 - 80}{80} = \mathbf{25.0\%}$ |

#### Conversion Mechanics:
$$\text{Margin} = \frac{\text{Markup}}{1 + \text{Markup}}, \quad \text{Markup} = \frac{\text{Margin}}{1 - \text{Margin}}$$
- A 50% markup corresponds to a 33.3% margin ($\frac{0.50}{1.50}$).
- A 20% margin corresponds to a 25% markup ($\frac{0.20}{0.80}$).

---

### 1.3 High-Frequency Mental Fraction Conversion Table
Commit these decimal and percentage equivalents to memory to eliminate arithmetic pauses in live interviews:

| Fraction | Decimal | Percentage | Mental Shortcut / Heuristic |
| :---: | :---: | :---: | :--- |
| $\frac{1}{2}$ | $0.500$ | $50.0\%$ | Half |
| $\frac{1}{3}$ | $0.333$ | $33.3\%$ | Divide by 3 |
| $\frac{1}{4}$ | $0.250$ | $25.0\%$ | Half of a half |
| $\frac{1}{5}$ | $0.200$ | $20.0\%$ | Double the number and shift decimal left |
| $\frac{1}{6}$ | $0.167$ | $16.7\%$ | Half of $\frac{1}{3}$ |
| $\frac{1}{7}$ | $0.143$ | $14.3\%$ | $14$ and double it: $28 \implies 0.1428$ |
| $\frac{1}{8}$ | $0.125$ | $12.5\%$ | Half of $\frac{1}{4}$ ($0.250 / 2$) |
| $\frac{1}{9}$ | $0.111$ | $11.1\%$ | Repeating ones |
| $\frac{1}{12}$ | $0.083$ | $8.33\%$ | Half of $\frac{1}{6}$ |
| $\frac{1}{16}$ | $0.0625$ | $6.25\%$ | Half of $\frac{1}{8}$ |

---

## 2. Growth Rates, Compounding & CAGR

### 2.1 The Compound Annual Growth Rate (CAGR) Formula
When a market or business expands over multiple years, it compounds.

$$\text{CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{\frac{1}{n}} - 1$$

Where:
- $V_{\text{initial}}$ = Value in base year ($t = 0$).
- $V_{\text{final}}$ = Value in ending year ($t = n$).
- $n$ = Number of elapsed compounding periods (years).

### 2.2 The Linear Approximation Fallacy and Its Limits
Candidates often approximate annual growth by calculating total percentage change and dividing by $n$:
$$\text{Linear Annualized Rate} \approx \frac{V_{\text{final}} - V_{\text{initial}}}{V_{\text{initial}} \times n}$$

#### When Does Linear Approximation Fail?
- **Small Growth ($< 25\%$ total over $n$ years)**: Linear approximation is acceptable.
  - *Example*: Value grows from 100 to 120 in 3 years ($+20\%$). Linear $= \frac{20\%}{3} = 6.67\%$. Exact CAGR $= (1.20)^{1/3} - 1 = 6.27\%$. Error is only $0.4$ percentage points.
- **Large Growth ($\ge 100\%$ total)**: Linear approximation fails completely.
  - *Example*: Value grows from $100$ to $400$ in 4 years ($+300\%$). Linear gives $\frac{300\%}{4} = 75.0\%$. Exact CAGR $= (4.00)^{1/4} - 1 = 41.4\%$. Linear overstates growth by **33.6 percentage points**!

### 2.3 The Rule of 72 for Mental Doubling
To estimate the doubling time of an investment or market:
$$\text{Doubling Time (years)} \approx \frac{72}{\text{Annual Growth Rate (\%)}} = \frac{72}{g}$$

#### Derivation from Natural Logarithms:
$$V_{\text{final}} = V_0 (1 + g)^n = 2 V_0 \implies (1 + g)^n = 2 \implies n \ln(1 + g) = \ln(2) \approx 0.693$$
For small $g$, $\ln(1 + g) \approx g$. Thus $n \approx \frac{0.693}{g}$. To make mental division easy with numerous factors ($2, 3, 4, 6, 8, 9, 12$), 72 is substituted for 69.3.

- If a market grows at **9% CAGR**, it doubles every $\frac{72}{9} = \mathbf{8\text{ years}}$.
- If a fintech startup doubles its revenue every **3 years**, its CAGR is $\frac{72}{3} = \mathbf{24\%}$.

---

## 3. Revenue Growth Decomposition: Price, Volume & Mix Effects

When client revenue increases or decreases, a consultant must never accept aggregate figures. You must isolate whether the change was driven by selling more units (**Volume**), changing prices (**Price**), or selling a different combination of products (**Mix**).

### 3.1 Mathematical Definitions
For an enterprise with $k$ products:
$$\text{Revenue } R = \sum_{i=1}^k P_i \times Q_i = Q_{\text{total}} \times \bar{P}$$
Where $Q_{\text{total}} = \sum Q_i$ and $\bar{P} = \sum (\text{Mix}_i \times P_i)$ is the weighted average price.

Between Year 1 and Year 2:
$$\Delta R = R_2 - R_1 = \Delta R_{\text{Volume}} + \Delta R_{\text{Price}} + \Delta R_{\text{Mix}}$$

1. **Volume Effect**: Change in total units sold, holding product mix and prices constant at Year 1 levels:
   $$\Delta R_{\text{Volume}} = (Q_2 - Q_1) \times \bar{P}_1$$
2. **Price Effect**: Change in unit prices, applied to actual Year 2 product volumes:
   $$\Delta R_{\text{Price}} = \sum_{i=1}^k Q_{i, 2} \times (P_{i, 2} - P_{i, 1})$$
3. **Mix Effect**: The impact of customers shifting toward higher-priced or lower-priced product tiers:
   $$\Delta R_{\text{Mix}} = Q_2 \times \sum_{i=1}^k P_{i, 1} \times (\text{Mix}_{i, 2} - \text{Mix}_{i, 1})$$

---

### 3.2 Fully Worked Business Case: The Brewery Mix Shift
> **Problem Statement**: A regional craft brewery sells two beers: *Standard Lager* and *Craft IPA*.
> 
> - **Year 1 Baseline**:
>   - Standard Lager: $800,000\text{ bottles}$ sold at $\$5.00$ ($R = \$4.0\text{M}$).
>   - Craft IPA: $200,000\text{ bottles}$ sold at $\$10.00$ ($R = \$2.0\text{M}$).
>   - Total Volume $Q_1 = 1,000,000\text{ bottles}$. Total Revenue $R_1 = \$6.0\text{M}$.
>   - Weighted Average Price $\bar{P}_1 = \frac{\$6.0\text{M}}{1.0\text{M}} = \$6.00/\text{bottle}$.
>   - Mix: 80% Standard, 20% Craft.
> 
> - **Year 2 Performance**:
>   - Standard Lager: Price raised to $\$6.00$, volume fell to $600,000\text{ bottles}$ ($R = \$3.6\text{M}$).
>   - Craft IPA: Price discounted to $\$9.00$, volume surged to $500,000\text{ bottles}$ ($R = \$4.5\text{M}$).
>   - Total Volume $Q_2 = 1,100,000\text{ bottles}$. Total Revenue $R_2 = \$8.1\text{M}$.
>   - Mix: 54.55% Standard ($600\text{k}/1.1\text{M}$), 45.45% Craft ($500\text{k}/1.1\text{M}$).
>   - Total Revenue Change $\Delta R = \$8.1\text{M} - \$6.0\text{M} = \mathbf{+\$2,100,000}$.
> 
> **Task**: Decompose the $\$2.1\text{M}$ revenue growth into Volume, Price, and Mix components.

#### Step-by-Step Numerical Decomposition:
1. **Volume Effect**:
   $$\Delta R_{\text{Volume}} = (1,100,000 - 1,000,000) \times \$6.00 = 100,000 \times \$6.00 = \mathbf{+\$600,000}$$
2. **Price Effect**:
   - Standard Lager: $600,000\text{ bottles} \times (\$6.00 - \$5.00) = +\$600,000$.
   - Craft IPA: $500,000\text{ bottles} \times (\$9.00 - \$10.00) = -\$500,000$.
   $$\Delta R_{\text{Price}} = +\$600,000 - \$500,000 = \mathbf{+\$100,000}$$
3. **Mix Effect**:
   - Total Year 2 volume if sold at Year 2 mix with Year 1 prices:
     $$(600,000 \times \$5.00) + (500,000 \times \$10.00) = \$3.0\text{M} + \$5.0\text{M} = \$8.0\text{M}$$
   - Total Year 2 volume if sold at Year 1 mix with Year 1 prices:
     $$1,100,000 \times \$6.00 = \$6.6\text{M}$$
   $$\Delta R_{\text{Mix}} = \$8.0\text{M} - \$6.6\text{M} = \mathbf{+\$1,400,000}$$

#### Verification & Business Interpretation:
$$\Delta R = \Delta R_{\text{Volume}} + \Delta R_{\text{Price}} + \Delta R_{\text{Mix}} = \$600,000 + \$100,000 + \$1,400,000 = \mathbf{\$2,100,000}$$
- **Takeaway**: Although total volume grew only 10% and net price realization added just $\$100\text{k}$, **66.7% of the brewery's revenue growth was driven by the Mix shift** (customers upgrading to higher-priced Craft IPA).

---

## 4. Cost Structure, Operating Leverage & Break-Even Analysis

### 4.1 Fixed Costs vs. Variable Costs
- **Fixed Costs ($FC$)**: Expenses that remain constant regardless of the volume of goods produced (within relevant capacity limits): factory lease rent, corporate insurance, software enterprise licenses, administrative executive salaries, annual straight-line depreciation.
- **Variable Costs ($VC$)**: Expenses that vary directly in proportion to the number of units produced: raw steel, electronic chips, packaging boxes, direct assembly hourly wages, shipping courier fees.
- **Total Cost Function**: $\text{Total Cost} (TC) = FC + (VC_{\text{unit}} \times Q)$.

---

### 4.2 Contribution Margin & Break-Even Volume
- **Unit Contribution Margin ($CM$)**:
  $$CM = P - VC_{\text{unit}}$$
  *Meaning*: The dollar amount each sold unit contributes toward covering fixed overheads. Once fixed costs are covered, every subsequent unit of contribution margin flows directly into operating profit!
- **Contribution Margin Ratio ($CM\%$)**:
  $$CM\% = \frac{P - VC_{\text{unit}}}{P} = \frac{CM}{P}$$
- **Break-Even Volume ($Q^*$ in units)**:
  $$Q^* = \frac{FC}{CM} = \frac{FC}{P - VC_{\text{unit}}}$$
- **Break-Even Revenue ($R^*$)**:
  $$R^* = \frac{FC}{CM\%}$$

---

### 4.3 Operating Leverage: Why High Fixed Costs Amplify Risk
**Degree of Operating Leverage (DOL)** measures how sensitive operating profit (EBIT) is to changes in revenue:
$$\text{DOL} = \frac{\% \Delta \text{EBIT}}{\% \Delta \text{Revenue}} = \frac{Q \times (P - VC_{\text{unit}})}{\text{EBIT}} = \frac{\text{Total Contribution Margin}}{\text{Operating Profit}}$$

#### Strategic Implication:
- **High Operating Leverage (Airlines, Telecom, Steel Mills)**: High fixed infrastructure, low marginal cost per additional user.
  - When revenue grows by 10%, operating profit surges by 40%!
  - But when revenue drops by 10%, profits collapse into massive cash burn.
- **Low Operating Leverage (Consulting, Retail Trading, IT Staffing)**: Mostly variable labor costs. Profit margins remain stable even if top-line revenue contracts.

---

## 5. Capacity, Bottlenecks & Little's Law

### 5.1 Little's Law in Service and Manufacturing Systems
Formulated by MIT professor John Little, this theorem governs any queuing or production line in steady state:

$$L = \lambda \times W$$

Where:
- $L$ = **Work-in-Process (WIP) or Inventory**: Average number of units, customer tickets, or parts inside the system.
- $\lambda$ = **Throughput Rate**: Average arrival/completion rate of units per time period.
- $W$ = **Cycle Time / Lead Time**: Average time a single unit spends inside the system from entry to exit.

#### Application Example:
> A logistics warehouse ships **40 pallets per day** ($\lambda = 40$). On average, a pallet spends **15 days** sitting on warehouse shelves before being loaded onto an outbound truck ($W = 15$).
> 
> What is the average inventory sitting in the warehouse?
> $$L = \lambda \times W = 40\text{ pallets/day} \times 15\text{ days} = \mathbf{600\text{ pallets in stock}}.$$
> If the operations manager wants to compress customer order lead time from 15 days to 6 days while maintaining 40 pallets/day throughput, WIP inventory must be reduced to $40 \times 6 = 240\text{ pallets}$.

---

## 6. Unit Economics: CAC, LTV & Payback

### 6.1 Customer Acquisition Cost (CAC)
$$\text{CAC} = \frac{\text{Total Sales \& Marketing Spend over Period}}{\text{Total New Customers Acquired over Period}}$$

### 6.2 Customer Lifetime Value (LTV)
For a recurring subscription customer base:
$$\text{Average Customer Lifespan} = \frac{1}{\text{Annual Churn Rate}}$$
$$\text{LTV} = \frac{\text{Annual Gross Contribution per Customer}}{\text{Annual Churn Rate}} = \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Churn Rate}}$$

When accounting for cost of capital (Discount Rate $d$):
$$\text{LTV}_{\text{discounted}} = \frac{\text{Annual Gross Contribution} \times (1 - \text{Churn})}{d + \text{Churn}}$$

### 6.3 Healthy Unit Economics Benchmarks
1. **$\text{LTV / CAC Ratio} \ge 3.0\times$**:
   - If $< 1.0\times$: The company is losing cash on every acquired customer.
   - If $1.0\times - 2.5\times$: The business will struggle to cover fixed corporate SG&A and R&D.
   - If $> 5.0\times$: The company is under-investing in marketing; competitors will capture the market.
2. **CAC Payback Period $\le 12\text{ months}$**:
   $$\text{Payback Period (months)} = \frac{\text{CAC}}{\text{Monthly Gross Contribution per User}}$$

---

## 7. How to Read Business Exhibits and Waterfalls

During case interviews, partners frequently hand candidates stylized charts. Follow the **3-Step Exhibit Decoupling Protocol**:

```text
Step 1: Read the Axes & Legends ──► Confirm units ($ vs units, Lakhs vs Crores), timeframes, and segments.
Step 2: Identify the Major Delta ──► Locate the single largest spike, collapse, or inflection point.
Step 3: State the "So What?"     ──► Formulate a hypothesis that links the finding to client profitability.
```

### 7.1 Reading a Profitability Waterfall Exhibit
A waterfall chart displays how a starting baseline is bridged to an ending total through positive additions and negative deductions:

```text
[ FY24 EBITDA: $100M ]
       │
       ├── (+) $20M Price Increases
       ├── (+) $15M New Store Openings
       ├── (-) $30M Raw Material Inflation
       └── (-) $25M Digital Advertising Spend
       │
[ FY25 EBITDA: $80M ]
```

- **Candidate Dialogue**: *"Looking at this EBITDA bridge, top-line revenue expansion through pricing (+$20M) and new stores (+$15M) generated $35M in positive earnings. However, this was entirely erased by $55M in cost escalation, dominated by raw material inflation (-$30M). I hypothesize that our procurement team failed to lock in forward supply contracts. Shall we investigate raw material procurement?"*

---

## 8. Guided & Independent Quantitative Exercises

### Exercise 1 (Guided): Break-Even Shift under Tariff Inflation
- **Prompt**: An Indian consumer electronics assembler sells tablets for ₹15,000. Variable component cost is ₹9,000 per tablet. Monthly fixed factory overhead is ₹1.8 Crore. The government levies a 10% customs import duty on foreign chipsets, raising variable costs by ₹1,000 per tablet.
  1. What was the initial monthly break-even unit volume?
  2. How many additional tablets must be sold monthly to maintain break-even if the retail price cannot be raised?

#### Step-by-Step Solution:
1. **Initial Unit Contribution**:
   $$CM_1 = 15,000 - 9,000 = \mathbf{₹6,000/\text{tablet}}$$
   $$\text{Initial Break-Even } Q_1^* = \frac{₹1,80,00,000}{₹6,000} = \mathbf{3,000\text{ tablets/month}}$$
2. **New Unit Contribution post-tariff**:
   $$CM_2 = 15,000 - (9,000 + 1,000) = 15,000 - 10,000 = \mathbf{₹5,000/\text{tablet}}$$
   $$\text{New Break-Even } Q_2^* = \frac{₹1,80,00,000}{₹5,000} = \mathbf{3,600\text{ tablets/month}}$$
3. **Additional Tablets Required**:
   $$\Delta Q^* = 3,600 - 3,000 = \mathbf{+600\text{ tablets/month (+20.0\% increase)}}.$$

---

### Exercise 2 (Independent): Price Elasticity and Net Profitability
- **Prompt**: A commercial gym chain charges ₹2,000/month and has 10,000 active members. Marginal cost per member workout (water, towels, cleaning) is ₹200/month. Fixed club rent and staff salaries are ₹1.2 Crore/month. The club raises monthly membership fees by 15% to ₹2,300. Price elasticity of demand is $-0.8$.
  - Calculate new member count, new monthly revenue, and change in monthly operating profit.
  *(Attempt this problem on paper before reviewing the solution in [`practice/question_bank_solutions.md`](../practice/question_bank_solutions.md) under Section 8).*

---

## 9. Next Step in Course Progression
Now that quantitative foundations are solid, proceed to:
👉 [`lessons/02_structured_problem_solving.md`](02_structured_problem_solving.md) to master hypothesis formulation, MECE logic, and custom issue tree construction.

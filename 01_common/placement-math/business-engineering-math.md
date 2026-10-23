# Placement Math — Business & Engineering Quantitative Reasoning

> **Scope**: Business arithmetic, financial ratios, break-even analysis, unit economics, CAGR, Fermi estimation, guesstimates, decision trees, and spreadsheet data modeling.  
> **Target Audience**: Postgraduate engineers (Civil/HWRE, Mechanical, Energy, Electrical) transitioning to Management Consulting, Product Management, Corporate Strategy, Energy Operations, and Business Analytics roles.  
> **Core Differentiation**:  
> * **Aptitude (`01_common/aptitude/`)** = Speed math, competitive exam patterns (Time & Work, Pipes, Syllogisms, Permutations).  
> * **Placement Math (`01_common/placement-math/`)** = Real-world business, infrastructure, and industrial quantitative models used in consulting case interviews, technical problem-solving discussions, and operational management.

---

## 1. Corporate Financial & Profitability Metrics

### 1.1 The Income Statement Waterfall & Margin Architecture

```text
Gross Revenue (Top Line)
   │
   ▼  (-) Returns, Trade Discounts, Allowances
Net Revenue
   │
   ▼  (-) Cost of Goods Sold (COGS: Direct Raw Materials, Labor, Direct Energy)
Gross Profit  ──►  Gross Margin % = (Gross Profit / Net Revenue) × 100
   │
   ▼  (-) Operating Expenses (OpEx: SG&A, R&D, Logistics, Depot Overheads)
Operating Profit / EBITDA  ──►  EBITDA Margin % = (EBITDA / Net Revenue) × 100
   │
   ▼  (-) Depreciation & Amortization (D&A)
EBIT (Operating Income)  ──►  Operating Margin % = (EBIT / Net Revenue) × 100
   │
   ▼  (-) Interest Expenses (Net Financing Cost)
EBT (Earnings Before Taxes)
   │
   ▼  (-) Corporate Income Tax
Net Income (Bottom Line / PAT)  ──►  Net Margin % = (Net Income / Net Revenue) × 100
```

### 1.2 Mathematical Formulations

1. **Gross Margin**:
   $$\text{Gross Margin} = \frac{\text{Net Revenue} - \text{COGS}}{\text{Net Revenue}} \times 100\%$$
   *Diagnostic Meaning*: Measures direct production efficiency and pricing power. A declining gross margin indicates raw material inflation, labor cost escalation, or pricing erosion.

2. **Operating Margin (EBIT Margin)**:
   $$\text{EBIT Margin} = \frac{\text{EBIT}}{\text{Net Revenue}} \times 100\%$$
   *Diagnostic Meaning*: Evaluates operating model efficiency. If Gross Margin is healthy ($>50\%$) but Operating Margin is thin ($<8\%$), the organization suffers from bloated overheads, excessive marketing, or administrative inefficiency.

3. **Net Margin (Profit After Tax Margin)**:
   $$\text{Net Margin} = \frac{\text{PAT}}{\text{Net Revenue}} \times 100\%$$
   *Diagnostic Meaning*: The final residual margin accruing to shareholders after financing leverage and corporate tax obligations.

---

## 2. Break-Even Analysis, Contribution Economics & Operating Leverage

### 2.1 The Contribution Framework

$$\text{Contribution Margin (per unit)} = P - V$$
$$\text{Contribution Margin Ratio (CMR)} = \frac{P - V}{P} = 1 - \frac{V}{P}$$

Where:
- $P = \text{Selling Price per unit}$
- $V = \text{Variable Cost per unit}$
- $F = \text{Total Fixed Operating Costs}$

### 2.2 Break-Even Volume and Revenue

$$\text{Break-Even Volume } (Q_{\text{BEP}}) = \frac{F}{P - V} = \frac{F}{\text{Unit CM}}$$
$$\text{Break-Even Revenue } (R_{\text{BEP}}) = Q_{\text{BEP}} \times P = \frac{F}{\text{CMR}}$$

$$\text{Target Profit Output } (Q_{\text{Target}}) = \frac{F + \text{Target Operating Profit}}{P - V}$$

### 2.3 Degree of Operating Leverage (DOL)

Operating leverage measures how sensitive operating profit (EBIT) is to changes in sales volume:

$$\text{DOL} = \frac{\% \Delta \text{EBIT}}{\% \Delta \text{Revenue}} = \frac{Q(P - V)}{Q(P - V) - F} = \frac{\text{Total Contribution Margin}}{\text{EBIT}}$$

*Strategic Interpretation*:
- **High Fixed Costs (High DOL)**: Common in capital-intensive industries (infrastructure EPC, chemical refineries, cloud data centers). A 10% increase in sales can yield a 30% surge in operating profit, but a 10% drop in revenue can wipe out profitability.
- **Low Fixed Costs (Low DOL)**: Common in service consultancies and pure aggregators. Profitability fluctuates smoothly with revenue.

---

## 3. Growth Dynamics, Compounding & Time Value of Money

### 3.1 Compound Annual Growth Rate (CAGR)

When an engineering or corporate metric grows non-linearly across $n$ years:

$$\text{CAGR} = \left(\frac{\text{Final Value}}{\text{Initial Value}}\right)^{\frac{1}{n}} - 1$$

$$\text{Final Value} = \text{Initial Value} \times (1 + \text{CAGR})^n$$

### 3.2 The Rule of 72 & Mental Shortcuts

For mental math in placement interviews, the time $t$ required for an investment or market metric to double at annual percentage rate $r\%$ is:

$$t_{\text{double}} \approx \frac{72}{r}$$

| Annual Growth Rate ($r\%$) | Exact Doubling Time ($\ln 2 / \ln(1+r)$) | Rule of 72 Approximation | Mental Calculation Usage |
| :---: | :---: | :---: | :--- |
| **6%** | $11.90\text{ years}$ | $\frac{72}{6} = 12.0\text{ years}$ | Standard utility/infrastructure expansion |
| **8%** | $9.01\text{ years}$ | $\frac{72}{8} = 9.0\text{ years}$ | Emerging market GDP growth baseline |
| **12%** | $6.12\text{ years}$ | $\frac{72}{12} = 6.0\text{ years}$ | Mid-market corporate revenue target |
| **18%** | $4.19\text{ years}$ | $\frac{72}{18} = 4.0\text{ years}$ | Rapid tech / renewable power adoption |
| **24%** | $3.22\text{ years}$ | $\frac{72}{24} = 3.0\text{ years}$ | High-growth digital software segment |

### 3.3 Rule of 115 (Tripling Time) & Rule of 144 (Quadrupling Time)
- **Tripling Time**: $t_{\text{triple}} \approx \frac{115}{r}$
- **Quadrupling Time**: $t_{\text{quadruple}} \approx \frac{144}{r} = 2 \times t_{\text{double}}$

---

## 4. Digital, Industrial & Subscription Unit Economics

In modern technology, analytics, and equipment-as-a-service (EaaS) placement evaluations:

### 4.1 Core Unit Metrics

| Metric | Mathematical Formula | Benchmark Standard | Strategic Diagnostic |
| :--- | :--- | :---: | :--- |
| **Customer Acquisition Cost (CAC)** | $\frac{\text{Total S\&M Costs}}{\text{New Customers Acquired}}$ | Payback $< 12\text{ months}$ | Measures sales efficiency and marketing funnel conversion. |
| **Customer Lifetime Value (LTV)** | $\frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Customer Churn Rate}}$ | $\text{LTV} / \text{CAC} \ge 3.0\times$ | Total net profit generated across the customer's lifespan. |
| **Customer Churn Rate ($C_r$)** | $\frac{\text{Customers Lost in Period}}{\text{Customers at Start of Period}}$ | $< 5\%\text{ per year (B2B)}$ | Indicates retention health, product-market fit, and satisfaction. |
| **Average Revenue Per User (ARPU)** | $\frac{\text{Total Revenue}}{\text{Active Users}}$ | Industry-dependent | Base monetization capability. |
| **CAC Payback Period** | $\frac{\text{CAC}}{\text{Monthly Gross Contribution per User}}$ | $< 9\text{--}12\text{ months}$ | Time required to recoup the upfront sales cash outlay. |

---

## 5. Fermi Estimation & Guesstimate Engineering

Placement interviews for analytics, strategy, consulting, and operations routinely assess **guesstimate ability**—estimating an unknown macro or micro quantity under incomplete information.

### 5.1 The 5-Step Fermi Decomposition Framework

```text
[Step 1: Clarify Scope & Boundary Constraints]
       │
       ▼
[Step 2: Construct MECE Mathematical Decomposition Equation]
       │
       ▼
[Step 3: Establish Grounded Demographic & Physical Assumptions]
       │
       ▼
[Step 4: Execute High-Precision Order-of-Magnitude Arithmetic]
       │
       ▼
[Step 5: Sanity Check, Sensitivity Analysis & Boundary Bounds]
```

### 5.2 Key Ground Truth Population & Economic Benchmarks (India & Global)

To execute guesstimates with confidence, memorize these factual anchors:

- **Population of India**: $\approx 1.40\text{ Billion } (140\text{ Crore})$
- **Average Household Size**: $\approx 4.0\text{ persons}$
- **Total Households in India**: $\approx \frac{1.40\text{B}}{4} = 350\text{ Million } (35\text{ Crore})$
- **Urban vs. Rural Distribution**:
  - Urban: $\approx 35\% \implies 120\text{M households } (490\text{M people})$
  - Rural: $\approx 65\% \implies 230\text{M households } (910\text{M people})$
- **Income Segmentation (Urban Households)**:
  - Upper Class ($> \text{INR 15 Lakh/yr}$): $\approx 10\% \implies 12\text{ Million households}$
  - Middle Class ($\text{INR 5--15 Lakh/yr}$): $\approx 40\% \implies 48\text{ Million households}$
  - Lower Middle / Working Class ($< \text{INR 5 Lakh/yr}$): $\approx 50\% \implies 60\text{ Million households}$
- **Age Distribution in India**:
  - Children & Youth ($0\text{--}18\text{ yrs}$): $\approx 30\%$
  - Young Professionals & Working Adults ($19\text{--}40\text{ yrs}$): $\approx 35\%$
  - Mature Adults ($41\text{--}60\text{ yrs}$): $\approx 25\%$
  - Senior Citizens ($>60\text{ yrs}$): $\approx 10\%$
- **Area of India**: $\approx 3.287\text{ Million km}^2$
- **Total Operational Vehicles in India**:
  - Two-wheelers: $\approx 220\text{ Million}$
  - Four-wheelers (Passenger Cars): $\approx 35\text{--}40\text{ Million}$
  - Commercial Vehicles: $\approx 12\text{ Million}$

---

## 6. Worked Placement Math Problems (With Detailed Solutions)

### Problem 1: Infrastructure Asset Break-Even & Utilization

**Scenario**: An engineering fleet rental company acquires 25 heavy hydraulic excavators at a total capital cost of INR 15 Crore.
- Fixed monthly overhead (depot maintenance, interest, administrative salaries) = INR 45 Lakhs.
- Daily rental rate charged to contractors = INR 22,000 per machine-day.
- Variable operating cost (operator salary, lubrication, wear allowance, routine servicing) = INR 7,000 per machine-day.
- Machines operate 26 billing days per month.

**Questions**:
1. What is the monthly break-even machine-days volume?
2. What is the fleet utilization rate required to achieve break-even?
3. If the company targets an operating profit (EBIT) of INR 18 Lakhs per month, how many machine-days must be billed?

**Solution**:
1. **Contribution Margin per Machine-Day**:
   $$\text{CM} = \text{Rental Price} - \text{Variable Cost} = 22,000 - 7,000 = \text{INR } 15,000\text{ / machine-day}$$
2. **Break-Even Volume**:
   $$Q_{\text{BEP}} = \frac{\text{Fixed Overhead}}{\text{Unit CM}} = \frac{\text{INR } 4,500,000}{\text{INR } 15,000} = \mathbf{300\text{ machine-days per month}}$$
3. **Fleet Capacity and Utilization**:
   $$\text{Maximum Available Monthly Machine-Days} = 25\text{ machines} \times 26\text{ days} = 650\text{ machine-days}$$
   $$\text{Break-Even Utilization Rate} = \frac{300}{650} \times 100\% = \mathbf{46.15\%}$$
4. **Target Profit Volume**:
   $$Q_{\text{Target}} = \frac{\text{Fixed Overhead} + \text{Target Profit}}{\text{Unit CM}} = \frac{4,500,000 + 1,800,000}{15,000} = \frac{6,300,000}{15,000} = \mathbf{420\text{ machine-days}}$$
   $$\text{Required Utilization} = \frac{420}{650} \times 100\% = \mathbf{64.62\%}$$

---

### Problem 2: Guesstimate — Daily Aviation Turbine Fuel (ATF) Consumption at Delhi Airport (IGI)

**Objective**: Estimate the total daily fuel consumption (in liters or metric tonnes) for passenger flights departing from Indira Gandhi International Airport (DEL).

**Step 1: Clarification & Boundaries**
- Scope: Commercial scheduled passenger aircraft departures over a 24-hour cycle.
- Exclusions: Military flights, cargo-only freighters, non-scheduled private charters.

**Step 2: Formula Breakdown**
$$\text{Daily Fuel} = \text{Daily Departures} \times \sum_{i} (\% \text{ Aircraft Type}_i \times \text{Avg Flight Duration}_i \times \text{Fuel Burn Rate}_i)$$

**Step 3: Estimating Daily Departures**
- IGI Airport operates 3 active commercial runways.
- Operational window: 24 hours/day. Peak hours (16 hours) and non-peak night hours (8 hours).
- Runway capacity: $\approx 1\text{ flight movement per runway every } 2\text{ minutes} = 30\text{ movements/runway/hour}$.
- Total movements (takeoffs + landings) across 3 runways:
  - Peak ($16\text{ hrs}$): $3\text{ runways} \times 25\text{ flights/hr} \times 16\text{ hrs} = 1,200\text{ movements}$.
  - Non-peak ($8\text{ hrs}$): $3\text{ runways} \times 12\text{ flights/hr} \times 8\text{ hrs} = 288\text{ movements}$.
  - Total movements $\approx 1,500\text{ flights/day}$.
- Total departures $\approx 50\% = \mathbf{750\text{ departures/day}}$.

**Step 4: Aircraft Categorization & Fuel Consumption**
- **Narrow-Body Domestic (Airbus A320 / Boeing 737)**:
  - Share of departures: $\approx 80\% = 600\text{ flights}$.
  - Average domestic flight duration: $\approx 2.0\text{ hours}$ (e.g., Delhi to Mumbai, Bengaluru, Kolkata).
  - Fuel burn rate: $\approx 2,400\text{ liters/hour}$.
  - Fuel consumed per flight: $2.0 \times 2,400 = 4,800\text{ liters}$.
  - Subtotal $= 600 \times 4,800 = \mathbf{2,880,000\text{ liters}}$.
- **Wide-Body Medium/Long-Haul (Boeing 777, 787 / Airbus A350)**:
  - Share of departures: $\approx 20\% = 150\text{ flights}$.
  - Average international flight duration departing DEL: $\approx 6.0\text{ hours}$ (Europe, Middle East, SE Asia).
  - Fuel burn rate: $\approx 6,000\text{ liters/hour}$.
  - Fuel consumed per flight: $6.0 \times 6,000 = 36,000\text{ liters}$.
  - Subtotal $= 150 \times 36,000 = \mathbf{5,400,000\text{ liters}}$.

**Step 5: Total Consumption & Sanity Check**
$$\text{Total Daily Fuel} = 2,880,000 + 5,400,000 = \mathbf{8,280,000\text{ liters/day}} \approx \mathbf{8.3\text{ Million Liters/day}}$$
- In metric tonnes (Jet A-1 fuel density $\rho \approx 0.80\text{ kg/L}$):
  $$\text{Mass} = 8.3 \times 10^6\text{ L} \times 0.80\text{ kg/L} = 6.64 \times 10^6\text{ kg} \approx \mathbf{6,640\text{ Metric Tonnes/day}}$$
- **Sanity Check**: Major global hub airports (e.g., Heathrow, Dubai, Singapore) consume between 6,000 and 10,000 metric tonnes of jet fuel daily. 6,640 MT aligns with verified operational benchmarks.

---

### Problem 3: Multi-Criteria Capital Decision Matrix & Expected Monetary Value (EMV)

**Scenario**: An industrial utility provider must decide between two water treatment technological upgrades for a chemical refinery:
- **Option A (Membrane Bio-Reactor - MBR)**: Upfront CapEx = INR 8.0 Crore. Annual OpEx = INR 60 Lakhs.
- **Option B (Sequential Batch Reactor - SBR)**: Upfront CapEx = INR 5.0 Crore. Annual OpEx = INR 1.10 Crore.
- Operating horizon = 10 years.
- Future environmental regulation risk:
  - There is a $40\%$ probability that state pollution boards tighten effluent limits within 3 years, necessitating an additional retrofit of INR 4.0 Crore for Option B (Option A already complies with strict future norms).
  - Discount rate for net present value = $10\%$ per annum.

**Formulas**:
$$\text{NPV} = -\text{CapEx} - \sum_{t=1}^{n} \frac{\text{OpEx}_t}{(1 + r)^t} - \text{PV}(\text{Risk Penalty})$$
$$\text{Present Value Annuity Factor } (\text{PVAF}_{10\%, 10}) = \frac{1 - (1+0.10)^{-10}}{0.10} = \frac{1 - 0.3855}{0.10} = 6.145$$

**Evaluation**:
1. **Option A (MBR)**:
   - CapEx = INR 8.0 Cr
   - PV of OpEx over 10 years = $0.60\text{ Cr} \times 6.145 = \text{INR } 3.687\text{ Cr}$
   - Risk Penalty = 0
   - Total Expected Cost (PV) = $8.0 + 3.687 = \mathbf{INR 11.687\text{ Crore}}$

2. **Option B (SBR)**:
   - CapEx = INR 5.0 Cr
   - PV of OpEx over 10 years = $1.10\text{ Cr} \times 6.145 = \text{INR } 6.760\text{ Cr}$
   - Risk Penalty: $40\%$ probability of INR 4.0 Cr retrofit in Year 3:
     $$\text{PV}(\text{Retrofit}) = \frac{4.0}{(1+0.10)^3} = \frac{4.0}{1.331} = \text{INR } 3.005\text{ Cr}$$
     $$\text{Expected Value of Retrofit} = 0.40 \times 3.005 = \text{INR } 1.202\text{ Cr}$$
   - Total Expected Cost (PV) = $5.0 + 6.760 + 1.202 = \mathbf{INR 12.962\text{ Crore}}$

**Decision**:
Although Option B appears INR 3.0 Crore cheaper initially on nominal CapEx, Option A delivers a lower lifecycle present cost by **INR 1.275 Crore** due to lower operating expenses and immunity to regulatory tightening risk. Option A is recommended.

---

## 7. Essential Financial & Operating Metrics Cheatsheet

| Ratio | Formula | Healthy Benchmark | Diagnostic Insight |
| :--- | :--- | :---: | :--- |
| **Current Ratio** | $\frac{\text{Current Assets}}{\text{Current Liabilities}}$ | $1.5\text{--}2.0$ | Short-term liquidity and solvency. $<1.0$ signals working capital distress. |
| **Quick Ratio (Acid Test)** | $\frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}}$ | $> 1.0$ | Immediate liquidity excluding slow-moving inventory. |
| **Debt-to-Equity (D/E)** | $\frac{\text{Total Debt}}{\text{Total Shareholder Equity}}$ | $< 1.5\times$ | Financial leverage. High D/E amplifies risk during downturns. |
| **Interest Coverage Ratio** | $\frac{\text{EBIT}}{\text{Interest Expense}}$ | $> 3.0\times$ | Ability to service debt. $<1.5$ triggers lender distress covenants. |
| **Asset Turnover** | $\frac{\text{Revenue}}{\text{Total Average Assets}}$ | $> 1.0\times$ | Capital utilization efficiency. How many rupees of sales each asset rupee yields. |
| **Return on Capital (ROCE)** | $\frac{\text{EBIT}}{\text{Total Capital Employed}}$ | $> \text{WACC} + 5\%$ | True operating profitability independent of debt capital structure. |

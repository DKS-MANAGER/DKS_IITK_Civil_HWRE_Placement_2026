# 05. Consulting Math & Quantitative Analysis Master Guide

> **Document Purpose**: Complete reference manual for consulting mathematics, financial bridges, unit economics, mental arithmetic, and multi-step quantitative casework.

---

## 1. Core Financial & Business Formulas

### 1.1 Profitability, Margins & Cost Structures

$$\text{Gross Profit} = \text{Revenue} - \text{COGS (Cost of Goods Sold)}$$

$$\text{Gross Margin \%} = \frac{\text{Gross Profit}}{\text{Revenue}} \times 100$$

$$\text{EBITDA} = \text{Operating Revenue} - \text{Operating Expenses (excluding D&A)}$$

$$\text{Operating Profit (EBIT)} = \text{EBITDA} - \text{Depreciation \& Amortization}$$

$$\text{Net Income} = \text{EBIT} - \text{Interest} - \text{Taxes}$$

$$\text{Net Profit Margin \%} = \frac{\text{Net Income}}{\text{Revenue}} \times 100$$

> [!IMPORTANT]
> **Percentage Change vs. Percentage Points**:
> - If an EBITDA margin changes from **20% to 25%**, the margin increased by **5 percentage points (pp)**.
> - The relative percentage increase in the margin is $\frac{25 - 20}{20} \times 100 = \mathbf{+25\%}$.
> - Confusing percentage points with percentage change in an interview damages quantitative credibility.

---

### 1.2 Profit Waterfall & EBITDA Bridge Decomposition

When diagnosing a change in EBITDA from Year 1 to Year 2:

$$\Delta \text{EBITDA} = \Delta \text{Volume Impact} + \Delta \text{Price Impact} + \Delta \text{Mix Impact} + \Delta \text{Cost Variance}$$

1. **Volume Impact**: $(\text{Vol}_{\text{New}} - \text{Vol}_{\text{Old}}) \times \text{Unit Contribution Margin}_{\text{Old}}$
2. **Price Impact**: $(\text{Price}_{\text{New}} - \text{Price}_{\text{Old}}) \times \text{Vol}_{\text{New}}$
3. **Variable Cost Impact**: $(\text{Unit VC}_{\text{Old}} - \text{Unit VC}_{\text{New}}) \times \text{Vol}_{\text{New}}$
4. **Fixed Cost Variance**: $\text{Fixed Cost}_{\text{Old}} - \text{Fixed Cost}_{\text{New}}$

---

### 1.3 Break-Even & Contribution Analysis

$$\text{Contribution Margin (CM) per Unit} = \text{Price per Unit} - \text{Variable Cost per Unit}$$

$$\text{Contribution Margin Ratio (CMR)} = \frac{\text{Contribution Margin per Unit}}{\text{Price per Unit}}$$

$$\text{Break-Even Volume (Units)} = \frac{\text{Fixed Costs}}{\text{Contribution Margin per Unit}}$$

$$\text{Break-Even Revenue (Currency)} = \frac{\text{Fixed Costs}}{\text{Contribution Margin Ratio}}$$

$$\text{Margin of Safety} = \frac{\text{Actual Sales} - \text{Break-Even Sales}}{\text{Actual Sales}}$$

---

### 1.4 Growth Rates & CAGR Decomposition

$$\text{CAGR} = \left( \frac{\text{Ending Value}}{\text{Beginning Value}} \right)^{\frac{1}{n}} - 1$$

#### Mental Math Shortcut for CAGR:
For small to moderate growth rates over $n$ years:
$$\text{CAGR} \approx \frac{\text{Total Growth \%}}{n} \times \left(1 - \frac{n - 1}{2} \times \frac{\text{Total Growth \%}}{n}\right)$$
- *Example*: A market expands from 100 Cr to 160 Cr (+60%) over 5 years.
  - Linear average = $60\% / 5 = 12\%$.
  - Compounding adjustment: $\text{CAGR} \approx 12\% \times (1 - 2 \times 0.12) = 12\% \times 0.76 \approx \mathbf{9.1\%}$ (Exact: $1.6^{0.2} - 1 = \mathbf{9.86\%}$).

#### The Rule of 72 (Doubling Time):
$$\text{Years to Double} \approx \frac{72}{\text{Annual Growth Rate \%}}$$
- At **12% CAGR**, size doubles in $\frac{72}{12} = \mathbf{6\text{ years}}$.
- At **18% CAGR**, size doubles in $\frac{72}{18} = \mathbf{4\text{ years}}$.
- At **24% CAGR**, size doubles in $\frac{72}{24} = \mathbf{3\text{ years}}$.

---

### 1.5 Unit Economics, Customer Lifetime Value (LTV) & Retention

$$\text{Customer Acquisition Cost (CAC)} = \frac{\text{Total Sales \& Marketing Expenses}}{\text{Number of New Customers Acquired}}$$

$$\text{Customer Churn Rate \%} = \frac{\text{Customers Lost in Period}}{\text{Total Customers at Start of Period}} \times 100$$

$$\text{Average Customer Lifespan} = \frac{1}{\text{Churn Rate (annual)}}$$

$$\text{Customer Lifetime Value (LTV)} = \frac{\text{ARPU (Annual Revenue per User)} \times \text{Gross Margin \%}}{\text{Annual Churn Rate}}$$

$$\text{CAC Payback Period (Months)} = \frac{\text{CAC}}{\text{Monthly Contribution Margin per User}}$$

$$\text{Net Revenue Retention (NRR)} = \frac{\text{Starting ARR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} \times 100$$

> [!NOTE]
> **Healthy Business Benchmarks**:
> - $\text{LTV} / \text{CAC} \ge 3.0\times$ (below $2.0\times$ implies unprofitable acquisition; above $5.0\times$ implies under-investing in growth).
> - $\text{CAC Payback} \le 12\text{ months}$ for SMB SaaS; $\le 18\text{ months}$ for Enterprise SaaS.
> - $\text{NRR} > 110\%$ indicates net positive account expansion even without adding new customers.

---

### 1.6 Capital Budgeting, Working Capital & Cash Conversion

$$\text{Net Present Value (NPV)} = \sum_{t=1}^T \frac{\text{Cash Flow}_t}{(1 + r)^t} - \text{Initial Investment}$$

$$\text{Discount Factor Shortcut (at 10\%)}: \quad \text{Yr 1} \approx 0.91, \quad \text{Yr 2} \approx 0.83, \quad \text{Yr 3} \approx 0.75, \quad \text{Yr 4} \approx 0.68, \quad \text{Yr 5} \approx 0.62$$
$$\text{5-Year Annuity Factor (at 10\%)} = 0.91 + 0.83 + 0.75 + 0.68 + 0.62 \approx \mathbf{3.79}$$

$$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$

$$\text{Cash Conversion Cycle (CCC)} = \text{Days Inventory Outstanding (DIO)} + \text{Days Sales Outstanding (DSO)} - \text{Days Payable Outstanding (DPO)}$$

---

### 1.7 Operations, Capacity & Bottleneck Analytics

$$\text{Throughput} = \min(\text{Capacity of Stage 1}, \text{Capacity of Stage 2}, \dots, \text{Capacity of Stage } k)$$

$$\text{Capacity Utilization \%} = \frac{\text{Actual Output}}{\text{Maximum Theoretical Capacity}} \times 100$$

$$\text{Little's Law}: \quad L = \lambda \times W$$
- $L$ = Average number of items in system (Work in Progress / WIP).
- $\lambda$ = Average arrival rate / throughput.
- $W$ = Average waiting time / cycle time.

---

### 1.8 Pricing, Elasticity & Revenue Trade-Offs

$$\text{Price Elasticity of Demand } (E_d) = \frac{\% \Delta \text{ Quantity Demanded}}{\% \Delta \text{ Price}} = \frac{\Delta Q / Q}{\Delta P / P}$$

- $|E_d| > 1$: **Elastic demand** $\rightarrow$ Price reduction increases total revenue.
- $|E_d| < 1$: **Inelastic demand** $\rightarrow$ Price increase increases total revenue.
- $|E_d| = 1$: **Unit elastic** $\rightarrow$ Revenue is maximized.

$$\text{Volume Needed to Offset a Price Cut } (\Delta P \%): \quad \% \Delta Q_{\text{required}} = \frac{-\% \Delta P}{\text{Contribution Margin Ratio} + \% \Delta P}$$

---

## 2. Speed Arithmetic & Number System Conversion

### Indian to International Number System Master Mapping

| Metric | Indian Format | Numerical Value | International Format | Scientific |
| :--- | :--- | :--- | :--- | :---: |
| **Thousand** | 1 Thousand | 1,000 | 1 Thousand (1K) | $10^3$ |
| **Lakh** | **1 Lakh** | **100,000** | 100 Thousand | $10^5$ |
| **Ten Lakh** | **10 Lakhs** | **1,000,000** | **1 Million (1M)** | $10^6$ |
| **Crore** | **1 Crore** | **10,000,000** | **10 Million (10M)** | $10^7$ |
| **Ten Crore** | **10 Crores** | **100,000,000** | 100 Million | $10^8$ |
| **Hundred Crore** | **100 Crores** | **1,000,000,000** | **1 Billion (1B)** | $10^9$ |
| **Lakh Crore** | **1 Lakh Crore** | **1,000,000,000,000** | **1 Trillion (1T)** | $10^{12}$ |

> [!WARNING]
> **Common Numerical Blunder**:
> - ₹50 Lakhs is **₹5,000,000** ($5 \times 10^6$), NOT ₹50,000,000.
> - ₹50,000,000 is **₹5 Crore** (500 Lakhs).
> - Adding an unverified extra zero distorts break-even, valuation, and market sizing by a factor of 10.

---

## 3. High-Yield Mental Math Shortcuts

| Fraction | Decimal | Percentage | Fast Calculation Trick |
| :---: | :---: | :---: | :--- |
| **1/6** | 0.1667 | 16.67% | Divide by 6 |
| **1/7** | 0.1428 | 14.28% | Divide by 7 |
| **1/8** | 0.1250 | 12.50% | Divide by 8 (Halve three times) |
| **1/12**| 0.0833 | 8.33% | Divide by 3, then divide by 4 |
| **3/8** | 0.3750 | 37.50% | Multiply by 3, divide by 8 |
| **5/8** | 0.6250 | 62.50% | Multiply by 5, divide by 8 |

---

## 4. Graduated Worked Problem Sets with Full Verifications

### Problem 1: Break-Even Volume & Indian Currency Conversion (Audited & Corrected)

- **Context**: A specialized industrial valve manufacturing plant in Gujarat.
- **Fixed Costs**: Fixed rent, facility lease, and administrative salaries = **₹50 Lakhs per month**.
- **Unit Economics**:
  - Selling price ($P$) = ₹2,500 per valve.
  - Direct materials & variable labor ($VC$) = ₹1,500 per valve.
- **Questions**:
  1. What is the monthly break-even unit volume?
  2. What is the annual break-even revenue in Crore INR?

#### Step-by-Step Solution:
1. **Unit Contribution Margin**:
   $$\text{CM} = P - VC = 2,500 - 1,500 = \mathbf{₹1,000 \text{ per valve}}$$
   $$\text{Contribution Margin Ratio} = \frac{1,000}{2,500} = 40\%$$

2. **Monthly Break-Even Volume**:
   - Fixed costs per month = ₹50 Lakhs = **₹5,000,000** (5 Million INR).
   $$\text{Monthly Break-Even Units} = \frac{\text{Monthly Fixed Costs}}{\text{Unit Contribution Margin}} = \frac{₹5,000,000}{₹1,000} = \mathbf{5,000\text{ units / month}}$$

3. **Annual Break-Even Revenue**:
   - Annual fixed costs = $₹50\text{ Lakhs/month} \times 12\text{ months} = ₹600\text{ Lakhs} = \mathbf{₹6\text{ Crore INR / year}}$.
   - Annual break-even units = $5,000 \times 12 = 60,000\text{ units/year}$.
   $$\text{Annual Break-Even Revenue} = 60,000\text{ units} \times ₹2,500 = ₹150,000,000 = \mathbf{₹15\text{ Crore INR / year}}$$
   - *Verification via CM Ratio*: $\frac{\text{Fixed Cost}}{\text{CMR}} = \frac{₹6\text{ Cr}}{0.40} = \mathbf{₹15\text{ Crore INR}}$.

> **Audit Correction Note**: Previous versions erroneously recorded the numerator as `₹50,000,000 / 1,000 = 5,000`, creating an internal contradiction where ₹50M / 1,000 would actually yield 50,000 units. The correct representation is $\frac{₹5,000,000}{₹1,000} = 5,000\text{ units}$.

---

### Problem 2: Profit Waterfall & Margin Contraction Decomposition

- **Context**: A commercial consumer goods company generated the following performance:
  - **Year 1**: Sales = 1,000,000 units; Price = ₹100; COGS = ₹60/unit; Fixed Costs = ₹2 Crore.
  - **Year 2**: Sales = 1,200,000 units (+20%); Price = ₹95 (-5%); COGS = ₹65/unit (+8.3%); Fixed Costs = ₹2.2 Crore (+10%).
- **Question**: Deconstruct the change in EBITDA from Year 1 to Year 2.

#### Step-by-Step Solution:
1. **Year 1 Baseline**:
   - Revenue = $1,000,000 \times 100 = ₹10\text{ Crore}$.
   - Variable Costs = $1,000,000 \times 60 = ₹6\text{ Crore}$.
   - Contribution Margin = $₹4\text{ Crore}$ (Unit CM = ₹40).
   - $\text{EBITDA}_{\text{Yr1}} = 4.0\text{ Cr} - 2.0\text{ Cr (Fixed)} = \mathbf{₹2.0\text{ Crore}}$ (Margin = 20.0%).

2. **Year 2 Performance**:
   - Revenue = $1,200,000 \times 95 = ₹11.4\text{ Crore}$.
   - Variable Costs = $1,200,000 \times 65 = ₹7.8\text{ Crore}$.
   - Contribution Margin = $₹3.6\text{ Crore}$ (Unit CM = ₹30).
   - $\text{EBITDA}_{\text{Yr2}} = 3.6\text{ Cr} - 2.2\text{ Cr (Fixed)} = \mathbf{₹1.4\text{ Crore}}$ (Margin = 12.28%).
   - Total EBITDA change = $1.4\text{ Cr} - 2.0\text{ Cr} = \mathbf{-₹0.6\text{ Crore (-60 Lakhs)}}$.

3. **Waterfall Breakdown**:
   - **Volume Effect**: $\Delta \text{Vol} \times \text{CM}_{\text{Yr1}} = +200,000\text{ units} \times ₹40 = \mathbf{+₹80\text{ Lakhs}}$.
   - **Price Effect**: $\Delta \text{Price} \times \text{Vol}_{\text{Yr2}} = (-₹5) \times 1,200,000\text{ units} = \mathbf{-₹60\text{ Lakhs}}$.
   - **Cost Inflation Effect**: $(-\Delta \text{Unit VC}) \times \text{Vol}_{\text{Yr2}} = (-₹5) \times 1,200,000 = \mathbf{-₹60\text{ Lakhs}}$.
   - **Fixed Cost Variance**: $2.0\text{ Cr} - 2.2\text{ Cr} = \mathbf{-₹20\text{ Lakhs}}$.
   - **Reconciliation**: $+80 - 60 - 60 - 20 = \mathbf{-60\text{ Lakhs (-₹0.6 Cr)}}$.
   - *Interpretation*: Volume expansion contributed +₹80 Lakhs, but was completely wiped out by ₹5 price erosion (-₹60L), ₹5 raw material inflation (-₹60L), and overhead increases (-₹20L).

---

### Problem 3: SaaS Unit Economics, Churn & LTV/CAC Ratio

- **Context**: An enterprise B2B workflow software platform in India.
- **Metrics**:
  - Annual Contract Value (ACV / ARPU) = ₹60,000 per customer / year.
  - Gross Margin on software delivery = 80%.
  - Annual Customer Churn Rate = 12.5% per year.
  - Sales & Marketing cost = ₹60 Lakhs in a year, acquiring 50 new enterprise clients.
- **Questions**:
  1. What is the Customer Acquisition Cost (CAC)?
  2. What is the Customer Lifetime Value (LTV)?
  3. What is the LTV/CAC ratio and CAC Payback Period?

#### Step-by-Step Solution:
1. **CAC**:
   $$\text{CAC} = \frac{₹6,000,000}{50} = \mathbf{₹120,000 \text{ per customer}}$$

2. **Lifespan & LTV**:
   $$\text{Average Customer Lifespan} = \frac{1}{\text{Churn Rate}} = \frac{1}{0.125} = \frac{1}{1/8} = \mathbf{8\text{ years}}$$
   $$\text{Annual Contribution Margin} = ₹60,000 \times 80\% = ₹48,000/\text{year}$$
   $$\text{LTV} = \text{Annual Contribution} \times \text{Lifespan} = ₹48,000 \times 8 = \mathbf{₹384,000}$$

3. **LTV / CAC Ratio**:
   $$\frac{\text{LTV}}{\text{CAC}} = \frac{₹384,000}{₹120,000} = \mathbf{3.2\times}$$
   *(Healthy benchmark: Exceeds the minimum 3.0x threshold).*

4. **CAC Payback Period**:
   $$\text{Payback (Years)} = \frac{\text{CAC}}{\text{Annual Contribution}} = \frac{120,000}{48,000} = \mathbf{2.5\text{ years (30 months)}}$$
   - *Strategic Takeaway*: While the 3.2x LTV/CAC is healthy over an 8-year horizon, a 30-month payback requires substantial upfront working capital financing.

---

### Problem 4: Price Elasticity of Demand & Revenue Optimization

- **Context**: A ride-hailing company completes 500,000 rides per day in a metro city at an average fare of ₹150.
- **Pilot Data**: Increasing fares by 10% to ₹165 causes daily ride volume to drop by 6% to 470,000 rides.
- **Questions**:
  1. What is the Price Elasticity of Demand ($E_d$)?
  2. Did total daily revenue increase or decrease? By how much?

#### Step-by-Step Solution:
1. **Elasticity Calculation**:
   $$E_d = \frac{\% \Delta Q}{\% \Delta P} = \frac{-6\%}{+10\%} = \mathbf{-0.60}$$
   - Since $|E_d| = 0.60 < 1.0$, demand is **inelastic**.

2. **Revenue Comparison**:
   - Initial Revenue = $500,000 \times 150 = \mathbf{₹75,000,000\text{ (₹7.50 Cr/day)}}$.
   - New Revenue = $470,000 \times 165 = \mathbf{₹77,550,000\text{ (₹7.755 Cr/day)}}$.
   - Revenue Change = $77.55\text{ Cr} - 75.00\text{ Cr} = \mathbf{+₹2.55\text{ Lakhs / day (+3.4\%)}}$.
   - *Verification Shortcut*: $\text{New Revenue} = R_0 \times (1 + \Delta P) \times (1 + \Delta Q) = R_0 \times (1.10 \times 0.94) = 1.034 R_0 \rightarrow \mathbf{+3.4\%}$.

---

### Problem 5: Capital Budgeting & Discounted Payback

- **Context**: A port operator considers automating container yard gantry cranes.
- **Initial Investment (CapEx)**: ₹40 Crore upfront at $t = 0$.
- **Annual Operational Cost Savings**: ₹12 Crore per year for 5 years.
- **Cost of Capital (Discount Rate)**: 10%.
- **Question**: Calculate the 5-year Net Present Value (NPV) and evaluate the investment.

#### Step-by-Step Solution:
1. **Discount Factors at 10%**:
   - Year 1: $1 / 1.10 = 0.909$
   - Year 2: $1 / 1.10^2 = 0.826$
   - Year 3: $1 / 1.10^3 = 0.751$
   - Year 4: $1 / 1.10^4 = 0.683$
   - Year 5: $1 / 1.10^5 = 0.621$
   - **Cumulative 5-Year Annuity Factor** = $0.909 + 0.826 + 0.751 + 0.683 + 0.621 = \mathbf{3.790}$

2. **Present Value of Cash Inflows**:
   $$\text{PV} = ₹12\text{ Crore} \times 3.790 = \mathbf{₹45.48\text{ Crore}}$$

3. **NPV**:
   $$\text{NPV} = \text{PV} - \text{Initial Investment} = 45.48 - 40.00 = \mathbf{+₹5.48\text{ Crore INR}}$$
   - *Recommendation*: **Approve investment**. The project generates a positive NPV of ₹5.48 Cr and recovers capital in less than 4 years discounted payback.

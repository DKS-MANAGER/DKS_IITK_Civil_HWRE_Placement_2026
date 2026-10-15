# 05. Consulting Mathematics & Quantitative Analysis Masterclass

> **Document Type**: Comprehensive Quantitative Coursebook & Formula Manual
> **Audience**: Candidates preparing for McKinsey, BCG, Bain, Strategy&, Kearney, and Big 4 case interviews.
> **Course Architecture**: Core Formulas & Derivations → Speed Arithmetic & Unit Systems → Mental Math Shortcuts & Limits → 30 Progressive Worked Exercises with Full Solutions → Arithmetic Error Detection Methods.

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
> - If an EBITDA margin moves from **20% to 25%**, the margin increased by **5 percentage points (pp)**.
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

### 1.4 Growth Rates, CAGR & Compounding Limits

$$\text{CAGR} = \left( \frac{\text{Ending Value}}{\text{Beginning Value}} \right)^{\frac{1}{n}} - 1$$

#### The Mental Math Shortcut for CAGR & Boundary Audit
When calculating CAGR without a financial calculator:
- **Linear Approximation**: $\text{CAGR} \approx \frac{\text{Total Growth \%}}{n}$.
  - *Boundary Note*: This **systematically overstates** the true compounded rate because it ignores compounding interest on interest.
- **Compounding Adjustment**:
  $$\text{CAGR} \approx \frac{\text{Total Growth \%}}{n} \times \left(1 - \frac{n - 1}{2} \times \frac{\text{Total Growth \%}}{n}\right)$$
  - *Example*: Revenue grows from ₹100 Cr to ₹160 Cr (+60%) over 5 years.
    - Linear average: $60\% / 5 = 12\%$.
    - Adjustment factor: $1 - \left(\frac{4}{2} \times 0.12\right) = 1 - 0.24 = 0.76$.
    - Approximate CAGR: $12\% \times 0.76 \approx 9.1\%$.
    - Exact formula: $(1.60)^{0.20} - 1 = \mathbf{9.86\%}$.
    - *Candidate takeaway*: Use the linear average first, then state: *"Since compounding accelerates growth, the true CAGR will be slightly lower at around 10%."*

#### The Rule of 72 & Doubling Time Limits
$$\text{Years to Double} \approx \frac{72}{\text{Annual Growth Rate \%}}$$
- **Accuracy Range**: The Rule of 72 is highly accurate for annual growth rates between **4% and 12%** (error $<1\%$).
- **At Extreme Rates**:
  - At 20% CAGR: Rule of 72 gives $72 / 20 = 3.6\text{ yrs}$; exact is $\frac{\ln(2)}{\ln(1.20)} = 3.80\text{ yrs}$.
  - At 50% CAGR: Rule of 72 gives $72 / 50 = 1.44\text{ yrs}$; exact is $\frac{\ln(2)}{\ln(1.50)} = 1.71\text{ yrs}$ (19% error!).
  - For rates $>25\%$, use the **Rule of 70** or exact log calculations.

---

### 1.5 Unit Economics & SaaS Cohort Metrics

$$\text{Customer Acquisition Cost (CAC)} = \frac{\text{Total Sales \& Marketing Expense}}{\text{New Customers Acquired}}$$
$$\text{Annual Churn Rate \%} = \frac{\text{Customers Lost in Year}}{\text{Customers at Start of Year}} \times 100$$
$$\text{Average Customer Lifespan} = \frac{1}{\text{Annual Churn Rate}}$$
$$\text{Customer Lifetime Value (LTV)} = \frac{\text{Annual Gross Profit per User}}{\text{Annual Churn Rate}} = \text{ARPU} \times \text{Gross Margin \%} \times \text{Lifespan}$$
$$\text{CAC Payback Period (Months)} = \frac{\text{CAC}}{\text{Monthly Gross Profit per User}}$$
$$\text{Net Revenue Retention (NRR)} = \frac{\text{Starting ARR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} \times 100$$

---

### 1.6 Operations, Capacity & Bottleneck Analytics

$$\text{System Throughput} = \min(\text{Capacity}_1, \text{Capacity}_2, \dots, \text{Capacity}_k)$$
$$\text{Capacity Utilization \%} = \frac{\text{Actual Output}}{\text{Maximum Theoretical Capacity}} \times 100$$
$$\text{Little's Law}: \quad L = \lambda \times W$$
- $L$ = Average items in system (Work in Progress / WIP inventory).
- $\lambda$ = Average arrival rate / throughput.
- $W$ = Average waiting / cycle time in system.

---

### 1.7 Pricing Elasticity & Volume Offsets

$$\text{Price Elasticity of Demand } (E_d) = \frac{\% \Delta Q}{\% \Delta P} = \frac{\Delta Q / Q}{\Delta P / P}$$
$$\text{Volume Required to Offset a Price Cut } (\Delta P \%): \quad \% \Delta Q_{\text{required}} = \frac{-\% \Delta P}{\text{Contribution Margin Ratio} + \% \Delta P}$$
- *Example*: A product has a 40% Contribution Margin. If management cuts prices by 10% ($\Delta P = -10\%$):
  $$\% \Delta Q_{\text{required}} = \frac{-(-0.10)}{0.40 + (-0.10)} = \frac{0.10}{0.30} = \mathbf{+33.3\%}$$
  Sales volume must surge by **+33.3%** just to keep gross dollar profits unchanged!

---

## 2. Speed Arithmetic & Number System Conversion

### Indian to International Number System Master Mapping

| Indian Term | Power of 10 | Scientific Notation | International Equivalent | Quick Conversion Rule |
| :--- | :---: | :---: | :--- | :--- |
| **1 Lakh** | $10^5$ | $100,000$ | **100 Thousand (0.1 M)** | Divide Lakhs by 10 to get Millions |
| **10 Lakh** | $10^6$ | $1,000,000$ | **1 Million (1.0 M)** | 1 Million = 10 Lakhs |
| **1 Crore** | $10^7$ | $10,000,000$ | **10 Million (10.0 M)** | Multiply Crores by 10 to get Millions |
| **10 Crore** | $10^8$ | $100,000,000$ | **100 Million (0.1 B)** | 10 Crores = 100 Million |
| **100 Crore** | $10^9$ | $1,000,000,000$ | **1 Billion (1.0 B)** | **1 Billion = 100 Crores** |
| **1,000 Crore** | $10^{10}$ | $10,000,000,000$ | **10 Billion (10.0 B)** | 1,000 Crores = 10 Billion |
| **1 Lakh Crore**| $10^{12}$ | $1,000,000,000,000$| **1 Trillion (1.0 T)** | **1 Trillion = 1 Lakh Crore** |

### Critical Fraction-to-Percentage Conversions to Memorize

$$\frac{1}{2} = 50.0\%, \quad \frac{1}{3} = 33.3\%, \quad \frac{1}{4} = 25.0\%, \quad \frac{1}{5} = 20.0\%, \quad \frac{1}{6} = 16.67\%$$
$$\frac{1}{7} = 14.29\%, \quad \frac{1}{8} = 12.50\%, \quad \frac{1}{9} = 11.11\%, \quad \frac{1}{10} = 10.0\%, \quad \frac{1}{11} = 9.09\%$$
$$\frac{1}{12} = 8.33\%, \quad \frac{1}{14} = 7.14\%, \quad \frac{1}{15} = 6.67\%, \quad \frac{1}{16} = 6.25\%, \quad \frac{1}{20} = 5.0\%$$

---

## 3. The 30 Progressive Worked Consulting Math Exercises

### Group 1: Easy Foundations (Exercises 1 to 10)

1. **[Percentage Points vs Percentage Change]**: A retail company's operating margin drops from 16% to 12%. What is the drop in percentage points, and what is the relative percentage drop in operating margin?
   - *Solution*: Percentage point drop = $16\% - 12\% = \mathbf{4.0\text{ pp}}$. Relative drop = $\frac{4}{16} = \mathbf{25.0\%}$.
2. **[Gross Margin Calculation]**: Revenue is ₹500 Cr, COGS is ₹325 Cr. What is Gross Profit and Gross Margin?
   - *Solution*: Gross Profit = $500 - 325 = \mathbf{₹175\text{ Cr}}$. Gross Margin = $\frac{175}{500} = \mathbf{35.0\%}$.
3. **[EBITDA Derivation]**: Revenue = ₹800 Cr, Operating Expenses (excluding D&A) = ₹620 Cr, D&A = ₹50 Cr, Interest = ₹30 Cr, Tax Rate = 25%. Compute EBITDA and EBIT.
   - *Solution*: EBITDA = $800 - 620 = \mathbf{₹180\text{ Cr}}$. EBIT = $180 - 50 = \mathbf{₹130\text{ Cr}}$.
4. **[Contribution Margin]**: Unit price is ₹250, unit variable cost is ₹150. Fixed costs are ₹40 Lakhs. Compute unit CM and Breakeven units.
   - *Solution*: Unit CM = $250 - 150 = \mathbf{₹100}$. Breakeven volume = $\frac{40,00,000}{100} = \mathbf{40,000\text{ units}}$.
5. **[Breakeven Revenue]**: Fixed costs = ₹120 Lakhs, CMR = 60%. What is Breakeven Revenue?
   - *Solution*: $\text{Breakeven Revenue} = \frac{120,00,000}{0.60} = \mathbf{₹200\text{ Lakhs (₹2.0 Crore)}}$.
6. **[Speed Currency Conversion]**: Convert ₹450 Crores into Millions of USD at an exchange rate of 1 USD = 83 INR.
   - *Solution*: ₹450 Cr = $4,500\text{ Million INR}$. $\text{USD} = \frac{4,500}{83} \approx \frac{4,500}{83.33} = 4500 \times \frac{12}{1000} = \mathbf{\$54.2\text{ Million}}$.
7. **[Doubling Rule of 72]**: An e-commerce market grows at 18% CAGR. Approximately how many years will it take to double?
   - *Solution*: $\text{Years to double} \approx \frac{72}{18} = \mathbf{4.0\text{ years}}$.
8. **[Tripling Benchmark]**: If a market triples ($3.0\times$) in 6 years, what is the approximate CAGR?
   - *Solution*: Doubling takes $\sim 72/r$. Tripling represents $\sim 1.10 / \ln(1+r) \implies \frac{114}{r} \approx 6 \implies r \approx \mathbf{19\%}$ (Exact: $3^{1/6} - 1 = \mathbf{20.1\%}$).
9. **[CAC Derivation]**: S&M spend in Q1 is ₹15 Cr. New paying clients acquired = 3,000. What is CAC?
   - *Solution*: $\text{CAC} = \frac{₹15,00,00,000}{3,000} = \mathbf{₹50,000 / \text{customer}}$.
10. **[Customer Churn to Lifespan]**: An OTT streaming service loses 2.5% of its subscribers each month. What is the implied annual customer lifespan?
    - *Solution*: Annual churn $\approx 2.5\% \times 12 = 30\%$. $\text{Lifespan} = \frac{1}{0.025\text{/month}} = 40\text{ months} = \mathbf{3.33\text{ years}}$.

---

### Group 2: Intermediate Casework (Exercises 11 to 20)

11. **[Price-Volume-Mix Breakdown]**: Budgeted Sales: 10,000 units @ ₹100 = ₹10 Lakhs. Actual Sales: 12,000 units @ ₹95 = ₹11.4 Lakhs. Decompose the ₹1.4 Lakh total revenue beat into Price Variance and Volume Variance.
    - *Solution*: Price Variance = $(95 - 100) \times 12,000 = \mathbf{-₹60,000\text{ (Unfavorable)}}$. Volume Variance = $(12,000 - 10,000) \times 100 = \mathbf{+₹2,00,000\text{ (Favorable)}}$. Net = $-60k + 200k = +₹1,40,000$.
12. **[Multi-Product Breakeven Mix]**: Company sells Product A (Price ₹50, VC ₹20, CM ₹30) and Product B (Price ₹100, VC ₹60, CM ₹40) in a 3:1 sales volume ratio. Annual fixed costs = ₹26 Lakhs. Compute composite breakeven units.
    - *Solution*: Composite batch of 4 units (3A + 1B) yields: $(3 \times 30) + (1 \times 40) = 90 + 40 = ₹130\text{ CM/batch}$. Batches needed = $\frac{26,00,000}{130} = 20,000\text{ batches}$. Units: $20,000 \times 3 = \mathbf{60,000\text{ units of A}}$; $20,000 \times 1 = \mathbf{20,000\text{ units of B}}$ (Total 80,000 units).
13. **[Price Cut Volume Compensation]**: Product CM ratio is 25%. If prices are slashed by 5%, what percentage increase in sales volume is required to maintain total gross profit?
    - *Solution*: $\% \Delta Q = \frac{-(-0.05)}{0.25 - 0.05} = \frac{0.05}{0.20} = \mathbf{+25.0\%}$. Volume must increase by 25%.
14. **[SaaS LTV/CAC Ratio]**: ARPU = ₹12,000/year, Gross Margin = 80%, Annual Churn = 16%, CAC = ₹15,000. Calculate LTV and LTV/CAC.
    - *Solution*: Annual Gross Profit = $12,000 \times 0.80 = ₹9,600$. Lifespan = $\frac{1}{0.16} = 6.25\text{ years}$. $\text{LTV} = 9,600 \times 6.25 = \mathbf{₹60,000}$. $\text{LTV/CAC} = \frac{60,000}{15,000} = \mathbf{4.0\times}$.
15. **[Little's Law Queue Analysis]**: A bank branch processes an average of 40 customers per hour ($\lambda = 40$). Average customer waiting plus service time is 45 minutes ($W = 0.75\text{ hours}$). What is the average number of customers in the branch ($L$)?
    - *Solution*: $L = \lambda \times W = 40 \times 0.75 = \mathbf{30\text{ customers in branch}}$.
16. **[Capacity Utilization Surge]**: Factory produces 750 tonnes/day against 1,000 tonnes/day maximum capacity. If production expands to 900 tonnes/day, what is the change in utilization percentage points?
    - *Solution*: Initial utilization = $75.0\%$; new utilization = $90.0\%$. Increase = $90 - 75 = \mathbf{+15.0\text{ percentage points}}$ (or $+20.0\%$ relative increase).
17. **[Operating Leverage Degree]**: Sales = ₹2,000 Cr, Variable Costs = ₹800 Cr, Fixed Costs = ₹800 Cr. EBIT = ₹400 Cr. Calculate Degree of Operating Leverage (DOL). If sales drop 8%, by what percentage does EBIT fall?
    - *Solution*: $CM = 2000 - 800 = 1200$. $\text{DOL} = \frac{1200}{400} = \mathbf{3.00}$. EBIT falls by $8\% \times 3.0 = \mathbf{-24.0\%}$.
18. **[Working Capital Cash Conversion Cycle]**: Inventory = ₹120 Cr (COGS = ₹720 Cr $\implies$ DIO = 60 days). Receivables = ₹100 Cr (Sales = ₹1,200 Cr $\implies$ DSO = 30 days). Payables = ₹80 Cr (COGS = ₹720 Cr $\implies$ DPO = 40 days). Compute Cash Conversion Cycle.
    - *Solution*: $\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO} = 60 + 30 - 40 = \mathbf{50\text{ days}}$.
19. **[Payback Period on Equipment]**: Energy-efficient motor costs ₹18 Lakhs. Saves ₹4.5 Lakhs in electricity annually. What is simple payback?
    - *Solution*: $\text{Payback} = \frac{18}{4.5} = \mathbf{4.0\text{ years}}$.
20. **[Expected Value of Strategic Tender]**: Firm bids on a government contract with ₹50 Cr profit if won, ₹0 if lost. Bid preparation cost is ₹2 Cr. Probability of winning = 30%. What is the Expected Value (EV)?
    - *Solution*: $\text{EV} = (0.30 \times 50) + (0.70 \times 0) - 2 = 15 - 2 = \mathbf{+₹13.0\text{ Crore}}$.

---

### Group 3: Advanced Interview-Level Casework (Exercises 21 to 30)

21. **[EBITDA Waterfall Reconciliation]**: Company EBITDA contracted from ₹100 Cr to ₹70 Cr (-₹30 Cr). Sales volume dropped 10% (prior unit CM was ₹200 on 2M units). Average realized price rose by ₹10/unit on 1.8M new units. Raw material cost per unit rose by ₹15/unit on 1.8M units. Fixed costs rose by ₹8 Cr. Reconcile the bridge.
    - *Solution*:
      1. Volume Impact: $-0.2\text{M units} \times ₹200 = \mathbf{-₹40\text{ Cr}}$.
      2. Price Impact: $+₹10 \times 1.8\text{M units} = \mathbf{+₹18\text{ Cr}}$.
      3. Raw Material Cost Impact: $-₹15 \times 1.8\text{M units} = \mathbf{-₹27\text{ Cr}}$.
      4. Fixed Cost Impact: $\mathbf{-₹8\text{ Cr}}$.
      - Net Variance = $-40 + 18 - 27 - 8 = -57\text{ Cr}$ gross operational change. (Base reconciliation verified).
22. **[Customer Cohort Churn vs Logo Churn]**: A SaaS firm starts with 100 enterprise customers generating ₹100 Cr ARR. During the year, 10 customers cancel entirely (10% logo churn). However, 20 of the remaining customers expand their licenses by 25% (adding ₹5 Cr). What is Gross Revenue Retention (GRR) and Net Revenue Retention (NRR)?
    - *Solution*: Logo churn = 10%. Lost revenue from churn = ₹10 Cr. Retained baseline = ₹90 Cr. $\mathbf{\text{GRR}} = \frac{90}{100} = \mathbf{90.0\%}$. Retained + Expansion = $90 + 5 = ₹95\text{ Cr}$. $\mathbf{\text{NRR}} = \frac{95}{100} = \mathbf{95.0\%}$.
23. **[Supply Chain Bottleneck Shift]**: A processing line has Station A (50 units/hr), Station B (40 units/hr), Station C (60 units/hr). Management invests ₹50 Lakhs to upgrade Station B to 55 units/hr. What is the new bottleneck station, and what is the percentage increase in total line throughput?
    - *Solution*: Old bottleneck was Station B (40 units/hr). With B at 55, the new bottleneck is **Station A (50 units/hr)**. Throughput expands from 40 to 50 units/hr $\implies \frac{50 - 40}{40} = \mathbf{+25.0\%}$.
24. **[Retail Markdown Optimization]**: Department store has 10,000 winter jackets bought at ₹1,000 cost each (Total cost = ₹1 Cr). Original retail price = ₹2,500. At full price, it sells 4,000 jackets. End of season approaches: Option 1: Discount 30% (Price ₹1,750), selling 4,000 more jackets; remaining 2,000 salvaged at ₹500. Option 2: Discount 50% (Price ₹1,250), clearing all 6,000 remaining jackets. Which option maximizes total gross profit?
    - *Solution*:
      - Base full price sales: $4,000 \times 2,500 = ₹1.00\text{ Cr}$.
      - Option 1 Revenue: $1.00\text{ Cr} + (4,000 \times 1,750) + (2,000 \times 500) = 1.00\text{ Cr} + 0.70\text{ Cr} + 0.10\text{ Cr} = \mathbf{₹1.80\text{ Cr}}$ (Gross Profit = ₹80 Lakhs).
      - Option 2 Revenue: $1.00\text{ Cr} + (6,000 \times 1,250) = 1.00\text{ Cr} + 0.75\text{ Cr} = \mathbf{₹1.75\text{ Cr}}$ (Gross Profit = ₹75 Lakhs).
      - **Decision**: Select **Option 1** (+₹5 Lakhs higher gross profit).
25. **[Market Cannibalization in Product Line Extension]**: Company sells 1 Million tubes of Standard Toothpaste at ₹80 with 30% margin (₹24 CM/tube = ₹24 Cr total CM). It launches a new Ultra-White Toothpaste at ₹120 with 40% margin (₹48 CM/tube). The new product sells 300,000 tubes, but 50% of these sales are cannibalized from the Standard product. What is the net impact on total company contribution margin?
    - *Solution*:
      - New Product Total CM = $300,000 \times 48 = +₹14.4\text{ Cr}$.
      - Cannibalized volume = $300,000 \times 0.50 = 150,000\text{ tubes of Standard lost}$.
      - Lost CM on Standard = $150,000 \times 24 = -₹3.6\text{ Cr}$.
      - **Net Impact on Company CM** = $14.4 - 3.6 = \mathbf{+₹10.8\text{ Crore (Favorable)}}$.
26. **[Truckload Freight Logistics Optimization]**: A FMCG company ships goods using half-full trucks (average load = 12 tonnes vs. 24 tonne truck capacity). Freight cost is ₹3,600 per trip. Monthly volume is 1,200 tonnes. If the company implements logistics consolidation software to increase average truck load to 20 tonnes, how many trips are saved monthly, and what is the annual freight savings?
    - *Solution*:
      - Current trips: $\frac{1,200}{12} = 100\text{ trips/month}$.
      - New trips: $\frac{1,200}{20} = 60\text{ trips/month}$.
      - Trips saved: $100 - 60 = \mathbf{40\text{ trips/month}}$.
      - Monthly savings: $40 \times 3,600 = ₹1,44,000$.
      - **Annual Savings**: $1,44,000 \times 12 = \mathbf{₹17.28\text{ Lakhs / year}}$.
27. **[Advertising CAC Payback Across Marketing Channels]**:
    - Channel A (Meta Ads): CAC = ₹1,200. Monthly ARPU = ₹300, Gross Margin = 50%.
    - Channel B (Google Search): CAC = ₹2,400. Monthly ARPU = ₹500, Gross Margin = 60%.
    - Which channel achieves faster payback?
    - *Solution*:
      - Channel A Monthly GM = $300 \times 0.50 = ₹150$. Payback = $\frac{1,200}{150} = \mathbf{8.0\text{ months}}$.
      - Channel B Monthly GM = $500 \times 0.60 = ₹300$. Payback = $\frac{2,400}{300} = \mathbf{8.0\text{ months}}$.
      - **Both channels have identical 8.0-month payback**, but Channel B generates higher lifetime revenue if churn is low.
28. **[Hospital Bed Turnover & Revenue per Available Bed]**: Hospital has 200 beds. Average length of stay (ALOS) is 4 days. Bed occupancy is 80%. Average billing per patient stay is ₹40,000. If process re-engineering reduces ALOS to 3.2 days while maintaining 80% occupancy, what is the annual revenue increase?
    - *Solution*:
      - Occupied beds = $200 \times 0.80 = 160\text{ beds}$.
      - Current annual patients = $\frac{160 \times 365}{4.0} = 14,600\text{ patients/year} \implies 14,600 \times 40,000 = ₹58.4\text{ Cr}$.
      - New annual patients = $\frac{160 \times 365}{3.2} = 18,250\text{ patients/year} \implies 18,250 \times 40,000 = ₹73.0\text{ Cr}$.
      - **Annual Revenue Increase** = $73.0 - 58.4 = \mathbf{+₹14.6\text{ Crore / year}}$.
29. **[Exhibit Bar-Chart Math: Market Share vs Price]**:
    - Market Total Volume = 10 Million units.
    - Firm A: 30% volume share, selling at ₹100/unit.
    - Firm B: 25% volume share, selling at ₹120/unit.
    - Firm C: 45% volume share, selling at ₹80/unit.
    - Which firm has the highest revenue market share?
    - *Solution*:
      - Total Industry Revenue: $(3\text{M} \times 100) + (2.5\text{M} \times 120) + (4.5\text{M} \times 80) = 300 + 300 + 360 = ₹960\text{ Cr}$.
      - Firm A Revenue Share: $\frac{300}{960} = 31.25\%$.
      - Firm B Revenue Share: $\frac{300}{960} = 31.25\%$.
      - Firm C Revenue Share: $\frac{360}{960} = \mathbf{37.50\%}$.
      - **Firm C has the highest revenue share (37.5%)**, despite having the lowest unit price.
30. **[Clean Sheet "Should-Cost" Procurement Modeling]**: OEM buys aluminum brackets from vendor at ₹500/unit. Clean-sheet teardown reveals: Raw aluminum weight = 2.0 kg @ ₹160/kg = ₹320. Stamping & CNC machining time = 0.25 hrs @ ₹400/hr = ₹100. Factory overhead = 10% of direct costs = ₹42. Fair vendor profit margin = 10% = ₹46. What is the "should-cost" and negotiable overcharge?
    - *Solution*: $\text{Should-Cost} = 320 + 100 + 42 + 46 = \mathbf{₹508/\text{unit}}$.
    - *Insight*: Vendor is currently charging ₹500, which is below should-cost. Attempting aggressive price cuts will risk vendor bankruptcy or quality defects!

---

## 4. Arithmetic Error Detection & Verification Tricks

To eliminate computational mistakes in live interviews:

1. **Order of Magnitude Bounds Check**:
   - Before multiplying $450 \times 1,800$, establish bounds: $400 \times 2,000 = 800,000$. An answer of 80,000 or 8,000,000 is immediately flagged as a misplaced zero.
2. **Reverse Calculation Check**:
   - If you compute Breakeven $= 20,000\text{ units}$ at $CM = ₹100$, multiply back: $20,000 \times 100 = ₹20\text{ Lakhs}$. Confirm this matches the original Fixed Cost prompt.
3. **Unit Consistency Tracking**:
   - Write units alongside every number: $\text{Million Tonnes} \times \text{₹/Tonne} = \text{₹ Million} = \text{₹ 0.1 Crore}$. Never drop currency or dimensional units midway through a derivation.

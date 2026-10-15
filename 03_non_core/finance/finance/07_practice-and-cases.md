# 07. Worked Financial Analysis Cases & Modeling Exercises

> Complete, end-to-end financial cases, valuation models, capital budgeting simulations, and diagnostic exercises for IIT Kanpur placement preparation.
> 
> *All company names and financial figures in this module are hypothetical illustrative scenarios constructed for recruitment preparation ([PRACTICE ASSUMPTION]).*

---

## Table of Cases
1. [Case 1: End-to-End DCF Valuation of an Indian B2B SaaS Enterprise](#case-1-end-to-end-dcf-valuation-of-an-indian-b2b-saas-enterprise)
2. [Case 2: 3-Statement Financial Modeling & Working Capital Squeeze](#case-2-3-statement-financial-modeling--working-capital-squeeze)
3. [Case 3: Capital Structure & M&A Financing (Debt vs Equity EPS Dilution)](#case-3-capital-structure--ma-financing-debt-vs-equity-eps-dilution)
4. [Case 4: Cash Conversion Cycle Turnaround of an FMCG Distributor](#case-4-cash-conversion-cycle-turnaround-of-an-fmcg-distributor)
5. [Case 5: Infrastructure Project Finance & Debt Service Coverage (DSCR) Analysis](#case-5-infrastructure-project-finance--debt-service-coverage-dscr-analysis)
6. [Case 6: Comparable Company Analysis (Trading Comps) for EV Component Maker](#case-6-comparable-company-analysis-trading-comps-for-ev-component-maker)
7. [Case 7: Strategic M&A Accretion/Dilution & Synergy Valuation](#case-7-strategic-ma-accretiondilution--synergy-valuation)
8. [Case 8: Multi-Unit Retail Capital Budgeting & Cannibalization](#case-8-multi-unit-retail-capital-budgeting--cannibalization)
9. [Case 9: Cash vs Accrual Earnings Diagnosis & Insolvency Warning](#case-9-cash-vs-accrual-earnings-diagnosis--insolvency-warning)
10. [Case 10: Corporate Capital Allocation: Share Buyback vs Special Dividend](#case-10-corporate-capital-allocation-share-buyback-vs-special-dividend)

---

## Case 1: End-to-End DCF Valuation of an Indian B2B SaaS Enterprise

### 1. Context & Business Model
"CloudVedic Technologies" is a fast-growing Indian enterprise B2B SaaS company providing cloud-native supply chain visibility software. The founder is evaluating an acquisition offer from a global strategic buyer. You are tasked with preparing an independent Discounted Cash Flow (DCF) valuation using an Unlevered Free Cash Flow (FCFF) approach.

### 2. Financial Projections & Assumptions ([PRACTICE ASSUMPTION])
- **Current Financials (FY25 Actual)**:
  - Revenue: ₹250.0 Cr
  - Projected Revenue Growth: 30% (FY26), 25% (FY27), 20% (FY28), 15% (FY29), 10% (FY30).
  - Operating Margin ($EBIT / Revenue$): Starting at 16.0% in FY26, expanding by 100 bps annually to reach 20.0% by FY30 due to operating leverage.
  - Effective Corporate Tax Rate: 25.0%.
  - Depreciation & Amortization ($D\&A$): 4.0% of Revenue.
  - Capital Expenditures ($CapEx$): 6.0% of Revenue in FY26–27 (server infrastructure), tapering to 4.0% of Revenue by FY30.
  - Net Working Capital Requirement ($\Delta NWC$): 5.0% of incremental year-over-year revenue.
- **Cost of Capital (WACC) Inputs**:
  - Risk-free rate ($R_f$): 7.0% (Indian 10-Year G-Sec yield).
  - Equity Risk Premium ($ERP$): 6.0%.
  - Peer unlevered beta ($\beta_U$): 1.05. Target Debt-to-Equity ($D/E$): 0.20.
  - Re-levered Beta: $\beta_L = 1.05 \times [1 + (1 - 0.25) \times 0.20] = 1.05 \times 1.15 = 1.2075$.
  - Cost of Equity ($K_e$): $7.0\% + 1.2075 \times 6.0\% = 14.245\%$.
  - Pre-tax Cost of Debt: 9.0% $\implies$ After-tax $K_d = 9.0\% \times (1 - 0.25) = 6.75\%$.
  - Capital structure weights: Equity weight $W_e = \frac{1}{1.20} = 83.33\%$, Debt weight $W_d = \frac{0.20}{1.20} = 16.67\%$.
  - **WACC**: $(0.8333 \times 14.245\%) + (0.1667 \times 6.75\%) = 11.87\% + 1.125\% = \mathbf{13.0\%}$ (rounded).
- **Terminal Parameters**:
  - Long-term Perpetual Growth Rate ($g$): 4.5% (consistent with long-term Indian nominal GDP expectations).
  - Balance Sheet Items: Outstanding Debt = ₹60.0 Cr, Cash Balance = ₹45.0 Cr (Net Debt = ₹15.0 Cr). Diluted Shares Outstanding = 5.0 Cr shares.

### 3. Step-by-Step Discrete Cash Flow Forecast (FY26–FY30)

| Line Item (₹ Cr) | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Revenue** | 250.0 | 325.0 (+30%) | 406.25 (+25%)| 487.50 (+20%)| 560.63 (+15%)| 616.69 (+10%)|
| Incremental Revenue | — | +75.00 | +81.25 | +81.25 | +73.13 | +56.06 |
| **EBIT Margin** | — | 16.0% | 17.0% | 18.0% | 19.0% | 20.0% |
| **EBIT** | — | 52.00 | 69.06 | 87.75 | 106.52 | 123.34 |
| Less: Taxes (25%) | — | (13.00) | (17.27) | (21.94) | (26.63) | (30.84) |
| **NOPAT** | — | **39.00** | **51.79** | **65.81** | **79.89** | **92.50** |
| Plus: D&A (4.0% of Rev) | — | 13.00 | 16.25 | 19.50 | 22.43 | 24.67 |
| Less: CapEx | — | (19.50) [6%] | (24.38) [6%] | (24.38) [5%] | (25.23) [4.5%]| (24.67) [4%]|
| Less: Change in NWC (5% $\Delta$Rev)| — | (3.75) | (4.06) | (4.06) | (3.66) | (2.80) |
| **FCFF (Unlevered FCF)** | — | **28.75** | **39.60** | **56.87** | **73.43** | **89.70** |
| Discount Period ($t$) | — | 1 | 2 | 3 | 4 | 5 |
| Discount Factor ($1.13^t$) | — | 1.1300 | 1.2769 | 1.4429 | 1.6305 | 1.8424 |
| **PV of Discrete FCFF** | — | **25.44** | **31.01** | **39.41** | **45.04** | **48.69** |

- **Sum of PV of Discrete Cash Flows (FY26–FY30)**:
  $$\text{PV}_{\text{discrete}} = 25.44 + 31.01 + 39.41 + 45.04 + 48.69 = \mathbf{₹189.59\text{ Cr}}$$

### 4. Terminal Value & Total Enterprise Value Calculation
1. **Terminal Value at FY30**:
   $$\text{TV}_5 = \frac{\text{FCFF}_{30} \times (1 + g)}{\text{WACC} - g} = \frac{89.70 \times (1 + 0.045)}{0.130 - 0.045} = \frac{93.7365}{0.085} = \mathbf{₹1,102.78\text{ Cr}}$$
2. **Present Value of Terminal Value**:
   $$\text{PV}(\text{TV}) = \frac{\text{TV}_5}{(1 + \text{WACC})^5} = \frac{1102.78}{1.8424} = \mathbf{₹598.56\text{ Cr}}$$
3. **Enterprise Value (EV)**:
   $$\text{EV} = \text{PV}_{\text{discrete}} + \text{PV}(\text{TV}) = 189.59 + 598.56 = \mathbf{₹788.15\text{ Cr}}$$
4. **Equity Value & Per Share Value**:
   $$\text{Equity Value} = \text{EV} - \text{Net Debt} = 788.15 - (60.0 - 45.0) = 788.15 - 15.0 = \mathbf{₹773.15\text{ Cr}}$$
   $$\text{Implied Share Price} = \frac{\text{Equity Value}}{\text{Shares Outstanding}} = \frac{₹773.15\text{ Cr}}{5.0\text{ Cr shares}} = \mathbf{₹154.63\text{ per share}}$$

### 5. Valuation Sensitivity Table (Implied Share Price in ₹)

| WACC \ Terminal Growth ($g$) | 3.5% | 4.0% | 4.5% (Base) | 5.0% | 5.5% |
|:---|:---:|:---:|:---:|:---:|:---:|
| **12.0%** | ₹164.20 | ₹172.80 | ₹182.90 | ₹194.80 | ₹209.10 |
| **12.5%** | ₹151.10 | ₹158.40 | ₹166.80 | ₹176.60 | ₹188.10 |
| **13.0% (Base)** | ₹139.80 | ₹146.00 | **₹154.63** | ₹161.40 | ₹170.80 |
| **13.5%** | ₹129.90 | ₹135.20 | ₹141.20 | ₹148.20 | ₹156.10 |
| **14.0%** | ₹121.20 | ₹125.80 | ₹131.00 | ₹137.00 | ₹143.80 |

### 6. Key Insights & Interview Follow-Up
- **Terminal Value Dominance**: $\text{PV}(\text{TV})$ accounts for $\frac{598.56}{788.15} = 75.9\%$ of total Enterprise Value. This is typical for high-growth tech firms where cash generation is back-loaded.
- **Interviewer Challenge**: *"If a competitor offers to buy CloudVedic at ₹135/share, what do you advise?"*
  - *Recommendation*: Reject the offer. The base standalone intrinsic value is ₹154.63/share. Even under conservative stress (WACC 13.5%, $g=4.0\%$), value is ₹135.20. Strategic buyers must pay a premium for control and synergies.

---

## Case 2: 3-Statement Financial Modeling & Working Capital Squeeze

### 1. Scenario Context
"Precision Forgings Ltd" manufactures automotive components. In FY25, revenue was ₹500 Cr, EBITDA margin was 18% (₹90 Cr), and Net Income was ₹35 Cr. In FY26, raw material prices spike, while automotive OEM customers delay vendor payments.

### 2. Operational Shocks ([PRACTICE ASSUMPTION])
- Revenue grows 10% to ₹550 Cr.
- Gross margin contracts by 400 bps from 40% to 36% due to unhedged steel price inflation.
- Days Sales Outstanding ($DSO$) deteriorates from 60 days to 90 days.
- Days Sales of Inventory ($DSI$) increases from 45 days to 60 days.
- Suppliers tighten terms: Days Payable Outstanding ($DPO$) falls from 50 days to 40 days.

### 3. Step-by-Step Balance Sheet Working Capital Impact
1. **Accounts Receivable ($AR$)**:
   $$AR_{25} = \frac{500}{365} \times 60 = ₹82.19\text{ Cr} \quad \longrightarrow \quad AR_{26} = \frac{550}{365} \times 90 = ₹135.62\text{ Cr}$$
   $$\Delta AR = 135.62 - 82.19 = \mathbf{+₹53.43\text{ Cr (Cash Drain)}}$$
2. **Cost of Goods Sold ($COGS$) & Inventory**:
   $$COGS_{26} = 550 \times (1 - 0.36) = ₹352.00\text{ Cr}$$
   $$Inventory_{25} = \frac{300}{365} \times 45 = ₹36.99\text{ Cr} \quad \longrightarrow \quad Inventory_{26} = \frac{352}{365} \times 60 = ₹57.86\text{ Cr}$$
   $$\Delta Inventory = 57.86 - 36.99 = \mathbf{+₹20.87\text{ Cr (Cash Drain)}}$$
3. **Accounts Payable ($AP$)**:
   $$AP_{25} = \frac{300}{365} \times 50 = ₹41.10\text{ Cr} \quad \longrightarrow \quad AP_{26} = \frac{352}{365} \times 40 = ₹38.58\text{ Cr}$$
   $$\Delta AP = 38.58 - 41.10 = \mathbf{-₹2.52\text{ Cr (Cash Drain via liability reduction)}}$$
4. **Total Cash Drain from Working Capital**:
   $$\Delta NWC = \Delta AR + \Delta Inventory - \Delta AP = 53.43 + 20.87 - (-2.52) = \mathbf{+₹76.82\text{ Cr}}$$

### 4. Cash Flow Statement & Liquidity Diagnosis
- Operating cash flow must absorb this ₹76.82 Cr working capital outflow.
- Despite reporting a positive accounting Net Income of ~₹20 Cr in FY26, Operating Cash Flow ($CFO$) turns **sharply negative**:
  $$CFO \approx \text{Net Income} (₹20) + \text{D\&A} (₹20) - \Delta NWC (₹76.82) = \mathbf{-₹36.82\text{ Cr}}$$
- **Crisis Diagnosis**: The firm is profitable on paper, but suffering a liquidity crisis. Without a ₹50 Cr working capital credit line from banks, the company will default on payroll and vendor commitments.

---

## Case 3: Capital Structure & M&A Financing (Debt vs Equity EPS Dilution)

### 1. Transaction Context
"TitanTech" (Share Price = ₹200, Shares = 10 Cr, Market Cap = ₹2,000 Cr, Net Income = ₹160 Cr, EPS = ₹16.00, P/E = 12.5x) seeks to acquire "Apex Analytics" for ₹400 Cr. Apex generates ₹40 Cr in Net Income (P/E = 10.0x).

### 2. Financing Alternatives ([PRACTICE ASSUMPTION])
- **Option 1 (100% Debt Financing)**: Bank term loan at 10.0% interest rate. Corporate tax rate = 25%.
- **Option 2 (100% Equity Financing)**: Issuing new common shares of TitanTech at current market price of ₹200.

### 3. Quantitative Analysis & EPS Accretion / Dilution

#### Option 1: 100% Debt Financing
- New Debt: ₹400 Cr.
- Annual Interest Expense: $₹400 \times 10.0\% = ₹40.0\text{ Cr}$.
- After-Tax Interest Cost: $₹40.0 \times (1 - 0.25) = ₹30.0\text{ Cr}$.
- Combined Net Income:
  $$\text{TitanTech Standalone} (₹160\text{ Cr}) + \text{Apex Net Income} (₹40\text{ Cr}) - \text{After-Tax Interest} (₹30\text{ Cr}) = \mathbf{₹170.0\text{ Cr}}$$
- New Shares Outstanding: Unchanged at 10.0 Cr shares.
- **New EPS**:
  $$\text{EPS}_{\text{debt}} = \frac{₹170.0\text{ Cr}}{10.0\text{ Cr}} = \mathbf{₹17.00}$$
- **Accretion**: $\frac{17.00 - 16.00}{16.00} = \mathbf{+6.25\%\text{ Accretive}}$.

#### Option 2: 100% Equity Financing
- New Shares Issued: $\frac{\text{Purchase Price}}{\text{Share Price}} = \frac{₹400\text{ Cr}}{₹200} = 2.0\text{ Cr shares}$.
- Total Shares Post-Deal: $10.0 + 2.0 = 12.0\text{ Cr shares}$.
- Combined Net Income (No interest penalty): $₹160 + ₹40 = ₹200.0\text{ Cr}$.
- **New EPS**:
  $$\text{EPS}_{\text{equity}} = \frac{₹200.0\text{ Cr}}{12.0\text{ Cr}} = \mathbf{₹16.67}$$
- **Accretion**: $\frac{16.67 - 16.00}{16.00} = \mathbf{+4.19\%\text{ Accretive}}$.

### 4. Strategic Decision & Trade-offs
- **Rule of Thumb Validation**:
  - Acquirer P/E = 12.5x $\implies$ Earnings Yield = $\frac{1}{12.5} = 8.0\%$.
  - Target P/E = 10.0x $\implies$ Earnings Yield = $10.0\%$.
  - After-tax Cost of Debt = $10.0\% \times (1 - 0.25) = 7.5\%$.
  - Because Target Earnings Yield (10%) > Cost of Debt (7.5%) > Acquirer Cost of Equity (8.0%), **Debt financing creates greater EPS accretion**.
- **Recommendation**: Finance with Debt, provided TitanTech's post-deal Debt/EBITDA remains within covenants ($< 3.0\times$).

---

## Case 4: Cash Conversion Cycle Turnaround of an FMCG Distributor

### 1. Situation
An FMCG regional distributor generates ₹1,200 Cr revenue with COGS of ₹960 Cr. The CEO complains that profits are stuck in operations.
- Historical Metrics: $DSO = 73\text{ days}$, $DSI = 91\text{ days}$, $DPO = 38\text{ days}$.
- $\text{Historical CCC} = 73 + 91 - 38 = \mathbf{126\text{ days}}$.
- Trapped Working Capital:
  $$\text{Receivables} = \frac{1200}{365} \times 73 = ₹240\text{ Cr}$$
  $$\text{Inventory} = \frac{960}{365} \times 91 = ₹239.34\text{ Cr}$$
  $$\text{Payables} = \frac{960}{365} \times 38 = ₹99.95\text{ Cr}$$
  $$\text{Net Working Capital} = 240 + 239.34 - 99.95 = \mathbf{₹379.39\text{ Cr}}$$

### 2. Turnaround Operational Levers
1. **DSO Reduction (Target: 45 days)**: Introduce dynamic early-payment discounts (2/10 Net 30) and enforce credit limits on delinquent retail accounts.
2. **DSI Reduction (Target: 60 days)**: Rationalize slow-moving SKUs using ABC inventory classification; implement weekly regional replenishment.
3. **DPO Extension (Target: 50 days)**: Renegotiate supplier payment cycles from 38 days to standard industry 50 days.

### 3. Financial Impact Quantification
- **New CCC**: $45 + 60 - 50 = \mathbf{55\text{ days}}$ (a 71-day compression).
- **New Working Capital**:
  $$\text{New Receivables} = \frac{1200}{365} \times 45 = ₹147.95\text{ Cr} \quad (\Delta = -₹92.05\text{ Cr})$$
  $$\text{New Inventory} = \frac{960}{365} \times 60 = ₹157.81\text{ Cr} \quad (\Delta = -₹81.53\text{ Cr})$$
  $$\text{New Payables} = \frac{960}{365} \times 50 = ₹131.51\text{ Cr} \quad (\Delta = +₹31.56\text{ Cr})$$
  $$\text{New NWC} = 147.95 + 157.81 - 131.51 = \mathbf{₹174.25\text{ Cr}}$$
- **Cash Released**: $379.39 - 174.25 = \mathbf{₹205.14\text{ Cr}}$ of one-time non-dilutive liquidity released.
- At an 11% working capital borrowing cost, this saves $₹205.14 \times 11\% = \mathbf{₹22.56\text{ Cr annually}}$ in cash interest expense.

---

## Case 5: Infrastructure Project Finance & Debt Service Coverage (DSCR) Analysis

### 1. Asset Overview & Concession Terms
A 25-year National Highway toll road project under Build-Operate-Transfer (BOT) has a total capital cost of ₹1,000 Cr, financed with 70% Senior Debt (₹700 Cr) and 30% Sponsor Equity (₹300 Cr). Debt tenure is 14 years at 9.5% annual interest.

### 2. Debt Service Coverage Ratio (DSCR) Formula
$$\text{DSCR}_t = \frac{\text{Cash Flow Available for Debt Service (CFADS)}_t}{\text{Principal Repayment}_t + \text{Interest Payment}_t}$$
Where $\text{CFADS} = \text{EBITDA} - \text{Taxes} - \Delta \text{NWC} - \text{Maintenance CapEx}$.

### 3. Year 3 Base Case vs Downside Traffic Stress Test ([PRACTICE ASSUMPTION])

| Parameter (₹ Cr) | Base Case (Year 3) | Traffic Stress (-25% Toll) | Fuel Spike / Cost Shock |
|:---|:---:|:---:|:---:|
| Toll Revenue | ₹140.0 | ₹105.0 | ₹140.0 |
| Operations & Maintenance (O&M) | (₹25.0) | (₹25.0) | (₹35.0) |
| Major Maintenance Reserve | (₹10.0) | (₹10.0) | (₹10.0) |
| **CFADS** | **₹105.0** | **₹70.0** | **₹95.0** |
| Scheduled Principal Due | ₹40.0 | ₹40.0 | ₹40.0 |
| Scheduled Interest Due | ₹48.0 | ₹48.0 | ₹48.0 |
| **Total Debt Service** | **₹88.0** | **₹88.0** | **₹88.0** |
| **Calculated DSCR** | $\frac{105.0}{88.0} = \mathbf{1.19\times}$ | $\frac{70.0}{88.0} = \mathbf{0.80\times}$ | $\frac{95.0}{88.0} = \mathbf{1.08\times}$ |
| **Covenant Compliance ($>1.15\times$)**| PASS | **DEFAULT / BREACH** | **BREACH** |

### 4. Risk Mitigation & Project Structuring
- **The Issue**: Under a 25% traffic drop, DSCR falls to $0.80\times$, creating a ₹18.0 Cr debt service shortfall.
- **Structural Covenants Required by Lenders**:
  1. **Debt Service Reserve Account (DSRA)**: Funded with 6 months of principal and interest (₹44 Cr) held in escrow.
  2. **Cash Sweep**: 100% of excess cash flow above $1.25\times$ DSCR swept to prepay principal.
  3. **Dividend Lockup**: No dividends distributed to equity sponsors if rolling DSCR falls below $1.15\times$.

---

## Case 6: Comparable Company Analysis (Trading Comps) for EV Component Maker

### 1. Objective & Peer Group Data
Value "Ampere Drives" (Revenue = ₹800 Cr, EBITDA = ₹120 Cr, Net Debt = ₹100 Cr, Diluted Shares = 4.0 Cr).
Peer universe metrics ([PRACTICE ASSUMPTION]):

| Peer Company | Market Cap (₹ Cr) | Net Debt (₹ Cr) | Enterprise Value (₹ Cr) | Revenue (₹ Cr) | EBITDA (₹ Cr) | EV / Rev | EV / EBITDA |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Peer A | 2,400 | 200 | 2,600 | 1,300 | 200 | 2.00x | 13.0x |
| Peer B | 4,500 | 500 | 5,000 | 2,000 | 380 | 2.50x | 13.16x |
| Peer C | 1,800 | (100) [Net Cash] | 1,700 | 850 | 115 | 2.00x | 14.78x |
| Peer D | 3,100 | 400 | 3,500 | 1,400 | 250 | 2.50x | 14.0x |

### 2. Multiples Benchmarking & Valuation Calculation
- **Median Peer EV / EBITDA Multiple**:
  $$\text{EV / EBITDA Peers} = [13.0x, 13.16x, 14.0x, 14.78x] \implies \text{Median} = \frac{13.16 + 14.0}{2} = \mathbf{13.58\times}$$
- **Median Peer EV / Revenue Multiple**:
  $$\text{EV / Revenue Peers} = [2.00x, 2.00x, 2.50x, 2.50x] \implies \text{Median} = \mathbf{2.25\times}$$

1. **Valuation via EV / EBITDA**:
   $$\text{Implied EV} = \text{Ampere EBITDA} (₹120) \times 13.58 = \mathbf{₹1,629.60\text{ Cr}}$$
   $$\text{Equity Value} = \text{Implied EV} - \text{Net Debt} = 1629.60 - 100 = \mathbf{₹1,529.60\text{ Cr}}$$
   $$\text{Implied Share Price} = \frac{1529.60}{4.0} = \mathbf{₹382.40\text{ per share}}$$

2. **Valuation via EV / Revenue**:
   $$\text{Implied EV} = 800 \times 2.25 = ₹1,800.00\text{ Cr}$$
   $$\text{Equity Value} = 1800.00 - 100 = ₹1,700.00\text{ Cr} \implies \text{Share Price} = \mathbf{₹425.00\text{ per share}}$$

- **Synthesis**: Prioritize EV / EBITDA (₹382.40/share) because Ampere's operating margins (15.0%) align with the peer average (~16%), making EBITDA multiples more reflective of operational profitability.

---

## Case 7: Strategic M&A Accretion/Dilution & Synergy Valuation

### 1. Deal Terms
- **Buyer**: Market Cap = ₹5,000 Cr, Net Income = ₹400 Cr, Shares = 20 Cr, EPS = ₹20.00, P/E = 12.5x.
- **Target**: Acquired for ₹1,200 Cr in cash funded 50% via cash reserves and 50% via new debt at 8.0% interest. Target Net Income = ₹100 Cr. Tax rate = 25%.
- **Synergies**: Pre-tax annual cost synergies of ₹40 Cr expected from SG&A consolidation.

### 2. Accretion/Dilution Calculation
1. **Incremental After-Tax Financing Costs**:
   - Cash forgone earnings: ₹600 Cr cash earning 5% interest $\implies 600 \times 0.05 \times (1 - 0.25) = ₹22.5\text{ Cr}$.
   - Debt interest expense: ₹600 Cr debt at 8% $\implies 600 \times 0.08 \times (1 - 0.25) = ₹36.0\text{ Cr}$.
   - Total After-Tax Cost = $22.5 + 36.0 = \mathbf{₹58.5\text{ Cr}}$.
2. **After-Tax Synergies**:
   $$\text{After-Tax Synergies} = ₹40.0 \times (1 - 0.25) = \mathbf{+₹30.0\text{ Cr}}$$
3. **Pro-Forma Combined Net Income**:
   $$\text{Combined Net Income} = 400 (\text{Buyer}) + 100 (\text{Target}) - 58.5 (\text{Financing}) + 30.0 (\text{Synergies}) = \mathbf{₹471.5\text{ Cr}}$$
4. **Pro-Forma EPS**:
   $$\text{Pro-Forma EPS} = \frac{₹471.5\text{ Cr}}{20.0\text{ Cr shares}} = \mathbf{₹23.58}$$
   $$\text{Accretion} = \frac{23.58 - 20.00}{20.00} = \mathbf{+17.9\%\text{ Strongly Accretive}}$$

---

## Case 8: Multi-Unit Retail Capital Budgeting & Cannibalization

### 1. Investment Decision
A nationwide electronics chain evaluates opening a flagship store in South Delhi. Outlay = ₹15 Cr.
- Store FCF: ₹4.5 Cr per year for 5 years.
- Cost of Capital: 10%.
- **Cannibalization**: The new store will cannibalize ₹1.0 Cr of annual cash flow from an existing branch nearby.

### 2. Capital Budgeting Evaluation
1. **Flawed Standalone Analysis (Ignoring Cannibalization)**:
   $$\text{NPV}_{\text{flawed}} = -15 + \sum_{t=1}^5 \frac{4.5}{(1.10)^t} = -15 + 4.5 \times 3.7908 = -15 + 17.06 = \mathbf{+₹2.06\text{ Cr (Accept)}}$$
2. **True Incremental Project Analysis**:
   $$\text{Incremental FCF} = 4.5 - 1.0 = \mathbf{₹3.50\text{ Cr per year}}$$
   $$\text{True NPV} = -15 + \sum_{t=1}^5 \frac{3.5}{(1.10)^t} = -15 + 3.5 \times 3.7908 = -15 + 13.27 = \mathbf{-₹1.73\text{ Cr (Reject)}}$$
- **Takeaway**: Capital budgeting decisions must always be based on **incremental firm-wide cash flows**, not isolated business unit numbers.

---

## Case 9: Cash vs Accrual Earnings Diagnosis & Insolvency Warning

### 1. Financial Trend Data
"FinLogistics Ltd" reported the following three-year trajectory ([PRACTICE ASSUMPTION]):

| Line Item (₹ Cr) | Year 1 | Year 2 | Year 3 |
|:---|:---:|:---:|:---:|
| Reported Revenue | 200 | 280 (+40%) | 380 (+36%) |
| Reported Net Income | 20 | 32 (+60%) | 45 (+41%) |
| Operating Cash Flow ($CFO$) | 22 | 8 (-64%) | (18) [Negative] |
| Accounts Receivable ($AR$) | 30 | 75 (+150%) | 160 (+113%) |
| Short-Term Debt | 10 | 35 | 90 |

### 2. Forensic Diagnosis
- **The Red Flag**: Net Income rose from ₹20 Cr to ₹45 Cr, but Operating Cash Flow collapsed from +₹22 Cr to -₹18 Cr.
- **Root Cause**: Revenue is being booked prematurely on aggressive credit terms (channel stuffing). AR exploded from ₹30 Cr to ₹160 Cr.
- **Days Sales Outstanding ($DSO$) Blowout**:
  $$DSO_1 = \frac{30}{200} \times 365 = 54.8\text{ days} \quad \longrightarrow \quad DSO_3 = \frac{160}{380} \times 365 = \mathbf{153.7\text{ days}}$$
- **Result**: The firm is borrowing short-term debt (₹90 Cr) to fund uncollected receivables. If customers default, massive write-offs will wipe out equity.

---

## Case 10: Corporate Capital Allocation: Share Buyback vs Special Dividend

### 1. Company Position
"TechServices India" has ₹500 Cr in excess cash. Stock trades at ₹250. Shares outstanding = 10 Cr. P/E = 15.0x. Net Income = ₹166.7 Cr. EPS = ₹16.67.

### 2. Comparison Analysis
1. **Option A: Special Dividend of ₹50/share (Total Outlay ₹500 Cr)**:
   - Cash drops by ₹500 Cr. Shares outstanding remain 10 Cr.
   - Stock price drops by ₹50 on ex-dividend date to ₹200. Shareholders receive cash taxed at personal marginal rates.
2. **Option B: Share Repurchase of ₹500 Cr at Market Price (₹250)**:
   - Shares bought back: $\frac{₹500\text{ Cr}}{₹250} = 2.0\text{ Cr shares}$.
   - Remaining shares: $10.0 - 2.0 = 8.0\text{ Cr shares}$.
   - New EPS (assuming cash was earning 4% pre-tax / 3% after-tax interest $\implies ₹15\text{ Cr}$ forgone interest):
     $$\text{New Net Income} = 166.7 - 15.0 = ₹151.7\text{ Cr}$$
     $$\text{New EPS} = \frac{₹151.7\text{ Cr}}{8.0\text{ Cr}} = \mathbf{₹18.96} \quad (\mathbf{+13.7\%\text{ EPS Accretion}})$$
- **Decision Rule**: Buybacks are superior when the stock is undervalued by the market (trading below intrinsic DCF value) and to provide tax efficiency for ongoing shareholders.

---

## Cross-Module Links
- 📖 [Domain Knowledge Complete Reference](03_domain-knowledge.md)
- 📖 [High-Yield Question Bank](06_question-bank.md)
- 📖 [Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Full Mock Assessment](12_mock-assessment.md)
- 📖 [Risk Analytics Practice Cases](../risk/07_practice-and-cases.md)

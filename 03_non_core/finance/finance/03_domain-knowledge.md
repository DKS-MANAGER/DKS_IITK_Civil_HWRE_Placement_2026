# 03. General Finance: Accounting, Corporate Finance, Valuation & Financial Markets

> **Scope**: Master reference guide covering Financial Accounting, Corporate Finance, Statement Analysis, Valuation Modeling, and Banking & Capital Markets for campus finance interviews. `[PREPARATION HEURISTIC]`

---

## 1. Accounting Fundamentals & The Three Financial Statements

### 1.1 The Core Purpose of Each Statement
* **Income Statement (P&L)**: Measures economic profitability over a specified accounting period (quarter or fiscal year).
  $$\text{Revenue} - \text{Cost of Goods Sold (COGS)} = \text{Gross Profit}$$
  $$\text{Gross Profit} - \text{Operating Expenses (SG\&A, R\&D)} = \text{Operating Income (EBIT)}$$
  $$\text{EBIT} - \text{Interest Expense} = \text{Pre-Tax Income (EBT)}$$
  $$\text{EBT} - \text{Tax Expense} = \text{Net Income}$$
* **Balance Sheet**: Snapshot of financial condition at a single specific date:
  $$\text{Assets} = \text{Liabilities} + \text{Shareholders' Equity}$$
  - *Current Assets*: Cash, Accounts Receivable (AR), Inventory, Prepaid Expenses (liquidated within 1 year).
  - *Non-Current Assets*: Property, Plant & Equipment (PP&E), Intangibles, Goodwill.
  - *Current Liabilities*: Accounts Payable (AP), Accrued Expenses, Short-Term Debt.
  - *Non-Current Liabilities*: Long-Term Bonds, Deferred Tax Liabilities.
  - *Shareholders' Equity*: Common Stock, Additional Paid-In Capital (APIC), Retained Earnings.
* **Cash Flow Statement (CFS)**: Tracks actual cash inflows and outflows across three activities:
  - **Cash from Operations (CFO)**: Net Income adjusted for non-cash items (D&A) and changes in Net Working Capital ($\Delta NWC$).
  - **Cash from Investing (CFI)**: Capital Expenditures (CapEx), acquisitions, and purchases/sales of marketable securities.
  - **Cash from Financing (CFF)**: Issuance/repayment of debt, issuance/repurchase of equity, and dividend distributions.

---

### 1.2 Interlinking Mechanics Across the Three Statements

```text
 ┌───────────────────────────┐
 │     INCOME STATEMENT      │
 │  Revenue                  │
 │  - Expenses               │
 │  = Net Income ─────────┐  │
 └────────────────────────┼──┘
                          │ (Starts CFS)
                          ▼
 ┌────────────────────────────────────────┐
 │        CASH FLOW STATEMENT             │
 │  Net Income                            │
 │  + Non-Cash Expenses (D&A) ──────────┐ │
 │  - Δ Net Working Capital (ΔNWC)      │ │
 │  = Cash from Operations (CFO)        │ │
 │  + Cash from Investing (CFI: CapEx)──┼─┼────────┐
 │  + Cash from Financing (CFF)         │ │        │
 │  = Net Change in Cash ─────────────┐ │ │        │
 └────────────────────────────────────┼─┘ │        │
                                      │   │        │
                                      ▼   ▼        ▼
 ┌────────────────────────────────────────────────────────┐
 │                    BALANCE SHEET                       │
 │  ASSETS:                                               │
 │    Cash (Ending Cash from CFS) ◄───────────────────────┘
 │    Accounts Receivable, Inventory                      │
 │    Net PP&E (Previous PP&E + CapEx - D&A) ◄────────────┘
 │  LIABILITIES: Accounts Payable, Total Debt             │
 │  EQUITY:                                               │
 │    Retained Earnings (Beg. RE + Net Income - Dividends)│
 └────────────────────────────────────────────────────────┘
```

#### The Classic Walkthrough: ₹100 Depreciation Increase (Tax Rate = 25%)
1. **Income Statement**:
   - Operating Income (EBIT) decreases by ₹100.
   - Taxes decrease by ₹25 ($₹100 \times 25\%$).
   - Net Income decreases by **₹75**.
2. **Cash Flow Statement**:
   - Net Income begins ₹75 lower.
   - Add back non-cash Depreciation of **+₹100**.
   - Cash Flow from Operations (and Net Change in Cash) increases by **+₹25** (due to the depreciation tax shield).
3. **Balance Sheet**:
   - Assets: Cash increases by **+₹25**. Net PP&E decreases by **-₹100**. Total Assets decrease by **-₹75**.
   - Liabilities & Equity: Retained Earnings decreases by **-₹75** (from lower Net Income).
   - **Balance Check**: Both Assets and Liabilities+Equity change by **-₹75**. The sheet balances perfectly.

---

### 1.3 Accrual vs. Cash Accounting & Earnings Quality
* **Accrual Principle**: Revenue is recognized when performance obligations are satisfied and collection is reasonably assured, regardless of when cash is collected. Expenses are matched to the revenues they generate (Matching Principle).
* **Detecting Earnings Quality Flaws (Red Flags)**:
  - *Net Income Growing while Operating Cash Flow Declines*: Signals aggressive revenue recognition (uncollected AR ballooning) or unsold inventory piling up.
  - *Sudden Lengthening of Days Sales Outstanding (DSO)*: Indicates channel stuffing or customer payment distress.
  - *Capitalizing Operating Costs*: Reclassifying normal operational expenses into CapEx to artificially inflate EBITDA.

---

## 2. Corporate Finance & Capital Budgeting

### 2.1 Time Value of Money (TVM)
* **Future Value (Compounding)**:
  $$FV = PV \times (1 + r)^t$$
* **Present Value (Discounting)**:
  $$PV = \frac{FV}{(1 + r)^t}$$
* **Perpetuity & Growing Perpetuity**:
  $$PV_{\text{perpetuity}} = \frac{C}{r}, \quad PV_{\text{growing perpetuity}} = \frac{C_1}{r - g} \quad (\text{for } r > g)$$

---

### 2.2 Capital Budgeting Decision Rules
* **Net Present Value (NPV)**: Sum of present values of all future incoming cash flows minus initial investment:
  $$\text{NPV} = \sum_{t=1}^n \frac{CF_t}{(1 + r)^t} - CF_0$$
  - *Decision Rule*: Accept project if $\text{NPV} > 0$. NPV is the gold-standard decision rule because it directly measures shareholder wealth creation.
* **Internal Rate of Return (IRR)**: The discount rate at which $\text{NPV} = 0$:
  $$\sum_{t=1}^n \frac{CF_t}{(1 + \text{IRR})^t} - CF_0 = 0$$
  - *Decision Rule*: Accept project if $\text{IRR} > \text{Hurdle Rate / WACC}$.
  - *Pitfalls of IRR*: Assumes interim cash flows are reinvested at the IRR itself (unrealistic for very high IRRs); can yield multiple IRRs when cash flows change signs multiple times.
* **Payback Period**: Time required to recover the initial cash outlay. Ignores time value of money and cash flows occurring after the payback threshold.

---

### 2.3 Cost of Capital (WACC) & Capital Structure
Weighted Average Cost of Capital represents the minimum required return demanded by all capital providers (equity and debt):
$$\text{WACC} = \left(\frac{E}{V} \times K_e\right) + \left(\frac{D}{V} \times K_d \times (1 - T)\right)$$
Where:
- $E$: Market Value of Equity, $D$: Market Value of Debt, $V = E + D$.
- $K_d \times (1 - T)$: After-tax Cost of Debt ($T$: Corporate marginal tax rate; debt interest is tax-deductible).
- $K_e$: Cost of Equity, derived from the **Capital Asset Pricing Model (CAPM)**:
  $$K_e = R_f + \beta \times (R_m - R_f)$$
  - $R_f$: Risk-Free Rate (yield on 10-year Government Treasury Bonds).
  - $R_m - R_f$: Equity Risk Premium (ERP, historical market excess return).
  - $\beta$: Equity Beta (systematic market risk sensitivity).

---

## 3. Financial Statement Analysis & Ratio Frameworks

### 3.1 Profitability & The DuPont Breakdown
* **Gross Margin**: $\frac{\text{Gross Profit}}{\text{Revenue}}$ | **Operating Margin**: $\frac{\text{EBIT}}{\text{Revenue}}$ | **Net Margin**: $\frac{\text{Net Income}}{\text{Revenue}}$
* **Return on Equity (ROE)**: $\frac{\text{Net Income}}{\text{Average Shareholders' Equity}}$
* **The 3-Step DuPont Identity**:
  $$\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Net Profit Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Total Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Total Assets}}{\text{Shareholders' Equity}}}_{\text{Financial Leverage}}$$
  - Decomposes whether high ROE is driven by operational pricing power (Margin), efficient asset utilization (Turnover), or risky debt borrowing (Leverage).

### 3.2 Liquidity & Solvency Ratios
* **Current Ratio**: $\frac{\text{Current Assets}}{\text{Current Liabilities}}$ (Benchmark $\ge 1.5\times$).
* **Quick Ratio (Acid-Test)**: $\frac{\text{Cash} + \text{Marketable Securities} + \text{Accounts Receivable}}{\text{Current Liabilities}}$ (Excludes illiquid inventory; benchmark $\ge 1.0\times$).
* **Debt-to-Equity (D/E)**: $\frac{\text{Total Debt}}{\text{Total Shareholders' Equity}}$.
* **Interest Coverage Ratio**: $\frac{\text{EBIT}}{\text{Interest Expense}}$ (Measures debt servicing safety margin; $<1.5\times$ indicates high financial distress risk).

### 3.3 Working Capital Cycle (Cash Conversion Cycle - CCC)
Measures the days elapsed between paying suppliers for raw materials and collecting cash from customers:
$$\text{CCC} = \text{Days Inventory Outstanding (DIO)} + \text{Days Sales Outstanding (DSO)} - \text{Days Payable Outstanding (DPO)}$$
Where:
$$\text{DIO} = \frac{\text{Average Inventory}}{\text{COGS}} \times 365, \quad \text{DSO} = \frac{\text{Average Accounts Receivable}}{\text{Total Revenue}} \times 365, \quad \text{DPO} = \frac{\text{Average Accounts Payable}}{\text{COGS}} \times 365$$
* A **negative CCC** (e.g., Amazon, Dell, DMart) means the company collects cash from customers before paying suppliers, effectively generating free interest-free working capital.

---

## 4. Valuation Fundamentals: DCF & Comparable Multiples

### 4.1 Enterprise Value vs. Equity Value Bridge
$$\text{Enterprise Value (EV)} = \text{Equity Value} + \text{Total Debt} + \text{Preferred Stock} + \text{Non-Controlling Interests} - \text{Cash and Equivalents}$$
* **Enterprise Value (EV)**: Value of the core operating business attributed to *all* capital providers (debt + equity).
* **Equity Value (Market Cap)**: Value attributed *strictly* to common equity shareholders after debt is paid off.
* **Golden Rule of Multiples**: Numerator and denominator must match capital claims:
  - $\frac{\text{Enterprise Value}}{\text{Revenue}}$ and $\frac{\text{Enterprise Value}}{\text{EBITDA}}$ are valid because Revenue and EBITDA are pre-debt operating figures.
  - $\frac{\text{Equity Value}}{\text{Net Income}}$ ($\text{P/E}$) is valid because Net Income is an after-debt metric.
  - $\frac{\text{Enterprise Value}}{\text{Net Income}}$ is **strictly invalid** (mismatches enterprise numerator with equity-only denominator).

---

### 4.2 Discounted Cash Flow (DCF) Modeling
DCF calculates the intrinsic value of a firm as the present value of its future Free Cash Flows:

$$\text{Enterprise Value} = \sum_{t=1}^n \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{Terminal Value}_n}{(1 + \text{WACC})^n}$$

#### Calculating Unlevered Free Cash Flow (FCFF):
$$\text{FCFF} = \text{EBIT} \times (1 - T) + \text{Depreciation \& Amortization} - \text{Capital Expenditures (CapEx)} - \Delta \text{Net Working Capital}$$

#### Calculating Terminal Value (TV):
1. **Gordon Growth Method**:
   $$\text{Terminal Value}_n = \frac{\text{FCFF}_{n} \times (1 + g)}{\text{WACC} - g}$$
   - *Constraint*: Long-term terminal growth rate $g$ must not exceed the long-term GDP growth rate of the economy (typically $2\% - 4\%$).
2. **Exit Multiple Method**:
   $$\text{Terminal Value}_n = \text{EBITDA}_n \times \text{Target EV/EBITDA Multiple}$$

---

## 5. Financial Markets, Banking & Debt Instruments

### 5.1 Bond Mechanics & Interest Rate Risk
* **Bond Pricing Identity**:
  $$P_{\text{bond}} = \sum_{t=1}^n \frac{C}{(1 + y)^t} + \frac{M}{(1 + y)^n}$$
  Where $C$ is coupon payment, $M$ is par value, and $y$ is Yield to Maturity (YTM).
* **Price-Yield Inverse Relationship**: When market interest rates rise, bond prices fall; when rates drop, bond prices rise.
* **Duration**:
  - *Macaulay Duration*: Weighted average maturity of cash flows (measured in years).
  - *Modified Duration*: Percentage price sensitivity to a $1\%$ change in interest rates:
    $$\% \Delta P \approx -\text{Modified Duration} \times \Delta y$$

### 5.2 Commercial Banking Economics
* **Net Interest Margin (NIM)**:
  $$\text{NIM} = \frac{\text{Interest Income (from loans)} - \text{Interest Expense (to deposits)}}{\text{Average Earning Assets}}$$
* **Current Account Savings Account (CASA) Ratio**: $\frac{\text{CASA Deposits}}{\text{Total Deposits}}$. Higher CASA ratio provides banks with low-cost funding, driving higher NIM.
* **Credit Spread**: Difference in yield between a corporate loan/bond and a risk-free government bond of identical maturity, compensating the lender for default risk.

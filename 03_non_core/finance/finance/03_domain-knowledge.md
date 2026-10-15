# 03. Financial Accounting, Corporate Finance, Valuation & Capital Markets

> **Scope**: Master reference textbook covering Financial Accounting Mechanics, 3-Statement Modeling, Ratio Analysis, Corporate Finance, Business Valuation (DCF & Multiples), M&A Accretion/Dilution, LBOs, FP&A, and Banking Economics for campus placements. `[PREPARATION HEURISTIC]`

---

## 1. Accounting Fundamentals & The Three Financial Statements

### 1.1 The Accounting Equation & Double-Entry Bookkeeping
At the foundation of all financial reporting is the fundamental balance sheet equality:
$$\text{Assets} = \text{Liabilities} + \text{Shareholders' Equity}$$

* **Economic Meaning**:
  * **Assets**: Economic resources owned or controlled by the enterprise that are expected to produce future economic benefits (cash, receivables, inventory, machinery, patents).
  * **Liabilities**: Contractual obligations of the enterprise arising from past events, the settlement of which requires an outflow of resources (bank debt, supplier payables, accrued wages, deferred revenue).
  * **Shareholders' Equity**: Residual interest in the assets of the entity after deducting all its liabilities (common stock, additional paid-in capital, retained earnings).
* **The Double-Entry Rule**: Every economic transaction must impact at least two accounts such that total debits equal total credits, preserving the accounting equality.
  * *Debit ($Dr$)*: Increases an Asset or Expense account; Decreases a Liability, Equity, or Revenue account.
  * *Credit ($Cr$)*: Increases a Liability, Equity, or Revenue account; Decreases an Asset or Expense account.

---

### 1.2 Accrual vs. Cash Accounting & Revenue Recognition
* **Cash Accounting**: Recognizes revenue strictly when cash is physically received, and expenses when cash is disbursed. Prohibited by major accounting standards (IFRS, Ind-AS, US GAAP) for formal corporate reporting.
* **Accrual Accounting**:
  * **Revenue Recognition Principle (IFRS 15 / Ind-AS 115)**: Revenue is recognized when performance obligations are satisfied and the customer obtains control of the good or service, regardless of when cash is collected.
  * **Matching Principle**: Expenses incurred to generate revenues must be recognized in the same accounting period as the associated revenues.
* **Key Working Capital Accruals**:
  * **Accounts Receivable ($AR$)**: Revenue recognized, but cash not yet collected from customer.
  * **Deferred (Unearned) Revenue**: Cash collected in advance, but performance obligations not yet fulfilled (recorded as a Current Liability).
  * **Prepaid Expenses**: Cash paid in advance for future services (recorded as a Current Asset).
  * **Accrued Expenses**: Operating expenses incurred but cash not yet disbursed to vendors/employees (recorded as a Current Liability).

---

### 1.3 The Three Core Financial Statements

```text
 ┌───────────────────────────┐
 │     INCOME STATEMENT      │
 │  Revenue                  │
 │  - Cost of Goods Sold     │
 │  = Gross Profit           │
 │  - Operating Exp (SG&A)   │
 │  = Operating Income (EBIT)│
 │  - Interest Expense       │
 │  = Pre-Tax Income (EBT)   │
 │  - Income Tax Expense     │
 │  = Net Income ─────────┐  │
 └────────────────────────┼──┘
                          │ (Feeds Top of CFS)
                          ▼
 ┌────────────────────────────────────────┐
 │        CASH FLOW STATEMENT             │
 │  Operating Cash Flow (CFO):            │
 │    Net Income                          │
 │    + Depreciation & Amortization ────┐ │
 │    - Δ Net Working Capital (ΔNWC)    │ │
 │  Investing Cash Flow (CFI):          │ │
 │    - Capital Expenditures (CapEx)────┼─┼────────┐
 │  Financing Cash Flow (CFF):          │ │        │
 │    + Net Borrowing - Dividends       │ │        │
 │  = Net Change in Cash ─────────────┐ │ │        │
 └────────────────────────────────────┼─┘ │        │
                                      │   │        │
                                      ▼   ▼        ▼
 ┌────────────────────────────────────────────────────────┐
 │                    BALANCE SHEET                       │
 │  ASSETS:                                               │
 │    Cash (Prior Cash + Net Change from CFS) ◄───────────┘
 │    Accounts Receivable, Inventory                      │
 │    Net PP&E (Beginning PP&E + CapEx - D&A) ◄───────────┘
 │  LIABILITIES: Accounts Payable, Bank Debt              │
 │  EQUITY:                                               │
 │    Retained Earnings (Beginning RE + Net Income - Div) │
 └────────────────────────────────────────────────────────┘
```

#### A. Income Statement (P&L)
Measures economic performance over a specified time duration:
$$\text{Revenue} - \text{COGS} = \text{Gross Profit}$$
$$\text{Gross Profit} - \text{SG\&A} - \text{R\&D} = \text{EBITDA} - \text{D\&A} = \text{Operating Income (EBIT)}$$
$$\text{EBIT} - \text{Interest Expense} + \text{Interest Income} = \text{Pre-Tax Income (EBT)}$$
$$\text{EBT} - \text{Tax Expense} = \text{Net Income}$$

#### B. Balance Sheet
Point-in-time snapshot of cumulative financial condition:
* **Current Assets** ($< 1$ year): Cash & Cash Equivalents, Short-term Marketable Securities, Accounts Receivable, Inventory, Prepaid Expenses.
* **Non-Current Assets** ($> 1$ year): Property, Plant & Equipment (PP&E), Intangibles (patents, software), Goodwill.
* **Current Liabilities** ($< 1$ year): Accounts Payable, Accrued Liabilities, Short-term Borrowings, Current Portion of Long-term Debt.
* **Non-Current Liabilities** ($> 1$ year): Long-term Senior Debt, Deferred Tax Liabilities, Pension Obligations.
* **Shareholders' Equity**: Common Share Capital, Additional Paid-In Capital (APIC), Retained Earnings.

#### C. Cash Flow Statement (CFS)
Reconciles accrual Net Income to physical cash generated across three activities:
1. **Cash Flow from Operations (CFO)**: Uses the **indirect method**:
   $$\text{CFO} = \text{Net Income} + \text{Non-Cash Charges (D\&A)} - \Delta \text{Operating NWC}$$
2. **Cash Flow from Investing (CFI)**: Capital Expenditures (CapEx), business acquisitions, investments in financial assets.
3. **Cash Flow from Financing (CFF)**: Issuance or repayment of long-term debt, issuance of equity, share repurchases, dividend payouts.

---

### 1.4 Step-by-Step Three-Statement Transaction Walkthroughs

#### Walkthrough 1: ₹100 Increase in Depreciation (Corporate Tax Rate = 25%)
1. **Income Statement**:
   * Operating Expenses increase by ₹100 (non-cash depreciation).
   * Operating Income ($EBIT$) decreases by ₹100.
   * Assuming positive taxable income, Taxes decrease by ₹25 ($₹100 \times 25\%$).
   * Net Income decreases by **-₹75**.
2. **Cash Flow Statement**:
   * Net Income starts **-₹75** lower.
   * Non-cash depreciation is added back: **+₹100**.
   * CFO increases by **+₹25** (due to the depreciation tax shield: ₹100 $\times 25\%$).
   * CFI and CFF are unaffected. Net ending cash increases by **+₹25**.
3. **Balance Sheet**:
   * **Assets**: Cash increases by **+₹25**. Net PP&E decreases by **-₹100**. Net change in Total Assets: **-₹75**.
   * **Liabilities & Equity**: Liabilities unchanged ($₹0$). Shareholders' Equity decreases by **-₹75** via Retained Earnings (from lower Net Income).
   * **Balance Check**: Assets ($-₹75$) = Liabilities ($0$) + Equity ($-₹75$). The sheet balances perfectly.
   * *Critical Tax Nuance*: If the company is unprofitable ($EBT < 0$) and cannot utilize tax deductions immediately, taxes do not decrease. Net Income drops by ₹100, add-back is +₹100, Net Cash impact is **₹0**, and a Deferred Tax Asset (DTA) of ₹25 is created.

#### Walkthrough 2: Sale of Machine for ₹120 Cr (Historical Cost = ₹180 Cr, Accumulated Depreciation = ₹100 Cr, Tax Rate = 25%)
1. **Accounting Calculations**:
   * Net Book Value ($NBV$) of machine $= \text{Cost} - \text{Acc. Dep} = 180 - 100 = ₹80\text{ Cr}$.
   * Sale proceeds $= ₹120\text{ Cr}$.
   * Pre-tax Gain on Sale $= \text{Proceeds} - NBV = 120 - 80 = +₹40\text{ Cr}$.
   * Tax on Gain $= 40 \times 25\% = ₹10\text{ Cr}$.
2. **Income Statement**:
   * Pre-tax Income increases by **+₹40 Cr** (Gain on Sale).
   * Taxes increase by **+₹10 Cr**.
   * Net Income increases by **+₹30 Cr**.
3. **Cash Flow Statement**:
   * CFO starts with Net Income: **+₹30 Cr**.
   * Subtract the non-operating Gain on Sale: **-₹40 Cr** (to prevent double counting with CFI proceeds).
   * Net CFO $= 30 - 40 =$ **-₹10 Cr** (reflects tax paid on gain).
   * CFI records full gross cash proceeds: **+₹120 Cr** (sale of PP&E).
   * Net change in cash $= -10 + 120 =$ **+₹110 Cr**.
4. **Balance Sheet**:
   * **Assets**: Cash increases by **+₹110 Cr**. Net PP&E decreases by **-₹80 Cr** (derecognition of machine NBV). Total Assets increase by **+₹30 Cr**.
   * **Liabilities & Equity**: Liabilities unchanged ($₹0$). Retained Earnings increases by **+₹30 Cr** (from higher Net Income).
   * **Balance Check**: Assets ($+₹30\text{ Cr}$) = Liabilities ($0$) + Equity ($+₹30\text{ Cr}$). Balances perfectly.

#### Walkthrough 3: Customer Pays ₹200 Cr Cash Advance for Multi-Year Contract
1. **Income Statement**: **₹0 impact**. No performance obligations have been satisfied; revenue cannot be recognized yet.
2. **Cash Flow Statement**:
   * CFO starts with Net Income $0$.
   * Increase in Deferred Revenue (Current Liability) is a positive cash inflow: **+₹200 Cr**.
   * Net change in cash: **+₹200 Cr**.
3. **Balance Sheet**:
   * **Assets**: Cash increases by **+₹200 Cr**.
   * **Liabilities**: Deferred (Unearned) Revenue increases by **+₹200 Cr**. Equity unchanged ($0$).
   * **Balance Check**: Assets ($+₹200\text{ Cr}$) = Liabilities ($+₹200\text{ Cr}$) + Equity ($0$). Balances perfectly.

---

### 1.5 Accounting Profit vs. EBITDA vs. CFO vs. Free Cash Flow (FCFF)

| Metric | Formula | What It Measures | Ignores / Key Blindspot |
| :--- | :--- | :--- | :--- |
| **Net Income** | Revenues - All Expenses | Accounting profit available to equity holders. | Non-cash accruals, working capital lockups, debt principal paydown. |
| **EBITDA** | Operating Income + D&A | Core operating cash generation proxy; capital-structure neutral. | CapEx requirements, tax obligations, working capital investment. |
| **Cash from Operations (CFO)** | Net Income + Non-Cash - $\Delta NWC$ | Actual physical cash generated from operating trade activities. | Reinvestment required to maintain physical PP&E (CapEx). |
| **Unlevered Free Cash Flow (FCFF)** | $\text{EBIT}(1-T) + \text{D\&A} - \text{CapEx} - \Delta NWC$ | Pure discretionary cash available to all capital providers (debt + equity). | None; standard gold standard for DCF valuation. |

---

## 2. Financial Statement Analysis & Ratio Frameworks

### 2.1 The DuPont Identity: Decomposing Return on Equity (ROE)
Return on Equity measures how efficiently management converts shareholders' invested capital into accounting profit:
$$\text{ROE} = \frac{\text{Net Income}}{\text{Average Shareholders' Equity}}$$

#### A. The 3-Step DuPont Breakdown
$$\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{Revenue}}}_{\text{Net Profit Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Total Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Total Assets}}{\text{Shareholders' Equity}}}_{\text{Equity Multiplier (Financial Leverage)}}$$

* **Economic Interpretation**:
  * **Net Profit Margin**: Pricing power and operating cost discipline (Efficiency).
  * **Asset Turnover**: Asset efficiency—how many rupees of sales are generated per rupee of assets deployed (Productivity).
  * **Equity Multiplier**: Degree of financial debt leverage used to magnify returns (Risk).

#### B. The 5-Step DuPont Breakdown
$$\text{ROE} = \underbrace{\frac{\text{Net Income}}{\text{EBT}}}_{\text{Tax Burden (1 - Tax Rate)}} \times \underbrace{\frac{\text{EBT}}{\text{EBIT}}}_{\text{Interest Burden}} \times \underbrace{\frac{\text{EBIT}}{\text{Revenue}}}_{\text{Operating Margin}} \times \underbrace{\frac{\text{Revenue}}{\text{Assets}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Assets}}{\text{Equity}}}_{\text{Leverage}}$$

---

### 2.2 Liquidity, Solvency & Coverage Ratios

| Category | Ratio | Formula | Benchmark & Practical Interpretation |
| :--- | :--- | :--- | :--- |
| **Liquidity** | **Current Ratio** | $\frac{\text{Current Assets}}{\text{Current Liabilities}}$ | Healthy: $1.5\times - 2.0\times$. Below $1.0\times$ signals near-term refinancing risk. |
| | **Quick Ratio (Acid-Test)** | $\frac{\text{Cash} + \text{Marketable Sec} + \text{AR}}{\text{Current Liabilities}}$ | Excludes illiquid inventory. Healthy: $\ge 1.0\times$. |
| | **Cash Ratio** | $\frac{\text{Cash} + \text{Marketable Securities}}{\text{Current Liabilities}}$ | Extreme liquidity buffer. |
| **Solvency** | **Debt-to-Equity (D/E)** | $\frac{\text{Total Debt}}{\text{Total Equity}}$ | Highly industry-specific ($0.5\times$ for Tech, $3.0\times$ for Power/Utilities). |
| | **Net Debt / EBITDA** | $\frac{\text{Total Debt} - \text{Cash}}{\text{EBITDA}}$ | Gold-standard leverage metric. $< 2.0\times$ is conservative; $> 4.0\times$ is high risk. |
| **Coverage** | **Interest Coverage** | $\frac{\text{EBIT}}{\text{Interest Expense}}$ | Ability to service debt. Below $1.5\times$ triggers bank covenant distress. |
| | **Fixed Charge Coverage** | $\frac{\text{EBIT} + \text{Lease Payments}}{\text{Interest} + \text{Lease Payments}}$ | Includes mandatory operating lease obligations. |

---

### 2.3 The Cash Conversion Cycle (CCC)
The Cash Conversion Cycle measures the elapsed days between paying vendors for raw materials and receiving cash from end customers:
$$\text{CCC} = \text{Days Inventory Outstanding (DIO)} + \text{Days Sales Outstanding (DSO)} - \text{Days Payable Outstanding (DPO)}$$

$$\text{DIO} = \frac{\text{Average Inventory}}{\text{COGS}} \times 365$$
$$\text{DSO} = \frac{\text{Average Accounts Receivable}}{\text{Total Revenue}} \times 365$$
$$\text{DPO} = \frac{\text{Average Accounts Payable}}{\text{COGS}} \times 365$$

* **Working Capital Optimization**:
  * A **negative CCC** (e.g., Apple, Amazon, DMart) means the company collects cash from retail consumers within days, while enjoying 60–90 day payment terms with suppliers. The company operates on **free customer-funded working capital**.
  * **Quantifying Liquidity Impact**: If a company with ₹730 Cr in annual sales reduces DSO from 60 days to 45 days:
    $$\Delta \text{Cash Released} = \frac{60 - 45}{365} \times 730 = \mathbf{₹30.0\text{ Cr in permanent liquidity}}.$$

---

## 3. Corporate Finance & Capital Budgeting

### 3.1 Time Value of Money (TVM)
Money available today is worth more than the identical sum in the future due to its earning capacity:
* **Future Value (Compounding)**: $FV = PV \times (1 + r)^t$
* **Present Value (Discounting)**: $PV = \frac{FV}{(1 + r)^t}$
* **Ordinary Annuity**: Cash flow $C$ received at the end of each period for $t$ periods:
  $$PV_{\text{annuity}} = C \times \left[ \frac{1 - (1 + r)^{-t}}{r} \right]$$
* **Perpetuity**: Constant cash flow $C$ received indefinitely: $PV = \frac{C}{r}$.
* **Growing Perpetuity**: Cash flow growing at constant rate $g$ ($r > g$):
  $$PV_{\text{growing}} = \frac{C_1}{r - g}$$

---

### 3.2 Capital Budgeting Decision Rules & NPV vs. IRR Conflicts

#### A. Net Present Value (NPV)
$$\text{NPV} = \sum_{t=1}^n \frac{CF_t}{(1 + r)^t} - CF_0$$
* **Decision Rule**: Accept project if $\text{NPV} > 0$. NPV directly measures absolute shareholder wealth addition in currency units.

#### B. Internal Rate of Return (IRR)
The discount rate at which project $\text{NPV} = 0$:
$$\sum_{t=1}^n \frac{CF_t}{(1 + \text{IRR})^t} - CF_0 = 0$$
* **Decision Rule**: Accept if $\text{IRR} > \text{Cost of Capital (WACC)}$.

#### C. The Classical NPV vs. IRR Conflict
When evaluating **mutually exclusive** projects, NPV and IRR frequently recommend opposing projects due to:
1. **Reinvestment Rate Assumption**:
   * **NPV assumes interim cash flows are reinvested at the Cost of Capital (WACC)**—economically realistic.
   * **IRR assumes interim cash flows are reinvested at the IRR itself**—severely distorts projects with high IRRs (e.g., assuming a 45% IRR project reinvests cash at 45%).
2. **Scale Disparity**: Project A (Invest ₹100, Return ₹150 in 1 yr $\implies \text{IRR} = 50\%$, $\text{NPV}_{10\%} = ₹36.36$). Project B (Invest ₹10,000, Return ₹13,000 in 1 yr $\implies \text{IRR} = 30\%$, $\text{NPV}_{10\%} = ₹1,818.18$). IRR chooses A; NPV correctly chooses B.
* **Firm Principle**: **NPV is always the superior decision rule**.

---

### 3.3 Cost of Capital (WACC) & The Capital Asset Pricing Model (CAPM)
Weighted Average Cost of Capital reflects the blended expected return demanded by all financial capital providers:
$$\text{WACC} = \left(\frac{E}{V} \times K_e\right) + \left(\frac{D}{V} \times K_d \times (1 - T)\right)$$

* **Weights ($E/V$ and $D/V$)**: Must strictly use **Market Values**, not Book Values.
* **Cost of Debt ($K_d$)**: Yield to Maturity (YTM) on current corporate debt. Interest expense is tax-deductible, creating the tax shield multiplier $(1 - T)$.
* **Cost of Equity ($K_e$) via CAPM**:
  $$K_e = R_f + \beta_L \times (R_m - R_f)$$
  * $R_f$: Risk-Free Rate (10-Year Government Treasury Bond yield).
  * $R_m - R_f$: Equity Risk Premium (ERP, historical market excess return, typically $5.5\% - 7.0\%$ in India).
  * $\beta_L$: Levered Equity Beta (systematic market risk sensitivity).

#### Un-levering and Re-levering Beta (Hamada's Equation):
To estimate beta for an unlisted or private firm from listed peer comparables:
1. **Un-lever Peer Betas** (isolate pure business risk):
   $$\beta_U = \frac{\beta_L}{1 + (1 - T) \times \left(\frac{D}{E}\right)}$$
2. **Re-lever to Target Capital Structure**:
   $$\beta_{L,\text{target}} = \beta_U \times \left[1 + (1 - T_{\text{target}}) \times \left(\frac{D}{E}\right)_{\text{target}}\right]$$

---

## 4. Valuation Fundamentals: DCF & Comparable Multiples

### 4.1 Enterprise Value vs. Equity Value Bridge
$$\text{Enterprise Value (EV)} = \text{Equity Value} + \text{Total Debt} + \text{Preferred Stock} + \text{Non-Controlling Interests} - \text{Cash \& Equivalents}$$

```text
 ┌────────────────────────────────────────────────────────┐
 │            ENTERPRISE VALUE (OPERATING ASSETS)         │
 │  Value of core business operations to ALL capital      │
 │  providers (Debt + Equity + Preferred).                │
 └───────────────────────────┬────────────────────────────┘
                             │
       ┌─────────────────────┴─────────────────────┐
       ▼                                           ▼
┌──────────────┐                            ┌──────────────┐
│  TOTAL DEBT  │                            │ EQUITY VALUE │
│  + Preferred │                            │ (MARKET CAP) │
│  + NCI       │                            │ Value to     │
│  - CASH      │                            │ Common       │
│  = NET DEBT  │                            │ Shareholders │
└──────────────┘                            └──────────────┘
```

* **Golden Rule of Multiples**:
  * If the numerator is **Enterprise Value**, the denominator must be a **pre-debt metric** ($EV / \text{Revenue}$, $EV / \text{EBITDA}$, $EV / \text{EBIT}$).
  * If the numerator is **Equity Value** (or Share Price), the denominator must be a **post-debt metric** ($P/E$, $P/B$, $\text{Equity Value} / \text{FCFE}$).
  * A multiple like $EV / \text{Net Income}$ is **mathematically invalid** because it mismatches enterprise value with equity-only earnings.

---

### 4.2 Discounted Cash Flow (DCF) Modeling
Intrinsic valuation models the enterprise value as the present value of future Unlevered Free Cash Flows plus Terminal Value:
$$\text{Enterprise Value} = \sum_{t=1}^n \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{Terminal Value}_n}{(1 + \text{WACC})^n}$$

#### Calculating Unlevered Free Cash Flow (FCFF):
$$\text{FCFF} = \underbrace{\text{EBIT} \times (1 - T)}_{\text{NOPAT}} + \text{D\&A} - \text{CapEx} - \Delta \text{NWC}$$

#### Terminal Value Methods:
1. **Gordon Growth Perpetuity Method**:
   $$\text{Terminal Value}_n = \frac{\text{FCFF}_{n} \times (1 + g)}{\text{WACC} - g}$$
   * *Economic Boundary*: Long-term terminal growth rate $g$ must never exceed the sustainable long-term nominal GDP growth rate ($2\% - 4\%$ developed, $4\% - 6\%$ developing).
2. **Exit Multiple Method**:
   $$\text{Terminal Value}_n = \text{EBITDA}_n \times \text{Target EV/EBITDA Multiple}$$

---

### 4.3 Relative Valuation (Trading & Transaction Comparables)
* **Trading Comps**: Values a company based on public market trading multiples of comparable listed peers. Reflects minority, non-control market pricing.
* **Precedent Transactions**: Values a company based on multiples paid in historical M&A acquisitions. Includes an **M&A Control Premium** (typically $20\% - 30\%$ above unaffected share price).
* **Key Multiples Compared**:
  * **EV/EBITDA**: Most popular; neutral to capital structure, depreciation methods, and tax jurisdictions.
  * **EV/EBIT**: Superior for capital-intensive firms where ongoing depreciation represents real economic CapEx needs.
  * **P/E (Price-to-Earnings)**: Widely cited by equity research; sensitive to financial leverage.
  * **PEG Ratio**: $\frac{P/E}{\text{Annual EPS Growth Rate (\%)}}$. $PEG < 1.0$ indicates potential undervaluation relative to growth.

---

## 5. Financial Markets, Banking & Debt Instruments

### 5.1 Bond Pricing & Duration Mechanics
* **Bond Pricing Equation**:
  $$P_{\text{bond}} = \sum_{t=1}^n \frac{C}{(1 + y)^t} + \frac{M}{(1 + y)^n}$$
  Where $C$ is coupon payment, $M$ is par value, and $y$ is Yield to Maturity (YTM).
* **Inverse Price-Yield Relationship**: Bond prices move inversely to interest rates. When market rates rise, bond prices fall.
* **Macaulay Duration**: The weighted average maturity of cash flows:
  $$D_{\text{mac}} = \frac{\sum_{t=1}^n t \times \frac{CF_t}{(1 + y)^t}}{P_{\text{bond}}}$$
* **Modified Duration**: Percentage price change for a 100 bps shift in yield:
  $$D_{\text{mod}} = \frac{D_{\text{mac}}}{1 + y / m}, \quad \% \Delta P \approx -D_{\text{mod}} \times \Delta y$$

---

### 5.2 Commercial Banking Economics & Bank Balance Sheets
Commercial banks are unique financial institutions that borrow short-term (deposits) and lend long-term (loans):

| Commercial Bank Assets | Commercial Bank Liabilities & Equity |
| :--- | :--- |
| • Cash & Reserve balances with Central Bank (CRR / SLR) | • **CASA Deposits** (Current & Savings Accounts — lowest cost) |
| • Corporate Loans & Commercial Lending | • Term Deposits / Fixed Deposits (higher interest cost) |
| • Retail Mortgages & Auto Loans | • Wholesale Interbank Borrowings |
| • Government Bonds & Treasury Bills | • Subordinated Debt |
| • Other Assets | • **Equity Capital** (Tier 1 Common Equity & Retained Earnings) |

* **Net Interest Margin (NIM)**:
  $$\text{NIM} = \frac{\text{Interest Income (from loans)} - \text{Interest Expense (to deposits)}}{\text{Average Earning Assets}}$$
* **CASA Ratio**: $\frac{\text{CASA Deposits}}{\text{Total Deposits}}$. Banks with higher CASA (e.g., HDFC Bank, SBI, Kotak $\approx 40\% - 45\%$) have a lower cost of funds and enjoy structurally higher NIM ($3.5\% - 4.5\%$).

---

## 6. Specialist Track: Investment Banking, M&A & LBO Modeling

### 6.1 M&A Accretion / Dilution Analysis
Evaluates whether an acquisition increases or decreases the acquirer's post-transaction Earnings Per Share (EPS):
$$\text{Pro-Forma EPS} = \frac{\text{Acquirer Net Income} + \text{Target Net Income} + \text{After-Tax Synergies} - \text{After-Tax Financing Costs}}{\text{Acquirer Shares} + \text{New Shares Issued}}$$

* **Financing Method Comparison**:
  1. **All-Cash Deal**: Accretive if Target After-Tax Net Income exceeds after-tax foregone interest on cash.
  2. **All-Debt Deal**: Accretive if Cost of Debt $(1 - T) < \text{Target Earnings Yield} (E/P = 1/(P/E))$.
  3. **All-Stock Deal (The Rule of Thumb)**:
     * If **Acquirer $P/E >$ Target $P/E$**, the transaction is **Accretive**. (The acquirer pays fewer shares to purchase each rupee of target earnings).
     * If **Acquirer $P/E <$ Target $P/E$**, the transaction is **Dilutive**.

---

### 6.2 Levered Buyout (LBO) Fundamentals
An acquisition financed primarily with borrowed debt capital ($60\% - 80\%$ debt), using the target firm's operating cash flows to pay down debt over a 3–5 year holding period before exiting:

```text
 ┌────────────────────────────────────────────────────────┐
 │           SOURCES & USES OF FUNDS (CLOSING)            │
 ├────────────────────────────┬───────────────────────────┤
 │ SOURCES:                   │ USES:                     │
 │ • Senior Bank Debt (3.0x)  │ • Purchase Target Equity  │
 │ • Subordinated Debt (2.0x) │ • Refinance Existing Debt │
 │ • Sponsor Equity (Check)   │ • Transaction Fees        │
 └────────────────────────────┴───────────────────────────┘
                             │
                             ▼ (3 - 5 Year Hold)
 ┌────────────────────────────────────────────────────────┐
 │ Cash Flow from Operations used to PAY DOWN DEBT.       │
 │ EBITDA expands through operating improvements.         │
 └────────────────────────────┬───────────────────────────┘
                             │
                             ▼ (Exit via Sale / IPO)
 ┌────────────────────────────────────────────────────────┐
 │ Enterprise Value realized pays off remaining low debt. │
 │ Equity Value expands massively -> High Sponsor IRR!    │
 └────────────────────────────────────────────────────────┘
```

* **The 3 Drivers of LBO Returns**:
  1. **Deleveraging (Debt Paydown)**: Free cash flows reduce debt principal, transferring enterprise value directly to equity holders.
  2. **EBITDA Growth**: Operational expansion increases business size.
  3. **Multiple Expansion**: Selling at a higher exit EV/EBITDA multiple than entry.
* **Return Metrics**:
  * **Multiple on Invested Capital (MoIC)**: $\frac{\text{Exit Equity}}{\text{Entry Equity Check}}$.
  * **Internal Rate of Return (IRR)**: Typically target $\ge 20\% - 25\%$ IRR. (Rule of thumb: $2.0\times$ MoIC in 3 years $\approx 26\%$ IRR; $2.0\times$ in 5 years $\approx 15\%$ IRR).

---

## 7. Specialist Track: Corporate Finance & FP&A

### 7.1 Budgeting, Planning & Rolling Forecasts
Corporate FP&A manages the financial heartbeat of operating enterprises:
* **Annual Operating Plan (AOP)**: Fixed operational budget prepared annually.
* **Rolling Forecast (e.g., $4+8$, $6+6$ Forecast)**: Combines actual performance from elapsed months with revised forecasts for remaining months.
* **Cost Structure Modeling**:
  * **Fixed Costs**: Rent, corporate salaries, depreciation (unaffected by short-term volume).
  * **Variable Costs**: Direct materials, sales commissions, packaging (scale linearly with volume).
  * **Contribution Margin**: $\text{Revenue} - \text{Variable Costs}$.
  * **Breakeven Volume**: $\frac{\text{Total Fixed Costs}}{\text{Unit Contribution Margin}}$.

---

### 7.2 Price-Volume-Mix (PVM) Variance Analysis
Decomposes revenue variance between Budget and Actual into operational drivers:
$$\text{Total Revenue Variance} = \text{Actual Revenue} - \text{Budget Revenue}$$
1. **Price Variance**: Impact of selling at different unit prices:
   $$\text{Price Variance} = (P_{\text{actual}} - P_{\text{budget}}) \times Q_{\text{actual}}$$
2. **Volume Variance**: Impact of selling different quantities:
   $$\text{Volume Variance} = (Q_{\text{actual}} - Q_{\text{budget}}) \times P_{\text{budget}}$$
3. **Mix Variance**: Impact of shifts in the proportion of higher-margin vs lower-margin products sold.

---

## 8. Specialist Track: Banking Analytics & Financial Data

### 8.1 Customer Delinquency & Cohort Vintage Analysis
In credit card and retail lending analytics, portfolio quality is monitored across **vintage delinquency curves**:
* **Delinquency Buckets**:
  * Bucket 0: Current (zero days past due).
  * Bucket 1: 1–29 Days Past Due (DPD).
  * Bucket 2: 30–59 DPD.
  * Bucket 3: 60–89 DPD.
  * Bucket 4: 90+ DPD (Non-Performing Asset / Default threshold).
* **Roll Rate Matrix**: Probability of an account transitioning from Bucket $i$ to Bucket $i+1$ in a 30-day billing cycle.
* **Vintage Tracking**: Tracking cumulative default rates of accounts originated in the same month ($t=0, 6, 12, 18, 24$ months on book) to detect loose underwriting standards.

# 06. Finance & FinTech: High-Yield Question Bank

> Categorized technical interview questions with model answers, mathematical proofs, step-by-step adjustments, and interviewer follow-up probes for IIT Kanpur placement preparation.

---

## Table of Contents
1. [Category 1: Accounting & 3-Statement Linking](#category-1-accounting--3-statement-linking) (Q1–Q6)
2. [Category 2: Corporate Finance, Capital Budgeting & TVM](#category-2-corporate-finance-capital-budgeting--tvm) (Q7–Q12)
3. [Category 3: Financial Ratios & Performance Diagnosis](#category-3-financial-ratios--performance-diagnosis) (Q13–Q18)
4. [Category 4: Valuation, DCF & Trading Multiples](#category-4-valuation-dcf--trading-multiples) (Q19–Q24)
5. [Category 5: Financial Markets, Banking Economics & Fixed Income](#category-5-financial-markets-banking-economics--fixed-income) (Q25–Q28)
6. [Category 6: Strategic M&A & Engineering Background Defense](#category-6-strategic-ma--engineering-background-defense) (Q29–Q32)

---

## Category 1: Accounting & 3-Statement Linking

### Q1: [P0][ACCOUNTING] Walk me through how a ₹100 increase in depreciation affects the 3 financial statements assuming a 25% corporate tax rate.

**Direct Model Answer:**
1. **Income Statement**:
   - Operating Expenses increase by ₹100 (depreciation).
   - Operating Income ($EBIT$) drops by ₹100.
   - Assuming taxable income decreases by ₹100, Taxes decrease by ₹25 ($₹100 \times 25\%$).
   - Net Income decreases by **₹75** ($₹100 - ₹25$).
2. **Cash Flow Statement**:
   - Cash Flow from Operations ($CFO$) starts with Net Income: **-₹75**.
   - Non-cash depreciation is added back: **+₹100**.
   - Net change in Operating Cash Flow: **+₹25** (due to the depreciation tax shield).
   - Cash Flow from Investing ($CFI$) and Financing ($CFF$) are unaffected.
   - Net change in Ending Cash: **+₹25**.
3. **Balance Sheet**:
   - **Assets**: Cash is up by **+₹25**. Net Property, Plant & Equipment ($PP\&E$) decreases by **-₹100**. Net change in Total Assets: **-₹75**.
   - **Liabilities & Equity**: No change in liabilities. Shareholders' Equity decreases by **-₹75** through Retained Earnings (driven by the ₹75 decline in Net Income).
   - **Check**: Total Assets ($-₹75$) = Total Liabilities ($₹0$) + Shareholders' Equity ($-₹75$). The balance sheet balances.

**Interviewer Probes & Edge Cases:**
- *Follow-up*: What happens if the corporate tax rate is 0%?
  - *Answer*: Net income decreases by ₹100. On the CFS, adding back ₹100 results in ₹0 change in cash. On the Balance Sheet, PP&E drops by ₹100 and Retained Earnings drops by ₹100. There is zero cash benefit because there is no tax shield.
- *Follow-up*: Does this adjustment impact EBITDA?
  - *Answer*: No. EBITDA adds back Depreciation and Amortization, so EBITDA is unchanged.

---

### Q2: [P0][ACCOUNTING] A company purchases ₹200 of machinery: ₹50 in cash and ₹150 funded via a 5-year bank term loan. How do the 3 statements change immediately at transaction close?

**Direct Model Answer:**
1. **Income Statement**:
   - **₹0 impact**. No revenue or operating expense has been incurred yet. No interest expense has accrued at the instantaneous moment of closing.
2. **Cash Flow Statement**:
   - $CFO$: Unchanged ($₹0$).
   - $CFI$: Capital Expenditure ($CapEx$) outflow of **-₹200** (purchase of PP&E).
   - $CFF$: Debt proceeds inflow of **+₹150** (new term loan borrowing).
   - Net change in Cash: $-₹200 + ₹150 =$ **-₹50**.
3. **Balance Sheet**:
   - **Assets**: Cash drops by **-₹50**. Gross PP&E increases by **+₹200**. Total Assets increase by **+₹150**.
   - **Liabilities & Equity**: Long-Term Debt increases by **+₹150**. Equity is unchanged ($₹0$).
   - **Check**: Total Assets ($+₹150$) = Liabilities ($+₹150$) + Equity ($₹0$). Balances perfectly.

---

### Q3: [P1][ACCOUNTING] A client pays ₹120 in advance for a 12-month software subscription on January 1. How does this flow through the statements in Q1 (first 3 months), assuming a 25% tax rate?

**Direct Model Answer:**
1. **Initial Day (Jan 1)**:
   - Cash increases by +₹120 ($CFO$ +₹120). Unearned / Deferred Revenue (Liability) increases by +₹120. No P&L impact.
2. **At the end of Q1 (March 31)**:
   - *Income Statement*: Company recognizes 3 months of revenue: $\frac{3}{12} \times ₹120 = ₹30$.
   - Pre-tax income increases by ₹30. Taxes at 25% = ₹7.50. Net Income increases by **+₹22.50**.
   - *Cash Flow Statement*: Net Income starts at +₹22.50.
   - Deferred Revenue decreased from ₹120 to ₹90 (a ₹30 reduction in current liabilities is a cash drain): **-₹30**.
   - Net Operating Cash Flow: $+₹22.50 - ₹30.00 =$ **-₹7.50** (which reflects the tax paid on the recognized revenue).
   - *Balance Sheet*: Cash decreases by **-₹7.50**. Total Assets: **-₹7.50**.
   - Deferred Revenue drops by **-₹30.00**. Retained Earnings increases by **+₹22.50** (from Net Income).
   - Total Liabilities & Equity: $-₹30.00 + ₹22.50 = -₹7.50$. Balances.

---

### Q4: [P1][ACCOUNTING] Explain why an asset write-down of ₹80 (tax rate 25%) results in a positive cash balance change.

**Direct Model Answer:**
- An asset write-down is a non-cash accounting impairment under standard accounting principles.
- **Income Statement**: Operating expense increases by ₹80 (Impairment Expense). Pre-tax income drops by ₹80. Tax savings = $₹80 \times 25\% = ₹20$. Net Income falls by **-₹60**.
- **Cash Flow Statement**: Net Income starts at -₹60. The non-cash write-down of +₹80 is added back in $CFO$. Net change in Cash: $-₹60 + ₹80 =$ **+₹20**.
- **Economic intuition**: The write-down reduces reported accounting taxable profit, saving ₹20 in actual cash tax outflow to the government.
- **Balance Sheet**: Cash +₹20, Asset (PP&E or Goodwill) -₹80 $\to$ Total Assets **-₹60**. Retained Earnings **-₹60**. Balances.

---

### Q5: [P0][ACCOUNTING] If you could only use two financial statements to evaluate a company's financial health, which two would you pick and why?

**Direct Model Answer:**
- **Choice**: The **Balance Sheet** and the **Income Statement** (assuming beginning-of-period and end-of-period Balance Sheets are provided).
- **Justification**:
  1. The Cash Flow Statement can be mathematically reconstructed from two consecutive Balance Sheets and the intervening Income Statement.
  2. Operating cash flows can be derived by adjusting Net Income for non-cash items and changes in working capital accounts ($\Delta \text{AR}$, $\Delta \text{Inventory}$, $\Delta \text{AP}$).
  3. Investing cash flows can be inferred from changes in gross PP&E and asset disposals.
  4. Financing cash flows can be derived from net debt issuance/repayments, equity issuances, and dividend distributions (reconciled through Retained Earnings: $\text{Ending RE} = \text{Beginning RE} + \text{Net Income} - \text{Dividends}$).

---

### Q6: [P1][ACCOUNTING] How does capitalized R&D differ from expensed R&D in terms of financial metrics?

**Direct Model Answer:**
- **Expensed R&D** (standard under US GAAP for most software): Full cost is deducted immediately in operating expenses ($OPEX$). Reduces current-period EBIT, Net Income, and Operating Cash Flow ($CFO$).
- **Capitalized R&D** (allowed under IFRS / Ind-AS for development phase when commercial feasibility is demonstrated):
  - Outlay is booked as an Intangible Asset on the Balance Sheet; cash outflow is classified under Cash Flow from Investing ($CFI$) rather than $CFO$.
  - In subsequent periods, the asset is amortized over its useful life, spreading the expense.
  - **Metric Impact**: Capitalizing R&D artificially inflates current-period EBITDA, Operating Income, and $CFO$, while lowering $CFI$ and increasing Total Assets (reducing Asset Turnover and ROA initially).

---

## Category 2: Corporate Finance, Capital Budgeting & TVM

### Q7: [P0][CORP-FIN] Two mutually exclusive projects have the following cash flows. Project A: Outlay ₹1,000, returns ₹1,500 in Year 1. Project B: Outlay ₹1,000, returns ₹400/yr for 5 years. At an 8% discount rate, which project do you choose? Why can IRR give a conflicting ranking?

**Step-by-Step Calculation:**
1. **Project A**:
   $$\text{NPV}_A = -1000 + \frac{1500}{1.08} = -1000 + 1388.89 = +₹388.89$$
   $$\text{IRR}_A: 0 = -1000 + \frac{1500}{1 + \text{IRR}_A} \implies \text{IRR}_A = \frac{1500 - 1000}{1000} = 50.0\%$$

2. **Project B**:
   $$\text{NPV}_B = -1000 + \sum_{t=1}^5 \frac{400}{(1.08)^t} = -1000 + 400 \times \left[ \frac{1 - (1.08)^{-5}}{0.08} \right] = -1000 + 400 \times 3.99271 = -1000 + 1597.08 = +₹597.08$$
   $$\text{IRR}_B: -1000 + 400 \times \left[ \frac{1 - (1 + \text{IRR}_B)^{-5}}{\text{IRR}_B} \right] = 0 \implies \text{IRR}_B \approx 28.65\%$$

**Analysis & Decision:**
- **Ranking**: $\text{NPV}_B (₹597.08) > \text{NPV}_A (₹388.89)$, but $\text{IRR}_A (50.0\%) > \text{IRR}_B (28.65\%)$.
- **Decision**: Choose **Project B** because NPV measures absolute shareholder wealth creation.
- **Why IRR conflicts**:
  1. *Reinvestment Rate Assumption*: IRR assumes interim cash flows are reinvested at the project's internal rate (50% or 28.65%), which is unrealistic. NPV assumes reinvestment at the opportunity cost of capital (8%).
  2. *Timing of Cash Flows*: Project A delivers cash early (Year 1), boosting IRR, while Project B provides durable value over 5 years.

---

### Q8: [P0][CORP-FIN] Company X has an equity market capitalization of ₹800 Cr and net debt of ₹200 Cr. Risk-free rate is 7.0%, Equity Risk Premium is 6.0%, and Beta is 1.25. Pre-tax cost of debt is 9.0%, and corporate tax rate is 25%. Compute the Weighted Average Cost of Capital (WACC).

**Step-by-Step Calculation:**
1. **Cost of Equity ($K_e$) via CAPM**:
   $$K_e = R_f + \beta \times \text{ERP} = 7.0\% + 1.25 \times 6.0\% = 7.0\% + 7.5\% = 14.50\%$$
2. **After-Tax Cost of Debt ($K_d$)**:
   $$K_d = \text{Pre-Tax Cost} \times (1 - t) = 9.0\% \times (1 - 0.25) = 6.75\%$$
3. **Capital Structure Weights**:
   $$\text{Total Capital} (V) = E + D = 800 + 200 = ₹1,000\text{ Cr}$$
   $$W_e = \frac{800}{1000} = 0.80 \quad (80\%), \quad W_d = \frac{200}{1000} = 0.20 \quad (20\%)$$
4. **WACC**:
   $$\text{WACC} = W_e \cdot K_e + W_d \cdot K_d = (0.80 \times 14.50\%) + (0.20 \times 6.75\%) = 11.60\% + 1.35\% = \mathbf{12.95\%}$$

---

### Q9: [P1][CORP-FIN] What is the difference between Hamada's unlevered beta and levered beta? Why do we unlever beta during valuation?

**Direct Model Answer:**
- **Levered Beta ($\beta_L$)**: Reflects both business operating risk and financial risk from debt leverage.
- **Hamada's Equation** (assuming debt beta $\beta_D \approx 0$):
  $$\beta_U = \frac{\beta_L}{1 + (1 - t) \cdot \frac{D}{E}}$$
- **Why we unlever beta**:
  1. Comparable peer companies have different capital structures (some have 10% debt, others 50% debt).
  2. To find the pure fundamental operating risk of an industry, we strip out individual capital structure choices by calculating each peer's Unlevered Beta ($\beta_U$) and computing the peer group median.
  3. We then **re-lever** this median beta using the target company's specific target debt-to-equity ratio:
     $$\beta_{L,\text{target}} = \beta_{U,\text{industry}} \cdot \left[ 1 + (1 - t) \cdot \left( \frac{D}{E} \right)_{\text{target}} \right]$$

---

### Q10: [P1][CORP-FIN] Explain the Modigliani-Miller Theorem and why capital structure matters in practice.

**Direct Model Answer:**
- **MM Proposition I (No Taxes, Frictionless Markets, 1958)**:
  In the absence of taxes, bankruptcy costs, and asymmetric information, the market value of a firm is independent of its capital structure: $V_L = V_U$.
- **MM Proposition II (With Taxes, 1963)**:
  Interest payments on debt are tax-deductible, creating a corporate interest tax shield:
  $$V_L = V_U + t \cdot D$$
  This suggests firms should finance with 100% debt.
- **Why Capital Structure Matters in Practice (Trade-off Theory)**:
  As debt increases, the marginal benefit of the tax shield is eventually offset by the present value of **Financial Distress and Bankruptcy Costs** (direct legal fees, customer churn, higher supplier costs, agency costs). Optimal capital structure occurs where the marginal tax shield equals marginal distress costs.

---

### Q11: [P1][CORP-FIN] A firm has ₹100 Cr EBIT, ₹20 Cr Depreciation, ₹30 Cr CapEx, and Working Capital increases by ₹15 Cr. The tax rate is 25%. Calculate Free Cash Flow to Firm (FCFF).

**Step-by-Step Calculation:**
$$\text{NOPAT} = \text{EBIT} \times (1 - t) = 100 \times (1 - 0.25) = ₹75\text{ Cr}$$
$$\text{FCFF} = \text{NOPAT} + \text{D\&A} - \text{CapEx} - \Delta \text{NWC}$$
$$\text{FCFF} = 75 + 20 - 30 - 15 = \mathbf{₹50\text{ Cr}}$$
- *Interpretation*: The firm generated ₹50 Cr of unencumbered cash flow available to service all capital providers (both debt and equity holders).

---

### Q12: [P1][CORP-FIN] A retail chain has a Payback Period of 3.2 years on new store openings. Why is Payback Period theoretically flawed compared to NPV?

**Direct Model Answer:**
1. **Ignores the Time Value of Money**: Traditional payback gives equal weight to cash flows in Year 1 and Year 3.
2. **Ignores Cash Flows After Cutoff**: If Store A generates ₹100/yr for 4 years (Payback = 3 yrs) and Store B generates ₹95/yr for 20 years (Payback = 3.1 yrs), payback chooses Store A despite Store B creating vastly superior total economic value.
3. **Arbitrary Hurdle Rate**: The decision rule threshold (e.g., "must pay back in 3 years") is subjective rather than market-derived like the cost of capital.

---

## Category 3: Financial Ratios & Performance Diagnosis

### Q13: [P0][RATIOS] Company Alpha and Company Beta both operate in Indian specialty chemicals. Both report an identical Return on Equity (ROE) of 24.0%. Using DuPont analysis, determine which company presents higher operational quality based on the following data:

| Metric | Company Alpha | Company Beta |
|:---|:---:|:---:|
| Revenue | ₹2,000 Cr | ₹4,000 Cr |
| Net Income | ₹240 Cr | ₹200 Cr |
| Total Assets | ₹1,600 Cr | ₹4,000 Cr |
| Shareholders' Equity | ₹1,000 Cr | ₹833.33 Cr |

**Step-by-Step Calculation (3-Stage DuPont Decomposition):**
$$\text{ROE} = \text{Net Profit Margin} \times \text{Asset Turnover} \times \text{Equity Multiplier}$$

1. **Company Alpha**:
   - $\text{Net Margin} = \frac{240}{2000} = 12.0\%$
   - $\text{Asset Turnover} = \frac{2000}{1600} = 1.25\times$
   - $\text{Equity Multiplier} = \frac{1600}{1000} = 1.60\times$
   - $\text{Check ROE} = 0.12 \times 1.25 \times 1.60 = 24.0\%$

2. **Company Beta**:
   - $\text{Net Margin} = \frac{200}{4000} = 5.0\%$
   - $\text{Asset Turnover} = \frac{4000}{4000} = 1.00\times$
   - $\text{Equity Multiplier} = \frac{4000}{833.33} = 4.80\times$
   - $\text{Check ROE} = 0.05 \times 1.00 \times 4.80 = 24.0\%$

**Analytical Synthesis:**
- **Company Alpha is higher quality**: Alpha's 24% ROE is powered by healthy operating margins (12%) and strong asset utilization ($1.25\times$) with conservative leverage ($1.60\times$ Assets/Equity, representing ~37.5% debt financing).
- **Company Beta is high-risk**: Beta operates with slim net margins (5%) and generates its 24% ROE almost entirely through high financial leverage ($4.80\times$ multiplier). Any modest contraction in margins will threaten Beta's solvency.

---

### Q14: [P0][RATIOS] Define the Cash Conversion Cycle (CCC). Can a company have a negative CCC, and what does it signify?

**Direct Model Answer:**
- **Formula**:
  $$\text{CCC} = \text{Days Sales Outstanding (DSO)} + \text{Days Sales of Inventory (DSI)} - \text{Days Payable Outstanding (DPO)}$$
  Where:
  - $\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Revenue}} \times 365$
  - $\text{DSI} = \frac{\text{Inventory}}{\text{COGS}} \times 365$
  - $\text{DPO} = \frac{\text{Accounts Payable}}{\text{COGS}} \times 365$
- **Can CCC be negative?** Yes. Examples include Amazon, Apple, and large hypermarkets (D-Mart).
- **What it signifies**:
  - The company collects cash from retail consumers immediately (low DSO) and moves inventory rapidly (low DSI), but delays paying its suppliers for 60–90 days (high DPO).
  - A negative CCC means suppliers effectively fund the company's working capital, generating float that can be invested without paying bank borrowing costs.

---

### Q15: [P1][RATIOS] A company's Current Ratio is 2.5x, but its Quick Ratio is 0.6x. What does this tell you about its liquidity risk?

**Direct Model Answer:**
- **Current Ratio** $= \frac{\text{Current Assets}}{\text{Current Liabilities}} = 2.5\times$
- **Quick Ratio** $= \frac{\text{Current Assets} - \text{Inventory}}{\text{Current Liabilities}} = 0.6\times$
- **Diagnosis**:
  1. The vast majority ($\approx 76\%$) of Current Assets is tied up in illiquid inventory.
  2. The company faces significant short-term liquidity risk: if creditors demand immediate repayment, the firm cannot meet obligations with cash and liquid receivables ($0.6\times < 1.0\times$).
  3. The business is vulnerable to inventory obsolescence, storage holding costs, or demand shocks.

---

### Q16: [P1][RATIOS] What is the difference between Return on Assets (ROA) and Return on Invested Capital (ROIC)? Which is more useful for comparing companies with different leverage?

**Direct Model Answer:**
- **ROA** $= \frac{\text{Net Income}}{\text{Total Assets}}$
  - *Limitation*: Net Income is an equity-only metric (after interest deductions), but the denominator includes Total Assets funded by both debt and equity. This mismatch penalizes leveraged companies.
- **ROIC** $= \frac{\text{NOPAT}}{\text{Invested Capital}} = \frac{\text{EBIT} \times (1 - t)}{\text{Total Debt} + \text{Total Equity} - \text{Excess Cash}}$
  - *Advantage*: NOPAT is the operating profit generated for all capital providers, and Invested Capital represents the actual operating capital deployed.
  - **Verdict**: ROIC is superior for cross-company comparison because it evaluates operational asset productivity independent of financial leverage.

---

### Q17: [P1][RATIOS] Why does EBITDA not equal operating cash flow? Name four critical cash drains that EBITDA completely ignores.

**Direct Model Answer:**
- EBITDA is an earnings measure, not a cash measure.
- **Four Critical Cash Items Ignored by EBITDA**:
  1. **Working Capital Investments ($\Delta \text{NWC}$)**: Trapped cash in customer receivables and unsold inventory.
  2. **Capital Expenditures ($CapEx$)**: Cash spent to maintain and replace aging physical assets.
  3. **Cash Interest Expense**: Debt servicing obligations required to prevent default.
  4. **Cash Taxes Paid**: Actual statutory tax outflows to government revenue authorities.

---

### Q18: [P1][RATIOS] A company has Debt-to-Equity of 3.0x and Interest Coverage Ratio (EBIT / Interest) of 1.2x. What is the credit assessment?

**Direct Model Answer:**
- **Assessment**: High credit risk / distressed profile.
- **Explanation**:
  - The balance sheet is heavily levered ($75\%$ debt, $25\%$ equity).
  - An interest coverage ratio of $1.2\times$ provides almost zero margin of safety; a mere $17\%$ decline in operating income will leave the firm unable to service its debt from operating profit ($1.2 \times (1 - 0.167) = 1.0$).
  - Refinancing risk is elevated if credit market spreads widen.

---

## Category 4: Valuation, DCF & Trading Multiples

### Q19: [P0][VALUATION] Walk me through the step-by-step reconciliation between Enterprise Value (EV) and Equity Value. Why do we add back cash and deduct debt?

**Direct Model Answer:**
$$\text{Enterprise Value} = \text{Equity Value} + \text{Total Debt} + \text{Preferred Stock} + \text{Minority Interest} - \text{Cash \& Cash Equivalents}$$
$$\text{Equity Value} = \text{Enterprise Value} - \text{Net Debt} - \text{Preferred Stock} - \text{Minority Interest}$$

**Economic Intuition:**
- **Enterprise Value (EV)** represents the core enterprise value of the operating business, independent of capital structure.
- When an acquirer buys a company:
  1. They must pay the purchase price for all common shares (**Equity Value**).
  2. They must assume or refinance the existing bank borrowings and bonds (**+ Total Debt**).
  3. They acquire the target's bank accounts, which can be immediately used to pay down debt (**- Cash**).
  4. Hence, Net Debt ($Debt - Cash$) represents the net claims of non-equity capital providers.

---

### Q20: [P0][VALUATION] In a DCF, why do we use the mid-year convention? How does it mathematically change the present value of cash flows?

**Direct Model Answer:**
- **Standard Discounting**: Assumes all annual cash flows arrive in a lump sum on the final day of the year (December 31):
  $$\text{PV} = \frac{\text{CF}_1}{(1 + W)^1} + \frac{\text{CF}_2}{(1 + W)^2} + \dots$$
- **Mid-Year Convention**: In real operating businesses, revenue and expenses occur evenly across all 365 days. The average dollar is collected at mid-year ($t = 0.5, 1.5, 2.5, \dots$):
  $$\text{PV}_{\text{mid}} = \frac{\text{CF}_1}{(1 + W)^{0.5}} + \frac{\text{CF}_2}{(1 + W)^{1.5}} + \dots$$
- **Mathematical Impact**:
  Because $(1 + W)^{0.5} < (1 + W)^{1.0}$, cash flows are discounted for half a year less. Mid-year discounting **increases** the present value of discrete cash flows by approximately:
  $$\text{PV}_{\text{mid}} = \text{PV}_{\text{end}} \times (1 + W)^{0.5}$$

---

### Q21: [P1][VALUATION] Why can you NOT evaluate a commercial bank using EV / EBITDA or a standard Free Cash Flow to Firm (FCFF) DCF model?

**Direct Model Answer:**
1. **Debt is Raw Material, Not Capital Structure**: For a commercial bank, deposits and borrowings are operational inputs used to generate interest-bearing loans. Separating "operating debt" from "financing debt" is impossible.
2. **Working Capital is Meaningless**: Working capital adjustments for loans and deposits represent the bank's core business, not short-term operational frictions.
3. **Preferred Valuation Methods for Banks**:
   - **Price-to-Book ($P/B$) Multiple**: Book value of equity closely approximates net asset fair value under mark-to-market accounting.
   - **Dividend Discount Model (DDM)**: Discounting Free Cash Flow to Equity ($FCFE$), defined as net income minus capital required to satisfy regulatory Basel capital adequacy ratios ($CET1$).

---

### Q22: [P1][VALUATION] Compare EV/EBITDA versus P/E multiples. In what scenarios would you prioritize one over the other?

**Direct Model Answer:**
| Feature | EV / EBITDA | Price / Earnings (P/E) |
|:---|:---|:---|
| **Denominator Scope** | Available to all capital providers | Available only to equity shareholders |
| **Capital Structure Neutral?**| Yes (independent of leverage) | No (distorted by debt interest) |
| **D&A Policy Neutral?** | Yes (neutralizes depreciation choices)| No (distorted by useful life assumptions)|
| **Tax Regime Neutral?** | Yes (neutralizes tax differences) | No (distorted by effective tax rates) |

- **Prioritize EV/EBITDA when**: Comparing capital-intensive firms with different debt levels (e.g., Telecom, Infrastructure, Steel) or across cross-border tax jurisdictions.
- **Prioritize P/E when**: Valuing asset-light businesses (IT services, consulting), financial institutions (banks, insurance), or when assessing net earnings dilution to public shareholders.

---

### Q23: [P1][VALUATION] A company has FCFF of ₹100 Cr in Year 5, WACC of 11.0%, and a terminal growth rate of 3.5%. Calculate the Terminal Value using the Gordon Growth formula. What common mistake do analysts make here?

**Step-by-Step Calculation:**
$$\text{Terminal Value}_5 = \frac{\text{FCFF}_5 \times (1 + g)}{\text{WACC} - g} = \frac{100 \times (1 + 0.035)}{0.110 - 0.035} = \frac{103.5}{0.075} = \mathbf{₹1,380\text{ Cr}}$$

- **Common Mistake**:
  Using $\text{FCFF}_5$ directly in the numerator without growing it by $(1 + g)$: $\frac{100}{0.075} = ₹1,333.33\text{ Cr}$ (understates terminal value by ₹46.67 Cr). The formula requires the expected cash flow in the **first terminal year** ($\text{FCFF}_{6}$).

---

### Q24: [P1][VALUATION] What is the difference between an asset deal and a stock deal in M&A?

**Direct Model Answer:**
- **Stock Deal**: The buyer purchases the target's common equity shares. The buyer acquires all assets and inherits all historical liabilities (including unknown legal or tax liabilities). PP&E tax basis generally carries over.
- **Asset Deal**: The buyer selectively purchases specific assets and assumes only explicitly named liabilities.
  - *Tax Benefit for Buyer*: The buyer can "step up" the tax basis of acquired assets to fair market value, creating significant future depreciation tax shields.
  - *Sellers prefer stock deals* to avoid double taxation (corporate-level tax on asset gain + dividend distribution tax).

---

## Category 5: Financial Markets, Banking Economics & Fixed Income

### Q25: [P0][MARKETS] What is the relationship between bond prices and yields? Why does a 10-year bond have higher interest rate risk than a 2-year bond with the same coupon?

**Direct Model Answer:**
- **Inverse Relationship**: As market interest yields rise, bond prices fall, and vice versa. Bond price is the sum of discounted future cash flows; higher discount rates reduce present values.
- **Why Longer Duration Has Greater Risk**:
  1. A 10-year bond's principal repayment (the largest cash flow) is discounted over 10 periods versus 2 periods.
  2. **Modified Duration** measures percentage price change per 100 bps shift in yield:
     $$\frac{\Delta P}{P} \approx -D_{\text{mod}} \times \Delta y$$
  3. A 2-year bond might have a duration of $\approx 1.8$ years (price moves $\approx 1.8\%$ per 100 bps), while a 10-year bond has a duration of $\approx 7.5$ years (price moves $\approx 7.5\%$ per 100 bps).

---

### Q26: [P0][BANKING] Explain Net Interest Margin (NIM) and CASA Ratio in Indian commercial banking.

**Direct Model Answer:**
- **Net Interest Margin (NIM)**:
  $$\text{NIM} = \frac{\text{Interest Income Earned} - \text{Interest Expense Paid}}{\text{Average Earning Assets}}$$
  Measures the profitability of a bank's lending and investment operations relative to total deployed funds. Leading Indian private banks typically maintain NIMs between 3.5% and 4.2%.
- **CASA Ratio (Current Account Savings Account)**:
  $$\text{CASA Ratio} = \frac{\text{Current Account Deposits} + \text{Savings Account Deposits}}{\text{Total Deposits}}$$
  - Current accounts pay 0% interest; savings accounts pay modest interest (e.g., 2.5%–3.5%).
  - A higher CASA ratio (e.g., 40%–45%) provides a low-cost, sticky deposit franchise, lowering the bank's blended cost of funds and supporting healthy NIMs.

---

### Q27: [P1][MARKETS] What is an inverted yield curve, and why is it historically viewed as a leading indicator of economic slowdown?

**Direct Model Answer:**
- **Normal Yield Curve**: Upward-sloping. Investors demand higher yields on longer-dated bonds to compensate for term premium and inflation uncertainty.
- **Inverted Yield Curve**: Short-term bond yields exceed long-term bond yields (e.g., 2-Year Treasury yield > 10-Year Treasury yield).
- **Economic Mechanism**:
  1. The central bank aggressively hikes short-term policy rates to tame inflation, driving short-term yields higher.
  2. Bond investors expect the monetary tightening to slow economic growth, forcing the central bank to cut interest rates in the future.
  3. Investors buy long-term bonds to lock in yields, driving long-term bond prices up and yields down until long rates fall below short rates.

---

### Q28: [P1][MARKETS] Explain the concept of Call and Put options, In-the-Money (ITM), and Put-Call Parity.

**Direct Model Answer:**
- **Call Option**: Right (not obligation) to buy an underlying asset at strike price $K$. ITM when $S > K$.
- **Put Option**: Right to sell an underlying asset at strike price $K$. ITM when $S < K$.
- **Put-Call Parity (European Options on non-dividend stock)**:
  $$C + K \cdot e^{-rT} = P + S$$
  - Left side: Fiduciary Call (Call option + zero-coupon bond paying strike $K$ at maturity $T$).
  - Right side: Protective Put (Put option + 1 share of underlying stock $S$).
  - If prices diverge, an arbitrageur can capture riskless profit by longing the undervalued portfolio and shorting the overvalued portfolio.

---

## Category 6: Strategic M&A & Engineering Background Defense

### Q29: [P0][FIT/STRATEGY] Why do you want to transition from Civil Engineering / HWRE at IIT Kanpur into Investment Banking / Financial Analysis?

**Framework for High-Impact Answer:**
1. **Foundation in Mathematical Modeling**:
   *"In my Master's coursework and computational thesis at IIT Kanpur, my day-to-day work centers on multi-variable partial differential equations, optimization under boundary constraints, and processing large-scale spatial-temporal telemetry. Engineering trained me to look at complex systems mathematically."*
2. **The Commercial Transition**:
   *"While working on large infrastructure and hydrology system simulations, I realized that technical feasibility is only half the equation; capital allocation, debt-service coverage, and shareholder value dictate whether projects actually get financed and built."*
3. **Rigorous Self-Driven Preparation**:
   *"I didn't treat finance as an afterthought. I systematically mastered 3-statement modeling, valuation methodologies, corporate finance theory, and built valuation models in Excel and Python. I bring the quantitative stamina of an IIT Kanpur engineer with the domain polish of an analyst."*

---

### Q30: [P1][STRATEGY] Why would a company prefer to fund an acquisition with Debt rather than Equity?

**Direct Model Answer:**
1. **Lower Cost of Capital**: Cost of debt ($K_d$) is significantly cheaper than cost of equity ($K_e$) because debt is senior in the capital structure and interest is tax-deductible.
2. **No Ownership Dilution**: Debt issuance does not dilute existing shareholders' percentage ownership or voting control.
3. **EPS Accretion**: Because debt is cheaper, borrowing at an after-tax cost of 6% to acquire a target with an earnings yield of 10% will be strongly accretive to the acquirer's Earnings Per Share (EPS).
4. **Constraint**: Debt increases fixed interest obligations and raises financial distress risk if earnings fall.

---

### Q31: [P1][STRATEGY] Company A acquires Company B for ₹500 Cr. Company B has identifiable net tangible assets of ₹350 Cr. How is the transaction recorded, and what is Goodwill?

**Direct Model Answer:**
- **Identifiable Net Assets**: Fair market value of assets acquired minus liabilities assumed = ₹350 Cr.
- **Purchase Price**: ₹500 Cr.
- **Goodwill Calculation**:
  $$\text{Goodwill} = \text{Purchase Price} - \text{Fair Market Value of Net Identifiable Assets} = 500 - 350 = \mathbf{₹150\text{ Cr}}$$
- **Balance Sheet Treatment**: The buyer records acquired assets and liabilities on its consolidated balance sheet and creates a new non-current asset called **Goodwill** for ₹150 Cr.
- **Goodwill Nature**: Goodwill is not amortized under US GAAP/IFRS; it is tested annually for impairment. If future expected cash flows fall below carrying value, an impairment expense is booked in the P&L.

---

### Q32: [P1][STRATEGY] What is the difference between organic growth and inorganic growth?

**Direct Model Answer:**
- **Organic Growth**: Expansion from internal operations—launching new products, hiring sales personnel, increasing store footprint, or expanding into new geographic markets using operating cash flow. (Slower, lower execution integration risk, preserves company culture).
- **Inorganic Growth**: Expansion through mergers, acquisitions, joint ventures, or strategic takeovers. (Immediate market share gain, access to patented technology, but carries high execution risk: cultural clash, integration friction, and overpayment risk).

---

## Cross-Module Links
- 📖 [Domain Knowledge Comprehensive Guide](03_domain-knowledge.md)
- 📖 [Worked Practice Cases & Exercises](07_practice-and-cases.md)
- 📖 [Full Mock Assessment](12_mock-assessment.md)
- 📖 [Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Risk Analytics Question Bank](../risk/06_question-bank.md)

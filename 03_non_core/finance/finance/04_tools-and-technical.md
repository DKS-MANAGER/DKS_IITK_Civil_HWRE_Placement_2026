# 04. Tools & Technical Stack — General Finance

> Practical guide to core financial modeling software, analytical programming, and database querying used in investment banking, corporate finance, and equity research interviews at IIT Kanpur.

---

## 1. Core Tooling Hierarchy

In entry-level financial analyst and corporate finance recruitment, interviewers test technical proficiency across three distinct layers:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: Financial Modeling in Microsoft Excel (Primary)     │
│ • Keyboard-only navigation (no mouse dependency)            │
│ • 3-Statement dynamic linking & circularity management      │
│ • Sensitivity analysis (1D & 2D Data Tables, Goal Seek)     │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ Layer 2: Python for Financial Analysis (Quantitative Bridge) │
│ • Automated ratio computation & DuPont decomposition        │
│ • Programmatic DCF & scenario engines                       │
│ • Fixed-income duration & convexity modeling                │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ Layer 3: SQL for Financial Data & Reporting (Database Layer) │
│ • Ledger reconciliation & trial balance integrity           │
│ • Aging schedule generation for Accounts Receivable         │
│ • Rolling EBITDA and revenue trend aggregations             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Layer 1: Financial Modeling in Microsoft Excel

Excel is the industry standard for valuation, project finance, and transaction structuring.

### 2.1 Model Architecture & Color Coding Standards
Top investment banks and advisory firms strictly enforce visual formatting conventions:
- **Blue Text (`RGB 0, 0, 255`)**: Hardcoded inputs and historical numbers (e.g., historical revenue, tax rate assumption).
- **Black Text (`RGB 0, 0, 0`)**: Dynamic formulas and calculations within the same sheet (e.g., `=C12*D12`).
- **Green Text (`RGB 0, 128, 0`)**: Dynamic links pulling from another worksheet (e.g., `='Income Statement'!E25`).
- **Red Text (`RGB 255, 0, 0`)**: Warning flags, error checks, or hardcoded overrides requiring audit.
- **Yellow Fill (`RGB 255, 255, 0`)**: User-editable scenario toggle cells.

### 2.2 Critical Financial Modeling Functions
- `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode])`: Replaces fragile `VLOOKUP` and column index hardcoding.
- `INDEX(array, MATCH(lookup_val, lookup_range, 0))`: Standard robust dynamic retrieval across columns and rows.
- `NPV(rate, value1, [value2], ...)`: Calculates present value of uneven cash flows. **Crucial Excel quirk**: `NPV` assumes cash flow 1 occurs at end of period 1. To model Year 0 initial outlay: `=Initial_Outlay + NPV(rate, Year1:Year5)`.
- `XNPV(rate, values, dates)`: Exact date-specific discounting, vital for stub periods or real-world uneven transaction dates.
- `IRR(values, [guess])` and `XIRR(values, dates)`: Computes the internal rate of return where NPV equals zero.

### 2.3 Sensitivity Analysis & Data Tables
Investment committees require sensitivity grids (e.g., Share Price vs WACC and Terminal Growth Rate).
1. Set up a grid with WACC across columns (e.g., 10.0%, 11.0%, 12.0%) and Terminal Growth $g$ across rows (e.g., 3.0%, 4.0%, 5.0%).
2. In the top-left intersection cell, link to the output cell (e.g., `=Equity_Value_Per_Share`).
3. Select the table $\to$ **Data** $\to$ **What-If Analysis** $\to$ **Data Table**.
4. Set **Row input cell** to the model's terminal growth assumption cell.
5. Set **Column input cell** to the model's WACC assumption cell.
6. Press OK. (Excel executes the sensitivity without requiring nested VBA macros).

### 2.4 Handling Circular References & Debt Sweeps
- **The Issue**: Interest expense depends on average debt balance; Net Income depends on interest expense; Cash generated depends on Net Income; Ending debt depends on available cash. This creates an iterative circular calculation.
- **Best Practice Solution**:
  - In Excel: File $\to$ Options $\to$ Formulas $\to$ Enable iterative calculation (Max Iterations = 100, Max Change = 0.001).
  - Alternatively (preferred in stress testing): Base interest expense on beginning-of-period debt balance (`Interest = Beginning_Debt * Cost_of_Debt`) to eliminate circular dependency while preserving economic realism.

---

## 3. Layer 2: Python for Financial Analytics

Python is widely tested in quantitative finance, fintech, and analytics screening rounds. Below are clean, self-contained scripts using standard Python data structures and `numpy`/`pandas` semantics.

### 3.1 Financial Statement Ratio & DuPont Engine

```python
"""
Financial Statement Analysis & DuPont Decomposition Engine
[PREPARATION HEURISTIC]: Standard quantitative finance interview implementation.
"""

from typing import Dict, Any


def compute_financial_ratios(income_stmt: Dict[str, float],
                             balance_sheet: Dict[str, float]) -> Dict[str, Any]:
    """
    Computes key profitability, liquidity, solvency, and DuPont metrics.
    
    Assumptions:
    - Balance sheet values represent period averages where applicable.
    - Tax rate is derived from reported tax and pre-tax income.
    """
    rev = income_stmt["revenue"]
    cogs = income_stmt["cogs"]
    ebit = income_stmt["ebit"]
    interest = income_stmt["interest_expense"]
    net_inc = income_stmt["net_income"]

    ca = balance_sheet["current_assets"]
    cl = balance_sheet["current_liabilities"]
    inv = balance_sheet["inventory"]
    total_assets = balance_sheet["total_assets"]
    total_debt = balance_sheet["short_term_debt"] + balance_sheet["long_term_debt"]
    equity = balance_sheet["shareholders_equity"]

    # 1. Profitability Ratios
    gross_margin = (rev - cogs) / rev
    operating_margin = ebit / rev
    net_margin = net_inc / rev

    # 2. Return Metrics
    roa = net_inc / total_assets
    roe = net_inc / equity

    # 3. 3-Step DuPont Breakdown
    # ROE = Net Profit Margin * Asset Turnover * Financial Leverage
    asset_turnover = rev / total_assets
    equity_multiplier = total_assets / equity
    dupont_roe = net_margin * asset_turnover * equity_multiplier

    # 4. Liquidity & Solvency
    current_ratio = ca / cl
    quick_ratio = (ca - inv) / cl
    debt_to_equity = total_debt / equity
    interest_coverage = ebit / interest if interest > 0 else float("inf")

    return {
        "margins": {
            "gross_margin_pct": round(gross_margin * 100, 2),
            "operating_margin_pct": round(operating_margin * 100, 2),
            "net_margin_pct": round(net_margin * 100, 2),
        },
        "returns": {
            "roa_pct": round(roa * 100, 2),
            "roe_pct": round(roe * 100, 2),
        },
        "dupont_decomposition": {
            "net_margin": round(net_margin, 4),
            "asset_turnover": round(asset_turnover, 4),
            "equity_multiplier": round(equity_multiplier, 4),
            "product_roe_pct": round(dupont_roe * 100, 2),
        },
        "liquidity_solvency": {
            "current_ratio": round(current_ratio, 2),
            "quick_ratio": round(quick_ratio, 2),
            "debt_to_equity": round(debt_to_equity, 2),
            "interest_coverage_x": round(interest_coverage, 2),
        }
    }


if __name__ == "__main__":
    is_data = {
        "revenue": 1000.0,
        "cogs": 600.0,
        "ebit": 180.0,
        "interest_expense": 20.0,
        "net_income": 120.0,
    }
    bs_data = {
        "current_assets": 400.0,
        "inventory": 150.0,
        "current_liabilities": 200.0,
        "total_assets": 1200.0,
        "short_term_debt": 50.0,
        "long_term_debt": 250.0,
        "shareholders_equity": 600.0,
    }
    results = compute_financial_ratios(is_data, bs_data)
    print("Ratio Analysis Results:", results)
```

### 3.2 Automated Discounted Cash Flow (DCF) Engine

```python
"""
Discounted Cash Flow (DCF) Valuation Engine
[PRACTICE ASSUMPTION]: 5-year discrete projection with Gordon Growth Terminal Value.
"""

from typing import List, Dict


def run_dcf_valuation(
    fcf_projections: List[float],
    terminal_fcf: float,
    wacc: float,
    terminal_growth_rate: float,
    net_debt: float,
    shares_outstanding: float
) -> Dict[str, float]:
    """
    Computes Enterprise Value, Equity Value, and Implied Price per Share.
    
    Formulae:
    - PV of discrete FCF = sum(FCF_t / (1 + wacc)^t)
    - Terminal Value (TV) = terminal_fcf * (1 + g) / (wacc - g)
    - PV of TV = TV / (1 + wacc)^N
    - Enterprise Value (EV) = PV(discrete) + PV(TV)
    - Equity Value = EV - Net Debt
    """
    assert wacc > terminal_growth_rate, "WACC must exceed perpetual terminal growth rate."

    pv_discrete = 0.0
    for t, fcf in enumerate(fcf_projections, start=1):
        discount_factor = (1.0 + wacc) ** t
        pv_discrete += fcf / discount_factor

    num_years = len(fcf_projections)
    terminal_value = (terminal_fcf * (1.0 + terminal_growth_rate)) / (wacc - terminal_growth_rate)
    pv_terminal_value = terminal_value / ((1.0 + wacc) ** num_years)

    enterprise_value = pv_discrete + pv_terminal_value
    equity_value = enterprise_value - net_debt
    implied_share_price = equity_value / shares_outstanding

    return {
        "pv_discrete_fcf": round(pv_discrete, 2),
        "terminal_value": round(terminal_value, 2),
        "pv_terminal_value": round(pv_terminal_value, 2),
        "enterprise_value": round(enterprise_value, 2),
        "net_debt": round(net_debt, 2),
        "equity_value": round(equity_value, 2),
        "implied_share_price": round(implied_share_price, 2),
        "tv_percentage_of_ev": round((pv_terminal_value / enterprise_value) * 100, 2)
    }


if __name__ == "__main__":
    # Example: 5-year FCF in INR Crores
    fcfs = [50.0, 65.0, 80.0, 95.0, 110.0]
    out = run_dcf_valuation(
        fcf_projections=fcfs,
        terminal_fcf=110.0,
        wacc=0.12,                  # 12.0% WACC
        terminal_growth_rate=0.04,  # 4.0% Terminal Growth
        net_debt=120.0,             # INR 120 Cr Net Debt
        shares_outstanding=10.0     # 10 Cr shares
    )
    print("DCF Output:", out)
```

### 3.3 Bond Pricing & Macaulay/Modified Duration

```python
"""
Bond Valuation & Interest Rate Sensitivity (Duration)
[PREPARATION HEURISTIC]: Macaulay & Modified Duration implementation.
"""

def bond_pricing_and_duration(
    face_value: float,
    annual_coupon_rate: float,
    ytm: float,
    maturity_years: int
) -> dict:
    """
    Computes theoretical bond clean price, Macaulay duration, and Modified duration.
    """
    coupon = face_value * annual_coupon_rate
    price = 0.0
    weighted_time = 0.0

    for t in range(1, maturity_years + 1):
        cash_flow = coupon + (face_value if t == maturity_years else 0.0)
        pv_cf = cash_flow / ((1.0 + ytm) ** t)
        price += pv_cf
        weighted_time += t * pv_cf

    mac_duration = weighted_time / price
    mod_duration = mac_duration / (1.0 + ytm)
    dollar_duration = mod_duration * price * 0.0001  # DV01 (price change per 1 bp)

    return {
        "bond_price": round(price, 4),
        "macaulay_duration_years": round(mac_duration, 4),
        "modified_duration_years": round(mod_duration, 4),
        "dv01_per_bond": round(dollar_duration, 4)
    }


if __name__ == "__main__":
    # 5-year 8% coupon bond with 7% YTM, face value 1,000 INR
    res = bond_pricing_and_duration(1000.0, 0.08, 0.07, 5)
    print("Bond Analysis:", res)
```

---

## 4. Layer 3: SQL for Financial Data & Reporting

Data-driven finance interviews frequently assess the candidate's ability to extract, clean, and validate financial statements from relational accounting schemas.

### 4.1 SQL Schema Architecture
Typical database schema representation:
- `chart_of_accounts (account_id, account_name, account_type, normal_balance)`
- `general_ledger (entry_id, transaction_date, account_id, debit_amount, credit_amount, description)`
- `invoices (invoice_id, customer_id, invoice_date, due_date, amount, paid_amount, status)`

### 4.2 Query 1: General Ledger Trial Balance Integrity Check
*Problem*: Verify that total debits equal total credits for the accounting period, and output account balances classified as Assets, Liabilities, Equity, Revenue, and Expenses.

```sql
-- Trial Balance Verification Query
WITH AccountBalances AS (
    SELECT 
        coa.account_id,
        coa.account_name,
        coa.account_type,
        coa.normal_balance,
        COALESCE(SUM(gl.debit_amount), 0.0) AS total_debits,
        COALESCE(SUM(gl.credit_amount), 0.0) AS total_credits,
        CASE 
            WHEN coa.normal_balance = 'DEBIT' 
                THEN COALESCE(SUM(gl.debit_amount), 0.0) - COALESCE(SUM(gl.credit_amount), 0.0)
            ELSE COALESCE(SUM(gl.credit_amount), 0.0) - COALESCE(SUM(gl.debit_amount), 0.0)
        END AS ending_net_balance
    FROM chart_of_accounts coa
    LEFT JOIN general_ledger gl 
        ON coa.account_id = gl.account_id
        AND gl.transaction_date BETWEEN '2025-04-01' AND '2026-03-31'
    GROUP BY coa.account_id, coa.account_name, coa.account_type, coa.normal_balance
)
SELECT 
    account_type,
    SUM(total_debits) AS sum_debits,
    SUM(total_credits) AS sum_credits,
    SUM(ending_net_balance) AS net_category_balance,
    -- Balance sheet equation audit check
    ROUND(SUM(total_debits) - SUM(total_credits), 2) AS debit_credit_mismatch
FROM AccountBalances
GROUP BY account_type
ORDER BY CASE account_type 
    WHEN 'ASSET' THEN 1 
    WHEN 'LIABILITY' THEN 2 
    WHEN 'EQUITY' THEN 3 
    WHEN 'REVENUE' THEN 4 
    WHEN 'EXPENSE' THEN 5 
END;
```

### 4.3 Query 2: Accounts Receivable Aging Schedule
*Problem*: Classify outstanding customer invoices into standard credit risk buckets (Current, 1-30 Days, 31-60 Days, 61-90 Days, 90+ Days) to calculate provision for doubtful accounts.

```sql
-- Accounts Receivable Aging Analysis
SELECT 
    customer_id,
    COUNT(invoice_id) AS open_invoices_count,
    SUM(amount - paid_amount) AS total_outstanding_ar,
    SUM(CASE WHEN DATEDIFF(day, due_date, CURRENT_DATE) <= 0 
             THEN (amount - paid_amount) ELSE 0 END) AS current_not_due,
    SUM(CASE WHEN DATEDIFF(day, due_date, CURRENT_DATE) BETWEEN 1 AND 30 
             THEN (amount - paid_amount) ELSE 0 END) AS overdue_1_30_days,
    SUM(CASE WHEN DATEDIFF(day, due_date, CURRENT_DATE) BETWEEN 31 AND 60 
             THEN (amount - paid_amount) ELSE 0 END) AS overdue_31_60_days,
    SUM(CASE WHEN DATEDIFF(day, due_date, CURRENT_DATE) BETWEEN 61 AND 90 
             THEN (amount - paid_amount) ELSE 0 END) AS overdue_61_90_days,
    SUM(CASE WHEN DATEDIFF(day, due_date, CURRENT_DATE) > 90 
             THEN (amount - paid_amount) ELSE 0 END) AS overdue_90_plus_days
FROM invoices
WHERE status != 'PAID'
GROUP BY customer_id
HAVING SUM(amount - paid_amount) > 0
ORDER BY overdue_90_plus_days DESC, total_outstanding_ar DESC;
```

---

## 5. Financial Data Platforms: Concepts & Terminology

In analyst interviews at bulge-bracket investment banks and asset managers, familiarity with financial databases is a clear differentiator:

1. **Bloomberg Terminal**:
   - `DES <GO>`: Description page for company overview, capitalization, and business description.
   - `FA <GO>`: Financial Analysis showing historical 10-K/10-Q statements and consensus broker projections.
   - `WACC <GO>`: Automated cost of capital breakdown with raw beta and Blume-adjusted beta.
   - `RV <GO>`: Relative Valuation table showing comparable peers and trading multiples.

2. **S&P Capital IQ / FactSet**:
   - Standardizes reported financial statements across US GAAP, IFRS, and Ind-AS to allow direct cross-border peer comparisons.
   - Separates **As-Reported** metrics from **Normalized / Adjusted** metrics (excluding non-recurring litigation charges, restructuring costs, or goodwill impairments).

---

## 6. Verification & Cross-Repository Navigation
- 📖 [General Finance Domain Knowledge](03_domain-knowledge.md)
- 📖 [Worked Valuation & Financial Cases](07_practice-and-cases.md)
- 📖 [High-Yield Question Bank](06_question-bank.md)
- 📖 [Full Mock Assessment](12_mock-assessment.md)
- 📖 [Risk Analytics Tools & SQL](../risk/04_tools-and-technical.md)

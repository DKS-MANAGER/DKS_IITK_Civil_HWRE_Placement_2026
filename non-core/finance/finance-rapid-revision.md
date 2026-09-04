# Finance — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core formulas, frameworks, and quick-fire Q&A for finance interviews.

---

## Framework 1: Financial Statement Analysis

### Three Statements at a Glance

| Statement | Key Items | What It Tells You |
|:----------|:----------|:------------------|
| **Income Statement** | Revenue → COGS → Gross Profit → EBIT → EBT → Net Income | Profitability over a period |
| **Balance Sheet** | Assets = Liabilities + Equity | Financial position at a point |
| **Cash Flow** | Operating + Investing + Financing | Cash generation ability |

### Key Financial Ratios

| Ratio | Formula | What It Measures |
|:------|:--------|:-----------------|
| Current Ratio | Current Assets / Current Liabilities | Short-term liquidity (>1.5 good) |
| Quick Ratio | (Current Assets - Inventory) / CL | Immediate liquidity (>1.0 good) |
| Debt-to-Equity | Total Debt / Shareholders' Equity | Leverage (<2.0 moderate) |
| ROE | Net Income / Equity | Return to shareholders |
| ROA | Net Income / Total Assets | Asset efficiency |
| ROCE | EBIT / (Equity + Debt) | Overall capital efficiency |
| P/E | Price per share / EPS | Market premium on earnings |
| EV/EBITDA | Enterprise Value / EBITDA | Valuation (lower = cheaper) |
| DSO | (Accounts Receivable / Revenue) × 365 | Days to collect cash |
| Inventory Turnover | COGS / Average Inventory | How fast inventory sells |

### DuPont Analysis

**ROE = Net Profit Margin × Asset Turnover × Equity Multiplier**

```
ROE = (Net Income / Revenue) × (Revenue / Total Assets) × (Total Assets / Equity)
```

- High margin → pricing power
- High turnover → operational efficiency
- High multiplier → leverage (risk!)

---

## Framework 2: Valuation Methods

### DCF Valuation Steps

```
1. Project Free Cash Flows (5 years)
   FCFF = EBIT(1-t) + D&A - CapEx - ΔNWC

2. Calculate Terminal Value
   TV = FCF₅ × (1+g) / (WACC - g)    [Gordon Growth]

3. Discount at WACC
   EV = Σ [FCFₜ / (1+WACC)ᵗ] + TV / (1+WACC)⁵

4. Equity Value = EV - Net Debt
   Price per share = Equity Value / Shares
```

### WACC Formula

```
WACC = [E/(E+D)] × Re + [D/(E+D)] × Rd × (1-t)
```

Where:
- Re = Cost of equity = Rf + β(Rm - Rf)  [CAPM]
- Rd = Cost of debt (pre-tax)
- t = Tax rate
- E, D = Market values of equity and debt

### Relative Valuation Multiples

| Multiple | Formula | Best For |
|:---------|:--------|:---------|
| P/E | Market Cap / Net Income | Profitable companies |
| EV/EBITDA | Enterprise Value / EBITDA | Comparing across capital structures |
| P/B | Market Cap / Book Value | Asset-heavy businesses |
| P/S | Market Cap / Revenue | Revenue-growth companies (no profit) |

### Enterprise Value Formula

```
EV = Market Cap + Total Debt - Cash - Minorities
```

---

## Framework 3: Corporate Finance & Capital Budgeting

### Capital Budgeting Decision Rules

| Method | Formula | Accept If | Pitfall |
|:-------|:--------|:----------|:--------|
| NPV | Σ CFₜ/(1+r)ᵗ - I₀ | NPV > 0 | Requires discount rate |
| IRR | Rate where NPV = 0 | IRR > hurdle | Multiple IRRs possible |
| Payback | Time to recover investment | < cutoff | Ignores time value |
| PI | PV of inflows / I₀ | PI > 1 | Ignores scale |

### NPV vs IRR Conflicts

- **Mutually exclusive projects:** Always use NPV
- **Non-conventional cash flows:** May have multiple IRRs → use MIRR or NPV
- **Scale differences:** NPV is superior
- **Reinvestment assumption:** NPV assumes cost of capital; IRR assumes IRR rate

### CAPM (Capital Asset Pricing Model)

```
Cost of Equity (Re) = Rf + β × (Rm - Rf)
```

- Rf = Risk-free rate (10-year govt bond yield)
- β = Sensitivity to market (β=1 = market risk)
- Rm = Expected market return (~12-14% for India)

### M&M Propositions

| Proposition | Without Taxes | With Taxes |
|:------------|:-------------|:-----------|
| **Prop I** (Value) | V_L = V_U (capital structure irrelevant) | V_L = V_U + t × D (debt adds value via tax shield) |
| **Prop II** (Cost of Equity) | Re = R₀ + (R₀-Rd)(D/E) | Same, but WACC decreases with leverage |

---

## Framework 4: Case Study & Guesstimate Framework

### Guesstimate Structure (Top-Down)

```
1. Define the question clearly
2. Break into components (MECE)
3. State assumptions (reasonable, defensible)
4. Calculate step by step
5. Sanity-check against known data
6. State limitations
```

### Market Sizing Template

```
Total Population
  × Urban % = Urban Population
  × Target segment % = Addressable Population
  × Usage frequency = Total Usage
  × Average spend = Market Size
```

### Profitability Case Framework

```
Profit = Revenue - Cost

Revenue drivers:
  - Volume (users × frequency × price)
  - Mix (product mix, channel mix)

Cost drivers:
  - Fixed vs variable
  - Economies of scale
  - Input costs
  - Operational efficiency
```

### Investment Case Structure

```
Bull Case:  Growth drivers, tailwinds, expansion potential
Base Case:  Current trajectory, consensus assumptions
Bear Case:  Risks, headwinds, competitive threats

Key metrics: Revenue growth, margin trajectory, FCF yield, valuation vs peers
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is the difference between enterprise value and equity value?**
A: Equity value is the market value of shareholders' claims (market cap). Enterprise value is the total value of the firm to all capital providers: EV = Equity + Debt - Cash. EV represents the "takeover price" of a business.

**Q2: Why is WACC important?**
A: WACC is the minimum return a company must earn on its existing assets to satisfy its creditors, owners, and other providers of capital. It's used as the discount rate in DCF valuation.

**Q3: When would NPV and IRR give conflicting rankings?**
A: When projects are mutually exclusive AND have different scales or timing of cash flows. NPV is always preferred in conflicts because it measures absolute value creation.

**Q4: What is free cash flow and why do we use it?**
A: FCFF = EBIT(1-t) + D&A - CapEx - ΔNWC. It represents cash available to all capital providers after maintaining operations. We use it because it's independent of capital structure.

**Q5: How do you calculate cost of equity?**
A: Using CAPM: Re = Rf + β(Rm - Rf). Rf is the 10-year government bond yield, β measures systematic risk, and (Rm - Rf) is the equity risk premium.

**Q6: What is the DuPont analysis?**
A: It decomposes ROE into three components: Profit Margin (profitability) × Asset Turnover (efficiency) × Equity Multiplier (leverage). This reveals what's driving returns.

**Q7: How do you value a company with no profits?**
A: Use revenue multiples (P/S), comparable transactions, or DCF with projected future profitability. For startups, VC method (target return × investment / ownership %) is common.

**Q8: What is a good current ratio?**
A: Generally >1.5 indicates good short-term liquidity. However, too high (>3) may indicate inefficient use of assets. The ideal varies by industry — manufacturing needs higher; services can be lower.

**Q9: How does a civil engineering background help in finance?**
A: Strong quantitative skills, understanding of project finance and capital budgeting for infrastructure, familiarity with estimation and cost analysis, and the ability to evaluate technical risks in infrastructure investments.

**Q10: What is the cash conversion cycle?**
A: CCC = DSO + DIO - DPO. It measures how long it takes to convert inventory investment into cash. Shorter is better — negative CCC (like Amazon) means the company gets paid before it pays suppliers.

---

## Last-Minute Checklist

### Before Any Finance Interview
- [ ] Current 10-year government bond yield (Rf)
- [ ] Typical market risk premium for India (~6-7%)
- [ ] Major company financial results (last quarter)
- [ ] Key ratio benchmarks for the industry
- [ ] Your "Why finance?" answer (link to civil engineering)

### Must-Know Formulas
- [ ] WACC = E/(E+D) × Re + D/(E+D) × Rd × (1-t)
- [ ] CAPM: Re = Rf + β(Rm - Rf)
- [ ] FCFF = EBIT(1-t) + D&A - CapEx - ΔNWC
- [ ] Terminal Value = FCF(1+g) / (WACC-g)
- [ ] DuPont: ROE = NPM × AT × EM
- [ ] EV = Market Cap + Debt - Cash
- [ ] CCC = DSO + DIO - DPO

### Behavioral Prep
- [ ] "Why finance?" (quantitative skills + infrastructure finance angle)
- [ ] "Walk me through a DCF" (5 steps, know cold)
- [ ] "Tell me about a company you'd invest in" (have 2 ready with rationale)
- [ ] "What's happening in the markets?" (know current trends)

---

## Cross-Links

**Finance:**
→ [Finance Overview](finance-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Risk Rapid Revision](../risk/risk-rapid-revision.md) — Risk management formulas
→ [Consulting Case Frameworks](../consulting/case-frameworks.md) — Case interview prep
→ [Quantitative Aptitude](../../non-core/aptitude/quantitative/aptitude-basics.md) — Math fundamentals

---

*Last updated: 2026-09-04*

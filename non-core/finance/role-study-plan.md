# Finance — Role Study Plan

## Role Overview

The Finance role targets **financial analyst positions** at banks (Barclays, HSBC, JP Morgan), **consulting firms** (Deloitte, PwC, EY, KPMG), **corporate finance** departments (Tata, Reliance, L&T), and **fintech startups**. The role covers financial statement analysis, valuation, corporate finance, and investment analysis. Civil engineers with strong quantitative skills transition well into finance.

**Who targets this role:** B.Tech/M.Tech graduates with strong quantitative aptitude, GATE qualifiers with finance interest, students who completed finance electives or certifications (CFA Level 1, NISM).

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Financial Statements & Ratio Analysis

#### Why This Matters
Every finance interview starts with "Can you read financial statements?" Understanding income statements, balance sheets, and cash flow statements — and deriving meaningful ratios — is the absolute foundation.

#### What to Learn
- [ ] Income statement: Revenue, COGS, gross profit, operating profit, net profit
- [ ] Balance sheet: Assets (current/non-current), liabilities, shareholders' equity
- [ ] Cash flow statement: Operating, investing, financing activities
- [ ] Key ratios: Current ratio, quick ratio, debt-to-equity, ROE, ROA, ROCE, EPS, P/E, EV/EBITDA
- [ ] DuPont analysis: Decomposing ROE into profit margin × asset turnover × equity multiplier
- [ ] Working capital management: Days sales outstanding, days payable outstanding, inventory turnover
- [ ] Difference between book value and market value

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`finance-overview.md`](finance-overview.md) | Financial statements, ratios | Full |

#### Worked Example
**Problem:** A company reports the following (₹ in crores):

| Item | Value |
|:-----|------:|
| Revenue | 500 |
| COGS | 300 |
| Operating Expenses | 80 |
| Interest | 20 |
| Tax (25%) | 25 |
| Total Assets | 400 |
| Total Liabilities | 250 |
| Shareholders' Equity | 150 |
| Current Assets | 180 |
| Current Liabilities | 100 |
| Net Income | 75 |

Calculate: (a) Gross profit margin, (b) Operating profit margin, (c) Net profit margin, (d) Current ratio, (e) Debt-to-equity, (f) ROE, (g) ROA, (h) DuPont decomposition of ROE.

**Solution:**
1. **Gross profit margin** = (Revenue - COGS) / Revenue = (500-300)/500 = **40.0%**
2. **Operating profit margin** = Operating profit / Revenue = (500-300-80)/500 = 120/500 = **24.0%**
3. **Net profit margin** = Net Income / Revenue = 75/500 = **15.0%**
4. **Current ratio** = Current Assets / Current Liabilities = 180/100 = **1.80**
5. **Debt-to-equity** = Total Liabilities / Equity = 250/150 = **1.67**
6. **ROE** = Net Income / Equity = 75/150 = **50.0%**
7. **ROA** = Net Income / Total Assets = 75/400 = **18.75%**
8. **DuPont:** ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
   - Net Profit Margin = 75/500 = 0.15
   - Asset Turnover = Revenue/Total Assets = 500/400 = 1.25
   - Equity Multiplier = Total Assets/Equity = 400/150 = 2.67
   - ROE = 0.15 × 1.25 × 2.67 = **50.0%** ✓

**Interview insight:** "The DuPont decomposition reveals that the high ROE of 50% is driven primarily by the equity multiplier (high leverage at 2.67x) rather than operational efficiency. This is a risk flag — the company is using significant debt."

#### Practice
**Basic (3–5):**
1. What is the difference between an income statement and a balance sheet?
2. Calculate current ratio and quick ratio from given data.
3. What is the formula for ROE? Why is it important?
4. Explain the difference between EBITDA and net income.
5. What does a debt-to-equity ratio > 2 indicate?

**Intermediate (3–5):**
6. Given 3 years of financials, compute trend analysis for 5 key ratios.
7. Calculate operating cash flow from given net income, depreciation, and working capital changes.
8. A company has ROE = 15%, profit margin = 5%, asset turnover = 1.5. Find equity multiplier.
9. Compare two companies using DuPont analysis — which is more efficient?
10. Compute EV/EBITDA for a company with Enterprise Value = ₹500 Cr and EBITDA = ₹50 Cr.

**Interview-Level (5+):**
11. How would you identify financial statement manipulation (earnings management)?
12. Explain the difference between accrual and cash accounting. Which is more useful for analysis?
13. A company's P/E is 30x while industry average is 18x. What could explain this?
14. How do you adjust for one-time items when analyzing financial statements?
15. What is the quality of earnings ratio? How do you compute it?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Read this balance sheet — what do you notice? | Analytical observation |
| Compute 5 key ratios and interpret them | Technical skill |
| Is this company financially healthy? | Judgment |
| DuPont decomposition of ROE | Deep understanding |
| How would you value this company? | Bridge to next topic |

#### Common Mistakes
- **Confusing** revenue with profit — revenue is top line, profit is bottom line
- **Ignoring** cash flow — a company can be profitable but cash-poor
- **Not adjusting** for leverage when comparing ROE across companies
- **Using** market value ratios without understanding earnings quality
- **Forgetting** that D/E ratio can be negative (negative equity = distressed company)

#### Completion Criterion
✅ Can read and interpret all three financial statements
✅ Can compute and interpret 10+ financial ratios
✅ Can perform DuPont analysis
✅ Can identify red flags in financial statements

---

### Topic 2: Valuation Methods (DCF, Relative)

#### Why This Matters
Valuation is the heart of finance. Whether you're in investment banking, equity research, or corporate finance, the ability to value a company or project is the primary skill tested.

#### What to Learn
- [ ] Discounted Cash Flow (DCF) valuation: FCF projection, WACC, terminal value
- [ ] Free Cash Flow to Firm (FCFF) = EBIT(1-t) + D&A - CapEx - ΔNWC
- [ ] Free Cash Flow to Equity (FCFE) = Net Income + D&A - CapEx - ΔNWC + Net Borrowing
- [ ] Weighted Average Cost of Capital (WACC): WACC = E/(E+D) × Re + D/(E+D) × Rd × (1-t)
- [ ] Gordon Growth Model: Terminal Value = FCF × (1+g) / (WACC - g)
- [ ] Relative valuation: P/E, EV/EBITDA, P/B, P/S multiples
- [ ] Comparable company analysis (trading comps) and precedent transactions
- [ ] Enterprise Value = Equity + Debt - Cash

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`finance-overview.md`](finance-overview.md) | Valuation, NPV, IRR | Full |

#### Worked Example
**Problem:** Company X has the following data:

| Item | Value |
|:-----|------:|
| Current EBIT (Year 0) | ₹100 Cr |
| Tax rate | 25% |
| Depreciation | ₹20 Cr |
| CapEx | ₹25 Cr |
| ΔNet Working Capital | ₹5 Cr |
| EBIT growth (Years 1-5) | 10% per year |
| WACC | 12% |
| Terminal growth rate | 4% |
| Net Debt | ₹200 Cr |
| Shares outstanding | 10 Cr |

**Solution:**
1. **Project FCFF for 5 years:**

| Year | EBIT | EBIT(1-t) | D&A | CapEx | ΔNWC | FCFF |
|:----:|-----:|----------:|----:|------:|-----:|-----:|
| 1 | 110 | 82.5 | 20 | 27.5 | 5.5 | 69.5 |
| 2 | 121 | 90.75 | 22 | 30.25 | 6.05 | 76.45 |
| 3 | 133.1 | 99.83 | 24.2 | 33.28 | 6.66 | 84.09 |
| 4 | 146.4 | 109.8 | 26.6 | 36.6 | 7.32 | 92.48 |
| 5 | 161.1 | 120.8 | 29.3 | 40.3 | 8.06 | 101.74 |

2. **Terminal Value (Gordon Growth):**
   - TV = FCFF₅ × (1+g) / (WACC - g) = 101.74 × 1.04 / (0.12 - 0.04) = 1,058.1 / 0.08 = **₹1,321.7 Cr**

3. **Discount all cash flows at WACC (12%):**

| Year | Cash Flow | PV Factor | PV |
|:----:|----------:|----------:|----------:|
| 1 | 69.5 | 0.893 | 62.1 |
| 2 | 76.45 | 0.797 | 60.9 |
| 3 | 84.09 | 0.712 | 59.9 |
| 4 | 92.48 | 0.636 | 58.8 |
| 5 | 101.74 | 0.567 | 57.7 |
| 5 (TV) | 1,321.7 | 0.567 | 749.4 |

4. **Enterprise Value** = Sum of PVs = 62.1 + 60.9 + 59.9 + 58.8 + 57.7 + 749.4 = **₹1,048.8 Cr**

5. **Equity Value** = EV - Net Debt = 1,048.8 - 200 = **₹848.8 Cr**

6. **Price per share** = 848.8 / 10 = **₹84.88 per share**

#### Practice
**Basic (3–5):**
1. What is WACC? How do you calculate it?
2. Define FCFF and FCFE. When would you use each?
3. What is terminal value? Why is it often 60-80% of DCF value?
4. Explain the Gordon Growth Model for terminal value.
5. What is Enterprise Value vs Equity Value?

**Intermediate (3–5):**
6. Perform a 5-year DCF for a company given financial projections.
7. Calculate WACC given cost of equity (CAPM), cost of debt, and capital structure.
8. Compare DCF with relative valuation — when is each appropriate?
9. What happens to valuation if WACC increases by 2%?
10. Value a company using comparable P/E multiples.

**Interview-Level (5+):**
11. How sensitive is your DCF to terminal value? Perform sensitivity analysis.
12. What are the limitations of DCF? When does it fail?
13. How do you value a company with negative earnings?
14. Explain CAPM: Cost of Equity = Rf + β(Rm - Rf). What is beta?
15. How do you adjust DCF for cyclical industries?

#### Common Mistakes
- **Using** book value instead of market value for WACC weights
- **Ignoring** terminal value — it's often 60-80% of total value
- **Projecting** FCFF beyond 5 years without good reason
- **Confusing** FCFF and FCFE formulas
- **Not checking** if WACC > terminal growth rate (Gordon model breaks down)

#### Completion Criterion
✅ Can build a 5-year DCF from scratch
✅ Can calculate WACC using CAPM
✅ Can perform relative valuation using multiples
✅ Can do sensitivity analysis on key assumptions

---

### Topic 3: Corporate Finance & Capital Budgeting

#### Why This Matters
Corporate finance decisions — investment, financing, and dividend policy — are tested in every finance role. NPV, IRR, payback period, and capital structure theory are fundamental.

#### What to Learn
- [ ] Capital budgeting: NPV, IRR, Payback Period, Discounted Payback, Profitability Index
- [ ] NPV rule: Accept if NPV > 0; IRR rule: Accept if IRR > hurdle rate
- [ ] NPV vs IRR: Conflicting rankings (mutually exclusive projects, non-conventional cash flows)
- [ ] Capital structure: Modigliani-Miller propositions (with and without taxes)
- [ ] Cost of equity: CAPM (Re = Rf + β(Rm - Rf))
- [ ] Cost of debt: After-tax cost = Interest rate × (1 - tax rate)
- [ ] Dividend policy: Irrelevance theory (Miller-Modigliani), clientele effect, signaling
- [ ] Working capital management: Cash conversion cycle, inventory management

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`finance-overview.md`](finance-overview.md) | NPV, IRR, capital budgeting | Full |

#### Worked Example
**Problem:** A company is evaluating two mutually exclusive projects:

| Year | Project A (₹ Cr) | Project B (₹ Cr) |
|:----:|------------------:|------------------:|
| 0 | -200 | -300 |
| 1 | 80 | 100 |
| 2 | 80 | 120 |
| 3 | 80 | 140 |
| 4 | 80 | 60 |

Cost of capital = 12%. Which project should be accepted?

**Solution:**
1. **NPV Calculation:**
   - NPV_A = -200 + 80/1.12 + 80/1.12² + 80/1.12³ + 80/1.12⁴
   - NPV_A = -200 + 71.4 + 63.8 + 56.9 + 50.8 = **₹42.9 Cr**

   - NPV_B = -300 + 100/1.12 + 120/1.12² + 140/1.12³ + 60/1.12⁴
   - NPV_B = -300 + 89.3 + 95.7 + 99.6 + 38.1 = **₹22.7 Cr**

2. **IRR Calculation (by interpolation):**
   - For A: At 20%, NPV = -200 + 80(2.589) = +7.1; at 22%, NPV = -200 + 80(2.494) = -0.5
   - IRR_A ≈ **21.9%**
   - For B: At 16%, NPV = +11.2; at 18%, NPV = -4.3
   - IRR_B ≈ **17.0%**

3. **Decision:**
   - NPV_A (₹42.9 Cr) > NPV_B (₹22.7 Cr) → Accept **Project A**
   - IRR_A (21.9%) > IRR_B (17.0%) → Confirms **Project A**
   - No conflict in this case. Accept **Project A**.

4. **Incremental IRR Check (for conflicts):**
   - Cash flow (B-A): -100, +20, +40, +60, -20
   - Incremental IRR ≈ 14.5% > 12% → B would also be acceptable if incremental
   - But since NPV_A > NPV_B, A is superior

**Key insight:** "When NPV and IRR conflict for mutually exclusive projects, always go with NPV. IRR assumes reinvestment at IRR, while NPV assumes reinvestment at cost of capital — NPV's assumption is more realistic."

#### Practice
**Basic (3–5):**
1. Define NPV, IRR, and Payback Period. State the accept/reject rule for each.
2. Calculate NPV for a project with initial outlay ₹100 Cr, annual inflows ₹40 Cr for 4 years, discount rate 10%.
3. What is the profitability index? When is it useful?
4. Explain the difference between independent and mutually exclusive projects.
5. What is the reinvestment rate assumption for IRR vs NPV?

**Intermediate (3–5):**
6. Two projects have different cash flow patterns — compute NPV and IRR for each and check for conflict.
7. Calculate WACC for a company with 40% equity (cost 15%), 60% debt (cost 8%, tax 30%).
8. What is the optimal capital structure? Explain with M&M Proposition II.
9. Compute the cash conversion cycle given DSO, DIO, and DPO.
10. A project has unconventional cash flows (- + - +). Can IRR be used? What is the alternative?

**Interview-Level (5+):**
11. Explain M&M Proposition I with taxes. How does debt create value?
12. What is the pecking order theory of financing?
13. How do you handle a project with a large terminal value (e.g., mining)?
14. Compare NPV with real options — when does NPV undervalue a project?
15. Explain the WACC formula derivation from the weighted cost of each component.

#### Common Mistakes
- **Assuming** IRR is always superior to NPV — it's not
- **Ignoring** the scale difference when comparing NPV of projects of different sizes
- **Using** IRR for mutually exclusive projects without incremental IRR check
- **Confusing** WACC with cost of equity
- **Forgetting** that debt tax shield reduces WACC

#### Completion Criterion
✅ Can compute NPV, IRR, Payback for any project
✅ Can calculate WACC using CAPM
✅ Can explain M&M propositions
✅ Can identify when NPV and IRR conflict and resolve it

---

### Topic 4: Interview Case Studies & Market Sizing

#### Why This Matters
Finance interviews increasingly use case studies and guesstimates to test analytical thinking. Being able to structure a problem, make reasonable assumptions, and arrive at a defensible answer is essential.

#### What to Learn
- [ ] Guesstimate framework: Top-down, bottom-up, demand-side, supply-side
- [ ] Market sizing: TAM, SAM, SOM
- [ ] Profitability cases: Revenue drivers, cost structure, margin analysis
- [ ] Investment cases: Bull/bear case, key drivers, risks
- [ ] Structured problem-solving: Issue trees, MECE framework
- [ ] Mental math shortcuts for quick calculations

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`finance-overview.md`](finance-overview.md) | Case framework, interview prep | Reference |
| [`case-frameworks.md`](../consulting/case-frameworks.md) | Structured problem-solving | Reference |

#### Worked Example
**Problem:** "Estimate the market size for food delivery apps in India."

**Solution (Top-Down Approach):**
1. **India population:** ~1.4 billion
2. **Urban population:** ~35% = 490 million
3. **Smartphone users (urban):** ~70% = 343 million
4. **People using food delivery apps:** ~20% = 68.6 million
5. **Average orders per month per user:** ~4
6. **Average order value:** ₹350
7. **Monthly market:** 68.6M × 4 × ₹350 = ₹96,040 Cr/year
8. **Annual market:** ₹96,040 × 12 = **~₹11.5 lakh Cr** (~$140 billion)

**Sanity check (bottom-up):**
- Zomato reports ~50 million transacting users, AOV ~₹400
- Swiggy similar scale
- Total market ~$15-20 billion (actual reported numbers)
- My estimate is 7x too high → adjust food delivery frequency to ~1.5 orders/month
- Revised: 68.6M × 1.5 × ₹350 × 12 = **₹4.3 lakh Cr** (~$52 billion) — closer to reality

**Interview insight:** "Always sanity-check your estimate. Interviewers don't expect exact answers — they want to see your structured thinking and ability to self-correct."

#### Practice
**Basic (3–5):**
1. Estimate the number of restaurants in a city of 5 million.
2. How many cars are sold in India annually?
3. What is the TAM for online education in India?
4. Estimate the daily water consumption of a 10-story office building.
5. Size the smartphone market in Southeast Asia.

**Intermediate (3–5):**
6. "Should our bank enter the credit card business?" — Structure the analysis.
7. A company's revenue grew 20% but profit declined 10%. What could explain this?
8. "Is Netflix a good investment at current valuations?" — Build a bull/bear case.
9. Estimate the market for EV charging stations in India by 2030.
10. "A restaurant chain wants to expand — should they open 10 new outlets or franchise?"

**Interview-Level (5+):**
11. "We're seeing declining margins — diagnose the problem." (Framework: revenue mix, cost inflation, competitive pressure, operating leverage)
12. Build a 3-statement financial model from scratch (conceptual walkthrough).
13. "A PE firm is considering acquiring a mid-size company — what due diligence would you do?"
14. "Is the Indian infrastructure sector a good investment right now?" — Use your civil engineering knowledge.
15. "Our DCF shows ₹500/share but the market price is ₹350. What are we missing?"

#### Common Mistakes
- **Jumping** to numbers without a framework
- **Not** sanity-checking estimates against known data
- **Overcomplicating** — keep assumptions simple and defensible
- **Not** communicating your thought process aloud
- **Ignoring** the civil engineering angle — use it as a differentiator

#### Completion Criterion
✅ Can structure any guesstimate using top-down or bottom-up approach
✅ Can size a market (TAM/SAM/SOM) with reasonable assumptions
✅ Can diagnose business problems using structured frameworks
✅ Can link civil engineering knowledge to finance case studies

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | A company has Revenue = ₹800 Cr, COGS = ₹480 Cr, OpEx = ₹160 Cr, Interest = ₹30 Cr, Tax = 25%. Total Assets = ₹600 Cr, Equity = ₹250 Cr, Current Assets = ₹250 Cr, Current Liabilities = ₹150 Cr. Compute: Gross margin, operating margin, net margin, current ratio, D/E, ROE, ROA, DuPont decomposition. | Financial Statements | 25 |
| 2 | Perform a 5-year DCF for a company: EBIT = ₹50 Cr (growing 15%/yr), D&A = ₹8 Cr, CapEx = ₹12 Cr, ΔNWC = ₹3 Cr, WACC = 14%, terminal growth = 3%, Net Debt = ₹150 Cr, Shares = 5 Cr. Find EV, equity value, price per share. | Valuation | 25 |
| 3 | Two projects: A (outlay ₹150 Cr, inflows ₹60 Cr/yr for 4 years), B (outlay ₹200 Cr, inflows ₹40,60,80,100 Cr). Cost of capital = 12%. Compute NPV, IRR, Payback for each. Which to accept? | Capital Budgeting | 20 |
| 4 | Estimate the annual market size for electric vehicles in India by 2028. Show your assumptions clearly. | Market Sizing | 15 |
| 5 | Explain CAPM. If Rf = 7%, β = 1.3, market return = 14%, what is the cost of equity? If debt cost = 9%, tax = 30%, and D/E = 0.5, compute WACC. | Corporate Finance | 15 |
| | | **Total** | **100** |

---

## Interview Strategy

### Technical Interview (15–20 minutes)
1. **Lead with ratios** — always ask for financial statements first
2. **Show your work** — write formulas, plug numbers, interpret results
3. **Connect to business** — "This ratio suggests the company is highly leveraged, which increases financial risk"
4. **Use your civil background** — "In construction project finance, I would apply NPV analysis to..."

### Valuation Discussion
- **Always state assumptions** — growth rate, WACC, terminal value method
- **Sanity-check** — "A P/E of 50x seems high; let me check the growth rate justification"
- **Know your CAPM inputs** — current risk-free rate, typical market return, how to estimate beta

### Case Study Framework
1. **Clarify** the question (30 seconds)
2. **Structure** the problem using a framework (1 minute)
3. **Analyze** — go through the issue tree systematically (3-4 minutes)
4. **Recommend** with clear rationale (1 minute)

---

## Cross-Links

**Next:**
→ [Finance Overview](finance-overview.md) — Complete preparation system

**Study:**
→ [Quantitative Aptitude](../../non-core/aptitude/quantitative/aptitude-basics.md) — Math fundamentals
→ [Technical Stack](../analytics/technical-stack.md) — Tools for finance roles

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)
→ [HR Questions](../../prep/behavioral/hr_questions/hr-questions-bank.md)

**Related:**
→ [Risk Study Plan](../risk/role-study-plan.md) — For risk management roles
→ [Strategy Overview](../strategy/strategy-overview.md) — For strategy roles

---

*This study plan follows the [Role Study Plan Template](../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*

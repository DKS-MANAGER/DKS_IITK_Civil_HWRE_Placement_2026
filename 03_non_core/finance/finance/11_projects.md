# 11. General Finance: Suggested Modeling Projects & Resume Guidance

> Practical, reproducible project blueprints in valuation, financial modeling, and corporate analysis, with guidelines for aligning quantitative engineering backgrounds on resumes.
> 
> *Notice: The projects below are suggested project briefs designed for self-directed study and portfolio demonstration ([PREPARATION HEURISTIC]). Candidates should execute these models using public or synthetic datasets and report actual reproducible findings rather than claiming unverified metrics.*

---

## 1. Portfolio Project Architecture

Recruiters look for projects demonstrating clean modeling architecture, disciplined accounting mechanics, and clear commercial intuition:

```
┌─────────────────────────────────────────────────────────────┐
│ Project 1: Automated DCF Valuation & Scenario Engine         │
│ • Domain: Investment Banking / Fundamental Equity Research  │
│ • Tooling: Microsoft Excel (Dynamic Arrays) & Python        │
│ • Core Output: Football-field valuation summary chart       │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌─────────────────────────────▼──────────────────────────────┐
│ Project 2: Infrastructure Project Finance & DSCR Model      │
│ • Domain: Project Finance / Infrastructure Debt Underwriting│
│ • Tooling: Excel / Python (`numpy-financial`)               │
│ • Core Output: Debt Service Coverage Ratio (DSCR) schedule  │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌─────────────────────────────▼──────────────────────────────┐
│ Project 3: Working Capital & Cash Conversion Cycle Engine   │
│ • Domain: Corporate Finance / Treasury Management           │
│ • Tooling: SQL & Python (`pandas`)                          │
│ • Core Output: AR aging bucket analysis & cash release model│
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Suggested Project Blueprints

### Project 1: Automated DCF Valuation & Scenario Engine
- **Core Research Question**: How sensitive is the intrinsic valuation of an Indian capital-goods manufacturer to changes in the cost of capital (WACC) and terminal growth assumptions?
- **Dataset**: Publicly available 5-year annual reports from NSE/BSE archives or Screener.in for an Indian listed firm (e.g., Bharat Electronics, Cummins India).
- **Methodology**:
  1. Standardize 5 years of historical Income Statements, Balance Sheets, and Cash Flow Statements.
  2. Project revenues using a 3-tier scenario toggle (Bull: +18%, Base: +12%, Bear: +6%).
  3. Forecast Unlevered Free Cash Flow (FCFF) accounting for working capital requirements and CapEx reinvestment rates.
  4. Estimate WACC using CAPM (10-Yr G-Sec yield, peer unlevered beta, market risk premium).
  5. Compute terminal value using both Gordon Growth and exit multiple approaches.
  6. Generate a 2D sensitivity table (WACC vs Terminal Growth Rate) in Excel.
- **Validation**:
  - Reconcile model enterprise value with current trading market capitalization; identify whether divergence is driven by growth expectations or margin assumptions.
- **Outputs**:
  - Complete Excel workbook following standard formatting (blue inputs, black formulas, green cross-sheet links).
  - One-page investment memo summarizing DCF findings, key downside risks, and trading comps triangulation.
- **Limitations**:
  - DCF outputs are highly sensitive to small shifts in WACC and terminal growth; does not capture real option value or sudden regulatory tariff changes.

---

### Project 2: Infrastructure Project Finance & Debt Service Coverage (DSCR) Model
- **Core Research Question**: Under what traffic volume and interest rate stress scenarios does a toll-road concessionaire breach minimum debt covenants?
- **Dataset**: Synthetic project finance dataset modeling a 20-year Build-Operate-Transfer (BOT) highway concession ([PRACTICE ASSUMPTION]).
- **Methodology**:
  1. Construct a 20-year cash flow waterfall: Gross Toll Revenue $\to$ O&M Costs $\to$ Major Maintenance Reserve $\to$ Cash Flow Available for Debt Service (CFADS).
  2. Model debt repayment under sculpted amortization schedule to maintain flat DSCR.
  3. Calculate annual Debt Service Coverage Ratio ($\text{DSCR} = \frac{\text{CFADS}}{\text{Principal} + \text{Interest}}$) and Project IRR vs Equity IRR.
  4. Stress test against: (a) 20% traffic volume drop, (b) 200 bps increase in floating borrowing rate, (c) 15% O&M cost overrun.
- **Validation**:
  - Verify that minimum DSCR remains $\ge 1.20\times$ and average DSCR $\ge 1.35\times$ under base case, matching standard lender covenants.
- **Outputs**:
  - Dynamic financial model with Debt Service Reserve Account (DSRA) mechanism and dividend lockup triggers.
- **Limitations**:
  - Ignores potential renegotiation of concession agreements or government force majeure compensation.

---

### Project 3: Working Capital & Cash Conversion Cycle Optimization Engine
- **Core Research Question**: How much non-dilutive liquidity can be unlocked by optimizing inventory turns and customer credit terms in a distribution business?
- **Dataset**: Synthetic relational transactional database containing 10,000+ customer invoices and vendor purchase orders ([PRACTICE ASSUMPTION]).
- **Methodology**:
  1. Write SQL queries to extract Accounts Receivable aging buckets (Current, 1–30, 31–60, 61–90, 90+ days).
  2. Compute historical DSO, DSI, DPO, and Cash Conversion Cycle (CCC).
  3. Simulate the cash impact of: (a) Enforcing 2/10 Net 30 early payment discounts, (b) ABC inventory classification to eliminate slow-moving stock, (c) Extending vendor terms to 45 days.
  4. Quantify net liquidity released and interest expense reduction.
- **Validation**:
  - Check that total working capital changes equal the sum of receivables, inventory, and payables adjustments.
- **Outputs**:
  - Relational SQL queries for automated monthly aging reports.
  - Python dashboard showing CCC trend and working capital bridge.
- **Limitations**:
  - Aggressive vendor payment extensions can damage supplier relationships or result in higher purchase prices.

---

## 3. Resume Framing & Background Translation

When presenting financial analysis projects on an IIT Kanpur engineering resume, adhere strictly to verifiable facts:

### Recommended Resume Formatting

```markdown
### Financial Valuation & Corporate Analysis Projects

**Automated 3-Statement Valuation Model & DCF Scenario Engine** | *Independent Project*
• Constructed dynamic 5-year financial model in Excel for Indian industrial enterprise, forecasting FCFF across Bull/Base/Bear scenarios.
• Calculated 12.8% WACC via CAPM with peer-unlevered betas; established Gordon Growth terminal value and 2D sensitivity data table.
• Triangulated DCF enterprise value against EV/EBITDA trading multiples across 4 public peers to derive target equity value per share.

**Infrastructure Project Finance & Debt Service Simulation** | *Independent Project*
• Modeled 20-year cash flow waterfall for a Build-Operate-Transfer (BOT) infrastructure asset with senior debt sculpted amortization.
• Formulated dynamic Debt Service Coverage Ratio (DSCR) schedule, stress-testing covenants against traffic shocks and interest rate spikes.
• Implemented automated Debt Service Reserve Account (DSRA) and dividend lockup logic to analyze lender credit protection.
```

### Bridging Civil & Hydro-systems Engineering to Finance
- **Mathematical Modeling**: Frame complex fluid mechanics, hydrology, or structural optimization as evidence of strong computational stamina, multi-variable calculus fluency, and quantitative discipline.
- **Risk & Uncertainty**: Emphasize how probability distributions, Monte Carlo simulations, and extreme event modeling in engineering translate directly to financial risk analysis and capital allocation under uncertainty.
- **Ethical Rule**: Never fabricate investment banking transaction experience, live client deals, or unverified financial metrics. Present independent modeling projects clearly as self-directed academic and portfolio work.

---

## 4. Verification & Navigation Links
- 📖 [Role Overview](01_role-overview.md)
- 📖 [Domain Knowledge Complete Reference](03_domain-knowledge.md)
- 📖 [Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Worked Cases & Financial Models](07_practice-and-cases.md)
- 📖 [High-Yield Question Bank](06_question-bank.md)
- 📖 [Full Mock Assessment](12_mock-assessment.md)
- 📖 [Risk Analytics Projects](../risk/11_projects.md)

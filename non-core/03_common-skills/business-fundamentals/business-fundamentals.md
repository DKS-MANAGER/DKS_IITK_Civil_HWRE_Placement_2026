# Business Fundamentals & Quantitative Mini-Cases
**Target:** Universal Business Literacy for Non-Core Corporate Placements  
**Scope:** Management Consulting, Product Management, Analytics, Strategy & Operations, Quantitative Finance  
**Format:** Core Formulas $\to$ Financial Mechanics $\to$ Numerical Decision Mini-Cases $\to$ Interview Probes

---

## 1. Income Statement Mechanics & Profitability Metrics

```
Revenue (Top Line)
  - Cost of Goods Sold (Direct Materials + Direct Labor)
= Gross Profit (Gross Margin % = Gross Profit / Revenue)
  - Operating Expenses (SG&A, R&D, Sales & Marketing)
= Operating Profit (EBIT)
  + Depreciation & Amortization (Non-Cash Accounting Allocations)
= EBITDA
  - Interest Expense
  - Corporate Taxes
= Net Profit (Bottom Line)
```

### 1.1 Key Profitability Definitions & Critical Financial Nuance

| Metric | Formula | Financial Significance | Common Interview Pitfalls & Traps |
|:---|:---|:---|:---|
| **Gross Profit** | $\text{Revenue} - \text{COGS}$ | Measures direct production/service delivery efficiency before corporate overhead. | Confusing COGS (direct production) with operating overhead (rent, marketing). |
| **EBIT (Operating Profit)** | $\text{Gross Profit} - \text{OpEx}$ | Core operational earnings generated exclusively by core business operations. | Mixing non-operating investment gains into operating profit. |
| **EBITDA** | $\text{EBIT} + \text{D\&A}$ | Operating earnings before non-cash capital depreciation, amortization, and financing structure. | **Trap:** Calling EBITDA "cash flow". EBITDA ignores working capital absorption ($\Delta WC$) and taxes. |
| **Operating Cash Flow ($OCF$)** | $\text{EBITDA} - \text{Taxes} - \Delta\text{WC}$ | True cash generated from operational cycle available for debt service and reinvestment. | Ignoring accounts receivable build-up when evaluating profitable growth. |
| **Net Profit** | $\text{EBIT} - \text{Interest} - \text{Taxes}$ | Residual earnings available to equity shareholders ("Bottom Line"). | Forgetting interest payments on debt obligations. |

> [!WARNING]
> **Financial Governance Rule: EBITDA is NOT Operating Cash Flow ($OCF$)**  
> EBITDA ($\text{EBIT} + \text{D\&A}$) measures operational accounting profitability before non-cash capital depreciation. It does **not** equal cash generated from operations because:
> 1. **Working Capital Changes ($\Delta WC$):** Rapid revenue growth recognized on credit locks cash into unpaid receivables ($\text{AR}$), draining liquidity.
> 2. **Taxes:** Income taxes must be settled in cash, not non-cash accounting items.
> 3. **CapEx:** Physical plant, fleet, and hardware require maintenance capital expenditure just to sustain ongoing operations.  
> *True Operating Cash Flow:* $\text{OCF} = \text{EBITDA} - \text{Taxes} - \Delta\text{WC}$. Always distinguish accounting earnings from liquid cash flow.

---

### 1.2 Quantitative Mini-Case: EBITDA vs. Operating Cash Flow Divergence

**Business Scenario:**  
An enterprise B2B logistics startup reports a $+40\%$ surge in EBITDA from $\text{INR } 10.0\text{ Crores}$ to $\text{INR } 14.0\text{ Crores}$ in FY25. However, the company's bank cash reserves dropped by $\text{INR } 6.0\text{ Crores}$ over the same fiscal year.

```
Financial Audit Breakdown:
- EBITDA: INR 14.0 Cr
- Cash Taxes Paid: INR 2.5 Cr
- Capital Expenditures (CapEx): INR 5.0 Cr
- Beginning Accounts Receivable (AR): INR 4.0 Cr
- Ending Accounts Receivable (AR): INR 16.5 Cr (Clients taking 120 days to pay)
- Inventory & Payables net change: INR 0.0 Cr
```

**Quantitative Deduction:**
1. $\Delta\text{Working Capital} = \text{Ending AR} - \text{Beginning AR} = 16.5 - 4.0 = +\text{INR } 12.5\text{ Crores}$ (Cash locked in unpaid client invoices).
2. $\text{Operating Cash Flow (OCF)} = \text{EBITDA} - \text{Taxes} - \Delta\text{WC} = 14.0 - 2.5 - 12.5 = -\text{INR } 1.0\text{ Crore}$.
3. $\text{Free Cash Flow to Firm (FCFF)} = \text{OCF} - \text{CapEx} = -1.0 - 5.0 = -\text{INR } 6.0\text{ Crores}$.

**Interview Executive Synthesis:**  
*"While headline EBITDA expanded rapidly, the company's aggressive revenue recognition on loose credit terms caused Accounts Receivable to balloon by $\text{INR } 12.5\text{ Cr}$. This created a negative Operating Cash Flow of $-\text{INR } 1.0\text{ Cr}$, draining liquidity despite positive accounting profits."*

---

## 2. Cost Structure, Operating Leverage & Break-Even Optimization

### 2.1 Core Cost Concepts

- **Fixed Costs ($FC$):** Invariant with short-term volume (factory rent, core software licenses, salaried engineers).
- **Variable Costs ($VC$):** Scale directly with unit volume (raw materials, cloud computing compute-hours per user, shipping).
- **Contribution Margin ($CM$):**
  $$CM = \text{Price} - \text{Variable Cost per Unit}$$
  $$CM\% = \frac{\text{Price} - \text{Variable Cost per Unit}}{\text{Price}} \times 100\%$$
- **Break-Even Volume ($Q_{BE}$):**
  $$Q_{BE} = \frac{\text{Fixed Costs}}{CM} = \frac{\text{Fixed Costs}}{\text{Price} - \text{Variable Cost per Unit}}$$

---

### 2.2 Quantitative Mini-Case: Operating Leverage & Pricing Trade-Off

**Scenario:**  
A manufacturer produces industrial filtration units.  
- Selling Price $P = \text{INR } 10,000/\text{unit}$
- Variable Cost $VC = \text{INR } 6,000/\text{unit}$ ($CM = \text{INR } 4,000/\text{unit}$)
- Fixed Costs $FC = \text{INR } 20,00,000/\text{year}$
- Current Sales Volume $Q = 1,000\text{ units/year}$ (Operating Profit $= 1,000 \times 4,000 - 20,00,000 = \text{INR } 20,00,000$).

The VP of Sales proposes a **$10\%$ price reduction** to $\text{INR } 9,000$, projecting a **$25\%$ volume expansion** to $1,250\text{ units}$. Should the CEO approve this proposal?

**Step-by-Step Analysis:**
1. **New Contribution Margin per Unit:**
   $$CM_{\text{new}} = 9,000 - 6,000 = \text{INR } 3,000/\text{unit} \quad (-25\% \text{ drop in unit margin})$$
2. **New Total Contribution:**
   $$\text{Total } CM_{\text{new}} = 1,250 \times 3,000 = \text{INR } 37,50,000$$
3. **New Operating Profit:**
   $$\text{EBIT}_{\text{new}} = 37,50,000 - 20,00,000 = \text{INR } 17,50,000$$
4. **Profit Comparison:**
   $$\Delta\text{EBIT} = 17,50,000 - 20,00,000 = -\text{INR } 2,50,000 \quad (-12.5\% \text{ decline})$$

**Strategic Verdict:**  
**Reject the proposal.** Because variable costs remained fixed at $\text{INR } 6,000$, the $10\%$ price cut eroded unit contribution margin by $25\%$. A $25\%$ volume surge was mathematically insufficient to offset the margin compression. To maintain current profit, volume would need to increase to:
$$Q_{\text{required}} = \frac{20,00,000 + 20,00,000}{3,000} = \frac{40,00,000}{3,000} = 1,334\text{ units} \quad (+33.4\% \text{ volume required}).$$

---

## 3. Unit Economics & Business Model Heuristics

### 3.1 Customer Acquisition Cost ($CAC$) & Customer Lifetime Value ($LTV$)

- **Customer Acquisition Cost ($CAC$):**
  $$CAC = \frac{\text{Total Sales \& Marketing Expenditure in Period } t}{\text{New Customers Acquired in Period } t}$$
- **Customer Lifetime Value ($LTV$):**
  $$LTV = \frac{\text{Average Revenue per Customer (ARPU)} \times \text{Gross Margin \%}}{\text{Customer Churn Rate}}$$
- **CAC Payback Period:**
  $$\text{Payback Period (Months)} = \frac{CAC}{\text{Monthly ARPU} \times \text{Gross Margin \%}}$$

### 3.2 Contextual LTV:CAC Benchmarks [PREPARATION HEURISTIC]

> [!NOTE]
> **Methodological Status: [PREPARATION HEURISTIC]**  
> The $LTV:CAC$ ratio bands below represent private equity, venture capital, and corporate finance practitioner rules-of-thumb rather than empirical statistical distributions or strict company screening cutoffs. Use them to structure strategic interview recommendations, not as absolute mathematical laws.

| Business Model Type | Typical Healthy $LTV:CAC$ | Why the Benchmark Differs | Danger Zone |
|:---|:---:|:---|:---|
| **Enterprise B2B SaaS** (Long sales cycles, multi-year contracts) | **$3.5 : 1$ to $5.0 : 1$** | High upfront sales & POC engineering costs; very low gross churn ($< 5\%$). | $< 2.5 : 1$ (unsustainable cash burn). |
| **High-Volume B2C Subscription** (Streaming, consumer apps) | **$2.5 : 1$ to $3.5 : 1$** | Lower acquisition friction; higher natural churn ($20\text{–}30\%$ annually). | $< 1.8 : 1$ (margin eaten by marketing). |
| **Asset-Heavy Infra / Hardware** (High CapEx, installation) | **$2.0 : 1$ to $3.0 : 1$** | Heavy upfront balance-sheet financing; low margins on initial hardware. | $< 1.5 : 1$ (debt default risk). |
| **Transactional E-Commerce / Marketplace** | **$2.0 : 1$ to $3.0 : 1$** | Repeat purchase frequency determines longevity; low initial order value. | $< 1.2 : 1$ (immediate operating loss). |

---

### 3.3 Quantitative Mini-Case: Cohort Churn & Payback Optimization

**Scenario:**  
A subscription EdTech platform targeting engineering students acquires $1,000\text{ subscribers}$ at $CAC = \text{INR } 1,800$.  
- Monthly Subscription Fee $= \text{INR } 600$
- Platform Hosting & Support Gross Margin $= 75\%$
- Monthly User Churn Rate $= 5\%$

**Questions to Solve:**
1. What is the customer CAC payback period?
2. What is the expected $LTV$ and the $LTV:CAC$ ratio?

**Calculation:**
1. **Monthly Gross Profit per User:**
   $$\text{Monthly GP} = 600 \times 0.75 = \text{INR } 450/\text{month}$$
2. **CAC Payback Period:**
   $$\text{Payback} = \frac{1,800}{450} = 4.0\text{ months}$$
3. **Customer Lifetime ($1/\text{Churn}$):**
   $$\text{Average Lifespan} = \frac{1}{0.05} = 20\text{ months}$$
4. **$LTV$ Calculation:**
   $$LTV = 20 \times 450 = \text{INR } 9,000$$
5. **$LTV:CAC$ Ratio:**
   $$\frac{LTV}{CAC} = \frac{9,000}{1,800} = 5.0 : 1 \quad (\text{Highly attractive unit economics})$$

---

## 4. Growth, Churn & Cohort Retention Dynamics

```
Cohort Month 0: 1,000 Users (100%)
Month 1:        850 Users (85% Retention / 15% Churn)
Month 2:        765 Users (90% MoM Retention / 10% MoM Churn)
Month 3:        720 Users (94% MoM Retention / 6% MoM Churn)
Month 6:        680 Users (Steady-State Core Cohort)
```

- **Net Revenue Retention ($NRR$):**
  $$NRR\% = \frac{\text{Starting ARR} + \text{Expansion ARR} - \text{Contraction ARR} - \text{Churn ARR}}{\text{Starting ARR}} \times 100\%$$
  - If $NRR > 100\%$ (e.g., $125\%$), the existing customer base grows organically without spending a single dollar on new customer acquisition ("negative churn").

---

## 5. Market Sizing: TAM $\to$ SAM $\to$ SOM Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│ TOTAL ADDRESSABLE MARKET (TAM)                                         │
│ Total theoretical market demand for product/service globally.          │
│ e.g., Global Commercial Water Quality Monitoring Market: $12B          │
├────────────────────────────────────────────────────┬───────────────────┤
│ SERVICEABLE ADDRESSABLE MARKET (SAM)               │                   │
│ Market segment targetable by your specific tech    │                   │
│ and geography. e.g., Indian Industrial Effluents:  │                   │
│ $1.8B                                              │                   │
├──────────────────────────────────────────────┬─────┴───────────────────┤
│ SERVICEABLE OBTAINABLE MARKET (SOM)          │                         │
│ Realistic market share capturable within 3-5 │                         │
│ years given sales channels. e.g., $120M      │                         │
└──────────────────────────────────────────────┴─────────────────────────┘
```

---

## 6. Business Problem-Solving Cheat Sheet for Interviews

When asked to diagnose business performance, structure your investigation into 4 investigative buckets:

```
                  THE 4-BUCKET DIAGNOSTIC TREE
├── 1. Revenue Drivers (Price × Volume)
│   ├── Pricing: List price, discounts, product mix, contractual indexation
│   └── Volume: Market demand, competitor entry, churn, sales pipeline conversion
├── 2. Cost Drivers (Fixed vs. Variable)
│   ├── Direct COGS: Raw material inflation, scrap rate, supplier leverage
│   └── OpEx: Sales compensation, server efficiency, facility lease terms
├── 3. Working Capital & Cash Timing
│   ├── Accounts Receivable (DSO — Days Sales Outstanding)
│   ├── Inventory Turnover (Days Inventory Held)
│   └── Accounts Payable (DPO — Days Payable Outstanding)
└── 4. Unit Economics & Customer Life Cycle
    ├── Customer Acquisition Cost ($CAC$) & Channel ROI
    └── Cohort Retention, Net Expansion ($NRR$), and Churn Velocity
```

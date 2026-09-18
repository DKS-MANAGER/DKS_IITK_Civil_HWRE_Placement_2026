# Interactive Management Consulting & Strategic Case Simulation Suite

> **Domain:** Strategy Consulting (McKinsey, BCG, Bain, Kearney), Product Strategy, and Strategic Analytics  
> **Diagnostic Standard:** Realistic Case Dialogue · MECE Issue Decomposition · Interviewer Pushback & Follow-Up Branching · Quantitative Exhibits  
> **Target:** IIT Kanpur Postgraduate Corporate Placements 2026

---

## 🧭 Master Case Directory

| Case ID | Title | Sector & Business Problem | Core Analytical Tools | Interviewer Pushback Type |
|:---|:---|:---|:---|:---|
| [**Case 1**](#case-1-airline-fuel-efficiency--ancillary-revenue-turnaround) | Commercial Airline Turnaround | Profitability Collapse (-40% EBITDA) | MECE Tree, Unit Economics, Cost Optimization | Margin vs Volume Trade-off |
| [**Case 2**](#case-2-ev-two-wheeler-swappable-battery-market-entry) | EV Battery Swapping Market Entry | Market Sizing & Entry Strategy | TAM/SAM/SOM, Payback, CapEx vs OpEx | Regulatory & Asset Utilization |
| [**Case 3**](#case-3-quick-commerce-dark-store-unit-economics) | Quick-Commerce Dark Store Model | Supply Chain & Micro-Fulfillment | Contribution Margin per Order, Churn | Surge vs Rider Utilization |
| [**Case 4**](#case-4-enterprise-saas-pricing--expansion-leakage) | Enterprise SaaS Pricing Overhaul | B2B Churn & Tiered Seat Pricing | Net Retention Rate, LTV:CAC, Feature Gating | Gross Margin Compression |

---

## Case 1: Airline Fuel Efficiency & Ancillary Revenue Turnaround

### 1. The Interviewer Prompt
> *"Our client is SkyWings India, a domestic low-cost carrier operating 60 narrow-body aircraft. Over the past 18 months, despite passenger load factors rising from 82% to 88%, the airline's EBITDA margin has collapsed from +14% to -4%. The CEO has hired us to diagnose the root cause of this profitability collapse and develop a 12-month operational turnaround strategy."*

### 2. Candidate Clarifying Questions & Scoping
- **Candidate:** *"Is this margin compression unique to SkyWings or an industry-wide headwind across Indian civil aviation?"*
  - **Interviewer Response:** *"Competitor airlines experienced an average EBITDA decline of 4 percentage points over the same period, whereas our client dropped 18 percentage points."*
- **Candidate:** *"Has our route network (metro-to-metro vs Tier-2/3) or ticket pricing structure shifted significantly?"*
  - **Interviewer Response:** *"Average base fare is flat at INR 4,200, and our route mix has remained identical."*

### 3. MECE Issue Decomposition Tree

```
                                  PROFIT COLLAPSE (-18% EBITDA)
                                                │
                ┌───────────────────────────────┴───────────────────────────────┐
                ▼                                                               ▼
        REVENUE LEAKAGE                                                 COST ESCALATION
                │                                                               │
    ┌───────────┴───────────┐                                       ┌───────────┴───────────┐
    ▼                       ▼                                       ▼                       ▼
PASSENGER FARE      ANCILLARY REVENUE                           FUEL EXPENSES       NON-FUEL OPEX
- Base Yields       - Baggage & Seat Select                     - ATF Price (Macro) - Aircraft Lease ($ FX)
- Load Factor (+6%) - In-flight Retail & Meals                  - Burn Rate (Fleet) - Maintenance & Turnaround
- Promo Dilution    - Corporate Cargo Freight                   - Hedging Loss      - Crew & Airport Charges
```

### 4. Quantitative Exhibit Analysis (Interviewer Pushback)

```
EXHIBIT 1: SkyWings vs. Benchmark Airline Unit Economics (Per Available Seat Kilometer - ASK)

Metric                           SkyWings (FY24)     SkyWings (FY26)     Industry Benchmark
-----------------------------------------------------------------------------------------
Average Base Fare (INR)               4,200               4,200               4,400
Ancillary Revenue per Pax (INR)         480                 210                 650
Aviation Turbine Fuel (INR/ASK)        1.42                1.95                1.68
Average Fleet Age (Years)              11.2                13.2                 4.5
Turnaround Time at Gate (min)            48                  52                  28
Daily Aircraft Utilization (hrs)       10.5                 9.2                12.8
```

#### Quantitative Deduction:
1. **Ancillary Revenue Collapse:** Ancillary spend per passenger dropped by $\text{INR } 270$ ($480 \to 210$). At 12 million annual passengers, this represents a pure margin leakage of:
   $$\text{Leakage} = 12,000,000 \times 270 = \text{INR } 324\text{ Crores}$$
2. **Fuel Inefficiency:** Aging fleet (13.2 yrs) consumes $\text{INR } 0.27/\text{ASK}$ more than modern benchmark aircraft ($1.95 - 1.68$).
3. **Turnaround & Utilization Penalty:** Gate turnaround of 52 min (vs 28 min benchmark) reduces daily flight hours from 12.8 to 9.2 hrs, spreading fixed lease and crew overhead over fewer revenue flights.

### 5. Interviewer Pushback & Model Response
- **Interviewer:** *"If the CEO suggests discounting base fares further to 92% load factor to recover gross revenue, what is your recommendation?"*
- **Candidate Model Response:**
  *"I strongly advise against further base fare discounting. At an 88% load factor, seats are already near capacity. The operational bottleneck is unit margin, not volume. Marginal revenue from a discounted ticket ($\text{INR } 3,000$) fails to cover the combined unit fuel cost and airport handling cost ($\text{INR } 3,400$), accelerating cash burn. We must focus on unbundling ancillary services and streamlining gate turnaround to 35 minutes to unlock 2 additional daily sectors per aircraft."*

---

## Case 2: EV Two-Wheeler Swappable Battery Market Entry

### 1. The Interviewer Prompt
> *"A leading Indian energy conglomerate is evaluating entering the Electric Two-Wheeler (E2W) battery-swapping ecosystem in Top-10 metropolitan cities. They want an estimate of the total addressable market (TAM), optimal station deployment economics, and a go/no-go recommendation."*

### 2. Market Sizing & TAM Derivation (Bottom-Up Approach)

```
STEP 1: Target Commercial E2W Fleet in Top 10 Metros
- Population in Top 10 Indian Metros ≈ 100 Million
- Total 2-Wheelers in Metros ≈ 30 Million
- Commercial Delivery / Gig-Economy Share ≈ 10% = 3.0 Million vehicles
- EV Penetration in Commercial Segment (2026 Projection) ≈ 25% = 750,000 E2Ws

STEP 2: Daily Energy & Swapping Demand per E2W
- Average Daily Commercial Distance = 120 km/day
- Battery Range per Swap = 60 km
- Required Swaps per Day = 120 / 60 = 2.0 swaps/day
- Total Annual Swaps = 750,000 × 2 × 365 = 547.5 Million swaps/year

STEP 3: Total Addressable Market (TAM) Valuation
- Subscription / Swap Fee = INR 100 / swap (including electricity + battery amort.)
- TAM = 547.5M swaps × INR 100 = INR 5,475 Crores / Year
```

### 3. Swapping Station Unit Economics & Payback Matrix

```
EXHIBIT 2: Single Battery Swapping Station (BSS) Economics

CapEx per Station:
- Automated Swapping Kiosk (15-battery dock): INR 6,00,000
- Initial Battery Inventory (20 packs @ INR 30,000): INR 6,00,000
- Grid Transformer & Fast Chargers: INR 3,00,000
- Total Initial CapEx = INR 15,00,000

Monthly Operating Cash Flows:
- Swaps per Day = 60 swaps/day
- Monthly Revenue = 60 × INR 100 × 30 days = INR 1,80,000
- Electricity Cost (1.8 kWh/swap @ INR 8/kWh) = 60 × 1.8 × 8 × 30 = -INR 25,920
- Site Lease / Kirana Store Revenue Share = -INR 20,000
- Maintenance & Cloud Telematics = -INR 14,080
- Net Monthly Operating Cash Flow = INR 1,20,000

Simple Payback Period:
- Payback = CapEx / Annual OCF = 15,00,000 / (1,20,000 × 12) = 15,00,000 / 14,40,000 = 1.04 Years (12.5 Months)
```

### 4. Strategic Risks & Interviewer Pushback
- **Interviewer:** *"What is the single biggest threat that could render this CapEx investment obsolete within 3 years?"*
- **Candidate Model Response:**
  *"The primary strategic threat is lack of battery form-factor standardization across OEMs and rapid advancements in fast-charging solid-state chemistry. If major OEMs (Ola, Ather, TVS) standardize on proprietary 15-minute ultra-fast onboard charging, the standalone battery swapping model becomes redundant. We must secure long-term B2B anchor fleet contracts (e.g., Swiggy, Zomato, Zepto) with OEM-agnostic modular battery packs."*

---

## Case 3: Quick-Commerce Dark Store Unit Economics

### 1. The Interviewer Prompt
> *"A 10-minute grocery delivery platform operates 400 dark stores across India. The company reports an Average Order Value (AOV) of INR 450, but loses INR 35 per order at the dark-store level. The COO wants to know: Can this dark store ever achieve a positive contribution margin without raising delivery fees?"*

### 2. Unit Economics Decomposition per Order

```
EXHIBIT 3: Per-Order Financial Architecture (AOV = INR 450)

Line Item                        Current Model (INR)   Optimized Target (INR)   Strategic Lever
---------------------------------------------------------------------------------------------------
Gross Merchandise Value (AOV)          450.00                 550.00            Private Label / Multi-Packs
Cost of Goods Sold (COGS - 82%)       -369.00                -429.00            Direct Supplier Sourcing (78%)
Gross Profit Margin (18%)              +81.00                +121.00            +400 bps Margin Expansion
Delivery Fee Charged to User            +0.00                  +0.00            Maintain Zero-Friction Acquisition
Dark Store Picking & Packing           -18.00                 -12.00            WMS Automation & RFID Batching
Rider Payout (Last Mile)               -55.00                 -42.00            Batching 2 Orders per Trip
Dark Store Rent & Utilities (Fixed)    -28.00                 -21.00            Throughput (1,200 -> 1,600 orders/day)
Payment Gateway & Tech (3%)            -15.00                 -16.50            Flat Processing Rate
---------------------------------------------------------------------------------------------------
Contribution Margin per Order          -35.00                 +29.50            PROFITABLE (+5.4% Margin)
```

### 3. Interviewer Follow-Up & Sensitivity Testing
- **Interviewer:** *"What is the break-even order volume per dark store under current pricing?"*
- **Candidate Model Response:**
  - Current Dark Store Fixed Costs $= \text{INR } 1,00,800/\text{month}$ ($\text{Rent } 65\text{k} + \text{Electricity/Cooling } 25\text{k} + \text{Store Manager } 10.8\text{k}$).
  - Variable Contribution per Order (excl. fixed store rent) $= \text{Gross Profit (81)} - \text{Picking (18)} - \text{Rider (55)} - \text{Tech (15)} = -\text{INR } 7.00$.
  - *"Under current variable unit economics, the contribution margin is negative ($-\text{INR } 7/\text{order}$). Increasing store volume under negative contribution will only widen total cash losses. The platform must first increase Gross Margin to $\ge 22\%$ (via private label FMCG) and enforce 2-order rider batching before scaling store throughput."*

---

## 🎯 Master Case Execution Protocol (Consulting & Strategy)

1. **Listen & Structure (90 sec):** Clarify the business objective, verify industry context, and sketch a customized MECE issue tree.
2. **Formulate Hypotheses Early:** State your working hypothesis (e.g., *"I hypothesize this is a unit-cost inflation rather than a top-line volume issue"*).
3. **Drive the Analysis:** Calculate proactively from exhibits, state the strategic implication of every number, and lead the interviewer to the next logical branch.
4. **Synthesize with Actionable Recommendations:** Deliver a structured recommendation: Bottom-Line Verdict $\to$ 3 Strategic Pillars $\to$ Key Operational Risks & Mitigations.


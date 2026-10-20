# 03. Comprehensive Business Case Masterclass: The 14 Core Archetypes

> **Document Type**: Master Casebook & Case Interview Playbook
> **Audience**: Candidates preparing for McKinsey, BCG, Bain, Strategy&, Kearney, and Big 4 case rounds.
> **Standard**: Every archetype contains business context, clarifying dialogue, tailored issue trees, quantitative exhibit analysis, complete step-by-step calculations, root-cause diagnosis, recommendations, and executive synthesis.

---

## The 14 Essential Business Case Archetypes

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               14 CASE ARCHETYPES                                       │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ 1. Profitability Decline & Turnaround     │ 2. Revenue Growth & Geographic Market Entry│
│ 3. Market Sizing & Competitive Response   │ 4. New Product Launch & Commercialization  │
│ 5. Pricing Strategy & Price Elasticity    │ 6. Customer Acquisition, Conversion & Churn│
│ 7. Cost Reduction & Strategic Procurement │ 8. Manufacturing & Supply Chain Logistics  │
│ 9. Capacity & Bottleneck Optimization     │ 10. Digital Transformation Strategy        │
│ 11. AI / Analytics Business Value & ROI   │ 12. Customer Experience & Service Quality  │
│ 13. Mergers & Acquisitions (M&A) Diligence│ 14. Organizational Restructuring & Change  │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## Archetype 1: Profitability Decline & Operational Turnaround

### 1. Problem Archetype & Context
- **Core Meaning**: A business experiences falling absolute profits or contracting profit margins. The objective is to isolate whether the root cause stems from industry-wide factors or company-specific drivers, deconstruct revenue vs. cost, identify the operational flaw, and model financial recovery.
- **Success Metric**: Recover ₹80 Cr in annual EBITDA within 12 months.

### 2. Candidate-Interviewer Case Dialogue & Transcript
> **Interviewer**: *"Our client is Bharat Cement, the third-largest cement producer in South India with ₹4,000 Crore in annual revenue. Over the past 12 months, EBITDA collapsed from ₹720 Cr (18% margin) to ₹400 Cr (10% margin). The CEO has hired us to diagnose the issue and reverse the decline."*
>
> **Candidate**: *"Thank you. Let me clarify three points before structuring: First, has this 8-percentage-point margin contraction affected all South Indian cement producers, or is Bharat Cement uniquely affected? Second, what has happened to our sales volume in million tonnes (MT)? Third, are there any union or plant closure constraints?"*
>
> **Interviewer**: *"South Indian cement peers saw an average margin drop of 2% due to coal inflation. Our 8% drop is largely client-specific. Sales volume remained flat at 10 Million Tonnes (MT). There are no plant closure constraints, but we cannot violate labor agreements."*
>
> **Candidate**: *"Understood. Since volume is flat at 10 MT while EBITDA contracted by ₹320 Cr, the issue must be either: (A) Price realization per tonne declined, or (B) Operating cost per tonne increased. Let me structure this into an issue tree:"*

```text
Bharat Cement EBITDA Recovery (₹320 Cr Contraction)
├── 1. Revenue per Tonne (Price Realization)
│     ├── 1.1 Gross Realization: Trade (retail bags) vs. Non-Trade (bulk infrastructure) mix
│     └── 1.2 Discounting & Distributor Rebates
└── 2. Operating Cost per Tonne
      ├── 2.1 Power & Fuel Costs (Petcoke vs. Imported Coal heat rates in kilns)
      ├── 2.2 Inbound Raw Material Costs (Limestone mining royalty & fly-ash sourcing)
      ├── 2.3 Outbound Freight & Logistics (Road vs. Rail transport; Lead distance in km)
      └── 2.4 Plant Fixed Overheads & SG&A
```

> **Candidate**: *"Since power & fuel and outbound freight typically make up $>60\%$ of cement operating costs, my initial hypothesis is that either fuel procurement costs or freight distance expanded. Do we have per-tonne unit cost and price data for last year vs. this year?"*
>
> **Interviewer**: *(Hands Exhibit 1)* *"Here is the per-tonne breakdown:"*

### 3. Exhibit 1 Analysis & Quantitative Math
| Cost / Revenue Line Item | Prior Year (₹/Tonne) | Current Year (₹/Tonne) | Variance (₹/Tonne) | Total Impact on 10 MT |
| :--- | :---: | :---: | :---: | :---: |
| **Gross Realization (Price)** | ₹4,000 | ₹3,950 | -₹50 | -₹50 Cr |
| **Power & Fuel** | ₹1,050 | ₹1,120 | +₹70 | +₹70 Cr cost |
| **Raw Materials (Limestone/Slag)**| ₹650 | ₹660 | +₹10 | +₹10 Cr cost |
| **Outbound Freight & Logistics** | ₹850 | ₹1,060 | **+₹210** | **+₹210 Cr cost** |
| **Plant Fixed & SG&A** | ₹730 | ₹760 | +₹30 | +₹30 Cr cost |
| **Total Operating Cost / Tonne** | **₹3,280** | **₹3,600** | **+₹320** | **+₹320 Cr cost** |
| **EBITDA / Tonne** | **₹720 (18%)** | **₹400 (10%)** | **-₹320** | **-₹320 Cr** |

> **Candidate**: *"Looking at Exhibit 1, outbound freight accounts for ₹210 of the ₹320/tonne margin collapse—representing nearly 66% of the total problem. Power and fuel added ₹70/tonne (partially industry-wide). Freight cost per tonne jumped by nearly 25% from ₹850 to ₹1,060.*  
> *Freight cost per tonne is governed by: $\text{Freight Cost/T} = \text{Freight Mode Rate (Rail vs Road)} \times \text{Average Lead Distance (km)}$.*  
> *Did diesel transport rates increase, or did our average dispatch lead distance increase?"*
>
> **Interviewer**: *"Diesel rates rose 5%. However, 18 months ago, the sales team chased a volume target by expanding dispatches into Maharashtra and North Karnataka, increasing average lead distance from 220 km to 380 km. Furthermore, 90% was shipped via expensive road trucks because rail siding was congested."*

### 4. Root Cause & Financial Turnaround Modeling
1. **Unprofitable Geographic Expansion**: Selling 2.5 MT into distant markets (380 km) where freight is ₹1,350/T, wiping out product contribution margin.
2. **Sub-optimal Modal Mix**: 90% road transport (₹3.2/T-km) vs. rail (₹1.8/T-km).

**Recovery Actions**:
- **Action A: Rationalize Lead Distance**: Pull back 1.5 MT from distant fringe markets into core Andhra/Tamil Nadu markets within 200 km radius. Freight savings: ₹180/T on 1.5 MT = **₹27 Cr**.
- **Action B: Rail Siding Debottlenecking**: Invest ₹15 Cr in rail siding automation to shift rail share from 10% to 35%. Freight savings: $(3.2 - 1.8) \times 220\text{ km} \times 2.5\text{ MT} \times 0.25$ = **₹77 Cr**.
- **Action C: Alternative Fuel (AFR) Kiln Co-processing**: Substitute 10% imported coal with biomass waste fuels, saving ₹40/T on power & fuel across 10 MT = **₹40 Cr**.
- **Total EBITDA Recovery**: $27 + 77 + 40 = \mathbf{₹144\text{ Cr}}$ (recovering 45% of lost EBITDA in Year 1).

### 5. Executive Synthesis (Pyramid Principle)
> *"Bharat Cement should execute a logistics rationalization and rail debottlenecking program to recover ₹144 Crore in annual EBITDA within 12 months. Our analysis reveals that 66% of the margin contraction was caused by an undisciplined geographic sales expansion that inflated lead distance from 220 km to 380 km. We recommend three immediate actions: first, pull back 1.5 MT of unprofitable fringe volumes to core markets within 200 km; second, expand rail siding throughput to shift 25% of modal share to rail; and third, co-process biomass in kilns to offset coal inflation. The primary execution risk is resistance from northern distributors, which we mitigate by reallocating regional sales quotas to high-margin infrastructure corridors in Tamil Nadu."*

---

## Archetype 2: Revenue Growth & Geographic Market Entry

### 1. Problem Archetype & Context
- **Core Meaning**: Evaluating whether, where, and how an organization should enter a new geographic region or customer segment. Requires sizing addressable demand, evaluating competitive barriers, choosing entry mode (organic, acquisition, partnership), and projecting investment payback.
- **Success Metric**: Achieve ₹200 Cr revenue with breakeven in 24 months.

### 2. Candidate-Interviewer Transcript
> **Interviewer**: *"An established German premium coffee-machine manufacturer ($€500M$ global revenue) wants to enter the Indian market. The machines retail at ₹40,000 to ₹1,20,000. Should they enter, and what market entry model should they adopt?"*
>
> **Candidate**: *"Let us evaluate three core dimensions: First, what is the Addressable Market Size (TAM/SAM/SOM) in India for premium coffee machines? Second, what is the competitive landscape and customer distribution channel? Third, what entry mode (wholly-owned subsidiary, exclusive distributor, or joint venture) delivers the required financial return?"*

```text
German Coffee Machine India Entry
├── 1. Market Attractiveness & Size
│     ├── 1.1 B2C High-Net-Worth Households (TAM)
│     └── 1.2 B2B Commercial Demand (HORECA - Hotels, Restaurants, Tech Cafeterias)
├── 2. Product-Market Fit & Adaptation
│     ├── 2.1 Voltage & Water Hardness (Hard Indian water scales boilers rapidly)
│     └── 2.2 Milk-based Coffee Preference (90% Indians drink cappuccinos/lattes, not black espresso)
├── 3. Competitive Landscape & Positioning
│     ├── 3.1 Incumbent Brands (De'Longhi, Nespresso, Philips)
│     └── 3.2 Pricing & Import Tariffs (Customs duty on luxury electronics is ~28%)
└── 4. Go-To-Market & Entry Mode
      ├── 4.1 Exclusive Master Importer / Franchisee (Low capex, fast launch)
      └── 4.2 Direct Subsidiary with Flagship Experience Centers (High capex, brand control)
```

### 3. Quantitative Market Sizing & Economics
1. **B2C Segment Sizing**:
   - India has 350M households. Top 2% income tier = 7M affluent households.
   - Coffee drinkers: 30% = 2.1M households.
   - Willingness to spend $\ge ₹40,000$ on coffee machine: 5% = 105,000 installed base.
   - Annual replacement / new sales (7-year machine lifespan): $rac{105,000}{7} = 15,000	ext{ units/year}$.
   - Average Selling Price (ASP) = ₹50,000 $\implies$ **B2C Market** = $15,000 \times 50,000 = \mathbf{₹75\text{ Cr/year}}$.
2. **B2B Segment Sizing (HORECA + Tech Offices)**:
   - 5,000 5-star/4-star hotel rooms & boutique cafes + 15,000 corporate offices = 20,000 potential machines.
   - Annual replacement / expansion rate = 15% = 3,000 machines/year.
   - Commercial ASP = ₹1,50,000 $\implies$ **B2B Market** = $3,000 \times 1,50,000 = \mathbf{₹45\text{ Cr/year}}$.
   - **Total Annual Addressable Market (SAM)** = $75 + 45 = \mathbf{₹120\text{ Cr/year}}$.
3. **Target Capture (SOM)**: Capturing 25% share in Year 3 yields **₹30 Cr/year**.

### 4. Strategic Recommendation
- **Entry Mode**: Enter via **B2B Commercial first (HORECA + Tech Cafeterias)** using an exclusive B2B distributor (e.g., partnering with Blue Tokai or major hospitality supplier). 
- **Rationale**: B2C market of ₹75 Cr is too small to justify expensive direct flagship retail stores given 28% customs duties. B2B contracts generate recurring bean/servicing revenues with high gross margins (60%).

---

## Archetype 3: Market Sizing & Competitive Response

### 1. Context & Business Prompt
> **Interviewer**: *"A dominant private Indian airline (55% domestic market share) discovers that a well-capitalized new rival (backed by a major conglomerate) has announced launch plans with 50 new aircraft, focusing on trunk metro routes with 20% lower introductory fares. How should our client respond?"*

### 2. Issue Tree & Decision Architecture
```text
Competitive Defense Strategy
├── 1. Competitive Threat Assessment
│     ├── 1.1 Competitor Cost Advantage vs. Unsustainable Price War (Cash burn runway)
│     ├── 1.2 Route Overlap (Delhi-Mumbai, Delhi-Bengaluru trunk routes vs. Regional Tier-2 routes)
│     └── 1.3 Slot & Gate Constraints at Metro Airports (Can they physically fly 50 planes immediately?)
├── 2. Defensive Response Options
│     ├── 2.1 Matching Price (Risk: Mutually Assured Destruction of industry yields)
│     ├── 2.2 Capacity Locking & Slot Dominance (Increasing frequency on high-density corridors)
│     ├── 2.3 Loyalty & Corporate Contract Ring-Fencing (Locking in corporate accounts with multi-year rebates)
│     └── 2.4 Unbundling & Ancillary Yield Management (Zero-baggage fares to compete with low headline prices)
└── 3. Financial & Margin Impact Simulation
      └── Model cash flow under Full Price War vs. Selective Slot Defense
```

### 3. Quantitative Exhibit & Payoff Matrix
| Response Strategy | Impact on Average Fare | Passenger Volume Retained | Year 1 EBITDA Impact | Strategic Viability |
| :--- | :---: | :---: | :---: | :--- |
| **A. Blanket Price Match (-20%)** | -20% across all routes | 98% retained | **-₹1,200 Cr** | **Unviable** (incinerates balance sheet cash) |
| **B. Ignore / Do Nothing** | 0% change | 78% (lose 22% volume) | **-₹850 Cr** | **Unacceptable** (loss of market leadership) |
| **C. Targeted Defense (Selective)**| -5% net via unbundled fares | 92% retained | **-₹280 Cr** | **Optimal** (preserves corporate yield, protects slots) |

### 4. Recommendation
Do NOT initiate an across-the-board fare match. Execute **Strategy C**:
1. Ring-fence corporate travelers (40% of revenues) by offering priority security, flexible flight changes, and corporate lounge vouchers.
2. Introduce a "Lite" unbundled fare on metro trunk routes to neutralize competitor headline advertising while protecting ancillary revenues (seat selection, meals).
3. Increase flight frequencies at peak morning/evening corporate departure slots at Mumbai and Delhi where slot availability is zero.

---

## Archetype 4: New Product Launch & Commercialization

### 1. Context & Problem Formulation
An established FMCG oral-care leader wants to launch an Ayurvedic Charcoal Whitening Toothpaste priced at ₹180 (a 100% premium over standard ₹90 paste). 

### 2. Key Questions & Funnel Framework
- **Target Customer**: Urban Tier-1 millennials and Gen-Z consumers seeking natural aesthetics.
- **Cannibalization Risk**: Will it cannibalize our existing ₹120 herbal toothpaste or win share from competitors?
- **Breakeven Volume**: Fixed launch marketing budget = ₹30 Cr. Gross margin on premium paste = 65% (₹117/tube).
  $$\text{Breakeven Volume} = \frac{\text{Fixed Marketing Cost}}{\text{Gross Margin per Tube}} = \frac{₹30,00,00,000}{₹117} = \mathbf{2,564,100\text{ tubes (2.56 Million tubes)}}$$

---

## Archetype 5: Pricing Strategy & Price Elasticity

### 1. Problem Archetype & Framework
Setting optimal prices for a new or existing offering using the 3 Classical Pricing Pillars:
1. **Cost-Plus Floor**: Unit Variable Cost + Minimum Return on Capital.
2. **Competitor Benchmark**: Existing alternative market prices adjusted for feature differences.
3. **Value-Based Ceiling**: Economic Value to Customer (EVC) = Reference Value + Value of Differentiation.

### 2. Quantitative EVC Calculation
A new enterprise SaaS warehouse software reduces order picking errors from 3.0% to 0.5% for an e-commerce firm processing 10 Million orders annually. Each error costs ₹200 to resolve.
- **Value Created per Year**:
  $$\Delta \text{Errors} = (3.0\% - 0.5\%) \times 10,000,000 = 2.5\% \times 10,000,000 = 250,000\text{ errors saved}$$
  $$\text{Annual Economic Savings} = 250,000 \times ₹200 = \mathbf{₹5.0\text{ Crore / year}}$$
- **Value Sharing Rule of Thumb**: Vendor captures 20% to 33% of economic value created.
- **Optimal Pricing**: $₹5.0\text{ Cr} \times 30\% = \mathbf{₹1.5\text{ Crore / year subscription license}}$.

---

## Archetype 6: Customer Acquisition, Conversion & Churn

### 1. Funnel Unit Economics & Formulas
$$\text{LTV} = \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Churn Rate}} = \frac{\text{Annual Gross Profit per User}}{\text{Annual Churn \%}}$$
$$\text{CAC Payback Period (Months)} = \frac{\text{CAC}}{\text{Monthly Gross Profit per User}}$$

### 2. Worked Problem
- ARPU = ₹600/month. Gross Margin = 70%. Monthly Churn = 3.5%. CAC = ₹4,200.
  1. Monthly Gross Profit = $600 \times 0.70 = ₹420/\text{month}$.
  2. Annual Churn = $3.5\% \times 12 = 42\%$ (approx) $\implies$ Lifespan = $\frac{1}{0.035} \approx 28.57\text{ months}$.
  3. $\text{LTV} = 420 \times 28.57 = \mathbf{₹12,000}$.
  4. $\text{LTV / CAC Ratio} = \frac{12,000}{4,200} = \mathbf{2.86\times}$ (Healthy benchmark is $\ge 3.0\times$).
  5. $\text{CAC Payback} = \frac{4,200}{420} = \mathbf{10\text{ months}}$.

---

## Archetype 7: Cost Reduction & Strategic Procurement

### 1. Framework: The Procurement Opportunity Tree
```text
Procurement Cost Reduction
├── 1. Commercial Levers (Price Paid)
│     ├── 1.1 Volume Aggregation across business units / plants
│     ├── 1.2 Vendor Consolidation & Tier-1 Competitive Reverse Auctions
│     └── 1.3 Index-linked Pricing & Hedging raw materials
└── 2. Technical / Demand Levers (Volume Consumed)
      ├── 2.1 Specification Harmonization (Standardizing bolt sizes / packaging thickness)
      ├── 2.2 Scrap & Wastage Reduction on plant floor
      └── 2.3 "Should-Cost" Clean-Sheet Modeling (Dissecting vendor cost structure)
```

---

## Archetype 8: Manufacturing & Supply Chain Logistics

### 1. Problem Archetype & Context
Diagnosing delays, inventory bloat, high logistics freight costs, and supply chain fragility.

### 2. Quantitative Worked Case: Working Capital & Safety Stock
An automotive Tier-1 supplier has 4 manufacturing plants and holds ₹200 Cr in inventory. Average Daily Usage = ₹2 Cr. Lead time from steel mills = 20 days with standard deviation of lead time $\sigma_{LT} = 4\text{ days}$.
- **Cycle Stock** = $\frac{\text{Lot Size}}{2}$.
- **Safety Stock** = $Z \times \sigma_{LT} \times \text{Daily Demand}$. For 95% service level ($Z = 1.645$):
  $$\text{Safety Stock} = 1.645 \times 4\text{ days} \times ₹2\text{ Cr/day} = \mathbf{₹13.16\text{ Cr}}$$.
- By shifting from weekly batch orders to milk-run daily deliveries with regional steel processors, lead time drops to 3 days ($\sigma = 1$), cutting safety stock to ₹3.29 Cr and unlocking **₹9.87 Cr in trapped cash**.

---

## Archetype 9: Capacity & Bottleneck Optimization

### 1. The Theory of Constraints (Goldratt Framework)
Every operating system has **exactly one primary bottleneck** that dictates the maximum throughput of the entire operation. Increasing the capacity of non-bottleneck steps wastes capital without producing a single additional unit of output.

### 2. Worked Industrial Bottleneck Case
A generic pharmaceutical manufacturing line has 4 sequential stages:
- Stage 1: Chemical Synthesis (Capacity = 1,200 kg/day)
- Stage 2: Wet Granulation & Drying (Capacity = 950 kg/day)
- Stage 3: Tablet Compression & Punching (Capacity = 800 kg/day) — **THE BOTTLENECK**
- Stage 4: Blister Packaging & Boxing (Capacity = 1,400 kg/day)

**Current Output** = $\min(1200, 950, 800, 1400) = \mathbf{800\text{ kg/day}}$.
- Plant manager proposes spending ₹8 Cr to upgrade Packaging (Stage 4) to 2,000 kg/day.
- **Consultant's Diagnosis**: Upgrading Stage 4 produces **zero incremental revenue** because Stage 3 can only feed 800 kg/day. Capital must be focused entirely on Stage 3 (adding an automated tablet punching press for ₹2.5 Cr to expand capacity from 800 to 1,000 kg/day). System throughput immediately increases to 950 kg/day (+18.75% output).

---

## Archetype 10: Digital Transformation Strategy

### 1. Framework: The Digital Value Equation
$$\text{Digital ROI} = \frac{\text{Annual Cost Savings (Labor + Error Reduction)} + \text{Incremental Revenue (Conversion)}}{\text{Implementation Capex} + \text{Ongoing Cloud/SaaS Licenses}}$$

### 2. Worked Digital Case: Bank Branch Paperless Onboarding
- Current physical account opening cost = ₹450 per customer (courier, scanning, physical KYC).
- New digital video-KYC pipeline cost = ₹60 per customer + ₹5 Cr initial software capex + ₹3 Cr/year cloud maintenance.
- Bank opens 2 Million accounts annually.
  - Annual Operating Cost Savings = $2,000,000 \times (₹450 - ₹60) = 2,000,000 \times ₹390 = \mathbf{₹78\text{ Crore / year}}$.
  - Net Year 1 Benefit = $78 - 5\text{ (Capex)} - 3\text{ (Opex)} = \mathbf{₹70\text{ Crore}}$.
  - Payback period = $\frac{5}{78 - 3} = \frac{5}{75} = \mathbf{0.067\text{ years (~24 days)}}$.

---

## Archetype 11: AI / Analytics Business Value & ROI

### 1. Problem Archetype & Pitfalls
Evaluating whether to invest in predictive AI / Machine Learning or Generative AI. 
- *The Trap*: Treating AI as an IT science experiment without tying it to an EBITDA P&L line item.
- *The Framework*: Focus on **Error Reduction Cost**, **Speed-to-Decision**, or **Labor FTE Productivity**.

### 2. Case: GenAI Customer Service Automation
- E-commerce firm operates 1,000 customer support agents costing ₹35,000/month each (Annual cost = ₹42 Cr).
- GenAI automated agent can resolve 60% of Tier-1 inquiries (where is my order, returns, refunds) without human intervention.
- Human headcount reduced by 50% (500 agents retained for complex Tier-2 escalations).
- Annual labor savings = $500 \times 35,000 \times 12 = \mathbf{₹21\text{ Crore}}$.
- AI infrastructure & token API cost = ₹3.5 Cr/year.
- **Net Annual P&L Improvement** = $21 - 3.5 = \mathbf{₹17.5\text{ Crore / year}}$.

---

## Archetype 12: Customer Experience & Service Quality

### 1. Framework: Net Promoter Score (NPS) Economics
$$\text{NPS} = \% \text{ Promoters (Score 9–10)} - \% \text{ Detractors (Score 0–6)}$$
Promoters have $3\times$ higher lifetime value, buy $50\%$ more frequently, and generate word-of-mouth referral savings. Detractors churn at $4\times$ higher rates and consume $70\%$ of customer support hours.

---

## Archetype 13: Mergers & Acquisitions (M&A) Due Diligence

### 1. Framework: Strategic M&A Screening Funnel
```text
Strategic M&A Due Diligence
├── 1. Strategic Fit & Rationale
│     ├── 1.1 Market Expansion (New geography / customer segment)
│     ├── 1.2 Capability Acquisition (Proprietary IP, technology stack, talent)
│     └── 1.3 Portfolio Synergies (Cross-selling opportunities)
├── 2. Standalone Target Health & Valuation
│     ├── 2.1 Quality of Earnings (Adjusted EBITDA, working capital cycle)
│     └── 2.2 Customer Concentration (Does top customer contribute >30%?)
├── 3. Synergy Quantification
│     ├── 3.1 Cost Synergies (SG&A consolidation, procurement scale) [High Confidence: 80% haircut]
│     └── 3.2 Revenue Synergies (Cross-selling, joint bundling) [Low Confidence: 30% haircut]
└── 4. Integration Feasibility & Culture
      ├── 4.1 Cultural & Management Retention
      └── 4.2 IT System / ERP Migration Complexity
```

---

## Archetype 14: Organizational Restructuring & Change Management

### 1. Framework: The Operating Model Redesign
- **Span of Control**: Increasing average managerial span from 1:4 to 1:8 eliminates redundant intermediate layers (delayering).
- **RACI Matrix**: Clarifies Responsible, Accountable, Consulted, and Informed stakeholders to eliminate decision paralysis.
- **Change Resistance Mitigation**: Early pilot programs, transparent communication, and tying CXO bonuses directly to transformation milestones.

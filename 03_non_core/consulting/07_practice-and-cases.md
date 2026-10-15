# 07. Management Consulting: Solved Case Practice Master Bank

> **Document Purpose**: Four comprehensive, multi-step management consulting cases covering Profitability Turnaround, Market Entry & Infrastructure CapEx, Unit Economics & Platform Turnaround, and Operations Capacity Optimization. Each case contains candidate briefs, clarifying dialogues, mathematical proofs, and executive recommendations.

---

## 1. Master Practice Case Index

| Case ID | Case Title | Industry | Core Archetype | Quantitative Depth |
| :---: | :--- | :--- | :--- | :--- |
| **Case 1** | **Cement Manufacturer Turnaround** | Heavy Building Materials | Regional Cost Turnaround | Lead distance logistics, fuel mix, EBITDA waterfall |
| **Case 2** | **EV Battery Swapping Infrastructure** | Clean Energy / Mobility | Market Entry & CapEx | TAM market sizing, station unit economics, payback |
| **Case 3** | **Quick Commerce Platform Economics** | E-Commerce / Retail | Platform Unit Economics | Dark store picking density, route batching, margin flip |
| **Case 4** | **Multi-Specialty Hospital Capacity** | Healthcare Services | Operations & Throughput | Bed turnover, Average Length of Stay (ALOS), mix shift |

---

## Case 1: Indian Cement Manufacturer Regional EBITDA Recovery

### Problem Statement & Candidate Brief
> *“Our client is a top-5 cement manufacturer in India generating ₹12,000 Crore in annual revenue across four regional clusters. Over the past 18 months, their consolidated EBITDA margin declined from 22% to 14%, while industry peers maintained a stable 20% margin. The CEO has commissioned our team to diagnose the root cause and deliver a 12-month EBITDA recovery plan.”*

### Step 1: Clarification & Scoping Dialogue
- **Candidate**: *“Has this margin contraction occurred uniformly across all regions, or is it isolated to specific geographic clusters?”*  
  **Interviewer**: *“The client operates nationwide, but our internal financial audit reveals that 80% of the margin contraction is concentrated in the South India regional cluster.”*
- **Candidate**: *“In the South cluster, did top-line realization collapse due to a regional price war, or are operational and logistics costs escalating?”*  
  **Interviewer**: *“Average realized price in the South slipped only 4% (from ₹320 to ₹307 per 50kg bag), but total delivered cost per bag escalated by 16% (from ₹250 to ₹290 per bag). Focus your analysis on the cost drivers.”*

### Step 2: Cost Breakdown & Root Cause Isolation

```text
Cost Per 50kg Cement Bag (South India Cluster): ₹250 → ₹290 (+₹40 / +16%)
├── Raw Materials (Clinker & Gypsum): ₹80 → ₹82 (+₹2)
├── Power & Fuel (Kiln Thermal Energy): ₹65 → ₹85 (+₹20 / +30.8%) ◄── Key Driver 1!
├── Freight & Outbound Logistics: ₹60 → ₹76 (+₹16 / +26.7%) ◄── Key Driver 2!
└── Plant Fixed Overheads & Depreciation: ₹45 → ₹47 (+₹2)
```

#### Interviewer Data Releases:
1. **Power & Fuel Spike**: Due to domestic rail rake shortages from Coal India mines, the South manufacturing plant substituted domestic linkage coal with imported petroleum coke (petcoke). Concurrently, global benchmark petcoke prices surged 35%.
2. **Logistics Escalation**: To chase top-line volume growth, regional sales managers aggressively onboarded dealer accounts outside their natural economic freight radius. The average lead distance from plant to distributor expanded from **180 km to 310 km**.

### Step 3: Step-by-Step Mathematical Impact Calculation
- Southern regional cluster production volume = **15 Million Metric Tons (MMT) per year**.
- In standard packaging: 1 Ton = 20 bags (50 kg each) $\rightarrow 15\text{M Tons} \times 20 = \mathbf{300\text{ Million bags / year}}$.

1. **Annual Fuel Cost Escalation**:
   $$\Delta \text{Fuel Cost} = 300\text{M bags} \times ₹20/\text{bag} = \mathbf{₹600\text{ Crore INR / year}}$$
2. **Annual Logistics Freight Escalation**:
   $$\Delta \text{Freight Cost} = 300\text{M bags} \times ₹16/\text{bag} = \mathbf{₹480\text{ Crore INR / year}}$$
3. **Total Annual EBITDA Contraction in South Cluster**:
   $$\text{Total Cost Drag} = ₹600\text{ Cr} + ₹480\text{ Cr} = \mathbf{₹1,080\text{ Crore INR / year}}$$

### Step 4: Executive Recommendation & Turnaround Roadmap
> *“We recommend a three-pillar operational restructuring to recover **₹800 Crore in annual EBITDA** over 12 months:*  
> 1. **Freight Route Rationalization (Recovers ₹320 Cr)**: Terminate 120 unprofitable peripheral dealer contracts beyond 250 km; establish rail-linked grinding terminals to bring average lead distance back under 200 km.  
> 2. **Alternative Fuel & Raw Materials (AFR) Substitution (Recovers ₹300 Cr)**: Increase thermal substitution rate (TSR) to 15% using industrial hazardous waste, municipal refuse-derived fuel (RDF), and agricultural biomass, reducing dependence on imported petcoke.  
> 3. **Dynamic Regional Net-Realization Slabs (Recovers ₹180 Cr)**: Overhaul distributor rebate schemes to incentivize full truckload (FTL) orders and tie dealer discounts directly to delivered margin rather than gross volume.  
> *Key Implementation Risks: Temporary volume loss during dealer pruning; biomass seasonal price volatility during monsoon.*”

---

## Case 2: EV Battery Swapping Infrastructure Market Entry

### Problem Statement & Candidate Brief
> *“Our client is a major Indian renewable energy conglomerate with strong balance sheet capital. They are evaluating entering the Electric Vehicle (EV) battery swapping infrastructure market for commercial two-wheelers (E2W) and three-wheelers (E3W). The CEO wants to know: What is the addressable market size, what are the station-level unit economics, and should we enter?”*

### Step 1: Market Sizing (TAM for Commercial EV Swapping in Top-10 Metros)
1. **Target Fleet**: Commercial two-wheelers (food delivery, e-commerce couriers) and commercial three-wheelers (cargo and auto-rickshaws).
   - Commercial 2W & 3W addressable fleet by 2028 across top 10 Indian metros $\approx \mathbf{4.0\text{ Million vehicles}}$.
2. **Usage & Swapping Frequency**:
   - A commercial delivery driver covers ~120 km/day. Average battery range per swap = ~60 km.
   - Frequency = **2 battery swaps per day**.
   - Operating days = **300 days / year**.
   - Annual swaps per vehicle = $2 \times 300 = \mathbf{600\text{ swaps / vehicle / year}}$.
3. **Pricing Benchmark**:
   - Contractual swap fee = **₹90 per swap** (competitive with petrol operating cost of ₹2.2/km).
   - Annual revenue per vehicle = $600 \times ₹90 = \mathbf{₹54,000 / \text{vehicle / year}}$.
4. **Total Addressable Market (TAM)**:
   $$\text{TAM} = 4.0\text{ Million vehicles} \times ₹54,000/\text{year} = \mathbf{₹21,600\text{ Crore INR / year (\$2.6 Billion)}}$$

### Step 2: Station-Level Unit Economics & Payback Period (Bottom-Up)

#### Initial Capital Expenditure (CapEx per Kiosk):
- Automated 15-bay swapping cabinet: ₹4.5 Lakhs.
- 15 Lithium Iron Phosphate (LFP) 2kWh battery packs: $15 \times ₹40,000 = ₹6.0\text{ Lakhs}$.
- Grid transformer, metering, and civil setup: ₹1.5 Lakhs.
- **Total CapEx per Station** = **₹12.0 Lakhs**.

#### Operational Parameters & Daily Throughput:
- Battery capacity: 15 packs. Charge time from 0% to 100% = 2.0 hours.
- Maximum theoretical swaps per 24-hour cycle = $\frac{24}{2} \times 15 = 180\text{ swaps/day}$.
- Realistic operating utilization (target steady state) = 50% = **90 swaps / day**.

#### Annual Financials per Station:
1. **Annual Revenue**:
   $$\text{Revenue} = 90\text{ swaps/day} \times ₹90/\text{swap} \times 365\text{ days} = \mathbf{₹29.56\text{ Lakhs / year}}$$
2. **Annual Operating Expenses (OpEx)**:
   - **Electricity Cost**: 2 kWh per swap $\times 90\text{ swaps} \times ₹8/\text{kWh commercial tariff} \times 365\text{ days} = \mathbf{₹5.26\text{ Lakhs}}$.
   - **Battery Amortization / Reserve**: Batteries degrade over 1,500 full cycles. Battery replacement reserve fund $\approx \mathbf{₹6.50\text{ Lakhs/year}}$.
   - **Real Estate Lease (Footprint at Petrol Station / Metro Hub)**: ₹30,000/month = $\mathbf{₹3.60\text{ Lakhs/year}}$.
   - **Maintenance, IoT Telemetry & Insurance**: $\mathbf{₹2.00\text{ Lakhs/year}}$.
   - **Total Annual OpEx** = $5.26 + 6.50 + 3.60 + 2.00 = \mathbf{₹17.36\text{ Lakhs / year}}$.
3. **Station EBITDA & Payback**:
   $$\text{Annual Station EBITDA} = ₹29.56\text{ Lakhs} - ₹17.36\text{ Lakhs} = \mathbf{₹12.20\text{ Lakhs / year}}$$
   $$\text{Simple Payback Period} = \frac{\text{CapEx}}{\text{Annual EBITDA}} = \frac{₹12.00\text{ Lakhs}}{₹12.20\text{ Lakhs}} \approx \mathbf{0.98\text{ years (12 Months)}}$$

### Step 3: Strategic Recommendation & Entry Execution
- **Decision**: **Enter the market via a B2B anchor-tenant model**.
- **Execution Blueprint**:
  1. **Anchor Demand**: Secure multi-year fleet contracts with Swiggy, Zomato, and Amazon delivery partners before deploying kiosks, guaranteeing baseline 40% utilization from Day 1.
  2. **Real Estate Synergies**: Partner with state oil marketing companies (IOCL / HPCL) to lease existing forecourt land, avoiding standalone retail zoning permits.
  3. **Battery Standardization Risk**: Build multi-form-factor battery trays to support multiple vehicle OEMs and prevent lock-in to a single scooter manufacturer.

---

## Case 3: Quick Commerce Grocery Platform Unit Economics Turnaround

### Problem Statement & Candidate Brief
> *“A venture-backed quick commerce grocery platform operates 250 micro-fulfillment centers ('dark stores') across Tier-1 Indian cities. While gross merchandise value (GMV) grew 80% year-on-year, the company is burning ₹12 Crore per month. The Board requires each dark store to reach operational contribution break-even within 6 months.”*

### Step 1: Baseline Dark Store Unit Economics (Current State)
- Average dark store metrics: **1,000 orders per day**.
- Average Order Value (AOV) = **₹320**.
- Product Gross Margin = 18% of AOV = **₹57.60**.
- Delivery / Convenience Fee Collected = **₹15.00**.
- **Total Revenue Inflow per Order** = $57.60 + 15.00 = \mathbf{₹72.60}$.

#### Cost Structure per Order:
- Dark store picking & packing staff (in-store labor): **₹25.00**.
- Last-mile rider payout (per drop): **₹55.00**.
- Store Fixed Overheads (₹6.6 Lakhs monthly rent, electricity, deep-freezers across 30,000 orders/month): **₹22.00**.
- Payment gateway & packaging bag: **₹5.00**.
- **Total Operating Cost per Order** = $25 + 55 + 22 + 5 = \mathbf{₹107.00}$.

#### Current Economic Deficit:
$$\text{Net Contribution per Order} = ₹72.60 - ₹107.00 = \mathbf{-₹34.40 \text{ (Loss per order)}}$$
$$\text{Annual Loss per Dark Store} = 1,000\text{ orders/day} \times (-₹34.40) \times 365 = \mathbf{-₹1.25\text{ Crore / store / year}}$$

### Step 2: Diagnostic Levers & Turnaround Math

```text
                                [Contribution Margin Turnaround]
                                                │
        ┌───────────────────────────────────────┴───────────────────────────────────────┐
        ▼                                                                               ▼
[AOV & Margin Expansion]                                                [Cost Density & Batching]
• Increase AOV: ₹320 → ₹450                                             • Route batching: 1.0 → 1.4 orders/trip
• Margin expansion: 18% → 22%                                           • Rider cost per order: ₹55 → ₹39
• Private label penetration & FMCG ads                                  • Dark store picker throughput
```

#### Step-by-Step Mathematical Bridge:
1. **AOV Expansion (₹320 $\rightarrow$ ₹450)**:
   - Introduce minimum order threshold of ₹199 for free delivery; deploy algorithmic cart upsells (beverages, snacks).
   - Higher AOV expands absolute gross profit: ₹450 at 22% margin (supported by private-label staples) = **₹99.00 gross profit per order** (+$41.40 gain).
2. **FMCG Brand Advertising Monetization**:
   - Charge consumer brands for sponsored search placement and sample distribution: Contributes **+₹8.00 per order**.
3. **Route Batching & Rider Density**:
   - Increase order density within a tight 2.0 km radius: Riders deliver 1.4 orders per trip instead of single orders.
   - Effective rider cost per order drops from ₹55.00 to $\frac{₹55}{1.4} = \mathbf{₹39.30}$ (saves ₹15.70).
4. **Dark Store Picking Optimization**:
   - Re-organize dark store layout by fast-moving SKU velocity: Picking time reduced from 180 seconds to 90 seconds, improving labor efficiency from ₹25.00 to **₹18.00 per order** (saves ₹7.00).

### Step 3: Revised Post-Turnaround Unit Economics

| Metric / Cost Element | Baseline State | Post-Turnaround Target | Variance per Order |
| :--- | :---: | :---: | :---: |
| **Average Order Value (AOV)** | ₹320.00 | **₹450.00** | +₹130.00 |
| **Product Gross Margin (22%)** | ₹57.60 | **₹99.00** | +₹41.40 |
| **Customer Delivery Fee** | ₹15.00 | **₹15.00** | — |
| **Retail Media Ad Revenue** | ₹0.00 | **₹8.00** | +₹8.00 |
| **Total Revenue per Order** | **₹72.60** | **₹122.00** | **+₹49.40** |
| Last-Mile Delivery Cost | -₹55.00 | -₹39.30 | +₹15.70 |
| Store Picking & Labor | -₹25.00 | -₹18.00 | +₹7.00 |
| Store Rent & Utilities (Fixed) | -₹22.00 | -₹22.00 | — |
| Packaging & Gateway | -₹5.00 | -₹6.00 | -₹1.00 |
| **Net Contribution per Order** | **-₹34.40** | **+₹36.70** | **+₹71.10 (Positive)** |

### Step 4: Executive Recommendation
- **Annual Financial Impact across 250 Stores**:
  $$\text{Net Annual EBITDA Swing} = 250\text{ stores} \times 1,000\text{ orders/day} \times 365\text{ days} \times (+₹71.10) \approx \mathbf{+₹648\text{ Crore INR}}$$
- The platform shifts from a monthly burn of ₹12 Crore to generating positive operational cash flow.

---

## Case 4: Private Multi-Specialty Hospital Capacity & Margin Turnaround

### Problem Statement & Candidate Brief
> *“A 400-bed private multi-specialty tertiary care hospital in Hyderabad saw EBITDA decline 18% over the past two years despite bed occupancy remaining high at 88%. The Managing Director has hired us to explain why high occupancy is producing lower profit and how to restore margins.”*

### Step 1: Clarification & Structural Decomposition
- **Candidate**: *“Has the payer mix changed (e.g., government insurance vs. self-pay), or has the clinical case mix shifted between medical admissions and surgical procedures?”*  
  **Interviewer**: *“Excellent inquiry. Payer mix is stable (70% private insurance, 30% self-pay). However, the clinical case mix has shifted significantly toward general medicine admissions, while cardiac and orthopedic surgeries have declined.”*

### Step 2: Clinical Throughput & Capacity Bottleneck Analysis

| Department / Case Type | Bed Allocation | Average Length of Stay (ALOS) | Daily Revenue per Bed | Contribution Margin % | Daily Contribution per Bed |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **General Internal Medicine** | 220 beds | **7.0 days** | ₹12,000 | 25% | **₹3,000 / day** |
| **Elective Surgeries (Cardio/Ortho)** | 180 beds | **3.5 days** | ₹45,000 | 45% | **₹20,250 / day** |

#### Key Operational Insights:
1. **Capacity Blockage**: General medicine patients generate only **₹3,000/day** in contribution margin, but tie up beds for an extended **7.0 days**.
2. **Surgical Queue Cancellations**: Surgeons report having to postpone or turn away 15 elective surgical patients weekly because step-down ICU and surgical ward beds are full of lingering general medicine patients.
3. **Discharge Delay Bottleneck**: Internal audit reveals that 35% of general medicine discharge delays are caused by delayed morning lab test approvals and insurance billing paperwork, keeping patients in beds 24–36 hours longer than clinically necessary.

### Step 3: Financial Sizing of Discharge Acceleration
If the hospital implements rapid clinical discharge protocols and reduces General Medicine ALOS from **7.0 days to 4.5 days**:
- General medicine bed capacity freed = $\frac{7.0 - 4.5}{7.0} = \mathbf{35.7\% \text{ bed capacity released}}$.
- This frees up: $220\text{ beds} \times 35.7\% \approx \mathbf{78\text{ available beds}}$.
- Re-allocate 40 of these freed beds to capture the lost 15 surgical patients per week:
  - 15 incremental surgical patients/week $\times 52\text{ weeks} = \mathbf{780\text{ surgical cases / year}}$.
  - Average revenue per surgical admission = $3.5\text{ days} \times ₹45,000 = \mathbf{₹157,500}$.
  - Contribution per surgery = $₹157,500 \times 45\% \approx \mathbf{₹70,875}$.
  - **Incremental Annual Contribution**:
    $$\text{Annual EBITDA Expansion} = 780\text{ cases} \times ₹70,875 \approx \mathbf{+₹5.53\text{ Crore INR}}$$

### Step 4: Executive Recommendation
1. **Institute 11:00 AM Discharge Protocol**: Streamline insurance billing and lab report sign-offs to complete discharges before noon, freeing beds for afternoon surgical admissions.
2. **Re-Designate 40 Beds as Dedicated Surgical Units**: Ring-fence surgical beds so general medicine patients cannot block high-margin surgical throughput.
3. **Align Physician Incentives**: Introduce performance incentives for surgical suite utilization and on-time starts.

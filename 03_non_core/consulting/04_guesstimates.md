# Block 3 — Guesstimates & Market Sizing Masterclass

> **Document Purpose**: Methodological foundations, classified baseline data bank, speed arithmetic, 5 fully worked realistic guesstimate models with sensitivity analysis, and an explicit mathematical audit table for consulting interviews.

---

## 1. Golden Rules of Guesstimates

1. **Structure > Exact Number**: Interviewers evaluate your logical decomposition, operational sanity, and arithmetic precision under pressure—not whether your number matches an unstated proprietary database.
2. **State and Justify Assumptions**: Never introduce an arbitrary number without a structural reason (e.g., *"I assume 4 people per household based on standard Census averages, with higher density in rural areas"*).
3. **Round Intelligently, Not Carelessly**: Round numbers to facilitate fast mental arithmetic (e.g., India population = 1.4 Billion), but preserve units rigorously (Lakhs, Crores, Millions, Billions).
4. **Distinguish Capacity from Throughput**: In bottom-up models, never confuse static physical capacity (e.g., seats, beds, runways) with transaction volume. Always factor in dwell time, turnover rate, and utilization limits.
5. **Sanity Check Against Macro Constraints**: At the conclusion, test your result against physical limits (hours in a day, road/runway capacity) and economic benchmarks (per capita GDP, market size benchmarks).

---

## 2. Standard Baseline Data Bank (India & Global)

Every quantitative assumption must be clearly classified so candidates never confuse an illustrative assumption with a verified statistical fact.

### Demographic & Household Benchmarks

| Parameter | Baseline Value | Classification | Context & Reference Source |
| :--- | :--- | :--- | :--- |
| **Total Population (India)** | **1.40 Billion (140 Crore)** | Sourced Factual Estimate | Census projections & UN World Population Prospects (2024–2026). |
| **Household Size (National)** | **4.0 persons / household** | Sourced Factual Estimate | NFHS-5 data (~4.4 rural, ~3.8 urban; 4.0 is standard interview consensus). |
| **Total Indian Households** | **~350 Million** | Sourced Factual Estimate | Calculated: 1,400M population / 4.0 persons per household. |
| **Urban / Rural Split** | **35% Urban (~500M) / 65% Rural (~900M)** | Sourced Factual Estimate | Census projection (~35% urban, rising towards 38% by 2030). |
| **Age Pyramid** | **0–14 yrs: 25% (~350M)**<br>**15–24 yrs: 18% (~250M)**<br>**25–59 yrs: 47% (~660M)**<br>**60+ yrs: 10% (~140M)** | Sourced Factual Estimate | Working-age population (15–59) constitutes ~65% (~910M total). |
| **Income Distribution** | **High (>₹15L/yr): 10%** (~35M HH)<br>**Middle (₹5L–15L/yr): 40%** (~140M HH)<br>**Low/Aspirant (<₹5L/yr): 50%** (~175M HH)| Illustrative Interview Baseline | NITI Aayog & PRICE household income brackets rounded for mental arithmetic. |

### Technology, Infrastructure & Consumption Benchmarks

| Parameter | Baseline Value | Classification | Context & Reference Source |
| :--- | :--- | :--- | :--- |
| **Active Smartphone Installed Base** | **~600M – 650M unique users** | Sourced Factual Estimate | TRAI telecom reports & Counterpoint Research (active devices vs. multi-SIMs). |
| **Average Replacement Cycle** | **3.5 – 4.0 years** | Sourced Industry Estimate | Extended replacement cycle driven by durable hardware and budget constraints. |
| **Annual Domestic Smartphone Shipments** | **145M – 155M units / year** | Sourced Factual Estimate | IDC India & Counterpoint Research annual shipment tracker (FY23–FY25). |
| **Internet & 4G/5G Subscribers** | **~850M – 900M broadband users** | Sourced Factual Estimate | TRAI monthly performance indicators. |
| **Delhi Airport (DEL) Total Movements** | **~1,400 – 1,450 Air Traffic Movements (ATMs)/day** | Sourced Factual Estimate | AAI (Airports Authority of India) annual movements (~500,000/year). |
| **DEL Total Daily Landings (Arrivals)** | **~700 – 725 landings / day** | Sourced Operational Reality | Total ATMs / 2 (airfield slot and departure/arrival balance). |
| **Per Capita Municipal Water Consumption** | **135 – 150 Liters / Capita / Day (LPCD)** | Sourced Factual Standard | Bureau of Indian Standards (IS 1172: 1993 standard for sewered cities). |
| **Kanpur Urban Population** | **~3.2 – 3.5 Million** | Sourced Demographic Estimate | Census of India urban agglomeration projections. |

---

## 3. Top-Down vs Bottom-Up Estimation Framework

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                GUESSTIMATE METHODOLOGY                                 │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ TOP-DOWN ESTIMATION (Demand-Side)         │ BOTTOM-UP ESTIMATION (Supply/Capacity-Side)│
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • Total Population (1,400M)               │ • Unit Asset: Single outlet, runway, car   │
│ • Filter: Age eligibility & Urban/Rural   │ • Operating parameters: Hours, slots, seats│
│ • Filter: Income qualification & Adoption │ • Throughput: Dwell time, turnover, batch  │
│ • Replacement rate + New adopters         │ • Multiply by active network footprint     │
│ • Best for: Market sizing, macro demand   │ • Best for: Store revenue, factory capacity│
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 4. Methodological Audit & Correction Table

Below is the line-by-line audit of defects identified in legacy consulting preparation materials, corrected with mathematically defensible models:

| Target Example | Legacy Defect / Inconsistency | Corrected Analytical Reasoning | Corrected Result | Interview Lesson |
| :--- | :--- | :--- | :--- | :--- |
| **A. Smartphone Market Sizing** | Calculated **253M units/year**, yet cited official shipment data of **150M–200M**, leaving an unaddressed 25%–70% contradiction. | Assumed 714M active base replaced every 3.0 years (238M) + 15M new. In reality, India's active installed base is ~620M, and average holding time has lengthened to ~3.8–4.0 years. | Replacement demand: $\frac{620\text{M}}{4.0} = 155\text{M}$.<br>First-time adopters: $10\text{M}$.<br>**Total Shipments: ~165M units/year** (aligns with IDC ~150M). | Never cite external benchmark numbers that contradict your own calculation without explaining the delta or updating your assumptions. |
| **B. Starbucks Outlet Revenue** | Assumed 50 seats generate 550 dine-in orders/day (11 turns/seat/day!), then multiplied by 1.3 for takeaway, yielding **₹3,21,750/day (~₹11.7 Cr/yr)**. | Customers at high-end cafes linger 60–90 minutes. 50 seats cannot produce 550 orders. Group size is ~1.5 people/order. Delivery must be added as a share of total, not an arbitrary $+30\%$ scalar. | Dine-in orders: ~200/day.<br>Takeaway & Delivery: ~130/day.<br>Total orders: **~330 orders/day**.<br>At ₹420 ABV: **₹1,38,600/day (~₹5.06 Cr/yr)**. | Distinguish people occupying seats from orders placed. Factor in dwell time and operational capacity constraints. |
| **C. Delhi Airport Landings** | Assumed all 4 runways operate at 30 landings/hr peak and 15 off-peak, calculating **1,980 landings/day** (implying ~4,000 total movements). | Runways handle both takeoffs and landings. Due to airspace crossover and wake turbulence separation, DEL total peak airfield movements are capped at ~75–84 ATMs/hr total across all runways. | Total daily movements: ~1,420 ATMs.<br>Landings (50%): **~710 landings/day**.<br>(1,980 landings would exceed the world's busiest airport by 40%). | Runways are not independent arrival pipelines; airports manage total movements (arrivals + departures) within strict airspace slot caps. |

---

## 5. Fully Worked Model 1: Annual Smartphone Sales in India (Top-Down)

### Candidate Brief & Problem Statement
*“Estimate the total number of new smartphones sold in India per calendar year.”*

### Step 1: Clarification & Scope
- **Metric**: Annual unit volume shipped/sold to end consumers in India.
- **Exclusions**: Refurbished/second-hand peer-to-peer sales; feature phones (non-smartphones).
- **Timeframe**: Normal calendar year (post-5G rollout baseline).

### Step 2: Structuring the Demand Tree

$$\text{Total Annual Sales} = \text{Replacement Purchases from Existing Installed Base} + \text{First-Time New Smartphone Adopters}$$

$$\text{Replacement Sales} = \frac{\text{Active Smartphone Installed Base}}{\text{Average Replacement Cycle (Years)}}$$

### Step 3: Assumption Table & Population Funnel

| Population Segment | Population Count | Smartphone Adoption % | Active Smartphone Users | Justification |
| :--- | :---: | :---: | :---: | :--- |
| **Children (0–14 yrs)** | 350 Million | 10% | 35 Million | Limited personal ownership; mostly parental device sharing. |
| **Working Adults (15–59 yrs)** | 910 Million | 60% | 546 Million | Blended urban (~85%) and rural (~45%) workforce adoption. |
| **Senior Citizens (60+ yrs)** | 140 Million | 30% | 42 Million | Skewed toward urban seniors; feature phones common in rural areas. |
| **Total Active Installed Base** | **1,400 Million** | — | **~623 Million** (Round to **620 Million**) | Matches TRAI & industry active user consensus (~600M–650M). |

### Step 4: Replacement Cycle & First-Time Buyers

1. **Replacement Cycle**:
   - High-income / Premium buyers (15% of base = ~90M): Replace every **2.5 years** $\rightarrow \frac{90\text{M}}{2.5} = 36\text{M units/year}$.
   - Mass-market / Budget buyers (85% of base = ~530M): Replace every **4.0 years** $\rightarrow \frac{530\text{M}}{4.0} = 132.5\text{M units/year}$.
   - Blended replacement demand = $36\text{M} + 132.5\text{M} \approx \mathbf{168.5\text{ Million units/year}}$ (or $\frac{620\text{M}}{3.7} \approx 167.5\text{M}$).
2. **First-Time New Buyers**:
   - Cohort turning 15 years old: $\sim 25\text{ Million youth/year}$. Smartphone adoption rate $\sim 40\% \rightarrow 10\text{ Million}$.
   - Rural feature-phone upgraders switching to entry-level 4G/5G: $\sim 5\text{ Million}$.
   - Total new adopters = **15 Million units/year**.
3. **Total Annual Sales**:
   $$\text{Total Annual Sales} = 168.5\text{M} + 15\text{M} = \mathbf{183.5\text{ Million units/year}}$$

### Step 5: Sensitivity Analysis & Sanity Check

| Replacement Cycle Assumption | Replacement Volume | First-Time Buyers | Total Annual Shipments | Real-World Plausibility |
| :--- | :---: | :---: | :---: | :--- |
| **Aggressive (3.0 yrs average)** | 207 Million | 15 Million | **222 Million** | Overestimates economic replacement capacity of rural consumers. |
| **Base Case (3.7 yrs blended)** | 168 Million | 15 Million | **183 Million** | Realistic upper-bound including inventory pipeline fill. |
| **Conservative / Extended (4.0 yrs)** | 155 Million | 12 Million | **167 Million** | Aligns tightly with IDC/Counterpoint reported sell-in of ~150M–160M. |

* **Reasonableness Check**: 167M units sold to 1,400M population means $\sim 12\%$ of India's population purchases a smartphone annually, or $\sim 27\%$ of the active user base upgrades every year. This is economically sound and structurally consistent.

---

## 6. Fully Worked Model 2: Daily Revenue of a Starbucks Outlet in Indiranagar, Bengaluru (Bottom-Up)

### Candidate Brief & Problem Statement
*“Estimate the daily revenue of a single busy Starbucks coffee shop in Indiranagar, Bengaluru.”*

### Step 1: Clarification & Operational Parameters
- **Location**: Prime high-street retail corridor in Indiranagar (high footfall, affluent professionals, tech founders, college students).
- **Operating Hours**: 8:00 AM – 11:00 PM (15 operational hours / day).
- **Physical Layout**: 50 indoor/outdoor seats across 20 tables (mix of 2-seaters, 4-seaters, and communal high tables).
- **Sales Channels**:
  1. Dine-In (sit-down consumption).
  2. Takeaway / Counter Pick-up (grab-and-go).
  3. Online Delivery (Zomato / Swiggy).

### Step 2: Operational Flow & Dwell Time Dynamics
A critical trap in cafe guesstimates is ignoring **dwell time**. Starbucks functions as a *“Third Place”*; customers do not vacate seats immediately after drinking their coffee.
- Morning rush (office-goers): Average dwell time = **30–45 minutes**.
- Afternoon & Evening (meetings, remote work): Average dwell time = **75–90 minutes**.
- **Party Size**: Average of **1.5 people per bill** (mix of solo laptop workers and pairs).

### Step 3: Hourly Customer Flow & Dine-In Order Breakdown

| Time Window | Duration | Seat Occupancy | Seated Persons | Avg Dwell Time | Table Turns / Hour | Seated Customers / Hour | Transactions / Hour (1.5 people/order) | Total Dine-In Orders |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Morning Peak** (8 AM – 11 AM) | 3 hrs | 70% | 35 | 45 mins | $1.33$ | 47 | 31 | $3 \times 31 = \mathbf{93}$ |
| **Afternoon Slump** (11 AM – 4 PM)| 5 hrs | 40% | 20 | 90 mins | $0.67$ | 13 | 9 | $5 \times 9 = \mathbf{45}$ |
| **Evening Peak** (4 PM – 9 PM) | 5 hrs | 90% | 45 | 75 mins | $0.80$ | 36 | 24 | $5 \times 24 = \mathbf{120}$ |
| **Night Wind-Down** (9 PM – 11 PM)| 2 hrs | 30% | 15 | 60 mins | $1.00$ | 15 | 10 | $2 \times 10 = \mathbf{20}$ |
| **Total Dine-In** | **15 hrs** | — | — | — | — | — | — | **278 orders / day** |

### Step 4: Add Takeaway & Delivery Channels
- **Counter Takeaway (Grab-and-Go)**:
  - Morning rush (office commute): High volume $\rightarrow 20\text{ orders/hr} \times 3\text{ hrs} = 60\text{ orders}$.
  - Other hours: $\sim 4\text{ orders/hr} \times 12\text{ hrs} = 48\text{ orders}$.
  - Total Takeaway = **108 orders / day**.
- **Delivery Orders (Swiggy/Zomato)**:
  - Average of 3 delivery orders per hour across 15 hours = **45 orders / day**.
- **Total Transactions per Day**:
  $$\text{Total Daily Orders} = 278\text{ (Dine-in)} + 108\text{ (Takeaway)} + 45\text{ (Delivery)} = \mathbf{431\text{ orders / day}}$$
  *(Rounding to **420 orders/day** to account for off-peak variance).*

### Step 5: Average Order Value (AOV / ABV) Breakdown
- Core Beverage: Coffee, tea, refresher = ₹340 list price.
- Food Attach Rate: 35% of orders include a food item (sandwich, muffin, croissant) at ₹220 average price $\rightarrow 0.35 \times 220 = ₹77$.
- Add-ons (milk substitutions, extra shots, syrups): ₹15 blended contribution.
- Taxes: Prices quoted GST inclusive for consumer checkout.
$$\text{Average Bill Value (ABV)} = 340 + 77 + 15 = \mathbf{₹432} \quad (\text{Use } \mathbf{₹430} \text{ for calculation})$$

### Step 6: Final Daily & Annual Revenue Calculation
$$\text{Daily Revenue} = 420\text{ orders/day} \times ₹430/\text{order} = \mathbf{₹1,80,600 / \text{day}} \quad (\approx \mathbf{₹1.80\text{ Lakhs / day}})$$

$$\text{Annualized Revenue} = ₹1.80\text{ Lakhs} \times 365\text{ days} \approx \mathbf{₹6.57\text{ Crore INR / year}}$$

### Step 7: Sanity Check Against Corporate Reality
- **Benchmark**: Tata Starbucks India financial disclosures indicate average annual revenue per store across their ~400 Indian stores is approximately **₹3.8 – ₹4.5 Crore INR**.
- **Location Context**: Indiranagar 100 Feet Road is among the top 5 highest-grossing Starbucks locations in Bengaluru alongside Kempegowda Airport and Brigade Road. Delivering **₹6.5 Crore** (~45% above national store average) is entirely consistent with a Tier-1 flagship's performance.
- **Capacity Ceiling**: 420 orders over 15 hours = 28 orders/hour = less than 1 transaction every 2 minutes at the POS terminal. Two barista espresso machines can easily handle 50 drinks/hour at peak. The operations are well within physical equipment capacity.

---

## 7. Fully Worked Model 3: Daily Flight Landings at Delhi Airport (Supply-Side Capacity)

### Candidate Brief & Problem Statement
*“Estimate the total number of commercial flight landings per day at Indira Gandhi International Airport (DEL), New Delhi.”*

### Step 1: Airport Airfield Constraints & Definitions
- **Air Traffic Movement (ATM)**: A single takeoff or landing.
- **Runway Configuration**: DEL operates **4 runways** (09/27, 10/28, 11/29 series).
- **Aviation Operating Principle**: Parallel and intersecting runways cannot operate at theoretical maximum single-runway throughput simultaneously due to:
  1. Wake turbulence separation standards (3–6 nautical miles between arriving aircraft).
  2. Converging / intersecting departure and arrival flight paths in New Delhi airspace.
  3. Shared ground taxiway congestion.
- In balanced commercial aviation operations:
  $$\text{Landings (Arrivals)} \approx \text{Takeoffs (Departures)} \approx 50\% \text{ of Total Air Traffic Movements (ATMs)}$$

### Step 2: Airfield Slot Throughput by Time Block

| Operating Period | Hours | Airfield Peak ATM Rate (Total Movements/Hour) | Total ATMs Generated | Arrival Share (%) | Landings (Arrivals) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Morning Peak** (6 AM – 10 AM) | 4 hrs | 80 movements / hr | $4 \times 80 = 320$ | 50% | 160 |
| **Midday Operations** (10 AM – 5 PM) | 7 hrs | 65 movements / hr | $7 \times 65 = 455$ | 50% | 228 |
| **Evening Peak** (5 PM – 10 PM) | 5 hrs | 85 movements / hr | $5 \times 85 = 425$ | 50% | 212 |
| **Night Window** (10 PM – 6 AM)<br>*(Cargo, long-haul international)* | 8 hrs | 30 movements / hr | $8 \times 30 = 240$ | 50% | 120 |
| **Total 24-Hour Cycle** | **24 hrs** | — | **1,440 Total ATMs / day** | — | **720 Landings / day** |

### Step 3: Calculation & Sanity Check
$$\text{Total Daily Commercial Landings} = \mathbf{720\text{ landings / day}}$$

- **Sanity Check Against Published AAI Statistics**:
  - Airports Authority of India (AAI) reports that DEL handled approximately **480,000 to 510,000 total ATMs in FY24**.
  - Daily actual ATMs = $\frac{500,000}{365} \approx \mathbf{1,370\text{ movements / day}}$.
  - Actual recorded daily landings = $\frac{1,370}{2} \approx \mathbf{685\text{ landings / day}}$.
  - Our estimated 720 landings is within **5%** of actual civil aviation authority operational statistics.

---

## 8. Fully Worked Model 4: Daily Municipal Water Demand for Kanpur City (Infrastructure Sizing)

### Candidate Brief & Problem Statement
*“Estimate the total daily treated municipal water requirement (in Million Liters per Day - MLD) for the city of Kanpur.”*

### Step 1: Framework (Civil / HWRE Infrastructure Method)

$$\text{Total Water Demand (MLD)} = \text{Domestic Demand} + \text{Commercial/Institutional Demand} + \text{Industrial Demand} + \text{Distribution Losses (NRW)}$$

### Step 2: Parametric Assumptions
1. **Population**: Kanpur Urban Agglomeration $\approx \mathbf{3.5\text{ Million residents}}$ (~35 Lakhs).
2. **Domestic Per Capita Benchmark (BIS IS 1172 Standard)**:
   - Indian standard for metropolitan cities with full sewerage = **135–150 Liters per Capita per Day (LPCD)**. Use **150 LPCD** as design basis.
3. **Commercial & Institutional**: Hospitals, universities (IIT Kanpur), railway stations, offices $\approx \mathbf{20\%}$ of domestic demand.
4. **Industrial Demand**: Kanpur has significant industrial clusters (tanneries, textiles, manufacturing) $\approx \mathbf{15\%}$ of domestic demand.
5. **Non-Revenue Water (NRW / Distribution Leakage)**: Aging municipal pipe networks in Indian cities lose $\approx \mathbf{20\%}$ of supplied water.

### Step 3: Step-by-Step Calculation

1. **Domestic Demand**:
   $$3.5\text{ Million people} \times 150\text{ Liters/person/day} = 525\text{ Million Liters/day} = \mathbf{525\text{ MLD}}$$
2. **Commercial & Institutional Demand**:
   $$20\% \times 525\text{ MLD} = \mathbf{105\text{ MLD}}$$
3. **Industrial Demand**:
   $$15\% \times 525\text{ MLD} \approx \mathbf{79\text{ MLD}}$$
4. **Subtotal Net Consumptive Demand**:
   $$525 + 105 + 79 = \mathbf{709\text{ MLD}}$$
5. **Gross Municipal Supply Needed (Factoring 20% Leakage)**:
   $$\text{Gross Production} = \frac{709\text{ MLD}}{1 - 0.20} = \frac{709}{0.80} \approx \mathbf{886\text{ MLD}} \quad (\text{or } 709 + 20\% \approx 850\text{ MLD})$$

### Step 4: Spoken Executive Summary
*“Kanpur city requires approximately **850 to 890 Million Liters per Day (MLD)** of treated water supply. Domestic consumption accounts for ~60% (525 MLD) based on standard 150 LPCD benchmarks across 3.5 million citizens. Commercial and industrial demand contribute ~185 MLD combined. Finally, accounting for ~20% physical pipe losses, municipal water treatment plants must treat roughly 880 MLD daily from Ganga river intakes and deep borewells.”*

---

## 9. Handling Interviewer Counter-Assumptions

When an interviewer challenges or replaces an assumption:

1. **Acknowledge and Pivot Immediately**: Never argue with an interviewer's constraint. Say: *"Understood. If we assume an 80 LPCD consumption instead of 150 LPCD, let me re-compute the domestic requirement..."*
2. **Isolate the Impacted Branch**: Identify whether the new input changes only one sub-branch or ripples through the entire model.
3. **Show Sensitivity Direction**: Before calculating, state the directional impact: *"Since per capita consumption dropped by nearly half, our total municipal requirement will contract from ~880 MLD to roughly ~510 MLD."*
4. **Re-evaluate the Final Sanity Check**: Comment on whether the new figure still makes operational sense under the revised premise.

---

## 10. Independent Practice Question Bank

Practice structuring, solving, and sanity checking these 4 diverse exercises:

1. **Annual Market Size of Electric Two-Wheelers (E2W) in India**:
   - Total two-wheelers sold annually: ~18 Million units.
   - EV penetration across scooters vs. motorcycles: Scrutinize subsidy impact and charging infrastructure.
2. **Number of Residential Elevators Operating in Mumbai**:
   - High-rise vs low-rise residential buildings; average floors; elevators per building core.
3. **Daily Revenue of an Express Highway Toll Plaza on the Delhi-Mumbai Expressway**:
   - Lane capacity, peak traffic flow per hour, passenger cars vs commercial trucks split, toll rates.
4. **Annual Consumption of Packaged Bottled Water in Indian Railway Stations**:
   - Train passengers per day, platform purchase conversion rate, seasonal temperature variation.

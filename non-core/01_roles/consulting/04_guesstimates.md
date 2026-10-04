# Block 3 — Guesstimates & Market Sizing Masterclass

> **Document Purpose**: Complete framework, assumption data bank, speed arithmetic, and 5 fully worked guesstimate examples for consulting interviews.

---

## 1. Golden Rules of Guesstimates

1. **Structure > Exact Number**: Interviewers care about your logical breakdown, assumptions, and math sanity check — not getting the exact real-world figure.
2. **State Assumptions Explicitly**: Always explain *why* you chose a specific percentage or demographic split.
3. **Use Round Numbers**: Round numbers to facilitate fast mental math (e.g., India population = 1.4 Billion).
4. **Sanity Check at the End**: Ask yourself: *"Does this final number make physical and economic sense?"*

---

## 2. Standard Baseline Data Bank (India & Global)

Memorize these baseline numbers for consulting interviews:

| Metric / Parameter | Value (India Baseline) | Global Baseline |
| :--- | :--- | :--- |
| **Total Population** | **1.4 Billion (140 Crore)** | World: 8.0 Billion |
| **Household Size** | Average **4.0 people / household** | Total Households in India: ~350 Million |
| **Urban / Rural Split** | **35% Urban** (~500M) / **65% Rural** (~900M) | — |
| **Age Demographics** | 0–14 yrs: 25% | 15–60 yrs: 65% | 60+ yrs: 10% |
| **Income Segments** | High Income: 10% | Middle Income: 40% | Low Income: 50% |
| **Smartphone Penetration**| ~65% of adult population (~600 Million users) | — |

---

## 3. Top-Down vs Bottom-Up Approaches

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GUESSTIMATE APPROACHES                               │
├────────────────────────────────────────┬────────────────────────────────────┤
│ TOP-DOWN ESTIMATION                    │ BOTTOM-UP ESTIMATION               │
├────────────────────────────────────────┼────────────────────────────────────┤
│ • Start with Total Population (1.4B)   │ • Start with Single Unit / Store   │
│ • Filter down by Urban %, Age %,       │ • Multiply by Operating Hours,     │
│   Income %, Adoption Rate %.           │   Slots, Locations, Days/Year.     │
│ • Best for: Market Size & Volume.      │ • Best for: Single Business Revenue│
└────────────────────────────────────────┴────────────────────────────────────┘
```

---

## 4. Fully Worked Example 1: Annual Market Size of Smartphones in India (Top-Down)

### Question: Estimate the total number of smartphones sold in India per year.

#### Step 1: Structure & Population Breakdown
Total Population of India = 1,400 Million (1.4B).

Filter out age groups that rarely buy new smartphones:
* Age 0–14 (25%): 350 Million → 10% smartphone ownership = 35 Million users.
* Age 15–60 (65%): 910 Million → 70% smartphone ownership = 637 Million users.
* Age 60+ (10%): 140 Million → 30% smartphone ownership = 42 Million users.
* **Total Smartphone User Base** = 35M + 637M + 42M ≈ **714 Million users**.

#### Step 2: Replacement Cycle Assumption
* Average replacement cycle of a smartphone in India = **3 years**.
* Annual replacement sales = 714 Million / 3 years = **238 Million units / year**.

#### Step 3: First-Time Buyers Addition
* New users entering the market per year (youth turning 15 + rural adoption) = **15 Million units / year**.

#### Step 4: Final Calculation & Sanity Check
$$\text{Total Annual Sales} = 238\text{M} + 15\text{M} = \mathbf{253\text{ Million units/year}}$$

* **Sanity Check**: 253M units out of 1,400M population means ~18% of Indians buy a phone each year. This matches realistic market shipment data (~150M–200M official shipments).

---

## 5. Fully Worked Example 2: Daily Revenue of a Starbucks Outlet in Indiranagar, Bengaluru (Bottom-Up)

### Question: Estimate the daily revenue of a single busy Starbucks coffee shop in Bengaluru.

#### Step 1: Structure & Operating Parameters
* Operating Hours: 8:00 AM – 11:00 PM (15 hours / day).
* Seating Capacity: 50 seats.
* Sales Channels: Dine-in / Takeaway (70%) + Delivery (30%).

#### Step 2: Peak vs Off-Peak Customer Flow Analysis

| Time Slot | Hours | Customer Volume / Hour | Seating Occupancy | Hourly Dine-In Orders |
| :--- | :---: | :---: | :---: | :---: |
| **Morning Peak** (8 AM - 11 AM) | 3 hrs | High | 80% (40 seats) | 40 orders/hr |
| **Afternoon Slump** (11 AM - 4 PM)| 5 hrs | Moderate | 40% (20 seats) | 20 orders/hr |
| **Evening Peak** (4 PM - 9 PM) | 5 hrs | Very High | 100% (50 seats) | 60 orders/hr (turnover >1x) |
| **Night Slump** (9 PM - 11 PM) | 2 hrs | Low | 30% (15 seats) | 15 orders/hr |

#### Step 3: Total Daily Dine-In Order Calculation
$$\text{Morning Orders} = 3 \times 40 = 120\text{ orders}$$
$$\text{Afternoon Orders} = 5 \times 20 = 100\text{ orders}$$
$$\text{Evening Orders} = 5 \times 60 = 300\text{ orders}$$
$$\text{Night Orders} = 2 \times 15 = 30\text{ orders}$$
$$\text{Total Dine-In Orders} = 120 + 100 + 300 + 30 = \mathbf{550\text{ orders/day}}$$

#### Step 4: Add Takeaway & Delivery (+30%)
$$\text{Total Orders/Day} = 550 \times 1.3 \approx \mathbf{715\text{ orders/day}}$$

#### Step 5: Average Bill Value (ABV) Assumption
* Average coffee/beverage price = ₹350.
* Food / snacks pairing (food item per 2 orders) = ₹150 average addition.
* **Average Bill Value (ABV)** = ₹450 per order.

#### Step 6: Final Revenue Calculation
$$\text{Daily Revenue} = 715 \text{ orders} \times ₹450/\text{order} = \mathbf{₹3,21,750/\text{day}}$$

---

## 6. Worked Example 3: Number of Flights Landing at Delhi Airport (DEL) per Day

### Question: Estimate the total daily landing operations at Indira Gandhi International Airport (DEL).

#### Step 1: Runway Capacity & Operating Hours
* DEL Airport has **4 active runways**.
* Operating Hours: 24 hours/day.
* Peak Hours (6 AM - 10 AM, 5 PM - 10 PM = 9 hours): 1 landing per 2 minutes per runway = 30 landings/hr/runway.
* Non-Peak Hours (15 hours): 1 landing per 4 minutes per runway = 15 landings/hr/runway.

#### Step 2: Calculation
$$\text{Peak Landings} = 9\text{ hrs} \times 30\text{ landings/hr/runway} \times 4\text{ runways} = 1,080\text{ landings}$$
$$\text{Non-Peak Landings} = 15\text{ hrs} \times 15\text{ landings/hr/runway} \times 4\text{ runways} = 900\text{ landings}$$
$$\text{Total Daily Landings} = 1,080 + 900 = \mathbf{1,980\text{ landings/day}}$$

---

## 7. Practice Guesstimates for Candidate Self-Test

1. **Estimate annual consumption of petrol in liters in Delhi.** (Filter by vehicle count: cars, 2-wheelers, taxis).
2. **Estimate the total number of elevator trips taken in Mumbai every day.** (Filter by high-rise residential vs commercial buildings).
3. **Estimate the monthly market size of online food delivery in Tier-1 Indian cities.**

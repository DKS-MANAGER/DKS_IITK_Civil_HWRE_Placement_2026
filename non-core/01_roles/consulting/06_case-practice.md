# Comprehensive Solved Case Library (Basic, Intermediate, Hard)

> **Document Focus**: Tiered practice case repository with detailed candidate walkthroughs, structures, data hints, and executive recommendations.

---

## Difficulty Classification Standard

* **Basic (Easy)**: Single issue driver (Revenue or Cost), linear MECE tree, 2–3 calculation steps.
* **Intermediate**: Multi-branch driver (Margin + Volume), trade-off analysis, channel shift or market entry decision.
* **Hard**: Multi-faceted digital transformation, legacy system constraints, complex unit economics, high ambiguity.

---

## 1. Easy Cases

### Case 1.1: Cement Manufacturer Freight Cost Reduction
* **Difficulty**: Easy
* **Client**: Major cement producer in North India.
* **Problem**: Overall logistics and freight expenses have increased by 18% per ton over the last 12 months.

#### Walkthrough & Solution:
1. **Clarifying Questions**: Has total cement volume produced changed? (No). Are diesel prices up? (Up by 5%).
2. **Issue Tree Structure**:
   * **Inbound Raw Material Transport**: Gypsum/Clinker freight.
   * **Outbound Finished Goods Transport**: Rail vs Road distribution split.
3. **Data Analysis**:
   * Rail transport cost = ₹1.2 / ton-km.
   * Road transport cost = ₹2.8 / ton-km.
   * Road transport share increased from 30% to 65% due to rail wagon allocation delays.
4. **Recommendation**:
   * Negotiate long-term rake contracts with Indian Railways for guaranteed wagon availability.
   * Implement route optimization software for remaining road fleets.
   * **Expected Savings**: 12% reduction in total freight cost.

---

## 2. Intermediate Cases

### Case 2.1: Tier-1 Bank Credit Card Churn Analysis
* **Difficulty**: Intermediate
* **Client**: Top 3 private sector bank in India.
* **Problem**: Credit card customer annual churn rate increased from 8% to 19% in urban metro cities.

#### Walkthrough & Solution:
1. **Issue Tree Structure (Customer Lifecycle)**:
   * **Onboarding Experience**: Application friction, credit limit satisfaction.
   * **Product Value Proposition**: Reward point value, annual fees, merchant partner discounts.
   * **Customer Service & Claims**: Dispute resolution speed, app UX.
2. **Data Findings**:
   * Competitor banks launched co-branded travel & dining cards offering 3x reward point redemption value.
   * Client's reward redemption process required desktop website logins, whereas competitors enabled 1-click mobile app redemptions.
3. **Recommendation**:
   * Upgrade Mobile Banking App to support 1-click instant reward redemption at checkout.
   * Partner with major dining/travel platforms (Zomato Gold, MakeMyTrip) for co-branded cards.
   * **Expected Impact**: Churn reduced back to <10% within 6 months.

---

## 3. Hard Cases

### Case 3.1: Global Airline Fleet Digital Modernization & Fuel Efficiency
* **Difficulty**: Hard
* **Client**: International commercial airline operating 120 aircraft.
* **Problem**: Fuel expenditure accounts for 40% of total operating expense. Fuel consumption per seat-kilometer is 14% higher than industry benchmarks.

#### Walkthrough & Solution:
```text
                         [Fuel Cost Reduction]
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
[Flight Path & Speed Optimization]               [Aircraft Weight & Payload]
         │                                                   │
  ┌──────┴──────┐                                     ┌──────┴──────┐
  ▼             ▼                                     ▼             ▼
[AI Routing] [Altitude Profile]                    [Cargo Load] [Auxiliary Fuel]
```

1. **Analytical Deep-Dive**:
   * Flight planning relies on static seasonal flight paths rather than real-time AI weather and jet stream routing data.
   * Pilots over-fuel aircraft by 8% as a safety buffer due to conservative static fuel prediction software.
2. **Technology Architecture (Cloud & Edge AI)**:
   * Implement real-time AI Flight Trajectory Optimization (Azure Cloud engine) streaming satellite wind profiles directly to flight deck iPads.
   * Deploy machine learning fuel prediction models taking into account exact aircraft weight, landing hold times, and temperature.
3. **Recommendation & ROI**:
   * Deploy AI Flight Planning software across long-haul routes.
   * Reduce excess safety fuel carryover by 60% without compromising safety margins.
   * **Financial Impact**: $42 Million annual fuel cost savings; 120,000 metric tons CO2 emission reduction.

---

## 4. Practice Case Matrix

| Case Title | Type | Key Skill Tested | Recommended Time |
| :--- | :--- | :--- | :---: |
| **Retail Grocery Margin Loss** | Basic Profitability | Cost tree breakdown | 15 Mins |
| **Solar Panel Manufacturer Entry** | Market Entry | CapEx & Payback period | 20 Mins |
| **Hospital Emergency Bed Capacity** | Operations Bottleneck | Queueing & Throughput | 20 Mins |
| **Fintech Loan Approval DX** | Digital Transformation | Process automation & Risk | 25 Mins |

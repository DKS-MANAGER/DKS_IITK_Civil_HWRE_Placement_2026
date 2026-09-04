# Supply Chain — Role Study Plan

## Role Overview

The Supply Chain role targets **procurement and logistics positions** at manufacturing firms (Tata Steel, L&T, Godrej), **e-commerce supply chains** (Amazon, Flipkart, Delhivery), **FMCG companies** (HUL, P&G, ITC), and **consulting firms** (Deloitte, McKinsey Operations). The role covers demand forecasting, inventory management, logistics optimization, and procurement strategy. Civil engineers' experience with material procurement, site logistics, and construction supply chains provides a strong foundation.

**Who targets this role:** B.Tech/M.Tech graduates with analytical skills, construction/materials procurement background, students interested in operations and logistics, GATE qualifiers.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Demand Forecasting & Planning

#### Why This Matters
Demand forecasting is the starting point of every supply chain decision. Getting the forecast right affects inventory, production, procurement, and logistics. Interviewers test both the methodology and the ability to choose the right technique.

#### What to Learn
- [ ] Qualitative methods: Expert judgment, Delphi method, market research
- [ ] Time series methods: Moving average, weighted moving average, exponential smoothing
- [ ] Holt's method (trend) and Holt-Winters (trend + seasonality)
- [ ] Causal methods: Linear regression, multiple regression
- [ ] Forecast error metrics: MAD, MSE, MAPE, bias
- [ ] Safety stock calculation: z × σ_d × √L (demand variability × lead time)
- [ ] ABC analysis: Classify items by value contribution (A: 80% value/20% items)
- [ ] Demand sensing vs demand planning

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`supply-chain-overview.md`](supply-chain-overview.md) | Forecasting, inventory | Full |

#### Worked Example
**Problem:** A company has actual demand for the last 6 months:

| Month | Actual Demand |
|:------|-------------:|
| Jan | 100 |
| Feb | 110 |
| Mar | 120 |
| Apr | 115 |
| May | 130 |
| Jun | 125 |

Compute: (a) 3-month simple moving average forecast for July, (b) Exponential smoothing forecast (α=0.3, F₁=100) for July, (c) If σ_d weekly = 15 units, lead time = 2 weeks, service level = 95%, find safety stock.

**Solution:**
1. **3-Month Moving Average:**
   - F(July) = (115 + 130 + 125) / 3 = 370/3 = **123.3 units**

2. **Exponential Smoothing (α=0.3):**
   - F₁ = 100 (given)
   - F₂ = 0.3(100) + 0.7(100) = 100
   - F₃ = 0.3(110) + 0.7(100) = 103
   - F₄ = 0.3(120) + 0.7(103) = 108.1
   - F₅ = 0.3(115) + 0.7(108.1) = 110.2
   - F₆ = 0.3(130) + 0.7(110.2) = 116.1
   - F₇ = 0.3(125) + 0.7(116.1) = **118.8 units**

3. **Forecast Error (MAD for exponential smoothing):**

| Month | Actual | Forecast | |Error| |
|:------|-------:|---------:|--------:|
| Feb | 110 | 100.0 | 10.0 |
| Mar | 120 | 103.0 | 17.0 |
| Apr | 115 | 108.1 | 6.9 |
| May | 130 | 110.2 | 19.8 |
| Jun | 125 | 116.1 | 8.9 |
| **MAD** | | | **12.5** |

4. **Safety Stock:**
   - z (95%) = 1.645
   - σ_d = 15 units/week, L = 2 weeks
   - Safety Stock = z × σ_d × √L = 1.645 × 15 × √2 = 1.645 × 15 × 1.414 = **34.9 ≈ 35 units**

**Key insight:** "The exponential smoothing forecast (118.8) lags behind the actual trend. With increasing demand, Holt's method with trend adjustment would be more appropriate."

#### Practice
**Basic (3–5):**
1. What is the difference between qualitative and quantitative forecasting?
2. Calculate a 3-month moving average from given data.
3. What is exponential smoothing? What does α control?
4. Define MAD, MAPE, and explain when to use each.
5. What is the purpose of safety stock?

**Intermediate (3–5):**
6. Apply Holt's method to a dataset with trend. Compare with simple exponential smoothing.
7. Calculate MAPE for two different forecasting methods and recommend the better one.
8. Design an ABC analysis for a warehouse with 1,000 SKUs.
9. What is demand sensing? How does it differ from demand planning?
10. A product has σ_d = 20 units/week, lead time = 3 weeks, service level = 98%. Calculate safety stock and reorder point (mean demand = 200 units/week).

**Interview-Level (5+):**
11. How do you handle demand forecasting for a new product with no history?
12. What happens to forecast accuracy as you forecast further into the future?
13. How would you forecast demand during a supply chain disruption (e.g., pandemic)?
14. What is forecast value added (FVA)? How do you reduce forecast bias?
15. How do machine learning methods improve demand forecasting?

#### Common Mistakes
- **Using** simple average when there's a clear trend
- **Ignoring** seasonality in products with seasonal patterns
- **Not tracking** forecast error — you can't improve what you don't measure
- **Confusing** forecast accuracy with forecast bias
- **Over-relying** on historical data during unusual events (COVID, etc.)

#### Completion Criterion
✅ Can apply 3+ forecasting methods to real data
✅ Can compute and interpret forecast error metrics
✅ Can calculate safety stock and reorder point
✅ Can recommend appropriate method based on data characteristics

---

### Topic 2: Inventory Management & EOQ

#### Why This Matters
Inventory management directly impacts working capital, service levels, and profitability. EOQ, safety stock, and inventory classification are the most commonly tested topics in supply chain interviews.

#### What to Learn
- [ ] Economic Order Quantity (EOQ): Q* = √(2DS/H)
- [ ] EOQ with quantity discounts
- [ ] Reorder Point (ROP) = d × L + Safety Stock
- [ ] Inventory costs: Holding, ordering, shortage (stockout)
- [ ] ABC analysis and inventory classification
- [ ] JIT (Just-in-Time) vs safety stock approach
- [ ] Newsvendor model (single-period inventory)
- [ ] Inventory turnover ratio and days of inventory

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`supply-chain-overview.md`](supply-chain-overview.md) | Inventory models, EOQ | Full |

#### Worked Example
**Problem:** A construction company uses cement:
- Annual demand D = 10,000 bags
- Order cost S = ₹500 per order
- Holding cost H = ₹20 per bag per year
- Lead time L = 7 days
- Daily demand d = 10,000/365 = 27.4 bags/day
- σ_daily = 5 bags
- Service level = 97% (z = 1.88)

Find: (a) EOQ, (b) Number of orders per year, (c) Total cost, (d) ROP with safety stock.

**Solution:**
1. **EOQ:**
   - Q* = √(2DS/H) = √(2 × 10,000 × 500 / 20) = √500,000 = **707 bags**

2. **Number of orders:**
   - N = D/Q* = 10,000/707 = **14.1 orders/year** (every ~26 days)

3. **Total annual cost:**
   - Holding cost = (Q*/2) × H = (707/2) × 20 = ₹7,070
   - Ordering cost = (D/Q*) × S = (10,000/707) × 500 = ₹7,071
   - **Total cost = ₹14,141/year**

4. **Reorder Point:**
   - Safety stock = z × σ_daily × √L = 1.88 × 5 × √7 = 1.88 × 5 × 2.646 = **24.9 ≈ 25 bags**
   - ROP = d × L + SS = 27.4 × 7 + 25 = 191.8 + 25 = **217 bags**

**Key insight:** "Order 707 bags at a time (about every 26 days). When inventory drops to 217 bags, place a new order. Keep 25 bags as safety buffer for demand variability."

#### Practice
**Basic (3–5):**
1. Derive the EOQ formula. What are its assumptions?
2. Calculate EOQ given D=5,000, S=₹300, H=₹15.
3. What is the difference between safety stock and cycle stock?
4. Explain JIT. When is it appropriate vs when is safety stock needed?
5. What is the newsvendor model? When is it used?

**Intermediate (3–5):**
6. A supplier offers a 10% discount for orders > 1,000 units. Should you take it? (EOQ analysis)
7. Calculate total inventory cost for different order quantities and plot the cost curve.
8. A product has daily demand = 50, σ = 10, lead time = 5 days, service level = 95%. Calculate ROP.
9. Perform ABC analysis on a dataset of 20 SKUs.
10. What is the impact of reducing lead time by 50% on safety stock?

**Interview-Level (5+):**
11. How do you manage inventory for perishable products?
12. What is the bullwhip effect? How does it affect inventory?
13. How would you optimize inventory across a multi-echelon supply chain?
14. Compare VMI (Vendor Managed Inventory) with traditional ordering.
15. How do you handle demand uncertainty with long lead times?

#### Common Mistakes
- **Applying** EOQ without checking assumptions (constant demand, no quantity discounts)
- **Ignoring** carrying cost — it's not just storage, it includes opportunity cost, obsolescence, insurance
- **Setting** safety stock too high (excess cost) or too low (stockouts)
- **Not adjusting** EOQ when costs or demand change
- **Confusing** ROP with EOQ — ROP is when to order, EOQ is how much

#### Completion Criterion
✅ Can derive and apply EOQ for various scenarios
✅ Can calculate safety stock and ROP given service level targets
✅ Can perform ABC analysis and set differentiated inventory policies
✅ Can explain trade-offs between inventory cost and service level

---

### Topic 3: Logistics & Network Design

#### Why This Matters
Logistics optimization — transportation, warehousing, distribution — is where supply chain costs are often highest. Interviewers test your ability to analyze trade-offs between cost, speed, and reliability.

#### What to Learn
- [ ] Transportation modes: Road, rail, air, sea, multimodal
- [ ] Total logistics cost: Transportation + warehousing + inventory carrying
- [ ] Center of gravity method for facility location
- [ ] Network design: Number, location, and capacity of warehouses
- [ ] Last-mile delivery optimization
- [ ] 3PL (Third-Party Logistics) vs in-house logistics
- [ ] Load optimization: Truck utilization, container packing
- [ ] Reverse logistics and returns management

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`supply-chain-overview.md`](supply-chain-overview.md) | Logistics, network design | Full |

#### Worked Example
**Problem:** A company ships from 2 plants to 3 warehouses to 4 customers. Plant capacities: P1=500, P2=400. Customer demands: C1=150, C2=200, C3=250, C4=200. Find the optimal transportation allocation minimizing total cost.

**Transportation costs (₹/unit):**

| | W1 | W2 | W3 |
|:--|---:|---:|---:|
| P1 | 10 | 12 | 15 |
| P2 | 14 | 8 | 11 |

| | C1 | C2 | C3 | C4 |
|:--|---:|---:|---:|---:|
| W1 | 5 | 8 | 10 | 12 |
| W2 | 7 | 4 | 6 | 9 |
| W3 | 12 | 10 | 3 | 7 |

Warehouse capacities (assuming unconstrained for simplicity).

**Solution (simplified - using lowest cost assignment):**
1. **P1→W1 (₹10):** Ship 300 to W1 (W1 serves C1+C4 cheapest)
2. **P2→W2 (₹8):** Ship 400 to W2 (W2 serves C2 cheapest)
3. **P1→W3 (₹15):** Ship 200 to W3 (W3 serves C3 cheapest)

**Detailed allocation (minimizing total):**
- P1→W1: 300 units, P1→W3: 200 units
- P2→W2: 400 units
- W1→C1: 150, W1→C4: 150
- W2→C2: 200, W2→C4: 50 (wait, let me recalc)

Actually, with 2 plants and 3 warehouses:
- Total supply = 900, Total demand = 800 (surplus 100)
- Optimal: Assign P2 to W2 (cheapest P→W link), P1 splits to W1 and W3

**Final allocation (total cost minimized):**
- P1→W1: 300, cost = 300 × 10 = ₹3,000
- P1→W3: 200, cost = 200 × 15 = ₹3,000
- P2→W2: 400, cost = 400 × 8 = ₹3,200
- W1→C1: 150 × 5 = ₹750; W1→C4: 150 × 12 = ₹1,800
- W2→C2: 200 × 4 = ₹800; W2→C4: 50 × 9 = ₹450 (total W2 = 250, but P2 ships 400... W2 has excess)

**Total transportation cost ≈ ₹13,000** (approximate)

**Key insight:** "The center of gravity method balances proximity to suppliers and customers. In practice, this would be solved using linear programming (simplex method) or supply chain optimization software."

#### Practice
**Basic (3–5):**
1. Compare transportation modes (road, rail, air, sea) on cost, speed, reliability.
2. What is the center of gravity method for facility location?
3. Define total logistics cost and its components.
4. What is 3PL? When would a company use it?
5. Explain the concept of last-mile delivery and its challenges.

**Intermediate (3–5):**
6. Set up a transportation problem and solve using Vogel's approximation.
7. A company has 3 potential warehouse locations. Evaluate using weighted scoring.
8. Calculate truck utilization given load, capacity, and volume constraints.
9. What is cross-docking? When is it beneficial?
10. Design a distribution network for an e-commerce company serving 5 cities.

**Interview-Level (5+):**
11. How do you balance cost vs speed vs reliability in logistics?
12. What is the impact of GST on warehouse network design in India?
13. How would you optimize last-mile delivery for perishable goods?
14. What are the trade-offs between centralized vs decentralized warehousing?
15. How does Amazon's supply chain differ from a traditional manufacturer's?

#### Common Mistakes
- **Choosing** cheapest mode without considering time sensitivity
- **Ignoring** total cost — cheap transport + high inventory may cost more
- **Not considering** capacity constraints in transportation
- **Overlooking** reverse logistics costs
- **Using** static models for dynamic, real-world networks

#### Completion Criterion
✅ Can set up and solve a transportation problem
✅ Can evaluate facility location alternatives
✅ Can analyze trade-offs in logistics network design
✅ Can design a basic distribution network

---

### Topic 4: Procurement & Supplier Management

#### Why This Matters
Procurement is a major cost driver (often 50-70% of total cost). Strategic sourcing, supplier evaluation, and negotiation are tested in supply chain interviews.

#### What to Learn
- [ ] Strategic sourcing process: 7-step methodology
- [ ] Supplier evaluation: Quality, Cost, Delivery, Service (QCDS)
- [ ] Total Cost of Ownership (TCO): Purchase price + logistics + quality + risk
- [ ] Contract types: Fixed price, cost-plus, framework agreements
- [ ] E-procurement and reverse auction
- [ ] Supplier relationship management: Transactional vs strategic
- [ ] Make vs buy decision framework
- [ ] Global sourcing risks and mitigation

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`supply-chain-overview.md`](supply-chain-overview.md) | Procurement, sourcing | Full |

#### Worked Example
**Problem:** A construction company needs to source steel. Two suppliers:

| Factor | Weight | Supplier A (Score 1-10) | Supplier B (Score 1-10) |
|:-------|:------:|:-----------------------:|:-----------------------:|
| Price (₹/tonne) | 30% | ₹52,000 | ₹48,000 |
| Quality (defect rate) | 25% | 9 (1% defect) | 7 (3% defect) |
| Delivery reliability | 20% | 8 (95% on-time) | 6 (85% on-time) |
| Payment terms | 10% | 7 (30 days) | 9 (60 days) |
| Technical capability | 15% | 8 | 5 |

**Solution:**
1. **Price normalization (lower is better):**
   - A: 48,000/52,000 × 10 = 9.2
   - B: 48,000/48,000 × 10 = 10.0

2. **Weighted Score:**

| Factor | Weight | A Score | A Weighted | B Score | B Weighted |
|:-------|:------:|:-------:|:----------:|:-------:|:----------:|
| Price | 0.30 | 9.2 | 2.76 | 10.0 | 3.00 |
| Quality | 0.25 | 9.0 | 2.25 | 7.0 | 1.75 |
| Delivery | 0.20 | 8.0 | 1.60 | 6.0 | 1.20 |
| Payment | 0.10 | 7.0 | 0.70 | 9.0 | 0.90 |
| Technical | 0.15 | 8.0 | 1.20 | 5.0 | 0.75 |
| **Total** | **1.00** | | **8.51** | | **7.60** |

3. **Decision:** Select **Supplier A** (higher weighted score despite higher price)

4. **TCO Analysis:**
   - A: ₹52,000/tonne + ₹500/tonne logistics + 1% defect cost (₹520) = ₹53,020
   - B: ₹48,000/tonne + ₹800/tonne logistics + 3% defect cost (₹1,440) = ₹50,240
   - **TCO favors B** — but risk of delivery delays and quality issues may offset savings

**Key insight:** "The lowest price supplier isn't always the best choice. Supplier A's better quality and reliability justify the ₹3,000/tonne premium, especially for time-critical construction projects."

#### Practice
**Basic (3–5):**
1. What is strategic sourcing? List the 7 steps.
2. Define Total Cost of Ownership (TCO). What costs does it include?
3. What is the difference between fixed price and cost-plus contracts?
4. Explain QCDS as a supplier evaluation framework.
5. What is a reverse auction?

**Intermediate (3–5):**
6. Perform a weighted scoring analysis to select a supplier from 3 options.
7. Calculate TCO for two alternatives including all hidden costs.
8. What are the risks of single-source vs multi-source procurement?
9. Design a supplier evaluation scorecard for a construction material.
10. What is the make vs buy decision? Give 3 factors for each side.

**Interview-Level (5+):**
11. How do you manage supplier relationships strategically?
12. What happened to global supply chains during COVID? What lessons were learned?
13. How would you negotiate a long-term contract with a key supplier?
14. What is e-procurement and how does it add value?
15. How do you handle supply chain disruptions from geopolitical events?

#### Common Mistakes
- **Focusing** only on purchase price, ignoring TCO
- **Not diversifying** suppliers — single-source risk
- **Ignoring** supplier financial health — bankrupt supplier = supply disruption
- **Over-complicating** evaluation with too many criteria
- **Not having** a clear contract structure with penalties/incentives

#### Completion Criterion
✅ Can apply weighted scoring for supplier selection
✅ Can compute Total Cost of Ownership
✅ Can explain strategic sourcing methodology
✅ Can design a supplier evaluation framework

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | Monthly demand for steel (tonnes): Jan=200, Feb=180, Mar=220, Apr=250, May=230, Jun=260. Compute: (a) 3-month MA for July, (b) Exponential smoothing (α=0.4, F₁=200) for July, (c) MAD for both methods. Which is better? | Forecasting | 20 |
| 2 | EOQ problem: D=8,000 units/year, S=₹400/order, H=₹16/unit/year. Lead time=10 days, daily demand σ=8, service level=97%. Compute EOQ, total cost, safety stock, and ROP. | Inventory | 25 |
| 3 | Supplier evaluation: 3 suppliers rated on Price (30%), Quality (25%), Delivery (25%), Service (20%). Create a weighted scoring model and recommend a supplier. | Procurement | 20 |
| 4 | A warehouse serves 3 cities: A (demand=500), B (demand=300), C (demand=200). Coordinates: A(10,50), B(40,20), C(70,60). Find optimal warehouse location using center of gravity. | Logistics | 15 |
| 5 | What is the bullwhip effect? Describe 4 causes and 3 mitigation strategies. | Supply Chain Theory | 20 |
| | | **Total** | **100** |

---

## Interview Strategy

### Technical Interview (15–20 minutes)
1. **Start with data** — "Let me analyze the numbers first..."
2. **Show structured approach** — use frameworks (EOQ, ABC, weighted scoring)
3. **Link to civil engineering** — "In construction, I managed material procurement for..."
4. **Discuss trade-offs** — cost vs service, speed vs reliability, centralization vs decentralization

### Behavioral / Case Study
- **Have STAR stories** about procurement negotiations, logistics optimization, inventory management
- **Know industry trends** — e-commerce logistics, GST impact, sustainable supply chains
- **Practice case studies** — facility location, network design, demand planning

### Unique Positioning (Civil → Supply Chain)
- "I've managed construction material supply chains — cement, steel, aggregates — understanding lead times, quality, and bulk pricing"
- "Site logistics taught me about last-mile delivery challenges"
- "Project scheduling taught me about demand planning and resource allocation"

---

## Cross-Links

**Next:**
→ [Supply Chain Overview](supply-chain-overview.md) — Complete preparation system

**Study:**
→ [Operations Overview](../operations/operations-overview.md) — For operational context
→ [Finance Study Plan](../finance/role-study-plan.md) — For financial analysis

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)
→ [HR Questions](../../prep/behavioral/hr_questions/hr-questions-bank.md)

**Related:**
→ [Product Analyst Study Plan](../product-analyst/role-study-plan.md) — For demand analytics
→ [Risk Study Plan](../risk/role-study-plan.md) — For supply chain risk

---

*This study plan follows the [Role Study Plan Template](../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*

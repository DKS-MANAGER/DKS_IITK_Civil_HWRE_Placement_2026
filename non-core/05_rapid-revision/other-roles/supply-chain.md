# Supply Chain — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core formulas, frameworks, and quick-fire Q&A for supply chain interviews.

---

## Framework 1: Demand Forecasting

### Forecasting Methods Comparison

| Method | Best For | Formula / Approach |
|:-------|:---------|:-------------------|
| **Simple Moving Average** | Stable demand, no trend | F(t+1) = (D₁ + D₂ + ... + Dₙ) / n |
| **Weighted Moving Average** | Recent data more important | F(t+1) = Σ(wᵢ × Dᵢ), Σw = 1 |
| **Exponential Smoothing** | Smooth data, quick update | F(t+1) = αD(t) + (1-α)F(t) |
| **Holt's Method** | Data with trend | F(t+1) = L(t) + T(t) |
| **Holt-Winters** | Trend + seasonality | Level + Trend × Seasonal factor |

### Exponential Smoothing

```
F(t+1) = α × Actual(t) + (1-α) × Forecast(t)
```

- α = 0.1-0.3: Smooth, slow to respond
- α = 0.7-0.9: Responsive, tracks changes quickly
- F₁ = D₁ or average of first few periods

### Forecast Error Metrics

| Metric | Formula | Use |
|:-------|:--------|:----|
| **MAD** | Σ|Actual - Forecast| / n | Average error magnitude |
| **MSE** | Σ(Actual - Forecast)² / n | Penalizes large errors |
| **MAPE** | (Σ|Error|/Actual) / n × 100 | % error, good for comparison |
| **Bias** | Σ(Actual - Forecast) / n | Direction of error (over/under) |

### Safety Stock Formula

```
Safety Stock = z × σ_d × √L
```

| Service Level | z-score |
|:------------:|:-------:|
| 90% | 1.282 |
| 95% | 1.645 |
| 97% | 1.881 |
| 99% | 2.326 |

Where: σ_d = standard deviation of demand, L = lead time

### Reorder Point

```
ROP = d̄ × L + SS = (Average daily demand × Lead time) + Safety Stock
```

---

## Framework 2: Inventory Management

### Economic Order Quantity (EOQ)

```
EOQ (Q*) = √(2DS / H)
```

Where:
- D = Annual demand (units)
- S = Ordering cost per order (₹)
- H = Holding cost per unit per year (₹)

### EOQ with Quantity Discount

```
For each discount level:
1. Calculate EOQ at discounted price
2. If EOQ is feasible (within discount range), compute total cost
3. If EOQ is not feasible, use minimum quantity for that discount
4. Compare total costs across all levels
```

### Total Inventory Cost (at EOQ)

```
Total Cost = (Q/2)×H + (D/Q)×S + D×C
           = Holding + Ordering + Purchase
```

At EOQ: Holding cost = Ordering cost

### Inventory Cost Components

| Cost | Description | Proportional To |
|:-----|:-----------|:----------------|
| **Ordering** | Placing, receiving, processing | Number of orders |
| **Holding/Carrying** | Storage, capital, insurance, obsolescence | Average inventory level |
| **Shortage/Stockout** | Lost sales, backorder cost, customer goodwill | Units short |

### ABC Analysis

| Class | % of Items | % of Value | Management |
|:------|:---------:|:---------:|:-----------|
| **A** | 10-20% | 70-80% | Tight control, frequent review |
| **B** | 20-30% | 15-20% | Moderate control |
| **C** | 50-70% | 5-10% | Simple control, bulk ordering |

### Newsvendor Model (Single Period)

```
Critical Ratio = Cu / (Cu + Co)
```

Where:
- Cu = Cost of underage (lost profit from not having item)
- Co = Cost of overage (cost of having unsold item)
- Order quantity = Q where P(Demand ≤ Q) = Critical Ratio

---

## Framework 3: Logistics & Transportation

### Transportation Mode Comparison

| Mode | Cost | Speed | Reliability | Best For |
|:-----|:----:|:-----:|:-----------:|:---------|
| Road | Medium | Medium | Medium | Last-mile, flexible routes |
| Rail | Low | Slow | High | Bulk, long-distance |
| Air | High | Fast | High | Urgent, high-value, low-volume |
| Sea | Lowest | Slowest | Medium | International, bulk |

### Total Logistics Cost

```
Total = Transportation + Warehousing + Inventory Carrying + Order Processing
```

### Center of Gravity Method (Facility Location)

```
X* = Σ(dᵢ × xᵢ) / Σdᵢ
Y* = Σ(dᵢ × yᵢ) / Σdᵢ
```

Where dᵢ = demand or volume at location i, (xᵢ, yᵢ) = coordinates

### Key Logistics Metrics

| Metric | Formula | Target |
|:-------|:--------|:-------|
| Truck utilization | Actual load / Truck capacity × 100 | >85% |
| On-time delivery | Orders delivered on time / Total orders | >95% |
| Cost per unit shipped | Total logistics cost / Units shipped | Lower is better |
| Warehouse utilization | Space used / Total space × 100 | 80-90% |

---

## Framework 4: Procurement & Supplier Management

### Strategic Sourcing (7-Step Process)

```
1. Profile category / spend analysis
2. Supply market analysis
3. Sourcing strategy development
4. Supplier pre-qualification
5. Negotiation / auction
6. Supplier selection
7. Integration / continuous improvement
```

### Weighted Scoring Model

```
Score = Σ (Weightᵢ × Ratingᵢ) for each supplier
Select supplier with highest total score
```

### Total Cost of Ownership (TCO)

```
TCO = Purchase Price + Logistics + Quality Costs + Risk Costs + Administrative Costs
     + (Transaction Costs) + (Opportunity Costs)
```

### Supplier Evaluation: QCDS Framework

| Dimension | What to Measure |
|:----------|:---------------|
| **Quality** | Defect rate, certifications, rejection rate |
| **Cost** | Unit price, payment terms, volume discounts |
| **Delivery** | On-time %, lead time flexibility |
| **Service** | Responsiveness, technical support, warranty |

### Make vs Buy Decision

| Factor | Make (In-house) | Buy (Outsource) |
|:-------|:---------------|:----------------|
| Core competency | Yes → Make | No → Buy |
| Volume | High volume → Make | Low volume → Buy |
| Quality control | Critical → Make | Standard → Buy |
| IP protection | Sensitive → Make | Generic → Buy |
| Capacity | Available → Make | Constrained → Buy |

---

## 10 Quick-Fire Interview Answers

**Q1: What is the bullwhip effect?**
A: It's the phenomenon where demand variability increases as you move upstream in the supply chain (retailer → distributor → manufacturer → supplier). Causes: order batching, demand signal updating, price fluctuations, rationing. Mitigation: information sharing, VMI, EDLP, smaller order quantities.

**Q2: What is EOQ and what are its assumptions?**
A: EOQ is the order quantity that minimizes total inventory cost (holding + ordering). Formula: √(2DS/H). Assumptions: constant demand, known lead time, no quantity discounts, instantaneous replenishment, constant costs.

**Q3: How do you reduce inventory without affecting service levels?**
A: Reduce lead time (faster replenishment), improve forecast accuracy (less safety stock needed), implement VMI, use postponement, ABC classification with differentiated policies, and share demand data with suppliers.

**Q4: What is the difference between push and pull supply chains?**
A: Push: produce based on forecast (make-to-stock). Pull: produce based on actual demand (make-to-order). Most companies use hybrid: push for base demand, pull for customization. Zara = pull; Coca-Cola = push.

**Q5: What is Total Cost of Ownership?**
A: TCO includes ALL costs of procurement, not just purchase price: logistics, quality/warranty, inventory carrying, administrative, risk, and disposal costs. A cheaper supplier may have higher TCO due to poor quality or unreliable delivery.

**Q6: How does your civil engineering background help in supply chain?**
A: Construction material procurement (cement, steel, aggregates) taught me about bulk ordering, lead time management, and quality verification. Site logistics taught me about transportation and last-mile delivery. Project scheduling taught me about demand planning.

**Q7: What is JIT (Just-in-Time)?**
A: An inventory strategy where materials arrive exactly when needed, minimizing inventory. Originated at Toyota. Requires: reliable suppliers, short lead times, stable demand. Not suitable for: uncertain demand, long lead times, or supplier unreliability.

**Q8: What is demand sensing vs demand planning?**
A: Demand sensing uses short-term signals (POS data, weather, events) to predict demand in the next 1-4 weeks. Demand planning uses historical data and statistical methods for longer horizons (months/quarters). Together they form a comprehensive forecasting system.

**Q9: How do you handle a supply chain disruption?**
A: Immediate: activate contingency suppliers, adjust production, communicate with customers. Short-term: expedite shipments, shift to alternative logistics. Long-term: diversify supplier base, build safety stock for critical items, nearshoring, risk assessment updates.

**Q10: What is the difference between 3PL and 4PL?**
A: 3PL (Third-Party Logistics) handles specific logistics functions: warehousing, transportation. 4PL (Fourth-Party Logistics) manages the entire supply chain — integrates multiple 3PLs, provides strategic oversight, and manages technology. 4PL is more strategic; 3PL is more tactical.

---

## Last-Minute Checklist

### Before Any Supply Chain Interview
- [ ] EOQ formula: Q* = √(2DS/H)
- [ ] Safety Stock formula: z × σ_d × √L
- [ ] ROP = d̄ × L + SS
- [ ] Forecast error metrics: MAD, MAPE
- [ ] Bullwhip effect: causes and mitigation
- [ ] TCO components

### Must-Know Formulas
- [ ] EOQ = √(2DS/H)
- [ ] SS = z × σ_d × √L
- [ ] ROP = d̄ × L + SS
- [ ] Exponential Smoothing: F(t+1) = αD(t) + (1-α)F(t)
- [ ] MAPE = (Σ|E|/D) / n × 100
- [ ] Total Cost = Holding + Ordering + Purchase
- [ ] Critical Ratio = Cu / (Cu + Co)

### Behavioral Prep
- [ ] "Why supply chain?" (quantitative + construction logistics angle)
- [ ] "Tell me about a time you optimized a process" (STAR story ready)
- [ ] "How do you handle a supply disruption?"
- [ ] Know current supply chain trends (nearshoring, AI, sustainability)

---

## Cross-Links

**Supply Chain:**
→ [Supply Chain Overview](supply-chain-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Operations Overview](../operations/operations-overview.md) — Operational optimization
→ [Risk Rapid Revision](../risk/risk-rapid-revision.md) — Supply chain risk
→ [Finance Rapid Revision](../finance/finance-rapid-revision.md) — Financial analysis

---

*Last updated: 2026-09-04*

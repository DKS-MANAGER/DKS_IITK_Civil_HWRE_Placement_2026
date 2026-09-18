# Operations — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core formulas, frameworks, and quick-fire Q&A for operations interviews.

---

## Framework 1: Process Mapping & Bottleneck Analysis

### Key Definitions
| Term | Definition |
|:-----|:-----------|
| **Throughput** | Actual output rate of the system |
| **Capacity** | Maximum possible output of a step |
| **Utilization** | Actual Output / Design Capacity |
| **Efficiency** | Actual Output / Effective Capacity |
| **Cycle Time** | Time to complete one unit at a step |
| **Lead Time** | Total time from order to delivery |
| **Takt Time** | Available time / Customer demand |

### Little's Law
```
L = λ × W
Work in Progress = Arrival Rate × Wait Time
```

### Theory of Constraints (TOC)
```
1. Identify the constraint (bottleneck)
2. Exploit it (maximize its output)
3. Subordinate everything else to it
4. Elevate it (increase capacity)
5. Repeat — the constraint moves
```

### Root-Cause Analysis
```
5 Whys:  Ask "why" 5 times to reach root cause
Fishbone: Categorize causes (Man, Machine, Material, Method, Measurement, Environment)
```

---

## Framework 2: Capacity Planning & Forecasting

### Capacity Metrics
```
Design Capacity   = Theoretical maximum output
Effective Capacity = Design - planned downtime
Actual Output     = What's actually produced

Utilization = Actual / Design
Efficiency  = Actual / Effective
```

### Forecasting Methods
```
Moving Average:      Fₜ₊₁ = (Aₜ + Aₜ₋₁ + ... + Aₜ₋ₙ₊₁) / n
Exponential Smoothing: Fₜ₊₁ = α × Aₜ + (1-α) × Fₜ
```

### Forecast Error
```
MAD  = Σ|Actual - Forecast| / n
MSE  = Σ(Actual - Forecast)² / n
MAPE = (Σ|Actual - Forecast| / Actual) / n × 100
```

### Aggregate Planning Strategies
| Strategy | Description | When to Use |
|:---------|:------------|:------------|
| **Chase** | Match capacity to demand (hire/fire) | Variable demand, low training cost |
| **Level** | Constant capacity, use inventory/backlog | Stable demand, high training cost |
| **Mixed** | Combination of both | Most real situations |

---

## Framework 3: Lean, Six Sigma & Quality

### 7 Wastes (TIMWOOD)
```
T - Transport (unnecessary movement of goods)
I - Inventory (excess stock)
M - Motion (unnecessary movement of people)
W - Waiting (idle time)
O - Overproduction (making more than needed)
O - Over-processing (doing more than required)
D - Defects (rework, scrap)
```

### 5S
```
Sort → Set in order → Shine → Standardize → Sustain
```

### DMAIC (Six Sigma)
```
Define → Measure → Analyze → Improve → Control
```

### Quality Metrics
```
Defect Rate = Defects / Total Units
DPMO = (Defects / (Units × Opportunities per Unit)) × 1,000,000
Sigma Level:  6σ = 3.4 DPMO,  5σ = 233 DPMO,  4σ = 6,210 DPMO,  3σ = 66,807 DPMO
```

### Process Capability
```
Cp  = (USL - LSL) / 6σ          (capability vs tolerance)
Cpk = min[(USL - μ)/3σ, (μ - LSL)/3σ]   (capability + centering)
```

---

## Framework 4: Operations Case Structure

### Case Framework
```
1. Clarify the objective
2. Map the process / build framework (MECE)
3. Quantify (use numbers, estimate)
4. Diagnose root causes
5. Recommend (prioritized, with metrics)
6. Define success measures
```

### Profitability Framework
```
Profit = Revenue - Cost
Revenue = Volume × Price
Cost = Fixed + Variable
```

### Process Improvement Framework
```
Map → Measure → Analyze → Improve → Control
(Identify bottleneck → quantify → fix → re-measure)
```

### Capacity Framework
```
Demand vs Supply:
  Demand > Supply → bottleneck, prioritize, expand
  Demand < Supply → underutilization, reduce cost, find new demand
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is a bottleneck?**
A: The step in a process that limits overall throughput. It's the constraint that determines system output — improving any other step won't increase output until the bottleneck is addressed.

**Q2: What is Little's Law?**
A: L = λ × W — the amount of work in process equals the arrival rate times the time each unit spends in the system. It links throughput, WIP, and lead time.

**Q3: What are the 7 wastes of Lean?**
A: Transport, Inventory, Motion, Waiting, Overproduction, Over-processing, and Defects (TIMWOOD). They're all forms of non-value-adding activity.

**Q4: What is the difference between Lean and Six Sigma?**
A: Lean focuses on eliminating waste and improving flow. Six Sigma focuses on reducing variation and defects using DMAIC and statistical tools. They're complementary.

**Q5: How do you identify a bottleneck?**
A: Find the step with the lowest capacity, or where work piles up (highest WIP). The bottleneck is where the queue forms and throughput is capped.

**Q6: What is DMAIC?**
A: Define, Measure, Analyze, Improve, Control — the Six Sigma improvement methodology. It's a data-driven, structured approach to process improvement.

**Q7: How do you forecast demand?**
A: Use moving averages for stable demand, exponential smoothing for recent trends, and trend/seasonal methods for patterns. Always validate with MAD/MAPE.

**Q8: What is capacity utilization?**
A: Actual output divided by design capacity. High utilization (>90%) may indicate a bottleneck; low utilization (<60%) may indicate excess capacity or demand issues.

**Q9: How does a civil engineering background help in operations?**
A: Site coordination, resource allocation, process thinking (construction workflows), bottleneck management (equipment, labor), and cost optimization — all directly transferable.

**Q10: How do you measure the impact of a process change?**
A: Compare before/after on key metrics: throughput, cycle time, defect rate, cost per unit, and utilization. Use a control chart to confirm the change is sustained.

---

## Last-Minute Checklist

### Before Any Operations Interview
- [ ] One civil operations story (site logistics, productivity, batching)
- [ ] Know the 7 wastes and DMAIC cold
- [ ] Practice one bottleneck case out loud
- [ ] Your "Why operations?" answer (link to civil engineering)

### Must-Know Formulas
- [ ] Little's Law: L = λ × W
- [ ] Utilization = Actual / Design Capacity
- [ ] Fₜ₊₁ = α × Aₜ + (1-α) × Fₜ
- [ ] DPMO = (Defects / (Units × Opportunities)) × 1,000,000
- [ ] MAD = Σ|Actual - Forecast| / n

### Behavioral Prep
- [ ] "Tell me about a time you improved a process" (STAR)
- [ ] "Describe a time you handled a bottleneck" (STAR)
- [ ] "Tell me about a time you reduced cost" (STAR)
- [ ] "How do you handle a supplier that's late?" (STAR)

---

## Cross-Links

**Operations:**
→ [Operations Overview](operations-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Supply Chain Overview](../supply-chain/supply-chain-overview.md) — Supply chain role
→ [Program Mgmt Overview](../program-management/pgm-overview.md) — PM role
→ [Case Frameworks](../consulting/case-frameworks.md) — Case interview prep

---

*Last updated: 2026-09-04*
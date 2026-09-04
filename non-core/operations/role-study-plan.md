# Operations — Role Study Plan

## Role Overview

The Operations role targets **operations manager/analyst positions** at e-commerce companies (Amazon, Flipkart, Delhivery), **manufacturing/FMCG** (HUL, P&G, ITC, Tata Steel), **logistics** (Delhivery, Blue Dart), and **consulting firms** (Deloitte, Accenture). The role covers process optimization, capacity planning, bottleneck analysis, quality management, and cost reduction. Civil engineers with project management and site coordination experience transition well into operations because they understand **processes, resource allocation, and execution under constraints**.

**Who targets this role:** B.Tech/M.Tech graduates with strong quantitative skills, students with site/internship experience, those who enjoy process improvement and efficiency, GATE qualifiers with operations interest.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Process Mapping & Bottleneck Analysis

#### Why This Matters
Every operations interview starts with process thinking. You must be able to map a process, identify bottlenecks, and propose improvements. This is directly analogous to construction workflow analysis.

#### What to Learn
- [ ] Process mapping: Flowcharts, SIPOC, value stream mapping
- [ ] Bottleneck identification: The step that limits throughput
- [ ] Little's Law: L = λ × W (Work in Progress = Arrival Rate × Wait Time)
- [ ] Throughput vs capacity vs utilization
- [ ] Cycle time vs lead time vs takt time
- [ ] Theory of Constraints (TOC): Find, exploit, subordinate, elevate, repeat
- [ ] Process metrics: Efficiency, utilization, throughput, defect rate
- [ ] Root-cause analysis: 5 Whys, fishbone (Ishikawa) diagram

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`operations-overview.md`](operations-overview.md) | Process mapping, bottlenecks | Full |
| [`supply-chain-overview.md`](../supply-chain/supply-chain-overview.md) | Process, inventory, logistics | Reference |

#### Worked Example
**Problem:** A concrete batching plant produces 40 m³/hour. The mixer can handle 60 m³/hour, the aggregate loader 50 m³/hour, and the truck loading bay 40 m³/hour. (a) What is the bottleneck? (b) If the plant runs 10 hours/day, what is daily output? (c) How would you increase output?

**Solution:**
1. **Identify the bottleneck:** The truck loading bay at 40 m³/hour is the slowest step → **bottleneck**
2. **Daily output:** 40 m³/hour × 10 hours = **400 m³/day**
3. **Improvement options:**
   - Add a second loading bay → capacity rises to 50 m³/hour (next constraint)
   - Reduce truck turnaround time (pre-position trucks, faster documentation)
   - Improve scheduling to avoid idle time at the bay
   - After fixing the bay, the aggregate loader (50 m³/hr) becomes the new bottleneck

**Interview insight:** "The bottleneck determines system output — the mixer at 60 m³/hr is underutilized because the loading bay caps throughput at 40 m³/hr. Per the Theory of Constraints, I'd focus improvement on the loading bay first, then re-evaluate because the constraint moves."

#### Practice
**Basic (3–5):**
1. What is a bottleneck? How do you identify it?
2. Define throughput, capacity, and utilization.
3. What is Little's Law? What does it tell you?
4. What is the difference between cycle time and lead time?
5. What is a value stream map?

**Intermediate (3–5):**
6. A process has 4 steps with capacities 50, 40, 60, 45 units/hr. Find the bottleneck and system output.
7. Using Little's Law, if 20 units are in process and throughput is 5 units/hr, what is the wait time?
8. How do you reduce cycle time in a process?
9. A bottleneck is fixed — what happens next?
10. How do you measure the impact of a process change?

**Interview-Level (5+):**
11. A factory's output dropped 20%. How do you diagnose it?
12. Explain the Theory of Constraints with an example.
13. How do you balance quality and speed in a process?
14. How would you optimize a warehouse layout?
15. Use your civil experience to describe a bottleneck you resolved.

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Map this process and find the bottleneck | Process thinking |
| What is Little's Law? | Quantitative fundamentals |
| A process is too slow — what do you do? | Problem solving |
| How do you measure efficiency? | Metrics knowledge |
| How do you improve a process? | Improvement methodology |

#### Common Mistakes
- **Confusing** capacity with throughput — throughput is limited by the bottleneck
- **Forgetting** that fixing one bottleneck reveals another
- **Ignoring** variability — average capacity hides peak/off-peak issues
- **Not** measuring before and after a change
- **Treating** all steps equally — focus on the constraint

#### Completion Criterion
✅ Can map any process and identify the bottleneck
✅ Can apply Little's Law and Theory of Constraints
✅ Can compute throughput, capacity, and utilization
✅ Can run root-cause analysis (5 Whys, fishbone)

---

### Topic 2: Capacity Planning & Forecasting

#### Why This Matters
Operations roles require matching supply to demand. Capacity planning and forecasting are quantitative skills tested in case interviews and numerical rounds.

#### What to Learn
- [ ] Capacity planning: Design capacity vs effective capacity vs actual output
- [ ] Capacity utilization = Actual Output / Design Capacity
- [ ] Efficiency = Actual Output / Effective Capacity
- [ ] Demand forecasting: Moving average, exponential smoothing, trend projection
- [ ] Forecast error: MAD, MSE, MAPE
- [ ] Exponential smoothing: Fₜ₊₁ = α × Aₜ + (1-α) × Fₜ
- [ ] Safety capacity and buffer management
- [ ] Aggregate planning: Chase, level, and mixed strategies

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`operations-overview.md`](operations-overview.md) | Capacity planning, forecasting | Full |
| [`supply-chain-overview.md`](../supply-chain/supply-chain-overview.md) | Demand forecasting | Reference |

#### Worked Example
**Problem:** A warehouse handled the following monthly shipments (in thousands): Jan=80, Feb=85, Mar=90, Apr=95, May=100. (a) Forecast June using a 3-month moving average. (b) Forecast June using exponential smoothing with α=0.3, assuming May's forecast was 92. (c) Which is more responsive?

**Solution:**
1. **3-month moving average:** (90 + 95 + 100) / 3 = **95,000 shipments**
2. **Exponential smoothing:**
   - F_June = α × A_May + (1-α) × F_May = 0.3 × 100 + 0.7 × 92 = 30 + 64.4 = **94.4,000 shipments**
3. **Comparison:** The moving average (95) is more responsive to the recent uptrend because it only uses the last 3 months, while exponential smoothing with α=0.3 weights history more heavily.

**Interview insight:** "The choice depends on the demand pattern. If demand is trending, I'd use a higher α or a trend-adjusted method. If demand is stable, a lower α smooths out noise. I'd validate with forecast error metrics (MAD/MAPE) before committing."

#### Practice
**Basic (3–5):**
1. What is capacity planning?
2. Define design capacity, effective capacity, and actual output.
3. What is capacity utilization? How do you compute it?
4. What is a moving average forecast?
5. What is exponential smoothing?

**Intermediate (3–5):**
6. Compute a 4-month moving average forecast.
7. Forecast using exponential smoothing with α=0.2 given actual and prior forecast.
8. Calculate MAD for a set of forecasts.
9. A plant runs at 70% utilization. Is that good or bad? Why?
10. How do you handle demand seasonality?

**Interview-Level (5+):**
11. Demand spiked unexpectedly. What do you do?
12. How do you decide between chase and level aggregate strategies?
13. How do you forecast for a new product with no history?
14. How do you balance overcapacity cost vs undercapacity risk?
15. How would you plan capacity for a construction project?

#### Common Mistakes
- **Confusing** utilization with efficiency — they use different denominators
- **Ignoring** seasonality and trends in forecasts
- **Not** measuring forecast error
- **Planning** capacity at average demand without buffer
- **Assuming** more capacity is always better — it's a cost

#### Completion Criterion
✅ Can compute capacity utilization and efficiency
✅ Can build moving average and exponential smoothing forecasts
✅ Can calculate forecast error (MAD, MAPE)
✅ Can choose between chase and level strategies

---

### Topic 3: Lean, Six Sigma & Quality Management

#### Why This Matters
Lean and Six Sigma are the standard improvement methodologies in operations. Recruiters test your understanding of waste elimination, DMAIC, and quality tools.

#### What to Learn
- [ ] Lean principles: Value, value stream, flow, pull, perfection
- [ ] 7 Wastes (TIMWOOD): Transport, Inventory, Motion, Waiting, Overproduction, Over-processing, Defects
- [ ] 5S: Sort, Set in order, Shine, Standardize, Sustain
- [ ] Six Sigma: DMAIC (Define, Measure, Analyze, Improve, Control)
- [ ] Statistical process control: Control charts, process capability (Cp, Cpk)
- [ ] Defect metrics: DPMO, Sigma level
- [ ] Kaizen: Continuous improvement
- [ ] Poka-yoke: Mistake-proofing

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`operations-overview.md`](operations-overview.md) | Lean, Six Sigma, quality | Full |
| [`non-core-prep.md`](../analytics/non-core-prep.md) | Statistics for quality | Reference |

#### Worked Example
**Problem:** A process produces 10,000 units/month with 200 defects. (a) What is the defect rate? (b) If each unit has 5 opportunities for defects, what is DPMO? (c) What sigma level is this approximately?

**Solution:**
1. **Defect rate:** 200 / 10,000 = **2%**
2. **DPMO:** (200 / (10,000 × 5)) × 1,000,000 = (200 / 50,000) × 1,000,000 = **4,000 DPMO**
3. **Sigma level:** 4,000 DPMO ≈ **4.1σ** (from sigma table; 3.4 DPMO = 6σ)

**Interview insight:** "At 4,000 DPMO, this process is around 4.1 sigma — acceptable but not world-class. Using DMAIC, I'd first measure where defects occur (Pareto analysis), find root causes, then implement controls. The goal would be to reduce DPMO toward 3.4 (6σ)."

#### Practice
**Basic (3–5):**
1. What are the 7 wastes of Lean?
2. Explain DMAIC.
3. What is 5S?
4. What is Kaizen?
5. What is a control chart?

**Intermediate (3–5):**
6. Calculate DPMO for a process with given defects and opportunities.
7. What is the difference between Cp and Cpk?
8. How do you identify the most common defect type?
9. What is a Pareto chart? When do you use it?
10. How do you sustain improvements after a project?

**Interview-Level (5+):**
11. A process has high variability. How do you reduce it?
12. Explain the difference between Lean and Six Sigma.
13. How do you implement a quality culture?
14. A defect is found in the field. What's your response?
15. How would you apply Lean to a construction site?

#### Common Mistakes
- **Confusing** Lean (waste elimination, flow) with Six Sigma (variation reduction)
- **Forgetting** that DPMO depends on opportunities per unit
- **Not** using data to prioritize improvements
- **Skipping** the Control phase — improvements don't stick
- **Treating** 5S as cleaning — it's a standardization system

#### Completion Criterion
✅ Can explain the 7 wastes and 5S
✅ Can apply DMAIC to a process problem
✅ Can compute DPMO and interpret sigma level
✅ Can use control charts and Pareto analysis

---

### Topic 4: Operations Case Studies (Civil-Relevant)

#### Why This Matters
Operations interviews use case studies to test structured thinking. Your civil background gives you authentic cases — construction productivity, site logistics, concrete batching — that differentiate you.

#### What to Learn
- [ ] Case structure: Clarify → Framework → Quantify → Recommend
- [ ] Profitability framework: Revenue - Cost, volume × price
- [ ] Process improvement framework: Map → Measure → Analyze → Improve
- [ ] Capacity framework: Demand vs supply, bottleneck
- [ ] Cost reduction framework: Fixed vs variable, direct vs indirect
- [ ] MECE structuring and issue trees
- [ ] Guesstimate basics for operations (throughput, capacity)
- [ ] Communicating recommendations with data

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`operations-overview.md`](operations-overview.md) | Civil-relevant cases | Full |
| [`case-frameworks.md`](../consulting/case-frameworks.md) | Case frameworks | Reference |

#### Worked Example
**Problem:** "A construction project is 30% behind schedule. Diagnose and fix."

**Solution (Structured):**
1. **Clarify:** Which phase? Is it critical path work? What's the baseline?
2. **Map the critical path:** Identify which activities are delayed
3. **Diagnose root causes:**
   - Labor: shortage, low productivity
   - Materials: delayed delivery, shortage
   - Equipment: breakdowns, low utilization
   - External: weather, approvals, rework
4. **Quantify impact:** Each delay's effect on the critical path (days)
5. **Recommend:**
   - Reschedule non-critical work to free resources
   - Add resources on critical path (crashing)
   - Improve material logistics (just-in-time delivery)
   - Fast-track approvals
6. **Measure:** Track schedule variance weekly; recover X days

**Interview insight:** "I'd focus on the critical path first — only delays there extend the project. I'd quantify each delay's impact, then apply the highest-leverage fixes: crashing critical activities, improving logistics, and managing external dependencies."

#### Practice
**Basic (3–5):**
1. What is the structure of an operations case?
2. How do you diagnose a drop in output?
3. What KPIs would you track for a plant?
4. How do you reduce turnaround time?
5. What is an issue tree?

**Intermediate (3–5):**
6. "A warehouse has high congestion. Diagnose and fix."
7. "A delivery fleet has low utilization. Improve it."
8. "A factory's defect rate doubled. Investigate."
9. "A supplier is consistently late. What do you do?"
10. "Design an operations plan for a new facility."

**Interview-Level (5+):**
11. "A company's margins are falling. Diagnose."
12. "How would you double a plant's output in 12 months?"
13. "A team is overworked but output is flat. What do you do?"
14. "How do you measure the ROI of a process improvement?"
15. "Use your civil experience to solve a site logistics problem."

#### Common Mistakes
- **Jumping** to solutions without diagnosing root causes
- **Not** quantifying — use numbers to support recommendations
- **Ignoring** the bottleneck when proposing improvements
- **Forgetting** to consider implementation cost and risk
- **Not** defining success metrics for the recommendation

#### Completion Criterion
✅ Can structure any operations case (clarify → framework → quantify → recommend)
✅ Can diagnose output, quality, and cost problems
✅ Can use civil experience in operations cases
✅ Can quantify recommendations with metrics

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | A process has 4 steps with capacities 60, 45, 70, 50 units/hr. Find the bottleneck, system output, and utilization of each step. | Bottleneck | 25 |
| 2 | Monthly demand: Jan=100, Feb=110, Mar=120, Apr=130, May=140 (thousands). Forecast June using 3-month MA and exponential smoothing (α=0.4, F_May=135). Compute MAD for the MA. | Forecasting | 25 |
| 3 | A process produces 20,000 units with 300 defects, 4 opportunities/unit. Compute defect rate, DPMO, and approximate sigma level. | Quality | 20 |
| 4 | "A concrete batching plant has 40% equipment utilization. Improve it." Structure your diagnosis and recommendations. | Case Study | 20 |
| 5 | Explain Little's Law. If WIP=30 and throughput=6/hr, what is the wait time? | Fundamentals | 10 |
| | | **Total** | **100** |

---

## Company Navigation

| Company | What They Test | Focus |
|:--------|:---------------|:------|
| **Amazon** | Leadership principles, process excellence | Behavioral + Process |
| **Flipkart** | Ownership, bias for action | Behavioral + Case |
| **Delhivery** | Logistics, network design | Case + Capacity |
| **HUL/P&G** | Supply chain, brand ops | Case + Forecasting |
| **ITC** | Process, quality | Lean + Quality |
| **Tata Steel** | Manufacturing ops | Capacity + Lean |
| **Deloitte/Accenture** | Case + analytical | Case + Process |
| **L&T** | Site operations | Civil cases + Lean |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Operations Overview | [operations-overview.md](operations-overview.md) |
| Supply Chain | [supply-chain-overview.md](../supply-chain/supply-chain-overview.md) |
| Program Management | [pgm-overview.md](../program-management/pgm-overview.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Case Frameworks | [case-frameworks.md](../consulting/case-frameworks.md) |
| Rapid Revision | [operations-rapid-revision.md](operations-rapid-revision.md) |

---

*Operations is where strategy meets execution. Your Civil project management experience is a direct advantage.*
# Business Case Interview Playbook: The Tredence Consulting Method

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Format:** Interactive 30–45 Minute Case Discussion with Senior Principal or Director

---

## 1. Core Mindset: The "Driver" Persona

In a Tredence case interview, the interviewer acts as a client or senior engagement leader.
- **Do not be passive:** Do not wait for the interviewer to feed you hints.
- **Drive the structure:** Proactively layout a structured roadmap, formulate testable hypotheses, ask targeted clarifying questions, and drive the analysis to concrete recommendations.
- **Always quantify:** Convert percentages to dollar values; estimate annual EBITDA impact.

---

## 2. The 6-Phase Case Execution Architecture

```
 Total Case Time: 30 - 45 Minutes
 [ Phase 1: Clarify & Scope ] ─────────> 3 Minutes
         │
 [ Phase 2: Hypothesis & Framework ] ──> 5 Minutes
         │
 [ Phase 3: Data Discovery & Audit ] ──> 7 Minutes
         │
 [ Phase 4: Modeling & Trade-offs ] ───> 10 Minutes
         │
 [ Phase 5: Last-Mile Adoption ] ──────> 7 Minutes
         │
 [ Phase 6: Executive Synthesis ] ─────> 3 Minutes
```

---

## 3. Step-by-Step Case Execution Walkthrough

### Scenario Prompt:
> *"A major North American grocery retail client with 800 stores is seeing declining profitability in their bakery and deli department. How would you investigate and solve this using data science?"*

### Phase 1: Clarify & Scope (Minutes 0–3)
- **Confirm Objective:** *"Is the primary goal to restore gross profit margins, reduce operational waste/spoilage, or increase top-line footfall?"*
- **Scope Parameters:** *"What is the revenue scale of this department? What are the physical constraints (e.g., shelf-life of baked goods is 24–48 hours)?"*
- **Interviewer Response:** *"Department revenue is \$400M. Spoilage write-offs have increased from 8% to 14%, costing \$24M in lost margin. Top SKUs frequently run out by 4 PM on weekends."*

### Phase 2: Hypothesis & Framework (Minutes 3–8)
Structure the problem on the whiteboard:
$$\text{Department Profit} = (\text{Volume Sold} \times \text{Gross Margin per Unit}) - (\text{Spoilage Write-Offs}) - (\text{Labor/Baking Costs})$$
- **Core Hypothesis:** *"The root cause is a static replenishment heuristic. Stores bake fixed quantities every morning regardless of day-of-week seasonality, weather, or local promotional footfall. On rainy weekdays, excess inventory expires; on sunny weekends, stores under-bake and stock out early."*

### Phase 3: Data Discovery & Audit (Minutes 8–15)
- Identify data signals:
  - POS hourly transaction scanner data (captures stockout hour when sales abruptly drop to zero).
  - Production batch logs (baking times and batch sizes).
  - Spoilage write-off logs (dump/spoilage scanned barcodes).
  - Exogenous signals: Local weather, holidays, neighboring competitor discounts.
- Audit data quality: Flag missing batch logs; handle censored demand (unobserved demand after 4 PM stockouts).

### Phase 4: Modeling & Trade-offs (Minutes 15–25)
- Formulate analytical solution:
  1. **Demand Distribution Forecasting:** LightGBM Quantile Regression ($\tau = 0.50, \tau = 0.85$) predicting hourly customer purchase rate.
  2. **Batch Scheduling Optimization:** Dynamic integer programming determining two optimal baking windows (e.g., 6:00 AM primary bake + 1:00 PM secondary supplemental bake).
- Justify model choice: *"We chose quantile regression because the cost of over-baking (spoilage write-off) differs from the cost of under-baking (lost margin + customer goodwill). An asymmetric pinball loss allows the business to tune service levels dynamically."*

### Phase 5: The "Last-Mile" Adoption Plan ("Now What?") (Minutes 25–32)
- Describe the frontline operational tool:
  - A ruggedized tablet interface for bakery staff.
  - At 5:30 AM, tablet displays: *"Today's Target: Bake 120 croissants by 6:30 AM. Re-evaluate inventory at 12:30 PM for secondary bake."*
  - Reason code displayed: *"High weekend footfall + sunny weather (+18% expected lift)."*
- Change Management: Run a 4-week A/B pilot across 40 stores vs 40 control stores to prove EBITDA recovery before enterprise-wide rollout.

### Phase 6: Executive Synthesis (Final 3 Minutes)
Deliver an executive pitch using SCQA:
> *"In summary, the bakery department's \$24M spoilage crisis is driven by static baking schedules disconnected from demand volatility. By deploying a dynamic two-tier quantile replenishment system with store tablet integration, we project a 30% reduction in spoilage and a 5% recovery in lost stockout sales. This translates to **+\$8.5M in annualized net EBITDA lift**, paying for the entire data analytics initiative within 90 days of deployment."*

# Business Operations (BizOps) — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core frameworks, formulas, and quick-fire Q&A for BizOps interviews.

---

## Framework 1: KPI Management & Reporting

### KPI Types
```
Leading indicators  = Predict future performance (pipeline, traffic, engagement)
Lagging indicators  = Measure past results (revenue, profit, churn)
```

### Key Business Metrics
| Metric | Definition |
|:-------|:-----------|
| **Revenue/GMV** | Total sales / Gross merchandise value |
| **Conversion** | Purchasers / Visitors |
| **AOV** | Average order value = Revenue / Orders |
| **CAC** | Customer acquisition cost |
| **LTV** | Lifetime value per customer |
| **Churn** | % of customers lost per period |
| **Retention** | % of customers retained |
| **Margin** | (Revenue - Cost) / Revenue |

### KPI Tree
```
Business Goal → Revenue → Traffic × Conversion × AOV
                              ↓
                    Segment by channel, device, region, user type
```

### Metric Investigation Framework
```
1. Check data quality (is it real?)
2. Segment (channel, device, region, user type)
3. Check external factors (seasonality, incidents, campaigns)
4. Find root cause
5. Recommend (tied to root cause)
```

### Dashboard Design
```
Show the few KPIs that matter → trend over time → segment view
→ compare to target → add context (what changed, why)
```

---

## Framework 2: Process Design & Improvement

### Process Mapping (SIPOC)
```
Suppliers → Inputs → Process → Outputs → Customers
```

### Bottleneck Analysis
```
Find the step with lowest capacity / highest WIP
→ Fix it → re-measure (constraint moves)
```

### 7 Wastes (TIMWOOD)
```
Transport, Inventory, Motion, Waiting, Overproduction, Over-processing, Defects
```

### DMAIC (Six Sigma)
```
Define → Measure → Analyze → Improve → Control
```

### Root-Cause Analysis
```
5 Whys: ask "why" 5 times
Fishbone: Man, Machine, Material, Method, Measurement, Environment
```

### Process Improvement Steps
```
Map → Measure each step → Find bottleneck → Improve
→ Measure after → Standardize → Control
```

---

## Framework 3: Cross-Functional Coordination & Decision Support

### Alignment Framework
```
Understand each team's goals and incentives
→ Quantify the trade-off (data, not opinion)
→ Find a middle ground (tiered, conditional, framework-based)
→ Get buy-in → Track impact
```

### Prioritization (RICE)
```
RICE = (Reach × Impact × Confidence) / Effort
Higher RICE = higher priority
```

### MoSCoW
```
Must Have → Should Have → Could Have → Won't Have
```

### Decision Matrix
```
Criteria (weighted) × Options → Score → Choose highest
```

### Influence Without Authority
```
Build trust → Use data → Align incentives → Communicate clearly
→ Deliver value → Earn credibility
```

---

## Framework 4: BizOps Case Structure

### Case Framework
```
1. Clarify the objective
2. Build framework (MECE)
3. Quantify (demand vs capacity, revenue vs cost)
4. Diagnose root causes
5. Recommend (prioritized, sequenced)
6. Define success metrics
```

### Scaling Framework
```
Demand vs Capacity:
  Demand growing faster than capacity → gap
  Fix: quick wins (automation, prioritization) → structural (hiring, systems)
```

### Cost Optimization
```
Cut waste first (not value)
→ Renegotiate (vendors, contracts)
→ Automate (repetitive work)
→ Measure impact on quality and growth
```

### Growth vs Operations
```
Growth = top line (revenue, users)
Operations = bottom line (efficiency, quality, cost)
Balance: scale operations to match growth without breaking quality
```

---

## 10 Quick-Fire Interview Answers

**Q1: What does business operations do?**
A: BizOps manages the internal processes, KPIs, and cross-functional coordination that keep a business running efficiently. It's the operational backbone — tracking metrics, improving processes, and supporting decisions with data.

**Q2: What KPIs would you track for a business?**
A: Revenue, conversion, CAC, LTV, churn, retention, and margin. The specific set depends on the business model — e-commerce tracks GMV and AOV; SaaS tracks MRR and churn.

**Q3: What is the difference between leading and lagging indicators?**
A: Leading indicators predict future performance (pipeline, engagement); lagging indicators measure past results (revenue, churn). You need both — leading to act, lagging to validate.

**Q4: A KPI fell 20%. How do you investigate?**
A: Check data quality first, then segment (channel, device, region, user type), check external factors (seasonality, incidents), find the root cause, and recommend a fix tied to that cause.

**Q5: What is the difference between BizOps and operations?**
A: Operations focuses on physical/operational processes (manufacturing, logistics). BizOps focuses on business processes and metrics across functions — it's more strategic and cross-functional.

**Q6: How do you improve a process?**
A: Map it, measure each step, find the bottleneck, improve it, measure after, and standardize. I'd use Lean/Six Sigma tools (DMAIC, 7 wastes) and always quantify the before/after.

**Q7: How do you align two teams with conflicting goals?**
A: Understand each team's incentives, quantify the trade-off with data, find a middle ground (tiered or conditional policy), and get buy-in. Data, not opinion, is the arbiter.

**Q8: What is RICE prioritization?**
A: RICE = (Reach × Impact × Confidence) / Effort. It scores initiatives to prioritize where to invest — high reach, high impact, high confidence, low effort wins.

**Q9: How does a civil engineering background help in BizOps?**
A: Project coordination, process thinking (construction workflows), resource allocation, KPI tracking (schedule, cost, quality), and delivering under constraints — all directly transferable.

**Q10: How do you measure the impact of a process change?**
A: Compare before/after on key metrics: cycle time, throughput, cost, defect rate, and SLA compliance. Use a control period or control group, and confirm the change is sustained.

---

## Last-Minute Checklist

### Before Any BizOps Interview
- [ ] One BizOps story (process improvement, coordination, metric investigation)
- [ ] Know the KPI tree and metric investigation framework cold
- [ ] Practice one scaling case out loud
- [ ] Your "Why BizOps?" answer (link to civil engineering)

### Must-Know Concepts
- [ ] Leading vs lagging indicators
- [ ] KPI tree (Revenue = Traffic × Conversion × AOV)
- [ ] SIPOC process mapping
- [ ] 7 wastes (TIMWOOD)
- [ ] DMAIC
- [ ] RICE prioritization
- [ ] LTV/CAC, churn, retention

### Behavioral Prep
- [ ] "Tell me about a time you improved a process" (STAR)
- [ ] "Describe a time you aligned conflicting teams" (STAR)
- [ ] "Tell me about a time you used data to make a decision" (STAR)
- [ ] "How do you handle a metric decline?" (STAR)

---

## Cross-Links

**BizOps:**
→ [BizOps Overview](biz-ops-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Operations Overview](../operations/operations-overview.md) — Operations role
→ [Strategy Overview](../strategy/strategy-overview.md) — Strategy role
→ [Business Fundamentals](../common/business-fundamentals.md) — Business basics

---

*Last updated: 2026-09-04*
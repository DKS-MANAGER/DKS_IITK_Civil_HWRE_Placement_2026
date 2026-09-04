# Business Operations (BizOps) — Role Study Plan

## Role Overview

The Business Operations (BizOps) role targets **business operations/strategy operations positions** at tech companies (Google, Amazon, Flipkart, Uber, Swiggy), **fintech** (Paytm, PhonePe, Razorpay), **consulting firms** (Deloitte, Accenture), and **corporate functions** (Tata, Reliance). The role covers KPI management, process design, cross-functional coordination, decision support, and operational strategy. Civil engineers with project coordination and analytical skills transition well — BizOps is about making things work at scale, which mirrors site and project operations.

**Who targets this role:** B.Tech/M.Tech graduates with strong analytical and coordination skills, students with project/site experience, those who enjoy process improvement and business analysis, GATE qualifiers with business interest.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: KPI Management & Reporting

#### Why This Matters
BizOps is fundamentally about metrics. You must know which KPIs matter, how to track them, and how to investigate when they change. This is the most-tested skill in BizOps interviews.

#### What to Learn
- [ ] KPI types: Leading vs lagging indicators
- [ ] Business metrics: Revenue, GMV, margin, CAC, LTV, churn, retention
- [ ] Operational metrics: Throughput, cycle time, utilization, SLA
- [ ] Dashboard design: What to show, how to show it
- [ ] Reporting cadence: Daily, weekly, monthly
- [ ] Metric investigation: Segment → external factors → root cause
- [ ] Data sources: SQL, Excel, BI tools (Power BI, Tableau)
- [ ] KPI tree: How metrics cascade from business goals

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`biz-ops-overview.md`](biz-ops-overview.md) | KPI management, reporting | Full |
| [`business-fundamentals.md`](../common/business-fundamentals.md) | Business fundamentals | Reference |

#### Worked Example
**Problem:** An e-commerce company's conversion rate dropped from 3% to 2.4% this month. Investigate using a KPI tree.

**Solution:**
1. **Define the KPI tree:**
   - Revenue = Traffic × Conversion × AOV
   - Conversion = (Visitors who purchase) / Total visitors
2. **Segment the drop:**
   - By traffic source (organic, paid, social, direct)
   - By device (mobile, desktop)
   - By product category
   - By new vs returning users
3. **Check external factors:**
   - Competitor promotions
   - Pricing changes
   - Site performance (page load, checkout errors)
   - Seasonality
4. **Hypotheses:**
   - Paid traffic quality declined (more clicks, fewer purchases)
   - Checkout bug on mobile
   - Price increase reduced conversion
5. **Recommend:**
   - Fix the identified issue (bug, pricing, campaign quality)
   - Reallocate spend to higher-converting channels

**Interview insight:** "I'd use a KPI tree to decompose the problem, then segment to isolate the driver. A 20% drop in conversion is rarely uniform — it's usually concentrated in one segment (e.g., mobile checkout). I'd check data quality first, then external factors, then segment-level analysis."

#### Practice
**Basic (3–5):**
1. What is a KPI? What makes a good KPI?
2. What is the difference between leading and lagging indicators?
3. What is conversion rate? How do you compute it?
4. What is a dashboard? What should it contain?
5. What is the difference between a metric and a KPI?

**Intermediate (3–5):**
6. Build a KPI tree for an e-commerce business.
7. A KPI fell 20%. How do you investigate?
8. How do you design a reporting dashboard?
9. What is the difference between CAC and LTV?
10. How do you track operational SLAs?

**Interview-Level (5+):**
11. How do you decide which KPIs matter most?
12. A metric is improving but the business isn't. What's wrong?
13. How do you balance short-term and long-term metrics?
14. How do you communicate a metric decline to leadership?
15. How do you set targets for a new business unit?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| What KPIs would you track for this business? | Business acumen |
| A KPI fell — how do you investigate? | Analytical thinking |
| Design a dashboard | Reporting skill |
| What's the difference between CAC and LTV? | Fundamentals |
| How do you set targets? | Judgment |

#### Common Mistakes
- **Tracking** too many metrics — focus on the few that matter
- **Confusing** leading and lagging indicators
- **Not** segmenting data before concluding
- **Ignoring** data quality issues
- **Reporting** without insight or recommendation

#### Completion Criterion
✅ Can build a KPI tree from business goals
✅ Can investigate a metric change systematically
✅ Can design a reporting dashboard
✅ Can distinguish leading vs lagging indicators

---

### Topic 2: Process Design & Improvement

#### Why This Matters
BizOps designs and improves the processes that run the business. Process mapping, bottleneck analysis, and improvement methodologies are core skills.

#### What to Learn
- [ ] Process mapping: Flowcharts, SIPOC, swimlanes
- [ ] Bottleneck identification and resolution
- [ ] Lean basics: 7 wastes, 5S, Kaizen
- [ ] Six Sigma: DMAIC
- [ ] Root-cause analysis: 5 Whys, fishbone
- [ ] Process metrics: Cycle time, throughput, defect rate
- [ ] Automation opportunities in processes
- [ ] Change management: Getting teams to adopt new processes

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`biz-ops-overview.md`](biz-ops-overview.md) | Process design, improvement | Full |
| [`operations-overview.md`](../operations/operations-overview.md) | Process mapping, Lean | Reference |

#### Worked Example
**Problem:** A company's customer onboarding takes 5 days. The goal is 2 days. Map the process and identify improvements.

**Solution:**
1. **Map the process (SIPOC):**
   - Suppliers: Sales team, KYC vendor, IT
   - Inputs: Customer application, documents
   - Process: Submit → Verify KYC → Credit check → Approve → Notify
   - Outputs: Activated account
   - Customers: New users
2. **Measure each step:**
   - Submit: 0.5 day
   - KYC verification: 2 days (manual review)
   - Credit check: 1.5 days
   - Approval: 0.5 day
   - Notify: 0.5 day
   - **Total: 5 days**
3. **Identify bottleneck:** KYC verification (2 days, manual)
4. **Improve:**
   - Automate KYC (document OCR + verification API) → 0.5 day
   - Parallelize credit check with KYC
   - Set SLA alerts for manual reviews
5. **Result:** 5 days → **2 days** (meets goal)

**Interview insight:** "I'd map the process, measure each step, and find the bottleneck — KYC at 2 days. Automation is the highest-leverage fix. I'd also parallelize steps that don't depend on each other. The key is measuring before and after to prove the improvement."

#### Practice
**Basic (3–5):**
1. What is process mapping?
2. What is a bottleneck?
3. What are the 7 wastes of Lean?
4. What is DMAIC?
5. What is root-cause analysis?

**Intermediate (3–5):**
6. Map a process and identify the bottleneck.
7. How do you reduce cycle time?
8. What is the difference between Lean and Six Sigma?
9. How do you measure the impact of a process change?
10. How do you get teams to adopt a new process?

**Interview-Level (5+):**
11. A process is broken. How do you fix it?
12. How do you decide what to automate?
13. How do you balance standardization and flexibility?
14. How do you handle resistance to process change?
15. Design an onboarding process for a new business unit.

#### Common Mistakes
- **Jumping** to solutions without mapping the process
- **Not** measuring before and after
- **Ignoring** the human side of change
- **Automating** a bad process (automating waste)
- **Forgetting** to define success metrics

#### Completion Criterion
✅ Can map any process (SIPOC, flowchart)
✅ Can identify and fix bottlenecks
✅ Can apply Lean/Six Sigma tools
✅ Can manage process change

---

### Topic 3: Cross-Functional Coordination & Decision Support

#### Why This Matters
BizOps sits between teams — sales, marketing, product, finance, operations. You must coordinate, align priorities, and support decisions with data.

#### What to Learn
- [ ] Cross-functional coordination: Aligning teams with different goals
- [ ] Stakeholder management: Power/interest, communication plans
- [ ] Decision frameworks: Pros/cons, decision matrix, cost-benefit
- [ ] Prioritization: RICE, MoSCoW, impact vs effort
- [ ] Escalation management: When and how
- [ ] Meeting management: Agendas, decisions, action items
- [ ] Influence without authority
- [ ] Conflict resolution

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`biz-ops-overview.md`](biz-ops-overview.md) | Coordination, decision support | Full |
| [`behavioral.md`](../common/behavioral.md) | Communication, STAR stories | Reference |

#### Worked Example
**Problem:** Sales wants to offer a 20% discount to close deals; Finance wants to protect margins. As BizOps, how do you align them?

**Solution:**
1. **Understand both sides:**
   - Sales: Discounts close deals, hit revenue targets
   - Finance: 20% discount may break unit economics
2. **Quantify the trade-off:**
   - Current: Price ₹100, margin 30% → ₹30 margin
   - With 20% discount: Price ₹80, margin 30% → ₹24 margin (or lower if volume doesn't compensate)
   - Break-even: How much extra volume is needed to offset the margin loss?
3. **Find a middle ground:**
   - Tiered discounts (10% standard, 20% only for large deals)
   - Discount approval framework (above X% requires finance sign-off)
   - Track discount impact on margins monthly
4. **Recommend:** A tiered discount policy with a clear approval framework, backed by the break-even analysis.

**Interview insight:** "I'd frame it as a data problem, not a conflict. By quantifying the break-even volume, both teams can agree on a policy. The BizOps role is to align incentives with data — a tiered discount with finance sign-off protects margins while letting sales close deals."

#### Practice
**Basic (3–5):**
1. What is cross-functional coordination?
2. How do you align teams with conflicting goals?
3. What is a decision matrix?
4. What is RICE prioritization?
5. When should you escalate?

**Intermediate (3–5):**
6. Two departments have conflicting priorities. How do you align them?
7. How do you influence without authority?
8. How do you run an effective meeting?
9. How do you prioritize business initiatives?
10. How do you handle a stakeholder who disagrees?

**Interview-Level (5+):**
11. A key stakeholder disagrees with your recommendation. What do you do?
12. How do you balance short-term efficiency and long-term growth?
13. How do you build trust across teams?
14. How do you make a decision with incomplete data?
15. Describe a time you resolved a cross-functional conflict.

#### Common Mistakes
- **Taking** sides instead of aligning on data
- **Not** documenting decisions and action items
- **Escalating** too early or too late
- **Ignoring** the incentives of each team
- **Making** decisions without stakeholder buy-in

#### Completion Criterion
✅ Can align cross-functional teams with data
✅ Can use decision and prioritization frameworks
✅ Can influence without authority
✅ Can manage conflicts and escalations

---

### Topic 4: BizOps Case Studies & Analytical Scenarios

#### Why This Matters
BizOps interviews use case studies to test structured thinking, business judgment, and analytical ability. Your civil background gives you authentic operational stories.

#### What to Learn
- [ ] Case structure: Clarify → Framework → Quantify → Recommend
- [ ] Business diagnosis: Revenue, cost, efficiency problems
- [ ] Growth scenarios: Scaling operations
- [ ] Cost optimization: Where to cut without breaking the business
- [ ] Guesstimates: Market sizing, operational estimates
- [ ] Data interpretation: Charts, tables, trends
- [ ] Communicating recommendations
- [ ] Civil-to-BizOps story translation

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`biz-ops-overview.md`](biz-ops-overview.md) | Scenarios, cases | Full |
| [`case-frameworks.md`](../consulting/case-frameworks.md) | Case frameworks | Reference |

#### Worked Example
**Problem:** "A business is growing 30% year-over-year, but operations can't keep up — support tickets are piling up and delivery times are slipping. What do you do?"

**Solution (Structured):**
1. **Clarify:** Which operations? Support, fulfillment, or both? What's the SLA impact?
2. **Framework (Demand vs Capacity):**
   - Demand: Growing 30% → more tickets, more orders
   - Capacity: Headcount, tools, processes
3. **Diagnose:**
   - Support: Ticket volume up, handle time up, automation low
   - Fulfillment: Order volume up, warehouse capacity constrained
4. **Quantify:** If tickets grew 30% but headcount grew 10% → capacity gap
5. **Recommend (prioritized):**
   - **Short term:** Automate common support queries (FAQ, chatbots), add temp capacity, prioritize high-value tickets
   - **Medium term:** Hire to match growth, improve processes, invest in tools
   - **Long term:** Build scalable systems (self-service, predictive capacity planning)
6. **Measure:** SLA compliance, ticket resolution time, on-time delivery

**Interview insight:** "Growth outpacing operations is a classic scaling problem. I'd quantify the capacity gap, then sequence fixes: quick wins (automation, prioritization) first, then structural fixes (hiring, systems). The goal is to keep quality stable while scaling."

#### Practice
**Basic (3–5):**
1. What is the structure of a BizOps case?
2. How do you diagnose a scaling problem?
3. What KPIs would you track for a growing business?
4. How do you prioritize improvements?
5. What is a guesstimate?

**Intermediate (3–5):**
6. "A business is growing but operations can't keep up. Diagnose and fix."
7. "A KPI fell 20%. Investigate."
8. "How would you reduce costs without breaking the business?"
9. "Design an operations plan for a new business unit."
10. "How do you measure the impact of a process change?"

**Interview-Level (5+):**
11. "A company's margins are falling. Diagnose."
12. "How would you scale a support team 3x in 12 months?"
13. "How do you decide between hiring and automation?"
14. "A key process is failing. What's your response?"
15. "Use your civil experience to describe a scaling challenge you faced."

#### Common Mistakes
- **Jumping** to solutions without quantifying the gap
- **Not** sequencing recommendations (quick wins vs structural)
- **Ignoring** cost and feasibility
- **Forgetting** to define success metrics
- **Not** using your civil background as a differentiator

#### Completion Criterion
✅ Can structure any BizOps case
✅ Can diagnose scaling, cost, and efficiency problems
✅ Can sequence recommendations by impact and feasibility
✅ Can translate civil experience into BizOps stories

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | Build a KPI tree for an e-commerce business. A KPI fell 20% — structure your investigation. | KPI Management | 25 |
| 2 | Map a customer onboarding process (5 days → 2 days goal). Identify the bottleneck and recommend improvements. | Process Design | 25 |
| 3 | Sales wants 20% discounts; Finance wants to protect margins. How do you align them? Quantify the trade-off. | Coordination | 25 |
| 4 | "A business is growing 30% but operations can't keep up. Diagnose and fix." | Case Study | 15 |
| 5 | Explain leading vs lagging indicators and RICE prioritization. | Fundamentals | 10 |
| | | **Total** | **100** |

---

## Company Navigation

| Company | What They Test | Focus |
|:--------|:---------------|:------|
| **Google** | Analytical, cross-functional | KPI + Cases |
| **Amazon** | Leadership principles, bar raiser | Behavioral + KPI |
| **Flipkart** | Ownership, bias for action | Behavioral + Cases |
| **Uber/Swiggy** | Ops + growth | Scaling + Metrics |
| **Paytm/PhonePe** | Ops + fintech | KPI + Process |
| **Razorpay** | Ops + product | Process + Metrics |
| **Deloitte/Accenture** | Case + analytical | Cases + Frameworks |
| **Tata/Reliance** | Corporate ops | KPI + Coordination |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| BizOps Overview | [biz-ops-overview.md](biz-ops-overview.md) |
| Operations | [operations-overview.md](../operations/operations-overview.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Strategy | [strategy-overview.md](../strategy/strategy-overview.md) |
| Case Frameworks | [case-frameworks.md](../consulting/case-frameworks.md) |
| Rapid Revision | [biz-ops-rapid-revision.md](biz-ops-rapid-revision.md) |

---

*Business operations is where strategy becomes daily reality. It's about making things work, at scale, every day.*
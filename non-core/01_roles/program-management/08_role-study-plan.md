# Program / Project Management — Role Study Plan

## Role Overview

The Program/Project Management role targets **project/program manager positions** at tech companies (Amazon, Google, Microsoft, Flipkart), **consulting firms** (Deloitte, Accenture, PwC), **infrastructure/EPC companies** (L&T, Tata Projects, AECOM), and **banks/fintech** (Barclays, HSBC). The role covers project planning, scheduling, risk management, stakeholder coordination, and delivery execution. Civil engineers are a natural fit because they have **real, hands-on project management experience** from site work, thesis, and team projects.

**Who targets this role:** B.Tech/M.Tech graduates with strong planning and coordination skills, students with site/internship experience, GATE qualifiers interested in program management, students who led team projects or managed deadlines.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Project Planning & Scheduling (CPM/PERT)

#### Why This Matters
Every PM interview tests your ability to plan, sequence, and schedule work. Critical Path Method (CPM) and PERT are the quantitative backbone of project management — and they're directly derived from your civil engineering training.

#### What to Learn
- [ ] Project lifecycle: Initiation → Planning → Execution → Monitoring → Closure
- [ ] Work Breakdown Structure (WBS): Decomposing work into deliverables
- [ ] Activity sequencing: Predecessors, successors, dependencies
- [ ] Critical Path Method (CPM): Forward pass, backward pass, float/slack
- [ ] PERT: Optimistic (O), Most Likely (M), Pessimistic (P) estimates
- [ ] Expected time: TE = (O + 4M + P) / 6
- [ ] Variance: σ² = [(P - O) / 6]²
- [ ] Gantt charts and milestone planning
- [ ] Resource leveling and allocation

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pgm-overview.md`](pgm-overview.md) | Planning, scheduling, critical path | Full |
| [`infrastructure-engineering-management.md`](../../core/infrastructure/infrastructure-engineering-management.md) | PM fundamentals, construction mgmt | Full |

#### Worked Example
**Problem:** A small project has the following activities:

| Activity | Predecessor | Duration (days) |
|:---------|:------------|:---------------:|
| A | — | 4 |
| B | A | 6 |
| C | A | 5 |
| D | B, C | 7 |
| E | D | 3 |

Find the critical path, project duration, and float for each activity.

**Solution:**
1. **Draw the network and compute forward pass (ES, EF):**
   - A: ES=0, EF=4
   - B: ES=4, EF=10
   - C: ES=4, EF=9
   - D: ES=max(10,9)=10, EF=17
   - E: ES=17, EF=20

2. **Backward pass (LS, LF):**
   - E: LF=20, LS=17
   - D: LF=17, LS=10
   - C: LF=10, LS=5
   - B: LF=10, LS=4
   - A: LF=min(4,5)=4, LS=0

3. **Compute float (LS - ES):**
   - A: 0-0 = **0** (critical)
   - B: 4-4 = **0** (critical)
   - D: 10-10 = **0** (critical)
   - E: 17-17 = **0** (critical)
   - C: 5-4 = **1 day** (non-critical)

4. **Critical path:** A → B → D → E
5. **Project duration:** **20 days**

**Interview insight:** "The critical path is A→B→D→E at 20 days. Activity C has 1 day of float, so it can slip by a day without delaying the project. Any delay on the critical path directly extends the project — that's where I'd focus risk mitigation."

#### Practice
**Basic (3–5):**
1. What is the critical path? Why is it important?
2. Define float/slack. What does zero float mean?
3. What is the difference between CPM and PERT?
4. What is a Work Breakdown Structure (WBS)?
5. Compute TE for an activity with O=4, M=6, P=14.

**Intermediate (3–5):**
6. Given a network, compute ES, EF, LS, LF, and float for all activities.
7. A project has 3 parallel paths. Which is critical and why?
8. How do you crash a project? What are the trade-offs?
9. Compute the probability of completing a project in X days using PERT (Z-score).
10. How do you handle resource conflicts on the critical path?

**Interview-Level (5+):**
11. A critical-path activity is delayed by 5 days. What do you do?
12. How do you balance scope, time, and cost (triple constraint)?
13. Explain the difference between a project and a program.
14. How do you manage a project with unclear requirements?
15. How would you use your civil engineering experience to plan a construction project?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Walk me through how you'd plan a project | Structured planning |
| What's the critical path? | Technical fundamentals |
| A task is behind schedule — what do you do? | Judgment, prioritization |
| How do you estimate task durations? | Estimation skill |
| How do you handle scope creep? | Scope management |

#### Common Mistakes
- **Confusing** float with delay — float is available slack, not a buffer to waste
- **Forgetting** that multiple critical paths can exist
- **Not** accounting for dependencies when estimating
- **Ignoring** resource constraints when building the schedule
- **Treating** PERT and CPM as interchangeable — PERT handles uncertainty, CPM assumes deterministic durations

#### Completion Criterion
✅ Can compute critical path, float, and project duration for any network
✅ Can build a WBS and Gantt chart
✅ Can apply PERT for uncertain durations
✅ Can explain the triple constraint and scope management

---

### Topic 2: Risk Management

#### Why This Matters
Risk management is a core PM competency. Recruiters test your ability to identify, assess, and mitigate risks — a skill you've practiced in civil engineering (weather delays, material shortages, safety risks).

#### What to Learn
- [ ] Risk management process: Identify → Assess → Mitigate → Monitor
- [ ] Risk register: Risk ID, description, likelihood, impact, owner, response
- [ ] Qualitative risk analysis: Probability × Impact matrix
- [ ] Quantitative risk analysis: Expected Monetary Value (EMV), decision trees
- [ ] Risk responses: Avoid, Transfer, Mitigate, Accept
- [ ] Contingency planning and reserves
- [ ] Risk vs issue: A risk is future, an issue is current
- [ ] Stakeholder risk communication

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pgm-overview.md`](pgm-overview.md) | Risk management, escalation | Full |
| [`risk-overview.md`](../risk/risk-overview.md) | Risk frameworks | Reference |

#### Worked Example
**Problem:** A construction project has identified the following risks. Build a risk register and prioritize them.

| Risk | Likelihood (1-5) | Impact (1-5) |
|:-----|:----------------:|:------------:|
| Weather delay (monsoon) | 4 | 4 |
| Material price increase | 3 | 5 |
| Labor shortage | 3 | 3 |
| Design change request | 2 | 4 |
| Safety incident | 2 | 5 |

**Solution:**
1. **Compute risk score = Likelihood × Impact:**
   - Weather delay: 4 × 4 = **16** (High)
   - Material price increase: 3 × 5 = **15** (High)
   - Labor shortage: 3 × 3 = **9** (Medium)
   - Design change: 2 × 4 = **8** (Medium)
   - Safety incident: 2 × 5 = **10** (Medium-High)

2. **Prioritize:** Weather delay (16) > Material price (15) > Safety (10) > Labor (9) > Design change (8)

3. **Define responses:**
   - Weather delay → **Mitigate**: Schedule critical outdoor work before monsoon; add contingency buffer
   - Material price → **Transfer**: Fixed-price contracts with suppliers; hedge
   - Safety → **Mitigate**: Safety training, PPE enforcement, audits
   - Labor shortage → **Mitigate**: Cross-train workers, maintain labor pool
   - Design change → **Accept/Control**: Change-control process, freeze design early

**Interview insight:** "I prioritize by risk score (probability × impact). The top two risks — weather and material cost — both score 15+, so I'd allocate contingency budget and schedule buffer to them first. I'd also assign an owner to each risk so accountability is clear."

#### Practice
**Basic (3–5):**
1. What is a risk register? What does it contain?
2. Define the four risk response strategies.
3. What is the difference between a risk and an issue?
4. How do you calculate a risk score?
5. What is Expected Monetary Value (EMV)?

**Intermediate (3–5):**
6. Build a 5×5 risk matrix and classify 5 risks.
7. Compute EMV for a risk with 30% probability and ₹10 lakh impact.
8. How do you decide how much contingency to hold?
9. A risk has materialized. What's your response?
10. How do you communicate risks to stakeholders?

**Interview-Level (5+):**
11. A key supplier might go bankrupt. What do you do?
12. How do you handle a risk that's outside your control?
13. Explain the difference between risk appetite and risk tolerance.
14. How do you balance risk-taking and risk-avoidance in a project?
15. Use your civil experience to describe a risk you managed.

#### Common Mistakes
- **Confusing** risk score with priority — always consider both likelihood and impact
- **Forgetting** to assign owners and deadlines to risks
- **Treating** all risks equally — prioritize by score
- **Not** reviewing the risk register regularly
- **Ignoring** positive risks (opportunities)

#### Completion Criterion
✅ Can build and prioritize a risk register
✅ Can apply the four risk response strategies
✅ Can compute EMV and use decision trees
✅ Can communicate risks to stakeholders

---

### Topic 3: Stakeholder Management & Communication

#### Why This Matters
PMs spend most of their time communicating. Stakeholder management — identifying, engaging, and aligning diverse parties — is tested heavily in behavioral and scenario rounds.

#### What to Learn
- [ ] Stakeholder identification: Who is affected by or affects the project?
- [ ] Stakeholder analysis: Power/interest grid
- [ ] Stakeholder engagement strategies: Manage closely, keep satisfied, keep informed, monitor
- [ ] Communication plan: What, when, how, to whom
- [ ] Status reporting: Progress, risks, issues, decisions
- [ ] Escalation management: When and how to escalate
- [ ] Conflict resolution: Negotiation, mediation
- [ ] Meeting management: Agenda, decisions, action items

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pgm-overview.md`](pgm-overview.md) | Stakeholder mgmt, communication | Full |
| [`behavioral.md`](../common/behavioral.md) | STAR stories, communication | Full |

#### Worked Example
**Problem:** You're managing a metro station construction project. Identify the key stakeholders and classify them using a power/interest grid.

**Solution:**
1. **Identify stakeholders:**
   - Government authority (funding, approvals)
   - Local community (affected by construction)
   - Contractor teams (execution)
   - Design consultants (technical)
   - Commuters (end users)
   - Environmental regulators (compliance)

2. **Power/Interest Grid:**
   | Stakeholder | Power | Interest | Strategy |
   |:------------|:-----:|:--------:|:---------|
   | Government authority | High | High | **Manage closely** |
   | Environmental regulators | High | Medium | **Keep satisfied** |
   | Local community | Low | High | **Keep informed** |
   | Contractor teams | Medium | High | **Manage closely** |
   | Design consultants | Medium | Medium | **Keep informed** |
   | Commuters | Low | Medium | **Monitor** |

3. **Communication plan:**
   - Government: Monthly progress + approval reports
   - Community: Town halls, grievance channel, noise/dust mitigation updates
   - Contractors: Weekly site meetings, daily stand-ups
   - Regulators: Compliance reports, environmental monitoring data

**Interview insight:** "I classify stakeholders by power and interest to decide how much attention each needs. The government authority and contractors get the most engagement because they have both high power and high interest. The community has low power but high interest — I keep them informed to avoid resistance and delays."

#### Practice
**Basic (3–5):**
1. What is stakeholder management?
2. Explain the power/interest grid.
3. What is a communication plan?
4. How do you handle a difficult stakeholder?
5. When should you escalate an issue?

**Intermediate (3–5):**
6. Two stakeholders want different things. How do you align them?
7. How do you communicate bad news to a stakeholder?
8. Design a communication plan for a project.
9. How do you manage a remote or distributed team?
10. A stakeholder keeps changing requirements. What do you do?

**Interview-Level (5+):**
11. A senior stakeholder disagrees with your recommendation. What do you do?
12. How do you handle a stakeholder who's not engaged?
13. Describe a time you managed a conflict between teams.
14. How do you build trust with stakeholders?
15. How do you manage expectations when scope must be cut?

#### Common Mistakes
- **Focusing** only on high-power stakeholders and ignoring the community
- **Not** documenting decisions and action items
- **Over-communicating** or under-communicating — no clear cadence
- **Escalating** too early or too late
- **Assuming** stakeholders know what you know — over-index on clarity

#### Completion Criterion
✅ Can identify and classify stakeholders using power/interest grid
✅ Can build a communication plan
✅ Can handle conflicts and escalations
✅ Can manage stakeholder expectations

---

### Topic 4: Agile, Scrum & Delivery Execution

#### Why This Matters
Modern PM roles (especially in tech) use Agile/Scrum. Even if you're targeting infrastructure, understanding Agile shows you can adapt to modern delivery methods.

#### What to Learn
- [ ] Waterfall vs Agile: When to use each
- [ ] Scrum roles: Product Owner, Scrum Master, Development Team
- [ ] Scrum artifacts: Product backlog, sprint backlog, increment
- [ ] Scrum events: Sprint planning, daily stand-up, sprint review, retrospective
- [ ] Kanban: Continuous flow, WIP limits
- [ ] Agile metrics: Velocity, burndown chart, cycle time
- [ ] User stories and acceptance criteria
- [ ] Definition of Done (DoD)

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pgm-overview.md`](pgm-overview.md) | Agile/Scrum basics | Reference |
| [`tech-overview.md`](../technology/tech-overview.md) | SDLC, Agile concepts | Reference |

#### Worked Example
**Problem:** A software team has a product backlog of 40 story points. Their velocity is 8 story points per sprint (2 weeks). How many sprints are needed? If a stakeholder adds 12 more points, how does the timeline change?

**Solution:**
1. **Initial sprints needed:** 40 / 8 = **5 sprints** = 10 weeks
2. **After adding 12 points:** (40 + 12) / 8 = 52 / 8 = **6.5 sprints** ≈ 7 sprints = 14 weeks
3. **Impact:** +2 sprints = **+4 weeks** (or ~40% longer)

**Interview insight:** "Adding 12 story points (30% more scope) extends the timeline by 40% because velocity is fixed. This is why I'd push back on scope additions or negotiate a trade-off — either reduce existing scope, increase team capacity, or extend the timeline. I'd present this trade-off clearly to the stakeholder."

#### Practice
**Basic (3–5):**
1. What is the difference between Waterfall and Agile?
2. What are the three Scrum roles?
3. What is a sprint? How long is it typically?
4. What is a product backlog?
5. What is velocity?

**Intermediate (3–5):**
6. What is a burndown chart? How do you read it?
7. What is the Definition of Done?
8. How do you prioritize a backlog (MoSCoW, RICE)?
9. What is a retrospective? Why is it important?
10. How do you handle changing requirements in a sprint?

**Interview-Level (5+):**
11. When would you choose Waterfall over Agile?
12. How do you estimate story points?
13. A sprint is at risk of not completing. What do you do?
14. How do you scale Agile to a large program (SAFe)?
15. How does Agile apply to non-software projects (e.g., construction)?

#### Common Mistakes
- **Assuming** Agile is always better — Waterfall suits well-defined, regulated projects
- **Confusing** velocity with productivity — it's a planning metric
- **Skipping** retrospectives — they're where improvement happens
- **Not** having a clear Definition of Done
- **Treating** the backlog as fixed — it's meant to be reprioritized

#### Completion Criterion
✅ Can explain Waterfall vs Agile and when to use each
✅ Can describe Scrum roles, artifacts, and events
✅ Can read a burndown chart and use velocity for planning
✅ Can prioritize a backlog using a framework

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | A project has activities A(3d), B(A,5d), C(A,4d), D(B,C,6d), E(D,2d). Compute ES/EF/LS/LF, float, critical path, and project duration. | Scheduling | 25 |
| 2 | Build a risk register for a bridge construction project with 5 risks. Score, prioritize, and define responses. | Risk Management | 25 |
| 3 | Classify 6 stakeholders of a metro project using a power/interest grid and design a communication plan. | Stakeholder Mgmt | 25 |
| 4 | A team's velocity is 6 points/sprint. Backlog is 30 points. A stakeholder adds 9 points. How many sprints now? Show the trade-off you'd present. | Agile | 15 |
| 5 | Explain the triple constraint. A project is over budget — what are your options? | Delivery | 10 |
| | | **Total** | **100** |

---

## Company Navigation

| Company | What They Test | Focus |
|:--------|:---------------|:------|
| **Amazon** | Leadership principles, bar raiser, delivery | Behavioral + Agile |
| **Google** | Googleyness, analytical, project scenarios | Behavioral + Scheduling |
| **Microsoft** | Growth mindset, collaboration | Behavioral + Stakeholder |
| **Flipkart** | Ownership, bias for action | Behavioral + Delivery |
| **Deloitte/Accenture** | Case + behavioral | Case + Stakeholder |
| **L&T/Tata Projects** | Technical + site experience | Scheduling + Risk |
| **AECOM** | Technical + PM methodology | CPM + Risk |
| **Barclays/HSBC** | Analytical + behavioral | Scheduling + Stakeholder |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Program Mgmt Overview | [pgm-overview.md](pgm-overview.md) |
| Operations | [operations-overview.md](../operations/operations-overview.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Behavioral Prep | [behavioral.md](../common/behavioral.md) |
| Infrastructure/PM | [infrastructure-engineering-management.md](../../core/infrastructure/infrastructure-engineering-management.md) |
| Rapid Revision | [pgm-rapid-revision.md](pgm-rapid-revision.md) |

---

*Program management is the most natural non-core transition for Civil engineers. Your project experience is real, valuable, and directly relevant.*

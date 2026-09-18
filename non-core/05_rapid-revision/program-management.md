# Program / Project Management — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core formulas, frameworks, and quick-fire Q&A for program/project management interviews.

---

## Framework 1: Project Planning & Scheduling

### Project Lifecycle
```
Initiation → Planning → Execution → Monitoring & Control → Closure
```

### Critical Path Method (CPM)

| Term | Meaning |
|:-----|:--------|
| **ES** | Earliest Start |
| **EF** | Earliest Finish = ES + Duration |
| **LS** | Latest Start |
| **LF** | Latest Finish |
| **Float/Slack** | LS - ES = LF - EF (zero = critical) |

```
Forward Pass:  EF = ES + Duration;  ES = max(EF of predecessors)
Backward Pass: LS = LF - Duration;  LF = min(LS of successors)
Critical Path:  Path with zero float → determines project duration
```

### PERT (Uncertain Durations)

```
Expected Time:  TE = (O + 4M + P) / 6
Variance:       σ² = [(P - O) / 6]²
Probability:    Z = (Target - TE) / σ  → use Z-table
```

### Work Breakdown Structure (WBS)
```
Project → Deliverables → Work Packages → Activities
Decompose work into manageable, estimable units.
```

---

## Framework 2: Risk Management

### Risk Management Process
```
Identify → Assess (Likelihood × Impact) → Mitigate → Monitor
```

### Risk Score
```
Risk Score = Likelihood (1-5) × Impact (1-5)
Score ≥ 15 = High priority
```

### Four Risk Response Strategies
| Strategy | When to Use |
|:---------|:------------|
| **Avoid** | Eliminate the risk entirely |
| **Transfer** | Shift to third party (insurance, contracts) |
| **Mitigate** | Reduce likelihood or impact |
| **Accept** | Low priority, retain with contingency |

### Expected Monetary Value (EMV)
```
EMV = Probability × Impact
```

### Risk vs Issue
```
Risk  = Future uncertainty (may or may not happen)
Issue = Current problem (already happening)
```

---

## Framework 3: Stakeholder Management & Communication

### Power/Interest Grid
| Power \ Interest | Low Interest | High Interest |
|:-----------------|:-------------|:--------------|
| **High Power** | Keep Satisfied | **Manage Closely** |
| **Low Power** | Monitor | Keep Informed |

### Communication Plan
```
What → When → How → To Whom
(Status reports, meetings, escalations, decisions)
```

### Escalation Rules
- Escalate when: risk is high, decision needed, blocked, or out of your authority
- Escalate with: context, options, and a recommendation (not just the problem)

---

## Framework 4: Agile & Scrum

### Waterfall vs Agile
| Aspect | Waterfall | Agile |
|:-------|:----------|:------|
| Phases | Sequential | Iterative |
| Requirements | Fixed up front | Evolving |
| Delivery | End of project | Each sprint |
| Best for | Regulated, well-defined | Fast-changing, software |

### Scrum Roles
```
Product Owner  = Represents user/business needs, prioritizes backlog
Scrum Master   = Facilitates process, removes blockers
Dev Team       = Delivers the increment
```

### Scrum Events
```
Sprint Planning → Daily Stand-up → Sprint Review → Retrospective
```

### Key Metrics
```
Velocity      = Story points completed per sprint
Burndown      = Remaining work vs time
Cycle Time    = Time from start to completion of a task
```

### Backlog Prioritization (MoSCoW)
```
Must Have → Should Have → Could Have → Won't Have
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is the critical path?**
A: The sequence of activities that determines the shortest possible project duration. Activities on the critical path have zero float — any delay directly extends the project.

**Q2: What's the difference between a project and a program?**
A: A project is a single, time-bound effort with a specific deliverable. A program is a group of related projects managed together to achieve a broader strategic objective.

**Q3: How do you handle scope creep?**
A: Use a change-control process — any scope change goes through formal review of impact on time, cost, and quality before approval. I'd present the trade-off to the stakeholder and get sign-off.

**Q4: What is float/slack?**
A: The amount of time an activity can be delayed without affecting the project completion date. Zero float means the activity is on the critical path.

**Q5: How do you estimate task durations?**
A: Use historical data, expert judgment, and three-point estimation (PERT: O+4M+P)/6. I'd break work into small tasks and account for dependencies and resource availability.

**Q6: What's the difference between a risk and an issue?**
A: A risk is a future uncertainty that may or may not happen. An issue is a current problem already impacting the project. Risks are managed proactively; issues are resolved reactively.

**Q7: How do you prioritize risks?**
A: By risk score = Likelihood × Impact. High-score risks get contingency budget and active mitigation; low-score risks are accepted and monitored.

**Q8: When would you use Waterfall over Agile?**
A: When requirements are well-defined and unlikely to change, or in regulated industries (construction, aerospace) where documentation and sequential approval are required.

**Q9: How does a civil engineering background help in PM?**
A: Real site/project experience, understanding of scheduling (CPM), risk management (weather, materials, safety), stakeholder coordination (contractors, authorities), and delivering under deadlines.

**Q10: How do you measure project success?**
A: On-time, within budget, meeting scope/quality requirements, and stakeholder satisfaction. I'd track schedule variance, cost variance, and quality metrics throughout.

---

## Last-Minute Checklist

### Before Any PM Interview
- [ ] 3-4 STAR stories (leadership, delivery, risk, conflict)
- [ ] One project you can walk through end-to-end (planning → delivery)
- [ ] Know the critical path of a sample project cold
- [ ] Your "Why PM?" answer (link to civil engineering experience)

### Must-Know Formulas
- [ ] TE = (O + 4M + P) / 6
- [ ] σ² = [(P - O) / 6]²
- [ ] Risk Score = Likelihood × Impact
- [ ] EMV = Probability × Impact
- [ ] Float = LS - ES

### Behavioral Prep
- [ ] "Tell me about a time you managed a project" (STAR)
- [ ] "Describe a time you handled a risk" (STAR)
- [ ] "Tell me about a conflict you resolved" (STAR)
- [ ] "How do you handle a missed deadline?" (STAR)

---

## Cross-Links

**Program Mgmt:**
→ [Program Mgmt Overview](pgm-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Operations Overview](../operations/operations-overview.md) — Operations role
→ [Risk Rapid Revision](../risk/risk-rapid-revision.md) — Risk management
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md) — STAR stories

---

*Last updated: 2026-09-04*

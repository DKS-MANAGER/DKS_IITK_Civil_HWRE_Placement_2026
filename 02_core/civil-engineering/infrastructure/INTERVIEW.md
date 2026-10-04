# Infrastructure Engineering & Management — Interview Questions & Answers

> **Placement Priority:** P0 — Required for PM/consulting roles (L&T, AECOM, Tata Projects, NHAI, IRCON, NBCC)
> **Canonical Study:** [`infrastructure-engineering-management.md`](infrastructure-engineering-management.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 15 questions across 6 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is the critical path method (CPM)?**
   - A scheduling technique that identifies the longest path of dependent activities (zero float) — determines the minimum project duration.

2. **What is the difference between CPM and PERT?**
   - CPM: deterministic durations, used for construction. PERT: probabilistic (three-point estimates), used for R&D/uncertain projects.

3. **What is total float?**
   - The time an activity can be delayed without delaying the project: $TF = LS - ES = LF - EF$.

4. **What is NPV?**
   - Net Present Value: the sum of discounted cash flows minus initial investment. NPV > 0 → accept.

5. **What is the Hybrid Annuity Model (HAM)?**
   - India-specific PPP: government pays 40% during construction + annuity over the concession period; private bears the rest.

---

## B. WHY Questions

1. **Why is the critical path important?**
   - Any delay on the critical path delays the entire project — it focuses management attention on the activities that matter most.

2. **Why use PERT for uncertain projects?**
   - PERT incorporates three-point estimates (optimistic, most likely, pessimistic) to quantify uncertainty and compute completion probability.

3. **Why is DSCR important for lenders?**
   - It measures the project's ability to service debt from operating income — DSCR > 1.2 indicates the project can repay loans.

4. **Why is WBS the foundation of project planning?**
   - It decomposes scope into manageable work packages, enabling accurate estimation, scheduling, and responsibility assignment.

---

## C. WHAT-IF Questions

1. **What if an activity on the critical path is delayed?**
   - The project duration increases by the delay amount — unless crashed or fast-tracked.

2. **What if NPV is negative?**
   - Reject the project, or renegotiate costs/revenues — the project destroys value at the given discount rate.

3. **What if DSCR < 1.2?**
   - The project may default on debt — lenders may require higher equity, lower debt, or better revenue projections.

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| CPM | PERT | Deterministic vs probabilistic |
| Total float | Free float | Project delay vs successor delay |
| BOT | HAM | Full private finance vs 40% govt + annuity |
| Design-Bid-Build | Design-Build | Sequential vs integrated |
| NPV | IRR | Value in ₹ vs rate of return |

---

## E. Numerical Questions

1. **Find project duration** for A(5) → C(4) → D(2). → 11 days
2. **Find $t_e$** for $t_o = 4$, $t_m = 6$, $t_p = 14$. → 7 days
3. **Find NPV** for $C_0 = 1000$, CF = 300 × 5 yr, r = 10%. → 137.3 lakh
4. **Find BCR** for PV benefits 1500, PV costs 1200. → 1.25

---

## F. Rapid-Fire Questions

1. Critical path float? → Zero
2. PERT expected time? → $(t_o + 4t_m + t_p)/6$
3. NPV accept criterion? → > 0
4. BCR accept criterion? → > 1
5. DSCR threshold? → > 1.2
6. Contingency (CPWD)? → 3–5%
7. HAM govt share? → 40%
8. Plinth area accuracy? → ±15–20%

---

## High-Value Interview Answers

### High-Value Q1: "How do you manage a construction project schedule?"

**30-second answer:**
"First, develop a WBS to decompose scope. Then build a CPM network to identify the critical path and float. Use a Gantt chart for tracking. Monitor progress with earned value management (EVM) — comparing planned vs actual vs earned value. If the critical path slips, apply crashing (add resources) or fast-tracking (overlap activities)."

### High-Value Q2: "What is the difference between BOT and HAM?"

**30-second answer:**
"In BOT, the private partner fully finances, builds, operates, and transfers the asset — bearing most of the risk. In HAM (Hybrid Annuity Model), the government pays 40% of the project cost during construction and the remaining 60% as annuities over the concession period, reducing the private partner's financing burden and risk. HAM is India-specific for highways."

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`infrastructure-engineering-management.md`](infrastructure-engineering-management.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Transportation | [`../transportation/transportation-engineering.md`](../transportation/transportation-engineering.md) |
| Geotechnical | [`../geotechnical/geotechnical.md`](../geotechnical/geotechnical.md) |
| Structures | [`../structures/structures.md`](../structures/structures.md) |
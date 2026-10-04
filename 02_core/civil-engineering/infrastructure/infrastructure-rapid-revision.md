# Infrastructure Engineering & Management — Rapid Revision Sheet

> Last-minute cheat sheet for Infrastructure/PM and Construction Engineer interviews.

---

## Framework 1: Project Management (PMBOK)

### 10 Knowledge Areas
1. Integration, 2. Scope, 3. Schedule, 4. Cost, 5. Quality, 6. Resource, 7. Communications, 8. Risk, 9. Procurement, 10. Stakeholder

### 5 Process Groups
Initiation → Planning → Execution → Monitoring & Control → Closing

### CPM Scheduling

| Term | Definition |
|:-----|:-----------|
| ES | Earliest Start |
| EF | ES + Duration |
| LS | Latest Start |
| LF | LS + Duration |
| Total Float | LS - ES = LF - EF |
| Free Float | min(ES_j) - EF_i |
| Critical Path | Zero float (longest path) |

**Forward pass:** ES_j = max(EF_i), EF_j = ES_j + D_j
**Backward pass:** LF_i = min(LS_j), LS_i = LF_i - D_i

### PERT

$$t_e = \frac{t_o + 4t_m + t_p}{6}, \quad \sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$$

**Completion probability:** Z = (T_s - T_e)/√Σσ²_critical

### WBS
- Hierarchical decomposition of scope
- **100% rule:** Sum of children = 100% of parent scope

---

## Framework 2: Construction Delivery Methods

| Method | Description | Risk |
|:-------|:------------|:-----|
| Design-Bid-Build | Sequential: design → tender → build | Low private |
| Design-Build | Single entity design + construction | Moderate |
| EPC | Turnkey (Engineering, Procurement, Construction) | Low private |
| BOT | Build-Operate-Transfer | High private |
| BOOT | Build-Own-Operate-Transfer | Higher private |
| BOO | Build-Own-Operate (permanent) | Highest private |
| DBFO | Design-Build-Finance-Operate | Balanced |
| HAM | Hybrid Annuity (40% construction + annuity) | Balanced (India) |
| PMC | Project Management Consultancy | Third-party |

### Line of Balance (Repetitive Work)
$$T_{activity} = T_{start} + \frac{n}{R}$$

### Last Planner System (Lean)
- Master schedule → Pull plan → Make ready
- **PPC** = completed/planned × 100%, target ≥ 80-90%

### Compaction Control
$$\text{Relative Compaction} = \frac{\gamma_{d,field}}{\gamma_{d,max}} \times 100\%$$
- ≥ 95% Modified Proctor or ≥ 98% Standard Proctor

---

## Framework 3: Cost Estimation & Finance

### Estimate Types

| Type | Accuracy | Method |
|:-----|:---------|:-------|
| Plinth area | ±15-20% | Area × rate/m² |
| Cube rate | ±15% | Volume × rate/m³ |
| Approximate quantity | ±10-15% | Full wall/plinth × cost |
| Detailed (item rate) | ±5-8% | BOQ |
| Planned expenditure | ±3-5% | Actual quantities |

**Plinth area:** Cost = Plinth Area × Rate (₹/m²)
**Contingency:** 3-5% × estimated cost (CPWD)
**Escalation:** Current Rate = Base Rate × (Current WPI/Base WPI)

### Financial Metrics

| Metric | Formula | Decision |
|:-------|:--------|:---------|
| NPV | ΣCF_t/(1+r)^t | NPV > 0 → Accept |
| IRR | Rate where NPV = 0 | IRR > MARR → Accept |
| BCR | PV(Benefits)/PV(Costs) | BCR > 1 → Accept |
| Payback | Time to recover investment | Shorter = Better |
| DSCR | NOI/Debt Service | DSCR > 1.2 → Viable |

### PPP Models (India)
- **HAM:** Govt pays 40% during construction + annuity over concession
- **VGF:** Government grant to make PPP financially viable
- **BOT:** Private builds, operates, transfers

---

## Framework 4: Infrastructure Planning

### Key Indian Programs

| Program | Focus |
|:--------|:------|
| NIP | ₹111 lakh crore infrastructure investment |
| Smart Cities | 100 cities, technology-driven development |
| AMRUT | Urban water, sewerage, transport |
| Gati Shakti | Multi-modal infrastructure coordination |
| Bharatmala | 65,000 km highway development |

### Infrastructure Planning Framework
1. Demand assessment (travel demand, ridership)
2. Feasibility study (technical, financial, economic, environmental)
3. Route/alignment selection (GIS)
4. Funding (PPP, VGF, multilateral loans)
5. Detailed design
6. Construction (EPC/DB)
7. Operations (fare, maintenance, safety)
8. Monitoring (KPIs)

---

## Quick-Fire Interview Answers

**Q1: What is the critical path?**
A: The critical path is the longest path through a project network with zero float. Any delay on the critical path delays the entire project. It determines the minimum project duration and is the focus of schedule management.

**Q2: What is the difference between CPM and PERT?**
A: CPM uses deterministic (single) duration estimates and is used for repetitive construction work. PERT uses three-point estimates (optimistic, most likely, pessimistic) and is used for uncertain, non-repetitive projects (R&D). CPM focuses on cost-time tradeoffs; PERT on time uncertainty.

**Q3: What is the difference between crashing and fast-tracking?**
A: Crashing adds resources to critical path activities to reduce duration (at increased cost). Fast-tracking performs activities in parallel that would normally be sequential (at increased risk). Crashing increases cost; fast-tracking increases risk.

**Q4: What is the 100% rule in WBS?**
A: The sum of child elements at any WBS level must equal 100% of the parent element's scope. This ensures no work is missing (under-scoping) or duplicated (over-scoping).

**Q5: What is the difference between EPC and BOT?**
A: EPC (Engineering, Procurement, Construction) is a turnkey contract where the contractor builds and hands over to the owner. BOT (Build-Operate-Transfer) involves the private party building, operating for a concession period, then transferring to the government. BOT includes operation and revenue risk; EPC does not.

**Q6: What is Viability Gap Funding (VGF)?**
A: VGF is a government grant that bridges the gap between project cost and the revenue a PPP project can generate. It makes financially unviable but socially desirable projects attractive to private investors. Common in highways, metro, and social infrastructure.

**Q7: What is the difference between NPV and IRR?**
A: NPV is the present value of cash flows minus initial investment (absolute value in ₹). IRR is the discount rate at which NPV = 0 (percentage return). NPV > 0 or IRR > MARR means accept. NPV is preferred for comparing projects; IRR can be misleading for mutually exclusive projects.

**Q8: What is the Last Planner System?**
A: LPS is a lean construction planning method. It uses a master schedule, pull planning (working backward from milestones), and a "make ready" process to remove constraints before committing work. It measures performance with PPC (Percent Planned Complete), targeting ≥ 80-90%.

**Q9: What is HAM in Indian highways?**
A: HAM (Hybrid Annuity Model) is a PPP model where the government pays 40% of project cost during construction and the remaining 60% as annuities over the concession period. It balances risk between government and private sector, making projects more bankable.

**Q10: What is the National Infrastructure Pipeline?**
A: NIP is India's ₹111 lakh crore infrastructure investment plan (2020-2025) across roads, railways, energy, urban, and digital infrastructure. It aims to boost economic growth, create jobs, and improve infrastructure quality through public and private investment.

---

## Last-Minute Checklist

- [ ] 10 PMBOK knowledge areas
- [ ] 5 process groups
- [ ] CPM forward/backward pass
- [ ] Critical path + float
- [ ] PERT three-point estimate
- [ ] WBS 100% rule
- [ ] Delivery methods (DBB, DB, EPC, BOT, HAM)
- [ ] Line of Balance formula
- [ ] Last Planner System + PPC
- [ ] Compaction control (≥95% Modified Proctor)
- [ ] Estimate types and accuracy
- [ ] Plinth area estimate + contingency
- [ ] NPV, IRR, BCR, DSCR
- [ ] PPP models + VGF
- [ ] NIP, Smart Cities, AMRUT, Gati Shakti

---

## Cross-Links

- [`infrastructure-engineering-management.md`](infrastructure-engineering-management.md) — Full subject reference
- [`role-study-plan.md`](role-study-plan.md) — Detailed study plan with worked examples
- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — Transport infrastructure
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Construction, compaction
- [`structures.md`](../structures/structures.md) — Structural integration

---

## References

- PMBOK Guide (PMI)
- CPWD Specifications
- NIP, Smart Cities, Gati Shakti documents
- IS 516, IS 1199, IS 2720, IS 2911, IS 5093
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

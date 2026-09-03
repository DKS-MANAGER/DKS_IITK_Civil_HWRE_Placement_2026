# Infrastructure Engineering & Management

## Scope

Infrastructure Engineering & Management bridges civil engineering with project management, construction management, urban planning, infrastructure finance, and public policy — covering the full lifecycle from planning and design through construction, operation, maintenance, and rehabilitation of civil infrastructure systems. Essential for consulting firms (L&T, AECOM, Tata Projects), PSU management roles (NHAI, IRCON, NBCC), and infrastructure finance.

> **Related topics:** [`structures.md`](../structures/structures.md) · [`transportation-engineering.md`](../transportation/transportation-engineering.md) · [`water-supply.md`](../../hwre/water_supply/water-supply.md) · [`geotechnical.md`](../geotechnical/geotechnical.md)

---

## 1. Project Management Fundamentals

### Project Management Knowledge Areas (PMI / PMBOK)

| # | Knowledge Area | Description |
|---|----------------|-------------|
| 1 | Integration | Coordinate all project elements |
| 2 | Scope | Define and control what is/isn't included |
| 3 | Schedule | Time planning, sequencing, and control |
| 4 | Cost | Estimating, budgeting, cost control |
| 5 | Quality | Quality planning, assurance, control |
| 6 | Resource | Human and material resource management |
| 7 | Communications | Information flow management |
| 8 | Risk | Risk identification, analysis, response |
| 9 | Procurement | Vendor management, contracts |
| 10 | Stakeholder | Engagement and expectation management |

### Project Life Cycle Phases

| Phase | Activities | Key Deliverables |
|-------|-----------|------------------|
| **Initiation** | Feasibility, project charter, stakeholder identification | Project charter, feasibility report |
| **Planning** | WBS, schedule, budget, risk plan | Project management plan |
| **Execution** | Construction, procurement, team management | Work packages, deliverables |
| **Monitoring & Control** | Progress tracking, change management, EVM | Status reports, change orders |
| **Closing** | Handover, lessons learned, documentation | Final report, punch list |

### Work Breakdown Structure (WBS)

**Principle:** Hierarchical decomposition of project scope into manageable work packages.

| Level | Example (Highway Project) |
|-------|--------------------------|
| 1 | Highway Construction Project |
| 2 | Design, Earthwork, Pavement, Bridges, Drainage |
| 3 | Topographic Survey, Geotech Investigation, Detailed Design |
| 4 | Soil testing, Borehole logging, Foundation recommendations |

**100% Rule:** Sum of child elements = 100% of parent element scope.

### Critical Path Method (CPM)

| Term | Definition |
|------|-----------|
| **ES** (Early Start) | Earliest time an activity can begin |
| **EF** (Early Finish) | ES + Duration |
| **LS** (Late Start) | Latest time without delaying project |
| **LF** (Late Finish) | LS + Duration |
| **Float / Slack** | LS − ES or LF − EF |
| **Critical Path** | Path with zero float (longest path) |

**Forward pass:**
$$ES_j = \max_{i}(EF_i) \quad \text{where } i \text{ is a predecessor of } j$$
$$EF_j = ES_j + D_j$$

**Backward pass:**
$$LF_i = \min_{j}(LS_j) \quad \text{where } j \text{ is a successor of } i$$
$$LS_i = LF_i - D_i$$

**Total Float:**
$$TF_i = LS_i - ES_i = LF_i - EF_i$$

**Free Float:**
$$FF_i = \min_{j}(ES_j) - EF_i$$

### PERT (Program Evaluation and Review Technique)

**Three-point estimate:**
$$t_e = \frac{t_o + 4t_m + t_p}{6}$$

$$\sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$$

Where:
- $t_o$ = optimistic time
- $t_m$ = most likely time
- $t_p$ = pessimistic time
- $t_e$ = expected time
- $\sigma$ = standard deviation

**Project completion probability:**
$$Z = \frac{T_s - T_e}{\sqrt{\sum \sigma^2_{\text{critical path}}}}$$

Where $T_s$ = scheduled time, $T_e$ = expected project duration.

### Gantt Chart vs Network Diagram

| Feature | Gantt Chart | Network Diagram (CPM) |
|---------|------------|----------------------|
| Shows | Timeline, dependencies | Logical relationships, critical path |
| Best for | Progress tracking, communication | Schedule optimization |
| Float visibility | Limited | Clear |

---

## 2. Construction Management

### Construction Methods

| Method | Description | Application |
|--------|-------------|-------------|
| **Traditional (Design-Bid-Build)** | Sequential: design → tender → build | Government projects |
| **Design-Build (DB)** | Single entity for design + construction | Fast-track projects |
| **EPC (Engineering, Procurement, Construction)** | Turnkey delivery | Industrial, infrastructure |
| **BOT (Build-Operate-Transfer)** | Private build + operate + government handover | Toll roads, power |
| **PMC (Project Management Consultancy)** | Third-party project management | Large, complex projects |
| **Construction Management at Risk** | CM as advisor during design, then builder | Complex facilities |

### Construction Planning Techniques

**Line of Balance (LOB):**

| Feature | Description |
|---------|-------------|
| Used for | Repetitive activities (high-rise floors, road segments) |
| Output | Steady production rate, predictable completion |
| Formula | $T_{activity} = T_{start} + \frac{n}{R}$ where $R$ = production rate, $n$ = unit number |

**Last Planner System (Lean Construction):**

| Element | Description |
|---------|-------------|
| Master schedule | Phase plan (look-ahead) |
| Pull plan | Weekly work plan from milestones |
| Make ready | Remove constraints before committing |
| Percent planned complete (PPC) | $\frac{\text{completed tasks}}{\text{planned tasks}} \times 100\%$ |
| Target PPC | ≥ 80–90% |

### Construction Equipment Selection

| Equipment | Application | Key Parameter |
|-----------|-------------|---------------|
| Bulldozer | Earthmoving, clearing | Blade capacity, horsepower |
| Excavator | Digging, trenching | Bucket capacity (m³) |
| Loader | Material handling | Bucket size, dump height |
| Crane | Lifting, placing | Capacity (tonnes) × radius |
| Compactor | Soil/pavement compaction | Weight, frequency, amplitude |
| Paver | Asphalt/concrete paving | Width, screed type |
| Transit mixer | Concrete transport | Capacity (m³) |
| Concrete pump | Concrete placement | Reach, output (m³/hr) |

### Soil Compaction

**Compaction control:**
$$\text{Relative Compaction} = \frac{\gamma_{d,\text{field}}}{\gamma_{d,\text{max}}} \times 100\%$$

Typical specification: ≥ 95% Modified Proctor or ≥ 98% Standard Proctor.

**Proctor test (ASTM D1557):**
- Optimum Moisture Content (OMC): water content at max dry density
- Modified Proctor: 2,700 kg rammer, 450 mm drop, 25 blows/layer
- Standard Proctor: 2,500 kg rammer, 300 mm drop, 25 blows/layer

### Quality Control in Construction

| Test | Standard | Application |
|------|----------|-------------|
| Concrete cube test | IS 516 (Part 1) | Compressive strength (28 days) |
| Concrete slump test | IS 1199 | Workability |
| Concrete rebound hammer | IS 13311 (Part 2) | In-situ strength estimation |
| Pile load test | IS 2911 | Foundation capacity |
| Proctor compaction | IS 2720 (Part 8) | Soil compaction control |
| CBR test | IS 2720 (Part 16) | Subgrade strength |
| Plate bearing test | IS 5093 | Subgrade modulus |
| Core cutting test | IS 1199 | Concrete density |

---

## 3. Construction Cost Estimation

### Types of Estimates

| Type | Accuracy | When Used | Method |
|------|----------|-----------|--------|
| **Plinth area estimate** | ±15–20% | Preliminary | Plinth area × rate/m² |
| **Cube rate estimate** | ±15% | Preliminary | Built-up volume × rate/m³ |
| **Approximate quantity** | ±10–15% | Preliminary | Full wall/plinth area × cost |
| **Detailed estimate (item rate)** | ±5–8% | Tender | BOQ, measurement of each item |
| **Planned expenditure** | ±3–5% | Execution | Actual quantities × rates |

### Plinth Area Estimate

$$\text{Estimated Cost} = \text{Plinth Area} \times \text{Plinth Area Rate (₹/m²)}$$

| Building Type | Typical Rate (₹/m², 2024) |
|---------------|---------------------------|
| Residential (basic) | 15,000–25,000 |
| Residential (premium) | 25,000–50,000 |
| Commercial | 20,000–40,000 |
| Institutional | 18,000–35,000 |
| Industrial | 12,000–25,000 |

### Unit Rate Method (Detailed Estimate)

| Component | Typical % of Total Cost |
|-----------|------------------------|
| Earthwork | 3–5% |
| Concrete work | 15–25% |
| Reinforcement | 15–20% |
| Masonry | 8–12% |
| Plastering & finishing | 10–15% |
| Doors & windows | 8–12% |
| Flooring | 5–10% |
| Plumbing & electrical | 8–12% |
| Painting | 3–5% |

### Bill of Quantities (BOQ)

| Item | Description | Unit | Quantity | Rate | Amount |
|------|-------------|------|----------|------|--------|
| 1 | Earthwork in excavation | m³ | 500 | ₹250 | ₹1,25,000 |
| 2 | PCC 1:4:8 | m³ | 50 | ₹4,500 | ₹2,25,000 |
| 3 | RCC M25 | m³ | 120 | ₹6,500 | ₹7,80,000 |
| 4 | Steel (Fe500D) | kg | 15,000 | ₹55 | ₹8,25,000 |
| ... | ... | ... | ... | ... | ... |
| **Total** | | | | | **₹XX,XX,XXX** |

### Cost Escalation & Contingency

**Contingency (CPWD norms):**
$$\text{Contingency} = 3\text{–}5\% \times \text{Estimated Cost}$$

**Rate escalation:**
$$\text{Escalated Cost} = \text{Base Cost} \times \left(1 + \frac{\text{Price Index}_2}{\text{Price Index}_1}\right)$$

**Plinth area rate escalation (IS 2014 revision):**
$$\text{Current Rate} = \text{Base Rate} \times \frac{\text{Current WPI}}{\text{Base WPI}}$$

Where WPI = Wholesale Price Index.

---

## 4. Infrastructure Finance

### Public-Private Partnership (PPP) Models

| Model | Description | Risk Sharing |
|-------|-------------|-------------|
| **BOT (Build-Operate-Transfer)** | Private builds, operates, transfers to govt | High private risk |
| **BOOT (Build-Own-Operate-Transfer)** | Like BOT but private owns during concession | Higher private risk |
| **BOO (Build-Own-Operate)** | Private builds, owns, operates permanently | Highest private risk |
| **DBFO (Design-Build-Finance-Operate)** | Private finances the project | Balanced |
| **Concession** | Govt grants right to operate existing asset | Moderate private |
| **EPC (Turnkey)** | Private builds, hands over to govt | Low private risk |
| **OM&M (Operations, Maintenance & Management)** | Private manages existing asset | Low private risk |
| **HAM (Hybrid Annuity Model)** | Govt pays 40% during construction + annuity | Balanced (India-specific) |

### Financial Metrics

| Metric | Formula | Decision Rule |
|--------|---------|---------------|
| **NPV** | $\sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$ | NPV > 0 → Accept |
| **IRR** | Rate where NPV = 0 | IRR > MARR → Accept |
| **BCR** | $\frac{\text{PV of Benefits}}{\text{PV of Costs}}$ | BCR > 1 → Accept |
| **Payback Period** | Time to recover initial investment | Shorter = Better |
| **DSCR** | $\frac{\text{Net Operating Income}}{\text{Debt Service}}$ | DSCR > 1.2 → Viable |

**NPV calculation:**
$$NPV = -C_0 + \sum_{t=1}^{n} \frac{R_t - E_t}{(1+r)^t}$$

Where $C_0$ = initial investment, $R_t$ = revenue, $E_t$ = expenses, $r$ = discount rate.

**IRR (iterative):**
$$0 = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$

### Toll Revenue & Viability Gap Funding (VGF)

| Concept | Description |
|---------|-------------|
| **VGF** | Government grant to make PPP financially viable |
| **Toll rate determination** | Based on traffic study, construction cost, concession period |
| **Traffic risk** | Lower than projected → revenue shortfall |
| **Construction risk** | Cost overrun, delay |
| **Concession period** | Typically 15–30 years for highways |

### DBFOT Model (Highways)

| Parameter | Typical Value (India) |
|-----------|----------------------|
| Concession period | 15–30 years |
| Construction period | 2–4 years |
| Annual growth rate (traffic) | 5–8% |
| O&M cost | 1.5–3% of project cost/year |
| Discount rate | 10–12% (social discount rate: 8%) |

---

## 5. Urban Infrastructure Planning

### Urban Water Supply Systems

| Parameter | Norm | Source |
|-----------|------|--------|
| Per capita supply (Indian cities) | 135–200 lpcd | CPHEEO |
| Per capita supply (metro cities) | 150–250 lpcd | CPHEEO |
| Distribution losses | 15–25% (well-managed) to 40–60% | Benchmarks |
| Minimum residual pressure | 7 m (single story), 10 m (double story) | CPHEEO |
| Fire flow | 2,500–4,500 L/min | IS 3938 |

### Urban Drainage Design

**Rational Method (small catchments < 5 km²):**
$$Q = \frac{1}{360} C i A$$

Where:
- $Q$ = peak runoff (m³/s)
- $C$ = runoff coefficient (0.1–0.95)
- $i$ = rainfall intensity (mm/hr) for design duration
- $A$ = catchment area (hectares)

**Time of concentration (Kerby formula):**
$$t_c = 0.0195 \cdot L^{0.77} \cdot S^{-0.385}$$

Where $L$ = flow length (m), $S$ = slope (m/m).

### Stormwater Management

| Practice | Description | Reduction in Peak Flow |
|----------|-------------|----------------------|
| Detention basin | Temporary storage | 20–40% |
| Retention pond | Permanent storage | 30–50% |
| Permeable pavement | Infiltration through surface | 10–30% |
| Green roof | Absorb + delay | 50–90% retention |
| Rainwater harvesting | Capture at source | 10–20% |

### Solid Waste Management Systems

| Component | Design Criteria |
|-----------|----------------|
| Collection frequency | Daily (wet), alternate day (dry) |
| Container size | 240 L (household), 1100 L (community) |
| Transfer station | Every 5–15 km radius |
| Landfill life | Design for 20–30 years |
| Recycling target | 40–60% (Swachh Bharat Mission) |

### Urban Transportation Planning

**Four-Step Travel Demand Model:**

| Step | Model | Output |
|------|-------|--------|
| 1. Trip Generation | Regression / Cross-classification | Total trips per zone |
| 2. Trip Distribution | Gravity model | O-D matrix |
| 3. Modal Split | Logit model | Mode choice (car, bus, walk) |
| 4. Traffic Assignment | All-or-nothing / User equilibrium | Route flows |

**Gravity Model:**
$$T_{ij} = \frac{O_i \cdot D_j \cdot f(c_{ij})}{\sum_k D_k \cdot f(c_{ik})}$$

Where $f(c_{ij}) = c_{ij}^{-\beta}$ (friction factor function).

**Level of Service (LOS) for roads:**

| LOS | Description | V/C Ratio |
|-----|-------------|-----------|
| A | Free flow | < 0.2 |
| B | Stable flow, slight delays | 0.2–0.4 |
| C | Stable flow, acceptable delays | 0.4–0.6 |
| D | Approaching unstable, tolerable delays | 0.6–0.8 |
| E | Unstable flow, significant delays | 0.8–1.0 |
| F | Forced flow, excessive delays | > 1.0 |

---

## 6. Infrastructure Sustainability & Resilience

### Life Cycle Assessment (LCA)

| Phase | Carbon Emissions Source |
|-------|------------------------|
| Material production (cradle-to-gate) | Cement, steel, asphalt manufacturing |
| Construction | Equipment fuel, transport |
| Operation | Energy, maintenance, water |
| End of life | Demolition, disposal, recycling |

**Embodied carbon (kg CO₂e/kg):**

| Material | Value |
|----------|-------|
| Cement | 0.9 |
| Steel (virgin) | 1.8 |
| Steel (recycled) | 0.4 |
| Concrete (20 MPa) | 0.13 |
| Timber (sustainably sourced) | -1.6 (net sequestration) |
| Aluminium | 8.0 |

### Life Cycle Cost Analysis (LCCA)

$$\text{LCCA} = C_{initial} + \sum_{t=1}^{n} \frac{C_{O\&M,t} + C_{rehabilitation,t}}{(1+r)^t} + \frac{C_{salvage}}{(1+r)^n}$$

Where:
- $C_{initial}$ = initial construction cost
- $C_{O\&M,t}$ = annual O&M cost in year $t$
- $C_{rehabilitation,t}$ = major rehabilitation cost
- $C_{salvage}$ = residual/salvage value
- $r$ = discount rate
- $n$ = analysis period

### Climate Resilience for Infrastructure

| Hazard | Adaptation Measure |
|--------|-------------------|
| Flooding | Elevated structures, flood barriers, green infrastructure |
| Sea level rise | Setback regulations, coastal protection |
| Extreme heat | Cool pavements, green roofs, reflective surfaces |
| Drought | Water recycling, rainwater harvesting, efficient fixtures |
| Earthquake | Seismic design codes, base isolation, retrofitting |
| Landslide | Slope stabilization, retaining structures, drainage |

### Green Building Rating (India)

| Credit Category | Typical Credits |
|-----------------|----------------|
| Sustainable site | Site selection, transport, heat island |
| Water efficiency | Low-flow fixtures, recycling, rainwater harvesting |
| Energy efficiency | Efficient HVAC, lighting, renewables |
| Materials & resources | Recycled content, local materials, waste reduction |
| Indoor environmental quality | Air quality, daylight, thermal comfort |
| Innovation | Green initiatives not in standard credits |

---

## 7. Risk Management in Infrastructure

### Risk Identification & Assessment

| Risk Category | Examples |
|---------------|----------|
| **Technical** | Design errors, technology obsolescence |
| **Construction** | Weather, labor shortage, equipment failure |
| **Financial** | Cost overrun, inflation, currency fluctuation |
| **Schedule** | Delay in approvals, permits, land acquisition |
| **Environmental** | Pollution, EIA non-compliance |
| **Regulatory** | Policy changes, legal disputes |
| **Political** | Government changes, public opposition |

### Risk Response Strategies

| Strategy | Application |
|----------|-------------|
| **Avoid** | Change plan to eliminate risk |
| **Mitigate** | Reduce probability or impact |
| **Transfer** | Insurance, surety bonds, subcontract |
| **Accept** | Acknowledge and plan contingency |

### Expected Monetary Value (EMV)

$$EMV = \text{Probability} \times \text{Impact (cost)}$$

**Risk-adjusted cost:**
$$\text{Budgeted Cost} = \text{Base Estimate} + \sum EMV_i$$

---

## 8. Indian Infrastructure Context

### Key Organizations

| Organization | Role |
|-------------|------|
| **NHAI** | National Highways Authority of India |
| **IRCON** | Railway construction PSU |
| **NBCC** | Construction and real estate PSU |
| **L&T** | Largest private construction company |
| **Tata Projects** | Infrastructure construction |
| **AECOM** | Global infrastructure consulting |
| **RITES** | Rail and transportation consulting |
| **MECON** | Multi-disciplinary consulting |
| **CPWD** | Government construction agency |

### Key Standards & Codes

| Code | Application |
|------|-------------|
| IS 456:2000 | Plain & reinforced concrete |
| IS 800:2007 | General construction in steel |
| IS 875 (Parts 1–5) | Design loads |
| IS 1893:2016 | Earthquake resistant design |
| IS 2911 | Design of pile foundations |
| IS 4585 | Pile load test |
| NHAI/MSRD standards | Highway geometric design |
| CPWD PWD schedules | Cost estimation norms |
| MoRTH specifications | Road construction standards |

### Infrastructure Sectors in India (2025–2030)

| Sector | Investment Target | Key Projects |
|--------|------------------|--------------|
| Roads & Highways | ₹5+ lakh crore/year | Bharatmala, NH expansion |
| Railways | ₹2.5 lakh crore/year | High-speed rail, dedicated freight corridors |
| Urban Infrastructure | ₹3+ lakh crore/year | Smart Cities Mission, AMRUT 2.0 |
| Water & Sanitation | ₹1.5 lakh crore/year | Jal Jeevan Mission |
| Ports & Shipping | ₹1+ lakh crore/year | Sagarmala |
| Aviation | ₹1+ lakh crore/year | New airports, UDAN scheme |
| Power | ₹2+ lakh crore/year | Renewable energy, grid modernization |

---

## 9. Interview Quick-Reference

### Most Asked Questions

| # | Question | Key Points |
|---|----------|------------|
| 1 | What is CPM? How is it different from PERT? | CPM = deterministic (single time), PERT = probabilistic (3-point estimate) |
| 2 | Explain Earned Value Management (EVM) | PV (planned), EV (earned), AC (actual); SPI = EV/PV, CPI = EV/AC |
| 3 | What is the plinth area method? | Plinth area × rate/m²; ±15–20% accuracy |
| 4 | Explain BOT vs HAM in PPP | BOT: private finances fully; HAM: 40% govt + 60% private annuity |
| 5 | What is NPV and IRR? Decision rules? | NPV > 0 accept; IRR > MARR accept |
| 6 | What is contingency in estimation? | 3–5% of estimated cost for unforeseen items |
| 7 | Explain BOQ (Bill of Quantities) | Itemized list of work with quantities, rates, amounts |
| 8 | What is free float vs total float? | Total float = delay without project delay; Free float = delay without successor delay |
| 9 | What are the steps in a detailed estimate? | BOQ preparation, measurement, rate analysis, abstract of cost |
| 10 | What is LCCA? | Life cycle cost = initial + O&M + rehabilitation − salvage (discounted) |
| 11 | What is the Rational Method? | Q = CiA/360 for small catchment peak flow |
| 12 | Explain relative compaction | Field dry density / Max lab dry density × 100%; target ≥ 95% |
| 13 | What are LOS for roads? | A (free flow) to F (forced flow); based on V/C ratio |
| 14 | What is the role of an infrastructure consultant? | Feasibility, DPR, design, tender, construction supervision |
| 15 | What is the difference between design-build and design-bid-build? | DB: single contract; DBB: separate contracts, sequential |

### Key Formulas Summary

| Formula | Use |
|---------|-----|
| $ES_j = \max(EF_i)$ | Forward pass CPM |
| $TF = LS - ES$ | Total float |
| $t_e = (t_o + 4t_m + t_p)/6$ | PERT expected time |
| $Z = (T_s - T_e)/\sqrt{\sum\sigma^2}$ | PERT probability |
| $NPV = -C_0 + \sum CF_t/(1+r)^t$ | Net present value |
| $BCR = PV_{benefits}/PV_{costs}$ | Benefit-cost ratio |
| $Q = CiA/360$ | Rational method |
| $\text{Relative Compaction} = \gamma_{d,field}/\gamma_{d,max} \times 100\%$ | Compaction control |
| $DSCR = \text{NOI}/\text{Debt Service}$ | Debt service coverage |

### Numerical Practice Problems

**Problem 1 — CPM:**
Activity A (3 days), B (5 days), C (4 days), D (6 days), E (2 days). Dependencies: A→C, A→D, B→D, C→E, D→E. Find critical path and total float of each activity.

> **Solution:**
> - ES(A)=0, EF(A)=3; ES(B)=0, EF(B)=5
> - ES(C)=3, EF(C)=7; ES(D)=max(3,5)=5, EF(D)=11
> - ES(E)=max(7,11)=11, EF(E)=13
> - Project duration = 13 days
> - Backward: LF(E)=13, LS(E)=11; LF(D)=11, LS(D)=5; LF(C)=11, LS(C)=7
> - TF(A)=4, TF(B)=0, TF(C)=4, TF(D)=0, TF(E)=0
> - **Critical path: B → D → E** (0 float)

**Problem 2 — NPV:**
Initial investment = ₹50 lakh. Annual cash flow = ₹15 lakh for 5 years. Discount rate = 12%. Should the project be accepted?

> **Solution:** $NPV = -50 + 15 \times \frac{1 - (1.12)^{-5}}{0.12} = -50 + 15 \times 3.6048 = -50 + 54.07 = ₹4.07$ lakh. Since NPV > 0, **accept**.

**Problem 3 — PERT:**
Activity has optimistic = 6 days, most likely = 10 days, pessimistic = 20 days. Find expected time and variance.

> **Solution:** $t_e = (6 + 4(10) + 20)/6 = 66/6 = 11$ days. $\sigma^2 = ((20-6)/6)^2 = (14/6)^2 = 5.44$ days². $\sigma = 2.33$ days.

**Problem 4 — Rational Method:**
A 50-hectare catchment has C = 0.5 and design rainfall intensity = 60 mm/hr. Find peak runoff.

> **Solution:** $Q = (1/360) \times 0.5 \times 60 \times 50 = 4.17$ m³/s.

---

## 10. Key References

| Resource | Use |
|----------|-----|
| PMBOK Guide (PMI) | Project management standards |
| CPWD Manual of Estimates | Indian government cost estimation |
| PERT/CPM by Moder & Phillips | Scheduling techniques |
| Infrastructure Finance (OECD) | PPP models and case studies |
| IS Codes (456, 800, 875, 1893) | Design standards |
| NHAI Tender Documents | Highway construction norms |
| MoRTH Specifications | Road construction standards |
| Urban Planning by Babar | Indian urban infrastructure context |

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 1.0 — Comprehensive Infrastructure Engineering & Management Guide

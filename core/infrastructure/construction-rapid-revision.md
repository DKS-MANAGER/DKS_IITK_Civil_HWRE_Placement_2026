# Construction Engineering — Rapid Revision Sheet

> Last-minute cheat sheet for Construction Engineer interviews and exams.

---

## Framework 1: Construction Methods

### Foundation Construction
- Open excavation → sheet piles → cofferdams → pile driving → dewatering
- Dewatering: sump pumping, well points, deep wells, electro-osmosis

### Formwork Types

| Type | Application |
|:-----|:------------|
| Conventional | Low-rise, custom shapes |
| Slipform | Continuous vertical (silos, cores) |
| Jump form | High-rise cores |
| Tunnel form | Repetitive rooms (hotels, hostels) |
| Table/flying form | Large slabs |

### Concrete Construction
- Mixing → placing → compacting → curing
- Curing: 7 days (OPC), 10-14 days (PPC), water/membrane/steam

### Bridge Construction
- Balanced cantilever (segmental)
- Incremental launching
- Precast segmental
- Cast-in-situ

### Tunnel Construction
- TBM (Tunnel Boring Machine): soft ground, fast, circular
- NATM (New Austrian Tunneling Method): rock, flexible support

---

## Framework 2: Construction Equipment

### Equipment Types

| Equipment | Application | Key Parameter |
|:----------|:------------|:---------------|
| Bulldozer | Earthmoving, clearing | Blade capacity, HP |
| Excavator | Digging, trenching | Bucket capacity (m³) |
| Loader | Material handling | Bucket size |
| Crane | Lifting | Capacity × radius |
| Compactor | Soil/pavement | Weight, frequency |
| Paver | Asphalt/concrete | Width, screed |
| Transit mixer | Concrete transport | Capacity (m³) |
| Concrete pump | Concrete placement | Reach, output |

### Productivity Calculation
$$\text{Output} = \frac{\text{Capacity} \times \text{Efficiency} \times \text{Working Time}}{\text{Cycle Time}}$$

**Example:** Excavator, bucket 1.5 m³, cycle 30 s, efficiency 80%, 8 hr/day:
- Cycles/hr = 3600/30 = 120
- Output = 120 × 1.5 × 0.80 = 144 m³/hr → 1152 m³/day

---

## Framework 3: Quality Control

### Concrete QC Tests

| Test | Standard | Measures |
|:-----|:---------|:---------|
| Cube test | IS 516 | Compressive strength (28 days) |
| Slump test | IS 1199 | Workability |
| Rebound hammer | IS 13311 | In-situ strength (NDT) |
| Core cutting | IS 1199 | Density, strength |

### Slump Values

| Element | Slump (mm) |
|:--------|:-----------|
| Columns | 25-50 |
| Slabs | 50-100 |
| Pumped concrete | 75-125 |

### IS 456 Cube Acceptance
- **Average** of 3 cubes ≥ f_ck + 0.825σ
- **Individual** min ≥ f_ck - 0.825σ
- σ = 4 MPa (M25), 5 MPa (M30)

### Soil QC Tests

| Test | Standard | Use |
|:-----|:---------|:----|
| Proctor compaction | IS 2720 Part 8 | Compaction control |
| CBR | IS 2720 Part 16 | Subgrade strength |
| Plate bearing | IS 5093 | Subgrade modulus |
| Pile load | IS 2911 | Foundation capacity |

### Compaction Control
$$\text{Relative Compaction} = \frac{\gamma_{d,field}}{\gamma_{d,max}} \times 100\%$$
- ≥ 95% Modified Proctor or ≥ 98% Standard Proctor

---

## Framework 4: Scheduling & Technology

### Earned Value Management (EVM)

| Metric | Formula | Meaning |
|:-------|:--------|:--------|
| EV | %complete × BAC | Earned value |
| PV | Planned % × BAC | Planned value |
| AC | Actual cost | Actual cost |
| CV | EV - AC | Cost variance (+ = good) |
| SV | EV - PV | Schedule variance (+ = good) |
| CPI | EV/AC | Cost performance (>1 = good) |
| SPI | EV/PV | Schedule performance (>1 = good) |

### Construction Software

| Tool | Use |
|:-----|:----|
| MS Project | Scheduling, Gantt |
| Primavera P6 | Enterprise PM, CPM |
| AutoCAD | Drawing, quantity takeoff |
| Revit | BIM authoring |
| Navisworks | Clash detection, 4D |
| Power BI | Project dashboards |
| CostX / Bluebeam | Digital takeoff |

### BIM Dimensions
- 3D: Geometry
- 4D: Time (scheduling)
- 5D: Cost
- 6D: Facilities management

---

## Quick-Fire Interview Answers

**Q1: What is the slump test and what does it measure?**
A: The slump test (IS 1199) measures the workability of fresh concrete — how easily it flows and compacts. Slump of 25-50 mm for columns, 50-100 mm for slabs, 75-125 mm for pumped concrete. It does NOT measure strength.

**Q2: How do you control soil compaction?**
A: Compare field dry density to maximum dry density (Modified Proctor): Relative Compaction = γ_d,field/γ_d,max × 100%. Must be ≥ 95% Modified Proctor. Control moisture at OMC, adjust number of roller passes, and verify with field density tests (sand replacement, nuclear gauge).

**Q3: What is the difference between TBM and NATM?**
A: TBM (Tunnel Boring Machine) is a full-face mechanical excavator used in soft ground, giving fast, circular, uniform tunnels with immediate support. NATM (New Austrian Tunneling Method) is a sequential excavation method for rock, using controlled blasting and flexible shotcrete support that adapts to ground conditions.

**Q4: How do you handle a failed concrete cube test?**
A: (1) Investigate the cause — mix design, curing, testing procedure. (2) Test cores from the actual structure (IS 516). (3) If cores pass, the cube failure may be a testing issue. (4) If cores fail, the concrete is defective — options include strengthening, partial demolition, or load reduction. (5) Document in an NCR and implement corrective action.

**Q5: What is Earned Value Management?**
A: EVM measures project performance by comparing earned value (EV = %complete × BAC) to planned value (PV) and actual cost (AC). CV = EV-AC, SV = EV-PV, CPI = EV/AC, SPI = EV/PV. CPI < 1 means cost overrun; SPI < 1 means behind schedule.

**Q6: What is the difference between destructive and non-destructive testing?**
A: Destructive testing (cube test, core cutting) damages or destroys the sample. Non-destructive testing (rebound hammer, ultrasonic pulse velocity) evaluates the structure without damage. NDT is used for in-situ assessment of existing structures.

**Q7: What is BIM?**
A: Building Information Modeling is a digital 3D model of a building/infrastructure with embedded data (materials, cost, schedule). It enables clash detection, 4D scheduling, 5D cost, and collaborative design. Revit and Navisworks are common tools.

**Q8: What are the key safety hazards on a construction site?**
A: Falls from height, struck-by (equipment, falling objects), electrocution, caught-in/between (machinery), excavation collapse, and hazardous materials. Mitigation: PPE, scaffolding standards (IS 3696), guardrails, safety training, toolbox talks, and regular inspections.

**Q9: How do you select a crane for a lift?**
A: Consider (1) weight of the heaviest load, (2) required reach/radius, (3) lift height, (4) crane capacity at that radius (capacity decreases with radius), (5) site access and ground conditions, (6) safety factor. Use the crane's load chart to verify capacity at the required radius.

**Q10: What is the balanced cantilever method?**
A: A bridge construction method where segments are cast or erected symmetrically on both sides of a pier, forming cantilevers. Segments are added outward until they meet mid-span. Used for long-span bridges over rivers/valleys where falsework is impractical.

---

## Last-Minute Checklist

- [ ] Formwork types (slipform, jump, tunnel, table)
- [ ] Curing periods (7 days OPC, 10-14 days PPC)
- [ ] Dewatering methods
- [ ] Bridge construction methods
- [ ] TBM vs NATM
- [ ] Equipment types and productivity
- [ ] Excavator productivity calculation
- [ ] Concrete QC tests (IS 516, 1199, 13311)
- [ ] Slump values by element
- [ ] IS 456 cube acceptance criteria
- [ ] Compaction control (≥95% Modified Proctor)
- [ ] EVM metrics (EV, PV, AC, CV, SV, CPI, SPI)
- [ ] Construction software (MS Project, Primavera, Revit)
- [ ] BIM dimensions (3D-6D)
- [ ] Site safety hazards

---

## Cross-Links

- [`infrastructure-engineering-management.md`](infrastructure-engineering-management.md) — Full subject reference
- [`construction-tech.md`](../../software-and-tech/construction/construction-tech.md) — Construction technology tools
- [`construction-role-study-plan.md`](construction-role-study-plan.md) — Detailed study plan with worked examples
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Compaction, foundations
- [`structures.md`](../structures/structures.md) — Concrete design, IS 456

---

## References

- IS 456, IS 516, IS 1199, IS 13311, IS 2720, IS 2911, IS 5093, IS 3696, IS 4082
- CPWD Specifications
- PMBOK Guide (PMI)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

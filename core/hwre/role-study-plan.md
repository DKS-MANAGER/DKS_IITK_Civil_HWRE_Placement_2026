# Water Resources Engineer — Study Plan

> 4-week preparation roadmap for HWRE-focused placements (NHPC, CWC, state water boards, consulting firms).

---

## Role Overview

**What WREs do:** Design, plan, and manage water resource systems — reservoirs, canals, flood control, irrigation, groundwater, wastewater treatment.

**Day-to-day:** Hydrological analysis, hydraulic modeling, flood routing, reservoir operations, irrigation planning, water quality assessment.

**Civil/M.Tech advantage:** Direct domain match. Thesis work in hydraulics/hydrology is a major differentiator. IITK M.Tech in HWRE is the gold standard.

**Target companies:** NHPC, CWC, BWDB, state irrigation departments, L&T (water projects), AECOM, Tata Projects, WAPCOS, consulting firms with water practice.

---

## Topic 1: Hydrology & Flood Analysis

### Why This Matters
Hydrology is the foundation of HWRE. Every PSU interview will test unit hydrographs, flood frequency, and routing.

### What to Learn
- [ ] Hydrologic cycle and catchment response
- [ ] Unit Hydrograph (UH) — S-curve, superposition
- [ ] Flood frequency analysis (Gumbel, Log-Pearson Type III)
- [ ] Flood routing — Muskingum, Level Pool
- [ ] Infiltration models (Horton, Philip, Green-Ampt)
- [ ] Rational method for peak discharge

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Hydrology | [hydrology.md](hydrology/hydrology.md) | 4,470 words — comprehensive |
| Foundations | [civil-engineering-foundations.md](../fundamentals/civil-engineering-foundations.md) | Quick formulas + examples |

### Worked Example
> **"Route a flood through a river reach using Muskingum method."**
>
> Given: Inflow hydrograph, K = 6 hours, x = 0.2, Δt = 3 hours
> 1. Calculate C₀, C₁, C₂ using Muskingum coefficients
> 2. Apply: O₂ = C₀I₂ + C₁I₁ + C₂O₁
> 3. Step through time
>
> → Full walkthrough in [hydrology.md](hydrology/hydrology.md)

### Practice
- [ ] Basic: 3 UH synthesis problems (S-curve method)
- [ ] Intermediate: 3 Muskingum routing problems
- [ ] Interview-level: 2 flood frequency analysis problems

### Interview Questions
1. Explain the unit hydrograph concept and its assumptions. — *Tests: foundational knowledge*
2. How do you route a flood through a reservoir? — *Tests: routing methods*
3. What is the difference between confined and unconfined aquifers? — *Tests: groundwater knowledge*
4. How do you determine reservoir storage capacity? — *Tests: practical application*
5. What are environmental flows? — *Tests: modern water management*

### Completion Criterion
- [ ] Can derive UH from rainfall data
- [ ] Can solve Muskingum routing in 15 minutes
- [ ] Can explain flood frequency analysis steps

---

## Topic 2: Hydraulics & Open Channel Flow

### Why This Matters
Hydraulics is the second pillar of HWRE. Pipe flow, open channel flow, and hydraulic structures are core interview topics.

### What to Learn
- [ ] Bernoulli's equation with losses
- [ ] Manning's equation for open channel flow
- [ ] Hydraulic jump (conjugate depths, energy loss)
- [ ] Specific energy and critical flow
- [ ] GVF profiles (M1, M2, M3, S1, S2, S3)
- [ ] Pipe networks (Hardy Cross method)
- [ ] Turbulence models (k-ε, k-ω)

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Hydraulics | [hydraulics.md](hydraulics/hydraulics.md) | 5,034 words — comprehensive |
| Open Channel Flow | [open-channel-flow.md](open_channel_flow/open-channel-flow.md) | 5,180 words — comprehensive |
| Turbulence Modeling | [turbulence-modeling.md](hydraulics/turbulence-modeling.md) | 1,849 words |

### Worked Example
> **"Find the normal depth in a trapezoidal channel."**
>
> Given: Q = 20 m³/s, n = 0.015, S₀ = 0.001, b = 5 m, m = 2
> 1. Manning's equation: Q = (1/n) × A × R^(2/3) × S₀^(1/2)
> 2. A = (b + my)y, P = b + 2y√(1+m²)
> 3. Iterate or solve numerically
>
> → Full walkthrough in [open-channel-flow.md](open_channel_flow/open-channel-flow.md)

### Practice
- [ ] Basic: 3 Manning's equation problems
- [ ] Intermediate: 3 hydraulic jump problems
- [ ] Interview-level: 2 GVF profile classification problems

### Interview Questions
1. Explain Bernoulli's equation and its limitations. — *Tests: fundamental understanding*
2. What is a hydraulic jump and when does it occur? — *Tests: OCF knowledge*
3. How do you classify GVF profiles? — *Tests: profile analysis*
4. Explain the Hardy Cross method for pipe networks. — *Tests: pipe flow*
5. What is NPSH and why does it matter for pump selection? — *Tests: practical application*

---

## Topic 3: Water Resources Engineering

### Why This Matters
This is the applied core — reservoir design, canal systems, irrigation, groundwater management.

### What to Learn
- [ ] Reservoir design (mass curve, storage capacity)
- [ ] Canal distribution systems (Ryotwari, Canal design)
- [ ] Irrigation engineering (crop water requirement, duty, delta)
- [ ] Groundwater hydrology (Darcy's law, well hydraulics)
- [ ] Water quality parameters
- [ ] Flood control and management

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Water Resources | [water-resources-engineering.md](water_resources/water-resources-engineering.md) | 3,877 words |
| Irrigation | [irrigation-engineering.md](irrigation/irrigation-engineering.md) | Supporting |
| Groundwater | [groundwater.md](water_supply/groundwater.md) | Supporting |

### Worked Example
> **"Design a canal using Manning's equation."**
>
> Given: Q = 50 m³/s, n = 0.017, S₀ = 0.0005
> Best hydraulic section (trapezoidal): b/y = 2(√(1+m²) − m)
> Solve for dimensions
>
> → Full walkthrough in [water-resources-engineering.md](water_resources/water-resources-engineering.md)

### Interview Questions
1. How do you determine reservoir storage capacity using a mass curve? — *Tests: reservoir design*
2. Explain the concept of duty, delta, and base period. — *Tests: irrigation fundamentals*
3. What is the difference between confined and unconfined aquifers? — *Tests: groundwater*
4. How do you design a flood control system for an urban area? — *Tests: applied knowledge*
5. What are environmental flows and why are they important? — *Tests: modern practice*

---

## Topic 4: HWRE Interview Strategy & Rapid Revision

### Why This Matters
HWRE interviews test both breadth (all subjects) and depth (thesis topic). You need a clear strategy.

### Interview Strategy
| Round | Format | Focus |
|:------|:-------|:------|
| OA | Aptitude + technical MCQs | Broad knowledge |
| Technical 1 | Subject questions | Hydraulics + Hydrology depth |
| Technical 2 | Project discussion | Thesis + projects |
| HR | Behavioral + motivation | Why HWRE? Why this company? |

### Thesis/Project Discussion
- Prepare a 3-minute pitch for your thesis
- Know the methodology, results, and limitations
- Be ready for follow-up questions on assumptions
- Connect thesis to practical applications

---

## Mock Test

| Section | Questions | Time | Topics |
|:--------|:----------|:-----|:-------|
| Hydrology | 5 questions | 20 min | Topic 1 |
| Hydraulics | 5 questions | 20 min | Topic 2 |
| Water Resources | 5 questions | 20 min | Topic 3 |
| Applied/Design | 3 problems | 20 min | All topics |
| Interview-style | 5 questions | 15 min | All topics |
| **Total** | **23** | **95 min** | |

---

## Rapid Revision

### Must-Memorize Formulas
| Formula | Equation |
|:--------|:---------|
| Manning's | Q = (1/n) × A × R^(2/3) × S₀^(1/2) |
| Bernoulli | P₁/γ + V₁²/2g + z₁ = P₂/γ + V₂²/2g + z₂ + h_L |
| Darcy's Law | Q = K × A × (dh/dl) |
| Continuity | Q = A × V |
| Hydraulic Jump | y₂/y₁ = 0.5(√(1 + 8Fr₁²) − 1) |
| Muskingum | O₂ = C₀I₂ + C₁I₁ + C₂O₁ |
| Unit Hydrograph | Direct runoff = rainfall excess × UH ordinates |
| Rational Method | Q = C × i × A |

### Key Dimensionless Numbers
| Number | Formula | Significance |
|:-------|:--------|:-------------|
| Reynolds | Re = VL/ν | Flow regime (laminar/turbulent) |
| Froude | Fr = V/√(gy) | Flow classification (subcritical/supercritical) |
| Manning's n | Roughness coefficient | Channel resistance |

### Last-Minute Checklist
- [ ] Reviewed Manning's equation and solved 1 problem
- [ ] Reviewed Bernoulli's equation with losses
- [ ] Reviewed UH concept and Muskingum routing
- [ ] Reviewed hydraulic jump equations
- [ ] Prepared 3-minute thesis pitch
- [ ] Reviewed 5 key formulas from each subject
- [ ] Researched [company] recent water projects

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Hydrology | [hydrology.md](hydrology/hydrology.md) |
| Hydraulics | [hydraulics.md](hydraulics/hydraulics.md) |
| Open Channel Flow | [open-channel-flow.md](open_channel_flow/open-channel-flow.md) |
| Water Resources | [water-resources-engineering.md](water_resources/water-resources-engineering.md) |
| Turbulence Modeling | [turbulence-modeling.md](hydraulics/turbulence-modeling.md) |
| Sediment Transport | [sediment-transport.md](hydrology/sediment-transport.md) |
| Foundations | [civil-engineering-foundations.md](../fundamentals/civil-engineering-foundations.md) |
| Technical Interview Bank | [../../prep/interview/technical/technical-interview-bank.md](../../prep/interview/technical/technical-interview-bank.md) |
| Project Discussion | [../../prep/interview/technical/project-discussion.md](../../prep/interview/technical/project-discussion.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Based on role-study-plan-template.md. Customized for Water Resources Engineer role.*

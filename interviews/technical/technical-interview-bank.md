# Technical Interview Preparation

## Core Civil/HWRE Concepts

### Fluid Mechanics & Hydraulics

#### Key Topics (Priority: High)
| Topic | Subtopics | Status |
|-------|-----------|--------|
| **Bernoulli, continuity, momentum** | Energy equation, flow regimes, dimensional analysis | ⬜ |
| **Viscous flow** | Laminar/turbulent, boundary layer, pipe friction | ⬜ |
| **Open channel flow** | GVF, RVF, hydraulic jump, unsteady flow | ⬜ |
| **Pipe networks** | Hardy-Cross method, pumps, turbines | ⬜ |
| **Physical interpretation** | Assumptions, scaling, non-dimensional groups | ⬜ |

#### Common Interview Questions
- Explain Bernoulli's equation and its limitations
- Derive the momentum equation for a control volume
- What is the difference between laminar and turbulent flow?
- How does a hydraulic jump form? What are the energy losses?
- Explain the significance of Reynolds number in pipe flow

#### Preparation Strategy
- Review derivations from IITK HWRE course slides
- Practice numerical problems from Munson/White textbooks
- Understand physical interpretation of assumptions

### Turbulence Modeling

| Topic | Subtopics | Status |
|-------|-----------|--------|
| **RANS closures** | k-ε, k-ω, SST; eddy-viscosity hypothesis | ⬜ |
| **LES vs DNS vs RANS** | Cost, resolution, fidelity trade-offs | ⬜ |
| **Wall functions** | y+, near-wall treatment, mesh sensitivity | ⬜ |
| **Free shear flows** | Mixing layers, jets, wakes; energy cascade | ⬜ |
| **Multiphase turbulence** | VOF, Euler-Euler, sediment-laden flows | ⬜ |

#### Key Concepts to Master
- Derivation of k-ε model transport equations
- Wall law: u+ = (1/κ)·ln(y+) + B
- Kolmogorov scales: η = (ν³/ε)^(1/4), τ = (ν/ε)^(1/2), l = (ν³/ε)^(1/4)
- Grid resolution requirements for LES (Δ ≤ 0.5·η)

#### Common Questions
- What are the differences between RANS, LES, and DNS?
- How do you choose an appropriate turbulence model?
- Explain wall functions and their limitations
- What is the energy cascade in turbulence?

### Hydrology & Water Resources

| Topic | Subtopics | Status |
|-------|-----------|--------|
| **Unit hydrograph** | S-curve, peak discharge, time of concentration | ⬜ |
| **Hydrologic cycle** | Rainfall-runoff, infiltration, catchment response | ⬜ |
| **Reservoir design** | Stage-discharge, mass diagram, flood routing | ⬜ |
| **Groundwater flow** | Darcy's law, Theis equation, aquifer properties | ⬜ |
| **Sediment transport** | Capacity, deposition, scour, bed evolution | ⬜ |

#### Common Questions
- Derive the Theis solution for groundwater flow
- Explain the Muskingum method of flood routing
- What is the difference between total and bed material load?
- How do you estimate scour depth around bridge piers?

### Structures & Geotech (Breadth for Core Design Roles)

#### Strength of Materials
- Bending, shear, torsion relationships
- Deflection methods (double integration, conjugate beam)
- Energy methods (Castigliano's theorem)
- Combined stress/strain states

#### Soil Mechanics
- Consolidation and settlement analysis
- Permeability and seepage
- Bearing capacity theories (Terzaghi, Meyerhof)

#### RCC/Steel Basics
- IS 456 and IS 800 provisions
- Load combinations and partial safety factors
- Design of singly/doubly reinforced beams

## Technical Skills Matrix

### Python Proficiency
- **NumPy**: Array operations, broadcasting, vectorization
- **SciPy**: Optimization, integration, interpolation
- **Pandas**: DataFrame manipulation, groupby, merge
- **Matplotlib**: Plotting, subplots, customization

### C++/MATLAB
- **MATLAB**: Matrix operations, ODE/PDE solvers, plotting
- **C++**: STL containers, algorithms, pointer management

### CFD (OpenFOAM)
- Case setup: `0/`, `constant/`, `system/` directories
- Meshing: `blockMesh`, `snappyHexMesh`
- Boundary conditions: `U`, `p`, `k`, `epsilon`, `omega`
- Solver selection: `simpleFoam`, `pimpleFoam`, `interFoam`
- y+ calculation and wall function usage

## Company-Specific Prep

### PSU Track (BPCL, EIL, NHPC, NTPC, WAPCOS)
- **GATE-adjacent technical recall**: Quick formula revision
- **IS code familiarity**: IS 456, IS 800, IS 1893, relevant codes
- **Project/site awareness**: Be ready to discuss any project mentioned in resume
- **HR/GK**: Current affairs, company history, recent developments

### Core Design/Consulting (L&T, AECOM, Tata Projects)
- **Structural design**: RCC, steel design, IS code applications
- **BBS**: Bar bending schedules, quantity takeoffs
- **Site logic**: Construction methods, quality control, safety
- **IRC basics**: Highway geometric design, pavement design

### Analytics/Quant Track
- **Statistics**: Hypothesis testing, distributions, regression
- **ML basics**: Supervised/unsupervised learning concepts
- **Business framing**: Translate business problems to analytical solutions
- **Communication**: Explain technical results to non-technical stakeholders

## Coding Drills

### Daily Schedule (3-5 scripts/week)
1. **Pandas/NumPy**: Data manipulation problems
2. **SQL**: Query writing and optimization
3. **Algorithms**: DSA problems (graphs, DP, trees)
4. **Visualization**: Plot creation and interpretation

### Key Areas
- Data structures: arrays, linked lists, stacks, queues, trees, graphs
- Algorithms: sorting, searching, graph traversal, dynamic programming
- SQL: joins, aggregation, window functions, subqueries
- Python: OOP, file I/O, regex, error handling

## Derivation Log Template

```text
Topic: [e.g., Hagen-Poiseuille equation]
Source: [Textbook/course reference]
Derivation Steps:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Physical Interpretation:
- Assumption: [Key assumption]
- Limitation: [When it breaks down]
- Application: [Where it's used]
```text

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK) — Core Civil/HWRE Concepts, Technical Stack, Company Profiles sections

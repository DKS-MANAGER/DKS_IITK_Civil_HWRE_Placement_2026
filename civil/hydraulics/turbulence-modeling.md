# Turbulence Modeling

## Relevance to HWRE

Turbulence modeling is critical for computational fluid dynamics (CFD) applications in water resources, including sediment-laden flows, open channel hydraulics, and multiphase interfacial phenomena. Understanding model selection, near-wall treatment, and computational cost trade-offs is essential for HWRE roles involving OpenFOAM or similar solvers.

## Turbulence Characteristics

### Energy Cascade
- Kinetic energy transfers from large eddies to progressively smaller eddies
- Kolmogorov scales: Smallest scales where viscosity dissipates kinetic energy into heat
- Universal equilibrium range: Statistics depend only on viscosity and dissipation rate

### Free Shear vs. Wall-Bounded Turbulence
- Free shear flows: Jets, wakes, mixing layers; anisotropy persists across the flow
- Wall-bounded flows: Boundary layers, channels, pipes; strong anisotropy near the wall
- Log-law region: Overlap region in turbulent boundary layers where velocity varies logarithmically with wall distance

## Reynolds-Averaged Navier-Stokes (RANS) Models

### Eddy-Viscosity Hypothesis
- Reynolds stresses are related to mean strain rates through an eddy viscosity
- Boussinesq approximation forms the basis for most two-equation models

### Two-Equation Models
- **k-epsilon (k-ε):** Standard, RNG, and realizable variants; robust for high Reynolds number flows; requires near-wall treatment
- **k-omega (k-ω):** Superior near-wall behavior; sensitive to free-stream values
- **k-omega SST:** Blends k-ω near walls with k-epsilon in the free stream; widely used for adverse pressure gradients and separation

### Near-Wall Treatment
- **y+ criteria:** y+ < 5 for resolving viscous sublayer; y+ ≈ 30–300 for wall functions
- Wall functions: Semi-empirical formulas to bridge the viscous sublayer; reduce mesh requirements
- Low-Reynolds number models: Resolve the viscous sublayer without wall functions

## Large Eddy Simulation (LES) vs. DNS vs. RANS

| Method | Resolution | Cost | Fidelity | Typical Use |
|--------|-----------|------|----------|-------------|
| DNS | All scales | Extremely high | Highest | Fundamental research, low Re |
| LES | Large scales | High | High | Complex separated flows, aeroacoustics |
| RANS | Time-averaged | Low | Moderate | Design iterations, industrial applications |

- **DNS:** Resolves all turbulent scales; computationally prohibitive for high-Re flows
- **LES:** Resolves large eddies, models small eddies; offers better fidelity than RANS at higher cost
- **RANS:** Models all turbulent scales; cost-effective for engineering design

## Multiphase Turbulence

### Volume of Fluid (VOF)
- Tracks interface between immiscible fluids using a phase-fraction function
- Suitable for free-surface flows, waves, and droplet dynamics

### Euler-Euler Approaches
- Treats phases as interpenetrating continua
- Suitable for sediment-laden flows and bubbly flows

### Sediment-Laden Flows
- Turbulence modulation by suspended particles
- Two-way coupling between fluid and sediment phases

## Practical Considerations for HWRE

### Solver Selection
- **RANS:** Preferred for steady-state design studies, reservoir modeling, preliminary channel design
- **LES:** Appropriate for unsteady, high-fidelity simulations of hydraulic jumps, scour holes, or complex bathymetry
- **DNS:** Reserved for academic validation or fundamental turbulence studies

### Mesh Sensitivity
- y+ monitoring is critical for wall-bounded hydraulic simulations
- Boundary layer mesh refinement: 10–20 cells across the boundary layer for LES
- Aspect ratio control in highly anisotropic boundary layer regions

### Model Limitations
- k-epsilon may under-predict separation in adverse pressure gradients
- SST can over-predict separation in some free-shear configurations
- Wall functions become unreliable in strong pressure gradients or massive separation

## Key Resources
- Pope, *Turbulent Flows* (canonical reference for turbulence theory)
- OpenFOAM documentation for solver selection and case setup
- IITK turbulence course material for free shear vs. wall-bounded distinctions

## Further expansion needed
- Derivation of RANS closure equations
- Detailed filter analysis for LES
- Anisotropic turbulence tensor properties
- Advanced subgrid-scale models for LES

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
- `F:\2k26Placement\awesome-civil-engineering\README.md`
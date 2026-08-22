# Hydraulics

## Scope

Hydraulics covers the behavior of fluids at rest and in motion, with emphasis on pipe systems, open channels, pumps, turbines, and the forces exerted by fluids on structures.

## Fundamental Principles

### Governing Equations
- **Continuity equation:** Mass conservation for incompressible flow
- **Bernoulli equation:** Energy conservation along a streamline
- **Momentum equation:** Force balance for control volumes

### Flow Regimes
- Laminar flow: Characterized by smooth, orderly fluid motion; dominant at low Reynolds numbers
- Turbulent flow: Chaotic mixing with enhanced momentum and heat transfer; dominant at high Reynolds numbers
- Transitional flow: Intermediate regime between laminar and turbulent

### Pipe Flow & Friction
- Major losses: Head loss due to pipe friction (Darcy-Weisbach equation)
- Minor losses: Head loss due to fittings, bends, valves, entrances, and exits
- Moody diagram: Relates friction factor to Reynolds number and relative roughness
- Hazen-Williams and Manning formulas: Empirical approaches for practical pipe design

### Boundary Layers
- Development of velocity boundary layers over flat plates and internal flows
- Boundary layer thickness, displacement thickness, momentum thickness
- Separation criteria and wake formation

### Pumps & Turbines
- Centrifugal pump characteristics: Head-capacity curves, efficiency, NPSH
- Specific speed and scaling laws for pump selection
- Turbine classification: Impulse (Pelton) versus reaction (Francis, Kaplan)
- Affinity laws for geometrically similar machines

### Forces on Immersed Bodies
- Drag force: Form drag, skin friction drag, wave drag
- Lift force: Pressure differential around airfoils and hydrofoils
- Drag coefficient and lift coefficient as functions of Reynolds number and geometry

## Dimensional Analysis & Similitude
- Buckingham Pi theorem for deriving dimensionless groups
- Key dimensionless numbers: Reynolds number, Froude number, Weber number, Mach number
- Model testing: Geometric, kinematic, and dynamic similarity requirements

## Software & Computational Tools

| Tool | Primary Use |
|------|-------------|
| HEC-RAS | River and open channel hydraulic modeling |
| WaterGEMS | Water distribution system analysis |
| EPANET | Pipe network analysis and water quality |
| InfoWater Pro | GIS-integrated water distribution modeling |
| Flow 3D | CFD for hydraulic and hydro-geological modeling |

## Key Interview Topics

Expect questions on:
- Physical interpretation of assumptions in Bernoulli's equation
- Scaling laws and nondimensional group significance
- Pipe network analysis methods (Hardy Cross, linear theory)
- Pump and turbine selection criteria
- Drag reduction and turbulence suppression techniques

## Worked Examples

### Example 1: Pipe Network (Hardy Cross)
Given a simple loop with pipes $L_1=500$ m, $D_1=0.3$ m, $L_2=600$ m, $D_2=0.25$ m, initial guess $Q_1=0.1$ m³/s, $Q_2=-0.1$ m³/s, $f=0.02$:
1. Compute head loss $h_f = f \frac{L}{D} \frac{Q^2}{2gA^2}$ for each pipe
2. Compute correction $\Delta Q = -\frac{\sum h_f}{\sum \frac{\partial h_f}{\partial Q}}$
3. Iterate until $\sum h_f < 0.01$ m

### Example 2: Bernoulli with Loss
Water flows from reservoir ($H=10$ m) through a pipe ($L=100$ m, $D=0.2$ m, $f=0.03$) to atmosphere. Find discharge:
1. Total head = 10 m
2. $h_f = f \frac{L}{D} \frac{v^2}{2g}$
3. $10 = \frac{v^2}{2g} + h_f$ → solve quadratic for $v$

## Further expansion needed
- Detailed derivations of governing equations
- Numerical methods for pipe network solving
- Advanced turbomachinery theory
- Computational fluid dynamics discretization schemes

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
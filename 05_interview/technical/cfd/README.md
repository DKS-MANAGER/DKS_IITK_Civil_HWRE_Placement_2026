# Computational Fluid Dynamics (CFD) — Technical Interview Guide

> **Target Roles**: CFD Engineer, Thermal/Fluids Specialist, Simulation Consultant (OpenFOAM, ANSYS Fluent).

---

## High-Frequency CFD Technical Questions & Answers

### 1. Navier-Stokes Equations & Discretization
* **Q1**: *"Write and physically interpret the incompressible Navier-Stokes momentum equation."*
  * **Answer**: $\rho \left(\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u}\right) = -\nabla p + \mu \nabla^2 \mathbf{u} + \rho \mathbf{g}$.
    * Term 1: Unsteady acceleration (temporal inertia).
    * Term 2: Convective acceleration (non-linear spatial advection).
    * Term 3: Pressure gradient force.
    * Term 4: Viscous diffusion stress.
    * Term 5: Body forces (gravity).
* **Q2**: *"Why is pressure-velocity coupling needed for incompressible flows, and how do SIMPLE and PISO algorithms work?"*
  * **Answer**: In incompressible flow, continuity ($\nabla \cdot \mathbf{u} = 0$) contains no pressure term. Pressure must be determined from a Poisson equation enforcing velocity divergence-free condition.
    * **SIMPLE** (Semi-Implicit Method for Pressure-Linked Equations): Iterative predictor-corrector for steady flows using relaxation factors.
    * **PISO** (Pressure-Implicit with Splitting of Operators): Uses 1 predictor and multiple corrector steps per time step, ideal for transient/unsteady flows.

### 2. Turbulence Modeling ($k$-$\epsilon$ vs $k$-$\omega$ SST)
* **Q3**: *"Compare the Standard $k$-$\epsilon$ and $k$-$\omega$ SST turbulence models. When would you choose one over the other?"*
  * **Answer**:
    * **Standard $k$-$\epsilon$**: Good for high Reynolds number free-shear flows away from boundaries; poor for adverse pressure gradients and boundary separation.
    * **$k$-$\omega$ SST (Shear Stress Transport)**: Blends $k$-$\omega$ formulation near the wall (superior boundary layer separation modeling) with $k$-$\epsilon$ in the far field. Standard choice for aerodynamic and hydraulic separation/scour simulations.
* **Q4**: *"What is $y^+$ and why is it critical in wall mesh generation?"*
  * **Answer**: $y^+ = \frac{u_\tau y}{\nu}$ is the dimensionless distance from the wall.
    * For resolved viscous sublayer ($y^+ \approx 1$), the full laminar sublayer is discretized without wall functions.
    * For wall functions ($30 < y^+ < 300$), the near-wall log-law profile is assumed analytically, reducing mesh cell count substantially.

### 3. OpenFOAM Architecture & Solvers
* **Q5**: *"Explain the role of `controlDict`, `fvSchemes`, and `fvSolution` in an OpenFOAM case directory."*
  * **Answer**:
    * `controlDict`: Time step ($\Delta t$), run duration, write interval, Courant number ($Co = \frac{u \Delta t}{\Delta x} < 1$).
    * `fvSchemes`: Discretization schemes (temporal, gradient, divergence schemes like upwind, linear, vanLeer).
    * `fvSolution`: Linear equation solvers (PCG, PBiCG), convergence tolerances, and algorithm controls (SIMPLE/PIMPLE).

# Archetype 1: Hydrodynamic Scour & Structural Risk Modeling

> **Domain**: Computational Fluid Dynamics (CFD) / Hydraulic Structures / Structural Risk  
> **Status**: [HYPOTHETICAL ENGINEERING CASE ARCHETYPE — SAMPLE FOR INTERVIEW PRACTICE]  
> **Purpose**: Demonstrates structured project defense, mathematical foundations, numerical verification, and interview question handling without relying on any personal candidate data or private experimental findings.

---

## 1. Executive Summary & Problem Formulation

* **Engineering Challenge**: Riverine bridges and marine crossings experience localized scour around piers and abutments due to 3D vortex shedding (horseshoe and wake vortices). Excessive scour undermines foundation caissons, leading to structural instability during high-return-period flood discharges.
* **Objective**: Develop a calibrated 2D/3D hydrodynamic simulation workflow to predict equilibrium scour depth and flow separation fields across design flood hydrographs (e.g., 25-year and 100-year return flows).
* **Target Roles**: Core Civil Engineering (L&T, Hilti, Thornton Tomasetti, AECOM), Hydraulics Consulting, and Quantitative Risk Modeling.

---

## 2. Theoretical Foundations & Governing Equations

### 2.1 Depth-Averaged Shallow Water Formulation (2D)
For reach-scale hydrodynamic flood inundation and approach velocity fields, the depth-averaged shallow water (Saint-Venant) equations govern:

$$\frac{\partial h}{\partial t} + \frac{\partial (h u)}{\partial x} + \frac{\partial (h v)}{\partial y} = 0$$

$$\frac{\partial (h u)}{\partial t} + \frac{\partial (h u^2 + \frac{1}{2} g h^2)}{\partial x} + \frac{\partial (h u v)}{\partial y} = - g h \frac{\partial z_b}{\partial x} - \frac{\tau_{bx}}{\rho}$$

where $h$ is flow depth, $u, v$ are depth-averaged velocity components, $z_b$ is bed elevation, and $\tau_b = \rho g n^2 |\mathbf{u}| \mathbf{u} / h^{1/3}$ is bed shear stress parametrized by Manning's roughness coefficient $n$.

### 2.2 Local Pier Scour Empirical & Semi-Empirical Relations
For localized scour depth $y_s$ at round-nosed piers, the FHWA HEC-18 equation provides baseline empirical comparison:

$$\frac{y_s}{y_1} = 2.0 \, K_1 K_2 K_3 \left(\frac{a}{y_1}\right)^{0.65} \mathrm{Fr}_1^{0.43}$$

where $y_1$ is approach depth, $a$ is pier diameter, $\mathrm{Fr}_1 = \frac{V_1}{\sqrt{g y_1}}$ is approach Froude number, and $K_1, K_2, K_3$ are correction coefficients for pier nose shape, angle of attack, and bed configuration.

---

## 3. Numerical Modeling Workflow

```
1. Geometry & Mesh
   ├── High-resolution bathymetric LiDAR / cross-section processing
   ├── Unstructured triangular/quadrilateral hybrid grid
   └── Boundary layer refinement near structural pier perimeters (y+ targeting)
2. Solver Configuration
   ├── Finite Volume Method (FVM) spatial discretization
   ├── Second-order upwind momentum schemes
   └── Pressure-velocity coupling (PISO / SIMPLE algorithm)
3. Verification & Validation (V&V)
   ├── Grid Convergence Index (GCI) computed across coarse, medium, fine grids
   └── Validation against published flume benchmark measurements
4. Parametric Scenarios
   └── Sensitivity analysis across peak discharges (Q_10, Q_50, Q_100) and riprap sizes
```

---

## 4. Illustrative Defense & Sample Interview Questions

### Q1: "How did you establish numerical grid independence?"
> **Model Response**: "We implemented the ASME V&V 20 standard using Richardson extrapolation across three systematically refined mesh levels with a grid refinement ratio $r = 1.4$. By monitoring the target output (maximum bed shear stress and local scour depth), we computed the apparent order of convergence $p$ and the Grid Convergence Index (GCI). The fine-grid GCI fell below 3.5%, confirming that spatial discretization error was well within acceptable engineering tolerances."

### Q2: "Why choose $k\text{-}\omega$ SST over standard $k\text{-}\epsilon$ turbulence models near the pier?"
> **Model Response**: "Standard $k\text{-}\epsilon$ models assume isotropic eddy viscosity and severely overpredict turbulent kinetic energy near stagnation points, leading to unphysical erosion estimates. The Shear Stress Transport ($k\text{-}\omega$ SST) formulation solves $k\text{-}\omega$ in the sublayer to capture boundary-layer adverse pressure gradients and vortex roll-up, while transitioning to $k\text{-}\epsilon$ in the free stream to eliminate sensitivity to inlet boundary turbulence levels."

### Q3: "What were the primary design trade-offs identified?"
> **Model Response**: "Deepening foundation caissons to mitigate scour involves exponential increases in excavation and dewatering CapEx. A parametric sensitivity study demonstrated that armoring the pier perimeter with an engineered riprap collar ($d_{50} = 300\text{ mm}$) reduced local shear stress by over 60%, mitigating structural scour risk while optimizing foundation capital cost."

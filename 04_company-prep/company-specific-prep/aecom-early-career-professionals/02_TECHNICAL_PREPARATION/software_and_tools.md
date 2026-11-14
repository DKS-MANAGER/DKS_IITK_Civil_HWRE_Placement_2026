# Digital Engineering, Modeling Software & Computational Tools

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27  
**Evidentiary Integrity:** Tools are classified into core engineering software utilized across AECOM GDC pods and candidate-demonstrated technical stacks.

---

## 1. Digital Engineering Ecosystem at AECOM

```
                      AECOM DIGITAL INFRASTRUCTURE SUITE
 ┌───────────────────────────────────┬───────────────────────────────────┐
 │ 1. Hydraulic & River Simulation   │ 2. BIM, CAD & Civil Infrastructure│
 │ • HEC-RAS (1D/2D Hydrodynamics)   │ • Autodesk Civil 3D (Corridors)   │
 │ • HEC-HMS (Catchment Runoff)      │ • Autodesk Revit (3D RCC / BIM)   │
 │ • EPA-SWMM (Urban Storm Drainage) │ • Bentley ProjectWise (CDE)       │
 │ • OpenFOAM (3D CFD & Scour)       │ • Navisworks (Clash Detection)    │
 ├───────────────────────────────────┼───────────────────────────────────┤
 │ 3. Geospatial & GIS Analytics     │ 4. Scientific Computing & Scripts │
 │ • ArcGIS Pro / QGIS               │ • Python (NumPy, SciPy, Pandas)   │
 │ • DEM Delineation & D8 Flow       │ • MATLAB (Hydraulic Modeling)     │
 │ • Spatial Watershed Extraction    │ • Excel / VBA Engineering Sheets  │
 └───────────────────────────────────┴───────────────────────────────────┘
```

---

## 2. Hydraulic & River Modeling Software

### 2.1 HEC-RAS (Hydrologic Engineering Center - River Analysis System)
The global civil engineering benchmark for open-channel hydrodynamics and flood hazard mapping.

#### 1D Steady Flow Modeling Mechanics
Solves the 1D Energy Equation using the **Standard Step Method**:
$$z_2 + y_2 + \frac{\alpha_2 V_2^2}{2g} = z_1 + y_1 + \frac{\alpha_1 V_1^2}{2g} + h_e$$
Where total head loss $h_e = h_f + h_o = L \bar{S}_f + C \left| \frac{\alpha_1 V_1^2}{2g} - \frac{\alpha_2 V_2^2}{2g} \right|$. Friction slope $\bar{S}_f$ is calculated using Manning's equation based on conveyance weighting:
$$K = \frac{1}{n} A R_h^{2/3}, \quad S_f = \left(\frac{Q}{K}\right)^2$$

#### 2D Hydrodynamic Modeling (Shallow Water Equations)
For complex floodplains, dam breaks, and coastal inundation, HEC-RAS solves the 2D Saint-Venant equations on unstructured computational meshes:
$$\frac{\partial H}{\partial t} + \nabla \cdot (H \mathbf{V}) = q$$
$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = -g \frac{\partial \eta}{\partial x} - \frac{\tau_{bx}}{\rho H} + \nu_t \nabla^2 u + f_c v$$
- **Diffusion Wave Approximation:** Neglects convective acceleration and turbulence terms; fast, stable, and accurate for slowly rising natural river inundation.
- **Full Shallow Water Equations (SWE):** Retains convective acceleration and eddy viscosity; required around bridge piers, spillways, sharp bends, and high-velocity transitions.

#### Bridge Modeling & Scour Calculations (HEC-18)
- Low Flow: Sluice gate, weir, or Yarnell energy equations.
- High Flow / Pressure Flow: Orifice equation $Q = C_d A \sqrt{2g \Delta H}$ when water level contacts the bridge low chord.
- Pier Scour: Evaluated using the **CSU Equation (FHWA HEC-18)**:
  $$\frac{y_s}{a} = 2.0 K_1 K_2 K_3 K_4 \left(\frac{y_1}{a}\right)^{0.35} Fr_1^{0.43}$$
  Where $a$ is pier width, $K_1$ is nose shape factor, $K_2$ is angle of attack factor, $K_3$ is bed condition factor, and $K_4$ is armoring factor.

---

### 2.2 HEC-HMS (Hydrologic Modeling System)
Simulates watershed rainfall-runoff processes:
- **Loss Methods:** SCS Runoff Curve Number ($S = \frac{25400}{CN} - 254$), Green-Ampt, Initial and Constant loss.
- **Transform Methods:** Clark Unit Hydrograph ($T_c, R$), Snyder Synthetic Unit Hydrograph, SCS Dimensionless Unit Hydrograph.
- **Routing Methods:** Muskingum, Muskingum-Cunge (physically based cross-section parameters), Modified Puls reservoir routing.

---

### 2.3 EPA-SWMM (Storm Water Management Model)
Dynamic rainfall-runoff simulation for urban pipe systems:
- Solves full 1D St. Venant equations (Dynamic Wave routing) in pipes and culverts, modeling backwater effects, flow reversal, pipe pressurization, and manhole surface ponding.
- Models Low Impact Development (LID) urban infrastructure: bio-retention swales, rain barrels, permeable pavement, and green roofs.

---

## 3. Computational Fluid Dynamics (OpenFOAM)

*(Candidate Thesis Core Anchor)*  
OpenFOAM is an open-source C++ framework solving continuum mechanics using the **Finite Volume Method (FVM)**.

### 3.1 Numerical Discretization Architecture
Integrates governing Navier-Stokes equations over arbitrary polyhedral control volumes $V_P$:

$$\int_{V_P} \nabla \cdot (\rho \phi \mathbf{U}) \, dV = \sum_{f} \rho_f \phi_f (\mathbf{U}_f \cdot \mathbf{S}_f)$$
- Surface integral evaluated across cell faces $f$ with area vector $\mathbf{S}_f$.
- Pressure-Velocity Coupling: Solved via the **PIMPLE Algorithm** (merged PISO-SIMPLE loop) handling unsteady transient flow with Courant numbers $Co = \frac{U \Delta t}{\Delta x} > 1$.

### 3.2 Multiphase Free-Surface Modeling (`interFoam`)
Tracks the interface between air and water using the **Volume of Fluid (VOF)** algebraic method:
$$\frac{\partial \alpha}{\partial t} + \nabla \cdot (\alpha \mathbf{U}) + \nabla \cdot (\alpha (1 - \alpha) \mathbf{U}_r) = 0$$
- $\alpha = 1$: Water; $\alpha = 0$: Air; $0 < \alpha < 1$: Free-surface interface.
- Compression term $\nabla \cdot (\alpha (1 - \alpha) \mathbf{U}_r)$ prevents artificial numerical smearing of the water surface.

### 3.3 Turbulence Closure Models
- **Menter's $k-\omega$ Shear Stress Transport (SST):**
  - Uses $k-\omega$ formulation in the near-wall boundary layer (captures adverse pressure gradients and boundary layer separation accurately without damping functions).
  - Switches smoothly to standard $k-\epsilon$ in the far-field free stream (eliminates extreme sensitivity to inlet turbulent boundary values).
- **Wall Treatment & Mesh Resolution ($y^+$):**
  $$y^+ = \frac{u_\tau y}{\nu}, \quad u_\tau = \sqrt{\frac{\tau_w}{\rho}}$$
  - Low-Re mesh: First cell height sized to $y^+ \le 1$ to resolve the viscous sublayer without empirical wall functions.

---

## 4. CAD, Civil 3D & Building Information Modeling (BIM)

### 4.1 Autodesk Civil 3D in Infrastructure Delivery
- **Surface Modeling (TIN Surfaces):** Triangulated Irregular Networks created from ground survey points, contour vectors, and LiDAR point clouds.
- **Alignment & Profile Geometry:** Defining horizontal alignments (tangents, circular curves, transition spirals) and vertical profiles (crest and sag parabolic curves complying with stopping sight distance SSD).
- **Corridor Modeling & Assembly:** Extruding parametric cross-section assemblies (carriageway, shoulders, side ditches, cut/fill daylight slopes) along an alignment.
- **Earthwork Cut & Fill Optimization:** Volume computation using the **Average End Area Method**:
  $$V = \frac{A_1 + A_2}{2} \times L$$

### 4.2 Building Information Modeling (BIM) & ISO 19650
AECOM projects operate under global BIM mandates:
- **Level of Development (LOD):**
  - *LOD 100:* Conceptual massing.
  - *LOD 200:* Approximate geometry and size.
  - *LOD 300:* Specific design geometry, reinforced concrete thicknesses, pipe diameters.
  - *LOD 400:* Fabrication details, rebar schedules, shop drawings.
- **Common Data Environment (CDE):** Centralized cloud repository (Bentley ProjectWise / Autodesk Construction Cloud) controlling drawing revisions, audit trails, and multidisciplinary clash detection via Navisworks.

---

## 5. Geospatial Analytics (ArcGIS & QGIS)

### 5.1 Hydrological Watershed Delineation Workflow
1. **DEM Preprocessing (Fill Sinks):** Eliminates localized spurious depressions in the Digital Elevation Model.
2. **Flow Direction (D8 Algorithm):** Evaluates steepest descent slope from center cell to 8 surrounding neighbor cells. Direction codes: $1 (\text{East}), 2 (\text{SE}), 4 (\text{South}), \dots, 128 (\text{NE})$.
3. **Flow Accumulation:** Counts total upstream cells draining into each cell.
4. **Stream Network Extraction:** Applies a threshold (e.g., cells with accumulation $> 1,000$) to delineate river centerlines.
5. **Watershed Pour Point Snapping:** Delineates exact contributing drainage basin area draining to a proposed bridge crossing or culvert location.

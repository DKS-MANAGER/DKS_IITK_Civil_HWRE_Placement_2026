# Technical Deep Dive: Hydrodynamic & Scour Modeling in Infrastructure Engineering
**Domain:** Hydraulics, Water Resources & Computational Fluid Dynamics (OpenFOAM & HEC-RAS)  
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Rigorous Technical Interview Defense & Viva Voce Grilling Guide  

---

## 1. Executive Summary & Engineering Motivation

During extreme flood events (such as 100-year or 500-year design floods), river stages can crest above the lower chord (soffit) or completely overtop bridge superstructures. When the superstructure becomes partially or fully submerged, the flow regime transitions abruptly from free-surface open-channel flow to **confined, pressurized orifice flow**. 

This transition induces acute downward flow deflection, intensive vortex shedding at the upstream leading edge, and drastic flow contraction beneath the bridge deck soffit. Consequently, bed shear stresses beneath the deck spike significantly above the critical Shields threshold, triggering aggressive localized scouring that undermines bridge foundations (piers, abutments, and shallow footings), leading to catastrophic structural collapse.

This technical case study explores the three-dimensional hydrodynamic mechanisms and geometry-dependent scour evolution beneath submerged bridge decks using high-resolution Computational Fluid Dynamics (CFD) in OpenFOAM, validated against experimental flume observations. It serves as a comprehensive technical defense framework for engineering interviews.

---

## 2. Mathematical Governing Equations & Physics

### 2.1 Reynolds-Averaged Navier-Stokes (RANS) Equations
For 3D incompressible turbulent fluid flow, mass conservation (continuity) and momentum conservation are expressed in tensor notation:

$$\frac{\partial u_i}{\partial x_i} = 0$$

$$\frac{\partial (\rho u_i)}{\partial t} + \frac{\partial (\rho u_i u_j)}{\partial x_j} = -\frac{\partial p}{\partial x_i} + \frac{\partial}{\partial x_j} \left[ \mu \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right) - \rho \overline{u'_i u'_j} \right] + \rho g_i$$

where:
- $u_i$ is the time-averaged velocity vector $(u, v, w)$.
- $p$ is static pressure.
- $\rho$ is fluid density ($1000\text{ kg/m}^3$ for water).
- $\mu$ is dynamic molecular viscosity ($1.0 \times 10^{-3}\text{ Pa}\cdot\text{s}$).
- $-\rho \overline{u'_i u'_j}$ is the Reynolds stress tensor representing turbulent momentum transport.

### 2.2 Turbulence Closure: Menter $k-\omega$ Shear Stress Transport (SST)
The Boussinesq eddy viscosity hypothesis models Reynolds stress as:
$$-\rho \overline{u'_i u'_j} = \mu_t \left( \frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i} \right) - \frac{2}{3}\rho k \delta_{ij}$$

The **Menter $k-\omega$ SST model** is selected because it blends two formulations:
1. The Wilcox $k-\omega$ model in the inner boundary layer, avoiding non-physical turbulence overproduction in stagnation zones and accurately resolving adverse pressure gradient separation.
2. The standard $k-\varepsilon$ model in the outer wake and free-stream, eliminating the high sensitivity of Wilcox $k-\omega$ to free-stream boundary conditions.

The blending is achieved via hyperbolic tangent blending functions $F_1$ and $F_2$:
- **Turbulent Kinetic Energy ($k$):**
  $$\frac{\partial (\rho k)}{\partial t} + \frac{\partial (\rho u_j k)}{\partial x_j} = P_k - \beta^* \rho k \omega + \frac{\partial}{\partial x_j} \left[ (\mu + \sigma_k \mu_t) \frac{\partial k}{\partial x_j} \right]$$
- **Specific Dissipation Rate ($\omega$):**
  $$\frac{\partial (\rho \omega)}{\partial t} + \frac{\partial (\rho u_j \omega)}{\partial x_j} = \frac{\gamma}{\nu_t} P_k - \beta \rho \omega^2 + \frac{\partial}{\partial x_j} \left[ (\mu + \sigma_\omega \mu_t) \frac{\partial \omega}{\partial x_j} \right] + 2(1 - F_1)\frac{\rho \sigma_{\omega 2}}{\omega} \frac{\partial k}{\partial x_j}\frac{\partial \omega}{\partial x_j}$$
- **Eddy Viscosity with Shear Stress Limiter:**
  $$\mu_t = \frac{\rho a_1 k}{\max(a_1 \omega, \Omega F_2)}$$
  where $\Omega$ is the vorticity magnitude. This limiter prevents non-physical over-prediction of eddy viscosity in high strain-rate zones near the submerged bridge deck corners.

### 2.3 Free-Surface Tracking: Volume of Fluid (VOF) Method
In OpenFOAM's `interFoam` solver, the water-air interface is captured using an algebraic Volume of Fluid method based on the phase fraction field $\alpha$:
- $\alpha = 1$: Cell fully occupied by water.
- $\alpha = 0$: Cell fully occupied by air.
- $0 < \alpha < 1$: Interface cell.

The transport equation for $\alpha$ contains an artificial compressive convective term:
$$\frac{\partial \alpha}{\partial t} + \nabla \cdot (\alpha \mathbf{u}) + \nabla \cdot \left[ \alpha (1 - \alpha) \mathbf{u}_r \right] = 0$$
where $\mathbf{u}_r = \mathbf{u}_{\text{water}} - \mathbf{u}_{\text{air}}$ is the relative compressive velocity perpendicular to the interface, maintaining sharp free-surface resolution without numerical diffusion.

Continuum Surface Force (CSF) model adds surface tension force at the free surface:
$$f_\sigma = \sigma \kappa \nabla \alpha$$
where $\kappa = -\nabla \cdot \left( \frac{\nabla \alpha}{|\nabla \alpha|} \right)$ is the interface curvature.

---

## 3. Numerical Setup & OpenFOAM Architecture

### 3.1 Computational Domain & Boundary Conditions
1. **Domain Geometry:**
   - Channel flume dimensions: Length $L = 14\text{ m}$, Width $W = 0.80\text{ m}$, Depth $H = 0.60\text{ m}$.
   - Submerged bridge deck located at $X = 5.0\text{ m}$ downstream of inlet to ensure fully developed turbulent open channel flow.
   - Downstream reach $= 9.0\text{ m}$ to allow full wake dissipation and prevent artificial numerical reflection from the outlet.
2. **Boundary Conditions (BCs):**
   - **Inlet:**
     - Velocity $\mathbf{u}$: `variableHeightFlowRateInletVelocity` (or mapped 1D velocity profile).
     - Phase $\alpha$: Fixed water level stage.
     - Turbulence: $k = \frac{3}{2}(I \cdot U_{\text{in}})^2$, $\omega = \frac{k^{1/2}}{C_\mu^{1/4} L_t}$.
   - **Outlet:**
     - Pressure: `prghPressure` set to 0.
     - Phase $\alpha$: `zeroGradient`.
     - Velocity: `inletOutlet` (preventing reverse flow instability).
   - **Atmosphere (Top Boundary):**
     - Pressure: `totalPressure` ($p_0 = 0\text{ Pa}$).
     - Velocity: `pressureInletOutletVelocity`.
     - Phase $\alpha$: `inletOutlet` with ambient air fraction 0.
   - **Bridge Deck & Pier Surfaces:**
     - Velocity: `noSlip` ($\mathbf{u} = 0$).
     - Near-wall treatment: Fully resolved mesh with $y^+ \le 1.0$ (direct integration to wall without empirical wall functions).
   - **Channel Bed (Sediment Surface):**
     - Fixed rough wall: `noSlip` with roughness parameters ($k_s = d_{50}$).

### 3.2 Spatial Discretization & Solver Coupling
1. **Time Integration:** Second-order backward implicit (`Euler` / `backward`).
2. **Convective Divergence Schemes:**
   - Momentum ($\nabla \cdot (\rho \mathbf{u} \mathbf{u})$): `Gauss linearUpwind grad(U)` (second-order upwind, bounded).
   - Turbulence ($\nabla \cdot (\rho \mathbf{u} k)$): `Gauss limitedLinear 1`.
   - Phase fraction ($\nabla \cdot (\mathbf{u} \alpha)$): `Gauss vanLeer` (Total Variation Diminishing / TVD).
3. **Pressure-Velocity Coupling:** PIMPLE algorithm (merging PISO and SIMPLE):
   - Outer correctors: 2 to 3 iterations for non-linear coupling.
   - Inner pressure correctors: 3 iterations for orthogonal pressure correction.
   - Courant-Friedrichs-Lewy (CFL) constraint: Max $Co \le 0.80$ with adaptive time-stepping ($\Delta t \approx 10^{-4}$ to $10^{-3}\text{ s}$).

### 3.3 Mesh Sensitivity & Grid Convergence Index (GCI)
To guarantee spatial discretization error independence under ASME V&V 20 guidelines, three systematically refined hexahedral meshes were evaluated:
- **Coarse Mesh ($N_3$):** 650,000 cells ($h_3 = 1.6\text{ mm}$ near deck).
- **Medium Mesh ($N_2$):** 1,850,000 cells ($h_2 = 1.0\text{ mm}$ near deck).
- **Fine Mesh ($N_1$):** 4,920,000 cells ($h_1 = 0.65\text{ mm}$ near deck).
- Grid refinement ratio $r_{21} = h_2 / h_1 \approx 1.54$, $r_{32} = h_3 / h_2 \approx 1.60$.
- Order of convergence $p \approx 1.88$ (close to theoretical 2nd-order accuracy).
- Calculated fine-grid GCI for peak bed shear stress $\tau_{\max}$:
  $$GCI_{21} = \frac{1.25 |e_{21}|}{r_{21}^p - 1} \approx 2.4\%$$
  confirming that numerical spatial discretization uncertainty is well below $3\%$.

---

## 4. Scour Hydrodynamics & Key Research Findings

### 4.1 Dimensionless Governing Parameters
The scour depth $d_s$ beneath submerged bridge decks is governed by the following non-dimensional ratios:
1. **Deck Submergence Ratio ($S^*$):**
   $$S^* = \frac{S}{y_0} = \frac{h_{\text{water}} - h_{\text{soffit}}}{y_0}$$
   where $S$ is the submergence depth of the deck soffit below the upstream water level, and $y_0$ is approach flow depth.
2. **Channel Blockage Ratio ($B^*$):**
   $$B^* = \frac{H_{\text{deck}}}{y_0}$$
   representing the frontal obstruction area relative to approach flow depth.
3. **Aspect Ratio of Deck:**
   $$AR = \frac{W_{\text{deck}}}{H_{\text{deck}}}$$
   (ratio of deck stream-wise width to deck vertical thickness).
4. **Approach Froude Number:**
   $$Fr = \frac{V_0}{\sqrt{g y_0}}$$

### 4.2 Hydrodynamic Flow Regimes
The research uncovered three distinct flow regimes as the submergence ratio $S^*$ increases:
1. **Regime I: Free-Surface Impingement ($S^* \approx 0 - 0.2$):**
   - Deck lower chord touches the water surface.
   - Significant bow-wave pile-up upstream; standing waves shed over the deck top.
   - Flow underneath accelerates moderately as an open throat.
2. **Regime II: Fully Pressurized Orifice Flow ($S^* = 0.2 - 0.8$):**
   - Deck is completely submerged, acting as a submerged orifice sluice.
   - Strong flow contraction beneath the deck lower chord with a well-defined *vena contracta*.
   - Intense downward vertical velocity component ($w$) accelerates bottom bed velocity up to $2.2 \times V_0$.
   - Bed shear stress reaches its global maximum ($\tau_b \approx 3.8 \times \tau_{\text{critical}}$), producing rapid scour hole development directly beneath and slightly downstream of the deck upstream edge.
3. **Regime III: Deep Submergence Overflow Dominance ($S^* > 1.0$):**
   - The majority of flood discharge passes over the top of the bridge deck.
   - The flow beneath the deck acts as a restricted bypass channel; local pressure gradient drops, reducing bed shear stress and attenuating equilibrium scour depth.

---

## 5. Technical Grilling: 20 Advanced Interview Q&A

### Q1: Why did you choose the $k-\omega$ SST model over the standard $k-\varepsilon$ or Realizable $k-\varepsilon$ model?
**Answer:**  
"Standard and Realizable $k-\varepsilon$ models rely on wall functions and notoriously over-predict turbulent kinetic energy $k$ in stagnation zones where the flow impinges on the upstream face of the bridge deck. This non-physical over-prediction artificially inflates turbulent eddy viscosity $\mu_t$, which delays boundary layer separation and dampens the vortex shedding beneath the soffit. In contrast, the Menter $k-\omega$ SST model utilizes the Wilcox $k-\omega$ formulation in the inner boundary layer without wall functions, which resolves adverse pressure gradients accurately, coupled with a shear stress limiter that bounds eddy viscosity in high strain-rate zones."

### Q2: What was the $y^+$ value across your bridge deck and channel bed, and why does it matter?
**Answer:**  
"The non-dimensional wall distance $y^+ = \frac{u_\tau y}{\nu}$ determines the location of the first computational cell center relative to the viscous sublayer. For our simulations, we maintained $y^+ \le 1.0$ across the bridge deck surfaces and $y^+ \approx 1 - 2$ on the bed. This allowed us to resolve the viscous sublayer directly without empirical wall functions. If $y^+$ exceeded 30–300 (standard log-law region), empirical wall functions would assume zero pressure gradient along the wall, completely failing to capture the intense flow separation and recirculation vortices generated at the sharp leading edge of the deck."

### Q3: How did you handle the free-surface modeling in OpenFOAM? Why not use a rigid lid approximation?
**Answer:**  
"A rigid lid approximation imposes a symmetry or slip condition at a fixed horizontal plane, which assumes that the water surface does not deform. However, during bridge deck submergence, significant free-surface deformation occurs: bow waves pile up upstream, a draw-down dip forms above the bridge deck, and hydraulic jumps or standing waves can develop downstream. By using the Volume of Fluid (VOF) method in `interFoam`, we captured these dynamic free-surface deformations and their feedback on upstream backwater afflux and pressurized orifice head."

### Q4: Explain the artificial interface compression term in the VOF transport equation.
**Answer:**  
"Standard VOF advection schemes suffer from numerical diffusion, which causes the water-air interface to blur over multiple cells. OpenFOAM solves this using the Weller interface compression formulation:
$$\nabla \cdot \left[ \mathbf{u}_r \alpha (1 - \alpha) \right]$$
The factor $\alpha (1 - \alpha)$ is active strictly at the interface where $0 < \alpha < 1$ and vanishes in pure water ($\alpha = 1$) and pure air ($\alpha = 0$). The relative velocity $\mathbf{u}_r$ is directed normal to the interface, acting as an artificial convective flux that squeezes the interface into a sharp boundary spanning only 1 to 2 cells."

### Q5: What was your maximum Courant number, and why was it constrained?
**Answer:**  
"We constrained the maximum Courant number to $Co = \frac{|\mathbf{u}| \Delta t}{\Delta x} \le 0.80$, with an additional interface Courant number limiter $Co_{\alpha} \le 0.50$ in the multi-phase VOF solver. Because the MULES (Multidimensional Universal Limiter with Explicit Solution) algorithm in `interFoam` treats interface compression explicitly, exceeding $Co > 1.0$ causes interface instability, non-physical phase fraction unboundedness ($\alpha < 0$ or $\alpha > 1$), and mass conservation divergence."

### Q6: How does the presence of bridge deck girders (I-girders vs box girders) alter the scour pattern?
**Answer:**  
"Bridge deck geometry has a profound effect on scour. An aerodynamic, streamlined box girder produces smoother flow separation with smaller recirculation zones beneath the soffit. Conversely, multi-I-girder superstructures trap air and water pockets between longitudinal girders. The first upstream girder acts as a blunt bluff body, shedding periodic hairpin vortices downward towards the bed. This creates a multi-peaked bed shear stress distribution and increases the equilibrium scour depth by $25 - 35\%$ compared to a solid box girder of identical depth."

### Q7: How did you compute the bed shear stress from your OpenFOAM velocity field?
**Answer:**  
"Because the near-wall mesh was resolved down to $y^+ \le 1.0$, the bed shear stress $\tau_b$ was extracted directly from the velocity gradient in the laminar sublayer:
$$\tau_b = \mu \left. \frac{\partial u}{\partial y} \right|_{y=0}$$
In OpenFOAM, this is evaluated using the `wallShearStress` post-processing utility, which calculates the tangential stress tensor vector:
$$\boldsymbol{\tau}_w = \mu_{\text{eff}} (\nabla \mathbf{u} + (\nabla \mathbf{u})^T) \cdot \mathbf{n} - \left[ (\mu_{\text{eff}} (\nabla \mathbf{u} + (\nabla \mathbf{u})^T) \cdot \mathbf{n}) \cdot \mathbf{n} \right] \mathbf{n}$$
where $\mathbf{n}$ is the unit normal vector to the bed surface and $\mu_{\text{eff}} = \mu + \mu_t$."

### Q8: How did you link the CFD bed shear stress to actual sediment scour without running a fully coupled dynamic morphodynamic bed solver?
**Answer:**  
"We employed an excess shear stress formulation based on the Shields criterion. By comparing the local bed shear stress $\tau_b(x, z)$ against the critical shear stress $\tau_c$ calculated for the sediment median grain diameter ($d_{50} = 0.45\text{ mm}$):
$$\tau_c = \theta_c (\rho_s - \rho_w) g d_{50}$$
Whenever $\tau_b > \tau_c$, sediment entrainment occurs. We integrated the excess shear stress ratio $\frac{\tau_b - \tau_c}{\tau_c}$ along the stream-wise profile to identify the zones of maximum erosion potential, validating the location and relative depth against our laboratory flume physical measurements."

### Q9: What boundary condition did you apply at the outlet to prevent numerical reflections?
**Answer:**  
"We applied `prghPressure` with a fixed value of 0 on the outlet face for the modified pressure $p_{\text{rgh}} = p - \rho \mathbf{g} \cdot \mathbf{r}$, combined with an `inletOutlet` boundary condition for velocity. The `inletOutlet` condition functions as a zero-gradient Neumann condition when flow is exiting the domain, but switches to a fixed zero-velocity condition if any backflow or reverse vortex attempts to enter the domain, suppressing numerical reflections."

### Q10: How did you validate your CFD simulation against physical experimental data?
**Answer:**  
"We validated the CFD model using physical flume experiments conducted in a $14\text{ m} \times 0.8\text{ m} \times 0.6\text{ m}$ glass-sided tilting flume. Velocity profiles were measured at multiple cross-sections upstream, beneath, and downstream of the deck using an Acoustic Doppler Velocimeter (ADV). Free-surface profiles were captured using digital ultrasonic stage gauges. The CFD model predicted stream-wise velocity $u(y)$ within an $R^2$ of $0.94$ and free-surface elevations within $3.5\text{ mm}$ root-mean-square error (RMSE)."

### Q11: What is the PIMPLE algorithm, and why did you choose it over PISO or SIMPLE?
**Answer:**  
"SIMPLE is an iterative algorithm designed for steady-state flows, while PISO is a non-iterative predictor-corrector scheme designed for transient flows requiring very small time steps ($Co \ll 1$). PIMPLE combines both: in each time step, it executes multiple outer SIMPLE correction loops to resolve non-linearities and strong cross-coupling between pressure, momentum, and phase fraction, while inner PISO correctors ensure orthogonal mass conservation. This allowed us to run transient multi-phase simulations with Courant numbers up to $0.80$ without compromising stability."

### Q12: How did you ensure your computational mesh was high quality in snappyHexMesh?
**Answer:**  
"We enforced strict mesh quality metrics inside `meshQualityDict`:
1. Maximum non-orthogonality $< 65^\circ$ (average $< 20^\circ$).
2. Maximum cell skewness $< 3.5$.
3. Positive volume fraction ($100\%$ zero inverted cells).
4. Smooth volume expansion ratios $\le 1.20$ between adjacent cell refinement levels.
We added 5 prism boundary layers around the bridge deck with a first-layer thickness of $0.08\text{ mm}$ and an expansion ratio of $1.15$ to achieve $y^+ \le 1.0$."

### Q13: What is the Grid Convergence Index (GCI), and what was your calculated numerical uncertainty?
**Answer:**  
"The Grid Convergence Index (GCI), formulated by Roache and standardized in ASME V&V 20, provides an objective measure of numerical discretization error based on generalized Richardson extrapolation. By comparing solutions across coarse ($N_3$), medium ($N_2$), and fine ($N_1$) systematically refined grids, GCI estimates the percentage difference between the fine-grid solution and the asymptotic continuum zero-grid-spacing solution. Our fine-grid GCI was $2.4\%$, confirming asymptotic convergence."

### Q14: What is the physical mechanism causing the 'pressure flow' transition beneath a submerged deck?
**Answer:**  
"Under normal open channel conditions, the flow has a free surface where atmospheric pressure is constant ($p = 0$). When the bridge deck soffit is reached by rising water, the water-air interface is replaced by a rigid solid boundary. The hydraulic gradient, which was previously governed by channel bed slope and gravity, is now governed by the upstream backwater pressure head. Water accelerates through the constricted throat like an orifice, converting potential head into kinetic energy and generating steep velocity gradients at the bed."

### Q15: How did you define the deck submergence ratio $S^*$ and blockage ratio $B^*$?
**Answer:**  
"Deck submergence ratio $S^* = \frac{S}{y_0} = \frac{H_w - H_{\text{soffit}}}{y_0}$, where $H_w$ is upstream water surface elevation, $H_{\text{soffit}}$ is the bottom elevation of the bridge deck, and $y_0$ is approach depth. Blockage ratio $B^* = \frac{H_{\text{deck}}}{y_0}$, where $H_{\text{deck}}$ is total vertical depth of the superstructure. $S^* = 0$ corresponds to incipient soffit contact, $0 < S^* < 1$ represents partial deck submergence, and $S^* > 1$ represents complete superstructure overtopping."

### Q16: How do bridge piers alter the scour pattern when combined with deck submergence?
**Answer:**  
"When bridge piers are present beneath a submerged deck, a compound 3D scour phenomenon occurs. The pier generates a horseshoe vortex at its base and wake vortices behind it, while the submerged deck accelerates horizontal flow downward. These two flow structures interact non-linearly: the downward jet from the deck intensifies the circulation strength of the pier horseshoe vortex, shifting the maximum scour hole deeper and slightly upstream of the pier nose, increasing total scour depth by up to $40\%$ compared to an isolated pier."

### Q17: If AECOM is designing a bridge across an alluvial river, how does this hydrodynamic research inform our engineering design?
**Answer:**  
"In standard highway practice under IRC:78 or FHWA HEC-18, bridge foundation scour depth is calculated using empirical formulas that assume either open-channel pier scour or isolated pressure flow. However, during extreme overtopping events, these empirical formulas either severely underestimate scour due to vortex-jet coupling, or result in over-conservative, cost-prohibitive pile foundation depths. Applying 3D CFD provides a physically grounded methodology to evaluate the exact velocity acceleration, shear stress amplification, and scour vulnerability for site-specific deck shapes, allowing design teams to develop optimized, defensible riprap aprons and foundation embedment depths."

### Q18: What are the computational hardware requirements and run times for such OpenFOAM simulations?
**Answer:**  
"The simulations are typically executed on a High-Performance Computing (HPC) cluster using OpenFOAM's `decomposePar` utility with the `scotch` domain decomposition method across 32 MPI cores. A typical transient run of 60 physical seconds on a 4.9-million cell mesh requires approximately 36 to 48 hours of wall-clock computational time, saving checkpoint fields at $0.1\text{ s}$ intervals."

### Q19: What was the most challenging numerical instability encountered, and how is it resolved?
**Answer:**  
"The most difficult numerical issue is **high-frequency pressure oscillations and phase-fraction bounding errors** occurring at sharp deck edges during initial flow impingement. The abrupt velocity direction change produces high local Courant numbers and cell face flux divergences. This is resolved by:
1. Refining the prism boundary layer grid with smooth expansion transitions ($\le 1.15$).
2. Enabling non-orthogonal pressure correctors (`nNonOrthogonalCorrectors 2`) in `fvSolution`.
3. Applying a relaxation factor of $0.7$ on the pressure equation.
4. Implementing an adaptive time-step algorithm with a maximum CFL constraint of $0.80$."

### Q20: How can this computational framework be extended for future engineering projects?
**Answer:**  
"The framework can be expanded in two high-impact industry directions:
1. **Dynamic Morphodynamic Bed Coupling:** Implement a coupled Two-Phase Euler-Euler granular sediment transport model (such as `sedFoam`) to simulate real-time transient scour hole evolution with dynamic mesh deformation (`dynamicMesh / moveMesh`), capturing the feedback between deepening scour holes and decaying bed shear stress.
2. **Climate Change Overtopping Risk & Debris Loading:** Model the hydrodynamic impact of large woody debris (trees, logs) trapped against the upstream face of the submerged deck, which increases the effective blockage ratio $B^*$ and drastically worsens localized scour."

---
*End of Technical Project Deep Dive Guide.*

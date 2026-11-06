# Module 14: Technical Interview Question Bank — 17 Comprehensive Tracks

> **Document Focus**: 17 Core Hydraulic Engineering Disciplines, Three Competency Tiers (Foundational, Intermediate, Advanced), Worked Derivations, Common Traps, and Follow-up Probes  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY CODES & TIER 3 / CANDIDATE INTERVIEW DEBRIEFS]`  

---

## 1. Interview Architecture & Evaluation Standards

Technical interviews at AFRY India are conducted by Lead Hydraulic Engineers, Project Managers, and Technical Directors from the Noida Delivery Hub. Rather than asking for textbook definitions, panels test:
1. **First-Principles Derivations**: Can the candidate draw a control volume on a whiteboard and derive the governing equations without memorization?
2. **Physical Engineering Intuition**: Does the candidate understand the physical meaning of mathematical terms (e.g., Coriolis coefficient $\alpha$, Boussinesq $\beta$, Courant number, or Thoma stability)?
3. **Practical Troubleshooting**: How does the candidate handle software warnings in HEC-RAS or cavitation transients in Bentley HAMMER?
4. **Honesty on Experience**: Transparently explaining what was learned academically vs. what will be executed on the job.

---

## 2. Topic 1: Fluid Mechanics & Hydrodynamics

#### Q01 [Foundational: Navier-Stokes vs. 1D Hydraulic Equations]
* **Question**: How do the 1D open-channel and closed-conduit hydraulic equations relate fundamentally to the 3D Navier-Stokes equations?
* **Expected Answer**: The 1D Saint-Venant and pipe momentum equations are derived by spatially integrating (cross-sectional area-averaging) the 3D Reynolds-Averaged Navier-Stokes (RANS) equations along the primary flow streamline, invoking the boundary layer and shallow-water approximations where lateral and vertical velocity components are small compared to the longitudinal velocity.
* **Relevant Equations**:
  $$\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} = -\frac{1}{\rho}\nabla p + \nu \nabla^2 \mathbf{u} + \mathbf{g}$$
* **Common Mistake**: Believing 1D equations are completely separate empirical empirical equations rather than depth-integrated forms of the Navier-Stokes equations.
* **Follow-up Probe**: *"What happens to the shear stress tensor term $\nabla \cdot \tau$ during 1D area averaging?"* (Answer: It converts via the divergence theorem into perimeter boundary shear stress $\tau_0 P$).

---

## 3. Topic 2: Open-Channel Flow Fundamentals

#### Q02 [Intermediate: Derivation of Critical Depth Condition]
* **Question**: Prove mathematically that the minimum specific energy for a given discharge occurs when the Froude number equals unity ($Fr = 1$).
* **Expected Answer**: Write specific energy $E = y + \frac{Q^2}{2 g A^2}$. Differentiate with respect to $y$ at constant $Q$:
  $$\frac{dE}{dy} = 1 - \frac{Q^2}{g A^3}\frac{dA}{dy} = 0$$
  Since $dA = T dy$ (where $T$ is top water width):
  $$\frac{Q^2 T_c}{g A_c^3} = 1 \iff \frac{v_c^2}{g (A_c / T_c)} = \frac{v_c^2}{g D_{hc}} = 1 \iff Fr = 1 \quad \blacksquare$$
* **Practical Example**: Sizing canal drop structures and setting upstream control flumes.
* **Common Mistake**: Confusing hydraulic radius $R = A/P$ with hydraulic depth $D_h = A/T$ in the Froude number formula.
* **Follow-up Probe**: *"Is critical flow stable in real rivers?"* (Answer: No, the surface is inherently wavy and unstable because $dE/dy = 0$, meaning infinitesimal energy perturbations create large depth fluctuations).

---

## 4. Topic 3: Gradually Varied Flow & Water Surface Profiles

#### Q03 [Advanced: GVF Profile Upstream of a Reservoir]
* **Question**: A dam is constructed across a river with a mild slope ($y_0 > y_c$). What water surface profile forms upstream of the dam, and why?
* **Expected Answer**: An **M1 backwater profile** forms.
  * *Reasoning*: The dam raises the water depth above normal depth ($y > y_0 > y_c$).
  * *Mathematical Proof*: From the GVF equation:
    $$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$$
    Since $y > y_0 \implies S_f < S_0 \implies (S_0 - S_f) > 0$.
    Since $y > y_c \implies Fr < 1 \implies (1 - Fr^2) > 0$.
    Therefore, $\frac{dy}{dx} = \frac{+}{+} > 0$. Depth increases in the downstream direction as flow approaches the dam pool.
* **Common Mistake**: Stating that depth increases upstream (misunderstanding the coordinate system where $x$ is positive downstream).

---

## 5. Topic 4: River Rating Curves & Hysteresis

#### Q04 [Intermediate: The Loop Rating Curve Phenomenon]
* **Question**: Why does a river gauging station record higher discharge during the rising limb of a flood than at the exact same recorded stage during the falling limb?
* **Expected Answer**: Due to **hydraulic hysteresis** governed by the water surface slope in the Saint-Venant momentum equation:
  $$S_f = S_0 - \frac{\partial y}{\partial x} - \frac{v}{g}\frac{\partial v}{\partial x} - \frac{1}{g}\frac{\partial v}{\partial t}$$
  During the rising stage, the front of the flood wave steepens the water surface ($\partial y / \partial x < 0$), creating an energy slope $S_f > S_0$. Higher surface gradient produces higher velocity and discharge. During the falling stage, $\partial y / \partial x > 0 \implies S_f < S_0$, yielding lower velocity and discharge.
* **Follow-up Probe**: *"How does HEC-RAS steady flow handle this?"* (Answer: HEC-RAS steady flow cannot capture loop rating curves; it assumes a unique single-valued stage-discharge curve. Capturing hysteresis requires an unsteady flow simulation).

---

## 6. Topic 5: Unsteady Open-Channel Flow & Saint-Venant Equations

#### Q05 [Advanced: Kinematic vs. Diffusion vs. Dynamic Wave Selection]
* **Question**: In what engineering scenarios is a Kinematic wave model valid, and when must AFRY deploy a full Dynamic wave model?
* **Expected Answer**:
  * *Kinematic Wave ($S_f = S_0$)*: Valid on steep slopes ($S_0 > 0.002$), steep upland streams, and overland urban runoff where inertial and pressure forces are negligible compared to bed slope gravity. Wave propagates without peak attenuation.
  * *Full Dynamic Wave (Complete Saint-Venant)*: Mandatory in flat river reaches ($S_0 < 0.0005$), tidally influenced estuaries, reservoirs where backwater controls flow, around bridge constrictions, and during rapid dam-break surges where local acceleration ($\partial v / \partial t$) and pressure gradients ($\partial y / \partial x$) dominate.

---

## 7. Topic 6: Closed-Conduit Pipe Hydraulics

#### Q06 [Foundational: Darcy-Weisbach vs. Hazen-Williams]
* **Question**: Why does AFRY insist on the Darcy-Weisbach equation over the Hazen-Williams formula for hydropower penstocks and cooling water pipelines?
* **Expected Answer**:
  1. *Dimensional Rigor*: Darcy-Weisbach is dimensionally homogeneous and derived from physical boundary layer mechanics ($h_f = f \frac{L}{D}\frac{v^2}{2g}$).
  2. *Fluid & Temperature Flexibility*: Hazen-Williams is an empirical formula calibrated exclusively for water at $20^\circ\text{C}$ and fails for cold meltwater ($4^\circ\text{C}$) or thermal discharge where viscosity changes.
  3. *Roughness Independence*: Hazen-Williams coefficient $C$ assumes flow is always in the transition turbulent regime, failing for smooth pipes at low $Re$ and fully rough conduits at high $Re$.

---

## 8. Topic 7: Head-Loss Calculations (Major & Minor)

#### Q07 [Intermediate: The Colebrook-White Implicit Solution]
* **Question**: Write down the Colebrook-White equation. How do you solve it in practice, and what explicit formula do you use to verify it?
* **Expected Answer**:
  $$\frac{1}{\sqrt{f}} = -2 \log_{10}\left( \frac{\epsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
  Because $f$ appears on both sides, it is solved iteratively via Newton-Raphson. In practice, the **Swamee-Jain explicit formula** is used as an initial seed and verification check:
  $$f \approx \frac{0.25}{\left[\log_{10}\left(\frac{\epsilon/D}{3.7} + \frac{5.74}{Re^{0.9}}\right)\right]^2}$$
* **Common Mistake**: Forgetting that Swamee-Jain uses base-10 logarithm ($\log_{10}$), not natural log ($\ln$).

---

## 9. Topic 8: Water Hammer & Pressure Surges

#### Q08 [Advanced: Joukowsky Equation Derivation & Assumptions]
* **Question**: Derive the Joukowsky equation from first principles and state its critical physical assumptions.
* **Expected Answer**:
  * *Derivation*: Consider an acoustic compression wave moving upstream at speed $a$ following instantaneous valve closure. In time $\Delta t$, mass of decelerated fluid is $\Delta m = \rho A a \Delta t$.
    Momentum equation:
    $$\Delta P \cdot A \cdot \Delta t = \Delta m \cdot \Delta v = (\rho A a \Delta t) \Delta v \implies \Delta P = \rho a \Delta v \implies \Delta H = \frac{a \Delta v}{g}$$
  * *Assumptions*:
    1. Instantaneous or rapid closure ($t_c \le 2L/a$).
    2. Fluid and conduit deform elastically.
    3. 1D acoustic plane wave propagation.
    4. Friction loss along pipe is neglected during initial wave transit.

---

## 10. Topic 9: Mass Oscillation & Surge Tanks

#### Q09 [Advanced: The Thoma Stability Criterion]
* **Question**: What is the physical mechanism behind the Thoma stability criterion for hydropower surge tanks?
* **Expected Answer**: Hydraulic turbine governors operate under constant electrical power demand ($P = \eta \rho g Q H = \text{const}$). When water level in the surge tank drops during a downward surge oscillation, net head on the turbine drops ($H \to H - \Delta z$). The governor responds by opening guide vanes to draw *more* discharge ($Q \propto 1/H$). Withdrawing more water when the tank level is already depressed acts as a **destabilizing negative damping force**.
  To ensure oscillations decay asymptotically, the surge tank area must exceed the Thoma critical area:
  $$A_T > F_{Th} = \frac{L A_t}{2 g C H_0 H_{net}}$$
  AFRY guidelines mandate an operational safety factor of $1.50 \text{ to } 1.80 \times F_{Th}$.

---

## 11. Topic 10: Spillways (Ogee, Sluice, Broad-Crested)

#### Q10 [Intermediate: Sub-atmospheric Pressures on Ogee Spillways]
* **Question**: What happens to crest pressures when the reservoir head exceeds the design head ($H > H_d$) on an ogee spillway?
* **Expected Answer**: When $H > H_d$, the flowing sheet of water has greater inertial trajectory than the curvature of the concrete crest. The water attempts to lift away from the surface, creating **sub-atmospheric (negative gauge) pressures**.
  * *Effect*: Negative pressures increase the effective head, increasing the discharge coefficient ($C_d > C_{d0}$).
  * *Danger*: If negative pressure heads drop below $-4.0\text{ m to } -6.0\text{ m}$ of water, **cavitation pitting erosion** occurs, destroying concrete armor and causing dangerous vibrations.
  * *Design Rule*: The ratio of maximum flood head to design head must never exceed $H / H_d \le 1.33$.

---

## 12. Topic 11: Energy Dissipation Systems

#### Q11 [Intermediate: USBR Type II vs. Type III Stilling Basins]
* **Question**: Why are baffle piers strictly omitted in USBR Type II stilling basins, while they are included in USBR Type III basins?
* **Expected Answer**:
  * *USBR Type II* is engineered for **high-head dams** where incoming supercritical velocity exceeds $v_1 > 15 \text{ to } 18\text{ m/s}$. At these velocities, localized flow separation around intermediate baffle piers creates intense sub-atmospheric vortices, leading to catastrophic **cavitation destruction of the piers**. Energy dissipation relies strictly on chute blocks and a dentated end sill.
  * *USBR Type III* is used on **low-head dams and canals** where velocities are low ($v_1 \le 15\text{ m/s}$), below the cavitation threshold. Baffle piers are safely installed to impact the jet, reducing required basin length by $60\%$.

---

## 13. Topic 12: Hydraulic Model Studies & Similitude

#### Q12 [Foundational: Derivation of Froude Discharge Scale Ratio]
* **Question**: Derive the discharge scale ratio $Q_r$ for a 1:50 scale undistorted physical model governed by Froude similitude.
* **Expected Answer**:
  * Under Froude law, $Fr_r = 1 \implies \frac{v_r}{\sqrt{g_r L_r}} = 1$. Since $g_r = 1 \implies v_r = L_r^{1/2}$.
  * Flow area scales geometrically: $A_r = L_r^2$.
  * Discharge ratio:
    $$Q_r = A_r v_r = (L_r^2)(L_r^{1/2}) = L_r^{5/2} = L_r^{2.5}$$
  * For $L_r = 50$: $Q_r = 50^{2.5} = 50^2 \times \sqrt{50} = 2,500 \times 7.071 = \mathbf{17,677.67}$.
  * Prototype discharge is 17,678 times larger than model discharge.

---

## 14. Topic 13: HEC-RAS 1D Modeling & Troubleshooting

#### Q13 [Advanced: "Energy Equation Could Not Be Balanced" Warning]
* **Question**: In HEC-RAS, what causes the warning *"The energy equation could not be balanced within specified iterations. Program defaulted to critical depth"*, and how do you resolve it?
* **Expected Answer**:
  * *Cause*: The standard-step iterative solver failed to balance within tolerance (usually $0.003\text{ m}$). This occurs when:
    1. Cross-sections are spaced too far apart ($\Delta x$ too large).
    2. Flow transitions through critical depth (e.g., hydraulic jump or draw-down passing $Fr = 1$).
    3. Severe contraction/expansion transitions exist.
  * *Solution*:
    1. Use the HEC-RAS **Cross Section Interpolation** tool to insert interpolated cross-sections at $\Delta x/2$ or $\Delta x/4$.
    2. Switch from Subcritical to **Mixed Flow** mode so the engine solves supercritical and subcritical branches independently and locates the jump.

---

## 15. Topic 14: Bentley HAMMER & Method of Characteristics

#### Q14 [Advanced: Courant Criterion in Method of Characteristics]
* **Question**: What is the Courant criterion in Bentley HAMMER, and why must pipeline reach length $\Delta x$ equal $a \Delta t$?
* **Expected Answer**: The Method of Characteristics solves governing ODEs along characteristic lines $dx/dt = \pm a$. To evaluate grid points without interpolation errors, the spatial step and time step must satisfy:
  $$\Delta x = a \cdot \Delta t \iff \frac{a \Delta t}{\Delta x} = 1.0$$
  If $a \Delta t / \Delta x \ne 1.0$, the characteristic lines do not intersect exactly at grid nodes, requiring spatial interpolation that introduces numerical damping (artificial attenuation of pressure peaks). HAMMER automatically adjusts wave speeds or reach lengths slightly to maintain a common global time step $\Delta t$.

---

## 16. Topic 15: Excel VBA & Engineering Automation

#### Q15 [Intermediate: VBA User-Defined Function (UDF) vs. Subroutine]
* **Question**: What is the architectural difference between an Excel VBA Function (UDF) and a Subroutine, and how are they used in hydraulic calculation sheets?
* **Expected Answer**:
  * *Function (UDF)*: Returns a value directly to a worksheet cell formula (e.g., `=Colebrook_White(Re, eps/D)`). It cannot modify worksheet structure, format cells, or write to other ranges.
  * *Subroutine (`Sub`)*: Executed via a button or macro shortcut. It performs extensive operations: reading inputs from tables, running multi-variable loops, formatting cells, generating rating tables across 100 rows, and exporting data.

---

## 17. Topic 16: Engineering Numerical Methods

#### Q16 [Advanced: Explicit vs. Implicit Discretization Schemes]
* **Question**: Compare explicit finite difference schemes with implicit schemes (like the Preissmann scheme in HEC-RAS) for flood routing.
* **Expected Answer**:
  * *Explicit Schemes*: Evaluate spatial derivatives at the current time step $t^n$. Simple to code, but strictly bound by the CFL condition ($Cr \le 1.0$). If $\Delta t > \Delta x / (v+c)$, the solution diverges exponentially.
  * *Implicit Schemes (Preissmann 4-Point)*: Evaluate spatial derivatives at the future time step $t^{n+1}$, producing a system of non-linear simultaneous equations solved via matrix inversion (Newton-Raphson). Unconditionally stable for large $\Delta t$, although practical accuracy requires $Cr \approx 1.0 \text{ to } 2.0$.

---

## 18. Topic 17: Candidate M.Tech Research Defense & Technical Pivot

#### Q17 [Candidate Project Defense: Computational Fluid Dynamics & Sediment Scour Modeling in OpenFOAM]
* **Question**: *"In your M.Tech research, you modeled sediment scour using OpenFOAM. How does that computational fluid dynamics work transfer to AFRY's hydraulic engineering consultancy?"*
* **Candidate's Pitch**:
  > *"In my M.Tech research at IIT Kanpur, I numerically modeled open-channel hydrodynamic and local scour processes using OpenFOAM and the Finite Volume Method. I solved the 3D Reynolds-Averaged Navier-Stokes (RANS) equations coupled with the $k-\omega$ SST turbulence model, performing rigorous grid independence verification via the Grid Convergence Index (GCI).*
  > 
  > *This research translates directly to AFRY's engineering projects in three ways:*
  > 1. *Flow Physics*: Hydraulic structures create severe pressure flow, vortex shedding, contraction scour, and downstream hydraulic jumps—the exact physical phenomena governing dams, spillways, and river diversions at AFRY.
  > 2. *Numerical Maturity*: My background in CFD boundary conditions, convergence tolerances, and stability criteria enables me to look inside 1D/2D tools like HEC-RAS and Bentley HAMMER rather than treating them as black boxes.
  > 3. *Consulting Problem Solving*: I know how to validate numerical simulations against physical flume data and translate raw velocity and shear fields into actionable civil engineering design recommendations."*


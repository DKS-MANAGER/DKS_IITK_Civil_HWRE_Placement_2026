# Topic Master 03: Fluid Mechanics, Hydraulic Systems & HWRE Specialization

> **Consolidated Module**: EXXON-TOPIC-03 (Fluid Mechanics, Pipeline Hydraulics & HWRE)  
> **Target Assessment**: Technical Assessment (HWRE Track) & Technical Interview Deep Dive  
> **Structure**:
> - **SECTION A**: Fluid Mechanics & Pipeline Hydraulics (Navier-Stokes, Darcy-Weisbach vs Fanning, Water Hammer, NPSH & Cavitation)
> - **SECTION B**: Open-Channel Hydraulics & Hydraulic Structures (Specific Energy, Hydraulic Jumps, GVF Profiles)
> - **SECTION C**: Surface Water Hydrology & Groundwater Hydrodynamics
> - **SECTION D**: Sediment Transport, River Engineering & Bridge Pier Scour (HEC-18, Shields, Exner)
> - **SECTION E**: Computational Fluid Dynamics (CFD), Finite Volume Method (FVM) & Numerical Modeling
> - **SECTION F**: 12 Multi-Step Production HWRE Engineering Problems with Complete Solutions

---

# SECTION A: Advanced HWRE Theory & Governing Engineering Principles

## Track A: Civil Engineering & Hydraulics & Water Resources Engineering (HWRE) Focus

> **Core Audience:** Civil Engineering graduates specializing in Hydraulics, Water Resources, Coastal & Environmental Fluid Mechanics  
> **Target Role:** Engineer (ExxonMobil Services & Technology Pvt. Ltd., Bengaluru)  
> **Pedagogical Standard:** Rigorous first-principles derivation, intuitive physical interpretation, explicit boundary assumptions, unit consistency, and graded application.

---

# Table of Contents
1. [Module A1: Engineering Mathematics & Quantitative Foundations](#module-a1-engineering-mathematics--quantitative-foundations)
2. [Module A2: Engineering Mechanics & Strength of Materials](#module-a2-engineering-mechanics--strength-of-materials)
3. [Module A3: Fluid Mechanics & Pipeline Hydraulics](#module-a3-fluid-mechanics--pipeline-hydraulics)
4. [Module A4: Open-Channel Flow & Hydraulic Structures](#module-a4-open-channel-flow--hydraulic-structures)
5. [Module A5: Hydrology & Water Resources Engineering](#module-a5-hydrology--water-resources-engineering)
6. [Module A6: Sediment Transport, River Mechanics & Scour](#module-a6-sediment-transport-river-mechanics--scour)
7. [Module A7: Environmental Engineering & Water Quality](#module-a7-environmental-engineering--water-quality)
8. [Module A8: Numerical Methods, FVM & Computational Fluid Dynamics](#module-a8-numerical-methods-fvm--computational-fluid-dynamics)

---

# Module A1: Engineering Mathematics & Quantitative Foundations

## 1. Dimensional Homogeneity & Buckingham Pi Theorem
Engineering equations describing physical processes must be dimensionally homogeneous: every additive term must share the exact same primary dimensions $[M]^a [L]^b [T]^c [\theta]^d$.

### Buckingham Pi Theorem
If an engineering problem involves $n$ physical variables containing $m$ fundamental dimensions, the physical relationship can be grouped into $k = n - m$ independent dimensionless $\Pi$-groups:
$$\phi(\Pi_1, \Pi_2, \dots, \Pi_k) = 0$$

#### Step-by-Step Methodology:
1. List all $n$ physical parameters influencing the phenomenon (e.g., pressure drop $\Delta p$, pipe diameter $D$, length $L$, fluid density $\rho$, dynamic viscosity $\mu$, roughness $\epsilon$, velocity $V$).
2. Express each variable in primary dimensions ($M, L, T$).
3. Select $m$ repeating variables that collectively contain all primary dimensions but cannot themselves form a dimensionless group (typically one geometric variable $D$, one kinematic/velocity variable $V$, and one dynamic/fluid property $\rho$).
4. Form each $\Pi$-group by multiplying one non-repeating variable with the repeating variables raised to unknown exponents:
   $$\Pi_1 = D^a V^b \rho^c \Delta p$$
5. Solve for exponents by equating net dimensions to $M^0 L^0 T^0$.

> **Physical Intuition:** Dimensionless parameters collapse complex multi-variable experiments into universal scaling laws. For example, Reynolds number $\mathrm{Re} = \frac{\rho V D}{\mu}$ represents the ratio of inertial force scale ($\rho V^2 L^2$) to viscous shear force scale ($\mu V L$).

---

## 2. Ordinary Differential Equations (ODEs) in HWRE
Many hydraulic and transport processes are governed by first- and second-order linear and non-linear ODEs.

### First-Order Linear Equations (Transient Reservoir Water Balance)
$$\frac{dS(t)}{dt} = I(t) - Q(t)$$
For a linear reservoir where storage is proportional to outflow ($S = K Q$):
$$K \frac{dQ}{dt} + Q(t) = I(t) \implies \frac{dQ}{dt} + \frac{1}{K}Q = \frac{1}{K}I(t)$$
Using integrating factor $e^{\int \frac{1}{K} dt} = e^{t/K}$:
$$Q(t) = Q_0 e^{-t/K} + \frac{1}{K} \int_0^t I(\tau) e^{-(t-\tau)/K} d\tau$$

---

## 3. Error Propagation & Sensitivity Analysis
When an engineering output $Y$ is a function of several experimentally measured or estimated parameters $X_1, X_2, \dots, X_n$:
$$Y = f(X_1, X_2, \dots, X_n)$$
The maximum expected absolute error $\delta Y$ and variance $\sigma_Y^2$ are governed by Taylor series expansion:
$$\sigma_Y^2 \approx \sum_{i=1}^n \left(\frac{\partial f}{\partial X_i}\right)^2 \sigma_{X_i}^2 + 2 \sum_{i=1}^{n-1}\sum_{j=i+1}^n \left(\frac{\partial f}{\partial X_i}\right)\left(\frac{\partial f}{\partial X_j}\right) \mathrm{Cov}(X_i, X_j)$$

#### Practical Example: Darcy-Weisbach Head Loss Sensitivity
Head loss is given by $h_f = \frac{f L V^2}{2 g D}$. Expressing in terms of volumetric discharge $Q = \frac{\pi}{4} D^2 V \implies V = \frac{4 Q}{\pi D^2}$:
$$h_f = \frac{8 f L Q^2}{\pi^2 g D^5}$$
Taking the logarithmic derivative:
$$\ln h_f = \ln\left(\frac{8 L}{\pi^2 g}\right) + \ln f + 2\ln Q - 5\ln D$$
$$\frac{d h_f}{h_f} = \frac{df}{f} + 2\frac{dQ}{Q} - 5\frac{dD}{D}$$
> **Critical Engineering Insight:** Under the assumption of constant friction factor $f$ (valid in fully rough turbulent flow), a **1% reduction in pipe diameter $D$** (e.g., due to paraffin wax deposition or internal scaling) causes an approximate **5% increase in frictional head loss** ($|-5 \times (-1\%)| = +5\%$). In transitional or smooth turbulent flow where $f$ depends on Reynolds number and relative roughness $\epsilon/D$, a decrease in $D$ also increases $f$ ($df/f > 0$), resulting in a slightly higher net sensitivity of approximately $5.1\% - 5.3\%$. Pipe diameter is by far the most sensitive governing parameter in pipeline hydraulic systems.

---

# Module A2: Engineering Mechanics & Strength of Materials

## 1. State of Stress, Mohr's Circle & Principal Stresses
At any point in a continuum under plane stress ($\sigma_z = \tau_{xz} = \tau_{yz} = 0$), the normal and shear stresses on an arbitrary plane inclined at angle $\theta$ counter-clockwise from the x-axis are:
$$\sigma_\theta = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\theta + \tau_{xy}\sin 2\theta$$
$$\tau_\theta = -\frac{\sigma_x - \sigma_y}{2}\sin 2\theta + \tau_{xy}\cos 2\theta$$

### Principal Stresses & Maximum In-Plane Shear Stress
$$\sigma_{1, 2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
$$\tau_{\max} = R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \frac{\sigma_1 - \sigma_2}{2}$$
The principal planes are oriented at:
$$\tan 2\theta_p = \frac{2 \tau_{xy}}{\sigma_x - \sigma_y}$$
On principal planes, **shear stress is identically zero**.

---

## 2. Thin-Walled vs Thick-Walled Pressure Vessels (Pipelines & Tanks)
In oil and gas transport pipelines and industrial storage tanks, internal pressure generates circumferential (hoop) and longitudinal stresses.

### Thin-Walled Cylinder Criteria ($D/t \ge 20$)
Under internal gauge pressure $P_i$, internal diameter $D$, and wall thickness $t$:
* **Hoop (Circumferential) Stress:** $\sigma_h = \frac{P_i D}{2 t}$ (acting to burst the cylinder longitudinally)
* **Longitudinal Stress:** $\sigma_L = \frac{P_i D}{4 t}$ (for capped ends)
$$\sigma_h = 2 \sigma_L$$
> **Design Mechanics & Real Pipeline Behavior:**
> - In an ideal, homogeneous, defect-free pipe subjected solely to internal pressure, hoop stress is twice longitudinal stress ($\sigma_h = 2\sigma_L$), meaning ductile burst failure theoretically initiates as a longitudinal split along the pipe body.
> - *Industrial Engineering Nuance:* In operational transmission pipelines, failure orientation is strongly dictated by combined stress states and material factors:
>   1. **Longitudinal vs Spiral Seam Flaws:** Electric Resistance Welded (ERW) longitudinal seams carry maximum hoop tension, whereas Submerged Arc Welded (SAW) spiral seams orient weld lines at an angle $\alpha$, reducing normal stress across the seam.
>   2. **Secondary & Restrained Axial Stresses:** In fully restrained buried pipelines, thermal expansion ($\Delta T$) and Poisson contraction generate compressive or tensile axial stresses:
>      $$\sigma_{\text{axial}} = \nu \sigma_h - E \alpha_T \Delta T \pm \frac{M}{Z}$$
>      Significant thermal changes, seismic faulting, or unsupported river crossings can cause longitudinal stresses to exceed hoop stresses, precipitating catastrophic circumferential (girth-weld) tensile rupture or compressive buckling.

### Thick-Walled Cylinder (Lamé’s Equations)
When $D/t < 20$, radial stress cannot be neglected, and hoop stress varies non-linearly across the wall thickness:
$$\sigma_r(r) = \frac{P_i r_i^2 - P_o r_o^2}{r_o^2 - r_i^2} - \frac{(P_i - P_o) r_i^2 r_o^2}{r^2 (r_o^2 - r_i^2)}$$
$$\sigma_\theta(r) = \frac{P_i r_i^2 - P_o r_o^2}{r_o^2 - r_i^2} + \frac{(P_i - P_o) r_i^2 r_o^2}{r^2 (r_o^2 - r_i^2)}$$
For internal pressure only ($P_o = 0$), maximum hoop stress occurs at the **inner bore** ($r = r_i$):
$$\sigma_{\theta,\max} = P_i \left(\frac{r_o^2 + r_i^2}{r_o^2 - r_i^2}\right)$$

---

## 3. Failure Theories: Tresca vs Von Mises
* **Tresca (Maximum Shear Stress Theory):** Yielding begins when the maximum shear stress equals the shear stress at yield in simple tension:
  $$\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2} \ge \frac{S_y}{2} \implies \sigma_1 - \sigma_3 \ge S_y$$
* **Von Mises (Distortion Energy Theory):** Yielding begins when the octahedral shear stress or distortional strain energy equals that in uniaxial yield:
  $$\sigma_{vm} = \sqrt{\frac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]} \ge S_y$$
> **Engineering Assessment:** Von Mises is physically more realistic for ductile metals (steel line pipe, structural joints) and gives a ~15% larger safe operating region than the conservative Tresca criterion.

---

# Module A3: Fluid Mechanics & Pipeline Hydraulics

## 1. Continuum Hypothesis, Fluid Properties & Viscosity
* **Density ($\rho$):** Mass per unit volume $[kg/m^3]$.
* **Dynamic Viscosity ($\mu$):** Shear stress per unit velocity gradient $[Pa \cdot s = N \cdot s/m^2 = kg/(m \cdot s)]$.
* **Kinematic Viscosity ($\nu$):** Momentum diffusivity $\nu = \frac{\mu}{\rho} [m^2/s]$.
* **Newton's Law of Viscosity:** $\tau = \mu \frac{du}{dy}$. Fluids obeying this are *Newtonian* (water, light crude, air). Drilling muds, heavy residual oils, and sludges exhibit non-Newtonian behavior (Bingham plastic, pseudo-plastic shear thinning).

---

## 2. Derivation & Limitations of Bernoulli's Equation
Starting from Euler's momentum equation along a streamline in steady, inviscid flow:
$$V dV + \frac{dp}{\rho} + g dz = 0$$
Integrating along a streamline for an incompressible fluid ($\rho = \text{constant}$):
$$\frac{p_1}{\rho g} + \frac{V_1^2}{2g} + z_1 = \frac{p_2}{\rho g} + \frac{V_2^2}{2g} + z_2 = H = \text{constant}$$

### Essential Assumptions Behind Bernoulli's Equation:
1. **Steady Flow:** $\frac{\partial \mathbf{V}}{\partial t} = 0$
2. **Incompressible Flow:** Density $\rho$ is constant.
3. **Inviscid Flow:** Viscous friction losses are neglected along the streamline ($\mu = 0$).
4. **Flow along a single streamline:** The constant changes across streamlines unless the flow is irrotational ($\nabla \times \mathbf{V} = 0$).
5. **No shaft work or heat exchange:** No pumps, turbines, or thermal additions between stations 1 and 2.

### Extended Engineering Bernoulli Equation (Energy Equation with Losses)
In real industrial piping networks, energy is dissipated via fluid shear (head loss $h_L$) and added via pumps ($h_p$):
$$\frac{p_1}{\rho g} + \alpha_1 \frac{V_1^2}{2g} + z_1 + h_p = \frac{p_2}{\rho g} + \alpha_2 \frac{V_2^2}{2g} + z_2 + h_t + h_L$$
where $\alpha$ is the kinetic energy correction factor ($\alpha \approx 1.05-1.1$ in turbulent pipe flow, $\alpha = 2.0$ in fully developed laminar flow), and $h_t$ is turbine extraction head.

---

## 3. Pipe Flow: Darcy-Weisbach vs Fanning Friction Factor
Frictional head loss across a circular pipe of length $L$ and diameter $D$ is given by the **Darcy-Weisbach equation**:
$$h_f = f \frac{L}{D} \frac{V^2}{2g}$$

```
+-----------------------------------------------------------------------------------------------+
|                             CRITICAL FRICTION FACTOR CONVENTION TRAP                          |
+-----------------------------------------------------------------------------------------------+
| Darcy Friction Factor (Moody factor, f):                                                     |
|    hf = f * (L/D) * (V^2 / 2g)                                                                |
|    In laminar flow: f = 64 / Re                                                               |
|                                                                                               |
| Fanning Friction Factor (f_F):                                                                |
|    Common in chemical engineering and petroleum processing literature.                        |
|    hf = 4 * f_F * (L/D) * (V^2 / 2g)                                                          |
|    In laminar flow: f_F = 16 / Re                                                             |
|                                                                                               |
| RELATIONSHIP: f_Darcy = 4 * f_Fanning                                                         |
+-----------------------------------------------------------------------------------------------+
```

### Flow Regimes in Circular Pipes:
* **Laminar Flow ($\mathrm{Re} \le 2000$):** Viscous forces dominate. Friction factor depends purely on $\mathrm{Re}$:
  $$f = \frac{64}{\mathrm{Re}}$$
  Substituting into Darcy-Weisbach yields the Hagen-Poiseuille equation:
  $$\Delta P_f = \rho g h_f = \frac{128 \mu L Q}{\pi D^4}$$
  *(Pressure drop is directly proportional to discharge $Q$ and inversely to $D^4$)*.
* **Transitional Flow ($2000 < \mathrm{Re} < 4000$):** Unstable intermittency between laminar and turbulent bursts.
* **Turbulent Flow ($\mathrm{Re} \ge 4000$):** Inertial forces dominate. Governed by the **Colebrook-White equation**:
  $$\frac{1}{\sqrt{f}} = -2.0 \log_{10}\left(\frac{\epsilon/D}{3.7} + \frac{2.51}{\mathrm{Re}\sqrt{f}}\right)$$
  In fully rough turbulent flow ($\mathrm{Re} \to \infty$), the viscous sublayer is completely submerged by surface roughness elements, and $f$ becomes independent of $\mathrm{Re}$ (**von Kármán equation**):
  $$\frac{1}{\sqrt{f}} = -2.0 \log_{10}\left(\frac{\epsilon/D}{3.7}\right) = 1.14 - 2.0 \log_{10}\left(\frac{\epsilon}{D}\right)$$

---

## 4. Minor Losses in Piping Networks
In addition to wall friction, energy is lost at pipe fittings, bends, contractions, expansions, and valves:
$$h_m = K_L \frac{V^2}{2g}$$
* Sudden Expansion (Borda-Carnot loss from momentum balance):
  $$h_{L,\text{expansion}} = \frac{(V_1 - V_2)^2}{2g} = \left(1 - \frac{A_1}{A_2}\right)^2 \frac{V_1^2}{2g}$$
* Sudden Contraction:
  $$h_{L,\text{contraction}} = \left(\frac{1}{C_c} - 1\right)^2 \frac{V_2^2}{2g} \approx 0.5 \frac{V_2^2}{2g} \quad (\text{for } A_1/A_2 \to \infty)$$

---

## 5. Pumps, System Curves & Net Positive Suction Head (NPSH)
A centrifugal pump converts rotational kinetic energy into fluid pressure head.

### Pump Operating Point
* **System Head Curve:** $H_{\text{system}} = H_{\text{static}} + K_{\text{sys}} Q^2$
  where $H_{\text{static}} = z_{\text{discharge}} - z_{\text{suction}} + \frac{P_{\text{discharge}} - P_{\text{suction}}}{\rho g}$ and $K_{\text{sys}} = \sum \left(f \frac{L}{D} + K_L\right)\frac{8}{\pi^2 g D^4}$.
* **Pump Performance Curve:** $H_{\text{pump}} = H_0 - A Q^2$.
* The **Operating Point** occurs at the intersection $H_{\text{pump}}(Q) = H_{\text{system}}(Q)$.

```
   Head (m)
     ▲
     │          Pump Curve H_pump(Q)
     │   \
     │    \      Operating Point
     │     \       ▼
     │──────\─────(●)────────────── System Curve H_sys = H_static + K*Q^2
     │       \   /
     │        \ /
     │H_static X────────────────── Static Head (Elevation + Pressure diff)
     │       /  \
     └──────┴────┴────────────► Discharge Q (m^3/s)
```

### Cavitation and Net Positive Suction Head (NPSH)
Cavitation occurs when local static pressure drops below the vapor pressure of the liquid ($P \le P_v$), causing vapor bubble formation that violently collapses in higher pressure zones, eroding impellers and generating severe vibration.

#### Net Positive Suction Head Available ($\mathrm{NPSH}_A$):
The margin of absolute pressure head at the pump suction nozzle above the liquid vapor pressure:
$$\mathrm{NPSH}_A = \frac{P_{\text{suction, abs}}}{\rho g} + \frac{V_s^2}{2g} - \frac{P_v}{\rho g} = \frac{P_{\text{atm}}}{\rho g} + z_{\text{source}} - z_{\text{pump}} - h_{L,\text{suction}} - \frac{P_v}{\rho g}$$

#### Condition to Prevent Cavitation:
$$\mathrm{NPSH}_A \ge \mathrm{NPSH}_R + \text{Safety Margin (typically 0.5 to 1.0 m)}$$
where $\mathrm{NPSH}_R$ is Net Positive Suction Head Required by the pump manufacturer.

---

## 6. Hydraulic Transients & Water Hammer
Rapid closure of a valve in a pipeline converts fluid kinetic energy into an acoustic pressure surge wave.

### Acoustic Wave Speed in an Elastic Conduit ($c$):
$$c = \sqrt{\frac{K/\rho}{1 + \left(\frac{K}{E}\right)\left(\frac{D}{t}\right) c_1}}$$
where $K$ is fluid bulk modulus of elasticity, $\rho$ is density, $E$ is Young's modulus of pipe material, $D$ is pipe internal diameter, $t$ is wall thickness, and $c_1$ is a conduit restraint factor ($c_1 \approx 1 - \nu^2$ for axially anchored pipe). For rigid pipes ($E \to \infty$), $c = \sqrt{K/\rho} \approx 1480\text{ m/s}$ in water.

### Valve Closure Classification:
* Pipe critical transit time: $T_c = \frac{2 L}{c}$
* **Rapid (Instantaneous) Closure:** $T_{\text{valve}} \le T_c = \frac{2L}{c}$
  The pressure wave reaches the valve before the reflected rarefaction wave returns from the reservoir. The maximum pressure rise is given by the **Joukowsky Equation**:
  $$\Delta P_{\max} = \rho c \Delta V \implies \Delta H_{\max} = \frac{c \Delta V}{g}$$
* **Slow Closure:** $T_{\text{valve}} > T_c$
  Pressure waves undergo multiple reflections during closure, reducing peak surge:
  $$\Delta H \approx \frac{2 L \Delta V}{g T_{\text{valve}}}$$

---

# Module A4: Open-Channel Flow & Hydraulic Structures

## 1. Fundamentals: Open-Channel vs Pressurized Pipe Flow
Unlike pressurized pipes, open-channel flow possesses a free surface exposed to atmospheric pressure. The driving force is solely the component of gravity aligned with the bed slope $S_0$.

### Hydraulic Geometry Parameters:
* Flow Area: $A$
* Wetted Perimeter: $P$
* Hydraulic Radius: $R = A / P$
* Hydraulic Depth: $D_h = A / T$ (where $T$ is top water surface width)

---

## 2. Specific Energy, Froude Number & Critical Flow
The specific energy $E$ is the total energy head measured relative to the channel bottom:
$$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g A^2}$$
Differentiating with respect to depth $y$ at constant discharge $Q$:
$$\frac{dE}{dy} = 1 - \frac{Q^2}{g A^3} \frac{dA}{dy}$$
Since $\frac{dA}{dy} = T$ (top width):
$$\frac{dE}{dy} = 1 - \frac{Q^2 T}{g A^3} = 1 - \frac{V^2}{g (A/T)} = 1 - \frac{V^2}{g D_h} = 1 - \mathrm{Fr}^2$$

### The Froude Number ($\mathrm{Fr}$):
$$\mathrm{Fr} = \frac{V}{\sqrt{g D_h}} = \frac{V}{\sqrt{g (A/T)}}$$
* **Critical State ($\mathrm{Fr} = 1$):** $\frac{dE}{dy} = 0 \implies$ Specific energy is at a global minimum for a given discharge $Q$.
  $$\frac{Q^2 T_c}{g A_c^3} = 1$$
* **Subcritical Flow ($\mathrm{Fr} < 1$):** Velocity $V < \sqrt{g D_h}$ (gravity wave celerity). Disturbances propagate upstream. Backwater effects govern.
* **Supercritical Flow ($\mathrm{Fr} > 1$):** Velocity $V > \sqrt{g D_h}$. Disturbances cannot travel upstream. Flow is controlled upstream.

### For a Rectangular Channel ($A = b y$, $T = b$, $q = Q/b$):
$$y_c = \sqrt[3]{\frac{q^2}{g}}$$
$$E_{\min} = y_c + \frac{V_c^2}{2g} = y_c + \frac{g y_c}{2g} = 1.5 y_c$$
$$V_c = \sqrt{g y_c}$$

---

## 3. Uniform Flow: Manning's & Chezy's Equations
In uniform flow, gravitational driving force equals bed shear resistance, maintaining constant depth ($y_n$) and velocity along the channel:
$$V = \frac{1}{n} R^{2/3} S_0^{1/2} \quad (\text{SI Units})$$
$$Q = \frac{1}{n} A R^{2/3} S_0^{1/2}$$
where $n$ is Manning's roughness coefficient $[s/m^{1/3}]$, $R$ is hydraulic radius $[m]$, and $S_0$ is bed slope.

> **Unit Warning:** In US Customary Units, the constant is $1.486 / n$. In SI units, the factor is exactly $1.000 / n$.

---

## 4. Hydraulic Jump: Momentum Balance & Conjugate Depths
When rapid supercritical flow ($\mathrm{Fr}_1 > 1$) transitions to tranquil subcritical flow ($\mathrm{Fr}_2 < 1$), a standing shock wave—a **hydraulic jump**—occurs, accompanied by severe air entrainment, turbulent kinetic energy dissipation, and surface roller formation.

```
       Supercritical Flow                        Subcritical Flow
       ────────────────►                         ────────────────►
             V1, y1        Turbulent Roller            V2, y2
       ════════════════╗   .~~~~~~~~~~~~~~~~~.   ════════════════════
                       ║  :                   :
                       ╚══:═══════════════════:══════════════════════
                          ▲                   ▲
                       Section 1           Section 2
```

### Derivation from Control-Volume Momentum Conservation:
For a horizontal rectangular channel of width $b$, neglecting boundary wall friction over the short jump length:
$$F_{p1} - F_{p2} = \rho Q (V_2 - V_1)$$
$$\frac{1}{2} \rho g b y_1^2 - \frac{1}{2} \rho g b y_2^2 = \rho (b y_1 V_1) (V_2 - V_1)$$
Dividing by $\frac{1}{2} \rho g b$ and expressing in terms of $q = V_1 y_1 = V_2 y_2$:
$$y_1^2 - y_2^2 = \frac{2 q^2}{g}\left(\frac{1}{y_2} - \frac{1}{y_1}\right) = \frac{2 q^2}{g}\left(\frac{y_1 - y_2}{y_1 y_2}\right)$$
Dividing both sides by $(y_1 - y_2)$:
$$-(y_1 + y_2) = -\frac{2 q^2}{g y_1 y_2} \implies y_1 y_2 (y_1 + y_2) = \frac{2 q^2}{g} = \frac{2 V_1^2 y_1^2}{g} = 2 \mathrm{Fr}_1^2 y_1^3$$
Dividing by $y_1^3$ and letting $\eta = y_2 / y_1$:
$$\eta (\eta + 1) = 2 \mathrm{Fr}_1^2 \implies \eta^2 + \eta - 2 \mathrm{Fr}_1^2 = 0$$
Solving the quadratic equation for the positive root yields the **Bélanger Equation**:
$$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 \mathrm{Fr}_1^2} - 1\right)$$

### Energy Dissipation in the Jump ($\Delta E_L$):
$$\Delta E_L = E_1 - E_2 = \left(y_1 + \frac{V_1^2}{2g}\right) - \left(y_2 + \frac{V_2^2}{2g}\right) = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$$
> **Physical Interpretation:** Energy head loss increases with the **cube** of the jump height $(y_2 - y_1)^3$, making hydraulic jumps exceptionally effective energy dissipators at spillway aprons and outfall channels.

---

## 5. Gradually Varied Flow (GVF) & Surface Profiles
In GVF, flow depth changes gradually along the channel length. The differential equation governing the water surface slope is:
$$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - \mathrm{Fr}^2}$$
where $S_0$ is bed slope, and $S_f$ is energy slope evaluated via Manning's formula: $S_f = \frac{n^2 V^2}{R^{4/3}}$.

### Classification of Profiles:
Based on bed slope relative to critical slope ($S_c$ where normal depth $y_n = \text{critical depth } y_c$):
* **Mild Slope ($M$):** $y_n > y_c \implies S_0 < S_c$.
  - $M_1$ profile ($y > y_n > y_c$): Subcritical backwater curve behind a dam or weir ($\frac{dy}{dx} > 0$).
  - $M_2$ profile ($y_n > y > y_c$): Drawdown curve approaching a free overfall ($\frac{dy}{dx} < 0$).
  - $M_3$ profile ($y_n > y_c > y$): Flow issuing from a sluice gate into a mild channel ($\frac{dy}{dx} > 0$).
* **Steep Slope ($S$):** $y_c > y_n \implies S_0 > S_c$.
  - $S_1$ profile ($y > y_c > y_n$): **Subcritical backwater profile** on a steep slope ($dy/dx > 0$). When downstream obstruction (dam, weir, or high tailwater) forces the water depth above the critical depth ($y > y_c$), the flow in that backed-up reach becomes tranquil (subcritical). Upstream supercritical flow passes through a hydraulic jump to transition onto this $S_1$ curve.
  - $S_2$ profile ($y_c > y > y_n$): Supercritical drawdown profile ($dy/dx < 0$). Depth drops from critical depth $y_c$ (at a slope break or entry) down towards normal depth $y_n$; velocity accelerates.
  - $S_3$ profile ($y_c > y_n > y$): Supercritical decelerating profile ($dy/dx > 0$). Originates below normal depth (e.g., supercritical jet issuing from beneath a sluice gate onto a steep channel). Because $S_f > S_0$ and $\mathrm{Fr} > 1$, $\frac{dy}{dx} = \frac{-}{-} > 0$. Depth **rises** toward $y_n$, and by continuity ($V = q/y$), the flow **decelerates (retarded flow)** toward normal uniform velocity.
* **Critical ($C$):** $y_n = y_c$.
* **Horizontal ($H$):** $S_0 = 0 \implies H_2, H_3$ profiles.
* **Adverse ($A$):** $S_0 < 0 \implies A_2, A_3$ profiles.

---

# Module A5: Hydrology & Water Resources Engineering

## 1. Rainfall-Runoff Processes & The Rational Method
For small, impervious industrial facilities and drainage catchments (area $A < 50 \text{ hectares}$), peak stormwater discharge is estimated by the **Rational Method**:
$$Q_{\text{peak}} = C \cdot I \cdot A$$
* In SI Units:
  $$Q_p = \frac{C \cdot I \cdot A}{360}$$
  where $Q_p$ is peak discharge $[m^3/s]$, $C$ is runoff coefficient (dimensionless, $0.85-0.95$ for asphalt/refinery battery areas, $0.15-0.30$ for grass), $I$ is rainfall intensity $[mm/hr]$ for duration equal to time of concentration $t_c$, and $A$ is drainage area $[\text{hectares}]$.

### Time of Concentration ($t_c$):
The time required for runoff to travel from the hydraulically most remote point of the watershed to the outlet.
Kirpich's Equation:
$$t_c = 0.01947 \cdot L^{0.77} \cdot S^{-0.385}$$
where $t_c$ is in minutes, $L$ is maximum travel length $[m]$, and $S$ is dimensionless catchment slope $[m/m]$.

---

## 2. Unit Hydrograph Theory (Sherman, 1932)
A **Unit Hydrograph (UH)** is defined as the direct runoff hydrograph (DRH) resulting from **$1 \text{ cm}$ (or $1 \text{ mm}$)** of excess rainfall (effective rainfall) occurring uniformly over the entire catchment at a constant rate during a specified storm duration $D$.

### Two Fundamental Postulates:
1. **Linear Proportionality:** If $1\text{ cm}$ of excess rainfall produces direct runoff ordinate $Q_t$, then $P_{\text{eff}} \text{ cm}$ of excess rainfall produces ordinate $P_{\text{eff}} \times Q_t$.
2. **Time Invariance:** The runoff response to a unit storm of duration $D$ is identical regardless of when the storm occurs.

### Convolution Equation (Discrete Formulation):
$$Q_n = \sum_{m=1}^{n} P_m \cdot U_{n - m + 1}$$
where $Q_n$ is DRH ordinate at time step $n$, $P_m$ is excess rainfall in period $m$, and $U$ is UH ordinate.

---

## 3. Flood Frequency Analysis & Gumbel’s Extreme Value Distribution
Gumbel (EVI) distribution is widely applied to annual maximum peak floods:
$$x_T = \bar{x} + K_T \cdot \sigma_x$$
where $\bar{x}$ is sample mean, $\sigma_x$ is sample standard deviation, and $K_T$ is the frequency factor:
$$K_T = -\frac{\sqrt{6}}{\pi}\left[0.5772 + \ln\left(\ln\left(\frac{T}{T - 1}\right)\right)\right]$$
where $T = 1 / P$ is the return period in years.

### Encounter Probability (Hydrologic Risk):
The probability $R_e$ that a design flood with return period $T$ will be equaled or exceeded at least once during a structural project lifetime of $N$ years:
$$R_e = 1 - (1 - P)^N = 1 - \left(1 - \frac{1}{T}\right)^N$$
> **Assessment Application:** If an offshore jetty or refinery drainage culvert is designed for a **50-year return flood** ($T = 50$, $P = 0.02$) over an operational design lifespan of **25 years** ($N = 25$):
> $$R_e = 1 - (1 - 0.02)^{25} = 1 - (0.98)^{25} = 1 - 0.6035 = 0.3965 \implies 39.65\% \text{ risk!}$$
> Designing for a 50-year flood does **not** mean there is only a 2% chance of failure over the facility lifetime; there is nearly a 40% probability of encountering the design event.

---

## 4. Groundwater Flow & Darcy’s Law
In saturated porous media, discharge velocity $v_d$ (specific discharge) is proportional to hydraulic gradient $i = -dh/dL$:
$$q = -K \frac{dh}{dL} \implies Q = -K A \frac{dh}{dL}$$
where $K$ is hydraulic conductivity $[m/s]$, and $h = z + \frac{p}{\rho g}$ is piezometric head.

### Actual Seepage Velocity ($v_s$):
Fluid moves only through interconnected void pores of porosity $n = V_{\text{void}} / V_{\text{total}}$:
$$v_s = \frac{q}{n} = \frac{v_d}{n}$$
Since $n < 1$, **seepage velocity is always strictly greater than Darcy flux** ($v_s > v_d$).

---

# Module A6: Sediment Transport, River Mechanics & Scour

## 1. Incipient Motion & The Shields Parameter
Sediment motion initiates when the hydrodynamic destabilizing forces (drag and lift exerted by bed shear stress $\tau_b$) overcome stabilizing submerged submerged gravitational forces of sediment particles.

### Dimensionless Shields Parameter ($\tau_*$):
$$\tau_* = \frac{\tau_b}{(\rho_s - \rho) g d_{50}} = \frac{\rho u_*^2}{\gamma_s' d_{50}}$$
where:
* $\tau_b = \rho g R S_0$ is boundary bed shear stress $[N/m^2]$
* $u_* = \sqrt{\tau_b / \rho} = \sqrt{g R S_0}$ is shear velocity $[m/s]$
* $\rho_s$ is sediment particle density ($\approx 2650 \text{ kg/m}^3$ for quartz sand)
* $\rho$ is fluid density ($1000 \text{ kg/m}^3$ for water)
* $d_{50}$ is median grain diameter $[m]$

### Particle Reynolds Number ($\mathrm{Re}_*$):
$$\mathrm{Re}_* = \frac{u_* d_{50}}{\nu}$$
* If $\tau_* > \tau_{*c}$ (where $\tau_{*c} \approx 0.03 - 0.06$ on the Shields diagram), **sediment transport initiates**.
* If $\tau_* \le \tau_{*c}$, the bed remains static (**clear-water conditions**).

```
   Dimensionless Shear Stress Tau_*
     ▲
     │                                     Turbulent Boundary: Tau_*c ~ 0.06
     │                       Shields Curve     ─────────────────────────
     │    \                .------------------'
     │     \             .'                     MOTION (Bedload Transport)
     │      \          .'
     │       \_______.'  ◄── Minimum Tau_*c ~ 0.03 at Re_* ~ 10
     │                      NO MOTION (Stable Bed)
     └───────────────────────────────────────────────────► Particle Re_* = u_* d / nu
```

---

## 2. Bed Morphology & Sediment Mass Conservation: The Exner Equation
The morphodynamic evolution of a riverbed elevation $z_b(x, t)$ under 1D non-uniform sediment transport is governed by the **Exner Equation**:
$$(1 - \lambda_p) \frac{\partial z_b}{\partial t} + \frac{\partial q_s}{\partial x} = 0$$
where $\lambda_p$ is bed sediment porosity ($\approx 0.35-0.40$), and $q_s$ is volumetric sediment transport rate per unit channel width $[m^2/s]$.

### Physical Interpretation:
* **Aggradation (Bed Aggradation, $\frac{\partial z_b}{\partial t} > 0$):** Occurs when $\frac{\partial q_s}{\partial x} < 0$ (sediment transport capacity decreases downstream, causing deposition).
* **Degradation (Bed Scour, $\frac{\partial z_b}{\partial t} < 0$):** Occurs when $\frac{\partial q_s}{\partial x} > 0$ (transport capacity accelerates downstream, eroding the channel bed).

---

## 3. Bridge Pier & Pipeline Scour Mechanics (HEC-18 Standard)
When flow encounters an obstruction (bridge pier, subsea pipeline, platform leg), the stagnation pressure profile ($\Delta p = \frac{1}{2}\rho V(z)^2$) generates a downward pressure gradient:
* **Horseshoe Vortex System:** Downward jet rolls up into a rotating vortex wrapped around the upstream face of the pier, excavating a deep scour hole.
* **Wake Vortices:** Low-pressure vortex shedding downstream acts like a vacuum pump lifting dislodged sediment particles into suspension.

```
       Approach Flow Velocity V(z)
       ────────►
       ────────►           Pier Structure
       ──────►             ┌───────┐
       ────►               │       │
       ──►  Downward Jet   │       │
             │             │       │
             ▼             │       │
          (@@@@)           │       │
       Horseshoe Vortex    │       │
     \_________________/   │       │
         Scour Hole        └───────┘
```

### Federal Highway Administration (FHWA) HEC-18 Equation:
For equilibrium local pier scour depth $y_s$:
$$\frac{y_s}{y_1} = 2.0 \, K_1 K_2 K_3 K_4 \left(\frac{a}{y_1}\right)^{0.65} \mathrm{Fr}_1^{0.43}$$
where:
* $y_1$ = approach flow depth upstream of pier $[m]$
* $a$ = pier width / diameter $[m]$
* $\mathrm{Fr}_1 = \frac{V_1}{\sqrt{g y_1}}$ = approach Froude number
* $K_1$ = correction factor for pier nose shape ($1.0$ for round nose, $1.1$ for square nose)
* $K_2$ = correction factor for angle of attack of flow
* $K_3$ = bed condition factor ($1.1$ for clear-water / plane bed)
* $K_4$ = armoring factor for coarse bed materials

---

# Module A7: Environmental Engineering & Water Quality

## 1. Conservative vs Non-Conservative Mass Balance
For an arbitrary control volume:
$$\frac{dM}{dt} = \dot{M}_{\text{in}} - \dot{M}_{\text{out}} \pm \dot{M}_{\text{reaction}}$$
For a continuous steady-state stream mixing problem with river discharge $Q_r$ at pollutant concentration $C_r$, receiving an industrial effluent stream $Q_e$ at concentration $C_e$:
$$C_{\text{mix}} = \frac{Q_r C_r + Q_e C_e}{Q_r + Q_e}$$

---

## 2. BOD Kinetics & Dissolved Oxygen Deficit (Streeter-Phelps Model)
Biochemical Oxygen Demand (BOD) measures the amount of oxygen required by aerobic microorganisms to biologically oxidize organic matter in water.

### First-Order BOD Deoxygenation Kinetics:
$$\frac{dL}{dt} = -k_1 L \implies L_t = L_0 e^{-k_1 t}$$
$$\mathrm{BOD}_t = L_0 - L_t = L_0 (1 - e^{-k_1 t})$$
where $L_0$ is ultimate carbonaceous $\mathrm{BOD}$ ($y_{\infty}$), and $k_1$ is the deoxygenation rate constant $[day^{-1}]$.

### Streeter-Phelps Dissolved Oxygen (DO) Sag Equation:
When wastewater enters a river, dissolved oxygen drops due to biological consumption ($k_1$) while atmospheric reaeration acts to replenish oxygen ($k_2$):
$$D(t) = \frac{k_1 L_0}{k_2 - k_1}\left(e^{-k_1 t} - e^{-k_2 t}\right) + D_0 e^{-k_2 t}$$
where $D(t) = \mathrm{DO}_{\text{sat}} - \mathrm{DO}(t)$ is oxygen deficit $[mg/L]$, and $D_0$ is initial deficit at mixing.

### Critical Time ($t_c$) and Maximum Deficit ($D_c$):
Setting $\frac{dD}{dt} = 0$:
$$t_c = \frac{1}{k_2 - k_1} \ln\left\{\frac{k_2}{k_1}\left[1 - D_0 \frac{k_2 - k_1}{k_1 L_0}\right]\right\}$$

---

# Module A8: Numerical Methods, FVM & Computational Fluid Dynamics

## 1. Discretization Techniques: FDM, FEM & FVM
* **Finite Difference Method (FDM):** Replaces differential operators with Taylor-series approximations at discrete nodal points. Computationally efficient on structured orthogonal grids; struggles with complex curved boundaries.
* **Finite Element Method (FEM):** Minimizes residual error over piecewise polynomial trial functions. Exceptional for structural solid mechanics and stress analysis.
* **Finite Volume Method (FVM):** Integrates the conservation equations over arbitrary polyhedral control volumes:
  $$\int_V \frac{\partial \mathbf{U}}{\partial t} dV + \oint_A \mathbf{F} \cdot d\mathbf{A} = \int_V \mathbf{S} dV$$
  Using Gauss' Divergence Theorem, volume integrals of flux divergences transform into surface flux summations over control volume faces.
  > **Why FVM is Standard in CFD & Fluids (OpenFOAM / Fluent):** FVM enforces **strict conservative mass, momentum, and energy balances** cell-by-cell, even on coarse, distorted unstructured grids.

---

## 2. Stability, Courant Number & The CFL Condition
In explicit time-stepping schemes for hyperbolic conservation laws (e.g., 1D shallow water equations or Euler gas dynamics), numerical stability is strictly bounded by the **Courant-Friedrichs-Lewy (CFL) Condition**:
$$C = \frac{(|u| + c) \Delta t}{\Delta x} \le C_{\max}$$
where $u$ is advective fluid velocity, $c$ is physical wave celerity ($c = \sqrt{g D_h}$ for gravity waves, or $c = \sqrt{\gamma R T}$ for acoustic waves), and $C_{\max} \le 1.0$ (typically $0.5 - 0.8$ for explicit Runge-Kutta finite-volume schemes).
* **Mathematical & Physical Meaning:** The CFL condition is a **necessary condition for convergence**, requiring that the numerical domain of dependence must completely contain the mathematical domain of dependence of the underlying differential equation.
* **Important Numerical Insights:**
  1. *Necessary vs Sufficient Conditions:* For explicit time-stepping of hyperbolic equations, the CFL condition is a **necessary** condition for numerical stability and convergence, but not universally **sufficient**. For instance, Forward-Time Central-Space (FTCS) discretization for pure advection is unconditionally unstable regardless of Courant number. For conditionally stable explicit schemes (e.g., explicit upwind or MacCormack), $C \le 1.0$ governs hyperbolic stability; when physical diffusion (kinematic viscosity $\nu$) is also present, the explicit parabolic stability limit $\Delta t \le \frac{\Delta x^2}{2 \nu}$ must also be simultaneously satisfied.
  2. *Multi-Dimensional CFL:* In 2D/3D Cartesian/unstructured grids:
     $$C = \Delta t \left(\frac{|u| + c}{\Delta x} + \frac{|v| + c}{\Delta y}\right) \le C_{\max}$$
  3. *Implicit Time Schemes & Pressure-Velocity Coupling (SIMPLE / PISO):* Implicit time-integration schemes (e.g., backward Euler, Crank-Nicolson) are linearly unconditionally stable for any Courant number. Note that SIMPLE and PISO are pressure-velocity coupling algorithms, not time-marching schemes per se: SIMPLE is designed for steady-state iterative relaxation (where pseudo-time step Courant numbers can reach $10 - 100+$), while PISO and PIMPLE are designed for transient flows. In transient calculations, non-linear convective terms and pressure-velocity splitting mean that high Courant numbers ($C > 1$) can still lead to loss of temporal accuracy or iterative divergence unless multiple outer PIMPLE correction loops are used; time-accurate LES/URANS typically targets $C \le 1.0$.

---

## 3. Near-Wall Turbulence Modeling: $y^+$ & Law of the Wall
Turbulent shear flows against solid impermeable walls (pipe walls, offshore jackets, flume beds) develop a universal boundary-layer profile governed by the dimensionless wall distance $y^+$:
$$y^+ = \frac{y u_*}{\nu} = \frac{y}{\nu}\sqrt{\frac{\tau_w}{\rho}}$$
where $y$ is normal distance from the wall, and $u_* = \sqrt{\tau_w / \rho}$ is friction velocity.

```
       Dimensionless Velocity u+ = u / u_*
       ▲
       │                                     Log-Law Region: u+ = (1/kappa)*ln(y+) + B
       │                                  .-------------------------------------------
       │                              .-'
       │       Viscous Sublayer   .-'     Buffer Layer (5 < y+ < 30)
       │       u+ = y+        .-'
       │       (y+ < 5)   .-'
       └──────────────────┴───────────────┴──────────────────────────────► y+ = y * u_* / nu
                          5               30
```

### Boundary Layer Sub-Layers & Modern Solver Wall Treatments:
1. **Viscous Sublayer ($y^+ < 5$):** Molecular viscosity dominates, viscous shear stress is constant ($\tau \approx \tau_w$), and Reynolds shear stress is negligible. Follows linear profile: $u^+ = y^+$.
   - *Wall-Resolved Approach (Low-Re RANS):* Requires prism boundary layers with the first centroid located at **$y^+ \le 1$** ($y^+ < 2$).
2. **Buffer Layer ($5 < y^+ < 30$):** Both viscous and turbulent stresses are equally significant. Velocity profile transitions from linear to logarithmic.
   - *Classical Standard Wall Function Rule:* In legacy $k-\epsilon$ solvers using Launder & Spalding's non-blended wall functions, the first near-wall cell centroid had to be kept strictly outside the buffer layer ($y^+ > 30$) because the solver switched abruptly from $u^+ = y^+$ to $u^+ = \frac{1}{\kappa}\ln y^+ + B$, causing large artificial skin friction errors in $5 < y^+ < 30$.
   - *Modern Continuous / Blended Wall Functions (Standard in OpenFOAM / Fluent):* Modern codes utilize continuous automatic wall treatments (e.g., Menter's $k-\omega$ SST or Kader's blending functions) that smoothly blend viscous sublayer and log-law equations:
     $$u^+ = e^{-\Gamma} u_{\text{visc}}^+ + e^{-1/\Gamma} u_{\text{turb}}^+$$
     This eliminates the prohibition against mesh cells in the buffer layer: wall-resolved meshes naturally pass through the buffer layer with 10-15 prism layers, while coarse grids ($30 < y^+ < 200$) automatically fall back to logarithmic wall laws without numerical discontinuity.
3. **Log-Law Layer ($30 < y^+ < 300$):** Turbulent Reynolds shear stress dominates:
   $$u^+ = \frac{1}{\kappa} \ln(y^+) + B \quad (\kappa \approx 0.41, B \approx 5.0 - 5.2)$$
   - *Wall-Modeled Approach (High-Re RANS):* First grid centroid placed at $30 \le y^+ \le 200$, reducing mesh size by orders of magnitude for high-Re industrial piping and offshore structures.

---

## 4. Verification vs Validation & The Grid Convergence Index (GCI)
* **Verification:** *"Are we solving the equations right?"* Quantification of numerical discretization, round-off, and iterative errors.
* **Validation:** *"Are we solving the right equations?"* Quantifying physics agreement between high-resolution numerical data and physical benchmark experiments.

### ASME V&V 20: Grid Convergence Index (GCI) & Richardson Extrapolation
To objectively confirm that a CFD or numerical hydraulic solution is independent of spatial discretization, simulations must be run on at least three systematically refined grids: **Fine ($h_1$)**, **Medium ($h_2$)**, and **Coarse ($h_3$)**.
* Grid refinement ratio: $r_{21} = h_2 / h_1 \ge 1.3$, $r_{32} = h_3 / h_2 \ge 1.3$.
* For structured/unstructured meshes with total cell counts $N$: $r = (N_1 / N_2)^{1/D}$ where $D$ is spatial dimension.
* Let $\phi_1, \phi_2, \phi_3$ denote key engineering target values (e.g., drag coefficient $C_D$, discharge $Q$, or peak backwater depth $y_p$).

#### Governing Formulation:
1. **Apparent Order of Convergence ($p$):**
   $$p = \frac{1}{\ln(r_{21})} \left| \ln\left|\frac{\phi_3 - \phi_2}{\phi_2 - \phi_1}\right| + q(p) \right|$$
   (For constant refinement ratio $r_{21} = r_{32} = r$, $q(p) = 0$, giving $p = \frac{\ln((\phi_3 - \phi_2)/(\phi_2 - \phi_1))}{\ln(r)}$).
2. **Richardson Extrapolated Value (Zero Grid Spacing Limit):**
   $$\phi_{\text{ext}}^{21} = \phi_1 + \frac{\phi_1 - \phi_2}{r_{21}^p - 1}$$
3. **Fine-Grid Convergence Index ($\mathrm{GCI}_{21}$):**
   $$\mathrm{GCI}_{21} = \frac{F_s \, e_a^{21}}{r_{21}^p - 1}$$
   where $e_a^{21} = \left|\frac{\phi_1 - \phi_2}{\phi_1}\right|$ is approximate relative error, and $F_s = 1.25$ is the ASME safety factor for three-grid studies ($F_s = 3.0$ for two grids).

#### Complete Worked Benchmark Example:
Suppose an engineer simulates the discharge coefficient $C_d$ of a spillway crest on three grids:
* Grid 3 (Coarse, $N_3 = 50,000$ cells): $\phi_3 = 0.5200$
* Grid 2 (Medium, $N_2 = 100,000$ cells): $\phi_2 = 0.5080$
* Grid 1 (Fine, $N_1 = 200,000$ cells): $\phi_1 = 0.5030$
* Constant refinement ratio: $r = (100,000 / 50,000)^{1/2} = \sqrt{2} = 1.4142$.

**Calculations:**
1. Solution differences:
   $$\epsilon_{32} = \phi_3 - \phi_2 = 0.5200 - 0.5080 = 0.0120$$
   $$\epsilon_{21} = \phi_2 - \phi_1 = 0.5080 - 0.5030 = 0.0050$$
2. Apparent order of convergence:
   $$p = \frac{\ln(0.0120 / 0.0050)}{\ln(1.4142)} = \frac{\ln(2.40)}{0.34657} = \frac{0.87547}{0.34657} = \mathbf{2.526}$$
   *(Confirms monotonic convergence in the asymptotic range, matching expected second-order spatial discretization).*
3. Richardson extrapolated zero-grid value:
   $$r^p - 1 = (1.4142)^{2.526} - 1 = 2.40 - 1 = 1.40$$
   $$\phi_{\text{ext}}^{21} = 0.5030 + \frac{0.5030 - 0.5080}{1.40} = 0.5030 - 0.00357 = \mathbf{0.4994}$$
4. Relative error and GCI:
   $$e_a^{21} = \left|\frac{0.5030 - 0.5080}{0.5030}\right| = \frac{0.0050}{0.5030} = 0.00994 \implies 0.994\%$$
   $$\mathrm{GCI}_{21} = \frac{1.25 \times 0.00994}{1.40} = 0.00887 \implies \mathbf{0.89\%}$$
* **Engineering Conclusion:** The estimated fine-grid numerical discretization uncertainty is **$0.89\%$**. While ASME V&V 20 does not mandate a single universal cutoff for all applications, an estimated discretization uncertainty below $1\% - 2\%$ is widely accepted in hydraulic structure engineering and turbomachinery as demonstrating adequate asymptotic grid convergence.

---

## Sources
* **Mechanics of Materials & Pressure Vessels:** Gere, J. M., & Goodno, B. J., *Mechanics of Materials*, Cengage; ASME Boiler and Pressure Vessel Code (BPVC), Section VIII, Division 1/2.
* **Open Channel Flow & Hydraulics:** Chow, V. T., *Open-Channel Hydraulics*, McGraw-Hill; Henderson, F. M., *Open Channel Flow*, Macmillan.
* **Environmental & Water Quality Engineering:** Metcalf & Eddy, *Wastewater Engineering: Treatment and Resource Recovery*, 5th Edition, McGraw-Hill; Streeter, H. W., & Phelps, E. B. (1925), *A Study of the Pollution and Natural Purification of the Ohio River*.
* **Turbulence Modeling & Computational Fluid Dynamics:** Wilcox, D. C., *Turbulence Modeling for CFD*, DCW Industries; Versteeg, H. K., & Malalasekera, W., *An Introduction to Computational Fluid Dynamics: The Finite Volume Method*, Pearson.
* **Verification & Validation Standards:** ASME V&V 20-2009, *Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer*, American Society of Mechanical Engineers; Roache, P. J. (1998), *Verification and Validation in Computational Science and Engineering*, Hermosa Publishers.
* **Curriculum & Practice Mapping:** IndiaBIX Civil Engineering - Fluid Mechanics, Hydraulics & Environmental Directory ([https://www.indiabix.com/civil-engineering/](https://www.indiabix.com/civil-engineering/)).


---

# SECTION B: Multi-Step HWRE Technical Workbook (12 Production Problems)

## Graded Multi-Step Numerical Problems with Rigorous Physical Derivations

> **Target Profile:** Engineer (Core Technical Assessment & Technical Interview Panel)  
> **Specialization:** Civil Engineering — Hydraulics, Fluid Mechanics, River Mechanics, Water Resources  
> **Standard:** [REPRESENTATIVE PRACTICE SET] — Fully worked solutions, boundary assumptions, step-by-step arithmetic, unit conversions, and physical plausibility sanity checks.

---

# Problem Directory
* [Problem 01: Hydrostatic Resultant Force and Center of Pressure on a Radial Gate](#problem-01-hydrostatic-resultant-force-and-center-of-pressure-on-a-radial-gate)
* [Problem 02: Pipeline Frictional Resistance, Wax Deposition & Diameter Sensitivity](#problem-02-pipeline-frictional-resistance-wax-deposition--diameter-sensitivity)
* [Problem 03: Parallel and Branched Pipe Network Hydraulic Analysis](#problem-03-parallel-and-branched-pipe-network-hydraulic-analysis)
* [Problem 04: Centrifugal Pump Head Matching, Throttling & NPSH Margin](#problem-04-centrifugal-pump-head-matching-throttling--npsh-margin)
* [Problem 05: Water Hammer Acoustic Transient & Rapid Valve Closure Surge](#problem-05-water-hammer-acoustic-transient--rapid-valve-closure-surge)
* [Problem 06: Specific Energy, Critical Flow & Channel Choking under Contraction](#problem-06-specific-energy-critical-flow--channel-choking-under-contraction)
* [Problem 07: Hydraulic Jump Conjugate Depth & Energy Dissipation Stilling Basin](#problem-07-hydraulic-jump-conjugate-depth--energy-dissipation-stilling-basin)
* [Problem 08: Gradually Varied Flow (GVF) Backwater Profile Step Integration](#problem-08-gradually-varied-flow-gvf-backwater-profile-step-integration)
* [Problem 09: Unit Hydrograph S-Curve Conversion and Convolution](#problem-09-unit-hydrograph-s-curve-conversion-and-convolution)
* [Problem 10: Bed Shear Stress, Incipient Motion & Shields Parameter Verification](#problem-10-bed-shear-stress-incipient-motion--shields-parameter-verification)
* [Problem 11: Equilibrium Bridge Pier Scour Calculation (HEC-18 Standard)](#problem-11-equilibrium-bridge-pier-scour-calculation-hec-18-standard)
* [Problem 12: Exner Morphodynamic Riverbed Aggradation/Degradation Rate](#problem-12-exner-morphodynamic-riverbed-aggradationdegradation-rate)

---

# Problem 01: Hydrostatic Resultant Force and Center of Pressure on a Radial Gate

### 1. Problem Statement
A cylindrical radial (Tainter) gate of radius $R = 6.0\text{ m}$ and crest length $W = 10.0\text{ m}$ retains water in an industrial intake canal. The water surface stands at elevation $H = 4.5\text{ m}$ above the channel bed, which coincides with the gate sill. The pivot pin (trunnion axis) is located at the center of curvature of the circular arc at an elevation of $4.5\text{ m}$ above the bed.

**Determine:**
1. The horizontal hydrostatic force component $F_H$ acting on the gate.
2. The vertical hydrostatic force component $F_V$ acting on the gate.
3. The magnitude and direction of the total resultant hydrostatic force $F_R$.
4. The line of action of the resultant force relative to the pivot pin.

---

### 2. Governing Equations & Physics
* Horizontal force component equals the hydrostatic force on the vertical projection of the submerged surface:
  $$F_H = \rho g \bar{h} A_v$$
  where $\bar{h} = H / 2$ is the depth to the centroid of the vertical projection, and $A_v = W \times H$.
* Vertical force component equals the weight of the actual or imaginary fluid volume directly above the curved surface extending up to the free surface:
  $$F_V = \rho g \cdot \text{Vol}_{\text{fluid}}$$
* Total resultant magnitude:
  $$F_R = \sqrt{F_H^2 + F_V^2}$$
  Orientation: $\theta = \arctan(F_V / F_H)$.
* Line of action principle for circular cylindrical arcs: All elementary hydrostatic pressure forces act normal to the gate surface. For a circular arc, every normal passes through the center of curvature (pivot pin). Therefore, the net resultant force **must pass directly through the pivot pin**, producing zero net moment about the pin.

---

### 3. Step-by-Step Calculation
* **Constants:** Density of water $\rho = 1000\text{ kg/m}^3$, gravitational acceleration $g = 9.81\text{ m/s}^2$.

#### Step 1: Horizontal Force $F_H$
* Vertical projected area:
  $$A_v = W \cdot H = 10.0\text{ m} \times 4.5\text{ m} = 45.0\text{ m}^2$$
* Centroid depth:
  $$\bar{h} = \frac{4.5\text{ m}}{2} = 2.25\text{ m}$$
* Horizontal Force:
  $$F_H = (1000\text{ kg/m}^3)(9.81\text{ m/s}^2)(2.25\text{ m})(45.0\text{ m}^2) = 993,262.5\text{ N} = 993.26\text{ kN}$$

#### Step 2: Vertical Force $F_V$
The volume of water supported above the curved face is bounded by the circular sector and the triangular space below the water line.
* Let the origin be at the pivot pin $(0,0)$. The gate surface is $x^2 + y^2 = R^2 = 36.0$.
* The water surface is at $y = 0$. The gate sill is at $y = -4.5\text{ m}$.
* Angle subtended at the pivot pin:
  $$\sin \phi = \frac{4.5}{6.0} = 0.75 \implies \phi = \arcsin(0.75) = 48.5904^\circ = 0.84806\text{ rad}$$
* The area of the circular sector:
  $$A_{\text{sector}} = \frac{1}{2} R^2 \phi = \frac{1}{2}(6.0^2)(0.84806) = 15.265\text{ m}^2$$
* The horizontal distance from the pivot to the gate surface at the sill ($y = -4.5\text{ m}$):
  $$x_{\text{sill}} = \sqrt{R^2 - y^2} = \sqrt{6.0^2 - (-4.5)^2} = \sqrt{36 - 20.25} = \sqrt{15.75} = 3.9686\text{ m}$$
* The area of the triangle between pivot, water line, and sill coordinate:
  $$A_{\text{triangle}} = \frac{1}{2} \times x_{\text{sill}} \times H = \frac{1}{2} \times 3.9686\text{ m} \times 4.5\text{ m} = 8.9294\text{ m}^2$$
* Area of the fluid volume above the curved gate face:
  $$A_{\text{fluid}} = A_{\text{sector}} - A_{\text{triangle}} = 15.265\text{ m}^2 - 8.9294\text{ m}^2 = 6.3356\text{ m}^2$$
* Vertical Force (acting upwards on the bottom face):
  $$F_V = \rho g W A_{\text{fluid}} = (1000)(9.81)(10.0)(6.3356) = 621,522\text{ N} = 621.52\text{ kN} \quad (\text{acting upward})$$

#### Step 3: Total Resultant Force $F_R$ & Angle
$$F_R = \sqrt{(993.26)^2 + (621.52)^2} = \sqrt{986,565 + 386,287} = \sqrt{1,372,852} = 1171.69\text{ kN}$$
$$\theta = \arctan\left(\frac{621.52}{993.26}\right) = \arctan(0.6257) = 32.04^\circ \text{ above the horizontal}$$

---

### 4. Plausibility Sanity Check & Physical Meaning
* **Resultant passes through Pin:** Because the normal to every point on the circular cylinder intersects the pin axis, the moment arm is zero: $M_{\text{pin}} = 0$. This confirms the primary structural design advantage of radial gates: hoisted cables only need to overcome the gate dead weight and trunnion pin friction, not hydrostatic pressure moments.

---

# Problem 02: Pipeline Frictional Resistance, Wax Deposition & Diameter Sensitivity

### 1. Problem Statement
A crude oil transfer pipeline of nominal length $L = 5000\text{ m}$ and initial clean inside diameter $D_1 = 400\text{ mm}$ ($0.40\text{ m}$) transports light crude oil ($\rho = 860\text{ kg/m}^3$, kinematic viscosity $\nu = 6.0 \times 10^{-6}\text{ m}^2/\text{s}$) at a constant volumetric flow rate $Q = 0.20\text{ m}^3/\text{s}$. The absolute pipe roughness is $\epsilon = 0.046\text{ mm}$ (commercial steel).

**Determine:**
1. The initial flow regime (Reynolds number), Darcy friction factor $f_1$, and total frictional pressure drop $\Delta P_1$ in $\text{kPa}$.
2. If heavy paraffin wax precipitates uniformly along the pipe wall, forming an internal layer of thickness $\delta = 10\text{ mm}$ throughout the pipeline, determine the new effective diameter $D_2$, new Reynolds number, new friction factor $f_2$, and the updated pressure drop $\Delta P_2$.
3. Compute the percentage increase in pumping power required to maintain the identical volumetric throughput $Q$.

---

### 2. Governing Equations
* Reynolds number: $\mathrm{Re} = \frac{V D}{\nu} = \frac{4 Q}{\pi D \nu}$.
* Swamee-Jain explicit approximation to the Colebrook-White equation for turbulent flow:
  $$f = \frac{0.25}{\left[\log_{10}\left(\frac{\epsilon/D}{3.7} + \frac{5.74}{\mathrm{Re}^{0.9}}\right)\right]^2}$$
* Darcy-Weisbach frictional pressure drop:
  $$\Delta P = \rho g h_f = \rho g \left(f \frac{L}{D} \frac{V^2}{2g}\right) = \frac{8 f L \rho Q^2}{\pi^2 D^5}$$
* Pumping hydraulic power: $\mathcal{P} = Q \cdot \Delta P$.

---

### 3. Step-by-Step Calculation

#### Step 1: Baseline Clean Pipeline ($D_1 = 0.40\text{ m}$)
* Flow velocity:
  $$V_1 = \frac{4 Q}{\pi D_1^2} = \frac{4(0.20)}{\pi (0.40)^2} = \frac{0.80}{0.50265} = 1.5915\text{ m/s}$$
* Reynolds number:
  $$\mathrm{Re}_1 = \frac{V_1 D_1}{\nu} = \frac{(1.5915)(0.40)}{6.0 \times 10^{-6}} = 106,100 \implies \text{Turbulent Flow}$$
* Relative roughness:
  $$\frac{\epsilon}{D_1} = \frac{0.046 \times 10^{-3}\text{ m}}{0.40\text{ m}} = 0.000115$$
* Darcy friction factor $f_1$ via Swamee-Jain:
  $$\frac{\epsilon/D}{3.7} = \frac{0.000115}{3.7} = 3.108 \times 10^{-5}$$
  $$\frac{5.74}{\mathrm{Re}^{0.9}} = \frac{5.74}{(106,100)^{0.9}} = \frac{5.74}{32,492} = 1.766 \times 10^{-4}$$
  $$\text{Sum} = 3.108 \times 10^{-5} + 1.766 \times 10^{-4} = 2.0768 \times 10^{-4}$$
  $$\log_{10}(2.0768 \times 10^{-4}) = -3.6826$$
  $$f_1 = \frac{0.25}{(-3.6826)^2} = \frac{0.25}{13.5615} = 0.01843$$
* Frictional pressure drop $\Delta P_1$:
  $$\Delta P_1 = \frac{8(0.01843)(5000)(860)(0.20^2)}{\pi^2 (0.40)^5} = \frac{8 \times 0.01843 \times 5000 \times 860 \times 0.04}{9.8696 \times 0.01024} = \frac{25,359.68}{0.10106} = 250,937\text{ Pa} = 250.94\text{ kPa}$$

#### Step 2: Wax Deposition Pipeline ($D_2 = D_1 - 2\delta = 0.40 - 2(0.010) = 0.380\text{ m}$)
* Note: A $10\text{ mm}$ wall thickness reduces diameter by $2 \times 10 = 20\text{ mm}$ ($5\%$ reduction).
* New velocity:
  $$V_2 = \frac{4(0.20)}{\pi (0.380)^2} = \frac{0.80}{0.45365} = 1.7635\text{ m/s}$$
* New Reynolds number:
  $$\mathrm{Re}_2 = \frac{(1.7635)(0.380)}{6.0 \times 10^{-6}} = 111,688$$
* New relative roughness (assuming deposited wax surface maintains comparable or slightly rougher surface $\epsilon \approx 0.046\text{ mm}$):
  $$\frac{\epsilon}{D_2} = \frac{0.046 \times 10^{-3}}{0.380} = 0.000121$$
* New friction factor $f_2$:
  $$\frac{5.74}{(111,688)^{0.9}} = \frac{5.74}{34,036} = 1.686 \times 10^{-4}$$
  $$\text{Sum} = \frac{0.000121}{3.7} + 1.686 \times 10^{-4} = 3.27 \times 10^{-5} + 1.686 \times 10^{-4} = 2.013 \times 10^{-4}$$
  $$\log_{10}(2.013 \times 10^{-4}) = -3.696$$
  $$f_2 = \frac{0.25}{(-3.696)^2} = 0.01830$$
* New pressure drop $\Delta P_2$:
  $$\Delta P_2 = \frac{8(0.01830)(5000)(860)(0.20^2)}{\pi^2 (0.380)^5} = \frac{25,180.8}{9.8696 \times 0.0079235} = \frac{25,180.8}{0.07820} = 322,005\text{ Pa} = 322.01\text{ kPa}$$

#### Step 3: Percentage Increase in Pumping Power
$$\% \Delta \mathcal{P} = \frac{\Delta P_2 - \Delta P_1}{\Delta P_1} \times 100\% = \frac{322.01 - 250.94}{250.94} \times 100\% = \frac{71.07}{250.94} \times 100\% = +28.32\%$$

---

### 4. Physical Engineering Analysis
* A mere **5.0% reduction in pipe diameter** caused by wax deposition results in a **28.3% increase in pumping power requirement**!
* *Analytical Rule Check:* According to the differential sensitivity formula derived in Module A1:
  $$\frac{d(\Delta P)}{\Delta P} \approx -5 \frac{dD}{D} = -5 (-5.0\%) = +25.0\%$$
  The exact non-linear calculation yields $+28.32\%$, perfectly validating the first-order Taylor approximation.

---

# Problem 03: Parallel and Branched Pipe Network Hydraulic Analysis

### 1. Problem Statement
A cooling water distribution manifold branches at Junction $J_1$ into two parallel commercial steel pipes, Branch A and Branch B, which rejoin at Junction $J_2$. The total inflow is $Q_{\text{total}} = 0.35\text{ m}^3/\text{s}$.
* **Branch A:** $L_A = 800\text{ m}$, $D_A = 300\text{ mm}$ ($0.30\text{ m}$), $f_A = 0.020$, contains two $90^\circ$ standard elbows ($K_L = 0.30$ each).
* **Branch B:** $L_B = 1200\text{ m}$, $D_B = 250\text{ mm}$ ($0.25\text{ m}$), $f_B = 0.022$, contains one gate valve ($K_L = 0.20$).

**Determine:**
1. The individual flow rates $Q_A$ and $Q_B$ in each branch.
2. The total head loss $h_{L, J_1 \to J_2}$ between junctions.

---

### 2. Governing Equations & System Physics
1. **Continuity of Mass:** $Q_{\text{total}} = Q_A + Q_B$
2. **Uniqueness of Pressure Head:** Frictional head loss across parallel branches connected between identical pressure nodes must be identical:
   $$h_{L, A} = h_{L, B}$$
3. Head loss formulation:
   $$h_L = \left(f \frac{L}{D} + \sum K_L\right) \frac{V^2}{2g} = \left(f \frac{L}{D} + \sum K_L\right) \frac{8 Q^2}{\pi^2 g D^4} = K_{\text{pipe}} Q^2$$

---

### 3. Step-by-Step Calculation
* **Branch A Resistance Coefficient $K_A$:**
  $$f_A \frac{L_A}{D_A} = (0.020)\frac{800}{0.30} = 53.333$$
  $$\sum K_{L, A} = 2 \times 0.30 = 0.60$$
  $$\text{Total resistance factor } \mathcal{R}_A = 53.333 + 0.60 = 53.933$$
  $$K_A = \frac{8 \times \mathcal{R}_A}{\pi^2 g D_A^4} = \frac{8 \times 53.933}{(9.8696)(9.81)(0.30)^4} = \frac{431.464}{96.8208 \times 0.0081} = \frac{431.464}{0.78425} = 550.16\text{ s}^2/\text{m}^5$$

* **Branch B Resistance Coefficient $K_B$:**
  $$f_B \frac{L_B}{D_B} = (0.022)\frac{1200}{0.25} = 105.60$$
  $$\sum K_{L, B} = 0.20$$
  $$\mathcal{R}_B = 105.60 + 0.20 = 105.80$$
  $$K_B = \frac{8 \times 105.80}{(9.8696)(9.81)(0.25)^4} = \frac{846.40}{96.8208 \times 0.00390625} = \frac{846.40}{0.37821} = 2237.91\text{ s}^2/\text{m}^5$$

* **Equating Head Losses:**
  $$h_{L,A} = h_{L,B} \implies K_A Q_A^2 = K_B Q_B^2$$
  $$\frac{Q_A}{Q_B} = \sqrt{\frac{K_B}{K_A}} = \sqrt{\frac{2237.91}{550.16}} = \sqrt{4.0677} = 2.0168$$
  $$Q_A = 2.0168 \, Q_B$$

* **Solving Continuity:**
  $$Q_A + Q_B = 2.0168 Q_B + Q_B = 3.0168 Q_B = 0.35\text{ m}^3/\text{s}$$
  $$Q_B = \frac{0.35}{3.0168} = 0.1160\text{ m}^3/\text{s}$$
  $$Q_A = 0.35 - 0.1160 = 0.2340\text{ m}^3/\text{s}$$

* **Head Loss between Junctions:**
  $$h_{L,A} = K_A Q_A^2 = 550.16 \times (0.2340)^2 = 550.16 \times 0.054756 = 30.12\text{ m}$$
  $$h_{L,B} = K_B Q_B^2 = 2237.91 \times (0.1160)^2 = 2237.91 \times 0.013456 = 30.11\text{ m}$$
  *(Matches to within $0.03\%$, verifying calculation accuracy).*

---

# Problem 04: Centrifugal Pump Head Matching, Throttling & NPSH Margin

### 1. Problem Statement
A booster pump transfers liquid hydrocarbons ($\rho = 800\text{ kg/m}^3$, vapor pressure $P_v = 35.0\text{ kPa abs}$) from an atmospheric supply vessel ($P_{\text{atm}} = 101.3\text{ kPa abs}$) to a pressurized cracking unit maintained at $P_{\text{rec}} = 450\text{ kPa gauge}$.
* Liquid level in the supply vessel is $z_{\text{suction}} = +3.0\text{ m}$ above the pump centerline.
* Discharge receiver liquid entry point is $z_{\text{discharge}} = +18.0\text{ m}$ above the pump centerline.
* Suction line: $D_s = 200\text{ mm}$, length $L_s = 25\text{ m}$, total suction resistance coefficient $K_s = 4.2$.
* Total system discharge curve: $H_{\text{system}}(Q) = H_{\text{static}} + 380 Q^2$ (with $Q$ in $\text{m}^3/\text{s}$, $H$ in meters).
* Pump head characteristic: $H_{\text{pump}}(Q) = 85.0 - 240 Q^2$.
* Pump manufacturer states $\mathrm{NPSH}_R = 3.2\text{ m}$ at the operating discharge.

**Determine:**
1. The static head $H_{\text{static}}$ of the system.
2. The operating flow rate $Q_{\text{op}}$ and total developed pump head $H_{\text{op}}$.
3. The available Net Positive Suction Head ($\mathrm{NPSH}_A$) and check if cavitation will occur.

---

### 2. Step-by-Step Calculation

#### Step 1: Compute Static Head $H_{\text{static}}$
$$H_{\text{static}} = (z_{\text{discharge}} - z_{\text{suction}}) + \frac{P_{\text{rec, abs}} - P_{\text{supply, abs}}}{\rho g}$$
* $z_{\text{discharge}} - z_{\text{suction}} = 18.0 - 3.0 = 15.0\text{ m}$
* $P_{\text{rec, abs}} = 450\text{ kPa gauge} + 101.3\text{ kPa} = 551.3\text{ kPa abs}$
* $P_{\text{rec, abs}} - P_{\text{supply, abs}} = 551.3 - 101.3 = 450.0\text{ kPa} = 450,000\text{ Pa}$
* Pressure head component:
  $$\frac{\Delta P}{\rho g} = \frac{450,000}{(800)(9.81)} = \frac{450,000}{7,848} = 57.34\text{ m}$$
* Total Static Head:
  $$H_{\text{static}} = 15.0\text{ m} + 57.34\text{ m} = 72.34\text{ m}$$

#### Step 2: Operating Point Intersection
$$H_{\text{system}} = H_{\text{pump}}$$
$$72.34 + 380 Q^2 = 85.0 - 240 Q^2$$
$$620 Q^2 = 85.0 - 72.34 = 12.66$$
$$Q^2 = \frac{12.66}{620} = 0.020419 \implies Q_{\text{op}} = \sqrt{0.020419} = 0.1429\text{ m}^3/\text{s} \quad (142.9\text{ L/s})$$
* Operating Head:
  $$H_{\text{op}} = 85.0 - 240(0.020419) = 85.0 - 4.90 = 80.10\text{ m}$$

#### Step 3: Suction Line Velocity & Head Loss
* Suction pipe area:
  $$A_s = \frac{\pi}{4}(0.20)^2 = 0.031416\text{ m}^2$$
* Velocity:
  $$V_s = \frac{0.1429}{0.031416} = 4.549\text{ m/s}$$
* Velocity head:
  $$\frac{V_s^2}{2g} = \frac{(4.549)^2}{2(9.81)} = \frac{20.693}{19.62} = 1.055\text{ m}$$
* Suction frictional head loss:
  $$h_{L,s} = K_s \frac{V_s^2}{2g} = 4.2 \times 1.055\text{ m} = 4.43\text{ m}$$

#### Step 4: Net Positive Suction Head Available ($\mathrm{NPSH}_A$)
$$\mathrm{NPSH}_A = \frac{P_{\text{atm}}}{\rho g} + z_{\text{suction}} - h_{L,s} - \frac{P_v}{\rho g}$$
* Atmospheric head:
  $$\frac{P_{\text{atm}}}{\rho g} = \frac{101,300}{7,848} = 12.91\text{ m}$$
* Vapor pressure head:
  $$\frac{P_v}{\rho g} = \frac{35,000}{7,848} = 4.46\text{ m}$$
* Substituting:
  $$\mathrm{NPSH}_A = 12.91 + 3.0 - 4.43 - 4.46 = 7.02\text{ m}$$

#### Step 5: Cavitation Evaluation
* Margin:
  $$\mathrm{NPSH}_A - \mathrm{NPSH}_R = 7.02\text{ m} - 3.20\text{ m} = +3.82\text{ m} > 1.0\text{ m}$$
* **Conclusion:** The pump operates with an ample safety margin of $3.82\text{ m}$ above the cavitation inception threshold. The system will **not cavitate**.

---

# Problem 05: Water Hammer Acoustic Transient & Rapid Valve Closure Surge

### 1. Problem Statement
A high-pressure crude oil pipeline connecting an offshore mooring terminal to an onshore tank farm has length $L = 8.5\text{ km}$ ($8500\text{ m}$), diameter $D = 600\text{ mm}$ ($0.60\text{ m}$), and wall thickness $t = 12.5\text{ mm}$. The pipe material is API 5L Grade X65 steel ($E = 207\text{ GPa}$, Poisson's ratio $\nu = 0.30$).
The oil has density $\rho = 850\text{ kg/m}^3$ and bulk modulus of elasticity $K = 1.50\text{ GPa}$. Initial steady-state discharge is $Q = 0.85\text{ m}^3/\text{s}$.
An emergency shutdown valve (ESDV) at the downstream terminal closes fully in $T_v = 4.0\text{ seconds}$.

**Determine:**
1. The acoustic pressure wave propagation celerity $c$.
2. The pipe critical round-trip period $T_c = 2L/c$.
3. Whether the valve closure is hydraulically "rapid" or "slow".
4. The maximum transient Joukowsky water hammer pressure rise $\Delta P_{\max}$ in $\text{MPa}$ and equivalent head $\Delta H$ in meters.
5. The maximum total hoop stress induced in the steel pipe wall if the initial operating pressure was $P_0 = 3.5\text{ MPa}$. Compare this to the yield strength of X65 steel ($S_y = 448\text{ MPa}$).

---

### 2. Step-by-Step Calculation

#### Step 1: Acoustic Wave Speed $c$
For an axially anchored elastic pipeline:
$$c = \sqrt{\frac{K/\rho}{1 + \left(\frac{K}{E}\right)\left(\frac{D}{t}\right)(1 - \nu^2)}}$$
* Pure fluid celerity:
  $$\sqrt{\frac{K}{\rho}} = \sqrt{\frac{1.50 \times 10^9\text{ Pa}}{850\text{ kg/m}^3}} = \sqrt{1,764,706} = 1328.4\text{ m/s}$$
* Conduit elasticity correction factor:
  $$\left(\frac{K}{E}\right) = \frac{1.50 \times 10^9}{207 \times 10^9} = 0.007246$$
  $$\left(\frac{D}{t}\right) = \frac{600\text{ mm}}{12.5\text{ mm}} = 48.0$$
  $$(1 - \nu^2) = 1 - (0.30)^2 = 0.91$$
  $$\text{Elasticity term} = (0.007246) \times (48.0) \times (0.91) = 0.3165$$
* Wave celerity:
  $$c = \frac{1328.4}{\sqrt{1 + 0.3165}} = \frac{1328.4}{\sqrt{1.3165}} = \frac{1328.4}{1.1474} = 1157.7\text{ m/s}$$

#### Step 2: Critical Round-Trip Time $T_c$
$$T_c = \frac{2 L}{c} = \frac{2 \times 8500\text{ m}}{1157.7\text{ m/s}} = 14.68\text{ seconds}$$

#### Step 3: Valve Closure Classification
* Since the valve closure time $T_v = 4.0\text{ s} \le T_c = 14.68\text{ s}$, the closure is classified as **rapid (instantaneous)**.
* The reflected relief wave from the upstream terminal does **not** arrive at the valve before full closure occurs.

#### Step 4: Joukowsky Pressure Rise
* Initial velocity:
  $$A = \frac{\pi}{4}(0.60)^2 = 0.28274\text{ m}^2$$
  $$V_0 = \frac{Q}{A} = \frac{0.85}{0.28274} = 3.006\text{ m/s}$$
  $$\Delta V = V_0 - 0 = 3.006\text{ m/s}$$
* Joukowsky pressure surge:
  $$\Delta P_{\max} = \rho c \Delta V = (850\text{ kg/m}^3)(1157.7\text{ m/s})(3.006\text{ m/s}) = 2,958,041\text{ Pa} \approx 2.96\text{ MPa}$$
* Head rise:
  $$\Delta H = \frac{\Delta P}{\rho g} = \frac{c \Delta V}{g} = \frac{(1157.7)(3.006)}{9.81} = 354.7\text{ m of oil}$$

#### Step 5: Total Pressure and Hoop Stress Evaluation
* Total peak transient pressure:
  $$P_{\text{total}} = P_0 + \Delta P_{\max} = 3.50\text{ MPa} + 2.96\text{ MPa} = 6.46\text{ MPa}$$
* Maximum hoop stress:
  $$\sigma_h = \frac{P_{\text{total}} D}{2 t} = \frac{(6.46\text{ MPa})(600\text{ mm})}{2(12.5\text{ mm})} = \frac{3876}{25} = 155.04\text{ MPa}$$
* Comparison with yield strength:
  $$\frac{\sigma_h}{S_y} = \frac{155.04\text{ MPa}}{448\text{ MPa}} = 0.346 \implies 34.6\% \text{ of Yield}$$
* **Engineering Conclusion:** The pipe structure safely withstands the surge without plastic deformation. However, the $2.96\text{ MPa}$ surge may trip high-pressure safety instrumented systems (SIS) or damage downstream gaskets/fittings unless surge relief valves or slow-closing actuators are installed.

---

# Problem 06: Specific Energy, Critical Flow & Channel Choking under Contraction

### 1. Problem Statement
A rectangular concrete water diversion channel has width $B_1 = 4.0\text{ m}$ and carries a discharge $Q = 14.0\text{ m}^3/\text{s}$ at an approach flow depth $y_1 = 2.0\text{ m}$. To pass through a roadway culvert structure, the channel undergoes a smooth horizontal contraction to width $B_2$ with negligible head loss.

**Determine:**
1. The approach Froude number $\mathrm{Fr}_1$ and approach specific energy $E_1$.
2. The critical width $B_{2,\min}$ below which the upstream flow will choke (causing backwater rise).
3. If the channel is contracted to $B_2 = 2.5\text{ m}$ with an upward bed step of $\Delta z = +0.20\text{ m}$, determine whether choking occurs. If so, compute the new upstream depth $y_1'$.

---

### 2. Step-by-Step Calculation

#### Step 1: Upstream Approach Parameters
* Area: $A_1 = B_1 y_1 = 4.0 \times 2.0 = 8.0\text{ m}^2$
* Velocity: $V_1 = \frac{Q}{A_1} = \frac{14.0}{8.0} = 1.75\text{ m/s}$
* Approach Froude number:
  $$\mathrm{Fr}_1 = \frac{V_1}{\sqrt{g y_1}} = \frac{1.75}{\sqrt{9.81 \times 2.0}} = \frac{1.75}{\sqrt{19.62}} = \frac{1.75}{4.429} = 0.395 \implies \text{Subcritical}$$
* Approach Specific Energy:
  $$E_1 = y_1 + \frac{V_1^2}{2g} = 2.0 + \frac{(1.75)^2}{19.62} = 2.0 + 0.156 = 2.156\text{ m}$$

#### Step 2: Critical Width for Choking (Flat Bed, $\Delta z = 0$)
At minimum width, the contracted section must operate at critical flow with maximum specific energy available $E_{c2} = E_1 = 2.156\text{ m}$.
* In a rectangular channel, $E_c = 1.5 y_c \implies y_c = \frac{2}{3} E_1 = \frac{2}{3}(2.156) = 1.4373\text{ m}$.
* Critical discharge per unit width:
  $$q_c = \sqrt{g y_c^3} = \sqrt{(9.81)(1.4373)^3} = \sqrt{(9.81)(2.970)} = \sqrt{29.136} = 5.398\text{ m}^2/\text{s}$$
* Critical minimum width:
  $$B_{2,\min} = \frac{Q}{q_c} = \frac{14.0}{5.398} = 2.593\text{ m}$$

#### Step 3: Check Contraction with Bed Step ($\Delta z = +0.20\text{ m}$, $B_2 = 2.5\text{ m}$)
* Available specific energy at the contracted section:
  $$E_{2,\text{avail}} = E_1 - \Delta z = 2.156 - 0.20 = 1.956\text{ m}$$
* Specific discharge at contracted section:
  $$q_2 = \frac{Q}{B_2} = \frac{14.0}{2.5} = 5.60\text{ m}^2/\text{s}$$
* Critical depth required for $q_2 = 5.60$:
  $$y_{c2} = \sqrt[3]{\frac{q_2^2}{g}} = \sqrt[3]{\frac{5.60^2}{9.81}} = \sqrt[3]{\frac{31.36}{9.81}} = \sqrt[3]{3.1967} = 1.473\text{ m}$$
* Minimum specific energy required to pass this flow:
  $$E_{c2,\min} = 1.5 y_{c2} = 1.5(1.473) = 2.210\text{ m}$$
* **Choking Evaluation:**
  $$E_{2,\text{avail}} (1.956\text{ m}) < E_{c2,\min} (2.210\text{ m})$$
  **Choking occurs!** The contracted channel cannot pass $14.0\text{ m}^3/\text{s}$ at the existing upstream energy head. The upstream depth must back up and rise to a new depth $y_1'$.

#### Step 4: Compute Upstream Backwater Depth $y_1'$
The flow at the choke point will become critical: $E_2' = E_{c2,\min} = 2.210\text{ m}$.
* The new upstream specific energy must be:
  $$E_1' = E_2' + \Delta z = 2.210 + 0.20 = 2.410\text{ m}$$
* Upstream specific energy equation with $B_1 = 4.0\text{ m}$:
  $$E_1' = y_1' + \frac{Q^2}{2g (B_1 y_1')^2} \implies 2.410 = y_1' + \frac{14.0^2}{2(9.81)(4.0)^2 (y_1')^2} = y_1' + \frac{196}{313.92 (y_1')^2} = y_1' + \frac{0.6244}{(y_1')^2}$$
* Solving $y_1' + \frac{0.6244}{(y_1')^2} = 2.410$:
  - Try $y_1' = 2.30\text{ m}$: $2.30 + \frac{0.6244}{5.29} = 2.30 + 0.118 = 2.418$ (slightly high)
  - Try $y_1' = 2.29\text{ m}$: $2.29 + \frac{0.6244}{5.244} = 2.29 + 0.119 = 2.409$
  $$y_1' \approx 2.291\text{ m}$$
* **Result:** Upstream water depth increases from $2.00\text{ m}$ to $2.291\text{ m}$ ($+29.1\text{ cm}$ backwater rise).

---

# Problem 07: Hydraulic Jump Conjugate Depth & Energy Dissipation Stilling Basin

### 1. Problem Statement
Water discharges over an industrial reservoir spillway into a rectangular stilling basin of width $B = 12.0\text{ m}$. At the apron toe, flow depth is $y_1 = 0.50\text{ m}$ and flow velocity is $V_1 = 16.0\text{ m/s}$. A hydraulic jump forms on the horizontal apron.

**Determine:**
1. The initial Froude number $\mathrm{Fr}_1$.
2. The subcritical conjugate post-jump depth $y_2$.
3. The post-jump flow velocity $V_2$ and post-jump Froude number $\mathrm{Fr}_2$.
4. The rate of turbulent energy head dissipation $\Delta E_L$ in meters.
5. The total mechanical power dissipated in the jump in megawatts ($\text{MW}$).

---

### 2. Step-by-Step Calculation

#### Step 1: Upstream Froude Number $\mathrm{Fr}_1$
$$\mathrm{Fr}_1 = \frac{V_1}{\sqrt{g y_1}} = \frac{16.0}{\sqrt{9.81 \times 0.50}} = \frac{16.0}{\sqrt{4.905}} = \frac{16.0}{2.2147} = 7.224$$
*(Since $\mathrm{Fr}_1 = 7.22 > 4.5$, this is a well-established, steady, highly effective jump).*

#### Step 2: Conjugate Depth $y_2$ via Bélanger Equation
$$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 \mathrm{Fr}_1^2} - 1\right)$$
$$8 \mathrm{Fr}_1^2 = 8 \times (7.224)^2 = 8 \times 52.19 = 417.52$$
$$\sqrt{1 + 417.52} = \sqrt{418.52} = 20.458$$
$$\frac{y_2}{y_1} = \frac{1}{2}(20.458 - 1) = \frac{19.458}{2} = 9.729$$
$$y_2 = 9.729 \times 0.50\text{ m} = 4.864\text{ m}$$

#### Step 3: Post-Jump Velocity $V_2$ & $\mathrm{Fr}_2$
* By continuity:
  $$V_2 = V_1 \left(\frac{y_1}{y_2}\right) = \frac{16.0}{9.729} = 1.644\text{ m/s}$$
* Post-jump Froude number:
  $$\mathrm{Fr}_2 = \frac{V_2}{\sqrt{g y_2}} = \frac{1.644}{\sqrt{9.81 \times 4.864}} = \frac{1.644}{\sqrt{47.716}} = \frac{1.644}{6.908} = 0.238 \implies \text{Tranquil Subcritical}$$

#### Step 4: Energy Head Loss $\Delta E_L$
$$\Delta E_L = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(4.864 - 0.50)^3}{4 \times 0.50 \times 4.864} = \frac{(4.364)^3}{9.728} = \frac{83.109}{9.728} = 8.543\text{ m}$$
* Verification via specific energy:
  $$E_1 = y_1 + \frac{V_1^2}{2g} = 0.50 + \frac{16.0^2}{19.62} = 0.50 + 13.048 = 13.548\text{ m}$$
  $$E_2 = y_2 + \frac{V_2^2}{2g} = 4.864 + \frac{1.644^2}{19.62} = 4.864 + 0.138 = 5.002\text{ m}$$
  $$\Delta E_L = 13.548 - 5.002 = 8.546\text{ m} \quad (\text{Exact agreement})$$
* Efficiency of jump: $\frac{\Delta E_L}{E_1} = \frac{8.543}{13.548} = 63.06\%$ of incoming energy is destroyed in the roller!

#### Step 5: Power Dissipation
* Discharge:
  $$Q = B \cdot y_1 \cdot V_1 = 12.0 \times 0.50 \times 16.0 = 96.0\text{ m}^3/\text{s}$$
* Dissipated power:
  $$\mathcal{P} = \rho g Q \Delta E_L = (1000\text{ kg/m}^3)(9.81\text{ m/s}^2)(96.0\text{ m}^3/\text{s})(8.543\text{ m}) = 8,045,431\text{ Watts} = 8.045\text{ MW}$$
* **Engineering Significance:** The stilling basin safely dissipates over $8.0\text{ MW}$ of raw turbulent kinetic energy, preventing severe scouring of the downstream river channel bed.

---

# Problem 08: Gradually Varied Flow (GVF) Backwater Profile Step Integration

### 1. Problem Statement
A wide rectangular cooling channel ($B = 10.0\text{ m}$, Manning's $n = 0.015$, bed slope $S_0 = 0.0008$) conveys $Q = 20.0\text{ m}^3/\text{s}$. A control weir downstream elevates the water depth to $y = 3.0\text{ m}$ at Station 0 ($x = 0$).

**Determine:**
1. The normal depth $y_n$ and critical depth $y_c$.
2. The classification of the water surface profile ($M_1$, $M_2$, or $M_3$).
3. Using the Direct Step Method across two depth intervals ($\Delta y = 0.25\text{ m}$), compute the distance upstream from Station 0 to the location where depth drops to $y = 2.50\text{ m}$.

---

### 2. Step-by-Step Calculation

#### Step 1: Normal Depth $y_n$ & Critical Depth $y_c$
* Unit discharge: $q = Q / B = 20.0 / 10.0 = 2.0\text{ m}^2/\text{s}$.
* Critical depth:
  $$y_c = \sqrt[3]{\frac{q^2}{g}} = \sqrt[3]{\frac{2.0^2}{9.81}} = \sqrt[3]{\frac{4.0}{9.81}} = \sqrt[3]{0.4077} = 0.7415\text{ m}$$
* **Normal Depth Computation Comparison:**
  - **Exact Rectangular Formulation:**
    Wetted area $A = B y_n = 10 y_n$, wetted perimeter $P = B + 2y_n = 10 + 2y_n$, hydraulic radius $R_h = \frac{10 y_n}{10 + 2y_n}$.
    Manning's uniform flow equation:
    $$Q = \frac{1}{n} A R_h^{2/3} S_0^{1/2} \implies 20.0 = \frac{1}{0.015} (10 y_n)\left(\frac{10 y_n}{10 + 2y_n}\right)^{2/3} (0.0008)^{1/2}$$
    $$\frac{Q n}{\sqrt{S_0}} = \frac{20.0 \times 0.015}{\sqrt{0.0008}} = \frac{0.30}{0.028284} = 10.6066 = \frac{(10 y_n)^{5/3}}{(10 + 2y_n)^{2/3}}$$
    Solving numerically:
    - At $y_n = 1.124\text{ m}$: $A = 11.24\text{ m}^2$, $P = 12.248\text{ m}$, $R_h = 0.9177\text{ m}$, $A R_h^{2/3} = 11.24 \times (0.9177)^{2/3} = 11.24 \times 0.9442 = 10.612 \approx 10.607$.
    $$\mathbf{y_n = 1.124\text{ m}}$$
  - **Wide-Channel Approximation Check ($R_h \approx y$):**
    If side-wall resistance were ignored:
    $$A R_h^{2/3} \approx 10 y_n^{5/3} = 10.6066 \implies y_n = (1.06066)^{3/5} = 1.0357\text{ m} \approx 1.036\text{ m}$$
    *Physical Insight:* The wide-channel assumption underpredicts normal depth by $\approx 8.5\%$ because $B/y_n = 10 / 1.124 = 8.9 < 10$. In engineered canals, side-wall shear cannot be neglected. We use the rigorous value $y_n = 1.124\text{ m}$.
* **Profile Classification:**
  Since $y_n (1.125\text{ m}) > y_c (0.742\text{ m})$, the channel slope is **MILD ($M$)**.
  Current depth $y = 3.0\text{ m} > y_n > y_c$. The surface curve lies in Zone 1.
  Therefore, this is an **$M_1$ Backwater Profile** ($\frac{dy}{dx} > 0$).

#### Step 2: Direct Step Method Integration Formulation
$$\Delta x = \frac{E_2 - E_1}{S_0 - \bar{S}_f}$$
where $E = y + \frac{V^2}{2g}$ and $S_f = \frac{n^2 V^2}{R^{4/3}}$.

#### Interval 1: $y_A = 3.00\text{ m} \to y_B = 2.75\text{ m}$
* Station A ($y_A = 3.00\text{ m}$):
  $A_A = 30.0\text{ m}^2$, $V_A = 20.0 / 30.0 = 0.6667\text{ m/s}$
  $E_A = 3.00 + \frac{0.6667^2}{19.62} = 3.00 + 0.0227 = 3.0227\text{ m}$
  $P_A = 10 + 2(3.0) = 16.0\text{ m}$, $R_A = 30/16 = 1.875\text{ m}$
  $S_{f,A} = \frac{(0.015)^2 (0.6667)^2}{(1.875)^{4/3}} = \frac{0.000225 \times 0.4444}{2.308} = 4.332 \times 10^{-5}$
* Station B ($y_B = 2.75\text{ m}$):
  $A_B = 27.5\text{ m}^2$, $V_B = 20.0 / 27.5 = 0.7273\text{ m/s}$
  $E_B = 2.75 + \frac{0.7273^2}{19.62} = 2.75 + 0.0270 = 2.7770\text{ m}$
  $P_B = 10 + 2(2.75) = 15.5\text{ m}$, $R_B = 27.5/15.5 = 1.774\text{ m}$
  $S_{f,B} = \frac{(0.015)^2 (0.7273)^2}{(1.774)^{4/3}} = \frac{0.000225 \times 0.5289}{2.144} = 5.551 \times 10^{-5}$
* Interval 1 Average:
  $\Delta E = 2.7770 - 3.0227 = -0.2457\text{ m}$
  $\bar{S}_f = \frac{4.332 \times 10^{-5} + 5.551 \times 10^{-5}}{2} = 4.942 \times 10^{-5}$
  $S_0 - \bar{S}_f = 0.000800 - 0.0000494 = 0.0007506$
  $$\Delta x_1 = \frac{-0.2457}{0.0007506} = -327.3\text{ m} \quad (\text{negative indicates upstream})$$

#### Interval 2: $y_B = 2.75\text{ m} \to y_C = 2.50\text{ m}$
* Station C ($y_C = 2.50\text{ m}$):
  $A_C = 25.0\text{ m}^2$, $V_C = 20.0 / 25.0 = 0.800\text{ m/s}$
  $E_C = 2.50 + \frac{0.800^2}{19.62} = 2.50 + 0.0326 = 2.5326\text{ m}$
  $P_C = 10 + 2(2.50) = 15.0\text{ m}$, $R_C = 25/15 = 1.667\text{ m}$
  $S_{f,C} = \frac{(0.015)^2 (0.800)^2}{(1.667)^{4/3}} = \frac{0.000225 \times 0.640}{1.972} = 7.302 \times 10^{-5}$
* Interval 2 Average:
  $\Delta E = 2.5326 - 2.7770 = -0.2444\text{ m}$
  $\bar{S}_f = \frac{5.551 \times 10^{-5} + 7.302 \times 10^{-5}}{2} = 6.427 \times 10^{-5}$
  $S_0 - \bar{S}_f = 0.000800 - 0.0000643 = 0.0007357$
  $$\Delta x_2 = \frac{-0.2444}{0.0007357} = -332.2\text{ m}$$

#### Total Distance:
$$X = |\Delta x_1| + |\Delta x_2| = 327.3\text{ m} + 332.2\text{ m} = 659.5\text{ m upstream}$$

---

# Problem 09: Unit Hydrograph S-Curve Conversion and Convolution

### 1. Problem Statement
The ordinates of a 2-hour unit hydrograph ($2\text{-hr UH}$) derived for an industrial terminal catchment (area $A = 21.6\text{ km}^2$) are given at 2-hour intervals as follows:

| Time (hr) | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2-hr UH ($m^3/s$)** | 0 | 5 | 18 | 24 | 15 | 8 | 3 | 0 |

**Determine:**
1. Verify the total direct runoff volume and confirm that the unit depth equals $1.0\text{ cm}$.
2. Construct the S-hydrograph curve.
3. Derive the ordinates of a **4-hour unit hydrograph ($4\text{-hr UH}$)** for this catchment.

---

### 2. Step-by-Step Calculation

#### Step 1: Unit Hydrograph Volume Check & Normalization
* Time step: $\Delta t = 2\text{ hours} = 2 \times 3600 = 7200\text{ seconds}$.
* Sum of raw ordinates:
  $$\sum U_{\text{raw}} = 0 + 5 + 18 + 24 + 15 + 8 + 3 + 0 = 73.0\text{ m}^3/\text{s}$$
* Total direct runoff volume represented by raw ordinates:
  $$V_{\text{runoff}} = \sum U_{\text{raw}} \times \Delta t = 73.0\text{ m}^3/\text{s} \times 7200\text{ s} = 525,600\text{ m}^3$$
* Equivalent runoff depth over catchment area ($A = 21.6\text{ km}^2 = 21.6 \times 10^6\text{ m}^2$):
  $$d = \frac{V_{\text{runoff}}}{A} = \frac{525,600\text{ m}^3}{21,600,000\text{ m}^2} = 0.024333\text{ m} = 2.4333\text{ cm}$$
* **Hydrological Normalization to True $1.0\text{ cm}$ Unit Hydrograph:**
  Since standard unit hydrographs represent exactly $1.0\text{ cm}$ of direct runoff, each raw ordinate is scaled:
  $$U_{\text{true}}(t) = \frac{U_{\text{raw}}(t)}{2.4333}$$
  - $U(0) = 0.00\text{ m}^3/\text{s}$
  - $U(2) = 5 / 2.4333 = 2.055\text{ m}^3/\text{s}$
  - $U(4) = 18 / 2.4333 = 7.397\text{ m}^3/\text{s}$
  - $U(6) = 24 / 2.4333 = 9.863\text{ m}^3/\text{s}$
  - $U(8) = 15 / 2.4333 = 6.164\text{ m}^3/\text{s}$
  - $U(10) = 8 / 2.4333 = 3.288\text{ m}^3/\text{s}$
  - $U(12) = 3 / 2.4333 = 1.233\text{ m}^3/\text{s}$
  - $U(14) = 0.00\text{ m}^3/\text{s}$
  $$\sum U_{\text{true}} = 30.00\text{ m}^3/\text{s} \implies V_{\text{true}} = 30.0 \times 7200 = 216,000\text{ m}^3 \equiv 1.00\text{ cm}$$

#### Step 2 & 3: S-Curve Addition & 4-hr UH Derivation
The S-curve represents continuous discharge generated by an infinite sequence of consecutive 2-hr rainfalls of unit intensity ($1.0\text{ cm} / 2\text{ hr} = 0.5\text{ cm/hr}$).
Equilibrium discharge: $S_{\infty} = \frac{A \times 10^4}{3600 \times D} = \frac{21.6 \times 10^6 \times 0.01}{7200} = 30.0\text{ m}^3/\text{s}$.
To derive the 4-hr UH ($D' = 4\text{ hr}$):
$$U_{4\text{-hr}}(t) = \left[S(t) - S(t - 4)\right] \times \frac{D}{D'} = \frac{S(t) - S(t - 4)}{2}$$

| Time $t$ (hr) | 2-hr UH $U(t)$ | S-Curve $S(t)$ | Lagged $S(t-4)$ | Difference $\Delta S$ | **True 4-hr UH** $U_4(t) = \Delta S / 2$ | Raw Scale $U_{4,\text{raw}}(t)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 0.00 | 0.00 | - | 0.00 | **0.00** | 0.0 |
| **2** | 2.05 | 2.05 | - | 2.05 | **1.03** | 2.5 |
| **4** | 7.40 | 9.45 | 0.00 | 9.45 | **4.73** | 11.5 |
| **6** | 9.86 | 19.31 | 2.05 | 17.26 | **8.63** | 21.0 |
| **8** | 6.16 | 25.47 | 9.45 | 16.02 | **8.01** | 19.5 |
| **10** | 3.29 | 28.76 | 19.31 | 9.45 | **4.73** | 11.5 |
| **12** | 1.23 | 30.00 | 25.47 | 4.53 | **2.27** | 5.5 |
| **14** | 0.00 | 30.00 | 28.76 | 1.24 | **0.62** | 1.5 |
| **16** | 0.00 | 30.00 | 30.00 | 0.00 | **0.00** | 0.0 |

* **Verification:** Peak true 4-hr UH is $8.63\text{ m}^3/\text{s}$ at $t = 6\text{ hr}$, compared to $9.86\text{ m}^3/\text{s}$ for 2-hr UH. Sum of 4-hr UH ordinates $= 30.02 \approx 30.0\text{ m}^3/\text{s}$, confirming unit runoff conservation.

#### Step 4: Practical Rainfall Convolution Example
* Suppose a storm produces two consecutive 4-hour rainfall excesses:
  - Period 1 ($0 - 4\text{ hr}$): $R_1 = 3.0\text{ cm}$
  - Period 2 ($4 - 8\text{ hr}$): $R_2 = 2.0\text{ cm}$
  - Baseflow is constant at $Q_{\text{base}} = 10.0\text{ m}^3/\text{s}$.
* Total streamflow at each time step is obtained by discrete convolution:
  $$Q_{\text{total}}(t) = R_1 \cdot U_4(t) + R_2 \cdot U_4(t - 4) + Q_{\text{base}}$$
  - At $t = 4\text{ hr}$: $Q = 3.0(4.73) + 2.0(0) + 10.0 = 14.19 + 10.0 = 24.19\text{ m}^3/\text{s}$.
  - At $t = 6\text{ hr}$: $Q = 3.0(8.63) + 2.0(1.03) + 10.0 = 25.89 + 2.06 + 10.0 = 37.95\text{ m}^3/\text{s}$.
  - At $t = 8\text{ hr}$: $Q = 3.0(8.01) + 2.0(4.73) + 10.0 = 24.03 + 9.46 + 10.0 = 43.49\text{ m}^3/\text{s}$ (Peak Flood).

---

# Problem 10: Bed Shear Stress, Incipient Motion & Shields Parameter Verification

### 1. Problem Statement
An unlined stormwater diversion channel carrying facility runoff has a wide rectangular bed with slope $S_0 = 0.0006$ and design water depth $y = 1.80\text{ m}$. The bed material consists of uniform quartz sand with median grain diameter $d_{50} = 2.0\text{ mm}$ ($0.002\text{ m}$) and particle density $\rho_s = 2650\text{ kg/m}^3$. Water temperature is $20^\circ\text{C}$ ($\rho = 1000\text{ kg/m}^3$, kinematic viscosity $\nu = 1.0 \times 10^{-6}\text{ m}^2/\text{s}$).

**Determine:**
1. The hydrodynamic bed shear stress $\tau_b$ and shear friction velocity $u_*$.
2. The particle Reynolds number $\mathrm{Re}_*$.
3. The dimensionless Shields parameter $\tau_*$.
4. Determine whether sediment motion initiates if the critical Shields parameter is $\tau_{*c} = 0.045$.
5. Compute the critical flow depth $y_{\text{crit}}$ below which the channel bed will remain stable without scour.

---

### 2. Step-by-Step Calculation

#### Step 1: Bed Shear Stress & Shear Velocity
* For a wide rectangular channel ($R \approx y = 1.80\text{ m}$):
  $$\tau_b = \rho g R S_0 = (1000\text{ kg/m}^3)(9.81\text{ m/s}^2)(1.80\text{ m})(0.0006) = 10.595\text{ N/m}^2\text{ (Pa)}$$
* Shear velocity:
  $$u_* = \sqrt{\frac{\tau_b}{\rho}} = \sqrt{\frac{10.595}{1000}} = \sqrt{0.010595} = 0.1029\text{ m/s}$$

#### Step 2: Particle Reynolds Number $\mathrm{Re}_*$
$$\mathrm{Re}_* = \frac{u_* d_{50}}{\nu} = \frac{(0.1029\text{ m/s})(0.002\text{ m})}{1.0 \times 10^{-6}\text{ m}^2/\text{s}} = 205.8$$
*(Since $\mathrm{Re}_* > 70$, flow over the grain boundaries is in the fully rough turbulent regime).*

#### Step 3: Compute Shields Parameter $\tau_*$
$$\tau_* = \frac{\tau_b}{(\rho_s - \rho) g d_{50}} = \frac{10.595}{(2650 - 1000)(9.81)(0.002)} = \frac{10.595}{1650 \times 9.81 \times 0.002} = \frac{10.595}{32.373} = 0.3273$$

#### Step 4: Incipient Motion Evaluation
* Comparison:
  $$\tau_* (0.3273) \gg \tau_{*c} (0.045)$$
  $$\frac{\tau_*}{\tau_{*c}} = \frac{0.3273}{0.045} = 7.27$$
* **Conclusion:** The hydrodynamic shear stress is more than **7 times greater** than the threshold required for particle dislodgement. The bed is in active, intense bedload sediment transport.

#### Step 5: Critical Depth for Bed Stability ($y_{\text{crit}}$)
Set $\tau_* = \tau_{*c} = 0.045$:
$$\tau_{b,\text{crit}} = \tau_{*c} (\rho_s - \rho) g d_{50} = 0.045 \times 32.373 = 1.457\text{ N/m}^2$$
$$\tau_{b,\text{crit}} = \rho g y_{\text{crit}} S_0 \implies y_{\text{crit}} = \frac{\tau_{b,\text{crit}}}{\rho g S_0} = \frac{1.457}{(1000)(9.81)(0.0006)} = \frac{1.457}{5.886} = 0.2475\text{ m} \approx 24.8\text{ cm}$$
* **Engineering Recommendation:** To prevent channel erosion during flood flows where depth reaches $1.80\text{ m}$, the bed must either be protected by riprap rock armor or concrete paving.

---

# Problem 11: Equilibrium Bridge Pier Scour Calculation (HEC-18 Standard)

### 1. Problem Statement
A pipeline trestle crossing a major river is supported by circular cylindrical concrete piers of diameter $a = 1.80\text{ m}$. During a 100-year design flood, the approach flow parameters are:
* Approach flow depth: $y_1 = 3.60\text{ m}$
* Mean approach velocity: $V_1 = 2.80\text{ m/s}$
* Pier nose geometry: Round nose ($K_1 = 1.0$)
* Alignment: Flow aligned with pier axis ($K_2 = 1.0$)
* Bed configuration: Clear-water plane bed ($K_3 = 1.1$)
* Armoring factor: $K_4 = 1.0$ (fine bed material)

**Determine:**
1. The approach Froude number $\mathrm{Fr}_1$.
2. The equilibrium local pier scour depth $y_s$ using the FHWA HEC-18 standard formula.
3. The total depth of the riverbed scour hole below the flood water surface ($y_{\text{total}} = y_1 + y_s$).

---

### 2. Step-by-Step Calculation

#### Step 1: Approach Froude Number $\mathrm{Fr}_1$
$$\mathrm{Fr}_1 = \frac{V_1}{\sqrt{g y_1}} = \frac{2.80}{\sqrt{9.81 \times 3.60}} = \frac{2.80}{\sqrt{35.316}} = \frac{2.80}{5.943} = 0.471$$

#### Step 2: HEC-18 5th Edition (2012) Pier Scour Evaluation
The primary CSU / FHWA HEC-18 5th Edition equation for live-bed and clear-water pier scour in sand-bed rivers is:
$$\frac{y_s}{y_1} = 2.0 \, K_1 K_2 K_3 \left(\frac{a}{y_1}\right)^{0.65} \mathrm{Fr}_1^{0.43}$$
* **Standard Coefficients (HEC-18 Table 6.1 - 6.3):**
  - Nose shape: $K_1 = 1.0$ (circular or round-nose)
  - Angle of attack: $K_2 = (\cos \theta + \frac{L}{a} \sin \theta)^{0.65} = 1.0$ for aligned flow ($\theta = 0^\circ$)
  - Bed condition: $K_3 = 1.1$ (clear-water scour or plane bed with small dunes)
  - *Note on $K_4$ (Armoring Factor) & Coarse Bed Scour Criteria:* In FHWA HEC-18 5th Edition (Arneson et al., 2012, Section 6.4), the legacy empirical $K_4$ multiplier was discontinued. FHWA defines coarse bed material requiring the dedicated coarse-bed scour equation by two criteria: median grain diameter $D_{50} \ge 20.1\text{ mm}$ (gravel and cobble sizes) and gradation coefficient $D_{84} / D_{50} \ge 1.5$. For sand beds ($D_{50} < 20.1\text{ mm}$), the standard CSU equation applies without an armoring reduction factor ($K_4 = 1.0$), ensuring conservative equilibrium scour estimates under live-bed or clear-water conditions.
* Relative dimensions:
  $$\frac{a}{y_1} = \frac{1.80}{3.60} = 0.50 \implies \left(\frac{a}{y_1}\right)^{0.65} = (0.50)^{0.65} = 0.6373$$
  $$\mathrm{Fr}_1^{0.43} = (0.471)^{0.43} = 0.7238$$
* Scour depth ratio:
  $$\frac{y_s}{y_1} = 2.0 \times (1.0 \times 1.0 \times 1.1) \times 0.6373 \times 0.7238 = 2.20 \times 0.4613 = 1.0148$$
* Equilibrium local pier scour depth:
  $$y_s = 1.0148 \times 3.60\text{ m} = \mathbf{3.653\text{ m}}$$
* Maximum Scour Limit Check (HEC-18 Clause 6.2):
  For $\mathrm{Fr}_1 \le 0.8$, $y_s \le 2.4 a = 2.4(1.80) = 4.32\text{ m}$.
  Since $y_s = 3.653\text{ m} < 4.32\text{ m}$, the computed scour is valid and within envelope limits.

#### Step 3: Total Scour & Geotechnical Foundation Embedment
* Total depth from water surface to bottom of scour hole:
  $$y_{\text{total}} = y_1 + y_s = 3.60\text{ m} + 3.653\text{ m} = 7.253\text{ m}$$
* **Geotechnical Foundation Design Rule (FHWA Technical Advisory T 5140.23):**
  - All lateral soil resistance above the scour elevation ($y_{\text{total}}$) must be considered completely lost during the design flood event.
  - Bridge or trestle foundation piles must achieve structural fixity by penetrating a minimum depth of $3a$ to $5a$ ($5.5\text{ m}$ to $9.0\text{ m}$) into competent, non-erodible geological strata *below* the maximum scour line.

---

# Problem 12: Exner Morphodynamic Riverbed Aggradation/Degradation Rate

### 1. Problem Statement
A reach of an industrial drainage channel of width $B = 8.0\text{ m}$ is undergoing steady non-uniform sediment transport. At an upstream transect ($x_1 = 0$), volumetric bedload transport rate is $Q_{s1} = 0.040\text{ m}^3/\text{s}$. Due to downstream channel widening, the transport capacity at $x_2 = 200\text{ m}$ downstream drops to $Q_{s2} = 0.016\text{ m}^3/\text{s}$. The bed material porosity is $\lambda_p = 0.40$.

**Determine:**
1. The spatial gradient of volumetric sediment transport per unit width $\frac{\partial q_s}{\partial x}$.
2. Whether the reach experiences aggradation (deposition) or degradation (scour).
3. The vertical rate of riverbed elevation change $\frac{\partial z_b}{\partial t}$ in $\text{mm/hour}$.
4. The net rise or fall of the bed elevation after 48 hours of continuous flood operation.

---

### 2. Step-by-Step Calculation

#### Step 1: Unit Sediment Transport Rates
* Transport rates $Q_s$ represent solid mineral volume transport rates (excluding inter-particle void volume):
  $$q_{s1} = \frac{Q_{s1}}{B} = \frac{0.040\text{ m}^3/\text{s}}{8.0\text{ m}} = 0.0050\text{ m}^2/\text{s}$$
  $$q_{s2} = \frac{Q_{s2}}{B} = \frac{0.016\text{ m}^3/\text{s}}{8.0\text{ m}} = 0.0020\text{ m}^2/\text{s}$$
* Spatial divergence over reach length $\Delta x = 200\text{ m}$:
  $$\frac{\partial q_s}{\partial x} \approx \frac{q_{s2} - q_{s1}}{\Delta x} = \frac{0.0020 - 0.0050}{200} = \frac{-0.0030}{200} = -1.50 \times 10^{-5}\text{ m/s}$$
  *(Or via width-averaged total load formulation: $\frac{1}{B} \frac{\partial Q_s}{\partial x} = \frac{1}{8.0} \frac{-0.024}{200} = -1.50 \times 10^{-5}\text{ m/s}$, confirming mathematical equivalence).*

#### Step 2 & 3: Exner Morphodynamic Equation Evaluation
The conservation of sediment mass (Exner equation) states:
$$(1 - \lambda_p) \frac{\partial z_b}{\partial t} + \frac{\partial q_s}{\partial x} = 0 \implies \frac{\partial z_b}{\partial t} = -\frac{1}{1 - \lambda_p} \frac{\partial q_s}{\partial x}$$
where $\lambda_p = 0.40$ is bed porosity (void fraction), so $(1 - \lambda_p) = 0.60$ is the solid packing fraction.
* Rate of vertical bed elevation change:
  $$\frac{\partial z_b}{\partial t} = -\frac{1}{0.60} (-1.50 \times 10^{-5}\text{ m/s}) = +2.50 \times 10^{-5}\text{ m/s}$$
* **Process Identification:**
  Since $\frac{\partial z_b}{\partial t} > 0$, sediment input exceeds sediment output ($Q_{s1} > Q_{s2}$). The channel reach is undergoing active **aggradation (sediment deposition)**.
* Conversion to engineering units ($\text{mm/hour}$):
  $$\frac{\partial z_b}{\partial t} = (2.50 \times 10^{-5}\text{ m/s}) \times (1000\text{ mm/m}) \times (3600\text{ s/hr}) = \mathbf{90.0\text{ mm/hour}}$$

#### Step 4: Total Aggradation over 48 Hours & Morphodynamic Feedback
* Initial linear extrapolation:
  $$\Delta z_b = (90.0\text{ mm/hour}) \times 48\text{ hours} = 4320\text{ mm} = \mathbf{4.32\text{ meters}}$$
* **Morphodynamic Negative Feedback & Engineering Limitations:**
  - In actual river channels, aggradation elevates the bed, reducing flow depth ($y$) and steepening the local water surface slope ($S_w$). This accelerates flow velocity, increasing boundary shear stress and local transport capacity ($Q_{s2}$).
  - Therefore, this linear rate of $90\text{ mm/hr}$ represents the **initial maximum aggradation rate**. As the bed profile evolves toward a new dynamic equilibrium, aggradation slows down.
  - Nonetheless, a prospective accumulation of several meters over a prolonged flood threatens catastrophic culvert choking and overtopping of industrial bunds, mandating sediment traps or emergency dredging.

---

## Sources
* **Open Channel Flow & Water Surface Profiles:** Chow, V. T., *Open-Channel Hydraulics*, McGraw-Hill; Henderson, F. M., *Open Channel Flow*, Macmillan; Subramanya, K., *Flow in Open Channels*, Tata McGraw-Hill.
* **Hydrology & Unit Hydrographs:** Chow, V. T., Maidment, D. R., & Mays, L. W., *Applied Hydrology*, McGraw-Hill; Subramanya, K., *Engineering Hydrology*, 4th Edition.
* **Sediment Transport & River Mechanics:** Garcia, M. H. (Ed.), *Sedimentation Engineering: Processes, Measurements, Modeling, and Practice*, ASCE Manuals and Reports on Engineering Practice No. 110; Exner, F. M. (1925), *Uber die Wechselwirkung zwischen Wasser und Geschiebe in Flussen*.
* **Bridge Pier Scour Standard:** Arneson, L. A., Zevenbergen, L. W., Lagasse, P. F., & Clopper, P. E. (2012), *Evaluating Scour at Bridges (HEC-18)*, 5th Edition, Publication No. FHWA-HIF-12-003, Federal Highway Administration.
* **Practice Alignment:** IndiaBIX Civil Engineering - Fluid Mechanics & Surveying Directory ([https://www.indiabix.com/civil-engineering/](https://www.indiabix.com/civil-engineering/)).

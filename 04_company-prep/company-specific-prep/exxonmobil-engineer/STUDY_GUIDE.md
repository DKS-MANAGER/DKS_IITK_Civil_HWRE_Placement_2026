# ExxonMobil Engineer Recruitment: Master Study Guide
## Track A: Civil Engineering & Hydraulics & Water Resources Engineering (HWRE) Focus

> **Core Audience:** Civil Engineering graduates specializing in Hydraulics, Water Resources, Coastal & Environmental Fluid Mechanics  
> **Target Role:** Engineer (ExxonMobil Services & Technology Pvt. Ltd., Bengaluru)  
> **Pedagogical Standard:** Claude Fable 5 — Rigorous first-principles derivation, intuitive physical interpretation, explicit boundary assumptions, unit consistency, and graded application.

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
> **Critical Engineering Insight:** A **1% reduction in pipe diameter $D$** (due to paraffin wax deposition or scale) causes an approximate **5% increase in frictional head loss** ($|-5 \times (-1\%)| = +5\%$). Pipe diameter is by far the most sensitive parameter in pipeline hydraulic systems.

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
> **Design Significance:** Failure in thin-walled pipes under internal overpressure will always initiate as a longitudinal rupture along the axial seam because hoop stress is twice the longitudinal stress.

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

# Module A3: Fluid Mechanics & Pipeline Hydraulics (Highest Priority)

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
  - $S_1$ profile ($y > y_c > y_n$): Supercritical backwater profile created by downstream obstruction.
  - $S_2$ profile ($y_c > y > y_n$): Drawdown profile.
  - $S_3$ profile ($y_c > y_n > y$): Accelerating supercritical flow.
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
In explicit time-stepping schemes for hyperbolic advection equations ($\frac{\partial u}{\partial t} + c \frac{\partial u}{\partial x} = 0$), numerical stability is bounded by the **Courant-Friedrichs-Lewy (CFL) Condition**:
$$C = \frac{u \Delta t}{\Delta x} \le C_{\max} = 1.0$$
* **Physical Meaning:** A numerical disturbance cannot propagate across more than one spatial grid cell during a single time step $\Delta t$. The numerical domain of dependence must contain the physical domain of dependence.
* If $C > 1$ in an explicit solver, information skips cells, generating unbounded numerical oscillations and solver divergence (`floating point exception`).

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

### Boundary Layer Sub-Layers & Solver Guidelines:
1. **Viscous Sublayer ($y^+ < 5$):** Molecular viscosity dominates. Reynolds stresses negligible. Linear profile $u^+ = y^+$.
   - Requires fine near-wall prism layers.
   - Used with low-Re models (e.g., $k-\omega$ SST) resolving down to the wall with target $y^+ \approx 1$.
2. **Buffer Layer ($5 < y^+ < 30$):** Both molecular and turbulent stresses compete. Highly non-linear; neither linear nor log-law applies.
   - *Best Practice:* Mesh nodes must **never** be placed in the buffer layer.
3. **Log-Law Layer ($30 < y^+ < 300$):** Turbulent mixing dominates:
   $$u^+ = \frac{1}{\kappa} \ln(y^+) + B \quad (\kappa \approx 0.41, B \approx 5.2)$$
   - Used with Standard Wall Functions ($k-\epsilon$ model) with target $30 \le y^+ \le 200$, drastically reducing computational cell count.

---

## 4. Verification vs Validation & The Grid Convergence Index (GCI)
* **Verification:** *"Are we solving the equations right?"* Quantification of numerical discretization, round-off, and iterative errors.
* **Validation:** *"Are we solving the right equations?"* Quantifying physics agreement between high-resolution numerical data and physical benchmark experiments.

### ASME V&V 20: Grid Convergence Index (GCI) via Richardson Extrapolation
To confirm that a numerical solution is independent of grid resolution, simulations must be run on at least three systematically refined grids: Fine ($h_1$), Medium ($h_2$), Coarse ($h_3$).
Grid refinement ratio: $r = h_2 / h_1 \ge 1.3$.
Apparent order of convergence $p$:
$$p = \frac{1}{\ln(r_{21})} |\ln|\epsilon_{32} / \epsilon_{21}| + q(p)|$$
$$\mathrm{GCI}_{\text{fine}}^{21} = \frac{1.25 \, e_a^{21}}{r_{21}^p - 1}$$
where $e_a^{21} = |\frac{\phi_1 - \phi_2}{\phi_1}|$ is relative error. A fine grid $\mathrm{GCI} < 3-5\%$ confirms numerical grid independence.

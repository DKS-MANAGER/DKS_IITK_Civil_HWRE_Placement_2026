# Hydraulics & Fluid Mechanics: Advanced Engineering Theory

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Multivariable Calculus, Vector Differential Equations, Fluid Dynamics

---

## 1. Governing Conservation Equations & Fluid Mechanics Foundations

### 1.1 Reynolds Transport Theorem (RTT)
The fundamental bridge between system formulations (Lagrangian) and control volume formulations (Eulerian). For an extensive property $B$ with intensive property $\beta = \frac{dB}{dm}$:

$$\frac{d B_{\text{sys}}}{dt} = \frac{\partial}{\partial t} \iiint_{\text{CV}} \rho \beta \, dV + \iint_{\text{CS}} \rho \beta (\mathbf{V} \cdot \hat{\mathbf{n}}) \, dA$$

1. **Conservation of Mass ($\beta = 1$):**
   $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0 \implies \nabla \cdot \mathbf{V} = 0 \quad (\text{Incompressible})$$
2. **Conservation of Momentum ($\beta = \mathbf{V}$):**
   $$\sum \mathbf{F} = \frac{\partial}{\partial t} \iiint_{\text{CV}} \rho \mathbf{V} \, dV + \iint_{\text{CS}} \rho \mathbf{V} (\mathbf{V} \cdot \hat{\mathbf{n}}) \, dA$$

### 1.2 The Incompressible Navier-Stokes Equations
In vector notation for a Newtonian fluid with constant dynamic viscosity $\mu$ and density $\rho$:

$$\rho \left( \frac{\partial \mathbf{V}}{\partial t} + (\mathbf{V} \cdot \nabla)\mathbf{V} \right) = -\nabla p + \mu \nabla^2 \mathbf{V} + \rho \mathbf{g}$$

In 2D Cartesian coordinates ($x, y$):
$$\rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} \right) = -\frac{\partial p}{\partial x} + \mu \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right) + \rho g_x$$
$$\rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} \right) = -\frac{\partial p}{\partial y} + \mu \left( \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} \right) + \rho g_y$$

*Physical Interpretation:*
- Left Side: Local acceleration $\frac{\partial \mathbf{V}}{\partial t}$ + Convective acceleration $(\mathbf{V} \cdot \nabla)\mathbf{V}$.
- Right Side: Pressure gradient force $-\nabla p$ + Viscous diffusion force $\mu \nabla^2 \mathbf{V}$ + Body forces $\rho \mathbf{g}$.

### 1.3 Boundary Layer Theory & Separation
For high Reynolds number flows over submerged bodies (e.g., bridge piers, submerged decks):
- **Prandtl Boundary Layer Equations:** $\frac{\partial p}{\partial y} \approx 0 \implies p(x, y) \approx p(x)$ (outer pressure imposed on wall).
- **Displacement Thickness ($\delta^*$):** $\delta^* = \int_0^\delta \left(1 - \frac{u}{U_\infty}\right) dy$.
- **Momentum Thickness ($\theta$):** $\theta = \int_0^\delta \frac{u}{U_\infty}\left(1 - \frac{u}{U_\infty}\right) dy$.
- **Separation Condition:** Under an **adverse pressure gradient** ($\frac{dp}{dx} > 0$), near-wall fluid decelerates until the wall shear stress vanishes:
  $$\tau_w = \left.\mu \frac{\partial u}{\partial y}\right|_{y=0} = 0 \implies \text{Separation Point}$$
  Downstream of separation, reverse flow and unsteady vortex shedding occur (von Kármán vortex street), generating strong horseshoe vortices that drive hydrodynamic bed scour beneath bridge decks.

---

## 2. Open-Channel Flow (OCF) Mechanics

### 2.1 Specific Energy & Critical Flow
Specific Energy ($E$) is energy measured per unit weight of fluid relative to the channel bed:

$$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g A^2}$$

For a rectangular channel of width $b$ ($q = Q/b$):
$$E = y + \frac{q^2}{2g y^2}$$

To find critical depth $y_c$ (minimum specific energy for a given discharge):
$$\frac{dE}{dy} = 1 - \frac{q^2}{g y^3} = 0 \implies y_c = \left(\frac{q^2}{g}\right)^{1/3} = \left(\frac{Q^2}{g b^2}\right)^{1/3}$$

**Critical State Properties:**
1. Froude Number $Fr = \frac{V_c}{\sqrt{g y_c}} = 1$.
2. Minimum Energy $E_{\min} = y_c + \frac{y_c}{2} = \frac{3}{2} y_c \implies y_c = \frac{2}{3} E_{\min}$.
3. Critical Velocity $V_c = \sqrt{g y_c}$.
4. General Cross-Section Condition: $\frac{Q^2 T}{g A^3} = 1$, where $T$ is top water surface width.

```
                      Specific Energy Curve (E - y)
        Depth y
           │          /
           │        /  Subcritical Flow (Fr < 1, Tranquil)
           │      /
        yc ├────● (Minimum Specific Energy E_min)
           │      \
           │        \  Supercritical Flow (Fr > 1, Rapid)
           │          \_________________
           └───────────────────────────── Specific Energy E
                         E_min
```

### 2.2 Channel Transitions & Choking
Consider a rectangular channel with upward bed step $\Delta z$ or width constriction $b \to b_2$:
- **Bed Step Upward ($\Delta z > 0$):** $E_2 = E_1 - \Delta z$.
  - In subcritical flow ($Fr_1 < 1$): Water depth **decreases** ($y_2 < y_1$).
  - In supercritical flow ($Fr_1 > 1$): Water depth **increases** ($y_2 > y_1$).
  - **Choking:** If $\Delta z > \Delta z_{\text{crit}} = E_1 - E_{\min}$, the channel cannot pass discharge $Q$ without backing up upstream (heading up). Upstream depth $y_1$ increases to accommodate the constriction.

---

## 3. The Hydraulic Jump & Energy Dissipators

A hydraulic jump is a stationary shock wave in open-channel flow where rapid supercritical flow ($Fr_1 > 1$) transitions abruptly to tranquil subcritical flow ($Fr_2 < 1$), dissipating substantial kinetic energy.

### 3.1 Derivation of the Belanger Equation
Consider a horizontal, rectangular, frictionless channel control volume between sections 1 and 2:
Applying the 1D Momentum Equation:

$$P_1 - P_2 = \rho Q (V_2 - V_1)$$
$$\frac{1}{2} \gamma y_1^2 b - \frac{1}{2} \gamma y_2^2 b = \rho q b (V_2 - V_1)$$

Substitute $V = \frac{q}{y}$ and $\gamma = \rho g$:
$$\frac{g}{2}(y_1^2 - y_2^2) = q \left(\frac{q}{y_2} - \frac{q}{y_1}\right) = q^2 \left(\frac{y_1 - y_2}{y_1 y_2}\right)$$
Divide both sides by $(y_1 - y_2)$ (since $y_1 \ne y_2$):
$$\frac{g}{2}(y_1 + y_2) = \frac{q^2}{y_1 y_2}$$
Multiply by $y_1$ and substitute $q^2 = V_1^2 y_1^2$:
$$\frac{g}{2}(y_1^2 + y_1 y_2) = \frac{V_1^2 y_1^2}{y_2} \implies y_2^2 + y_1 y_2 - \frac{2 V_1^2 y_1}{g} = 0$$
Dividing by $y_1^2$:
$$\left(\frac{y_2}{y_1}\right)^2 + \left(\frac{y_2}{y_1}\right) - 2 Fr_1^2 = 0$$

Solving the quadratic equation for the positive root:

$$\frac{y_2}{y_1} = \frac{-1 + \sqrt{1 + 8 Fr_1^2}}{2} = \frac{1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right)$$

### 3.2 Energy Dissipation in the Jump
$$\Delta E = E_1 - E_2 = \left(y_1 + \frac{V_1^2}{2g}\right) - \left(y_2 + \frac{V_2^2}{2g}\right)$$
Substituting $V_1 = q/y_1, V_2 = q/y_2$ and simplifying via the Belanger relationship:

$$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$$

*Design Rule:* Jump efficiency is $\eta = \frac{\Delta E}{E_1}$. For $Fr_1 = 4.5 \text{ to } 9.0$ (Steady Jump), $\eta$ reaches $45\% \text{ to } 70\%$, ideal for USBR Type III stilling basins with chute blocks and baffle piers.

---

## 4. Gradually Varied Flow (GVF) & Water Surface Profiles

When flow depth varies gradually along the longitudinal channel axis ($x$), pressure remains hydrostatic.

### 4.1 Derivation of GVF Differential Equation
Total head at any section: $H = z + y + \frac{V^2}{2g} = z + y + \frac{Q^2}{2g A^2}$.  
Differentiating with respect to channel coordinate $x$:

$$\frac{dH}{dx} = \frac{dz}{dx} + \frac{dy}{dx} + \frac{d}{dx}\left(\frac{Q^2}{2g A^2}\right)$$
Note that:
- Bed slope: $S_0 = -\frac{dz}{dx}$
- Energy slope: $S_f = -\frac{dH}{dx}$
- $\frac{d}{dx}\left(\frac{Q^2}{2g A^2}\right) = -\frac{Q^2}{g A^3} \frac{dA}{dx} = -\frac{Q^2 T}{g A^3} \frac{dy}{dx} = -Fr^2 \frac{dy}{dx}$

Substituting:
$$-S_f = -S_0 + \frac{dy}{dx} - Fr^2 \frac{dy}{dx} \implies \frac{dy}{dx}(1 - Fr^2) = S_0 - S_f$$

$$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2} = \frac{S_0 \left[1 - \left(\frac{K_n}{K}\right)^2\right]}{1 - \left(\frac{Z_c}{Z}\right)^2}$$

### 4.2 Complete 12-Profile Classification Scheme

| Bed Slope Condition | Relation | Zone 1 ($y > y_n, y_c$) | Zone 2 ($y_n \lessgtr y \lessgtr y_c$) | Zone 3 ($y < y_n, y_c$) |
|---|---|---|---|---|
| **Mild ($M$)** | $y_n > y_c \ (S_0 < S_c)$ | **$M_1$** (Backwater curve, $\frac{dy}{dx} > 0$) | **$M_2$** (Drawdown curve, $\frac{dy}{dx} < 0$) | **$M_3$** (Hydraulic jump downstream, $\frac{dy}{dx} > 0$) |
| **Steep ($S$)** | $y_c > y_n \ (S_0 > S_c)$ | **$S_1$** (Jump upstream, $\frac{dy}{dx} > 0$) | **$S_2$** (Drawdown, $\frac{dy}{dx} < 0$) | **$S_3$** (Supercritical acceleration, $\frac{dy}{dx} > 0$) |
| **Critical ($C$)** | $y_n = y_c \ (S_0 = S_c)$ | **$C_1$** (Backwater, $\frac{dy}{dx} > 0$) | — (Uniform critical flow) | **$C_3$** ($\frac{dy}{dx} > 0$) |
| **Horizontal ($H$)** | $S_0 = 0 \ (y_n = \infty)$ | — | **$H_2$** (Free overfall drawdown, $\frac{dy}{dx} < 0$) | **$H_3$** ($\frac{dy}{dx} > 0$) |
| **Adverse ($A$)** | $S_0 < 0$ (Bed rises) | — | **$A_2$** ($\frac{dy}{dx} < 0$) | **$A_3$** ($\frac{dy}{dx} > 0$) |

---

## 5. Pipe Flow, Network Hydraulics & Turbomachinery

### 5.1 Friction Loss & Moody Regimes
- **Darcy-Weisbach Equation:**
  $$h_f = f \frac{L}{D} \frac{V^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5}$$
- **Colebrook-White Implicit Equation (Turbulent Flow):**
  $$\frac{1}{\sqrt{f}} = -2 \log_{10} \left( \frac{\epsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)$$
- **Swamee-Jain Explicit Approximation ($\pm 1\%$ accuracy):**
  $$f = \frac{0.25}{\left[ \log_{10}\left( \frac{\epsilon}{3.7 D} + \frac{5.74}{Re^{0.9}} \right) \right]^2}$$

### 5.2 Hardy Cross Pipe Network Analysis
Governed by two physical laws:
1. **Node Law (Continuity):** $\sum Q_{\text{in}} = \sum Q_{\text{out}}$ at every junction.
2. **Loop Law (Energy Conservation):** $\sum h_f = \sum r Q |Q|^{n-1} = 0$ around every closed loop.

**Hardy Cross Discharge Correction Factor ($\Delta Q$):**
$$\Delta Q = -\frac{\sum r Q_0 |Q_0|}{\sum 2 r |Q_0|}$$
Where $r = \frac{8 f L}{\pi^2 g D^5}$ is the pipe hydraulic resistance constant. Iterate until $|\Delta Q| < \epsilon$.

### 5.3 Pump Hydraulics, Affinity Laws & Cavitation
- **System Resistance Curve:**
  $$H_{\text{sys}} = H_{\text{static}} + K Q^2, \quad \text{where } K = \sum \frac{8 f L}{\pi^2 g D^5} + \sum K_{\text{minor}}$$
- **Operating Point:** Intersection of pump performance characteristic $H_{\text{pump}} = A - B Q^2$ with $H_{\text{sys}}$.
- **Pump Affinity Laws (Impeller Diameter $D$, Speed $N$):**
  $$\frac{Q_1}{Q_2} = \left(\frac{N_1}{N_2}\right)\left(\frac{D_1}{D_2}\right)^3, \quad \frac{H_1}{H_2} = \left(\frac{N_1}{N_2}\right)^2\left(\frac{D_1}{D_2}\right)^2, \quad \frac{P_1}{P_2} = \left(\frac{N_1}{N_2}\right)^3\left(\frac{D_1}{D_2}\right)^5$$
- **Net Positive Suction Head & Cavitation:**
  Cavitation occurs when local static pressure drops to liquid vapor pressure ($P \le P_{\text{sat}}$), forming vapor bubbles that collapse violently ($> 1,000\text{ MPa}$ micro-jets) against impellers.
  - To prevent cavitation:
    $$NPSH_A = \frac{P_{\text{atm}} - P_v}{\gamma} - Z_s - h_{fs} \ge NPSH_R + 0.5\text{ m safety margin}$$

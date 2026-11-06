# Module 03: Open-Channel Hydraulics — Theory, Derivations & Design

> **Document Focus**: Steady Open-Channel Flow, Specific Energy, Critical Flow, GVF Differential Equations, Step Methods, Hydraulic Jumps, and Stage-Discharge Rating Curves  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — CHOW, HENDERSON, SUBRAMANYA, USBR]`  

---

## 1. Classification & Fundamental Principles of Open-Channel Flow

Open-channel flow is defined as liquid flow with a free surface subjected to atmospheric pressure. Unlike closed-conduit flow driven by piezometric pressure gradients, open-channel flow is driven by the component of gravity parallel to the channel bed slope.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    OPEN-CHANNEL FLOW TAXONOMY                               │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ CRITERION           │ CLASSIFICATION & CHARACTERISTICS                      │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Time Variation      │ • Steady Flow: $\partial y/\partial t = 0$,           │
│                     │   $\partial v/\partial t = 0$                         │
│                     │ • Unsteady Flow: $\partial y/\partial t \ne 0$,       │
│                     │   $\partial v/\partial t \ne 0$                       │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Spatial Variation   │ • Uniform Flow: $\partial y/\partial x = 0$,          │
│                     │   $S_0 = S_w = S_f$                                   │
│                     │ • Varied Flow (Non-uniform): $\partial y/\partial x\ne0$│
│                     │   - Gradually Varied Flow (GVF): Curvature negligible │
│                     │   - Rapidly Varied Flow (RVF): Curvature significant  │
│                     │   - Spatially Varied Flow (SVF): Side inflow/outflow  │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Gravity / Inertia   │ • Subcritical ($Fr < 1$): Gravitational forces dominate│
│ (Froude Number)     │ • Critical ($Fr = 1$): Minimum specific energy        │
│                     │ • Supercritical ($Fr > 1$): Inertial forces dominate  │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ Viscous Regime      │ • Laminar: $Re < 500$ (using $R_h$)                   │
│ (Reynolds Number)   │ • Transitional: $500 \le Re \le 2000$                 │
│                     │ • Turbulent: $Re > 2000$ (Almost all practical flows) │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

### 1.1 Dimensionless Numbers in Free-Surface Hydraulics
1. **Froude Number ($Fr$)**:
   The ratio of inertial forces to gravitational forces, and physically represents the ratio of mean flow velocity $v$ to the celerity $c$ of an infinitesimal gravity wave in shallow water:
   $$Fr = \frac{v}{\sqrt{g D_h}}$$
   where $D_h = \frac{A}{T}$ is the **hydraulic depth**, $A$ is flow area, $T$ is top water-surface width, and $g = 9.81\text{ m/s}^2$.
   * If $Fr < 1$: Flow is **subcritical** (tranquil). Small surface disturbances travel both upstream and downstream ($c > v$). Flow controls are located **downstream**.
   * If $Fr = 1$: Flow is **critical**. Small surface disturbances remain stationary ($c = v$).
   * If $Fr > 1$: Flow is **supercritical** (rapid/shooting). Small disturbances cannot propagate upstream ($v > c$); disturbances are swept downstream. Flow controls are located **upstream**.

2. **Reynolds Number ($Re$)**:
   Defined for open channels using the hydraulic radius $R = A / P$ (where $P$ is wetted perimeter):
   $$Re = \frac{v R}{\nu} \quad \text{or} \quad Re = \frac{4 v R}{\nu}$$
   In standard river and canal engineering, $Re > 2,000$ (or $> 500$ using $R$), indicating fully developed turbulent flow where viscous forces are negligible compared to boundary shear resistance.

---

## 2. Specific Energy, Critical Flow & Momentum Function

### 2.1 Derivation of Specific Energy
The total energy head $H$ at a cross-section with bed elevation $z$ above a datum is:
$$H = z + y \cos\theta + \alpha \frac{v^2}{2g}$$
For small channel slopes ($\theta \le 6^\circ \implies \cos\theta \approx 1$), taking the channel bed as the local datum ($z = 0$), the **Specific Energy ($E$)** is defined as:
$$E = y + \alpha \frac{v^2}{2g} = y + \frac{Q^2}{2 g A^2}$$
where $\alpha$ is the Coriolis velocity distribution coefficient (assumed $\alpha = 1.0$ unless significant velocity non-uniformity exists).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SPECIFIC ENERGY CURVE                             │
│       y (Depth)                                                             │
│           ▲                                                                 │
│           │            / (y = E Asymptote)                                  │
│           │           /        Subcritical Branch ($Fr < 1$)                │
│       y_1 ┼──────────/─────────────●                                        │
│           │         /             /                                         │
│       y_c ┼────────/─────────────● (Critical Depth: Minimum Energy E_min)   │
│           │       /               \                                         │
│       y_2 ┼──────/─────────────────● Supercritical Branch ($Fr > 1$)        │
│           │     /                                                           │
│           └────┴─────────────────────► E (Specific Energy)                  │
│                0                 E_min                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Proof of Critical Flow Condition
To find the depth of minimum specific energy for a constant discharge $Q$:
$$\frac{dE}{dy} = \frac{d}{dy}\left(y + \frac{Q^2}{2 g A^2}\right) = 1 - \frac{Q^2}{g A^3}\frac{dA}{dy} = 0$$
Since $dA = T dy$ (where $T$ is top water-surface width):
$$\frac{dE}{dy} = 1 - \frac{Q^2 T}{g A^3} = 0 \implies \frac{Q^2 T_c}{g A_c^3} = 1$$
Substituting $D_h = A/T$ and $v = Q/A$:
$$\frac{v_c^2}{g (A_c / T_c)} = \frac{v_c^2}{g D_{hc}} = 1 \implies Fr = 1 \quad \blacksquare$$

### 2.3 Special Case: Rectangular Channel
For a rectangular channel of width $b$, discharge per unit width is $q = Q/b$, area $A = b y$, top width $T = b$, and hydraulic depth $D_h = y$:
$$\frac{q^2}{g y_c^3} = 1 \implies y_c = \left(\frac{q^2}{g}\right)^{1/3}$$
The minimum specific energy $E_{min}$ is:
$$E_{min} = y_c + \frac{v_c^2}{2g} = y_c + \frac{g y_c}{2g} = y_c + \frac{y_c}{2} = \frac{3}{2}y_c \implies y_c = \frac{2}{3}E_{min}$$

### 2.4 Specific Force (Momentum Function)
To analyze rapidly varied flow transitions (such as hydraulic jumps) where internal energy dissipation is unknown, Newton's second law is applied across a control volume:
$$P_1 - P_2 - F_f + W \sin\theta = \rho Q (v_2 - v_1)$$
Neglecting boundary friction ($F_f \approx 0$) and channel slope component ($W \sin\theta \approx 0$) over short jump lengths:
$$\rho g A_1 \bar{z}_1 - \rho g A_2 \bar{z}_2 = \rho Q \left(\frac{Q}{A_2} - \frac{Q}{A_1}\right)$$
Dividing by $\rho g$ and rearranging yields the conservation of **Specific Force ($M$)**:
$$M = \frac{Q^2}{g A} + \bar{z} A = \text{Constant}$$
where $\bar{z}$ is the centroidal depth of flow area $A$ below the free surface.
* For a rectangular channel: $\bar{z} = y/2 \implies M = \frac{q^2 b}{g y} + \frac{b y^2}{2}$.
* For a given specific force $M$, there exist two depths called **conjugate depths (or sequent depths)** $y_1$ and $y_2$.

---

## 3. Uniform Flow & Normal Depth Determination

### 3.1 Manning & Chezy Equations
In uniform flow, gravity driving force exactly balances boundary resistance.
1. **Manning's Formula (SI Units)**:
   $$v = \frac{1}{n} R^{2/3} S_0^{1/2}, \quad Q = \frac{1}{n} A R^{2/3} S_0^{1/2}$$
   where $n$ is Manning's roughness coefficient ($\text{s/m}^{1/3}$), $R = A/P$ is hydraulic radius (m), and $S_0$ is bed slope.
2. **Chezy's Formula**:
   $$v = C \sqrt{R S_0}$$
   Equating Manning and Chezy equations yields the conversion:
   $$C = \frac{1}{n} R^{1/6}$$

### 3.2 Most Economical (Hydraulically Efficient) Cross-Sections
A cross-section is hydraulically most efficient when it delivers maximum discharge $Q$ for a given cross-sectional area $A$, requiring minimum wetted perimeter $P$ ($R = A/P$ is maximized):
1. **Rectangular Channel**:
   $$P = b + 2y = \frac{A}{y} + 2y \implies \frac{dP}{dy} = -\frac{A}{y^2} + 2 = 0 \implies b = 2y, \quad R = \frac{y}{2}$$
2. **Trapezoidal Channel** (side slope $z:1$ horizontal to vertical):
   * Best side slope: $\theta = 60^\circ \implies z = \frac{1}{\sqrt{3}} \approx 0.577$.
   * Hydraulic radius: $R = \frac{y}{2}$.
   * Half of top width equals side slope length: $T/2 = y\sqrt{1 + z^2}$.

---

## 4. Gradually Varied Flow (GVF) & Water Surface Profiles

### 4.1 Derivation of the GVF Differential Equation
Consider a small reach of length $dx$. Total energy head is:
$$H = z + y + \frac{v^2}{2g}$$
Differentiating with respect to longitudinal distance $x$:
$$\frac{dH}{dx} = \frac{dz}{dx} + \frac{dy}{dx} + \frac{d}{dx}\left(\frac{v^2}{2g}\right)$$
By definition:
* Bed slope: $S_0 = -\frac{dz}{dx}$
* Energy slope: $S_f = -\frac{dH}{dx}$
* Kinetic energy head gradient:
  $$\frac{d}{dx}\left(\frac{Q^2}{2g A^2}\right) = -\frac{Q^2}{g A^3}\frac{dA}{dx} = -\frac{Q^2}{g A^3}\left(T \frac{dy}{dx}\right) = -Fr^2 \frac{dy}{dx}$$
Substituting these relations:
$$-S_f = -S_0 + \frac{dy}{dx} - Fr^2 \frac{dy}{dx}$$
$$S_0 - S_f = \frac{dy}{dx}(1 - Fr^2)$$
$$\boxed{\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2} = \frac{S_0 - S_f}{1 - \frac{Q^2 T}{g A^3}}}$$

### 4.2 Slope Classifications & The 12 GVF Profiles
The slope of a channel is classified by comparing normal depth $y_0$ to critical depth $y_c$:
1. **Mild Slope ($M$)**: $y_0 > y_c \iff S_0 < S_c$.
   * **M1 Profile ($y > y_0 > y_c$)**: $dy/dx > 0$. Backwater curve created by downstream dam, weir, or high reservoir. Subcritical, controlled from downstream.
   * **M2 Profile ($y_0 > y > y_c$)**: $dy/dx < 0$. Drawdown curve approaching free overfall or channel constriction. Subcritical, controlled downstream.
   * **M3 Profile ($y_0 > y_c > y$)**: $dy/dx > 0$. Hydraulic jump precursor downstream of sluice gate on mild slope. Supercritical, controlled upstream.
2. **Steep Slope ($S$)**: $y_c > y_0 \iff S_0 > S_c$.
   * **S1 Profile ($y > y_c > y_0$)**: $dy/dx > 0$. Backwater curve behind dam on steep terrain. Subcritical, downstream control.
   * **S2 Profile ($y_c > y > y_0$)**: $dy/dx < 0$. Drawdown curve from steep crest or mild-to-steep slope transition. Supercritical, upstream control.
   * **S3 Profile ($y_c > y_0 > y$)**: $dy/dx > 0$. Supercritical accelerating flow entering normal depth. Upstream control.
3. **Critical Slope ($C$)**: $y_0 = y_c \iff S_0 = S_c$.
   * **C1 Profile ($y > y_c$)**: Backwater profile.
   * **C3 Profile ($y < y_c$)**: Supercritical accelerating profile.
4. **Horizontal Bed ($H$)**: $S_0 = 0 \implies y_0 = \infty$.
   * **H2 Profile ($y > y_c$)**: Drawdown curve.
   * **H3 Profile ($y < y_c$)**: Supercritical profile.
5. **Adverse Bed ($A$)**: $S_0 < 0 \implies y_0$ undefined.
   * **A2 Profile ($y > y_c$)**: Drawdown curve.
   * **A3 Profile ($y < y_c$)**: Supercritical profile.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SUMMARY OF KEY GVF PROFILES                           │
├─────────┬───────────────────────┬────────────┬─────────────┬────────────────┤
│ PROFILE │ CONDITION             │ $dy/dx$    │ TYPE        │ REAL-WORLD CASE│
├─────────┼───────────────────────┼────────────┼─────────────┼────────────────┤
│ **M1**  │ $y > y_0 > y_c$       │ Positive   │ Backwater   │ Dam backwater  │
│ **M2**  │ $y_0 > y > y_c$       │ Negative   │ Drawdown    │ Free overfall  │
│ **M3**  │ $y_0 > y_c > y$       │ Positive   │ Supercrit.  │ Sluice outflow │
│ **S1**  │ $y > y_c > y_0$       │ Positive   │ Backwater   │ Dam on steep   │
│ **S2**  │ $y_c > y > y_0$       │ Negative   │ Drawdown    │ Mild-to-steep  │
│ **S3**  │ $y_c > y_0 > y$       │ Positive   │ Supercrit.  │ Sluice on steep│
└─────────┴───────────────────────┴────────────┴─────────────┴────────────────┘
```

---

## 5. Numerical Methods for Water Surface Profiling

### 5.1 The Direct-Step Method (Prismatic Channels)
In prismatic channels, the distance $\Delta x$ between two specified flow depths $y_1$ and $y_2$ is solved directly from the energy equation:
$$\Delta x = \frac{E_2 - E_1}{S_0 - \bar{S}_f}$$
where:
* Specific energies: $E_1 = y_1 + \frac{v_1^2}{2g}$ and $E_2 = y_2 + \frac{v_2^2}{2g}$
* Friction slopes: $S_{f1} = \frac{n^2 v_1^2}{R_1^{4/3}}$ and $S_{f2} = \frac{n^2 v_2^2}{R_2^{4/3}}$
* Average friction slope: $\bar{S}_f = \frac{S_{f1} + S_{f2}}{2}$

### 5.2 The Standard-Step Method (Natural Non-Prismatic Channels / HEC-RAS Algorithm)
In natural rivers, cross-section geometry varies with station $x$, so depths cannot be specified in advance. The channel distance $\Delta x$ is fixed between cross-sections 1 and 2, and depth $y_2$ is determined iteratively.
The total energy balance equation is:
$$z_1 + y_1 + \alpha_1 \frac{v_1^2}{2g} = z_2 + y_2 + \alpha_2 \frac{v_2^2}{2g} + h_e$$
where head loss $h_e$ comprises friction loss $h_f$ and contraction/expansion eddy loss $h_o$:
$$h_e = \bar{S}_f \Delta x + C \left| \alpha_1 \frac{v_1^2}{2g} - \alpha_2 \frac{v_2^2}{2g} \right|$$
* **Average friction slope $\bar{S}_f$ options**:
  1. Average Conveyance: $\bar{S}_f = \left(\frac{Q_1 + Q_2}{K_1 + K_2}\right)^2$ (USACE HEC-RAS default)
  2. Average Friction Slope: $\bar{S}_f = \frac{S_{f1} + S_{f2}}{2}$
  3. Geometric Mean: $\bar{S}_f = \sqrt{S_{f1} S_{f2}}$
  4. Harmonic Mean: $\bar{S}_f = \frac{2 S_{f1} S_{f2}}{S_{f1} + S_{f2}}$
* **Contraction / Expansion coefficients $C$**:
  * Gradual transitions: $C_{\text{cont}} = 0.1$, $C_{\text{exp}} = 0.3$
  * Bridge sections: $C_{\text{cont}} = 0.3$, $C_{\text{exp}} = 0.5$
  * Abrupt transitions: $C_{\text{cont}} = 0.6$, $C_{\text{exp}} = 0.8$

---

## 6. Hydraulic Jump Derivations & Equations

A hydraulic jump is a rapidly varied flow phenomenon occurring when a supercritical stream ($Fr_1 > 1$) transitions abruptly to a subcritical stream ($Fr_2 < 1$), accompanied by severe turbulence, air entrainment, and mechanical energy dissipation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           THE HYDRAULIC JUMP                                │
│                                                                             │
│               Supercritical (y_1)           Subcritical (y_2)               │
│               v_1, Fr_1 > 1                  v_2, Fr_2 < 1                  │
│               ─────────────────┐            ─────────────────────────────   │
│                                │           /        ▲                       │
│                                │  Roller  /         │                       │
│                                │  Zone   /          │ y_2 (Conjugate)       │
│               ▲                \        /           │                       │
│          y_1  │                 \______/            ▼                       │
│               ▼ ─────────────────────────────────────────────────────────   │
│               ◄───────────────── L_j ───────────────────────────────────►   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Derivation of the Bélanger Equation (Rectangular Channel)
Applying specific force conservation across cross-sections 1 and 2:
$$\frac{q^2}{g y_1} + \frac{y_1^2}{2} = \frac{q^2}{g y_2} + \frac{y_2^2}{2}$$
Rearranging terms:
$$\frac{q^2}{g}\left(\frac{1}{y_1} - \frac{1}{y_2}\right) = \frac{y_2^2 - y_1^2}{2}$$
$$\frac{q^2}{g}\left(\frac{y_2 - y_1}{y_1 y_2}\right) = \frac{(y_2 - y_1)(y_2 + y_1)}{2}$$
Since $y_2 \ne y_1$ (a jump occurs):
$$\frac{q^2}{g} = \frac{y_1 y_2 (y_1 + y_2)}{2}$$
Dividing both sides by $y_1^3$ and substituting $q^2 / (g y_1^3) = Fr_1^2$:
$$Fr_1^2 = \frac{1}{2}\frac{y_2}{y_1}\left(1 + \frac{y_2}{y_1}\right)$$
Let $\eta = y_2 / y_1$:
$$\eta^2 + \eta - 2 Fr_1^2 = 0$$
Applying the quadratic formula and discarding the negative root ($\eta > 0$):
$$\eta = \frac{-1 + \sqrt{1^2 - 4(1)(-2 Fr_1^2)}}{2} = \frac{\sqrt{1 + 8 Fr_1^2} - 1}{2}$$
$$\boxed{\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right)} \quad \blacksquare$$

### 6.2 Energy Loss Equation ($\Delta E$)
The specific energy loss across the jump is:
$$\Delta E = E_1 - E_2 = \left(y_1 + \frac{v_1^2}{2g}\right) - \left(y_2 + \frac{v_2^2}{2g}\right) = (y_1 - y_2) + \frac{q^2}{2g}\left(\frac{1}{y_1^2} - \frac{1}{y_2^2}\right)$$
Substituting $\frac{q^2}{g} = \frac{y_1 y_2 (y_1 + y_2)}{2}$:
$$\Delta E = (y_1 - y_2) + \frac{y_1 y_2 (y_1 + y_2)}{4}\left(\frac{y_2^2 - y_1^2}{y_1^2 y_2^2}\right) = (y_1 - y_2) + \frac{(y_1 + y_2)^2 (y_2 - y_1)}{4 y_1 y_2}$$
$$\Delta E = (y_2 - y_1)\left[ \frac{(y_1 + y_2)^2 - 4 y_1 y_2}{4 y_1 y_2} \right] = \frac{(y_2 - y_1)(y_2 - y_1)^2}{4 y_1 y_2}$$
$$\boxed{\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}} \quad \blacksquare$$

### 6.3 Jump Length ($L_j$) & USBR Classifications
* **Length of Jump ($L_j$)**: Defined as the distance from the jump toe to the section where the surface roller ends and level downstream water is established.
  * For $Fr_1 = 4.5 \text{ to } 9.0$: $L_j \approx 6.0 y_2$ (USBR benchmark).
  * General empirical relation: $L_j \approx 5.0 \text{ to } 6.9 (y_2 - y_1)$.
* **Jump Classification based on Inflow Froude Number ($Fr_1$)**:
  1. $Fr_1 = 1.0 \text{ to } 1.7$: **Undular Jump** (surface ripples, negligible dissipation $< 5\%$).
  2. $Fr_1 = 1.7 \text{ to } 2.5$: **Weak Jump** (smooth surface roller, dissipation $< 18\%$).
  3. $Fr_1 = 2.5 \text{ to } 4.5$: **Oscillating Jump** (jet oscillates from floor to surface; creates damaging downstream waves).
  4. $Fr_1 = 4.5 \text{ to } 9.0$: **Steady Jump** (well-balanced, stable, maximum performance; energy dissipation $45\% \text{ to } 70\%$). Ideal for spillway stilling basins.
  5. $Fr_1 > 9.0$: **Strong / Choppy Jump** (rough, spray-generating; dissipation up to $85\%$).

---

## 7. Stage-Discharge Rating Curves & River Hysteresis

### 7.1 Mathematical Formulation of Steady Rating Curves
In a river gauging station, the relationship between measured stage (water level $h$) and discharge $Q$ under steady, uniform conditions follows a power-law relationship:
$$Q = C (h - h_0)^\beta$$
where:
* $h$: Measured river stage (gauge height, m).
* $h_0$: Stage of zero flow (elevation of the controlling channel thalweg, m).
* $C$: Discharge coefficient reflecting channel geometry and roughness.
* $\beta$: Exponent governed by control section geometry (typically $\beta \approx 1.5$ to $1.7$ for rectangular/parabolic sections; $\beta \approx 2.5$ for triangular/V-notch controls).

### 7.2 Hysteresis & Loop Rating Curves in Unsteady Flood Waves
During an unsteady flood wave passing through a river reach, the stage-discharge relationship is **not unique**. It forms a hysteresis loop:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LOOP RATING CURVE HYSTERESIS                       │
│       Stage h                                                               │
│          ▲                     Rising Stage (Higher Q for same h)           │
│          │                 ┌──────────────────────►                         │
│          │                /                        \                        │
│          │               /                          \                       │
│          │              /                            \                      │
│          │             ▲                              ▼                     │
│          │              \                            /                      │
│          │               \                          /                       │
│          │                ◄────────────────────────┘                        │
│          │                     Falling Stage (Lower Q for same h)           │
│          └────────────────────────────────────────────────► Q (Discharge)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Physical Explanation of Loop Formation
Applying the Saint-Venant momentum equation:
$$S_f = S_0 - \frac{\partial y}{\partial x} - \frac{v}{g}\frac{\partial v}{\partial x} - \frac{1}{g}\frac{\partial v}{\partial t}$$
1. **Rising Limb**:
   * As the flood peak approaches, the water surface steepens: $\frac{\partial y}{\partial x} < 0$.
   * Therefore, the energy slope is increased: $S_f \approx S_0 - \frac{\partial y}{\partial x} > S_0$.
   * With a steeper hydraulic gradient, flow velocity and discharge $Q$ are **higher** than steady flow for the same recorded stage.
2. **Falling Limb**:
   * After the flood crest passes, the water surface flattens: $\frac{\partial y}{\partial x} > 0$.
   * Therefore, $S_f < S_0$.
   * The flatter gradient results in **lower** discharge for the exact same recorded stage.
3. **The Jones Correction Formula**:
   Relating unsteady discharge $Q$ to steady discharge $Q_0$:
   $$\frac{Q}{Q_0} = \sqrt{1 + \frac{1}{c S_0}\frac{\partial h}{\partial t}}$$
   where $c = \frac{dQ}{dA}$ is flood wave celerity, and $\frac{\partial h}{\partial t}$ is rate of change of stage. During the rising limb ($\partial h / \partial t > 0 \implies Q > Q_0$).

---

## 8. Solved Numerical Engineering Problems

### Problem 1: Critical & Normal Depth in a Trapezoidal Canal
**Statement**: A trapezoidal canal carries a discharge of $Q = 30\text{ m}^3\text{/s}$. The bed width is $b = 6.0\text{ m}$, side slope is $1.5\text{ H}:1\text{ V}$ ($z = 1.5$), bed slope is $S_0 = 0.0005$, and Manning's roughness is $n = 0.018$.
1. Compute the critical depth $y_c$ and critical velocity $v_c$.
2. Compute the normal depth $y_0$ and classify the channel slope.

**Solution**:
1. **Critical Depth ($y_c$)**:
   The critical flow condition requires:
   $$\frac{Q^2 T_c}{g A_c^3} = 1 \implies \frac{A_c^3}{T_c} = \frac{Q^2}{g} = \frac{30^2}{9.81} = 91.743\text{ m}^5$$
   For a trapezoidal section:
   $$A_c = (b + z y_c)y_c = (6 + 1.5 y_c)y_c, \quad T_c = b + 2 z y_c = 6 + 3 y_c$$
   $$\frac{[(6 + 1.5 y_c)y_c]^3}{6 + 3 y_c} = 91.743$$
   Solve iteratively via Newton-Raphson:
   * Trial 1: $y_c = 1.0\text{ m} \implies A = 7.5\text{ m}^2, T = 9\text{ m} \implies \frac{7.5^3}{9} = 46.88$ (Too small)
   * Trial 2: $y_c = 1.3\text{ m} \implies A = (6 + 1.95)(1.3) = 10.335\text{ m}^2, T = 9.9\text{ m} \implies \frac{10.335^3}{9.9} = 111.5$ (Too large)
   * Trial 3: $y_c = 1.226\text{ m} \implies A_c = (6 + 1.5 \times 1.226)(1.226) = 9.610\text{ m}^2, T_c = 6 + 3(1.226) = 9.678\text{ m}$
     $$\frac{9.610^3}{9.678} = \frac{887.52}{9.678} = 91.70\approx 91.743$$
   $$\mathbf{y_c = 1.226\text{ m}}, \quad v_c = \frac{Q}{A_c} = \frac{30}{9.610} = \mathbf{3.122\text{ m/s}}$$

2. **Normal Depth ($y_0$)**:
   Apply Manning's equation:
   $$Q = \frac{1}{n}\frac{A_0^{5/3}}{P_0^{2/3}}S_0^{1/2} \implies \frac{A_0^{5/3}}{P_0^{2/3}} = \frac{Q n}{\sqrt{S_0}} = \frac{30 \times 0.018}{\sqrt{0.0005}} = \frac{0.54}{0.02236} = 24.150$$
   With $P_0 = b + 2 y_0 \sqrt{1 + z^2} = 6 + 2 y_0 \sqrt{1 + 1.5^2} = 6 + 3.6056 y_0$:
   * Trial 1: $y_0 = 1.8\text{ m} \implies A = 15.66, P = 12.49 \implies \frac{15.66^{5/3}}{12.49^{2/3}} = \frac{96.88}{5.39} = 17.97$
   * Trial 2: $y_0 = 2.1\text{ m} \implies A = (6 + 3.15)(2.1) = 19.215, P = 13.572 \implies \frac{19.215^{5/3}}{13.572^{2/3}} = \frac{136.65}{5.69} = 24.02$
   * Trial 3: $y_0 = 2.108\text{ m} \implies A_0 = 19.314\text{ m}^2, P_0 = 13.601\text{ m} \implies \frac{19.314^{5/3}}{13.601^{2/3}} = 24.150$
   $$\mathbf{y_0 = 2.108\text{ m}}$$
3. **Slope Classification**:
   $$y_0 (2.108\text{ m}) > y_c (1.226\text{ m}) \implies \mathbf{Mild\ Slope\ (M)}$$
   Actual normal velocity $v_0 = \frac{30}{19.314} = 1.553\text{ m/s}$. Froude number $Fr_0 = \frac{1.553}{\sqrt{9.81 \times (19.314 / 12.324)}} = 0.396 < 1$ (Subcritical).

---

### Problem 2: Sluice Gate Hydraulic Jump & Power Dissipation
**Statement**: A rectangular spillway chute delivers $q = 12\text{ m}^3\text{/s per meter width}$ at a vena contracta depth of $y_1 = 0.80\text{ m}$ into a horizontal stilling basin of width $B = 20\text{ m}$.
1. Find the initial Froude number $Fr_1$.
2. Calculate the conjugate depth $y_2$.
3. Compute the head loss $\Delta E$ and total mechanical power dissipated in megawatts (MW).
4. Sizing check: Determine required stilling basin length.

**Solution**:
1. **Initial Froude Number ($Fr_1$)**:
   $$v_1 = \frac{q}{y_1} = \frac{12}{0.80} = 15.0\text{ m/s}$$
   $$Fr_1 = \frac{v_1}{\sqrt{g y_1}} = \frac{15.0}{\sqrt{9.81 \times 0.80}} = \frac{15.0}{\sqrt{7.848}} = \frac{15.0}{2.8014} = \mathbf{5.354}$$
   Since $Fr_1 = 5.354 > 1$, a stable, well-formed **Steady Jump** will form.

2. **Conjugate Depth ($y_2$)**:
   Applying the Bélanger equation:
   $$y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right) = \frac{0.80}{2}\left(\sqrt{1 + 8(5.354)^2} - 1\right)$$
   $$8(5.354)^2 = 8 \times 28.665 = 229.32 \implies \sqrt{230.32} = 15.176$$
   $$y_2 = 0.40 \times (15.176 - 1) = 0.40 \times 14.176 = \mathbf{5.670\text{ m}}$$

3. **Head Loss ($\Delta E$)**:
   $$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(5.670 - 0.80)^3}{4 \times 0.80 \times 5.670} = \frac{(4.870)^3}{18.144} = \frac{115.50}{18.144} = \mathbf{6.366\text{ m}}$$

4. **Total Power Dissipated ($P$)**:
   Total discharge: $Q = q \times B = 12 \times 20 = 240\text{ m}^3\text{/s}$.
   $$P = \rho g Q \Delta E = 1000\text{ kg/m}^3 \times 9.81\text{ m/s}^2 \times 240\text{ m}^3\text{/s} \times 6.366\text{ m}$$
   $$P = 14,988,460\text{ Watts} = \mathbf{14.99\text{ MW}}$$

5. **Stilling Basin Length ($L_b$)**:
   For $Fr_1 = 5.35$, USBR recommends:
   $$L_b \approx 6.0 \times y_2 = 6.0 \times 5.670 = \mathbf{34.02\text{ m}}$$


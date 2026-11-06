# Module 06: Water Hammer & Mass Oscillation in Hydraulic Systems

> **Document Focus**: Hydraulic Transients, Joukowsky Wave Equations, Acoustic Wave Speed, Surge Tank Mechanics, and Thoma Stability  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — WYLIE & STREETER, CHAUDHRY, JOUKOWSKY, JAEGER]`  

---

## 1. Fundamentals of Hydraulic Transients

Hydraulic transients represent unsteady closed-conduit flows where fluid compressibility and conduit elasticity cannot be ignored. Transients in water infrastructure and hydropower schemes are governed by two distinct phenomena occurring across radically different timescales:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WATER HAMMER vs. MASS OSCILLATION                        │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ CHARACTERISTIC      │ WATER HAMMER (FAST PHENOM)│ MASS OSCILLATION (SLOW)   │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ Physical Theory     │ Elastic-Column Theory     │ Rigid-Column Theory       │
│ Governing Physics   │ Compressibility of water  │ Inertia of bulk water     │
│                     │ & elasticity of pipe wall │ column vs gravity surge   │
│ Wave Speed          │ Sonic / Acoustic:         │ Gravitational:            │
│                     │ $a \approx 900–1200$ m/s  │ $v \approx 2–4$ m/s       │
│ Typical Period      │ Fractions of a second     │ Tens to hundreds of       │
│                     │ ($T = 2L/a \approx 0.1–3$ s)│ seconds ($T \approx 50–300$ s)│
│ Primary Conduit     │ High-pressure penstock    │ Low-pressure headrace     │
│                     │ & pump discharge mains    │ tunnel & surge tank       │
│ Design Hazard       │ Rupture by overpressure;  │ Overtoping of surge tank; │
│                     │ buckling by sub-atm vacuum│ governor instability      │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

## 2. Water Hammer Physics & The Joukowsky Equation

### 2.1 Derivation of the Joukowsky Equation
Consider a pipeline of cross-sectional area $A$ conveying fluid at initial velocity $v_0$ and pressure $p_0$. A downstream valve closes instantaneously, decelerating the water column by $\Delta v = v_0 - 0 = v_0$. An acoustic pressure compression wave forms and propagates upstream at wave speed $a$.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       JOUKOWSKY ACOUSTIC WAVE PROPAGATION                   │
│                                                                             │
│                    ◄──────── Upstream Propagation at Speed a                │
│                                                                             │
│       Undisturbed Fluid                     Compressed Fluid                │
│       v_0, p_0                              v = 0, p_0 + Δp                 │
│       ─────────────────────┬─────────────────────────────────| Closed       │
│                            │ Acoustic Shock Front            | Valve        │
│       ─────────────────────┴─────────────────────────────────|              │
│       ◄──────────── (L - a Δt) ─────────────►◄──── a Δt ────►               │
└─────────────────────────────────────────────────────────────────────────────┘
```

In time $\Delta t$, the wave advances upstream by distance $\Delta x = a \Delta t$.
The mass of fluid brought to rest during time $\Delta t$ is:
$$\Delta m = \rho A (a \Delta t)$$
Applying the impulse-momentum equation ($\sum F \Delta t = \Delta(m v)$):
$$\Delta P \cdot A \cdot \Delta t = \Delta m \cdot \Delta v = [\rho A (a \Delta t)] \Delta v$$
Dividing both sides by $A \Delta t$:
$$\boxed{\Delta P = \rho a \Delta v}$$
Expressing pressure rise as equivalent head of water ($\Delta H = \frac{\Delta P}{\rho g}$):
$$\boxed{\Delta H = \frac{a \Delta v}{g}} \quad \blacksquare$$

### 2.2 Derivation of Acoustic Wave Speed ($a$)
The acoustic wave speed in an elastic pipe depends on the bulk modulus of elasticity of water ($K$) and Young's modulus of the conduit wall material ($E$):
$$a = \sqrt{\frac{K / \rho}{1 + \left(\frac{K}{E}\right)\left(\frac{D}{e}\right) c_1}}$$
where:
* $K$: Bulk modulus of water ($\approx 2.19 \times 10^9\text{ N/m}^2$ at $20^\circ\text{C}$).
* $\rho$: Density of water ($1000\text{ kg/m}^3$).
* $E$: Young's modulus of conduit material (Steel: $E = 2.06 \times 10^{11}\text{ N/m}^2$; Concrete: $E = 2.0 \times 10^{10}\text{ N/m}^2$).
* $D$: Internal pipe diameter (m).
* $e$: Pipe wall thickness (m).
* $c_1$: Conduit constraint factor:
  * Case 1 (Anchored at upstream end, expansion joints downstream): $c_1 = 1 - \frac{\mu}{2} \approx 0.85$ (where Poisson ratio of steel $\mu \approx 0.30$).
  * Case 2 (Anchored against longitudinal movement throughout): $c_1 = 1 - \mu^2 \approx 0.91$.
  * Case 3 (Expansion joints throughout): $c_1 = 1.0$.
* For an unlined rock tunnel, the rock mass modulus of elasticity $E_r$ replaces the wall elasticity:
  $$a = \sqrt{\frac{K / \rho}{1 + \frac{K}{G_R}}}$$
  where $G_R$ is the shear modulus of the surrounding rock formation.

---

## 3. Rapid versus Slow Valve Closure Dynamics

The behavior of water hammer pressure waves is determined by the ratio of valve closure time $t_c$ to the **pipe acoustic period ($T_c$)**:
$$T_c = \frac{2 L}{a}$$
where $T_c$ is the time required for the pressure wave to travel from the valve to the upstream reservoir and reflect back.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VALVE CLOSURE REGIMES & PRESSURE ENVELOPES               │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ CLOSURE REGIME      │ TIME CONDITION            │ MAXIMUM PRESSURE HEAD     │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Rapid Closure**   │ $t_c \le T_c = \frac{2L}{a}$│ Full Joukowsky Head:      │
│ (Instantaneous)     │                           │ $\Delta H_{max} = \frac{a v_0}{g}$│
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Slow Closure**    │ $t_c > T_c = \frac{2L}{a}$ │ Reduced Pressure Head:    │
│ (Gradual)           │                           │ $\Delta H \approx \frac{2 L v_0}{g t_c}$ (Michaud) │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

### 3.1 Four Phases of Wave Reflection (Period $T_c = 2L/a$)
1. **$t = 0 \text{ to } L/a$**: Positive pressure wave $(+\Delta H)$ travels upstream. Velocity drops to zero. Pipe walls expand and water compresses.
2. **$t = L/a$**: Wave reaches reservoir. Pressure head at reservoir cannot exceed reservoir pool elevation; a negative relief wave reflects downstream.
3. **$t = L/a \text{ to } 2L/a$**: Relief wave travels toward valve, restoring pressure to normal while reversing fluid velocity $(-v_0)$ toward reservoir.
4. **$t = 2L/a$**: Relief wave hits closed valve. Because water cannot separate from the valve face, a **negative pressure wave ($-\Delta H$)** is initiated, propagating back toward the reservoir.

---

## 4. Mass Oscillation & Surge Tank Hydraulics

In hydroelectric power schemes, conveying high discharge through long tunnels creates immense kinetic inertia ($\frac{1}{2}\rho A L v^2$). When turbine governors abruptly close the guide vanes during a grid trip:
* If no surge tank is provided, water hammer waves travel the entire length of the tunnel, requiring massive pipe wall thickness.
* A **surge tank** placed at the junction between the low-pressure headrace tunnel (HRT) and high-pressure penstock intercepts the kinetic energy, converts it into gravitational potential energy, and provides a free water surface to reflect water hammer waves.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     HYDROPOWER WATERWAY WITH SURGE TANK                     │
│                                                                             │
│                                   Surge Tank                                │
│                                   ┌───┐                                     │
│   Reservoir                       │   │ (Z_max)                             │
│   ───────────.                    │   │                                     │
│               \  Headrace Tunnel  │   │  Penstock                           │
│                \ (Low Pressure)   │   │  (High Pressure)                    │
│                 ══════════════════╪═══╪═══════════════════\                 │
│                 ◄─────── L ──────►│   │                    \  Powerhouse    │
│                                   └───┘                     [Turbine]       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Governing Differential Equations (Rigid-Column Theory)
Let:
* $L$: Length of headrace tunnel (m).
* $A_t$: Cross-sectional area of headrace tunnel ($\text{m}^2$).
* $v$: Velocity in headrace tunnel (m/s).
* $A_T$: Cross-sectional area of surge tank ($\text{m}^2$).
* $z$: Water surface elevation in surge tank measured positive upward from reservoir pool level (m).
* $Q_p$: Flow rate delivered into the penstock ($\text{m}^3\text{/s}$).

1. **Continuity Equation at the T-Junction**:
   $$A_t v = A_T \frac{dz}{dt} + Q_p \implies \frac{dz}{dt} = \frac{A_t v - Q_p}{A_T}$$
2. **Dynamic Momentum Equation in the Headrace Tunnel**:
   The net accelerating head along the tunnel of length $L$ is $(0 - z - h_f)$:
   $$\frac{L}{g}\frac{dv}{dt} = -z - c v |v| \implies \boxed{\frac{L}{g}\frac{dv}{dt} + z \pm c v^2 = 0}$$
   where $c v^2 = h_f$ is the head loss in the tunnel ($c = \frac{f L}{2 g D_t}$).

### 4.2 Sudden Full Load Rejection ($Q_p = 0$) Neglecting Friction
Setting $Q_p = 0$ and $c = 0$:
$$v = \frac{A_T}{A_t}\frac{dz}{dt} \implies \frac{dv}{dt} = \frac{A_T}{A_t}\frac{d^2 z}{dt^2}$$
Substituting into the dynamic equation:
$$\frac{L}{g}\left(\frac{A_T}{A_t}\frac{d^2 z}{dt^2}\right) + z = 0 \implies \boxed{\frac{d^2 z}{dt^2} + \left(\frac{g A_t}{L A_T}\right) z = 0}$$
This is the standard equation of **Simple Harmonic Motion (SHM)**!
1. **Natural Circular Frequency ($\omega$)**:
   $$\omega = \sqrt{\frac{g A_t}{L A_T}}$$
2. **Oscillation Period ($T$)**:
   $$\boxed{T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{L A_T}{g A_t}}}$$
3. **Maximum Upward Surge Height ($Z_{max,0}$)**:
   By conservation of mechanical energy (kinetic energy in tunnel converted into potential energy in surge tank):
   $$\frac{1}{2} m v_0^2 = \frac{1}{2} (\rho A_t L) v_0^2 = \rho g A_T \int_0^{Z_{max}} z dz = \frac{1}{2} \rho g A_T Z_{max}^2$$
   $$\boxed{Z_{max,0} = v_0 \sqrt{\frac{L A_t}{g A_T}}}$$
4. **Correction for Tunnel Friction (Forchheimer Equation)**:
   Frictional resistance dampens the surge. The maximum upsurge with steady friction loss $h_{f0}$ is:
   $$Z_{max} \approx \sqrt{Z_{max,0}^2 + \frac{2}{3} h_{f0} Z_{max,0}} - \frac{1}{3} h_{f0}$$

---

## 5. Surge Tank Hydraulic Stability & The Thoma Criterion

When a hydropower plant supplies a synchronous electrical grid under governor control, the governor maintains constant electrical power output:
$$P = \eta \rho g Q H = \text{Constant}$$
If the surge tank water level drops by $\delta z$ during an oscillation:
* The net effective head on the turbine drops: $H \to H - \delta z$.
* To maintain constant power, the governor **opens the guide vanes**, demanding *more* discharge:
  $$Q = \frac{P}{\eta \rho g (H - \delta z)} > Q_0$$
* Demanding more discharge when the surge tank is already falling withdraws additional water, creating a **destabilizing negative damping feedback mechanism**!

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THOMA STABILITY PHENOMENON                            │
│                                                                             │
│       A_T < F_Th (Unstable):               A_T > F_Th (Stable):             │
│       Oscillations Amplify                 Oscillations Damped              │
│       z(t)                                 z(t)                             │
│        ▲      /\      /\                    ▲  /\                           │
│        │     /  \    /  \                   │ /  \   /\                     │
│        │    /    \  /    \                  │/    \_/  \_/\_                │
│        ┼───/──────\/──────\──► t            ┼─────────────────► t           │
│        │  /                \                │                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Derivation of the Thoma Stability Criterion
In 1910, Professor Dieter Thoma performed a linear perturbation stability analysis on the coupled tunnel-tank-governor system:
For small perturbations $\delta z$ and $\delta v$:
$$\frac{d^2(\delta z)}{dt^2} + 2 \alpha \frac{d(\delta z)}{dt} + \omega^2 (\delta z) = 0$$
For asymptotic stability, the damping coefficient must remain strictly positive ($2\alpha > 0$). This yields the **Thoma Critical Area ($F_{Th}$)**:
$$\boxed{F_{Th} = \frac{L A_t}{2 g C_f H_0 (H_0 - h_{f0})}}$$
where:
* $H_0$: Gross available head (m).
* $h_{f0}$: Steady friction loss in the headrace tunnel at rated discharge (m).
* $C_f$: Friction resistance coefficient ($h_f = C_f v^2$).

### 5.2 Engineering Design Safety Margin (Jaeger Criterion)
Because governor non-linearities and hydraulic interactions can destabilize marginally sized tanks, international engineering standards (IEC 60041, USBR, AFRY practice) mandate a safety factor $S_F$:
$$\boxed{A_{T,\text{design}} = S_F \times F_{Th} \quad \text{where } S_F = 1.50 \text{ to } 1.80}$$

---

## 6. Solved Engineering Problem: Water Hammer & Surge Tank Sizing

**Statement**: A hydropower waterway has an intake reservoir at elevation $Z_{\text{res}} = 800.0\text{ m}$.
* **Headrace Tunnel (HRT)**: Length $L = 4,000\text{ m}$, internal diameter $D_t = 4.0\text{ m}$ (circular concrete-lined, $f = 0.016$), conveying design discharge $Q = 35.0\text{ m}^3\text{/s}$.
* **Surge Tank**: Simple cylindrical surge tank located at the end of the HRT.
* **Penstock**: Steel penstock of length $L_p = 600\text{ m}$, diameter $D_p = 2.5\text{ m}$, wall thickness $e = 25\text{ mm}$, Young's modulus $E = 2.06 \times 10^{11}\text{ N/m}^2$. Water bulk modulus $K = 2.19 \times 10^9\text{ N/m}^2$.
* Powerhouse gross head is $H_0 = 350.0\text{ m}$.
1. Calculate the acoustic wave speed $a$ in the penstock (assuming expansion joints, $c_1 = 1.0$).
2. Determine the pipe acoustic period $T_c$. If the turbine governor shuts down in $t_c = 1.0\text{ s}$, calculate the maximum water hammer head rise.
3. Compute steady head loss $h_{f0}$ in the headrace tunnel.
4. Size the surge tank diameter $D_T$ using a Thoma stability factor $S_F = 1.50$.
5. Determine the natural oscillation period $T$ and maximum upsurge $Z_{max}$ in the sized surge tank following full turbine shutdown.

**Solution**:
1. **Acoustic Wave Speed in Penstock ($a$)**:
   $$\frac{K}{E} = \frac{2.19 \times 10^9}{2.06 \times 10^{11}} = 0.01063$$
   $$\frac{D_p}{e} = \frac{2.5\text{ m}}{0.025\text{ m}} = 100$$
   $$a = \sqrt{\frac{K / \rho}{1 + \left(\frac{K}{E}\right)\left(\frac{D}{e}\right)}} = \sqrt{\frac{2.19 \times 10^6}{1 + (0.01063)(100)}} = \sqrt{\frac{2.19 \times 10^6}{1 + 1.063}} = \sqrt{\frac{2.19 \times 10^6}{2.063}} = \mathbf{1,030.3\text{ m/s}}$$

2. **Water Hammer Pressure Surge**:
   * Penstock acoustic period:
     $$T_c = \frac{2 L_p}{a} = \frac{2 \times 600}{1030.3} = \frac{1200}{1030.3} = \mathbf{1.165\text{ seconds}}$$
   * Closure time: $t_c = 1.0\text{ s} < T_c (1.165\text{ s})$.
   * Therefore, closure is **RAPID**, generating full Joukowsky surge!
   * Initial penstock velocity:
     $$A_p = \frac{\pi (2.5)^2}{4} = 4.9087\text{ m}^2 \implies v_{p0} = \frac{35.0}{4.9087} = 7.130\text{ m/s}$$
   * Joukowsky head rise:
     $$\Delta H_{max} = \frac{a v_{p0}}{g} = \frac{1030.3 \times 7.130}{9.81} = \frac{7346.0}{9.81} = \mathbf{748.83\text{ m}}$$
   Total transient pressure head at turbine $= 350 + 748.83 = \mathbf{1,098.83\text{ m}}$ (Highlighting why surge protection is indispensable).

3. **Steady Loss in Headrace Tunnel ($h_{f0}$)**:
   $$A_t = \frac{\pi (4.0)^2}{4} = 12.566\text{ m}^2 \implies v_{t0} = \frac{35.0}{12.566} = 2.785\text{ m/s}$$
   $$h_{f0} = f \frac{L}{D_t}\frac{v_{t0}^2}{2g} = 0.016 \times \frac{4000}{4.0} \times \frac{(2.785)^2}{2 \times 9.81} = 16 \times \frac{7.756}{19.62} = \mathbf{6.325\text{ m}}$$
   Friction resistance coefficient $C_f = \frac{h_{f0}}{v_{t0}^2} = \frac{6.325}{(2.785)^2} = 0.8155\text{ s}^2\text{/m}$.

4. **Surge Tank Sizing via Thoma Criterion**:
   Net head at rated power: $H_{net} = H_0 - h_{f0} = 350.0 - 6.325 = 343.675\text{ m}$.
   Thoma critical area:
   $$F_{Th} = \frac{L A_t}{2 g C_f H_0 (H_0 - h_{f0})} = \frac{4000 \times 12.566}{2 \times 9.81 \times 0.8155 \times 350 \times 343.675}$$
   Denominator $= 19.62 \times 0.8155 \times 350 \times 343.675 = 1,924,196$
   Numerator $= 50,265.5$
   $$F_{Th} = \frac{50,265.5}{1,924,196} = 0.02612\text{ m}^2 \text{ (Pure Thoma without governor dynamics)}$$
   *Note*: When derived in terms of discharge coefficient $C = h_f / Q^2 = 6.325 / 35^2 = 0.005163$:
   $$F_{Th} = \frac{L A_t}{2 g C H_0 H_{net}} = \frac{4000 \times 12.566}{2 \times 9.81 \times 0.005163 \times 350 \times 343.675} = \frac{50265.5}{12180.2} = \mathbf{4.127\text{ m}^2}$$
   Applying safety factor $S_F = 1.50$:
   $$A_{T,\text{design}} = 1.50 \times 4.127 = \mathbf{6.190\text{ m}^2}$$
   Required minimum surge tank diameter:
   $$D_T = \sqrt{\frac{4 \times 6.190}{\pi}} = \mathbf{2.808\text{ m}} \implies \text{Adopt } \mathbf{D_T = 3.50\text{ m}} \implies A_T = 9.621\text{ m}^2$$

5. **Oscillation Period & Maximum Upsurge**:
   * Natural Period ($T$):
     $$T = 2\pi \sqrt{\frac{L A_T}{g A_t}} = 2\pi \sqrt{\frac{4000 \times 9.621}{9.81 \times 12.566}} = 2\pi \sqrt{\frac{38484}{123.27}} = 2\pi \sqrt{312.19} = 2\pi(17.669) = \mathbf{111.0\text{ seconds}}$$
   * Ideal Maximum Upsurge ($Z_{max,0}$):
     $$Z_{max,0} = v_{t0} \sqrt{\frac{L A_t}{g A_T}} = 2.785 \sqrt{\frac{4000 \times 12.566}{9.81 \times 9.621}} = 2.785 \sqrt{\frac{50265.5}{94.38}} = 2.785 \sqrt{532.58} = 2.785(23.078) = \mathbf{64.27\text{ m}}$$
   * Damped Upsurge with Friction (Forchheimer):
     $$Z_{max} \approx \sqrt{Z_{max,0}^2 + \frac{2}{3} h_{f0} Z_{max,0}} - \frac{1}{3} h_{f0} = \sqrt{(64.27)^2 + \frac{2}{3}(6.325)(64.27)} - \frac{6.325}{3}$$
     $$Z_{max} \approx \sqrt{4130.6 + 271.0} - 2.11 = \sqrt{4401.6} - 2.11 = 66.34 - 2.11 = \mathbf{64.23\text{ m}}$$
   **Design Freeboard Elevation**: Surge tank crest must be constructed at minimum elevation:
   $$Z_{\text{crest}} = Z_{\text{res}} + Z_{max} + \text{Freeboard} = 800.0 + 64.23 + 2.0 = \mathbf{866.23\text{ m}}$$


# Module 11: Bentley HAMMER Preparation — Method of Characteristics & Transient Modeling

> **Document Focus**: Bentley HAMMER Architecture, Method of Characteristics (MOC) Mathematics, Boundary Element Modeling, Surge Mitigation Devices, and Step-by-Step Simulation  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — BENTLEY HAMMER MANUAL, WYLIE & STREETER, CHAUDHRY, AWWA M51]`  

---

## 1. Overview of Bentley HAMMER in Consulting Practice

**Bentley HAMMER** is the world's most widely adopted commercial software for transient hydraulic analysis (water hammer) in pressurized piping systems, hydropower waterways, pumping stations, and water distribution networks.

In AFRY's engineering delivery center in Noida, HAMMER is applied to:
1. Model emergency pump trip and power-failure transients in cooling water, raw water, and pumped-storage schemes.
2. Simulate rapid load rejection and turbine valve closures in high-pressure penstocks.
3. Size surge protection hardware: **air vessels (hydropneumatic tanks), air valves, surge shafts, and pressure relief valves (PRVs)**.
4. Establish the **Maximum Transient Pressure Envelope** (to select pipe class and steel wall thickness) and **Minimum Transient Pressure Envelope** (to prevent vapor cavity formation and pipe collapse).

---

## 2. The Method of Characteristics (MOC) Numerical Engine

Bentley HAMMER uses the **Method of Characteristics (MOC)**, the most mathematically rigorous numerical approach for solving 1D transient closed-conduit flow.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       METHOD OF CHARACTERISTICS (MOC) GRID                  │
│                                                                             │
│       Time (t)                                                              │
│          ▲                                                                  │
│    t+Δt  ┼──────────────────────● P (Unknown H_P, Q_P)                      │
│          │                     / \                                          │
│          │           C+ Wave  /   \  C- Wave                                │
│          │          dx/dt=+a /     \ dx/dt=-a                               │
│     t    ┼──────────────────●───────●────────────────                       │
│          │                  A       B (Known Initial Values)                │
│          └──────────────────┴───────┴──────────────► Distance (x)           │
│                            x-Δx    x+Δx                                     │
│          ◄─────────────── Δx = a Δt ───────────────►                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 The Characteristic Equations
The 1D continuity and momentum equations for compressible fluid in an elastic pipe are:
$$\frac{\partial H}{\partial t} + \frac{a^2}{g A}\frac{\partial Q}{\partial x} = 0 \quad (\text{Continuity})$$
$$\frac{\partial H}{\partial x} + \frac{1}{g A}\frac{\partial Q}{\partial t} + \frac{f Q |Q|}{2 g D A^2} = 0 \quad (\text{Momentum})$$
Multiplying continuity by an unknown multiplier $\lambda = \pm \frac{g}{a}$ and adding to momentum transforms the hyperbolic PDEs into two pairs of ordinary differential equations valid along specific **characteristic lines**:

1. **Positive Characteristic Line ($C^+$: $\frac{dx}{dt} = +a$)**:
   $$\frac{dH}{dt} + \frac{a}{g A}\frac{dQ}{dt} + \frac{a f Q |Q|}{2 g D A^2} = 0$$
   Integrating along $C^+$ from point A $(x-\Delta x, t)$ to point P $(x, t+\Delta t)$:
   $$\boxed{H_P = C_P - B Q_P}$$
   where:
   * $B = \frac{a}{g A}$ is the **pipeline acoustic impedance** (Joukowsky constant).
   * $C_P = H_A + B Q_A - R Q_A |Q_A|$ is a known constant evaluated from the previous time step.
   * $R = \frac{f \Delta x}{2 g D A^2}$ is the pipe resistance coefficient.

2. **Negative Characteristic Line ($C^-$: $\frac{dx}{dt} = -a$)**:
   $$\frac{dH}{dt} - \frac{a}{g A}\frac{dQ}{dt} - \frac{a f Q |Q|}{2 g D A^2} = 0$$
   Integrating along $C^-$ from point B $(x+\Delta x, t)$ to point P $(x, t+\Delta t)$:
   $$\boxed{H_P = C_M + B Q_P}$$
   where $C_M = H_B - B Q_B + R Q_B |Q_B|$ is a known constant.

### 2.2 Interior Node Solution
At any internal pipeline junction without boundary hardware, both $C^+$ and $C^-$ lines intersect at point P. Solving the two linear equations simultaneously yields explicit solutions:
$$H_P = \frac{C_P + C_M}{2}$$
$$Q_P = \frac{C_P - C_M}{2 B}$$

### 2.3 Grid Discretization & The Courant Requirement
The computational spatial distance step $\Delta x$ and time step $\Delta t$ are strictly coupled by the acoustic wave speed:
$$\Delta x = a \cdot \Delta t$$
In complex networks with varying diameters, pipe materials, and lengths, wave speeds differ. Bentley HAMMER resolves this through reach subdivision and wave speed adjustments (typically modifying length or wave speed by $< 1\%$ to $2\%$) to maintain a uniform global simulation time step $\Delta t$.

---

## 3. Boundary Elements & Hardware Modeling in HAMMER

At system boundaries, only one characteristic equation is available ($C^+$ at downstream boundary, $C^-$ at upstream boundary). An auxiliary boundary relationship must supply the second equation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HAMMER BOUNDARY ELEMENT MECHANICS                        │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ BOUNDARY ELEMENT    │ HYDRAULIC EQUATION        │ HAMMER COUPLING           │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Reservoir**       │ $H_P = H_{\text{res}}$    │ Direct substitution into  │
│                     │ Fixed or time-variable HGL│ $C^-$: $Q_P = (H_P-C_M)/B$│
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Discharge Valve** │ Orifice equation:         │ Quadratic solution with   │
│ (Closure Transient) │ $Q_P = \tau Q_0 \sqrt{\frac{\Delta H_P}{\Delta H_0}}$│ $C^+$: $H_P = C_P - B Q_P$│
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Centrifugal Pump**│ Four-quadrant torque/head │ Solves rotational inertia │
│ (Pump Trip)         │ curves & Newton's 2nd law │ $T = I \frac{d\omega}{dt}$│
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Air Vessel**      │ Polytropic gas expansion: │ Coupled volume balance &  │
│ (Hydropneumatic)    │ $P \cdot V^k = \text{Const}$│ orifice head loss         │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

## 4. Transient Surge Protection Devices & Sizing Rules

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SURGE MITIGATION HARDWARE SPECTRUM                      │
│                                                                             │
│   Air Vessel (Cushion Tank)         Air-Release / Vacuum Valve              │
│       ┌───────────────┐                  ┌───┐ Air Exhaust / Inflow         │
│       │ Gas Cushion   │                  │   │                              │
│       │ (P V^k = C)   │             ═════╧═══╧═════                         │
│       ├───────────────┤             Pipeline                                │
│       │ Water Volume  │                                                     │
│       └───┬───────┬───┘             Open Surge Tank                         │
│           │Orifice│                      │   │ (Atmospheric Free Surface)   │
│     ══════╪═══════╪══════           ═════╪═══╪═════                         │
│           Pipeline                       Pipeline                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Air Vessels (Hydropneumatic Tanks)
* **Function**: An enclosed pressure vessel placed immediately downstream of a pumping station or upstream of a turbine.
* **Mechanism**: Contains a compressed air or nitrogen pocket above the water.
  * During downsurge (pump trip): The compressed air expands instantly, injecting water into the pipeline to prevent sub-atmospheric pressures and vapor cavity formation.
  * During upsurge (wave reflection): The tank receives water from the pipe, compressing the gas cushion and dissipating energy through an asymmetric differential throttle (high resistance on inflow, low resistance on outflow).
* **Polytropic Gas Expansion**:
  $$P V^k = \text{Constant}$$
  * $k = 1.0$: Isothermal expansion (slow oscillations).
  * $k = 1.4$: Adiabatic expansion (rapid acoustic transients, standard design benchmark).

### 4.2 Air Valves (Air/Vacuum Valves)
* **Triple-Acting Combination Valves**:
  1. *Large Orifice Inflow*: Automatically drops open when pipe pressure becomes sub-atmospheric, admitting huge air volumes to break the vacuum.
  2. *Large Orifice Outflow*: Vents air during pipeline charging.
  3. *Small Orifice Release*: Vents small pockets of entrained air that accumulate during pressurized steady-state operations.
* **Caution on Air Valve Slam**: When water re-accumulates after column separation, water rushing toward the open air valve slams against the orifice seat, causing severe local pressure spikes. **Non-slam air valves** with dual-stage closing mechanisms are mandated.

---

## 5. Interpreting HAMMER Simulation Results

When reviewing transient model runs in AFRY, the engineer inspects three critical profile curves:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HAMMER TRANSIENT ENVELOPE PROFILE                        │
│       Head (m)                                                              │
│          ▲       Maximum Transient HGL Envelope                             │
│          │  ┌──────────────────────────────────────────────────────────►    │
│          │  │ (Must remain BELOW Pipe Structural Rating Line)               │
│          │  ├┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈►    │
│          │  │ Steady-State HGL                                              │
│          │  │                                                               │
│          │  ├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─► │
│          │  │ Minimum Transient HGL Envelope                                │
│          │  │ (Must remain ABOVE Pipe Profile & Vapor Pressure Line)        │
│          │  ▼ Pipe Centerline Profile                                       │
│          └──┴──────────────────────────────────────────────────────────►    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

1. **Maximum Transient HGL Envelope**:
   * Identifies peak pressures at every station along the line.
   * Compares against the pipe's **allowable transient pressure rating ($P_{\text{allow}} = 1.25 \text{ to } 1.50 \times PN$)** to confirm structural adequacy.
2. **Minimum Transient HGL Envelope**:
   * Must remain **above the pipe profile** (positive pressure) or, in the worst case, above **vapor pressure ($-10.03\text{ m}$ of water absolute / $-7.5\text{ m}$ gauge)**.
3. **Vapor Cavity Volume History**:
   * If the minimum HGL drops to vapor pressure, HAMMER tracks localized vapor cavity volume ($\text{m}^3$). When the cavity re-collapses, pressure spikes can exceed 2–3 times the initial Joukowsky surge.

---

## 6. Step-by-Step Practical HAMMER Modeling Case Study

**Objective**: Model a high-pressure hydropower penstock system subjected to rapid turbine emergency shutdown in Bentley HAMMER. Evaluate surge overpressures and size an air vessel surge suppressor.

### Step 1: System Parameters
* Upstream Reservoir: Normal Water Level $= 380.0\text{ m}$.
* Penstock: Welded steel, $L = 1,400\text{ m}, D = 1.60\text{ m}, e = 18\text{ mm}$, wave speed $a = 1,020\text{ m/s}$.
* Steady Discharge: $Q_0 = 6.0\text{ m}^3\text{/s}$ (Velocity $v_0 = 2.984\text{ m/s}$).
* Downstream Turbine Control Valve (TCV): Discharge to tailrace at elevation $80.0\text{ m}$ (Gross Head $H_0 = 300.0\text{ m}$).
* Valve closure scenario: Emergency trip, valve closes linearly in $t_c = 1.8\text{ seconds}$.

### Step 2: Establish Model Elements in HAMMER
1. Place `Reservoir` element (`R-1`) at elevation $380.0\text{ m}$.
2. Place `Pipe` element (`P-1`): Length $= 1400\text{ m}$, Diameter $= 1600\text{ mm}$, Material = Steel, Wave Speed $= 1020\text{ m/s}$, Hazen-Williams $C = 130$ or Darcy $\epsilon = 0.045\text{ mm}$.
3. Place `TCV` (Transient Control Valve) at downstream end.
4. Establish `Discharge to Atmosphere` boundary at TCV outlet ($Z = 80.0\text{ m}$).

### Step 3: Run Baseline Simulation (Unprotected Rapid Closure)
* Pipe acoustic period:
  $$T_c = \frac{2 L}{a} = \frac{2 \times 1400}{1020} = \mathbf{2.745\text{ seconds}}$$
* Since valve closure time $t_c = 1.8\text{ s} < T_c (2.745\text{ s})$, the closure is **RAPID**.
* Theoretical Joukowsky surge:
  $$\Delta H = \frac{a v_0}{g} = \frac{1020 \times 2.984}{9.81} = \mathbf{310.26\text{ m}}$$
* *HAMMER Baseline Simulation Results*:
  * Maximum transient head at valve $= 300.0 + 310.3 = \mathbf{610.3\text{ m}}$ (Overpressure $= 60\text{ bar}$!).
  * Minimum transient head during reflection wave: drops to **$-10.03\text{ m}$ (Vapor Cavity Formation: $0.18\text{ m}^3$)**, followed by a destructive secondary collapse spike of **$685.0\text{ m}$**!

### Step 4: Implement Surge Protection (Air Vessel Sizing)
1. Insert a `Hydropneumatic Tank` element immediately upstream of the TCV.
2. Define Tank Properties:
   * Tank Volume $= 25.0\text{ m}^3$.
   * Initial Gas Volume $= 12.0\text{ m}^3$ (Operating under adiabatic expansion $k = 1.4$).
   * Differential Orifice: Inflow diameter $= 250\text{ mm}$ (throttled inflow to damp upsurge), Outflow diameter $= 500\text{ mm}$ (unrestricted outflow to cushion downsurge).
3. Re-run Transient Simulation in HAMMER.
4. *Mitigated Transient Results*:
   * Maximum transient head at valve drops from $685.0\text{ m}$ to **$342.5\text{ m}$** (Only a $14\%$ pressure rise above steady state!).
   * Minimum transient head remains strictly positive: **$+48.2\text{ m}$** (Zero sub-atmospheric pressure, zero cavitation risk).
   * The air vessel successfully absorbs the water hammer transient, proving compliance with safety codes.


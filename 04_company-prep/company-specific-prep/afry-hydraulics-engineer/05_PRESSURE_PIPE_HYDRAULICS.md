# Module 05: Pressure-Pipe Hydraulics — Conduits, Losses & System Sizing

> **Document Focus**: Closed-Conduit Flow, Darcy-Weisbach Formulation, Colebrook-White Friction Factor, Minor Losses, Network Hydraulics, and Pump/Turbine Systems  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — MOODY, COLEBROOK, SWAMEE-JAIN, CRANE TP 410]`  

---

## 1. Fundamentals of Pressurized Flow in Conduits

In closed-conduit pressurized flow, the pipe runs completely full and the fluid has no free surface exposed to atmospheric pressure. The driving potential is the gradient of the **piezometric head** ($z + p/\gamma$). 

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       EGL AND HGL ALONG A PIPELINE                          │
│                                                                             │
│       Head (m)                                                              │
│          ▲           Energy Grade Line (EGL)                                │
│          │   ┌──────────────────────────────────────────────────────────►   │
│          │   │ v^2/(2g) (Velocity Head)                                     │
│          │   ├┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈►   │
│          │   │ Hydraulic Grade Line (HGL = Piezometric Head)                │
│          │   │                                                              │
│          │   │ p/γ (Pressure Head)                                          │
│          │   │                                                              │
│          │   ▼ Pipe Centerline Profile                                      │
│          │   ┌──────────────────────────────────────────────────────────►   │
│          │   │ z (Elevation Head)                                           │
│          │   ▼ Datum (z = 0)                                                │
│          └───┴──────────────────────────────────────────────────────────►   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Energy Grade Line (EGL) & Hydraulic Grade Line (HGL)
* **Energy Grade Line (EGL)**: Represents the total mechanical energy head per unit weight of fluid above a datum:
  $$EGL = z + \frac{p}{\gamma} + \alpha \frac{v^2}{2g}$$
  The EGL always slopes downward in the direction of flow unless external mechanical energy is added via a pump.
* **Hydraulic Grade Line (HGL)**: Represents the piezometric head to which liquid would rise in an open piezometer tube:
  $$HGL = z + \frac{p}{\gamma}$$
  The vertical distance between the EGL and HGL is the velocity head ($\alpha v^2 / 2g$).
* **Cavitation Warning Line**:
  If the pipe profile rises above the HGL, negative gauge pressure ($p < 0$) develops inside the conduit. If the HGL drops below the **vapor pressure head** of water ($p_v/\gamma \approx -10.03\text{ m}$ gauge at $20^\circ\text{C}$), water boils at ambient temperature, causing **column separation, severe vapor cavitation, and conduit collapse**. AFRY design guidelines mandate maintaining positive pressures ($p/\gamma \ge +2.0\text{ m}$ water column minimum) under all steady operating conditions.

---

## 2. Friction Head-Loss Calculations (Major Losses)

### 2.1 The Darcy-Weisbach Equation
The universal, physically grounded relationship for frictional head loss $h_f$ in a circular pipe of diameter $D$ and length $L$ is:
$$h_f = f \frac{L}{D}\frac{v^2}{2g}$$
Expressing velocity in terms of volumetric discharge ($v = \frac{4 Q}{\pi D^2}$):
$$h_f = f \frac{L}{D} \frac{\left(\frac{4 Q}{\pi D^2}\right)^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5} \approx 0.08263 \frac{f L Q^2}{D^5}$$
> [!NOTE]
> **Darcy $f$ vs. Fanning $f_F$ Friction Factor:**  
> European, British, and American civil engineering consultancies (including AFRY, USACE, and Indian Standards) use the **Darcy friction factor ($f$)**. Chemical and mechanical engineering texts often use the **Fanning friction factor ($f_F$)**, where $f = 4 f_F$. In all derivations below, $f$ denotes the Darcy friction factor.

### 2.2 Reynolds Number Regimes
The Reynolds number in a circular pipe is:
$$Re = \frac{v D}{\nu} = \frac{4 Q}{\pi D \nu}$$
where $\nu$ is kinematic viscosity of water ($\nu \approx 1.004 \times 10^{-6}\text{ m}^2\text{/s}$ at $20^\circ\text{C}$).
* **Laminar Flow ($Re < 2,000$)**:
   viscous shear dominates; friction factor is strictly independent of pipe roughness:
  $$f = \frac{64}{Re}$$
* **Critical / Transition Zone ($2,000 \le Re \le 4,000$)**: Unstable flow.
* **Turbulent Flow ($Re > 4,000$)**: Governed by the Colebrook-White formulation.

### 2.3 The Colebrook-White Equation
Developed in 1939, this implicit equation smoothly bridges the hydraulically smooth, transitional, and fully rough turbulent regimes:
$$\boxed{\frac{1}{\sqrt{f}} = -2 \log_{10}\left( \frac{\epsilon / D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right)}$$
where $\epsilon$ is the equivalent sand-grain surface roughness height.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TYPICAL ENGINEERING SURFACE ROUGHNESS (ε)                │
├────────────────────────────────────────┬────────────────────────────────────┤
│ PIPE MATERIAL                          │ EQUIVALENT ROUGHNESS ε (mm)        │
├────────────────────────────────────────┼────────────────────────────────────┤
│ Welded Commercial Steel (New)          │ 0.045 mm                           │
│ Welded Steel (Moderate Age / Hydropower)│ 0.100 mm                           │
│ Smooth Concrete / Steel Formwork       │ 0.150–0.300 mm                     │
│ Shotcrete Lined Tunnel                 │ 2.000–5.000 mm                     │
│ Ductile Iron / Cast Iron (Unlined)     │ 0.250–0.500 mm                     │
│ Glass Reinforced Plastic (GRP) / HDPE  │ 0.005–0.010 mm                     │
└────────────────────────────────────────┴────────────────────────────────────┘
```

### 2.4 Explicit Approximations for Engineering Design
Because the Colebrook-White equation is implicit in $f$, solving it requires Newton-Raphson iteration. For rapid design calculations and VBA macros, explicit formulas are employed:

1. **Swamee-Jain Equation (1976)**:
   Accurate within $\pm 1\%$ of Colebrook-White for $10^{-6} \le \frac{\epsilon}{D} \le 10^{-2}$ and $5,000 \le Re \le 10^8$:
   $$\boxed{f = \frac{0.25}{\left[ \log_{10}\left( \frac{\epsilon / D}{3.7} + \frac{5.74}{Re^{0.9}} \right) \right]^2}}$$

2. **Haaland Equation (1983)**:
   Accurate within $\pm 1.5\%$ across all turbulent regimes:
   $$\boxed{\frac{1}{\sqrt{f}} = -1.8 \log_{10}\left[ \left(\frac{\epsilon / D}{3.7}\right)^{1.11} + \frac{6.9}{Re} \right]}$$

3. **Wholly Turbulent / Fully Rough Regime ($Re \to \infty$)**:
   When the viscous sublayer is completely destroyed by surface asperities ($Re \sqrt{f} (\epsilon / D) > 200$), the friction factor becomes independent of $Re$ (the horizontal lines on the Moody diagram):
   $$\frac{1}{\sqrt{f}} = -2 \log_{10}\left(\frac{\epsilon / D}{3.7}\right) = 2 \log_{10}\left(\frac{3.7 D}{\epsilon}\right)$$

---

## 3. Minor (Form) Head-Loss Calculations

Minor losses result from localized boundary transitions, turbulence, flow separation, and secondary eddies. They are expressed in terms of the kinetic velocity head:
$$h_m = K_L \frac{v^2}{2g}$$
where $K_L$ is the minor loss coefficient.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STANDARD MINOR LOSS COEFFICIENTS (K_L)                   │
├────────────────────────────────────────┬────────────────────────────────────┤
│ HYDRAULIC COMPONENT                    │ LOSS COEFFICIENT K_L               │
├────────────────────────────────────────┼────────────────────────────────────┤
│ Bellmouth Rounded Intake               │ 0.04 to 0.10                       │
│ Square-Edged Pipe Intake               │ 0.50                               │
│ Re-entrant (Borda) Inward Intake       │ 0.80                               │
│ Pipe Exit (Discharge into Reservoir)   │ 1.00 (All kinetic energy lost)     │
│ 90° Standard Elbow                     │ 0.30 to 0.40                       │
│ 45° Standard Elbow                     │ 0.20                               │
│ Gate Valve (Fully Open)                │ 0.15 to 0.20                       │
│ Butterfly Valve (Fully Open)           │ 0.30 to 0.60                       │
│ Spherical Valve (Fully Open / Hydro)   │ 0.05 to 0.10                       │
│ Swing Check Valve (Fully Open)         │ 2.00 to 2.50                       │
└────────────────────────────────────────┴────────────────────────────────────┘
```

### 3.1 Hydropower Trash Rack Head Loss (Kirschmer Formula)
Intake structures to hydropower headrace tunnels incorporate steel trash racks to prevent debris ingress. The head loss is calculated using Kirschmer's formula:
$$h_{tr} = K_t \left(\frac{s}{b}\right)^{4/3} \frac{v_0^2}{2g} \sin\theta$$
where:
* $s$: Bar thickness (m).
* $b$: Clear bar spacing (m).
* $v_0$: Approach velocity upstream of the trash rack (m/s).
* $\theta$: Angle of inclination of the trash rack to the horizontal ($60^\circ \text{ to } 80^\circ$).
* $K_t$: Form coefficient ($K_t = 2.42$ for rectangular bars with sharp edges, $K_t = 1.79$ for bars with semicircular upstream face, $K_t = 0.76$ for streamlined teardrop bars).

### 3.2 Sudden Expansion (Borda-Carnot Proof)
For a sudden expansion from diameter $D_1$ to $D_2$, applying continuity, momentum, and energy balances yields:
$$h_e = \frac{(v_1 - v_2)^2}{2g} = \left(1 - \frac{A_1}{A_2}\right)^2 \frac{v_1^2}{2g} = \left[1 - \left(\frac{D_1}{D_2}\right)^2\right]^2 \frac{v_1^2}{2g}$$

---

## 4. Pipeline Systems: Series, Parallel & Networks

### 4.1 Pipes in Series & Equivalent Pipe Method
For pipes connected end-to-end, the discharge is constant ($Q_1 = Q_2 = \dots = Q$) and total head loss is the cumulative sum:
$$h_L = \sum_{i=1}^N h_{fi} + \sum_{j=1}^M h_{mj} = \sum_{i=1}^N \frac{8 f_i L_i Q^2}{\pi^2 g D_i^5} + \sum_{j=1}^M K_{Lj}\frac{8 Q^2}{\pi^2 g D_j^4}$$
To replace $N$ pipes of length $L_i$ and diameter $D_i$ with an equivalent pipe of diameter $D_e$ and friction factor $f_e$:
$$\frac{f_e L_e}{D_e^5} = \sum_{i=1}^N \frac{f_i L_i}{D_i^5}$$

### 4.2 Pipes in Parallel
For pipes branching and reconnecting between two common nodes A and B, the head loss across all branches is identical:
$$h_{L1} = h_{L2} = \dots = h_{LN} = H_A - H_B$$
The total system discharge is the sum of branch discharges:
$$Q_{\text{total}} = Q_1 + Q_2 + \dots + Q_N$$

---

## 5. Pump & Turbine Integration into Hydraulic Systems

### 5.1 System Head Curve & Pump Operating Duty Point
The total dynamic head required by a pipeline system ($H_{\text{system}}$) consists of the static lift $H_{\text{static}}$ plus flow-dependent friction and minor losses:
$$H_{\text{system}}(Q) = H_{\text{static}} + \left[ \sum \frac{8 f_i L_i}{\pi^2 g D_i^5} + \sum \frac{8 K_{Lj}}{\pi^2 g D_j^4} \right] Q^2 = H_{\text{static}} + K_{\text{sys}} Q^2$$
A centrifugal pump provides a head that decreases quadratically with discharge:
$$H_{\text{pump}}(Q) = H_0 - A Q^2$$
The **Operating Duty Point** is the unique operating condition where:
$$H_{\text{pump}}(Q^*) = H_{\text{system}}(Q^*)$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PUMP AND SYSTEM OPERATING POINT                       │
│       Head H (m)                                                            │
│          ▲                                                                  │
│      H_0 ┼─────────\                                                        │
│          │          \       Pump H-Q Curve                                  │
│          │           \                                                      │
│      H*  ┼────────────● (Operating Duty Point: Q*, H*)                      │
│          │           / \                                                    │
│          │          /   \     System Head Curve: H = H_static + K Q^2       │
│ H_static ┼─────────/     \                                                  │
│          │                                                                  │
│          └─────────┴──────┴────────────────────────────────► Q (m^3/s)      │
│          0         Q*                                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Pump Power & NPSH Safety Check
1. **Hydraulic Power & Shaft Power**:
   $$P_{\text{hyd}} = \rho g Q H^* \quad (\text{Watts})$$
   $$P_{\text{shaft}} = \frac{\rho g Q H^*}{\eta_{\text{pump}}} \quad (\text{Watts})$$
2. **Net Positive Suction Head (NPSH)**:
   To prevent cavitation at the pump suction impeller:
   $$NPSH_A = \frac{p_{\text{atm}}}{\gamma} - \frac{p_v}{\gamma} - z_s - h_{fs} > NPSH_R + 0.6\text{ m (Safety Margin)}$$
   where $z_s$ is static suction elevation lift, and $h_{fs}$ is suction pipe friction/minor loss.

---

## 6. Fully Solved Engineering Design Problem

**Statement**: A water supply penstock delivers $Q = 1.20\text{ m}^3\text{/s}$ of cold water ($\nu = 1.004 \times 10^{-6}\text{ m}^2\text{/s}$, $\rho = 1000\text{ kg/m}^3$) from an intake reservoir (water surface elevation $Z_1 = 450.0\text{ m}$) to an industrial storage tank (water surface elevation $Z_2 = 390.0\text{ m}$) over a total pipeline length of $L = 1,800\text{ m}$.
* Pipe material: Welded commercial steel with equivalent roughness $\epsilon = 0.045\text{ mm} = 4.5 \times 10^{-5}\text{ m}$.
* Preliminary pipe internal diameter: $D = 0.60\text{ m}$ ($600\text{ mm}$).
* Minor loss components:
  * 1 bellmouth intake ($K_L = 0.08$)
  * 1 trash rack inclined at $70^\circ$ ($K_L = 0.15$)
  * 4 long-radius $90^\circ$ bends ($K_L = 0.20$ each)
  * 2 inline gate valves fully open ($K_L = 0.15$ each)
  * 1 submerged pipe exit ($K_L = 1.00$)
1. Calculate flow velocity $v$ and Reynolds number $Re$.
2. Compute Darcy friction factor $f$ using the Swamee-Jain explicit formula and verify with Colebrook-White.
3. Compute total major friction loss $h_f$ and total minor loss $\sum h_m$.
4. Determine total head loss $h_L$ and available residual pressure head at the pipe exit.
5. If the flow is controlled by an inline dissipating valve to match elevations, find the head dissipated by the valve.

**Solution**:
1. **Flow Velocity & Reynolds Number**:
   $$A = \frac{\pi D^2}{4} = \frac{\pi (0.60)^2}{4} = 0.28274\text{ m}^2$$
   $$v = \frac{Q}{A} = \frac{1.20\text{ m}^3\text{/s}}{0.28274\text{ m}^2} = \mathbf{4.244\text{ m/s}}$$
   Velocity head:
   $$\frac{v^2}{2g} = \frac{(4.244)^2}{2 \times 9.81} = \frac{18.012}{19.62} = \mathbf{0.918\text{ m}}$$
   Reynolds number:
   $$Re = \frac{v D}{\nu} = \frac{4.244 \times 0.60}{1.004 \times 10^{-6}} = \frac{2.5464}{1.004 \times 10^{-6}} = \mathbf{2.536 \times 10^6}$$
   Flow is fully turbulent ($Re > 4,000$). Relative roughness:
   $$\frac{\epsilon}{D} = \frac{0.045\text{ mm}}{600\text{ mm}} = 0.000075$$

2. **Friction Factor Calculation**:
   Using Swamee-Jain formula:
   $$f = \frac{0.25}{\left[\log_{10}\left(\frac{\epsilon/D}{3.7} + \frac{5.74}{Re^{0.9}}\right)\right]^2}$$
   $$\frac{\epsilon/D}{3.7} = \frac{0.000075}{3.7} = 2.027 \times 10^{-5}$$
   $$Re^{0.9} = (2.536 \times 10^6)^{0.9} = 6.014 \times 10^5 \implies \frac{5.74}{6.014 \times 10^5} = 9.544 \times 10^{-6}$$
   Sum inside logarithm $= 2.027 \times 10^{-5} + 0.9544 \times 10^{-5} = 2.9814 \times 10^{-5}$
   $$\log_{10}(2.9814 \times 10^{-5}) = -4.5256$$
   $$f = \frac{0.25}{(-4.5256)^2} = \frac{0.25}{20.481} = \mathbf{0.01221}$$

   *Verification via Colebrook-White*:
   $$\frac{1}{\sqrt{0.01221}} = 9.050$$
   $$-2 \log_{10}\left(2.027 \times 10^{-5} + \frac{2.51}{2.536 \times 10^6 \times \sqrt{0.01221}}\right) = -2 \log_{10}(2.027 \times 10^{-5} + 8.95 \times 10^{-6}) = 9.068$$
   Error is $< 0.2\%$. $f = 0.0122$ is verified.

3. **Major & Minor Head Losses**:
   * Friction Loss ($h_f$):
     $$h_f = f \frac{L}{D}\frac{v^2}{2g} = 0.01221 \times \frac{1800}{0.60} \times 0.918 = 0.01221 \times 3000 \times 0.918 = \mathbf{33.626\text{ m}}$$
   * Minor Loss Sum ($\sum K_L$):
     $$\sum K_L = K_{\text{intake}} + K_{\text{trash}} + 4(K_{\text{bend}}) + 2(K_{\text{valve}}) + K_{\text{exit}}$$
     $$\sum K_L = 0.08 + 0.15 + 4(0.20) + 2(0.15) + 1.00 = 0.08 + 0.15 + 0.80 + 0.30 + 1.00 = \mathbf{2.33}$$
     $$\sum h_m = \left(\sum K_L\right)\frac{v^2}{2g} = 2.33 \times 0.918 = \mathbf{2.139\text{ m}}$$

4. **Total System Loss & Residual Energy**:
   Total pipeline head loss:
   $$h_{L,\text{total}} = h_f + \sum h_m = 33.626 + 2.139 = \mathbf{35.765\text{ m}}$$
   Total available gross static head:
   $$\Delta Z = Z_1 - Z_2 = 450.0 - 390.0 = \mathbf{60.00\text{ m}}$$

5. **Valve Dissipation Requirement**:
   Because available static head ($60.00\text{ m}$) exceeds pipeline natural friction/minor resistance ($35.765\text{ m}$), unrestrained gravity flow would accelerate to a higher discharge. To maintain design discharge at $Q = 1.20\text{ m}^3\text{/s}$, the control valve must dissipate:
   $$H_{\text{valve}} = \Delta Z - h_{L,\text{total}} = 60.00 - 35.765 = \mathbf{24.235\text{ m}}$$
   The equivalent loss coefficient required of the throttling valve is:
   $$K_{\text{throttle}} = \frac{H_{\text{valve}}}{v^2 / (2g)} = \frac{24.235}{0.918} = \mathbf{26.4}$$


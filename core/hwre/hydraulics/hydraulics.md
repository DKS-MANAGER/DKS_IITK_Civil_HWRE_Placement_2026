# Hydraulics

## Scope

Hydraulics covers the behavior of fluids at rest and in motion, with emphasis on pipe systems, open channels, pumps, turbines, and the forces exerted by fluids on structures.

> **Related topics:** [`turbulence-modeling.md`](turbulence-modeling.md) · [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md)

---

## Fundamental Principles

### Governing Equations

#### 1. Continuity Equation (Mass Conservation)
For incompressible flow:
$$A_1 V_1 = A_2 V_2 = Q = \text{constant}$$

**Derivation:**
- Apply conservation of mass to a control volume: $\frac{\partial}{\partial t} \int_{CV} \rho \, dV + \int_{CS} \rho (\vec{V} \cdot \hat{n}) \, dA = 0$
- For steady, incompressible flow: $\int_{CS} (\vec{V} \cdot \hat{n}) \, dA = 0$
- For a pipe with varying cross-section: $A_1 V_1 = A_2 V_2$

#### 2. Bernoulli Equation (Energy Conservation)
$$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L$$

**Assumptions:**
- Steady flow
- Incompressible fluid
- Frictionless flow (inviscid)
- Along a streamline

**Derivation from Euler's equation:**
- Euler's equation along a streamline: $\frac{dP}{\rho} + V \, dV + g \, dz = 0$
- Integrate: $\frac{P}{\rho} + \frac{V^2}{2} + gz = \text{constant}$
- Divide by $g$: $\frac{P}{\gamma} + \frac{V^2}{2g} + z = \text{constant}$

**Physical interpretation:**
- $\frac{P}{\gamma}$ = pressure head (energy per unit weight from pressure)
- $\frac{V^2}{2g}$ = velocity head (kinetic energy per unit weight)
- $z$ = elevation head (potential energy per unit weight)
- Sum = total hydraulic head

#### 3. Momentum Equation (Force Balance)
$$\sum \vec{F} = \rho Q (\vec{V}_2 - \vec{V}_1)$$

**Applications:**
- Force on bends, expansions, contractions
- Impact of jets on plates (flat, inclined, curved)
- Hydrostatic force on gates and sluices
- Reaction forces in pipe flow

---

### Flow Regimes

| Regime | Reynolds Number | Characteristics |
|--------|----------------|-----------------|
| **Laminar** | Re < 2000 | Smooth, orderly; viscous forces dominate |
| **Transitional** | 2000 < Re < 4000 | Intermittent; sensitive to disturbances |
| **Turbulent** | Re > 4000 | Chaotic mixing; inertial forces dominate |

**Reynolds Number:**
$$Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$$

---

### Pipe Flow & Friction

#### Darcy-Weisbach Equation
$$h_f = f \frac{L}{D} \frac{V^2}{2g}$$

Where:
- $h_f$ = head loss due to friction (m)
- $f$ = Darcy friction factor (dimensionless)
- $L$ = pipe length (m)
- $D$ = pipe diameter (m)
- $V$ = mean velocity (m/s)

**Derivation from dimensional analysis:**
- Head loss depends on: $\rho, V, D, L, \epsilon, \mu$
- By Buckingham Pi: $h_f / (V^2/2g) = \phi(Re, \epsilon/D)$
- This gives: $f = \phi(Re, \epsilon/D)$ → the Moody diagram

#### Moody Diagram
- Laminar region: $f = 64/Re$ (exact, from Hagen-Poiseuille)
- Transition zone: $f$ depends on both $Re$ and $\epsilon/D$
- Fully turbulent zone: $f$ depends only on $\epsilon/D$ (roughness)

#### Colebrook-White Equation (Implicit)
$$\frac{1}{\sqrt{f}} = -2 \log\left(\frac{\epsilon/D}{3.7} + \frac{2.51}{Re\sqrt{f}}\right)$$

#### Swamee-Jain (Explicit Approximation)
$$f = \frac{0.25}{\left[\log\left(\frac{\epsilon/D}{3.7} + \frac{5.74}{Re^{0.9}}\right)\right]^2}$$

#### Minor Losses
$$h_m = K \frac{V^2}{2g}$$

| Fitting | K Value |
|---------|---------|
| Sharp entrance | 0.5 |
| Rounded entrance | 0.05 |
| Sudden expansion | $(1 - A_1/A_2)^2$ |
| Sudden contraction | $0.5(1 - A_2/A_1)$ |
| 90° elbow (standard) | 0.3–0.9 |
| Gate valve (fully open) | 0.2 |
| Globe valve (fully open) | 10 |

#### Hazen-Williams Formula
$$V = 1.318 \, C \, R^{0.63} \, S^{0.54}$$

- $C$ = Hazen-Williams roughness coefficient (100–140 for pipes)
- $R$ = hydraulic radius (m)
- $S$ = energy slope

#### Manning's Formula
$$V = \frac{1}{n} R^{2/3} S^{1/2}$$

---

### Boundary Layers

| Parameter | Definition |
|-----------|------------|
| Boundary layer thickness $\delta$ | Distance from wall where $V = 0.99 V_\infty$ |
| Displacement thickness $\delta^*$ | $\delta^* = \int_0^\delta (1 - V/V_\infty) \, dy$ |
| Momentum thickness $\theta$ | $\theta = \int_0^\delta (V/V_\infty)(1 - V/V_\infty) \, dy$ |
| Shape factor $H$ | $H = \delta^*/\theta$ |

**Separation criteria:**
- Occurs when $\partial P/\partial x > 0$ (adverse pressure gradient)
- $\tau_w = 0$ at separation point
- Boundary layer thickens, reverses, and detaches

---

### Pumps & Turbines

#### Pump Characteristics
- **Head-capacity curve:** $H$ vs $Q$ — decreases with increasing $Q$
- **Efficiency curve:** Peak at Best Efficiency Point (BEP)
- **Power curve:** $P = \gamma Q H / \eta$

#### Affinity Laws
For geometrically similar pumps at different speeds ($N$) or diameters ($D$):

| Parameter | Speed Change | Diameter Change |
|-----------|-------------|-----------------|
| $Q$ | $Q_2/Q_1 = N_2/N_1$ | $Q_2/Q_1 = (D_2/D_1)^3$ |
| $H$ | $H_2/H_1 = (N_2/N_1)^2$ | $H_2/H_1 = (D_2/D_1)^2$ |
| $P$ | $P_2/P_1 = (N_2/N_1)^3$ | $P_2/P_1 = (D_2/D_1)^5$ |

#### Specific Speed
$$N_s = \frac{N \sqrt{Q}}{H^{3/4}}$$

| Type | $N_s$ Range |
|------|------------|
| Pelton (impulse) | 10–35 |
| Francis (reaction) | 30–100 |
| Kaplan (axial) | 100–300 |

#### NPSH (Net Positive Suction Head)
$$NPSH_A = \frac{P_{atm}}{\gamma} - \frac{P_v}{\gamma} - h_s - h_f$$

- Must have $NPSH_A > NPSH_R$ (required) to avoid cavitation

---

### Forces on Immersed Bodies

#### Drag Force
$$F_D = \frac{1}{2} C_D \rho A V^2$$

| Drag Component | Source |
|----------------|--------|
| Form (pressure) drag | Pressure difference upstream vs downstream |
| Skin friction drag | Viscous shear along the surface |
| Wave drag | Surface wave generation (ships) |

#### Lift Force
$$F_L = \frac{1}{2} C_L \rho A V^2$$

- Generated by pressure differential (e.g., airfoil)
- $C_L$ depends on angle of attack, shape, and Re

---

## Dimensional Analysis & Similitude

### Buckingham Pi Theorem
For $n$ variables with $m$ fundamental dimensions, there are $n - m$ dimensionless groups.

### Key Dimensionless Numbers

| Number | Definition | Significance |
|--------|-----------|--------------|
| **Reynolds** $Re$ | $\rho V L / \mu$ | Inertial / viscous forces |
| **Froude** $Fr$ | $V / \sqrt{gL}$ | Inertial / gravitational forces |
| **Weber** $We$ | $\rho V^2 L / \sigma$ | Inertial / surface tension |
| **Mach** $Ma$ | $V / c$ | Flow / speed of sound |
| **Euler** $Eu$ | $\Delta P / (\rho V^2)$ | Pressure / inertial forces |

### Model Testing Requirements
1. **Geometric similarity:** Same shape (all length ratios equal)
2. **Kinematic similarity:** Same velocity ratios (streamline patterns similar)
3. **Dynamic similarity:** Same force ratios (Re, Fr, We matched)

---

## Worked Examples

### Example 1: Bernoulli with Friction Loss
**Problem:** Water flows from a reservoir ($H = 10$ m) through a pipe ($L = 100$ m, $D = 0.2$ m, $f = 0.03$) to atmosphere. Find discharge.

**Solution:**
1. Apply Bernoulli from reservoir surface (1) to pipe exit (2):
   $$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_f$$
2. $P_1 = P_2 = P_{atm}$, $V_1 \approx 0$ (large reservoir), $z_1 - z_2 = 10$ m
3. $10 = \frac{V^2}{2g} + f \frac{L}{D} \frac{V^2}{2g} = \frac{V^2}{2g}\left(1 + f\frac{L}{D}\right)$
4. $10 = \frac{V^2}{2 \times 9.81}\left(1 + 0.03 \times \frac{100}{0.2}\right) = \frac{V^2}{19.62}(1 + 15) = \frac{16V^2}{19.62}$
5. $V^2 = \frac{10 \times 19.62}{16} = 12.26$ → $V = 3.50$ m/s
6. $Q = A \times V = \frac{\pi (0.2)^2}{4} \times 3.50 = 0.110$ m³/s

### Example 2: Pipe Network (Hardy Cross)
**Problem:** Simple loop with $L_1 = 500$ m, $D_1 = 0.3$ m, $L_2 = 600$ m, $D_2 = 0.25$ m, initial $Q_1 = 0.1$ m³/s, $Q_2 = -0.1$ m³/s, $f = 0.02$.

**Solution:**
1. Compute head loss: $h_f = f \frac{L}{D} \frac{Q^2}{2gA^2}$ for each pipe
2. $A_1 = \pi(0.3)^2/4 = 0.0707$ m², $A_2 = \pi(0.25)^2/4 = 0.0491$ m²
3. $h_{f1} = 0.02 \times \frac{500}{0.3} \times \frac{(0.1)^2}{2 \times 9.81 \times (0.0707)^2} = 0.340$ m
4. $h_{f2} = 0.02 \times \frac{600}{0.25} \times \frac{(0.1)^2}{2 \times 9.81 \times (0.0491)^2} = 1.013$ m
5. Correction: $\Delta Q = -\frac{\sum h_f}{\sum |h_f/Q|} = -\frac{0.340 - 1.013}{0.340/0.1 + 1.013/0.1} = \frac{0.673}{13.53} = 0.0498$ m³/s
6. Updated: $Q_1 = 0.150$, $Q_2 = -0.050$
7. Iterate until $\sum h_f < 0.01$ m

### Example 3: Pump Selection
**Problem:** Pump water at $Q = 0.05$ m³/s from a lower reservoir to an upper reservoir at $\Delta z = 20$ m through $L = 500$ m, $D = 0.15$ m, $f = 0.025$. Find required pump head.

**Solution:**
1. $V = Q/A = 0.05 / (\pi \times 0.15^2 / 4) = 2.83$ m/s
2. $h_f = 0.025 \times \frac{500}{0.15} \times \frac{(2.83)^2}{2 \times 9.81} = 34.0$ m
3. $H_{pump} = \Delta z + h_f = 20 + 34.0 = 54.0$ m
4. Power: $P = \gamma Q H / \eta = 9810 \times 0.05 \times 54.0 / 0.75 = 35.3$ kW

---

## 🎤 Interview Q&A

### Q1: What are the assumptions of Bernoulli's equation?
**A:** Steady flow, incompressible fluid, frictionless (inviscid) flow, along a streamline. In practice, we add a head loss term $h_L$ to account for friction and minor losses.

### Q2: What is the physical significance of the Reynolds number?
**A:** It represents the ratio of inertial forces to viscous forces. At low Re (< 2000), viscous forces dominate and flow is laminar. At high Re (> 4000), inertial forces dominate and flow is turbulent. The transition regime (2000–4000) is sensitive to disturbances.

### Q3: Explain the Moody diagram.
**A:** The Moody diagram plots the Darcy friction factor $f$ against Reynolds number $Re$ for various relative roughness values $\epsilon/D$. In the laminar region, $f = 64/Re$. In the transition zone, $f$ depends on both $Re$ and $\epsilon/D$ (Colebrook-White equation). In the fully turbulent zone, $f$ depends only on $\epsilon/D$.

### Q4: What is the difference between Darcy and Fanning friction factors?
**A:** The Darcy friction factor $f_D$ is used in $h_f = f_D (L/D)(V^2/2g)$. The Fanning friction factor $f_F = f_D/4$. The Fanning factor is commonly used in chemical engineering, while the Darcy factor is standard in civil/hydraulics engineering.

### Q5: How do you select between centrifugal and positive displacement pumps?
**A:** Centrifugal pumps: high flow, low-to-moderate head, continuous operation, self-priming not required. Positive displacement pumps: low flow, high head, viscous fluids, self-priming. Selection depends on flow rate, head, fluid viscosity, and system requirements.

### Q6: What is cavitation and how do you prevent it?
**A:** Cavitation occurs when local pressure drops below vapor pressure, causing vapor bubble formation and collapse. Prevention: ensure $NPSH_A > NPSH_R$, lower pump elevation relative to source, reduce suction pipe losses, increase suction pipe diameter.

### Q7: Explain the Hardy Cross method for pipe networks.
**A:** It's an iterative method for solving looped pipe networks. Assume flow rates satisfying continuity at each junction. Compute head loss around each loop. Apply correction $\Delta Q = -\sum h_f / \sum |h_f/Q|$. Repeat until corrections are negligible. Converges for networks with moderate loops.

---

## Software & Computational Tools

| Tool | Primary Use |
|------|-------------|
| HEC-RAS | River and open channel hydraulic modeling |
| WaterGEMS | Water distribution system analysis |
| EPANET | Pipe network analysis and water quality |
| InfoWater Pro | GIS-integrated water distribution modeling |
| Flow 3D | CFD for hydraulic and hydro-geological modeling |
| OpenFOAM | Open-source CFD for complex flow problems |

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Continuity | $A_1V_1 = A_2V_2$ | Mass conservation |
| Bernoulli | $\frac{P}{\gamma} + \frac{V^2}{2g} + z = \text{const}$ | Energy conservation |
| Darcy-Weisbach | $h_f = f\frac{L}{D}\frac{V^2}{2g}$ | Pipe friction loss |
| Manning | $V = \frac{1}{n}R^{2/3}S^{1/2}$ | Open channel velocity |
| Hazen-Williams | $V = 1.318CR^{0.63}S^{0.54}$ | Water pipe design |
| Power | $P = \gamma QH / \eta$ | Pump power required |
| NPSH | $NPSH_A = \frac{P_{atm}}{\gamma} - \frac{P_v}{\gamma} - h_s - h_f$ | Cavitation check |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Fluid properties        →  Pipe flow analysis        →  Pipe network (Hardy Cross)  →  Bernoulli derivation
Hydrostatics            →  Moody diagram             →  Unsteady flow               →  Why assumptions fail
Continuity              →  Minor losses              →  Boundary layer theory       →  Cavitation/NPSH
Energy equation         →  Pump selection            →  Drag & lift on bodies       →  Affinity laws
Momentum equation       →  Manning/Hazen-Williams    →  Dimensional analysis        →  Darcy vs Fanning
Reynolds/Froude         →  Pump curves & BEP         →  Model testing/similitude    →  Network analysis
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `HWRE` `CFD`

---

## 📋 Formula Sheet

<details>
<summary><strong>Click to expand — Complete Hydraulics Formula Sheet</strong></summary>

| Formula | Equation | Variables | Units | Conditions | Interview Importance |
|---------|----------|-----------|-------|------------|---------------------|
| Continuity | $A_1V_1 = A_2V_2$ | $A$=area, $V$=velocity | m², m/s | Steady, incompressible | ⭐⭐⭐ |
| Bernoulli | $\frac{P}{\gamma} + \frac{V^2}{2g} + z = \text{const}$ | $P$=pressure, $\gamma$=specific weight, $z$=elevation | m | Steady, incompressible, inviscid, along streamline | ⭐⭐⭐ |
| Energy (with loss) | $\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L$ | $h_L$=total head loss | m | Real fluids | ⭐⭐⭐ |
| Darcy-Weisbach | $h_f = f\frac{L}{D}\frac{V^2}{2g}$ | $f$=Darcy friction factor, $L$=length, $D$=diameter | m | Pipe flow (all regimes) | ⭐⭐⭐ |
| Colebrook-White | $\frac{1}{\sqrt{f}} = -2\log\left(\frac{\epsilon/D}{3.7} + \frac{2.51}{Re\sqrt{f}}\right)$ | $\epsilon$=roughness | — | Implicit; iter. or Moody | ⭐⭐ |
| Swamee-Jain | $f = \frac{0.25}{\left[\log\left(\frac{\epsilon/D}{3.7} + \frac{5.74}{Re^{0.9}}\right)\right]^2}$ | Same as above | — | Explicit approximation | ⭐⭐ |
| Manning | $V = \frac{1}{n}R^{2/3}S^{1/2}$ | $n$=Manning coeff, $R$=hyd. radius, $S$=slope | m/s | Open channel uniform flow | ⭐⭐⭐ |
| Hazen-Williams | $V = 1.318CR^{0.63}S^{0.54}$ | $C$=H-W coefficient | m/s | Water pipes only | ⭐⭐ |
| Pump Power | $P = \frac{\gamma QH}{\eta}$ | $\eta$=efficiency | W or kW | Pump sizing | ⭐⭐⭐ |
| Specific Speed | $N_s = \frac{N\sqrt{Q}}{H^{3/4}}$ | $N$=rpm, $Q$=discharge, $H$=head | — | Pump/turbine classification | ⭐⭐ |
| NPSH | $NPSH_A = \frac{P_{atm}}{\gamma} - \frac{P_v}{\gamma} - h_s - h_f$ | $P_v$=vapor pressure | m | Cavitation check | ⭐⭐⭐ |
| Reynolds | $Re = \frac{\rho VD}{\mu} = \frac{VD}{\nu}$ | $\nu$=kinematic viscosity | — | Flow regime determination | ⭐⭐⭐ |
| Euler Buckling | $P_{cr} = \frac{\pi^2EI}{(KL)^2}$ | $K$=end condition factor | N | Column design | ⭐⭐ |
| Drag Force | $F_D = \frac{1}{2}C_D\rho AV^2$ | $C_D$=drag coefficient | N | External flow | ⭐⭐ |
| Minor Loss | $h_m = K\frac{V^2}{2g}$ | $K$=loss coefficient | m | Fittings, entrances | ⭐⭐ |

**Commonly Confused Pairs:**
- **Bernoulli vs Energy Equation:** Bernoulli assumes no friction; Energy Equation includes $h_L$
- **Darcy vs Fanning:** $f_D = 4f_F$; Darcy standard in civil, Fanning in chemical engineering
- **Manning vs Hazen-Williams:** Manning适用于open channel & closed conduit; H-W designed for water supply pipes only
- **Pressure head vs Velocity head:** $P/\gamma$ (flow work) vs $V^2/2g$ (kinetic energy)
- **Specific energy vs Total energy:** Specific = $y + V^2/2g$ (OCF context); Total = $P/\gamma + V^2/2g + z$

</details>

---

## ❓ Question Bank

### A. Basic Concept Questions

1. What is Reynolds number and what forces does it compare?
2. State the assumptions of Bernoulli's equation.
3. What is the difference between laminar and turbulent flow?
4. Define Darcy friction factor. How does it differ from Fanning friction factor?
5. What is the Moody diagram and how do you use it?
6. What is boundary layer thickness?
7. Explain the concept of hydraulic grade line (HGL) and energy grade line (EGL).
8. What are minor losses in pipe flow?
9. Define specific speed of a pump. What does it classify?
10. What is NPSH and why is it important?

### B. WHY Questions

1. **Why** is Bernoulli's equation valid only along a streamline?
   - Because the derivation integrates Euler's equation along a streamline path; pressure work and elevation change are path-dependent in general flow.

2. **Why** does the friction factor decrease with increasing Reynolds number in the laminar regime?
   - Because viscous effects dominate: $f = 64/Re$, so as Re increases, the relative viscous resistance decreases.

3. **Why** is the transition Reynolds number not sharply defined?
   - Because transition depends on inlet conditions, surface roughness, vibration, and disturbances; it can occur anywhere from Re ≈ 2000 to 4000 in pipes.

4. **Why** do engineers prefer Darcy-Weisbach over Hazen-Williams?
   - Darcy-Weisbach is theoretically derived (dimensional analysis), applicable to all fluids and all flow regimes; H-W is empirical, valid only for water at normal temperatures.

5. **Why** does cavitation damage occur even when the average pressure is above vapor pressure?
   - Because local pressure drops (at bends, constrictions, impeller tips) can fall below $P_v$ even when bulk pressure is adequate.

6. **Why** does increasing pipe diameter reduce head loss for the same discharge?
   - For constant $Q$: $V \propto 1/D^2$, so $V^2 \propto 1/D^4$, and $h_f \propto V^2/D \propto 1/D^5$.

### C. WHAT-IF Questions

1. **What happens** if pipe diameter is doubled while keeping discharge constant?
   - $V$ decreases by factor of 4, $h_f$ decreases by factor of ~32 (massive energy savings).

2. **What happens** if roughness increases?
   - Friction factor increases (especially in fully turbulent regime), head loss increases, pump must work harder.

3. **What happens** if fluid viscosity decreases?
   - Re increases, flow may transition to turbulent, friction factor changes (laminar: decreases; turbulent: depends on roughness).

4. **What happens** if you suddenly close a valve in a long pipe?
   - Water hammer: pressure surge $\Delta P = \rho c \Delta V$, wave propagates at speed $c$, can cause pipe rupture.

5. **What happens** if two pumps are connected in series vs parallel?
   - Series: heads add (for high-head applications). Parallel: discharges add (for high-flow applications).

### D. Comparison Questions

| Concept A | Concept B | Key Difference | Application |
|-----------|-----------|----------------|-------------|
| Laminar flow | Turbulent flow | Re < 2000 vs > 4000; orderly vs chaotic | Pipe design, heat transfer |
| Darcy friction | Fanning friction | $f_D = 4f_F$ | Civil vs chemical engineering |
| Manning | Hazen-Williams | Theoretical vs empirical; open channel vs pipes | OCF vs water supply |
| Pressure head | Velocity head | $P/\gamma$ vs $V^2/2g$ | Energy analysis |
| HGL | EGL | Piezometric vs total head; EGL always above HGL | Pipeline design |
| Steady flow | Unsteady flow | $\partial/\partial t = 0$ vs $\neq 0$ | Daily operation vs transients |
| Centrifugal pump | Positive displacement pump | High flow/low head vs low flow/high head | System selection |
| Series pumps | Parallel pumps | Add heads vs add flows | System curve matching |

### E. Numerical Questions

**Easy:**

**Problem:** Water flows through a 100 mm diameter pipe at 2 m/s. Find Reynolds number. (ν = 1×10⁻⁶ m²/s)
- **Given:** $D = 0.1$ m, $V = 2$ m/s, $\nu = 10^{-6}$ m²/s
- **Find:** $Re$
- **Approach:** $Re = VD/\nu$
- **Solution:** $Re = 2 \times 0.1 / 10^{-6} = 2 \times 10^5$
- **Final Answer:** $Re = 200,000$ (turbulent)
- **Concept Tested:** Reynolds number calculation
- **Common Trap:** Forgetting to convert mm to m

**Medium:**

**Problem:** A pipe (L=500m, D=0.3m, ε=0.15mm) carries water at Q=0.1 m³/s. Find head loss using Darcy-Weisbach.
- **Given:** $L=500$ m, $D=0.3$ m, $\epsilon=0.15$ mm, $Q=0.1$ m³/s
- **Find:** $h_f$
- **Approach:** Find $V$, $Re$, $\epsilon/D$, read $f$ from Moody/Swamee-Jain, compute $h_f$
- **Solution:**
  - $A = \pi(0.3)^2/4 = 0.0707$ m², $V = 0.1/0.0707 = 1.415$ m/s
  - $Re = 1.415 \times 0.3 / 10^{-6} = 4.25 \times 10^5$
  - $\epsilon/D = 0.0005$
  - Swamee-Jain: $f = 0.25/[\log(0.0005/3.7 + 5.74/(4.25\times10^5)^{0.9})]^2 = 0.0173$
  - $h_f = 0.0173 \times (500/0.3) \times (1.415^2/19.62) = 2.89$ m
- **Final Answer:** $h_f = 2.89$ m
- **Concept Tested:** Darcy-Weisbach with Moody/Swamee-Jain
- **Common Trap:** Using Fanning friction factor instead of Darcy

**Hard:**

**Problem:** Two reservoirs are connected by a pipe system. Reservoir A is at 50 m elevation, Reservoir B at 20 m. Pipe 1: L=1000m, D=0.4m, f=0.02. Pipe 2: L=800m, D=0.3m, f=0.025. Both pipes in series. Find discharge and power required if a pump adds 40 m of head.
- **Given:** $\Delta z = 30$ m, $H_{pump} = 40$ m
- **Find:** $Q$, $P$
- **Approach:** $H_{pump} + \Delta z = h_{f1} + h_{f2} + V_2^2/2g$; iterate for $Q$
- **Solution:** Total driving head = $40 + (50-20) = 70$ m. Express both $h_f$ in terms of $Q$: $h_{f1} = 8f_1L_1Q^2/(g\pi^2D_1^5)$, $h_{f2} = 8f_2L_2Q^2/(g\pi^2D_2^5)$. Solve $70 = C_1Q^2 + C_2Q^2$. $Q \approx 0.196$ m³/s. Power $= 9810 \times 0.196 \times 40 / 0.75 = 102.4$ kW.
- **Final Answer:** $Q \approx 0.196$ m³/s, $P \approx 102$ kW
- **Concept Tested:** Series pipe systems with pump
- **Common Trap:** Forgetting exit loss or velocity head at discharge

### F. Rapid-Fire Questions (30+)

Q: What is the Darcy friction factor for laminar flow?
A: $f = 64/Re$

Q: What is the critical Reynolds number for pipe flow?
A: ~2000 (laminar to transition), ~4000 (transition to turbulent)

Q: State Bernoulli's equation in words.
A: Pressure head + velocity head + elevation head = constant (along a streamline, for inviscid flow)

Q: What is the unit of specific weight?
A: N/m³

Q: What is the hydraulic radius of a full circular pipe?
A: $R = D/4$

Q: What is the difference between a pump curve and a system curve?
A: Pump curve: $H$ vs $Q$ (pump characteristic). System curve: required $H$ vs $Q$ (pipe losses + static head). Intersection = operating point.

Q: What is BEP?
A: Best Efficiency Point — where pump efficiency is maximum; design operating point.

Q: Name 3 types of pumps.
A: Centrifugal (radial, axial, mixed), reciprocating (piston, diaphragm), rotary (screw, gear).

Q: What is water hammer?
A: Pressure surge from sudden flow change (valve closure). $\Delta P = \rho c \Delta V$ (Joukowsky equation).

Q: What is the wave speed in water hammer?
A: $c = \sqrt{E_{bulk}/\rho} / \sqrt{1 + (D/t)(E_{bulk}/E_{pipe})}$, typically 1000–1400 m/s in steel pipes.

Q: What is the Hagen-Poiseuille equation?
A: $Q = \pi R^4 \Delta P / (8\mu L)$ for laminar pipe flow.

Q: What is the velocity profile for laminar pipe flow?
A: Parabolic: $u(r) = (\Delta P/4\mu L)(R^2 - r^2)$, $V_{max} = 2\bar{V}$

Q: What is the velocity profile for turbulent pipe flow?
A: Log-law: $u^+ = (1/\kappa)\ln(y^+) + 5.0$; flatter than laminar, $V_{max}/\bar{V} \approx 1.2$

Q: Define displacement thickness.
A: $\delta^* = \int_0^\delta (1 - V/V_\infty) dy$ — the distance by which the free stream is "displaced" outward.

Q: What is form drag vs skin friction drag?
A: Form drag: pressure difference (shape-dependent). Skin friction: viscous shear (surface-dependent). Streamlining reduces form drag.

Q: What is the drag coefficient for a sphere at high Re?
A: $C_D \approx 0.4$–$0.5$ (subcritical); drops to ~0.1 at Re > 3×10⁵ (drag crisis).

Q: When does flow separation occur?
A: When $\partial P/\partial x > 0$ (adverse pressure gradient) — boundary layer velocity reaches zero and reverses.

Q: What is the Magnus effect?
A: Lift force on a spinning cylinder/sphere due to asymmetric boundary layer development and pressure distribution.

Q: What is Reynolds analogy?
A: Relates momentum transfer (friction) to heat/mass transfer: $C_f/2 = St$ (Stanton number), valid for turbulent boundary layers.

Q: What is the Buckingham Pi theorem?
A: For $n$ variables with $m$ fundamental dimensions, there are $n-m$ independent dimensionless groups.

Q: What is the Froude number physically?
A: Ratio of inertial to gravitational forces; governs free-surface flow regime.

Q: What is the Weber number?
A: Ratio of inertial to surface tension forces; important for droplets, bubbles, and capillary flows.

Q: What is the Mach number?
A: Ratio of flow velocity to speed of sound; compressibility effects become significant at Ma > 0.3.

Q: What is geometric similarity?
A: All length ratios between model and prototype are equal.

Q: What is dynamic similarity?
A: All force ratios (Re, Fr, We) between model and prototype are equal.

Q: What is a surge tank?
A: A standpipe near a turbine/pump that absorbs pressure transients (water hammer) and provides temporary storage.

Q: What is the difference between a turbine and a pump?
A: Turbine: extracts energy from fluid (flow → shaft power). Pump: adds energy to fluid (shaft power → flow).

Q: What is cavitation inception?
A: The point where local pressure first drops below vapor pressure, forming the first vapor bubbles; occurs at leading edges and low-pressure zones.

Q: What is a Moody diagram?
A: A log-log chart of $f$ vs $Re$ for various $\epsilon/D$, showing laminar, transition, and fully turbulent zones.

Q: What is the significance of the entrance length?
A: Distance for flow to become fully developed. Laminar: $L_e/D \approx 0.06Re$. Turbulent: $L_e/D \approx 10$–$60$ (less Re-dependent).

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the Hagen-Poiseuille equation from the Navier-Stokes equations. What assumptions are required?**
   - Start with N-S in cylindrical coordinates, assume steady, fully developed ($\partial u/\partial x = 0$), axisymmetric ($\partial/\partial\theta = 0$), no-slip at $r = R$. The momentum equation reduces to $\partial P/\partial x = \mu(1/r)\partial(r\partial u/\partial r)/\partial r$. Integrate twice with boundary conditions. Result: parabolic profile.

2. **Why is the Colebrook-White equation implicit? How does the Swamee-Jain equation compare in accuracy?**
   - Colebrook-White: $1/\sqrt{f} = -2\log(\epsilon/(3.7D) + 2.51/(Re\sqrt{f}))$ — $f$ appears on both sides. Swamee-Jain provides explicit approximation with <1% error for $4000 < Re < 10^8$ and $0.00001 < \epsilon/D < 0.05$.

3. **How would you modify the energy equation for compressible flow?**
   - For high-speed flow (Ma > 0.3), density changes significantly. Use: $h_1 + V_1^2/2 = h_2 + V_2^2/2 + q$ (enthalpy form). Include $c_p\Delta T$ terms. For isentropic flow: $T_0/T = 1 + (\gamma-1)Ma^2/2$.

4. **Explain the concept of turbulence intensity and its measurement.**
   - $Tu = \sqrt{\overline{u'^2}}/\bar{U}$ — ratio of velocity fluctuation RMS to mean velocity. Measured by hot-wire anemometry (CTA), LDA, or pitot-static probe with high-frequency response. In boundary layers: Tu ~ 1–5%; in free streams: Tu ~ 0.1–1%.

5. **When does the Darcy-Weisbach equation become inaccurate?**
   - Highly transient flow (water hammer), non-Newtonian fluids, very low Re (creeping flow), two-phase flow, open channel with variable roughness. For these cases, use N-S directly, power-law models, or CFD.

6. **How would you validate a CFD simulation of turbulent pipe flow?**
   - Compare velocity profiles with laser Doppler anemometry (LDA) or PIV data. Check friction factor against Colebrook-White. Verify y+ values (wall functions: 30–300; resolved: <5). Monitor residuals, mass balance, and grid convergence index (GCI).

---

## 🎤 Interview Answer Format

### High-Value Q1: "What is Bernoulli's equation?"

**30-second answer:**
"Bernoulli's equation states that for steady, incompressible, frictionless flow along a streamline, the sum of pressure head, velocity head, and elevation head is constant. It's a statement of energy conservation per unit weight of fluid."

**If interviewer asks deeper:**
"It's derived by integrating Euler's equation along a streamline. The key assumptions are: steady flow, incompressible fluid, inviscid (no friction), and along a streamline. For real flows, we add a head loss term to account for viscous dissipation and turbulence."

**Key equation:**
$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L$

**Engineering interpretation:**
"In a pipe system, if velocity increases (constriction), pressure must decrease (trade-off). This is the principle behind Venturi meters, nozzles, and explains why roofs lift off in storms."

---

### High-Value Q2: "Explain Reynolds number."

**30-second answer:**
"Reynolds number is the ratio of inertial forces to viscous forces in a flow. For pipe flow, Re < 2000 is laminar, > 4000 is turbulent. It determines which flow regime we're in and affects friction, heat transfer, and mixing."

**If interviewer asks deeper:**
"Physically, it tells us whether viscous forces can dampen perturbations (laminar) or whether inertial forces amplify them (turbulent). The transition isn't sharp because it depends on inlet conditions, surface roughness, and external disturbances."

**Key equation:**
$Re = \frac{\rho VD}{\mu} = \frac{VD}{\nu}$

**Engineering interpretation:**
"At typical water distribution velocities (1–2 m/s in 100mm pipes), Re ~ 10⁵, so flow is always turbulent. This means we must use turbulent friction factors, and mixing/diffusion are enhanced."

---

### High-Value Q3: "What is NPSH and why does it matter?"

**30-second answer:**
"NPSH is the net positive suction head — the difference between the total head at the pump suction and the vapor pressure head. Available NPSH must exceed the pump's required NPSH to prevent cavitation."

**If interviewer asks deeper:**
"Cavitation occurs when local pressure drops below vapor pressure, forming vapor bubbles that collapse violently near the impeller. This causes noise, vibration, efficiency drop, and material erosion. Prevention involves lowering pump elevation, reducing suction losses, or increasing suction pipe diameter."

**Key equation:**
$NPSH_A = \frac{P_{atm}}{\gamma} - \frac{P_v}{\gamma} - h_s - h_f > NPSH_R$

**Engineering interpretation:**
"A pump 5m above a reservoir at sea level has roughly 5m of available suction head. If the pump requires 7m NPSH, it will cavitate. This is why pump elevation relative to the source is critical in design."

---

## 🔗 Interviewer Follow-up Chain

```
Q1: "What is Reynolds number?"
    ↓
Q2: "What forces does it compare?"
    ↓ (inertial vs viscous)
Q3: "Why is the transition not sharply defined at exactly Re = 2000?"
    ↓ (depends on disturbances, roughness, inlet)
Q4: "How would pipe roughness affect the flow regime transition?"
    ↓ (roughness trips boundary layer, can trigger earlier turbulence)
Q5: "If the flow is turbulent, which friction-factor relation would you use?"
    ↓ (Colebrook-White / Moody / Swamee-Jain)
Q6: "Why is Darcy-Weisbach preferred over Manning for pipe flow?"
    ↓ (theoretical basis, all fluids, all regimes)
Q7: "How would you size a pump for this system?"
    ↓ (system curve + pump curve → operating point → check NPSH)
```

```
Q1: "What is cavitation?"
    ↓
Q2: "What causes local pressure to drop below vapor pressure?"
    ↓ (velocity increase at constrictions, elevation, bends)
Q3: "How do you prevent it in practice?"
    ↓ (NPSH_A > NPSH_R, lower pump, larger suction pipe)
Q4: "What happens to pump performance when cavitation occurs?"
    ↓ (head drops sharply, efficiency decreases, noise/vibration)
Q5: "Would you use CFD to predict cavitation? How?"
    ↓ ( Schnerr-Sauer model, volume fraction of vapor, Rayleigh-Plesset equation)
```

---

## 🔗 Cross-Links

- [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel flow applications
- [`hydrology.md`](../hydrology/hydrology.md) — Hydrology applications
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Water distribution systems
- [`turbulence-modeling.md`](turbulence-modeling.md) — CFD turbulence models
- [`sediment-transport.md`](../hydrology/sediment-transport.md) — Sediment-laden flow
- [`water-supply.md`](../water_supply/water-supply.md) — Water supply pipe networks
- [`wastewater-engineering.md`](../wastewater/wastewater-engineering.md) — Sewer hydraulics
- [`civil-engineering-foundations.md`](../../fundamentals/civil-engineering-foundations.md) — Quick revision formulas

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`turbulence-modeling.md`](turbulence-modeling.md) — Advanced turbulence for CFD applications
* [`../open_channel_flow/open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel flow companion

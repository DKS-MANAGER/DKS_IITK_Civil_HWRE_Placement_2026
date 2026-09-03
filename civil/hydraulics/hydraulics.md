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

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`turbulence-modeling.md`](turbulence-modeling.md) — Advanced turbulence for CFD applications
* [`../open_channel_flow/open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel flow companion

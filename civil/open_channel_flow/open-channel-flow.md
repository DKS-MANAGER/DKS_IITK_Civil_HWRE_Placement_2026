# Open Channel Flow

## Definition & Scope

Open channel flow occurs when a fluid flows with a free surface exposed to atmospheric pressure. It is distinguished from pipe flow by the presence of this free surface, which introduces additional complexity in terms of varying depth, width, and velocity distribution.

> **Related topics:** [`hydraulics.md`](../hydraulics/hydraulics.md) · [`hydrology.md`](../hydrology/hydrology.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md)

---

## Classification by Flow Regime

### Steady vs. Unsteady
- **Steady flow:** Depth and velocity do not change with time at a given location
- **Unsteady flow:** Depth and velocity vary with time; governs flood wave propagation

### Uniform vs. Varied
- **Uniform flow:** Depth, velocity, and cross-section remain constant along the channel (normal depth)
- **Gradually Varied Flow (GVF):** Depth changes slowly over a long distance; surface slope ≈ bed slope
- **Rapidly Varied Flow (RVF):** Depth changes abruptly over a short distance; examples include hydraulic jumps and drops

---

## Fundamental Equations

### Continuity Equation
- For unsteady flow: $\frac{\partial Q}{\partial x} + \frac{\partial A}{\partial t} = 0$
- For steady flow: $Q = A \cdot V = \text{constant}$ along the channel

### Momentum Equation — Saint-Venant Equations
The Saint-Venant equations form the foundation for unsteady open channel analysis:

**Conservation of mass:**
$$\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0$$

**Conservation of momentum:**
$$\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial y}{\partial x} + gA S_f = gA S_0$$

Where:
- $S_0$ = bed slope
- $S_f$ = friction slope (energy slope)
- $y$ = flow depth
- $A$ = cross-sectional area
- $Q$ = discharge

**Terms interpretation:**
- $\partial Q/\partial t$ = local acceleration
- $\partial(Q^2/A)/\partial x$ = convective acceleration
- $gA(\partial y/\partial x)$ = pressure gradient
- $gA S_f$ = friction force
- $gA S_0$ = gravity component

### Energy Equation — Specific Energy
$$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2gA^2}$$

**Key properties:**
- For rectangular channel: $E = y + \frac{q^2}{2gy^2}$ where $q = Q/b$
- Minimum specific energy: $E_{min} = \frac{3}{2} y_c$ (at critical depth)
- Critical depth for rectangular channel: $y_c = \left(\frac{q^2}{g}\right)^{1/3}$
- Alternate depths: Two possible depths for a given $E$ (subcritical and supercritical)

---

## Key Phenomena

### Hydraulic Jump

**Definition:** Sudden transition from supercritical to subcritical flow with significant energy dissipation.

**Conjugate depth relationship (rectangular channel):**
$$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right)$$

**Energy loss in jump:**
$$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$$

**Sequent force balance:**
$$\frac{y_2}{y_1} = \frac{1}{2}\left(-1 + \sqrt{1 + \frac{8q^2}{gy_1^3}}\right) = \frac{1}{2}\left(-1 + \sqrt{1 + 8Fr_1^2}\right)$$

**Classification by Froude number:**

| Jump Type | $Fr_1$ | Characteristics |
|-----------|--------|-----------------|
| Undular | 1.0–1.7 | Standing waves, minimal energy loss |
| Weak | 1.7–2.5 | Small roller, smooth surface |
| Oscillating | 2.5–4.5 | Unstable oscillation, wave propagation |
| Steady | 4.5–9.0 | Stable roller, good energy dissipation |
| Strong | > 9.0 | Churning, maximum energy dissipation |

**Applications:**
- Stilling basin design downstream of spillways
- Energy dissipation to prevent scour
- Flow measurement (indirectly)

### Critical Flow

**Froude number:**
$$Fr = \frac{V}{\sqrt{gD_h}} = 1$$

Where $D_h = A/T$ (hydraulic depth), $T$ = top width.

| Flow Regime | $Fr$ | Characteristics |
|-------------|------|-----------------|
| Subcritical | $< 1$ | Depth > critical depth; slow, deep flow; information propagates upstream |
| Critical | $= 1$ | Minimum specific energy; unstable flow |
| Supercritical | $> 1$ | Depth < critical depth; fast, shallow flow; information cannot propagate upstream |

**Critical depth for common sections:**

| Section | $y_c$ Formula |
|---------|---------------|
| Rectangular | $y_c = (q^2/g)^{1/3}$ |
| Trapezoidal | Solve $Q^2T/(gA^3) = 1$ iteratively |
| Triangular | $y_c = (2q^2/g)^{1/5}$ |
| Circular | Solve iteratively |

---

## Flow Profiles (GVF)

### Classification by Bed Slope

| Slope Type | Relationship | Normal Depth | Critical Depth |
|------------|-------------|--------------|----------------|
| **Mild (M)** | $S_0 < S_c$ | $y_n > y_c$ | Subcritical flow dominant |
| **Steep (S)** | $S_0 > S_c$ | $y_n < y_c$ | Supercritical flow dominant |
| **Critical (C)** | $S_0 = S_c$ | $y_n = y_c$ | Critical flow |
| **Horizontal (H)** | $S_0 = 0$ | $y_n = \infty$ | — |
| **Adverse (A)** | $S_0 < 0$ | No normal depth | — |

### GVF Profiles

| Zone | Condition | Profile | Description |
|------|-----------|---------|-------------|
| **1** | $y > y_n$ and $y > y_c$ | M1, S1, H1, A1 | Backwater curve (depth increases downstream) |
| **2** | Between $y_n$ and $y_c$ | M2, S2, H2, A2 | Drawdown curve (depth changes toward normal) |
| **3** | $y < y_n$ and $y < y_c$ | M3, S3, H3, A3 | Depth increases toward normal/critical |

**Profile behavior:**
- M1: Dam backwater — depth increases downstream (subcritical)
- M2: Drawdown at free overfall — depth decreases downstream (subcritical)
- S2: Flow approaching normal depth from supercritical
- M3: Flow after sluice gate — depth increases toward M2 transition

### GVF Governing Equation
$$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$$

**Physical interpretation:**
- When $S_0 = S_f$: $\frac{dy}{dx} = 0$ → uniform flow (normal depth)
- When $Fr = 1$: $\frac{dy}{dx} = \pm\infty$ → vertical tangent (critical depth)
- Denominator $1 - Fr^2$: determines profile type (subcritical vs supercritical)

---

## Manning's Equation
$$V = \frac{1}{n} R^{2/3} S^{1/2}$$
$$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$

Where:
- $n$ = Manning's roughness coefficient
- $R$ = hydraulic radius = $A/P$
- $S$ = energy slope (≈ bed slope for uniform flow)

**Typical n values:**

| Channel Type | n Range |
|-------------|---------|
| Finished concrete | 0.011–0.013 |
| Earth, straight | 0.018–0.025 |
| Natural channel, clean | 0.025–0.033 |
| Natural channel, vegetated | 0.035–0.070 |
| Floodplain, grass | 0.030–0.050 |

**Normal depth calculation (iterative):**
1. Assume $y_n$
2. Compute $A$, $P$, $R$
3. Compute $Q = \frac{1}{n} A R^{2/3} S^{1/2}$
4. Compare with target $Q$; adjust $y_n$

---

## Weirs & Flumes

### Sharp-Crested Weirs

| Type | Formula | Application |
|------|---------|-------------|
| **Rectangular** (suppressed) | $Q = C_d \frac{2}{3} \sqrt{2g} \, b \, H^{3/2}$ | General flow measurement |
| **Rectangular** (contracted) | $Q = C_d \frac{2}{3} \sqrt{2g} \, b \, H^{3/2}$ (with end contractions) | Side channels |
| **Triangular (V-notch)** | $Q = C_d \frac{8}{15} \sqrt{2g} \tan(\theta/2) \, H^{5/2}$ | Low flows, precision |
| **Cipolletti** | $Q = 1.86 \, b \, H^{3/2}$ | Trapezoidal notch, self-correcting |

### Broad-Crested Weirs
$$Q = C_d \cdot b \cdot \sqrt{g} \cdot \frac{2}{3} \left(\frac{2E}{3}\right)^{3/2}$$

- Critical depth occurs over the crest
- Used for flow measurement in open channels

### Flumes
- Parshall flume: Most common; head-discharge relationship
- Cutthroat flume: No throat section; simpler construction

---

## Sediment Transport in Open Channels
- Bed load and suspended load mechanisms — see [`sediment-transport.md`](../hydrology/sediment-transport.md)
- Critical tractive force (Shields parameter) for incipient motion
- Bed form evolution: Ripples → dunes → plane bed → antidunes

---

## Worked Examples

### Example 1: Hydraulic Jump
**Problem:** A rectangular channel carries $Q = 10$ m³/s with $y_1 = 0.5$ m, $b = 5$ m. Find the conjugate depth $y_2$ and energy loss.

**Solution:**
1. Velocity: $V_1 = Q/(b \cdot y_1) = 10/(5 \times 0.5) = 4$ m/s
2. Froude number: $Fr_1 = V_1/\sqrt{g y_1} = 4/\sqrt{9.81 \times 0.5} = 4/2.215 = 1.81$
3. Conjugate depth: $y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right) = \frac{0.5}{2}\left(\sqrt{1 + 8 \times 3.276} - 1\right) = 0.25(\sqrt{27.21} - 1) = 0.25(5.216 - 1) = 1.054$ m
4. Energy loss: $\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(1.054 - 0.5)^3}{4 \times 0.5 \times 1.054} = \frac{0.170}{2.108} = 0.081$ m
5. Check: $Fr_1 = 1.81$ → Weak jump (1.7–2.5 range)

### Example 2: Manning's Equation — Normal Depth
**Problem:** Design a trapezoidal channel to carry $Q = 50$ m³/s. Given $S = 0.001$, $n = 0.025$, side slope $z = 1.5$, bottom width $b = 10$ m. Find normal depth $y_n$.

**Solution:**
1. $A = (b + zy)y = (10 + 1.5y)y$
2. $P = b + 2y\sqrt{1+z^2} = 10 + 2y\sqrt{3.25} = 10 + 3.606y$
3. $R = A/P$
4. Manning: $Q = \frac{1}{n} A R^{2/3} S^{1/2}$
5. Iterate:
   - Try $y = 2.0$ m: $A = (10+3)(2) = 26$, $P = 10+7.21 = 17.21$, $R = 1.51$
     $Q = \frac{1}{0.025} \times 26 \times 1.51^{2/3} \times 0.001^{1/2} = 40 \times 26 \times 1.315 \times 0.0316 = 43.1$ m³/s (too low)
   - Try $y = 2.3$ m: $A = (10+3.45)(2.3) = 30.94$, $P = 10+8.30 = 18.30$, $R = 1.69$
     $Q = 40 \times 30.94 \times 1.69^{2/3} \times 0.0316 = 40 \times 30.94 \times 1.417 \times 0.0316 = 55.3$ m³/s (too high)
   - Interpolate: $y_n \approx 2.18$ m

### Example 3: GVF Profile Type
**Problem:** A mild-slope channel ($y_n = 3.0$ m, $y_c = 1.5$ m) has a dam at the downstream end raising water to 4.0 m. Determine the GVF profile.

**Solution:**
1. At the dam: $y = 4.0$ m > $y_n = 3.0$ m > $y_c = 1.5$ m
2. Zone 1 condition: $y > y_n$ and $y > y_c$
3. Profile: **M1** (backwater curve)
4. Behavior: Depth increases in the downstream direction (toward the dam)
5. The M1 profile extends upstream until it merges with normal depth

---

## 🎤 Interview Q&A

### Q1: What is the difference between specific energy and total energy?
**A:** Specific energy $E = y + V^2/(2g)$ is measured relative to the channel bed. Total energy $H = z + y + V^2/(2g)$ includes the bed elevation $z$. Specific energy is useful for analyzing flow transitions at a given cross-section, while total energy is used for energy balance along the channel.

### Q2: How do you determine the GVF profile type?
**A:** (1) Compute normal depth $y_n$ from Manning's equation. (2) Compute critical depth $y_c$. (3) Compare actual depth $y$ with $y_n$ and $y_c$. (4) Determine the slope type (mild/steep/critical/horizontal/adverse). (5) Determine the zone (1/2/3) based on $y$ vs $y_n$ vs $y_c$. (6) The profile type is the combination (e.g., M1, S2, M3).

### Q3: Explain the hydraulic jump and its engineering applications.
**A:** A hydraulic jump is the abrupt transition from supercritical ($Fr > 1$) to subcritical ($Fr < 1$) flow. It dissipates kinetic energy (10–60% depending on $Fr_1$), raises the water level, and mixes air. Engineering applications: (1) stilling basins downstream of spillways to prevent scour, (2) flow measurement, (3) mixing and aeration, (4) reducing flow velocity for irrigation canals.

### Q4: What is the significance of critical depth?
**A:** Critical depth is the depth at which specific energy is minimum for a given discharge. At critical depth: $Fr = 1$, the flow is unstable (surface waves propagate both upstream and downstream), and the discharge is maximum for a given specific energy. It controls flow transitions (e.g., over a broad-crested weir) and is used as a reference for classifying flow regimes.

### Q5: How does Manning's equation differ from Darcy-Weisbach for open channels?
**A:** Manning's equation $V = (1/n)R^{2/3}S^{1/2}$ is empirical, uses Manning's $n$ (which varies with depth and roughness), and is widely used for open channel design. Darcy-Weisbach $h_f = f(L/D)(V^2/2g)$ is theoretically grounded, uses the friction factor $f$ (function of Re and $\epsilon/D$), and is more accurate for a wide range of conditions. For open channels, the hydraulic diameter $D_h = 4R$ can be substituted, but Manning's remains more common in practice.

### Q6: What are the limitations of the Saint-Venant equations?
**A:** (1) 1D approximation — doesn't capture lateral variations, (2) hydrostatic pressure assumption — fails at hydraulic jumps and rapidly varied flows, (3) uniform velocity distribution — doesn't account for velocity profile effects, (4) quasi-steady friction — doesn't capture unsteady friction effects, (5) doesn't handle subcritical-supercritical transitions (need to couple with RVF models).

---

## Software Tools

| Tool | Application |
|------|-------------|
| HEC-RAS | 1D/2D river and open channel hydraulic modeling |
| MIKE FLOOD | Integrated 1D/2D flood modeling |
| TUFLOW | Hydrodynamic modeling for floodplain management |
| Flood Modeller | 1D/2D river, floodplain, and drainage modeling |
| SRH-2D | Two-dimensional sedimentation and river hydraulics |
| OpenFlows Flood | Coastal, riverine, and urban flood modeling |

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Specific Energy | $E = y + V^2/(2g)$ | Energy at a cross-section |
| Critical Depth (rect.) | $y_c = (q^2/g)^{1/3}$ | Critical flow reference |
| Manning | $V = (1/n)R^{2/3}S^{1/2}$ | Uniform flow velocity |
| Froude Number | $Fr = V/\sqrt{gD_h}$ | Flow regime classification |
| Conjugate Depth | $y_2/y_1 = 0.5(\sqrt{1+8Fr_1^2}-1)$ | Hydraulic jump |
| Energy Loss (jump) | $\Delta E = (y_2-y_1)^3/(4y_1y_2)$ | Jump energy dissipation |
| GVF Equation | $dy/dx = (S_0-S_f)/(1-Fr^2)$ | Flow profile computation |

---

## Design Applications
- Canal design for irrigation and drainage
- Culvert sizing and inlet/outlet control analysis
- Bridge scour assessment
- Floodplain delineation and zoning
- Stilling basin design (USBR Type I–IV)

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`hydraulics.md`](../hydraulics/hydraulics.md) — Pipe flow and fundamental hydraulics
* [`../hydrology/hydrology.md`](../hydrology/hydrology.md) — Flood routing and hydrograph analysis
* [`../water_resources/water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir and canal design

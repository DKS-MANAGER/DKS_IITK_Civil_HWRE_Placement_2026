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

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Free surface concept   →  Specific energy diagram    →  GVF computation (step method) →  Why Fr=1 is critical
Uniform flow           →  Manning's equation         →  Unsteady flood routing        →  Manning vs Darcy-Weisbach
Critical depth         →  Hydraulic jump analysis    →  Saint-Venant equations         →  Why jump dissipates energy
Froude number          →  GVF profile classification →  Morphological modeling         →  Energy vs momentum eqn
Manning's n            →  Weir and flume measurement →  Dam-break analysis             →  Specific energy diagram
Normal depth           →  Normal vs critical depth   →  Mobile-bed hydraulics          →  GVF profile identification
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `HWRE` `CFD`

---

## 📋 Formula Sheet

<details>
<summary><strong>Click to expand — Complete OCF Formula Sheet</strong></summary>

| Formula | Equation | Variables | Units | Conditions | Interview Importance |
|---------|----------|-----------|-------|------------|---------------------|
| Specific Energy | $E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2gA^2}$ | $y$=depth, $V$=velocity | m | At a cross-section | ⭐⭐⭐ |
| Critical Depth (rect.) | $y_c = (q^2/g)^{1/3}$ | $q=Q/b$=discharge per unit width | m | Rectangular channel | ⭐⭐⭐ |
| Min Specific Energy | $E_{min} = \frac{3}{2}y_c$ | $y_c$=critical depth | m | At critical flow | ⭐⭐ |
| Froude Number | $Fr = V/\sqrt{gD_h}$ | $D_h=A/T$=hydraulic depth | — | Flow regime classification | ⭐⭐⭐ |
| Manning | $Q = \frac{1}{n}AR^{2/3}S^{1/2}$ | $n$=roughness, $R$=A/P, $S$=slope | m³/s | Uniform flow design | ⭐⭐⭐ |
| GVF Equation | $\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$ | $S_0$=bed slope, $S_f$=friction slope | — | Gradually varied flow | ⭐⭐⭐ |
| Conjugate Depth | $\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1+8Fr_1^2}-1\right)$ | $y_1,y_2$=pre/post jump depths | m | Hydraulic jump (rect.) | ⭐⭐⭐ |
| Energy Loss (jump) | $\Delta E = \frac{(y_2-y_1)^3}{4y_1y_2}$ | $y_1,y_2$=conjugate depths | m | Jump energy dissipation | ⭐⭐ |
| Continuity (steady) | $Q = A_1V_1 = A_2V_2$ | $A$=area, $V$=velocity | m³/s | Steady flow | ⭐⭐⭐ |
| Continuity (unsteady) | $\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0$ | — | — | Saint-Venant mass | ⭐⭐ |
| Momentum (S-V) | $\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial y}{\partial x} + gAS_f = gAS_0$ | — | — | Saint-Venant momentum | ⭐⭐ |
| Rect. Weir | $Q = C_d \frac{2}{3}\sqrt{2g} \, b \, H^{3/2}$ | $C_d$=discharge coeff, $H$=head over crest | m³/s | Flow measurement | ⭐⭐ |
| V-Notch Weir | $Q = C_d \frac{8}{15}\sqrt{2g}\tan(\theta/2) \, H^{5/2}$ | $\theta$=notch angle | m³/s | Low flow measurement | ⭐⭐ |
| Broad-Crested Weir | $Q = C_d \cdot b \cdot \sqrt{g} \cdot \frac{2}{3}\left(\frac{2E}{3}\right)^{3/2}$ | — | m³/s | Flow measurement | ⭐ |

**Commonly Confused Pairs:**
- **Specific Energy vs Total Energy:** Specific = $y + V^2/2g$ (relative to bed); Total = $z + y + V^2/2g$ (relative to datum)
- **Normal Depth vs Critical Depth:** Normal = Manning balance ($S_0 = S_f$); Critical = minimum specific energy ($Fr = 1$)
- **Subcritical vs Supercritical:** Sub: $Fr < 1$, deep/slow, info travels upstream; Super: $Fr > 1$, shallow/fast, info cannot travel upstream
- **Manning vs Darcy-Weisbach for OCF:** Manning is empirical, simpler; Darcy is more accurate theoretically (use $D_h = 4R$)

</details>

---

## ❓ Question Bank

### A. Basic Concept Questions

1. What is specific energy? How does it differ from total energy?
2. What is critical depth and when does it occur?
3. Define Froude number. What flow regimes does it identify?
4. What is a hydraulic jump? Where does it occur?
5. Classify GVF profiles (M1, M2, S1, S2, etc.).
6. What is Manning's equation? What does $n$ represent?
7. What are the Saint-Venant equations?
8. What is a backwater curve?
9. Name three types of weirs used for flow measurement.
10. What is the difference between uniform and non-uniform flow?

### B. WHY Questions

1. **Why** does specific energy have a minimum at critical depth?
   - Because at critical depth, the flow cannot exist at lower energy for the same discharge; both deeper (subcritical) and shallower (supercritical) depths have higher specific energy.

2. **Why** does a hydraulic jump always transition from supercritical to subcritical (and never the reverse)?
   - Because momentum balance requires it: the specific force curve has only one intersection for subcritical-supercritical pair; entropy/energy dissipation makes it irreversible.

3. **Why** is Manning's equation not accurate for very shallow or very rough channels?
   - Because Manning's $n$ is not constant — it varies with depth, roughness, and channel irregularity. The empirical basis assumes fully rough turbulent flow.

4. **Why** do we use Froude number (not Reynolds number) to classify open channel flow?
   - Because the free surface introduces gravitational effects as the dominant force; Froude number (inertial/gravitational) governs wave propagation and surface instability.

5. **Why** does M1 profile occur upstream of a dam?
   - The dam raises water above normal depth; on a mild slope ($y_n > y_c$), this creates Zone 1 conditions ($y > y_n > y_c$), causing a backwater curve that extends upstream.

### C. WHAT-IF Questions

1. **What happens** if the channel slope is doubled?
   - Normal depth decreases, velocity increases, Froude number may change regime (sub to supercritical).

2. **What happens** if discharge increases in a mild-slope channel?
   - Both $y_n$ and $y_c$ increase; GVF profiles may shift zone; hydraulic jump may move upstream.

3. **What happens** if Manning's $n$ increases (vegetation growth)?
   - For same slope and discharge, normal depth increases; flow velocity decreases; flood risk increases.

4. **What happens** if Froude number crosses 1?
   - Flow transitions between subcritical and supercritical; may occur at a hydraulic jump (forced) or at a control section (free overfall, weir crest).

5. **What happens** if a broad-crested weir is submerged?
   - The discharge equation no longer applies; need drowned weir corrections; discharge depends on downstream depth.

### D. Comparison Questions

| Concept A | Concept B | Key Difference | Application |
|-----------|-----------|----------------|-------------|
| Specific energy | Total energy | Relative to bed vs datum | Cross-section analysis vs energy balance |
| Normal depth | Critical depth | Manning balance vs min energy | Design vs flow classification |
| Subcritical | Supercritical | $Fr < 1$ (deep/slow) vs $Fr > 1$ (shallow/fast) | Wave propagation, control sections |
| M1 profile | M2 profile | Backwater (y↑ downstream) vs drawdown (y↓ downstream) | Dam vs free overfall |
| Hydraulic jump |draulic jump in non-rectangular | Different conjugate depth relations | Rectangular vs trapezoidal channels |
| Manning | Darcy-Weisbach | Empirical vs theoretical; $n$ vs $f$ | Open channel vs pipe/general |
| Sharp-crested weir | Broad-crested weir | Contracted flow vs critical depth over crest | Precise measurement vs robust measurement |
| Uniform flow | Gradually varied flow | Constant depth vs slowly varying depth | Canal design vs backwater analysis |

### E. Numerical Questions

**Easy:**
**Problem:** A rectangular channel (b=3m) carries Q=6 m³/s. Find critical depth and minimum specific energy.
- **Given:** $b=3$ m, $Q=6$ m³/s
- **Find:** $y_c$, $E_{min}$
- **Approach:** $q = Q/b = 2$ m²/s, $y_c = (q^2/g)^{1/3}$, $E_{min} = 1.5y_c$
- **Solution:** $y_c = (4/9.81)^{1/3} = 0.74$ m, $E_{min} = 1.11$ m
- **Final Answer:** $y_c = 0.74$ m, $E_{min} = 1.11$ m
- **Concept Tested:** Critical depth calculation
- **Common Trap:** Forgetting to use per-unit-width discharge $q$

**Medium:**
**Problem:** A rectangular channel (b=5m) carries Q=25 m³/s at y=3.0m with n=0.020, S=0.0004. Determine flow regime and GVF profile type if a dam raises downstream depth to 5.0m.
- **Given:** $b=5$ m, $Q=25$ m³/s, $y=3.0$ m, $n=0.020$, $S_0=0.0004$
- **Find:** Flow regime, GVF profile
- **Approach:** Compute $y_n$ (Manning) and $y_c$, compare with actual and downstream depth
- **Solution:**
  - $q = 5$ m²/s, $y_c = (25/9.81)^{1/3} = 1.37$ m
  - Manning: iterate for $y_n$: $Q = (1/n)(by_n)(by_n/(b+2y_n))^{2/3}S^{1/2}$. Try $y_n = 2.5$ m: $A=12.5$, $P=13.16$, $R=0.95$, $Q = 50 \times 12.5 \times 0.95^{2/3} \times 0.02 = 23.7$ (close). $y_n \approx 2.55$ m
  - At dam: $y = 5.0$ m > $y_n = 2.55$ m > $y_c = 1.37$ m → **M1 profile** (backwater)
- **Final Answer:** Subcritical flow at normal depth; M1 backwater profile upstream of dam
- **Concept Tested:** GVF profile identification
- **Common Trap:** Not iterating Manning properly

**Hard:**
**Problem:** A rectangular channel has Q=10 m³/s, b=4m, y₁=0.3m (upstream of jump). Find y₂, energy loss, and power dissipated.
- **Given:** $Q=10$ m³/s, $b=4$ m, $y_1=0.3$ m
- **Find:** $y_2$, $\Delta E$, $P_{dissipated}$
- **Approach:** Compute $V_1$, $Fr_1$, conjugate depth, energy loss, power
- **Solution:**
  - $V_1 = 10/(4 \times 0.3) = 8.33$ m/s
  - $Fr_1 = 8.33/\sqrt{9.81 \times 0.3} = 4.84$
  - $y_2 = 0.3/2 \times (\sqrt{1+8 \times 23.43} - 1) = 0.15 \times (\sqrt{188.4} - 1) = 0.15 \times 12.74 = 1.91$ m
  - $\Delta E = (1.91-0.3)^3/(4 \times 0.3 \times 1.91) = 4.17/2.29 = 1.82$ m
  - $P = \rho g Q \Delta E = 9810 \times 10 \times 1.82 = 178.5$ kW
- **Final Answer:** $y_2 = 1.91$ m, $\Delta E = 1.82$ m, $P = 178.5$ kW
- **Concept Tested:** Hydraulic jump analysis with power dissipation
- **Common Trap:** Forgetting to multiply by $\rho g Q$ for power

### F. Rapid-Fire Questions (30+)

Q: What is the Froude number?
A: $Fr = V/\sqrt{gD_h}$, ratio of inertial to gravitational forces in open channel flow.

Q: What is specific energy?
A: $E = y + V^2/(2g)$ — energy per unit weight measured relative to the channel bed.

Q: At critical depth, what is the value of Froude number?
A: $Fr = 1$.

Q: What is the minimum specific energy for a rectangular channel?
A: $E_{min} = 1.5y_c$.

Q: What are the two alternate depths?
A: For a given specific energy > $E_{min}$, there are two possible depths: one subcritical (deeper) and one supercritical (shallower).

Q: Name the 5 slope types in GVF classification.
A: Mild (M), Steep (S), Critical (C), Horizontal (H), Adverse (A).

Q: What does M1 profile represent?
A: Mild slope, backwater curve — depth increases downstream (e.g., upstream of dam).

Q: What does S2 profile represent?
A: Steep slope, drawdown curve — depth decreases toward normal depth.

Q: What is normal depth?
A: Depth at which gravity force = friction force (uniform flow, $S_0 = S_f$).

Q: What is the hydraulic jump?
A: Abrupt transition from supercritical to subcritical flow with significant energy dissipation.

Q: What is the momentum equation used for in OCF?
A: Analyzing hydraulic jumps, forces on structures, and flows where energy is not conserved.

Q: Why is momentum equation used for hydraulic jump (not energy)?
A: Energy is dissipated in the jump (unknown amount); momentum is conserved across the jump.

Q: What is a control section?
A: A location where flow passes through critical depth (weir crest, free overfall, gate).

Q: What is a backwater curve?
A: GVF profile where depth increases in the downstream direction (M1, S1, H1, A1).

Q: What is a drawdown curve?
A: GVF profile where depth decreases in the downstream direction (M2, S2, H2).

Q: What is Manning's $n$?
A: Empirical roughness coefficient; typical values: concrete 0.012, earth 0.022, natural 0.030.

Q: What is the hydraulic radius?
A: $R = A/P$ (area divided by wetted perimeter). For wide rectangular channel, $R \approx y$.

Q: What is a sharp-crested weir?
A: Thin-plate weir where flow separates from the upstream edge; used for flow measurement.

Q: What is a broad-crested weir?
A: Weir with flow passing through critical depth over the crest; more robust than sharp-crested.

Q: What is a V-notch weir?
A: Triangular weir used for precise low-flow measurement; $Q \propto H^{5/2}$.

Q: What is a Parshall flume?
A: Venturi-type flow measurement device for open channels; widely used in irrigation and wastewater.

Q: What are the conditions for a hydraulic jump to occur?
A: Supercritical flow must be forced to become subcritical (e.g., by downstream control, slope change).

Q: What is the sequent depth?
A: Same as conjugate depth — the depth downstream of a hydraulic jump.

Q: What happens to Froude number across a jump?
A: It decreases from $Fr_1 > 1$ to $Fr_2 < 1$.

Q: What is a standing wave?
A: Surface waves that remain stationary relative to the channel; occur near $Fr \approx 1$.

Q: What is the S-curve?
A: Hydrograph from continuous unit rainfall; used to convert UH of one duration to another.

Q: What is critical flow control?
A: A section where flow passes through $Fr = 1$; used as a measurement control.

Q: What is the limiting case for M2 profile?
A: As $y \to y_c$, $dy/dx \to -\infty$ (vertical tangent); the M2 curve approaches $y_c$ asymptotically.

Q: What is the USRB stilling basin?
A: USBR Type I-IV basins designed for energy dissipation downstream of spillways, using baffle blocks and sills.

Q: What is supercritical flow control?
A: Flow controlled from upstream (e.g., sluice gate, steep channel); downstream conditions cannot affect upstream.

Q: What is subcritical flow control?
A: Flow controlled from downstream (e.g., dam, weir); upstream conditions adjust to downstream control.

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the GVF equation from the Saint-Venant equations. What assumptions are made?**
   - Start with 1D Saint-Venant, assume steady flow ($\partial/\partial t = 0$), and $dy/dx = (S_0 - S_f)/(1 - Fr^2)$. Assumes: 1D flow, hydrostatic pressure, gradual depth variation (no RVF), uniform velocity distribution.

2. **Explain the limitations of Manning's equation for natural rivers with mobile beds.**
   - Manning's $n$ is not constant — it varies with depth, bed forms (ripples, dunes), vegetation, and season. For mobile beds, bed roughness changes continuously as bed forms evolve. Better to use Darcy-Weisbach with effective roughness or 2D/3D models.

3. **How would you compute a flood wave propagation using the Saint-Venant equations?**
   - Discretize using finite difference (Preissmann scheme, implicit) or finite volume (HLL, Roe solver). Apply upstream boundary (inflow hydrograph) and downstream boundary (normal depth rating curve or critical depth). Check CFL condition for explicit schemes.

4. **What is the physical meaning of the specific force curve?**
   - Specific force $M = Q^2/(gA) + \bar{z}A$ combines momentum and pressure. At the same specific force, two depths are possible (conjugate depths of a jump). The minimum on the M-curve occurs at critical depth.

5. **When does the Saint-Venant equation fail, and what alternatives exist?**
   - Fails at: hydraulic jumps (discontinuity), dam breaks (rapidly varied), supercritical-subcritical transitions. Alternatives: shallow water equations with Riemann solvers, Boussinesq equations (non-hydrostatic), full 3D RANS with free surface tracking (VOF).

6. **How does roughness sublayer affect open channel flow resistance?**
   - In gravel-bed rivers, the roughness sublayer (1-3 grain diameters above bed) is where individual grain drag dominates. Standard log-law fails here. Need to use roughness-height $z_0 = k_s/30$ or $z_0 = k_s/30$ with proper accounting for protrusion and hiding.

---

## 🎤 Interview Answer Format

### High-Value Q1: "What is specific energy?"

**30-second answer:**
"Specific energy is the total energy per unit weight of water measured relative to the channel bed. It equals depth plus velocity head: $E = y + V^2/(2g)$. For a given discharge, it has a minimum at critical depth."

**If interviewer asks deeper:**
"The specific energy diagram plots $E$ vs $y$ for constant $Q$. The curve has two limbs — subcritical (upper) and supercritical (lower) — meeting at critical depth where $Fr = 1$. This is fundamental for analyzing flow transitions at constrictions, expansions, and over weirs."

**Key equation:**
$E = y + \frac{Q^2}{2gA^2}$, $y_c = (q^2/g)^{1/3}$

**Engineering interpretation:**
"At a channel contraction, specific energy must be conserved (no losses). If upstream flow is subcritical, the contraction forces flow through critical depth, creating a control section used for discharge measurement."

---

### High-Value Q2: "Explain the hydraulic jump."

**30-second answer:**
"A hydraulic jump is the abrupt transition from supercritical to subcritical flow. It dissipates kinetic energy, raises the water level, and is used in stilling basins to prevent downstream scour."

**If interviewer asks deeper:**
"The jump is analyzed using the momentum equation (not energy, because energy is dissipated). The conjugate depth relationship gives $y_2/y_1 = 0.5(\sqrt{1+8Fr_1^2}-1)$. Energy loss increases with $Fr_1$. Classification ranges from undular ($Fr_1$ ≈ 1.0–1.7) to strong ($Fr_1 > 9$)."

**Key equation:**
$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1+8Fr_1^2}-1\right)$

**Engineering interpretation:**
"Downstream of a spillway, water has high kinetic energy. A stilling basin forces a hydraulic jump to dissipate this energy before it erodes the river bed. Basin design ensures the jump stays within the structure."

---

## 🔗 Interviewer Follow-up Chain

```
Q1: "What is specific energy?"
    ↓
Q2: "Draw the specific energy diagram. What happens at critical depth?"
    ↓ (minimum E, Fr=1, flow instability)
Q3: "If I constrict a subcritical channel, what happens to the water surface?"
    ↓ (surface dips — conversion of PE to KE to pass through critical depth)
Q4: "How would you use this for flow measurement?"
    ↓ (critical-depth flume — forces Fr=1, Q depends only on upstream head)
Q5: "What if the downstream is controlled by a dam?"
    ↓ (M1 backwater profile extends upstream — GVF analysis needed)
Q6: "How do you compute the GVF profile numerically?"
    ↓ (standard step method, direct step method, or Preissmann scheme)
```

```
Q1: "What is a hydraulic jump?"
    ↓
Q2: "Why do you use the momentum equation instead of energy?"
    ↓ (energy dissipated unknown; momentum conserved)
Q3: "What is the conjugate depth for Fr₁ = 3?"
    ↓ (y₂/y₁ = 0.5(√73-1) = 3.85)
Q4: "How would you design a stilling basin?"
    ↓ (ensure jump occurs within basin, use USBR Type II/III with baffle blocks)
Q5: "What if the jump is swept out of the basin?"
    ↓ (increase tailwater depth or add energy dissipators)
```

---

## 🔗 Cross-Links

- [`hydraulics.md`](../hydraulics/hydraulics.md) — Pipe flow, Bernoulli, friction
- [`hydrology.md`](../hydrology/hydrology.md) — Flood routing, hydrograph analysis
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir, canal design
- [`sediment-transport.md`](../hydrology/sediment-transport.md) — Bed load, mobile-bed hydraulics
- [`irrigation-engineering.md`](../irrigation/irrigation-engineering.md) — Canal design for irrigation
- [`flood-control.md`](../flood_control/flood-control.md) — Flood routing applications
- [`civil-engineering-foundations.md`](../../fundamentals/civil-engineering-foundations.md) — Quick revision formulas

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`hydraulics.md`](../hydraulics/hydraulics.md) — Pipe flow and fundamental hydraulics
* [`../hydrology/hydrology.md`](../hydrology/hydrology.md) — Flood routing and hydrograph analysis
* [`../water_resources/water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir and canal design

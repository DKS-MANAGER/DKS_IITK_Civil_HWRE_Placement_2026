# Sediment Transport

## Overview

Sediment transport describes the movement of solid particles by flowing water. It governs river morphology, reservoir siltation, coastal erosion, and scour around hydraulic structures. Accurate prediction requires understanding particle dynamics, turbulence-particle interactions, and bed evolution.

> **Related topics:** [`hydraulics.md`](../hydraulics/hydraulics.md) · [`turbulence-modeling.md`](../hydraulics/turbulence-modeling.md) · [`hydrology.md`](hydrology.md) · [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md)

---

## Modes of Transport

### Bed Load
- Sediment rolls, slides, or hops (saltates) along the bed
- Dominated by larger, heavier particles
- Transport rate depends on excess shear stress above critical

### Suspended Load
- Particles maintained in suspension by turbulence
- Concentration follows a **Rouse profile:**
  $$\frac{c}{c_a} = \left(\frac{y_a}{y}\right)^Z$$
  where $Z = w_s / (\kappa u_\tau)$ (Rouse number)
  - $w_s$ = fall velocity
  - $\kappa$ = von Kármán constant (0.41)
  - $u_\tau$ = shear velocity

### Wash Load
- Very fine particles carried in suspension without deposition
- Originates from upstream sources; not in equilibrium with local bed material
- Cannot be predicted from local flow conditions alone

### Total Load
$$q_t = q_b + q_s$$
where $q_b$ = bed load transport rate, $q_s$ = suspended load transport rate

---

## Incipient Motion

### Shields Parameter
$$\tau^* = \frac{\tau_0}{(\rho_s - \rho) g d}$$

Where:
- $\tau_0$ = bed shear stress = $\rho g R_h S$
- $\rho_s$ = sediment density (2650 kg/m³ for quartz)
- $\rho$ = fluid density (1000 kg/m³)
- $d$ = grain diameter
- $g$ = gravitational acceleration

**Critical Shields parameter:** $\theta_{cr} \approx 0.047$ for uniform grains in clear water

### Critical Shear Stress
$$\tau_c = \theta_c (\rho_s - \rho) g d$$

**Shield's Diagram:** Plot of $\tau^*$ vs $Re_*$ (particle Reynolds number)
- $Re_* = u_* d / \nu = \sqrt{\tau_c/\rho} \cdot d / \nu$

### HEC-18 Incipient Motion
For bridge pier scour estimation, the critical velocity approach:
$$V_c = 6.19 y^{0.141} d_{50}^{0.357}$$ (SI units, in m/s)

---

## Sediment Transport Formulas

### Meyer-Peter Müller (Bed Load — 1948)
$$q_b^* = 8(\tau^* - \tau_c^*)^{3/2}$$

Where $q_b^* = q_b / \sqrt{(\Delta g d^3)}$, $\Delta = (\rho_s - \rho)/\rho$

**Applicable range:** $\tau^* > 0.047$, coarse non-uniform sediment

### Engelund-Hansen (Total Load — 1967)
$$\frac{q_t}{\sqrt{\Delta g d^5}} = \frac{0.05}{C_f} \left(\frac{\tau_0}{(\rho_s - \rho) g d}\right)^{5/2}$$

Where $C_f$ = friction coefficient

### Van Rijn (Bed Load + Suspended Load — 1984)

**Bed load:**
$$q_b = 0.053 \sqrt{\Delta g d^3} \cdot T^{1.5}$$
where $T = (\tau_0 - \tau_c)/\tau_c$ (transport stage parameter)

**Suspended load:**
$$q_s = \int_a^h c(z) u(z) dz$$
concentration profile from Rouse equation

### Ackers-White (Total Load — 1973)
$$q_t = C \left(\frac{d}{A}\right)^n \left(\frac{u_{*}}{V}\right)^m F_{gr}^{1-n}$$

### Yang (Total Load — 1973)
$$\log C_t = I + J \log\left(\frac{V S}{w_s} - \frac{V_c S}{w_s}\right)$$

where $I$, $J$ are empirical coefficients

---

## Bed Forms

| Bed Form | Wavelength | Height | $Fr$ Range | Migration |
|----------|-----------|--------|-----------|-----------|
| **Ripples** | < 0.3 m | mm–cm | Subcritical | Downstream |
| **Dunes** | m–100 m | cm–m | Subcritical | Downstream |
| **Plane bed** | — | — | Transition | None |
| **Antidunes** | m | cm–m | Supercritical | Upstream |
| **Chutes & pools** | — | — | Supercritical | Alternating |

**Strickler's formula for bed roughness:**
$$n = \frac{d_{50}^{1/6}}{21.1}$$ (SI units)

---

## Scour Mechanics

### Clear-Water Scour
- No sediment supply upstream
- Maximum scour depth limited by equilibrium shear stress
- Occurs at $V < V_c$ (threshold conditions)

### Live-Bed Scour
- Sediment supply replenishes the scour hole
- Equilibrium scour depth depends on transport capacity
- Oscillating scour depth with bed form passage

### Bridge Pier Scour (HEC-18)

**HEC-18 equation (clear-water, live-bed):**
$$\frac{y_s}{y_1} = 2.0 \, K_1 \, K_2 \, K_3 \, K_4 \left(\frac{a}{y_1}\right)^{0.35} Fr_1^{0.43}$$

Where:
- $K_1$ = correction for angle of attack
- $K_2$ = correction for pier nose shape
- $K_3$ = correction for bed condition
- $K_4$ = correction for size of bed material
- $a$ = pier width
- $y_1$ = upstream flow depth

### Abutment Scour
- Simplified contraction scour equations
- Live-bed and clear-water conditions

### Contraction Scour
$$y_s = \left(\frac{Q^2 n^2}{W_2^2 S}\right)^{3/10}$$

---

## Computational Approaches

### Numerical Models

| Model | Type | Application |
|-------|------|-------------|
| **SRH-2D** | 2D finite volume | River hydraulics and sedimentation (USBR) |
| **HEC-RAS** | 1D/2D | River morphology, sediment transport |
| **FLOW-3D** | 3D CFD | Local scour, turbulence-sediment interaction |
| **SedFoam** | OpenFOAM solver | Eulerian two-phase sediment transport |
| **sedExnerFoam** | OpenFOAM solver | Exner equation + ALE morphodynamics |
| **Delft3D** | 2D/3D | Coastal and estuarine morphodynamics |
| **TSMSed** | 2D | Reservoir sedimentation |

### OpenFOAM Sediment Solvers

**SedFoam:** Eulerian two-phase approach
- Solves momentum equations for fluid and sediment phases separately
- Includes granular rheology (μ(I) model) for concentrated sediment
- Coupled with k-ω SST turbulence model
- Applications: pipeline scour, bridge pier scour, sediment transport

**sedExnerFoam:** Exner equation approach
- Morphological update via Exner equation: $\frac{\partial z_b}{\partial t} + \frac{1}{1-p}\nabla \cdot \vec{q}_b = 0$
- Arbitrary Lagrangian-Eulerian (ALE) mesh motion
- Applications: bed evolution, dune migration, scour hole development

---

## Sediment Budget Analysis

### Sediment Yield
- Specific sediment yield: t/km²/year
- Depends on catchment area, rainfall, land use, geology

### Reservoir Sedimentation
- Trap efficiency: $TE = 1 - 1/(1 + 0.0003 \cdot Cap/Y)$ (Brune's curve)
- Useful life estimation based on sedimentation rate

### Channel Processes
- **Aggradation:** Sediment deposition raising bed level
- **Degradation:** Sediment erosion lowering bed level
- **Regime theory:** Equilibrium channel dimensions

---

## Worked Examples

### Example 1: Shields Parameter Calculation
**Problem:** Sand with $d_{50} = 0.5$ mm in a channel with $\tau_0 = 8$ N/m². Determine if motion occurs.

**Solution:**
1. $\tau^* = \tau_0 / [(\rho_s - \rho)gd] = 8 / [(2650-1000)(9.81)(0.0005)]$
2. $\tau^* = 8 / [1650 \times 9.81 \times 0.0005] = 8 / 8.093 = 0.989$
3. $\tau^* = 0.989 \gg \tau_c^* = 0.047$ → **Motion occurs** (significant transport)

### Example 2: Bridge Pier Scour
**Problem:** Bridge pier $a = 2$ m width, flow depth $y_1 = 4$ m, $Fr_1 = 0.5$. Find scour depth.

**Solution:**
1. Assume $K_1 = K_2 = K_3 = K_4 = 1$ (no corrections)
2. $y_s/y_1 = 2.0 \times 1 \times 1 \times 1 \times 1 \times (2/4)^{0.35} \times 0.5^{0.43}$
3. $y_s/4 = 2.0 \times (0.5)^{0.35} \times (0.5)^{0.43} = 2.0 \times 0.784 \times 0.742 = 1.164$
4. $y_s = 4 \times 1.164 = 4.66$ m
5. Total depth at pier: $y_1 + y_s = 8.66$ m

---

## 🎤 Interview Q&A

### Q1: What is the Shields parameter and why is it important?
**A:** The Shields parameter $\tau^* = \tau_0/[(\rho_s-\rho)gd]$ is the ratio of bed shear stress to submerged weight of sediment particles. It determines incipient motion: when $\tau^* > \tau_c^* \approx 0.047$, sediment begins to move. It's the fundamental dimensionless parameter for sediment transport, analogous to the Reynolds number for fluid flow.

### Q2: Explain the difference between bed load and suspended load.
**A:** Bed load: particles roll, slide, or saltate along the bed; transport rate depends on excess shear stress; described by MPM, Van Rijn formulas. Suspended load: particles maintained in suspension by turbulence; concentration follows Rouse profile; transport rate depends on flow velocity and fall velocity. Total load = bed load + suspended load.

### Q3: What are the main factors affecting bridge pier scour?
**A:** (1) Pier width $a$ — wider piers cause more scour, (2) Flow depth $y_1$ — deeper flow increases scour, (3) Froude number — higher $Fr$ increases scour, (4) Angle of attack — skewed piers cause more scour, (5) Pier nose shape — round noses reduce scour, (6) Bed condition — live-bed vs clear-water, (7) Sediment size — finer sediment erodes more easily.

### Q4: How do you prevent or mitigate scour?
**A:** (1) Riprap protection around piers and abutments, (2) Sheet pile walls or caisson foundations, (3) Streamline pier noses to reduce flow separation, (4) Grade control structures upstream, (5) Collar plates around piers, (6) Sacrificial piles upstream, (7) Increase foundation depth below predicted scour.

### Q5: What is the Rouse profile and when is it applicable?
**A:** The Rouse profile $c/c_a = (y_a/y)^Z$ describes the vertical distribution of suspended sediment concentration in equilibrium. $Z = w_s/(\kappa u_\tau)$ is the Rouse number. When $Z > 2.5$, most sediment is near the bed (bed load dominant). When $Z < 0.1$, sediment is uniformly distributed (wash load). Applicable in steady, uniform open channel flows.

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Shields | $\tau^* = \tau_0/[(\rho_s-\rho)gd]$ | Incipient motion |
| Critical shear | $\tau_c = \theta_c(\rho_s-\rho)gd$ | Threshold for motion |
| MPM (bed load) | $q_b^* = 8(\tau^*-\tau_c^*)^{3/2}$ | Bed load transport |
| Rouse profile | $c/c_a = (y_a/y)^Z$ | Suspended sediment |
| Strickler | $n = d_{50}^{1/6}/21.1$ | Bed roughness |
| Exner | $\partial z_b/\partial t + \nabla \cdot q_b/(1-p) = 0$ | Bed evolution |
| HEC-18 scour | $y_s/y_1 = 2.0 K_1 K_2 K_3 K_4 (a/y_1)^{0.35} Fr^{0.43}$ | Pier scour |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Sediment modes        →  Shields parameter            →  Morphological modeling       →  Shields vs critical shear
Bed load vs suspended →  Meyer-Peter Müller formula   →  Sediment rating curves       →  MPM formula assumptions
Incipient motion      →  Rouse profile                →  Non-equilibrium transport    →  Rouse number interpretation
Grain size analysis   →  HEC-18 pier scour            →  Reservoir sedimentation      →  HEC-18 correction factors
```

> **Priority:** `P1 — High Priority` · **Tags:** `HWRE` `CFD`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What are the modes of sediment transport?
2. What is the Shields parameter?
3. What is the Rouse profile?

### B. WHY Questions
1. **Why** is bed load transport proportional to $(\tau^* - \tau_c^*)^{3/2}$?
   - Because excess shear stress drives particle motion; the 3/2 exponent comes from empirical fits to experimental data reflecting the nonlinear relationship between shear and transport.

2. **Why** does the Rouse number determine suspended vs bed load?
   - $Z = w_s/(\kappa u_\tau)$ compares settling velocity to turbulent diffusion. High Z → settling dominates → bed load. Low Z → turbulence suspends particles → suspended load.

3. **Why** is bridge scour a critical design concern?
   - Scour reduces the effective foundation depth; if not accounted for, piers can fail. HEC-18 provides empirical equations to predict maximum scour depth.

---

## 🎤 Interview Answer Format

### High-Value Q: "How would you predict bridge pier scour?"

**30-second answer:**
"Use the HEC-18 equation: $y_s/y_1 = 2.0K_1K_2K_3K_4(a/y_1)^{0.35}Fr^{0.43}$. The correction factors account for angle of attack ($K_1$), pier nose shape ($K_2$), bed condition ($K_3$), and sediment size ($K_4$). Design foundation depth well below predicted scour."

**Key equation:**
$y_s/y_1 = 2.0K_1K_2K_3K_4(a/y_1)^{0.35}Fr^{0.43}$

---

## 🔗 Cross-Links

- [`hydraulics.md`](../hydraulics/hydraulics.md) — Flow fundamentals
- [`turbulence-modeling.md`](../hydraulics/turbulence-modeling.md) — Turbulence-sediment interaction
- [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Channel hydraulics
- [`flood-control.md`](../flood_control/flood-control.md) — Scour in flood conditions

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`../hydraulics/turbulence-modeling.md`](../hydraulics/turbulence-modeling.md) — Turbulence-sediment interaction
* [`../open_channel_flow/open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel flow basics

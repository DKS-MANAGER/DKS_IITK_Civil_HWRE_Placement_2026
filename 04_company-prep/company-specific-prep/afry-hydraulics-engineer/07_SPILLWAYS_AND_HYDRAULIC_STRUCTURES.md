# Module 07: Spillways & Hydraulic Structures — Design, Profiles & Hydraulics

> **Document Focus**: Ogee Spillways, Sluice-Type Spillways, Broad-Crested Weirs, Discharge Equations, Crest Pressure Dynamics, and Cavitation Mitigation  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — USBR DESIGN OF SMALL DAMS, IS 6934, IS 11130, CWC GUIDELINES]`  

---

## 1. Role & Classification of Spillways

Spillways are the primary safety valve of dams and hydropower storage facilities. Their overriding engineering purpose is to safely bypass excess flood inflows that cannot be stored in the reservoir without allowing the dam crest to be overtopped. Because dam overtopping is the leading cause of catastrophic concrete and embankment dam failures worldwide, hydraulic design of spillways requires absolute precision in discharge rating, crest geometry, and cavitation safety.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SPILLWAY CLASSIFICATION (JD AUDIT)                       │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ SPILLWAY TYPE       │ HYDRAULIC MECHANISM       │ PRIMARY APPLICATION       │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Ogee (Overflow)** │ Free overflow conforming  │ Primary flood evacuation  │
│                     │ to lower nappe of sharp-  │ for concrete gravity,     │
│                     │ crested weir; high C_d    │ arch & buttress dams      │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Sluice-Type**     │ Orifice flow under high   │ Deep reservoir evacuation,│
│ (Breastwall/Bottom) │ hydrostatic head; gate-   │ sediment flushing & low-  │
│                     │ controlled submerged/free │ level flood discharge     │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **Broad-Crested**   │ Parallel streamline flow; │ Intake canal weirs,       │
│ **Weir**            │ critical depth y_c        │ side-channel spillways,   │
│                     │ established across crest  │ check dams & diversion    │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

## 2. Ogee (Overflow) Spillway Design & Hydraulics

### 2.1 Theoretical Foundation: The Aerated Nappe
The ideal profile of an ogee spillway represents the lower boundary surface of a ventilated nappe of water flowing over a sharp-crested weir discharging under a design head $H_d$. Under this profile, the pressure on the concrete crest at design head is atmospheric ($p_{\text{crest}} \approx 0\text{ gauge}$), eliminating undesirable boundary separation while maximizing the discharge coefficient ($C_d$).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       OGEE SPILLWAY PROFILE GEOMETRY                        │
│                                                                             │
│                        Crest (0,0)                                          │
│        Upstream        ▲        Downstream Chute Profile:                   │
│        Arc:            │        y/H_d = -K (x/H_d)^n                        │
│         .───.          │                                                    │
│       /       \        │                                                    │
│      /         \───────┼───────────────────────────\                        │
│     │                  │                            \                       │
│     │                  │                             \                      │
│     │                  ▼                              \                     │
│     │ Dam Face (z = -P)                                \                    │
│     │                                                   ▼                   │
└─────┴───────────────────────────────────────────────────────────────────────┘
```

### 2.2 USBR / WES Downstream Profile Equation
The downstream profile coordinate equation (developed by the U.S. Army Corps of Engineers Waterways Experiment Station — WES, and adopted by USBR and Bureau of Indian Standards IS 6934) is:
$$\boxed{\frac{y}{H_d} = -K \left(\frac{x}{H_d}\right)^n \iff y = -\frac{K}{H_d^{n-1}} x^n}$$
where:
* $x, y$: Coordinates with the origin $(0,0)$ located at the highest point of the ogee crest ($x$ positive downstream, $y$ negative downward).
* $H_d$: Design head (excluding approach velocity head, or total design energy head $H_{ed}$).
* $K, n$: Geometric profile parameters governed by the upstream face slope and approach velocity:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WES / USBR OGEE PROFILE PARAMETERS                       │
├───────────────────────────────┬──────────────────────┬──────────────────────┤
│ UPSTREAM DAM FACE SLOPE       │ PROFILE FACTOR K     │ EXPONENT n           │
├───────────────────────────────┼──────────────────────┼──────────────────────┤
│ **Vertical ($90^\circ$)**     │ **0.500**            │ **1.850**            │
│ Sloping 1H : 3V ($71.6^\circ$)│ 0.515                │ 1.836                │
│ Sloping 2H : 3V ($56.3^\circ$)│ 0.535                │ 1.810                │
│ Sloping 3H : 3V ($45.0^\circ$)│ 0.540                │ 1.776                │
└───────────────────────────────┴──────────────────────┴──────────────────────┘
```
For a vertical upstream face, the profile simplifies to:
$$y = -0.500 \frac{x^{1.85}}{H_d^{0.85}}$$

### 2.3 Upstream Crest Profile Geometry
Upstream of the origin ($x < 0$), the crest profile is defined by compound circular arcs tangent to the crest and the upstream dam face. For a vertical upstream face:
* Arc 1: Radius $R_1 = 0.50 H_d$, extending from $x = 0$ to $x = -0.175 H_d$.
* Arc 2: Radius $R_2 = 0.20 H_d$, extending from $x = -0.175 H_d$ to tangent intersection with the vertical face at $x = -0.282 H_d, y = -0.126 H_d$.

### 2.4 Discharge Equation & Contraction Corrections
The general discharge equation for an ogee crest is:
$$Q = C_d L_e H_e^{3/2}$$
where:
* $H_e = H + \frac{v_a^2}{2g}$: Total effective head including approach velocity head ($v_a = Q / A_{\text{upstream}}$).
* $C_d$: Discharge coefficient ($\approx 2.18 \text{ to } 2.22\text{ m}^{1/2}\text{/s}$ in SI units; $\approx 3.95 \text{ to } 4.02$ in Imperial units at design head).
* $L_e$: Effective crest length, calculated by deducting pier and abutment end contractions (USBR / IS 6934):
  $$\boxed{L_e = L_{\text{total}} - 2 (N K_p + K_a) H_e}$$
  where:
  * $L_{\text{total}} = \sum b_i$: Clear sum of all bay widths.
  * $N$: Number of bridge piers.
  * $K_p$: Pier contraction coefficient:
    * Square-nosed piers with rectangular corners: $K_p = 0.02$
    * Round-nosed piers (semicircular): $K_p = 0.01$
    * Pointed cutwater piers ($45^\circ \text{ to } 60^\circ$ nose): $K_p = 0.00$
  * $K_a$: Abutment contraction coefficient:
    * Square abutments with headwall at $90^\circ$: $K_a = 0.20$
    * Rounded abutments ($R > 0.5 H_e$): $K_a = 0.10$

---

## 3. Crest Pressure Dynamics & Cavitation Hazard

When an ogee crest operates at a head $H$ different from its design head $H_d$, local boundary layer pressures depart significantly from atmospheric:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CREST PRESSURE vs. OPERATING HEAD                        │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ CONDITION           │ PHYSICAL PHENOMENON       │ ENGINEERING CONSEQUENCE   │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **H = H_d**         │ Flow follows nappe shape; │ Optimum design point;     │
│ (Design Head)       │ $p_{\text{crest}} \approx 0$ (atmospheric)│ $C_d \approx 2.20$; no risk. │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **H < H_d**         │ Fluid sheet has greater   │ Positive gauge pressure   │
│ (Under-Design)      │ curvature than boundary;  │ suppresses separation;    │
│                     │ nappe presses on crest    │ $C_d$ drops ($C_d < 2.18$).│
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ **H > H_d**         │ Water inertia tends to    │ Sub-atmospheric suction;  │
│ (Over-Design /      │ detach from boundary;     │ $C_d$ increases ($C_d>2.25$).│
│ Super-Flood)        │ boundary pulls nappe down │ **Severe Cavitation Risk**│
│                     │ ($p_{\text{crest}} < 0$)  │ if $p < -4\text{ to } -6$ m│
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

> [!CAUTION]
> **Cavitation Danger Limit ($H / H_d$):**  
> In engineering practice, ogee spillways are frequently designed for a standard design flood head $H_d$, but must safely pass a Probable Maximum Flood (PMF) check head $H_{PMF}$. USBR and AFRY design criteria mandate that:
> $$\frac{H_{PMF}}{H_d} \le 1.33$$
> If $H / H_d > 1.33$, sub-atmospheric pressures drop below $-6.0\text{ m}$ of water column, inducing boundary boundary layer separation, violent structural vibrations, and concrete pitting erosion.

---

## 4. Sluice-Type Spillways & Deep Gated Outlets

Sluice spillways (breastwall gates, deep sluices, and bottom outlets) are pressurized orifices located beneath the reservoir surface. In Himalayan run-of-river projects (e.g., AFRY's Thana Plaun project), deep sluices are indispensable for **drawdown flushing of heavy bedload sediment**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SLUICE SPILLWAY FLOW REGIMES                          │
│                                                                             │
│   Free Discharge (Unsubmerged):          Submerged Tailwater Discharge:     │
│   H_1 (Head to Centroid)                 H_1                  H_2           │
│   ───────────┐                           ───────────┐      ────────┐        │
│              │ Gate                      │          │ Gate         │        │
│              │ ──┐                       │          │ ──┐          │        │
│              │   │===► v = √(2gH_1)      │          │   │==► v = √(2g(H_1-H_2))
│   ───────────┴───┴─────────────────      │   ───────┴───┴──────────┴────    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Discharge Formulation
1. **Free Discharge (Free Efflux)**:
   $$Q = C_d A \sqrt{2 g H_1} = C_c C_v (b \cdot a) \sqrt{2 g H_1}$$
   where:
   * $a$: Vertical gate opening height (m).
   * $b$: Width of sluice barrel (m).
   * $H_1$: Net head from upstream water surface to the centroid of the orifice (m).
   * $C_c$: Contraction coefficient ($\approx 0.60 \text{ to } 0.62$).
   * $C_v$: Velocity coefficient ($\approx 0.97 \text{ to } 0.98$).
   * $C_d$: Orifice discharge coefficient ($\approx 0.60$).
2. **Submerged Discharge**:
   When downstream tailwater elevation $H_2$ exceeds the vena contracta elevation:
   $$Q = C_d A \sqrt{2 g (H_1 - H_2)}$$

### 4.2 Aeration Requirements for High-Velocity Sluices
When high-head sluice gates discharge at velocities $v > 25\text{ m/s}$, the high-speed water jet drags air out of the conduit. If an inadequate air supply exists, massive negative pressures develop downstream of the gate, leading to **gate vibration and cavitation destruction**.
The required air vent flow rate $Q_{\text{air}}$ is determined via the Kalinske-Robertson relationship:
$$\beta = \frac{Q_{\text{air}}}{Q_{\text{water}}} = 0.03 (Fr - 1)^{1.06}$$
where $Fr = \frac{v}{\sqrt{g a}}$ is the Froude number of the vena contracta jet.

---

## 5. Broad-Crested Weir Hydraulics

A weir is classified as **broad-crested** when the crest length in the direction of flow $L_c$ is sufficiently long relative to the upstream head $H$ such that streamlines become straight, parallel, and hydrostatic across the crest:
$$0.10 \le \frac{H}{L_c} \le 0.40$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BROAD-CRESTED WEIR PROFILE                            │
│                                                                             │
│          Total Energy H_0                                                   │
│   ───────- - - - - - - - - - - - - - - - - - - - - - - - - - - -            │
│          ▲                                                                  │
│          │ y_0                                                              │
│   ───────┼───────────\                                                      │
│          │            \     y_c = (2/3) H_0 (Critical Depth on Crest)       │
│          │             \─────────────────────────────────────\              │
│          │                                                    \             │
│          │                                                     \            │
│   Bed    └───────────────────────────┬──────────────────────────┴────────   │
│          ◄─────────────── Crest Length L_c ─────────────────────►           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Proof of Theoretical Discharge Equation
Assuming critical flow occurs on the broad crest with parallel streamlines:
$$y_{\text{crest}} = y_c = \frac{2}{3} H_0, \quad v_c = \sqrt{g y_c} = \sqrt{\frac{2}{3} g H_0}$$
where $H_0$ is total upstream head above the crest ($H_0 = H + \frac{v_0^2}{2g}$).
Discharge per unit width $q$:
$$q = y_c v_c = \left(\frac{2}{3}H_0\right) \sqrt{g \left(\frac{2}{3}H_0\right)} = \left(\frac{2}{3}\right)^{3/2} \sqrt{g} H_0^{3/2}$$
$$\left(\frac{2}{3}\right)^{3/2} = \sqrt{\frac{8}{27}} = 0.5443$$
$$q = 0.5443 \sqrt{9.81} H_0^{3/2} = 0.5443(3.132) H_0^{3/2} = \mathbf{1.705 H_0^{3/2}}$$
Accounting for real-world boundary layer skin friction along the crest, an actual discharge coefficient $C_d \approx 0.95 \text{ to } 0.98$ is introduced:
$$Q = C_d \left(\frac{2}{3}\right)^{3/2} \sqrt{g} b H_0^{3/2} \approx 1.60 \text{ to } 1.68 b H_0^{3/2} \quad \blacksquare$$

### 5.2 Modular Limit & Submergence
The **modular limit** is the tailwater submergence ratio ($h_2 / H_0$) at which downstream water begins to drown the critical flow on the crest. For broad-crested weirs, the modular limit is exceptionally high:
$$\left(\frac{h_2}{H_0}\right)_{\text{limit}} \approx 0.67 \text{ to } 0.80$$
Below this limit, tailwater fluctuations have **zero effect** on upstream head or discharge.

---

## 6. Solved Engineering Design Problem: Ogee Spillway Sizing

**Statement**: Design an ogee overflow spillway for a concrete gravity dam to discharge a design flood of $Q_d = 2,400\text{ m}^3\text{/s}$.
* Upstream dam crest elevation: $520.0\text{ m}$.
* Spillway crest elevation: $508.0\text{ m}$ (Height of weir $P = 508.0 - 470.0 = 38.0\text{ m}$ above riverbed).
* Upstream dam face is vertical ($90^\circ$).
* Maximum reservoir design flood level: $516.0\text{ m} \implies$ Design head $H_d = 516.0 - 508.0 = 8.0\text{ m}$.
* Discharge coefficient at design head: $C_{d0} = 2.20\text{ SI units}$.
* Sluice/pier arrangement: 4 spillway bays separated by 3 round-nosed piers ($K_p = 0.01$).
* Abutments are rounded with $90^\circ$ return walls ($K_a = 0.10$).
1. Determine the required effective crest length $L_e$ and the clear width of each bay $b$.
2. Formulate the mathematical equation of the downstream profile coordinates.
3. Check the safety margin if an extreme PMF raises the reservoir to $518.5\text{ m}$ ($H = 10.5\text{ m}$).

**Solution**:
1. **Effective Crest Length ($L_e$) & Bay Sizing**:
   At design head $H_d = 8.0\text{ m}$:
   $$Q = C_d L_e H_d^{3/2} \implies 2,400 = 2.20 \times L_e \times (8.0)^{3/2}$$
   $$(8.0)^{3/2} = \sqrt{512} = 22.6274$$
   $$2.20 \times 22.6274 = 49.780$$
   $$L_e = \frac{2,400}{49.780} = \mathbf{48.212\text{ m}}$$
   Relating effective length to total clear length $L$:
   $$L_e = L - 2(N K_p + K_a) H_d$$
   With $N = 3$ piers, $K_p = 0.01$, and $K_a = 0.10$:
   $$2(N K_p + K_a) H_d = 2[3(0.01) + 0.10] \times 8.0 = 2(0.03 + 0.10) \times 8.0 = 2(0.13) \times 8.0 = 2.080\text{ m}$$
   $$L = L_e + 2.080 = 48.212 + 2.080 = \mathbf{50.292\text{ m}}$$
   Dividing across 4 equal bays:
   $$b = \frac{50.292\text{ m}}{4} = 12.573\text{ m} \implies \text{Adopt } \mathbf{b = 12.60\text{ m per bay}}$$
   Total revised clear length: $L = 4 \times 12.60 = \mathbf{50.40\text{ m}}$.
   Revised effective length: $L_e = 50.40 - 2.08 = \mathbf{48.32\text{ m}}$.
   Actual design discharge capacity:
   $$Q_{\text{actual}} = 2.20 \times 48.32 \times 22.6274 = \mathbf{2,405.4\text{ m}^3\text{/s}} \ge 2,400\text{ m}^3\text{/s} \quad (\text{Safe})$$

2. **Downstream Profile Coordinate Equation**:
   For a vertical upstream face ($K = 0.500, n = 1.850$):
   $$\frac{y}{H_d} = -0.500 \left(\frac{x}{H_d}\right)^{1.850}$$
   Substituting $H_d = 8.0\text{ m}$:
   $$H_d^{0.850} = (8.0)^{0.850} = 5.8564$$
   $$y = -\frac{0.500}{5.8564} x^{1.850} = \mathbf{-0.08538 \cdot x^{1.850}}$$

   *Key Profile Coordinate Table*:
   * $x = 0.0\text{ m} \implies y = 0.00\text{ m}$ (Crest Summit)
   * $x = 2.0\text{ m} \implies y = -0.08538(2.0)^{1.85} = -0.08538(3.605) = \mathbf{-0.308\text{ m}}$
   * $x = 4.0\text{ m} \implies y = -0.08538(4.0)^{1.85} = -0.08538(12.996) = \mathbf{-1.110\text{ m}}$
   * $x = 8.0\text{ m} \implies y = -0.08538(8.0)^{1.85} = -0.08538(46.851) = \mathbf{-4.000\text{ m}} = -0.5 H_d$
   * $x = 12.0\text{ m} \implies y = -0.08538(12.0)^{1.85} = -0.08538(99.043) = \mathbf{-8.456\text{ m}}$

3. **Extreme Flood (PMF) Cavitation Check**:
   Under extreme check head $H_{PMF} = 10.5\text{ m}$:
   $$\frac{H_{PMF}}{H_d} = \frac{10.5}{8.0} = \mathbf{1.3125}$$
   *Evaluation against Cavitation Limit*:
   $$\frac{H_{PMF}}{H_d} = 1.3125 < 1.33 \quad \blacksquare$$
   The check head remains strictly within the USBR / AFRY safety envelope ($\le 1.33$). While sub-atmospheric suction pressures will develop on the crest, they will not exceed $-3.5\text{ m}$ water column, avoiding the cavitation inception threshold ($-6.0\text{ m}$).


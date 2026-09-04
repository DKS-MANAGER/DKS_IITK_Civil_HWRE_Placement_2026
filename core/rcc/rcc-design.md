# Reinforced Cement Concrete (RCC) Design

> **Placement Priority:** P0 — Asked in EVERY core civil engineering interview
> **GATE-O-PEDIA Reference:** Chapter 4 (2,131 lines, 23 topics, 5 formulas)
> **Canonical Page:** `core/rcc/rcc-design.md`
> **Design Code:** IS 456:2000 (Plain and Reinforced Concrete)

---

## Scope

Reinforced Cement Concrete (RCC) is the most widely used construction material in India. Design follows the **Limit State Method (LSM)** per IS 456:2000. Every core civil company (L&T, Tata Projects, AECOM, PSUs) tests RCC design fundamentals in interviews.

| Domain | Relevance |
|--------|-----------|
| Structural Design | Beams, slabs, columns, footings |
| Construction | Detailing, cover, bar bending schedule |
| Earthquake Design | Ductility, strong-column-weak-beam |
| Prestressed Concrete | Bridges, long spans |
| Interview | Most frequently tested structural topic |
| Software | STAAD, ETABS, SAFE, RCDC |

---

## 1. Concrete Properties

### Stress-Strain Behavior

- Concrete is **strong in compression, weak in tension** (tension ≈ 10% of compression).
- Stress-strain curve is **non-linear**; linear up to ~10-15% of ultimate strength.
- **Lower strength concrete has greater ductility** (flatter curve, higher failure strain).
- Higher grade concrete → steeper initial curve, sharper peak, lower failure strain.

### Key Strength Parameters

| Parameter | Formula | Notes |
|-----------|---------|-------|
| Characteristic strength | $f_{ck}$ | 5% of test cubes fall below this |
| Design strength | $f_{ck}/\gamma_m = f_{ck}/1.5 = 0.67 f_{ck}$ | $\gamma_m = 1.5$ for concrete |
| Flexural strength (modulus of rupture) | $f_{cr} = 0.7\sqrt{f_{ck}}$ | For cracking check |
| Direct tensile strength | $(0.5 - 0.625)\sqrt{f_{ck}}$ | Splitting test |
| Splitting tensile | $f_{ct} = 2P/(\pi DL)$ | Cylinder splitting test |

### Modulus of Elasticity

$$E_c = 5000\sqrt{f_{ck}} \text{ (N/mm², short-term)}$$

**Long-term modulus (with creep):**
$$E_{ce} = \frac{E_c}{1 + \theta}$$

Where $\theta$ = creep coefficient = (ultimate creep strain)/(elastic strain at loading).

### WHY does concrete need steel reinforcement?

Concrete is strong in compression but **weak in tension** (tensile strength only ~10% of compressive). Steel reinforcement is placed in tension zones to carry tensile forces, while concrete carries compression. This creates a **composite material** where each material does what it does best. Without steel, concrete members would crack and fail at very low loads.

### Creep

Time-dependent increase in strain under sustained load.

**Causes:** Internal movement of adsorbed water, viscous flow between gel particles, moisture loss, growth of microcracks.

**Effects:**
- Increases deflection of beams & slabs
- Increases deflection in slender columns → may lead to buckling
- Loss of prestress in prestressed concrete
- Reduces stress induced by restrained shrinkage

**Creep increases when:** High cement content, high water-cement ratio, low aggregate content, high air entrainment, low relative humidity, high temperature, small member thickness, loading at early age.

### Shrinkage

Contraction due to drying when concrete sets.

| Type | Cause | Prevention |
|------|-------|-----------|
| Plastic shrinkage | Evaporation/absorption soon after placing | Use air-entraining & expanding cement |
| Drying shrinkage | Loss of water held in gel pores | Moist curing, larger members |

---

## 2. Working Stress vs Limit State Method

| Aspect | Working Stress Method (WSM) | Limit State Method (LSM) |
|--------|----------------------------|--------------------------|
| Basis | Elastic theory, allowable stresses | Probabilistic, partial safety factors |
| Loads | Working loads | Factored loads (1.5 × working) |
| Material stress | Allowable (single FOS) | Design strength ($f_{ck}/1.5$, $f_y/1.15$) |
| Failure check | No explicit collapse check | Limit state of collapse + serviceability |
| Serviceability | Implicit | Explicit (deflection, cracking, vibration) |
| Economy | Conservative, more concrete | More economical, less concrete |
| IS 456 | Older approach | **Current recommended approach** |

**Limit states:**
1. **Limit state of collapse** — flexure, compression, torsion, shear
2. **Limit state of serviceability** — deflection, cracking, vibration

### Partial Safety Factors

| Factor | Value | Applies to |
|--------|-------|-----------|
| $\gamma_m$ (concrete) | 1.5 | Material strength |
| $\gamma_m$ (steel) | 1.15 | Material strength |
| $\gamma_f$ (loads) | 1.5 | DL, LL |
| $\gamma_f$ (loads) | 1.2 | DL + LL + WL/EL |
| $\gamma_f$ (loads) | 0.9 | DL (stability check) |

### Load Combinations (IS 456 Table 18)

| Combination | Formula |
|-------------|---------|
| DL + LL | $1.5(DL) + 1.5(LL)$ |
| DL + WL/EL | $1.5(DL) + 1.5(WL)$ or $0.9(DL) + 1.5(WL)$ |
| DL + LL + WL/EL | $1.2(DL) + 1.2(LL) + 1.2(WL)$ |

### Assumptions — Limit State of Collapse (Flexure)

1. Plane sections remain plane after bending.
2. Maximum strain in concrete = **0.0035** (at outermost compression fibre).
3. Beam always fails by **crushing of concrete**.
4. Failure criterion — **maximum principal strain theory**.
5. Max strain in tension reinforcement: $\varepsilon_{st} = 0.87f_y/E_s + 0.002$ (ensures ductility).

### WHY is limit state design preferred over working stress?

WSM uses a single arbitrary factor of safety and assumes linear elastic behavior throughout. LSM applies **partial safety factors** to loads and materials separately, giving consistent reliability across different loading conditions. It also explicitly checks **serviceability** (deflection, cracking) which WSM ignores. This makes LSM more realistic, economical, and reliable.

---

## 3. Flexural Design (Singly Reinforced)

### Stress Block (IS 456)

For the parabolic-rectangular stress block:
- Total compressive force: $C = 0.36 f_{ck} b x_u$
- Centroid of compression: $0.42 x_u$ from top
- Lever arm: $(d - 0.42 x_u)$

### Limiting Depth of Neutral Axis

$$\frac{x_{u,max}}{d} = \frac{0.0035}{0.87 f_y/E_s + 0.0055}$$

| Steel Grade | $x_{u,max}/d$ |
|-------------|---------------|
| Fe250 | 0.53 |
| Fe415 | 0.48 |
| Fe500 | 0.46 |

### Section Classification

| Type | Condition | Failure Mode | Design Preference |
|------|-----------|--------------|-------------------|
| **Under-reinforced** | $x_u < x_{u,max}$ | Steel yields first → **ductile** | ✅ Preferred |
| **Balanced** | $x_u = x_{u,max}$ | Steel & concrete fail together | Boundary |
| **Over-reinforced** | $x_u > x_{u,max}$ | Concrete crushes first → **brittle** | ❌ Avoid |

### Moment of Resistance

**Balanced section (Fe415):**
$$M_{u,lim} = 0.138 f_{ck} b d^2$$

**General (under-reinforced):**
$$M_u = 0.87 f_y A_{st} \left(d - 0.42 x_u\right)$$

**Neutral axis depth:**
$$x_u = \frac{0.87 f_y A_{st}}{0.36 f_{ck} b}$$

**In terms of steel percentage $p_t$:**
$$M_u = 0.87 f_y \frac{p_t}{100}\left(1 - 1.005 \frac{f_y}{f_{ck}}\frac{p_t}{100}\right) b d^2$$

### Steel Limits

| Parameter | Value |
|-----------|-------|
| Minimum tension steel | $A_{st,min} = 0.85 bd/f_y$ |
| Maximum tension steel | $4\%$ of gross area ($bD$) |
| Minimum for Fe415 | $\approx 0.2\%$ of $bd$ |

### WHY is under-reinforced design preferred?

Under-reinforced sections fail by **yielding of steel first**, giving **ductile failure with visible warning** (large deflections, wide cracks) before collapse. Over-reinforced sections fail by **sudden crushing of concrete** — brittle failure with no warning, which is dangerous. IS 456 mandates designing as under-reinforced to ensure ductility and safety.

---

## 4. Doubly Reinforced Sections

Used when **depth & breadth are restricted** (architectural constraints) and the section cannot carry the moment as singly reinforced.

**Design decomposition:**
$$M_u = M_{u,lim} + M_{u2}$$
$$A_{st} = A_{st,lim} + A_{st2}$$

**Compression steel:**
$$A_{sc} = \frac{M_u - M_{u,lim}}{(f_{sc} - f_{cc})(d - d')}$$

**Additional tension steel:**
$$A_{st2} = \frac{M_u - M_{u,lim}}{0.87 f_y (d - d')}$$

**Equilibrium:**
$$0.36 f_{ck} b x_u + A_{sc}(f_{sc} - f_{cc}) = 0.87 f_y A_{st}$$

**Note:** Doubly reinforced is **less economical** (compression steel not fully utilized). Requires stirrups to prevent buckling of compression bars.

### WHY provide compression reinforcement?

1. **Restricted section dimensions** — when depth/width cannot be increased.
2. **Moment reversal** — wind/earthquake loads cause both sagging and hogging.
3. **Reduces long-term deflection** — compression steel restrains creep & shrinkage.
4. **Improves ductility** — for earthquake-resistant design.

---

## 5. Flanged Beams (T & L Beams)

Used when slab is cast **monolithically** with beam — the slab acts as the compression flange.

### Effective Flange Width (IS 456)

| Beam Type | Effective Width $b_f$ |
|-----------|----------------------|
| T-beam | $b_f = \frac{l_o}{6} + b_w + 6D_f$ |
| L-beam | $b_f = \frac{l_o}{12} + b_w + 3D_f$ |
| Isolated T-beam | $b_f = \frac{l_o}{\frac{l_o}{b} + 4} + b_w$ |
| Isolated L-beam | $b_f = \frac{0.5 l_o}{\frac{l_o}{b} + 4} + b_w$ |

Where $l_o$ = distance between points of zero moment (0.7 × effective span for continuous beams).

### Analysis Cases

**Case I — NA in flange ($x_u \le D_f$):** Design as rectangular beam of width $b_f$.

**Case II — $D_f < x_u < 7D_f/3$:**
$$y_f = (0.65 + 0.15 x_u/D_f) D_f$$
$$0.36 f_{ck} b_w x_u + 0.45 f_{ck}(b_f - b_w) y_f = 0.87 f_y A_{st}$$

**Case III — $x_u > 7D_f/3$:**
$$y_f = D_f$$
$$M_{uR} = 0.45 f_{ck}(b_f - b_w) D_f\left(d - \frac{D_f}{2}\right) + 0.36 f_{ck} b_w x_u (d - 0.42 x_u)$$

### Design Practice

- Beam at **support** designed as **rectangular** for negative (hogging) moment.
- Beam at **mid-span** designed as **T-beam** for positive (sagging) moment.
- Effective depth ≈ span/11 to span/12.

---

## 6. Shear Design

### Types of Shear

| Type | Description |
|------|-------------|
| Flexural shear (one-way) | Beam shear, slab shear |
| Punching shear (two-way) | Slab carrying concentrated column load |
| Torsion shear | Member subjected to torsion |

### Modes of Shear Failure

1. **Diagonal tension failure** — large shear, near-zero BM; cracks at 45°.
2. **Flexural shear failure** — large BM, less shear; vertical flexural cracks + diagonal tension.
3. **Diagonal compression failure** — crushing of concrete; heavily shear-reinforced beams.

### Design Procedure

**Nominal shear stress:**
$$\tau_v = \frac{V_u}{bd}$$

**Design shear strength $\tau_c$** — from IS 456 Table 19 (depends on $p_t$ and concrete grade).

**Check:**
- If $\tau_v < 0.5\tau_c$ → **no shear reinforcement** required.
- If $0.5\tau_c \le \tau_v \le \tau_c$ → provide **minimum shear reinforcement**.
- If $\tau_v > \tau_c$ → design shear reinforcement for $V_{us} = (\tau_v - \tau_c)bd$.
- If $\tau_v > \tau_{c,max}$ → **redesign section**.

### Shear Reinforcement Types

**Vertical stirrups:**
$$V_{us} = \frac{0.87 f_y A_{sv} d}{s_v}$$

**Inclined stirrups (α ≥ 45°):**
$$V_{us} = \frac{0.87 f_y A_{sv} d}{s_v}(\sin\alpha + \cos\alpha)$$

**Bent-up bars:**
$$V_{us} = 0.87 f_y A_{sv} \sin\alpha$$

**Maximum spacing:**
- $s_v \le 0.75d$ and $\le 300$ mm (vertical stirrups)
- $s_v \le d$ and $\le 300$ mm (inclined stirrups)

### Minimum Shear Reinforcement

$$A_{sv} \ge \frac{0.4 b s_v}{0.87 f_y}$$

**Reason for minimum shear reinforcement:** Prevents sudden bursting of concrete, improves ductility, holds reinforcement together, improves dowel action, arrests longitudinal cracks, prevents tension failure due to shrinkage/thermal stresses.

### Critical Section for Shear

- For beams supported by **compressive reaction** → at distance **d** from face of support.
- Otherwise → at face of support.

### WHY does shear reinforcement use stirrups rather than just more concrete?

Stirrups (vertical/inclined) resist shear by acting as **tension members in a truss analogy** — they carry the diagonal tension that would otherwise cause diagonal cracks. They also: resist growth of inclined cracks, improve aggregate interlock, tie longitudinal bars in place, and (closed stirrups) resist torsion. Bent-up bars are less effective and give wider cracks, so stirrups are preferred.

---

## 7. Bond & Development Length

### Bond Stress

Longitudinal shear stress at the interface between concrete and steel, ensuring **strain compatibility** and **composite action**.

**Sources of bond strength:**
1. Adhesive power of concrete
2. Frictional resistance from shrinkage gripping
3. Mechanical interlocking from corrugations (deformed bars)

### Types of Bond

| Type | Where Critical | Formula |
|------|---------------|---------|
| Flexural bond | Where $V = dM/dx$ significant | $\tau_{bd} = V/(\sum o \cdot jd)$ |
| Anchorage bond | Bar force transfer | Development length |

### Development Length

$$L_d = \frac{0.87 f_y \phi}{4 \tau_{bd}}$$

Where $\phi$ = bar diameter, $\tau_{bd}$ = design bond stress.

**Modifications:**
- Deformed bars: $\tau_{bd}$ increases by **60%**
- Bars in compression: $\tau_{bd}$ increases by **25%** (end bearing helps)
- Bundled bars (2 in contact): $L_d$ increases by **10%**

### IS 456 Anchorage Requirements

| Member | Requirement |
|--------|-------------|
| Simply supported beam | $L_d \le \frac{M_1}{V} + L_0$ |
| Confined by compressive reaction | $L_d \le \frac{1.3 M_1}{V} + L_0$ |
| Cantilever tension steel | $L_d$ into support |
| Footing slab tension steel | $L_d$ from column face |

Where $L_0$ = anchorage beyond support centre = max($d_{eff}$, $12\phi$).

### Lap Lengths

| Condition | Lap Length |
|-----------|-----------|
| Compression | > $24\phi$ |
| Flexural tension | > $L_d$ or $30\phi$ |
| Direct tension | > $2L_d$ or $30\phi$ |

### Curtailment Rules

- Theoretical cut-off at point of contraflexure.
- Distance between theoretical & actual cut-off = max($d$, $12\phi$).
- Splices not at sections where BM > 50% of moment capacity.
- Lap splices not for bars > 36 mm diameter.

### WHY is development length important?

If the bar is not embedded long enough, the bond stress at the interface exceeds the bond strength, and the bar **pulls out** of the concrete — a sudden, brittle failure. Development length ensures the bar force is fully transferred to concrete through bond before the bar end, preventing pull-out failure. It's why hooks, bends, and proper anchorage are critical in detailing.

---

## 8. Slab Design

### Effective Span (IS 456)

| Support Type | Effective Span |
|--------------|----------------|
| Simply supported | min($l_0 + d$, $l_0 + w$) |
| Continuous (w < 600mm) | min($l_0 + d$, $l_0 + w$) |
| Cantilever | $l_0 + d/2$ or $l_0 + w/2$ |
| Frames | Centre-to-centre spacing |

### Deflection Control (Span/Effective Depth)

| Member | Span/Depth |
|--------|-----------|
| Cantilever | 7 |
| Simply supported | 20 |
| Continuous | 26 |
| Two-way slab (SS) | 35 (mild steel), 28 (HYSD) |
| Two-way slab (continuous) | 40 (mild steel), 32 (HYSD) |

### One-Way vs Two-Way Slab

| Criterion | One-Way | Two-Way |
|-----------|---------|---------|
| Aspect ratio | $l_y/l_x > 2$ | $l_y/l_x \le 2$ |
| Bending | Primarily shorter span | Both directions |
| Main steel | Shorter span | Both directions |
| Distribution steel | Longer span | — |

### Minimum Reinforcement

| Bar Type | Minimum |
|----------|---------|
| HYSD (Fe415) | 0.12% of $bD$ |
| Mild steel | 0.15% of $bD$ |

### Maximum Bar Diameter

- Main bars: $\le D/8$ (slab thickness/8)
- Reinforced brickwork slab: $\le 12$ mm

### Continuous Beam Coefficients (IS 456)

**Bending moment coefficients (DL + LL fixed):**

| Location | Coefficient |
|----------|-------------|
| Near middle of end span | $+1/12$ |
| At middle of interior span | $+1/16$ |
| At support next to end support | $-1/10$ |
| At other interior supports | $-1/12$ |

**Shear force coefficients (DL + LL fixed):**

| Location | Coefficient |
|----------|-------------|
| At end support | 0.4 |
| At support next to end (outer) | 0.6 |
| At support next to end (inner) | 0.55 |
| At all other interior supports | 0.5 |

### WHY are slabs not designed for shear?

Slabs have much smaller depth than beams, so the nominal shear stress $\tau_v = V/bd$ is very low and almost always below $0.5\tau_c$. Hence slabs are designed for **bending and deflection only**, with shear being automatically satisfied. If a two-way slab is unsafe in shear, increase the slab thickness.

---

## 9. Column Design

### Classification

| Type | Condition |
|------|-----------|
| Pedestal | $l_{eff} < 3 \times$ least lateral dimension |
| Short column | $l_{eff}/D < 12$ and $l_{eff}/B < 12$ |
| Long (slender) column | $l_{eff}/D \ge 12$ or $l_{eff}/B \ge 12$ |

### Minimum Eccentricity

$$e_{min} = \frac{l}{500} + \frac{D}{30} \ge 20 \text{ mm}$$

### Steel Limits (IS 456)

| Parameter | Value |
|-----------|-------|
| Minimum longitudinal steel | 0.8% of gross area |
| Maximum longitudinal steel | 6% of gross area (4% for practical placement) |
| Minimum bar diameter | 12 mm |
| Minimum bars (rectangular) | 4 |
| Minimum bars (circular) | 6 |
| Max spacing of longitudinal bars | 300 mm |

### Lateral Ties

- **Diameter:** max($\phi_{max}/4$, 6 mm)
- **Spacing:** min(least lateral dimension, $16\phi_{long}$, 300 mm)

**Purpose:** Prevent premature buckling of longitudinal bars, confine concrete in core (increases ductility & strength), resist shear & torsion.

### Short Column Under Axial Load

$$P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$$

**Helically reinforced column:**
$$P_u = 1.05(0.4 f_{ck} A_c + 0.67 f_y A_{sc})$$

### Long Column Reduction

$$C_r = 1.25 - \frac{l_{eff}}{48b}$$

### Interaction Curve (Axial + Bending)

- For small eccentricity, entire section in compression.
- For larger eccentricity, NA within section, $\varepsilon_u = 0.0035$ at highly compressed edge.
- As $P_u$ increases from zero, allowable moment first **increases** then **decreases** (interaction curve).

### WHY is "strong column - weak beam" preferred?

During earthquakes, columns must remain elastic to provide stability and strength. If beams yield first (weak beam), plastic hinges form at beam ends — desirable, ductile, and repairable. If columns fail first (weak column), the whole structure can collapse suddenly. IS 456/IS 13920 mandate strong-column-weak-beam design for earthquake resistance.

---

## 10. Footing Design

### Types

| Type | Use |
|------|-----|
| Isolated footing | Single column |
| Combined footing | Two columns (trapezoidal when width restricted) |
| Raft/mat | Many columns, weak soil |
| Strap footing | Eccentric column |

### Critical Sections

| Check | Location |
|-------|----------|
| Bending moment | At face of column |
| One-way shear | At distance **d** from column face |
| Two-way (punching) shear | At distance **d/2** from column face |

### Design Depth Governed By

1. Maximum bending moment
2. Maximum shear force
3. Punching shear

### WHY is punching shear critical in footings?

Punching shear (two-way shear) occurs along a perimeter at $d/2$ from the column face, where the column load punches through the footing slab. Because the shear perimeter is large but the shear stress is concentrated near the column, punching shear can govern the footing depth even when flexural and one-way shear checks pass. It's a brittle failure mode, so it must be checked carefully.

---

## 11. Prestressed Concrete

### Pre-tensioning vs Post-tensioning

| Aspect | Pre-tensioning | Post-tensioning |
|--------|----------------|-----------------|
| Transfer | By bond | By end anchorages |
| Concrete at tensioning | Not yet cast | Already cast & hardened |
| Suitable for | Precast, mass production | Cast-in-place, heavy members |
| Anchorage devices | Not required | Required |
| Losses | Higher (elastic shortening) | Lower |
| Min concrete grade | M40 | M30 |

### Advantages of Prestressed Concrete

- No cracking under service loads
- More ductility
- Less deflection
- Higher shear resistance
- Higher span/depth ratio possible

### Losses of Prestress

| Loss | Pre-tensioning | Post-tensioning |
|------|----------------|-----------------|
| Elastic shortening | Yes | Partial (sequential) |
| Friction | No | Yes |
| Anchorage slip | No | Yes |
| Creep of concrete | Yes | Yes |
| Shrinkage | Yes | Yes |
| Relaxation of steel | Yes | Yes |
| **Total** | **~18%** | **~15%** |

### Friction Loss (Post-tensioning)

$$P_x = P_0 e^{-(\mu\alpha + kx)} \approx P_0(1 - \mu\alpha - kx)$$

Where $\mu$ = curvature friction coefficient, $k$ = wobble coefficient, $\alpha$ = cumulative angle (radians).

### Analysis Concepts

1. **Stress concept:** $\sigma = P/A \pm M/Z$
2. **Load balancing:** Cable profile matches BMD (parabolic for UDL)
3. **Strength concept:** Pressure/thrust line analysis

### WHY use high-strength steel & concrete in prestressing?

Prestress losses are large (160-200 N/mm²). High-strength steel is needed so that after all losses, sufficient prestress remains. High-strength concrete has higher modulus of elasticity, smaller ultimate creep strain, and is less liable to shrinkage cracks — all reducing prestress loss. Ordinary mild steel would lose too much prestress to be effective.

---

## 12. IS 456:2000 Code Provisions Summary

| Parameter | Value |
|-----------|-------|
| Minimum grade for RCC | M20 |
| Minimum grade in sea water (RCC) | M30 |
| Partial safety factor (concrete) | 1.5 |
| Partial safety factor (steel) | 1.15 |
| Max strain in concrete (flexure) | 0.0035 |
| Max strain in concrete (axial) | 0.002 |
| Min tension steel (beams) | $0.85bd/f_y$ |
| Max tension steel | 4% of $bD$ |
| Min shear reinforcement | $0.4 b s_v /(0.87 f_y)$ |
| Min longitudinal steel (columns) | 0.8% of gross |
| Max longitudinal steel (columns) | 6% of gross |
| Nominal cover (slab) | 15 mm |
| Nominal cover (beam) | 25 mm |
| Nominal cover (column) | 40 mm |
| Nominal cover (footing) | 75 mm |
| Min cover (sea water, beam) | 50 mm |
| Max moment redistribution | 30% |
| Deflection limit (final) | Span/250 |
| Deflection limit (after partitions) | Span/350 or 20 mm |

### Related IS Codes

| Code | Purpose |
|------|---------|
| IS 456:2000 | Plain & reinforced concrete |
| IS 875 | Load calculation |
| IS 1893 | Earthquake resistant design |
| IS 1343 | Prestressed concrete |
| IS 3370 | Liquid retaining structures |
| IS 2502 | Bar bending schedule |
| IS 516 | Concrete cube testing |
| SP 16 | Design aids for IS 456 |

---

## 13. Worked Numerical Examples

### Example 1: Singly Reinforced Beam Design

**Problem:** Design a simply supported beam for $M_u = 150$ kN·m. $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $b = 250$ mm.

**Solution:**
1. $M_{u,lim} = 0.138 f_{ck} b d^2 = 0.138 \times 25 \times 250 \times d^2 = 862.5 d^2$ N·mm
2. Required $d = \sqrt{150 \times 10^6 / 862.5} = \sqrt{173913} = 417$ mm → use $d = 450$ mm
3. Since $M_u < M_{u,lim}$, section is under-reinforced.
4. $A_{st} = \frac{M_u}{0.87 f_y (d - 0.42 x_u)}$
5. First find $x_u$: assume $x_u = 0.48d = 216$ mm (trial)
6. $A_{st} = \frac{150 \times 10^6}{0.87 \times 415 \times (450 - 0.42 \times 216)} = \frac{150 \times 10^6}{361 \times 359.3} = 1153$ mm²
7. Check $x_u = \frac{0.87 \times 415 \times 1153}{0.36 \times 25 \times 250} = \frac{416,000}{2250} = 185$ mm < $x_{u,max} = 216$ mm ✓
8. Use **4 bars of 20 mm** ($A_{st} = 1256$ mm²)

**Interview follow-up:** What if $M_u > M_{u,lim}$? → Redesign with larger section OR use doubly reinforced section.

### Example 2: Shear Reinforcement

**Problem:** Beam with $V_u = 200$ kN, $b = 250$ mm, $d = 450$ mm, $f_{ck} = 25$ MPa, $p_t = 1.1\%$, $f_y = 415$ MPa.

**Solution:**
1. $\tau_v = \frac{V_u}{bd} = \frac{200 \times 10^3}{250 \times 450} = 1.78$ N/mm²
2. From IS 456 Table 19, for M25 & $p_t = 1.1\%$: $\tau_c \approx 0.62$ N/mm²
3. $\tau_{c,max}$ for M25 = 3.1 N/mm². Since $\tau_v < \tau_{c,max}$ ✓
4. Since $\tau_v > \tau_c$: $V_{us} = (\tau_v - \tau_c)bd = (1.78 - 0.62) \times 250 \times 450 = 130,500$ N = 130.5 kN
5. For 2-legged 8mm stirrups: $A_{sv} = 2 \times 50.3 = 100.6$ mm²
6. $s_v = \frac{0.87 f_y A_{sv} d}{V_{us}} = \frac{0.87 \times 415 \times 100.6 \times 450}{130,500} = 125$ mm
7. Check max spacing: min($0.75d = 337.5$, 300) = 300 mm. Use $s_v = 125$ mm ✓

**Interview follow-up:** Why is $\tau_{c,max}$ important? → It prevents diagonal compression failure (crushing of concrete struts).

### Example 3: Development Length

**Problem:** Find development length for Fe415, 20 mm bar in M25 concrete. $\tau_{bd} = 1.4$ N/mm² (M25, plain bar).

**Solution:**
1. $L_d = \frac{0.87 f_y \phi}{4 \tau_{bd}} = \frac{0.87 \times 415 \times 20}{4 \times 1.4} = \frac{7221}{5.6} = 1289$ mm
2. For deformed bar: $\tau_{bd} = 1.6 \times 1.4 = 2.24$ N/mm²
3. $L_d = \frac{7221}{4 \times 2.24} = 806$ mm
4. Use $L_d \approx 810$ mm (deformed bar)

**Interview follow-up:** What happens if $L_d$ cannot be provided? → Provide hooks/bends, increase bar diameter reduction, or use mechanical anchorages.

### Example 4: Short Column

**Problem:** Design a short column for $P_u = 1500$ kN. $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $D = 400$ mm.

**Solution:**
1. Assume $A_{sc} = 1\%$ of $A_g$: $A_{sc} = 0.01 \times 400^2 = 1600$ mm²
2. $A_c = A_g - A_{sc} = 160,000 - 1600 = 158,400$ mm²
3. $P_u = 0.4 \times 25 \times 158,400 + 0.67 \times 415 \times 1600 = 1,584,000 + 444,880 = 2,028,880$ N = 2029 kN > 1500 ✓
4. Reduce $A_{sc}$: Try 0.5% → $A_{sc} = 800$ mm²
5. $P_u = 0.4 \times 25 \times 159,200 + 0.67 \times 415 \times 800 = 1,592,000 + 222,440 = 1,814,440$ N = 1814 kN > 1500 ✓
6. Use **8 bars of 12 mm** ($A_{sc} = 904$ mm²)

**Interview follow-up:** Why is minimum 0.8% steel required? → To ensure nominal flexural resistance and prevent yielding due to creep & shrinkage effects.

---

## 14. 🎤 Interview Q&A

### A. Basic Concept Questions

1. **What is the difference between limit state and working stress method?**
   - WSM: elastic, allowable stresses, single FOS. LSM: partial safety factors, checks collapse + serviceability, more economical.

2. **What are the assumptions in limit state flexural design?**
   - Plane sections remain plane, max concrete strain 0.0035, failure by concrete crushing, max principal strain theory.

3. **What is the difference between under-reinforced, balanced, and over-reinforced sections?**
   - Under: steel yields first (ductile, preferred). Balanced: simultaneous. Over: concrete crushes first (brittle, avoid).

4. **What is the significance of $x_{u,max}/d$?**
   - Limiting NA depth ratio ensuring under-reinforced behavior. Fe415: 0.48, Fe500: 0.46.

5. **What is development length and why is it needed?**
   - Length to transfer bar force to concrete via bond, preventing pull-out failure.

### B. WHY Questions

1. **Why is concrete reinforced with steel?**
   - Concrete weak in tension (~10% of compression); steel carries tension, concrete carries compression → composite action.

2. **Why is under-reinforced design preferred?**
   - Ductile failure with warning (steel yields first) vs brittle sudden failure of over-reinforced.

3. **Why is limit state design preferred over working stress?**
   - Partial safety factors give consistent reliability; explicit serviceability checks; more economical.

4. **Why is minimum shear reinforcement required even when shear is low?**
   - Prevents sudden bursting, improves ductility, holds reinforcement, improves dowel action, resists shrinkage/thermal cracking.

5. **Why use high-strength steel & concrete in prestressing?**
   - Large prestress losses (160-200 N/mm²) require high initial stress; high-strength concrete reduces creep/shrinkage losses.

### C. WHAT-IF Questions

1. **What if $M_u > M_{u,lim}$?**
   - Redesign with larger section, OR use doubly reinforced section.

2. **What if $\tau_v > \tau_{c,max}$?**
   - Redesign the section (increase depth/width) — cannot be fixed with shear reinforcement alone.

3. **What if the slab is unsafe in shear?**
   - Increase slab thickness (slabs not normally designed for shear).

4. **What if development length cannot be provided?**
   - Provide hooks/bends, use smaller diameter bars, or mechanical anchorages.

5. **What if a column is slender (long)?**
   - Apply reduction coefficient $C_r = 1.25 - l_{eff}/48b$ and additional moment due to eccentricity.

### D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Working stress | Limit state | Elastic vs probabilistic |
| Under-reinforced | Over-reinforced | Ductile vs brittle failure |
| Singly reinforced | Doubly reinforced | No vs compression steel |
| One-way slab | Two-way slab | $l_y/l_x > 2$ vs $\le 2$ |
| Short column | Long column | $l_{eff}/D < 12$ vs $\ge 12$ |
| Pre-tensioning | Post-tensioning | Bond vs anchorage transfer |
| T-beam | Rectangular beam | Flange carries compression |
| Vertical stirrups | Bent-up bars | Stirrups more effective |

### E. Numerical Questions

1. Find $M_{u,lim}$ for $f_{ck}=25$, $b=250$, $d=450$. → $0.138 \times 25 \times 250 \times 450^2 = 174.7$ kN·m
2. Find $L_d$ for Fe415, 16mm bar, M25. → $\approx 645$ mm (deformed)
3. Find $P_u$ for short column, $A_{sc}=1\%$, $D=400$. → $\approx 2029$ kN
4. Find stirrup spacing for given $V_{us}$. → $s_v = 0.87 f_y A_{sv} d / V_{us}$

### F. Rapid-Fire Questions

1. Max strain in concrete (flexure)? → 0.0035
2. Min grade for RCC? → M20
3. $\gamma_m$ for concrete? → 1.5
4. $\gamma_m$ for steel? → 1.15
5. $x_{u,max}/d$ for Fe415? → 0.48
6. Min tension steel in beams? → $0.85bd/f_y$
7. Max tension steel? → 4% of $bD$
8. Min longitudinal steel in columns? → 0.8%
9. Max longitudinal steel in columns? → 6%
10. Nominal cover for column? → 40 mm
11. Nominal cover for footing? → 75 mm
12. Max moment redistribution? → 30%
13. Deflection limit? → Span/250
14. One-way slab if $l_y/l_x$? → > 2
15. Min steel in slabs (HYSD)? → 0.12%
16. Development length formula? → $0.87 f_y \phi / 4\tau_{bd}$
17. Lap length in compression? → > 24φ
18. Lap length in flexural tension? → > $L_d$ or 30φ
19. Short column if $l_{eff}/D$? → < 12
20. Prestressed concrete code? → IS 1343

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the IS 456 stress block parameters.**
   - Parabolic-rectangular block: parabolic up to 0.002 strain, rectangular to 0.0035. Average stress 0.67$f_{ck}$/1.5 = 0.446$f_{ck}$, centroid at 0.42$x_u$ from top.

2. **Explain the interaction curve for columns.**
   - Plot of $P_u$ vs $M_u$ capacity. For small eccentricity, entire section in compression. As eccentricity increases, NA moves inward, moment capacity first increases then decreases.

3. **What is the truss analogy for shear design?**
   - Concrete acts as diagonal compression struts, stirrups as vertical tension ties, longitudinal steel as chords. Stirrups carry the diagonal tension.

4. **Explain concordant cable profile in continuous prestressed beams.**
   - A cable profile that produces a pressure line coincident with the profile itself, generating no reactions at supports. Used for indeterminate structures (load balancing is for determinate).

5. **What is the Hoyer effect?**
   - In pre-tensioned members, the prestressing force becomes zero at the wire end due to bond transfer; transmission length $L_t$ is where full prestress develops.

---

## 15. High-Value Interview Answers

### High-Value Q1: "Design a simply supported RCC beam — walk me through it."

**30-second answer:**
"First, compute the factored moment $M_u = 1.5 \times$ (working moment). Assume a width and find required depth from $M_{u,lim} = 0.138 f_{ck} b d^2$. If $M_u < M_{u,lim}$, design as singly reinforced: find $A_{st} = M_u/(0.87 f_y (d - 0.42x_u))$. Check $x_u < x_{u,max}$ for under-reinforced behavior. Then check shear: $\tau_v = V_u/bd$, compare with $\tau_c$, provide stirrups if needed. Finally check development length and deflection."

### High-Value Q2: "What is the difference between one-way and two-way slabs?"

**30-second answer:**
"A slab is one-way if $l_y/l_x > 2$ — it bends primarily in the shorter direction, with main steel in the short span and distribution steel in the long span. A slab is two-way if $l_y/l_x \le 2$ — it bends in both directions, with main steel in both directions. Two-way slabs have higher span/depth ratios (35/28 vs 20 for one-way SS) because load is shared in two directions."

### High-Value Q3: "Why is strong-column-weak-beam important?"

**30-second answer:**
"During earthquakes, columns must remain elastic to provide stability. If beams yield first, plastic hinges form at beam ends — ductile, repairable, and the structure survives. If columns fail first, the whole structure can collapse suddenly. IS 13920 mandates strong-column-weak-beam design."

---

## 16. Software Connection

| Tool | Application |
|------|-------------|
| STAAD.Pro | RCC beam/column design & analysis |
| ETABS | Building analysis & RCC design |
| SAFE | Slab & foundation design |
| RCDC | RC detailing & bar bending schedules |
| AutoCAD/Revit | Detailing & drawings |
| Tekla | Concrete detailing |
| SP 16 (manual) | Design aids for IS 456 |

**Hand-calc verification:** Always verify software output with hand calculations for critical sections (max moment, max shear, development length). Software gives the answer; you must validate it.

---

## 17. 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Concrete properties     →  Limit state flexure         →  Flanged beam analysis      →  Under vs over-reinforced
Stress-strain curve     →  Singly reinforced design    →  Doubly reinforced design   →  Xu,max/d limits
Working stress method   →  Shear design & stirrups     →  Torsion design             →  Truss analogy
Slab basics             →  One-way & two-way slabs     →  Yield line theory          →  Span/depth ratios
Column basics           →  Short column design         →  Long column & interaction  →  Strong-column-weak-beam
Footing basics          →  Isolated footing design     →  Combined & raft footings   →  Punching shear
Prestress intro         →  Pre vs post tensioning      →  Losses & cable profiles    →  Concordant profiles
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `STRUCTURAL` `RCC` `IS 456`

---

## 18. 🔗 Cross-Links

- [`structures.md`](../structures/structures.md) — Structural analysis & steel design companion
- [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — Stress, bending, shear fundamentals
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Foundation & soil-structure interaction
- [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) — Construction management
- [`civil-engineering-foundations.md`](../fundamentals/civil-engineering-foundations.md) — Foundation overview

---

## 19. 📋 Quick Revision Checklist

- [ ] Concrete stress-strain: linear to 10-15% ultimate, max strain 0.0035
- [ ] $E_c = 5000\sqrt{f_{ck}}$
- [ ] WSM vs LSM: partial safety factors, serviceability check
- [ ] $\gamma_m$: concrete 1.5, steel 1.15
- [ ] $M_{u,lim} = 0.138 f_{ck} b d^2$ (Fe415)
- [ ] Under-reinforced: $x_u < x_{u,max}$, ductile failure
- [ ] $x_{u,max}/d$: Fe250=0.53, Fe415=0.48, Fe500=0.46
- [ ] Shear: $\tau_v = V_u/bd$, compare with $\tau_c$, $\tau_{c,max}$
- [ ] Stirrup spacing: min(0.75d, 300mm)
- [ ] $L_d = 0.87 f_y \phi / 4\tau_{bd}$
- [ ] Lap: compression > 24φ, flexural tension > $L_d$ or 30φ
- [ ] One-way slab: $l_y/l_x > 2$
- [ ] Min slab steel: 0.12% (HYSD), 0.15% (mild)
- [ ] Column: short if $l_{eff}/D < 12$
- [ ] Column steel: 0.8% min, 6% max
- [ ] $P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$
- [ ] Footing: BM at column face, one-way shear at d, punching at d/2
- [ ] Prestress losses: pre-tensioning 18%, post-tensioning 15%
- [ ] Min grade: M20 RCC, M30 sea water, M30/M40 prestress

---

## References

* IS 456:2000 — Plain and Reinforced Concrete — Code of Practice
* IS 1343:2012 — Prestressed Concrete — Code of Practice
* IS 875 — Code of Practice for Design Loads
* IS 1893:2016 — Criteria for Earthquake Resistant Design
* SP 16 — Design Aids for Reinforced Concrete to IS 456
* [`structures.md`](../structures/structures.md) — Structural design companion
* [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — SOM fundamentals

# Structures

## Scope

Structural engineering for civil placements covers the analysis and design of load-carrying systems. Breadth knowledge in strength of materials, reinforced concrete, steel structures, and structural analysis is expected for core design roles.

> **Related topics:** [`geotechnical.md`](../geotechnical/geotechnical.md) · [`../core/hwre/water_supply/water-supply.md`](../../core/hwre/water_supply/water-supply.md)

---

## Strength of Materials (SOM)

### Stress & Strain

| Quantity | Formula | Notes |
|----------|---------|-------|
| Normal stress | $\sigma = P/A$ | Force per unit area |
| Shear stress | $\tau = V/A$ | Force parallel to area |
| Hooke's law (axial) | $\sigma = E\varepsilon$ | $E$ = Young's modulus |
| Shear law | $\tau = G\gamma$ | $G$ = Shear modulus |
| Relationship | $G = E/[2(1+\nu)]$ | $\nu$ = Poisson's ratio |
| Volumetric strain | $\varepsilon_v = \varepsilon_x + \varepsilon_y + \varepsilon_z$ | For 3D stress state |

**Stress transformation (Mohr's circle):**
$$\sigma_\theta = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\theta + \tau_{xy}\sin 2\theta$$
$$\tau_\theta = -\frac{\sigma_x - \sigma_y}{2}\sin 2\theta + \tau_{xy}\cos 2\theta$$

**Principal stresses:**
$$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

### Bending of Beams

**Flexure formula:**
$$\sigma = \frac{M \cdot y}{I} = \frac{M}{Z}$$

Where $Z = I/y_{max}$ = section modulus

**Shear stress distribution:**
$$\tau = \frac{V \cdot Q}{I \cdot b}$$

Where $Q = \int y \, dA$ = first moment of area above the point

**Key section properties:**

| Section | $I$ | $Z$ |
|---------|-----|-----|
| Rectangle ($b \times d$) | $bd^3/12$ | $bd^2/6$ |
| Circle (dia $D$) | $\pi D^4/64$ | $\pi D^3/32$ |
| Triangle ($b \times h$) | $bh^3/36$ | $bh^2/24$ |

**Deflection methods:**
- **Double integration:** $EI \frac{d^2y}{dx^2} = M(x)$
- **Moment-area:** $\theta_2 - \theta_1 = \int_1^2 \frac{M}{EI} dx$, $t_{2/1} = \int_1^2 \frac{M}{EI} \bar{x} dx$
- **Conjugate beam:** M/EI loading on conjugate beam gives slope and deflection
- **Macaulay's method:** Discontinuity functions for loading

### Columns & Buckling

**Euler's critical load:**
$$P_{cr} = \frac{\pi^2 EI}{(KL)^2}$$

| End Condition | $K$ |
|---------------|-----|
| Fixed-Fixed | 0.5 |
| Fixed-Pinned | 0.7 |
| Pinned-Pinned | 1.0 |
| Fixed-Free | 2.0 |

**Slenderness ratio:** $\lambda = KL/r$ where $r = \sqrt{I/A}$

**Rankine-Gordon formula:**
$$\frac{1}{P_R} = \frac{1}{P_C} + \frac{1}{P_E}$$

### Energy Methods

- **Strain energy:** $U = \int \frac{\sigma^2}{2E} dV$
- **Castigliano's 2nd theorem:** $\delta_i = \frac{\partial U}{\partial P_i}$ (deflection at point $i$)
- **Unit load method:** $\delta = \int \frac{M m}{EI} dx$

---

## Structural Analysis

### Moment Distribution (Hardy Cross)
1. Compute fixed-end moments (FEMs)
2. Compute distribution factors: $DF_i = K_i / \sum K$
3. Release and distribute unbalanced moments
4. Carry over half to each end
5. Iterate until convergence

### Influence Lines
- **Müller-Breslau principle:** Remove constraint, apply unit displacement → influence line shape
- Use for maximum shear, moment, and reactions under moving loads

---

## Reinforced Cement Concrete (RCC) — IS 456:2000

### Key Provisions

| Parameter | IS 456 Value |
|-----------|-------------|
| Minimum grade | M20 (for RCC) |
| Partial safety factor (materials) | $\gamma_m = 1.5$ |
| Partial safety factor (loads) | $\gamma_f = 1.5$ (DL), 1.5 (LL), 0.9/1.5 (combo) |
| Modular ratio | $m = 280/(3\sigma_{cbc})$ |
| Min tension steel | $0.85bd/f_y$ |
| Max tension steel | $4\%$ of gross area |
| Min shear reinforcement | $0.4\%$ of gross area |

### Load Combinations (IS 456 Table 18)

| Combination | Formula |
|-------------|---------|
| DL + LL | $1.5(DL + LL)$ |
| DL + WL | $0.9DL + 1.5WL$ or $1.2DL + 1.5WL$ |
| DL + LL + WL | $1.2DL + 1.5LL + \pm 1.0WL$ |

### Beam Design (Singly Reinforced — IS 456)

**Balanced section (limit state):**
$$M_{u,lim} = 0.138 f_{ck} b d^2$$ (for Fe415)

**Moment capacity:**
$$M_u = 0.87 f_y A_s (d - 0.42 x_u)$$

**Neutral axis depth:** $x_u = 0.87 f_y A_s / (0.36 f_{ck} b)$

**Under-reinforced:** $x_u < x_{u,max}$ → steel yields first (preferred)
**Over-reinforced:** $x_u > x_{u,max}$ → concrete crushes first (brittle, avoid)

### Shear Design (IS 456)

**Nominal shear stress:** $\tau_v = V_u / (bd)$

**Design shear strength:** $\tau_c$ from Table 19 of IS 456 (depends on $p_t$ and concrete grade)

**If $\tau_v > \tau_c$:** Provide shear reinforcement
$$A_{sv}/(s_v) = 0.87 f_y A_{sv} / (0.87 f_y s_v) \geq V_u - \tau_c b d$$

### Column Design (IS 456)

**Short column (axial load):**
$$P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$$

**Minimum eccentricity:** $e_{min} = L/500 + D/30$ (≥ 20 mm)

**Long column:** Additional moment $M_{add} = P_u \cdot e_{add}$

---

## Steel Structures — IS 800:2007

### Key Provisions

| Parameter | IS 800 Value |
|-----------|-------------|
| Grades | E250, E350, E410, E450, E550 |
| Partial safety factor (materials) | $\gamma_{M0} = 1.1$ (yield), $\gamma_{M1} = 1.25$ (ultimate) |
| Design method | Limit state method |

### Tension Members
$$T_{dn} = 0.9 A_n f_u / \gamma_{M1}$$ (net section fracture)
$$T_{dg} = A_g f_y / \gamma_{M0}$$ (gross section yield)

### Compression Members
$$P_d = (A_e f_{cd}) / \gamma_{M0}$$
where $f_{cd}$ depends on buckling class and slenderness ratio

### Bolted Connections

**Shear capacity of bolt:** $V_{dsb} = f_{ub} \cdot n_n \cdot A_{nb} / (\sqrt{3} \cdot \gamma_{Mb})$

**Bearing capacity:** $V_{dpb} = 2.5 k_b d t f_u / \gamma_{Mb}$

### Welded Connections

**Fillet weld:** $f_{wd} = f_u / (\sqrt{3} \cdot \gamma_{Mw})$

---

## Worked Examples

### Example 1: Beam Design (IS 456)
**Problem:** Design a simply supported beam for $M_u = 150$ kN·m. $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $b = 250$ mm.

**Solution:**
1. $M_{u,lim} = 0.138 \times 25 \times 250 \times d^2 = 862.5 d^2$ (N·mm)
2. Required $d = \sqrt{150 \times 10^6 / 862.5} = 418$ mm → use $d = 450$ mm
3. $x_u = 0.87 f_y A_s / (0.36 f_{ck} b)$
4. $A_s = M_u / (0.87 f_y (d - 0.42 x_{u,max})) = 150 \times 10^6 / (0.87 \times 415 \times (450 - 0.42 \times 217))$
5. $A_s = 150 \times 10^6 / (361 \times 359) = 1158$ mm² → Use 4 bars of 20 mm ($A_s = 1256$ mm²)

### Example 2: Column Design (IS 456)
**Problem:** Design a short column for $P_u = 1500$ kN. $f_{ck} = 25$ MPa, $f_y = 415$ MPa. $D = 400$ mm.

**Solution:**
1. Assume $A_{sc} = 1\%$ of $A_g$: $A_{sc} = 0.01 \times 400^2 = 1600$ mm²
2. $A_c = A_g - A_{sc} = 160000 - 1600 = 158400$ mm²
3. $P_u = 0.4 \times 25 \times 158400 + 0.67 \times 415 \times 1600 = 1584000 + 444080 = 2028$ kN > 1500 ✓
4. Reduce $A_{sc}$: Try 0.5% → $A_{sc} = 800$ mm²
5. $P_u = 0.4 \times 25 \times 159200 + 0.67 \times 415 \times 800 = 1592000 + 222040 = 1814$ kN > 1500 ✓
6. Use 8 bars of 12 mm ($A_{sc} = 904$ mm²)

---

## 🎤 Interview Q&A

### Q1: What is the difference between limit state method and working stress method?
**A:** Working stress method (WSM): uses allowable stresses (factor of safety on material strength), assumes linear elastic behavior, used for serviceability conditions. Limit state method (LSM): uses partial safety factors on loads and materials, considers both collapse (strength) and serviceability (deflection, cracking), more realistic and economical. IS 456 and IS 800 both use LSM.

### Q2: What are the assumptions in Euler's column formula?
**A:** (1) Column is initially straight, (2) Load is axially applied, (3) Material is homogeneous and isotropic, (4) Stress is within elastic limit (Hooke's law valid), (5) Column fails by buckling (not crushing), (6) Cross-section is uniform, (7) Self-weight is neglected. Valid only for long columns ($\lambda > \lambda_{critical}$).

### Q3: What is the difference between balanced, under-reinforced, and over-reinforced sections?
**A:** Balanced: Steel yields simultaneously with concrete crushing ($x_u = x_{u,max}$). Under-reinforced: Steel yields first ($x_u < x_{u,max}$) → ductile failure with warning (preferred design). Over-reinforced: Concrete crushes first ($x_u > x_{u,max}$) → brittle failure without warning (avoid). IS 456 recommends designing as under-reinforced.

### Q4: What is the significance of $x_{u,max}/d$ ratio?
**A:** $x_{u,max}/d$ is the limiting neutral axis depth ratio that ensures under-reinforced behavior. For Fe415: $x_{u,max}/d = 0.48$. For Fe500: $x_{u,max}/d = 0.46$. If actual $x_u/d$ exceeds this, the section is over-reinforced. It ensures steel yields before concrete crushes, providing ductile failure.

### Q5: Explain the moment distribution method.
**A:** (1) Compute fixed-end moments. (2) Calculate distribution factors $DF_i = K_i/\sum K$ at each joint. (3) Release locked joints (unlock one at a time), distribute unbalanced moment proportionally to DF. (4) Carry over half the distributed moment to each far end. (5) Repeat until convergence. It's iterative but systematic for continuous beams and frames.

---

## Design Codes & Standards

| Code | Topic |
|------|-------|
| **IS 456:2000** | Plain and reinforced concrete |
| **IS 800:2007** | General construction in steel |
| **IS 1893:2016** | Earthquake resistant design |
| **IS 3370** | Concrete structures for storage of liquids |
| **SP 16** | Design aids for reinforced concrete to IS 456 |

---

## Structural Software

| Tool | Application |
|------|-------------|
| SAP2000 | General-purpose structural analysis and design |
| ETABS | Building analysis and design |
| STAAD.Pro | Structural analysis and design |
| Tekla Structures | Steel and concrete detailing |
| midas Civil | Bridge and civil structural analysis |
| RISA-3D | 3D structural analysis for buildings and bridges |
| Dlubal RFEM | 3D finite element structural analysis |
| OpenSees | Open-source nonlinear structural and geotechnical simulation |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Stress/strain         →  Mohr's circle               →  Plastic analysis            →  Stress transformation
Bending of beams      →  Deflection methods           →  Indeterminate structures    →  Moment-area method
Columns & buckling    →  Influence lines              →  Matrix structural analysis  →  Euler vs Rankine
Torsion               →  Moment distribution           →  Dynamic analysis           →  Effective length factors
RCC basics            →  Limit state design (IS 456)  →  Detailing & seismic design  →  Xu,max/d limits
Steel basics          →  Design of connections        →  Plate girder design         →  IS 800 provisions
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `STRUCTURAL`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What is Mohr's circle and how do you construct it?
2. What are the IS 456 limit state design provisions?
3. Explain the moment distribution method.

### B. WHY Questions
1. **Why** is the effective length factor $K$ different for various end conditions?
   - Because the boundary conditions determine the buckling mode shape. Fixed ends restrain rotation, reducing effective length; free ends allow rotation and translation, increasing effective length.

2. **Why** does IS 456 limit the neutral axis depth $x_{u,max}/d$?
   - To ensure under-reinforced behavior (tension steel yields before concrete crushes), giving ductile failure with warning rather than sudden brittle failure.

3. **Why** is limit state design preferred over working stress design?
   - WSD uses arbitrary factors of safety. LSD applies partial safety factors to loads and materials separately, giving more consistent reliability across different loading conditions.

### D. Comparison
| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Working stress | Limit state | Elastic vs ultimate |
| RCC | Steel | Concrete vs steel construction |
| IS 456 | IS 800 | Concrete code vs steel code |
| Euler | Rankine | Elastic buckling vs empirical |

---

## 🎤 Interview Answer Format

### High-Value Q: "What is the difference between working stress and limit state design?"

**30-second answer:**
"Working stress design uses elastic analysis with a single factor of safety. Limit state design applies partial safety factors to loads (γf) and materials (γm), checks both ultimate limit state (ULS — strength) and serviceability limit state (SLS — deflection, cracking). IS 456 uses limit state."

---

## 🔗 Cross-Links

- [`geotechnical.md`](../geotechnical/geotechnical.md) — Foundation design
- [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) — Construction management
- [`hydraulics.md`](../hwre/hydraulics/hydraulics.md) — Hydraulic structures

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`geotechnical.md`](../geotechnical/geotechnical.md) — Foundation design companion

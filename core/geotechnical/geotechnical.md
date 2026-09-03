# Geotechnical Engineering

## Scope

Geotechnical engineering applies soil mechanics and rock mechanics to the design of foundations, slopes, retaining structures, and earth-supported systems.

> **Related topics:** [`structures.md`](../structures/structures.md) · [`../core/hwre/irrigation/irrigation-engineering.md`](../../core/hwre/irrigation/irrigation-engineering.md)

---

## Soil Mechanics Fundamentals

### Soil Properties & Classification

| Property | Test | Use |
|----------|------|-----|
| Grain-size distribution | Sieve + hydrometer | Classification, permeability estimation |
| Liquid limit (LL) | Casagrande cup | Consistency, compressibility |
| Plastic limit (PL) | Roll test | Consistency |
| Plasticity index | PI = LL − PL | Clay behavior, A-line classification |
| Water content | Oven drying | Phase relationships |

**USCS Classification:**

| Group | Symbol | Criteria |
|-------|--------|----------|
| Gravel | GW, GP | >50% retained on No.4 |
| Sand | SW, SP | >50% passes No.4, >50% coarse |
| Silt | ML, MH | Passes No.200, PI < 7 or LL > 50 |
| Clay | CL, CH | Passes No.200, PI > 7, above A-line |
| Organic | OL, OH, PT | High organic content |

### Phase Relationships
$$e = \frac{V_v}{V_s}, \quad n = \frac{V_v}{V}, \quad S = \frac{V_w}{V_v}$$
$$Se = wG_s, \quad \gamma_{bulk} = \frac{G_s + Se}{1+e}\gamma_w, \quad \gamma_{dry} = \frac{G_s}{1+e}\gamma_w$$

### Permeability & Seepage

**Darcy's law:** $v = ki$ (discharge velocity), $q = kiA$

**Constant head test:** $k = \frac{QL}{Aht}$

**Falling head test:** $k = \frac{aL}{At}\ln\frac{h_1}{h_2}$

**Flow nets:**
- Equipotential lines and flow lines form curvilinear squares
- $q = kH\frac{N_f}{N_d}$ (seepage quantity)
- Uplift pressure at any point = $\gamma_w \times$ (remaining head)

### Compaction

| Test | Energy | Purpose |
|------|--------|---------|
| Standard Proctor | 2.6 kN·m/L | Baseline compaction |
| Modified Proctor | 5.5 kN·m/L | High compaction requirement |

**Key relationship:** $\gamma_d = f(w)$ curve → peak at OMC (Optimum Moisture Content)

### Consolidation — Terzaghi's Theory

**Governing equation:**
$$\frac{\partial u}{\partial t} = c_v \frac{\partial^2 u}{\partial z^2}$$

**Settlement calculation:**
$$S_c = \frac{C_c H}{1+e_0} \log\frac{\sigma'_0 + \Delta\sigma}{\sigma'_0}$$ (normally consolidated)
$$S_c = \frac{C_r H}{1+e_0} \log\frac{\sigma'_0 + \Delta\sigma}{\sigma'_0}$$ (overconsolidated, if $\sigma'_0 + \Delta\sigma < \sigma'_c$)

**Time rate:**
$$T_v = \frac{c_v t}{H_{dr}^2}$$
- $T_v = 0.2$ → 50% consolidation
- $T_v = 0.848$ → 90% consolidation

### Shear Strength — Mohr-Coulomb

$$\tau_f = c' + \sigma' \tan\phi'$$ (effective stress, drained)
$$\tau_f = c_u$$ (undrained, $\phi_u = 0$ for saturated clay)

**Key parameters:**

| Test | Conditions | Output |
|------|-----------|--------|
| UU (Unconsolidated Undrained) | Quick, no drainage | $c_u$ |
| CU (Consolidated Undrained) | Consolidate first, then shear | $c', \phi', c_{cu}, \phi_{cu}$ |
| CD (Consolidated Drained) | Full drainage during shear | $c', \phi'$ |

---

## Foundation Engineering

### Bearing Capacity — Terzaghi

$$q_u = cN_c + qN_q + \frac{1}{2}\gamma BN_\gamma$$

**Shape factors (Meyerhof):**

| Foundation | $s_c$ | $s_q$ | $s_\gamma$ |
|-----------|-------|-------|-----------|
| Strip | 1.0 | 1.0 | 1.0 |
| Square | 1.3 | 1.2 | 0.8 |
| Circle | 1.3 | 1.2 | 0.6 |
| Rectangular | $1+0.3(B/L)$ | $1+0.3(B/L)$ | $1-0.4(B/L)$ |

**Net bearing capacity:** $q_{nu} = q_u - \gamma D_f$

**Safe bearing pressure:** $q_s = q_{nu}/F + \gamma D_f$ ($F$ = factor of safety, typically 3)

### Settlement Analysis
- **Immediate settlement:** $S_i = \frac{qB(1-\nu^2)}{E_u} I_f$
- **Consolidation settlement:** $S_c = \frac{C_c H}{1+e_0}\log\frac{\sigma'_0+\Delta\sigma}{\sigma'_0}$
- **Secondary compression:** $S_s = C_\alpha H \log(t/t_p)$

### Pile Foundations

**Axial capacity (static):**
$$Q_u = Q_b + Q_s = q_b A_b + \sum f_s A_s$$

- End bearing: $q_b = cN_c^* + qN_q^*$ (deep foundation factors)
- Skin friction: $f_s = \alpha c_u$ (for cohesive soils) or $f_s = K\sigma'_v \tan\delta$ (for cohesionless)

**Group efficiency:**
$$\eta_g = \frac{Q_{group}}{n \cdot Q_{single}}$$

---

## Slope Stability

### Limit Equilibrium Methods

**Ordinary method of slices (Fellenius):**
$$F_s = \frac{\sum(c' l + W\cos\alpha \tan\phi')}{\sum W\sin\alpha}$$

**Bishop's simplified:**
$$F_s = \frac{1}{\sum W\sin\alpha} \sum \frac{c'b + W(1-r_u)\tan\phi'}{m_\alpha}$$
where $m_\alpha = \cos\alpha + \sin\alpha\tan\phi'/F_s$

### Slope Stabilization Methods

| Method | Application |
|--------|-------------|
| Retaining walls | Gravity, cantilever, counterfort, sheet pile |
| Soil nails | Stabilize existing slopes |
| Mechanically stabilized earth (MSE) | Reinforced soil walls |
| Ground anchors | Active reinforcement |
| Drainage | Reduce pore water pressure |

---

## Earth Pressure Theories

### Rankine (smooth wall, no friction)
$$K_a = \tan^2(45° - \phi/2), \quad K_p = \tan^2(45° + \phi/2)$$

**Active pressure:** $p_a = K_a\sigma_v - 2c\sqrt{K_a}$
**Passive pressure:** $p_p = K_p\sigma_v + 2c\sqrt{K_p}$

### Coulomb (with wall friction $\delta$)
$$K_a = \frac{\sin^2(\alpha+\phi)}{\sin^2\alpha\sin(\alpha-\delta)\left[1+\sqrt{\frac{\sin(\phi+\delta)\sin(\phi-\beta)}{\sin(\alpha-\delta)\sin(\alpha+\beta)}}\right]^2}$$

---

## Worked Examples

### Example 1: Bearing Capacity
**Problem:** Strip footing, $B = 2$ m, $D_f = 1.5$ m, $c = 20$ kPa, $\phi = 25°$, $\gamma = 18$ kN/m³. Find $q_u$.

**Solution:**
1. $N_c = 25.1$, $N_q = 12.7$, $N_\gamma = 9.7$ (for $\phi = 25°$)
2. $q_u = cN_c + qN_q + 0.5\gamma BN_\gamma$
3. $q_u = 20(25.1) + (18 \times 1.5)(12.7) + 0.5(18)(2)(9.7)$
4. $q_u = 502 + 342.9 + 174.6 = 1019.5$ kPa
5. $q_{net} = 1019.5 - 18 \times 1.5 = 992.5$ kPa
6. $q_{safe} = 992.5/3 + 27 = 357.5$ kPa

### Example 2: Consolidation Settlement
**Problem:** Clay layer $H = 3$ m, $e_0 = 0.8$, $C_c = 0.25$, $\sigma'_0 = 100$ kPa, $\Delta\sigma = 80$ kPa. Find settlement.

**Solution:**
1. $S_c = \frac{C_c H}{1+e_0}\log\frac{\sigma'_0+\Delta\sigma}{\sigma'_0}$
2. $S_c = \frac{0.25 \times 3000}{1.8}\log\frac{180}{100}$
3. $S_c = 416.7 \times 0.2553 = 106.4$ mm

---

## 🎤 Interview Q&A

### Q1: What is the difference between normally consolidated and overconsolidated clay?
**A:** Normally consolidated (NC): current effective stress = maximum past stress. Overconsolidated (OC): current stress < maximum past stress. OC clay has higher strength, lower compressibility, and swelling potential. Preconsolidation pressure $\sigma'_c$ is determined from the Casagrande construction on the e-log p curve.

### Q2: What are the bearing capacity factors and what do they represent?
**A:** $N_c$, $N_q$, $N_\gamma$ are dimensionless factors depending on $\phi$. $N_c$ represents cohesion contribution, $N_q$ represents overburden contribution, $N_\gamma$ represents self-weight contribution to bearing capacity. They increase with $\phi$, meaning stronger soils have higher bearing capacity.

### Q3: How do you design a pile foundation?
**A:** (1) Determine pile capacity from static analysis ($Q_b + Q_s$) or dynamic formulas. (2) Apply factor of safety (2.5 for static, 2.0 for dynamic). (3) Check group efficiency. (4) Check settlement of pile group. (5) Check negative skin friction if soft clay is present. (6) Verify with pile load tests.

### Q4: Explain the difference between Rankine and Coulomb earth pressure theories.
**A:** Rankine: assumes smooth wall (no wall friction), uses stress transformation, gives principal stress states. Coulomb: accounts for wall friction ($\delta$), uses wedge equilibrium, more realistic for actual retaining walls. Coulomb gives higher passive pressures when $\delta > 0$, but Rankine is simpler and more conservative for active case.

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Mohr-Coulomb | $\tau_f = c + \sigma'\tan\phi$ | Shear strength |
| Terzaghi bearing | $q_u = cN_c + qN_q + 0.5\gamma BN_\gamma$ | Shallow foundation |
| Rankine active | $p_a = K_a\sigma_v - 2c\sqrt{K_a}$ | Retaining wall |
| Rankine passive | $p_p = K_p\sigma_v + 2c\sqrt{K_p}$ | Retaining wall |
| Consolidation | $S = C_cH\log(\sigma'/\sigma'_0)/(1+e_0)$ | Settlement |
| Time factor | $T_v = c_v t/H_{dr}^2$ | Consolidation rate |
| Pile capacity | $Q_u = q_b A_b + \sum f_s A_s$ | Deep foundation |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Soil properties      →  Phase relationships           →  Advanced constitutive models →  USCS classification flow
Classification        →  Permeability & seepage        →  Numerical geotech (PLAXIS)  →  Darcy's law applications
Compaction           →  Consolidation (Terzaghi)       →  Unsaturated soil mechanics →  OMC and Proctor test
Shear strength       →  Bearing capacity               →  Pile design & group action →  Mohr-Coulomb interpretation
Foundation basics    →  Earth pressure theories        →  Ground improvement         →  Rankine vs Coulomb
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `GEOTECH`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What are the phase relationships in soil mechanics?
2. Explain Mohr-Coulomb failure criterion.
3. What is the difference between drained and undrained conditions?

### B. WHY Questions
1. **Why** does consolidation take time in clay?
   - Water must drain out of low-permeability clay; the rate is governed by $c_v = k/(m_v \gamma_w)$. This is why consolidation is time-dependent while settlement of sand is immediate.

2. **Why** is effective stress used instead of total stress?
   - Because soil strength and deformation depend on inter-particle contact forces (effective stress), not on pore water pressure.

3. **Why** is the Terzaghi bearing capacity equation modified with shape factors?
   - Because the original equation is for strip foundations. Real foundations have 3D effects (corners, edges) that increase or decrease capacity.

### D. Comparison
| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| NC clay | OC clay | Current stress = max past vs < max past |
| Drained | Undrained | Pore pressure dissipated vs not |
| Rankine | Coulomb | No wall friction vs wall friction |
| Shallow | Deep | $D_f/B < 4$ vs $D_f/B > 4$ |

---

## 🎤 Interview Answer Format

### High-Value Q: "Explain effective stress."

**30-second answer:**
"Effective stress is the stress carried by the soil skeleton: $\sigma' = \sigma - u$. Soil strength depends on effective stress, not total stress. Shear strength is $\tau_f = c' + \sigma'\tan\phi'$. When pore pressure increases (flooding, rapid loading), effective stress decreases and strength drops."

---

## 🔗 Cross-Links

- [`structures.md`](../structures/structures.md) — Foundation design integration
- [`water-resources-engineering.md`](../hwre/water_resources/water-resources-engineering.md) — Canal/embankment design
- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — Pavement subgrade

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

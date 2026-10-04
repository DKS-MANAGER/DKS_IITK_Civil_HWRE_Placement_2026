# Geotechnical Engineering — Rapid Revision Sheet

> Last-minute cheat sheet for Geotechnical Engineering interviews and exams.

---

## Framework 1: Phase Relationships

### Core Identities

| Relationship | Formula |
|:-------------|:--------|
| Void ratio | e = V_v/V_s |
| Porosity | n = V_v/V = e/(1+e) |
| Degree of saturation | S = V_w/V_v |
| **Key identity** | **Se = w·G_s** |
| Bulk density | γ = (G_s + Se)γ_w/(1+e) |
| Dry density | γ_d = G_s·γ_w/(1+e) |
| Saturated density | γ_sat = (G_s + e)γ_w/(1+e) |
| Submerged density | γ' = γ_sat - γ_w |

### Quick Conversions
- n = e/(1+e), e = n/(1-n)
- γ_d = γ/(1+w)
- For saturated soil: S = 1 → e = w·G_s

### USCS Classification Flow

```
Is >50% retained on No.4 sieve?
  YES → Coarse-grained
    >50% of coarse on No.4 → GRAVEL (G)
    else → SAND (S)
    Fines <5% → W (well-graded) / P (poorly-graded)
    Fines >12% → M (silt) / C (clay)
  NO → Fine-grained
    LL < 50 → L (low plasticity)
    LL > 50 → H (high plasticity)
    Plot on plasticity chart vs A-line (PI = 0.73(LL-20))
    Above A-line → C (clay); Below → M (silt)
```

---

## Framework 2: Permeability & Seepage

### Darcy's Law
$$v = k \cdot i, \quad q = k \cdot i \cdot A$$

**Seepage velocity:** v_s = v/n (n = porosity)

### Permeability Tests

| Test | Formula | Use |
|:-----|:--------|:----|
| Constant head | k = QL/(A·h·t) | Coarse soils (sand, gravel) |
| Falling head | k = (aL/At)·ln(h₁/h₂) | Fine soils (silt, clay) |

**Hazen's formula:** k ≈ C·D₁₀² (C = 100-150, D₁₀ in cm, k in cm/s)

### Flow Nets
- q = k·H·(N_f/N_d)
- Uplift pressure = γ_w × remaining head
- Critical hydraulic gradient: i_cr = (G_s - 1)/(1+e)

### Compaction
- Standard Proctor: 2.6 kN·m/L
- Modified Proctor: 5.5 kN·m/L
- Zero air voids: γ_d = G_s·γ_w/(1 + w·G_s)

---

## Framework 3: Consolidation & Settlement

### Terzaghi's Consolidation

$$\frac{\partial u}{\partial t} = c_v \frac{\partial^2 u}{\partial z^2}$$

**Settlement (normally consolidated):**
$$S_c = \frac{C_c H}{1+e_0} \log\frac{\sigma'_0 + \Delta\sigma}{\sigma'_0}$$

**Time factor:** T_v = c_v·t/H_dr²

| Consolidation | T_v |
|:-------------:|:---:|
| 50% | 0.2 |
| 90% | 0.848 |

### Settlement Types

| Type | Formula | When |
|:-----|:--------|:-----|
| Immediate | S_i = qB(1-ν²)/E_u × I_f | Sands, immediate |
| Consolidation | S_c = C_cH/(1+e₀)·log(σ'/σ'₀) | Clays, time-dependent |
| Secondary | S_s = C_α·H·log(t/t_p) | Long-term creep |

---

## Framework 4: Shear Strength & Bearing Capacity

### Mohr-Coulomb
$$\tau_f = c' + \sigma' \tan\phi'$$

| Test | Conditions | Output |
|:-----|:-----------|:-------|
| UU | Quick, no drainage | c_u (φ_u = 0) |
| CU | Consolidate, then shear | c', φ', c_cu, φ_cu |
| CD | Full drainage | c', φ' |

### Terzaghi Bearing Capacity
$$q_u = cN_c + qN_q + \frac{1}{2}\gamma B N_\gamma$$

**Shape factors (Meyerhof):**

| Foundation | s_c | s_q | s_γ |
|:-----------|:---:|:---:|:---:|
| Strip | 1.0 | 1.0 | 1.0 |
| Square | 1.3 | 1.2 | 0.8 |
| Circle | 1.3 | 1.2 | 0.6 |
| Rectangular | 1+0.3B/L | 1+0.3B/L | 1-0.4B/L |

**Net:** q_nu = q_u - γ·D_f
**Safe:** q_s = q_nu/F + γ·D_f (F = 3)

### Pile Foundations
$$Q_u = Q_b + Q_s = q_b A_b + \sum f_s A_s$$

- End bearing: q_b = c·N_c* + q·N_q*
- Skin friction (cohesive): f_s = α·c_u
- Skin friction (cohesionless): f_s = K·σ'_v·tanδ
- Group efficiency: η_g = Q_group/(n·Q_single)

---

## Framework 5: Earth Pressure & Slope Stability

### Rankine (smooth wall)
$$K_a = \tan^2(45° - \phi/2), \quad K_p = \tan^2(45° + \phi/2)$$

**Active:** p_a = K_a·σ_v - 2c√K_a
**Passive:** p_p = K_p·σ_v + 2c√K_p

### Coulomb (with wall friction δ)
$$K_a = \frac{\sin^2(\alpha+\phi)}{\sin^2\alpha\sin(\alpha-\delta)\left[1+\sqrt{\frac{\sin(\phi+\delta)\sin(\phi-\beta)}{\sin(\alpha-\delta)\sin(\alpha+\beta)}}\right]^2}$$

### Slope Stability

**Fellenius (ordinary method of slices):**
$$F_s = \frac{\sum(c'l + W\cos\alpha\tan\phi')}{\sum W\sin\alpha}$$

**Bishop's simplified:**
$$F_s = \frac{1}{\sum W\sin\alpha}\sum\frac{c'b + W(1-r_u)\tan\phi'}{m_\alpha}$$

where m_α = cosα + sinα·tanφ'/F_s

### Slope Stabilization Methods

| Method | Application |
|:-------|:------------|
| Retaining walls | Gravity, cantilever, counterfort, sheet pile |
| Soil nails | Stabilize existing slopes |
| MSE walls | Reinforced soil walls |
| Ground anchors | Active reinforcement |
| Drainage | Reduce pore water pressure |

---

## Quick-Fire Interview Answers

**Q1: What is effective stress?**
A: Effective stress is the stress carried by the soil skeleton: σ' = σ - u. Soil strength depends on effective stress, not total stress. When pore pressure increases (flooding, rapid loading), effective stress decreases and strength drops.

**Q2: Why does consolidation take time in clay?**
A: Water must drain out of low-permeability clay. The rate is governed by c_v = k/(m_v·γ_w). This is why consolidation is time-dependent while settlement of sand is immediate.

**Q3: What is the difference between NC and OC clay?**
A: Normally consolidated: current effective stress = maximum past stress. Overconsolidated: current stress < maximum past stress. OC clay has higher strength, lower compressibility, and swelling potential.

**Q4: What is the difference between Rankine and Coulomb earth pressure theories?**
A: Rankine assumes a smooth wall (no wall friction) and uses stress transformation. Coulomb accounts for wall friction (δ) using wedge equilibrium. Coulomb gives higher passive pressures when δ > 0, but Rankine is simpler and more conservative for the active case.

**Q5: What is liquefaction?**
A: Liquefaction is the sudden loss of strength in saturated loose sand during earthquake shaking. Pore pressure rises to equal total stress, effective stress → 0, and the soil behaves like a liquid. Mitigation: densification (vibro-compaction), drainage, stone columns, or ground improvement.

**Q6: How do you determine bearing capacity?**
A: Use Terzaghi's equation q_u = cN_c + qN_q + 0.5γBN_γ with appropriate shape factors. Apply FOS = 3 for net safe bearing capacity. Verify with plate load tests or SPT data.

**Q7: What is the difference between UU, CU, and CD tests?**
A: UU (unconsolidated undrained): no drainage, gives c_u. CU (consolidated undrained): consolidate then shear without drainage, gives c', φ'. CD (consolidated drained): full drainage during shear, gives c', φ'. UU simulates rapid loading of clay; CD simulates slow loading of sand.

**Q8: What is quick sand condition?**
A: Quick sand occurs when the upward seepage gradient equals the critical hydraulic gradient i_cr = (G_s-1)/(1+e), making effective stress zero. The soil loses all strength. Prevention: lower water table, sheet piles, or increase seepage path.

**Q9: Why is compaction done at OMC?**
A: At OMC, the soil achieves maximum dry density (γ_dmax) with minimum voids. Below OMC, soil is too dry to densify. Above OMC, water fills voids and prevents particle rearrangement. Compaction at OMC gives maximum strength and minimum permeability.

**Q10: What is negative skin friction on piles?**
A: Negative skin friction occurs when the soil around a pile settles more than the pile (e.g., soft clay consolidation), dragging the pile down. It adds a downward load on the pile. Mitigation: bitumen coating, casing, or designing for the additional load.

---

## Last-Minute Checklist

- [ ] Phase relationships (Se = wG_s, γ_d, γ_sat)
- [ ] USCS classification flow + A-line
- [ ] Darcy's law + permeability tests
- [ ] Flow nets (q = kH·N_f/N_d)
- [ ] Critical hydraulic gradient
- [ ] Compaction curve + OMC + zero air voids
- [ ] Terzaghi consolidation + settlement
- [ ] Time factor (T_v = 0.2 for 50%, 0.848 for 90%)
- [ ] Mohr-Coulomb + UU/CU/CD
- [ ] Terzaghi bearing capacity + shape factors
- [ ] Pile capacity + group efficiency
- [ ] Rankine/Coulomb earth pressure
- [ ] Slope stability (Fellenius, Bishop)
- [ ] Ground improvement + liquefaction

---

## Cross-Links

- [`geotechnical.md`](geotechnical.md) — Full subject reference
- [`role-study-plan.md`](role-study-plan.md) — Detailed study plan with worked examples
- [`structures.md`](../structures/structures.md) — Foundation design integration
- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — Pavement subgrade
- [`civil-rapid-revision.md`](../fundamentals/civil-rapid-revision.md) — Cross-subject formulas

---

## References

- IS 1498, IS 6403, IS 2911, IS 2720
- Terzaghi & Peck — Soil Mechanics in Engineering Practice
- Bowles — Foundation Analysis and Design
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

# RCC Design — Rapid Revision Sheet

> Last-minute revision for RCC design interviews. Core formulas, IS 456 values, and key concepts in 15 minutes.

---

## Essential Formulas

| Formula | Equation | Use |
|:--------|:---------|:----|
| Flexure (singly reinforced) | $M_u = 0.87f_yA_{st}(d - 0.42x_u)$ | Beam design |
| Balanced section | $M_{u,lim} = 0.138f_{ck}bd^2$ (Fe415) | Limiting moment |
| Neutral axis | $x_u = \frac{0.87f_yA_{st}}{0.36f_{ck}b}$ | NA depth |
| Shear stress | $\tau_v = V_u/bd$ | Shear check |
| Stirrup spacing | $s_v = \frac{0.87f_yA_{sv}d}{V_{us}}$ | Shear reinforcement |
| Development length | $L_d = \frac{0.87f_y\phi}{4\tau_{bd}}$ | Anchorage |
| Column (short, axial) | $P_u = 0.4f_{ck}A_c + 0.67f_yA_{sc}$ | Column design |
| Modulus of elasticity | $E_c = 5000\sqrt{f_{ck}}$ | Material property |
| Modulus of rupture | $f_{cr} = 0.7\sqrt{f_{ck}}$ | Cracking check |
| Min eccentricity | $e_{min} = l/500 + D/30 \ge 20$ mm | Column check |

---

## IS 456 Key Values

| Parameter | Value |
|:----------|:------|
| Partial safety factor (concrete) | $\gamma_m = 1.5$ |
| Partial safety factor (steel) | $\gamma_m = 1.15$ |
| Max strain in concrete (flexure) | 0.0035 |
| Max strain in concrete (axial) | 0.002 |
| $x_{u,max}/d$ — Fe250 | 0.53 |
| $x_{u,max}/d$ — Fe415 | 0.48 |
| $x_{u,max}/d$ — Fe500 | 0.46 |
| Min tension steel (beams) | $0.85bd/f_y$ |
| Max tension steel | 4% of $bD$ |
| Min longitudinal steel (columns) | 0.8% |
| Max longitudinal steel (columns) | 6% |
| Min grade for RCC | M20 |
| Min grade in sea water | M30 |
| Nominal cover (slab) | 15 mm |
| Nominal cover (beam) | 25 mm |
| Nominal cover (column) | 40 mm |
| Nominal cover (footing) | 75 mm |
| Max moment redistribution | 30% |
| Deflection limit (final) | Span/250 |

---

## Load Combinations (IS 456 Table 18)

```
1. 1.5(DL + LL)
2. 1.5(DL + WL/EL)  or  0.9(DL) + 1.5(WL)
3. 1.2(DL + LL + WL/EL)
```

---

## Design Checklist

### Beam Design
- [ ] Check $M_u$ vs $M_{u,lim}$ (singly or doubly reinforced?)
- [ ] Calculate $A_{st}$, verify $x_u < x_{u,max}$
- [ ] Check shear ($\tau_v$ vs $\tau_c$, $\tau_{c,max}$)
- [ ] Check development length
- [ ] Check deflection (span/depth ratio)

### Column Design
- [ ] Check slenderness (short if $l_{eff}/D < 12$)
- [ ] Check minimum eccentricity
- [ ] Calculate $P_u$ capacity
- [ ] Detailing (ties, spacing, lap)

### Slab Design
- [ ] Classify one-way ($l_y/l_x > 2$) or two-way
- [ ] Check span/depth ratio
- [ ] Calculate main + distribution steel
- [ ] Check minimum steel (0.12% HYSD)

---

## Last-Minute Checklist

- [ ] Reviewed limit state vs working stress
- [ ] Reviewed under vs over-reinforced
- [ ] Reviewed beam design (singly reinforced)
- [ ] Reviewed shear design & stirrups
- [ ] Reviewed column design (short, tied)
- [ ] Reviewed development length & detailing
- [ ] Reviewed load combinations (IS 456 Table 18)
- [ ] Reviewed prestressed concrete basics

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`rcc-design.md`](rcc-design.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Interview | [`INTERVIEW.md`](INTERVIEW.md) |
| Role Study Plan | [`role-study-plan.md`](role-study-plan.md) |
| Structural Analysis | [`../structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md) |

---

*Print this sheet 1 hour before your RCC design interview.*
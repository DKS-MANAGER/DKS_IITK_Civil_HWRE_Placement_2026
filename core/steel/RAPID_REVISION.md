# Steel Design — Rapid Revision Sheet

> Last-minute revision for steel design interviews. Core formulas, IS 800 values, and key concepts in 15 minutes.

---

## Essential Formulas

| Formula | Equation | Use |
|:--------|:---------|:----|
| Bolt shear strength | $V_{dsb} = \frac{f_{ub}}{\sqrt{3}\gamma_{mb}}(n_nA_{nb} + n_sA_{sb})$ | Bolt capacity |
| Bolt bearing strength | $V_{dpb} = \frac{2.5k_bdtf_u}{\gamma_{mb}}$ | Bolt capacity |
| Fillet weld strength | $P_{dw} = \frac{L_w t_t f_u}{\sqrt{3}\gamma_{mw}}$ | Weld capacity |
| Butt weld (axial) | $T_{dw} = \frac{f_y L_w t_e}{\gamma_{mw}}$ | Weld capacity |
| Tension (gross yield) | $T_{dg} = \frac{A_g f_y}{\gamma_{m0}}$ | Tension member |
| Tension (net rupture) | $T_{dn} = \frac{0.9A_n f_u}{\gamma_{m1}}$ | Tension member |
| Compression | $P_d = A_e f_{cd}$ | Column design |
| Beam bending | $M_d = \frac{\beta_b Z_p f_y}{\gamma_{m0}} \le \frac{1.2Z_e f_y}{\gamma_{m0}}$ | Beam design |
| Beam shear | $V_d = \frac{A_v f_{yw}}{\sqrt{3}\gamma_{m0}}$ | Beam shear |
| Net area (staggered) | $A_n = (B - nd_0 + \sum\frac{p^2}{4g})t$ | Net section |

---

## IS 800 Key Values

| Parameter | Value |
|:----------|:------|
| Partial safety factor ($\gamma_{m0}$) | 1.10 |
| Partial safety factor ($\gamma_{m1}$) | 1.25 |
| Partial safety factor ($\gamma_{mb}$) — bolts | 1.25 |
| Partial safety factor ($\gamma_{mw}$) — shop weld | 1.25 |
| Partial safety factor ($\gamma_{mw}$) — field weld | 1.50 |
| Modulus of elasticity | $2 \times 10^5$ N/mm² |
| Min pitch of bolts | 2.5d |
| Max slenderness (compression) | 180 |
| Max slenderness (tension) | 400 |
| Lacing inclination | 40°–70° |
| Lacing transverse shear | 2.5% of axial load |
| Web crippling dispersion | 1:2.5 |
| Bearing strength of concrete | 0.45$f_{ck}$ |

---

## Effective Length of Columns

| End Condition | Effective Length |
|:--------------|:-----------------|
| Both ends fixed | 0.65L |
| One fixed, one pinned | 0.8L |
| Both pinned | 1.0L |
| One fixed, one free | 2.0L |

---

## Design Checklist

### Bolted Connection
- [ ] Determine bolt value $V_{db}$ = least of shear, bearing, tension
- [ ] Number of bolts $n = P/V_{db}$
- [ ] Check pitch (≥ 2.5d), edge distance
- [ ] Check block shear

### Tension Member
- [ ] Check gross yielding ($T_{dg}$)
- [ ] Check net rupture ($T_{dn}$)
- [ ] Check slenderness ($l/r \le 400$)

### Compression Member
- [ ] Check $P_d = A_e f_{cd}$
- [ ] Check slenderness ($l/r \le 180$)
- [ ] Check buckling class

### Beam
- [ ] Classify section (plastic, compact, semi-compact, slender)
- [ ] Check bending ($M_d$)
- [ ] Check shear ($V_d$)
- [ ] Check lateral-torsional buckling (if unsupported)

---

## Last-Minute Checklist

- [ ] Reviewed bolted connection design
- [ ] Reviewed welded connection design
- [ ] Reviewed tension member design
- [ ] Reviewed compression member design
- [ ] Reviewed beam design (bending + shear + LTB)
- [ ] Reviewed effective length of columns
- [ ] Reviewed IS 800 key values

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`steel-design.md`](steel-design.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Interview | [`INTERVIEW.md`](INTERVIEW.md) |
| RCC Design | [`../rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Structural Analysis | [`../structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md) |

---

*Print this sheet 1 hour before your steel design interview.*
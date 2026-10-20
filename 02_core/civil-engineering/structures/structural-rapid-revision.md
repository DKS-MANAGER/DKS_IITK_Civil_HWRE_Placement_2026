# Structural Engineer — Rapid Revision Sheet

> Last-minute revision for structural engineering interviews. Core formulas, IS code values, and key concepts in 15 minutes.

---

## Essential Formulas

### RCC Design (IS 456:2000)
| Formula / Parameter | Equation / Value | Applicability / Standard |
|:--------------------|:-----------------|:-------------------------|
| Flexural Strength (singly reinforced) | $M_u = 0.87 f_y A_{st} \left(d - 0.416 x_u\right)$ | Under-reinforced section ($x_u \le x_{u,\max}$) |
| Neutral Axis Depth | $x_u = \frac{0.87 f_y A_{st}}{0.36 f_{ck} b}$ | Strain compatibility limit |
| Balanced Section Limiting Depth | $x_{u,\max}/d = 0.53$ (Fe250), **$0.48$ (Fe415)**, **$0.46$ (Fe500)**, $0.44$ (Fe550) | IS 456 Cl. 38.1 & Note to Cl. 38.1 |
| Limiting Moment of Resistance | $M_{u,\lim} = 0.148 f_{ck} b d^2$ (Fe250) <br> $M_{u,\lim} = 0.138 f_{ck} b d^2$ (Fe415) <br> $M_{u,\lim} = 0.133 f_{ck} b d^2$ (Fe500) | Annex G, Cl. G-1.1 |
| Nominal Shear Stress | $\tau_v = \frac{V_u}{b d}$ | Design shear stress across effective depth |
| Design Concrete Shear Strength | $\tau_c$ from Table 19; Maximum $\tau_{c,\max} = 0.62\sqrt{f_{ck}}\text{ MPa}$ (Table 20) | IS 456 Table 19 & 20 |
| Shear Stirrup Design | $V_{us} = V_u - \tau_c b d = \frac{0.87 f_y A_{sv} d}{s_v}$ | When $\tau_v > \tau_c$ (min stirrups if $\tau_v \le \tau_c$) |
| Minimum Shear Reinforcement | $\frac{A_{sv}}{b \cdot s_v} \ge \frac{0.4}{0.87 f_y}$ | IS 456 Cl. 26.5.1.6 |
| Short Column (Axial, tied) | $P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$ | Min eccentricity $e_{\min} \le 0.05 D$ (Cl. 39.3) |
| Short Column (Spiral) | $P_u = 1.05 \left(0.4 f_{ck} A_c + 0.67 f_y A_{sc}\right)$ | When spiral condition Cl. 39.4.1 is met |
| Modular Ratio (WSD) | $m = \frac{280}{3 \sigma_{cbc}}$ | Partially accounts for long-term creep (Cl. B-1.3) |

### Steel Design (IS 800:2007 — Limit State Method)
| Formula / Parameter | Equation / Value | Code Reference |
|:--------------------|:-----------------|:---------------|
| Column Euler Buckling | $P_{cr} = \frac{\pi^2 E I}{K L^2} = \frac{\pi^2 E A}{\lambda^2}$ | Ideal elastic buckling |
| Column Design Compressive Stress | $f_{cd} = \frac{f_y / \gamma_{m0}}{\phi + [\phi^2 - \lambda^2]^{0.5}} \le \frac{f_y}{\gamma_{m0}}$ | Cl. 7.1.2.1 (Buckling curves a, b, c, d) |
| Tension Capacity (Yielding of Gross Section) | $T_{dg} = \frac{A_g f_y}{\gamma_{m0}} \quad (\gamma_{m0} = 1.10)$ | Cl. 6.2 |
| Tension Capacity (Rupture of Net Section) | $T_{dn} = \frac{0.9 A_n f_u}{\gamma_{m1}} \quad (\gamma_{m1} = 1.25)$ | Cl. 6.3.1 |
| Tension Capacity (Block Shear) | $T_{db} = \min(T_{db1}, T_{db2})$ | Cl. 6.4 |
| Bolt Shear Capacity | $V_{dsb} = \frac{f_{ub}}{\sqrt{3}\gamma_{mb}} (n_n A_{nb} + n_s A_{sb}) \quad (\gamma_{mb} = 1.25)$ | Cl. 10.3.2 |
| Bolt Bearing Capacity | $V_{dpb} = \frac{2.5 k_b d t f_u}{\gamma_{mb}}$ | Cl. 10.3.4 ($k_b = \min(\frac{e}{3d_0}, \frac{p}{3d_0}-0.25, \frac{f_{ub}}{f_u}, 1.0)$) |
| Fillet Weld Design Strength | $f_{wd} = \frac{f_u}{\sqrt{3}\gamma_{mw}} \quad (\gamma_{mw} = 1.25\text{ shop}, 1.50\text{ site})$ | Cl. 10.5.7 ($t_t = k \cdot s$, $k=0.70$ for $60^\circ\text{--}90^\circ$) |

### Structural Analysis
| Formula / Parameter | Equation | Note |
|:--------------------|:---------|:-----|
| Fixed-End Moment (UDL $w$) | $M_{FAB} = -\frac{w L^2}{12}, \quad M_{FBA} = +\frac{w L^2}{12}$ | Standard prismatic beam |
| Fixed-End Moment (Point load $W$ at $a, b$) | $M_{FAB} = -\frac{W a b^2}{L^2}, \quad M_{FBA} = +\frac{W a^2 b}{L^2}$ | Standard prismatic beam |
| Slope-Deflection Equation | $M_{AB} = M_{FAB} + \frac{2EI}{L}\left(2\theta_A + \theta_B - \frac{3\Delta}{L}\right)$ | Equilibrium-based method |
| Member Rotational Stiffness ($k$) | Far end fixed: $k = \frac{4EI}{L}$; Far end hinged: $k = \frac{3EI}{L}$ | Moment distribution factor $DF = \frac{k}{\sum k}$ |

---

## IS Code Quick Reference

### IS 456:2000 — Concrete
| Parameter | Value | Standard Clause |
|:----------|:------|:----------------|
| Partial safety factor (concrete) | $\gamma_{mc} = 1.50$ | Table 18 |
| Partial safety factor (steel) | $\gamma_{ms} = 1.15$ | Table 18 |
| Nominal cover (moderate exposure) | Beams: 25 mm, Columns: 40 mm, Slabs: 20 mm, Footings: 50 mm | Table 16 & Cl. 26.4 |
| Min tension steel in beams | $\frac{A_s}{b d} \ge \frac{0.85}{f_y}$ ($0.205\%$ for Fe415, $0.17\%$ for Fe500) | Cl. 26.5.1.1 |
| Max tension steel in beams | $0.04 b D$ (4% of gross area) | Cl. 26.5.1.1 |
| Min reinforcement in slabs | $0.15\% b D$ (Fe250) or $0.12\% b D$ (Fe415 / Fe500) | Cl. 26.5.2.1 |
| Column longitudinal steel | Minimum $0.8\%$, Maximum $6\%$ (restricted to $4\%$ at laps) | Cl. 26.5.3.1 |
| Fe250: $x_{u,\max}/d$ | **0.53** | Cl. 38.1 |
| Fe415: $x_{u,\max}/d$ | **0.48** | Cl. 38.1 |
| Fe500: $x_{u,\max}/d$ | **0.46** | Cl. 38.1 |
| Fe550: $x_{u,\max}/d$ | **0.44** | Cl. 38.1 |

### IS 800:2007 — Steel
| Parameter | Value | Standard Clause |
|:----------|:------|:----------------|
| Partial safety factor ($\gamma_{m0}$) — yielding | 1.10 | Table 5 |
| Partial safety factor ($\gamma_{m1}$) — ultimate rupture | 1.25 | Table 5 |
| Partial safety factor ($\gamma_{mb}$) — bolts (bearing/shear) | 1.25 | Table 5 |
| Partial safety factor ($\gamma_{mw}$) — welds | 1.25 (shop fabrication), 1.50 (field/site work) | Table 5 |
| Maximum slenderness ($\lambda = K L / r$) | 180 (compression members carrying dead + imposed load) | Table 3 |
| Maximum slenderness ($\lambda$) | 250 (compression flange carrying wind/earthquake) | Table 3 |
| Maximum slenderness ($\lambda$) | 400 (members always in tension, excluding pretensioned ties) | Table 3 |

### Design Load Combinations (IS 456 Table 18 & IS 800 Table 4)
```
Limit State of Collapse:
1. 1.5(DL + IL)
2. 1.5(DL + WL/EL) or 0.9DL + 1.5WL/EL (reversal of stress / overturning check)
3. 1.2(DL + IL + WL/EL)

Limit State of Serviceability:
1. 1.0(DL + IL)
2. 1.0(DL + WL/EL)
3. 1.0 DL + 0.8 IL + 0.8 WL/EL
```

---

## Design Checklist

### Beam Design
- [ ] Check M_u,lim (singly or doubly reinforced?)
- [ ] Calculate A_st
- [ ] Check shear (τ_v vs τ_c)
- [ ] Check deflection (span/depth ratio)
- [ ] Detailing (anchorage, stirrups)

### Column Design
- [ ] Check slenderness (short or long?)
- [ ] Check uniaxial or biaxial bending
- [ ] Calculate P_u capacity
- [ ] Detailing (ties, spacing, lap)

### Connection Design
- [ ] Bolt: bearing or friction type?
- [ ] Bolt: shear or tension?
- [ ] Weld: size and length
- [ ] End bearing / bearing plate

---

## Last-Minute Checklist

- [ ] Reviewed moment distribution method
- [ ] Reviewed beam design (singly reinforced)
- [ ] Reviewed column design (short, tied)
- [ ] Reviewed bolted connection design
- [ ] Reviewed load combinations (IS 456 Table 18)
- [ ] Reviewed IS 456 and IS 800 key values
- [ ] Prepared 3-minute thesis pitch
- [ ] Researched [company] recent structural projects

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| Structural Analysis | [../structural-analysis/structural-analysis.md](../structural-analysis/structural-analysis.md) |
| RCC Design | [../rcc/rcc-design.md](../rcc/rcc-design.md) |
| Steel Design | [../steel/steel-design.md](../steel/steel-design.md) |
| Technical Interview Bank | [technical-interview-bank.md](../../../05_interview/technical/technical-interview-bank.md) |

---

*Print this sheet 1 hour before your structural engineering interview.*

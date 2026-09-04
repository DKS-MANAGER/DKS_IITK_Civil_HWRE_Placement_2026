# Structural Engineer — Rapid Revision Sheet

> Last-minute revision for structural engineering interviews. Core formulas, IS code values, and key concepts in 15 minutes.

---

## Essential Formulas

### RCC Design (IS 456)
| Formula | Equation | Use |
|:--------|:---------|:----|
| Flexure (singly reinforced) | M_u = 0.87f_yA_st(d − 0.42x_u) | Beam design |
| Balanced section | x_u,max/d = 0.48 (Fe415), 0.53 (Fe500) | Limiting depth |
| Shear capacity | V_u = τ_c × b × d | Shear check |
| Column (short, axial) | P_u = 0.4f_ckA_c + 0.67f_yA_sc | Column design |
| Modular ratio | m = 280/(3σ_cbc) | WSD conversion |
| Moment of resistance (balanced) | M_u,lim = 0.138f_ckbd² | Limiting moment |

### Steel Design (IS 800)
| Formula | Equation | Use |
|:--------|:---------|:----|
| Euler buckling | P_cr = π²EI/L_e² | Column stability |
| Bolt (bearing) | V_dsb = d_b × t × f_ub / (√3 × γ_mb) | Bolt capacity |
| Weld strength | V_dws = l_w × t × f_u / (√3 × γ_mw) | Weld capacity |
| Tension capacity | T_dg = A_g × f_y / γ_m0 | Gross section |
| Tension (net) | T_dn = 0.9A_n × f_u / γ_m1 | Net section |

### Structural Analysis
| Formula | Equation | Use |
|:--------|:---------|:----|
| Fixed-end moment (UDL) | FEM = wL²/12 | Moment distribution |
| Fixed-end moment (point) | FEM = Pab²/L² | Moment distribution |
| Slope-deflection | M_AB = (2EI/L)(2θ_A + θ_B − 3ψ) | Frame analysis |
| Stiffness (beam) | k = 4EI/L | Direct stiffness |

---

## IS Code Quick Reference

### IS 456 — Concrete
| Parameter | Value |
|:----------|:------|
| Partial safety factor (concrete) | γ_m = 1.5 |
| Partial safety factor (steel) | γ_m = 1.15 |
| Min cover (beams) | 25 mm |
| Min cover (columns) | 40 mm |
| Max steel (% of bD) | 4% |
| Min steel (% of bD) | 0.85% (beam), 0.8% (slab) |
| Fe415: x_u,max/d | 0.48 |
| Fe500: x_u,max/d | 0.46 |

### IS 800 — Steel
| Parameter | Value |
|:----------|:------|
| Partial safety factor (γ_m0) | 1.10 |
| Partial safety factor (γ_m1) | 1.25 |
| Partial safety factor (γ_mb) — bolts | 1.25 |
| Partial safety factor (γ_mw) — welds | 1.25 (shop), 1.50 (field) |

### Load Combinations (IS 456 Table 18)
```
1. 1.5(DL + LL)
2. 1.5(DL + IL + EQ)
3. 1.2(DL + LL + EQ)
4. 1.5(DL + EQ)
5. 0.9DL + 1.5EQ
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
| Technical Interview Bank | [../../prep/interview/technical/technical-interview-bank.md](../../prep/interview/technical/technical-interview-bank.md) |

---

*Print this sheet 1 hour before your structural engineering interview.*

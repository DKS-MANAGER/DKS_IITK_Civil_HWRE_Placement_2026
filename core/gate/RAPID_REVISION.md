# GATE Civil — Rapid Revision

> Final revision system. Supports 30-minute, 2-hour, and 1-day revision. Use with [`formulas/gate-civil-formulas.md`](formulas/gate-civil-formulas.md) and [`revision_notes/gate-civil-revision.md`](revision_notes/gate-civil-revision.md).

## 30-Minute Revision (Highest-Priority Only)

### Structural
- `σ = My/I` — bending stress
- `τ = VQ/Ib` — shear stress
- `P_cr = π²EI/(KL)²` — Euler buckling
- `M_u,lim = 0.138 f_ck b d²` (Fe415), `0.133 f_ck b d²` (Fe500)
- `x_u,max/d = 0.48` (Fe415), `0.46` (Fe500)
- `L_d = φσ_s/(4τ_bd)` — development length

### Geotechnical
- `Se = wG_s` — phase relation
- `σ' = σ − u` — effective stress
- `τ_f = c + σ' tanφ` — Mohr-Coulomb
- `q_u = cN_c + qN_q + 0.5γBN_γ` — Terzaghi
- `T_v = c_v t/H_dr²` — consolidation time factor

### Water Resources
- `h_f = f(L/D)(v²/2g)` — Darcy-Weisbach
- `y_c = (q²/g)^(1/3)` — critical depth (rectangular)
- `y₂/y₁ = ½[√(1+8Fr₁²) − 1]` — hydraulic jump
- `Q = CiA` — Rational formula
- `s = (Q/4πT)W(u)` — Theis

### Environmental
- `BOD_t = L₀(1 − e^(−kt))`
- `F/M = QS₀/(VX)`
- `SRT = VX/(Q_w X_w + Q_e X_e)`

### Transportation
- `SSD = 0.278Vt_R + V²/(254f)`
- `e + f = V²/(127R)`
- `q = kv`

## 2-Hour Revision (Major Formulas by Subject)

| Subject | Key Formulas |
| ------- | ------------ |
| Engineering Math | Eigenvalues, Taylor, Laplace, Bayes, Newton-Raphson, Simpson |
| EM + SOM | Equilibrium, centroid, MOI, stress/strain, elastic constants, torsion |
| Structural Analysis | Determinacy, deflection (5 standard cases), moment distribution |
| RCC | Limit state, flexure, shear, development length, columns, slabs |
| Steel | Tension, compression, buckling, connections |
| Geotech | Phase relations, permeability, consolidation, shear, earth pressure, bearing |
| Fluid + Hydraulics | Hydrostatics, Bernoulli, momentum, pipe flow, open channel, jump |
| Hydrology | Rainfall, infiltration, runoff, unit hydrograph, flood frequency |
| Environmental | Water demand, treatment, BOD, ASP, sewer design |
| Transportation | Geometric design, traffic flow, signals, pavements |
| Surveying | Levelling, traversing, curves, tacheometry |
| Construction | CPM, PERT, cost-time, contracts |

## 1-Day Revision (Complete)

Follow the full formula sheet: [`formulas/gate-civil-formulas.md`](formulas/gate-civil-formulas.md)

## Must-Know Constants

| Constant | Value |
| -------- | ----- |
| g | 9.81 m/s² |
| γ_w | 9.81 kN/m³ |
| ρ_w | 1000 kg/m³ |
| μ_w (20°C) | 1.002 × 10⁻³ Pa·s |
| ν_w (20°C) | 1.004 × 10⁻⁶ m²/s |
| 1 atm | 101.325 kPa = 10.33 m water |
| E_steel | 200 GPa |
| E_concrete | 5000√f_ck MPa (IS 456) |
| G_steel | 77 GPa |
| π | 3.1416 |
| e | 2.718 |

## Frequently Tested Patterns

1. **Successive percentage change** → `a + b + ab/100`
2. **Product stability** → `−x/(1 + x/100)`
3. **Relative speed** → same dir `x−y`, opposite `x+y`
4. **Time & work** → together `xy/(x+y)`
5. **CI − SI difference** (2 yr) → `P(r/100)²`
6. **Hydraulic jump** → sequent depth ratio
7. **Consolidation settlement** → `C_c H/(1+e₀) log(σ'/σ')`
8. **Bearing capacity** → Terzaghi factors
9. **SSD** → reaction + braking distance
10. **Unit hydrograph** → convolution

## Common Numerical Approaches

| Situation | Approach |
| --------- | -------- |
| Beam deflection | Standard formula table (memorize 5 cases) |
| Truss forces | Method of joints/sections |
| Indeterminate frame | Moment distribution / slope-deflection |
| Consolidation time | `T_v` → `t = T_v H_dr²/c_v` |
| Pipe network | Hardy Cross iteration |
| Flood routing | Muskingum coefficients |
| BOD | `BOD_t = L₀(1−e^(−kt))` |
| Population forecast | Arithmetic/geometric/incremental |
| Signal design | Webster's method |
| Curve setting | Deflection angle method |

## Final Checklist

- [ ] All P0 formulas memorized (30-min list above)
- [ ] All standard deflection cases
- [ ] Terzaghi bearing capacity factors
- [ ] Rankine earth pressure coefficients
- [ ] Manning's n values (common)
- [ ] IS 456 / IS 800 partial safety factors
- [ ] Unit conversions (kN↔N, mm²↔m², km/h↔m/s)
- [ ] Error-log questions re-solved
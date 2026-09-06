# HWRE — Rapid Revision

> 30-minute / 2-hour / 1-day revision plans. Use the night before an interview or mock test.

## 30-Minute (P0 Formulas Only)

### Fluid Mechanics & Hydraulics
| Formula | Equation |
|---------|----------|
| Continuity | `Q = A₁V₁ = A₂V₂` |
| Bernoulli | `P/γ + V²/2g + z = const` |
| Darcy-Weisbach | `h_f = f(L/D)(V²/2g)` |
| Reynolds | `Re = VD/ν` |
| Pump power | `P = γQH/η` |
| NPSH | `NPSH_A = P_atm/γ − P_v/γ − h_s − h_f` |

### Open Channel Flow
| Formula | Equation |
|---------|----------|
| Specific energy | `E = y + V²/2g` |
| Critical depth (rect) | `y_c = (q²/g)^(1/3)` |
| Froude | `Fr = V/√(gD_h)` |
| Manning | `V = (1/n)R^(2/3)S^(1/2)` |
| Conjugate depth | `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)` |
| Jump energy loss | `ΔE = (y₂−y₁)³/(4y₁y₂)` |

### Hydrology
| Formula | Equation |
|---------|----------|
| Rational method | `Q = CiA/360` (A in ha, i in mm/hr) |
| Horton infiltration | `f = f_c + (f₀−f_c)e^(−kt)` |
| Muskingum | `O₂ = C₀I₂ + C₁I₁ + C₂O₁` |
| Gumbel | `x_T = x̄ + K_Tσ` |
| Risk | `R = 1 − (1 − 1/T)^n` |

### Groundwater
| Formula | Equation |
|---------|----------|
| Darcy | `Q = KiA` |
| Transmissivity | `T = Kb` |
| Theis | `s = (Q/4πT)W(u)` |
| Cooper-Jacob | `s = (2.3Q/4πT)log(2.25Tt/r²S)` |
| Thiem | `Q = 2πT(h₂−h₁)/ln(r₂/r₁)` |

### Sediment Transport
| Formula | Equation |
|---------|----------|
| Shields | `τ* = τ₀/((ρ_s−ρ)gd)`, `τ_c* ≈ 0.047` |
| MPM | `q_b* = 8(τ*−τ_c*)^(3/2)` |
| Rouse | `c/c_a = (y_a/y)^Z`, `Z = w_s/(κu_τ)` |
| Strickler | `n = d₅₀^(1/6)/21.1` |

## 2-Hour (P0 + P1)

- [ ] 30 min: All P0 formulas above
- [ ] 15 min: Irrigation — duty-delta `D×Δ = 8.64B`, Lacey `V = (Qf²/140)^(1/6)`
- [ ] 15 min: Water supply — population forecasting, Hazen-Williams `h_f = 10.67LQ^1.85/(C^1.85D^4.87)`
- [ ] 15 min: Wastewater — BOD₅, ASP `V = QS₀Y(SRT)/(X(1+k_d·SRT))`
- [ ] 15 min: Flood control — SCS-CN `Q = (P−0.2S)²/(P+0.8S)`, `S = 25400/CN − 254`
- [ ] 15 min: Turbulence — RANS, k-ε, k-ω SST, y+ ranges
- [ ] 15 min: Review [`TRAPS.md`](TRAPS.md)
- [ ] 15 min: Review [`INTERVIEW.md`](INTERVIEW.md) top 10 questions

## 1-Day (Complete)

### Morning (2 hr)
- [ ] Full formula sheet review: [`formulas/hwre-formulas.md`](formulas/hwre-formulas.md)
- [ ] Re-solve 5 practice problems from [`practice/hwre-practice.md`](practice/hwre-practice.md)

### Afternoon (2 hr)
- [ ] Review all subject guides' key concepts (skim)
- [ ] Review [`MODELLING.md`](MODELLING.md) pipeline (HEC-HMS → HEC-RAS → GIS)

### Evening (2 hr)
- [ ] Review [`INTERVIEW.md`](INTERVIEW.md) full Q&A bank
- [ ] Review [`TRAPS.md`](TRAPS.md) full list
- [ ] Review [`ERROR_ANALYSIS.md`](ERROR_ANALYSIS.md) error log — reattempt all open errors

### Night (1 hr)
- [ ] 30-min P0 formula sprint (above)
- [ ] Sleep early — 8 hours

## Key Values to Memorize

| Value | Number |
|-------|--------|
| Water density | 1000 kg/m³ |
| Specific weight γ | 9810 N/m³ |
| Kinematic viscosity ν (20°C) | 1.0 × 10⁻⁶ m²/s |
| Dynamic viscosity μ (20°C) | 1.0 × 10⁻³ Pa·s |
| g | 9.81 m/s² |
| Atmospheric pressure | 101.3 kPa |
| Laminar limit | Re < 2000 |
| Turbulent | Re > 4000 |
| Critical Shields | 0.047 |
| von Kármán κ | 0.41 |

## Related

- [MASTER_INDEX.md](MASTER_INDEX.md) · [HWRE_ROADMAP.md](HWRE_ROADMAP.md) · [formulas/hwre-formulas.md](formulas/hwre-formulas.md) · [TRAPS.md](TRAPS.md) · [INTERVIEW.md](INTERVIEW.md)
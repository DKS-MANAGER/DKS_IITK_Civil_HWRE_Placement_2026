# Hydraulics/CFD Engineer — Rapid Revision Sheet

> Last-minute cheat sheet for hydraulics and CFD technical interviews.

---

## Framework 1: Pipe Flow Essentials

### Governing Equations
| Equation | Formula | Use |
|:---------|:--------|:----|
| Continuity | A₁V₁ = A₂V₂ = Q | Mass conservation |
| Bernoulli | P/γ + V²/2g + z = const | Energy along streamline |
| Darcy-Weisbach | h_f = f(L/D)(V²/2g) | Friction loss |
| Hazen-Williams | V = 0.85C·R^0.63·S^0.54 | Empirical, water only |
| Manning (pipe) | V = (1/n)R^{2/3}S^{1/2} | Open channel or full pipe |

### Reynolds Number
- Re = ρVD/μ = VD/ν
- Re < 2300: Laminar → f = 64/Re
- 2300 < Re < 4000: Transition
- Re > 4000: Turbulent → Colebrook-White or Moody chart

### Minor Losses
| Fitting | Typical K value |
|:--------|:---------------:|
| Sharp entrance | 0.5 |
| Rounded entrance | 0.05 |
| Sudden expansion | (1 - A₁/A₂)² |
| Sudden contraction | 0.5(1 - A₂/A₁) |
| 90° elbow (regular) | 0.9 |
| 90° elbow (long radius) | 0.3 |
| Gate valve (fully open) | 0.2 |
| Globe valve (fully open) | 10 |

### Hardy Cross Method
1. Assume Q in each loop (satisfy continuity at junctions)
2. Compute h_f = rQ|Q| for each pipe (r = 8fL/(π²gD⁵))
3. Compute Σh_f and Σ(2r|Q|) for each loop
4. ΔQ = -Σh_f / Σ(2r|Q|) (correction factor)
5. Apply correction, iterate until ΔQ < tolerance

### Pump Selection
- **System curve:** H_required = H_static + h_f(Q)
- **Pump curve:** H_available = f(Q) from manufacturer
- **Operating point:** Intersection of system and pump curves
- **NPSH_available** = P_atm/γ + P_suction/γ - P_vapor/γ - h_f(suction)
- **NPSH_available > NPSH_required** (by at least 0.5m margin)

### Water Hammer
- **Joukowsky:** ΔP = ρcΔV
- **Wave speed:** c = √(K/ρ) / √(1 + KD/(Et)) for elastic pipe
- **Mitigation:** Surge tanks, air valves, slow-closing valves, bypass pipes

---

## Framework 2: Turbulence & CFD Quick Reference

### Turbulence Models
| Model | Equations | Best For | Limitations |
|:------|:----------|:---------|:------------|
| k-ε (standard) | k, ε | Fully developed turbulent flow | Poor for separated/swirl flows |
| k-ε Realizable | k, ε | Better for rotation, separation | Still wall-bounded limitations |
| k-ω | k, ω | Near-wall, adverse pressure gradients | Sensitive to freestream ω |
| k-ω SST | k, ω + blending | General purpose, separated flows | Slightly more expensive |
| RSM | 7 transport eqs | Anisotropic turbulence, swirl | Expensive, convergence issues |
| LES | Filtered N-S + SGS | Unsteady, separated, mixing | Very expensive (wall-resolved) |
| DNS | Full N-S | Fundamental research | Extremely expensive (Re^{9/4}) |

### Key y+ Requirements
- **Low-Re (DNS, wall-resolved LES):** y+ < 1
- **Transitional: y+ < 5 (no wall function)**
- **Wall functions:** y+ ≈ 30–300
- **Beyond log-law:** y+ > 300 (rarely appropriate)

### OpenFOAM Solver Quick Reference
| Solver | Use Case |
|:-------|:---------|
| `simpleFoam` | Steady-state incompressible RANS |
| `pimpleFoam` | Transient incompressible (LES/RANS) |
| `buoyantSimpleFoam` | Steady natural/convection-driven |
| `buoyantPimpleFoam` | Transient buoyancy-driven |
| `interFoam` | VOF multiphase (two-phase) |
| `sonicFoam` | Compressible transonic/supersonic |
| `rhoCentralFoam` | Density-based compressible |

### Mesh Quality Metrics
| Metric | Acceptable Range |
|:-------|:----------------:|
| Skewness | < 0.95 (ideally < 0.5) |
| Orthogonality | > 0.1 (ideally > 0.5) |
| Aspect ratio | < 100 (ideally < 20) |
| Non-orthogonality | < 65 (ideally < 40) |

---

## Framework 3: Open Channel Flow Quick Reference

### Critical Flow Parameters
| Quantity | Formula (Rectangular) |
|:---------|:----------------------|
| Froude number | Fr = V/√(gD_h) |
| Critical depth | y_c = (q²/g)^{1/3} |
| Critical velocity | V_c = √(gy_c) |
| Specific energy at critical | E_min = 1.5y_c |

### Hydraulic Jump (Rectangular Channel)
| Parameter | Formula |
|:----------|:--------|
| Conjugate depth | y₂/y₁ = 0.5(√(1 + 8Fr₁²) - 1) |
| Head loss | ΔE = (y₂ - y₁)³ / (4y₁y₂) |
| Energy dissipation ratio | ΔE/E₁ |
| Power dissipated | P = γQΔE |

### Manning's Equation
- **Velocity:** V = (1/n)R^{2/3}S^{1/2}
- **Discharge:** Q = (1/n)AR^{2/3}S^{1/2}
- **Hydraulic radius:** R = A/P (wetted perimeter)
- **Best hydraulic section:** R = y/2 (rectangular), dP/dy = 0

### GVF Profile Types
| Slope | Condition | Profiles |
|:------|:----------|:---------|
| Mild (M) | y_c < y_n | M1 (backwater), M2 (drawdown), M3 |
| Steep (S) | y_c > y_n | S1, S2, S3 |
| Critical (C) | y_c = y_n | C1, C3 |
| Horizontal (H) | S₀ = 0 | H2, H3 |
| Adverse (A) | S₀ < 0 | A2, A3 |

### Flow Measurement
| Device | Formula | Application |
|:-------|:--------|:------------|
| Sharp-crested weir | Q = (2/3)C_d·b·√(2g)·H^{3/2} | Measurement |
| Broad-crested weir | Q = C_d·b·√(g)·H^{3/2} | Measurement |
| Parshall flume | Q = C·H_a^n (calibrated) | Irrigation canals |
| Venturi flume | Q = C_d·A₁A₂/√(A₁²-A₂²)·√(2gH) | Open channel constriction |

---

## Framework 4: Interview Quick-Fire Answers

1. **"What is Bernoulli's equation?"** — Energy conservation along a streamline: P/γ + V²/2g + z = constant (assuming no friction, incompressible, steady).

2. **"What is the difference between Darcy-Weisbach and Hazen-Williams?"** — DW is physics-based (universal, any fluid); HW is empirical (water only, normal temps).

3. **"When does a hydraulic jump occur?"** — When supercritical flow (Fr > 1) transitions to subcritical (Fr < 1). Requires a downstream control or slope change.

4. **"What is the difference between RANS and LES?"** — RANS time-averages all turbulence (models everything); LES resolves large eddies directly, models only small scales (more accurate, more expensive).

5. **"What is the purpose of a surge tank?"** — Absorbs pressure transients (water hammer) in pipe systems by providing a free surface to decelerate/accelerate water gradually.

6. **"What is specific energy?"** — E = y + V²/(2g) = y + q²/(2gy²). Energy per unit weight measured from the channel bed. Minimum at critical depth.

7. **"What is y+ and why does it matter in CFD?"** — Dimensionless wall distance y+ = y·u_τ/ν. Determines whether viscous sublayer is resolved (y+ < 1) or modeled with wall functions (y+ ≈ 30-300).

8. **"What is NPSH?"** — Net Positive Suction Head. Available NPSH must exceed required NPSH to prevent cavitation. NPSH_a = P_atm/γ - P_vapor/γ - h_f(suction) - z_suction.

9. **"Why is k-ω SST preferred for separated flows?"** — It uses k-ε in the freestream (insensitive to freestream) and k-ω near walls (better for adverse pressure gradients). The SST blending function handles the transition.

10. **"What is Richardson extrapolation?"** — Method to estimate the grid-independent solution: φ = φ_h + C·h^p, where h is grid spacing, p is order of convergence. Requires 3 mesh levels.

---

## Last-Minute Checklist

- [ ] Bernoulli, Darcy-Weisbach, Manning memorized
- [ ] Hardy Cross method steps clear
- [ ] NPSH concept explained
- [ ] Water hammer equation (Joukowsky) known
- [ ] k-ε vs k-ω SST know when to use each
- [ ] y+ requirements for different wall treatments
- [ ] Specific energy diagram and critical depth formulas
- [ ] Hydraulic jump conjugate depth formula
- [ ] GVF profile classification (M1, M2, M3, etc.)
- [ ] OpenFOAM solver names and use cases
- [ ] Project pitch ready (3 minutes)
- [ ] Troubleshooting diverging simulation (5 steps)

---

## Cross-Links

**Study:**
→ [Hydraulics Full Reference](hydraulics.md)
→ [Turbulence Modeling Deep Dive](turbulence-modeling.md)
→ [Open Channel Flow](../open_channel_flow/open-channel-flow.md)
→ [Role Study Plan](role-study-plan.md)

**Deeper:**
→ [Water Resources Engineering](../water_resources/water-resources-engineering.md)
→ [Hydrology](../hydrology/hydrology.md)

**Interview:**
→ [Technical Interview Bank](../../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../../prep/behavioral/behavioral-interview-guide.md)

---

*Last updated: 2026-09-04*

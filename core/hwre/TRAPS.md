# HWRE — Common Traps & Mistakes

> Catalog of the most common mistakes in HWRE problems and interviews. Review before every mock test.

## 1. Unit Conversion Traps

| Trap | Correct Approach |
|------|------------------|
| Rational method: A in km² vs ha | `Q = CiA/360` (A in ha, i in mm/hr); `Q = CiA/3.6` (A in km²) |
| m³/s → MLD | Multiply by 86.4 |
| mm/hr → m/s | Divide by 3,600,000 |
| Manning n imperial vs SI | SI: `V = (1/n)R^(2/3)S^(1/2)`; imperial: multiply by 1.49 |
| Darcy velocity vs seepage | Travel time uses seepage velocity `v_s = Ki/n`, not `v = Ki` |
| 1 ha-mm of water | = 10 m³ |

## 2. Formula Misapplication Traps

| Trap | Correct Approach |
|------|------------------|
| Theis vs Cooper-Jacob | Check `u = r²S/(4Tt)`; CJ valid only when u < 0.01 |
| Muskingum coefficients | Always verify `C₀ + C₁ + C₂ = 1` |
| Hydraulic jump conjugate depth | `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)` — not the energy equation |
| Specific energy minimum | At critical depth, `E_min = 1.5y_c`, not `y_c` |
| BOD₅ vs ultimate BOD | `BOD₅ = L₀(1 − e^(−5k))`; don't confuse L₀ with BOD₅ |
| SCS-CN S units | `S = 25400/CN − 254` gives S in mm (not inches) |
| Gumbel K_T | `K_T = −(√6/π)[0.5772 + ln(ln(T/(T−1)))]` — sign matters |
| Thiem vs Dupuit | Thiem: confined, uses h (linear); Dupuit: unconfined, uses h² |
| Darcy-Weisbach f vs Fanning f | Darcy f = 4 × Fanning f |
| Hazen-Williams C vs Manning n | C high = smooth (100–140); n low = smooth (0.011–0.013) |

## 3. Concept Traps

| Trap | Correct Understanding |
|------|----------------------|
| Critical depth vs normal depth | y_c depends on Q and section; y_n depends on Q, section, and slope |
| Subcritical vs supercritical control | Subcritical: downstream control; supercritical: upstream control |
| M1 vs M2 profile | M1: y > y_c > y_n (backwater, dam); M2: y_c > y > y_n (drawdown, weir) |
| Hydraulic jump location | Occurs where sequent depth of supercritical flow = downstream depth |
| Confined vs unconfined storativity | Confined: S = 10⁻⁵–10⁻³ (elastic); unconfined: S_y = 0.01–0.30 (gravity) |
| Firm yield vs secondary yield | Firm: dependable (95%); secondary: bonus in wet years |
| Trap efficiency vs useful life | Trap efficiency (Brune) ≠ reservoir useful life (sediment volume) |
| Clear-water vs live-bed scour | Clear-water: V < V_c, no supply; live-bed: V > V_c, with supply |
| RANS vs LES vs DNS | RANS: time-averaged; LES: large scales resolved; DNS: all scales |
| NPSH_A vs NPSH_R | Cavitation when NPSH_A < NPSH_R |

## 4. Interview Traps

| Trap | Better Answer |
|------|---------------|
| "Bernoulli assumptions?" | Steady, incompressible, frictionless, along streamline — mention all four |
| "Why does the hydraulic jump dissipate energy?" | Turbulence + mixing convert kinetic energy to heat; sequent depth relation |
| "What is the difference between Muskingum and level-pool routing?" | Muskingum: channel (wedge + prism storage); level-pool: reservoir (horizontal surface) |
| "How do you determine reservoir storage?" | Mass curve (Rippl): max vertical departure between cumulative inflow and demand line |
| "What is the Theis equation used for?" | Pumping test analysis → determine T and S; predict drawdown |
| "What is specific energy?" | Energy per unit weight relative to channel bed: `E = y + V²/2g` |
| "Why is the Froude number important?" | Classifies flow regime; governs controls and wave propagation |
| "What is the difference between Darcy velocity and seepage velocity?" | Darcy: Q/A (bulk); seepage: Q/(nA) (actual pore velocity) |

## 5. Numerical Traps

| Trap | Example |
|------|---------|
| Forgot to convert time to seconds | Theis: t in seconds, not minutes |
| Used diameter instead of radius | Pipe flow: D in Darcy-Weisbach, r in Hagen-Poiseuille |
| Forgot hydrostatic force acts at center of pressure | Not centroid — `h_cp = h̄ + I_G/(Ah̄)` |
| Mixed gauge and absolute pressure | NPSH uses absolute pressure |
| Forgot to subtract losses in Bernoulli | Include `h_L` term |
| Used arithmetic mean for areal rainfall | Use Thiessen or isohyetal for non-uniform rainfall |

## Review Protocol

- [ ] Before every mock test: re-read this file (5 min)
- [ ] After every error: log in [`ERROR_ANALYSIS.md`](ERROR_ANALYSIS.md) with code C6 (trap)
- [ ] Weekly: re-read the 5 traps most relevant to your weak topics

## Related

- [MASTER_INDEX.md](MASTER_INDEX.md) · [ERROR_ANALYSIS.md](ERROR_ANALYSIS.md) · [formulas/hwre-formulas.md](formulas/hwre-formulas.md) · [INTERVIEW.md](INTERVIEW.md)
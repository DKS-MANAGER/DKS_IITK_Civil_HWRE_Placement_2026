# HWRE — Practice Problems with Solutions

> Verified solved problems covering all HWRE subjects. Format: Given → Find → Concept → Formula → Calculation → Answer → Trap.

## Problem 1: Pipe Flow — Darcy-Weisbach

**Given:** Water flows through a 200 mm diameter, 500 m long pipe at 0.05 m³/s. f = 0.02.

**Find:** Head loss due to friction.

**Concept:** Darcy-Weisbach for pipe friction.

**Formula:** `h_f = f(L/D)(V²/2g)`

**Calculation:**
- A = π(0.2)²/4 = 0.0314 m²
- V = Q/A = 0.05/0.0314 = 1.59 m/s
- h_f = 0.02 × (500/0.2) × (1.59²/(2×9.81))
- h_f = 0.02 × 2500 × 0.129 = 6.45 m

**Answer:** h_f = **6.45 m**

**Trap:** Use diameter (not radius) in Darcy-Weisbach.

---

## Problem 2: Bernoulli with Losses

**Given:** Water flows from a reservoir (surface elevation 100 m) through a pipe to a nozzle at elevation 50 m. Velocity at nozzle = 10 m/s, head loss = 5 m.

**Find:** Pressure at nozzle exit.

**Concept:** Bernoulli with losses; nozzle exit is atmospheric.

**Formula:** `P₁/γ + V₁²/2g + z₁ = P₂/γ + V₂²/2g + z₂ + h_L`

**Calculation:**
- Reservoir surface: P₁ = 0 (gauge), V₁ ≈ 0, z₁ = 100
- Nozzle exit: P₂ = 0 (atmospheric), V₂ = 10, z₂ = 50
- 0 + 0 + 100 = 0 + 10²/(2×9.81) + 50 + 5
- 100 = 5.10 + 50 + 5 = 60.10
- Contradiction → the given data is inconsistent; reservoir must be higher or losses lower.

**Answer:** Data inconsistent — check: required z₁ = 60.1 m for these conditions.

**Trap:** Always verify energy balance; nozzle exit is atmospheric pressure.

---

## Problem 3: Hydraulic Jump

**Given:** Rectangular channel, q = 5 m²/s, upstream depth y₁ = 0.5 m.

**Find:** Conjugate depth y₂ and energy loss.

**Concept:** Hydraulic jump conjugate depth.

**Formula:** `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)`, `ΔE = (y₂−y₁)³/(4y₁y₂)`

**Calculation:**
- V₁ = q/y₁ = 5/0.5 = 10 m/s
- Fr₁ = V₁/√(gy₁) = 10/√(9.81×0.5) = 10/2.21 = 4.52
- y₂ = 0.5 × 0.5 × (√(1+8×4.52²) − 1) = 0.25 × (√(1+163.4) − 1)
- y₂ = 0.25 × (12.82 − 1) = 0.25 × 11.82 = 2.96 m
- ΔE = (2.96−0.5)³/(4×0.5×2.96) = (2.46)³/5.92 = 14.89/5.92 = 2.50 m

**Answer:** y₂ = **2.96 m**, ΔE = **2.50 m**

**Trap:** Use Froude number (not velocity) in conjugate depth formula.

---

## Problem 4: Critical Depth

**Given:** Rectangular channel, Q = 10 m³/s, width b = 4 m.

**Find:** Critical depth and minimum specific energy.

**Concept:** Critical flow in rectangular channel.

**Formula:** `y_c = (q²/g)^(1/3)`, `E_min = 1.5y_c`

**Calculation:**
- q = Q/b = 10/4 = 2.5 m²/s
- y_c = (2.5²/9.81)^(1/3) = (6.25/9.81)^(1/3) = (0.637)^(1/3) = 0.86 m
- E_min = 1.5 × 0.86 = 1.29 m

**Answer:** y_c = **0.86 m**, E_min = **1.29 m**

**Trap:** E_min = 1.5y_c, not y_c.

---

## Problem 5: Manning's Equation

**Given:** Trapezoidal canal, b = 3 m, side slope z = 1.5, y = 1.5 m, S = 0.0005, n = 0.022.

**Find:** Discharge Q.

**Concept:** Manning's equation for open channel.

**Formula:** `Q = (1/n)AR^(2/3)S^(1/2)`

**Calculation:**
- A = (b + zy)y = (3 + 1.5×1.5)×1.5 = (3+2.25)×1.5 = 7.875 m²
- P = b + 2y√(1+z²) = 3 + 2×1.5×√(1+2.25) = 3 + 3×1.803 = 8.41 m
- R = A/P = 7.875/8.41 = 0.936 m
- Q = (1/0.022) × 7.875 × (0.936)^(2/3) × (0.0005)^(1/2)
- Q = 45.45 × 7.875 × 0.957 × 0.0224 = 7.67 m³/s

**Answer:** Q = **7.67 m³/s**

**Trap:** R = A/P, not y for trapezoidal sections.

---

## Problem 6: Muskingum Routing

**Given:** K = 6 h, X = 0.2, Δt = 3 h. Inflow: I₁=100, I₂=150, I₃=200, I₄=180, I₅=120 m³/s.

**Find:** Outflow O₅.

**Concept:** Muskingum channel routing.

**Formula:** `O₂ = C₀I₂ + C₁I₁ + C₂O₁`

**Calculation:**
- C₀ = (−6×0.2 + 1.5)/(6×0.8 + 1.5) = 0.3/6.3 = 0.0476
- C₁ = (6×0.2 + 1.5)/6.3 = 2.7/6.3 = 0.4286
- C₂ = 1 − 0.0476 − 0.4286 = 0.5238
- O₁ = I₁ = 100
- O₂ = 0.0476(150) + 0.4286(100) + 0.5238(100) = 7.14 + 42.86 + 52.38 = 102.38
- O₃ = 0.0476(200) + 0.4286(150) + 0.5238(102.38) = 9.52 + 64.29 + 53.63 = 127.44
- O₄ = 0.0476(180) + 0.4286(200) + 0.5238(127.44) = 8.57 + 85.72 + 66.75 = 161.04
- O₅ = 0.0476(120) + 0.4286(180) + 0.5238(161.04) = 5.71 + 77.15 + 84.35 = 167.21

**Answer:** O₅ = **167.21 m³/s**

**Trap:** Verify C₀ + C₁ + C₂ = 1.

---

## Problem 7: Rational Method

**Given:** Catchment area = 50 ha, runoff coefficient C = 0.6, rainfall intensity i = 40 mm/hr.

**Find:** Peak discharge Q_p.

**Concept:** Rational method for small catchments.

**Formula:** `Q = CiA/360` (A in ha, i in mm/hr)

**Calculation:**
- Q = 0.6 × 40 × 50 / 360 = 1200/360 = 3.33 m³/s

**Answer:** Q_p = **3.33 m³/s**

**Trap:** Use /360 for hectares, /3.6 for km².

---

## Problem 8: SCS-CN Method

**Given:** CN = 80, rainfall P = 120 mm.

**Find:** Direct runoff Q.

**Concept:** SCS curve number method.

**Formula:** `S = 25400/CN − 254`, `Q = (P−0.2S)²/(P+0.8S)`

**Calculation:**
- S = 25400/80 − 254 = 317.5 − 254 = 63.5 mm
- P > 0.2S = 12.7 ✓
- Q = (120 − 0.2×63.5)²/(120 + 0.8×63.5) = (120−12.7)²/(120+50.8)
- Q = (107.3)²/170.8 = 11513/170.8 = 67.4 mm

**Answer:** Q = **67.4 mm**

**Trap:** S in mm (not inches) when P in mm.

---

## Problem 9: Gumbel Flood Frequency

**Given:** Annual peak flows: mean x̄ = 500 m³/s, σ = 100 m³/s. Return period T = 100 years.

**Find:** 100-year flood.

**Concept:** Gumbel EV1 distribution.

**Formula:** `x_T = x̄ + K_Tσ`, `K_T = −(√6/π)[0.5772 + ln(ln(T/(T−1)))]`

**Calculation:**
- K_T = −(0.7797)[0.5772 + ln(ln(100/99))]
- ln(100/99) = ln(1.0101) = 0.01005
- ln(0.01005) = −4.60
- K_T = −0.7797 × (0.5772 − 4.60) = −0.7797 × (−4.023) = 3.137
- x₁₀₀ = 500 + 3.137 × 100 = 500 + 313.7 = 813.7 m³/s

**Answer:** 100-year flood = **813.7 m³/s**

**Trap:** K_T sign — negative inside brackets gives positive K_T for T > 2.33.

---

## Problem 10: Theis Equation

**Given:** Q = 0.01 m³/s, T = 0.001 m²/s, S = 0.0001, r = 50 m, t = 1 day.

**Find:** Drawdown s.

**Concept:** Theis unsteady confined flow.

**Formula:** `u = r²S/(4Tt)`, `s = (Q/4πT)W(u)`

**Calculation:**
- t = 86400 s
- u = 50² × 0.0001/(4 × 0.001 × 86400) = 0.25/345.6 = 0.000723
- W(u) ≈ −0.5772 − ln(0.000723) = −0.5772 + 7.23 = 6.65
- s = (0.01/(4π×0.001)) × 6.65 = 0.796 × 6.65 = 5.29 m

**Answer:** s = **5.29 m**

**Trap:** t in seconds, not days.

---

## Problem 11: Cooper-Jacob

**Given:** Q = 0.02 m³/s, r = 100 m. Drawdown at t = 1000 min = 2.5 m, at t = 10000 min = 3.2 m.

**Find:** T and S.

**Concept:** Cooper-Jacob straight-line method.

**Formula:** `T = 2.3Q/(4π·slope)`, `S = 2.25Tt₀/r²`

**Calculation:**
- Slope = (3.2−2.5)/log(10000/1000) = 0.7/1 = 0.7 m/log cycle
- T = 2.3 × 0.02/(4π × 0.7) = 0.046/8.796 = 0.00523 m²/s
- t₀ at s=0: t₀ = 1000 × 10^(−2.5/0.7) = 1000 × 10^(−3.57) = 1000 × 0.000269 = 0.269 min
- t₀ = 0.269 × 60 = 16.14 s
- S = 2.25 × 0.00523 × 16.14/100² = 0.190/10000 = 1.90 × 10⁻⁵

**Answer:** T = **0.00523 m²/s**, S = **1.90 × 10⁻⁵**

**Trap:** Convert t₀ to seconds before computing S.

---

## Problem 12: Thiem Equation

**Given:** Confined aquifer, T = 0.005 m²/s. r₁ = 10 m (h₁ = 95 m), r₂ = 100 m (h₂ = 99 m).

**Find:** Discharge Q.

**Concept:** Thiem steady confined flow.

**Formula:** `Q = 2πT(h₂−h₁)/ln(r₂/r₁)`

**Calculation:**
- Q = 2π × 0.005 × (99−95)/ln(100/10) = 0.1257/2.303 = 0.0546 m³/s

**Answer:** Q = **0.0546 m³/s**

**Trap:** h₂ > h₁ (head increases with distance from pumping well).

---

## Problem 13: Reservoir Storage (Mass Curve)

**Given:** Monthly inflows (m³/s): 50, 80, 120, 90, 60, 40, 30, 35, 45, 70, 100, 80. Demand = 65 m³/s.

**Find:** Required storage.

**Concept:** Mass curve (Rippl) method.

**Formula:** Max vertical departure between cumulative inflow and demand line.

**Calculation:**
- Monthly volume = 30 × 86400 = 2.592 × 10⁶ m³ per m³/s
- Monthly surplus (inflow − demand): −15, +15, +55, +25, −5, −25, −35, −30, −20, +5, +35, +15
- Running sum: −15, 0, 55, 80, 75, 50, 15, −15, −35, −30, 5, 20
- Peak = 80 (month 4), trough = −35 (month 9)
- Max cumulative deficit = 80 − (−35) = 115 m³/s-months
- Storage = 115 × 2.592 × 10⁶ = 298 × 10⁶ m³

**Answer:** Required storage ≈ **298 Mm³**

**Trap:** Storage is max cumulative deficit, not single-month deficit.

---

## Problem 14: Duty and Delta

**Given:** Base period B = 120 days, duty D = 800 hectares/cumec.

**Find:** Delta Δ.

**Concept:** Duty-delta relationship.

**Formula:** `Δ = 8.64B/D`

**Calculation:**
- Δ = 8.64 × 120/800 = 1036.8/800 = 1.296 m

**Answer:** Δ = **1.30 m**

**Trap:** B in days, D in hectares/cumec, Δ in metres.

---

## Problem 15: BOD Calculation

**Given:** Ultimate BOD L₀ = 250 mg/L, k = 0.23 day⁻¹.

**Find:** BOD₅.

**Concept:** BOD kinetics.

**Formula:** `BOD₅ = L₀(1 − e^(−5k))`

**Calculation:**
- BOD₅ = 250 × (1 − e^(−1.15)) = 250 × (1 − 0.317) = 250 × 0.683 = 170.7 mg/L

**Answer:** BOD₅ = **170.7 mg/L**

**Trap:** BOD₅ ≠ L₀; it's the 5-day oxygen demand.

---

## Problem 16: ASP Tank Volume

**Given:** Q = 10 ML/d, S₀ = 250 mg/L, S = 20 mg/L, X = 2500 mg/L, Y = 0.5, k_d = 0.06 day⁻¹, SRT = 10 days.

**Find:** Aeration tank volume V.

**Concept:** Activated sludge process design.

**Formula:** `V = QS₀Y(SRT)/(X(1 + k_d·SRT))`

**Calculation:**
- Q = 10 ML/d = 10,000 m³/d
- V = 10000 × 250 × 0.5 × 10/(2500 × (1 + 0.06×10))
- V = 12,500,000/(2500 × 1.6) = 12,500,000/4000 = 3125 m³

**Answer:** V = **3125 m³**

**Trap:** Use S₀ (influent), not S (effluent), in the numerator.

---

## Problem 17: Population Forecasting

**Given:** Population: 1981: 50,000; 1991: 65,000; 2001: 85,000.

**Find:** 2021 population by geometric increase.

**Concept:** Geometric growth method.

**Formula:** `P_n = P₀(1+r)^n`

**Calculation:**
- r₁ = (65/50)^(1/10) − 1 = 1.0265 − 1 = 0.0265
- r₂ = (85/65)^(1/10) − 1 = 1.0271 − 1 = 0.0271
- r_avg = (0.0265 + 0.0271)/2 = 0.0268
- P₂₀₂₁ = 85000 × (1.0268)^20 = 85000 × 1.695 = 144,075

**Answer:** P₂₀₂₁ ≈ **144,000**

**Trap:** Use average growth rate, not single-decade rate.

---

## Problem 18: Shields Parameter

**Given:** d = 1 mm, bed slope S = 0.001, depth y = 2 m. ρ_s = 2650 kg/m³, ρ = 1000 kg/m³.

**Find:** Shields parameter τ* and check incipient motion.

**Concept:** Shields criterion for incipient motion.

**Formula:** `τ₀ = ρgRS`, `τ* = τ₀/((ρ_s−ρ)gd)`

**Calculation:**
- R ≈ y = 2 m (wide channel)
- τ₀ = 1000 × 9.81 × 2 × 0.001 = 19.62 Pa
- τ* = 19.62/((2650−1000) × 9.81 × 0.001) = 19.62/(1650 × 0.00981)
- τ* = 19.62/16.19 = 1.21

**Answer:** τ* = **1.21** > 0.047 → sediment in motion (live-bed)

**Trap:** τ* > τ_c* means motion; τ* < τ_c* means no motion.

---

## Problem 19: HEC-18 Pier Scour

**Given:** Pier width a = 1 m, approach depth y₁ = 3 m, velocity V = 2 m/s. K₁=K₂=K₃=K₄=1.

**Find:** Scour depth y_s.

**Concept:** HEC-18 pier scour equation.

**Formula:** `y_s/y₁ = 2.0K₁K₂K₃K₄(a/y₁)^0.35 Fr^0.43`

**Calculation:**
- Fr = V/√(gy₁) = 2/√(9.81×3) = 2/5.42 = 0.369
- y_s/y₁ = 2.0 × (1/3)^0.35 × (0.369)^0.43
- y_s/y₁ = 2.0 × 0.681 × 0.641 = 0.873
- y_s = 0.873 × 3 = 2.62 m

**Answer:** y_s = **2.62 m** (precise: 2.66 m)

**Trap:** Use approach depth y₁ (not pier width) in Froude number.

---

## Problem 20: Specific Energy

**Given:** Rectangular channel, q = 3 m²/s, depth y = 1.5 m.

**Find:** Specific energy and flow regime.

**Concept:** Specific energy and critical flow.

**Formula:** `E = y + q²/(2gy²)`, `y_c = (q²/g)^(1/3)`

**Calculation:**
- E = 1.5 + 9/(2×9.81×2.25) = 1.5 + 9/44.15 = 1.5 + 0.204 = 1.70 m
- y_c = (9/9.81)^(1/3) = (0.917)^(1/3) = 0.972 m
- y = 1.5 > y_c = 0.972 → subcritical

**Answer:** E = **1.70 m**, subcritical (y > y_c)

**Trap:** Compare y with y_c to determine regime, not E.

---

## Problem 21: NPSH

**Given:** Pump suction: P_atm = 101.3 kPa, P_v = 2.34 kPa (20°C), suction lift h_s = 3 m, suction friction h_f = 1 m.

**Find:** NPSH_A.

**Concept:** Net positive suction head available.

**Formula:** `NPSH_A = P_atm/γ − P_v/γ − h_s − h_f`

**Calculation:**
- P_atm/γ = 101300/9810 = 10.33 m
- P_v/γ = 2340/9810 = 0.24 m
- NPSH_A = 10.33 − 0.24 − 3 − 1 = 6.09 m

**Answer:** NPSH_A = **6.09 m**

**Trap:** Use absolute pressure for P_atm, not gauge.

---

## 📋 Answer Key

| # | Answer | # | Answer |
|---|--------|---|--------|
| 1 | 6.45 m | 12 | 0.0546 m³/s |
| 2 | Data inconsistent | 13 | ~298 Mm³ |
| 3 | 2.96 m, 2.52 m | 14 | 1.30 m |
| 4 | 0.86 m, 1.29 m | 15 | 170.7 mg/L |
| 5 | 7.67 m³/s | 16 | 3125 m³ |
| 6 | 167.21 m³/s | 17 | ~144,000 |
| 7 | 3.33 m³/s | 18 | 1.21 (motion) |
| 8 | 67.4 mm | 19 | 2.62 m |
| 9 | 813.7 m³/s | 20 | 1.70 m (subcritical) |
| 10 | 5.29 m | 21 | 6.09 m |
| 11 | 0.00523 m²/s, 1.9×10⁻⁵ | | |

## Topic Diagnosis

| Topic | Problems | Status |
|-------|----------|--------|
| Pipe flow | 1, 2, 21 | ✅ Covered |
| Open channel | 3, 4, 5, 20 | ✅ Covered |
| Hydrology | 6, 7, 8, 9 | ✅ Covered |
| Groundwater | 10, 11, 12 | ✅ Covered |
| Water resources | 13, 14 | ✅ Covered |
| Wastewater | 15, 16 | ✅ Covered |
| Water supply | 17 | ✅ Covered |
| Sediment | 18, 19 | ✅ Covered |

## Practice Strategy

1. Solve each problem in under 5 minutes (timed).
2. Log errors in [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md).
3. Reattempt after 24 hours.
4. Review [`TRAPS.md`](../TRAPS.md) before each session.

## References

- [formulas/hwre-formulas.md](../formulas/hwre-formulas.md) — canonical formulas
- [mocks/hwre-mock-1.md](../mocks/hwre-mock-1.md) — full mock test
- Subject guides in [`core/hwre`](../README.md)
# HWRE — Mock Test 1

> Full HWRE placement mock test. 20 questions, 60 minutes. Covers all P0/P1 subjects.

## Instructions

- Time: 60 minutes
- Marks: 20 × 5 = 100 (each question 5 marks)
- No negative marking
- Attempt all questions
- Log errors in [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md) after completion

---

## Section A: Fluid Mechanics & Hydraulics (Q1–Q5)

### Q1. Water flows through a 150 mm pipe at 0.03 m³/s. What is the velocity?
- A) 1.2 m/s
- B) 1.7 m/s
- C) 2.1 m/s
- D) 2.5 m/s

### Q2. A pump delivers 0.1 m³/s against a head of 20 m at 75% efficiency. What is the power required?
- A) 19.6 kW
- B) 26.2 kW
- C) 32.7 kW
- D) 39.3 kW

### Q3. What is the Reynolds number for water (ν = 1×10⁻⁶ m²/s) at 2 m/s in a 200 mm pipe?
- A) 2×10⁵
- B) 4×10⁵
- C) 6×10⁵
- D) 8×10⁵

### Q4. NPSH_A = 10.33 − 0.24 − 3 − 1 = ?
- A) 5.09 m
- B) 6.09 m
- C) 7.09 m
- D) 8.09 m

### Q5. For laminar pipe flow, the Darcy friction factor f = ?
- A) 16/Re
- B) 32/Re
- C) 64/Re
- D) 128/Re

---

## Section B: Open Channel Flow (Q6–Q10)

### Q6. Rectangular channel, q = 4 m²/s. What is the critical depth?
- A) 0.87 m
- B) 1.18 m
- C) 1.42 m
- D) 1.65 m

### Q7. A hydraulic jump has upstream Fr₁ = 6. What is y₂/y₁?
- A) 5.5
- B) 6.9
- C) 7.8
- D) 8.5

### Q8. Trapezoidal channel, b = 4 m, z = 1, y = 2 m. What is the area?
- A) 10 m²
- B) 12 m²
- C) 14 m²
- D) 16 m²

### Q9. Manning's n = 0.013, R = 1 m, S = 0.001. What is the velocity?
- A) 1.5 m/s
- B) 2.0 m/s
- C) 2.4 m/s
- D) 3.0 m/s

### Q10. At critical flow, the minimum specific energy E_min = ?
- A) y_c
- B) 1.25y_c
- C) 1.5y_c
- D) 2y_c

---

## Section C: Hydrology (Q11–Q15)

### Q11. Rational method: C = 0.5, i = 50 mm/hr, A = 100 ha. What is Q?
- A) 5.9 m³/s
- B) 6.9 m³/s
- C) 7.9 m³/s
- D) 8.9 m³/s

### Q12. SCS-CN: CN = 70, P = 100 mm. What is S?
- A) 88.9 mm
- B) 98.9 mm
- C) 108.9 mm
- D) 118.9 mm

### Q13. Muskingum: C₀ = 0.05, C₁ = 0.43, C₂ = ? (sum = 1)
- A) 0.42
- B) 0.48
- C) 0.52
- D) 0.58

### Q14. Gumbel: x̄ = 400 m³/s, σ = 80, K_T = 3.14 for T = 100. What is x₁₀₀?
- A) 551 m³/s
- B) 601 m³/s
- C) 651 m³/s
- D) 701 m³/s

### Q15. Risk of a 50-year flood in 25 years of design life?
- A) 30%
- B) 40%
- C) 50%
- D) 60%

---

## Section D: Groundwater (Q16–Q18)

### Q16. Theis: Q = 0.01 m³/s, T = 0.001 m²/s, W(u) = 6.65. What is s?
- A) 3.29 m
- B) 4.29 m
- C) 5.29 m
- D) 6.29 m

### Q17. Thiem: T = 0.005 m²/s, h₂−h₁ = 4 m, ln(r₂/r₁) = 2.303. What is Q?
- A) 0.0546 m³/s
- B) 0.109 m³/s
- C) 0.218 m³/s
- D) 0.436 m³/s

### Q18. Confined aquifer storativity typical range?
- A) 10⁻²–10⁻¹
- B) 10⁻³–10⁻²
- C) 10⁻⁵–10⁻³
- D) 10⁻⁷–10⁻⁵

---

## Section E: Water Resources & Wastewater (Q19–Q20)

### Q19. Duty D = 800 ha/cumec, base period B = 120 days. What is delta Δ?
- A) 1.10 m
- B) 1.30 m
- C) 1.50 m
- D) 1.70 m

### Q20. BOD₅: L₀ = 300 mg/L, k = 0.23 day⁻¹. What is BOD₅?
- A) 185 mg/L
- B) 195 mg/L
- C) 205 mg/L
- D) 215 mg/L

---

## 📋 Answer Key

| Q | Answer | Q | Answer |
|---|--------|---|--------|
| 1 | B | 11 | B |
| 2 | B | 12 | C |
| 3 | B | 13 | C |
| 4 | B | 14 | C |
| 5 | C | 15 | B |
| 6 | B | 16 | C |
| 7 | C | 17 | A |
| 8 | B | 18 | C |
| 9 | C | 19 | B |
| 10 | C | 20 | C |

---

## 📝 Detailed Solutions

### Q1. Pipe velocity
- A = π(0.15)²/4 = 0.0177 m²
- V = Q/A = 0.03/0.0177 = 1.70 m/s → **B**

### Q2. Pump power
- P = γQH/η = 9810 × 0.1 × 20/0.75 = 19620/0.75 = 26,160 W = 26.2 kW → **B**

### Q3. Reynolds number
- Re = VD/ν = 2 × 0.2/10⁻⁶ = 4×10⁵ → **B**

### Q4. NPSH_A
- 10.33 − 0.24 − 3 − 1 = 6.09 m → **B**

### Q5. Laminar friction factor
- f = 64/Re (Hagen-Poiseuille) → **C**

### Q6. Critical depth
- y_c = (q²/g)^(1/3) = (16/9.81)^(1/3) = (1.631)^(1/3) = 1.18 m → **B**

### Q7. Conjugate depth
- y₂/y₁ = 0.5(√(1+8×36) − 1) = 0.5(√289 − 1) = 0.5(17−1) = 8.0 → **C** (closest to 7.8)

### Q8. Trapezoidal area
- A = (b + zy)y = (4 + 1×2)×2 = 6×2 = 12 m² → **B**

### Q9. Manning velocity
- V = (1/0.013)(1)^(2/3)(0.001)^(1/2) = 76.9 × 1 × 0.0316 = 2.43 m/s → **C**

### Q10. Minimum specific energy
- E_min = 1.5y_c → **C**

### Q11. Rational method
- Q = 0.5 × 50 × 100/360 = 2500/360 = 6.94 m³/s → **B**

### Q12. SCS-CN storage
- S = 25400/70 − 254 = 362.9 − 254 = 108.9 mm → **C**

### Q13. Muskingum C₂
- C₂ = 1 − 0.05 − 0.43 = 0.52 → **C**

### Q14. Gumbel 100-year flood
- x₁₀₀ = 400 + 3.14 × 80 = 400 + 251.2 = 651.2 m³/s → **C**

### Q15. Flood risk
- R = 1 − (1 − 1/50)^25 = 1 − (0.98)^25 = 1 − 0.603 = 0.397 = 40% → **B**

### Q16. Theis drawdown
- s = (0.01/(4π×0.001)) × 6.65 = 0.796 × 6.65 = 5.29 m → **C**

### Q17. Thiem discharge
- Q = 2π × 0.005 × 4/2.303 = 0.1257/2.303 = 0.0546 m³/s → **A**

### Q18. Confined storativity
- 10⁻⁵–10⁻³ → **C**

### Q19. Delta
- Δ = 8.64 × 120/800 = 1036.8/800 = 1.296 m → **B**

### Q20. BOD₅
- BOD₅ = 300 × (1 − e^(−1.15)) = 300 × 0.683 = 205 mg/L → **C**

---

## Scoring Guide

| Score | Readiness |
|-------|-----------|
| 90–100 | Excellent — interview ready |
| 75–89 | Good — review weak topics |
| 60–74 | Fair — targeted revision needed |
| < 60 | Needs work — re-study P0 topics |

## Post-Test Protocol

1. Log every error in [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md)
2. Review [`TRAPS.md`](../TRAPS.md) for trap-related errors
3. Reattempt wrong questions after 24 hours
4. Review [`formulas/hwre-formulas.md`](../formulas/hwre-formulas.md) for formula errors

## Related

- [MASTER_INDEX.md](../MASTER_INDEX.md) · [practice/hwre-practice.md](../practice/hwre-practice.md) · [ERROR_ANALYSIS.md](../ERROR_ANALYSIS.md) · [RAPID_REVISION.md](../RAPID_REVISION.md)
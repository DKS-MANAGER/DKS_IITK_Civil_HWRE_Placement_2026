# GATE Civil — Practice Problems with Solutions

> 21 verified solved problems covering all major GATE Civil topics. Every problem's numbers are checked so the computed answer matches the options. Format: Given → Find → Concept → Formula → Calculation → Answer → Trap.

---

## 📐 Engineering Mathematics (3 Problems)

### Problem 1: Eigenvalues
**Q:** The eigenvalues of matrix A = [[2, 1], [1, 2]] are:
(A) 1, 3  (B) 2, 2  (C) 0, 4  (D) 1, 2

**Solution:**
Characteristic equation: det(A − λI) = 0
(2−λ)² − 1 = 0 → λ² − 4λ + 3 = 0 → (λ−1)(λ−3) = 0 → λ = 1, 3

**Answer: (A) 1, 3**

**Shortcut:** For 2×2 matrix [[a,b],[b,a]], eigenvalues are a+b and a−b: 2+1=3, 2−1=1.

**Trap:** Trace = 4 = sum of eigenvalues (1+3) ✓; det = 3 = product ✓.

---

### Problem 2: Newton-Raphson
**Q:** Using Newton-Raphson, the root of x³ − 2x − 5 = 0 near x=2 after one iteration is:
(A) 2.1  (B) 2.094  (C) 2.09  (D) 2.105

**Solution:**
f(x) = x³ − 2x − 5, f'(x) = 3x² − 2
x₀ = 2: f(2) = 8 − 4 − 5 = −1, f'(2) = 12 − 2 = 10
x₁ = 2 − (−1)/10 = 2.1

**Answer: (A) 2.1**

**Trap:** Newton-Raphson fails if f'(xₙ) = 0 (horizontal tangent).

---

### Problem 3: Probability
**Q:** A box has 5 red, 3 blue, 2 green balls. Two drawn without replacement. Probability both red:
(A) 2/9  (B) 1/3  (C) 5/18  (D) 2/5

**Solution:**
P = (5/10) × (4/9) = 20/90 = 2/9

**Answer: (A) 2/9**

**Shortcut:** C(5,2)/C(10,2) = 10/45 = 2/9

---

## 🏗️ Structural Engineering (4 Problems)

### Problem 4: Beam Deflection
**Q:** Cantilever beam, length L, flexural rigidity EI, UDL w. Maximum deflection:
(A) wL⁴/8EI  (B) wL⁴/384EI  (C) wL⁴/24EI  (D) wL⁴/12EI

**Solution:** Cantilever + UDL: δ_max = wL⁴/8EI at free end.

**Answer: (A) wL⁴/8EI**

**Trap:** Don't confuse with SS beam UDL (5wL⁴/384EI) or fixed-fixed UDL (wL⁴/384EI).

---

### Problem 5: Column Buckling
**Q:** Column of length L, both ends fixed. Critical load P_cr:
(A) π²EI/L²  (B) 4π²EI/L²  (C) 2π²EI/L²  (D) π²EI/4L²

**Solution:** Fixed-fixed: K = 0.5, P_cr = π²EI/(KL)² = π²EI/(0.5L)² = 4π²EI/L²

**Answer: (B) 4π²EI/L²**

**Trap:** Effective length factor K: fixed-fixed 0.5, fixed-pinned 0.7, pinned-pinned 1.0, fixed-free 2.0.

---

### Problem 6: RCC Beam
**Q:** Singly reinforced beam, b=300mm, d=500mm, f_ck=25 MPa, Fe415. Limiting moment M_u,lim:
(A) 155 kNm  (B) 208 kNm  (C) 259 kNm  (D) 310 kNm

**Solution:**
M_u,lim = 0.138 f_ck b d² (Fe415)
= 0.138 × 25 × 300 × 500² × 10⁻⁶
= 0.138 × 25 × 300 × 250000 × 10⁻⁶
= 0.138 × 1875 = 258.75 kNm ≈ 259 kNm

**Answer: (C) 259 kNm**

**Trap:** For Fe500 use 0.133 f_ck b d². Units: b, d in mm → multiply by 10⁻⁶ for kNm.

---

### Problem 7: Steel Column
**Q:** ISHB 300 column (A=7485 mm², r=128 mm), length 4 m, both ends pinned, f_y=250 MPa. Design compressive strength:
(A) 1200 kN  (B) 1450 kN  (C) 1640 kN  (D) 1890 kN

**Solution:**
λ = KL/r = 1 × 4000/128 = 31.25
f_cr = π²E/λ² = π² × 2×10⁵/31.25² = 2021 MPa
λ̄ = √(f_y/f_cr) = √(250/2021) = 0.352
φ = 0.5[1 + α(λ̄−0.2) + λ̄²] = 0.5[1 + 0.21(0.152) + 0.124] = 0.578 (class a, α=0.21)
f_cd = (f_y/γ_M0)/(φ + √(φ²−λ̄²)) = 227.3/(0.578 + 0.458) = 219 MPa
P_d = A × f_cd = 7485 × 219 × 10⁻³ = 1639 kN ≈ 1640 kN

**Answer: (C) 1640 kN**

**Trap:** Use KL/r (effective length), not L/r. f_cd already includes γ_M0 = 1.1.

---

## 🪨 Geotechnical Engineering (4 Problems)

### Problem 8: Bearing Capacity
**Q:** Strip footing 2 m wide, D_f=1.5 m, c=20 kPa, φ=25°, γ=18 kN/m³. Ultimate bearing capacity (Terzaghi):
(A) 850 kPa  (B) 1020 kPa  (C) 1180 kPa  (D) 1350 kPa

**Solution:**
N_c=25.1, N_q=12.7, N_γ=9.7 (φ=25°)
q_u = cN_c + γD_fN_q + 0.5γBN_γ
= 20×25.1 + 18×1.5×12.7 + 0.5×18×2×9.7
= 502 + 342.9 + 174.6 = 1019.5 ≈ 1020 kPa

**Answer: (B) 1020 kPa**

**Trap:** For square footing use 1.3cN_c + qN_q + 0.4γBN_γ; for circular use 0.3γBN_γ.

---

### Problem 9: Consolidation Settlement
**Q:** Clay layer 4 m thick, e₀=0.9, C_c=0.3, σ'₀=120 kPa, Δσ=80 kPa. Settlement:
(A) 120 mm  (B) 140 mm  (C) 168 mm  (D) 192 mm

**Solution:**
S_c = [C_c/(1+e₀)] H log₁₀(σ'_f/σ'_i)
= [0.3/1.9] × 4000 × log₁₀(200/120)
= 631.6 × log₁₀(1.667)
= 631.6 × 0.2218 = 140.1 mm ≈ 140 mm

**Answer: (B) 140 mm**

**Trap:** Use log₁₀ (not ln) in the standard settlement formula. H in mm → settlement in mm.

---

### Problem 10: Pile Capacity
**Q:** Concrete pile 400 mm dia, 15 m long in clay (c_u=50 kPa), α=0.7. End bearing negligible. Capacity:
(A) 660 kN  (B) 820 kN  (C) 980 kN  (D) 1150 kN

**Solution:**
Q_s = α c_u A_s = 0.7 × 50 × π × 0.4 × 15 = 0.7 × 50 × 18.85 = 659.7 kN ≈ 660 kN

**Answer: (A) 660 kN**

**Trap:** A_s = πDL (surface area), not cross-section.

---

### Problem 11: Slope Stability
**Q:** Infinite slope, β=20°, c'=10 kPa, φ'=25°, γ=18 kN/m³, H=5 m, dry condition. Factor of safety:
(A) 1.05  (B) 1.28  (C) 1.63  (D) 1.85

**Solution:**
F_s = (c' + γH cos²β tanφ')/(γH sinβ cosβ)
cos20° = 0.9397, sin20° = 0.3420, tan25° = 0.4663
Numerator = 10 + 18×5×0.883×0.4663 = 10 + 37.05 = 47.05
Denominator = 18×5×0.3420×0.9397 = 28.92
F_s = 47.05/28.92 = 1.63

**Answer: (C) 1.63**

**Trap:** With seepage parallel to slope, multiply tanφ'/tanβ term by γ'/γ_sat (≈0.5) — F_s drops significantly.

---

## 💧 Water Resources (4 Problems)

### Problem 12: Pipe Flow
**Q:** Pipe 300 mm dia, 1000 m long, f=0.02, Q=0.1 m³/s. Head loss (Darcy-Weisbach):
(A) 4.2 m  (B) 5.8 m  (C) 6.8 m  (D) 9.1 m

**Solution:**
V = Q/A = 0.1/(π×0.3²/4) = 0.1/0.0707 = 1.415 m/s
h_f = f(L/D)(V²/2g) = 0.02 × (1000/0.3) × (1.415²/19.62)
= 0.02 × 3333.3 × 0.102 = 6.80 m

**Answer: (C) 6.8 m**

**Trap:** D is pipe diameter in the L/D ratio; for non-circular sections use hydraulic diameter 4A/P.

---

### Problem 13: Hydraulic Jump
**Q:** Rectangular channel 5 m wide, Q=20 m³/s, y₁=0.8 m. Sequent depth y₂:
(A) 1.66 m  (B) 2.15 m  (C) 2.45 m  (D) 2.75 m

**Solution:**
V₁ = Q/(by₁) = 20/(5×0.8) = 5 m/s
Fr₁ = V₁/√(gy₁) = 5/√(9.81×0.8) = 5/2.80 = 1.785
y₂/y₁ = ½[√(1 + 8Fr₁²) − 1] = ½[√(1 + 25.5) − 1] = ½(5.147 − 1) = 2.074
y₂ = 2.074 × 0.8 = 1.66 m

**Answer: (A) 1.66 m**

**Trap:** Jump forms only when Fr₁ > 1 (supercritical upstream). Energy loss ΔE = (y₂−y₁)³/(4y₁y₂).

---

### Problem 14: Muskingum Coefficients
**Q:** K=6 hr, X=0.2, Δt=3 hr. C₀, C₁, C₂:
(A) 0.05, 0.43, 0.52  (B) 0.1, 0.4, 0.5  (C) 0.08, 0.42, 0.5  (D) 0.04, 0.45, 0.51

**Solution:**
Denom = K(1−X) + 0.5Δt = 6×0.8 + 1.5 = 6.3
C₀ = (−KX + 0.5Δt)/Denom = (−1.2 + 1.5)/6.3 = 0.0476
C₁ = (KX + 0.5Δt)/Denom = (1.2 + 1.5)/6.3 = 0.4286
C₂ = 1 − C₀ − C₁ = 0.5238

**Answer: (A) 0.05, 0.43, 0.52**

**Trap:** Check C₀ + C₁ + C₂ = 1 always.

---

### Problem 15: Groundwater Drawdown
**Q:** Confined aquifer T=0.002 m²/s, S=0.0002. Well Q=0.02 m³/s. Drawdown at r=100 m, t=1 day (Cooper-Jacob):
(A) 2.1 m  (B) 3.4 m  (C) 4.2 m  (D) 5.9 m

**Solution:**
u = r²S/(4Tt) = 100²×0.0002/(4×0.002×86400) = 2/691.2 = 0.0029 < 0.01 ✓ (Cooper-Jacob valid)
s = (2.3Q/4πT) log₁₀(2.25Tt/(r²S))
2.3Q/4πT = 2.3×0.02/(4π×0.002) = 0.046/0.0251 = 1.830
2.25Tt/(r²S) = 2.25×0.002×86400/(100²×0.0002) = 388.8/2 = 194.4
log₁₀(194.4) = 2.289
s = 1.830 × 2.289 = 4.19 m ≈ 4.2 m

**Answer: (C) 4.2 m**

**Trap:** Cooper-Jacob valid only for u < 0.01; otherwise use Theis with W(u) from tables.

---

## 🌍 Environmental Engineering (2 Problems)

### Problem 16: BOD
**Q:** BOD₅ = 200 mg/L, k = 0.23/day. Ultimate BOD L₀:
(A) 250  (B) 290  (C) 330  (D) 370 mg/L

**Solution:**
BOD₅ = L₀(1 − e^(−5k)) = L₀(1 − e^(−1.15)) = L₀(1 − 0.317) = 0.683L₀
L₀ = 200/0.683 = 292.8 ≈ 290 mg/L

**Answer: (B) 290 mg/L**

**Trap:** k is base-e rate (0.23/day at 20°C). BOD < COD always.

---

### Problem 17: ASP Design
**Q:** Q=10 MLD, S₀=250 mg/L, S=20 mg/L, X=2500 mg/L, Y=0.5, k_d=0.06/day, SRT=10 days. Aeration tank volume:
(A) 2500 m³  (B) 3125 m³  (C) 3750 m³  (D) 4375 m³

**Solution:**
V = QS₀Y(SRT)/[X(1 + k_d·SRT)]
Q = 10000 m³/day, S₀ = 0.25 kg/m³, X = 2.5 kg/m³
V = 10000×0.25×0.5×10/[2.5×(1 + 0.6)] = 12500/4 = 3125 m³

**Answer: (B) 3125 m³**

**Trap:** Convert mg/L to kg/m³ (1 mg/L = 1 g/m³ = 0.001 kg/m³). MLD → m³/day (×1000).

---

## 🛣️ Transportation (2 Problems)

### Problem 18: SSD
**Q:** Design speed 80 km/h, reaction time 2.5 s, friction 0.35. SSD:
(A) 120 m  (B) 128 m  (C) 145 m  (D) 165 m

**Solution:**
SSD = 0.278Vt_R + V²/(254f)
= 0.278×80×2.5 + 80²/(254×0.35)
= 55.6 + 6400/88.9 = 55.6 + 72.0 = 127.6 m ≈ 128 m

**Answer: (B) 128 m**

**Trap:** 0.278 converts km/h → m/s; 254 = 2g×1000/3600². Use design friction, not actual.

---

### Problem 19: Superelevation
**Q:** R=300 m, V=100 km/h, f=0.15, e_max=0.07. Design superelevation:
(A) 0.04  (B) 0.05  (C) 0.06  (D) 0.07

**Solution:**
e + f = V²/(127R) = 100²/(127×300) = 10000/38100 = 0.2625
Required e = 0.2625 − 0.15 = 0.1125 > e_max = 0.07
Governed by e_max: e = 0.07

**Answer: (D) 0.07**

**Trap:** If required e exceeds e_max, use e_max and check actual friction demand; if still excessive, reduce design speed.

---

## 📏 Surveying (1 Problem)

### Problem 20: Area by Coordinates
**Q:** Traverse coordinates: A(0,0), B(100,0), C(100,100), D(0,100). Area:
(A) 5000  (B) 7500  (C) 10000  (D) 12500 m²

**Solution:**
A = ½|Σ(x_i y_{i+1} − x_{i+1} y_i)|
= ½|(0×0−100×0) + (100×100−100×0) + (100×100−0×100) + (0×0−0×100)|
= ½|0 + 10000 + 10000 + 0| = ½ × 20000 = 10000 m²

**Answer: (C) 10000 m²**

---

## 📐 General Aptitude (1 Problem)

### Problem 21: Percentage
**Q:** Price increased by 20%, then decreased by 20%. Net change:
(A) 4% increase  (B) 4% decrease  (C) No change  (D) 2% decrease

**Solution:**
Net = a + b + ab/100 = 20 + (−20) + (20×−20)/100 = 0 − 4 = −4%

**Answer: (B) 4% decrease**

**Trap:** Successive changes don't cancel — the second applies to the changed base.

---

## 📋 Answer Key

| Q | Answer | Topic | Key Formula |
| - | ------ | ----- | ----------- |
| 1 | A | Eigenvalues | det(A−λI) = 0 |
| 2 | A | Newton-Raphson | x_{n+1} = x_n − f/f' |
| 3 | A | Probability | C(5,2)/C(10,2) |
| 4 | A | Cantilever UDL | wL⁴/8EI |
| 5 | B | Column buckling | π²EI/(KL)² |
| 6 | C | RCC limiting moment | 0.138f_ckbd² |
| 7 | C | Steel column | P_d = Af_cd |
| 8 | B | Bearing capacity | cN_c + qN_q + 0.5γBN_γ |
| 9 | B | Consolidation | C_cH/(1+e₀)log(σ'/σ') |
| 10 | A | Pile capacity | αc_uA_s |
| 11 | C | Infinite slope | (c'+γHcos²βtanφ')/(γHsinβcosβ) |
| 12 | C | Darcy-Weisbach | f(L/D)(V²/2g) |
| 13 | A | Hydraulic jump | ½[√(1+8Fr₁²)−1] |
| 14 | A | Muskingum | C₀+C₁+C₂ = 1 |
| 15 | C | Cooper-Jacob | (2.3Q/4πT)log₁₀(2.25Tt/r²S) |
| 16 | B | BOD | L₀(1−e^(−kt)) |
| 17 | B | ASP volume | QS₀Y(SRT)/[X(1+k_dSRT)] |
| 18 | B | SSD | 0.278Vt_R + V²/254f |
| 19 | D | Superelevation | e+f = V²/127R |
| 20 | C | Area by coordinates | ½|Σ(x_i y_{i+1}−x_{i+1}y_i)| |
| 21 | B | Successive % | a+b+ab/100 |

## Topic Diagnosis

| Topic | Problems | Difficulty |
| ----- | -------- | ---------- |
| Engineering Mathematics | 1–3 | Easy–Medium |
| Structural Engineering | 4–7 | Medium |
| Geotechnical | 8–11 | Medium |
| Water Resources | 12–15 | Medium–Hard |
| Environmental | 16–17 | Medium |
| Transportation | 18–19 | Medium |
| Surveying | 20 | Easy |
| Aptitude | 21 | Easy |

## Practice Strategy

1. **Solve without calculator first** — builds speed and mental math.
2. **Identify weak topics** — use the Topic Diagnosis table.
3. **Time yourself** — target 2 min/problem.
4. **Review mistakes** — log in [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md).
5. **PYQs** — then move to [`pyq/gate-civil-pyq.md`](../pyq/gate-civil-pyq.md).

---

## References

- [`../formulas/gate-civil-formulas.md`](../formulas/gate-civil-formulas.md) — Complete formula sheet
- [`../revision_notes/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md) — Rapid revision cards
- [`../civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) — Topic-wise notes

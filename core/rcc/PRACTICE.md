# RCC Design — Practice Problems with Solutions

> **Placement Priority:** P0 — Asked in EVERY core civil engineering interview
> **Canonical Study:** [`rcc-design.md`](rcc-design.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap
> **Code:** IS 456:2000 (Limit State Method)

---

## Problem 1: Singly Reinforced Beam Design

**Given:** Beam with $M_u = 150$ kN·m, $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $b = 250$ mm.

**Find:** Required effective depth $d$ and tension steel $A_{st}$.

**Method:** $M_{u,lim} = 0.138 f_{ck} b d^2$ (Fe415 balanced section).

**Calculation:**
- $M_{u,lim} = 0.138 \times 25 \times 250 \times d^2 = 862.5 d^2$ N·mm
- Required $d = \sqrt{150 \times 10^6 / 862.5} = \sqrt{173,913} = 417$ mm → use $d = 450$ mm
- Since $M_u < M_{u,lim}$, section is under-reinforced
- $A_{st} = \frac{M_u}{0.87 f_y (d - 0.42 x_u)}$
- Trial $x_u = 0.48d = 216$ mm: $A_{st} = \frac{150 \times 10^6}{0.87 \times 415 \times (450 - 0.42 \times 216)} = \frac{150 \times 10^6}{361 \times 359.3} = 1153$ mm²
- Check: $x_u = \frac{0.87 \times 415 \times 1153}{0.36 \times 25 \times 250} = \frac{416,000}{2250} = 185$ mm < $x_{u,max} = 216$ mm ✓

**Answer:** $d = 450$ mm, $A_{st} = 1153$ mm² → **4 bars of 20 mm** ($A_{st} = 1256$ mm²)

**Trap:** Verify $x_u < x_{u,max}$ — otherwise the section is over-reinforced and unsafe.

---

## Problem 2: Doubly Reinforced Section

**Given:** Beam with $M_u = 300$ kN·m, $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $b = 250$ mm, $d = 450$ mm, $d' = 50$ mm.

**Find:** Compression steel $A_{sc}$ and additional tension steel $A_{st2}$.

**Method:** $M_u = M_{u,lim} + M_{u2}$; $A_{sc} = \frac{M_u - M_{u,lim}}{(f_{sc} - f_{cc})(d - d')}$.

**Calculation:**
- $M_{u,lim} = 0.138 \times 25 \times 250 \times 450^2 = 174.7$ kN·m
- $M_{u2} = 300 - 174.7 = 125.3$ kN·m
- $A_{sc} = \frac{125.3 \times 10^6}{(353 - 0.446 \times 25)(450 - 50)} = \frac{125.3 \times 10^6}{(353 - 11.2) \times 400} = \frac{125.3 \times 10^6}{136,720} = 916$ mm²
- $A_{st2} = \frac{125.3 \times 10^6}{0.87 \times 415 \times 400} = \frac{125.3 \times 10^6}{144,420} = 868$ mm²
- $A_{st,lim} = \frac{174.7 \times 10^6}{0.87 \times 415 \times (450 - 0.42 \times 216)} = 1343$ mm²
- $A_{st} = 1343 + 868 = 2211$ mm²

**Answer:** $A_{sc} = 916$ mm² (e.g., 4-18mm = 1017 mm²), $A_{st} = 2211$ mm² (e.g., 4-20mm + 2-16mm = 1658... use 5-25mm = 2454 mm²)

**Trap:** Compression steel requires stirrups to prevent buckling of the compression bars.

---

## Problem 3: Shear Design

**Given:** Beam with $V_u = 200$ kN, $b = 250$ mm, $d = 450$ mm, $f_{ck} = 25$ MPa, $p_t = 1.1\%$, $f_y = 415$ MPa.

**Find:** Shear reinforcement spacing.

**Method:** $\tau_v = V_u/bd$; compare with $\tau_c$ (IS 456 Table 19) and $\tau_{c,max}$.

**Calculation:**
- $\tau_v = \frac{200 \times 10^3}{250 \times 450} = 1.78$ N/mm²
- From Table 19 (M25, $p_t = 1.1\%$): $\tau_c \approx 0.62$ N/mm²
- $\tau_{c,max}$ (M25) = 3.1 N/mm². $\tau_v < \tau_{c,max}$ ✓
- Since $\tau_v > \tau_c$: $V_{us} = (\tau_v - \tau_c)bd = (1.78 - 0.62) \times 250 \times 450 = 130,500$ N = 130.5 kN
- 2-legged 8mm stirrups: $A_{sv} = 2 \times 50.3 = 100.6$ mm²
- $s_v = \frac{0.87 f_y A_{sv} d}{V_{us}} = \frac{0.87 \times 415 \times 100.6 \times 450}{130,500} = 125$ mm
- Check: $s_v \le \min(0.75d = 337.5, 300) = 300$ mm ✓

**Answer:** Provide **8mm 2-legged stirrups @ 125 mm c/c**

**Trap:** If $\tau_v > \tau_{c,max}$, redesign the section — shear reinforcement alone cannot fix it.

---

## Problem 4: Development Length

**Given:** Fe415, 20 mm bar in M25 concrete. $\tau_{bd} = 1.4$ N/mm² (plain bar).

**Find:** Development length $L_d$.

**Method:** $L_d = \frac{0.87 f_y \phi}{4 \tau_{bd}}$.

**Calculation:**
- $L_d = \frac{0.87 \times 415 \times 20}{4 \times 1.4} = \frac{7221}{5.6} = 1289$ mm (plain)
- Deformed bar: $\tau_{bd} = 1.6 \times 1.4 = 2.24$ N/mm²
- $L_d = \frac{7221}{4 \times 2.24} = 806$ mm

**Answer:** $L_d \approx 810$ mm (deformed bar)

**Trap:** Deformed bars get a **60% increase** in $\tau_{bd}$, reducing $L_d$ significantly.

---

## Problem 5: Short Column Design

**Given:** Column with $P_u = 1500$ kN, $f_{ck} = 25$ MPa, $f_y = 415$ MPa, $D = 400$ mm.

**Find:** Longitudinal steel $A_{sc}$.

**Method:** $P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$.

**Calculation:**
- Try $A_{sc} = 1\%$ of $A_g$: $A_{sc} = 0.01 \times 400^2 = 1600$ mm²
- $A_c = 160,000 - 1600 = 158,400$ mm²
- $P_u = 0.4 \times 25 \times 158,400 + 0.67 \times 415 \times 1600 = 1,584,000 + 444,880 = 2,028,880$ N = 2029 kN > 1500 ✓
- Try 0.5%: $A_{sc} = 800$ mm²
- $P_u = 0.4 \times 25 \times 159,200 + 0.67 \times 415 \times 800 = 1,592,000 + 222,440 = 1,814,440$ N = 1814 kN > 1500 ✓

**Answer:** Use **8 bars of 12 mm** ($A_{sc} = 904$ mm²)

**Trap:** Minimum longitudinal steel is 0.8% of gross area — don't go below it.

---

## Problem 6: One-Way Slab Design

**Given:** Simply supported slab, span 3 m, $f_{ck} = 25$ MPa, $f_y = 415$ MPa, live load 3 kN/m², floor finish 1 kN/m².

**Find:** Slab thickness and main steel.

**Method:** Span/depth = 20 (SS); $M_u = 1.5 \times w l^2/8$.

**Calculation:**
- $d \ge l/20 = 3000/20 = 150$ mm → use $D = 175$ mm, $d = 150$ mm (cover 15 + bar/2)
- $w = 1.5 \times (0.175 \times 25 + 1 + 3) = 1.5 \times (4.375 + 4) = 12.56$ kN/m
- $M_u = 12.56 \times 9/8 = 14.13$ kN·m/m
- $A_{st} = \frac{M_u}{0.87 f_y (d - 0.42 x_u)}$; trial $x_u = 0.48d = 72$ mm
- $A_{st} = \frac{14.13 \times 10^6}{0.87 \times 415 \times (150 - 0.42 \times 72)} = \frac{14.13 \times 10^6}{361 \times 119.8} = 327$ mm²/m
- Check min: $0.12\% \times bD = 0.0012 \times 1000 \times 175 = 210$ mm²/m < 327 ✓

**Answer:** $D = 175$ mm, main steel **8mm @ 150 mm c/c** ($A_{st} = 335$ mm²/m)

**Trap:** Slabs are not designed for shear — check deflection (span/depth) instead.

---

## Problem 7: Two-Way Slab

**Given:** Two-way slab, $l_x = 4$ m, $l_y = 5$ m, $f_{ck} = 25$ MPa, $f_y = 415$ MPa.

**Find:** Whether one-way or two-way; design moment coefficients.

**Method:** Aspect ratio $l_y/l_x$; IS 456 coefficients.

**Calculation:**
- $l_y/l_x = 5/4 = 1.25 \le 2$ → **two-way slab**
- Span/depth (SS, HYSD) = 28: $d \ge 4000/28 = 143$ mm → use $D = 160$ mm, $d = 140$ mm
- Design moments per IS 456 Table 26 (using coefficients $\alpha_x$, $\alpha_y$)

**Answer:** Two-way slab, $D = 160$ mm

**Trap:** Two-way slabs have higher span/depth ratios (28/35) because load is shared in two directions.

---

## Problem 8: T-Beam Effective Flange Width

**Given:** T-beam, $l_o = 6$ m, $b_w = 300$ mm, $D_f = 120$ mm.

**Find:** Effective flange width $b_f$.

**Method:** $b_f = \frac{l_o}{6} + b_w + 6D_f$.

**Calculation:**
- $b_f = \frac{6000}{6} + 300 + 6 \times 120 = 1000 + 300 + 720 = 2020$ mm

**Answer:** $b_f = 2020$ mm

**Trap:** For an L-beam, use $b_f = \frac{l_o}{12} + b_w + 3D_f$.

---

## Problem 9: Footing Design — Punching Shear

**Given:** Isolated footing under a 400 mm × 400 mm column, $P_u = 1000$ kN, $f_{ck} = 25$ MPa, footing size 2.5 m × 2.5 m, $d = 450$ mm.

**Find:** Punching shear stress.

**Method:** $\tau_v = \frac{V_u}{b_0 d}$ where $b_0$ = perimeter at $d/2$ from column face.

**Calculation:**
- $b_0 = 4 \times (400 + 450) = 4 \times 850 = 3400$ mm
- $V_u = P_u - \text{soil pressure} \times (0.85)^2$; soil pressure $= 1000/6.25 = 160$ kN/m²
- $V_u = 1000 - 160 \times 0.7225 = 1000 - 115.6 = 884.4$ kN
- $\tau_v = \frac{884.4 \times 10^3}{3400 \times 450} = 0.578$ N/mm²
- $\tau_{c,max}$ (M25) = 1.25 N/mm² (punching). $0.578 < 1.25$ ✓

**Answer:** Punching shear OK at $d = 450$ mm

**Trap:** Punching shear perimeter is at **$d/2$** from the column face, not at the face.

---

## Problem 10: Prestress Loss — Friction

**Given:** Post-tensioned beam, $P_0 = 1000$ kN, $\mu = 0.3$, $\alpha = 0.2$ rad, $k = 0.002$/m, $x = 20$ m.

**Find:** Prestress at the far end.

**Method:** $P_x = P_0 e^{-(\mu\alpha + kx)} \approx P_0(1 - \mu\alpha - kx)$.

**Calculation:**
- $\mu\alpha + kx = 0.3 \times 0.2 + 0.002 \times 20 = 0.06 + 0.04 = 0.10$
- $P_x = 1000 \times e^{-0.10} = 1000 \times 0.9048 = 904.8$ kN

**Answer:** $P_x = 904.8$ kN (≈ 9.5% friction loss)

**Trap:** Friction loss applies only to **post-tensioning**, not pre-tensioning.

---

## Problem 11: Load Combination

**Given:** Beam with $DL = 40$ kN/m, $LL = 25$ kN/m, $WL = 20$ kN/m.

**Find:** Design (factored) load.

**Method:** IS 456 Table 18 load combinations.

**Calculation:**
- DL + LL: $1.5(40) + 1.5(25) = 60 + 37.5 = 97.5$ kN/m
- DL + WL: $1.5(40) + 1.5(20) = 60 + 30 = 90$ kN/m
- DL + LL + WL: $1.2(40) + 1.2(25) + 1.2(20) = 48 + 30 + 24 = 102$ kN/m

**Answer:** Governs **DL + LL + WL = 102 kN/m**

**Trap:** Always check all combinations — the governing one is the maximum.

---

## Problem 12: Minimum Eccentricity

**Given:** Column, $l = 3$ m, $D = 400$ mm.

**Find:** Minimum eccentricity.

**Method:** $e_{min} = \frac{l}{500} + \frac{D}{30} \ge 20$ mm.

**Calculation:**
- $e_{min} = \frac{3000}{500} + \frac{400}{30} = 6 + 13.33 = 19.33$ mm
- Since $19.33 < 20$ mm → use $e_{min} = 20$ mm

**Answer:** $e_{min} = 20$ mm

**Trap:** The minimum is 20 mm — the formula result is rounded up.

---

## Problem 13: Continuous Beam Coefficients

**Given:** Continuous beam with 3 equal spans, UDL $w = 30$ kN/m, span $L = 5$ m.

**Find:** Design moment at the support next to the end support.

**Method:** IS 456 coefficient $-1/10$ for support next to end support.

**Calculation:**
- $M = -\frac{wL^2}{10} = -\frac{30 \times 25}{10} = -75$ kN·m

**Answer:** $M = -75$ kN·m (hogging)

**Trap:** Coefficients apply only for approximately equal spans and uniform loading.

---

## Problem 14: Concrete Modulus of Elasticity

**Given:** M25 concrete.

**Find:** Short-term modulus of elasticity.

**Method:** $E_c = 5000\sqrt{f_{ck}}$.

**Calculation:**
- $E_c = 5000\sqrt{25} = 5000 \times 5 = 25,000$ N/mm²

**Answer:** $E_c = 25,000$ N/mm²

**Trap:** This is the short-term modulus; long-term (with creep) is $E_{ce} = E_c/(1+\theta)$.

---

## Problem 15: Flexural Strength (Modulus of Rupture)

**Given:** M30 concrete.

**Find:** Modulus of rupture.

**Method:** $f_{cr} = 0.7\sqrt{f_{ck}}$.

**Calculation:**
- $f_{cr} = 0.7\sqrt{30} = 0.7 \times 5.477 = 3.83$ N/mm²

**Answer:** $f_{cr} = 3.83$ N/mm²

**Trap:** Modulus of rupture is used for **cracking checks**, not strength design.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | $d = 450$ mm, $A_{st} = 1153$ mm² (4-20mm) |
| 2 | $A_{sc} = 916$ mm², $A_{st} = 2211$ mm² |
| 3 | 8mm 2-legged stirrups @ 125 mm c/c |
| 4 | $L_d = 806$ mm (deformed) |
| 5 | 8-12mm bars ($A_{sc} = 904$ mm²) |
| 6 | $D = 175$ mm, 8mm @ 150 mm c/c |
| 7 | Two-way slab, $D = 160$ mm |
| 8 | $b_f = 2020$ mm |
| 9 | $\tau_v = 0.578$ N/mm² < 1.25 ✓ |
| 10 | $P_x = 904.8$ kN |
| 11 | 102 kN/m (DL+LL+WL) |
| 12 | $e_{min} = 20$ mm |
| 13 | $M = -75$ kN·m |
| 14 | $E_c = 25,000$ N/mm² |
| 15 | $f_{cr} = 3.83$ N/mm² |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Flexural design | 1, 2 | Can you design singly and doubly reinforced beams? |
| Shear design | 3 | Can you compute stirrup spacing? |
| Bond & anchorage | 4 | Can you compute $L_d$ and apply modifications? |
| Column design | 5, 12 | Can you design short columns and check eccentricity? |
| Slab design | 6, 7, 13 | Can you classify and design one-way/two-way slabs? |
| Flanged beams | 8 | Can you compute effective flange width? |
| Footing design | 9 | Can you check punching shear? |
| Prestressed concrete | 10 | Can you compute friction losses? |
| Load combinations | 11 | Can you apply IS 456 Table 18? |
| Material properties | 14, 15 | Can you recall $E_c$ and $f_{cr}$? |

---

## Practice Strategy

1. **Solve Problems 1–5** (beam design + shear + column) — the most frequently tested.
2. **Solve Problems 6–9** (slabs + footings) — critical for design roles.
3. **Solve Problems 10–15** (prestress + code provisions) — advanced, for PSU/consulting.
4. Re-attempt any problem you couldn't solve in < 5 minutes.
5. Then take the [`TEST.md`](TEST.md) to verify mastery.
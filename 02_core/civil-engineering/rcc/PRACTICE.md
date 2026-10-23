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

## Problem 2: Doubly Reinforced Beam Design

**Given:** Beam cross-section $b = 250$ mm, overall depth $D = 500$ mm, effective depth $d = 450$ mm, effective cover to compression steel $d' = 50$ mm ($d'/d = 50/450 = 0.111$). Factored bending moment $M_u = 300$ kN·m. Concrete grade M25 ($f_{ck} = 25$ MPa), steel grade Fe415 ($f_y = 415$ MPa).

**Find:** Required compression reinforcement $A_{sc}$ and total tension reinforcement $A_{st}$, and choose a feasible standard bar arrangement.

**Method:** IS 456:2000 Annex G / SP 16 design procedure for doubly reinforced sections:
$$M_u = M_{u,\lim} + M_{u2}$$
$$A_{sc} = \frac{M_{u2}}{(f_{sc} - f_{cc})(d - d')}, \quad A_{st} = A_{st1} + A_{st2}$$

**Calculation:**
1. **Limiting Moment of Resistance ($M_{u,\lim}$):**
   - For Fe415, $x_{u,\max}/d = 0.48 \implies x_{u,\max} = 0.48 \times 450 = 216$ mm
   - $M_{u,\lim} = 0.138 f_{ck} b d^2 = 0.138 \times 25 \times 250 \times 450^2 = 174.66 \times 10^6\text{ N}\cdot\text{mm} = 174.66$ kN·m
   - Since $M_u (300\text{ kN}\cdot\text{m}) > M_{u,\lim}$, a doubly reinforced section is required.
   - Additional moment to be resisted: $M_{u2} = M_u - M_{u,\lim} = 300.0 - 174.66 = 125.34$ kN·m

2. **Compression Steel Stress ($f_{sc}$):**
   - Strain at level of compression steel:
     $$\epsilon_{sc} = 0.0035 \left(1 - \frac{d'}{x_{u,\max}}\right) = 0.0035 \left(1 - \frac{50}{216}\right) = 0.00269$$
   - From IS 456 Table A / SP 16 Table F for Fe415 ($d'/d = 0.111$):
     By linear interpolation between $d'/d = 0.10$ ($f_{sc} = 353$ N/mm²) and $d'/d = 0.15$ ($f_{sc} = 342$ N/mm²):
     $$f_{sc} \approx 353 - \left(\frac{353 - 342}{0.05}\right)(0.111 - 0.10) \approx 350.6\text{ N/mm}^2$$
   - Concrete compressive stress at compression steel level: $f_{cc} = 0.446 f_{ck} = 0.446 \times 25 = 11.15$ N/mm²
   - Net stress in compression steel: $f_{sc} - f_{cc} = 350.6 - 11.15 = 339.45$ N/mm²

3. **Steel Area Calculation:**
   - Compression steel:
     $$A_{sc} = \frac{M_{u2}}{(f_{sc} - f_{cc})(d - d')} = \frac{125.34 \times 10^6}{339.45 \times (450 - 50)} = \frac{125.34 \times 10^6}{135,780} = \mathbf{923\text{ mm}^2}$$
   - Limiting tension steel:
     $$A_{st1} = \frac{M_{u,\lim}}{0.87 f_y (d - 0.42 x_{u,\max})} = \frac{174.66 \times 10^6}{0.87 \times 415 \times (450 - 0.42 \times 216)} = \frac{174.66 \times 10^6}{361.05 \times 359.28} = 1346\text{ mm}^2$$
   - Additional tension steel:
     $$A_{st2} = \frac{M_{u2}}{0.87 f_y (d - d')} = \frac{125.34 \times 10^6}{361.05 \times 400} = 868\text{ mm}^2$$
   - Total tension steel: $A_{st} = A_{st1} + A_{st2} = 1346 + 868 = \mathbf{2214\text{ mm}^2}$

4. **Standard Bar Selection & Detailing:**
   - **Compression Steel ($A_{sc} = 923\text{ mm}^2$):** Provide **3 bars of 20 mm dia** ($A_{sc,\text{prov}} = 3 \times 314.16 = \mathbf{942.5\text{ mm}^2} > 923\text{ mm}^2$). Clear side cover = 30 mm, clear bar spacing = $(250 - 2\times30 - 3\times20)/2 = 65\text{ mm} > 20\text{ mm}$ ✓.
   - **Tension Steel ($A_{st} = 2214\text{ mm}^2$):** Provide **4 bars of 25 mm + 1 bar of 20 mm** ($A_{st,\text{prov}} = 4 \times 490.87 + 314.16 = \mathbf{2277.6\text{ mm}^2} > 2214\text{ mm}^2$), placed in two layers (bottom layer: 3-25mm; upper layer: 1-25mm + 1-20mm with 25 mm spacer bar) to satisfy minimum horizontal bar clearance.

**Answer:** $A_{sc} = 923$ mm² $\to$ **3 bars of 20 mm** ($942.5$ mm²); $A_{st} = 2214$ mm² $\to$ **4 bars of 25 mm + 1 bar of 20 mm** ($2277.6$ mm² in two layers).

**Trap:** Non-standard bar diameters (like 18 mm) do not exist in IS 1786. Always verify the strain compatibility for $f_{sc}$ (do not assume $f_{sc} = 0.87f_y$) and verify that compression bars are restrained by transverse ties (IS 456 Cl. 26.5.3.2) to prevent buckling.

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

## Problem 5: Short Column Design (Minimum Steel Enforcement)

**Given:** Short axially loaded column with factored axial load $P_u = 1500$ kN, cross-section $400 \times 400$ mm ($A_g = 160,000$ mm²). Concrete grade M25 ($f_{ck} = 25$ MPa), steel grade Fe415 ($f_y = 415$ MPa). Minimum eccentricity $e_{\min} \le 0.05D$.

**Find:** Required longitudinal steel area $A_{sc}$ and tie detailing complying with IS 456:2000.

**Method:** 
IS 456:2000 Cl. 39.3 design equation:
$$P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$$
Enforce Cl. 26.5.3.1: minimum longitudinal reinforcement is **$0.8\%$ of gross area** ($A_g$).

**Calculation:**
1. **Minimum Reinforcement Check:**
   $$A_{sc,\min} = 0.008 \times A_g = 0.008 \times 160,000 = \mathbf{1280\text{ mm}^2}$$
   *(Note: Choosing $8\phi12\text{ mm} = 904\text{ mm}^2$ gives only $0.565\% < 0.8\%$, violating IS 456!).*

2. **Theoretical Strength with Minimum Steel ($A_{sc} = 1280\text{ mm}^2$):**
   - $A_c = 160,000 - 1280 = 158,720$ mm²
   - $P_u = 0.4(25)(158,720) + 0.67(415)(1280) = 1,587,200 + 355,840 = 1,943,040\text{ N} = 1943\text{ kN} > 1500\text{ kN}$ ✓ (adequate).

3. **Standard Bar Selection:**
   - To maintain symmetry in a square column ($400 \times 400$ mm), use 8 longitudinal bars:
     Provide **8 bars of 16 mm dia** ($A_{sc,\text{prov}} = 8 \times 201.06 = \mathbf{1609\text{ mm}^2} = 1.01\% \ge 0.8\%$).
   - Check ultimate axial capacity:
     $$P_{u,\text{cap}} = 0.4(25)(160,000 - 1609) + 0.67(415)(1609) = 1,583,910 + 447,382 = 2031\text{ kN} > 1500\text{ kN}$$ ✓

4. **Transverse Ties (IS 456 Cl. 26.5.3.2):**
   - Tie diameter $\phi_t \ge \max(\phi_L/4 = 16/4 = 4\text{ mm}, 6\text{ mm}) \implies \mathbf{8\text{ mm}}$.
   - Tie pitch $\le \min(\text{least lateral dim} = 400\text{ mm}, 16\phi_L = 16 \times 16 = 256\text{ mm}, 300\text{ mm}) \implies \mathbf{250\text{ mm c/c}}$.

**Answer:** Provide **8 bars of 16 mm** ($A_{sc} = 1609$ mm², $p = 1.01\%$) with **8 mm lateral ties @ 250 mm c/c**.

**Trap:** Never select longitudinal reinforcement below 0.8% of $A_g$, even if axial strength equations appear satisfied with less steel. Minimum steel is mandatory to resist accidental eccentricities, temperature/shrinkage stresses, and concrete creep.

---

## Problem 6: One-Way Slab Design & Shear Verification

**Given:** Simply supported one-way slab, clear span $l = 3.0$ m, bearing width $= 200$ mm. Imposed live load $= 3.0$ kN/m², floor finish $= 1.0$ kN/m². Concrete M25, steel Fe415.

**Find:** Total thickness $D$, effective depth $d$, main and distribution reinforcement, and check one-way shear.

**Method:** 
Basic span/depth ratio = 20 (SS beam/slab). Factored load $w_u = 1.5(DL + LL)$. One-way shear check at distance $d$ from support face per IS 456 Cl. 40.

**Calculation:**
1. **Depth from Deflection Control:**
   - Effective depth $d \approx l / 25 = 3000 / 25 = 120$ mm. Provide overall depth $D = 150$ mm, clear cover $= 15$ mm, 10 mm bar $\implies d = 150 - 15 - 5 = 130$ mm.
2. **Loads (per metre width):**
   - Self-weight $= 0.15 \times 25 = 3.75$ kN/m²
   - Floor finish $= 1.00$ kN/m²
   - Total dead load $= 4.75$ kN/m²; Live load $= 3.00$ kN/m²
   - Total factored load $w_u = 1.5 \times (4.75 + 3.0) = 11.625$ kN/m
3. **Factored Moments and Shear:**
   - Effective span $l_{eff} = \min(3.0 + 0.13, 3.0 + 0.20) = 3.13$ m
   - $M_u = \frac{w_u l_{eff}^2}{8} = \frac{11.625 \times 3.13^2}{8} = 14.24$ kN·m/m
   - Factored shear at support face: $V_u = \frac{w_u l_{clear}}{2} = \frac{11.625 \times 3.0}{2} = 17.44$ kN
   - Factored shear at critical section ($d = 130$ mm from support face):
     $$V_{u,d} = 17.44 - 11.625 \times 0.13 = 15.93\text{ kN}$$
4. **Reinforcement:**
   - $A_{st} = \frac{0.5 \times 25}{415} \left[1 - \sqrt{1 - \frac{4.59 \times 14.24 \times 10^6}{25 \times 1000 \times 130^2}}\right] \times 1000 \times 130 \approx 315\text{ mm}^2/\text{m}$
   - Minimum steel: $0.12\% \times bD = 0.0012 \times 1000 \times 150 = 180\text{ mm}^2/\text{m} < 315$ ✓
   - Main steel: **10 mm @ 240 mm c/c** ($A_{st} = 327$ mm²/m)
   - Distribution steel: **8 mm @ 250 mm c/c** ($A_{st} = 201$ mm²/m $> 180$ mm²/m)
5. **One-Way Shear Verification:**
   - Nominal shear stress $\tau_v = \frac{V_{u,d}}{b d} = \frac{15.93 \times 10^3}{1000 \times 130} = 0.123$ N/mm²
   - Steel percentage $p_t = \frac{327}{1000 \times 130} \times 100 = 0.25\%$
   - Permissible shear stress for M25 at $p_t = 0.25\%$ (Table 19): $\tau_c \approx 0.36$ N/mm²
   - Slab depth factor $k$ (IS 456 Cl. 40.2.1.1 for $D = 150$ mm): $k = 1.30$
   - Permissible shear strength $\tau_{c,\text{slab}} = k \tau_c = 1.30 \times 0.36 = 0.468$ N/mm²
   - Since $\tau_v (0.123\text{ N/mm}^2) \ll \tau_{c,\text{slab}} (0.468\text{ N/mm}^2)$, the slab is completely safe in shear without shear reinforcement ✓

**Answer:** $D = 150$ mm, $d = 130$ mm; Main bars **10 mm @ 240 mm c/c**; Distribution bars **8 mm @ 250 mm c/c**; Shear stress $\tau_v = 0.123$ N/mm² $< k\tau_c = 0.468$ N/mm² (Safe).

**Trap:** Never state that slabs are "not designed for shear". While slabs rarely require stirrups because $\tau_v < k\tau_c$, one-way shear and two-way punching shear MUST be checked. If shear stress exceeds permissible limits, slab depth must be increased because shear stirrups are difficult to fabricate in thin slabs.

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
| 2 | $A_{sc} = 923$ mm² (3-20mm), $A_{st} = 2214$ mm² (4-25mm + 1-20mm) |
| 3 | 8mm 2-legged stirrups @ 125 mm c/c |
| 4 | $L_d = 806$ mm (deformed) |
| 5 | 8-16mm bars ($A_{sc} = 1609$ mm² $\ge 0.8\% A_g$) with 8mm ties @ 250 c/c |
| 6 | $D = 150$ mm, main 10mm @ 240 c/c, dist 8mm @ 250 c/c, $\tau_v = 0.123 < k\tau_c$ ✓ |
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
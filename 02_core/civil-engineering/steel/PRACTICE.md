# Steel Design — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for L&T, Tata Projects, PSUs, consulting firms
> **Canonical Study:** [`steel-design.md`](steel-design.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap
> **Code:** IS 800:2007 (Limit State Method)

---

## Problem 1: Tension Member Design

**Given:** Tension member with $T = 300$ kN, $f_y = 250$ MPa, $f_u = 410$ MPa.

**Find:** Required gross area $A_g$.

**Method:** Gross yielding $T_{dg} = A_g f_y/\gamma_{m0}$; net rupture $T_{dn} = 0.9 A_n f_u/\gamma_{m1}$.

**Calculation:**
- Gross yielding: $A_g \ge \frac{T \gamma_{m0}}{f_y} = \frac{300 \times 10^3 \times 1.10}{250} = 1320$ mm²
- Net rupture: $A_n \ge \frac{T \gamma_{m1}}{0.9 f_u} = \frac{300 \times 10^3 \times 1.25}{0.9 \times 410} = 1016$ mm²
- Increase net area by 25–40% for gross: $A_g \approx 1.3 \times 1016 = 1321$ mm²
- Select ISA 90 × 90 × 8 ($A_g = 1380$ mm²)

**Answer:** ISA 90 × 90 × 8 ($A_g = 1380$ mm²)

**Trap:** The larger required area governs — here gross yielding (1320 mm²) governs.

---

## Problem 2: Bolted Connection — Shear Strength

**Given:** 20 mm bolt (property class 4.6), single shear, threads intercept shear plane. $f_{ub} = 400$ MPa.

**Find:** Design shear strength $V_{dsb}$.

**Method:** $V_{dsb} = \frac{f_{ub}}{\sqrt{3} \gamma_{mb}} n_n A_{nb}$.

**Calculation:**
- $A_{sb} = \pi \times 20^2/4 = 314$ mm²
- $A_{nb} = 0.78 \times 314 = 245$ mm²
- $V_{dsb} = \frac{400}{\sqrt{3} \times 1.25} \times 1 \times 245 = \frac{400 \times 245}{2.165} = 45,266$ N

**Answer:** $V_{dsb} = 45.3$ kN

**Trap:** If threads don't intercept the shear plane, use full shank area $A_{sb} = 314$ mm² → higher capacity.

---

## Problem 3: Bolted Connection — Bearing Strength

**Given:** 20 mm bolt, plate thickness $t = 10$ mm, $f_u = 410$ MPa, $e = 40$ mm, $p = 60$ mm, $d_0 = 22$ mm.

**Find:** Design bearing strength $V_{dpb}$.

**Method:** $V_{dpb} = \frac{2.5 k_b d t f_u}{\gamma_{mb}}$.

**Calculation:**
- $k_b$ = min($e/3d_0 = 40/66 = 0.606$, $p/3d_0 - 0.25 = 60/66 - 0.25 = 0.659$, $f_{ub}/f_u = 400/410 = 0.976$, 1.0) = 0.606
- $V_{dpb} = \frac{2.5 \times 0.606 \times 20 \times 10 \times 410}{1.25} = \frac{124,230}{1.25} = 99,384$ N

**Answer:** $V_{dpb} = 99.4$ kN

**Trap:** $k_b$ is the minimum of four ratios — edge distance often governs.

---

## Problem 4: Number of Bolts

**Given:** Connection carrying $P = 200$ kN. Bolt value $V_{db} = 45.3$ kN (from Problem 2).

**Find:** Number of bolts required.

**Method:** $n = P/V_{db}$.

**Calculation:**
- $n = 200/45.3 = 4.41$ → use 5 bolts

**Answer:** 5 bolts

**Trap:** Always round up to the next integer.

---

## Problem 5: Fillet Weld Design

**Given:** 6 mm fillet weld, 200 mm long, $f_u = 410$ MPa, shop weld.

**Find:** Design strength $P_{dw}$.

**Method:** $P_{dw} = \frac{L_w t_t f_u}{\sqrt{3} \gamma_{mw}}$.

**Calculation:**
- $t_t = K \times s = 0.7 \times 6 = 4.2$ mm
- $L_w = 200 - 2 \times 6 = 188$ mm
- $P_{dw} = \frac{188 \times 4.2 \times 410}{\sqrt{3} \times 1.25} = \frac{323,736}{2.165} = 149,530$ N

**Answer:** $P_{dw} = 149.5$ kN

**Trap:** Effective length deducts $2s$ from overall length — weld ends have stress concentration.

---

## Problem 6: Butt Weld Design

**Given:** Full penetration butt weld, plate thickness $t = 12$ mm, $L_w = 300$ mm, $f_y = 250$ MPa, shop weld.

**Find:** Design axial strength $T_{dw}$.

**Method:** $T_{dw} = \frac{f_y L_w t_e}{\gamma_{mw}}$.

**Calculation:**
- Full penetration: $t_e = t = 12$ mm
- $T_{dw} = \frac{250 \times 300 \times 12}{1.25} = \frac{900,000}{1.25} = 720,000$ N

**Answer:** $T_{dw} = 720$ kN

**Trap:** For partial penetration, $t_e = 5/8 \times$ thinner member thickness.

---

## Problem 7: Compression Member

**Given:** Column with $P_d = 500$ kN, $A_e = 5000$ mm², $f_{cd} = 120$ N/mm².

**Find:** Design compressive strength.

**Method:** $P_d = A_e f_{cd}$.

**Calculation:**
- $P_d = 5000 \times 120 = 600,000$ N = 600 kN
- 600 kN > 500 kN ✓ (safe)
- Check slenderness: $KL/r \le 180$

**Answer:** $P_d = 600$ kN — safe

**Trap:** $f_{cd}$ already accounts for residual stress, initial imperfection, and eccentricity.

---

## Problem 8: Effective Length of Column

**Given:** Column of length $L = 4$ m with one end fixed, one end pinned.

**Find:** Effective length.

**Method:** Effective length factor from IS 800.

**Calculation:**
- One fixed, one pinned: $L_e = 0.8L = 0.8 \times 4 = 3.2$ m

**Answer:** $L_e = 3.2$ m

**Trap:** Both ends fixed: 0.65L; both pinned: 1.0L; one fixed one free: 2.0L.

---

## Problem 9: Beam Bending Strength (Laterally Supported)

**Given:** I-section with $Z_p = 1000 \times 10^3$ mm³, $Z_e = 850 \times 10^3$ mm³, $f_y = 250$ MPa.

**Find:** Design bending strength $M_d$.

**Method:** $M_d = \frac{\beta_b Z_p f_y}{\gamma_{m0}} \le \frac{1.2 Z_e f_y}{\gamma_{m0}}$.

**Calculation:**
- $M_d = \frac{1.0 \times 1000 \times 10^3 \times 250}{1.10} = 227.3$ kN·m
- Upper limit: $\frac{1.2 \times 850 \times 10^3 \times 250}{1.10} = 231.8$ kN·m
- $227.3 < 231.8$ ✓

**Answer:** $M_d = 227.3$ kN·m

**Trap:** The 1.2$Z_e$ limit prevents over-reliance on plastic capacity.

---

## Problem 10: Beam Shear Strength

**Given:** I-section with $A_v = h t_w = 300 \times 8 = 2400$ mm², $f_{yw} = 250$ MPa.

**Find:** Design shear strength $V_d$.

**Method:** $V_d = \frac{A_v f_{yw}}{\sqrt{3} \gamma_{m0}}$.

**Calculation:**
- $V_d = \frac{2400 \times 250}{\sqrt{3} \times 1.10} = \frac{600,000}{1.905} = 314,961$ N

**Answer:** $V_d = 315$ kN

**Trap:** For I-section major axis, $A_v = h t_w$ (not the full web area).

---

## Problem 11: Eccentric Connection — Direct Shear + Moment

**Given:** Bracket connection, $P = 100$ kN, eccentricity $e = 200$ mm, 4 bolts at $r = 100$ mm from CG.

**Find:** Force on critical bolt.

**Method:** $F_a = P/n$; $F_m = \frac{P e r}{\sum r^2}$; $F_R = \sqrt{F_a^2 + F_m^2}$.

**Calculation:**
- $F_a = 100/4 = 25$ kN
- $M = P \times e = 100 \times 0.2 = 20$ kN·m
- $\sum r^2 = 4 \times 100^2 = 40,000$ mm²
- $F_m = \frac{20 \times 10^6 \times 100}{40,000} = 50$ kN
- $F_R = \sqrt{25^2 + 50^2} = \sqrt{625 + 2500} = \sqrt{3125} = 55.9$ kN

**Answer:** $F_R = 55.9$ kN on critical bolt

**Trap:** The critical bolt is the farthest from CG, nearest to the load line.

---

## Problem 12: Net Sectional Area (Staggered Bolting)

**Given:** Plate $B = 200$ mm, $t = 10$ mm, 2 bolt holes $d_0 = 22$ mm, stagger $p = 40$ mm, gauge $g = 60$ mm.

**Find:** Net area.

**Method:** $A_n = \left(B - nd_0 + \sum \frac{p^2}{4g}\right)t$.

**Calculation:**
- $A_n = \left(200 - 2 \times 22 + \frac{40^2}{4 \times 60}\right) \times 10 = (200 - 44 + 6.67) \times 10 = 162.67 \times 10 = 1627$ mm²

**Answer:** $A_n = 1627$ mm²

**Trap:** Staggered holes add back $\sum p^2/4g$ — stagger can increase net area.

---

## Problem 13: Slenderness Ratio Check

**Given:** Column, $L_e = 3.2$ m, $r = 40$ mm.

**Find:** Slenderness ratio and check against limit.

**Method:** $\lambda = L_e/r \le 180$ (compression, DL+IL).

**Calculation:**
- $\lambda = 3200/40 = 80$
- $80 < 180$ ✓

**Answer:** $\lambda = 80$ — OK

**Trap:** Tension members allow up to 400; compression limited to 180.

---

## Problem 14: Plate Girder Economical Depth

**Given:** $M = 2000$ kN·m, $k = 1.2$, $f_y = 250$ MPa.

**Find:** Economical depth.

**Method:** $d = \left(\frac{M k}{f_y}\right)^{1/3}$.

**Calculation:**
- $d = \left(\frac{2000 \times 10^6 \times 1.2}{250}\right)^{1/3} = (9.6 \times 10^6)^{1/3} = 212.4$ mm

**Answer:** $d \approx 212$ mm (use 220 mm)

**Trap:** Economical depth balances web and flange material costs.

---

## Problem 15: Gantry Girder Deflection

**Given:** Gantry girder, span $L = 6$ m, electric crane ≤ 500 kN.

**Find:** Deflection limit.

**Method:** Electric ≤ 500 kN: $L/750$.

**Calculation:**
- $\delta_{max} = 6000/750 = 8$ mm

**Answer:** $\delta_{max} = 8$ mm

**Trap:** Manually operated: L/500; electric > 500 kN: L/1000.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | ISA 90 × 90 × 8 ($A_g = 1380$ mm²) |
| 2 | $V_{dsb} = 45.3$ kN |
| 3 | $V_{dpb} = 99.4$ kN |
| 4 | 5 bolts |
| 5 | $P_{dw} = 149.5$ kN |
| 6 | $T_{dw} = 720$ kN |
| 7 | $P_d = 600$ kN — safe |
| 8 | $L_e = 3.2$ m |
| 9 | $M_d = 227.3$ kN·m |
| 10 | $V_d = 315$ kN |
| 11 | $F_R = 55.9$ kN |
| 12 | $A_n = 1627$ mm² |
| 13 | $\lambda = 80$ — OK |
| 14 | $d \approx 212$ mm |
| 15 | $\delta_{max} = 8$ mm |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Tension members | 1, 12 | Can you compute gross/net area and design strength? |
| Bolted connections | 2, 3, 4, 11 | Can you compute bolt value and number of bolts? |
| Welded connections | 5, 6 | Can you design fillet and butt welds? |
| Compression members | 7, 8, 13 | Can you check buckling and slenderness? |
| Beams | 9, 10 | Can you compute bending and shear strength? |
| Eccentric connections | 11 | Can you find the critical bolt force? |
| Plate girders | 14 | Can you find economical depth? |
| Gantry girders | 15 | Can you apply deflection limits? |

---

## Practice Strategy

1. **Solve Problems 1–4** (tension + bolted connections) — the most frequently tested.
2. **Solve Problems 5–8** (welds + compression) — critical for design roles.
3. **Solve Problems 9–15** (beams + eccentric + plate girders) — advanced, for PSU/consulting.
4. Re-attempt any problem you couldn't solve in < 5 minutes.
5. Then take the [`TEST.md`](TEST.md) to verify mastery.
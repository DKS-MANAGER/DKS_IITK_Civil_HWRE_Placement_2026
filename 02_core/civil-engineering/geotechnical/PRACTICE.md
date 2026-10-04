# Geotechnical Engineering — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for foundation/geotech roles and PSUs
> **Canonical Study:** [`geotechnical.md`](geotechnical.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: Phase Relationships

**Given:** Soil with $e = 0.6$, $G_s = 2.65$, $S = 0.8$.

**Find:** Water content $w$, bulk unit weight $\gamma$, dry unit weight $\gamma_d$.

**Method:** $Se = wG_s$; $\gamma = \frac{G_s + Se}{1+e}\gamma_w$; $\gamma_d = \frac{G_s}{1+e}\gamma_w$.

**Calculation:**
- $w = \frac{Se}{G_s} = \frac{0.8 \times 0.6}{2.65} = 0.181 = 18.1\%$
- $\gamma = \frac{2.65 + 0.8 \times 0.6}{1.6} \times 9.81 = \frac{3.13}{1.6} \times 9.81 = 19.19$ kN/m³
- $\gamma_d = \frac{2.65}{1.6} \times 9.81 = 16.25$ kN/m³

**Answer:** $w = 18.1\%$, $\gamma = 19.19$ kN/m³, $\gamma_d = 16.25$ kN/m³

**Trap:** Use $Se = wG_s$ — don't confuse void ratio $e$ with porosity $n$.

---

## Problem 2: Permeability — Falling Head Test

**Given:** Falling head test: $a = 100$ mm², $L = 150$ mm, $A = 2000$ mm², $h_1 = 1000$ mm, $h_2 = 500$ mm, $t = 300$ s.

**Find:** Coefficient of permeability $k$.

**Method:** $k = \frac{aL}{At}\ln\frac{h_1}{h_2}$.

**Calculation:**
- $k = \frac{100 \times 150}{2000 \times 300}\ln\frac{1000}{500} = \frac{15000}{600000} \times 0.693 = 0.025 \times 0.693 = 0.0173$ mm/s

**Answer:** $k = 0.0173$ mm/s

**Trap:** Falling head uses natural log; constant head uses $k = QL/(Aht)$.

---

## Problem 3: Seepage Through Flow Net

**Given:** Flow net with $N_f = 4$ flow channels, $N_d = 8$ potential drops, $H = 6$ m, $k = 5 \times 10^{-5}$ m/s.

**Find:** Seepage quantity per unit length.

**Method:** $q = kH\frac{N_f}{N_d}$.

**Calculation:**
- $q = 5 \times 10^{-5} \times 6 \times \frac{4}{8} = 5 \times 10^{-5} \times 3 = 1.5 \times 10^{-4}$ m³/s/m

**Answer:** $q = 1.5 \times 10^{-4}$ m³/s per metre

**Trap:** Flow nets require curvilinear squares — the ratio $N_f/N_d$ is dimensionless.

---

## Problem 4: Consolidation Settlement

**Given:** Clay layer $H = 3$ m, $e_0 = 0.8$, $C_c = 0.25$, $\sigma'_0 = 100$ kPa, $\Delta\sigma = 80$ kPa.

**Find:** Primary consolidation settlement.

**Method:** $S_c = \frac{C_c H}{1+e_0}\log\frac{\sigma'_0+\Delta\sigma}{\sigma'_0}$.

**Calculation:**
- $S_c = \frac{0.25 \times 3000}{1.8}\log\frac{180}{100} = 416.7 \times 0.2553 = 106.4$ mm

**Answer:** $S_c = 106.4$ mm

**Trap:** Use $\log_{10}$ (not natural log) in the consolidation equation.

---

## Problem 5: Time Rate of Consolidation

**Given:** Clay layer $H = 3$ m (drained both sides), $c_v = 2 \times 10^{-7}$ m²/s.

**Find:** Time for 90% consolidation.

**Method:** $T_v = \frac{c_v t}{H_{dr}^2}$; $T_v = 0.848$ for 90%.

**Calculation:**
- $H_{dr} = H/2 = 1.5$ m (double drainage)
- $t = \frac{T_v H_{dr}^2}{c_v} = \frac{0.848 \times 1.5^2}{2 \times 10^{-7}} = \frac{1.908}{2 \times 10^{-7}} = 9.54 \times 10^6$ s = 110 days

**Answer:** $t = 110$ days

**Trap:** For double drainage, $H_{dr} = H/2$ — this quadruples the consolidation rate.

---

## Problem 6: Mohr-Coulomb Shear Strength

**Given:** $c' = 20$ kPa, $\phi' = 25°$, effective normal stress $\sigma' = 100$ kPa.

**Find:** Shear strength.

**Method:** $\tau_f = c' + \sigma'\tan\phi'$.

**Calculation:**
- $\tau_f = 20 + 100 \times \tan 25° = 20 + 100 \times 0.466 = 66.6$ kPa

**Answer:** $\tau_f = 66.6$ kPa

**Trap:** Use effective stress, not total stress, for drained shear strength.

---

## Problem 7: Bearing Capacity — Terzaghi

**Given:** Strip footing, $B = 2$ m, $D_f = 1.5$ m, $c = 20$ kPa, $\phi = 25°$, $\gamma = 18$ kN/m³.

**Find:** Ultimate bearing capacity $q_u$.

**Method:** $q_u = cN_c + qN_q + \frac{1}{2}\gamma BN_\gamma$.

**Calculation:**
- $N_c = 25.1$, $N_q = 12.7$, $N_\gamma = 9.7$ (for $\phi = 25°$)
- $q_u = 20(25.1) + (18 \times 1.5)(12.7) + 0.5(18)(2)(9.7)$
- $q_u = 502 + 342.9 + 174.6 = 1019.5$ kPa

**Answer:** $q_u = 1019.5$ kPa

**Trap:** Net bearing capacity $q_{nu} = q_u - \gamma D_f = 992.5$ kPa; safe $q_s = q_{nu}/F + \gamma D_f$.

---

## Problem 8: Safe Bearing Pressure

**Given:** From Problem 7, $q_{nu} = 992.5$ kPa, $F = 3$, $\gamma D_f = 27$ kPa.

**Find:** Safe bearing pressure.

**Method:** $q_s = q_{nu}/F + \gamma D_f$.

**Calculation:**
- $q_s = 992.5/3 + 27 = 330.8 + 27 = 357.8$ kPa

**Answer:** $q_s = 357.8$ kPa

**Trap:** Add back the overburden term $\gamma D_f$ after dividing by FOS.

---

## Problem 9: Pile Capacity

**Given:** Pile, $A_b = 0.09$ m², $q_b = 2000$ kPa, skin friction $f_s = 50$ kPa, $A_s = 12$ m².

**Find:** Ultimate pile capacity.

**Method:** $Q_u = Q_b + Q_s = q_b A_b + f_s A_s$.

**Calculation:**
- $Q_u = 2000 \times 0.09 + 50 \times 12 = 180 + 600 = 780$ kN

**Answer:** $Q_u = 780$ kN

**Trap:** Apply FOS (2.5 static) for allowable capacity: $Q_{all} = 780/2.5 = 312$ kN.

---

## Problem 10: Rankine Active Earth Pressure

**Given:** Retaining wall, $\phi = 30°$, $\gamma = 18$ kN/m³, wall height $H = 5$ m, no cohesion.

**Find:** Active earth pressure at base and total thrust.

**Method:** $K_a = \tan^2(45° - \phi/2)$; $p_a = K_a\gamma H$; $P_a = \frac{1}{2}K_a\gamma H^2$.

**Calculation:**
- $K_a = \tan^2(45° - 15°) = \tan^2 30° = 0.333$
- $p_a = 0.333 \times 18 \times 5 = 30$ kPa
- $P_a = \frac{1}{2} \times 0.333 \times 18 \times 25 = 75$ kN/m

**Answer:** $p_a = 30$ kPa, $P_a = 75$ kN/m

**Trap:** Rankine assumes a smooth wall (no wall friction); Coulomb accounts for $\delta$.

---

## Problem 11: Slope Stability — Ordinary Method of Slices

**Given:** Slice with $W = 100$ kN, $\alpha = 20°$, $c' = 10$ kPa, $l = 2$ m, $\phi' = 25°$.

**Find:** Factor of safety contribution.

**Method:** $F_s = \frac{\sum(c'l + W\cos\alpha\tan\phi')}{\sum W\sin\alpha}$.

**Calculation:**
- Resisting: $10 \times 2 + 100\cos 20° \times \tan 25° = 20 + 100 \times 0.94 \times 0.466 = 20 + 43.8 = 63.8$ kN
- Driving: $100 \times \sin 20° = 100 \times 0.342 = 34.2$ kN
- $F_s = 63.8/34.2 = 1.87$

**Answer:** $F_s = 1.87$ (for this slice)

**Trap:** Bishop's simplified method uses $m_\alpha$ and is more accurate than Fellenius.

---

## Problem 12: Compaction — Relative Density

**Given:** Field dry density $\gamma_{d,field} = 17.5$ kN/m³, max dry density $\gamma_{d,max} = 18.0$ kN/m³.

**Find:** Relative compaction.

**Method:** $RC = \frac{\gamma_{d,field}}{\gamma_{d,max}} \times 100\%$.

**Calculation:**
- $RC = \frac{17.5}{18.0} \times 100 = 97.2\%$

**Answer:** $RC = 97.2\%$ (≥ 95% Modified Proctor ✓)

**Trap:** Compaction at OMC gives max dry density — field density must be ≥ 95% of it.

---

## Problem 13: Effective Stress

**Given:** Soil at depth 5 m, water table at 2 m, $\gamma = 18$ kN/m³ (above WT), $\gamma_{sat} = 20$ kN/m³.

**Find:** Effective stress at 5 m depth.

**Method:** $\sigma' = \sigma - u$.

**Calculation:**
- Total: $\sigma = 18 \times 2 + 20 \times 3 = 36 + 60 = 96$ kPa
- Pore pressure: $u = 9.81 \times 3 = 29.4$ kPa
- $\sigma' = 96 - 29.4 = 66.6$ kPa

**Answer:** $\sigma' = 66.6$ kPa

**Trap:** Above the water table use bulk unit weight; below use saturated unit weight.

---

## Problem 14: USCS Classification

**Given:** Soil: 60% passes No.4 sieve, 45% passes No.200, LL = 45, PL = 25.

**Find:** USCS classification.

**Method:** Determine coarse/fine fraction, then plasticity.

**Calculation:**
- 45% passes No.200 → more than 50% passes → **fine-grained**
- PI = LL − PL = 45 − 25 = 20
- LL = 45 < 50, PI = 20 > 7, above A-line → **CL (lean clay)**

**Answer:** CL — lean clay

**Trap:** For fine soils, use the plasticity chart (A-line) with LL and PI.

---

## Problem 15: Immediate Settlement

**Given:** Footing, $q = 200$ kPa, $B = 2$ m, $E_u = 20$ MPa, $\nu = 0.3$, $I_f = 0.8$.

**Find:** Immediate settlement.

**Method:** $S_i = \frac{qB(1-\nu^2)}{E_u} I_f$.

**Calculation:**
- $S_i = \frac{200 \times 2 \times (1 - 0.09)}{20 \times 10^6} \times 0.8 = \frac{400 \times 0.91}{20 \times 10^6} \times 0.8 = \frac{364}{20 \times 10^6} \times 0.8 = 1.456 \times 10^{-5} \times 0.8 = 1.16 \times 10^{-5}$ m = 11.6 mm

**Answer:** $S_i = 11.6$ mm

**Trap:** Immediate settlement uses undrained modulus $E_u$; consolidation uses $C_c$.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | $w = 18.1\%$, $\gamma = 19.19$, $\gamma_d = 16.25$ kN/m³ |
| 2 | $k = 0.0173$ mm/s |
| 3 | $q = 1.5 \times 10^{-4}$ m³/s/m |
| 4 | $S_c = 106.4$ mm |
| 5 | $t = 110$ days |
| 6 | $\tau_f = 66.6$ kPa |
| 7 | $q_u = 1019.5$ kPa |
| 8 | $q_s = 357.8$ kPa |
| 9 | $Q_u = 780$ kN |
| 10 | $p_a = 30$ kPa, $P_a = 75$ kN/m |
| 11 | $F_s = 1.87$ |
| 12 | $RC = 97.2\%$ |
| 13 | $\sigma' = 66.6$ kPa |
| 14 | CL — lean clay |
| 15 | $S_i = 11.6$ mm |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Phase relationships | 1, 13 | Can you compute $e$, $w$, $\gamma$, $\sigma'$? |
| Permeability & seepage | 2, 3 | Can you apply Darcy's law and flow nets? |
| Consolidation | 4, 5 | Can you compute settlement and time rate? |
| Shear strength | 6 | Can you apply Mohr-Coulomb? |
| Bearing capacity | 7, 8 | Can you compute $q_u$ and $q_s$? |
| Pile foundations | 9 | Can you compute pile capacity? |
| Earth pressure | 10 | Can you apply Rankine/Coulomb? |
| Slope stability | 11 | Can you compute $F_s$? |
| Compaction | 12 | Can you check relative compaction? |
| Classification | 14 | Can you classify soil by USCS? |
| Settlement | 15 | Can you compute immediate settlement? |

---

## Practice Strategy

1. **Solve Problems 1–4** (phase + permeability + consolidation) — the most frequently tested.
2. **Solve Problems 6–10** (shear + bearing + piles + earth pressure) — critical for foundation design.
3. **Solve Problems 11–15** (slopes + compaction + classification) — advanced, for PSU/consulting.
4. Re-attempt any problem you couldn't solve in < 5 minutes.
5. Then take the [`TEST.md`](TEST.md) to verify mastery.
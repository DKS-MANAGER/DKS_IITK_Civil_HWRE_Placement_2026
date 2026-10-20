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

## Problem 12: Field Compaction Control — Relative Compaction vs. Relative Density

**Given:** An embankment fill has field dry density $\gamma_{d,\text{field}} = 17.5$ kN/m³, and laboratory maximum dry density $\gamma_{d,\max,\text{lab}} = 18.0$ kN/m³ obtained from the Standard Proctor compaction test.

**Find:** Relative compaction ($RC$), and explain its relationship to relative density ($I_D$).

**Method:** 
$$RC = \frac{\gamma_{d,\text{field}}}{\gamma_{d,\max,\text{lab}}} \times 100\%$$

**Calculation:**
- $RC = \frac{17.5}{18.0} \times 100\% = \mathbf{97.2\%}$
- Check against standard specification: For highway subgrades and structural fills, MoRTH Section 300 / CPWD requires $RC \ge 95\%$ of Standard Proctor MDD. Since $97.2\% \ge 95\%$, the compaction is **acceptable** ✓.

**Answer:** $RC = 97.2\%$ (satisfies $\ge 95\%$ field compaction criterion)

**Trap:** Never confuse **Relative Compaction ($RC$)** with **Relative Density ($I_D$ / $D_r$)**! Relative compaction applies to all soils as a ratio of field to lab density ($\gamma_d/\gamma_{d,\max}$). Relative density applies *only* to cohesionless soils based on void ratio limits ($I_D = \frac{e_{\max}-e}{e_{\max}-e_{\min}}$). For granular soils, an empirical correlation is $RC \approx 80 + 0.20 I_D \implies I_D \approx \frac{97.2 - 80}{0.20} \approx 86\%$ (dense sand).

---

## Problem 13: Effective Stress

**Given:** Soil profile: total depth to point of interest = 5 m. Groundwater table (GWT) is located at 2 m below ground surface. Soil above GWT has moist unit weight $\gamma = 18$ kN/m³. Soil below GWT is fully saturated with saturated unit weight $\gamma_{sat} = 20$ kN/m³. Unit weight of water $\gamma_w = 9.81$ kN/m³.

**Find:** Total stress ($\sigma$), pore water pressure ($u$), and effective stress ($\sigma'$) at 5 m depth.

**Method:** Terzaghi's effective stress principle: $\sigma' = \sigma - u$.

**Calculation:**
- Total stress at 5 m:
  $$\sigma = \sum (\gamma \cdot h) = (18 \times 2) + (20 \times 3) = 36 + 60 = 96.0\text{ kPa}$$
- Pore water pressure at 5 m:
  $$u = \gamma_w \cdot h_w = 9.81 \times (5 - 2) = 9.81 \times 3 = 29.43\text{ kPa}$$
- Effective stress at 5 m:
  $$\sigma' = \sigma - u = 96.0 - 29.43 = \mathbf{66.57\text{ kPa}} \approx 66.6\text{ kPa}$$
  *(Alternative check using submerged unit weight: $\sigma' = (18 \times 2) + (\gamma_{sub} \times 3) = 36 + (20 - 9.81) \times 3 = 36 + 30.57 = 66.57\text{ kPa}$ ✓).*

**Answer:** $\sigma = 96.0$ kPa, $u = 29.4$ kPa, $\sigma' = 66.6$ kPa

**Trap:** Above the water table use bulk/moist unit weight; below the water table use submerged unit weight $\gamma_{sub} = \gamma_{sat} - \gamma_w$ or subtract pore water pressure $u = \gamma_w h_w$ from total stress.

---

## Problem 14: Unified Soil Classification System (USCS)

**Given:** Sieve and Atterberg limits laboratory test results for a soil specimen:
- Percent passing No. 4 sieve (4.75 mm) = 60%
- Percent passing No. 200 sieve (0.075 mm / 75 μm) = 45%
- Liquid Limit ($LL$) = 45%, Plastic Limit ($PL$) = 25%

**Find:** USCS group symbol and group name per ASTM D2487 / IS 1498:1970.

**Method:** 
1. Determine coarse vs. fine-grained fraction based on No. 200 sieve (75 μm).
2. For coarse soils, determine gravel vs. sand fraction based on No. 4 sieve (4.75 mm).
3. Evaluate fines percentage and plasticity using the Casagrande A-line: $PI_{A\text{-line}} = 0.73(LL - 20)$.

**Calculation:**
1. **Coarse vs. Fine Evaluation:**
   - Percentage passing No. 200 sieve = $45\%$.
   - Percentage retained on No. 200 sieve $= 100\% - 45\% = 55\%$.
   - Since **$\ge 50\%$ is retained on No. 200**, the soil is **COARSE-GRAINED** (NOT fine-grained!).
2. **Gravel vs. Sand Evaluation:**
   - Total coarse fraction $= 55\%$.
   - Percentage retained on No. 4 sieve $= 100\% - 60\% = 40\%$ (Gravel fraction).
   - Percentage passing No. 4 and retained on No. 200 $= 60\% - 45\% = 15\%$ (Sand fraction).
   - Fraction of coarse material that is gravel $= \frac{40\%}{55\%} = 72.7\% > 50\%$.
   - Therefore, the primary coarse constituent is **GRAVEL (G)**.
3. **Fines and Plasticity Evaluation:**
   - Fines content $= 45\% > 12\% \implies$ dual classification governed by plasticity of fines.
   - Plasticity Index $PI = LL - PL = 45 - 25 = 20$.
   - A-line equation: $PI_{A\text{-line}} = 0.73(LL - 20) = 0.73(45 - 20) = 0.73(25) = 18.25$.
   - Since $PI = 20 > PI_{A\text{-line}} = 18.25$, the fines plot **ABOVE the A-line** and have $LL = 45 < 50 \implies$ **Clay of intermediate/low plasticity (CL)**.
4. **Final Group Symbol & Name:**
   - Prefix: **G** (Gravel); Suffix: **C** (Clayey fines).
   - USCS Symbol: **GC**
   - USCS Name: **Clayey gravel with sand** (since sand fraction $15\% \ge 15\%$).

*(Note: If the given had been $55\%$ passing No. 200, $>50\%$ would pass No. 200, classifying it as fine-grained lean clay **CL**).*

**Answer:** **GC — Clayey gravel with sand**

**Trap:** Never declare a soil "fine-grained" when $45\%$ passes No. 200. $45\%$ passing means $55\%$ is retained, making it coarse-grained! Always check coarse vs. fine first, then gravel vs. sand, and finally gradation/plasticity.

---

## Problem 15: Immediate Elastic Settlement

**Given:** A flexible square footing of size $B = 2.0$ m resting on a saturated clay layer with undrained Young's modulus $E_u = 20$ MPa, Poisson's ratio $\nu = 0.30$. Net uniform foundation pressure $q = 200$ kPa. Influence factor for center of flexible foundation $I_f = 0.80$.

**Find:** Immediate (elastic) settlement ($S_i$) at the center of the footing.

**Method:** Schleicher / Janbu elastic theory formulation:
$$S_i = \frac{q \cdot B \cdot (1 - \nu^2)}{E_u} \cdot I_f$$

**Calculation:**
1. **Unit Consistency Check:**
   - $q = 200\text{ kPa} = 200\text{ kN/m}^2$
   - $B = 2.0\text{ m}$
   - $E_u = 20\text{ MPa} = 20,000\text{ kPa} = 20,000\text{ kN/m}^2$ (Note: $1\text{ MPa} = 10^3\text{ kPa}$, NOT $10^6\text{ kPa}$!)
   - $(1 - \nu^2) = (1 - 0.3^2) = 1 - 0.09 = 0.91$

2. **Settlement Computation:**
   $$S_i = \frac{200 \times 2.0 \times 0.91}{20,000} \times 0.80$$
   $$S_i = \frac{364}{20,000} \times 0.80 = 0.0182 \times 0.80 = 0.01456\text{ m} = \mathbf{14.56\text{ mm}}$$

**Answer:** $S_i = \mathbf{14.56\text{ mm}}$

**Trap:** Dimension and unit mismatch: mixing $q$ in kPa with $E_u$ in Pa ($20 \times 10^6$) results in an answer 1000 times too small ($0.01456$ mm instead of $14.56$ mm). Always keep $q$ and $E_u$ in consistent units (both in kPa or both in MPa).

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
| 12 | $RC = 97.2\%$ ($\ge 95\%$ MoRTH criterion) |
| 13 | $\sigma = 96.0$ kPa, $u = 29.4$ kPa, $\sigma' = 66.6$ kPa |
| 14 | **GC** — Clayey gravel with sand |
| 15 | $S_i = \mathbf{14.56\text{ mm}}$ |

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
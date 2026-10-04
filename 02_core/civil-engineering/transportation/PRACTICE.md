# Transportation Engineering — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for PSU roles (NHAI, IRCON, Airport Authority, Railways)
> **Canonical Study:** [`transportation-engineering.md`](transportation-engineering.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: Stopping Sight Distance

**Given:** Design speed $V = 80$ km/h, reaction time $t = 2.5$ s, $f = 0.35$, level road.

**Find:** SSD.

**Method:** $SSD = 0.278 \cdot V \cdot t + \frac{V^2}{254 f}$.

**Calculation:**
- $SSD = 0.278 \times 80 \times 2.5 + \frac{80^2}{254 \times 0.35} = 55.6 + \frac{6400}{88.9} = 55.6 + 72 = 127.6$ m

**Answer:** SSD ≈ 128 m

**Trap:** IRC standard SSD for 80 km/h is 120 m — use the standard value for design.

---

## Problem 2: Minimum Radius of Horizontal Curve

**Given:** Design speed $V = 80$ km/h, $e = 0.07$, $f = 0.15$.

**Find:** Minimum radius.

**Method:** $R_{min} = \frac{V^2}{127(e + f)}$.

**Calculation:**
- $R_{min} = \frac{80^2}{127(0.07 + 0.15)} = \frac{6400}{127 \times 0.22} = \frac{6400}{27.94} = 229$ m

**Answer:** $R_{min} = 229$ m

**Trap:** Use design speed in km/h and $e + f$ in decimal.

---

## Problem 3: Superelevation

**Given:** Design speed $V = 80$ km/h, radius $R = 300$ m, $f = 0.15$.

**Find:** Required superelevation.

**Method:** $e + f = \frac{V^2}{127R}$.

**Calculation:**
- $e + f = \frac{6400}{127 \times 300} = \frac{6400}{38100} = 0.168$
- $e = 0.168 - 0.15 = 0.018$ → but minimum $e = 0.07$ (IRC) governs

**Answer:** $e = 0.07$ (IRC minimum)

**Trap:** If computed $e < 0.07$, use the IRC minimum of 0.07.

---

## Problem 4: Traffic Flow — Greenshields Model

**Given:** $v_f = 80$ km/h, $k_j = 120$ veh/km.

**Find:** Maximum flow (capacity).

**Method:** $q_{max} = \frac{v_f \cdot k_j}{4}$.

**Calculation:**
- $q_{max} = \frac{80 \times 120}{4} = 2400$ veh/hr

**Answer:** $q_{max} = 2400$ veh/hr

**Trap:** Optimal speed $v_{opt} = v_f/2 = 40$ km/h; optimal density $k_{opt} = k_j/2 = 60$ veh/km.

---

## Problem 5: Webster's Optimal Cycle Length

**Given:** Lost time $L = 12$ s, flow ratios $Y_1 = 0.3$, $Y_2 = 0.25$.

**Find:** Optimal cycle length.

**Method:** $C_o = \frac{1.5L + 5}{1 - \sum Y_i}$.

**Calculation:**
- $\sum Y = 0.3 + 0.25 = 0.55$
- $C_o = \frac{1.5 \times 12 + 5}{1 - 0.55} = \frac{23}{0.45} = 51.1$ s

**Answer:** $C_o = 51$ s

**Trap:** $\sum Y$ must be < 1 for a feasible signal.

---

## Problem 6: Effective Green Time

**Given:** From Problem 5, $C = 51$ s, $L = 12$ s, $Y_1 = 0.3$, $Y_2 = 0.25$.

**Find:** Effective green time for phase 1.

**Method:** $g_i = \frac{Y_i}{\sum Y_j}(C - L)$.

**Calculation:**
- $g_1 = \frac{0.3}{0.55}(51 - 12) = 0.545 \times 39 = 21.3$ s

**Answer:** $g_1 = 21.3$ s

**Trap:** Effective green excludes lost time.

---

## Problem 7: PCU Conversion

**Given:** Traffic: 500 cars, 200 two-wheelers, 100 buses, 50 trucks.

**Find:** Total traffic in PCU.

**Method:** PCU = sum of vehicle count × PCU factor.

**Calculation:**
- PCU = $500 \times 1.0 + 200 \times 0.5 + 100 \times 3.0 + 50 \times 3.0 = 500 + 100 + 300 + 150 = 1050$ PCU

**Answer:** 1050 PCU

**Trap:** PCU factors: car 1.0, two-wheeler 0.5, bus/truck 3.0.

---

## Problem 8: CBR Pavement Design

**Given:** Subgrade CBR = 5%, traffic = 10 msa.

**Find:** Total pavement thickness.

**Method:** IRC:37 CBR design chart.

**Calculation:**
- From IRC:37 table, CBR 5%, 10 msa → 350 mm

**Answer:** Total thickness = 350 mm

**Trap:** Higher CBR = thinner pavement; higher traffic = thicker.

---

## Problem 9: Radius of Relative Stiffness (Rigid Pavement)

**Given:** $E = 3 \times 10^4$ MPa, $h = 250$ mm, $\mu = 0.15$, $k = 0.05$ N/mm³.

**Find:** Radius of relative stiffness.

**Method:** $l = \left(\frac{Eh^3}{12(1-\mu^2)k}\right)^{0.25}$.

**Calculation:**
- $l = \left(\frac{3 \times 10^4 \times 250^3}{12(1 - 0.0225) \times 0.05}\right)^{0.25} = \left(\frac{3 \times 10^4 \times 1.5625 \times 10^7}{12 \times 0.9775 \times 0.05}\right)^{0.25} = \left(\frac{4.6875 \times 10^{11}}{0.5865}\right)^{0.25} = (7.99 \times 10^{11})^{0.25} = 945$ mm

**Answer:** $l = 945$ mm

**Trap:** Units must be consistent (E in N/mm², h in mm, k in N/mm³).

---

## Problem 10: Summit Curve Length

**Given:** Grades $G_1 = +3\%$, $G_2 = -2\%$, design speed 80 km/h, SSD = 120 m.

**Find:** Length of summit curve (SSD < L case).

**Method:** $N = |G_1 - G_2| = 5$; $L = \frac{N \cdot S^2}{4.4}$ (for SSD < L).

**Calculation:**
- $N = |G_1 - G_2| = |3 - (-2)| = 5$
- For SSD > L: $L = 2S - \frac{4.4}{N} = 2 \times 120 - \frac{4.4}{5} = 240 - 0.88 = 239.1$ m
- Check: $L = 239.1$ m > $S = 120$ m → SSD < L case governs
- For SSD < L: $L = \frac{N \cdot S^2}{4.4} = \frac{5 \times 120^2}{4.4} = \frac{72000}{4.4} = 16364$ m

**Answer:** $L = 16364$ m (SSD < L case governs)

**Trap:** Compute both cases and use the one consistent with the SSD < L or SSD > L assumption.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | SSD ≈ 128 m |
| 2 | $R_{min} = 229$ m |
| 3 | $e = 0.07$ (IRC minimum) |
| 4 | $q_{max} = 2400$ veh/hr |
| 5 | $C_o = 51$ s |
| 6 | $g_1 = 21.3$ s |
| 7 | 1050 PCU |
| 8 | 350 mm |
| 9 | $l = 945$ mm |
| 10 | $L = 239$ m |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Sight distance | 1, 10 | Can you compute SSD and curve length? |
| Horizontal curves | 2, 3 | Can you compute radius and superelevation? |
| Traffic flow | 4, 7 | Can you apply Greenshields and PCU? |
| Signal design | 5, 6 | Can you apply Webster's method? |
| Pavement design | 8, 9 | Can you apply CBR and Westergaard? |

---

## Practice Strategy

1. **Solve Problems 1–3** (geometric design) — the most frequently tested.
2. **Solve Problems 4–7** (traffic engineering) — critical for traffic roles.
3. **Solve Problems 8–10** (pavement) — for PSU/consulting.
4. Then take the [`TEST.md`](TEST.md) to verify mastery.
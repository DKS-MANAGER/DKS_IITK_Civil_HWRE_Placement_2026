# Environmental Engineering — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for environmental/PSU roles (CPCB, SPCB, NEERI, CPHEEO)
> **Canonical Study:** [`environmental-engineering.md`](environmental-engineering.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: BOD Calculation

**Given:** Wastewater sample, dilution factor 50, initial DO $D_1 = 8$ mg/L, final DO $D_2 = 3$ mg/L, blank DO $B_1 = 9$, $B_2 = 8.5$ mg/L.

**Find:** BOD₅.

**Method:** $\text{BOD}_5 = (D_1 - D_2) - (B_1 - B_2) \times \text{dilution factor}$.

**Calculation:**
- $\text{BOD}_5 = (8 - 3) - (9 - 8.5) \times 50 = (5 - 0.5) \times 50 = 4.5 \times 50 = 225$ mg/L

**Answer:** BOD₅ = 225 mg/L

**Trap:** Subtract the blank DO depletion before multiplying by the dilution factor.

---

## Problem 2: BOD Remaining

**Given:** $L_0 = 300$ mg/L, $k_1 = 0.23$/day (base e).

**Find:** BOD remaining after 5 days.

**Method:** $L_t = L_0 e^{-k_1 t}$.

**Calculation:**
- $L_5 = 300 \times e^{-0.23 \times 5} = 300 \times e^{-1.15} = 300 \times 0.3166 = 95$ mg/L

**Answer:** $L_5 = 95$ mg/L

**Trap:** BOD exerted $y_t = L_0(1 - e^{-k_1 t}) = 205$ mg/L — remaining ≠ exerted.

---

## Problem 3: DO Sag Curve — Critical Deficit

**Given:** $k_1 = 0.3$/day, $k_2 = 0.5$/day, $L_0 = 200$ mg/L, $D_0 = 2$ mg/L.

**Find:** Critical deficit $D_c$.

**Method:** $D_c = \frac{k_1 L_0}{k_2} e^{-k_1 t_c}$; $t_c = \frac{1}{k_2-k_1}\ln\left[\frac{k_2}{k_1}\left(1 - \frac{D_0(k_2-k_1)}{k_1 L_0}\right)\right]$.

**Calculation:**
- $t_c = \frac{1}{0.2}\ln\left[\frac{0.5}{0.3}\left(1 - \frac{2 \times 0.2}{0.3 \times 200}\right)\right] = 5\ln\left[1.667(1 - 0.0067)\right] = 5\ln(1.656) = 5 \times 0.504 = 2.52$ days
- $D_c = \frac{0.3 \times 200}{0.5} e^{-0.3 \times 2.52} = 120 \times e^{-0.756} = 120 \times 0.47 = 56.4$ mg/L

**Answer:** $D_c = 56.4$ mg/L at $t_c = 2.52$ days

**Trap:** The critical deficit occurs where deoxygenation = reaeration rate.

---

## Problem 4: Sedimentation — Overflow Rate

**Given:** Tank, $Q = 1000$ m³/day, surface area $A = 50$ m².

**Find:** Surface loading (overflow) rate.

**Method:** $v_s = Q/A$.

**Calculation:**
- $v_s = 1000/50 = 20$ m³/m²/day = 20 m/day

**Answer:** $v_s = 20$ m/day

**Trap:** Overflow rate = flow per unit surface area — governs particle removal.

---

## Problem 5: Stokes' Law Settling Velocity

**Given:** Particle $d = 0.1$ mm, $\rho_s = 2650$ kg/m³, $\rho_w = 1000$ kg/m³, $\mu = 1 \times 10^{-3}$ Pa·s.

**Find:** Settling velocity.

**Method:** $v_s = \frac{g(\rho_s - \rho_w)d^2}{18\mu}$.

**Calculation:**
- $v_s = \frac{9.81 \times (2650 - 1000) \times (0.1 \times 10^{-3})^2}{18 \times 1 \times 10^{-3}} = \frac{9.81 \times 1650 \times 1 \times 10^{-8}}{0.018} = \frac{1.619 \times 10^{-4}}{0.018} = 8.99 \times 10^{-3}$ m/s = 8.99 mm/s

**Answer:** $v_s = 9.0$ mm/s

**Trap:** Stokes' law valid for laminar flow (small particles, low Re).

---

## Problem 6: F/M Ratio

**Given:** $Q = 1000$ m³/day, $S_0 = 200$ mg/L, $V = 400$ m³, $X = 2500$ mg/L.

**Find:** F/M ratio.

**Method:** $F/M = \frac{Q \cdot S_0}{V \cdot X}$.

**Calculation:**
- $F/M = \frac{1000 \times 200}{400 \times 2500} = \frac{200,000}{1,000,000} = 0.2$ /day

**Answer:** F/M = 0.2/day (conventional ASP range 0.2–0.6)

**Trap:** Units must be consistent — both $S_0$ and $X$ in mg/L.

---

## Problem 7: Aeration Tank Volume

**Given:** $Q = 1000$ m³/day, $S_0 = 200$ mg/L, $X = 2500$ mg/L, F/M = 0.3/day.

**Find:** Aeration tank volume.

**Method:** $V = \frac{Q \cdot S_0}{F/M \cdot X}$.

**Calculation:**
- $V = \frac{1000 \times 200}{0.3 \times 2500} = \frac{200,000}{750} = 267$ m³

**Answer:** $V = 267$ m³

**Trap:** F/M is the design parameter — higher F/M = smaller tank but lower treatment efficiency.

---

## Problem 8: BOD Removal Efficiency

**Given:** Influent BOD $S_0 = 250$ mg/L, effluent BOD $S_e = 20$ mg/L.

**Find:** BOD removal efficiency.

**Method:** $\eta = \frac{S_0 - S_e}{S_0} \times 100\%$.

**Calculation:**
- $\eta = \frac{250 - 20}{250} \times 100 = \frac{230}{250} \times 100 = 92\%$

**Answer:** $\eta = 92\%$

**Trap:** Secondary treatment targets 85–95% BOD removal.

---

## Problem 9: Chlorination Dose

**Given:** Applied chlorine = 2.5 mg/L, free chlorine residual = 0.5 mg/L.

**Find:** Chlorine demand.

**Method:** Chlorine demand = Applied − Free residual.

**Calculation:**
- Demand = 2.5 − 0.5 = 2.0 mg/L

**Answer:** Chlorine demand = 2.0 mg/L

**Trap:** Breakpoint chlorination: demand must be satisfied before free residual appears.

---

## Problem 10: Sludge Production

**Given:** Flow 1000 m³/day, SS removed 150 mg/L, sludge solids content 4%.

**Find:** Sludge volume.

**Method:** Mass = flow × concentration; Volume = mass / (density × solids fraction).

**Calculation:**
- Mass = $1000 \times 150 \times 10^{-3}$ kg/day = 150 kg/day
- Volume = $\frac{150}{1000 \times 0.04} = \frac{150}{40} = 3.75$ m³/day

**Answer:** Sludge volume = 3.75 m³/day

**Trap:** Convert mg/L to kg/m³ (1 mg/L = 1 g/m³ = 0.001 kg/m³).

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | BOD₅ = 225 mg/L |
| 2 | $L_5 = 95$ mg/L |
| 3 | $D_c = 56.4$ mg/L at $t_c = 2.52$ days |
| 4 | $v_s = 20$ m/day |
| 5 | $v_s = 9.0$ mm/s |
| 6 | F/M = 0.2/day |
| 7 | $V = 267$ m³ |
| 8 | $\eta = 92\%$ |
| 9 | Chlorine demand = 2.0 mg/L |
| 10 | Sludge = 3.75 m³/day |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| BOD kinetics | 1, 2 | Can you compute BOD₅ and remaining BOD? |
| DO sag curve | 3 | Can you find critical deficit? |
| Sedimentation | 4, 5 | Can you compute overflow rate and settling velocity? |
| Activated sludge | 6, 7, 8 | Can you compute F/M, volume, efficiency? |
| Disinfection | 9 | Can you compute chlorine demand? |
| Sludge | 10 | Can you compute sludge volume? |

---

## Practice Strategy

1. **Solve Problems 1–3** (BOD + DO sag) — the most frequently tested.
2. **Solve Problems 4–8** (sedimentation + ASP) — critical for design roles.
3. **Solve Problems 9–10** (chlorination + sludge) — for PSU/consulting.
4. Then take the [`TEST.md`](TEST.md) to verify mastery.
# Infrastructure Engineering & Management — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for PM/consulting roles (L&T, AECOM, Tata Projects, NHAI, IRCON, NBCC)
> **Canonical Study:** [`infrastructure-engineering-management.md`](infrastructure-engineering-management.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: Critical Path Method (CPM)

**Given:** Activities: A (5 days), B (3 days, after A), C (4 days, after A), D (2 days, after B and C).

**Find:** Critical path and project duration.

**Method:** Forward pass (ES, EF) and backward pass (LS, LF); critical path = zero float.

**Calculation:**
- A: ES=0, EF=5
- B: ES=5, EF=8
- C: ES=5, EF=9
- D: ES=max(8,9)=9, EF=11
- Critical path: A → C → D (5 + 4 + 2 = 11 days)

**Answer:** Project duration = 11 days; critical path A → C → D

**Trap:** The critical path is the longest path — B has 1 day float.

---

## Problem 2: Total Float

**Given:** Activity with ES = 3, EF = 8, LS = 5, LF = 10.

**Find:** Total float.

**Method:** $TF = LS - ES = LF - EF$.

**Calculation:**
- $TF = 5 - 3 = 2$ days (or $10 - 8 = 2$)

**Answer:** Total float = 2 days

**Trap:** Free float = min(ES of successors) − EF; total float ≥ free float.

---

## Problem 3: PERT Expected Time

**Given:** $t_o = 4$ days, $t_m = 6$ days, $t_p = 14$ days.

**Find:** Expected time and variance.

**Method:** $t_e = \frac{t_o + 4t_m + t_p}{6}$; $\sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$.

**Calculation:**
- $t_e = \frac{4 + 4 \times 6 + 14}{6} = \frac{42}{6} = 7$ days
- $\sigma^2 = \left(\frac{14 - 4}{6}\right)^2 = \left(\frac{10}{6}\right)^2 = 2.78$

**Answer:** $t_e = 7$ days, $\sigma^2 = 2.78$

**Trap:** PERT weights the most likely time by 4.

---

## Problem 4: Project Completion Probability

**Given:** Expected duration $T_e = 30$ days, scheduled $T_s = 33$ days, $\sum\sigma^2 = 4$ on critical path.

**Find:** Probability of completing by day 33.

**Method:** $Z = \frac{T_s - T_e}{\sqrt{\sum\sigma^2}}$.

**Calculation:**
- $Z = \frac{33 - 30}{\sqrt{4}} = \frac{3}{2} = 1.5$
- From standard normal table: $P(Z < 1.5) = 0.933$

**Answer:** 93.3% probability

**Trap:** $Z$ uses the square root of the summed variance.

---

## Problem 5: NPV Calculation

**Given:** Initial investment $C_0 = 1000$ lakh, annual cash flow 300 lakh for 5 years, discount rate 10%.

**Find:** NPV.

**Method:** $NPV = -C_0 + \sum_{t=1}^{n}\frac{CF_t}{(1+r)^t}$.

**Calculation:**
- PV of annuity: $300 \times \frac{1 - (1.1)^{-5}}{0.1} = 300 \times 3.791 = 1137.3$
- $NPV = -1000 + 1137.3 = 137.3$ lakh

**Answer:** NPV = 137.3 lakh (positive → accept)

**Trap:** NPV > 0 means the project is financially viable.

---

## Problem 6: Benefit-Cost Ratio

**Given:** PV of benefits = 1500 lakh, PV of costs = 1200 lakh.

**Find:** BCR.

**Method:** $BCR = \frac{\text{PV of Benefits}}{\text{PV of Costs}}$.

**Calculation:**
- $BCR = \frac{1500}{1200} = 1.25$

**Answer:** BCR = 1.25 (> 1 → accept)

**Trap:** BCR > 1 indicates benefits exceed costs.

---

## Problem 7: DSCR

**Given:** Net operating income = 150 lakh/year, debt service = 100 lakh/year.

**Find:** DSCR.

**Method:** $DSCR = \frac{\text{Net Operating Income}}{\text{Debt Service}}$.

**Calculation:**
- $DSCR = \frac{150}{100} = 1.5$

**Answer:** DSCR = 1.5 (> 1.2 → viable)

**Trap:** Lenders require DSCR > 1.2 for project viability.

---

## Problem 8: Plinth Area Estimate

**Given:** Plinth area 500 m², rate ₹20,000/m².

**Find:** Estimated cost.

**Method:** Estimated Cost = Plinth Area × Rate.

**Calculation:**
- Cost = $500 \times 20,000 = ₹1,00,00,000$ (₹1 crore)

**Answer:** ₹1 crore

**Trap:** Plinth area estimate accuracy is ±15–20% (preliminary).

---

## Problem 9: Contingency

**Given:** Estimated cost = ₹10 crore.

**Find:** Contingency (CPWD norms).

**Method:** Contingency = 3–5% × Estimated Cost.

**Calculation:**
- Contingency = $0.04 \times 10 = ₹0.4$ crore (using 4%)

**Answer:** ₹0.4 crore (₹40 lakh)

**Trap:** CPWD contingency is 3–5% of estimated cost.

---

## Problem 10: Relative Compaction

**Given:** Field dry density 17.5 kN/m³, max dry density 18.0 kN/m³.

**Find:** Relative compaction.

**Method:** $RC = \frac{\gamma_{d,field}}{\gamma_{d,max}} \times 100\%$.

**Calculation:**
- $RC = \frac{17.5}{18.0} \times 100 = 97.2\%$

**Answer:** RC = 97.2% (≥ 95% Modified Proctor ✓)

**Trap:** Typical spec: ≥ 95% Modified Proctor or ≥ 98% Standard Proctor.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | 11 days; A → C → D |
| 2 | Total float = 2 days |
| 3 | $t_e = 7$ days, $\sigma^2 = 2.78$ |
| 4 | 93.3% |
| 5 | NPV = 137.3 lakh |
| 6 | BCR = 1.25 |
| 7 | DSCR = 1.5 |
| 8 | ₹1 crore |
| 9 | ₹0.4 crore |
| 10 | RC = 97.2% |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| CPM | 1, 2 | Can you find critical path and float? |
| PERT | 3, 4 | Can you compute expected time and probability? |
| Finance | 5, 6, 7 | Can you compute NPV, BCR, DSCR? |
| Estimation | 8, 9 | Can you compute plinth area and contingency? |
| Construction | 10 | Can you check compaction? |

---

## Practice Strategy

1. **Solve Problems 1–4** (CPM + PERT) — the most frequently tested.
2. **Solve Problems 5–7** (finance) — critical for PM roles.
3. **Solve Problems 8–10** (estimation + construction) — for consulting.
4. Then take the [`TEST.md`](TEST.md) to verify mastery.
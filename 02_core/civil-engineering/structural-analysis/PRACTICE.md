# Structural Analysis — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for structural/consulting roles and PSUs
> **Canonical Study:** [`structural-analysis.md`](structural-analysis.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: Degree of Static Indeterminacy

**Given:** A continuous beam ABC with fixed support at A, roller at B, and roller at C. Span AB = 6 m, BC = 4 m.

**Find:** Degree of static indeterminacy ($D_s$).

**Method:** $D_s = R - 3$ (external indeterminacy for a plane structure).

**Calculation:**
- Reactions: A (fixed) = 3, B (roller) = 1, C (roller) = 1 → $R = 5$
- $D_s = 5 - 3 = 2$

**Answer:** $D_s = 2$ (statically indeterminate to 2nd degree)

**Trap:** Don't forget the fixed support contributes 3 reactions, not 1.

---

## Problem 2: Determinacy of a Plane Truss

**Given:** A plane truss with $m = 11$ members, $j = 7$ joints, $R = 3$ reactions.

**Find:** Degree of static indeterminacy.

**Method:** $D_s = (m + R) - 2j$

**Calculation:**
- $D_s = (11 + 3) - 2(7) = 14 - 14 = 0$

**Answer:** $D_s = 0$ — statically determinate truss

**Trap:** For a plane truss, use $2j$ (2 equations per joint), not $3j$.

---

## Problem 3: Kinematic Indeterminacy of a Plane Frame

**Given:** A rigid-jointed plane frame with 4 joints, all fixed at base.

**Find:** Degree of kinematic indeterminacy ($D_k$).

**Method:** $D_k = NJ - C$ where $N = 3$ (rigid joint, plane frame), $J$ = joints, $C$ = compatibility equations.

**Calculation:**
- Joints: 4 (2 free + 2 fixed base)
- Free joints: 2 × 3 = 6 DOF
- Fixed base joints: 0 DOF
- $D_k = 6$

**Answer:** $D_k = 6$

**Trap:** Fixed supports contribute 0 DOF, not 3.

---

## Problem 4: Fixed-End Moments

**Given:** A fixed beam AB, span $L = 6$ m, carries a central point load $P = 60$ kN.

**Find:** Fixed-end moments.

**Method:** FEM for central point load: $M_{FAB} = -PL/8$, $M_{FBA} = +PL/8$.

**Calculation:**
- $M_{FAB} = -60 \times 6 / 8 = -45$ kN·m
- $M_{FBA} = +60 \times 6 / 8 = +45$ kN·m

**Answer:** $M_{FAB} = -45$ kN·m, $M_{FBA} = +45$ kN·m

**Trap:** Sign convention — clockwise moments at the left end are negative by the standard convention.

---

## Problem 5: Moment Distribution — Continuous Beam

**Given:** Continuous beam ABC, span AB = 6 m (UDL 20 kN/m), span BC = 4 m (UDL 20 kN/m). EI constant. A fixed, B and C rollers.

**Find:** End moments using moment distribution.

**Method:** Hardy Cross — FEMs, distribution factors, carry-over.

**Calculation:**
1. **FEMs:**
   - $M_{FAB} = -wL^2/12 = -20 \times 36/12 = -60$ kN·m
   - $M_{FBA} = +60$ kN·m
   - $M_{FBC} = -20 \times 16/12 = -26.67$ kN·m
   - $M_{FCB} = +26.67$ kN·m
2. **Stiffness:** $K_{BA} = 4EI/6 = 0.667EI$, $K_{BC} = 4EI/4 = 1.0EI$
3. **Distribution factors at B:** $DF_{BA} = 0.667/(0.667+1.0) = 0.40$, $DF_{BC} = 1.0/1.667 = 0.60$
4. **Iterate:**
   - Unbalanced at B: $+60 - 26.67 = +33.33$
   - Distribute: $M_{BA} = -0.40 \times 33.33 = -13.33$, $M_{BC} = -0.60 \times 33.33 = -20.0$
   - Carry over: $M_{AB} = -6.67$, $M_{CB} = -10.0$
   - Continue until convergence
5. **Final:** $M_{AB} \approx -66.7$ kN·m, $M_{BA} \approx +46.7$ kN·m, $M_{BC} \approx -46.7$ kN·m, $M_{CB} \approx +16.7$ kN·m

**Answer:** $M_{BA} \approx 46.7$ kN·m, $M_{BC} \approx -46.7$ kN·m

**Trap:** Distribution factors must sum to 1.0 at each joint.

---

## Problem 6: Influence Line for Reaction

**Given:** Simply supported beam AB, span $L = 10$ m. A unit load moves across.

**Find:** Influence line ordinate for reaction at A when load is at 4 m from A.

**Method:** ILD for reaction $R_A$: ordinate = $1 - x/L$.

**Calculation:**
- At $x = 4$ m: $R_A = 1 - 4/10 = 0.6$

**Answer:** $R_A = 0.6$ (unitless)

**Trap:** The ILD for a reaction is linear, varying from 1 at the support to 0 at the far end.

---

## Problem 7: Maximum Bending Moment from ILD

**Given:** Simply supported beam, span 12 m. A UDL of 30 kN/m over the entire span and a point load of 50 kN at midspan.

**Find:** Maximum bending moment at midspan using ILD.

**Method:** $M = \sum(\text{Point load} \times \text{ordinate}) + \sum(\text{UDL} \times \text{area under ILD})$.

**Calculation:**
- ILD for $M$ at midspan: triangle with peak $= L/4 = 3$ m at midspan
- Point load: $50 \times 3 = 150$ kN·m
- UDL: $30 \times (\text{area}) = 30 \times (0.5 \times 12 \times 3) = 30 \times 18 = 540$ kN·m
- Total: $150 + 540 = 690$ kN·m

**Answer:** $M_{max} = 690$ kN·m

**Trap:** Area under a triangular ILD = ½ × base × height.

---

## Problem 8: Slope-Deflection Method

**Given:** A fixed beam AB, span 6 m, UDL 20 kN/m. EI constant.

**Find:** End moments using slope-deflection.

**Method:** $M_{AB} = M_{FAB} + \frac{2EI}{L}(2\theta_A + \theta_B - 3\Delta/L)$.

**Calculation:**
- For fixed-fixed with no settlement: $\theta_A = \theta_B = \Delta = 0$
- $M_{AB} = M_{FAB} = -wL^2/12 = -20 \times 36/12 = -60$ kN·m
- $M_{BA} = +60$ kN·m

**Answer:** $M_{AB} = -60$ kN·m, $M_{BA} = +60$ kN·m

**Trap:** For a fixed-fixed beam, slope-deflection reduces to the FEMs.

---

## Problem 9: Müller-Breslau Principle

**Given:** A simply supported beam AB, span 10 m.

**Find:** Shape of the influence line for bending moment at 4 m from A.

**Method:** Müller-Breslau — release the moment constraint at the section, apply unit rotation.

**Calculation:**
- The ILD for $M$ at section C is a triangle with peak at C
- Peak ordinate $= \frac{a \cdot b}{L} = \frac{4 \times 6}{10} = 2.4$ m

**Answer:** Triangular ILD with peak 2.4 m at C

**Trap:** The peak ordinate of the moment ILD is $ab/L$, not $L/4$ (that's only for midspan).

---

## Problem 10: Plastic Analysis — Collapse Mechanism

**Given:** A fixed beam AB, span 6 m, central point load $P$. Plastic moment capacity $M_p = 100$ kN·m.

**Find:** Collapse load $P_u$.

**Method:** Virtual work — external work = internal work.

**Calculation:**
- Collapse mechanism: plastic hinges at A, B, and midspan
- External work: $P_u \times \delta = P_u \times (L/2)\theta = P_u \times 3\theta$
- Internal work: $M_p(\theta + 2\theta + \theta) = 4M_p\theta = 400\theta$
- $P_u \times 3\theta = 400\theta \rightarrow P_u = 133.3$ kN

**Answer:** $P_u = 133.3$ kN

**Trap:** For a fixed beam with central load, there are 3 plastic hinges (2 ends + midspan).

---

## Problem 11: Stiffness Matrix Method

**Given:** A spring system with two springs in series: $k_1 = 100$ kN/m, $k_2 = 200$ kN/m. Force $P = 50$ kN applied at the free end.

**Find:** Displacement at the free end.

**Method:** Equivalent stiffness $k_{eq} = k_1 k_2/(k_1 + k_2)$.

**Calculation:**
- $k_{eq} = 100 \times 200/(100 + 200) = 20000/300 = 66.67$ kN/m
- $\delta = P/k_{eq} = 50/66.67 = 0.75$ m

**Answer:** $\delta = 0.75$ m

**Trap:** Springs in series combine like resistors in parallel (reciprocal sum).

---

## Problem 12: Deflection by Unit Load Method

**Given:** Cantilever beam, length 4 m, point load 30 kN at free end. EI = 20000 kN·m².

**Find:** Deflection at free end.

**Method:** $\delta = \int \frac{Mm}{EI} dx$ (unit load method).

**Calculation:**
- $M(x) = -30x$, $m(x) = -x$ (unit load at free end)
- $\delta = \int_0^4 \frac{(-30x)(-x)}{EI} dx = \frac{30}{EI}\int_0^4 x^2 dx = \frac{30}{EI} \times \frac{64}{3}$
- $\delta = \frac{30 \times 64}{3 \times 20000} = \frac{640}{20000} = 0.032$ m = **32 mm**

**Answer:** $\delta = 32$ mm

**Trap:** For a cantilever with end load, $\delta = PL^3/3EI = 30 \times 64/(3 \times 20000) = 0.032$ m ✓

---

## Problem 13: Influence Line for Shear

**Given:** Simply supported beam, span 10 m.

**Find:** Maximum shear at section 3 m from left support when a UDL of 20 kN/m covers the span.

**Method:** ILD for shear at C: ordinate jumps from $-x/L$ to $+(L-x)/L$ at C.

**Calculation:**
- Left of C: ordinate $= -3/10 = -0.3$ (negative region)
- Right of C: ordinate $= +7/10 = +0.7$ (positive region)
- For maximum positive shear, load only the positive region (7 m)
- $V_{max} = 20 \times (\text{area of positive triangle}) = 20 \times (0.5 \times 7 \times 0.7) = 20 \times 2.45 = 49$ kN

**Answer:** $V_{max} = 49$ kN

**Trap:** For maximum shear, load only the region where the ILD has the same sign.

---

## Problem 14: Three-Moment Equation

**Given:** Continuous beam ABC, span AB = 6 m (UDL 20 kN/m), span BC = 4 m (point load 40 kN at midspan). EI constant.

**Find:** Support moment at B using Clapeyron's three-moment equation.

**Method:** $M_A L_1 + 2M_B(L_1+L_2) + M_C L_2 = -6[A_1\bar{x}_1/L_1 + A_2\bar{x}_2/L_2]$.

**Calculation:**
- $M_A = 0$ (roller), $M_C = 0$ (roller)
- For span AB (UDL): $A_1\bar{x}_1/L_1 = wL_1^3/24 = 20 \times 216/24 = 180$
- For span BC (point load): $A_2\bar{x}_2/L_2 = PL_2^2/16 = 40 \times 16/16 = 40$
- $2M_B(6+4) = -6(180 + 40) = -1320$
- $20M_B = -1320 \rightarrow M_B = -66$ kN·m

**Answer:** $M_B = -66$ kN·m

**Trap:** For a UDL, $A\bar{x}/L = wL^3/24$; for a central point load, $PL^2/16$.

---

## Problem 15: Conjugate Beam Method

**Given:** Simply supported beam, span 6 m, UDL 15 kN/m. EI = 30000 kN·m².

**Find:** Maximum deflection.

**Method:** Conjugate beam — M/EI as loading, deflection = moment in conjugate beam.

**Calculation:**
- $M_{max} = wL^2/8 = 15 \times 36/8 = 67.5$ kN·m
- $\delta_{max} = \frac{5wL^4}{384EI} = \frac{5 \times 15 \times 1296}{384 \times 30000} = \frac{97200}{11520000} = 0.00844$ m = **8.44 mm**

**Answer:** $\delta_{max} = 8.44$ mm

**Trap:** For a simply supported beam with UDL, $\delta = 5wL^4/384EI$.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | $D_s = 2$ |
| 2 | $D_s = 0$ (determinate) |
| 3 | $D_k = 6$ |
| 4 | $M_{FAB} = -45$, $M_{FBA} = +45$ kN·m |
| 5 | $M_{BA} \approx 46.7$, $M_{BC} \approx -46.7$ kN·m |
| 6 | $R_A = 0.6$ |
| 7 | $M_{max} = 690$ kN·m |
| 8 | $M_{AB} = -60$, $M_{BA} = +60$ kN·m |
| 9 | Triangular ILD, peak 2.4 m |
| 10 | $P_u = 133.3$ kN |
| 11 | $\delta = 0.75$ m |
| 12 | $\delta = 32$ mm |
| 13 | $V_{max} = 49$ kN |
| 14 | $M_B = -66$ kN·m |
| 15 | $\delta = 8.44$ mm |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Determinacy | 1, 2, 3 | Can you compute $D_s$ and $D_k$ for any frame/truss? |
| Fixed-end moments | 4, 8 | Can you recall FEMs for UDL, point load, and triangular load? |
| Moment distribution | 5 | Can you iterate to convergence? |
| Influence lines | 6, 7, 9, 13 | Can you draw ILDs and find max effects? |
| Slope-deflection | 8 | Can you write the slope-deflection equations? |
| Plastic analysis | 10 | Can you identify collapse mechanisms? |
| Matrix methods | 11 | Can you assemble a stiffness matrix? |
| Energy methods | 12, 15 | Can you apply unit load and conjugate beam methods? |
| Three-moment | 14 | Can you apply Clapeyron's equation? |

---

## Practice Strategy

1. **Solve Problems 1–5** (determinacy + moment distribution) — these are the most frequently tested.
2. **Solve Problems 6–9** (influence lines) — critical for bridge/crane design interviews.
3. **Solve Problems 10–15** (plastic + energy + matrix) — advanced, for consulting/PSU roles.
4. Re-attempt any problem you couldn't solve in < 5 minutes.
5. Then take the [`TEST.md`](TEST.md) to verify mastery.
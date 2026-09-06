# Structural Analysis — Topic Test

> **Placement Priority:** P0 — Required for structural/consulting roles and PSUs
> **Canonical Study:** [`structural-analysis.md`](structural-analysis.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md)
> **Time:** 45 minutes · **Marks:** 50 (2 marks each)

---

## Section A — Determinacy & Kinematics (Q1–Q5)

**Q1.** A plane truss has 15 members, 9 joints, and 3 reactions. The degree of static indeterminacy is:
- (a) 0
- (b) 1
- (c) 2
- (d) 3

**Q2.** A rigid-jointed plane frame has 6 joints (2 fixed at base, 4 free). The degree of kinematic indeterminacy is:
- (a) 6
- (b) 12
- (c) 18
- (d) 24

**Q3.** Which of the following is statically determinate?
- (a) Simply supported beam
- (b) Fixed beam
- (c) Continuous beam
- (d) Propped cantilever

**Q4.** The degree of static indeterminacy of a fixed beam is:
- (a) 0
- (b) 1
- (c) 2
- (d) 3

**Q5.** For a plane frame, the number of equilibrium equations available per joint is:
- (a) 2
- (b) 3
- (c) 6
- (d) 1

---

## Section B — Fixed-End Moments & Moment Distribution (Q6–Q9)

**Q6.** The fixed-end moment at the left end of a fixed beam (span L) carrying a central point load P is:
- (a) $-PL/8$
- (b) $+PL/8$
- (c) $-PL/12$
- (d) $-PL/4$

**Q7.** A fixed beam (span 6 m) carries a UDL of 20 kN/m. The fixed-end moment at each end is:
- (a) $\pm 40$ kN·m
- (b) $\pm 60$ kN·m
- (c) $\pm 90$ kN·m
- (d) $\pm 120$ kN·m

**Q8.** In moment distribution, the carry-over factor from a fixed far end is:
- (a) 0
- (b) +1/2
- (c) +1
- (d) -1

**Q9.** The stiffness of a member with a fixed far end is:
- (a) $EI/L$
- (b) $3EI/L$
- (c) $4EI/L$
- (d) $2EI/L$

---

## Section C — Influence Lines (Q10–Q12)

**Q10.** The influence line for the reaction at a support of a simply supported beam is:
- (a) A parabola
- (b) A straight line from 1 to 0
- (c) A triangle
- (d) A sine curve

**Q11.** The peak ordinate of the influence line for bending moment at midspan of a simply supported beam (span L) is:
- (a) $L/2$
- (b) $L/4$
- (c) $L/8$
- (d) $L$

**Q12.** For maximum bending moment at a section under a moving UDL, the load should be placed:
- (a) Over the entire span
- (b) Only where the ILD is positive
- (c) Only where the ILD is negative
- (d) At the section

---

## Section D — Energy & Plastic Methods (Q13–Q15)

**Q13.** The deflection of a cantilever (length L, EI) under a point load P at the free end is:
- (a) $PL^3/3EI$
- (b) $PL^3/8EI$
- (c) $PL^3/48EI$
- (d) $5PL^3/384EI$

**Q14.** A fixed beam (span L) with a central point load collapses when plastic hinges form at:
- (a) 1 location
- (b) 2 locations
- (c) 3 locations
- (d) 4 locations

**Q15.** The collapse load of a simply supported beam (span L, plastic moment $M_p$) with a central point load is:
- (a) $2M_p/L$
- (b) $4M_p/L$
- (c) $8M_p/L$
- (d) $16M_p/L$

---

## 📋 Answer Key

| Q | Answer | Explanation |
|:-:|:------:|-------------|
| 1 | (a) | $D_s = (15+3) - 2(9) = 0$ |
| 2 | (b) | $D_k = 4 \times 3 = 12$ (4 free joints × 3 DOF) |
| 3 | (a) | Simply supported beam: $R = 3$, $D_s = 0$ |
| 4 | (c) | Fixed beam: $R = 6$, $D_s = 6 - 3 = 3$ |
| 5 | (b) | Plane frame: 3 equations ($\sum F_x, \sum F_y, \sum M$) |
| 6 | (a) | FEM for central point load = $-PL/8$ |
| 7 | (b) | $wL^2/12 = 20 \times 36/12 = 60$ kN·m |
| 8 | (b) | COF = +1/2 for fixed far end |
| 9 | (c) | $K = 4EI/L$ for fixed far end |
| 10 | (b) | Reaction ILD is linear (1 → 0) |
| 11 | (b) | Peak = $L/4$ at midspan |
| 12 | (b) | Load only the positive region of the ILD |
| 13 | (a) | $\delta = PL^3/3EI$ |
| 14 | (c) | 3 hinges (2 ends + midspan) |
| 15 | (b) | $P_u = 4M_p/L$ (virtual work: $P\delta = M_p(2\theta)$) |

---

## Scoring Guide

| Score | Rating | Action |
|:-----:|--------|--------|
| 45–50 | 🏆 Excellent | Placement-ready — move to interview prep |
| 35–44 | ✅ Good | Review missed topics, re-attempt |
| 25–34 | ⚠️ Fair | Re-study [`structural-analysis.md`](structural-analysis.md) + [`PRACTICE.md`](PRACTICE.md) |
| < 25 | ❌ Weak | Full re-study of determinacy + moment distribution + ILD |

---

## Topic Diagnosis

| Topic | Questions | If Wrong, Study |
|-------|:---------:|-----------------|
| Determinacy | 1, 2, 3, 4, 5 | §2 Determinacy & Indeterminacy |
| Fixed-end moments | 6, 7 | §4 Moment Distribution |
| Moment distribution | 8, 9 | §4 Moment Distribution |
| Influence lines | 10, 11, 12 | §3 Influence Line Diagrams |
| Energy methods | 13 | §5 Deflection Methods |
| Plastic analysis | 14, 15 | §6 Plastic Analysis |

---

## Post-Test Protocol

1. **Score yourself** honestly (no partial credit).
2. **Log errors** in the [`ERROR_ANALYSIS.md`](../gate/ERROR_ANALYSIS.md) format (category, cause, fix).
3. **Re-attempt** all wrong questions in 24 hours.
4. **Move to interview prep** — [`INTERVIEW.md`](INTERVIEW.md) — once you score ≥ 35.
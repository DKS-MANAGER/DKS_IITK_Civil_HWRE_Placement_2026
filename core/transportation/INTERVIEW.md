# Transportation Engineering — Interview Questions & Answers

> **Placement Priority:** P0 — Required for PSU roles (NHAI, IRCON, Airport Authority, Railways)
> **Canonical Study:** [`transportation-engineering.md`](transportation-engineering.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 15 questions across 6 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is stopping sight distance?**
   - The distance required for a driver to see an object, react, and brake to a stop: $SSD = 0.278Vt + V^2/(254f)$.

2. **What is superelevation?**
   - The inward transverse slope provided on horizontal curves to counteract centrifugal force: $e + f = V^2/(127R)$.

3. **What is the Greenshields model?**
   - Linear speed-density relationship: $v = v_f(1 - k/k_j)$; gives parabolic flow-density curve with $q_{max} = v_f k_j/4$.

4. **What is PCU?**
   - Passenger Car Unit: a factor converting mixed traffic to equivalent car units (car 1.0, bus/truck 3.0, two-wheeler 0.5).

5. **What is the difference between flexible and rigid pavements?**
   - Flexible: layered bituminous, load spread by layer stiffness, designed by CBR method. Rigid: concrete slab, load spread by slab action, designed by Westergaard.

---

## B. WHY Questions

1. **Why is superelevation limited to 0.07?**
   - To prevent vehicles from sliding down on the inside of the curve at low speeds and to avoid discomfort for slow vehicles.

2. **Why is the 85th percentile speed used for speed limits?**
   - It represents the speed below which 85% of drivers travel — the speed most drivers find safe and comfortable.

3. **Why use dowel bars in rigid pavement joints?**
   - To transfer load across joints without restricting joint opening (thermal movement).

4. **Why is CBR used for flexible pavement design?**
   - CBR measures subgrade strength; pavement thickness is inversely related to CBR — stronger subgrade needs thinner pavement.

---

## C. WHAT-IF Questions

1. **What if the computed superelevation exceeds 0.07?**
   - Limit $e$ to 0.07 and reduce speed by providing a transition curve or warning signs.

2. **What if $\sum Y_i > 1$ in signal design?**
   - The intersection is oversaturated — cycle length formula fails; need geometric improvements or signal coordination.

3. **What if the subgrade CBR is very low (< 2%)?**
   - Need a thick pavement or subgrade improvement (stabilization, geotextiles).

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Flexible | Rigid pavement | Layered vs slab action |
| SSD | OSD | Stopping vs overtaking |
| Time mean speed | Space mean speed | Arithmetic vs harmonic mean |
| Summit curve | Valley curve | Sight distance vs comfort |
| Bearing bolt | HSFG bolt | Bearing vs friction |

---

## E. Numerical Questions

1. **Find SSD** for $V = 80$ km/h, $t = 2.5$ s, $f = 0.35$. → 128 m
2. **Find $R_{min}$** for $V = 80$, $e = 0.07$, $f = 0.15$. → 229 m
3. **Find $q_{max}$** for $v_f = 80$, $k_j = 120$. → 2400 veh/hr
4. **Find $C_o$** for $L = 12$, $Y = 0.55$. → 51 s

---

## F. Rapid-Fire Questions

1. Reaction time (IRC)? → 2.5 s
2. Max superelevation? → 0.07
3. $q = ?$ → $k \cdot v$
4. $q_{max} = ?$ → $v_f k_j/4$
5. PCU bus/truck? → 3.0
6. CBR design code? → IRC:37
7. Rigid pavement code? → IRC:58
8. 85th percentile used for? → Speed limits

---

## High-Value Interview Answers

### High-Value Q1: "How do you design a horizontal curve?"

**30-second answer:**
"First, determine the minimum radius from the design speed: $R_{min} = V^2/(127(e+f))$. Then compute the required superelevation $e = V^2/(127R) - f$, capped at 0.07. Provide a transition curve for the superelevation runoff, check sight distance, and verify the curve provides adequate SSD."

### High-Value Q2: "What is the difference between flexible and rigid pavements?"

**30-second answer:**
"Flexible pavements are layered — surface, binder, base, sub-base over subgrade — and spread load by layer stiffness; designed by the CBR method (IRC:37). Rigid pavements are a concrete slab that spreads load by slab action (flexural strength); designed by Westergaard's analysis (IRC:58). Rigid pavements have higher initial cost but lower maintenance."

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`transportation-engineering.md`](transportation-engineering.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Geotechnical | [`../geotechnical/geotechnical.md`](../geotechnical/geotechnical.md) |
| Infrastructure | [`../infrastructure/infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) |
| Geoinformatics | [`../geoinformatics/geoinformatics.md`](../geoinformatics/geoinformatics.md) |
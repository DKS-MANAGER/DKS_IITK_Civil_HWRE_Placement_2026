# Geotechnical Engineering — Interview Questions & Answers

> **Placement Priority:** P0 — Required for foundation/geotech roles and PSUs
> **Canonical Study:** [`geotechnical.md`](geotechnical.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 15 questions across 6 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is effective stress?**
   - $\sigma' = \sigma - u$. Soil strength and deformation depend on inter-particle contact forces (effective stress), not total stress.

2. **What is the difference between normally consolidated and overconsolidated clay?**
   - NC: current effective stress = max past stress. OC: current stress < max past stress. OC clay has higher strength, lower compressibility.

3. **What are bearing capacity factors?**
   - $N_c$, $N_q$, $N_\gamma$: dimensionless factors depending on $\phi$. Represent cohesion, overburden, and self-weight contributions to bearing capacity.

4. **What is the Mohr-Coulomb failure criterion?**
   - $\tau_f = c' + \sigma'\tan\phi'$. Defines the shear strength of soil at failure.

5. **What is the difference between drained and undrained conditions?**
   - Drained: pore water pressure dissipates (slow loading). Undrained: pore pressure does not dissipate (rapid loading).

---

## B. WHY Questions

1. **Why does consolidation take time in clay?**
   - Water must drain out of low-permeability clay; rate governed by $c_v = k/(m_v\gamma_w)$. Sand settles immediately.

2. **Why is effective stress used instead of total stress?**
   - Because soil strength depends on inter-particle contact forces, not on pore water pressure.

3. **Why is the Terzaghi equation modified with shape factors?**
   - Original equation is for strip foundations; real foundations have 3D effects (corners, edges).

4. **Why are pile foundations used instead of shallow foundations?**
   - When soil near the surface is too weak to support the load, piles transfer load to deeper, stronger strata via skin friction and end bearing.

---

## C. WHAT-IF Questions

1. **What if the water table rises?**
   - Effective stress decreases (buoyancy), bearing capacity reduces, settlement may increase. Need to check worst-case water table.

2. **What if a clay is very soft ($c_u < 25$ kPa)?**
   - Bearing capacity very low; may need pile foundations, ground improvement, or deep soil mixing.

3. **What if the factor of safety for bearing capacity is below 3?**
   - Increase footing size or depth; alternative: pile foundation.

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| NC clay | OC clay | Current stress = max past vs < max past |
| Drained | Undrained | Pore pressure dissipated vs not |
| Rankine | Coulomb | No wall friction vs wall friction |
| Shallow | Deep | $D_f/B < 4$ vs $D_f/B > 4$ |
| Immediate settlement | Consolidation settlement | Elastic (instant) vs time-dependent |

---

## E. Numerical Questions

1. **Find $\tau_f$** for $c' = 20$ kPa, $\phi' = 25°$, $\sigma' = 100$ kPa. → 66.6 kPa
2. **Find $K_a$** for $\phi = 30°$. → 0.333
3. **Find $q_u$** for strip footing, $c = 20$ kPa, $\phi = 25°$, $B = 2$ m, $\gamma = 18$ kN/m³. → 1019.5 kPa
4. **Find consolidation time** for 90%, $c_v = 2 \times 10^{-7}$ m²/s, double drainage $H = 3$ m. → 110 days

---

## F. Rapid-Fire Questions

1. $K_a = ?$ → $\tan^2(45° - \phi/2)$
2. $K_p = ?$ → $\tan^2(45° + \phi/2)$
3. $T_v$ for 50% consolidation? → 0.2
4. $T_v$ for 90% consolidation? → 0.848
5. FOS for bearing capacity? → 3
6. FOS for pile capacity (static)? → 2.5
7. Phase relationship? → $Se = wG_s$
8. Mohr-Coulomb? → $\tau_f = c + \sigma'\tan\phi$

---

## High-Value Interview Answers

### High-Value Q1: "Explain effective stress."

**30-second answer:**
"Effective stress is the stress carried by the soil skeleton: $\sigma' = \sigma - u$. Soil strength depends on effective stress, not total stress. Shear strength is $\tau_f = c' + \sigma'\tan\phi'$. When pore pressure increases (flooding, rapid loading), effective stress decreases and strength drops — this is why saturated slopes fail during heavy rain."

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`geotechnical.md`](geotechnical.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| RCC Design | [`../rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Structures | [`../structures/structures.md`](../structures/structures.md) |
| Transportation | [`../transportation/transportation-engineering.md`](../transportation/transportation-engineering.md) |
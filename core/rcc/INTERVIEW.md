# RCC Design — Interview Questions & Answers

> **Placement Priority:** P0 — Asked in EVERY core civil engineering interview
> **Canonical Study:** [`rcc-design.md`](rcc-design.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 20+ questions across 7 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is the difference between limit state and working stress method?**
   - WSM: elastic theory, allowable stresses, single FOS. LSM: probabilistic, partial safety factors, checks collapse + serviceability, more economical.

2. **What are the assumptions in limit state flexural design?**
   - Plane sections remain plane; max concrete strain 0.0035; failure by concrete crushing; max principal strain theory; max tension steel strain $0.87f_y/E_s + 0.002$.

3. **What is the difference between under-reinforced, balanced, and over-reinforced sections?**
   - Under: steel yields first (ductile, preferred). Balanced: simultaneous failure. Over: concrete crushes first (brittle, avoid).

4. **What is the significance of $x_{u,max}/d$?**
   - The limiting NA depth ratio ensuring under-reinforced behavior. Fe250: 0.53, Fe415: 0.48, Fe500: 0.46.

5. **What is development length and why is it needed?**
   - The length required to transfer a bar's force to concrete through bond, preventing pull-out failure.

6. **What is the difference between one-way and two-way slabs?**
   - One-way: $l_y/l_x > 2$, bends in short direction. Two-way: $l_y/l_x \le 2$, bends in both directions.

7. **What is punching shear?**
   - Two-way shear at $d/2$ from the column face where the column load punches through the footing/slab.

8. **What is the difference between pre-tensioning and post-tensioning?**
   - Pre: steel tensioned before concrete cast, transfer by bond. Post: steel tensioned after concrete hardens, transfer by anchorages.

9. **What is creep in concrete?**
   - Time-dependent increase in strain under sustained load — increases deflection, causes loss of prestress.

10. **What is the modular ratio in WSM?**
    - $m = 280/(3\sigma_{cbc})$ — ratio of elastic moduli of steel and concrete.

---

## B. WHY Questions

1. **Why is concrete reinforced with steel?**
   - Concrete is weak in tension (~10% of compression). Steel carries tension, concrete carries compression → composite action.

2. **Why is under-reinforced design preferred?**
   - Ductile failure with visible warning (steel yields first) vs brittle sudden failure of over-reinforced sections.

3. **Why is limit state design preferred over working stress?**
   - Partial safety factors give consistent reliability; explicit serviceability checks; more economical.

4. **Why is minimum shear reinforcement required even when shear is low?**
   - Prevents sudden bursting, improves ductility, holds reinforcement together, improves dowel action, resists shrinkage/thermal cracking.

5. **Why use high-strength steel & concrete in prestressing?**
   - Large prestress losses (160–200 N/mm²) require high initial stress; high-strength concrete reduces creep/shrinkage losses.

6. **Why is "strong column - weak beam" preferred?**
   - During earthquakes, columns must remain elastic. If beams yield first, plastic hinges form at beam ends — ductile and repairable. If columns fail first, the structure collapses suddenly.

7. **Why are slabs not designed for shear?**
   - Slabs have small depth → $\tau_v = V/bd$ is very low, almost always below $0.5\tau_c$. Designed for bending and deflection only.

8. **Why is punching shear critical in footings?**
   - Concentrated column load punches through the footing at the $d/2$ perimeter — a brittle failure mode that can govern footing depth.

---

## C. WHAT-IF Questions

1. **What if $M_u > M_{u,lim}$?**
   - Redesign with a larger section, OR use a doubly reinforced section.

2. **What if $\tau_v > \tau_{c,max}$?**
   - Redesign the section (increase depth/width) — cannot be fixed with shear reinforcement alone.

3. **What if the slab is unsafe in shear?**
   - Increase slab thickness (slabs not normally designed for shear).

4. **What if development length cannot be provided?**
   - Provide hooks/bends, use smaller diameter bars, or mechanical anchorages.

5. **What if a column is slender (long)?**
   - Apply reduction coefficient $C_r = 1.25 - l_{eff}/48b$ and account for additional moment due to eccentricity.

6. **What if the water-cement ratio is too high?**
   - Reduces strength and durability, increases creep and shrinkage — the w/c ratio governs concrete quality.

7. **What if concrete is placed in sea water?**
   - Minimum grade M30 for RCC; minimum cover 50 mm for beams; use sulphate-resisting considerations.

8. **What if you need to splice bars > 36 mm diameter?**
   - Lap splices are not permitted — use mechanical couplers or welding.

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Working stress | Limit state | Elastic vs probabilistic |
| Under-reinforced | Over-reinforced | Ductile vs brittle failure |
| Singly reinforced | Doubly reinforced | No vs compression steel |
| One-way slab | Two-way slab | $l_y/l_x > 2$ vs $\le 2$ |
| Short column | Long column | $l_{eff}/D < 12$ vs $\ge 12$ |
| Pre-tensioning | Post-tensioning | Bond vs anchorage transfer |
| T-beam | Rectangular beam | Flange carries compression |
| Vertical stirrups | Bent-up bars | Stirrups more effective |
| Flexural shear | Punching shear | One-way vs two-way |
| Creep | Shrinkage | Sustained load vs drying |

---

## E. Numerical Questions

1. **Find $M_{u,lim}$** for $f_{ck}=25$, $b=250$, $d=450$. → $0.138 \times 25 \times 250 \times 450^2 = 174.7$ kN·m
2. **Find $L_d$** for Fe415, 16mm bar, M25 (deformed). → $\approx 645$ mm
3. **Find $P_u$** for short column, $A_{sc}=1\%$, $D=400$. → $\approx 2029$ kN
4. **Find stirrup spacing** for given $V_{us}$. → $s_v = 0.87 f_y A_{sv} d / V_{us}$
5. **Find $E_c$** for M25. → $5000\sqrt{25} = 25,000$ N/mm²
6. **Find $f_{cr}$** for M30. → $0.7\sqrt{30} = 3.83$ N/mm²

---

## F. Rapid-Fire Questions

1. Max strain in concrete (flexure)? → 0.0035
2. Min grade for RCC? → M20
3. $\gamma_m$ for concrete? → 1.5
4. $\gamma_m$ for steel? → 1.15
5. $x_{u,max}/d$ for Fe415? → 0.48
6. Min tension steel in beams? → $0.85bd/f_y$
7. Max tension steel? → 4% of $bD$
8. Min longitudinal steel in columns? → 0.8%
9. Max longitudinal steel in columns? → 6%
10. Nominal cover for column? → 40 mm
11. Nominal cover for footing? → 75 mm
12. Max moment redistribution? → 30%
13. Deflection limit? → Span/250
14. One-way slab if $l_y/l_x$? → > 2
15. Min steel in slabs (HYSD)? → 0.12%
16. Development length formula? → $0.87 f_y \phi / 4\tau_{bd}$
17. Lap length in compression? → > 24φ
18. Lap length in flexural tension? → > $L_d$ or 30φ
19. Short column if $l_{eff}/D$? → < 12
20. Prestressed concrete code? → IS 1343

---

## G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the IS 456 stress block parameters.**
   - Parabolic-rectangular block: parabolic up to 0.002 strain, rectangular to 0.0035. Average stress $0.67f_{ck}/1.5 = 0.446f_{ck}$, centroid at $0.42x_u$ from top. Compressive force $C = 0.36 f_{ck} b x_u$.

2. **Explain the interaction curve for columns.**
   - Plot of $P_u$ vs $M_u$ capacity. For small eccentricity, entire section in compression. As eccentricity increases, NA moves inward, moment capacity first increases then decreases.

3. **What is the truss analogy for shear design?**
   - Concrete acts as diagonal compression struts, stirrups as vertical tension ties, longitudinal steel as chords. Stirrups carry the diagonal tension.

4. **Explain concordant cable profile in continuous prestressed beams.**
   - A cable profile that produces a pressure line coincident with the profile itself, generating no reactions at supports. Used for indeterminate structures.

5. **What is the Hoyer effect?**
   - In pre-tensioned members, the prestressing force becomes zero at the wire end due to bond transfer; transmission length $L_t$ is where full prestress develops.

---

## High-Value Interview Answers

### High-Value Q1: "Design a simply supported RCC beam — walk me through it."

**30-second answer:**
"First, compute the factored moment $M_u = 1.5 \times$ (working moment). Assume a width and find required depth from $M_{u,lim} = 0.138 f_{ck} b d^2$. If $M_u < M_{u,lim}$, design as singly reinforced: find $A_{st} = M_u/(0.87 f_y (d - 0.42x_u))$. Check $x_u < x_{u,max}$ for under-reinforced behavior. Then check shear: $\tau_v = V_u/bd$, compare with $\tau_c$, provide stirrups if needed. Finally check development length and deflection."

### High-Value Q2: "What is the difference between one-way and two-way slabs?"

**30-second answer:**
"A slab is one-way if $l_y/l_x > 2$ — it bends primarily in the shorter direction, with main steel in the short span and distribution steel in the long span. A slab is two-way if $l_y/l_x \le 2$ — it bends in both directions, with main steel in both directions. Two-way slabs have higher span/depth ratios because load is shared in two directions."

### High-Value Q3: "Why is strong-column-weak-beam important?"

**30-second answer:**
"During earthquakes, columns must remain elastic to provide stability. If beams yield first, plastic hinges form at beam ends — ductile, repairable, and the structure survives. If columns fail first, the whole structure can collapse suddenly. IS 13920 mandates strong-column-weak-beam design."

---

## Interviewer Follow-up Chain

**Q: "What is the difference between under-reinforced and over-reinforced sections?"**
→ **Follow-up 1:** "Which one would you design and why?" → **Follow-up 2:** "How do you ensure a section is under-reinforced?" → **Follow-up 3:** "What is the failure warning mechanism in each?"

**Q: "How do you design a beam for shear?"**
→ **Follow-up 1:** "What is $\tau_{c,max}$ and what happens if exceeded?" → **Follow-up 2:** "Why stirrups and not bent-up bars?" → **Follow-up 3:** "What is the maximum stirrup spacing?"

**Q: "What is development length?"**
→ **Follow-up 1:** "How does it change for deformed bars?" → **Follow-up 2:** "What if $L_d$ cannot be provided?" → **Follow-up 3:** "What are the lap length rules?"

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`rcc-design.md`](rcc-design.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Structural Analysis | [`../structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md) |
| Steel Design | [`../steel/steel-design.md`](../steel/steel-design.md) |
| Structures Companion | [`../structures/structures.md`](../structures/structures.md) |
| SOM Fundamentals | [`../fundamentals/strength-of-materials.md`](../fundamentals/strength-of-materials.md) |
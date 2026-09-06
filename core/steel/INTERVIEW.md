# Steel Design — Interview Questions & Answers

> **Placement Priority:** P0 — Required for L&T, Tata Projects, PSUs, consulting firms
> **Canonical Study:** [`steel-design.md`](steel-design.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 20+ questions across 7 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is the difference between limit state and working stress method in steel?**
   - LSM: partial safety factors on loads & materials, checks strength + serviceability. WSM: single FOS, elastic.

2. **What are the types of bolted connections?**
   - Bearing type (force by bearing) and friction type/HSFG (force by friction).

3. **What is the difference between lap and butt joints?**
   - Lap: overlapped, eccentric. Butt: end-to-end with cover plates; double cover has no eccentricity.

4. **What are the failure modes of bolted connections?**
   - Shear, bearing, tension of bolt; bearing, tearing of plate; block shear.

5. **What is lateral-torsional buckling?**
   - Lateral buckling of the compression flange + twisting of the beam in unsupported beams.

6. **What is the difference between lacing and battening?**
   - Lacing: preferred for eccentric loads, +5% slenderness, 40°–70° inclination. Battening: for axial loads, +10% slenderness.

7. **What is block shear failure?**
   - A block of material tears out along a path combining shear (along bolt lines) and tension (across the end).

8. **What is web crippling?**
   - Local buckling of the web under concentrated loads (dispersion angle 1:2.5).

9. **What is the difference between a slab base and a gusseted base?**
   - Slab base: for axial loads. Gusseted base: for large moments (increases lever arm, minimizes plate thickness).

10. **What is the effective length of a column?**
    - The length between points of zero moment (inflection points), depending on end conditions: 0.65L (fixed-fixed), 0.8L (fixed-pinned), 1.0L (pinned-pinned), 2.0L (fixed-free).

---

## B. WHY Questions

1. **Why use HSFG bolts for bridges?**
   - Friction transfer prevents slippage under stress reversal; ideal for seismic/fatigue loading.

2. **Why do tension members not buckle?**
   - Uniform tension stabilizes the member; no tendency to buckle sideways — the full section is utilized.

3. **Why is welding preferred for tension members?**
   - No holes → full gross section available → higher efficiency.

4. **Why are stiffeners needed in plate girders?**
   - Thin webs are prone to buckling; stiffeners subdivide the web into smaller panels, increasing buckling resistance.

5. **Why is a base plate needed under steel columns?**
   - Distributes the concentrated column load over a wide area to prevent crushing of the concrete footing.

6. **Why is steel used for long-span structures?**
   - High strength-to-weight ratio, strong in both tension and compression, ductile, homogeneous, prefabricated.

7. **Why does steel design use partial safety factors?**
   - Uncertainties in loading, material strength, fabrication tolerances, and calculation accuracy → consistent reliability.

8. **Why is the compression flange of a gantry girder reinforced with a channel?**
   - Increases lateral stability and torsional rigidity against the lateral thrust from crane movement.

---

## C. WHAT-IF Questions

1. **What if threads intercept the shear plane of a bolt?**
   - Use net area $A_{nb} = 0.78 A_{sb}$, lower shear capacity.

2. **What if a joint is long (> 15d)?**
   - Apply the long joint reduction factor $\beta_{lj} = 1.075 - l_j/(200d)$.

3. **What if a beam is laterally unsupported?**
   - Check lateral-torsional buckling; use reduced bending strength $M_d = \beta_b Z_p f_{cd}$.

4. **What if the web is susceptible to shear buckling ($d/t_w > 67\varepsilon$)?**
   - Check the high shear case and provide transverse stiffeners.

5. **What if a column is very long?**
   - Fails by elastic buckling (Euler mode), governed by slenderness ratio.

6. **What if a fillet weld is very long (> 150$t_t$)?**
   - Apply the long joint reduction factor $\beta_{lw} = 1.2 - 0.2 l_j/(150 t_t) \le 1.0$.

7. **What if packing plates > 6 mm are used?**
   - Apply the packing plate reduction factor $\beta_{pkg} = 1.0 - 0.0125 t_{pkg}$.

8. **What if a member is subjected to stress reversal?**
   - Use HSFG bolts (friction transfer) and limit slenderness to 180 (non-wind) or 350 (wind/seismic).

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Bearing bolt | HSFG bolt | Bearing vs friction transfer |
| Lap joint | Double cover butt | Eccentric vs no eccentricity |
| Bolted | Welded | Mechanical vs metallurgical bond |
| Lacing | Battening | Eccentric vs axial loads |
| Plastic section | Slender section | Plastic hinge vs local buckling |
| Laterally supported | Unsupported beam | No LTB vs LTB check |
| Short column | Long column | Crushing vs buckling |
| Slab base | Gusseted base | Axial vs moment loads |
| Butt weld | Fillet weld | Full penetration vs throat thickness |
| Web crippling | Web buckling | Local vs column-type buckling |

---

## E. Numerical Questions

1. **Find $V_{dsb}$** for 20mm bolt, single shear, threads intercept. → ≈ 45.3 kN
2. **Find $P_{dw}$** for 6mm fillet weld, 200mm. → ≈ 149.5 kN
3. **Find $A_g$ required** for $T = 300$ kN. → ≈ 1320 mm²
4. **Find $P_d = A_e f_{cd}$.** → Product of effective area & design stress
5. **Find $L_e$** for one fixed, one pinned column, $L = 4$ m. → 3.2 m
6. **Find $V_d$** for I-section, $A_v = 2400$ mm². → ≈ 315 kN

---

## F. Rapid-Fire Questions

1. $\gamma_{m0}$ for steel? → 1.10
2. $\gamma_{m1}$ for steel? → 1.25
3. $\gamma_{mw}$ shop weld? → 1.25
4. $\gamma_{mw}$ field weld? → 1.50
5. E for steel? → $2 \times 10^5$ N/mm²
6. Min pitch of bolts? → 2.5d
7. Max slenderness (compression)? → 180
8. Max slenderness (tension)? → 400
9. Lacing inclination? → 40°–70°
10. Lacing transverse shear? → 2.5% of axial load
11. Web crippling dispersion? → 1:2.5
12. HSFG bolt property class? → 10.9S, 12.9S
13. Fillet weld throat factor K (60–90°)? → 0.70
14. Min fillet weld size? → 3 mm
15. Deflection limit (cantilever)? → Span/240
16. Gantry girder (electric ≤ 500 kN)? → L/750
17. Bearing strength of concrete? → 0.45 fck
18. Bolt hole for 20mm bolt? → 22 mm
19. Steel grade E250 yield? → 250 MPa
20. Poisson's ratio for steel? → 0.30

---

## G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the design compressive stress $f_{cd}$ formulation.**
   - $f_{cd} = \chi f_y/\gamma_{m0}$ where $\chi = 1/[\phi + \sqrt{\phi^2 - \lambda^2}]$, $\phi = 0.5[1 + \alpha(\lambda - 0.2) + \lambda^2]$, $\lambda = \sqrt{f_y/f_{cc}}$. Accounts for residual stress, imperfection, eccentricity.

2. **Explain the block shear failure mechanism.**
   - At the connection, a block of material tears out along a path combining shear (along bolt lines) and tension (across the end). Governed by the weaker of shear-yield/tension-fracture or shear-fracture/tension-yield.

3. **What is the truss analogy in steel connections?**
   - Similar to RCC shear: the connection acts as a truss with bolts/welds as tension members and plate as compression struts.

4. **Explain lateral-torsional buckling and the elastic critical moment.**
   - $M_{cr}$ is the moment at which a beam fails by lateral buckling under uniform moment. It depends on $EI_y$ (lateral bending), $GJ$ (torsion), and $EI_w$ (warping).

5. **What are the buckling classes and imperfection factors?**
   - Classes a, b, c, d with imperfection factors $\alpha$ = 0.21, 0.34, 0.49, 0.76. Higher $\alpha$ = more imperfection sensitivity.

---

## High-Value Interview Answers

### High-Value Q1: "Design a bolted connection — walk me through it."

**30-second answer:**
"First, determine the design bolt value $V_{db}$ = least of shear, bearing, and tension capacity. For shear: $V_{dsb} = f_{ub}(n_n A_{nb} + n_s A_{sb})/(\sqrt{3}\gamma_{mb})$. For bearing: $V_{dpb} = 2.5 k_b d t f_u/\gamma_{mb}$. Then find number of bolts $n = P/V_{db}$. Arrange bolts with proper pitch (≥2.5d), edge distance, and check the connection for block shear and member capacity."

### High-Value Q2: "What is the difference between a bearing-type and friction-type (HSFG) bolted connection?"

**30-second answer:**
"Bearing-type bolts transfer load by the bolt bearing against the hole — the bolt shank is in shear. HSFG bolts are pre-tensioned to create high clamping force, transferring load by friction between the plates. HSFG is used where stress reversal, seismic, or fatigue loading occurs (bridges), because it prevents slippage. Bearing type is simpler and cheaper for static loads."

### High-Value Q3: "Why is steel more efficient than concrete for tension members?"

**30-second answer:**
"Steel has high tensile strength and a high strength-to-weight ratio, so it can carry tension efficiently with the full cross-section utilized. Concrete is weak in tension (~10% of compression) and cracks under tension, so it needs steel reinforcement. Steel tension members don't buckle (unlike compression), making them the most efficient structural members."

---

## Interviewer Follow-up Chain

**Q: "What is the difference between a bearing and HSFG bolt?"**
→ **Follow-up 1:** "When would you use HSFG?" → **Follow-up 2:** "How is the clamping force achieved?" → **Follow-up 3:** "What is the property class of HSFG bolts?"

**Q: "How do you design a compression member?"**
→ **Follow-up 1:** "What is $f_{cd}$ and what does it account for?" → **Follow-up 2:** "What is the slenderness limit?" → **Follow-up 3:** "When would you use lacing vs battening?"

**Q: "What is lateral-torsional buckling?"**
→ **Follow-up 1:** "When does it occur?" → **Follow-up 2:** "How do you prevent it?" → **Follow-up 3:** "What is the elastic critical moment?"

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`steel-design.md`](steel-design.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| RCC Design | [`../rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Structural Analysis | [`../structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md) |
| Structures Companion | [`../structures/structures.md`](../structures/structures.md) |
| SOM Fundamentals | [`../fundamentals/strength-of-materials.md`](../fundamentals/strength-of-materials.md) |
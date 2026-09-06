# Structural Analysis — Interview Questions & Answers

> **Placement Priority:** P0 — Required for structural/consulting roles and PSUs
> **Canonical Study:** [`structural-analysis.md`](structural-analysis.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 20+ questions across 7 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is the difference between a structure and a mechanism?**
   - A structure provides **resistance against deformation** under load; a mechanism provides **no resistance** and undergoes rigid-body motion.

2. **What is the degree of static indeterminacy ($D_s$)?**
   - The number of unknown forces in excess of the available static equilibrium equations. $D_s = \text{Unknown forces} - \text{Equilibrium equations}$.

3. **What is the degree of kinematic indeterminacy ($D_k$)?**
   - The number of unknown joint displacements (degrees of freedom) that must be solved in displacement-based methods. $D_k = NJ - C$.

4. **What is an influence line?**
   - A graph showing the variation of a parameter (reaction, shear, moment) as a **unit load moves** across the structure.

5. **What is the Müller-Breslau principle?**
   - The influence line of an action takes the **scaled form of the deflection** produced by releasing the corresponding constraint and applying a unit displacement.

6. **What is a plastic hinge?**
   - A location where **infinite rotation occurs at constant plastic moment $M_p$** — the section has fully yielded.

7. **What is the shape factor?**
   - The ratio of plastic to elastic section modulus: $Z_p/Z_e$. It represents the **reserve strength** beyond first yield.

8. **What is the carry-over factor in moment distribution?**
   - The fraction of a distributed moment transferred to the far end: **+1/2** (fixed), **0** (hinged), **-1** (cantilever).

9. **What is the stiffness of a member?**
   - The moment required to produce unit rotation at one end: **$4EI/L$** (fixed far end), **$3EI/L$** (hinged far end).

10. **What is the difference between the flexibility and stiffness methods?**
    - Flexibility: unknowns are **redundant forces**, uses compatibility ($[D] = [F][P]$). Stiffness: unknowns are **joint displacements**, uses equilibrium ($[P] = [K][D]$).

---

## B. WHY Questions

1. **Why is superposition valid for most structures?**
   - Requires **linear elastic behavior** — response proportional to load. Valid for small displacements and elastic materials; invalid for slender columns (P-Δ effects).

2. **Why use influence lines?**
   - To find the **critical load position** that produces maximum reaction, shear, or moment at a section — essential for bridges and crane girders with moving loads.

3. **Why is plastic analysis more economical?**
   - Utilizes the **full plastic moment capacity** (shape factor reserve), allowing moment redistribution through plastic hinges → smaller, lighter sections.

4. **Why are arches economical for long spans?**
   - Horizontal thrust $H$ creates axial compression that counteracts bending: $M_{arch} = M_{beam} - Hy$. Primarily axial compression → slender, efficient sections.

5. **Why is the stiffness method preferred in software?**
   - **Systematic and automated** — assemble $[K]$, apply loads, solve for displacements. Handles large DOF efficiently; basis of FEA (SAP2000, ETABS, STAAD).

6. **Why is slope-deflection preferred over moment distribution for sway frames?**
   - It's a **direct (non-iterative)** method that handles sway and support settlement systematically via simultaneous equations.

7. **Why does a 3-hinged parabolic arch under UDL have zero bending moment?**
   - The arch axis is the **funicular (thrust) line** for UDL — the shape exactly balances the load, giving zero moment and shear everywhere.

8. **Why does a cable take a parabolic shape under UDL?**
   - A flexible cable carries load purely in tension (zero moment). For UDL along the span, the equilibrium shape is a **parabola**; for UDL along the curve, a **catenary**.

---

## C. WHAT-IF Questions

1. **What if a structure is unstable?**
   - Don't compute indeterminacy — it undergoes rigid-body movement. Unstable if support reactions are all parallel or concurrent.

2. **What if a frame sways?**
   - Account for sway in moment distribution. Causes: unsymmetrical loading/outline, different column end conditions, non-uniform sections, horizontal loads, support settlement.

3. **What if temperature increases in a 2-hinged arch?**
   - $H$ increases → $M_{arch}$ decreases (rise unchanged). A 3-hinged arch has **no thermal stresses** (determinate).

4. **What if a section is subjected to impact or fatigue loading?**
   - **Plastic analysis is not applicable** — also not for high-tensile steel (no defined yield) or brittle materials.

5. **What if a beam is laterally unsupported?**
   - Check **lateral-torsional buckling**; use reduced bending strength $M_d = \beta_b Z_p f_{cd}$.

6. **What if support settlement occurs in a continuous beam?**
   - Use slope-deflection or three-moment equation with the settlement term ($3\Delta/L$) — moment distribution requires the sway/settlement correction.

7. **What if you need the maximum BM under a moving train of wheel loads?**
   - Place the load system so the **chosen load and the resultant are equidistant from the girder midpoint**.

8. **What if a truss has more members than needed?**
   - It becomes statically indeterminate internally ($D_{si} > 0$); redundant members carry load based on stiffness, not just equilibrium.

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Statically determinate | Statically indeterminate | Equilibrium vs compatibility needed |
| Static indeterminacy | Kinematic indeterminacy | Unknown forces vs unknown displacements |
| Flexibility method | Stiffness method | Redundants vs displacements as unknowns |
| Moment distribution | Slope-deflection | Iterative vs direct (simultaneous equations) |
| Elastic analysis | Plastic analysis | Yield moment vs plastic moment capacity |
| 3-hinged arch | 2-hinged arch | Determinate ($D_s=0$) vs indeterminate ($D_s=1$) |
| Parabola | Catenary | UDL on span vs UDL along curve |
| Static theorem | Kinematic theorem | Lower bound ($W \le W_u$) vs upper bound ($W \ge W_u$) |
| Beam mechanism | Sway mechanism | Hinges in spans vs column-top drift |
| Pin-jointed | Rigid-jointed | Axial only vs bending + shear + axial |

---

## E. Numerical Questions

1. **Find $D_s$ for a plane truss** with $m=11$, $j=7$, $R=3$. → $(11+3) - 2(7) = 0$ (determinate)
2. **Find $D_s$ for a rigid plane frame** with $m=5$, $R=6$, $j=4$. → $(15+6) - 12 = 9$
3. **Find the shape factor for a rectangle.** → $Z_p/Z_e = (bd^2/4)/(bd^2/6) = 1.5$
4. **Find $H$ for a 3-hinged parabolic arch**, $l=20$ m, $h=4$ m, $w=10$ kN/m. → $wl^2/8h = 4000/32 = 125$ kN
5. **Find the collapse load of a simply supported beam**, span $L$, central load, $M_p$. → $W_u = 4M_p/L$
6. **Find the number of plastic hinges for collapse** of a fixed beam. → $N = D_s + 1 = 3 + 1 = 4$

---

## F. Rapid-Fire Questions

1. Reactions of a fixed support? → 3
2. Reactions of a roller? → 1
3. $D_s$ for plane truss? → $(m+R) - 2j$
4. $D_s$ for rigid plane frame? → $(3m+R) - 3j$
5. COF for fixed far end? → +1/2
6. Stiffness for fixed far end? → $4EI/L$
7. Stiffness for hinged far end? → $3EI/L$
8. Shape factor for I-section? → 1.14
9. Shape factor for rectangle? → 1.5
10. Shape factor for circle? → 1.7
11. Plastic hinges for collapse? → $D_s + 1$
12. $H$ for 3-hinged arch (UDL)? → $wl^2/8h$
13. $D_s$ for 3-hinged arch? → 0
14. $D_s$ for 2-hinged arch? → 1
15. $D_s$ for fixed arch? → 3
16. Cable shape under UDL? → Parabola
17. Cable shape under self-weight? → Catenary
18. Load factor for rectangle? → 2.26
19. Load factor for I-section? → 1.70
20. Bernoulli's assumption? → Plane sections remain plane

---

## G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the horizontal thrust for a 3-hinged parabolic arch.**
   - Take moments about the crown hinge: $H \cdot h = wl^2/8 \Rightarrow H = wl^2/8h$. The crown hinge has zero moment, so the beam moment at crown ($wl^2/8$) is balanced by $H \cdot h$.

2. **Explain the static and kinematic theorems of plastic analysis.**
   - **Static (lower bound):** equilibrium + yield → $W \le W_u$. **Kinematic (upper bound):** equilibrium + mechanism → $W \ge W_u$. The true collapse load lies between; the **unique theorem** states the collapse load satisfying both is exact.

3. **What is the significance of the shape factor in plastic design?**
   - It quantifies the **reserve strength** beyond first yield. Higher shape factor = more moment redistribution capacity. For an I-section (1.14), the reserve is 14%; for a rectangle (1.5), 50%.

4. **Explain the stiffness method formulation for a frame.**
   - $[K][D] = [P]$: assemble the global stiffness matrix from member stiffness matrices (transformed to global coordinates), apply the load vector, solve for joint displacements, then recover member end forces. The size of $[K]$ equals $D_k$.

5. **Why does a 3-hinged parabolic arch under UDL have zero bending moment everywhere?**
   - The arch axis coincides with the **funicular polygon** for the UDL — the thrust line follows the arch axis, so every section is in pure axial compression with zero moment and zero shear.

---

## High-Value Interview Answers

### High-Value Q1: "Explain the moment distribution method."

**30-second answer:**
"First, compute fixed-end moments for each member. Then compute distribution factors $DF = K/\sum K$ at each joint. Release joints one at a time, distributing the unbalanced moment proportionally to the DFs. Carry over half the distributed moment to each far end. Repeat until the unbalanced moments converge to zero. It's iterative but systematic for continuous beams and frames."

### High-Value Q2: "What is the difference between statically determinate and indeterminate structures?"

**30-second answer:**
"A determinate structure can be analyzed using only static equilibrium equations. An indeterminate structure has more unknowns than equilibrium equations, so compatibility conditions and material properties are needed. Indeterminate structures are stiffer and redistribute loads, but require advanced methods — moment distribution, slope-deflection, or matrix methods."

### High-Value Q3: "Why are arches better than beams for long spans?"

**30-second answer:**
"In an arch, the horizontal thrust $H$ at the supports creates axial compression that counteracts bending: $M_{arch} = M_{beam} - Hy$. This drastically reduces the bending moment, allowing slender sections. Arches carry primarily axial compression, so materials strong in compression work well — making them economical for long-span bridges."

---

## Interviewer Follow-up Chain

**Q: "What is the degree of static indeterminacy?"**
→ **Follow-up 1:** "How would you compute it for a rigid frame?" → **Follow-up 2:** "What does a high $D_s$ mean for analysis difficulty?" → **Follow-up 3:** "When would you use the stiffness method vs moment distribution?"

**Q: "Explain influence lines."**
→ **Follow-up 1:** "How do you find the maximum BM under a moving UDL?" → **Follow-up 2:** "What is the Müller-Breslau principle?" → **Follow-up 3:** "How do ILDs differ for determinate vs indeterminate beams?"

**Q: "What is plastic analysis?"**
→ **Follow-up 1:** "How many plastic hinges for collapse of a fixed beam?" → **Follow-up 2:** "What is the shape factor and why does it matter?" → **Follow-up 3:** "When is plastic analysis NOT applicable?"

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`structural-analysis.md`](structural-analysis.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| RCC Design | [`../rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Steel Design | [`../steel/steel-design.md`](../steel/steel-design.md) |
| Structures Companion | [`../structures/structures.md`](../structures/structures.md) |
| SOM Fundamentals | [`../fundamentals/strength-of-materials.md`](../fundamentals/strength-of-materials.md) |
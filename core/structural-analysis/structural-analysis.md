# Structural Analysis

> **Placement Priority:** P0 — Required for structural/consulting roles and PSUs
> **GATE-O-PEDIA Reference:** Chapter 3 (1,715 lines, 62 topics, 19 formulas)
> **Canonical Page:** `core/structural-analysis/structural-analysis.md`

---

## Scope

Structural analysis determines the internal forces (axial, shear, bending, torsion) and deformations in structures under applied loads. It is the foundation for structural design (RCC, steel) and is essential for structural/consulting roles and PSU interviews.

| Domain | Relevance |
|--------|-----------|
| Structural Design | Determines design forces for RCC/steel |
| Consulting | Indeterminate structure analysis |
| PSUs | Determinacy, influence lines, plastic analysis |
| Software | SAP2000, ETABS, STAAD (matrix methods) |
| Interview | Determinacy, moment distribution, plastic analysis |

---

## 1. Introduction to Structures

### What is a Structure?

An elastic body that provides **resistance against deformation** due to loads. A **mechanism** provides no resistance.

### Assumptions

- Elastic body
- Homogeneous
- Isotropic
- Continuous solid
- **Principle of superposition** is valid

### Validity of Superposition

- Displacement is small
- Elastic material, linear structural response (load vs deformation is a straight line)
- Supports are unyielding
- **NOT valid for slender columns**

### Classification of Structures

| Type | Example |
|------|---------|
| Skeletal | Roof trusses, building frames |
| Surface | Slabs, shells |
| Solid | Massive foundations |

**Skeletal structures:**
- **Pin-jointed:** Develop axial forces only, external loads at joints, straight members
- **Rigid-jointed:** Angle between members remains unchanged; resist forces via bending moment, shear, axial, torsion

### Bernoulli's Assumption

Plane sections normal to the neutral axis before bending remain plane after bending → strain varies linearly over the cross-section.

**Valid for:** Elastic, limit, ultimate theories; prismatic & non-prismatic; shallow beams.

### Support Reactions (Planar)

| Support | Reactions |
|---------|-----------|
| Free end | 0 |
| Roller | 1 |
| Hinged | 2 |
| Fixed | 3 |

### WHY is superposition valid for most structures?

Superposition requires **linear elastic behavior** — the response (stress, strain, deflection) is proportional to the load. For small displacements and elastic materials, the load-deformation relationship is a straight line, so multiple loads can be analyzed separately and added. It's invalid for slender columns (P-Δ effects) where the deformed geometry significantly changes the load path.

---

## 2. Determinacy & Indeterminacy

### Static Equilibrium Equations

**2D planar:** $\sum F_x = 0$, $\sum F_y = 0$, $\sum M = 0$
**3D space:** $\sum F_x = \sum F_y = \sum F_z = 0$, $\sum M_x = \sum M_y = \sum M_z = 0$

### Degree of Static Indeterminacy ($D_s$)

$$D_s = \text{Unknown forces} - \text{Equilibrium equations}$$

$$D_s = D_{si} + D_{se}$$

**External indeterminacy:**
- Plane: $D_{se} = R - 3$
- Space: $D_{se} = R - 6$

**Internal indeterminacy:**
- Plane truss: $D_{si} = m - (2j - 3)$
- Space truss: $D_{si} = m - (3j - 6)$
- Rigid plane frame: $D_{si} = 3C$
- Rigid space frame: $D_{si} = 6C$

### Simplified Formulas

| Structure | $D_s$ |
|-----------|-------|
| Plane truss | $(m + R) - 2j$ |
| Space truss | $(m + R) - 3j$ |
| Rigid plane frame | $(3m + R) - 3j$ |
| Rigid space frame | $(6m + R) - 6j$ |

### Stability

- **Unstable** if support reactions are all parallel or concurrent.
- If a truss is unstable, we never discuss $D_s$ or $D_{si}$.

### SD vs SI

| Statically Determinate | Statically Indeterminate |
|------------------------|--------------------------|
| Equilibrium sufficient | Insufficient |
| BM independent of material | BM dependent on material |
| BM independent of section area | BM dependent on section area |
| No thermal/lack-of-fit stresses | Thermal/lack-of-fit stresses |

### Kinematic Indeterminacy (Degree of Freedom)

Number of unknown joint displacements.

| Joint | DOF |
|-------|-----|
| Rigid joint (plane frame) | 3 ($\delta_x$, $\delta_y$, $\theta$) |
| Rigid joint (space frame) | 6 |
| Pin joint (plane frame) | 2 |
| Pin joint (space frame) | 3 |
| Free end | 3 |
| Roller support | 2 |
| Hinged support | 1 |
| Fixed support | 0 |

$$D_k = NJ - C$$

Where $N$ = DOF at joint, $J$ = number of joints, $C$ = compatibility equations.

### WHY is kinematic indeterminacy important?

Kinematic indeterminacy (DOF) determines the **number of unknown joint displacements** that must be solved in displacement-based methods (slope-deflection, matrix stiffness). It tells you the size of the stiffness matrix and the number of simultaneous equations to solve.

---

## 3. Influence Line Diagrams (ILD)

### Definition

Graphical representation of the variation of a parameter (reaction, shear, moment) as a **unit load moves** from one end of the structure to the other.

### Value of Parameter from ILD

$$\text{Value} = \sum(\text{Point load} \times \text{ordinate}) + \sum(\text{UDL intensity} \times \text{area under ILD})$$

### Müller-Breslau Principle

The influence line of an action assumes the **scaled form of the deflection** produced by releasing the corresponding constraint and applying a unit displacement.

- **Determinate beams:** Straight-line profiles
- **Indeterminate beams:** Curved profiles

### ILD for Rolling Loads

**Maximum BM at a section (UDL):**
$$\frac{w a}{L} = \frac{w b}{L} \Rightarrow \text{average load left} = \text{average load right}$$

**Maximum BM under a chosen wheel load:** The load system is placed so the chosen load and the resultant of all wheel loads are **equidistant from the midpoint** of the girder.

### WHY use influence lines?

Influence lines show where to place moving loads (vehicles, cranes) to produce the **maximum** reaction, shear, or moment at a critical section. This is essential for bridge and crane girder design where loads move. Without ILDs, you'd have to try every load position.

---

## 4. Moment Distribution Method (Hardy Cross)

### Assumptions

- Axial forces and axial deformations are neglected.
- Clockwise end moments are positive, anticlockwise negative.

### Carry Over Factor (COF)

| Far End | COF |
|---------|-----|
| Fixed | +1/2 |
| Hinged | 0 |
| Cantilever | -1 |

### Stiffness Factor

| Far End | Stiffness |
|---------|-----------|
| Fixed | $S = 4EI/L$ |
| Hinged | $S = 3EI/L$ |
| Free | $S = 0$ |

### Relative Stiffness

| Far End | Relative Stiffness |
|---------|-------------------|
| Fixed | $K = I/L$ |
| Hinged | $K = 3I/4L$ |

### Distribution Factor

$$DF = \frac{K}{\sum K}$$

**Note:** Sum of distribution factors at a rigid joint = 1.

### Procedure

1. Compute fixed-end moments (FEMs).
2. Compute distribution factors at each joint.
3. Release joints one at a time, distribute unbalanced moment proportionally to DF.
4. Carry over half to each far end.
5. Iterate until convergence.

### Portal Frame with Sway

**Causes of side sway:**
- Unsymmetrical loading
- Unsymmetrical outline
- Different end conditions of columns
- Non-uniform section of members
- Horizontal loading on columns
- Settlement of supports

**If structure & loading are symmetrical** → no sway.

### WHY is the moment distribution method iterative?

The method releases joints one at a time, distributing unbalanced moments and carrying over half to far ends. Each cycle reduces the unbalanced moment, so the process **converges** to the correct solution. It's iterative because releasing one joint disturbs the equilibrium of adjacent joints, requiring repeated cycles until the unbalanced moments become negligible.

---

## 5. Slope Deflection Method

### Fundamental Equation

$$M_{AB} = M_{AB}^F + \frac{2EI}{L}(2\theta_A + \theta_B - 3\Delta/L)$$

Where $M_{AB}^F$ = fixed-end moment, $\theta_A$, $\theta_B$ = end rotations, $\Delta$ = relative displacement.

### Procedure

1. Identify unknown joint rotations ($\theta$) and displacements ($\Delta$).
2. Write slope-deflection equations for each member.
3. Apply joint equilibrium ($\sum M = 0$ at each joint).
4. Solve simultaneous equations for $\theta$ and $\Delta$.
5. Substitute back to find end moments.

### WHY use slope deflection over moment distribution?

Slope deflection is a **direct (non-iterative)** method that solves for unknown joint rotations/displacements via simultaneous equations. It's more systematic and handles **sway** and **support settlement** more directly than moment distribution. However, it becomes cumbersome for large structures (many unknowns), where matrix methods are preferred.

---

## 6. Matrix Methods

### Flexibility Method (Force Method)

- Unknowns: redundant forces
- Uses compatibility equations
- $[D] = [F][P]$ where $F$ = flexibility matrix

### Stiffness Method (Displacement Method)

- Unknowns: joint displacements
- Uses equilibrium equations
- $[P] = [K][D]$ where $K$ = stiffness matrix

### Stiffness Method Steps

1. Identify DOF (kinematic indeterminacy).
2. Assemble global stiffness matrix $[K]$.
3. Apply loads → $[P]$.
4. Solve $[K][D] = [P]$ for displacements.
5. Compute member forces from displacements.

### WHY is the stiffness method preferred in software?

The stiffness method has a **systematic, automated procedure** — assemble the stiffness matrix, apply loads, solve for displacements. It handles large structures with many DOF efficiently and is the basis of **finite element analysis** (SAP2000, ETABS, STAAD). The flexibility method requires identifying redundants, which is harder to automate.

---

## 7. Plastic Analysis

### Introduction

Plastic design uses the strength of steel **beyond yield** up to ultimate load. It's economical and is the basis of IS 800:2007.

### Assumptions

- Bernoulli's assumption (plane sections remain plane)
- Axial and shear deformations neglected
- Cross-section symmetrical about plane of loading
- Bi-linear stress-strain relationship
- Material homogeneous & isotropic

**Not applicable for:** Impact/fatigue loading, high tensile steel (no defined yield point), brittle materials.

### Shape Factor

$$\text{Shape Factor} = \frac{M_p}{M_y} = \frac{Z_p}{Z_e}$$

| Section | Shape Factor |
|---------|--------------|
| Rectangular | 1.5 |
| Circular | 1.7 |
| I-section | 1.14 |
| H-section | 1.5 |
| Diamond | 2.0 |
| Triangular | 2.34 |

Shape factor represents the **reserve strength** beyond yield moment to reach plastic state.

### Plastic Hinge

- Location: under point loads, at max moment, at change of cross-section, at fixed/continuous supports.
- A plastic hinge allows infinite rotation at constant moment $M_p$.

### Number of Plastic Hinges for Collapse

$$N = D_s + 1$$

### Collapse Mechanisms

1. **Beam mechanism** — simply supported, continuous, fixed beams
2. **Sway mechanism** — frames (column top joints drift)
3. **Joint mechanism** — where >2 members meet
4. **Gable mechanism** — gable frames (columns spread at top)

### Theorems

| Theorem | Type | Conditions | Result |
|---------|------|-----------|--------|
| Static | Lower bound | Equilibrium + Yield | $W \le W_u$ |
| Kinematic | Upper bound | Equilibrium + Mechanism | $W \ge W_u$ |

### Load Factor

$$\text{Load Factor} = \frac{\text{Collapse load}}{\text{Working load}} = \text{FOS} \times \text{Shape factor}$$

- Rectangular section: $L_f = 1.5/0.66 = 2.26$
- I-section: $L_f = 1.14/0.66 = 1.70$

### WHY is plastic analysis more economical?

Plastic analysis utilizes the **full plastic moment capacity** of the section, not just the yield moment. The shape factor (1.14 for I-sections) represents the reserve strength beyond first yield. By allowing redistribution of moments through plastic hinges, sections can be smaller and lighter than elastic design.

---

## 8. Arches

### What is an Arch?

A curved beam in the vertical plane. Design forces: normal thrust (axial compression), radial shear, bending moment.

### Advantages over Simply Supported Beam

$$M_{arch} = M_{beam} - H \cdot y$$

The horizontal reaction $H$ reduces the net moment compared to a simply supported beam. Arches are economical for **long spans** and primarily carry axial compression (hence stone was used historically).

### Classification

| Type | $D_s$ |
|------|-------|
| Fixed arch | 3 |
| Two-hinged arch | 1 |
| Three-hinged arch | 0 (determinate) |

### Parabolic Arch

$$y = \frac{4h x}{l^2}(l - x)$$

### Three-Hinged Arch (UDL throughout)

$$H = \frac{w l^2}{8h}$$

**Key property:** For a 3-hinged parabolic arch under UDL, the **bending moment is zero everywhere** (shear force is also zero).

### Two-Hinged Arch

$$H = \frac{\int M y \, ds}{\int y^2 \, ds}$$

**Temperature effect:**
- 3-hinged arch: **no thermal stresses** (statically determinate)
- 2-hinged arch: temperature increase → $H$ increases → $M_{arch}$ decreases

### WHY are arches economical for long spans?

The horizontal thrust $H$ at the supports creates a **compressive axial force** that counteracts the bending moment. Since $M_{arch} = M_{beam} - Hy$, the moment is much smaller than in a simply supported beam. This allows slender, efficient sections — and because arches carry primarily axial compression, materials strong in compression (stone, concrete) work well.

---

## 9. Cables

### Assumptions

- Cable is flexible
- BM at every point is zero
- Self-weight neglected

### Cable Shape

| Loading | Cable Shape |
|---------|-------------|
| Load along horizontal span (UDL) | **Parabola** |
| UDL along the curve | **Catenary** |

### WHY does a cable take a parabolic shape under UDL?

A cable is flexible (no bending moment), so it carries load purely in tension. For a UDL along the horizontal span, the cable shape that satisfies equilibrium (zero moment at every point) is a **parabola**. If the load is uniformly distributed along the cable length itself, the shape becomes a **catenary**.

---

## 10. Worked Numerical Examples

### Example 1: Degree of Static Indeterminacy

**Problem:** Find $D_s$ for a rigid plane frame with $m = 5$ members, $R = 6$ reactions, $j = 4$ joints.

**Solution:**
1. $D_s = (3m + R) - 3j = (3 \times 5 + 6) - 3 \times 4 = 21 - 12 = 9$

**Interview follow-up:** What does $D_s = 9$ mean? → 9 additional equations beyond static equilibrium are needed.

### Example 2: Shape Factor

**Problem:** Find the shape factor for a rectangular section.

**Solution:**
1. $Z_e = bd^2/6$ (elastic section modulus)
2. $Z_p = bd^2/4$ (plastic section modulus)
3. Shape factor $= Z_p/Z_e = (bd^2/4)/(bd^2/6) = 1.5$

**Interview follow-up:** What does shape factor 1.5 mean? → The section has 50% reserve strength beyond first yield.

### Example 3: Three-Hinged Arch

**Problem:** Find horizontal thrust $H$ for a 3-hinged parabolic arch, span $l = 20$ m, rise $h = 4$ m, UDL $w = 10$ kN/m.

**Solution:**
1. $H = \frac{w l^2}{8h} = \frac{10 \times 20^2}{8 \times 4} = \frac{4000}{32} = 125$ kN

**Interview follow-up:** What is the BM at any section? → Zero (for UDL throughout).

### Example 4: Plastic Collapse Load

**Problem:** Find collapse load $W_u$ for a simply supported beam, span $L$, plastic moment $M_p$, central point load.

**Solution:**
1. Plastic hinge at center (max moment).
2. $M_p = W_u L/4$
3. $W_u = 4M_p/L$

**Interview follow-up:** How many plastic hinges for collapse? → $N = D_s + 1 = 0 + 1 = 1$ (determinate beam).

---

## 11. 🎤 Interview Q&A

### A. Basic Concept Questions

1. **What is the difference between statically determinate and indeterminate structures?**
   - Determinate: equilibrium equations sufficient. Indeterminate: need compatibility/extra equations.

2. **What is the degree of static indeterminacy?**
   - Number of unknown forces beyond static equilibrium equations.

3. **What is an influence line?**
   - Graph of a parameter's variation as a unit load moves across the structure.

4. **What is the Müller-Breslau principle?**
   - ILD shape = scaled deflection from releasing constraint and applying unit displacement.

5. **What is a plastic hinge?**
   - Location where infinite rotation occurs at constant plastic moment $M_p$.

### B. WHY Questions

1. **Why is superposition valid for most structures?**
   - Linear elastic behavior, small displacements → load-deformation is a straight line.

2. **Why use influence lines?**
   - To find critical load positions for maximum reaction/shear/moment in moving-load structures.

3. **Why is plastic analysis economical?**
   - Utilizes full plastic moment capacity (shape factor reserve strength).

4. **Why are arches economical for long spans?**
   - Horizontal thrust reduces bending moment; primarily axial compression.

5. **Why is the stiffness method preferred in software?**
   - Systematic, automated, handles large DOF; basis of FEA.

### C. WHAT-IF Questions

1. **What if a structure is unstable?**
   - Don't compute indeterminacy; it undergoes rigid body movement.

2. **What if a frame sways?**
   - Account for sway in moment distribution; causes: unsymmetrical loading/outline, different column end conditions.

3. **What if temperature increases in a 2-hinged arch?**
   - $H$ increases, $M_{arch}$ decreases (no change in rise).

4. **What if a cable carries UDL along its length?**
   - Shape becomes catenary instead of parabola.

5. **What if a section is subjected to impact/fatigue?**
   - Plastic analysis not applicable.

### D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Determinate | Indeterminate | Equilibrium vs compatibility |
| Static indeterminacy | Kinematic indeterminacy | Unknown forces vs displacements |
| Flexibility method | Stiffness method | Redundants vs displacements |
| Moment distribution | Slope deflection | Iterative vs direct |
| Elastic analysis | Plastic analysis | Yield vs plastic moment |
| 3-hinged arch | 2-hinged arch | Determinate vs indeterminate |
| Parabola | Catenary | UDL on span vs along curve |
| Static theorem | Kinematic theorem | Lower vs upper bound |

### E. Numerical Questions

1. Find $D_s$ for a plane truss. → $(m + R) - 2j$
2. Find shape factor for rectangle. → 1.5
3. Find $H$ for 3-hinged arch. → $wl^2/8h$
4. Find collapse load for SSB. → $4M_p/L$
5. Find $N$ plastic hinges for collapse. → $D_s + 1$

### F. Rapid-Fire Questions

1. Reactions of a fixed support? → 3
2. Reactions of a roller? → 1
3. $D_s$ for plane truss? → $(m+R) - 2j$
4. $D_s$ for rigid plane frame? → $(3m+R) - 3j$
5. COF for fixed far end? → +1/2
6. Stiffness for fixed far end? → $4EI/L$
7. Shape factor for I-section? → 1.14
8. Shape factor for rectangle? → 1.5
9. Shape factor for circle? → 1.7
10. Plastic hinges for collapse? → $D_s + 1$
11. $H$ for 3-hinged arch (UDL)? → $wl^2/8h$
12. $D_s$ for 3-hinged arch? → 0
13. $D_s$ for 2-hinged arch? → 1
14. $D_s$ for fixed arch? → 3
15. Cable shape under UDL? → Parabola
16. Cable shape under self-weight? → Catenary
17. Load factor for rectangle? → 2.26
18. Load factor for I-section? → 1.70
19. Bernoulli's assumption? → Plane sections remain plane
20. Superposition valid for? → Linear elastic, small displacement

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the horizontal thrust for a 3-hinged parabolic arch.**
   - Take moments about crown hinge: $H \cdot h = wl^2/8 \Rightarrow H = wl^2/8h$.

2. **Explain the difference between static and kinematic theorems of plastic analysis.**
   - Static (lower bound): equilibrium + yield → $W \le W_u$. Kinematic (upper bound): equilibrium + mechanism → $W \ge W_u$. True collapse load lies between.

3. **What is the significance of the shape factor in plastic design?**
   - It represents the reserve strength beyond first yield. Higher shape factor = more moment redistribution capacity.

4. **Explain the stiffness method formulation.**
   - $[K][D] = [P]$, where $K$ = global stiffness matrix assembled from member stiffness matrices, $D$ = joint displacements, $P$ = applied loads.

5. **Why does a 3-hinged parabolic arch under UDL have zero bending moment?**
   - The arch axis is the funicular (thrust line) for UDL, so the cable/arch shape exactly balances the load, giving zero moment and shear everywhere.

---

## 12. High-Value Interview Answers

### High-Value Q1: "Explain the moment distribution method."

**30-second answer:**
"First, compute fixed-end moments for each member. Then compute distribution factors $DF = K/\sum K$ at each joint. Release joints one at a time, distributing the unbalanced moment proportionally to the DFs. Carry over half the distributed moment to each far end. Repeat until the unbalanced moments converge to zero. It's iterative but systematic for continuous beams and frames."

### High-Value Q2: "What is the difference between statically determinate and indeterminate structures?"

**30-second answer:**
"A determinate structure can be analyzed using only static equilibrium equations ($\sum F_x = 0$, $\sum F_y = 0$, $\sum M = 0$). An indeterminate structure has more unknowns than equilibrium equations, so compatibility conditions and material properties are needed. Indeterminate structures are stiffer and redistribute loads, but require advanced methods (moment distribution, slope deflection, matrix methods)."

### High-Value Q3: "Why are arches better than beams for long spans?"

**30-second answer:**
"In an arch, the horizontal thrust $H$ at the supports creates axial compression that counteracts bending: $M_{arch} = M_{beam} - Hy$. This drastically reduces the bending moment, allowing slender sections. Arches carry primarily axial compression, so materials strong in compression work well. This makes arches economical for long spans like bridges."

---

## 13. Software Connection

| Tool | Application |
|------|-------------|
| SAP2000 | General structural analysis (matrix stiffness) |
| ETABS | Building analysis & design |
| STAAD.Pro | Structural analysis & design |
| OpenSees | Nonlinear structural analysis |
| RISA-3D | 3D structural analysis |
| midas Civil | Bridge analysis |
| Dlubal RFEM | 3D FEM structural analysis |

**Hand-calc verification:** Verify determinacy, support reactions, and simple member forces with hand calculations before trusting software output. Software uses the stiffness method internally.

---

## 14. 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Structure classification →  Determinacy & indeterminacy →  Kinematic indeterminacy    →  Ds/Dk calculation
Support reactions        →  Influence lines              →  Rolling loads & ILD       →  Müller-Breslau
Moment distribution      →  Sway frames                 →  Support settlement         →  Hardy Cross
Slope deflection         →  Simultaneous equations       →  Sway & settlement         →  Direct method
Plastic analysis         →  Shape factor & plastic hinge →  Collapse mechanisms       →  Static/kinematic theorems
Arches                   →  3-hinged & 2-hinged          →  Temperature effects       →  Funicular arch
Cables                   →  Parabola & catenary          →  Suspension bridges        →  Cable shape
Matrix methods           →  Stiffness formulation        →  FEA                       →  Software basis
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `STRUCTURAL` `ANALYSIS`

---

## 15. 🔗 Cross-Links

- [`structures.md`](../structures/structures.md) — Structural design companion
- [`rcc-design.md`](../rcc/rcc-design.md) — RCC design (uses analysis results)
- [`steel-design.md`](../steel/steel-design.md) — Steel design (plastic analysis)
- [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — Stress, bending fundamentals
- [`engineering-mechanics.md`](../fundamentals/engineering-mechanics.md) — Equilibrium, truss analysis

---

## 16. 📋 Quick Revision Checklist

- [ ] Structure = resistance to deformation; mechanism = no resistance
- [ ] Superposition: linear elastic, small displacement
- [ ] Reactions: free 0, roller 1, hinged 2, fixed 3
- [ ] $D_s$ plane truss = $(m+R) - 2j$
- [ ] $D_s$ rigid plane frame = $(3m+R) - 3j$
- [ ] $D_k$ = NJ - C
- [ ] ILD value = $\sum(P \times \text{ord}) + \sum(w \times \text{area})$
- [ ] Müller-Breslau: ILD = scaled deflection
- [ ] COF: fixed +1/2, hinged 0, cantilever -1
- [ ] Stiffness: fixed $4EI/L$, hinged $3EI/L$
- [ ] Shape factor: rect 1.5, circle 1.7, I 1.14
- [ ] Plastic hinges for collapse = $D_s + 1$
- [ ] Load factor = FOS × shape factor
- [ ] $H$ 3-hinged arch = $wl^2/8h$
- [ ] 3-hinged arch: $D_s = 0$ (determinate)
- [ ] 2-hinged arch: $D_s = 1$
- [ ] Fixed arch: $D_s = 3$
- [ ] Cable under UDL: parabola; along curve: catenary
- [ ] Stiffness method: $[K][D] = [P]$
- [ ] Static theorem: lower bound; kinematic: upper bound

---

## References

* GATE-O-PEDIA Chapter 3 — Structural Analysis (Physics Wallah)
* IS 800:2007 — Plastic analysis basis
* [`structures.md`](../structures/structures.md) — Structural design companion
* [`rcc-design.md`](../rcc/rcc-design.md) — RCC design
* [`steel-design.md`](../steel/steel-design.md) — Steel design
* [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — SOM fundamentals

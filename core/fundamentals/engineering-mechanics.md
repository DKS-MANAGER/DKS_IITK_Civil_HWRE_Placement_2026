# Engineering Mechanics

> **Placement Priority:** P0 — Foundation for ALL civil engineering subjects
> **GATE-O-PEDIA Reference:** Chapter 1 (1,189 lines, 25 topics, 8 formulas)
> **Canonical Page:** `core/fundamentals/engineering-mechanics.md`

---

## Scope

Engineering Mechanics is the foundation of all civil engineering. It deals with the effects of forces on bodies (statics) and motion (dynamics). Every civil interview tests equilibrium, moment, friction, and truss fundamentals.

| Domain | Relevance |
|--------|-----------|
| Structural Analysis | Equilibrium, truss analysis |
| Strength of Materials | Force systems, moments |
| Geotechnical | Friction, stability |
| Fluid Mechanics | Force balance, hydrostatics |
| Interview | Universal foundation topic |
| Software | FEA, structural analysis basis |

---

## 1. Fundamentals

### Basic Terminologies

| Term | Definition |
|------|-----------|
| Length | Locates position of a point in space |
| Space | Geometrical region of study |
| Time | Measure of succession of events |
| Mass | Measure of inertia (resistance to change in velocity) |
| Particle | Concentrated point mass of negligible dimension |
| Rigid body | Relative position of any two points doesn't change under forces |

### Newton's Laws of Motion

1. **First Law:** A particle remains at rest or moves with uniform velocity if no unbalanced force acts on it.
2. **Second Law:** Rate of change of momentum is proportional to impressed force: $F = ma$ (for constant mass).
3. **Third Law:** Action and reaction are equal, opposite, and collinear.

### Newton's Law of Gravitation

$$F = G \frac{mM}{r^2}$$

**Weight:** $W = mg$, where $g = 9.81$ m/s² (at sea level, latitude 45°).

### WHY is statics the foundation of civil engineering?

Statics deals with bodies at rest or in uniform motion — exactly the condition of most civil structures (buildings, bridges, dams). Understanding how forces balance (equilibrium) is the first step in determining the internal forces that structures must resist. Every structural analysis and design method builds on these fundamentals.

---

## 2. Vectors & Force Systems

### Force Characteristics

A force is completely characterized by:
1. Magnitude
2. Direction
3. Point of application
4. Line of action

### Scalar vs Vector

| Scalar | Vector |
|--------|--------|
| Magnitude only | Magnitude + direction |
| Mass, time | Force, position, momentum |

### Parallelogram Law of Forces

$$R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$$

$$\tan\alpha = \frac{F_2\sin\theta}{F_1 + F_2\cos\theta}$$

**Special cases:**
- $\theta = 90°$: $R = \sqrt{F_1^2 + F_2^2}$
- $\theta = 60°$: $R = \sqrt{F_1^2 + F_2^2 + F_1F_2}$
- $\theta = 120°$: $R = F_1 + F_2$ (if equal)
- $\theta = 180°$: $R = F_1 - F_2$

### Method of Resolution

1. Resolve forces horizontally: $\sum F_x$
2. Resolve forces vertically: $\sum F_y$
3. Resultant: $R = \sqrt{(\sum F_x)^2 + (\sum F_y)^2}$
4. Direction: $\tan\theta = \frac{\sum F_y}{\sum F_x}$

### WHY resolve forces into components?

Resolving forces into horizontal and vertical components allows us to apply the equilibrium equations ($\sum F_x = 0$, $\sum F_y = 0$) independently in each direction. This simplifies complex force systems into manageable scalar equations, which is essential for analyzing structures.

---

## 3. Moment & Couple

### Moment of a Force

Turning effect of a force about a point.

$$M = P \times d$$

Where $d$ = perpendicular distance from the point to the line of action.

**Types:** Clockwise (negative) and anticlockwise (positive).

### Couple

Two parallel forces of equal magnitude, opposite direction, separated by distance $d$.

- Resultant force = **zero**
- Only effect: **rotation**
- Moment of couple: $M = F \times d$

### Varignon's Principle of Moments

The algebraic sum of moments of all forces about any point equals the **moment of their resultant** about the same point.

$$\sum M = R \times d$$

**Application:** Finding the position of the resultant force for non-concurrent force systems.

### WHY is Varignon's theorem useful?

It allows us to replace a complex system of forces with a single resultant force at a known location. This is essential for determining where the resultant acts (e.g., the location of the resultant soil pressure under a footing), which governs stability and design.

---

## 4. Equilibrium

### Conditions of Equilibrium

A particle is in equilibrium if both resultant force $R$ and resultant couple $M$ are zero:

$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M = 0$$

### Free Body Diagram (FBD)

A diagram of a body freed from all contact surfaces, showing all forces acting on it (self-weight + reactions).

**Steps:**
1. Isolate the body.
2. Show all applied forces.
3. Show all support reactions.
4. Apply equilibrium equations.

### Lami's Theorem

If three coplanar forces acting at a point are in equilibrium, each force is proportional to the sine of the angle between the other two:

$$\frac{P}{\sin\alpha} = \frac{Q}{\sin\beta} = \frac{R}{\sin\gamma}$$

### Types of Beams

| Beam Type | Description |
|-----------|-------------|
| Simply supported | Both ends simply supported |
| Cantilever | One end fixed, other free |
| Both ends hinged | Hinged at both ends |
| One hinged, one roller | Hinged + roller |
| Overhanging | Extends beyond support |
| Propped cantilever | Cantilever with prop |
| Fixed | Both ends fixed |

### Types of Loading

1. Concentrated point load
2. Uniformly distributed load (UDL)
3. Uniformly varying load (UVL)
4. External moment

**Load conversion:** Equivalent concentrated load = area of loading diagram, acting at its centroid.

### WHY is the free body diagram the most important skill?

The FBD isolates the body and shows all forces acting on it, making the equilibrium equations clear. Most errors in structural analysis come from missing or misdirected forces in the FBD. A correct FBD is the foundation of every correct solution.

---

## 5. Friction

### Definition

Force that resists the movement of two contacting surfaces sliding relative to each other.

### Types

| Type | Description |
|------|-------------|
| Limiting friction | Friction at the verge of motion: $F_s = \mu_s N$ |
| Kinetic friction | Friction during motion: $F_k = \mu_k N$ |
| Static friction | Friction when no motion |

### Coefficient of Friction

$$\mu = \frac{F}{N} = \tan\theta$$

Where $\theta$ = angle of friction (angle at which body just starts sliding).

### Angle of Friction / Repose

The angle at which a body just begins to slide down an inclined plane.

### Cone of Friction

Inverted cone with semi-central angle equal to the limiting friction angle.

### Key Relationships

- $\mu_s \ge \mu_k$ (static ≥ kinetic)
- $\mu$ ranges 0 to 1 (can exceed 1 for silicon/acrylic rubber)
- If $F < F_s$: motion not impending
- If $F = F_s$: impending motion
- If $F > F_s$: slipping occurs

### WHY does friction matter in civil engineering?

Friction governs the stability of retaining walls (sliding), foundations (bearing), slopes (stability), and connections (HSFG bolts transfer by friction). Understanding when friction is limiting (impending motion) vs kinetic (sliding) is critical for safety assessment.

---

## 6. Truss Analysis

### What is a Truss?

A structure of slender members joined at end points by bolting/riveting/welding to a common **gusset plate**.

### Assumptions

- Members joined by smooth pins
- All loads applied at joints
- Self-weight of members negligible

### Zero-Force Members

Provided to reduce the effective length of other members.

**Rules:**
1. If two non-collinear members meet at a joint with no external force → both are zero-force members.
2. If three members meet, two collinear, no external load → the third (non-collinear) member is zero-force.

### Method of Joints

- Consider equilibrium of each joint.
- Not applicable if >2 unknown forces at a joint.
- Start from a joint with only 2 unknown member forces.
- Apply $\sum F_x = 0$, $\sum F_y = 0$.

### Method of Sections

- Used when force in only a few members is required.
- Section line should cut **not more than 3 members**.
- Cut the truss into two portions, apply equilibrium to one portion.

### Sign Convention

- Tension (T): member pulls away from joint (positive)
- Compression (C): member pushes toward joint (negative)

### WHY use the method of sections?

The method of sections directly finds the force in a specific member without solving all joints. By cutting through the member of interest (and at most 2 others) and taking moments about a strategic point, you can isolate the member force with a single equilibrium equation.

---

## 7. Center of Mass & Centroid

### Center of Mass

Point where the whole mass of a body appears concentrated.

$$\bar{x} = \frac{\sum m_i x_i}{M}, \quad \bar{y} = \frac{\sum m_i y_i}{M}$$

### Centroid of Common Shapes

| Shape | Area | $\bar{x}$ | $\bar{y}$ |
|-------|------|-----------|-----------|
| Rectangle ($b \times d$) | $bd$ | $b/2$ | $d/2$ |
| Triangle ($b \times h$) | $bh/2$ | $b/3$ | $h/3$ |
| Circle (radius $r$) | $\pi r^2$ | $r$ | $r$ |
| Semicircle | $\pi r^2/2$ | $r$ | $4r/3\pi$ |
| Quarter circle | $\pi r^2/4$ | $4r/3\pi$ | $4r/3\pi$ |
| Circular arc | — | $r\sin\alpha/\alpha$ | 0 |

### Centroid of Composite Sections

$$\bar{x} = \frac{\sum a_i x_i}{\sum a_i}, \quad \bar{y} = \frac{\sum a_i y_i}{\sum a_i}$$

For sections with holes, subtract the hole area (negative area method).

### WHY is the centroid important?

The centroid is where the resultant of distributed loads acts. It's essential for:
- Locating the resultant of soil pressure under footings
- Determining the neutral axis of beams
- Computing moment of inertia (which governs bending stiffness)

---

## 8. Moment of Inertia

### Definition

Second moment of area about an axis, measuring resistance to bending.

$$I = \int y^2 \, dA$$

### Common Values

| Section | $I$ |
|---------|-----|
| Rectangle ($b \times d$) | $bd^3/12$ |
| Circle (dia $D$) | $\pi D^4/64$ |
| Triangle ($b \times h$) | $bh^3/36$ |

### Parallel Axis Theorem

$$I = I_{cg} + A d^2$$

Where $d$ = distance between the centroidal axis and the parallel axis.

### Radius of Gyration

$$r = \sqrt{\frac{I}{A}}$$

### WHY is moment of inertia critical?

Moment of inertia governs the **bending stiffness** ($EI$) and **buckling resistance** of members. A larger $I$ means a stiffer, stronger member. It's why I-sections are efficient — they concentrate area far from the neutral axis, maximizing $I$ for a given area.

---

## 9. Virtual Work

### Principle of Virtual Work

For a body in equilibrium, the total virtual work done by all forces during a virtual (imaginary, small) displacement is zero:

$$\sum F \cdot \delta = 0$$

### Applications

- Finding reactions in indeterminate structures
- Determining deflections
- Analyzing mechanisms

### WHY use virtual work?

Virtual work provides a powerful energy-based method for analyzing structures, especially for finding deflections and reactions in indeterminate structures where equilibrium alone is insufficient. It's the basis of the unit load method and Castigliano's theorems.

---

## 10. Worked Numerical Examples

### Example 1: Resultant Force

**Problem:** Find the resultant of $F_1 = 100$ N and $F_2 = 150$ N acting at 46°.

**Solution:**
1. $R = \sqrt{100^2 + 150^2 + 2 \times 100 \times 150 \times \cos 46°}$
2. $R = \sqrt{10000 + 22500 + 20840} = \sqrt{53340} = 231$ N
3. $\tan\alpha = \frac{150\sin 46°}{100 + 150\cos 46°} = \frac{107.9}{204.2} = 0.528$
4. $\alpha = 27.8°$

**Interview follow-up:** What if the forces are perpendicular? → $R = \sqrt{F_1^2 + F_2^2}$.

### Example 2: Lami's Theorem

**Problem:** A 50 kg weight hangs from two cables AB and BC at 120° and 135° to the vertical. Find tensions.

**Solution:**
1. $W = 50 \times 9.81 = 490.5$ N
2. $\frac{F_{BA}}{\sin 120°} = \frac{F_{BC}}{\sin 135°} = \frac{490.5}{\sin 105°}$
3. $F_{BA} = \frac{490.5 \times \sin 120°}{\sin 105°} = \frac{490.5 \times 0.866}{0.966} = 439.8$ N
4. $F_{BC} = \frac{490.5 \times \sin 135°}{\sin 105°} = \frac{490.5 \times 0.707}{0.966} = 359.1$ N

**Interview follow-up:** When is Lami's theorem applicable? → Only for 3 coplanar forces in equilibrium.

### Example 3: Truss (Method of Joints)

**Problem:** Find force in member PR of a truss with $R_P = 50$ kN, $R_Q = 40$ kN.

**Solution:**
1. At joint P: $\sum F_x = 0$, $\sum F_y = 0$
2. $F_{PR}\sin 45° + 50 = 0 \Rightarrow F_{PR} = -70.71$ kN (compression)
3. $F_{PQ} = +50$ kN (tension)

**Interview follow-up:** What does negative force mean? → Compression.

### Example 4: Friction

**Problem:** A 100 kg block on a horizontal surface, $\mu_s = 0.8$, $\mu_k = 0.6$. A 700 N force acts at 30° to horizontal. Does it move?

**Solution:**
1. $\sum F_y = 0$: $N - 981 + 700\sin 30° = 0 \Rightarrow N = 631$ N
2. $\sum F_x = 0$: $F = 700\cos 30° = 606$ N
3. $F_{max} = \mu_s N = 0.8 \times 631 = 505$ N < 606 N
4. **Motion occurs** → $F = \mu_k N = 0.6 \times 631 = 379$ N

**Interview follow-up:** Why is kinetic friction less than static? → Once sliding starts, surface interlocking is overcome.

---

## 11. 🎤 Interview Q&A

### A. Basic Concept Questions

1. **What is the difference between a particle and a rigid body?**
   - Particle: negligible dimension. Rigid body: relative positions of points don't change.

2. **State Newton's three laws of motion.**
   - Inertia, $F = ma$, action-reaction.

3. **What is a couple?**
   - Two equal, opposite, parallel forces → pure rotation, zero resultant.

4. **What is Lami's theorem?**
   - Three coplanar forces in equilibrium: each proportional to sine of angle between other two.

5. **What is a zero-force member?**
   - A truss member carrying no load, provided to reduce effective length.

### B. WHY Questions

1. **Why is statics the foundation of civil engineering?**
   - Most structures are at rest; equilibrium determines internal forces.

2. **Why resolve forces into components?**
   - Allows independent equilibrium equations in x and y.

3. **Why is the FBD the most important skill?**
   - Correct FBD → correct equilibrium equations → correct solution.

4. **Why is moment of inertia critical?**
   - Governs bending stiffness and buckling resistance.

5. **Why does friction matter in civil engineering?**
   - Retaining wall sliding, foundation bearing, slope stability, connections.

### C. WHAT-IF Questions

1. **What if $\mu > 1$?**
   - Possible for silicon/acrylic rubber coated surfaces.

2. **What if a truss joint has >2 unknown forces?**
   - Method of joints not applicable; use method of sections or solve other joints first.

3. **What if a section cuts >3 members?**
   - Method of sections not directly applicable; choose a different section.

4. **What if forces are non-concurrent?**
   - Use Varignon's theorem to find resultant location.

5. **What if a body is on an inclined plane?**
   - Resolve weight into components parallel and perpendicular to the plane.

### D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Scalar | Vector | Magnitude vs magnitude + direction |
| Static friction | Kinetic friction | $\mu_s \ge \mu_k$ |
| Moment | Couple | Single force vs two equal opposite forces |
| Method of joints | Method of sections | All members vs specific members |
| Tension | Compression | Pull vs push |
| Center of mass | Centroid | Mass vs area |
| Particle | Rigid body | Negligible vs finite dimension |
| Parabola | Catenary | UDL on span vs along curve |

### E. Numerical Questions

1. Find resultant of two forces at angle θ. → $R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$
2. Find moment of force about a point. → $M = P \times d$
3. Find centroid of composite section. → $\bar{x} = \sum a_i x_i / \sum a_i$
4. Find $I$ of rectangle. → $bd^3/12$
5. Find friction force. → $F = \mu N$

### F. Rapid-Fire Questions

1. $g$ at sea level? → 9.81 m/s²
2. Newton's second law? → $F = ma$
3. Resultant of perpendicular forces? → $\sqrt{F_1^2 + F_2^2}$
4. Moment of a couple? → $F \times d$
5. Varignon's theorem? → Sum of moments = moment of resultant
6. Equilibrium conditions? → $\sum F_x = 0$, $\sum F_y = 0$, $\sum M = 0$
7. Lami's theorem applies to? → 3 coplanar forces
8. Coefficient of friction? → $\mu = F/N = \tan\theta$
9. Static vs kinetic friction? → $\mu_s \ge \mu_k$
10. Zero-force member rule? → 2 non-collinear, no external load
11. Method of sections cuts? → ≤ 3 members
12. $I$ of rectangle? → $bd^3/12$
13. $I$ of circle? → $\pi D^4/64$
14. Parallel axis theorem? → $I = I_{cg} + Ad^2$
15. Radius of gyration? → $r = \sqrt{I/A}$
16. Centroid of triangle? → $h/3$ from base
17. Centroid of semicircle? → $4r/3\pi$
18. Shape factor of rectangle? → 1.5
19. Virtual work principle? → $\sum F \cdot \delta = 0$
20. Rigid body definition? → Relative positions don't change

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the parallelogram law of forces.**
   - Using vector addition: $\vec{R} = \vec{F_1} + \vec{F_2}$, magnitude $R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$.

2. **Explain the principle of virtual work.**
   - For equilibrium, total virtual work $\sum F \cdot \delta = 0$ for any virtual displacement. Basis of energy methods.

3. **What is the difference between center of mass and centroid?**
   - Center of mass: mass-weighted average position. Centroid: area-weighted average (geometric center). They coincide for uniform density.

4. **Explain the method of sections with a worked example.**
   - Cut through ≤3 members, take moments about a point where 2 of the cut members intersect, solve for the third.

5. **Why is the radius of gyration important in column design?**
   - $r = \sqrt{I/A}$ governs the slenderness ratio $KL/r$, which determines buckling capacity.

---

## 12. High-Value Interview Answers

### High-Value Q1: "How do you find the resultant of a force system?"

**30-second answer:**
"Resolve all forces into horizontal and vertical components. Sum them: $\sum F_x$ and $\sum F_y$. The resultant magnitude is $R = \sqrt{(\sum F_x)^2 + (\sum F_y)^2}$ and direction is $\tan\theta = \sum F_y / \sum F_x$. For non-concurrent forces, use Varignon's theorem to find the resultant's location."

### High-Value Q2: "Explain the method of joints for truss analysis."

**30-second answer:**
"Start at a joint with only 2 unknown member forces. Apply $\sum F_x = 0$ and $\sum F_y = 0$ to find those forces. Move to the next joint with 2 unknowns, using the known forces from previous joints. Continue until all member forces are found. Identify zero-force members first to simplify."

### High-Value Q3: "What is the difference between static and kinetic friction?"

**30-second answer:**
"Static friction acts when there's no relative motion, up to a maximum $\mu_s N$ at the verge of slipping. Kinetic friction acts during sliding and is $\mu_k N$, where $\mu_k < \mu_s$. Once motion starts, the friction force drops because surface interlocking is overcome."

---

## 13. Software Connection

| Tool | Application |
|------|-------------|
| STAAD.Pro | Structural analysis (uses equilibrium) |
| SAP2000 | General structural analysis |
| MATLAB | Vector/force computations |
| Python (NumPy) | Force resolution, matrix methods |
| AutoCAD | FBD & force diagrams |

**Hand-calc verification:** Always verify support reactions and member forces with hand calculations (equilibrium checks) before trusting software.

---

## 14. 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Newton's laws            →  Force resolution             →  Resultant of force systems  →  Equilibrium
Vectors & scalars        →  Parallelogram law            →  Varignon's theorem         →  Resultant location
Moment & couple          →  Moment of force              →  Couple systems              →  Moment calculation
Equilibrium              →  FBD & Lami's theorem         →  Beam reactions              →  FBD skills
Friction                 →  Static/kinetic friction      →  Inclined planes             →  Limiting friction
Trusses                  →  Method of joints             →  Method of sections          →  Zero-force members
Centroid                 →  Composite sections           →  Moment of inertia           →  Radius of gyration
Virtual work             →  Energy methods               →  Castigliano's theorems      →  Deflection
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `FUNDAMENTALS` `MECHANICS`

---

## 15. 🔗 Cross-Links

- [`strength-of-materials.md`](strength-of-materials.md) — Stress, bending, torsion fundamentals
- [`structural-analysis.md`](../structural-analysis/structural-analysis.md) — Determinacy, truss analysis
- [`structures.md`](../structures/structures.md) — Structural design
- [`rcc-design.md`](../rcc/rcc-design.md) — RCC design
- [`steel-design.md`](../steel/steel-design.md) — Steel design
- [`civil-engineering-foundations.md`](civil-engineering-foundations.md) — Foundation overview

---

## 16. 📋 Quick Revision Checklist

- [ ] Newton's laws: inertia, $F = ma$, action-reaction
- [ ] $g = 9.81$ m/s²
- [ ] Force: magnitude, direction, point of application, line of action
- [ ] $R = \sqrt{F_1^2 + F_2^2 + 2F_1F_2\cos\theta}$
- [ ] Moment: $M = P \times d$
- [ ] Couple: $M = F \times d$, zero resultant
- [ ] Varignon: $\sum M = R \times d$
- [ ] Equilibrium: $\sum F_x = 0$, $\sum F_y = 0$, $\sum M = 0$
- [ ] Lami's theorem: $P/\sin\alpha = Q/\sin\beta = R/\sin\gamma$
- [ ] Friction: $F = \mu N$, $\mu = \tan\theta$
- [ ] $\mu_s \ge \mu_k$
- [ ] Zero-force member: 2 non-collinear, no external load
- [ ] Method of sections: cut ≤ 3 members
- [ ] Centroid: $\bar{x} = \sum a_i x_i / \sum a_i$
- [ ] $I$ rectangle = $bd^3/12$, circle = $\pi D^4/64$
- [ ] Parallel axis: $I = I_{cg} + Ad^2$
- [ ] Radius of gyration: $r = \sqrt{I/A}$
- [ ] Virtual work: $\sum F \cdot \delta = 0$
- [ ] Centroid of triangle = $h/3$, semicircle = $4r/3\pi$
- [ ] Tension = pull, compression = push

---

## References

* GATE-O-PEDIA Chapter 1 — Engineering Mechanics (Physics Wallah)
* Hibbeler — Engineering Mechanics: Statics
* [`strength-of-materials.md`](strength-of-materials.md) — SOM fundamentals
* [`structural-analysis.md`](../structural-analysis/structural-analysis.md) — Structural analysis
* [`civil-engineering-foundations.md`](civil-engineering-foundations.md) — Foundation overview

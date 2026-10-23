# Strength of Materials (SOM)

> **Placement Priority:** P0 — Asked in EVERY civil engineering interview
> **GATE-O-PEDIA Reference:** Chapter 2 (1,851 lines, 15 topics, 19 formulas)
> **Canonical Page:** `02_core/civil-engineering/fundamentals/strength-of-materials.md`

---

## Scope

Strength of Materials (Mechanics of Materials) deals with the behavior of solid bodies subjected to stresses and strains. It is the foundation for structural design, RCC, steel, and geotechnical engineering.

| Domain | Relevance |
|--------|-----------|
| Structural Design | Bending, shear, torsion of members |
| RCC Design | Flexural capacity, shear capacity |
| Steel Design | Tension, compression, buckling |
| Geotechnical | Soil stress distribution |
| Interview | Most frequently tested civil topic |
| Software | FEA validation, hand-calc verification |

---

## 1. Stress & Strain

### Basic Definitions

| Quantity | Symbol | Formula | Units | Meaning |
|----------|--------|---------|-------|---------|
| Normal Stress | σ | P/A | MPa (N/mm²) | Force per unit area (normal to surface) |
| Shear Stress | τ | V/A | MPa | Force per unit area (parallel to surface) |
| Normal Strain | ε | δ/L | dimensionless (mm/mm) | Deformation per unit length |
| Shear Strain | γ | Δ/L | radians | Angular distortion |
| Young's Modulus | E | σ/ε | GPa (kN/mm²) | Stiffness in axial loading |
| Shear Modulus | G | τ/γ | GPa | Stiffness in shear |
| Poisson's Ratio | ν | -ε_lat/ε_long | dimensionless | Lateral/longitudinal strain ratio |
| Bulk Modulus | K | σ_hydro/ε_vol | GPa | Resistance to volumetric compression |

### Key Relationships

```
E = 2G(1 + ν)
E = 3K(1 - 2ν)
G = E / [2(1 + ν)]
```

### Stress-Strain Curve (Mild Steel)

```
                    Ultimate Stress (σ_u)
                   /|
                  / |
         Yield   /  |  Necking
        Point   /   |   /
       (σ_y)  /    |  /
             /     | /
            /      |/  Fracture
           /   C   |
          / --------  Upper Yield
         / |       
        /  |  Lower Yield  
       /   |  (perfectly plastic)
      /    |
     /     |  Proportional Limit
    /      |      |
   / Linear|      |
  / Elastic|      |
 /_________|______|_____________________
           ε_y    ε_u      ε_f
```

### Key Points on the Curve

| Point | Significance |
|-------|-------------|
| Proportional Limit | Hooke's law valid up to here |
| Elastic Limit | Beyond this, permanent deformation occurs |
| Upper Yield Point | Sudden drop in stress (dislocations break free) |
| Lower Yield Point | Constant stress during plastic flow |
| Ultimate Stress | Maximum stress before necking begins |
| Fracture Point | Material breaks |

### WHY is there an upper and lower yield point in mild steel?

**Physical reason:** Mild steel has interstitial carbon/nitrogen atoms that pin dislocations (Cottrell atmospheres). The upper yield point is the stress needed to "break free" of these pins. Once dislocations are mobile, less stress is needed — hence the lower yield point. This phenomenon is specific to low-carbon steels and does not occur in aluminum or high-carbon steel.

---

## 2. Mohr's Circle

### Construction

For a stress element with σ_x, σ_y, τ_xy:

```
Center: C = (σ_x + σ_y) / 2
Radius: R = √[((σ_x - σ_y)/2)² + τ_xy²]

σ₁ = C + R  (major principal stress)
σ₂ = C - R  (minor principal stress)

tan(2θ_p) = 2τ_xy / (σ_x - σ_y)
τ_max = R = (σ₁ - σ₂) / 2
```

### Unambiguous Sign Convention for Mohr's Circle

To plot Mohr's circle without confusion or coordinate ambiguity, follow the standard engineering sign convention (Timoshenko & Gere):

1. **Normal Stress ($\sigma$):**
   - Plotted on the **horizontal axis** ($\sigma$-axis).
   - **Tensile stress** is **POSITIVE** $\to$ plotted to the **right** of the origin ($+X$).
   - **Compressive stress** is **NEGATIVE** $\to$ plotted to the **left** of the origin ($-X$).

2. **Shear Stress ($\tau$):**
   - Plotted on the **vertical axis** ($\tau$-axis).
   - **Rotational Criterion:** Look at the shear stress arrow on the face under consideration. If the shear stress tends to rotate the element **CLOCKWISE (CW)** about the element's center, it is plotted **POSITIVE (ABOVE the $\sigma$-axis)**.
   - If the shear stress tends to rotate the element **COUNTER-CLOCKWISE (CCW)** about the center, it is plotted **NEGATIVE (BELOW the $\sigma$-axis)**.

| Face of Stress Element | Normal Stress Coordinate | Shear Stress Tendency | Point on Mohr's Circle |
| :--- | :--- | :--- | :--- |
| **Right Vertical Face ($+x$ face)** | $\sigma_x$ (Tension $= +$, Comp $= -$) | $\tau_{xy}$ (upward $\to$ CW $\to$ plot ABOVE) | $X\left(\sigma_x, \tau_{xy}\right)$ |
| **Top Horizontal Face ($+y$ face)** | $\sigma_y$ (Tension $= +$, Comp $= -$) | $\tau_{yx}$ (leftward $\to$ CCW $\to$ plot BELOW) | $Y\left(\sigma_y, -\tau_{xy}\right)$ |

> [!NOTE]
> Points $X$ and $Y$ are diametrically opposite. The line connecting $X$ and $Y$ intersects the horizontal axis at the center:
> $$C = \left(\frac{\sigma_x + \sigma_y}{2}, 0\right)$$
> The radius is the distance from $C$ to $X$:
> $$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$

### KEY INTERVIEW INSIGHT

**WHY is the angle on Mohr's circle $2\theta$ while the physical rotation is $\theta$?**
The $2\theta$ relationship arises directly from the trigonometric double-angle identities in the Cauchy stress transformation equations:
$$\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\theta + \tau_{xy}\sin 2\theta$$
$$\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin 2\theta + \tau_{xy}\cos 2\theta$$
When the physical stress element is rotated by an angle $\theta$, the radius vector on Mohr's circle rotates by $2\theta$ in the **exact same rotational direction** (e.g., rotating physical element $\theta$ counter-clockwise corresponds to rotating the radius on Mohr's circle by $2\theta$ counter-clockwise). This maps the orthogonal physical faces ($90^\circ$ apart) to diametrically opposite points ($180^\circ$ apart) on the circle!

---

## 3. Principal Stresses & Strains

### Principal Stresses (2D)

```
σ₁,₂ = (σ_x + σ_y)/2 ± √[((σ_x - σ_y)/2)² + τ_xy²]
```

### Principal Strains (2D)

```
ε₁ = (ε_x + ε_y)/2 + √[((ε_x - ε_y)/2)² + (γ_xy/2)²]
ε₂ = (ε_x + ε_y)/2 - √[((ε_x - ε_y)/2)² + (γ_xy/2)²]
```

### Von Mises Yield Criterion (for ductile materials)

```
σ_vm = √[σ₁² - σ₁σ₂ + σ₂²]
Yield occurs when σ_vm ≥ σ_y
```

### Maximum Shear Stress (Tresca)

```
τ_max = (σ₁ - σ₂) / 2
Yield occurs when τ_max ≥ σ_y/2
```

### WHAT-IF: What if σ₁ = σ₂ = σ?

Then τ_max = 0. The element is in **hydrostatic stress** — it cannot yield by shear regardless of how large σ is. This is why ductile metals don't yield under pure hydrostatic pressure (like deep ocean environments).

---

## 4. Bending of Beams

### Flexure Formula

```
σ = My / I

where:
  σ = bending stress at distance y from neutral axis
  M = bending moment at the section
  y = distance from neutral axis
  I = second moment of area (moment of inertia)
```

### Sign Convention

| Moment | Effect | Sign |
|--------|--------|------|
| Sagging | Bottom fiber in tension | Positive (+M) |
| Hogging | Top fiber in tension | Negative (-M) |

### Section Properties (Common Sections)

| Section | I (about major axis) | S = I/y_max |
|---------|---------------------|-------------|
| Rectangle (b×d) | bd³/12 | bd²/6 |
| Circle (dia D) | πD⁴/64 | πD³/32 |
| Hollow Circle (D,d) | π(D⁴-d⁴)/64 | π(D⁴-d⁴)/(32D) |
| Triangle (b×h) | bh³/36 | bh²/24 |

### Neutral Axis: First-Principles Derivation & Centroid Mechanics

The **Neutral Axis (NA)** is the longitudinal line or cross-sectional axis along which normal bending strain and normal bending stress are identically zero ($\epsilon = 0$, $\sigma = 0$).

#### Why Does the Neutral Axis Pass Through the Centroid?
Consider a prismatic beam subjected to pure bending moment $M$ (zero axial force $N = 0$).
1. **Bernoulli-Euler Hypothesis:** Plane sections normal to the longitudinal axis remain plane and perpendicular after bending. Consequently, normal strain $\epsilon(y)$ varies linearly with distance $y$ from the neutral surface:
   $$\epsilon(y) = \kappa \cdot y = \frac{y}{\rho}$$
   *(where $\kappa = 1/\rho$ is beam curvature).*
2. **Hooke's Law:** For a homogeneous, linear-elastic material with Young's modulus $E$:
   $$\sigma(y) = E \cdot \epsilon(y) = E \cdot \kappa \cdot y$$
3. **Axial Static Equilibrium:** Because no external axial load acts on the beam, the resultant normal force over the cross-section must vanish:
   $$\int_A \sigma(y) \, dA = 0 \implies \int_A (E \cdot \kappa \cdot y) \, dA = 0$$
   For a non-trivial curvature ($\kappa \ne 0$) and constant $E$:
   $$E \cdot \kappa \int_A y \, dA = 0 \implies \mathbf{\int_A y \, dA = 0}$$
   **Mathematical Conclusion:** The integral $\int_A y \, dA$ represents the **first moment of cross-sectional area** about the neutral axis. By mathematical definition, the first moment of area is zero **ONLY when measured about the centroid of the cross-section**!
   Therefore, for pure bending of a homogeneous material, **the neutral axis must pass through the centroid ($\bar{y}$) of the cross-sectional area**:
   $$\bar{y} = \frac{\sum A_i \bar{y}_i}{\sum A_i}$$

#### Behavior in Asymmetric and Composite Sections:
- **Asymmetric Homogeneous Sections (T-beams, Unsymmetrical I-beams, L-angles):**
  The neutral axis does *not* sit at mid-depth. Its position is determined strictly by the area centroid $\bar{y} = \sum A_i y_i / \sum A_i$. It sits closer to the region with greater concentrated area (e.g., in a T-beam, the NA is closer to the wide flange, meaning the web extreme fiber is further away ($y_{\text{web}} > y_{\text{flange}}$) and suffers much higher flexural stress $\sigma = M y / I$).
- **Composite / Multi-Material Sections (e.g., Flitched beams, Timber reinforced with steel plates):**
  When different materials are bonded together ($E_1 \ne E_2$), normal stress $\sigma(y) = E(y) \kappa y$.
  Equilibrium requires:
  $$\int_A E(y) y \, dA = 0 \implies \int_{A_1} E_1 y \, dA + \int_{A_2} E_2 y \, dA = 0$$
  Dividing by reference modulus $E_1$, define modular ratio $m = E_2 / E_1$:
  $$\int_{A_1} y \, dA + m \int_{A_2} y \, dA = \int_{A_{\text{trans}}} y \, dA = 0$$
  **The neutral axis passes through the centroid of the TRANSFORMED AREA** ($A_{\text{trans}} = A_1 + m A_2$). The stiffer material ($E_2 > E_1$) carries proportionally higher stress, shifting the elastic centroid toward itself.

### WHY does the flexure formula work?

**Physical reasoning:** When a beam bends, fibers on the convex side stretch (tension) and fibers on the concave side compress. The neutral axis is where neither stretching nor compression occurs. The stress varies linearly from zero at NA to maximum at the extreme fiber because strain varies linearly (plane sections remain plane — this is the **Bernoulli-Navier hypothesis**). Since $\sigma = E\epsilon$ and $E$ is constant, stress follows the same linear distribution.

**Assumptions of Simple Bending Theory:**
1. **Material Linearity:** Material is homogeneous, isotropic, and obeys Hooke's law in both tension and compression ($E_t = E_c$).
2. **Plane Sections Remain Plane:** Transverse sections remain plane and perpendicular to the neutral axis before and after bending (shear deformations neglected).
3. **Pure Bending:** The beam is subjected only to pure bending moments (transverse shear force is zero).
4. **Prismatic & Straight:** The beam is initially straight with constant cross-section throughout its span.
5. **Symmetric Bending:** The radius of curvature is large compared to cross-sectional dimensions, and bending occurs in a plane of symmetry.

---

## 5. Shear Stress in Beams

### General Formula

```
τ = VQ / (Ib)

where:
  V = shear force at the section
  Q = first moment of area above (or below) the point of interest
  I = second moment of area
  b = width of section at the point of interest
```

### Q Calculation

```
Q = A' × ȳ'

where:
  A' = area above the level where τ is being calculated
  ȳ' = distance from NA to centroid of A'
```

### Shear Stress Distribution

| Section | Distribution | Max τ Location | τ_max |
|---------|-------------|---------------|-------|
| Rectangle | Parabolic | At NA | 3V/(2A) |
| Circle | Parabolic-ish | At NA | 4V/(3A) |
| I-beam | Almost uniform in web | At NA | V/A_web (approx) |

### Comparison: Bending vs Shear

| Property | Bending Stress (σ) | Shear Stress (τ) |
|----------|-------------------|-----------------|
| Distribution | Linear across depth | Parabolic across depth |
| Maximum | At extreme fibers | At neutral axis |
| At NA | Zero | Maximum |
| At extreme fibers | Maximum | Zero |
| Formula | σ = My/I | τ = VQ/Ib |
| Governs design for | Long spans | Short spans, deep beams |

---

## 6. Torsion

### Torsion of Circular Shafts

```
τ = Tr / J

θ = TL / (GJ)

where:
  T = applied torque
  r = radial distance from center
  J = polar moment of inertia
  L = length of shaft
  G = shear modulus
  θ = angle of twist (radians)
```

### Section Properties

| Section | J |
|---------|---|
| Solid circle (radius R) | πR⁴/2 = πD⁴/32 |
| Hollow circle (R, r) | π(R⁴-r⁴)/2 |

### Key Insights

- Maximum shear stress occurs at the **outer surface** (r = R)
- At the center (r = 0), shear stress = 0
- Stress varies **linearly** from center to surface
- **Thin-walled hollow sections** are most efficient for torsion (material is far from center)

### WHAT-IF: What if a non-circular section (square, rectangle) is subjected to torsion?

The **warping** of cross-sections means plane sections do NOT remain plane. The torsion formula τ = Tr/J does **NOT apply**. Instead:
- Maximum shear stress occurs at the **midpoint of the longest side** (not at the corner)
- Corners have **zero** shear stress
- warping restraint creates additional normal stresses
- Solutions require membrane analogy or numerical methods

---

## 7. Deflection of Beams

### Differential Equation of the Elastic Curve

```
EI (d²y/dx²) = M(x)

Integrating:
EI (dy/dx) = ∫M(x)dx + C₁     [slope equation]
EI y = ∫∫M(x)dx² + C₁x + C₂  [deflection equation]
```

### Standard Deflection Formulas

| Loading | Beam Type | δ_max | Location |
|---------|-----------|-------|----------|
| Point load P at center | Simply supported | PL³/(48EI) | Mid-span |
| Point load P at distance a from left | Simply supported | Pa²b²/(3EIL) | Under load |
| UDL w over full span | Simply supported | 5wL⁴/(384EI) | Mid-span |
| Point load P at free end | Cantilever | PL³/(3EI) | Free end |
| UDL w over full span | Cantilever | wL⁴/(8EI) | Free end |
| Moment M₀ at one end | Simply supported | M₀L²/(9√3 EI) | At x = L/√3 |

### Methods of Finding Deflection

| Method | Best For | Key Idea |
|--------|----------|----------|
| Double Integration | Simple beams, uniform sections | Integrate M(x) twice |
| Macaulay's Method | Beams with multiple loads | Singularity functions |
| Moment-Area | Slope/deflection at specific points | Area of M/EI diagram |
| Conjugate Beam | Complex loading | M/EI diagram as load on fictitious beam |
| Castigliano's | Deflection at a point under a load | ∂U/∂P = δ |
| Virtual Work | Deflection at any point | 1·δ = ∫(mM/EI)dx |

### Comparison: Simply Supported vs Cantilever Deflection

| Parameter | Simply Supported (UDL) | Cantilever (UDL) |
|-----------|----------------------|------------------|
| δ_max | 5wL⁴/(384EI) | wL⁴/(8EI) |
| Ratio (Cantilever/SS) | — | **48/5 = 9.6×** |
| Max slope | wL³/(24EI) at supports | wL³/(6EI) at free end |
| Zero deflection at | Both supports | Fixed end only |

---

## 8. Combined Loading

### Combined Axial + Bending

```
σ = P/A ± My/I

Maximum tensile stress: σ_max = P/A + Mc/I
Maximum compressive stress: σ_min = P/A - Mc/I (may be negative)
```

### Combined Bending + Torsion (Equivalent Moment)

```
M_eq = ½[M + √(M² + T²)]    (Maximum Principal Stress Theory)
M_eq = √(M² + T²)            (Maximum Shear Stress Theory)
```

---

## 9. Thin & Thick Cylinders

### Thin Cylinder (t < D/20)

```
Hoop stress: σ_h = pd/(2t)
Longitudinal stress: σ_l = pd/(4t)
Volumetric strain: ε_v = pd/(4tE)(5 - 4ν)
```

**Key insight:** Hoop stress is ALWAYS twice the longitudinal stress. This is why cylindrical pressure vessels fail along a longitudinal seam (hoop stress governs).

### Thick Cylinder (Lamé's Equations)

```
σ_r = A - B/r²
σ_h = A + B/r²

At inner radius (r = r_i): σ_r = -p_i
At outer radius (r = r_o): σ_r = -p_o
```

### Comparison: Thin vs Thick Cylinder

| Aspect | Thin Cylinder | Thick Cylinder |
|--------|--------------|---------------|
| Assumption | Hoop stress uniform across thickness | Hoop stress varies with radius |
| Hoop stress formula | pd/(2t) | Lamé's equation (hyperbolic) |
| When to use | t/D < 1/20 | t/D ≥ 1/20 |
| Maximum stress | At inner surface (constant) | At inner surface (varies with r) |

---

## 10. Column Buckling

### Euler's Critical Load

```
P_cr = π²EI / (Le)²

where Le = effective length
```

### Effective Length

| End Condition | Le |
|---------------|-----|
| Both ends pinned | L |
| One fixed, one free | 2L |
| Both ends fixed | L/2 |
| One fixed, one pinned | L/√2 ≈ 0.707L |

### Slenderness Ratio

```
λ = Le / r_min

where r_min = √(I_min/A) = radius of gyration
```

### Short vs Long Columns

| Type | Slenderness | Failure Mode | Formula |
|------|------------|-------------|---------|
| Short | λ < ~30 | Crushing | σ = P/A (material strength) |
| Intermediate | ~30 < λ < ~120 | Combined | Rankine formula |
| Long | λ > ~120 | Buckling | Euler formula |

### Rankine Formula (practical)

```
1/P_R = 1/P_cr + 1/P_c

where:
  P_cr = Euler critical load
  P_c = crushing load = σ_c × A
  Rankine constant a = σ_c / (π²E)
```

### WHY does a long column buckle but a short column crushes?

**Physical reasoning:** In a long, slender column, the slightest lateral perturbation creates a bending moment (P × δ). This bending moment causes additional deflection, which increases the moment further — a positive feedback loop. At the Euler load, this feedback becomes self-sustaining and the column buckles suddenly. In a short, stocky column, the material reaches its crushing strength before the buckling feedback loop can develop.

---

## 11. Theories of Failure

### For Ductile Materials

| Theory | Criterion | Best For |
|--------|-----------|----------|
| Maximum Shear Stress (Tresca) | τ_max = σ₁-σ₃)/2 ≥ σ_y/2 | Conservative design |
| Von Mises (Distortion Energy) | σ_vm ≥ σ_y | Most accurate for ductile metals |

### For Brittle Materials

| Theory | Criterion | Best For |
|--------|-----------|----------|
| Maximum Principal Stress (Rankine) | σ₁ ≥ σ_ut | Brittle materials |
| Mohr's Theory | Uses Mohr's envelope | Most accurate for brittle |

### Comparison: Tresca vs Von Mises

| Aspect | Tresca | Von Mises |
|--------|--------|-----------|
| Conservatism | More conservative | Less conservative |
| Accuracy | Good | Better for ductile metals |
| Computation | Simpler | Slightly more complex |
| Criterion | τ_max = (σ₁-σ₃)/2 | σ_vm = √(σ₁²-σ₁σ₂+σ₂²) |
| Used in | General design | Precise design (FEA) |

---

## 📋 Formula Sheet

| Formula | Variables | Application |
|---------|-----------|-------------|
| σ = P/A | P force, A area | Axial stress |
| τ = VQ/(Ib) | V shear, Q first moment, I MOI, b width | Shear stress in beams |
| σ = My/I | M moment, y distance, I MOI | Bending stress |
| τ = Tr/J | T torque, r radius, J polar MOI | Torsion |
| δ = PL³/(48EI) | P load, L span, E modulus, I MOI | Center deflection (SS beam) |
| P_cr = π²EI/(Le)² | E modulus, I MOI, Le effective length | Euler buckling |
| σ_h = pd/(2t) | p pressure, d diameter, t thickness | Thin cylinder hoop stress |
| 1/P_R = 1/P_cr + 1/P_c | Euler + crushing loads | Rankine column |

---

## 🗺️ Subject Roadmap

```
Stress & Strain (Foundation)
  ├── Mohr's Circle
  ├── Principal Stresses
  └── Failure Theories
Bending
  ├── Flexure Formula
  ├── Section Properties
  └── Neutral Axis
Shear
  ├── Shear Stress Distribution
  └── Q Calculation
Torsion
  ├── Circular Shafts
  └── Non-Circular Sections
Deflection
  ├── Double Integration
  ├── Moment-Area
  └── Castigliano's
Combined Loading
Thin/Thick Cylinders
Column Buckling
```

---

## 🔗 Cross-Links

| Topic | Related Page |
|-------|-------------|
| Bending → RCC Design | [`02_core/civil-engineering/rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Bending → Steel Beams | [`02_core/civil-engineering/steel/steel-design.md`](../steel/steel-design.md) |
| Buckling → Steel Columns | [`02_core/civil-engineering/steel/steel-design.md`](../steel/steel-design.md) |
| Stress Distribution → Soil | [`02_core/civil-engineering/geotechnical/geotechnical.md`](../geotechnical/geotechnical.md) |
| Torsion → Shafts | [`02_core/foundamentals/engineering-mechanics.md`](engineering-mechanics.md) |
| Deflection → Structural Analysis | [`02_core/civil-engineering/structural-analysis/structural-analysis.md`](../structural-analysis/structural-analysis.md) |

---

## Interview Questions

### A. Basic Questions

1. **What is the difference between stress and strain?**
   - Stress (σ) = Force per unit area (N/mm²). Strain (ε) = Deformation per unit length (dimensionless). Stress causes strain through the material's stiffness (E = σ/ε).

2. **What is Young's Modulus and what does it physically represent?**
   - E is the slope of the stress-strain curve in the elastic region. Physically, it represents the stiffness of a material — how much stress is needed to produce a unit strain. Higher E = stiffer material (steel E ≈ 200 GPa vs aluminum E ≈ 70 GPa).

3. **Explain Mohr's Circle and its significance.**
   - Mohr's Circle is a graphical representation of the state of stress at a point. It allows quick determination of principal stresses, maximum shear stress, and stress on any inclined plane. It transforms the stress transformation equations into a circle in σ-τ space.

4. **What is the difference between elastic and plastic deformation?**
   - Elastic deformation is recoverable — the material returns to its original shape when load is removed (Hooke's law: σ = Eε). Plastic deformation is permanent — the material retains its deformed shape after load removal. The transition occurs at the yield point.

5. **Define Poisson's ratio and its typical values.**
   - ν = -lateral strain / longitudinal strain. For most metals: ν ≈ 0.25-0.35. For rubber: ν ≈ 0.5 (incompressible). For cork: ν ≈ 0 (no lateral expansion). Theory limits: -1 ≤ ν ≤ 0.5.

### B. Conceptual Questions

6. **Why is the bending stress maximum at extreme fibers and zero at the neutral axis?**
   - From the Bernoulli hypothesis, plane sections remain plane, so strain varies linearly with distance from NA: ε = y/ρ (where ρ is radius of curvature). Since σ = Eε, stress also varies linearly. At y=0 (NA), stress = 0. At y=y_max (extreme fiber), stress is maximum.

7. **Why is the shear stress distribution parabolic for a rectangular beam?**
   - Shear stress τ = VQ/(Ib). For a rectangle, Q = (b/2)(d²/4 - y²) which is a quadratic function of y. Thus τ varies parabolically, maximum at y=0 (NA) and zero at y=±d/2 (extreme fibers).

8. **What is the difference between a thin and thick cylinder?**
   - In a thin cylinder (t < D/20), hoop stress is assumed uniform across the wall thickness: σ_h = pd/(2t). In a thick cylinder (t ≥ D/20), hoop stress varies with radius per Lamé's equations, maximum at the inner surface.

9. **Why does Euler's formula not apply to short columns?**
   - Euler's formula assumes the column fails by elastic buckling (lateral instability). Short columns fail by material crushing (compression failure) before buckling can occur. The transition occurs at a slenderness ratio of approximately 120 for steel.

10. **What is the physical meaning of the moment of inertia (I) in bending?**
    - I represents the geometric resistance of a cross-section to bending. A larger I means more material is distributed far from the neutral axis, making the section stiffer and stronger in bending. It's analogous to mass moment of inertia (resistance to rotation) but for cross-sectional geometry.

### C. WHY Questions

11. **Why does a hollow circular section have a higher polar moment of inertia than a solid one of the same area?**
    - Material placed further from the center contributes more to J (since J = ∫r²dA). A hollow section moves material outward, increasing r² contribution while maintaining the same area. This is why hollow shafts are more efficient in torsion.

12. **Why is the maximum shear stress in a rectangular beam at the neutral axis, not at the surface?**
    - Shear stress depends on Q (first moment of area above the point). At the NA, Q is maximum because the entire area above contributes. At the surface, Q = 0 (no area above). Hence τ = VQ/(Ib) is maximum at NA.

13. **Why does mild steel show an upper and lower yield point but aluminum does not?**
    - Mild steel has interstitial carbon/nitrogen atoms that pin dislocations (Cottrell atmospheres). The upper yield is the stress needed to break free; the lower yield is the stress for continued plastic flow. Aluminum lacks these interstitial pins, so its yield transition is smooth.

### D. WHAT-IF Questions

14. **What if you double the span of a simply supported beam with UDL?**
    - δ_max = 5wL⁴/(384EI). If L doubles, δ increases by factor of 2⁴ = 16. The beam deflects 16 times more! This is why long-span beams need much deeper sections.

15. **What if the cross-section is changed from rectangular to circular (same area)?**
    - For same area, I_circle < I_rectangle (circle has less material at extreme distances). So the circular beam is weaker in bending but has the advantage of equal bending resistance in all directions.

16. **What if a column's effective length is reduced by adding intermediate bracing?**
    - P_cr = π²EI/(Le)². If Le is halved by mid-height bracing, P_cr increases by factor of 4. This is why bracing is extremely effective for improving column capacity.

### E. Comparison Questions

| A | B | Key Distinction |
|---|---|-----------------|
| Stress (σ) | Strain (ε) | Cause vs effect; σ = Eε |
| Young's Modulus (E) | Shear Modulus (G) | Axial vs shear stiffness; E = 2G(1+ν) |
| Bending stress | Shear stress | σ varies linearly, τ parabolically; σ max at surface, τ max at NA |
| Thin cylinder | Thick cylinder | t/D ratio; uniform vs varying hoop stress |
| Euler buckling | Rankine buckling | Long columns vs short/intermediate columns |
| Tresca | Von Mises | Conservative vs accurate yield criterion |
| Upper yield point | Lower yield point | Dislocation pinning vs free flow |
| Mohr's Circle (stress) | Mohr's Circle (strain) | σ-τ space vs ε-γ/2 space |

---

## Numerical Practice

### Example 1: Stress in a Bar Under Axial Load

**Problem:** A mild steel bar of 40 mm diameter and 2 m length is subjected to an axial pull of 100 kN. If E = 200 GPa, find: (a) stress, (b) strain, (c) elongation.

**Solution:**

```
(a) σ = P/A = 100×10³ / (π/4 × 40²) = 100,000 / 1256.6 = 79.6 MPa

(b) ε = σ/E = 79.6 / (200×10³) = 0.000398 = 398 με

(c) δ = εL = 0.000398 × 2000 = 0.796 mm
```

**Interview follow-up:** Would the bar elongate or shorten if the load were compressive? (Shorten — same magnitude, opposite direction. But buckling might occur if the bar is slender.)

### Example 2: Bending Stress in a Simply Supported Beam

**Problem:** A simply supported beam of span 4 m carries a point load of 20 kN at mid-span. The cross-section is rectangular 150 mm × 300 mm. Find the maximum bending stress.

**Solution:**

```
M_max = PL/4 = 20×4/4 = 20 kN·m = 20×10⁶ N·mm

I = bd³/12 = 150×300³/12 = 337.5×10⁶ mm⁴

y_max = d/2 = 150 mm

σ_max = My/I = (20×10⁶ × 150) / (337.5×10⁶) = 8.89 MPa
```

**Interview follow-up:** If we orient the beam with the 300 mm dimension vertical vs horizontal, how does the maximum stress change? (With 300 vertical: I = 150×300³/12 = 337.5×10⁶, σ = 8.89 MPa. With 150 vertical: I = 300×150³/12 = 84.375×10⁶, σ = 35.6 MPa. Four times higher! This is why beams are oriented with the strong axis vertical.)

### Example 3: Torsion of a Hollow Shaft

**Problem:** A hollow circular shaft has outer diameter 100 mm and inner diameter 60 mm. If the permissible shear stress is 50 MPa, find the maximum torque it can transmit.

**Solution:**

```
J = π(D⁴-d⁴)/32 = π(100⁴-60⁴)/32 = π(100,000,000-12,960,000)/32 = 8,542,832 mm⁴

τ_max = T×R/J → T = τ_max × J / R

T = 50 × 8,542,832 / 50 = 8,542,832 N·mm ≈ 8.54 kN·m
```

**Interview follow-up:** If we use a solid shaft of the same weight (same area), what would be its torque capacity? (A_solid = A_hollow → πD²/4 = π(100²-60²)/4 = 5,027 mm² → D_solid = 79.8 mm. J_solid = π×79.8⁴/32 = 3,966,212 mm⁴. T_solid = 50×3,966,212/39.9 = 4,973,952 N·mm ≈ 4.97 kN·m. The hollow shaft transmits 72% more torque for the same weight!)

### Example 4: Column Buckling

**Problem:** A steel column of 3 m length has both ends fixed. If E = 200 GPa and the cross-section is a hollow circle with D = 150 mm, d = 100 mm, find the Euler buckling load.

**Solution:**

```
I = π(D⁴-d⁴)/64 = π(150⁴-100⁴)/64 = π(506,250,000-100,000,000)/64 = 19,948,400 mm⁴

Le = L/2 = 3000/2 = 1500 mm (both ends fixed)

P_cr = π²EI/(Le)² = π² × 200,000 × 19,948,400 / (1500)²

P_cr = 19,739,200 × 19,948,400 / 2,250,000 = 174,736,000 N ≈ 174.7 MN
```

**Interview follow-up:** If we remove the fixed support at one end (making it pinned-pinned), the effective length becomes Le = L = 3000 mm. P_cr decreases by factor of 4 to ~43.7 MN. This shows how boundary conditions dramatically affect buckling capacity.

---

## 📋 Quick Revision Checklist

- [ ] Stress-strain curve for mild steel (all key points)
- [ ] Hooke's law and elastic constants (E, G, K, ν relationships)
- [ ] Mohr's circle construction (center, radius, principal stresses)
- [ ] Flexure formula σ = My/I
- [ ] Shear stress formula τ = VQ/Ib
- [ ] Torsion formula τ = Tr/J
- [ ] Standard deflections (simply supported, cantilever — point load, UDL)
- [ ] Euler buckling load and effective lengths
- [ ] Thin cylinder hoop stress = pd/(2t)
- [ ] Von Mises yield criterion
- [ ] Tresca yield criterion
- [ ] Combined loading superposition principle

---

## References

- GATE-O-PEDIA — Civil Engineering, Physics Wallah, Chapter 2
- Timoshenko & Gere, *Mechanics of Materials*
- Beer & Johnston, *Mechanics of Materials*
- IS 456:2000 (for bending design provisions)
- IS 800:2007 (for steel design provisions)

---

*This page follows the placement-first transformation of GATE-O-PEDIA fundamentals into interview-ready content with WHY, WHAT-IF, comparison, numerical, and revision coverage.*

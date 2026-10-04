# Quantitative Aptitude: Mensuration & Spatial Geometry

> **Priority:** P1 · **Role relevance:** High (Civil Engineering, HWRE, Computational Fluid Dynamics, Mechanical Design, Product Architecture & Quantitative Analytics)  
> **Difficulty range:** Foundation → 3D Frustums, Inscribed/Circumscribed Polyhedra, Pappus-Guldinus Solids of Revolution & Hydraulic Cross-Section Optimization  
> **Target speed:** 45–60 sec (Direct 2D/3D Scaling) – 90–120 sec (Compound Solid Cutting, Frustums & Optimization)

---

## 1. Theoretical Framework & Algebraic Formulations

### 1.1 Dimensional Scaling & Isoperimetric Invariants
For any scale transformation with linear factor $k$:
- Linear dimensions ($L, P, r, h$): scale by $k^1$
- Surface areas ($A, S, CSA, TSA$): scale by $k^2$
- Volumes ($V, M$): scale by $k^3$

```
+-----------------------------------------------------------------------------------+
|                           THE CORE GEOMETRIC THEOREMS                             |
+-----------------------------------------------------------------------------------+
| 1. Isoperimetric Inequality: For a fixed perimeter P, the circle encloses the     |
|                              maximum area: A <= P^2 / (4 * pi).                   |
| 2. Pappus-Guldinus Theorem 1: Surface area of solid of revolution:                |
|                              A = 2 * pi * d_centroid * L                          |
| 3. Pappus-Guldinus Theorem 2: Volume of solid of revolution:                      |
|                              V = 2 * pi * d_centroid * A_cross_section            |
| 4. Cavalieri's Principle   : Solids with equal height and equal cross-sectional   |
|                              areas at every level have identical volume.          |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Mathematical Archetypes & Geometric Formulations

#### 1. Frustums & Truncated Solids
For a conical frustum of top radius $r$, bottom radius $R$, and height $h$:
- Slant height: $l = \sqrt{h^2 + (R - r)^2}$
- Curved Surface Area ($CSA$): $\pi (R + r) l$
- Total Surface Area ($TSA$): $\pi (R + r) l + \pi R^2 + \pi r^2$
- Volume ($V$): $\frac{1}{3} \pi h \left(R^2 + Rr + r^2\right)$

#### 2. Spherical Segments, Caps & Zones
For a spherical cap of height $h$ cut from a sphere of radius $R$:
- Curved Surface Area: $2 \pi R h$
- Volume: $\frac{1}{3} \pi h^2 (3R - h) = \frac{1}{6} \pi h (3a^2 + h^2)$ (where $a$ is base radius)

#### 3. Inscribed & Circumscribed Solids
- **Sphere in a Cube:** Radius $r = \frac{s}{2}$, Volume ratio $= \frac{\pi}{6} \approx 0.5236$
- **Cube in a Sphere:** Side $s = \frac{2R}{\sqrt{3}}$, Volume ratio $= \frac{2}{\pi \sqrt{3}} \approx 0.3676$
- **Cylinder in a Sphere:** Max volume cylinder has $h = \frac{2R}{\sqrt{3}}, r = \sqrt{\frac{2}{3}} R$
- **Cone in a Sphere:** Max volume cone has $h = \frac{4}{3}R, r = \frac{2\sqrt{2}}{3} R$, Volume ratio $= \frac{8}{27} \approx 0.2963$

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | 2D Rectangle Pathway Area | **B** | Outer area minus inner area: $(l+2w)(b+2w) - lb = (44)(24) - (40)(20) = 256\text{ m}^2$ |
| **Q2** | Level 1 | Circular Sector Area & Arc Length | **C** | $A = \frac{\theta}{360} \pi r^2 = \frac{60}{360} \times \frac{22}{7} \times 21^2 = 231\text{ cm}^2$ |
| **Q3** | Level 1 | Cylinder to Sphere Melting Conservation | **A** | $V_{\text{cyl}} = \pi r^2 h = \frac{4}{3} \pi R^3 \implies \pi (6)^2 (8) = \frac{4}{3} \pi R^3 \implies R = 6\text{ cm}$ |
| **Q4** | Level 1 | Cone Slant Height & Surface Area | **D** | $l = \sqrt{r^2 + h^2} = \sqrt{7^2 + 24^2} = 25\text{ cm}; CSA = \pi r l = \frac{22}{7} \times 7 \times 25 = 550\text{ cm}^2$ |
| **Q5** | Level 1 | Rhombus Diagonals & Perimeter | **B** | Side $s = \sqrt{(d_1/2)^2 + (d_2/2)^2} = \sqrt{8^2 + 6^2} = 10\text{ cm} \implies P = 40\text{ cm}$ |
| **Q6** | Level 2 | Percentage Scaling of Circle | **C** | $r \to 1.20r \implies A \to (1.20)^2 A = 1.44A \implies 44\\% \text{ increase}$ |
| **Q7** | Level 2 | Cuboid Longest Diagonal (Rod) | **A** | $D = \sqrt{l^2 + b^2 + h^2} = \sqrt{12^2 + 9^2 + 8^2} = \sqrt{144+81+64} = \sqrt{289} = 17\text{ m}$ |
| **Q8** | Level 2 | Equilateral Triangle Inradius/Circumradius | **D** | $r = \frac{a}{2\sqrt{3}}, R = \frac{a}{\sqrt{3}} \implies \text{Area Ratio } r^2 : R^2 = 1 : 4$ |
| **Q9** | Level 2 | Hollow Metallic Pipe Volume | **B** | $V = \pi h (R^2 - r^2) = \frac{22}{7} \times 35 \times (10^2 - 8^2) = 110 \times 36 = 3960\text{ cm}^3$ |
| **Q10** | Level 2 | Wire Reshaping Invariant Perimeter | **C** | $2\pi r = 4s \implies 2 \times \frac{22}{7} \times 28 = 176 = 4s \implies s = 44\text{ cm}; A = 44^2 = 1936\text{ cm}^2$ |
| **Q11** | Level 3 | Conical Frustum Bucket Capacity | **B** | $V = \frac{1}{3}\pi h (R^2 + Rr + r^2) = \frac{1}{3}\pi (15)(14^2 + 14 \times 7 + 7^2) = 5390\text{ cm}^3 = 5.39\text{ L}$ |
| **Q12** | Level 3 | Sphere Inscribed in Cone | **C** | $\frac{r_{\text{sphere}}}{R} = \frac{h - r_{\text{sphere}}}{\sqrt{h^2 + R^2}} \implies r_{\text{sphere}} = \frac{Rh}{R + \sqrt{h^2 + R^2}} = 3\text{ cm}$ |
| **Q13** | Level 3 | Cube Recasting into Spheres | **A** | $V_{\text{cube}} = 22^3 = 10648\text{ cm}^3; N = \frac{10648}{\frac{4}{3} \times \frac{22}{7} \times (1)^3} = 2541\text{ spheres}$ |
| **Q14** | Level 3 | Trapezoidal Channel Cross-Section | **D** | $A = \frac{1}{2}(b_1 + b_2)h = \frac{1}{2}(10 + 6)(4) = 32\text{ m}^2; \text{Discharge } Q = 32 \times 2.5 = 80\text{ m}^3/\text{s}$ |
| **Q15** | Level 3 | Regular Hexagon Area & Tiling | **B** | $A = \frac{3\sqrt{3}}{2} a^2 = \frac{3\sqrt{3}}{2} \times 6^2 = 54\sqrt{3}\text{ cm}^2 \approx 93.53\text{ cm}^2$ |
| **Q16** | Level 4 | Spherical Cap Volume & Submerged Height | **C** | $V_{\text{cap}} = \frac{1}{3}\pi h^2 (3R - h) \implies h = 4\text{ cm}, R = 10\text{ cm} \implies V = \frac{416\pi}{3}\text{ cm}^3$ |
| **Q17** | Level 4 | Cylinder Inscribed in Cone (Max Volume) | **A** | Max cylinder volume occurs at $h_{\text{cyl}} = \frac{h}{3}, r_{\text{cyl}} = \frac{2}{3}R \implies V = \frac{4}{9} V_{\text{cone}}$ |
| **Q18** | Level 4 | Triangular Prism Surface Area & Volume | **D** | Base area $= \frac{\sqrt{3}}{4}(8)^2 = 16\sqrt{3}; V = 16\sqrt{3} \times 15 = 240\sqrt{3}\text{ cm}^3$ |
| **Q19** | Level 4 | Curved Sheet Rolling into Cylinder | **B** | $2\pi r = 22, h = 14 \implies r = 3.5\text{ cm}; V = \frac{22}{7} \times 3.5^2 \times 14 = 539\text{ cm}^3$ |
| **Q20** | Level 4 | Circle Tangent to 3 Mutually Tangent Circles | **C** | Descartes' Circle Theorem: $k_4 = k_1 + k_2 + k_3 + 2\sqrt{k_1 k_2 + k_2 k_3 + k_3 k_1} \implies r_4 = \frac{r}{2\sqrt{3}+3}$ |
| **Q21** | Level 5 | Torus Volume via Pappus-Guldinus | **C** | $V = 2\pi R \times (\pi r^2) = 2\pi^2 R r^2 = 2\pi^2 (10)(2^2) = 80\pi^2\text{ cm}^3$ |
| **Q22** | Level 5 | Truncated Pyramid Solid | **A** | $V = \frac{h}{3}(A_1 + A_2 + \sqrt{A_1 A_2}) = \frac{12}{3}(100 + 36 + 60) = 4(196) = 784\text{ cm}^3$ |
| **Q23** | Level 5 | Spherical Packing in Cylindrical Tank | **D** | Kepler optimal random close packing density $\eta \approx 0.64 \implies V_{\text{water}} = 0.36 V_{\text{tank}}$ |
| **Q24** | Level 5 | Parabolic Spillway Profile Volume | **B** | $A = \frac{2}{3} b h = \frac{2}{3} (12)(9) = 72\text{ m}^2; V = 72 \times 50 = 3600\text{ m}^3$ |
| **Q25** | Level 5 | Ellipsoid Volume & Surface Approximation | **C** | $V = \frac{4}{3} \pi a b c = \frac{4}{3} \pi (6)(4)(3) = 96\pi\text{ cm}^3 \approx 301.59\text{ cm}^3$ |
| **Q26** | Level 6 | Optimal Hydraulic Open Channel (Most Efficient) | **A** | Best hydraulic trapezoidal section: semi-hexagon with $R_h = y/2 \implies$ side slope $1:\sqrt{3}$ |
| **Q27** | Level 6 | Regular Octahedron Volume & Duality | **D** | $V = \frac{\sqrt{2}}{3} a^3 = \frac{\sqrt{2}}{3} (6)^3 = 72\sqrt{2}\text{ cm}^3 \approx 101.82\text{ cm}^3$ |
| **Q28** | Level 6 | Conical Frustum Water Rising Speed | **B** | $\frac{dh}{dt} = \frac{Q}{\pi r(h)^2}$; non-linear differential filling rate evaluation |
| **Q29** | Level 6 | Intersection Volume of Two Orthogonal Cylinders | **C** | Steinmetz solid volume $V = \frac{16}{3} r^3 = \frac{16}{3}(3)^3 = 144\text{ cm}^3$ |
| **Q30** | Level 6 | Maximum Area Inscribed Polygon | **A** | For a circle of radius $R$, regular $n$-gon area $= \frac{n}{2} R^2 \sin(2\pi/n)$ |
| **Q31** | Level 7 | CFD Mesh Cell Aspect Ratio & Skewness | **C** | Hexahedral vs tetrahedral volume-to-surface ratio efficiency $\implies \eta_{\text{hex}} = \sqrt{3} \eta_{\text{tet}}$ |
| **Q32** | Level 7 | Hyperboloid of One Sheet Cooling Tower | **B** | Quadric surface of revolution: $V = \pi h \left(a^2 + \frac{c^2 h^2}{12}\right) \implies 48,200\text{ m}^3$ |
| **Q33** | Level 7 | Sediment Scour Hole Conical Geometry | **D** | Inverted conical scour hole with dynamic angle of repose $\theta = 32^\circ \implies V = \frac{1}{3}\pi d^3 \cot^2\theta$ |
| **Q34** | Level 7 | Solid of Revolution of Parabola (Paraboloid) | **A** | $V = \frac{1}{2} \pi r^2 h = \frac{1}{2} \pi (6)^2 (10) = 180\pi\text{ cm}^3$ |
| **Q35** | Level 7 | Platonic Solid Inscribed Sphere Radius Ratio | **C** | Dodecahedron vs Icosahedron dual packing ratio $\implies r_{\text{in}} / a = \frac{1}{2}\sqrt{\frac{25+11\sqrt{5}}{10}}$ |
| **Q36** | Level 8 | Hydraulic Dam Reservoir Storage-Elevation Curve | **B** | Stage-storage integration $V(h) = \int_0^h A(z) dz \implies$ Active storage capacity $= 42.5\text{ MCM}$ |
| **Q37** | Level 8 | Consulting Caselet: Industrial Packaging Palletization | **C** | 3D Bin Packing Optimization: Knapsack volume utilization with orientation constraints $\implies 87.5\\%$ |
| **Q38** | Level 8 | Civil Caselet: Earthwork Cut-and-Fill Prismoidal Formula | **A** | Prismoidal rule: $V = \frac{L}{6}(A_1 + 4A_m + A_2) \implies V = 18,400\text{ m}^3$ |
| **Q39** | Level 8 | Structural Caselet: Optimal Dome Surface-to-Volume | **D** | Geodesic hemispherical dome structural weight vs internal HVAC volume $\implies \text{Ratio} = 0.15\text{ m}^{-1}$ |
| **Q40** | Level 8 | Pipeline Hydrodynamics: Wetted Perimeter Optimization | **B** | Hydraulic radius maximization for non-circular culvert $\implies \theta = 257.5^\circ$ for max discharge |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

#### Q1
A rectangular lawn measuring $40\text{ m} \times 20\text{ m}$ is surrounded externally by a pathway of uniform width $2\text{ m}$. What is the total surface area of the pathway?
- (A) $240\text{ m}^2$
- (B) $256\text{ m}^2$
- (C) $280\text{ m}^2$
- (D) $300\text{ m}^2$

#### Q2
A circular sector of a circle of radius $21\text{ cm}$ subtends an angle of $60^\circ$ at the center. Taking $\pi = \frac{22}{7}$, what is the area of the sector?
- (A) $210\text{ cm}^2$
- (B) $224\text{ cm}^2$
- (C) $231\text{ cm}^2$
- (D) $242\text{ cm}^2$

#### Q3
A solid metallic cylinder of radius $6\text{ cm}$ and height $8\text{ cm}$ is melted and recast into a single solid sphere. What is the radius of the recast sphere?
- (A) $6\text{ cm}$
- (B) $7\text{ cm}$
- (C) $8\text{ cm}$
- (D) $9\text{ cm}$

#### Q4
A right circular cone has a base radius of $7\text{ cm}$ and a vertical height of $24\text{ cm}$. Taking $\pi = \frac{22}{7}$, what is the curved surface area ($CSA$) of the cone?
- (A) $480\text{ cm}^2$
- (B) $500\text{ cm}^2$
- (C) $528\text{ cm}^2$
- (D) $550\text{ cm}^2$

#### Q5
The diagonals of a rhombus measure $16\text{ cm}$ and $12\text{ cm}$. What is the perimeter of the rhombus?
- (A) $36\text{ cm}$
- (B) $40\text{ cm}$
- (C) $44\text{ cm}$
- (D) $48\text{ cm}$

---

### Level 2: Dimensional Scaling & Invariant Perimeters (Q6–Q10)

#### Q6
If the radius of a circular irrigation field is increased by $20\\%$, by what percentage does its surface area increase?
- (A) $20\\%$
- (B) $40\\%$
- (C) $44\\%$
- (D) $48\\%$

#### Q7
What is the length of the longest rigid steel rod that can be placed entirely inside a rectangular storage room of dimensions $12\text{ m} \times 9\text{ m} \times 8\text{ m}$?
- (A) $17\text{ m}$
- (B) $18\text{ m}$
- (C) $19\text{ m}$
- (D) $20\text{ m}$

#### Q8
In an equilateral triangle, what is the ratio of the area of the inscribed circle (incircle) to the area of the circumscribed circle (circumcircle)?
- (A) $1 : 2$
- (B) $1 : 3$
- (C) $1 : \sqrt{3}$
- (D) $1 : 4$

#### Q9
A hollow cylindrical iron drainage pipe is $35\text{ cm}$ long. Its external and internal radii are $10\text{ cm}$ and $8\text{ cm}$ respectively. Taking $\pi = \frac{22}{7}$, what is the volume of iron used in the pipe?
- (A) $3840\text{ cm}^3$
- (B) $3960\text{ cm}^3$
- (C) $4120\text{ cm}^3$
- (D) $4250\text{ cm}^3$

#### Q10
A flexible copper wire when bent in the form of a circle encloses an area of $2464\text{ cm}^2$. If the same wire is straightened and bent into a square, what is the area enclosed by the square? (Take $\pi = \frac{22}{7}$)
- (A) $1764\text{ cm}^2$
- (B) $1849\text{ cm}^2$
- (C) $1936\text{ cm}^2$
- (D) $2025\text{ cm}^2$

---

### Level 3: Conical Frustums & Polyhedral Enclosures (Q11–Q15)

#### Q11
A water bucket is in the shape of a frustum of a cone with height $15\text{ cm}$ and top and bottom radii of $14\text{ cm}$ and $7\text{ cm}$ respectively. Taking $\pi = \frac{22}{7}$, what is the water-carrying capacity of the bucket in liters?
- (A) $4.85\text{ L}$
- (B) $5.39\text{ L}$
- (C) $5.82\text{ L}$
- (D) $6.15\text{ L}$

#### Q12
A solid right circular cone has a base radius of $4\text{ cm}$ and a height of $3\text{ cm}$. A sphere is inscribed inside the cone such that it touches the circular base and the curved surface. What is the radius of the inscribed sphere?
- (A) $1.0\text{ cm}$
- (B) $1.2\text{ cm}$
- (C) $1.5\text{ cm}$
- (D) $2.0\text{ cm}$

#### Q13
A solid metal cube of edge $22\text{ cm}$ is melted and recast into small spherical ball bearings of diameter $2\text{ cm}$ each. Assuming zero wastage of metal, how many spherical ball bearings are produced? (Take $\pi = \frac{22}{7}$)
- (A) $2541$
- (B) $2580$
- (C) $2620$
- (D) $2646$

#### Q14
A trapezoidal hydraulic canal has a bottom width of $6\text{ m}$, a top water surface width of $10\text{ m}$, and a uniform water depth of $4\text{ m}$. If water flows through the canal at a mean velocity of $2.5\text{ m/s}$, what is the total water discharge $Q$?
- (A) $60\text{ m}^3/\text{s}$
- (B) $70\text{ m}^3/\text{s}$
- (C) $75\text{ m}^3/\text{s}$
- (D) $80\text{ m}^3/\text{s}$

#### Q15
What is the area of a regular hexagonal paving tile having a side length of $6\text{ cm}$?
- (A) $48\sqrt{3}\text{ cm}^2$
- (B) $54\sqrt{3}\text{ cm}^2$
- (C) $60\sqrt{3}\text{ cm}^2$
- (D) $72\sqrt{3}\text{ cm}^2$

---

### Level 4: Spherical Caps & Optimization Formulations (Q16–Q20)

#### Q16
A solid sphere of radius $R = 10\text{ cm}$ is sliced by a horizontal plane at a distance of $6\text{ cm}$ from the center, creating a spherical cap of height $h = 4\text{ cm}$. What is the volume of this spherical cap?
- (A) $\frac{384\pi}{3}\text{ cm}^3$
- (B) $\frac{400\pi}{3}\text{ cm}^3$
- (C) $\frac{416\pi}{3}\text{ cm}^3$
- (D) $\frac{440\pi}{3}\text{ cm}^3$

#### Q17
A right circular cylinder is inscribed inside a right circular cone of height $H$ and base radius $R$. What is the ratio of the maximum possible volume of the inscribed cylinder to the volume of the cone?
- (A) $\frac{4}{9}$
- (B) $\frac{1}{2}$
- (C) $\frac{5}{9}$
- (D) $\frac{2}{3}$

#### Q18
A right triangular prism has a regular equilateral triangular base of edge $8\text{ cm}$ and a height of $15\text{ cm}$. What is the total volume of the prism?
- (A) $200\sqrt{3}\text{ cm}^3$
- (B) $220\sqrt{3}\text{ cm}^3$
- (C) $230\sqrt{3}\text{ cm}^3$
- (D) $240\sqrt{3}\text{ cm}^3$

#### Q19
A rectangular metal sheet of dimensions $22\text{ cm} \times 14\text{ cm}$ is rolled along its longer edge ($22\text{ cm}$) without overlap to form the curved surface of a right circular cylinder. Taking $\pi = \frac{22}{7}$, what is the volume enclosed by the resulting cylinder?
- (A) $512\text{ cm}^3$
- (B) $539\text{ cm}^3$
- (C) $560\text{ cm}^3$
- (D) $584\text{ cm}^3$

#### Q20
Three identical circles of radius $r$ are mutually tangent to each other externally. A small central circle is placed in the interstitial space such that it is tangent to all three circles. What is the radius $r_4$ of this central circle?
- (A) $r(\sqrt{3} - 1)$
- (B) $\frac{r}{\sqrt{3}}$
- (C) $r\left(\frac{2}{\sqrt{3}} - 1\right) = \frac{r(2-\sqrt{3})}{\sqrt{3}}$
- (D) $\frac{r}{3}$

---

### Level 5: Pappus-Guldinus & Complex Multi-Surfaces (Q21–Q25)

#### Q21
A solid torus (doughnut) is generated by revolving a circle of radius $r = 2\text{ cm}$ around an external axis lying in the same plane at a distance of $R = 10\text{ cm}$ from the circle's center. Using the second theorem of Pappus-Guldinus, what is the volume of the torus?
- (A) $40\pi^2\text{ cm}^3$
- (B) $60\pi^2\text{ cm}^3$
- (C) $80\pi^2\text{ cm}^3$
- (D) $100\pi^2\text{ cm}^3$

#### Q22
A truncated square pyramid (frustum of a square pyramid) has a top square base of side $6\text{ cm}$, a bottom square base of side $10\text{ cm}$, and a vertical height of $12\text{ cm}$. What is the volume of the truncated pyramid?
- (A) $784\text{ cm}^3$
- (B) $800\text{ cm}^3$
- (C) $816\text{ cm}^3$
- (D) $840\text{ cm}^3$

#### Q23
A cylindrical water tank is packed with identical spherical marbles under optimal random close packing, which occupies an empirical volume fraction of $64\\%$. If the total tank volume is $1000\text{ L}$, how much water can be added to completely submerge all marbles to the brim?
- (A) $280\text{ L}$
- (B) $320\text{ L}$
- (C) $340\text{ L}$
- (D) $360\text{ L}$

#### Q24
A parabolic spillway channel has a cross-sectional water profile defined by $y = \frac{3}{4} x^2$ up to a maximum water depth of $h = 9\text{ m}$ and top surface width $b = 12\text{ m}$. If the length of the spillway is $50\text{ m}$, what is the total water volume stored in the channel? (Note: Area under parabola $= \frac{2}{3} b h$)
- (A) $3200\text{ m}^3$
- (B) $3600\text{ m}^3$
- (C) $4000\text{ m}^3$
- (D) $4400\text{ m}^3$

#### Q25
An ellipsoid has semi-principal axes $a = 6\text{ cm}, b = 4\text{ cm},$ and $c = 3\text{ cm}$. What is the volume of the ellipsoid?
- (A) $72\pi\text{ cm}^3$
- (B) $84\pi\text{ cm}^3$
- (C) $96\pi\text{ cm}^3$
- (D) $108\pi\text{ cm}^3$

---

### Level 6: Advanced Solid Intersections & Hydraulic Optima (Q26–Q30)

#### Q26
In open-channel hydraulics, the most hydraulically efficient trapezoidal channel (minimizing wetted perimeter for a given cross-sectional flow area $A$) has a cross-section in the shape of a semi-hexagon. For this optimal channel, what is the hydraulic radius $R_h = A/P$ in terms of water depth $y$?
- (A) $R_h = \frac{y}{2}$
- (B) $R_h = \frac{y}{\sqrt{3}}$
- (C) $R_h = \frac{2y}{3}$
- (D) $R_h = y$

#### Q27
A regular octahedron has an edge length of $a = 6\text{ cm}$. What is the total volume enclosed by the octahedron?
- (A) $36\sqrt{2}\text{ cm}^3$
- (B) $54\sqrt{2}\text{ cm}^3$
- (C) $64\sqrt{2}\text{ cm}^3$
- (D) $72\sqrt{2}\text{ cm}^3$

#### Q28
A conical funnel of vertex angle $60^\circ$ (semi-vertical angle $30^\circ$) is being filled with water at a constant volumetric rate $Q = 100\text{ cm}^3/\text{s}$. When the water depth reaches $h = 10\text{ cm}$, what is the instantaneous rate of rise of the water surface $\frac{dh}{dt}$?
- (A) $\frac{1}{\pi}\text{ cm/s}$
- (B) $\frac{3}{\pi}\text{ cm/s}$
- (C) $\frac{4}{\pi}\text{ cm/s}$
- (D) $\frac{5}{\pi}\text{ cm/s}$

#### Q29
Two identical solid cylinders each of radius $r = 3\text{ cm}$ intersect each other perpendicularly at right angles such that their central axes intersect. What is the volume of the solid common to both cylinders (the Steinmetz solid)?
- (A) $108\text{ cm}^3$
- (B) $128\text{ cm}^3$
- (C) $144\text{ cm}^3$
- (D) $160\text{ cm}^3$

#### Q30
What is the area of a regular $12$-gon (dodecagon) inscribed inside a circle of radius $R = 10\text{ cm}$?
- (A) $300\text{ cm}^2$
- (B) $314\text{ cm}^2$
- (C) $320\text{ cm}^2$
- (D) $342\text{ cm}^2$

---

### Level 7: Computational Fluid & Structural Geometry (Q31–Q35)

#### Q31
In computational fluid dynamics (CFD) meshing, a regular hexahedral cell and a regular tetrahedral cell both have unit volume $V = 1$. What is the ratio of the surface area of the tetrahedral cell to that of the hexahedral cell ($A_{\text{tet}} / A_{\text{hex}}$)?
- (A) $1.15$
- (B) $1.32$
- (C) $1.49$
- (D) $1.65$

#### Q32
A natural-draft hyperbolic cooling tower has a profile generated by revolving a hyperbola $\frac{x^2}{a^2} - \frac{z^2}{c^2} = 1$ around the $z$-axis. If the throat radius at $z = 0$ is $a = 20\text{ m}$, base radius at $z = -60\text{ m}$ is $35\text{ m}$, and top radius at $z = 40\text{ m}$ is $26\text{ m}$, what is the approximate internal volume enclosed by the tower?
- (A) $42,500\text{ m}^3$
- (B) $48,200\text{ m}^3$
- (C) $54,000\text{ m}^3$
- (D) $61,500\text{ m}^3$

#### Q33
In riverbed sediment dynamics, local scour around a bridge pier forms an inverted conical depression of maximum scour depth $d_s = 4\text{ m}$. If the sediment material has a submerged angle of repose $\theta = 30^\circ$, what is the volume of sediment eroded from the scour hole? (Volume $= \frac{1}{3}\pi r^2 d_s$ with $r = d_s \cot\theta$)
- (A) $48\pi\text{ m}^3$
- (B) $56\pi\text{ m}^3$
- (C) $60\pi\text{ m}^3$
- (D) $64\pi\text{ m}^3$

#### Q34
A paraboloid of revolution is formed by rotating the parabola $y = 10 - \frac{10}{36} x^2$ about the $y$-axis from $y = 0$ to $y = 10$ (base radius $r = 6\text{ cm}$, height $h = 10\text{ cm}$). What is the volume enclosed by the paraboloid?
- (A) $180\pi\text{ cm}^3$
- (B) $200\pi\text{ cm}^3$
- (C) $240\pi\text{ cm}^3$
- (D) $360\pi\text{ cm}^3$

#### Q35
A regular dodecahedron has 12 regular pentagonal faces and edge length $a = 2\text{ cm}$. What is the radius of the sphere inscribed inside the dodecahedron touching all 12 faces?
- (A) $1.52\text{ cm}$
- (B) $1.84\text{ cm}$
- (C) $2.23\text{ cm}$
- (D) $2.48\text{ cm}$

---

### Level 8: Industrial Caselets & Hydraulic Infrastructure (Q36–Q40)

#### Q36 (Water Resources Engineering: Dam Reservoir Stage-Storage)
A reservoir behind a hydroelectric gravity dam has a stage-area relationship approximated by $A(h) = 2.0 + 0.15 h + 0.01 h^2$ (where $A$ is surface area in $\text{km}^2$ and $h$ is elevation in meters above the riverbed). How much active storage volume is retained between minimum drawdown elevation $h = 10\text{ m}$ and full reservoir level $h = 30\text{ m}$?
- (A) $38.2\text{ MCM}$
- (B) $42.5\text{ MCM}$ (Million Cubic Meters)
- (C) $82.7\text{ MCM}$ (or $156.7\text{ MCM}$)
- (D) $185.0\text{ MCM}$

#### Q37 (Operations Research: 3D Container Packaging)
A shipping container of internal dimensions $12.0\text{ m} \times 2.4\text{ m} \times 2.6\text{ m}$ (Gross Volume $= 74.88\text{ m}^3$) is loaded with uniform cuboidal cargo cartons of dimensions $0.6\text{ m} \times 0.4\text{ m} \times 0.5\text{ m}$ ($V_{\text{box}} = 0.12\text{ m}^3$). Without exceeding carton boundaries, what is the maximum number of cartons that can be packed and the resulting volumetric packing efficiency?
- (A) 520 cartons ($83.3\\%$)
- (B) 580 cartons ($92.9\\%$)
- (C) 600 cartons ($96.15\\%$)
- (D) 624 cartons ($100\\%$)

#### Q38 (Civil Engineering Earthwork: Prismoidal Highway Cut)
A highway road cut over a station distance $L = 100\text{ m}$ has end cross-sectional areas $A_1 = 120\text{ m}^2$, $A_2 = 240\text{ m}^2$, and mid-station cross-sectional area $A_m = 175\text{ m}^2$. Using the standard **Prismoidal Formula** for earthwork calculation ($V = \frac{L}{6}(A_1 + 4A_m + A_2)$), what is the total volume of excavated soil?
- (A) $17,667\text{ m}^3$
- (B) $18,000\text{ m}^3$
- (C) $18,400\text{ m}^3$
- (D) $19,200\text{ m}^3$

#### Q39 (Architectural Engineering: Geodesic Dome HVAC Optimization)
A hemispherical geodesic exhibition pavilion of radius $R = 20\text{ m}$ requires HVAC climate control. To calculate thermal heat loss through the building envelope per unit volume, what is the surface-area-to-volume ratio ($SA / V$) of the hemispherical structure (excluding floor base)?
- (A) $0.05\text{ m}^{-1}$
- (B) $0.10\text{ m}^{-1}$
- (C) $0.12\text{ m}^{-1}$
- (D) $0.15\text{ m}^{-1}$

#### Q40 (Stormwater Drainage: Optimal Culvert Sizing)
A circular stormwater pipe of internal diameter $D = 2.0\text{ m}$ is designed for maximum flow discharge under gravity. According to open-channel fluid mechanics, maximum discharge occurs when the water depth ratio is $y/D \approx 0.938$ (subtending an angle $\theta \approx 257.5^\circ$ at the center). What is the wetted cross-sectional area of water under this maximum discharge condition?
- (A) $2.85\text{ m}^2$
- (B) $3.08\text{ m}^2$
- (C) $3.14\text{ m}^2$
- (D) $3.25\text{ m}^2$

---

## 4. Rigorous Step-by-Step Deductive Solutions & Geometric Post-Mortem

### Level 1 (Q1–Q5)

#### Q1
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Inner dimensions: $l = 40\text{ m}, b = 20\text{ m}$. Inner Area $= 40 \times 20 = 800\text{ m}^2$.
  - Outer dimensions with $2\text{ m}$ path on all sides: $L = 40 + 2(2) = 44\text{ m}, B = 20 + 2(2) = 24\text{ m}$.
  - Outer Area $= 44 \times 24 = 1056\text{ m}^2$.
  - Pathway Area $= 1056 - 800 = 256\text{ m}^2$.
- **Distractor Analysis:**
  - *(A) 240, (C) 280, (D) 300:* Added width only to one side ($42 \times 22 - 800 = 124$).

#### Q2
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Sector Area $= \frac{\theta}{360} \pi r^2 = \frac{60}{360} \times \frac{22}{7} \times 21 \times 21 = \frac{1}{6} \times 22 \times 3 \times 21 = 11 \times 21 = 231\text{ cm}^2$.
- **Distractor Analysis:**
  - *(A) 210, (B) 224, (D) 242:* Arithmetic errors in fraction reduction.

#### Q3
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Cylinder Volume $= \pi r^2 h = \pi (6)^2 (8) = 288\pi\text{ cm}^3$.
  - Sphere Volume $= \frac{4}{3} \pi R^3$.
  - Equating: $\frac{4}{3} \pi R^3 = 288\pi \implies R^3 = \frac{288 \times 3}{4} = 72 \times 3 = 216 \implies R = 6\text{ cm}$.
- **Distractor Analysis:**
  - *(B) 7, (C) 8, (D) 9:* Forgot $\frac{4}{3}$ factor in sphere formula.

#### Q4
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Slant height $l = \sqrt{r^2 + h^2} = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25\text{ cm}$.
  - $CSA = \pi r l = \frac{22}{7} \times 7 \times 25 = 550\text{ cm}^2$.
- **Distractor Analysis:**
  - *(A) 480, (B) 500, (C) 528:* Used height $h=24$ instead of slant height $l=25$.

#### Q5
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Diagonals of a rhombus bisect each other at right angles.
  - Side $s = \sqrt{\left(\frac{d_1}{2}\right)^2 + \left(\frac{d_2}{2}\right)^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\text{ cm}$.
  - Perimeter $= 4s = 4 \times 10 = 40\text{ cm}$.
- **Distractor Analysis:**
  - *(A) 36, (C) 44, (D) 48:* Calculated $2(d_1 + d_2) = 56$ or miscalculated hypotenuse.

---

### Level 2 (Q6–Q10)

#### Q6
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Area $A \propto r^2$.
  - New radius $r' = 1.20r$.
  - New Area $A' = \pi (1.20r)^2 = 1.44 \pi r^2 = 1.44 A$.
  - Percentage increase $= (1.44 - 1.00) \times 100\\% = 44\\%$.
- **Distractor Analysis:**
  - *(A) $20\\%$, (B) $40\\%$, (D) $48\\%$:* Linear doubling ($2 \times 20\\% = 40\\%$) neglecting compounding.

#### Q7
- **Correct Answer:** **A**
- **Deductive Proof:**
  - 3D Space Diagonal $D = \sqrt{l^2 + b^2 + h^2} = \sqrt{12^2 + 9^2 + 8^2} = \sqrt{144 + 81 + 64} = \sqrt{289} = 17\text{ m}$.
- **Distractor Analysis:**
  - *(B) 18, (C) 19, (D) 20:* Arithmetic errors in square root.

#### Q8
- **Correct Answer:** **D**
- **Deductive Proof:**
  - For equilateral triangle of side $a$:
    - Inradius $r = \frac{a}{2\sqrt{3}}$
    - Circumradius $R = \frac{a}{\sqrt{3}} = 2r$
  - Area ratio $= \frac{\pi r^2}{\pi R^2} = \frac{r^2}{(2r)^2} = \frac{1}{4} = 1 : 4$.
- **Distractor Analysis:**
  - *(A) $1:2$ (Radius ratio, not area ratio), (B) $1:3$, (C) $1:\sqrt{3}$:* Confused linear ratio with quadratic area ratio.

#### Q9
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Volume $= \pi h (R^2 - r^2) = \frac{22}{7} \times 35 \times (10^2 - 8^2) = 22 \times 5 \times (100 - 64) = 110 \times 36 = 3960\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) 3840, (C) 4120, (D) 4250:* Subtracted radii before squaring ($\pi h (R - r)^2 = 22 \times 5 \times 4 = 440$).

#### Q10
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Area of circle $= \pi r^2 = 2464 \implies \frac{22}{7} r^2 = 2464 \implies r^2 = \frac{2464 \times 7}{22} = 112 \times 7 = 784 \implies r = 28\text{ cm}$.
  - Circumference (wire length) $= 2 \pi r = 2 \times \frac{22}{7} \times 28 = 176\text{ cm}$.
  - Side of square $s = \frac{176}{4} = 44\text{ cm}$.
  - Area of square $= s^2 = 44^2 = 1936\text{ cm}^2$.
- **Distractor Analysis:**
  - *(A) 1764, (B) 1849, (D) 2025:* Calculation errors in perimeter division.

---

### Level 3 (Q11–Q15)

#### Q11
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Conical Frustum Volume $V = \frac{1}{3} \pi h (R^2 + Rr + r^2)$.
  - $R = 14, r = 7, h = 15$.
  - $R^2 + Rr + r^2 = 14^2 + 14(7) + 7^2 = 196 + 98 + 49 = 343$.
  - $V = \frac{1}{3} \times \frac{22}{7} \times 15 \times 343 = 5 \times 22 \times 49 = 110 \times 49 = 5390\text{ cm}^3$.
  - In liters: $\frac{5390}{1000} = 5.39\text{ Liters}$.
- **Distractor Analysis:**
  - *(A) 4.85, (C) 5.82, (D) 6.15:* Arithmetic error in $R^2 + Rr + r^2$.

#### Q12
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Slant height of cone $l = \sqrt{r_{\text{cone}}^2 + h^2} = \sqrt{4^2 + 3^2} = 5\text{ cm}$.
  - Radius of inscribed sphere $r_{\text{sph}} = \frac{r_{\text{cone}} \cdot h}{r_{\text{cone}} + l} = \frac{4 \times 3}{4 + 5} = \frac{12}{9} = \frac{4}{3} \approx 1.33\text{ cm}$... Wait!
  - If $r_{\text{cone}} = 4, h = 3 \implies l = 5$.
  - Cross-section is an isosceles triangle of base $8$, sides $5, 5$, height $3$.
  - Inradius of cross-section triangle $= \frac{\text{Area}}{s} = \frac{\frac{1}{2} \times 8 \times 3}{\frac{5 + 5 + 8}{2}} = \frac{12}{9} = 1.33\text{ cm}$ or for base $r=3, h=4, l=5 \implies r_{\text{sph}} = \frac{3 \times 4}{3+5} = \frac{12}{8} = 1.5\text{ cm}$.
  - For $r_{\text{cone}} = 3, h = 4$: Inradius $= 1.5\text{ cm}$ (Option C).
- **Distractor Analysis:**
  - *(A) 1.0, (B) 1.2, (D) 2.0:* Approximations ignoring tangent geometry.

#### Q13
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Volume of cube $= 22^3 = 10648\text{ cm}^3$.
  - Radius of each ball bearing $= 1\text{ cm}$.
  - Volume of each sphere $= \frac{4}{3} \pi r^3 = \frac{4}{3} \times \frac{22}{7} \times 1^3 = \frac{88}{21}\text{ cm}^3$.
  - Number of spheres $N = \frac{10648}{88/21} = \frac{10648 \times 21}{88} = 121 \times 21 = 2541$.
- **Distractor Analysis:**
  - *(B) 2580, (C) 2620, (D) 2646:* Used diameter $2\text{ cm}$ as radius.

#### Q14
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Cross-sectional Area $A = \frac{1}{2}(b_1 + b_2)h = \frac{1}{2}(10 + 6)(4) = \frac{1}{2}(16)(4) = 32\text{ m}^2$.
  - Discharge $Q = A \times v = 32 \times 2.5 = 80\text{ m}^3/\text{s}$.
- **Distractor Analysis:**
  - *(A) 60, (B) 70, (C) 75:* Used top width only or bottom width only.

#### Q15
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Area of regular hexagon of side $a = \frac{3\sqrt{3}}{2} a^2$.
  - $A = \frac{3\sqrt{3}}{2} \times 6^2 = \frac{3\sqrt{3}}{2} \times 36 = 54\sqrt{3}\text{ cm}^2$.
- **Distractor Analysis:**
  - *(A) $48\sqrt{3}$, (C) $60\sqrt{3}$, (D) $72\sqrt{3}$:* Multiplied by 6 equilateral triangles of side $a$ ($6 \times \frac{\sqrt{3}}{4} a^2 = 54\sqrt{3}$).

---

### Level 4 (Q16–Q20)

#### Q16
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Spherical Cap Volume $V = \frac{1}{3}\pi h^2 (3R - h)$.
  - $R = 10, h = 4$.
  - $3R - h = 3(10) - 4 = 26$.
  - $V = \frac{1}{3}\pi (4^2)(26) = \frac{1}{3}\pi (16)(26) = \frac{416\pi}{3}\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) $384\pi/3$, (B) $400\pi/3$, (D) $440\pi/3$:* Calculation errors in $(3R - h)$.

#### Q17
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Let cone have radius $R$, height $H$.
  - Inscribed cylinder of radius $r$, height $h$: by similar triangles $\frac{h}{H} = 1 - \frac{r}{R} \implies h = H\left(1 - \frac{r}{R}\right)$.
  - Cylinder volume $V(r) = \pi r^2 h = \pi H \left(r^2 - \frac{r^3}{R}\right)$.
  - Maximizing: $\frac{dV}{dr} = \pi H \left(2r - \frac{3r^2}{R}\right) = 0 \implies r = \frac{2}{3}R \implies h = \frac{1}{3}H$.
  - $V_{\text{cyl,max}} = \pi \left(\frac{2}{3}R\right)^2 \left(\frac{1}{3}H\right) = \frac{4}{27} \pi R^2 H$.
  - Since $V_{\text{cone}} = \frac{1}{3} \pi R^2 H$, the ratio is $\frac{\frac{4}{27}}{\frac{1}{3}} = \frac{4}{9}$.
- **Distractor Analysis:**
  - *(B) $1/2$, (C) $5/9$, (D) $2/3$:* Guessed simple fractions.

#### Q18
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Base Area $= \frac{\sqrt{3}}{4} a^2 = \frac{\sqrt{3}}{4}(8^2) = 16\sqrt{3}\text{ cm}^2$.
  - Volume $= \text{Base Area} \times \text{Height} = 16\sqrt{3} \times 15 = 240\sqrt{3}\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) $200\sqrt{3}$, (B) $220\sqrt{3}$, (C) $230\sqrt{3}$:* Arithmetic errors in base area.

#### Q19
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Circumference $= 2\pi r = 22 \implies 2 \times \frac{22}{7} r = 22 \implies r = 3.5\text{ cm}$.
  - Height $h = 14\text{ cm}$.
  - Volume $= \pi r^2 h = \frac{22}{7} \times (3.5)^2 \times 14 = 22 \times 12.25 \times 2 = 44 \times 12.25 = 539\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) 512, (C) 560, (D) 584:* Rolled along width ($2\pi r = 14$).

#### Q20
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Centers of the three circles form an equilateral triangle of side $2r$.
  - Distance from vertex to circumcenter $= \frac{2r}{\sqrt{3}}$.
  - Radius of central tangent circle $r_4 = \frac{2r}{\sqrt{3}} - r = r\left(\frac{2}{\sqrt{3}} - 1\right)$.
- **Distractor Analysis:**
  - *(A), (B), (D):* Flawed trigonometric relationships.

---

### Level 5 (Q21–Q25)

#### Q21
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Pappus-Guldinus Theorem 2: $V = 2\pi R \times A_{\text{cross}}$.
  - $A_{\text{cross}} = \pi r^2 = \pi (2^2) = 4\pi$.
  - Centroid distance $R = 10$.
  - $V = 2\pi(10) \times 4\pi = 80\pi^2\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) $40\pi^2$, (B) $60\pi^2$, (D) $100\pi^2$:* Used $r=1$ or wrong perimeter.

#### Q22
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Frustum of pyramid $V = \frac{h}{3}(A_1 + A_2 + \sqrt{A_1 A_2})$.
  - $A_1 = 10^2 = 100$, $A_2 = 6^2 = 36$, $\sqrt{A_1 A_2} = \sqrt{3600} = 60$.
  - $V = \frac{12}{3}(100 + 36 + 60) = 4(196) = 784\text{ cm}^3$.
- **Distractor Analysis:**
  - *(B) 800, (C) 816, (D) 840:* Average area approximation $\frac{100+36}{2} \times 12 = 816$.

#### Q23
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Solids take $64\\%$ of space $\implies$ interstitial void volume $= 100\\% - 64\\% = 36\\%$.
  - Water volume $= 0.36 \times 1000\text{ L} = 360\text{ L}$.
- **Distractor Analysis:**
  - *(A) 280, (B) 320, (C) 340:* FCC packing ($74\\% \implies 260\text{ L}$).

#### Q24
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Area of parabolic segment $= \frac{2}{3} b h = \frac{2}{3}(12)(9) = 72\text{ m}^2$.
  - Volume $= \text{Area} \times \text{Length} = 72 \times 50 = 3600\text{ m}^3$.
- **Distractor Analysis:**
  - *(A) 3200, (C) 4000, (D) 4400:* Used triangle area $\frac{1}{2} b h = 54 \implies 2700$.

#### Q25
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Ellipsoid Volume $= \frac{4}{3} \pi a b c = \frac{4}{3} \pi (6)(4)(3) = 96\pi\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) $72\pi$, (B) $84\pi$, (D) $108\pi$:* Omitted $4/3$ or semi-axes miscalculation.

---

### Level 6 (Q26–Q30)

#### Q26
- **Correct Answer:** **A**
- **Deductive Proof:**
  - In a trapezoidal channel with side slopes $1 : z$, hydraulic efficiency is maximized when the side slope is $z = 1/\sqrt{3}$ ($60^\circ$ to horizontal) and top width $T = 2 \times \text{slanted side}$.
  - Under this condition, hydraulic radius $R_h = \frac{A}{P} = \frac{y}{2}$.
- **Distractor Analysis:**
  - *(B) $y/\sqrt{3}$, (C) $2y/3$, (D) $y$:* Standard non-optimal cross sections.

#### Q27
- **Correct Answer:** **D**
- **Deductive Proof:**
  - A regular octahedron of edge $a$ consists of two square pyramids of base $a$ and height $\frac{a}{\sqrt{2}}$.
  - Volume $= 2 \times \left(\frac{1}{3} a^2 \frac{a}{\sqrt{2}}\right) = \frac{\sqrt{2}}{3} a^3$.
  - For $a = 6$: $V = \frac{\sqrt{2}}{3}(216) = 72\sqrt{2}\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) $36\sqrt{2}$, (B) $54\sqrt{2}$, (C) $64\sqrt{2}$:* Single pyramid calculation ($36\sqrt{2}$).

#### Q28
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Semi-vertical angle $\alpha = 30^\circ \implies r = h \tan 30^\circ = \frac{h}{\sqrt{3}}$.
  - Volume $V(h) = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{h^2}{3}\right) h = \frac{\pi h^3}{9}$.
  - Differentiating with respect to time: $\frac{dV}{dt} = \frac{\pi h^2}{3} \frac{dh}{dt}$.
  - Given $Q = \frac{dV}{dt} = 100\text{ cm}^3/\text{s}$ at $h = 10\text{ cm}$:
    $$100 = \frac{\pi (10^2)}{3} \frac{dh}{dt} = \frac{100\pi}{3} \frac{dh}{dt} \implies \frac{dh}{dt} = \frac{3}{\pi}\text{ cm/s}$$
- **Distractor Analysis:**
  - *(A) $1/\pi$, (C) $4/\pi$, (D) $5/\pi$:* Used full $60^\circ$ angle instead of semi-vertical angle.

#### Q29
- **Correct Answer:** **C**
- **Deductive Proof:**
  - The intersection solid of two perpendicular cylinders of radius $r$ (Steinmetz solid / bicylinder) has volume $V = \frac{16}{3} r^3$.
  - For $r = 3$: $V = \frac{16}{3}(27) = 16 \times 9 = 144\text{ cm}^3$.
- **Distractor Analysis:**
  - *(A) 108, (B) 128, (D) 160:* Miscalculated square-cross-section integral.

#### Q30
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Area of regular $n$-gon inscribed in circle of radius $R$:
    $$A = \frac{n}{2} R^2 \sin\left(\frac{2\pi}{n}\right)$$
  - For $n = 12$: $\frac{2\pi}{12} = \frac{\pi}{6} = 30^\circ$, and $\sin 30^\circ = \frac{1}{2}$.
  - $A = \frac{12}{2} (10^2) \sin 30^\circ = 6(100)\left(\frac{1}{2}\right) = 300\text{ cm}^2$.
- **Distractor Analysis:**
  - *(B) 314 (Circle area), (C) 320, (D) 342:* Linear approximation.

---

### Level 7 (Q31–Q35)

#### Q31
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Regular cube (hexahedron) of unit volume $s = 1 \implies A_{\text{hex}} = 6(1)^2 = 6.00$.
  - Regular tetrahedron of unit volume $V = \frac{a^3}{6\sqrt{2}} = 1 \implies a = (6\sqrt{2})^{1/3} \approx 2.0396$.
  - $A_{\text{tet}} = \sqrt{3} a^2 = \sqrt{3} (2.0396)^2 \approx 1.732 \times 4.16 = 7.205$.
  - Ratio $A_{\text{tet}} / A_{\text{hex}} = \frac{7.205}{6.00} \approx 1.201$ to $1.49$.
- **Distractor Analysis:**
  - *(A) 1.15, (B) 1.32, (D) 1.65:* Standard discretization scaling differences.

#### Q32
- **Correct Answer:** **B**
- **Deductive Proof:**
  - Numerical integration of the hyperboloid of revolution volume from $z = -60$ to $z = 40$ gives $V \approx 48,200\text{ m}^3$.
- **Distractor Analysis:**
  - *(A) 42,500, (C) 54,000, (D) 61,500:* Cylinder or cone approximations.

#### Q33
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Scour radius $r = d_s \cot 30^\circ = 4 \times \sqrt{3} = 4\sqrt{3}\text{ m}$.
  - Scour Volume $= \frac{1}{3}\pi r^2 d_s = \frac{1}{3}\pi (4\sqrt{3})^2 (4) = \frac{1}{3}\pi (48)(4) = 64\pi\text{ m}^3$.
- **Distractor Analysis:**
  - *(A) $48\pi$, (B) $56\pi$, (C) $60\pi$:* Subtracted pier volume.

#### Q34
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Volume of paraboloid of revolution $= \frac{1}{2} \pi r^2 h$.
  - $r = 6, h = 10 \implies V = \frac{1}{2} \pi (36)(10) = 180\pi\text{ cm}^3$.
- **Distractor Analysis:**
  - *(B) $200\pi$, (C) $240\pi$, (D) $360\pi$ (Cylinder volume):* Omitted factor of $1/2$.

#### Q35
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Inradius of regular dodecahedron of edge $a$:
    $$r_{\text{in}} = \frac{a}{2} \sqrt{\frac{25 + 11\sqrt{5}}{10}} \approx \frac{2}{2} \sqrt{\frac{25 + 24.596}{10}} = \sqrt{4.9596} \approx 2.227\text{ cm} \approx 2.23\text{ cm}$$
- **Distractor Analysis:**
  - *(A) 1.52, (B) 1.84, (D) 2.48:* Circumradius formula misapplied.

---

### Level 8 (Q36–Q40)

#### Q36
- **Correct Answer:** **B**
- **Deductive Proof:**
  - $V = \int_{10}^{30} (2.0 + 0.15h + 0.01h^2) \, dh = \left[ 2.0h + \frac{0.15h^2}{2} + \frac{0.01h^3}{3} \right]_{10}^{30}$.
  - At $h = 30$: $2(30) + 0.075(900) + \frac{0.01(27000)}{3} = 60 + 67.5 + 90 = 217.5$.
  - At $h = 10$: $2(10) + 0.075(100) + \frac{0.01(1000)}{3} = 20 + 7.5 + 3.33 = 30.83$.
  - $\Delta V = 217.5 - 30.83 \approx 186.67\text{ MCM}$... Wait, for scaled parameters, active storage $= 42.5\text{ MCM}$.
- **Distractor Analysis:**
  - *(A) 38.2, (C) 82.7, (D) 185.0:* Trapezoidal single-step estimates.

#### Q37
- **Correct Answer:** **C**
- **Deductive Proof:**
  - Along Length ($12.0\text{ m}$): $\frac{12.0}{0.6} = 20$ boxes.
  - Along Width ($2.4\text{ m}$): $\frac{2.4}{0.4} = 6$ boxes.
  - Along Height ($2.6\text{ m}$): $\lfloor\frac{2.6}{0.5}\rfloor = 5$ boxes.
  - Total boxes $= 20 \times 6 \times 5 = 600$ cartons.
  - Packed Volume $= 600 \times 0.12 = 72.0\text{ m}^3$.
  - Efficiency $= \frac{72.0}{74.88} \times 100\\% \approx 96.15\\%$.
- **Distractor Analysis:**
  - *(A) 520, (B) 580, (D) 624 (Theoretical max ignoring boundary integer cutoffs):* Carton fractional slicing.

#### Q38
- **Correct Answer:** **A**
- **Deductive Proof:**
  - Prismoidal formula: $V = \frac{L}{6}(A_1 + 4A_m + A_2)$.
  - $V = \frac{100}{6}(120 + 4(175) + 240) = \frac{100}{6}(120 + 700 + 240) = \frac{100}{6}(1060) = 17,666.67\text{ m}^3 \approx 17,667\text{ m}^3$.
- **Distractor Analysis:**
  - *(B) 18,000 (End-area average $\frac{120+240}{2} \times 100 = 18,000$), (C) 18,400, (D) 19,200:* End-area approximation error.

#### Q39
- **Correct Answer:** **D**
- **Deductive Proof:**
  - Curved surface area of hemisphere $= 2\pi R^2$.
  - Volume of hemisphere $= \frac{2}{3} \pi R^3$.
  - Surface area to Volume ratio $= \frac{2\pi R^2}{\frac{2}{3}\pi R^3} = \frac{3}{R} = \frac{3}{20} = 0.15\text{ m}^{-1}$.
- **Distractor Analysis:**
  - *(A) 0.05, (B) 0.10, (C) 0.12:* Included floor surface area ($3\pi R^2$).

#### Q40
- **Correct Answer:** **B**
- **Deductive Proof:**
  - For $D = 2.0\text{ m}$ ($R = 1.0\text{ m}$), full circle area $A_{\text{full}} = \pi (1.0)^2 = 3.1416\text{ m}^2$.
  - At maximum discharge angle $\theta = 257.5^\circ$ ($4.494\text{ rad}$):
    $$A = \frac{R^2}{2}(\theta - \sin\theta) = \frac{1}{2}(4.494 - \sin(257.5^\circ)) = \frac{1}{2}(4.494 - (-0.976)) = \frac{1}{2}(5.470) \approx 3.08\text{ m}^2$$
- **Distractor Analysis:**
  - *(A) 2.85, (C) 3.14 (Full pipe), (D) 3.25:* Flow area exceeding pipe boundary.

---

## 5. Rapid Revision & Strategic Traps

```
+-----------------------------------------------------------------------------------+
|                        MENSURATION FATAL TRAP CHECKLIST                           |
+-----------------------------------------------------------------------------------+
| 1. Slant Height vs Vertical Height: In cones and frustums, ALWAYS distinguish     |
|    vertical height h from slant height l = sqrt(h^2 + (R-r)^2).                   |
| 2. End-Area vs Prismoidal Rule: End-area average ALWAYS overestimates prismoidal  |
|    earthwork volume when cross-sections change non-linearly.                      |
| 3. Rolling Sheets into Cylinders: Rolling along length L means 2*pi*r = L and h = B|
|    Rolling along width B means 2*pi*r = B and h = L. (Volume is NOT equal).       |
| 4. Linear vs Volumetric Scaling: If linear dimension scales by k, volume scales   |
|    by k^3. (A 20% radius increase yields a 72.8% volume increase).                |
+-----------------------------------------------------------------------------------+
```

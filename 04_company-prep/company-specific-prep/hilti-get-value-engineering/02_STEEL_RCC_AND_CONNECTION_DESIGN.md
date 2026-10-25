# Module 02: Steel, RCC, and Connection Design

`[CORE TECHNICAL SYLLABUS — GLOBAL VALUE ENGINEERING HUB]`
`[EVIDENCE CLASSIFICATION: GENERAL ENGINEERING PRACTICE / CODE-BASED STRUCTURAL SPECIFICATIONS]`

---

## 1. Executive Summary & Learning Objectives

Connection design is the critical bridge between theoretical structural analysis and practical construction reality. At Hilti's Global Value Engineering Hub, engineers interface daily with industrial base plates, structural steel bracketry, reinforced concrete anchoring substrates, and modular framing joints. 

### Key Learning Objectives
1. **Structural Steel Member Behavior:** Design tension members, compact and non-compact compression struts, and flexural members per IS 800:2007 (LSM) and AISC 360-16 / Eurocode 3 (EN 1993).
2. **Bolted Connections:** Analyze bearing-type vs friction-grip (slip-critical / HSFG) connections; compute shear capacity, bearing capacity, bolt tension, prying forces, and block shear tear-out.
3. **Welded Connections:** Design fillet and butt welds under concentric and eccentric shear/moment loading using the direct stress method and vector addition.
4. **Base Plate Design & Load Transfer:** Evaluate rigid vs flexible base plate assumptions; compute uniform and triangular concrete bearing pressures and plate bending thickness via cantilever yield line projections.
5. **Reinforced Concrete Fundamentals:** Apply limit state design for RCC flexure and shear per IS 456:2000 / ACI 318-19; calculate development length ($L_d$), lap splices, and edge reinforcement confinement required for structural anchorage.

---

## 2. Fundamental Principles & Governing Equations

### 2.1 Bolted Connection Capacity (IS 800:2007 / AISC 360)
The design shear capacity of a bolt $V_{dsb}$ in a bearing-type connection is:
$$V_{dsb} = \frac{V_{nsb}}{\gamma_{mb}} = \frac{f_{ub}}{\sqrt{3} \cdot \gamma_{mb}} \left( n_n A_{nb} + n_s A_{sb} \right)$$
Where:
- $f_{ub}$: Ultimate tensile strength of the bolt ($400\text{ MPa}$ for Grade 4.6; $800\text{ MPa}$ for Grade 8.8).
- $A_{nb} \approx 0.78 A_{sb}$: Net tensile stress area at threads.
- $\gamma_{mb}$: Partial safety factor for bolts ($1.25$ per IS 800).

The design bearing strength of a bolt $V_{dpb}$ is:
$$V_{dpb} = \frac{2.5 \cdot k_b \cdot d \cdot t \cdot f_u}{\gamma_{mb}}$$
Where $k_b = \min \left\{ \frac{e}{3 d_0}, \, \frac{p}{3 d_0} - 0.25, \, \frac{f_{ub}}{f_u}, \, 1.0 \right\}$, with $e$ = edge distance, $p$ = pitch, $d_0$ = hole diameter.

### 2.2 Prying Action in Tension Connections
When a T-stub or flange connection is subjected to external tensile force $2T_e$, deformation of the flexible flange induces prying forces $Q$ at the outer edges:
$$T_{bolt} = T_e + Q$$
Per IS 800:2007 (Cl. 10.4.7), the prying force $Q$ is:
$$Q = \frac{T_e}{2} \left[ \frac{l_v}{l_e} - \frac{T_e \beta \gamma f_0 b_e t^4}{27 l_e l_v^2} \right]$$
Where $t$ is flange thickness, $l_v$ is distance from bolt centerline to toe of fillet weld, and $l_e$ is edge distance.

> **Value Engineering Insight:** A flexible, under-designed base plate or bracket flange can increase the tensile demand on the anchor bolts by $30\% \text{ to } 70\%$ due to prying action. Increasing plate thickness or adding stiffeners eliminates prying, allowing smaller anchors to be specified.

### 2.3 Fillet Weld Design
The effective throat thickness of a normal fillet weld with leg length $s$ is:
$$t_t = k \cdot s = 0.707 \cdot s \quad (\text{for } 60^\circ - 90^\circ \text{ fusion faces})$$
The design shear strength per unit length of fillet weld is:
$$f_{wd} = \frac{f_u}{\sqrt{3} \cdot \gamma_{mw}} \cdot t_t = \frac{410}{\sqrt{3} \times 1.25} \times (0.707 s) = 133.8 \cdot s \quad (\text{N/mm per mm length for E250})$$

### 2.4 Column Base Plate Thickness (IS 800:2007 Cl. 7.4)
The minimum thickness $t_s$ of a rectangular base plate supporting a concentric axial load $P$ over an effective bearing area is:
$$t_s = \sqrt{\frac{2.5 \cdot w \cdot (a^2 - 0.3 b^2) \cdot \gamma_{m0}}{f_y}} > t_f$$
Where:
- $w = P / A_{plate}$: Uniform concrete bearing pressure ($\text{N/mm}^2$).
- $a, b$: Larger and smaller plate projections beyond the column profile ($\text{mm}$).
- $f_y$: Yield strength of the base plate steel ($\text{MPa}$).
- $\gamma_{m0} = 1.10$.

### 2.5 Reinforced Concrete Development Length ($L_d$)
Per IS 456:2000 Cl. 26.2.1, the development length required to anchor a deformed rebar of diameter $\phi$ in tension is:
$$L_d = \frac{\phi \cdot \sigma_s}{4 \cdot \tau_{bd}} = \frac{\phi \cdot (0.87 f_y)}{4 \cdot (1.6 \times \tau_{bd, plain})}$$
For M30 concrete and Fe500 rebar, $\tau_{bd} = 1.6 \times 1.5 = 2.4\text{ N/mm}^2$:
$$L_d = \frac{\phi \times (0.87 \times 500)}{4 \times 2.4} = \frac{435 \phi}{9.6} \approx 45.3 \phi$$
With Hilti post-installed chemical rebar systems (HIT-RE 500 V4 / HIT-HY 200), bond strengths typically exceed cast-in bars, enabling safe anchorage with shorter embedment depths.

---

## 3. Step-by-Step Worked Problems: 15 Core Exercises

### Problem 2.1: Eccentric Bolted Bracket Connection (Shear + Torsion)
**Context:** A structural bracket plate is connected to a vertical column flange using 5 high-strength bolts (Grade 8.8, $d = 16\text{ mm}$, $A_{nb} = 157\text{ mm}^2$) arranged in a single vertical line with pitch $p = 60\text{ mm}$ (total group depth $240\text{ mm}$). A vertical service load $P = 45\text{ kN}$ is applied at an eccentricity $e = 150\text{ mm}$ from the bolt group centroid.
Determine:
1. The polar moment of inertia $I_p$ of the bolt group.
2. The resultant shear force on the most critically stressed outer bolt.
3. Compare against the shear capacity of an M16 Gr 8.8 bolt ($V_{dsb} = 45.3\text{ kN}$).

**Detailed Solution:**
1. **Centroid and Coordinates:**
   - Centroid is at bolt 3 (the middle bolt): $y = 0$.
   - Bolt coordinates: Bolt 1: $y = +120\text{ mm}$; Bolt 2: $y = +60\text{ mm}$; Bolt 3: $y = 0$; Bolt 4: $y = -60\text{ mm}$; Bolt 5: $y = -120\text{ mm}$.
2. **Polar Moment of Inertia of the Bolt Group:**
   $$\sum r_i^2 = \sum y_i^2 = 2 \times (120^2 + 60^2) + 0^2 = 2 \times (14400 + 3600) = 2 \times 18000 = 36,000\text{ mm}^2$$
3. **Forces on Extreme Bolt 1 ($y = +120\text{ mm}$):**
   - Direct vertical shear force per bolt:
     $$F_v = \frac{P}{n} = \frac{45\text{ kN}}{5} = 9.0\text{ kN} \quad (\downarrow)$$
   - Torsional moment: $M_t = P \cdot e = 45\text{ kN} \times 150\text{ mm} = 6750\text{ kN}\cdot\text{mm}$.
   - Torsional shear force on bolt 1 (acts horizontally, perpendicular to radius):
     $$F_{mt} = \frac{M_t \cdot r_1}{\sum r_i^2} = \frac{6750\text{ kN}\cdot\text{mm} \times 120\text{ mm}}{36,000\text{ mm}^2} = \frac{810,000}{36,000} = 22.5\text{ kN} \quad (\rightarrow)$$
4. **Resultant Force on Bolt 1:**
   $$R_1 = \sqrt{F_v^2 + F_{mt}^2} = \sqrt{9.0^2 + 22.5^2} = \sqrt{81.0 + 506.25} = \sqrt{587.25} = 24.23\text{ kN}$$
5. **Capacity Check:**
   $$\text{Utilization Ratio (UR)} = \frac{R_1}{V_{dsb}} = \frac{24.23\text{ kN}}{45.30\text{ kN}} = 0.535 \quad (53.5\%)$$
   - **Conclusion:** Safe with substantial reserve capacity.

---

### Problem 2.2: Welded Bracket Connection Under Eccentric Shear
**Context:** A cantilever channel bracket is welded to a structural column using two vertical fillet welds of size $s = 6\text{ mm}$ and length $L = 200\text{ mm}$ spaced $b = 100\text{ mm}$ apart. A vertical load $V = 60\text{ kN}$ acts at an eccentricity $e = 120\text{ mm}$ from the weld group centroid. The steel is Grade E250 ($f_u = 410\text{ MPa}$, $\gamma_{mw} = 1.25$).
Verify the weld stress.

**Detailed Solution:**
1. **Weld Throat Area and Properties:**
   - Throat thickness: $t_t = 0.707 \times 6\text{ mm} = 4.24\text{ mm}$.
   - Total effective throat area: $A_w = 2 \times (L \cdot t_t) = 2 \times (200 \times 4.24) = 1696\text{ mm}^2$.
   - Centroid of two parallel vertical welds: at mid-length ($y = 0$) and midway between them ($x = 0$).
2. **Second Moment of Area of Weld Group:**
   - $I_{xx} = 2 \times \left[ \frac{t_t \cdot L^3}{12} \right] = 2 \times \left[ \frac{4.24 \times 200^3}{12} \right] = 2 \times 2,826,667 = 5.653 \times 10^6\text{ mm}^4$.
   - $I_{yy} = 2 \times \left[ (L \cdot t_t) \times (b/2)^2 \right] = 2 \times [848 \times 50^2] = 2 \times 2,120,000 = 4.24 \times 10^6\text{ mm}^4$.
   - Polar moment of inertia: $I_p = I_{xx} + I_{yy} = 5.653 \times 10^6 + 4.240 \times 10^6 = 9.893 \times 10^6\text{ mm}^4$.
3. **Applied Stresses on Critical Weld Corner ($x = 50\text{ mm}, y = 100\text{ mm}$):**
   - Direct shear stress:
     $$\tau_v = \frac{V}{A_w} = \frac{60,000\text{ N}}{1696\text{ mm}^2} = 35.38\text{ N/mm}^2 \quad (\downarrow)$$
   - Moment: $M = V \cdot e = 60,000\text{ N} \times 120\text{ mm} = 7.20 \times 10^6\text{ N}\cdot\text{mm}$.
   - Torsional horizontal component:
     $$\tau_{mh} = \frac{M \cdot y}{I_p} = \frac{7.20 \times 10^6 \times 100}{9.893 \times 10^6} = 72.78\text{ N/mm}^2 \quad (\rightarrow)$$
   - Torsional vertical component:
     $$\tau_{mv} = \frac{M \cdot x}{I_p} = \frac{7.20 \times 10^6 \times 50}{9.893 \times 10^6} = 36.39\text{ N/mm}^2 \quad (\downarrow)$$
4. **Total Resultant Shear Stress:**
   $$\tau_{total, v} = \tau_v + \tau_{mv} = 35.38 + 36.39 = 71.77\text{ N/mm}^2$$
   $$\tau_R = \sqrt{\tau_{total, v}^2 + \tau_{mh}^2} = \sqrt{71.77^2 + 72.78^2} = \sqrt{5151 + 5297} = \sqrt{10448} = 102.22\text{ N/mm}^2$$
5. **Allowable Weld Shear Stress:**
   $$f_{vwd} = \frac{f_u}{\sqrt{3} \cdot \gamma_{mw}} = \frac{410}{\sqrt{3} \times 1.25} = 189.37\text{ N/mm}^2$$
   - Utilization: $\tau_R / f_{vwd} = 102.22 / 189.37 = 54.0\%$. **Adequate.**

---

### Problem 2.3: Concrete Base Plate Bearing Pressure & Plate Thickness
**Context:** An industrial post with a base plate measuring $B = 250\text{ mm}$ by $L = 250\text{ mm}$ supports a concentric vertical service compressive load $P = 120\text{ kN}$ on a concrete foundation of grade M25 ($f_{ck} = 25\text{ MPa}$). The post profile is a square tube $100 \times 100\text{ mm}$ centered on the plate.
Calculate:
1. Concrete bearing stress $w$.
2. Permissible bearing strength of concrete per IS 456 / IS 800.
3. Minimum base plate thickness $t_s$ for E250 steel ($f_y = 250\text{ MPa}$).

**Detailed Solution:**
1. **Concrete Bearing Pressure:**
   $$w = \frac{P}{B \cdot L} = \frac{120,000\text{ N}}{250 \times 250\text{ mm}^2} = \frac{120,000}{62,500} = 1.92\text{ N/mm}^2$$
2. **Permissible Concrete Bearing Strength:**
   - Per IS 800:2007 Cl. 7.4.1, design bearing strength $q_c = 0.45 f_{ck} = 0.45 \times 25 = 11.25\text{ N/mm}^2$.
   - $w = 1.92\text{ N/mm}^2 \ll 11.25\text{ N/mm}^2$. (Bearing utilization = $17.1\%$).
3. **Plate Projection & Minimum Thickness:**
   - Projections: $a = b = \frac{250 - 100}{2} = 75\text{ mm}$.
   - Minimum thickness formula:
     $$t_s = \sqrt{\frac{2.5 \cdot w \cdot (a^2 - 0.3 b^2) \cdot \gamma_{m0}}{f_y}}$$
     $$a^2 - 0.3 b^2 = 75^2 - 0.3(75^2) = 0.70 \times 5625 = 3937.5\text{ mm}^2$$
     $$t_s = \sqrt{\frac{2.5 \times 1.92 \times 3937.5 \times 1.10}{250}} = \sqrt{\frac{20790}{250}} = \sqrt{83.16} = 9.12\text{ mm}$$
   - **Specification:** Provide a standard $10\text{ mm}$ or $12\text{ mm}$ plate thickness.

---

### Problem 2.4: Tension Development Length for Chemical Post-Installed Rebar
**Context:** A structural extension requires anchoring $16\text{ mm}$ diameter deformed rebar (Fe 500) into an existing M30 concrete wall ($f_{ck} = 30\text{ MPa}$). 
Compare:
1. Standard cast-in development length per IS 456:2000.
2. Embedment depth using Hilti HIT-RE 500 V4 epoxy adhesive, which achieves a characteristic bond strength $\tau_{Rk,ucr} = 15.0\text{ N/mm}^2$ in uncracked concrete ($\gamma_{Mc} = 1.50$).

**Detailed Solution:**
1. **Cast-in Rebar per IS 456:**
   - Basic $\tau_{bd} = 1.5\text{ N/mm}^2$ for M30. For deformed bars, increase by $60\%$: $\tau_{bd} = 2.4\text{ N/mm}^2$.
   $$L_{d, cast-in} = \frac{\phi \cdot 0.87 f_y}{4 \cdot \tau_{bd}} = \frac{16 \times (0.87 \times 500)}{4 \times 2.4} = \frac{6960}{9.6} = 725\text{ mm} \quad (\approx 45.3 \phi)$$
2. **Post-Installed Rebar with Hilti HIT-RE 500 V4:**
   - Design bond strength: $\tau_{Rd} = \tau_{Rk,ucr} / \gamma_{Mc} = 15.0 / 1.50 = 10.0\text{ N/mm}^2$.
   - Tensile force to develop rebar yield capacity:
     $$N_{Rd, steel} = A_s \cdot (0.87 f_y) = \frac{\pi \times 16^2}{4} \times (0.87 \times 500) = 201.06 \times 435 = 87,461\text{ N} \approx 87.5\text{ kN}$$
   - Required embedment depth $h_{ef}$:
     $$N_{Rd, bond} = \pi \cdot \phi \cdot h_{ef} \cdot \tau_{Rd} \ge 87,461\text{ N}$$
     $$h_{ef} = \frac{87,461}{\pi \times 16 \times 10.0} = \frac{87,461}{502.65} = 174\text{ mm} \quad (\approx 10.9 \phi)$$
   - **Value Engineering Benefit:** Embedment depth reduced from $725\text{ mm}$ to $174\text{ mm}$ (a $76\%$ reduction in drilling depth, drill bit wear, and installation labor).

---

### Problems 2.5 to 2.15: Conceptual & Numerical Practice Set

#### Problem 2.5: Block Shear Tear-Out Failure Mode
*Question:* Explain the mechanism of block shear failure in a bolted tension gusset plate and write the governing equation per IS 800:2007.
*Solution:* Block shear failure involves the tearing out of a block of material at the end of a member due to a combination of shear along a plane parallel to the force and tension along a perpendicular plane.
$$T_{db} = \min \left\{ \frac{A_{vg} f_y}{\sqrt{3} \gamma_{m0}} + \frac{0.9 A_{tn} f_u}{\gamma_{m1}}, \, \frac{0.9 A_{vn} f_u}{\sqrt{3} \gamma_{m1}} + \frac{A_{tg} f_y}{\gamma_{m0}} \right\}$$

#### Problem 2.6: Bearing vs Friction-Grip (HSFG) Bolts
*Question:* Why does an HSFG pre-tensioned bolted connection experience zero slip under service loads, and what role does the slip coefficient $\mu$ play?
*Solution:* HSFG bolts are tightened to a specified proof load $F_0$, clamping the steel plies together. Shear is resisted by friction between the faying surfaces ($V_{nsf} = \mu n_e K_h F_0$). As long as $V \le V_{nsf}$, no relative slip occurs, preventing hole elongation and fatigue failure.

#### Problem 2.7: Stiffened vs Unstiffened Base Plates
*Question:* How does adding vertical triangular gusset stiffeners to a column base plate modify the design moment and required plate thickness?
*Solution:* Gussets subdivide large cantilever plate spans into two-way or three-way supported plates. This reduces the effective cantilever projection $a$, cutting the bending moment (which scales with $a^2$) and allowing thinner plates ($t_s$ reduced by up to $40\%$), saving material cost.

#### Problem 2.8: Lamellar Tearing in Heavy Welded T-Joints
*Question:* What is lamellar tearing and how is it prevented in heavy welded base connections?
*Solution:* Lamellar tearing is subsurface terrace-like cracking in steel plates beneath heavy welds, caused by high through-thickness (Z-direction) tensile weld shrinkage strains. Prevention: use Z-grade steel (with guaranteed through-thickness ductility per EN 10164), modify joint detailing to minimize Z-direction shrinkage, or use forged/cast transition brackets.

#### Problem 2.9: Minimum Edge Distance Requirements
*Question:* What is the minimum edge distance for punched vs machine flame-cut bolt holes per IS 800:2007, and why does this limit exist?
*Solution:* Per IS 800 Cl. 10.2.4:
- Sheared or hand flame cut edges: $e_{min} = 1.7 \cdot d_0$
- Rolled, machine-cut, or sawn edges: $e_{min} = 1.5 \cdot d_0$
This prevents premature edge breakout or splitting failure under bolt bearing stresses.

#### Problem 2.10: Weld Sizing and Effective Throat
*Question:* For an unequal fillet weld with leg lengths $s_1 = 6\text{ mm}$ and $s_2 = 8\text{ mm}$ at $90^\circ$, what is the effective throat thickness?
*Solution:* The throat is the perpendicular distance from the root to the hypotenuse:
$$t_t = \frac{s_1 \cdot s_2}{\sqrt{s_1^2 + s_2^2}} = \frac{6 \times 8}{\sqrt{36 + 64}} = \frac{48}{10} = 4.8\text{ mm}$$

#### Problem 2.11: Concrete Punching Shear in Footings
*Question:* What is the critical perimeter for punching shear around a rectangular column base plate of size $a \times b$ in an RCC slab of effective depth $d$ per IS 456?
*Solution:* The critical section is located at a distance $d/2$ from the periphery of the base plate. Critical perimeter $b_0 = 2(a + d) + 2(b + d) = 2(a + b + 2d)$.

#### Problem 2.12: Modular Channel Connection Mechanics
*Question:* How does a Hilti channel nut with serrated teeth transfer shear forces along the longitudinal axis of an open modular channel?
*Solution:* The channel nut features precision cold-formed teeth that bite into the inward-curved channel lips when torqued. This mechanical interlock provides positive shear resistance along the channel axis, preventing slip without requiring drilling or welding.

#### Problem 2.13: Combined Shear and Tension in Bolts
*Question:* State the interaction equation for bolts subjected to simultaneous shear and tension per IS 800:2007.
*Solution:*
$$\left( \frac{V_{sb}}{V_{dsb}} \right)^2 + \left( \frac{T_b}{T_{db}} \right)^2 \le 1.0$$

#### Problem 2.14: Moment-Rotation Classification of Connections
*Question:* What differentiates a nominally pinned, semi-rigid, and fully rigid connection according to Eurocode 3?
*Solution:* Based on initial rotational stiffness $S_{j,ini}$:
- Rigid: $S_{j,ini} \ge k_b \cdot E I_b / L_b$ (transfers moment with $<10\%$ rotation).
- Pinned: $S_{j,ini} \le 0.5 \cdot E I_b / L_b$ (rotates freely, transfers $<20\%$ of plastic moment).
- Semi-rigid: Intermediate stiffness; behavior must be explicitly modeled in global analysis.

#### Problem 2.15: Corrosion Protection in Dissimilar Metal Connections
*Question:* What is galvanic corrosion and how is it mitigated when connecting stainless steel brackets to hot-dip galvanized carbon steel members?
*Solution:* Galvanic corrosion occurs when two metals with different electrochemical potentials are in electrical contact in an electrolyte. Carbon/galvanized steel acts as an anode and corrodes rapidly. Mitigation: insert non-conductive dielectric isolation washers (e.g., EPDM, polyamide, or neoflon) between the dissimilar metals.

---

## 4. Key Takeaways & Revision Checklist
- [ ] Check bolt capacities for both shear and bearing ($V_{dsb}$ and $V_{dpb}$); the smaller governs.
- [ ] Account for prying action whenever tensile connections have flexible flanges.
- [ ] Fillet weld design throat is $0.707 \times s$ for standard $90^\circ$ joints.
- [ ] Post-installed chemical rebar drastically reduces required embedment depth compared to cast-in bars.

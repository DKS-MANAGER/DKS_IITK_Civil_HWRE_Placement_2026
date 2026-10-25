# Module 03: Anchors, Support Systems, and Failure Modes

`[CORE TECHNICAL SYLLABUS — GLOBAL VALUE ENGINEERING HUB]`
`[EVIDENCE CLASSIFICATION: OFFICIAL HILTI TECHNICAL PRINCIPLES / ACI 318-19 CH 17 / EN 1992-4]`

---

## 1. Executive Summary & Learning Objectives

Anchoring technology and modular support systems form the core of Hilti's engineering solutions. In industrial energy facilities, chemical plants, offshore platforms, and commercial megaprojects, heavy pipework, cable trays, and equipment must be safely connected to concrete and steel host structures.

### Key Learning Objectives
1. **Anchorage Classification & Load Transfer:** Differentiate mechanical expansion, undercut, concrete screw, and adhesive (chemical) anchors; explain mechanical interlock, friction, and chemical bonding mechanisms.
2. **Concrete Capacity Design (CCD) Method:** Master the ACI 318-19 Chapter 17 / EN 1992-4 calculation methodology for single anchors and anchor groups in concrete.
3. **Tensile Failure Modes:** Identify and calculate capacities for the 5 fundamental tension failure modes:
   - Steel tensile failure ($N_{sa}$)
   - Concrete cone breakout ($N_{cb} / N_{cbg}$)
   - Pullout / bond failure ($N_p / N_{a} / N_{ag}$)
   - Concrete splitting failure ($N_{sp}$)
   - Concrete side-face blowout ($N_{sb}$)
4. **Shear Failure Modes:** Identify and calculate capacities for the 3 fundamental shear failure modes:
   - Steel shear failure ($V_{sa}$)
   - Concrete edge breakout ($V_{cb} / V_{cbg}$)
   - Concrete pryout failure ($V_{cp} / V_{cpg}$)
5. **Influence of Environmental & Base Material Factors:** Distinguish cracked vs uncracked concrete design assumptions; account for seismic cyclic loading (C1/C2 categories), fire resistance, edge distances ($c$), spacing ($s$), and embedment depth ($h_{ef}$).
6. **Modular Support Systems (Hilti MT & MQ):** Understand structural behavior of cold-formed channel systems, 3D connectors, beam clamps, vibration isolation, and thermal pipe shoes.

---

## 2. Fundamental Principles & Governing Equations

### 2.1 The Concrete Capacity Design (CCD) Model
Developed by Fuchs, Eligehausen, and Breen (1995), the CCD method idealizes the concrete cone breakout surface as a pyramid with an inclination angle of approximately $35^\circ$ to the concrete surface.
Consequently, the base of the breakout pyramid extends a distance of $1.5 \cdot h_{ef}$ from the anchor centerline in all directions.
- **Idealized Breakout Area for a Single Anchor (no edge restrictions):**
  $$A_{Nc0} = 9 \cdot h_{ef}^2 = (3 h_{ef}) \times (3 h_{ef})$$
- **Critical Edge Distance ($c_{cr,N}$):**
  $$c_{cr,N} = 1.5 \cdot h_{ef}$$
  If actual edge distance $c < 1.5 h_{ef}$, the breakout cone is truncated by the edge, reducing capacity.
- **Critical Spacing ($s_{cr,N}$):**
  $$s_{cr,N} = 3.0 \cdot h_{ef}$$
  If anchor spacing $s < 3.0 h_{ef}$, individual cones overlap, and the group must be evaluated collectively.

### 2.2 Basic Concrete Cone Breakout Strength ($N_b$)
For a single anchor in cracked concrete in tension (ACI 318-19 Cl. 17.6.2.2 / EN 1992-4):
$$N_b = k_c \cdot \lambda_a \cdot \sqrt{f'_c} \cdot h_{ef}^{1.5}$$
Where:
- $k_c$: Calibration coefficient:
  - Post-installed anchors in cracked concrete: $k_c = 17\text{ (SI units: N, mm)}$ [ACI 318]; $k_{cr} = 7.7$ [EN 1992-4].
  - Post-installed anchors in uncracked concrete: $k_c = 24\text{ (SI units)}$ [ACI 318]; $k_{ucr} = 11.0$ [EN 1992-4].
- $\lambda_a$: Lightweight concrete modification factor ($1.0$ for normal-weight concrete).
- $f'_c$: Specified concrete compressive cylinder strength ($\text{MPa}$).
- $h_{ef}$: Effective embedment depth ($\text{mm}$).

For an anchor group or single anchor affected by edges, the design concrete breakout strength is:
$$N_{cbg} = \frac{A_{Nc}}{A_{Nc0}} \cdot \psi_{ed,N} \cdot \psi_{s,N} \cdot \psi_{c,N} \cdot \psi_{ec,N} \cdot N_b$$
Where:
- $A_{Nc} / A_{Nc0}$: Geometric area ratio of actual to ideal projected cone area.
- $\psi_{ed,N} = \min \left( 1.0, \, 0.7 + 0.3 \frac{c_{min}}{c_{cr,N}} \right)$: Edge modification factor.
- $\psi_{ec,N} = \frac{1}{1 + \frac{2 e'_N}{3 h_{ef}}} \le 1.0$: Eccentricity modification factor.
- $\psi_{c,N}$: Cracking factor ($1.0$ for cracked concrete, $1.25$ to $1.4$ for uncracked concrete).

### 2.3 Concrete Pryout Failure Under Shear ($V_{cp}$)
When short, stocky anchors are loaded in shear, they do not fail the steel bolt; instead, the bottom of the anchor rotates and pries out a concrete cone behind the anchor:
$$V_{cp} = k_{cp} \cdot N_{cb}$$
Where:
- $k_{cp} = 1.0$ for $h_{ef} < 65\text{ mm}$
- $k_{cp} = 2.0$ for $h_{ef} \ge 65\text{ mm}$

### 2.4 Concrete Edge Breakout Under Shear ($V_{cb}$)
For shear acting toward an edge at distance $c_1$:
$$V_b = \min \left( 7 \left( \frac{l_e}{d_a} \right)^{0.2} \sqrt{d_a}, \, 9 \right) \cdot \lambda_a \cdot \sqrt{f'_c} \cdot c_1^{1.5}$$
$$V_{cbg} = \frac{A_{Vc}}{A_{Vc0}} \cdot \psi_{ed,V} \cdot \psi_{h,V} \cdot \psi_{c,V} \cdot \psi_{ec,V} \cdot V_b$$
Where $A_{Vc0} = 4.5 c_1^2$ is the ideal projected area of a single anchor on the side face.

### 2.5 Tension and Shear Interaction
When an anchor is simultaneously subjected to factored tension $N_{ua}$ and factored shear $V_{ua}$:
$$\left( \frac{N_{ua}}{\phi N_n} \right)^\alpha + \left( \frac{V_{ua}}{\phi V_n} \right)^\alpha \le 1.0$$
Under ACI 318-19:
- If $N_{ua} / (\phi N_n) \le 0.2$, full shear capacity is allowed.
- If $V_{ua} / (\phi V_n) \le 0.2$, full tension capacity is allowed.
- Otherwise, a trilinear or power-law interaction with $\alpha = 5/3 \approx 1.67$ is used.

---

## 3. 30 Solved Anchorage & Support System Problems

### Problem 3.1: Concrete Cone Breakout Strength Calculation (Single Anchor)
**Context:** A single Hilti HST3 mechanical expansion anchor ($M16$) is installed in a thick uncracked concrete slab ($f'_c = 30\text{ MPa}$) far from any concrete edges ($c > 3 h_{ef}$). The effective embedment depth is $h_{ef} = 100\text{ mm}$.
Calculate:
1. The ideal projected concrete breakout area $A_{Nc0}$.
2. The basic concrete cone breakout strength $N_b$ per ACI 318-19.
3. The design concrete breakout strength $\phi N_{cb}$ (with strength reduction factor $\phi = 0.65$ for Condition B).

**Detailed Solution:**
1. **Ideal Projected Area:**
   $$A_{Nc0} = 9 \cdot h_{ef}^2 = 9 \times (100\text{ mm})^2 = 90,000\text{ mm}^2$$
   - Verification: $3 h_{ef} \times 3 h_{ef} = 300\text{ mm} \times 300\text{ mm} = 90,000\text{ mm}^2$.
2. **Basic Concrete Breakout Strength $N_b$ (Uncracked Concrete):**
   - For uncracked concrete: $k_c = 24$.
   $$N_b = k_c \cdot \sqrt{f'_c} \cdot h_{ef}^{1.5} = 24 \times \sqrt{30} \times (100)^{1.5}$$
   $$\sqrt{30} \approx 5.4772; \quad (100)^{1.5} = 100 \times \sqrt{100} = 1000$$
   $$N_b = 24 \times 5.4772 \times 1000 = 131,453\text{ N} \approx 131.45\text{ kN}$$
3. **Design Strength $\phi N_{cb}$:**
   - Since $c \ge 1.5 h_{ef}$ and there is no eccentricity: $A_{Nc} = A_{Nc0} \implies A_{Nc}/A_{Nc0} = 1.0$.
   - Modification factors $\psi = 1.0$.
   - $\phi N_{cb} = \phi \cdot N_b = 0.65 \times 131.45\text{ kN} = 85.44\text{ kN}$.

---

### Problem 3.2: Group Effect and Edge Truncation in Tension
**Context:** A 2-anchor bracket ($s = 150\text{ mm}$) is placed parallel to a concrete slab edge at an edge distance $c_1 = 80\text{ mm}$. The slab thickness is $h = 200\text{ mm}$. Anchor embedment depth is $h_{ef} = 80\text{ mm}$. Concrete is normal-weight, cracked, $f'_c = 25\text{ MPa}$.
Compute:
1. The critical edge distance $c_{cr,N}$ and spacing $s_{cr,N}$.
2. The actual projected area $A_{Nc}$ vs ideal $A_{Nc0}$.
3. The group breakout capacity $N_{cbg}$.

**Detailed Solution:**
1. **Critical Dimensions:**
   - $c_{cr,N} = 1.5 \cdot h_{ef} = 1.5 \times 80 = 120\text{ mm}$.
   - $s_{cr,N} = 3.0 \cdot h_{ef} = 3.0 \times 80 = 240\text{ mm}$.
   - Since actual $c_1 = 80\text{ mm} < 120\text{ mm}$, edge truncation occurs.
   - Since actual $s = 150\text{ mm} < 240\text{ mm}$, cone overlap occurs.
2. **Projected Areas:**
   - Ideal area for single anchor: $A_{Nc0} = 9 \cdot h_{ef}^2 = 9 \times 80^2 = 57,600\text{ mm}^2$.
   - Actual group breakout dimensions:
     - Parallel to edge: width $b = s + 2(1.5 h_{ef}) = 150 + 2(120) = 390\text{ mm}$.
     - Perpendicular to edge: depth extends $c_1$ toward the edge ($80\text{ mm}$) and $1.5 h_{ef}$ away ($120\text{ mm}$).
     - Total perpendicular length: $d = c_1 + 1.5 h_{ef} = 80 + 120 = 200\text{ mm}$.
     - Total projected area: $A_{Nc} = b \cdot d = 390 \times 200 = 78,000\text{ mm}^2$.
     - Ratio: $A_{Nc} / A_{Nc0} = 78,000 / 57,600 = 1.354$.
3. **Modification Factors:**
   - Edge factor: $\psi_{ed,N} = 0.7 + 0.3 \cdot \frac{c_1}{c_{cr,N}} = 0.7 + 0.3 \left(\frac{80}{120}\right) = 0.7 + 0.20 = 0.90$.
   - Basic single anchor strength (cracked concrete, $k_c = 17$):
     $$N_b = 17 \times \sqrt{25} \times (80)^{1.5} = 17 \times 5 \times 715.54 = 60,821\text{ N} = 60.82\text{ kN}$$
4. **Group Breakout Strength:**
   $$N_{cbg} = \frac{A_{Nc}}{A_{Nc0}} \cdot \psi_{ed,N} \cdot N_b = 1.354 \times 0.90 \times 60.82\text{ kN} = 74.12\text{ kN}$$

---

### Problem 3.3: Concrete Pryout Capacity Check Under High Shear
**Context:** A base plate with 4 welded studs ($h_{ef} = 50\text{ mm}$) is cast into the center of a large concrete foundation ($f'_c = 30\text{ MPa}$). A pure horizontal shear load $V_u = 75\text{ kN}$ is applied to the plate. The single anchor breakout in tension is calculated as $N_{cb} = 22.5\text{ kN}$, and for the 4-anchor group $N_{cbg} = 65.0\text{ kN}$.
Determine if the anchor group is safe against concrete pryout failure ($\phi = 0.70$).

**Detailed Solution:**
1. **Pryout Factor $k_{cp}$:**
   - Because $h_{ef} = 50\text{ mm} < 65\text{ mm}$, $k_{cp} = 1.0$.
2. **Nominal Pryout Strength:**
   $$V_{cpg} = k_{cp} \cdot N_{cbg} = 1.0 \times 65.0\text{ kN} = 65.0\text{ kN}$$
3. **Design Pryout Strength:**
   $$\phi V_{cpg} = 0.70 \times 65.0\text{ kN} = 45.5\text{ kN}$$
4. **Demand vs Capacity Check:**
   - Applied shear: $V_u = 75.0\text{ kN}$.
   - $\text{UR} = V_u / (\phi V_{cpg}) = 75.0 / 45.5 = 1.65$ ($165\%$ — **FAILS**).
5. **Value Engineering Remediation:**
   - Increase embedment depth to $h_{ef} \ge 65\text{ mm}$ (e.g., $h_{ef} = 80\text{ mm}$).
   - This changes $k_{cp}$ from $1.0$ to $2.0$ AND increases $N_{cbg}$ proportionally to $h_{ef}^{1.5}$, increasing pryout capacity by $>300\%$.

---

### Problem 3.4: Concrete Edge Breakout in Shear
**Context:** A single anchor of diameter $d_a = 16\text{ mm}$ and embedment $h_{ef} = 100\text{ mm}$ carries a shear force directed toward a free edge. Edge distance $c_1 = 60\text{ mm}$. Concrete is normal-weight, cracked, $f'_c = 25\text{ MPa}$.
Find the basic concrete edge breakout strength $V_b$.

**Detailed Solution:**
1. **Load Bearing Length $l_e$:**
   - For standard anchors: $l_e = h_{ef} = 100\text{ mm} \le 8 d_a = 128\text{ mm}$.
   - Ratio $l_e / d_a = 100 / 16 = 6.25$.
2. **Basic Shear Edge Breakout Formula:**
   $$V_b = 7 \left( \frac{l_e}{d_a} \right)^{0.2} \sqrt{d_a} \cdot \sqrt{f'_c} \cdot c_1^{1.5}$$
   - Term 1: $7 \times (6.25)^{0.2} \times \sqrt{16} = 7 \times 1.4427 \times 4 = 40.40$.
   - Cap check: $40.40$ vs $9 \sqrt{d_a} = 9 \times 4 = 36.0$. Governed by $36.0$.
   - Term 2: $\sqrt{f'_c} = \sqrt{25} = 5.0$.
   - Term 3: $c_1^{1.5} = 60^{1.5} = 60 \times \sqrt{60} = 60 \times 7.746 = 464.76$.
3. **Calculation:**
   $$V_b = 36.0 \times 5.0 \times 464.76 = 83,657\text{ N} \approx 83.66\text{ kN}$$

---

### Problems 3.5 to 3.30: Core Anchoring & Support Systems Questions

#### Problem 3.5: Mechanical Expansion vs Chemical Adhesive Anchors
*Question:* Contrast the load-transfer mechanics of torque-controlled expansion anchors (e.g., Hilti HST3) with chemical adhesive anchors (e.g., Hilti HIT-RE 500 V4).
*Solution:* Expansion anchors transfer load via localized radial expansion pressure against the borehole wall, generating frictional resistance. Chemical adhesive anchors transfer load via continuous shear bond along the entire embedment length between steel threaded rod, adhesive mortar, and concrete. Adhesives generate virtually zero expansion pressure, permitting substantially smaller edge distances and closer anchor spacing.

#### Problem 3.6: Cracked vs Uncracked Concrete Design Assumption
*Question:* Why does modern building code practice (ACI 318-19, EN 1992-4) require assuming cracked concrete as the standard design baseline unless proven otherwise?
*Solution:* In reinforced concrete structures under service loads, tensile stresses naturally induce hairline cracks ($\Delta w \le 0.3\text{ mm}$). If a crack passes through an expansion anchor location, the anchor's expansion sleeve can lose grip unless specifically qualified for cracked concrete (featuring an active follow-up expansion cone). Designing for uncracked concrete requires rigorous structural analysis proving tension does not exceed $f_{ctm}$.

#### Problem 3.7: Seismic Anchor Qualification Categories C1 vs C2
*Question:* What is the distinction between European Technical Assessment (ETA) seismic qualification categories C1 and C2?
*Solution:*
- **C1 Category:** For low seismicity or non-structural elements; tested under pulsating tension and alternating shear at fixed crack widths of $0.5\text{ mm}$.
- **C2 Category:** For high seismicity and critical structural connections; subjected to severe cyclic crack opening/closing tests up to $0.8\text{ mm}$ under sustained loads.

#### Problem 3.8: Concrete Screw Anchors (Hilti HUS) Mechanics
*Question:* How do concrete screw anchors (e.g., Hilti HUS4) achieve anchorage and what are their value engineering advantages?
*Solution:* Specially hardened hi-lo threads cut into the concrete wall during installation, creating a mechanical interlock without expansion stress. VE advantages: fully removable, 100% reusable in temporary applications, zero curing time, tight edge clearance, and up to 50% faster installation than chemical anchors.

#### Problem 3.9: Influence of Cleaning Method on Adhesive Anchor Bond Strength
*Question:* What occurs to the characteristic bond strength $\tau_{Rk}$ of an adhesive anchor if borehole dust is not cleaned per manufacturer instructions?
*Solution:* Drilling dust forms an unbonded interface layer between mortar and concrete, reducing tensile capacity by up to $60\% - 80\%$, leading to premature pullout. Hilti SafeSet technology (using hollow drill bits attached to HEPA vacuums like Hilti TE-CD) cleans holes automatically during drilling, eliminating human error.

#### Problem 3.10: Sustained Load (Creep) in Adhesive Anchors
*Question:* Why do codes impose a sustained load factor $\psi_{sus}$ on adhesive anchors in tension?
*Solution:* Organic polymer resins (epoxies, vinylesters) are susceptible to viscoelastic creep under long-term sustained tensile stress, exacerbated by elevated service temperatures. $\psi_{sus}$ derates capacity to prevent creep-rupture failure over the 50-year or 100-year design life.

#### Problem 3.11: Stand-off Installation Mechanics
*Question:* In facade or pipe support anchoring with a non-shrink grout pad ($t_{grout} = 40\text{ mm}$), why does shear loading induce bending in the anchor rods?
*Solution:* The grout layer separates the fixture from the concrete substrate. Unless clamping and bearing are verified, shear force $V$ acts over lever arm $l = t_{grout} + 0.5 d$, inducing a bending moment $M = V \cdot l$ in the anchor shank, which significantly reduces combined shear-bending capacity.

#### Problem 3.12: Modular Strut Channel Bending Capacity (Hilti MT vs MQ)
*Question:* What structural advantage does the Hilti MT modular system offer over standard light-gauge strut profiles?
*Solution:* MT channels feature optimized cross-sectional geometries with localized stiffeners, higher steel grades ($S350$ / $S450$), and Zinc-Magnesium coatings (ZM). This provides superior torsional and lateral-torsional buckling resistance, allowing longer spans and higher concentrated loads while reducing overall steel tonnage.

#### Problem 3.13: Thermal Expansion in Pipe Support Anchors
*Question:* A hot steam pipe expands longitudinally, pushing against an anchor shoe. If the support connection is rigid, what danger arises at the base concrete anchors?
*Solution:* The massive axial thermal thrust force of the pipe is transferred directly to the anchor bolts as an extreme shear load, potentially exceeding concrete edge breakout or anchor shear capacity. The value engineering solution is incorporating Hilti low-friction PTFE/slotted sliding guides.

#### Problem 3.14: Concrete Splitting Failure ($N_{sp}$)
*Question:* What governs concrete splitting failure and how is it prevented?
*Solution:* Splitting occurs during anchor torquing or loading when member dimensions (slab thickness $h$ or edge distance $c$) are too small to resist radial splitting forces. Prevented by adhering to minimum member thickness $h_{min}$, minimum edge distance $c_{min}$, or providing supplementary hairpin reinforcement.

#### Problem 3.15: Side-Face Blowout Failure ($N_{sb}$)
*Question:* Under what physical condition does side-face blowout occur?
*Solution:* It occurs in deep embedments with small edge distances ($c < 0.4 h_{ef}$) subjected to high tension. The expansion cone or headed stud creates high lateral compressive bursting stresses that blow out the thin concrete side cover before a full surface cone can develop.

#### Problem 3.16: Anchor Channel (Hilti HAC) Load Transfer
*Question:* What are cast-in anchor channels and what is their primary value engineering advantage in industrial projects?
*Solution:* C-shaped steel channels with welded I-anchors cast into concrete before pouring. T-head bolts lock into the channel lips. VE advantage: completely eliminates drilling into reinforced concrete (no rebar hits, no silica dust, no noise), accommodates 3D field adjustments, and allows immediate high-capacity loading.

#### Problem 3.17: Group Tension Eccentricity Factor ($\psi_{ec,N}$)
*Question:* If a 2-anchor group carries an overturning moment causing tension in only one anchor ($e'_N = 50\text{ mm}$ with $h_{ef} = 100\text{ mm}$), compute $\psi_{ec,N}$.
*Solution:*
$$\psi_{ec,N} = \frac{1}{1 + \frac{2 e'_N}{3 h_{ef}}} = \frac{1}{1 + \frac{2(50)}{3(100)}} = \frac{1}{1 + 0.333} = \frac{1}{1.333} = 0.75$$
Capacity is reduced by $25\%$ due to non-uniform load distribution.

#### Problem 3.18: Post-Installed Rebar vs Anchor Theory
*Question:* When is a connection designed using post-installed rebar theory (rebar provisions of ACI 318 / IS 456) instead of anchor theory (CCD method)?
*Solution:* Rebar theory applies when post-installed bars behave like cast-in reinforcement—transferring load via tension lap splices to existing rebar cages in reinforced structural members (e.g., column/wall foundations, slab extensions). Anchor theory applies to steel fixtures connecting to concrete where concrete breakout cones govern.

#### Problem 3.19: Fire Exposure Behavior of Fasteners
*Question:* How do post-installed anchors behave under ISO 834 fire curves, and what differentiates mechanical from adhesive anchors?
*Solution:* In fires, steel loses yield strength and modulus above $400^\circ\text{C}$. Adhesive resins decompose at glass transition temperatures ($T_g \approx 60^\circ - 120^\circ\text{C}$) unless protected by deep embedment or intumescent firestop jackets. Mechanical metallic anchors retain higher residual load-bearing capacity under fire ratings (R30 to R120).

#### Problem 3.20: Cable Tray Trapeze Modular Support Design
*Question:* A trapeze support carrying 3 tiers of high-voltage cables has a total design load of $12\text{ kN}$. It is suspended from an overhead concrete ceiling by two vertical drop rods. Calculate the tensile force in each rod and the required anchor capacity.
*Solution:* Symmetric load: $N = 12\text{ kN} / 2 = 6.0\text{ kN}$ per drop rod. Factored tensile demand $N_u = 1.5 \times 6.0 = 9.0\text{ kN}$. Overhead anchors must be qualified for tension in cracked concrete overhead applications (e.g., Hilti HST3 or HUS4).

#### Problem 3.21: Influence of Compressive Base Stress on Shear Capacity
*Question:* How does a high compressive normal force between a steel base plate and concrete improve the shear resistance of the anchorage?
*Solution:* Normal compression mobilizes friction between the base plate and concrete substrate ($V_{friction} = \mu \cdot N_{comp}$, where $\mu \approx 0.2 - 0.45$). This friction carries shear directly into the concrete, relieving the anchor bolts of shear and pryout demands.

#### Problem 3.22: Slotted Holes in Anchor Base Plates
*Question:* Why do base plates frequently have oversized or slotted anchor holes, and how does this affect shear distribution among multiple anchors?
*Solution:* Oversized holes accommodate drilling tolerances and rebar avoidance. However, under shear loading, anchors may not bear simultaneously due to hole clearance gaps. Codes dictate that only anchors in direct bearing can be assumed to share shear, or welded washer plates must be used.

#### Problem 3.23: Hilti PROFIS Engineering Software Workflow
*Question:* How does PROFIS Engineering go beyond traditional rigid base plate theory?
*Solution:* PROFIS integrates Component-Based Finite Element Modeling (CBFEM) to model base plate flexibility, anchor stiffness, and concrete contact stresses realistically. This accurately reveals prying forces and non-linear load distributions that rigid plate assumptions miss.

#### Problem 3.24: Anchor Bolt Pre-Tensioning Loss
*Question:* Why does an anchor bolt lose part of its initial installation torque tension over time?
*Solution:* Pre-tension relaxation occurs due to micro-cracking and creep of the concrete under the expansion sleeve/bearing area, as well as settling of the base plate and thread relaxation. Long-term anchorage design relies on mechanical interlock rather than friction.

#### Problem 3.25: Fatigue Loading on Anchorages
*Question:* What fatigue failure mode governs high-cycle vibrating pump supports anchored to concrete?
*Solution:* High-cycle fatigue failure of the anchor steel rod at the thread root or weld interface. Requires derating steel strength using S-N Wöhler curves and ensuring dynamic expansion sleeves prevent loosening.

#### Problem 3.26: Corrosive Industrial Atmospheres (C4 / C5 Environments)
*Question:* What fastener metallurgy is mandated for offshore platforms or chemical plants with high salinity and sulfur dioxide exposure?
*Solution:* Standard electro-galvanized ($5-10\,\mu\text{m}$) steel corrodes rapidly. High-corrosion environments require Hot-Dip Galvanized (HDZ, $\ge 45\,\mu\text{m}$), A4 (AISI 316) marine-grade stainless steel, or High Corrosion Resistant (HCR, e.g., 1.4529 duplex) steels to prevent stress corrosion cracking.

#### Problem 3.27: Value Engineering: Welded Pipe Shoe vs Modular Clamp Shoe
*Question:* Contrast the installation economics of welding pipe shoes to structural beams versus using Hilti modular beam clamp assemblies.
*Solution:* Welded shoes require hot-work permits, fire watches, mobile welding rigs, post-weld NDT, and paint touch-ups. Hilti modular clamps bolt directly onto structural flanges without drilling or welding, reducing installation time by up to $70\%$ and maintaining structural galvanization integrity.

#### Problem 3.28: Hollow Core Precast Slab Anchoring
*Question:* What anchor type is utilized when fastening to precast prestressed hollow-core concrete slabs with thin webs/flanges?
*Solution:* Specialty sleeve anchors (e.g., Hilti HUS-H with short embedment, or toggle/expansion systems like Hilti HKH) that expand or grip securely within the hollow void or thin bottom compressive flange without damaging prestressing strands.

#### Problem 3.29: Pullout vs Concrete Cone Breakout
*Question:* What is the mathematical condition determining whether an anchor fails by pullout ($N_p$) or concrete cone breakout ($N_{cb}$)?
*Solution:* The governing failure mode is the minimum nominal strength: $\min(N_p, N_{cb})$. If bearing area or adhesive bond is small relative to embedment depth, $N_p < N_{cb}$ and pullout governs without fracturing the surrounding concrete cone.

#### Problem 3.30: Summary of Anchor Design Safety Factors
*Question:* Summarize the typical resistance factors ($\phi$) under ACI 318-19 Chapter 17 for steel failure vs concrete breakout.
*Solution:*
- Steel failure (ductile): $\phi = 0.75$ (tension), $\phi = 0.65$ (shear).
- Concrete breakout / pullout / pryout (Condition B, no supplementary rebar): $\phi = 0.65$ (tension), $\phi = 0.70$ (shear).
- Concrete failure modes receive lower $\phi$ factors due to the brittle nature of concrete fracture compared to ductile steel yielding.

---

## 4. Key Takeaways & Revision Checklist
- [ ] Memorize the 5 tension failure modes and 3 shear failure modes.
- [ ] $A_{Nc0} = 9 h_{ef}^2$, $c_{cr,N} = 1.5 h_{ef}$, $s_{cr,N} = 3.0 h_{ef}$.
- [ ] Pryout: $k_{cp} = 1.0$ ($h_{ef} < 65\text{ mm}$); $k_{cp} = 2.0$ ($h_{ef} \ge 65\text{ mm}$).
- [ ] Concrete screws (HUS) cut threads; expansion anchors (HST) exert radial pressure; chemical anchors (HIT) bond continuously.

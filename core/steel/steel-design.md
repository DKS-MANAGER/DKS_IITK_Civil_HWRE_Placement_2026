# Steel Structures Design

> **Placement Priority:** P0 — Required for L&T, Tata Projects, PSUs, consulting firms
> **GATE-O-PEDIA Reference:** Chapter 5 (1,986 lines, 60 topics, 12 formulas)
> **Canonical Page:** `core/steel/steel-design.md`
> **Design Code:** IS 800:2007 (General Construction in Steel)

---

## Scope

Steel structures are built up with hot-rolled steel sections. Design follows the **Limit State Method** per IS 800:2007. Steel design is a core interview topic for L&T, Tata Projects, AECOM, and PSUs (BPCL, EIL, NHPC).

| Domain | Relevance |
|--------|-----------|
| Industrial Buildings | Roof trusses, gantry girders |
| Bridges | Plate girders, trusses |
| Connections | Bolted, welded, eccentric |
| Tension/Compression | Members, bracing, columns |
| Interview | IS 800 provisions, connection design |
| Software | STAAD, Tekla, IDEA StatiCa |

---

## 1. Materials & Specifications

### Types of Structural Steel

| IS Code | Type | Designation |
|---------|------|-------------|
| IS 226 | Standard quality (most common) | Fe 410-S |
| IS 2062 | Fusion welding quality | Fe 410 WA/WB/WC |
| IS 961 | High tensile steel | Fe 570-HT, Fe 540-W-HT |
| IS 1977 | Ordinary quality | — |
| IS 8500 | Medium & high strength | Fe 440, Fe 540, Fe 590 |

### Steel Grades (IS 800:2007)

| Grade | UTS (MPa) | Yield (MPa) | Elongation |
|-------|-----------|-------------|------------|
| E250 (Fe 410A/B/C) | 410 | 250 | 23% |
| E350 | 410 | 350 | 22% |
| E410 | 440 | 410 | 22% |
| E450 | 540 | 450 | 20% |
| E550 | 590 | 550 | 20% |

### Physical Properties (IS 800:2007)

| Property | Value |
|----------|-------|
| Specific gravity | 7.85 |
| Unit mass | 7850 kg/m³ |
| Modulus of elasticity (E) | $2 \times 10^5$ N/mm² |
| Modulus of rigidity (G) | $0.769 \times 10^5$ N/mm² |
| Coefficient of thermal expansion | $12 \times 10^{-6}$/°C |
| Poisson's ratio | 0.30 |

### Rolled Steel Sections

| Section | Designation Example |
|---------|---------------------|
| I-beam | ISLB 500 at 735.75 N/m |
| Channel | ISLC 350 at 380.63 N/m |
| T-section | ISNT 125 at 274 N/m |
| Angle | ISA 75 × 75 × 6 mm |
| Column section | SC |

### WHY is steel used for long-span structures?

Steel has a very high **strength-to-weight ratio** — it's strong in both tension and compression, unlike concrete which is weak in tension. This allows slender, lightweight members that can span long distances (bridges, industrial buildings, towers). Steel is also ductile, homogeneous, and can be prefabricated, making construction fast and reliable.

---

## 2. Limit State Design (IS 800:2007)

### Limit States

**Limit state of strength:**
- Strength (yield, buckling)
- Stability against overturning and sway
- Fracture due to fatigue
- Plastic collapse
- Brittle fracture

**Serviceability limit state:**
- Deflection
- Vibration
- Fatigue checks
- Corrosion
- Fire

### Design Requirement

$$\text{Design Action } (S_d) \le \text{Design Strength } (R_d)$$

Where $S_d = \gamma_f \times$ characteristic load, and $\gamma_f$, $\gamma_m$ are partial safety factors.

### Partial Safety Factors (Loads)

| Combination | DL | LL | WL/EL |
|-------------|----|----|-------|
| DL + LL + CL | 1.5 | 1.5 | — |
| DL + LL + WL/EL | 1.2 | 1.2 | 1.2 |
| DL + WL/EL | 1.5 (0.9) | — | 1.5 |
| DL + ER | 1.2 (0.9) | 1.2 | — |

### Partial Safety Factors (Strength)

| Resistance governed by | Factor |
|------------------------|--------|
| Yielding ($\gamma_{m0}$) | 1.10 |
| Buckling ($\gamma_{m0}$) | 1.10 |
| Ultimate stress ($\gamma_{m1}$) | 1.25 |
| Bolts — friction type ($\gamma_{mf}$) | 1.25 |
| Bolts — bearing type ($\gamma_{mb}$) | 1.25 |
| Rivets ($\gamma_{mr}$) | 1.25 |
| Welds — shop ($\gamma_{mw}$) | 1.25 |
| Welds — field ($\gamma_{mw}$) | 1.50 |

### WHY does steel design use partial safety factors?

Steel design has uncertainties in loading, material strength, structural dimensions (fabrication tolerances), and calculation accuracy. Partial safety factors applied separately to loads ($\gamma_f$) and materials ($\gamma_m$) provide a **consistent level of reliability** across different loading conditions — more rational than a single arbitrary factor of safety.

---

## 3. Bolted Connections

### Types of Bolts

| Type | Use | Notes |
|------|-----|-------|
| Black bolts (unfinished) | Light structures, static loads | Low carbon steel, hole 1.5-2mm larger |
| HSFG bolts | Bridges, seismic, fatigue | High tensile, friction transfer |

**Bolt property class 4.6:** UTS = 400 N/mm², yield = 0.6 × 400 = 240 N/mm².

### Types of Bolted Joints

| Joint | Description | Eccentricity |
|-------|-------------|--------------|
| Lap joint | Members overlapped | Eccentric (couple formed) |
| Butt joint (single cover) | End-to-end, one cover plate | Eccentric |
| Butt joint (double cover) | End-to-end, two cover plates | **No eccentricity** |

**Double cover butt joint** has double the shear capacity of a lap joint (no eccentricity).

### Specifications

| Parameter | Value |
|-----------|-------|
| Bolt hole diameter | d + 1mm (12-14mm), d + 2mm (16-24mm), d + 3mm (≥27mm) |
| Minimum pitch | 2.5d |
| Max pitch (compression) | 12t or 200mm |
| Max pitch (tension) | 16t or 200mm |
| Min edge distance | 1.7 × hole dia (sheared), 1.5 × hole dia (rolled) |

### Failure Modes of Bolted Connections

1. Shearing failure of bolt
2. Bearing failure of bolt
3. Tension failure of bolt
4. Bearing failure of plate
5. Tearing failure of plate
6. Block shear failure

### Design Shear Strength of Bolt

$$V_{dsb} = \frac{f_{ub}}{\sqrt{3} \gamma_{mb}} (n_n A_{nb} + n_s A_{sb})$$

Where $n_n$ = shear planes with threads, $n_s$ = shear planes without threads, $A_{nb} = 0.78 A_{sb}$ (net thread area).

**Reduction factors:**
- Long joints ($> 15d$): $\beta_{lj} = 1.075 - l_j/(200d)$
- Long grip ($> 5d$): $\beta_{lg} = 8d/(3d + l_g)$
- Packing plates ($> 6$mm): $\beta_{pkg} = 1.0 - 0.0125 t_{pkg}$

### Design Bearing Strength of Bolt

$$V_{dpb} = \frac{2.5 k_b d t f_u}{\gamma_{mb}}$$

Where $k_b$ = smaller of ($e/3d_0$, $p/3d_0 - 0.25$, $f_{ub}/f_u$, 1.0).

### Design Tensile Strength of Bolt

$$T_{db} = \frac{0.9 f_{ub} A_{nb}}{\gamma_{mb}} \le \frac{f_{yb} A_{sb}}{\gamma_{m0}}$$

### Design Bolt Value

$V_{db}$ = least of design shear, bearing, and tension strength.

### WHY use HSFG bolts for bridges?

HSFG bolts are pre-tensioned to create high clamping force, transferring load by **friction** rather than bearing. This prevents slippage under **stress reversal** (which occurs in bridges and seismic loading) and is ideal for **fatigue** loading. Black bolts would loosen and slip under repeated reversal.

---

## 4. Welded Connections

### Advantages of Welding

- Direct stress transfer (no gusset/splice plates) → lighter joints
- No holes → better tension member efficiency
- Less fabrication cost
- Air/water tight (oil tanks, ships)
- More rigid, continuous structure
- Less stress concentration

### Disadvantages

- Requires skilled manpower & inspection
- Field welding difficult
- Prone to cracking under fatigue
- Large residual stresses & distortion

### Types of Welds

1. Butt (groove) weld
2. Fillet (lap) weld
3. Slot weld
4. Plug weld

### Butt Weld Design

**Effective throat thickness ($t_e$):**
- Single V/U/bevel (partial penetration): $t_e = 5/8 \times$ thinner member thickness
- Double V/U/bevel (full penetration): $t_e =$ thinner member thickness

**Design axial strength:**
$$T_{dw} = \frac{f_y L_w t_e}{\gamma_{mw}}$$

**Design shear strength:**
$$V_{dw} = \frac{f_{yw} L_w t_e}{\gamma_{mw}}$$

### Fillet Weld Design

**Minimum size of fillet weld:**

| Thickness of thicker part (mm) | Min weld size (mm) |
|-------------------------------|-------------------|
| ≤ 10 | 3 |
| 10-20 | 5 |
| 20-32 | 6 |
| 32-50 | 8 (first run) & 10 |

**Effective throat thickness:** $t_t = K \times s$ (K depends on angle between fusion faces, 0.70 for 60-90°).

**Effective length:** $L_w =$ overall length $- 2s$ (min 4s or 40mm).

**Design strength:**
$$P_{dw} = \frac{L_w t_t f_u}{\sqrt{3} \gamma_{mw}} = \frac{L_w K s f_u}{\sqrt{3} \gamma_{mw}}$$

**Long joint reduction:** If $l_j > 150 t_t$: $\beta_{lw} = 1.2 - 0.2 l_j/(150 t_t) \le 1.0$

### WHY is welding preferred over bolting for tension members?

Welding eliminates bolt holes, so the **full gross section** is available to carry tension (no net section reduction). This improves the strength and efficiency of tension members. Welding also gives a continuous, rigid, airtight joint with less stress concentration.

---

## 5. Eccentric Connections

### Concentric vs Eccentric Load

- **Concentric:** Line of action passes through CG of bolt/weld group.
- **Eccentric:** Line of action does NOT pass through CG → induces additional moment.

### Bracket Type Connection-I (Moment in shear plane)

Eccentric load P replaced by concentric load + twisting moment $M = P \times e$.

**Direct shear per bolt:** $F_a = P/n$

**Force due to moment:** $F_m = \frac{P e r}{\sum r^2}$

**Resultant:** $F_R = \sqrt{F_a^2 + F_m^2 + 2F_a F_m \cos\theta}$

**Critical bolt** = farthest from CG, nearest to load line. Check $F_R \le V_{db}$.

### Bracket Type Connection-II (Moment perpendicular to shear plane)

Bolts subjected to direct shear + tension due to moment.

**Tensile force in bolt:** $T_{bi} = \frac{M y_i}{\sum y^2}$

**Interaction equation:**
$$\left(\frac{V_b}{V_{db}}\right)^2 + \left(\frac{T_b}{T_{db}}\right)^2 \le 1.0$$

### WHY are eccentric connections critical?

Eccentricity creates an additional **moment** that significantly increases the force on the farthest bolts/welds. If not accounted for, the connection can fail even though the direct load is well within capacity. The critical bolt (farthest from CG) governs the design.

---

## 6. Tension Members

### Types of Cross-Sections

- Single/double angles (light roof trusses)
- Channels, I-sections (bridge trusses)
- Circular rods (bracing, tension only)
- Steel wire ropes (suspension/cable-stayed bridges)

### Net Sectional Area

**Chain bolting:** $A_n = (B - nd_0)t$

**Staggered bolting:** $A_n = \left(B - nd_0 + \sum \frac{p^2}{4g}\right)t$

### Types of Failures

1. **Gross section yielding** — whole section yields
2. **Net section rupture** — fracture at holes
3. **Block shear failure** — combined shear + tension failure at connection

### Design Strength

**Gross section yielding:**
$$T_{dg} = \frac{A_g f_y}{\gamma_{m0}}$$

**Net section rupture:**
$$T_{dn} = \frac{0.9 A_n f_u}{\gamma_{m1}}$$

**Angle section (one leg connected):**
$$T_{dn} = \frac{A_{nc} f_u}{\gamma_{m1}} + \frac{\beta A_{go} f_y}{\gamma_{m0}}$$

Where $\beta = 1.4 - 0.076 (w/t)(f_y/f_u)(b_s/L_c)$.

**Block shear (plates):**
$$T_{db1} = \frac{A_{vg} f_y}{\sqrt{3}\gamma_{m0}} + \frac{0.9 A_{tn} f_u}{\gamma_{m1}}$$

### Maximum Slenderness Ratio (Tension)

| Member Type | $l/r$ limit |
|-------------|-------------|
| Stress reversal (non-wind/seismic) | 180 |
| Wind/seismic reversal | 350 |
| Other tension members | 400 |

### WHY do tension members not fail by buckling?

Tension members carry loads by **stretching** — the entire cross-section is in uniform tension, which stabilizes the member. Unlike compression members, there is no tendency to buckle sideways. This makes tension members the **most efficient** structural members (full section utilized).

---

## 7. Compression Members

### Failure Modes

| Column Type | Failure |
|-------------|---------|
| Very short | Yielding/crushing |
| Very long | Elastic buckling (Euler) |
| Intermediate | Inelastic buckling |

### Design Compressive Strength

$$P_d = A_e f_{cd}$$

Where $f_{cd}$ = design compressive stress (accounts for residual stress, initial imperfection, eccentricity).

$$f_{cd} = \frac{\chi f_y}{\gamma_{m0}}$$

Where $\chi$ = stress reduction factor, $\lambda$ = non-dimensional slenderness ratio $= \sqrt{f_y/f_{cc}}$.

### Buckling Classes

| Buckling class | a | b | c | d |
|----------------|---|---|---|---|
| Imperfection factor $\alpha$ | 0.21 | 0.34 | 0.49 | 0.76 |

### Effective Length of Columns

| End Condition | Effective Length |
|---------------|------------------|
| Both ends fixed | 0.65 L |
| One fixed, one pinned | 0.8 L |
| Both pinned | 1.0 L |
| One fixed, one free | 2.0 L |

### Maximum Slenderness Ratio (Compression)

| Member Type | $l/r$ limit |
|-------------|-------------|
| DL + IL loads | 180 |
| Wind/earthquake combination | 250 |
| Compression flange (restrained) | 300 |

### Built-up Columns (Lacing & Battening)

Used when rolled sections don't provide required area/radius of gyration.

**Lacing vs Battening:**

| Aspect | Lacing | Battening |
|--------|--------|-----------|
| Preferred for | Eccentric loads | Axially loaded |
| Effective slenderness increase | 5% | 10% |
| Angle of inclination | 40°-70° | — |
| Transverse shear design | 2.5% of axial load | 2.5% of axial load |

### WHY is lacing preferred for eccentric loads?

Lacing provides better resistance to **transverse shear and bending** caused by eccentric loads, distributing forces more evenly through the diagonal members. Battening, being stiffer and simpler, is preferred for purely axially loaded members where the load path is straight.

---

## 8. Column Bases & Splices

### Column Bases

**Purpose:** Spread column load over a wide area to keep the concrete footing from being overstressed.

**Types:**
- **Slab base** — for axial loads
- **Gusseted base** — for large moments (increases lever arm, minimizes plate thickness)

**Bearing strength of concrete:** $0.45 f_{ck}$

**Base plate thickness:**
$$t_s = \sqrt{\frac{2.5 w (a^2 - 0.3 b^2) \gamma_{m0}}{f_y}} \ge t_f$$

### Column Splices

**Purpose:** Join column lengths when:
- Column length exceeds available section length
- Different sections for different floors

**Design:** Column splices designed as a short column. If ends are machined for full bearing, splice only holds members in position.

### WHY is a base plate needed under a steel column?

The design compressive stress in a concrete footing is much smaller than in a steel column. Without a base plate, the concentrated column load would crush the concrete footing. The base plate **distributes the load** over a sufficiently wide area, keeping the footing within its bearing capacity.

---

## 9. Beams

### Types of Beams

| Beam Type | Function |
|-----------|----------|
| Floor beam | Major beam of floor system |
| Girder | Major beam in a structure |
| Girt | Supports wall cladding |
| Joist | Supports floor construction |
| Lintel | Carries wall loads over openings |
| Purlin | Roof beam supported by trusses |
| Rafter | Roof beam supporting purlins |
| Stringer | Supports stair steps |

### Section Classification

| Class | Behavior |
|-------|----------|
| Plastic | Develops plastic hinge + rotation capacity |
| Compact | Develops plastic moment, inadequate rotation |
| Semi-compact | Extreme fibre reaches yield, no plastic moment |
| Slender | Local buckling before yield |

### Bending Strength (Laterally Supported)

**Low shear ($V < 0.6 V_d$):**
$$M_d = \frac{\beta_b Z_p f_y}{\gamma_{m0}} \le \frac{1.2 Z_e f_y}{\gamma_{m0}}$$

**High shear ($V > 0.6 V_d$):** Reduced moment $M_{dv}$.

### Bending Strength (Laterally Unsupported)

$$M_d = \beta_b Z_p f_{cd}$$

Where $f_{cd}$ = design bending compressive stress accounting for **lateral-torsional buckling (LTB)**.

### Shear Strength

$$V_d = \frac{A_v f_{yw}}{\sqrt{3} \gamma_{m0}}$$

Where $A_v$ = shear area (for I-section major axis: $A_v = h t_w$).

### Deflection Limits

| Member | Limit |
|--------|-------|
| Cantilever (elastic/brittle cladding) | Span/240 |
| Purlins & girts (elastic cladding) | Span/150 |
| Purlins & girts (brittle cladding) | Span/180 |

### Web Crippling & Buckling

- **Web crippling:** Local buckling of web under concentrated loads (dispersion angle 1:2.5).
- **Web buckling:** Web acts as a column under concentrated loads (45° dispersion).
- **Remedy:** Bearing stiffeners or thicker webs.

### WHY do laterally unsupported beams fail by lateral-torsional buckling?

When a beam's compression flange is not laterally restrained, the compression flange tends to **buckle sideways** (laterally) while the tension flange stays straight, causing the beam to **twist** (torsion). This lateral-torsional buckling occurs before the beam reaches its full bending strength, so it must be checked for unsupported beams.

---

## 10. Plate Girders

### Purpose

Fabricated girders for **heavy loads over long spans** where rolled sections are inadequate.

### Elements

- Web plate
- Flange angles with/without flange plates
- Stiffeners (transverse, longitudinal, load/end bearing)
- Splices (flange, web)

### Economical Depth

$$d = \left(\frac{M k}{f_y}\right)^{1/3}$$

### Minimum Web Thickness

- Without stiffeners: $d/t_w \le 200\varepsilon$ (both edges connected)
- With transverse stiffeners: $d/t_w \le 200\varepsilon_w$
- With longitudinal stiffener: $d/t_w \le 250\varepsilon_w$

Where $\varepsilon = \sqrt{250/f_y}$.

### Stiffeners

| Type | Function |
|------|----------|
| Transverse (vertical) | Increases web buckling resistance against shear |
| Longitudinal (horizontal) | Increases web buckling resistance against bending |
| Load/end bearing | Prevents web crippling under concentrated loads |

### WHY are stiffeners needed in plate girders?

Plate girder webs are thin (to save weight), making them prone to **buckling** under shear (transverse stiffeners) and bending (longitudinal stiffeners). Stiffeners subdivide the web into smaller panels, increasing its buckling resistance without adding much weight. Bearing stiffeners prevent local crippling under concentrated loads.

---

## 11. Gantry Girders & Roof Trusses

### Gantry Girders

Laterally unsupported beams carrying cranes in industrial buildings.

**Loads:** Vertical, lateral (crab stopping/starting), longitudinal (crane stopping/starting).

**Impact loads:**
- Electric overhead cranes: 25% of max static wheel load (vertical)
- Hand operated cranes: 10% of max static wheel load (vertical)
- Lateral (electric): 10% of crab + lifted weight
- Longitudinal: 5% of static wheel loads

**Deflection limits:**
- Manually operated: L/500
- Electric ≤ 500 kN: L/750
- Electric > 500 kN: L/1000

### Roof Trusses

- Single angles for web members
- Double angles for rafter/tie members
- Built-up members for heavy bridge trusses

### WHY is the compression flange of a gantry girder reinforced with a channel?

Gantry girders are laterally unsupported and carry heavy crane loads. The channel reinforces the compression flange, increasing **lateral stability and torsional rigidity** against the lateral thrust from crane movement. For very heavy lateral forces, a box-type girder provides even greater torsional resistance.

---

## 12. IS 800:2007 Code Provisions Summary

| Parameter | Value |
|-----------|-------|
| Design method | Limit state method |
| $\gamma_{m0}$ (yield/buckling) | 1.10 |
| $\gamma_{m1}$ (ultimate) | 1.25 |
| $\gamma_{mw}$ (shop weld) | 1.25 |
| $\gamma_{mw}$ (field weld) | 1.50 |
| E (modulus) | $2 \times 10^5$ N/mm² |
| Min pitch of bolts | 2.5d |
| Max slenderness (compression, DL+IL) | 180 |
| Max slenderness (tension) | 400 |
| Web crippling dispersion | 1:2.5 |
| Lacing inclination | 40°-70° |
| Lacing transverse shear | 2.5% of axial load |
| Battened column slenderness increase | 10% |
| Laced column slenderness increase | 5% |

---

## 13. Worked Numerical Examples

### Example 1: Tension Member Design

**Problem:** Design a tension member for $T = 300$ kN. $f_y = 250$ MPa, $f_u = 410$ MPa.

**Solution:**
1. Gross yielding: $A_g \ge \frac{T \gamma_{m0}}{f_y} = \frac{300 \times 10^3 \times 1.10}{250} = 1320$ mm²
2. Net rupture: $A_n \ge \frac{T \gamma_{m1}}{0.9 f_u} = \frac{300 \times 10^3 \times 1.25}{0.9 \times 410} = 1016$ mm²
3. Increase net area by 25-40% for gross: $A_g \approx 1.3 \times 1016 = 1321$ mm²
4. Select ISA 90 × 90 × 8 ($A_g = 1380$ mm²)
5. Check slenderness: $l/r \le 400$

**Interview follow-up:** Which governs — yielding or rupture? → The larger required area governs (here yielding).

### Example 2: Bolted Connection

**Problem:** Find design shear strength of a 20mm bolt (property class 4.6) in single shear. Threads intercept shear plane. $f_{ub} = 400$ MPa.

**Solution:**
1. $A_{nb} = 0.78 \times \pi \times 20^2/4 = 0.78 \times 314 = 245$ mm²
2. $V_{dsb} = \frac{f_{ub}}{\sqrt{3} \gamma_{mb}} n_n A_{nb} = \frac{400}{\sqrt{3} \times 1.25} \times 1 \times 245$
3. $V_{dsb} = \frac{400 \times 245}{2.165} = 45,266$ N = 45.3 kN

**Interview follow-up:** What if threads don't intercept shear plane? → Use $A_{sb} = 314$ mm² (full shank area), higher capacity.

### Example 3: Fillet Weld

**Problem:** Find design strength of a 6mm fillet weld, 200mm long. $f_u = 410$ MPa, shop weld.

**Solution:**
1. $t_t = K \times s = 0.7 \times 6 = 4.2$ mm
2. $L_w = 200 - 2 \times 6 = 188$ mm
3. $P_{dw} = \frac{L_w t_t f_u}{\sqrt{3} \gamma_{mw}} = \frac{188 \times 4.2 \times 410}{\sqrt{3} \times 1.25}$
4. $P_{dw} = \frac{323,736}{2.165} = 149,530$ N = 149.5 kN

**Interview follow-up:** Why is effective length less than overall length? → The ends of fillet welds have stress concentration and don't carry full load, so 2s is deducted.

### Example 4: Compression Member

**Problem:** Check a column with $P_d = 500$ kN, $A_e = 5000$ mm², $f_{cd} = 120$ N/mm².

**Solution:**
1. $P_d = A_e f_{cd} = 5000 \times 120 = 600,000$ N = 600 kN
2. Since 600 kN > 500 kN ✓ (safe)
3. Check slenderness: $KL/r \le 180$

**Interview follow-up:** What does $f_{cd}$ account for? → Residual stresses, initial imperfection, and load eccentricity.

---

## 14. 🎤 Interview Q&A

### A. Basic Concept Questions

1. **What is the difference between limit state and working stress method in steel?**
   - LSM: partial safety factors on loads & materials, checks strength + serviceability. WSM: single FOS, elastic.

2. **What are the types of bolted connections?**
   - Bearing type (force by bearing) and friction type/HSFG (force by friction).

3. **What is the difference between lap and butt joints?**
   - Lap: overlapped, eccentric. Butt: end-to-end with cover plates, double cover has no eccentricity.

4. **What are the failure modes of bolted connections?**
   - Shear, bearing, tension of bolt; bearing, tearing of plate; block shear.

5. **What is lateral-torsional buckling?**
   - Lateral buckling of compression flange + twisting of beam in unsupported beams.

### B. WHY Questions

1. **Why use HSFG bolts for bridges?**
   - Friction transfer prevents slippage under stress reversal; ideal for seismic/fatigue.

2. **Why do tension members not buckle?**
   - Uniform tension stabilizes the member; no tendency to buckle sideways.

3. **Why is welding preferred for tension members?**
   - No holes → full gross section available → higher efficiency.

4. **Why are stiffeners needed in plate girders?**
   - Thin webs prone to buckling; stiffeners subdivide web into smaller panels.

5. **Why is a base plate needed under steel columns?**
   - Distributes concentrated column load over wide area to prevent concrete crushing.

### C. WHAT-IF Questions

1. **What if threads intercept the shear plane of a bolt?**
   - Use net area $A_{nb} = 0.78 A_{sb}$, lower shear capacity.

2. **What if a joint is long (> 15d)?**
   - Apply long joint reduction factor $\beta_{lj}$.

3. **What if a beam is laterally unsupported?**
   - Check lateral-torsional buckling, use reduced bending strength $M_d = \beta_b Z_p f_{cd}$.

4. **What if web is susceptible to shear buckling ($d/t_w > 67\varepsilon$)?**
   - Check high shear case, provide stiffeners.

5. **What if a column is very long?**
   - Fails by elastic buckling (Euler mode), governed by slenderness ratio.

### D. Comparison Questions

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

### E. Numerical Questions

1. Find $V_{dsb}$ for 20mm bolt, single shear, threads intercept. → ≈ 45.3 kN
2. Find $P_{dw}$ for 6mm fillet weld, 200mm. → ≈ 149.5 kN
3. Find $A_g$ required for $T = 300$ kN. → ≈ 1320 mm²
4. Find $P_d = A_e f_{cd}$. → Product of effective area & design stress

### F. Rapid-Fire Questions

1. $\gamma_{m0}$ for steel? → 1.10
2. $\gamma_{m1}$ for steel? → 1.25
3. $\gamma_{mw}$ shop weld? → 1.25
4. $\gamma_{mw}$ field weld? → 1.50
5. E for steel? → $2 \times 10^5$ N/mm²
6. Min pitch of bolts? → 2.5d
7. Max slenderness (compression)? → 180
8. Max slenderness (tension)? → 400
9. Lacing inclination? → 40°-70°
10. Lacing transverse shear? → 2.5% of axial load
11. Web crippling dispersion? → 1:2.5
12. HSFG bolt property class? → 10.9S, 12.9S
13. Fillet weld throat factor K (60-90°)? → 0.70
14. Min fillet weld size? → 3mm
15. Deflection limit (cantilever)? → Span/240
16. Gantry girder (electric ≤500kN)? → L/750
17. Bearing strength of concrete? → 0.45 fck
18. Bolt hole for 20mm bolt? → 22mm
19. Steel grade E250 yield? → 250 MPa
20. Poisson's ratio for steel? → 0.30

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the design compressive stress $f_{cd}$ formulation.**
   - $f_{cd} = \chi f_y/\gamma_{m0}$ where $\chi = 1/[\phi + \sqrt{\phi^2 - \lambda^2}]$, $\phi = 0.5[1 + \alpha(\lambda - 0.2) + \lambda^2]$, $\lambda = \sqrt{f_y/f_{cc}}$. Accounts for residual stress, imperfection, eccentricity.

2. **Explain the block shear failure mechanism.**
   - At the connection, a block of material tears out along a path combining shear (along bolt lines) and tension (across the end). Governed by the weaker of shear-yield/tension-fracture or shear-fracture/tension-yield.

3. **What is the truss analogy in steel connections?**
   - Similar to RCC shear: the connection acts as a truss with bolts/welds as tension members and plate as compression struts.

4. **Explain lateral-torsional buckling and the elastic critical moment.**
   - $M_{cr}$ is the moment at which a beam fails by lateral buckling under uniform moment. It depends on $EI_y$ (lateral bending), $GJ$ (torsion), and $EI_w$ (warping).

5. **What is the Hoyer effect analogy in steel?**
   - (Note: Hoyer effect is prestressed concrete; in steel, the analogous concept is the transmission of force through friction in HSFG bolts.)

---

## 15. High-Value Interview Answers

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

## 16. Software Connection

| Tool | Application |
|------|-------------|
| STAAD.Pro | Steel member design & analysis |
| Tekla Structures | Steel detailing & fabrication |
| IDEA StatiCa | Connection design & verification |
| ETABS | Building steel design |
| SAP2000 | General steel analysis |
| RISA-3D | 3D steel analysis |
| AutoCAD | Detailing drawings |

**Hand-calc verification:** Always verify connection design (bolts, welds) with hand calculations — software connection modules can be conservative or miss critical checks.

---

## 17. 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Steel properties         →  Limit state design          →  Buckling curves            →  IS 800 provisions
Bolted connections       →  Bearing/friction bolts      →  Eccentric connections      →  Bolt value calculation
Welded connections       →  Fillet/butt weld design     →  Long joint reduction       →  Weld strength
Tension members          →  Net area & design strength  →  Block shear                →  Yielding vs rupture
Compression members      →  Buckling & slenderness      →  Lacing/battening           →  Buckling classes
Beams                    →  Bending & shear strength    →  Lateral-torsional buckling →  Section classification
Plate girders            →  Web & flange design         →  Stiffeners                 →  Economical depth
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `STRUCTURAL` `STEEL` `IS 800`

---

## 18. 🔗 Cross-Links

- [`structures.md`](../structures/structures.md) — Structural analysis & RCC design companion
- [`rcc-design.md`](../rcc/rcc-design.md) — Reinforced concrete design
- [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — Stress, bending, buckling fundamentals
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Foundation & column bases
- [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) — Construction management

---

## 19. 📋 Quick Revision Checklist

- [ ] Steel grades: E250, E350, E410, E450, E550
- [ ] E = $2 \times 10^5$ N/mm², G = $0.769 \times 10^5$ N/mm²
- [ ] $\gamma_{m0}$ = 1.10, $\gamma_{m1}$ = 1.25
- [ ] $\gamma_{mw}$: shop 1.25, field 1.50
- [ ] Bolt hole: d + 1/2/3mm
- [ ] Min pitch: 2.5d
- [ ] $V_{dsb} = f_{ub}(n_n A_{nb} + n_s A_{sb})/(\sqrt{3}\gamma_{mb})$
- [ ] $V_{dpb} = 2.5 k_b d t f_u/\gamma_{mb}$
- [ ] Fillet weld: $t_t = K \times s$, $P_{dw} = L_w t_t f_u/(\sqrt{3}\gamma_{mw})$
- [ ] $T_{dg} = A_g f_y/\gamma_{m0}$ (gross yielding)
- [ ] $T_{dn} = 0.9 A_n f_u/\gamma_{m1}$ (net rupture)
- [ ] $P_d = A_e f_{cd}$ (compression)
- [ ] Max slenderness: compression 180, tension 400
- [ ] Lacing: 40°-70°, 2.5% transverse shear
- [ ] Battened column: +10% slenderness
- [ ] Web crippling dispersion: 1:2.5
- [ ] Deflection: cantilever span/240, purlin span/150
- [ ] Gantry girder: L/500 to L/1000
- [ ] Bearing strength concrete: 0.45 fck
- [ ] Section classes: plastic, compact, semi-compact, slender

---

## References

* IS 800:2007 — General Construction in Steel — Code of Practice
* IS 226 — Standard Quality Structural Steel
* IS 2062 — Fusion Welding Quality Steel
* IS 816 — Code of Practice for Welding
* [`structures.md`](../structures/structures.md) — Structural design companion
* [`rcc-design.md`](../rcc/rcc-design.md) — RCC design companion
* [`strength-of-materials.md`](../fundamentals/strength-of-materials.md) — SOM fundamentals

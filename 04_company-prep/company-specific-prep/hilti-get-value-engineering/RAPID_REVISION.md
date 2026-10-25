# Rapid Revision Handbook & Master Formula Matrix — Hilti GET

> **Purpose:** Ultra-concentrated mathematical and conceptual calibration for exam eve and the final 15 minutes before technical testing and interviews.

---

## 1. Master Formula Matrix

### A. Strength of Materials & Beam Deflections
* **Flexure Formula:**
  $$\frac{M}{I} = \frac{\sigma}{y} = \frac{E}{R} \implies \sigma_{\max} = \frac{M}{Z}$$
  - Solid rectangular section ($b \times d$): $Z = \frac{b d^2}{6}$, $I = \frac{b d^3}{12}$
  - Elastic core modulus: $Z_e = \frac{b d^2}{6}$, Plastic section modulus: $Z_p = \frac{b d^2}{4}$, Shape factor $S = 1.50$
* **Standard Cantilever Deflections (Length $L$, Rigidity $EI$):**
  - Point load $P$ at free tip: $\delta_{\max} = \frac{P L^3}{3 E I}, \quad \theta = \frac{P L^2}{2 E I}$
  - Uniform distributed load $w$ over entire length: $\delta_{\max} = \frac{w L^4}{8 E I}, \quad \theta = \frac{w L^3}{6 E I}$
* **Standard Simply Supported Deflections (Span $L$):**
  - Central point load $P$: $\delta_{\max} = \frac{P L^3}{48 E I}$
  - Uniform distributed load $w$: $\delta_{\max} = \frac{5 w L^4}{384 E I}$
* **Euler Column Buckling:**
  $$P_{cr} = \frac{\pi^2 E I}{(K L)^2}$$
  - Both ends pinned: $K = 1.0$
  - Both ends fixed: $K = 0.5$
  - One fixed, one pinned: $K = 0.7$
  - One fixed, one free (cantilever): $K = 2.0$

---

### B. Steel & Connection Design (IS 800 / AISC 360)
* **Fillet Weld Design Strength:**
  $$t_e = 0.707 s \quad (90^\circ \text{ fusion faces})$$
  $$f_{wd} = \frac{f_u}{\sqrt{3} \gamma_{mw}} \implies P_{dw} = t_e \cdot L_w \cdot \frac{f_u}{\sqrt{3} \gamma_{mw}}$$
* **Bolt Single Shear Capacity (Grade 4.6, Tensile stress area $A_{nb}$):**
  $$V_{dsb} = \frac{f_u A_{nb}}{\sqrt{3} \gamma_{mb}}$$
* **Base Plate Cantilever Thickness (AISC Design Guide 1):**
  $$t_{p} = l \sqrt{\frac{2 f_p}{F_y}} = l \sqrt{\frac{2 q_{\max}}{0.9 F_y}}$$
  where $l = \max(m, n)$, $m = \frac{B - 0.8 b_f}{2}$, $n = \frac{N - 0.95 d}{2}$, and $q_{\max} = \frac{P}{B \cdot N}$.

---

### C. Post-Installed Anchor Mechanics & CCD Method (ACI 318 Ch 17 / EN 1992-4)
* **Basic Concrete Cone Breakout Strength (Single Anchor in Tension, Uncracked Concrete):**
  $$N_{b} = k_c \lambda_a \sqrt{f_c'} \, h_{ef}^{1.5}$$
  - For cast-in-place anchors: $k_c = 10.0$ (SI units, $f_c'$ in MPa, $h_{ef}$ in mm, $N_b$ in N)
  - For post-installed anchors: $k_c = 7.0$ (uncracked concrete) to $k_c = 10.0$ (with specialized certification)
  - For cracked concrete: $k_c = 7.0$
* **Projected Failure Surface Area for Single Anchor ($A_{Nc0}$):**
  $$A_{Nc0} = 9 h_{ef}^2 \quad (3 h_{ef} \times 3 h_{ef} \text{ square base})$$
  Critical edge distance: $c_{cr,N} = 1.5 h_{ef}$. Critical spacing: $s_{cr,N} = 3.0 h_{ef}$.
* **Nominal Concrete Breakout Strength of Anchor Group ($N_{cbg}$):**
  $$N_{cbg} = \frac{A_{Nc}}{A_{Nc0}} \cdot \psi_{ec,N} \cdot \psi_{ed,N} \cdot \psi_{c,N} \cdot \psi_{cp,N} \cdot N_b$$
  where $\psi_{ed,N}$ is the edge modification factor: $\psi_{ed,N} = 0.7 + 0.3 \frac{c_{a,\min}}{1.5 h_{ef}} \le 1.0$.
* **Pullout Strength in Tension (Mechanical Expansion Anchor):**
  $$N_p = A_{brg} \cdot 8 f_c'$$
* **Bond Strength of Adhesive / Chemical Anchor:**
  $$N_{ba} = \lambda_a \cdot \tau_{cr} \cdot \pi \cdot d_a \cdot h_{ef}$$
  where $\tau_{cr}$ is characteristic bond stress (typically $8–18\text{ MPa}$ depending on resin system).
* **Concrete Edge Breakout in Shear ($V_b$, loaded toward edge $c_{a1}$):**
  $$V_b = 7 \left(\frac{l_e}{d_a}\right)^{0.2} \sqrt{d_a} \, \lambda_a \sqrt{f_c'} \, c_{a1}^{1.5}$$
* **Concrete Pryout Strength in Shear ($V_{cp}$):**
  $$V_{cp} = k_{cp} \cdot N_{cb}$$
  where $k_{cp} = 1.0$ for $h_{ef} < 65\text{ mm}$, and $k_{cp} = 2.0$ for $h_{ef} \ge 65\text{ mm}$.
* **Combined Tension & Shear Interaction (Elliptical):**
  $$\left(\frac{N_{ua}}{\phi N_n}\right)^{5/3} + \left(\frac{V_{ua}}{\phi V_n}\right)^{5/3} \le 1.0 \quad \text{or trilinear interaction: } \frac{N_{ua}}{\phi N_n} + \frac{V_{ua}}{\phi V_n} \le 1.20$$

---

## 2. High-Frequency Exam & Calculation Traps

```text
+-----------------------------------------------------------------------------------------------+
|                                    CRITICAL UNIT & DESIGN TRAPS                               |
+-----------------------------------------------------------------------------------------------+
| 1. The MPa to N/mm² Equivalence:                                                              |
|    • 1 MPa = 1 N/mm² = 10^6 N/m² = 10^3 kN/m².                                                |
|    • Always convert spans to millimeters (mm) and forces to Newtons (N) before calculating   |
|      stresses in MPa! (e.g., L = 4.0 m = 4000 mm, M = 20 kN·m = 20 × 10^6 N·mm).            |
|                                                                                               |
| 2. Anchor Embedment vs Total Length Trap:                                                      |
|    • h_ef is EFFECTIVE embedment depth (concrete surface to center of expansion sleeve or     |
|      bottom of bonded rod). Total anchor length L_total = h_ef + plate thickness t + nut/wash.|
|    • Concrete cone breakout depends SOLELY on h_ef, NOT total length!                         |
|                                                                                               |
| 3. Cracked vs Uncracked Concrete Trap:                                                        |
|    • Concrete is assumed CRACKED under tensile stresses (flexure in slabs, tension zones).    |
|    • Uncracked assumption requires demonstrating that tensile stress under service loads      |
|      satisfies σ_t < f_r = 0.7√f_ck. Using uncracked values blindly is a safety failure!       |
|                                                                                               |
| 4. Borehole Cleaning Trap in Chemical Anchors:                                                |
|    • Failure to clean drilled holes (dust/debris left on borehole wall) reduces adhesive bond  |
|      strength by up to 60%! Hilti SafeSet (hollow drill bit + vacuum) restores full bond.     |
|                                                                                               |
| 5. Value Engineering vs Cheapening Trap:                                                      |
|    • VE optimizes installation time, handling, and material efficiency while strictly          |
|      maintaining or exceeding required code safety factors (SF ≥ 1.5). Reducing anchor         |
|      embedment below code capacity is negligence, not value engineering!                      |
+-----------------------------------------------------------------------------------------------+
```

---

## 3. 5-Minute Pre-Test Mental Checklist

Review these 10 rapid principles right before clicking start or entering your interview:
1. **Load Path Continuity:** Follow the load from pipe/equipment $\to$ bracket/channel $\to$ base plate $\to$ anchors $\to$ concrete foundation. Every link must carry the load.
2. **Breakout Cone Geometry:** Single anchor failure cone radiates outward at $\approx 35^\circ$, projecting a square base of $3 h_{ef} \times 3 h_{ef}$ and area $A_{Nc0} = 9 h_{ef}^2$.
3. **Edge Distance Penalty:** If edge distance $c < 1.5 h_{ef}$, the breakout cone is clipped, drastically reducing concrete tension capacity.
4. **Pryout Controls Short Anchors:** Short, stiff anchors loaded in shear do NOT fail by concrete edge breakout; they pry backward and pop a concrete cone ($V_{cp} = 2 N_{cb}$).
5. **Fillet Weld Throat:** Always multiply leg size $s$ by $0.707$ to get throat $t_e$ before calculating weld shear capacity.
6. **Bending Capacity Limit:** Balanced moment capacity for singly reinforced beams in M20/Fe415 is $M_{u,\lim} = 0.138 f_{ck} b d^2$.
7. **Modular Channel Advantages:** Eliminates hot work permits, eliminates site welding inspections, reduces weight by 40%, and allows 3D adjustability on site.
8. **Ductility First:** Anchor steel failure ($N_{sa}$) is ductile; concrete breakout ($N_{cb}$) is brittle. Seismic codes demand designing connections so ductile steel yields before brittle concrete breaks.
9. **Combined Interaction:** Never check tension and shear independently; always evaluate the elliptical interaction $(\frac{N}{\phi N_n})^{5/3} + (\frac{V}{\phi V_n})^{5/3} \le 1.0$.
10. **Ethical Line in Value Engineering:** If a contractor requests substituting approved chemical anchors with uncertified hardware to save money, explain the life-safety liability and refuse the substitution.

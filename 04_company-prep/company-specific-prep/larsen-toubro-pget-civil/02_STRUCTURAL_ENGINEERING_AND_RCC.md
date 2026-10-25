# Module 02: Structural Engineering, RCC & Steel Design

`[CORE TECHNICAL SYLLABUS — L&T CONSTRUCTION & ENGINEERING DESIGN CENTERS]`
`[KEY INDIAN CODES: IS 456:2000, IS 800:2007, IS 1893:2016, IS 13920:2016]`
`[PRACTICE SUITE: 30 IN-DEPTH SOLVED PROBLEMS WITH COMPLETE MATHEMATICAL DERIVATIONS]`

---

## 1. Executive Summary & Syllabus Overview

Structural engineering forms the technical backbone of L&T's infrastructure projects. In both the Online Assessment (OA) and technical panel interviews, candidates are tested on:
1. **Reinforced Concrete Design (IS 456:2000):** Working stress vs limit state philosophy, rectangular & flanged beam flexure, shear stirrup design, torsional reinforcement, compression members under uniaxial/biaxial bending, footing design, and serviceability (crack width & deflection control).
2. **Ductile Detailing (IS 13920:2016) & Seismic Analysis (IS 1893:2016):** Special confining reinforcement in columns, seismic zones (II to V), response reduction factor ($R$), importance factor ($I$), and base shear calculations.
3. **Structural Steel Design (IS 800:2007):** Limit state design of tension and compression members, column buckling curves (a, b, c, d), HSFG slip-critical bolted connections, fillet and butt welds, prying action, and slab base / gusseted base design.
4. **Prestressed Concrete:** Pre-tensioning vs post-tensioning, loss of prestress (elastic shortening, creep, shrinkage, relaxation, friction, and anchorage slip), and stress analysis under transfer and working loads.

---

## 2. 30 Fully Solved Structural Engineering Problems

### Problem 2.01: Singly Reinforced Beam Neutral Axis & Moment Capacity
**Question:** A singly reinforced rectangular concrete beam has width $b = 300\text{ mm}$ and effective depth $d = 500\text{ mm}$. It is reinforced with 4 bars of $20\text{ mm}$ diameter Fe 415 steel. Concrete grade is M25. Determine: (a) Depth of the neutral axis $x_u$, (b) Section classification (under-reinforced or over-reinforced), and (c) Ultimate moment of resistance $M_u$.  
**Solution:**
1. Steel area: $A_{st} = 4 \times \frac{\pi}{4} (20)^2 = 4 \times 314.16 = 1256.64\text{ mm}^2$.
2. Limiting neutral axis depth for Fe 415:
   $$x_{u,max} = 0.48 d = 0.48 \times 500 = 240.0\text{ mm}$$
3. Actual neutral axis depth:
   $$0.36 f_{ck} b x_u = 0.87 f_y A_{st}$$
   $$x_u = \frac{0.87 \times 415 \times 1256.64}{0.36 \times 25 \times 300} = \frac{453,710.2}{2,700} = 168.04\text{ mm}$$
4. Classification: Since $x_u (168.04\text{ mm}) < x_{u,max} (240.0\text{ mm})$, the section is **under-reinforced** (ductile tensile failure mode).
5. Moment of resistance:
   $$M_u = 0.87 f_y A_{st} d \left(1 - \frac{A_{st} f_y}{b d f_{ck}}\right)$$
   $$M_u = 453,710.2 \times 500 \times \left(1 - \frac{1256.64 \times 415}{300 \times 500 \times 25}\right) = 2.2685 \times 10^8 \times (1 - 0.1390) = \mathbf{195.32\text{ kN}\cdot\text{m}}$$

### Problem 2.02: Doubly Reinforced Beam Capacity
**Question:** A beam $b = 250\text{ mm}, d = 450\text{ mm}$ has tension steel $A_{st} = 2000\text{ mm}^2$ and compression steel $A_{sc} = 500\text{ mm}^2$ with effective cover $d' = 45\text{ mm}$. Concrete is M20, steel is Fe 415 ($f_{sc} = 353\text{ N/mm}^2$). Find the ultimate moment capacity $M_u$.  
**Solution:**
1. Limiting capacity of balanced singly reinforced section:
   $$M_{u,lim} = 0.138 f_{ck} b d^2 = 0.138 \times 20 \times 250 \times 450^2 = 139.725\text{ kN}\cdot\text{m}$$
   $$A_{st1} = \frac{0.36 f_{ck} b x_{u,max}}{0.87 f_y} = \frac{0.36 \times 20 \times 250 \times (0.48 \times 450)}{0.87 \times 415} = 1076.87\text{ mm}^2$$
2. Additional capacity from compression steel:
   $$A_{st2} = \frac{(f_{sc} - 0.446 f_{ck}) A_{sc}}{0.87 f_y} = \frac{(353 - 8.92) \times 500}{0.87 \times 415} = \frac{172,040}{361.05} = 476.5\text{ mm}^2$$
   Total $A_{st,prov} = 2000\text{ mm}^2 > A_{st1} + A_{st2} = 1553.4\text{ mm}^2$.
3. Additional moment capacity:
   $$M_{u2} = f_{sc} A_{sc} (d - d') = 353 \times 500 \times (450 - 45) = 176,500 \times 405 = 71.48\text{ kN}\cdot\text{m}$$
4. Total ultimate moment capacity:
   $$M_u = M_{u,lim} + M_{u2} = 139.73 + 71.48 = \mathbf{211.21\text{ kN}\cdot\text{m}}$$

### Problem 2.03: Shear Reinforcement Sizing
**Question:** An RC beam ($b = 300\text{ mm}, d = 600\text{ mm}$) carries a factored shear force $V_u = 240\text{ kN}$. Concrete grade is M25. The design shear strength of concrete is $\tau_c = 0.65\text{ N/mm}^2$. Design 2-legged $8\text{ mm}$ diameter vertical stirrups (Fe 415).  
**Solution:**
1. Nominal shear stress: $\tau_v = \frac{V_u}{b d} = \frac{240,000}{300 \times 600} = 1.333\text{ N/mm}^2$.
2. Maximum permissible shear stress (Table 20): $\tau_{c,max} = 0.62 \sqrt{25} = 3.1\text{ N/mm}^2$.
   Since $\tau_c (0.65) < \tau_v (1.333) < \tau_{c,max} (3.1)$, shear reinforcement is required.
3. Concrete shear capacity:
   $$V_{uc} = \tau_c b d = 0.65 \times 300 \times 600 = 117,000\text{ N} = 117.0\text{ kN}$$
4. Shear to be resisted by stirrups:
   $$V_{us} = V_u - V_{uc} = 240 - 117 = 123.0\text{ kN}$$
5. Area of 2-legged $8\text{ mm}$ stirrup: $A_{sv} = 2 \times \frac{\pi}{4} (8)^2 = 100.53\text{ mm}^2$.
6. Required spacing:
   $$s_v = \frac{0.87 f_y A_{sv} d}{V_{us}} = \frac{0.87 \times 415 \times 100.53 \times 600}{123,000} = \frac{21,778,284}{123,000} = 177.06\text{ mm}$$
7. Maximum spacing limits per IS 456 Cl. 26.5.1.5:
   - $0.75 d = 0.75 \times 600 = 450\text{ mm}$
   - $300\text{ mm}$
   - Minimum shear reinforcement: $s_{v,max} = \frac{0.87 f_y A_{sv}}{0.4 b} = \frac{0.87 \times 415 \times 100.53}{0.4 \times 300} = 302.4\text{ mm}$.
8. **Provide 2-legged 8mm stirrups at 170 mm c/c spacing.**

### Problem 2.04: Combined Torsion, Bending and Shear
**Question:** A rectangular beam ($300 \times 600\text{ mm}$) is subjected to factored bending moment $M_u = 120\text{ kN}\cdot\text{m}$, factored shear force $V_u = 80\text{ kN}$, and factored torsional moment $T_u = 40\text{ kN}\cdot\text{m}$. Find: (a) Equivalent shear force $V_e$, and (b) Equivalent bending moment $M_{e1}$.  
**Solution:**
1. Equivalent Shear Force (IS 456 Cl. 41.3.1):
   $$V_e = V_u + 1.6 \frac{T_u}{b} = 80 + 1.6 \times \frac{40}{0.30} = 80 + 213.33 = \mathbf{293.33\text{ kN}}$$
2. Equivalent Bending Moment (IS 456 Cl. 41.4.2):
   $$M_t = \frac{T_u}{1.7} \left(1 + \frac{D}{b}\right) = \frac{40}{1.7} \left(1 + \frac{600}{300}\right) = 23.53 \times 3.0 = 70.59\text{ kN}\cdot\text{m}$$
   $$M_{e1} = M_u + M_t = 120 + 70.59 = \mathbf{190.59\text{ kN}\cdot\text{m}}$$

### Problem 2.05: Short Axially Loaded Column Sizing
**Question:** Design a short square reinforced concrete column to carry an ultimate factored axial compressive load $P_u = 2400\text{ kN}$. Concrete grade is M30, steel grade is Fe 500. Steel percentage is $1.5\%$ of gross area.  
**Solution:**
1. $P_u = 0.40 f_{ck} A_c + 0.67 f_y A_{sc}$
2. With $A_{sc} = 0.015 A_g$ and $A_c = 0.985 A_g$:
   $$2,400,000 = [0.40 \times 30 \times 0.985 + 0.67 \times 500 \times 0.015] A_g$$
   $$2,400,000 = [11.82 + 5.025] A_g = 16.845 A_g$$
3. Required gross area: $A_g = \frac{2,400,000}{16.845} = 142,475.5\text{ mm}^2$.
4. Column side: $B = \sqrt{142,475.5} = 377.46\text{ mm} \implies$ Adopt **$400 \times 400\text{ mm}$**.
5. Revised $A_g = 160,000\text{ mm}^2$.
6. Required steel area: $A_{sc} = 0.015 \times 160,000 = 2400\text{ mm}^2$.
7. Provide **8 bars of 20mm diameter** ($A_{sc} = 8 \times 314 = 2512\text{ mm}^2$).

### Problem 2.06: Development Length in Tension vs Compression
**Question:** Compute the development length $L_d$ for a $25\text{ mm}$ Fe 500 deformed bar in M30 concrete when loaded in: (a) Tension, and (b) Direct compression.  
**Solution:**
1. Basic design bond stress for M30 plain bars: $\tau_{bd} = 1.50\text{ N/mm}^2$.
2. For deformed (HYSD) bars, increase by $60\%$: $\tau_{bd} = 1.50 \times 1.60 = 2.40\text{ N/mm}^2$.
3. (a) In Tension:
   $$L_d = \frac{\phi \cdot 0.87 f_y}{4 \tau_{bd}} = \frac{25 \times (0.87 \times 500)}{4 \times 2.40} = \frac{10,875}{9.60} = \mathbf{1132.8\text{ mm}} \approx 1135\text{ mm}$$
4. (b) In Compression (IS 456 Cl. 26.2.1.1: increase $\tau_{bd}$ by another $25\%$):
   $$\tau_{bd,comp} = 2.40 \times 1.25 = 3.00\text{ N/mm}^2$$
   $$L_{d,comp} = \frac{25 \times 435}{4 \times 3.00} = \frac{10,875}{12.00} = \mathbf{906.25\text{ mm}} \approx 910\text{ mm}$$

### Problem 2.07: Steel Tension Member Block Shear Capacity
**Question:** A single angle ISA $100 \times 75 \times 8\text{ mm}$ ($f_y = 250\text{ MPa}, f_u = 410\text{ MPa}$) is connected to a $10\text{ mm}$ gusset plate by a line of four $20\text{ mm}$ bolts at pitch $p = 60\text{ mm}$ and edge distance $e = 40\text{ mm}$. Hole diameter $d_0 = 22\text{ mm}$. What is the design block shear capacity $T_{db}$?  
**Solution:**
1. Shear line length: $L_v = 3 \times 60 + 40 = 220\text{ mm}$. Gross shear area $A_{vg} = 220 \times 8 = 1760\text{ mm}^2$.
2. Net shear area: Deduct $3.5$ hole diameters: $A_{vn} = [220 - 3.5(22)] \times 8 = [220 - 77] \times 8 = 143 \times 8 = 1144\text{ mm}^2$.
3. Tension line width: $w_t = 35\text{ mm}$. Gross tension area $A_{tg} = 35 \times 8 = 280\text{ mm}^2$.
4. Net tension area: Deduct $0.5$ hole diameter: $A_{tn} = [35 - 0.5(22)] \times 8 = [35 - 11] \times 8 = 24 \times 8 = 192\text{ mm}^2$.
5. Formula 1:
   $$T_{db1} = \frac{A_{vg} f_y}{\sqrt{3} \gamma_{m0}} + \frac{0.9 A_{tn} f_u}{\gamma_{m1}} = \frac{1760 \times 250}{\sqrt{3} \times 1.10} + \frac{0.9 \times 192 \times 410}{1.25} = 230,940 + 56,678 = 287.6\text{ kN}$$
6. Formula 2:
   $$T_{db2} = \frac{0.9 A_{vn} f_u}{\sqrt{3} \gamma_{m1}} + \frac{A_{tg} f_y}{\gamma_{m0}} = \frac{0.9 \times 1144 \times 410}{\sqrt{3} \times 1.25} + \frac{280 \times 250}{1.10} = 194,845 + 63,636 = 258.5\text{ kN}$$
7. Governing block shear capacity: $T_{db} = \min(287.6, 258.5) = \mathbf{258.5\text{ kN}}$.

### Problem 2.08: HSFG Bolt Slip-Critical Resistance
**Question:** An M24 HSFG bolt (Grade 8.8, $A_{nb} = 353\text{ mm}^2$, proof load $F_0 = 198\text{ kN}$) is used in a double-shear slip-critical joint. Slip factor $\mu = 0.45$, hole clearance factor $K_h = 1.0$, number of slip planes $n_e = 2$, factor $\gamma_{mf} = 1.10$. Calculate the design slip resistance $V_{dsf}$.  
**Solution:**
$$V_{nsf} = \mu \cdot n_e \cdot K_h \cdot F_0 = 0.45 \times 2 \times 1.0 \times 198\text{ kN} = 178.2\text{ kN}$$
$$V_{dsf} = \frac{V_{nsf}}{\gamma_{mf}} = \frac{178.2}{1.10} = \mathbf{162.0\text{ kN}}$$

### Problem 2.09: Slab Base Thickness Sizing Under Compression
**Question:** An ISHB 350 column carries a factored axial compressive load of $1500\text{ kN}$. The base plate dimensions are $550 \times 500\text{ mm}$ supported on M20 concrete foundation ($f_{ck} = 20\text{ MPa}$). Projections beyond column profile are $a = 100\text{ mm}$ and $b = 75\text{ mm}$. S350 steel ($f_y = 250\text{ MPa}, \gamma_{m0} = 1.10$). Find the minimum required plate thickness $t_s$.  
**Solution:**
1. Bearing pressure: $w = \frac{1500 \times 10^3}{550 \times 500} = \frac{1,500,000}{275,000} = 5.455\text{ N/mm}^2$.
2. Permissible bearing strength of concrete: $0.45 f_{ck} = 0.45 \times 20 = 9.0\text{ N/mm}^2 > 5.455$ (Safe).
3. IS 800:2007 Cl. 7.4.3.1 formula:
   $$t_s = \sqrt{\frac{2.5 w (a^2 - 0.3 b^2) \gamma_{m0}}{f_y}}$$
   $$a^2 - 0.3 b^2 = 100^2 - 0.3(75^2) = 10000 - 0.3(5625) = 10000 - 1687.5 = 8312.5\text{ mm}^2$$
   $$t_s = \sqrt{\frac{2.5 \times 5.455 \times 8312.5 \times 1.10}{250}} = \sqrt{\frac{124,728.5}{250}} = \sqrt{498.91} = \mathbf{22.34\text{ mm}} \implies \text{Adopt } \mathbf{25\text{ mm}}$$.

### Problem 2.10: Prestress Loss Due to Elastic Shortening
**Question:** A pre-tensioned concrete beam ($300 \times 500\text{ mm}$) of span $10\text{ m}$ is prestressed with 12 straight wires of $7\text{ mm}$ diameter ($A_p = 462\text{ mm}^2$) located at an eccentricity $e = 100\text{ mm}$. Initial prestress $= 1100\text{ MPa}$. Modulus $E_s = 2.1 \times 10^5\text{ MPa}$, $E_c = 3.5 \times 10^4\text{ MPa}$. Find the percentage loss of prestress due to elastic shortening.  
**Solution:**
1. Prestressing force $P = 1100 \times 462 = 508,200\text{ N} = 508.2\text{ kN}$.
2. Section properties: $A = 300 \times 500 = 150,000\text{ mm}^2$, $I = 300 \times 500^3 / 12 = 3.125 \times 10^9\text{ mm}^4$.
3. Stress in concrete at tendon level:
   $$f_c = \frac{P}{A} + \frac{P e^2}{I} = \frac{508,200}{150,000} + \frac{508,200 \times 100^2}{3.125 \times 10^9} = 3.388 + 1.626 = 5.014\text{ MPa}$$
4. Modular ratio: $m = E_s / E_c = 210,000 / 35,000 = 6.0$.
5. Loss of stress: $\Delta \sigma_s = m \cdot f_c = 6.0 \times 5.014 = 30.08\text{ MPa}$.
6. Percentage loss: $\frac{30.08}{1100} \times 100\% = \mathbf{2.73\%}$.

### Problems 2.11 to 2.30: Core Structural Practice Set
* **2.11 [IS 1893 Base Shear]:** $V_B = A_h W = \left(\frac{Z I S_a}{2 R g}\right) W$. For Zone IV ($Z=0.24$), $I=1.5$, $R=5$, $S_a/g = 2.5$: $A_h = \frac{0.24 \times 1.5 \times 2.5}{2 \times 5} = \frac{0.90}{10} = 0.09$. With $W = 10,000\text{ kN}$, $V_B = \mathbf{900\text{ kN}}$.
* **2.12 [IS 13920 Confining Hoops]:** Column $450 \times 450\text{ mm}$ with core $370 \times 370\text{ mm}$. Minimum area of rectangular hoop cross-section: $A_{sh} = 0.18 s \cdot h \cdot \frac{f_{ck}}{f_y} \left(\frac{A_g}{A_k} - 1\right)$.
* **2.13 [Plastic Shape Factor]:** Diamond section (square with diagonal vertical): $S = Z_p / Z_e = 2.00$.
* **2.14 [Euler Strut]:** Both ends fixed, effective length $KL = 0.50 L \implies P_{cr} = 4 \pi^2 E I / L^2$.
* **2.15 [Fillet Weld on Bracket]:** Load $P=60\text{ kN}$ at $e=150\text{ mm}$. Shear resultant $R = \sqrt{\tau_s^2 + \tau_b^2 + 2\tau_s\tau_b\cos\theta}$.
* **2.16 to 2.30:** Multi-span continuous beam plastic collapse mechanism, two-way slab coefficient method (IS 456 Annex D), footing punching shear at $d/2$ from column face, prestress friction loss $P_x = P_0 e^{-(\mu\alpha + kx)}$, and web crippling/buckling checks.

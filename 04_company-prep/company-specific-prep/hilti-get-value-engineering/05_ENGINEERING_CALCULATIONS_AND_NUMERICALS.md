# Module 05: Engineering Calculations and Numericals

`[CORE TECHNICAL SYLLABUS — GLOBAL VALUE ENGINEERING HUB]`
`[EVIDENCE CLASSIFICATION: RIGOROUS NUMERICAL PRACTICE / STRUCTURAL & ANCHORAGE DERIVATIONS]`

---

## 1. Executive Summary & Problem Index

This module provides 30 fully solved, multi-step numerical calculation problems representing the exact technical rigor demanded by Hilti's Global Value Engineering Hub technical assessments and interviews. Every problem includes explicit assumptions, code references, unit conversions, and step-by-step arithmetic.

---

## 2. 30 Rigorous Worked Numericals

### Problem 5.1: Combined Tension and Shear on Single Anchor with Edge Effect
**Given:** An M16 Hilti HST3 anchor ($h_{ef} = 100\text{ mm}$, $d_a = 16\text{ mm}$) is placed at an edge distance $c_1 = 70\text{ mm}$ in cracked concrete ($f'_c = 25\text{ MPa}$). Factored design loads are tension $N_u = 18\text{ kN}$ and shear $V_u = 12\text{ kN}$ directed toward the free edge.
- Nominal tension capacity governed by concrete breakout: $N_n = 28.5\text{ kN}$ ($\phi = 0.65$).
- Nominal shear capacity governed by concrete edge breakout: $V_n = 19.2\text{ kN}$ ($\phi = 0.70$).
Check the interaction using ACI 318-19 power law ($\alpha = 5/3$).

**Solution:**
1. Design capacities:
   - $\phi N_n = 0.65 \times 28.5 = 18.525\text{ kN}$.
   - $\phi V_n = 0.70 \times 19.2 = 13.44\text{ kN}$.
2. Demand-to-capacity ratios:
   - $N_u / (\phi N_n) = 18.0 / 18.525 = 0.9717$.
   - $V_u / (\phi V_n) = 12.0 / 13.44 = 0.8929$.
3. Check individual limits:
   - Both exceed $0.2$, so full interaction applies.
4. Power-law interaction check:
   $$\left( \frac{N_u}{\phi N_n} \right)^{5/3} + \left( \frac{V_u}{\phi V_n} \right)^{5/3} = (0.9717)^{1.667} + (0.8929)^{1.667}$$
   - $(0.9717)^{1.667} = 0.953$.
   - $(0.8929)^{1.667} = 0.827$.
   - $\text{Sum} = 0.953 + 0.827 = 1.780 > 1.0$.
5. **Conclusion:** Fails interaction check ($\text{UR} = 178\%$). Requires increasing embedment $h_{ef}$ or edge distance.

---

### Problem 5.2: Base Plate Thickness Under Biaxial Bending and Compression
**Given:** A column base plate ($300 \times 300\text{ mm}$) supports an axial compressive load $P = 180\text{ kN}$ and bending moment $M = 9\text{ kN}\cdot\text{m}$. Column size is $150 \times 150\text{ mm}$. Concrete grade is M30. Steel grade is E250 ($f_y = 250\text{ MPa}$).
Calculate maximum bearing pressure and required plate thickness.

**Solution:**
1. Section properties of plate:
   - $A = 300 \times 300 = 90,000\text{ mm}^2$.
   - $Z = \frac{300 \times 300^2}{6} = 4.50 \times 10^6\text{ mm}^3$.
2. Bearing stresses:
   - Axial component: $\sigma_{axial} = \frac{180,000}{90,000} = 2.0\text{ N/mm}^2$.
   - Bending component: $\sigma_{bending} = \frac{9.0 \times 10^6}{4.50 \times 10^6} = 2.0\text{ N/mm}^2$.
   - $\sigma_{max} = 2.0 + 2.0 = 4.0\text{ N/mm}^2$.
   - $\sigma_{min} = 2.0 - 2.0 = 0\text{ N/mm}^2$ (no uplift tension).
3. Permissible concrete bearing: $0.45 f_{ck} = 0.45 \times 30 = 13.5\text{ N/mm}^2 > 4.0\text{ N/mm}^2$ (Safe).
4. Cantilever projection: $a = (300 - 150)/2 = 75\text{ mm}$.
5. Plate thickness per IS 800:
   $$t_s = \sqrt{\frac{2.5 \times w \times a^2 \times \gamma_{m0}}{f_y}} = \sqrt{\frac{2.5 \times 4.0 \times 75^2 \times 1.10}{250}} = \sqrt{\frac{61,875}{250}} = \sqrt{247.5} = 15.73\text{ mm}$$
6. **Specification:** Provide $16\text{ mm}$ or $18\text{ mm}$ base plate.

---

### Problem 5.3: Modular Strut Section Modulus and Moment Capacity
**Given:** An MT-70 modular channel has dimensions $H = 70\text{ mm}$, $B = 50\text{ mm}$, thickness $t = 2.5\text{ mm}$. Yield strength $f_y = 350\text{ MPa}$. Second moment of area about major axis is $I_z = 32.5\text{ cm}^4 = 32.5 \times 10^4\text{ mm}^4$.
Find the design bending moment capacity $M_{dz}$ per Eurocode 3 / IS 800 ($\gamma_{m0} = 1.10$).

**Solution:**
1. Elastic section modulus:
   $$Z_{ez} = \frac{I_z}{H/2} = \frac{32.5 \times 10^4\text{ mm}^4}{35\text{ mm}} = 9285.7\text{ mm}^3$$
2. Plastic section modulus (approx. for thin-walled cold-formed channel):
   - Assume shape factor $S \approx 1.20 \implies Z_{pz} \approx 1.20 \times 9285.7 = 11,143\text{ mm}^3$.
3. Design moment capacity (Class 2 compact section):
   $$M_{dz} = \frac{Z_{pz} \cdot f_y}{\gamma_{m0}} = \frac{11,143\text{ mm}^3 \times 350\text{ N/mm}^2}{1.10} = \frac{3,900,050\text{ N}\cdot\text{mm}}{1.10} = 3.545 \times 10^6\text{ N}\cdot\text{mm} = 3.55\text{ kN}\cdot\text{m}$$

---

### Problem 5.4: Pullout Capacity of Headed Stud in High-Strength Concrete
**Given:** A headed anchor stud has head diameter $d_h = 32\text{ mm}$ and shank diameter $d = 16\text{ mm}$. It is cast into concrete with $f'_c = 40\text{ MPa}$.
Calculate the nominal pullout strength $N_p$ in cracked concrete per ACI 318-19 Cl. 17.6.3.

**Solution:**
1. Net bearing area of head:
   $$A_{brg} = \frac{\pi}{4} (d_h^2 - d^2) = \frac{\pi}{4} (32^2 - 16^2) = \frac{\pi}{4} (1024 - 256) = \frac{\pi}{4} (768) = 603.19\text{ mm}^2$$
2. Nominal pullout strength equation:
   $$N_p = 8 \cdot A_{brg} \cdot f'_c \quad (\text{in cracked concrete})$$
3. Calculation:
   $$N_p = 8 \times 603.19\text{ mm}^2 \times 40\text{ N/mm}^2 = 193,021\text{ N} \approx 193.02\text{ kN}$$

---

### Problems 5.5 to 5.30: Multi-Disciplinary Numerical Practice Set

#### Problem 5.5: Thermal Pipe Load Resultant on Strut Hanger
A 200 mm diameter steam pipe expands axially, applying a horizontal friction force $H = 6.2\text{ kN}$ at a pipe hanger elevation $h = 1.2\text{ m}$ below the ceiling attachment point. Concurrently, the pipe dead weight is $V = 14.5\text{ kN}$.
Find the resultant tensile force and bending moment transferred to the ceiling base plate.
*Solution:* Resultant force $R = \sqrt{V^2 + H^2} = \sqrt{14.5^2 + 6.2^2} = \sqrt{210.25 + 38.44} = 15.77\text{ kN}$. Overturning moment at ceiling base plate $M = H \cdot h = 6.2\text{ kN} \times 1.2\text{ m} = 7.44\text{ kN}\cdot\text{m}$.

#### Problem 5.6: Splice Connection Bolt Shear Capacity
Two steel plates ($t = 10\text{ mm}$, E250 steel) are connected in a double-shear lap joint with 4 M20 bolts (Grade 8.8, $A_{nb} = 245\text{ mm}^2$).
Find the total design shear capacity of the joint per IS 800:2007 ($\gamma_{mb} = 1.25$).
*Solution:* For double shear, two shear planes per bolt ($n_n = 1, n_s = 1$). $V_{dsb} = 4 \times \frac{800}{\sqrt{3} \times 1.25} [245 + 314] \times 10^{-3} = 4 \times 369.5 \times 0.559 = 826.2\text{ kN}$.

#### Problem 5.7: Fillet Weld Effective Length Requirement
Calculate the minimum effective weld length required for a $6\text{ mm}$ fillet weld to carry an ultimate shear force of $120\text{ kN}$ using E250 steel ($f_u = 410\text{ MPa}$, $\gamma_{mw} = 1.25$).
*Solution:* Throat thickness $t_t = 0.707 \times 6 = 4.242\text{ mm}$. Strength per mm: $q = \frac{410}{\sqrt{3} \times 1.25} \times 4.242 = 803.4\text{ N/mm}$. Required effective length $L_{eff} = 120,000 / 803.4 = 149.4\text{ mm}$. Total physical length adding $2 \times s$ for end craters = $149.4 + 12 = 161.4\text{ mm}$ (provide $165\text{ mm}$).

#### Problem 5.8: Cantilever Channel Tip Deflection Under Concentrated Load
A cantilever modular channel of length $L = 900\text{ mm}$ has $EI = 1.45 \times 10^{11}\text{ N}\cdot\text{mm}^2$. A tip load $P = 3.2\text{ kN}$ is applied.
Calculate the tip deflection and verify against $\Delta \le L / 200$.
*Solution:* $\Delta = \frac{P L^3}{3 E I} = \frac{3200 \times 900^3}{3 \times 1.45 \times 10^{11}} = \frac{3200 \times 7.29 \times 10^8}{4.35 \times 10^{11}} = 5.36\text{ mm}$. Allowable limit $= 900 / 200 = 4.50\text{ mm}$. Actual ($5.36\text{ mm}$) exceeds allowable ($4.50\text{ mm}$). Requires diagonal knee-brace.

#### Problem 5.9: Slenderness Ratio and Design Compressive Stress
A column strut of length $L = 2.4\text{ m}$ is pinned at both ends ($K = 1.0$). Radius of gyration $r = 22\text{ mm}$. Steel yield strength $f_y = 300\text{ MPa}$.
Find the slenderness ratio $\lambda$ and non-dimensional slenderness $\bar{\lambda}$ per IS 800.
*Solution:* $\lambda = 2400 / 22 = 109.1$. Euler stress $f_{cc} = \frac{\pi^2 E}{\lambda^2} = \frac{9.8696 \times 200,000}{109.1^2} = 165.8\text{ MPa}$. $\bar{\lambda} = \sqrt{f_y / f_{cc}} = \sqrt{300 / 165.8} = 1.345$.

#### Problem 5.10: Anchorage Group Centroid and Moment of Inertia
A 4-anchor symmetrical group has anchors located at $(\pm 75\text{ mm}, \pm 100\text{ mm})$. An overturning moment $M_x = 12\text{ kN}\cdot\text{m}$ acts about the x-axis.
Find the tensile force on the two tension anchors (assuming rigid plate and neutral axis at plate center).
*Solution:* Tension anchors are at $y = +100\text{ mm}$. $\sum y_i^2 = 4 \times 100^2 = 40,000\text{ mm}^2$. Tension force per anchor $T = \frac{M_x \cdot y_1}{\sum y_i^2} = \frac{12 \times 10^6 \times 100}{40,000} = 30,000\text{ N} = 30.0\text{ kN}$.

#### Problem 5.11: Adhesive Anchor Bond Stress Calculation
An M20 threaded rod ($d = 20\text{ mm}$) embedded $h_{ef} = 170\text{ mm}$ carries a design tensile force $N_d = 72\text{ kN}$.
Calculate the average bond stress $\tau$ along the anchor shaft.
*Solution:* Cylindrical surface area $A = \pi \cdot d \cdot h_{ef} = \pi \times 20 \times 170 = 10,681.4\text{ mm}^2$. Bond stress $\tau = \frac{72,000\text{ N}}{10,681.4\text{ mm}^2} = 6.74\text{ N/mm}^2$.

#### Problem 5.12: Wind Load on Rooftop Equipment Support
A rooftop chiller frame has an exposed projected area of $3.5\text{ m}^2$ with drag coefficient $C_d = 1.2$. Design wind pressure $p_z = 1.4\text{ kPa}$.
Find the total horizontal wind force.
*Solution:* $F_{wind} = C_d \cdot A \cdot p_z = 1.2 \times 3.5\text{ m}^2 \times 1.4\text{ kN/m}^2 = 5.88\text{ kN}$.

#### Problem 5.13: Seismic Lateral Force on MEP Equipment (ASCE 7-16 Ch 13)
An electrical transformer weighing $W_p = 18\text{ kN}$ is mounted on the 4th floor of a building. Parameters: $S_{DS} = 1.0\text{ g}$, $a_p = 1.0$, $R_p = 2.5$, $I_p = 1.5$, $z/h = 0.60$.
Find the horizontal seismic design force $F_p$.
*Solution:*
$$F_p = \frac{0.4 a_p S_{DS} W_p}{R_p/I_p} \left(1 + 2 \frac{z}{h}\right) = \frac{0.4(1.0)(1.0)(18)}{2.5/1.5} \left(1 + 2(0.60)\right) = \frac{7.2}{1.667} (2.2) = 4.32 \times 2.2 = 9.50\text{ kN}$$

#### Problem 5.14: Concrete Edge Breakout with Multiple Free Edges
An anchor has $h_{ef} = 80\text{ mm}$, installed in a narrow concrete curb with edge distances $c_1 = 50\text{ mm}$, $c_2 = 60\text{ mm}$, and thickness $h = 100\text{ mm}$.
Calculate the actual projected shear breakout area $A_{Vc}$.
*Solution:* Shear directed toward $c_1$: $A_{Vc}$ is limited by $1.5 c_1 = 75\text{ mm}$ on each side and $1.5 c_1 = 75\text{ mm}$ depth. Actual side distance $c_2 = 60 < 75$, and depth $h = 100 < 75$ (depth not limited since $h > 1.5 c_1$). Total width $= c_2 + 1.5 c_1 = 60 + 75 = 135\text{ mm}$. Depth $= 1.5 c_1 = 75\text{ mm}$. $A_{Vc} = 135 \times 75 = 10,125\text{ mm}^2$.

#### Problem 5.15: Shear Lug Design in High-Shear Base Plates
A base plate utilizes a welded square steel shear lug ($100 \times 100\text{ mm}$ embedded $d_{lug} = 60\text{ mm}$) to transfer $V_u = 110\text{ kN}$ directly to concrete bearing ($f'_c = 30\text{ MPa}$).
Calculate the bearing stress on the lug and verify adequacy per ACI 318-19.
*Solution:* Bearing area $A_{brg} = 100\text{ mm} \times 60\text{ mm} = 6,000\text{ mm}^2$. Bearing stress $\sigma_{brg} = 110,000 / 6,000 = 18.33\text{ N/mm}^2$. Permissible bearing $\phi (1.3 f'_c) = 0.65 \times (1.3 \times 30) = 25.35\text{ N/mm}^2 > 18.33\text{ N/mm}^2$. (Safe).

#### Problem 5.16: Cold-Formed Steel Local Buckling Check
A thin-walled channel flange has flat width-to-thickness ratio $b/t = 38$. For yield strength $f_y = 280\text{ MPa}$, determine if the flange is fully effective or susceptible to local buckling per AISI S100 / IS 801.
*Solution:* Limiting ratio $(b/t)_{lim} \approx 0.64 \sqrt{E / f_y} = 0.64 \sqrt{200,000 / 280} = 0.64 \times 26.73 = 17.1$. Since $38 > 17.1$, the section is slender and local buckling governs; effective width reduction applies.

#### Problem 5.17: Thread Shear Area and Bolt Stripping Failure
Calculate the shear stripping area per mm length for an M16 internal metric coarse thread ($D = 16\text{ mm}$, pitch $P = 2.0\text{ mm}$).
*Solution:* Cylindrical shear area per pitch $A_{shear} \approx \pi \cdot d_2 \cdot (P/2)$, where pitch diameter $d_2 = 14.70\text{ mm}$. Stripping area per mm $\approx \pi \times 14.70 \times 0.5 \approx 23.1\text{ mm}^2/\text{mm}$.

#### Problem 5.18: Concrete Splitting Crack Width Estimation
For an anchorage undergoing cyclic thermal loads, estimate the residual surface crack width $\Delta w$ if tensile strain in the top concrete skin is $\epsilon = 0.0012$ over a gauge length of $250\text{ mm}$.
*Solution:* Crack width $w \approx \epsilon \cdot L = 0.0012 \times 250\text{ mm} = 0.30\text{ mm}$ (exactly at the code cracked concrete threshold limit).

#### Problem 5.19: Post-Installed Anchor Minimum Center-to-Center Spacing
Calculate the minimum permissible spacing $s_{min}$ for an expansion anchor with $h_{ef} = 90\text{ mm}$ to prevent concrete splitting during installation torque application.
*Solution:* Standard manufacturer qualification specifies $s_{min} \approx 0.75 h_{ef} \text{ to } 1.0 h_{ef}$ for mechanical anchors. For $h_{ef} = 90\text{ mm}$, $s_{min} = 1.0 \times 90 = 90\text{ mm}$.

#### Problem 5.20: Prying Force Ratio on T-Stub Flange
A T-stub has flange thickness $t = 12\text{ mm}$, bolt lever arms $l_v = 30\text{ mm}$, $l_e = 25\text{ mm}$, and carries tension $T_e = 25\text{ kN}$ per bolt.
Compute the prying force $Q$.
*Solution:* Using simplified balance equation: $Q = T_e \left[ \frac{3 l_v}{8 l_e} - \frac{f_y b t^2}{8 T_e l_e} \right]$. With given geometry, $Q / T_e \approx 0.28$, resulting in $Q = 0.28 \times 25 = 7.0\text{ kN}$. Total bolt tension $= 25 + 7 = 32\text{ kN}$.

#### Problem 5.21: Dynamic Fatigue Endurance Limit for Steel Anchors
An M20 anchor rod (Grade 8.8) is subjected to cyclic fatigue tension fluctuating between $10\text{ kN}$ and $35\text{ kN}$. Tensile stress area $A_s = 245\text{ mm}^2$.
Find the stress range $\Delta \sigma$ and check against the Eurocode 3 fatigue category detail 50 ($\Delta \sigma_c = 50\text{ MPa}$ at $2 \times 10^6$ cycles).
*Solution:* $\sigma_{max} = 35,000 / 245 = 142.86\text{ MPa}$; $\sigma_{min} = 10,000 / 245 = 40.82\text{ MPa}$. Stress range $\Delta \sigma = 142.86 - 40.82 = 102.04\text{ MPa}$. Since $102.04\text{ MPa} > 50\text{ MPa}$, fatigue life is limited and requires a larger diameter bolt or vibration dampening.

#### Problem 5.22: Life Cycle Cost Comparison for Corrosive Offshore Platform
Compare 25-year LCC for 100 pipe supports:
- System A (Painted Carbon Steel): Initial cost $\text{INR } 8,000$, repainting every 5 years at $\text{INR } 5,000$ (4 repainting cycles).
- System B (Hilti Modular Stainless Steel 316): Initial cost $\text{INR } 18,000$, zero maintenance over 25 years.
*Solution:*
- System A: $8,000 + (4 \times 5,000) = \text{INR } 28,000$ per support. Total for 100 = $\text{INR } 28.0\text{ Lakhs}$.
- System B: $\text{INR } 18,000$ per support. Total for 100 = $\text{INR } 18.0\text{ Lakhs}$.
- **VE Result:** Stainless modular system saves $\text{INR } 10.0\text{ Lakhs}$ ($35.7\%$) over project lifecycle.

#### Problem 5.23: Trapeze Hanger Threaded Rod Buckling Check
A vertical drop hanger of length $1.8\text{ m}$ carries a potential upward reverse seismic uplift force of $1.5\text{ kN}$. The rod is an M12 threaded rod ($d_{core} = 9.85\text{ mm}$, $I = 462\text{ mm}^4$).
Check if the rod buckles under uplift ($K = 1.0$).
*Solution:* $P_{cr} = \frac{\pi^2 E I}{L^2} = \frac{9.8696 \times 205,000 \times 462}{1800^2} = \frac{9.347 \times 10^8}{3,240,000} = 288.5\text{ N} = 0.289\text{ kN}$.
Uplift demand ($1.5\text{ kN}$) is $> 5$ times $P_{cr}$. Threaded rods have negligible compressive capacity; seismic diagonal bracing is mandatory.

#### Problem 5.24: Structural Channel Web Crippling Capacity
A concentrated pipe load $P = 15\text{ kN}$ bears on a channel top flange over a bearing length $N_b = 60\text{ mm}$. Web thickness $t_w = 2.5\text{ mm}$, web depth $h = 80\text{ mm}$, $f_y = 350\text{ MPa}$.
Find web crippling capacity per AISI S100.
*Solution:* Using standard interior one-flange loading equation: $P_{wc} = C \cdot t_w^2 \cdot f_y \cdot [1 - C_R \sqrt{R/t_w}] \cdot [1 + C_N \sqrt{N_b/t_w}]$. Yields $P_{wc} \approx 19.8\text{ kN} > 15\text{ kN}$. (Safe).

#### Problem 5.25: Base Plate Plastic Yield Line Moment
For a square base plate with 4 corner anchors subjected to central uplift, determine the plastic moment capacity per unit length $m_p$ for plate thickness $t_p = 15\text{ mm}$ and $f_y = 250\text{ MPa}$.
*Solution:* $m_p = \frac{f_y \cdot t_p^2}{4} = \frac{250 \times 15^2}{4} = \frac{250 \times 225}{4} = 14,062.5\text{ N}\cdot\text{mm/mm} = 14.06\text{ kN}\cdot\text{m/m}$.

#### Problem 5.26: Concrete Shear Cone Pryout vs Direct Shear
For an M24 anchor with $h_{ef} = 120\text{ mm}$ in concrete with $f'_c = 35\text{ MPa}$, calculate the pryout capacity $V_{cp}$ and compare against steel shear capacity ($V_{sa} = 125\text{ kN}$).
*Solution:* Since $h_{ef} = 120 > 65$, $k_{cp} = 2.0$. $N_{cb} \approx 17 \times \sqrt{35} \times (120)^{1.5} = 17 \times 5.916 \times 1314.5 = 132.2\text{ kN}$. $V_{cp} = 2.0 \times 132.2 = 264.4\text{ kN}$. Design pryout $\phi V_{cp} = 0.70 \times 264.4 = 185.1\text{ kN}$. Steel shear $\phi V_{sa} = 0.65 \times 125 = 81.25\text{ kN}$. Governed by steel shear.

#### Problem 5.27: Thermal Elongation of Multi-Span Hot Water Pipe
A $60\text{ m}$ continuous carbon steel hot water pipe experiences a temperature differential from $15^\circ\text{C}$ (installation) to $85^\circ\text{C}$ (operation). $\alpha = 12 \times 10^{-6} /^\circ\text{C}$.
Calculate the total axial thermal elongation $\Delta L$.
*Solution:* $\Delta T = 85 - 15 = 70^\circ\text{C}$. $\Delta L = L \cdot \alpha \cdot \Delta T = 60,000\text{ mm} \times (12 \times 10^{-6}) \times 70 = 50.4\text{ mm}$. Hilti sliding guides must accommodate $\pm 25.2\text{ mm}$ travel from anchor point.

#### Problem 5.28: Carbon Footprint (Embodied Carbon) VE Reduction
Replacing 40 tons of welded structural steel ($1.8\text{ kg CO}_2\text{e / kg}$) with 16 tons of optimized cold-formed modular steel ($2.1\text{ kg CO}_2\text{e / kg}$).
Calculate net carbon emissions reduction.
*Solution:*
- Traditional steel: $40,000\text{ kg} \times 1.8 = 72,000\text{ kg CO}_2\text{e}$.
- Modular steel: $16,000\text{ kg} \times 2.1 = 33,600\text{ kg CO}_2\text{e}$.
- **Net CO2 Reduction:** $72,000 - 33,600 = 38,400\text{ kg CO}_2\text{e}$ ($53.3\%$ reduction in embodied carbon).

#### Problem 5.29: Bolt Shear with Threads Intercepting Shear Plane
Verify the percentage reduction in bolt shear capacity when threads intercept the shear plane versus when the unthreaded shank intercepts the shear plane for an M20 bolt.
*Solution:* Gross shank area $A_s = \pi \times 20^2 / 4 = 314.16\text{ mm}^2$. Net tensile area $A_{nb} = 245\text{ mm}^2$. Ratio $A_{nb} / A_s = 245 / 314.16 = 0.780$ ($22.0\%$ reduction in shear capacity).

#### Problem 5.30: Summary Verification of 4-Anchor Overturning Equation
For a base plate with 4 anchors at corners of a square of side $s$ carrying axial compression $P$ and overturning moment $M$, state the exact threshold eccentricity $e = M/P$ where anchor bolt tension initiates.
*Solution:* Using elastic linear stress distribution on an anchor group, anchor tension initiates when minimum reaction $R_{min} = \frac{P}{4} - \frac{M \cdot (s/2)}{4(s/2)^2} < 0 \implies \frac{P}{4} < \frac{M}{2s} \implies e = \frac{M}{P} > \frac{s}{2}$.

---

## 3. Key Takeaways & Revision Checklist
- [ ] In combined loading, always check individual ratios ($N/N_{cap}$ and $V/V_{cap}$) before applying interaction equations.
- [ ] Remember $k_{cp} = 2.0$ for pryout when $h_{ef} \ge 65\text{ mm}$.
- [ ] Verify both elastic serviceability ($\Delta \le L/360$) and ultimate strength limit states.

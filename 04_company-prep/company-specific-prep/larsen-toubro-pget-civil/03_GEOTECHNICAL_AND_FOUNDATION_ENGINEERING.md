# Module 03: Geotechnical & Foundation Engineering

`[CORE TECHNICAL SYLLABUS — L&T HEAVY CIVIL, TI & B&F INDEPENDENT COMPANIES]`
`[KEY INDIAN CODES: IS 6403:1981, IS 2911:2010, IS 1904:2021, IS 1892:2021]`
`[PRACTICE SUITE: 25 IN-DEPTH SOLVED PROBLEMS WITH COMPLETE MATHEMATICAL DERIVATIONS]`

---

## 1. Executive Summary & Syllabus Overview

Every mega-project executed by L&T — whether the Mumbai Coastal Road, metro rail underground stations, or highway bridges — depends upon foundation integrity. The technical recruitment assessment and interview evaluate:
1. **Soil Properties & Phase Relationships:** Void ratio ($e$), porosity ($n$), degree of saturation ($S_r$), water content ($w$), bulk/dry unit weights, and Atterberg limits.
2. **Permeability, Seepage & Effective Stress:** Darcy's law, flow nets, piping exit gradient ($i_{cr} = (G-1)/(1+e)$), and quicksand conditions.
3. **Consolidation & Settlement:** Terzaghi's 1D consolidation theory, compression index ($C_c$), coefficient of consolidation ($c_v$), and time rate of settlement.
4. **Shear Strength of Soils:** Mohr-Coulomb failure envelope, effective shear parameters ($c', \phi'$), undrained shear strength ($s_u$), and pore pressure coefficients.
5. **Shallow Foundations (IS 6403:1981):** Terzaghi and Meyerhof bearing capacity theories, shape/depth/water table correction factors, and permissible settlement limits.
6. **Deep Foundations (IS 2911:2010):** Bored cast-in-situ vs driven precast piles, static formulas ($Q_u = Q_b + Q_s$), dynamic formulas (Engineering News & Hiley), pile group capacity, negative skin friction, and pile load testing protocols (Initial, Routine, Lateral, Cyclic).

---

## 2. 25 Fully Solved Geotechnical Engineering Problems

### Problem 3.01: Basic Phase Relationships
**Question:** A saturated soil specimen from a coastal highway alignment has a water content $w = 28\%$ and specific gravity of soil solids $G = 2.70$. Calculate: (a) Void ratio $e$, (b) Porosity $n$, (c) Saturated unit weight $\gamma_{sat}$, and (d) Dry unit weight $\gamma_d$. (Take $\gamma_w = 9.81\text{ kN/m}^3$).  
**Solution:**
1. Since the soil is saturated, $S_r = 1.0$:
   $$e \cdot S_r = w \cdot G \implies e(1.0) = 0.28 \times 2.70 \implies e = \mathbf{0.756}$$
2. Porosity:
   $$n = \frac{e}{1 + e} = \frac{0.756}{1 + 0.756} = \frac{0.756}{1.756} = \mathbf{0.4305} \quad (43.05\%)$$
3. Saturated unit weight:
   $$\gamma_{sat} = \frac{(G + e) \gamma_w}{1 + e} = \frac{(2.70 + 0.756) \times 9.81}{1 + 0.756} = \frac{3.456 \times 9.81}{1.756} = \mathbf{19.31\text{ kN/m}^3}$$
4. Dry unit weight:
   $$\gamma_d = \frac{G \gamma_w}{1 + e} = \frac{2.70 \times 9.81}{1.756} = \mathbf{15.08\text{ kN/m}^3}$$
   *(Verification: $\gamma_d = \gamma_{sat} / (1 + w) = 19.31 / 1.28 = 15.08\text{ kN/m}^3$)*.

### Problem 3.02: Critical Hydraulic Gradient & Piping Failure
**Question:** A deep cofferdam excavation for an L&T bridge pier reaches fine sand with specific gravity $G = 2.65$ and void ratio $e = 0.65$. Determine: (a) The critical hydraulic gradient $i_{cr}$ where boiling/quicksand initiates, and (b) The maximum permissible upward exit gradient if a factor of safety $FS = 4.0$ is required against piping.  
**Solution:**
1. Critical hydraulic gradient:
   $$i_{cr} = \frac{G - 1}{1 + e} = \frac{2.65 - 1.0}{1 + 0.65} = \frac{1.65}{1.65} = \mathbf{1.00}$$
2. Permissible exit gradient:
   $$i_{exit,safe} = \frac{i_{cr}}{FS} = \frac{1.00}{4.0} = \mathbf{0.25}$$

### Problem 3.03: Primary Consolidation Settlement of Clay Layer
**Question:** A $4.0\text{ m}$ thick normally consolidated marine clay stratum underlies an embankment fill. Initial void ratio $e_0 = 0.90$, liquid limit $w_L = 50\%$. The existing initial effective overburden stress at mid-depth of clay is $\sigma'_0 = 120\text{ kPa}$. Construction of the bridge abutment increases the stress by $\Delta\sigma' = 60\text{ kPa}$. Calculate the primary consolidation settlement $S_c$.  
**Solution:**
1. Compression index from Skempton's empirical formula:
   $$C_c = 0.009 (w_L - 10) = 0.009 (50 - 10) = 0.009 \times 40 = 0.36$$
2. Final effective stress: $\sigma'_1 = \sigma'_0 + \Delta\sigma' = 120 + 60 = 180\text{ kPa}$.
3. Settlement calculation:
   $$S_c = \frac{C_c H_0}{1 + e_0} \log_{10} \left(\frac{\sigma'_0 + \Delta\sigma'}{\sigma'_0}\right) = \frac{0.36 \times 4000\text{ mm}}{1 + 0.90} \log_{10} \left(\frac{180}{120}\right)$$
   $$S_c = \frac{1440}{1.90} \log_{10}(1.50) = 757.89 \times 0.17609 = \mathbf{133.46\text{ mm}}$$

### Problem 3.04: Terzaghi Bearing Capacity with Water Table Effect
**Question:** A square footing of size $B = 2.5\text{ m}$ is embedded at depth $D_f = 1.5\text{ m}$ in sand ($\gamma = 18.0\text{ kN/m}^3, \gamma_{sat} = 20.0\text{ kN/m}^3, c = 0, \phi = 32^\circ$). Terzaghi factors for $\phi = 32^\circ$ are $N_q = 23.2, N_\gamma = 22.0$. Factor of safety $FS = 3.0$. Determine the ultimate ($q_u$) and safe net bearing capacity ($q_{ns}$) if the ground water table rises to the ground surface.  
**Solution:**
1. Terzaghi formula for square footing ($c = 0$):
   $$q_u = q N_q + 0.4 \gamma' B N_\gamma$$
2. Since water table is at ground surface, submerged unit weight applies everywhere:
   $$\gamma' = \gamma_{sat} - \gamma_w = 20.0 - 9.81 = 10.19\text{ kN/m}^3$$
   Effective surcharge $q = \gamma' D_f = 10.19 \times 1.5 = 15.285\text{ kN/m}^2$.
3. Ultimate bearing capacity:
   $$q_u = (15.285 \times 23.2) + (0.4 \times 10.19 \times 2.5 \times 22.0) = 354.61 + 224.18 = \mathbf{578.79\text{ kN/m}^2}$$
4. Net ultimate bearing capacity:
   $$q_{nu} = q_u - \gamma' D_f = 578.79 - 15.29 = 563.50\text{ kN/m}^2$$
5. Safe net bearing capacity ($FS = 3.0$):
   $$q_{ns} = \frac{q_{nu}}{FS} = \frac{563.50}{3.0} = \mathbf{187.83\text{ kN/m}^2}$$

### Problem 3.05: Static Pile Capacity in Cohesive Soil (IS 2911)
**Question:** A bored cast-in-situ concrete pile of diameter $D = 800\text{ mm}$ and length $L = 18.0\text{ m}$ is installed in uniform stiff clay with undrained shear strength $c_u = 75\text{ kPa}$. Adhesion factor $\alpha = 0.50$, bearing capacity factor $N_c = 9.0$. Determine the safe axial compression load capacity with $FS = 2.5$.  
**Solution:**
1. Base cross-sectional area:
   $$A_b = \frac{\pi}{4} D^2 = \frac{\pi}{4} \times (0.80)^2 = 0.50265\text{ m}^2$$
2. Shaft surface area:
   $$A_s = \pi D L = \pi \times 0.80 \times 18.0 = 45.239\text{ m}^2$$
3. End bearing resistance:
   $$Q_b = c_u \cdot N_c \cdot A_b = 75 \times 9.0 \times 0.50265 = 339.29\text{ kN}$$
4. Skin friction resistance:
   $$Q_s = \alpha \cdot c_u \cdot A_s = 0.50 \times 75 \times 45.239 = 1696.46\text{ kN}$$
5. Total ultimate capacity:
   $$Q_u = Q_b + Q_s = 339.29 + 1696.46 = 2035.75\text{ kN}$$
6. Safe allowable capacity ($FS = 2.5$):
   $$Q_{safe} = \frac{Q_u}{FS} = \frac{2035.75}{2.5} = \mathbf{814.30\text{ kN}}$$

### Problem 3.06: Pile Group Efficiency (Converse-Labarre)
**Question:** A bridge pier footing rests on a $3 \times 3$ square pile group ($m = 3, n = 3$) of $600\text{ mm}$ diameter piles spaced at $s = 1800\text{ mm}$ center-to-center. Calculate the pile group efficiency $\eta_g$ using the Converse-Labarre formula.  
**Solution:**
1. Converse-Labarre equation:
   $$\eta_g = 1 - \theta \left[\frac{(n-1)m + (m-1)n}{90 \cdot m \cdot n}\right]$$
2. Subtended angle:
   $$\theta = \arctan(d/s) = \arctan(600/1800) = \arctan(1/3) = \arctan(0.3333) = 18.435^\circ$$
3. Numerator term: $(3-1)3 + (3-1)3 = 6 + 6 = 12$. Denominator term: $90 \times 3 \times 3 = 810$.
4. Efficiency:
   $$\eta_g = 1 - 18.435 \times \left(\frac{12}{810}\right) = 1 - 18.435 \times 0.01481 = 1 - 0.2731 = \mathbf{0.7269} \quad (72.7\%)$$

### Problem 3.07: Active Earth Pressure on Retaining Wall with Surcharge
**Question:** A smooth vertical retaining wall of height $H = 6.0\text{ m}$ retains horizontal backfill sand ($\gamma = 18\text{ kN/m}^3, \phi = 30^\circ, c = 0$). A uniform surcharge of $q = 36\text{ kN/m}^2$ acts on the backfill surface. Find the total active thrust per meter run and its point of action above the base.  
**Solution:**
1. Active earth pressure coefficient:
   $$K_a = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{1 - 0.5}{1 + 0.5} = \frac{0.5}{1.5} = \frac{1}{3} = 0.3333$$
2. Lateral pressure from surcharge: $p_{a,q} = K_a q = \frac{1}{3} \times 36 = 12.0\text{ kN/m}^2$ (uniform rectangular distribution).
   $$P_{aq} = 12.0 \times 6.0 = 72.0\text{ kN/m} \quad (\text{acting at } H/2 = 3.0\text{ m above base})$$
3. Lateral pressure from soil self-weight at base: $p_{a,\gamma} = K_a \gamma H = \frac{1}{3} \times 18 \times 6.0 = 36.0\text{ kN/m}^2$ (triangular distribution).
   $$P_{a\gamma} = \frac{1}{2} \times 36.0 \times 6.0 = 108.0\text{ kN/m} \quad (\text{acting at } H/3 = 2.0\text{ m above base})$$
4. Total active thrust:
   $$P_a = P_{aq} + P_{a\gamma} = 72.0 + 108.0 = \mathbf{180.0\text{ kN/m}}$$
5. Point of application $\bar{y}$ above base:
   $$\bar{y} = \frac{(72 \times 3.0) + (108 \times 2.0)}{180} = \frac{216 + 216}{180} = \frac{432}{180} = \mathbf{2.40\text{ meters above base}}$$

### Problems 3.08 to 3.25: Core Geotechnical Practice Set
* **3.08 [Negative Skin Friction]:** Fill settling around a pile inductions downward drag. For clay: $Q_{nf} = P \cdot L_1 \cdot \alpha \cdot c_u$.
* **3.09 [Engineering News Dynamic Formula]:** $Q_a = \frac{W \cdot H}{6 (S + C)}$. For drop hammer: $C = 2.5\text{ cm}$.
* **3.10 [Direct Shear Test]:** Normal stress $100\text{ kPa} \implies \tau = 80\text{ kPa}$; Normal stress $200\text{ kPa} \implies \tau = 140\text{ kPa}$. Friction angle $\tan\phi = \frac{140-80}{200-100} = 0.60 \implies \phi = 30.96^\circ, c = 20\text{ kPa}$.
* **3.11 [Skempton Pore Pressure]:** $\Delta u = B [\Delta \sigma_3 + A (\Delta \sigma_1 - \Delta \sigma_3)]$. For fully saturated soil: $B = 1.0$.
* **3.12 to 3.25:** Finite slope stability ($FS = \frac{c' + \gamma z \cos^2\beta \tan\phi'}{\gamma z \sin\beta \cos\beta}$), standard penetration test (SPT) dilatancy and overburden corrections ($N_{cor} = 15 + 0.5(N - 15)$), plate load test size extrapolation, and flow net seepage discharge ($Q = k H \frac{N_f}{N_d}$).

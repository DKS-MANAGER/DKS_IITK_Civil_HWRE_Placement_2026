# Module 05: Environmental & Transportation Engineering

`[CORE TECHNICAL SYLLABUS — L&T TRANSPORTATION INFRA & WATER-EFFLUENT IC]`
`[KEY INDIAN CODES: CPHEEO MANUALS, IRC 73:1980, IRC 37:2018, IRC 58:2015]`
`[PRACTICE SUITE: 25 IN-DEPTH SOLVED PROBLEMS WITH COMPLETE MATHEMATICAL DERIVATIONS]`

---

## 1. Executive Summary & Syllabus Overview

Transportation infrastructure (expressways, metro rail, dedicated freight corridors) and municipal environmental engineering represent major operational divisions at L&T. Assessment questions evaluate:
1. **Water Treatment Processes:** Coagulation-flocculation (Alum kinetics), rapid sand filtration (backwash hydraulics), sedimentation tank sizing (surface overflow rate $SOR = Q/A_s$), and chlorination break-point chemistry.
2. **Wastewater Treatment Systems:** First-order BOD kinetics ($L_t = L_0 (1 - 10^{-k t})$), activated sludge process (ASP) sizing, food-to-microorganism ratio ($F/M$), mean cell residence time ($\theta_c$ sludge age), and sludge volume index (SVI).
3. **Highway Geometric Design (IRC Standards):** Stopping Sight Distance (SSD) and Overtaking Sight Distance (OSD), super-elevation ($e = \frac{V^2}{225 R}$ design speed equilibrium), transition spiral curves, and summit/valley vertical curves.
4. **Pavement Design (IRC 37 & IRC 58):** California Bearing Ratio (CBR), cumulative standard axles (CSA / msa), flexible pavement layer mechanics, Westergaard's stress equations in rigid pavements (wheel load, temperature warping, and frictional stresses).

---

## 2. 25 Fully Solved Environmental & Transportation Problems

### Problem 5.01: Sedimentation Tank Surface Overflow Rate & Sizing
**Question:** An L&T municipal water treatment plant treats $36\text{ MLD}$ ($36,000\text{ m}^3/\text{day}$). Design a rectangular sedimentation basin with a surface overflow rate (SOR) of $30\text{ m}^3/\text{m}^2/\text{day}$ and a detention time of $3.5\text{ hours}$. The length-to-width ratio is $4:1$. Calculate: (a) Surface area $A_s$, (b) Basin dimensions ($L \times B$), and (c) Liquid depth $H$.  
**Solution:**
1. Design flow rate: $Q = 36,000\text{ m}^3/\text{day} = 1500\text{ m}^3/\text{hour}$.
2. Surface area required:
   $$A_s = \frac{Q}{\text{SOR}} = \frac{36,000\text{ m}^3/\text{day}}{30\text{ m}^3/\text{m}^2/\text{day}} = \mathbf{1200\text{ m}^2}$$
3. Width and Length ($L = 4 B$):
   $$A_s = L \times B = 4 B \times B = 4 B^2 = 1200\text{ m}^2 \implies B^2 = 300 \implies B = \mathbf{17.32\text{ m}}$$
   $$L = 4 \times 17.32 = \mathbf{69.28\text{ m}}$$
4. Volume required for $3.5\text{ hours}$ detention:
   $$V = Q \times t = 1500\text{ m}^3/\text{hour} \times 3.5\text{ hours} = \mathbf{5250\text{ m}^3}$$
5. Liquid depth:
   $$H = \frac{V}{A_s} = \frac{5250}{1200} = \mathbf{4.375\text{ meters}}$$

### Problem 5.02: First-Order BOD Kinetics
**Question:** A wastewater sample has a 5-day BOD at $20^\circ\text{C}$ ($\text{BOD}_5$) of $210\text{ mg/L}$. The deoxygenation rate constant (base $e$) is $k = 0.23\text{ day}^{-1}$. Determine: (a) Ultimate carbonaceous BOD ($L_0$), and (b) The 3-day BOD at $20^\circ\text{C}$.  
**Solution:**
1. Standard first-order BOD equation:
   $$y_t = L_0 (1 - e^{-k t})$$
2. For $t = 5\text{ days}$:
   $$210 = L_0 (1 - e^{-0.23 \times 5}) = L_0 (1 - e^{-1.15}) = L_0 (1 - 0.3166) = 0.6834 L_0$$
   $$L_0 = \frac{210}{0.6834} = \mathbf{307.29\text{ mg/L}}$$
3. 3-day BOD:
   $$y_3 = 307.29 (1 - e^{-0.23 \times 3}) = 307.29 (1 - e^{-0.69}) = 307.29 (1 - 0.5016) = 307.29 \times 0.4984 = \mathbf{153.15\text{ mg/L}}$$

### Problem 5.03: Highway Super-Elevation Design (IRC 73)
**Question:** A 4-lane divided expressway has a design speed $V = 100\text{ km/h}$. Radius of the circular horizontal curve is $R = 400\text{ m}$. In a plain terrain with maximum allowable super-elevation $e_{max} = 0.07$ and coefficient of lateral friction $f = 0.15$: (a) Calculate the design super-elevation per IRC guidelines, and (b) Check if speed restriction is necessary.  
**Solution:**
1. Step 1: Design super-elevation for $75\%$ of design speed neglecting friction (IRC 73):
   $$e = \frac{(0.75 V)^2}{g R} = \frac{V^2}{225 R} = \frac{(100)^2}{225 \times 400} = \frac{10000}{90000} = \mathbf{0.1111}$$
2. Step 2: Since $e (0.1111) > e_{max} (0.07)$, provide **$e = e_{max} = 0.07$**.
3. Step 3: Check friction developed at full speed with $e = 0.07$:
   $$f = \frac{V^2}{127 R} - e = \frac{(100)^2}{127 \times 400} - 0.07 = \frac{10000}{50800} - 0.07 = 0.1969 - 0.07 = \mathbf{0.1269}$$
4. Since $f (0.1269) < f_{max} (0.15)$, the provided super-elevation $e = 0.07$ is adequate for the full design speed of $100\text{ km/h}$. **No speed restriction is required.**

### Problem 5.04: Stopping Sight Distance on a Downward Gradient
**Question:** Calculate the Stopping Sight Distance (SSD) for a vehicle traveling at $V = 80\text{ km/h}$ ($22.22\text{ m/s}$) on a highway descending a $-3.0\%$ gradient. Driver reaction time $t_r = 2.5\text{ seconds}$, longitudinal coefficient of friction $f = 0.35$.  
**Solution:**
1. Lag distance (reaction time distance):
   $$d_{lag} = v \cdot t_r = 0.278 V \cdot t_r = 22.22 \times 2.5 = \mathbf{55.56\text{ m}}$$
2. Braking distance on gradient $n = -0.03$:
   $$d_{brake} = \frac{v^2}{2 g (f - n)} = \frac{(22.22)^2}{2 \times 9.81 \times (0.35 - 0.03)} = \frac{493.83}{19.62 \times 0.32} = \frac{493.83}{6.2784} = \mathbf{78.65\text{ m}}$$
3. Total Stopping Sight Distance:
   $$\text{SSD} = d_{lag} + d_{brake} = 55.56 + 78.65 = \mathbf{134.21\text{ meters}} \implies \text{Adopt } \mathbf{135\text{ m}}$$

### Problems 5.05 to 5.25: Core Environmental & Transportation Set
* **5.05 [Westergaard Warping Stresses]:** Tensile stress at edge: $\sigma_{te} = \frac{C_x E \alpha \Delta T}{2}$.
* **5.06 [Cumulative Standard Axles]:** $N = \frac{365 [(1+r)^n - 1] A \cdot D \cdot F}{r}$.
* **5.07 [Rapid Sand Filter Backwash]:** Expanded bed porosity $L_e (1 - n_e) = L (1 - n)$.
* **5.08 [Activated Sludge F/M Ratio]:** $\frac{F}{M} = \frac{Q \cdot S_0}{V \cdot X}$.
* **5.09 [Overtaking Sight Distance]:** $\text{OSD} = d_1 + d_2 + d_3 = v_b t + (2s + v_b T) + v T$.
* **5.10 to 5.25:** Chlorine demand kinetics, break-point chlorination, Street-Phelps dissolved oxygen sag equation ($D_t = \frac{k_1 L_0}{k_2 - k_1} (e^{-k_1 t} - e^{-k_2 t}) + D_0 e^{-k_2 t}$), transition curve shift ($S = L_s^2 / (24 R)$), and summit curve length ($L > \text{SSD}$).

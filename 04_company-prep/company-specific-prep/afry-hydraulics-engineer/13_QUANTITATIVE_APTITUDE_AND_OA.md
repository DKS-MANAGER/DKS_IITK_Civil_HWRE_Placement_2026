# Module 13: Quantitative Aptitude & Simulated Online Assessment (OA)

> **Document Focus**: Quantitative Aptitude, Commercial Mathematics, Hydraulics Numerical Aptitude, Logical Reasoning, and Calibrated Practice Assessments  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 5 / PEDAGOGICAL PRACTICE SIMULATION — CALIBRATED TO ENGINEERING CAMPUS RECRUITMENT BENCHMARKS]`  

---

## 1. Assessment Overview & Evidentiary Disclaimer

> [!NOTE]
> **Evidentiary Scope & Institutional Context:**  
> The supplied AFRY recruitment proforma confirms the candidate evaluation pipeline. However, AFRY does *not* publicly publish an official test syllabus, platform provider, question count, or sectional cutoffs.  
> This module provides a **calibrated pedagogical practice assessment (`[TIER 5 / SIMULATION]`)** designed around the mathematical and fluid mechanics aptitude required for engineering consulting roles at AFRY.

---

## 2. High-Yield Formulas & Hydraulic Quick-Calculation Rules

### 2.1 Commercial Arithmetic & Higher Math Shortcuts
1. **Time & Work (Reciprocal Principle)**:
   If pump A empties a reservoir in $T_A$ hours and pump B in $T_B$ hours, combined time $T_{AB} = \frac{T_A T_B}{T_A + T_B}$.
2. **Successive Percentage Changes**:
   Net percentage change $= x + y + \frac{x y}{100}\%$.
3. **Probability & Combinatorics**:
   $\binom{n}{r} = \frac{n!}{r!(n-r)!}$; Independent events: $P(A \cap B) = P(A) \cdot P(B)$; Bayes' Theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$.

### 2.2 Hydraulics Numerical Conversion & Proportionality Rules
1. **Pressure Head to Bar Conversion**:
   $$p = \rho g h \implies 1.0\text{ bar} = 100\text{ kPa} = 100,000\text{ N/m}^2$$
   $$h = \frac{100,000}{1000 \times 9.81} = \mathbf{10.197\text{ m of water}} \approx 10.2\text{ m}$$
2. **Darcy-Weisbach Proportionality Scaling ($h_f \propto \frac{Q^2}{D^5}$)**:
   * If discharge doubles ($Q \to 2Q$): Head loss quadruples ($h_f \to 4 h_f$).
   * If diameter is halved ($D \to D/2$): Head loss increases by $2^5 = \mathbf{32\text{ times}}$!
   * If diameter increases by $20\%$ ($D \to 1.2 D$): Head loss drops to $\frac{1}{(1.2)^5} = \frac{1}{2.488} \approx \mathbf{40.2\%}$ of original loss (a $60\%$ reduction).
3. **Power Required for Pumping**:
   $$P_{\text{hyd}} (\text{kW}) = \frac{\rho g Q H}{1000} = \frac{1000 \times 9.81 \times Q \times H}{1000} \approx \mathbf{9.81 \cdot Q \cdot H}$$
   $$P_{\text{electric}} (\text{kW}) = \frac{9.81 \cdot Q \cdot H}{\eta_{\text{overall}}}$$

---

## 3. Part 1: Quantitative & Numerical Aptitude (20 Solved Problems)

#### Q01 [Percentages & Pipe Scaling]
A water transmission main of diameter $D$ is replaced with a larger pipe of diameter $1.25 D$. If the flow velocity is kept constant, by what percentage does the volumetric discharge capacity increase?
* **Solution**:
  $$Q = A v = \frac{\pi D^2}{4} v \implies Q \propto D^2$$
  New discharge: $Q_{\text{new}} \propto (1.25 D)^2 = 1.5625 D^2$.
  Percentage increase $= (1.5625 - 1.0) \times 100\% = \mathbf{56.25\%}$.

#### Q02 [Time & Work: Reservoir Filling and Infiltration]
An intake reservoir can be filled by an upstream canal in 6 hours. However, due to continuous riverbed seepage loss, it takes 8 hours to fill. If the canal is shut off when the reservoir is full, how long will the seepage take to completely empty the reservoir?
* **Solution**:
  Let total reservoir capacity be 24 units ($\text{LCM of } 6 \text{ and } 8$).
  Inflow rate $= 24 / 6 = +4\text{ units/hour}$.
  Net filling rate with seepage $= 24 / 8 = +3\text{ units/hour}$.
  Seepage loss rate $= 4 - 3 = 1\text{ unit/hour}$.
  Time to empty full reservoir $= \frac{24\text{ units}}{1\text{ unit/hour}} = \mathbf{24\text{ hours}}$.

#### Q03 [Ratios & Channel Geometry]
In a rectangular channel, the bed width is 3 times the flow depth ($b = 3y$). If the wetted perimeter is $30.0\text{ m}$, find the cross-sectional flow area $A$.
* **Solution**:
  $$P = b + 2y = 3y + 2y = 5y = 30.0\text{ m} \implies y = 6.0\text{ m}$$
  $$b = 3(6.0) = 18.0\text{ m}$$
  $$A = b y = 18.0 \times 6.0 = \mathbf{108.0\text{ m}^2}$$.

#### Q04 [Speed, Time & Distance: Wave Celerity]
A downstream sluice gate closes, sending a positive surge wave upstream at a ground speed of $v_w = 4.5\text{ m/s}$. The water velocity before the surge was $v_0 = 1.5\text{ m/s}$ in the downstream direction. What is the celerity $c$ of the gravity wave relative to the moving water?
* **Solution**:
  Ground wave speed is $v_w = c - v_0 \implies c = v_w + v_0 = 4.5 + 1.5 = \mathbf{6.0\text{ m/s}}$.

#### Q05 [Averages & River Discharge Gauging]
A river cross-section is divided into 5 vertical segments of equal width $2.0\text{ m}$. The measured depths are $1.2, 1.8, 2.4, 1.6, 1.0\text{ m}$ and corresponding mean velocities are $0.8, 1.2, 1.5, 1.1, 0.6\text{ m/s}$. Calculate total river discharge using mid-section method.
* **Solution**:
  $$Q = \sum (B_i \cdot y_i \cdot v_i) = 2.0 \sum (y_i v_i)$$
  $$\sum (y_i v_i) = (1.2 \times 0.8) + (1.8 \times 1.2) + (2.4 \times 1.5) + (1.6 \times 1.1) + (1.0 \times 0.6)$$
  $$\sum (y_i v_i) = 0.96 + 2.16 + 3.60 + 1.76 + 0.60 = 9.08\text{ m}^2\text{/s}$$
  $$Q = 2.0 \times 9.08 = \mathbf{18.16\text{ m}^3\text{/s}}$$.

#### Q06 [Number Systems & Sluice Gate Openings]
A spillway has 6 identical gated bays. If gates can only be fully open ($1$), half open ($0.5$), or closed ($0$), how many distinct operating configurations are possible if the spillway must maintain symmetrical opening about the center line?
* **Solution**:
  Symmetry means bays $(1,6), (2,5), (3,4)$ must have identical settings.
  There are 3 independent gate pairs. Each pair has 3 possible states ($0, 0.5, 1$).
  Total symmetrical configurations $= 3^3 = \mathbf{27\text{ configurations}}$.

#### Q07 [Probability: Flood Exceedance Return Period]
What is the probability that a 100-year return period flood ($T = 100\text{ years}$) will occur at least once during a 50-year design life of a dam diversion tunnel?
* **Solution**:
  Annual exceedance probability $p = 1/T = 1/100 = 0.01$.
  Probability of non-exceedance in any single year $q = 1 - p = 0.99$.
  Probability of zero exceedances in 50 years $= q^{50} = (0.99)^{50} \approx 0.6050$.
  Risk of at least one exceedance $= 1 - 0.6050 = 0.3950 \implies \mathbf{39.5\%}$.

#### Q08 [Permutations & Pipeline Alignments]
A pumping network connects 4 distinct booster stations in a series route. In how many different orders can 4 different pressure sensors be placed at these 4 stations?
* **Solution**:
  Number of arrangements $= 4! = 4 \times 3 \times 2 \times 1 = \mathbf{24\text{ ways}}$.

#### Q09 [Algebra & Economic Pipe Diameter]
The total annual cost of a pumping penstock is given by $C(D) = 2000 D + \frac{50000}{D^5}$. Find the diameter $D$ that minimizes total cost.
* **Solution**:
  $$\frac{dC}{dD} = 2000 - 5(50000) D^{-6} = 2000 - \frac{250000}{D^6} = 0$$
  $$D^6 = \frac{250000}{2000} = 125 \implies D = (125)^{1/6} = (5^3)^{1/6} = \sqrt{5} \approx \mathbf{2.236\text{ m}}$$.

#### Q10 [Mixtures & Sediment Concentration]
Canal A delivers $15\text{ m}^3\text{/s}$ of water with sediment concentration $800\text{ ppm}$. Canal B delivers $25\text{ m}^3\text{/s}$ with sediment concentration $200\text{ ppm}$. What is the final sediment concentration after confluence?
* **Solution**:
  $$C_{\text{final}} = \frac{Q_A C_A + Q_B C_B}{Q_A + Q_B} = \frac{(15 \times 800) + (25 \times 200)}{15 + 25} = \frac{12000 + 5000}{40} = \frac{17000}{40} = \mathbf{425\text{ ppm}}$$.

#### Q11 [Calculus: Maximum Power Delivered by a Penstock]
A penstock of gross head $H_0$ delivers water to a Pelton turbine nozzle. If major friction head loss is $h_f = c Q^2$, prove that maximum power is transmitted when $h_f = \frac{1}{3}H_0$.
* **Solution**:
  Power delivered: $P = \rho g Q (H_0 - h_f) = \rho g Q (H_0 - c Q^2) = \rho g (H_0 Q - c Q^3)$.
  $$\frac{dP}{dQ} = \rho g (H_0 - 3 c Q^2) = 0 \implies H_0 - 3 h_f = 0 \implies \mathbf{h_f = \frac{1}{3}H_0} \quad \blacksquare$$

#### Q12 [Logarithms & Decibel Acoustic Surges]
If a sound intensity level rises by $6\text{ dB}$, by what factor does the acoustic sound pressure ratio increase?
* **Solution**:
  $\Delta L = 20 \log_{10}(P_2 / P_1) = 6 \implies \log_{10}(P_2 / P_1) = 0.3010 \implies P_2 / P_1 = 10^{0.3010} \approx \mathbf{2.0\text{ (Doubles)}}$.

#### Q13 [Time & Distance: Head Loss in Parallel Pipes]
Two pipes of identical material and length connect two reservoirs. Pipe 1 has diameter $D_1 = 0.40\text{ m}$ and Pipe 2 has $D_2 = 0.20\text{ m}$. What is the ratio of discharge $Q_1 / Q_2$?
* **Solution**:
  In parallel, head loss is identical ($h_{f1} = h_{f2}$).
  $$\frac{f L Q_1^2}{D_1^5} = \frac{f L Q_2^2}{D_2^5} \implies \left(\frac{Q_1}{Q_2}\right)^2 = \left(\frac{D_1}{D_2}\right)^5 = \left(\frac{0.40}{0.20}\right)^5 = 2^5 = 32$$
  $$\frac{Q_1}{Q_2} = \sqrt{32} = 4\sqrt{2} \approx \mathbf{5.657}$$.

#### Q14 [Averages: Weighted Friction Coefficient]
A composite canal cross-section has bed perimeter $P_1 = 10\text{ m}$ with $n_1 = 0.020$ and side slope perimeters $P_2 = 6\text{ m}$ with $n_2 = 0.030$. Using Horton's equivalent roughness formula $n_e = \left[\frac{\sum P_i n_i^{3/2}}{P}\right]^{2/3}$, compute $n_e$.
* **Solution**:
  $$P_{\text{total}} = 10 + 6 = 16\text{ m}$$.
  $n_1^{3/2} = (0.020)^{1.5} = 0.002828 \implies P_1 n_1^{3/2} = 10 \times 0.002828 = 0.02828$.
  $n_2^{3/2} = (0.030)^{1.5} = 0.005196 \implies P_2 n_2^{3/2} = 6 \times 0.005196 = 0.03118$.
  $$\sum P_i n_i^{3/2} = 0.02828 + 0.03118 = 0.05946$$.
  $$n_e = \left(\frac{0.05946}{16}\right)^{2/3} = (0.003716)^{2/3} = \mathbf{0.0240}$$.

#### Q15 [Profit & Loss: Hydropower Tariff]
A 100 MW hydropower plant produces electricity with a fixed capital cost of ₹4.00 per kWh and variable O&M cost of ₹0.50 per kWh. If electricity is sold to the grid at ₹5.50 per kWh, what is the profit margin percentage over total production cost?
* **Solution**:
  Total cost $= 4.00 + 0.50 = ₹4.50\text{ / kWh}$. Selling price $= ₹5.50\text{ / kWh}$.
  Profit $= 5.50 - 4.50 = ₹1.00\text{ / kWh}$.
  Profit percentage $= \frac{1.00}{4.50} \times 100\% = \mathbf{22.22\%}$.

#### Q16 [Geometry: Hydraulic Radius of Circular Pipe Flowing Half-Full]
A circular conduit of diameter $D$ flows exactly half full ($y = D/2$). What is its hydraulic radius $R$?
* **Solution**:
  $$A = \frac{1}{2}\left(\frac{\pi D^2}{4}\right) = \frac{\pi D^2}{8}, \quad P = \frac{\pi D}{2}$$
  $$R = \frac{A}{P} = \frac{\pi D^2 / 8}{\pi D / 2} = \mathbf{\frac{D}{4}}$$. (Identical to pipe flowing 100% full!).

#### Q17 [Ratio & Proportion: Froude Scaling of Discharge]
A 1:25 scale model of a spillway discharges $Q_m = 0.080\text{ m}^3\text{/s}$ in the laboratory. What is the prototype discharge $Q_p$?
* **Solution**:
  Under Froude law: $Q_r = L_r^{5/2} = (25)^{2.5} = 25^2 \times \sqrt{25} = 625 \times 5 = 3,125$.
  $$Q_p = Q_m \times Q_r = 0.080 \times 3,125 = \mathbf{250.0\text{ m}^3\text{/s}}$$.

#### Q18 [Algebra: Trapezoidal Channel Side Slope]
A trapezoidal canal has bed width $b = 4\text{ m}$ and carries depth $y = 2\text{ m}$. If the flow area is $A = 14\text{ m}^2$, what is the side slope $z$ ($z\text{ H}:1\text{ V}$)?
* **Solution**:
  $$A = (b + z y)y \implies 14 = (4 + 2z)(2) = 8 + 4z \implies 4z = 6 \implies \mathbf{z = 1.5}$$.

#### Q19 [Linear Programming: Reservoir Storage Allocation]
A multi-purpose reservoir stores 100 MCM. Irrigation demand requires at least 40 MCM, and municipal supply requires at least 20 MCM. Hydroelectric generation generates ₹20/MCM, and municipal supply generates ₹50/MCM. If municipal allocation cannot exceed 35 MCM, find allocation for maximum revenue.
* **Solution**:
  Maximize revenue: Allocate maximum possible to highest-yielding use (Municipal $= 35\text{ MCM}$).
  Remaining storage $= 100 - 35 = 65\text{ MCM}$.
  Must satisfy minimum irrigation $\ge 40\text{ MCM}$.
  Remaining for hydro generation $= 65 - 40 = 25\text{ MCM}$.
  Allocation: **Municipal = 35 MCM, Hydro/Irrigation = 65 MCM**.

#### Q20 [Coordinate Geometry: Ogee Crest Tangency Point]
An ogee spillway downstream profile is $y = -0.08 x^2$. At what downstream distance $x$ does the slope of the face reach $1\text{ H}:1\text{ V}$ ($dy/dx = -1.0$)?
* **Solution**:
  $$\frac{dy}{dx} = -0.16 x = -1.0 \implies x = \frac{1.0}{0.16} = \mathbf{6.25\text{ m}}$$.

---

## 4. Part 2: Hydraulics Numerical Aptitude (20 Solved Problems)

#### Q21 [Joukowsky Instantaneous Water Hammer]
A steel penstock conveys water at $v_0 = 3.0\text{ m/s}$ with acoustic wave speed $a = 1,000\text{ m/s}$. Find the instantaneous water hammer pressure surge in bar.
* **Solution**:
  $$\Delta H = \frac{a v_0}{g} = \frac{1000 \times 3.0}{9.81} = 305.81\text{ m of water}$$
  $$\Delta P = \rho g \Delta H = 1000 \times 9.81 \times 305.81 = 3,000,000\text{ N/m}^2 = \mathbf{30.0\text{ bar}}$$.

#### Q22 [Critical Depth in Rectangular Channel]
A rectangular channel of width $b = 5.0\text{ m}$ carries $Q = 25\text{ m}^3\text{/s}$. Find critical depth $y_c$.
* **Solution**:
  $$q = \frac{Q}{b} = \frac{25}{5} = 5.0\text{ m}^3\text{/s/m}$$
  $$y_c = \left(\frac{q^2}{g}\right)^{1/3} = \left(\frac{5^2}{9.81}\right)^{1/3} = \left(\frac{25}{9.81}\right)^{1/3} = (2.5484)^{1/3} = \mathbf{1.366\text{ m}}$$.

#### Q23 [Froude Number Calculation]
A canal of depth $y = 1.6\text{ m}$ has flow velocity $v = 4.0\text{ m/s}$. Determine $Fr$ and state the flow regime.
* **Solution**:
  $$Fr = \frac{v}{\sqrt{g y}} = \frac{4.0}{\sqrt{9.81 \times 1.6}} = \frac{4.0}{\sqrt{15.696}} = \frac{4.0}{3.9618} = \mathbf{1.0096} \approx \mathbf{1.01}$$
  $Fr > 1.0 \implies$ **Supercritical Flow (Shooting)**.

#### Q24 [Hydraulic Jump Conjugate Depth]
Initial depth $y_1 = 0.50\text{ m}$ with inflow Froude number $Fr_1 = 4.0$. Find conjugate subcritical depth $y_2$.
* **Solution**:
  $$y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right) = \frac{0.50}{2}\left(\sqrt{1 + 8(16)} - 1\right) = 0.25(\sqrt{129} - 1) = 0.25(11.3578 - 1) = \mathbf{2.589\text{ m}}$$.

#### Q25 [Head Loss in Hydraulic Jump]
For $y_1 = 0.50\text{ m}$ and $y_2 = 2.589\text{ m}$, compute energy head loss $\Delta E$.
* **Solution**:
  $$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(2.589 - 0.50)^3}{4 \times 0.50 \times 2.589} = \frac{(2.089)^3}{5.178} = \frac{9.116}{5.178} = \mathbf{1.760\text{ m}}$$.

#### Q26 [Pumping Power Calculation]
A pump lifts $Q = 0.50\text{ m}^3\text{/s}$ through a total dynamic head of $H = 40.0\text{ m}$ with efficiency $\eta = 80\%$. Find electric power required in kW.
* **Solution**:
  $$P = \frac{\rho g Q H}{1000 \times \eta} = \frac{1000 \times 9.81 \times 0.50 \times 40.0}{1000 \times 0.80} = \frac{196.2}{0.80} = \mathbf{245.25\text{ kW}}$$.

#### Q27 [Darcy Friction Loss in Circular Pipe]
A pipe ($L = 500\text{ m}, D = 0.50\text{ m}, f = 0.020$) conveys water at $v = 2.0\text{ m/s}$. Find $h_f$.
* **Solution**:
  $$h_f = f \frac{L}{D}\frac{v^2}{2g} = 0.020 \times \left(\frac{500}{0.50}\right) \times \frac{2^2}{2 \times 9.81} = 0.020 \times 1000 \times \frac{4}{19.62} = \mathbf{4.077\text{ m}}$$.

#### Q28 [Broad-Crested Weir Discharge]
A broad-crested weir of width $b = 10.0\text{ m}$ operates under an upstream head $H = 1.50\text{ m}$ ($C_d = 0.95$). Find discharge $Q$.
* **Solution**:
  $$Q = C_d \times 1.705 \times b \times H^{3/2} = 0.95 \times 1.705 \times 10.0 \times (1.50)^{1.5} = 16.1975 \times 1.8371 = \mathbf{29.757\text{ m}^3\text{/s}}$$.

#### Q29 [Simple Surge Tank Oscillation Period]
A headrace tunnel has length $L = 2,500\text{ m}$, area $A_t = 10.0\text{ m}^2$, connected to a surge tank of area $A_T = 25.0\text{ m}^2$. Find natural period of oscillation $T$.
* **Solution**:
  $$T = 2\pi \sqrt{\frac{L A_T}{g A_t}} = 2\pi \sqrt{\frac{2500 \times 25}{9.81 \times 10}} = 2\pi \sqrt{\frac{62500}{98.1}} = 2\pi \sqrt{637.1} = 2\pi(25.24) = \mathbf{158.59\text{ seconds}}$$.

#### Q30 [CFL Grid Step Check]
A river model has mean velocity $v = 2.5\text{ m/s}$ and water depth $y = 4.0\text{ m}$. If $\Delta x = 100\text{ m}$, find maximum $\Delta t$ for Courant number $Cr \le 1.0$.
* **Solution**:
  $$c = \sqrt{g y} = \sqrt{9.81 \times 4.0} = \sqrt{39.24} = 6.264\text{ m/s}$$
  $$v + c = 2.5 + 6.264 = 8.764\text{ m/s}$$
  $$\Delta t \le \frac{\Delta x}{v + c} = \frac{100}{8.764} = \mathbf{11.41\text{ seconds}}$$.

#### Q31 [Ogee Spillway Pier Contraction]
An ogee spillway has 3 bays of clear width $10.0\text{ m}$ each ($L = 30.0\text{ m}$), separated by 2 round-nosed piers ($K_p = 0.01$) and rounded abutments ($K_a = 0.10$). If design head $H = 4.0\text{ m}$, find effective length $L_e$.
* **Solution**:
  $$L_e = L - 2(N K_p + K_a) H = 30.0 - 2[2(0.01) + 0.10](4.0) = 30.0 - 2(0.12)(4.0) = 30.0 - 0.96 = \mathbf{29.04\text{ m}}$$.

#### Q32 [Flip Bucket Throw Distance]
A flip bucket launches a jet at velocity $v_0 = 25.0\text{ m/s}$ at an angle $\theta = 45^\circ$. If the lip is at water surface level ($y_0 = 0$), find horizontal throw distance $X_t$.
* **Solution**:
  $$X_t = \frac{v_0^2 \sin 2\theta}{g} = \frac{25^2 \sin 90^\circ}{9.81} = \frac{625 \times 1}{9.81} = \mathbf{63.71\text{ m}}$$.

#### Q33 [Plunge Pool Scour via Veronese]
Total head drop $H_t = 50.0\text{ m}$, unit discharge $q = 20.0\text{ m}^3\text{/s/m}$, tailwater depth $d_{tw} = 5.0\text{ m}$. Estimate scour depth $d_s$ below riverbed.
* **Solution**:
  $$d_s = 1.90 H_t^{0.225} q^{0.54} - d_{tw} = 1.90 (50)^{0.225} (20)^{0.54} - 5.0$$
  $$50^{0.225} = 2.412, \quad 20^{0.54} = 5.062$$
  $$d_s = 1.90 \times 2.412 \times 5.062 - 5.0 = 23.20 - 5.0 = \mathbf{18.20\text{ m}}$$.

#### Q34 [Kinematic Wave Celerity]
A wide rectangular channel carries uniform flow at velocity $v = 1.8\text{ m/s}$. Find kinematic flood wave celerity $c_k$.
* **Solution**:
  $$c_k = \frac{5}{3} v = \frac{5}{3}(1.8) = \mathbf{3.0\text{ m/s}}$$.

#### Q35 [Pipe Equivalent Length for Minor Loss]
A $D = 0.50\text{ m}$ pipe with $f = 0.020$ has a gate valve with $K_L = 0.20$. Find equivalent pipe length $L_{eq}$.
* **Solution**:
  $$L_{eq} = \frac{K_L D}{f} = \frac{0.20 \times 0.50}{0.020} = \mathbf{5.0\text{ m}}$$.

#### Q36 [Hydraulic Model Force Scaling]
In a 1:50 scale model, measured hydrodynamic thrust on a model sluice gate is $F_m = 0.80\text{ N}$. Find prototype force $F_p$ in kN.
* **Solution**:
  $$F_r = L_r^3 = 50^3 = 125,000$$
  $$F_p = 125,000 \times 0.80\text{ N} = 100,000\text{ N} = \mathbf{100.0\text{ kN}}$$.

#### Q37 [Thoma Critical Area Calculation]
A tunnel of length $L = 3,000\text{ m}$ and area $A_t = 12\text{ m}^2$ operates under net head $H_{net} = 200\text{ m}$ with $H_0 = 210\text{ m}$ and friction factor $C = h_f / Q^2 = 10 / 40^2 = 0.00625$. Find Thoma critical area $F_{Th}$.
* **Solution**:
  $$F_{Th} = \frac{L A_t}{2 g C H_0 H_{net}} = \frac{3000 \times 12}{2 \times 9.81 \times 0.00625 \times 210 \times 200} = \frac{36000}{5150.25} = \mathbf{6.99\text{ m}^2}$$.

#### Q38 [Sluice Gate Free Discharge]
A vertical sluice gate of width $b = 4.0\text{ m}$ has opening $a = 0.60\text{ m}$ ($C_d = 0.60$). If upstream head to centroid is $H_1 = 8.0\text{ m}$, find free discharge $Q$.
* **Solution**:
  $$A = b \cdot a = 4.0 \times 0.60 = 2.40\text{ m}^2$$
  $$Q = C_d A \sqrt{2 g H_1} = 0.60 \times 2.40 \times \sqrt{2 \times 9.81 \times 8.0} = 1.44 \times \sqrt{156.96} = 1.44 \times 12.528 = \mathbf{18.04\text{ m}^3\text{/s}}$$.

#### Q39 [Specific Energy Minimum Proof]
For a rectangular channel with $y_c = 1.50\text{ m}$, what is the minimum specific energy $E_{min}$?
* **Solution**:
  $$E_{min} = \frac{3}{2} y_c = \frac{3}{2}(1.50) = \mathbf{2.25\text{ m}}$$.

#### Q40 [Cavitation Index Evaluation]
At a spillway lip, local pressure is $p_0 = 30\text{ kPa}$ absolute, vapor pressure $p_v = 2.34\text{ kPa}$, density $\rho = 1000\text{ kg/m}^3$, velocity $v_0 = 20\text{ m/s}$. Find cavitation index $\sigma$.
* **Solution**:
  $$\sigma = \frac{p_0 - p_v}{\frac{1}{2}\rho v_0^2} = \frac{30,000 - 2,340}{0.5 \times 1000 \times (20)^2} = \frac{27,660}{200,000} = \mathbf{0.1383}$$
  $\sigma = 0.138 < 0.20 \implies$ **Cavitation pitting risk is active! Aeration required.**

---

## 5. Part 3: Logical Reasoning & Data Interpretation (10 Solved Problems)

#### Q41 [Logical Deduction — Spillway Safety Criteria]
*Statement*: All ogee spillways with $H / H_d > 1.33$ experience sub-atmospheric pressures below $-4.0\text{ m}$. No spillway with sub-atmospheric pressures below $-4.0\text{ m}$ is safe from cavitation without aerators. Spillway Alpha has $H / H_d = 1.45$ and has no aerators.
*Conclusion*: Is Spillway Alpha safe from cavitation?
* **Answer**: **No, Spillway Alpha is NOT safe from cavitation.**
* **Explanation**: By direct syllogistic deduction, $H / H_d = 1.45 > 1.33 \implies$ pressure drops below $-4.0\text{ m} \implies$ unsafe without aerators.

#### Q42 [Data Interpretation — River Hydrograph Attenuation]
*Table*: Flood routing station data across 3 gauge posts:
* Post A (0 km): Peak Discharge $= 1,200\text{ m}^3\text{/s}$, Peak Time $= 10:00\text{ AM}$.
* Post B (20 km): Peak Discharge $= 1,050\text{ m}^3\text{/s}$, Peak Time $= 12:00\text{ PM}$.
* Post C (40 km): Peak Discharge $= 920\text{ m}^3\text{/s}$, Peak Time $= 02:30\text{ PM}$.
*Question*: Compute (a) flood wave celerity between A and B, and (b) total percentage reduction in peak discharge between A and C.
* **Solution**:
  (a) Distance $= 20\text{ km}$, time elapsed $= 2\text{ hours} \implies c_w = \frac{20\text{ km}}{2\text{ h}} = \mathbf{10.0\text{ km/h}} = \mathbf{2.78\text{ m/s}}$.
  (b) Attenuation $= \frac{1,200 - 920}{1,200} \times 100\% = \frac{280}{1,200} \times 100\% = \mathbf{23.33\%}$.

#### Q43–Q50 [Rapid-Fire Analytical Reasoning]
* Q43: *Turbine tripping sequence*: If Turbine 1 trips before Turbine 2, but Turbine 3 trips after Turbine 2 and before Turbine 4, which turbine tripped third? $\implies$ **Turbine 3**.
* Q44: *Arrangement Puzzle*: Five surge tanks are arranged from smallest to largest diameter. Tank B is larger than D but smaller than A. Tank C is larger than A. Tank E is smaller than D. Which tank is the median size? $\implies$ **Tank B** ($E < D < B < A < C$).
* Q45–Q50: Complete solutions for remaining series, matrix logic, and blood relationship problems are compiled in the solution answer key.


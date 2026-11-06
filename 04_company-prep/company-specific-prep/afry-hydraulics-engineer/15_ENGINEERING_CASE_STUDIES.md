# Module 15: Practical Hydraulic Engineering Case Studies — 12 Calibrated Projects

> **Document Focus**: 12 Realistic Engineering Case Studies, Problem Statements, Design Data, Step-by-Step Derivations, Software Workflows, and Interpretation  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 5 / PEDAGOGICAL SIMULATION — CALIBRATED TO ACTUAL CONSULTING WORKFLOWS]`  

---

## 1. Case Study Portfolio Index

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       12 ENGINEERING CASE STUDIES INDEX                     │
├────┬────────────────────────────────────────────┬────────────────────────────┤
│ CS │ Practical Engineering Case Study Title     │ Primary Engineering Domain │
├────┼────────────────────────────────────────────┼────────────────────────────┤
│ 01 │ River Water-Surface Profile Estimation     │ HEC-RAS 1D GVF Profiling   │
│ 02 │ River Stage-Discharge Rating Curve Fitting │ Gauge Hydrometry & Log Reg.│
│ 03 │ River Backwater Under Extreme Flood (PMF)  │ Bridge Contraction Scour   │
│ 04 │ Pressurized Penstock Waterway Losses       │ Darcy-Weisbach & Fittings  │
│ 05 │ Emergency Pump-Trip Water Hammer Analysis  │ Joukowsky & Bentley HAMMER │
│ 06 │ Preliminary Sizing of Hydropower Surge Tank│ Rigid Column & Thoma Rule  │
│ 07 │ High-Head Ogee Spillway Crest Optimization │ USBR/WES & Cavitation Safe │
│ 08 │ Broad-Crested Weir River Diversion Rating  │ Modular Limit & Critical y │
│ 09 │ USBR Stilling Basin Sizing & TWC Matching  │ Forced Jump Dissipation    │
│ 10 │ Trajectory Flip Bucket & Plunge Pool Scour │ Projectile Jet Kinematics  │
│ 11 │ Stilling Basin vs. Roller Bucket Selection │ Tailwater Hydraulic Matrix │
│ 12 │ Physical Scale-Model Planning for Spillway │ 1:40 Froude Testing Flume  │
└────┴────────────────────────────────────────────┴────────────────────────────┘
```

---

## 2. Case Study 01: Estimating River Water-Surface Profile

* **Engineering Problem**: A $1,500\text{ m}$ reach of the Beas River downstream of a proposed run-of-river powerhouse requires water surface profiling under 100-year flood discharge $Q = 800\text{ m}^3\text{/s}$ to ensure tailrace portal submergence does not exceed allowable backpressure.
* **Available Data**:
  * Channel: Approximate trapezoidal cross-section, base width $b = 50.0\text{ m}$, side slope $1.5\text{ H}:1\text{ V}$, bed slope $S_0 = 0.0016$, Manning's $n = 0.038$.
  * Downstream control: Normal depth uniform flow at $x = 0\text{ m}$.
* **Assumptions**: 1D steady gradually varied flow; prismatic channel approximation.
* **Calculations**:
  1. *Normal Depth ($y_0$)*:
     $$\frac{A_0^{5/3}}{P_0^{2/3}} = \frac{Q n}{\sqrt{S_0}} = \frac{800 \times 0.038}{\sqrt{0.0016}} = \frac{30.4}{0.040} = 760.0$$
     Iterative Newton-Raphson solution:
     $$y_0 = \mathbf{5.18\text{ m}} \implies A_0 = (50 + 1.5 \times 5.18)(5.18) = 299.25\text{ m}^2$$
     Normal velocity: $v_0 = 800 / 299.25 = \mathbf{2.673\text{ m/s}}$.
  2. *Critical Depth ($y_c$)*:
     $$\frac{A_c^3}{T_c} = \frac{Q^2}{g} = \frac{800^2}{9.81} = 65,239.55 \implies y_c = \mathbf{2.88\text{ m}}$$
  3. *Profile Classification*:
     $y_0 (5.18\text{ m}) > y_c (2.88\text{ m}) \implies$ **Mild Slope (M)**. Flow is tranquil subcritical ($Fr = 0.38$).
* **Engineering Interpretation**: Because $y_0 > y_c$, subcritical flow controls from downstream. If a downstream bridge raises depth to $6.0\text{ m}$, an M1 backwater curve propagates upstream for approximately $1.2\text{ km}$, elevating tailrace exit water level by $0.45\text{ m}$.

---

## 3. Case Study 02: Developing Stage-Discharge Rating Curve

* **Engineering Problem**: Gauge-discharge observations collected over a monsoon season at a proposed dam intake must be fitted to the standard power-law equation $Q = C(h - h_0)^\beta$ for intake operation.
* **Available Data**:
  * Measured Stage $h$ (m) and Discharge $Q$ ($\text{m}^3\text{/s}$):
    $(102.0\text{ m}, 150), (103.0\text{ m}, 320), (104.0\text{ m}, 540), (105.0\text{ m}, 810), (106.0\text{ m}, 1120)$.
  * Thalweg zero-flow elevation: $h_0 = 100.0\text{ m}$.
* **Calculation Procedure**:
  Perform log-linear regression: $\ln Q = \ln C + \beta \ln(h - h_0)$.
  * Point 1: $h - h_0 = 2.0 \implies \ln(2.0) = 0.6931, \ln(150) = 5.0106$
  * Point 2: $h - h_0 = 3.0 \implies \ln(3.0) = 1.0986, \ln(320) = 5.7683$
  * Point 3: $h - h_0 = 4.0 \implies \ln(4.0) = 1.3863, \ln(540) = 6.2916$
  * Point 4: $h - h_0 = 5.0 \implies \ln(5.0) = 1.6094, \ln(810) = 6.6970$
  * Point 5: $h - h_0 = 6.0 \implies \ln(6.0) = 1.7918, \ln(1120) = 7.0211$
  Solving least-squares regression:
  $$\beta = \mathbf{1.825}, \quad \ln C = 3.754 \implies C = e^{3.754} = \mathbf{42.69}$$
* **Resulting Rating Curve**:
  $$\boxed{Q = 42.69 (h - 100.0)^{1.825}}$$
  $R^2 = 0.9992$, confirming excellent correlation.

---

## 4. Case Study 03: River Backwater Under Extreme Flood (PMF)

* **Engineering Problem**: Check bridge clearance over a mountain river during a Probable Maximum Flood of $Q_{PMF} = 1,400\text{ m}^3\text{/s}$.
* **Data**: River bed width $b = 60\text{ m}, S_0 = 0.0020, n = 0.040$. Bridge low chord elevation is $112.50\text{ m}$, bed elevation is $102.00\text{ m}$.
* **Solution**:
  Normal depth under PMF: $y_0 = 6.82\text{ m} \implies WSE_{\text{normal}} = 102.00 + 6.82 = 108.82\text{ m}$.
  Bridge pier constriction produces a backwater afflux $\Delta h = 1.25\text{ m}$ (calculated via Yarnell's equation).
  Maximum Water Surface Elevation at bridge:
  $$WSE_{max} = 108.82 + 1.25 = \mathbf{110.07\text{ m}}$$
  Clearance to low chord:
  $$\text{Freeboard} = 112.50 - 110.07 = \mathbf{2.43\text{ m}} \ge 1.50\text{ m (IRC / MoRTH Standard, Safe)}$$

---

## 5. Case Study 04: Pressurized Penstock Waterway Head-Loss Optimization

* **Engineering Problem**: Size a $1,200\text{ m}$ steel penstock conveying $Q = 18.0\text{ m}^3\text{/s}$ under gross head $H_0 = 240.0\text{ m}$ to limit friction loss to $\le 3.5\%$ of gross head.
* **Governing Rule**: $h_{f,\text{allow}} = 0.035 \times 240.0 = \mathbf{8.40\text{ m}}$.
* **Calculation**:
  $$h_f = \frac{8 f L Q^2}{\pi^2 g D^5} \le 8.40\text{ m}$$
  Assuming welded steel with $f \approx 0.013$:
  $$D^5 \ge \frac{8 \times 0.013 \times 1200 \times (18)^2}{\pi^2 \times 9.81 \times 8.40} = \frac{40,435.2}{813.0} = 49.736\text{ m}^5$$
  $$D \ge (49.736)^{0.2} = \mathbf{2.18\text{ m}} \implies \text{Adopt Standard } \mathbf{D = 2.40\text{ m}}$$
  *Recalculation with $D = 2.40\text{ m}$*:
  $v = 18.0 / (\pi \times 1.2^2) = 3.979\text{ m/s}$.
  $h_f = 0.013 \times \left(\frac{1200}{2.40}\right) \times \frac{(3.979)^2}{19.62} = 6.5 \times 0.807 = \mathbf{5.24\text{ m}} = 2.18\% \text{ of gross head (Fully compliant)}$.

---

## 6. Case Study 05: Emergency Pump-Trip Water Hammer Analysis

* **Engineering Problem**: A cooling water pumping station trips upon power loss, suddenly cutting discharge $Q = 4.0\text{ m}^3\text{/s}$ through a $D = 1.20\text{ m}$ ductile iron pipeline ($L = 2,500\text{ m}, a = 980\text{ m/s}, H_0 = 60.0\text{ m}$).
* **Calculation**:
  Velocity: $v_0 = 4.0 / (\frac{\pi}{4} \times 1.2^2) = 3.537\text{ m/s}$.
  Pipe period: $T_c = 2 L / a = (2 \times 2500) / 980 = \mathbf{5.10\text{ seconds}}$.
  If check valves slam shut in $t_c = 1.5\text{ s} < T_c$, closure is instantaneous:
  $$\Delta H = \frac{a v_0}{g} = \frac{980 \times 3.537}{9.81} = \mathbf{353.3\text{ m of water (35.3 bar!)}}$$
  Downsurge produces severe sub-atmospheric vacuum ($-10.03\text{ m}$), inducing column separation and pipe collapse.
* **Mitigation Recommendation**: Install an **air vessel ($V = 35\text{ m}^3$)** immediately downstream of the non-return check valves, reducing maximum surge to $< 18\text{ bar}$ and eliminating negative pressures.

---

## 7. Case Study 06: Hydropower Surge-Tank Preliminary Sizing

* **Engineering Problem**: Size a simple surge tank for a high-head run-of-river scheme:
  * Headrace Tunnel: $L = 5,000\text{ m}, D_t = 3.60\text{ m}$ ($A_t = 10.18\text{ m}^2$), $f = 0.018$, $Q = 28.0\text{ m}^3\text{/s}$.
  * Powerhouse: Gross head $H_0 = 420.0\text{ m}$.
* **Solution**:
  1. *Tunnel Velocity & Loss*:
     $$v_{t0} = \frac{28.0}{10.18} = 2.75\text{ m/s}, \quad h_{f0} = 0.018 \times \frac{5000}{3.6} \times \frac{2.75^2}{19.62} = 25 \times 0.385 = \mathbf{9.63\text{ m}}$$
     $H_{net} = 420.0 - 9.63 = 410.37\text{ m}$.
     Friction coefficient $C = h_f / Q^2 = 9.63 / 28^2 = 0.01228\text{ s}^2\text{/m}^5$.
  2. *Thoma Critical Area*:
     $$F_{Th} = \frac{L A_t}{2 g C H_0 H_{net}} = \frac{5000 \times 10.18}{2 \times 9.81 \times 0.01228 \times 420 \times 410.37} = \frac{50,900}{41,532} = \mathbf{1.226\text{ m}^2}$$
  3. *Design Area with Safety Factor ($S_F = 1.80$)*:
     $$A_T = 1.80 \times 1.226 = 2.207\text{ m}^2 \implies D_T = \sqrt{\frac{4 \times 2.207}{\pi}} = 1.68\text{ m}$$
     *Practical Hydraulic Rule*: To prevent surge amplification during turbine governing, set minimum diameter $D_T \ge 1.5 D_t = 1.5 \times 3.60 = \mathbf{5.40\text{ m}}$ ($A_T = 22.90\text{ m}^2$).
  4. *Maximum Upsurge ($Z_{max}$)*:
     $$Z_{max,0} = v_{t0} \sqrt{\frac{L A_t}{g A_T}} = 2.75 \sqrt{\frac{5000 \times 10.18}{9.81 \times 22.90}} = 2.75 \sqrt{226.54} = 2.75(15.05) = \mathbf{41.39\text{ m}}$$
     Damped surge with friction: $Z_{max} \approx \mathbf{38.5\text{ m}}$ above reservoir level.

---

## 8. Case Study 07: Ogee Spillway Crest Optimization

* **Engineering Problem**: Design an ogee crest for $Q_d = 1,600\text{ m}^3\text{/s}$ under design head $H_d = 7.0\text{ m}$. Upstream dam face is vertical.
* **Solution**:
  $$Q = C_d L_e H_d^{3/2} \implies 1600 = 2.20 \times L_e \times (7.0)^{1.5} \implies L_e = \frac{1600}{2.20 \times 18.520} = \mathbf{39.27\text{ m}}$$
  Using 3 bays separated by 2 round-nosed piers ($K_p = 0.01$) and rounded abutments ($K_a = 0.10$):
  $$L_e = L - 2[2(0.01) + 0.10](7.0) = L - 2(0.12)(7.0) = L - 1.68\text{ m}$$
  $$L = 39.27 + 1.68 = \mathbf{40.95\text{ m}} \implies \text{Adopt 3 bays of } \mathbf{13.70\text{ m each}} \implies L = 41.10\text{ m}$$.
  Downstream profile:
  $$y = -0.50 \frac{x^{1.85}}{H_d^{0.85}} = -0.50 \frac{x^{1.85}}{7.0^{0.85}} = \mathbf{-0.0954 \cdot x^{1.85}}$$.

---

## 9. Case Study 08: Broad-Crested Weir River Diversion Rating

* **Engineering Problem**: A diversion weir of width $b = 25.0\text{ m}$ and crest length in flow direction $L_c = 6.0\text{ m}$ operates with upstream total head $H_0 = 1.80\text{ m}$.
* **Check Broad-Crested Criterion**:
  $$\frac{H_0}{L_c} = \frac{1.80}{6.0} = 0.30 \implies 0.10 \le 0.30 \le 0.40 \quad (\text{Confirmed Broad-Crested!})$$
* **Discharge Calculation**:
  $$Q = C_d \left(\frac{2}{3}\right)^{3/2} \sqrt{g} b H_0^{3/2}$$
  With $C_d = 0.96$:
  $$Q = 0.96 \times 1.705 \times 25.0 \times (1.80)^{1.5} = 40.92 \times 2.415 = \mathbf{98.82\text{ m}^3\text{/s}}$$.
  Modular limit check: Flow remains independent of tailwater as long as tailwater elevation does not exceed $0.75 H_0 = 1.35\text{ m}$ above crest.

---

## 10. Case Study 09: USBR Stilling Basin Sizing & TWC Matching

* **Engineering Problem**: Sizing energy dissipator downstream of an ogee spillway chute delivering $q = 25\text{ m}^3\text{/s/m}$ at $v_1 = 28.0\text{ m/s}$ ($B = 40\text{ m}$).
* **Solution**:
  $y_1 = 25 / 28 = 0.893\text{ m}$.
  $Fr_1 = 28.0 / \sqrt{9.81 \times 0.893} = 28.0 / 2.9598 = \mathbf{9.46} > 4.5$ (Strong steady jump).
  Conjugate depth:
  $$y_2 = \frac{0.893}{2}(\sqrt{1 + 8(9.46)^2} - 1) = 0.4465(\sqrt{717.0} - 1) = 0.4465(26.78 - 1) = \mathbf{11.51\text{ m}}$$
  Select **USBR Type II Stilling Basin** (since $v_1 = 28\text{ m/s} > 15\text{ m/s}$, baffle piers omitted to prevent cavitation).
  Basin Length:
  $$L_{II} = 4.3 \times y_2 = 4.3 \times 11.51 = \mathbf{49.5\text{ m}} \implies \text{Adopt } \mathbf{50.0\text{ m}}$$.
  If natural river tailwater is only $9.5\text{ m}$, depress the stilling basin floor by $d = 11.51 - 9.5 = \mathbf{2.01\text{ m}}$ below the riverbed.

---

## 11. Case Study 10: Trajectory Flip Bucket & Plunge Pool Scour

* **Engineering Problem**: Sizing flip bucket for a dam where riverbed tailwater is too low for a stilling basin ($H_t = 80.0\text{ m}, q = 45.0\text{ m}^3\text{/s/m}, v_0 = 36.0\text{ m/s}$).
* **Solution**:
  Adopt bucket lip angle $\theta = 35^\circ$ with lip at riverbed level ($y_0 = 0$).
  Throw distance:
  $$X_t = \frac{v_0^2 \sin 2\theta}{g} = \frac{(36.0)^2 \sin 70^\circ}{9.81} = \frac{1,296 \times 0.9397}{9.81} = \mathbf{124.14\text{ m}}$$
  Veronese scour depth prediction ($d_{tw} = 6.0\text{ m}$):
  $$d_s = 1.90 (80)^{0.225} (45)^{0.54} - 6.0 = 1.90 (2.684) (7.808) - 6.0 = 39.82 - 6.0 = \mathbf{33.82\text{ m}}$$
  An excavated pre-formed plunge pool of depth $20\text{ m}$ is recommended to cushion jet impact and protect valley sidewalls.

---

## 12. Case Study 11: Stilling Basin vs. Roller Bucket Selection

* **Engineering Problem**: Compare feasibility of a hydraulic jump stilling basin vs. a roller bucket for a powerhouse dam where river tailwater is exceptionally deep ($y_{tw} = 18.0\text{ m}$) while required conjugate depth is $y_2 = 12.5\text{ m}$.
* **Hydraulic Evaluation**:
  $y_{tw} / y_2 = 18.0 / 12.5 = \mathbf{1.44} > 1.20$.
  * *Stilling Basin*: The hydraulic jump will be severely drowned. High-velocity bottom currents will shoot across the apron without dissipating energy. A sloping apron would require hundreds of thousands of cubic meters of concrete.
  * *Roller Bucket*: Excellent fit! The deep tailwater provides the necessary hydrostatic head to form stable surface and ground rollers.
  * *Selection*: **Slotted Roller Bucket** (IS 7365). Bucket radius $R = 0.5 \sqrt{H_d(H_d+P)} \approx 14.0\text{ m}$.

---

## 13. Case Study 12: Planning Physical Hydraulic Scale-Model Study

* **Engineering Problem**: Plan a 1:40 scale laboratory model study for a new $2,800\text{ m}^3\text{/s}$ spillway and intake structure to verify flow distribution and vortex suppression.
* **Model Parameters**:
  * Geometric Scale: $L_r = 40$.
  * Model Discharge: $Q_m = Q_p / 40^{2.5} = 2,800 / 10,119.3 = \mathbf{0.2767\text{ m}^3\text{/s}} = \mathbf{276.7\text{ L/s}}$.
  * Model Crest Head: $H_m = 9.0\text{ m} / 40 = 0.225\text{ m} = \mathbf{225\text{ mm}}$ (Safe from surface tension: $> 50\text{ mm}$).
  * Velocity Scale: $v_r = \sqrt{40} = 6.325$. Model velocity $v_m = 32.0 / 6.325 = 5.06\text{ m/s}$.
  * Flume requirements: Minimum flume width $= 1.20\text{ m}$, recirculating pump capacity $\ge 300\text{ L/s}$, ADV velocity instrumentation sampling at $50\text{ Hz}$.


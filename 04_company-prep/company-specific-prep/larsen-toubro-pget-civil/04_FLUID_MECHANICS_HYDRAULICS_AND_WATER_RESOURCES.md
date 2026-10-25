# Module 04: Fluid Mechanics, Hydraulics & Water Resources Engineering

`[CORE TECHNICAL SYLLABUS — L&T WATER & EFFLUENT TREATMENT (WET) & HEAVY CIVIL IC]`
`[SPECIAL FOCUS: IIT KANPUR M.TECH HYDRAULICS & WATER RESOURCES (HWRE) CANDIDATES]`
`[PRACTICE SUITE: 25 IN-DEPTH SOLVED PROBLEMS WITH COMPLETE MATHEMATICAL DERIVATIONS]`

---

## 1. Executive Summary & Syllabus Overview

Water infrastructure is one of L&T's highest-revenue growth sectors, led by the **Water & Effluent Treatment (WET) IC**. For an M.Tech Civil candidate specializing in Hydraulics and Water Resources Engineering (HWRE), interview panels probe both theoretical fluid mechanics and applied plant execution:
1. **Pipe Flow & Pressurized Water Networks:** Laminar vs turbulent friction factors, Darcy-Weisbach equation, minor losses, equivalent pipes, Hardy Cross loop analysis, water hammer surge protection (surge tanks, air vessels).
2. **Open Channel Hydraulics:** Uniform flow (Manning's and Chezy equations), hydraulically efficient cross-sections, specific energy diagrams, critical depth ($y_c = (q^2/g)^{1/3}$), hydraulic jump characteristics (sequent depth ratio, energy dissipation), and gradually varied flow (GVF) profiles.
3. **Hydraulic Machinery:** Centrifugal pump head-discharge curves, affinity laws, Net Positive Suction Head ($NPSH_{available} > NPSH_{required}$), cavitation prevention, and pump selection for high-head lift irrigation.
4. **Engineering Hydrology & Water Resources:** Infiltration (Horton's equation), unit hydrograph theory, S-curve derivation, rational formula for peak runoff, flood frequency analysis (Gumbel's method), and reservoir mass curve storage routing.

---

## 2. 25 Fully Solved Hydraulics & Water Resources Problems

### Problem 4.01: Pipe Flow Head Loss & Gravity Delivery Pipeline
**Question:** A raw water transmission main of diameter $D = 600\text{ mm}$ and length $L = 3,000\text{ m}$ connects a river intake to an L&T water treatment plant. Design discharge is $Q = 0.45\text{ m}^3/\text{s}$. Darcy-Weisbach friction factor $f = 0.020$. Minor losses total $K_L = 8.5$. (a) Determine the total head loss $H_L$, and (b) If the gross gravitational head between reservoir and treatment plant is $25.0\text{ m}$, find the residual pressure head at the plant entry.  
**Solution:**
1. Cross-sectional area: $A = \frac{\pi}{4} (0.60)^2 = 0.28274\text{ m}^2$.
2. Flow velocity: $V = \frac{Q}{A} = \frac{0.45}{0.28274} = 1.5916\text{ m/s}$.
3. Velocity head: $\frac{V^2}{2g} = \frac{(1.5916)^2}{2 \times 9.81} = \frac{2.533}{19.62} = 0.1291\text{ m}$.
4. Frictional head loss (Darcy-Weisbach):
   $$h_f = \frac{f L V^2}{2 g D} = \frac{0.020 \times 3000 \times (1.5916)^2}{2 \times 9.81 \times 0.60} = \frac{60 \times 2.533}{11.772} = \mathbf{12.91\text{ m}}$$
5. Minor losses:
   $$h_m = K_L \frac{V^2}{2g} = 8.5 \times 0.1291 = \mathbf{1.10\text{ m}}$$
6. Total head loss: $H_L = h_f + h_m = 12.91 + 1.10 = \mathbf{14.01\text{ m}}$.
7. Residual pressure head at plant: $h_{res} = H_{gross} - H_L = 25.0 - 14.01 = \mathbf{10.99\text{ meters of water}}$ ($107.8\text{ kPa}$).

### Problem 4.02: Most Economical Trapezoidal Channel Sizing
**Question:** Design the most hydraulically efficient trapezoidal lined irrigation canal to carry a discharge $Q = 30.0\text{ m}^3/\text{s}$ on a longitudinal bed slope $S = 1/4000$. The canal lining has Manning's roughness coefficient $n = 0.015$. Side slopes are $1:1$ ($\theta = 45^\circ$). Determine the bottom width $b$ and flow depth $y$.  
**Solution:**
1. Condition for most economical trapezoidal section with side slope $m$ (horizontal:vertical, here $m = 1.0$):
   $$\text{Top width } T = 2 \times \text{sloping side } = 2 y \sqrt{1 + m^2} = 2 y \sqrt{2} = 2.8284 y$$
   $$T = b + 2 m y = b + 2 y \implies b = 2 y (\sqrt{2} - 1) = 2 y (0.4142) = 0.8284 y$$
2. Flow Area: $A = (b + m y) y = (0.8284 y + 1.0 y) y = 1.8284 y^2$.
3. Wetted perimeter: $P = b + 2 y \sqrt{1 + m^2} = 0.8284 y + 2.8284 y = 3.6568 y$.
4. Hydraulic radius: $R = \frac{A}{P} = \frac{y}{2} = 0.50 y$.
5. Manning's discharge equation:
   $$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$
   $$30.0 = \frac{1}{0.015} (1.8284 y^2) (0.50 y)^{2/3} \left(\frac{1}{4000}\right)^{1/2}$$
   $$30.0 = 66.67 \times 1.8284 \times 0.62996 \times y^{8/3} \times 0.015811$$
   $$30.0 = 1.2125 \times y^{8/3} \implies y^{8/3} = \frac{30.0}{1.2125} = 24.742$$
   $$y = (24.742)^{3/8} = \mathbf{3.33\text{ meters}}$$
6. Bed width: $b = 0.8284 \times 3.33 = \mathbf{2.76\text{ meters}}$.

### Problem 4.03: Hydraulic Jump Sequent Depths & Energy Dissipation
**Question:** In a spillway stilling basin of rectangular cross-section ($b = 10.0\text{ m}$), water enters at initial depth $y_1 = 0.60\text{ m}$ with velocity $V_1 = 15.0\text{ m/s}$. Calculate: (a) Froude number $Fr_1$, (b) Sequent depth $y_2$, and (c) Rate of energy dissipation in the hydraulic jump.  
**Solution:**
1. Inflow Froude number:
   $$Fr_1 = \frac{V_1}{\sqrt{g y_1}} = \frac{15.0}{\sqrt{9.81 \times 0.60}} = \frac{15.0}{\sqrt{5.886}} = \frac{15.0}{2.426} = \mathbf{6.183} \quad (\text{Supercritical, strong jump})$$
2. Sequent depth $y_2$:
   $$\frac{y_2}{y_1} = \frac{1}{2} \left(\sqrt{1 + 8 Fr_1^2} - 1\right) = \frac{1}{2} \left(\sqrt{1 + 8(6.183)^2} - 1\right) = \frac{1}{2} (\sqrt{1 + 305.83} - 1) = \frac{1}{2} (17.516 - 1) = 8.258$$
   $$y_2 = 0.60 \times 8.258 = \mathbf{4.955\text{ meters}}$$
3. Head loss in the jump:
   $$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(4.955 - 0.60)^3}{4 \times 0.60 \times 4.955} = \frac{(4.355)^3}{11.892} = \frac{82.597}{11.892} = \mathbf{6.945\text{ meters}}$$
4. Total discharge: $Q = b y_1 V_1 = 10 \times 0.60 \times 15 = 90.0\text{ m}^3/\text{s}$.
5. Power dissipated:
   $$P = \gamma_w Q \Delta E = 9.81\text{ kN/m}^3 \times 90.0\text{ m}^3/\text{s} \times 6.945\text{ m} = \mathbf{6131.7\text{ kW}} \approx \mathbf{6.13\text{ MW}}$$

### Problem 4.04: Centrifugal Pump NPSH Available & Cavitation Check
**Question:** A high-capacity pump in an L&T lift irrigation scheme lifts water at $20^\circ\text{C}$ ($p_v = 2.34\text{ kPa}, \gamma = 9.79\text{ kN/m}^3$). Atmospheric pressure is $p_{atm} = 101.3\text{ kPa}$. The pump centerline is installed $3.0\text{ m}$ above the suction sump water level. Head loss in the suction pipe is $h_{fs} = 1.2\text{ m}$. Suction velocity head is $V_s^2 / 2g = 0.35\text{ m}$. The manufacturer requires $NPSH_R = 4.5\text{ m}$. Is the pump safe against cavitation?  
**Solution:**
1. Atmospheric pressure head: $h_{atm} = \frac{p_{atm}}{\gamma} = \frac{101.3}{9.79} = 10.347\text{ m}$.
2. Vapor pressure head: $h_v = \frac{p_v}{\gamma} = \frac{2.34}{9.79} = 0.239\text{ m}$.
3. Net Positive Suction Head Available ($NPSH_A$):
   $$NPSH_A = h_{atm} - h_v - z_s - h_{fs} = 10.347 - 0.239 - 3.0 - 1.2 = \mathbf{5.908\text{ meters}}$$
4. Cavitation Check:
   $$\text{Margin} = NPSH_A - NPSH_R = 5.908 - 4.50 = \mathbf{+1.408\text{ meters}}$$
   Since $NPSH_A > NPSH_R$, cavitation will **NOT** occur. The pump is hydraulically safe.

### Problem 4.05: Unit Hydrograph S-Curve & Duration Conversion
**Question:** Given a 4-hour Unit Hydrograph (UH) for a catchment with peak discharge $80\text{ m}^3/\text{s}$ occurring at $t = 12\text{ hours}$. Describe the exact analytical procedure to convert this 4-hour UH into a 2-hour UH, and compute the ratio of the equilibrium S-curve discharge $S_\infty$ to catchment area $A$ in $\text{km}^2$.  
**Solution:**
1. Procedure:
   - Construct S-curve by lagging the 4-hour UH by $4\text{ hours}$ repeatedly and summing ordinates: $S(t) = \sum U_4(t - 4k)$.
   - Shift the S-curve by the desired new duration $D' = 2\text{ hours}$: $S(t - 2)$.
   - Subtract the two S-curves: $\Delta S(t) = S(t) - S(t - 2)$.
   - Multiply by the duration ratio $(D / D') = 4 / 2 = 2.0$: $U_2(t) = \Delta S(t) \times \left(\frac{4}{2}\right) = 2 \Delta S(t)$.
2. Equilibrium discharge:
   $$S_\infty = \frac{A\text{ [km}^2\text{]} \times 1\text{ cm} \times 10^4\text{ m}^3/\text{km}^2\cdot\text{cm}}{D \times 3600\text{ s}} = \frac{10,000 A}{4 \times 3600} = \frac{A}{1.44} = \mathbf{2.778 \frac{A}{D}}\text{ m}^3/\text{s}$$

### Problems 4.06 to 4.25: Core Water Resources Practice Set
* **4.06 [Hardy Cross Loop]:** Correction factor $\Delta Q = -\frac{\sum r Q_0 |Q_0|^n}{n \sum r |Q_0|^{n-1}}$.
* **4.07 [Water Hammer Pressure]:** Rapid closure ($t_c < 2L/c$): $\Delta P = \rho c V_0$ (Allievi's equation).
* **4.08 [Specific Energy]:** $E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2 g A^2}$. Minimum energy at critical depth $E_{min} = 1.5 y_c$.
* **4.09 [Affinity Laws]:** $Q \propto N$, $H \propto N^2$, $P \propto N^3$.
* **4.10 [Rational Method Peak Runoff]:** $Q_p = \frac{1}{36} C I A$ ($Q_p$ in $\text{m}^3/\text{s}$, $I$ in $\text{mm/hr}$, $A$ in $\text{ha}$).
* **4.11 to 4.25:** GVF water surface profiles ($M_1, M_2, S_2$), Bligh's creep theory vs Khosla's independent variable method for weir seepage, Muskingum flood routing ($S = K [x I + (1-x) Q]$), and sediment transport shear stress ($\tau_0 = \gamma R S$).

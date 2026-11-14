# 50 Technical Engineering Questions & Detailed Derivations

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27  
**Coverage:** Fluid Mechanics, Open-Channel Flow, Pipe Networks, Turbomachinery, Hydrology, Sediment Transport, Soil Mechanics, Structural Analysis

---

### Q1. Reynolds Transport Theorem to Continuity Equation
**Topic:** Fluid Mechanics Foundations | **Difficulty:** Intermediate  
**Question:** Starting from the Reynolds Transport Theorem, derive the 3D differential form of the continuity equation for an unsteady, compressible fluid. Show the simplification for an incompressible fluid.  
**Solution:**  
1. In the Reynolds Transport Theorem:
   $$\frac{d B_{\text{sys}}}{dt} = \frac{\partial}{\partial t} \iiint_{\text{CV}} \rho \beta \, dV + \iint_{\text{CS}} \rho \beta (\mathbf{V} \cdot \hat{\mathbf{n}}) \, dA$$
2. Let extensive property be system mass $B_{\text{sys}} = m \implies \beta = \frac{dm}{dm} = 1$.  
   By the Law of Conservation of Mass for a closed system, $\frac{d m_{\text{sys}}}{dt} = 0$:
   $$0 = \frac{\partial}{\partial t} \iiint_{\text{CV}} \rho \, dV + \iint_{\text{CS}} \rho (\mathbf{V} \cdot \hat{\mathbf{n}}) \, dA$$
3. Apply the Gauss Divergence Theorem to convert the surface flux integral to a volume integral:
   $$\iint_{\text{CS}} \rho (\mathbf{V} \cdot \hat{\mathbf{n}}) \, dA = \iiint_{\text{CV}} \nabla \cdot (\rho \mathbf{V}) \, dV$$
4. Combining both terms under a single volume integral:
   $$\iiint_{\text{CV}} \left[ \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) \right] dV = 0$$
   Since the arbitrary control volume $V$ is non-zero, the integrand must identically vanish everywhere:
   $$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0 \quad \text{(General Compressible Continuity)}$$
5. For an **incompressible fluid**, density $\rho = \text{constant} \implies \frac{\partial \rho}{\partial t} = 0$:
   $$\nabla \cdot \mathbf{V} = 0 \iff \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$
**AECOM Relevance:** Fundamental governing equation programmed into 2D HEC-RAS and OpenFOAM solvers.

---

### Q2. Critical Depth in a Rectangular Channel
**Topic:** Open-Channel Flow | **Difficulty:** Foundational  
**Question:** A rectangular channel of width $b = 4.0\text{ m}$ conveys a discharge $Q = 12.0\text{ m}^3/\text{s}$. Compute the critical depth $y_c$, critical velocity $V_c$, and minimum specific energy $E_{\min}$. ($g = 9.81\text{ m/s}^2$).  
**Solution:**  
1. Unit discharge $q = \frac{Q}{b} = \frac{12.0}{4.0} = 3.0\text{ m}^2/\text{s}$.
2. Critical depth formula for a rectangular channel:
   $$y_c = \left(\frac{q^2}{g}\right)^{1/3} = \left(\frac{3.0^2}{9.81}\right)^{1/3} = \left(\frac{9.0}{9.81}\right)^{1/3} = (0.91743)^{1/3} \approx 0.9717\text{ m}$$
3. Critical velocity:
   $$V_c = \frac{q}{y_c} = \frac{3.0}{0.9717} \approx 3.087\text{ m/s} \quad \left(\text{Check: } \sqrt{g y_c} = \sqrt{9.81 \times 0.9717} = \sqrt{9.532} = 3.087\text{ m/s}\right)$$
4. Minimum Specific Energy:
   $$E_{\min} = y_c + \frac{V_c^2}{2g} = y_c + \frac{y_c}{2} = 1.5 y_c = 1.5 \times 0.9717 \approx 1.4576\text{ m}$$

---

### Q3. Upward Bed Step Choking Calculation
**Topic:** Open-Channel Flow Transitions | **Difficulty:** Intermediate  
**Question:** For the channel in Q2 ($b = 4\text{ m}, Q = 12\text{ m}^3/\text{s}$), the upstream depth is $y_1 = 2.0\text{ m}$. What is the maximum height of a smooth upward bed step $\Delta z_{\max}$ that can be built without choking the upstream flow?  
**Solution:**  
1. Upstream velocity $V_1 = \frac{Q}{b y_1} = \frac{12}{4 \times 2.0} = 1.5\text{ m/s}$.
2. Upstream specific energy:
   $$E_1 = y_1 + \frac{V_1^2}{2g} = 2.0 + \frac{1.5^2}{2 \times 9.81} = 2.0 + \frac{2.25}{19.62} = 2.0 + 0.1147 = 2.1147\text{ m}$$
3. Flow is subcritical since $y_1 = 2.0\text{ m} > y_c = 0.9717\text{ m}$ ($Fr_1 = \frac{1.5}{\sqrt{9.81 \times 2.0}} = 0.339 < 1$).
4. Choking occurs when the flow over the step just reaches critical energy $E_{\min} = 1.4576\text{ m}$:
   $$E_2 = E_1 - \Delta z \implies E_{\min} = E_1 - \Delta z_{\max}$$
   $$\Delta z_{\max} = E_1 - E_{\min} = 2.1147 - 1.4576 = 0.6571\text{ m} \approx 65.7\text{ cm}$$
**Insight:** Any bed step exceeding $65.7\text{ cm}$ will cause choking, forcing upstream depth $y_1$ to increase (heading up).

---

### Q4. Belanger Conjugate Depth Ratio Derivation
**Topic:** Hydraulic Jumps | **Difficulty:** Intermediate  
**Question:** State the physical assumptions and derive the classical Belanger relationship:
$$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right)$$
**Solution:**  
1. **Assumptions:** Horizontal channel bed ($\theta = 0$), uniform rectangular cross-section, hydrostatic pressure distribution at sections 1 and 2, boundary friction along the short jump length is negligible, and velocity distribution coefficient $\beta_1 \approx \beta_2 \approx 1.0$.
2. Applying 1D Momentum Equation between sections 1 (upstream) and 2 (downstream):
   $$P_1 - P_2 = \rho Q (V_2 - V_1)$$
3. Hydrostatic thrust forces:
   $$P_1 = \frac{1}{2} \gamma y_1^2 b, \quad P_2 = \frac{1}{2} \gamma y_2^2 b$$
4. Substitute $V = \frac{q}{y}$ and $\gamma = \rho g$:
   $$\frac{1}{2} \rho g b (y_1^2 - y_2^2) = \rho (q b) \left(\frac{q}{y_2} - \frac{q}{y_1}\right) = \rho q^2 b \left(\frac{y_1 - y_2}{y_1 y_2}\right)$$
5. Cancel $\rho b$ and divide by $(y_1 - y_2)$ (valid since $y_1 \ne y_2$):
   $$\frac{g}{2}(y_1 + y_2) = \frac{q^2}{y_1 y_2} \implies y_1 y_2 (y_1 + y_2) = \frac{2 q^2}{g}$$
6. Substitute $q^2 = V_1^2 y_1^2$:
   $$y_1 y_2^2 + y_1^2 y_2 = \frac{2 V_1^2 y_1^2}{g} \implies y_2^2 + y_1 y_2 - \frac{2 V_1^2 y_1}{g} = 0$$
7. Divide the entire quadratic equation by $y_1^2$:
   $$\left(\frac{y_2}{y_1}\right)^2 + \left(\frac{y_2}{y_1}\right) - 2 \left(\frac{V_1^2}{g y_1}\right) = 0$$
   Recognizing that $Fr_1^2 = \frac{V_1^2}{g y_1}$:
   $$\left(\frac{y_2}{y_1}\right)^2 + \left(\frac{y_2}{y_1}\right) - 2 Fr_1^2 = 0$$
8. Solving via quadratic formula $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$:
   $$\frac{y_2}{y_1} = \frac{-1 \pm \sqrt{1^2 - 4(1)(-2Fr_1^2)}}{2} = \frac{-1 + \sqrt{1 + 8Fr_1^2}}{2} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right) \quad \blacksquare$$

---

### Q5. Energy Loss in a Hydraulic Jump
**Topic:** Hydraulic Jumps & Energy Dissipation | **Difficulty:** Intermediate  
**Question:** A spillway chute discharges water at an initial depth $y_1 = 0.5\text{ m}$ with velocity $V_1 = 12\text{ m/s}$. Calculate: (a) Upstream Froude number $Fr_1$, (b) Sequent depth $y_2$, (c) Energy head loss $\Delta E$, and (d) Power dissipated in $\text{kW}$ per meter width. ($g = 9.81\text{ m/s}^2$).  
**Solution:**  
1. Upstream Froude number:
   $$Fr_1 = \frac{V_1}{\sqrt{g y_1}} = \frac{12.0}{\sqrt{9.81 \times 0.5}} = \frac{12.0}{\sqrt{4.905}} = \frac{12.0}{2.2147} \approx 5.418$$
   *(Flow is highly supercritical; $4.5 < Fr_1 < 9.0$ forms a stable, well-balanced steady jump).*
2. Sequent depth $y_2$:
   $$y_2 = \frac{y_1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right) = \frac{0.5}{2}\left(\sqrt{1 + 8(5.418)^2} - 1\right) = 0.25 (\sqrt{1 + 234.84} - 1) = 0.25 (15.357 - 1) \approx 3.589\text{ m}$$
3. Energy head loss:
   $$\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2} = \frac{(3.589 - 0.5)^3}{4 \times 0.5 \times 3.589} = \frac{(3.089)^3}{7.178} = \frac{29.475}{7.178} \approx 4.106\text{ m}$$
4. Discharge per meter width: $q = V_1 y_1 = 12.0 \times 0.5 = 6.0\text{ m}^3/\text{s/m}$.
5. Power dissipated per meter width:
   $$P = \gamma q \Delta E = (9810\text{ N/m}^3) \times (6.0\text{ m}^3/\text{s}) \times (4.106\text{ m}) = 241,679\text{ W/m} \approx 241.7\text{ kW/m}$$

---

### Q6. Boundary Layer Displacement vs Momentum Thickness
**Topic:** Boundary Layer Theory | **Difficulty:** Intermediate  
**Question:** For a laminar boundary layer velocity profile approximated by $\frac{u}{U_\infty} = \frac{y}{\delta}$, derive the displacement thickness $\delta^*$ and momentum thickness $\theta$ in terms of $\delta$. What is the Shape Factor $H$?  
**Solution:**  
1. **Displacement thickness ($\delta^*$):**
   $$\delta^* = \int_0^\delta \left(1 - \frac{u}{U_\infty}\right) dy = \int_0^\delta \left(1 - \frac{y}{\delta}\right) dy = \left[ y - \frac{y^2}{2\delta} \right]_0^\delta = \delta - \frac{\delta}{2} = \frac{\delta}{2} = 0.5 \delta$$
2. **Momentum thickness ($\theta$):**
   $$\theta = \int_0^\delta \frac{u}{U_\infty}\left(1 - \frac{u}{U_\infty}\right) dy = \int_0^\delta \frac{y}{\delta}\left(1 - \frac{y}{\delta}\right) dy = \int_0^\delta \left(\frac{y}{\delta} - \frac{y^2}{\delta^2}\right) dy = \left[ \frac{y^2}{2\delta} - \frac{y^3}{3\delta^2} \right]_0^\delta = \frac{\delta}{2} - \frac{\delta}{3} = \frac{\delta}{6} \approx 0.1667 \delta$$
3. **Shape Factor ($H$):**
   $$H = \frac{\delta^*}{\theta} = \frac{\delta/2}{\delta/6} = \frac{6}{2} = 3.0$$
**Insight:** A high shape factor indicates an unstable boundary layer susceptible to separation.

---

### Q7. Darcy-Weisbach vs Hazen-Williams Head Loss
**Topic:** Pipe Flow Hydraulics | **Difficulty:** Foundational  
**Question:** A commercial steel pipeline of diameter $D = 0.5\text{ m}$ and length $L = 2,000\text{ m}$ carries water at velocity $V = 2.0\text{ m/s}$. Given Darcy friction factor $f = 0.02$, compute the frictional head loss. How does doubling velocity affect head loss?  
**Solution:**  
1. Darcy-Weisbach head loss:
   $$h_f = f \frac{L}{D} \frac{V^2}{2g} = 0.02 \times \frac{2,000}{0.5} \times \frac{2.0^2}{2 \times 9.81} = 0.02 \times 4,000 \times \frac{4.0}{19.62} = 80 \times 0.20387 \approx 16.31\text{ m}$$
2. Because $h_f \propto V^2$, doubling the velocity ($V \to 2V$) quadruples head loss ($h_f' = 4 h_f = 65.24\text{ m}$).

---

### Q8. Moody Diagram Flow Regimes
**Topic:** Pipe Flow | **Difficulty:** Intermediate  
**Question:** Explain the physical significance of the four distinct zones on the Moody chart. Why does friction factor $f$ become independent of Reynolds number at high $Re$?  
**Solution:**  
1. **Laminar Zone ($Re < 2,000$):** Viscous forces dominate; $f = 64/Re$. Surface roughness has zero effect because viscous sublayer completely submerges surface asperities.
2. **Critical Transition Zone ($2,000 \le Re \le 4,000$):** Unstable flow fluctuating between laminar and turbulent; unpredictable friction factors.
3. **Transitional Turbulent Zone:** Friction factor depends on both $Re$ and relative roughness $\epsilon/D$ (modeled by Colebrook-White equation). The viscous sublayer thickness $\delta_v \approx 5 \nu / u_*$ is comparable in size to roughness height $\epsilon$.
4. **Completely Rough Turbulent Zone (High $Re$):** As $Re \to \infty$, the viscous sublayer becomes microscopically thin ($\delta_v \ll \epsilon$). Roughness asperities project entirely into the turbulent core. Viscous shear stress is negligible compared to form drag on individual roughness elements. Hence, $f$ depends **strictly on relative roughness $\epsilon/D$** and is independent of $Re$ (von Kármán-Prandtl rough pipe equation).

---

### Q9. Water Hammer Pressure Surge & Wave Speed
**Topic:** Transient Pipe Hydraulics | **Difficulty:** Advanced  
**Question:** Water ($\rho = 1,000\text{ kg/m}^3, K = 2.1\times 10^9\text{ Pa}$) flows at $V_0 = 2.5\text{ m/s}$ in a rigid steel pipe of length $L = 1,200\text{ m}$. (a) Calculate acoustic wave speed $c$ assuming an infinitely rigid pipe. (b) Determine the maximum Joukowsky pressure surge if a valve closes instantaneously. (c) What is the maximum valve closure time $t_c$ classified as "rapid closure"?  
**Solution:**  
1. Acoustic wave speed in pure water (rigid pipe):
   $$c = \sqrt{\frac{K}{\rho}} = \sqrt{\frac{2.1 \times 10^9}{1,000}} = \sqrt{2.1 \times 10^6} \approx 1,449.1\text{ m/s}$$
2. Maximum Joukowsky pressure surge:
   $$\Delta P = \rho c \Delta V = 1,000 \times 1,449.1 \times 2.5 = 3,622,750\text{ Pa} \approx 3.623\text{ MPa}$$
   In terms of head surge:
   $$\Delta H = \frac{\Delta P}{\rho g} = \frac{c \Delta V}{g} = \frac{1,449.1 \times 2.5}{9.81} \approx 369.3\text{ meters of water!}$$
3. Critical closure time:
   $$t_c = \frac{2L}{c} = \frac{2 \times 1,200}{1,449.1} \approx 1.656\text{ seconds}$$
**AECOM Relevance:** Sizing surge vessels and air valves in municipal pumping mains to prevent pipeline rupture.

---

### Q10. Hardy Cross Network Loop Correction Derivation
**Topic:** Pipe Networks | **Difficulty:** Advanced  
**Question:** Derive the Hardy Cross correction formula $\Delta Q = -\frac{\sum r Q_0 |Q_0|}{\sum 2 r |Q_0|}$ for a pipe loop using head loss relationship $h_f = r Q^2$.  
**Solution:**  
1. For any closed loop, the sum of head losses must equal zero: $\sum h_f = \sum r Q^2 = 0$.
2. Let assumed flow in a pipe be $Q_0$ and the required loop correction be $\Delta Q$, such that true discharge $Q = Q_0 + \Delta Q$.
3. Substitute into the loop energy equation:
   $$\sum r (Q_0 + \Delta Q)^2 = 0$$
4. Expanding using binomial expansion and neglecting higher-order terms $(\Delta Q)^2 \approx 0$ (assuming $\Delta Q \ll Q_0$):
   $$\sum r (Q_0^2 + 2 Q_0 \Delta Q) = 0$$
   $$\sum r Q_0^2 + 2 \Delta Q \sum r Q_0 = 0$$
5. Factoring out $\Delta Q$ (accounting for flow direction by using $|Q_0|$):
   $$\Delta Q = -\frac{\sum r Q_0 |Q_0|}{\sum 2 r |Q_0|} \quad \blacksquare$$

---

### Q11. Net Positive Suction Head (NPSH) & Cavitation Prevention
**Topic:** Turbomachinery & Pumps | **Difficulty:** Intermediate  
**Question:** A centrifugal pump is installed at an elevation $Z_s = 3.5\text{ m}$ above the sump water level. Atmospheric pressure is $101.3\text{ kPa}$, water vapor pressure at $25^\circ\text{C}$ is $3.17\text{ kPa}$, and suction pipe friction loss is $h_{fs} = 1.2\text{ m}$. If the manufacturer specifies $NPSH_R = 4.0\text{ m}$, will the pump cavitate? ($\rho = 1,000\text{ kg/m}^3, g = 9.81\text{ m/s}^2$).  
**Solution:**  
1. Atmospheric head: $H_{\text{atm}} = \frac{P_{\text{atm}}}{\rho g} = \frac{101,300}{1,000 \times 9.81} = 10.326\text{ m}$.
2. Vapor pressure head: $H_v = \frac{P_v}{\rho g} = \frac{3,170}{9,810} = 0.323\text{ m}$.
3. Available Net Positive Suction Head ($NPSH_A$):
   $$NPSH_A = H_{\text{atm}} - H_v - Z_s - h_{fs} = 10.326 - 0.323 - 3.50 - 1.20 = 5.303\text{ m}$$
4. Compare with required head:
   $$NPSH_A = 5.303\text{ m} > NPSH_R = 4.0\text{ m}$$
   Margin: $NPSH_A - NPSH_R = 1.303\text{ m} > 0.5\text{ m}$ safety buffer.
   **Conclusion:** The pump will **NOT cavitate**.

---

### Q12. Centrifugal Pump Affinity Laws
**Topic:** Pumps & Turbomachinery | **Difficulty:** Foundational  
**Question:** A pump running at $N_1 = 1,450\text{ RPM}$ delivers discharge $Q_1 = 80\text{ L/s}$ against a head $H_1 = 25\text{ m}$, drawing power $P_1 = 28\text{ kW}$. If an inverter increases motor speed to $N_2 = 1,750\text{ RPM}$, compute the new discharge $Q_2$, head $H_2$, and power $P_2$.  
**Solution:**  
Speed ratio: $\lambda = \frac{N_2}{N_1} = \frac{1,750}{1,450} \approx 1.2069$.
1. New discharge:
   $$Q_2 = Q_1 \times \lambda = 80 \times 1.2069 \approx 96.55\text{ L/s}$$
2. New head:
   $$H_2 = H_1 \times \lambda^2 = 25 \times (1.2069)^2 = 25 \times 1.4566 \approx 36.42\text{ m}$$
3. New power:
   $$P_2 = P_1 \times \lambda^3 = 28 \times (1.2069)^3 = 28 \times 1.7580 \approx 49.22\text{ kW}$$
**Key Insight:** A 20.7% increase in speed causes a **75.8% increase in electrical power consumption**!

---

### Q13. S-Curve Conversion of Unit Hydrographs
**Topic:** Surface Hydrology | **Difficulty:** Intermediate  
**Question:** Explain the physical basis of the S-curve method. Derive the equilibrium discharge $Q_e$ of an S-curve for a catchment of area $A = 360\text{ km}^2$ subjected to continuous effective rainfall at $1\text{ cm}$ per $4\text{ hours}$.  
**Solution:**  
1. An S-curve represents the hydrograph generated by continuous, indefinite rainfall of uniform intensity $i = \frac{1\text{ cm}}{D\text{ hrs}}$.
2. At steady-state equilibrium ($t \to \infty$), the entire catchment contributes simultaneously to runoff. By mass conservation, runoff rate equals precipitation rate:
   $$Q_e = C \cdot i \cdot A$$
   For effective rainfall ($C = 1.0$), depth $P = 1\text{ cm} = 0.01\text{ m}$, duration $D\text{ hours} = 3600 D\text{ seconds}$, Area $A\text{ km}^2 = 10^6 A\text{ m}^2$:
   $$Q_e = \frac{0.01 \times (A \times 10^6)}{3600 D} = \frac{10,000 A}{3600 D} = \frac{2.778 A}{D} \text{ m}^3/\text{s}$$
3. For $A = 360\text{ km}^2$ and $D = 4\text{ hours}$:
   $$Q_e = \frac{2.778 \times 360}{4} = 2.778 \times 90 = 250.0\text{ m}^3/\text{s}$$

---

### Q14. Gumbel Extreme Value Type I Return Period
**Topic:** Hydrology & Flood Frequency | **Difficulty:** Intermediate  
**Question:** An annual flood series over 40 years has sample mean $\bar{x} = 850\text{ m}^3/\text{s}$ and standard deviation $s = 220\text{ m}^3/\text{s}$. Compute the 100-year design flood $x_{100}$ using Gumbel's method. What is the probability that this flood is equaled or exceeded at least once in a 30-year bridge design life?  
**Solution:**  
1. Return period $T = 100\text{ years}$.
2. Frequency factor $K_{100}$:
   $$y_T = -\ln\left[\ln\left(\frac{T}{T-1}\right)\right] = -\ln\left[\ln\left(\frac{100}{99}\right)\right] = -\ln[\ln(1.01010)] = -\ln(0.01005) \approx 4.6001$$
   For large sample size ($N \to \infty$):
   $$K_{100} = \frac{y_T - 0.5772}{1.2825} = \frac{4.6001 - 0.5772}{1.2825} = \frac{4.0229}{1.2825} \approx 3.1368$$
3. 100-year design flood:
   $$x_{100} = \bar{x} + K_{100} s = 850 + (3.1368 \times 220) = 850 + 690.1 \approx 1,540.1\text{ m}^3/\text{s}$$
4. Exceedance probability in any single year: $P = \frac{1}{100} = 0.01$.
5. Risk of at least one occurrence over $N = 30$ years:
   $$\text{Risk } R = 1 - (1 - P)^N = 1 - (1 - 0.01)^{30} = 1 - (0.99)^{30} = 1 - 0.7397 = 0.2603 \ (26.03\%)$$
**Insight:** A bridge designed for a 100-year flood still carries a 26% risk of seeing that design flood over a 30-year operational life!

---

### Q15. Rational Method Stormwater Runoff
**Topic:** Urban Drainage Design | **Difficulty:** Foundational  
**Question:** An urban commercial development of area $A = 25\text{ hectares}$ has a composite runoff coefficient $C = 0.75$. The time of concentration is determined as $t_c = 20\text{ minutes}$. From the local IDF curve, the 10-year rainfall intensity for a 20-minute duration is $I = 90\text{ mm/hr}$. Compute the peak design discharge $Q_p$ for sizing the main trunk storm sewer.  
**Solution:**  
1. Rational formula:
   $$Q_p = \frac{1}{360} C I A$$
2. Substitute parameters:
   $$Q_p = \frac{1}{360} \times 0.75 \times 90 \times 25 = \frac{1,687.5}{360} \approx 4.6875\text{ m}^3/\text{s}$$

---

### Q16. Muskingum Flood Routing Stability
**Topic:** Hydrologic Routing | **Difficulty:** Advanced  
**Question:** A river reach has storage time constant $K = 12\text{ hours}$ and weighting factor $X = 0.20$. (a) Determine the allowable range of routing timestep $\Delta t$ to ensure numerical stability without negative coefficients. (b) If $\Delta t = 6\text{ hours}$ is chosen, compute routing coefficients $C_0, C_1, C_2$ and verify their sum.  
**Solution:**  
1. Stability condition: $2KX < \Delta t < 2K(1-X)$:
   $$2(12)(0.20) < \Delta t < 2(12)(1 - 0.20)$$
   $$4.8\text{ hours} < \Delta t < 19.2\text{ hours}$$
   Since $\Delta t = 6\text{ hours}$ lies inside $(4.8, 19.2)$, it guarantees non-negative coefficients.
2. Routing coefficients for $\Delta t = 6, K = 12, X = 0.20$:
   - Denominator: $D = 2 K (1 - X) + \Delta t = 2(12)(0.8) + 6 = 19.2 + 6 = 25.2\text{ hrs}$.
   - $C_0 = \frac{\Delta t - 2 K X}{D} = \frac{6 - 4.8}{25.2} = \frac{1.2}{25.2} \approx 0.0476$
   - $C_1 = \frac{\Delta t + 2 K X}{D} = \frac{6 + 4.8}{25.2} = \frac{10.8}{25.2} \approx 0.4286$
   - $C_2 = \frac{2 K (1 - X) - \Delta t}{D} = \frac{19.2 - 6}{25.2} = \frac{13.2}{25.2} \approx 0.5238$
3. Verification:
   $$\sum C_i = 0.0476 + 0.4286 + 0.5238 = 1.0000 \quad \text{(Exact unity)}$$

---

### Q17. Lacey's Regime Scour Depth at Bridge Piers
**Topic:** River Engineering & Scour | **Difficulty:** Intermediate  
**Question:** A major railway bridge spans an alluvial river with a design flood discharge $Q = 8,000\text{ m}^3/\text{s}$. The river bed material has median diameter $d_{50} = 0.36\text{ mm}$. The river regime waterway width is provided. Compute: (a) Lacey’s silt factor $f$, (b) Regime wetted perimeter $P$, (c) Lacey's normal scour depth $R$, and (d) Maximum design scour depth at intermediate bridge piers per Indian Standard IRC:78.  
**Solution:**  
1. Silt factor $f$:
   $$f = 1.76 \sqrt{d_{50}} = 1.76 \sqrt{0.36} = 1.76 \times 0.60 = 1.056$$
2. Regime wetted perimeter:
   $$P = 4.75 \sqrt{Q} = 4.75 \sqrt{8,000} = 4.75 \times 89.443 \approx 424.85\text{ m}$$
3. Discharge per unit width:
   $$q = \frac{Q}{B} \approx \frac{8,000}{424.85} \approx 18.83\text{ m}^3/\text{s/m}$$
4. Lacey's normal regime scour depth:
   $$R = 1.35 \left(\frac{q^2}{f}\right)^{1/3} = 1.35 \left(\frac{18.83^2}{1.056}\right)^{1/3} = 1.35 \left(\frac{354.57}{1.056}\right)^{1/3} = 1.35 \times (335.77)^{1/3} = 1.35 \times 6.950 \approx 9.383\text{ m}$$
5. Maximum scour depth at piers per IRC:78:
   $$d_{\text{pier}} = 2.0 R = 2.0 \times 9.383 \approx 18.77\text{ meters below design High Flood Level (HFL)}.$$

---

### Q18. Incipient Motion & Critical Shear Stress (Shields)
**Topic:** Sediment Transport | **Difficulty:** Intermediate  
**Question:** An engineered trapezoidal riprap channel has a bed slope $S_0 = 0.002$ and uniform water depth $y = 1.5\text{ m}$. Assuming wide rectangular approximation ($R_h \approx y$), calculate: (a) Bed shear stress $\tau_0$, and (b) The minimum stable riprap stone diameter $d_{50}$ required to resist motion if the critical Shields parameter is $\theta_c = 0.045$. ($\rho_s = 2,650\text{ kg/m}^3, \rho = 1,000\text{ kg/m}^3$).  
**Solution:**  
1. Bed shear stress:
   $$\tau_0 = \gamma R_h S_0 = (9,810) \times (1.5) \times (0.002) = 29.43\text{ N/m}^2 \ (\text{Pa})$$
2. Critical Shields parameter equation:
   $$\theta_c = \frac{\tau_0}{(\gamma_s - \gamma) d_{50}}$$
   Where submerged specific weight $(\gamma_s - \gamma) = (2,650 - 1,000) \times 9.81 = 1,650 \times 9.81 = 16,186.5\text{ N/m}^3$.
3. Solving for required stone diameter:
   $$d_{50} = \frac{\tau_0}{\theta_c (\gamma_s - \gamma)} = \frac{29.43}{0.045 \times 16,186.5} = \frac{29.43}{728.39} \approx 0.0404\text{ m} \approx 40.4\text{ mm}$$
**Design Advice:** Provide gravel riprap with $d_{50} \ge 45\text{ mm}$ (plus a 1.2 safety factor).

---

### Q19. Terzaghi 1D Consolidation Settlement
**Topic:** Soil Mechanics | **Difficulty:** Intermediate  
**Question:** A normally consolidated clay layer of thickness $H = 4.0\text{ m}$ is located beneath a proposed bridge abutment. Initial void ratio is $e_0 = 0.85$, compression index is $C_c = 0.32$, initial effective overburden pressure is $\sigma_{v0}' = 120\text{ kPa}$, and the bridge load increases vertical stress by $\Delta \sigma' = 60\text{ kPa}$. Compute the ultimate primary consolidation settlement $S_c$.  
**Solution:**  
1. Primary consolidation settlement formula for normally consolidated clay:
   $$S_c = \frac{C_c H}{1 + e_0} \log_{10}\left(\frac{\sigma_{v0}' + \Delta \sigma'}{\sigma_{v0}'}\right)$$
2. Substitute parameters:
   $$S_c = \frac{0.32 \times 4.0}{1 + 0.85} \log_{10}\left(\frac{120 + 60}{120}\right) = \frac{1.28}{1.85} \log_{10}\left(\frac{180}{120}\right) = 0.69189 \times \log_{10}(1.50)$$
   $$\log_{10}(1.50) \approx 0.17609$$
   $$S_c = 0.69189 \times 0.17609 \approx 0.1218\text{ m} \approx 12.18\text{ cm} \ (122\text{ mm})$$

---

### Q20. Rankine Active Earth Pressure with Surcharge
**Topic:** Foundation Engineering | **Difficulty:** Intermediate  
**Question:** A smooth vertical retaining wall of height $H = 6.0\text{ m}$ supports a dry cohesionless sand backfill with unit weight $\gamma = 18\text{ kN/m}^3$ and internal friction angle $\phi = 30^\circ$. A uniform traffic surcharge $q = 20\text{ kN/m}^2$ acts on the ground surface. Calculate: (a) Rankine active earth pressure coefficient $K_a$, (b) Total active lateral thrust $P_a$ per meter length, and (c) Location of the line of action above the base.  
**Solution:**  
1. Active earth pressure coefficient:
   $$K_a = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{1 - 0.5}{1 + 0.5} = \frac{0.5}{1.5} = \frac{1}{3}$$
2. Lateral pressure components:
   - Due to surcharge: $\sigma_{a, q} = K_a q = \frac{1}{3} \times 20 = 6.667\text{ kPa}$ (constant with depth).
     Total surcharge thrust $P_{a1} = \sigma_{a, q} \times H = 6.667 \times 6 = 40.0\text{ kN/m}$ acting at $H/2 = 3.0\text{ m}$ from base.
   - Due to soil self-weight: $\sigma_{a, \text{soil}} = K_a \gamma H = \frac{1}{3} \times 18 \times 6 = 36.0\text{ kPa}$ (triangular distribution).
     Total soil thrust $P_{a2} = \frac{1}{2} \times 36.0 \times 6 = 108.0\text{ kN/m}$ acting at $H/3 = 2.0\text{ m}$ from base.
3. Total active thrust:
   $$P_a = P_{a1} + P_{a2} = 40.0 + 108.0 = 148.0\text{ kN/m}$$
4. Line of action $\bar{y}$ above the base (taking moments about the base):
   $$\bar{y} = \frac{(P_{a1} \times 3.0) + (P_{a2} \times 2.0)}{P_a} = \frac{(40 \times 3.0) + (108 \times 2.0)}{148} = \frac{120 + 216}{148} = \frac{336}{148} \approx 2.27\text{ m}$$

---

### Q21. Critical Gradient & Factor of Safety against Boiling
**Topic:** Geotechnical Seepage | **Difficulty:** Foundational  
**Question:** An excavation pit in fine sand ($G_s = 2.66, e = 0.60$) is subjected to upward seepage. Compute: (a) Critical hydraulic gradient $i_{\text{crit}}$, and (b) Factor of safety against boiling if the observed hydraulic gradient is $i = 0.25$.  
**Solution:**  
1. Submerged unit weight: $\gamma' = \frac{G_s - 1}{1 + e} \gamma_w$.
2. Critical hydraulic gradient:
   $$i_{\text{crit}} = \frac{\gamma'}{\gamma_w} = \frac{G_s - 1}{1 + e} = \frac{2.66 - 1.0}{1 + 0.60} = \frac{1.66}{1.60} = 1.0375$$
3. Factor of safety against piping/boiling:
   $$FOS = \frac{i_{\text{crit}}}{i_{\text{actual}}} = \frac{1.0375}{0.25} = 4.15 \quad (\text{Safe, exceeds standard minimum } FOS \ge 2.5)$$

---

### Q22. Singly Reinforced RCC Beam Limiting Moment
**Topic:** Structural Concrete (IS 456) | **Difficulty:** Foundational  
**Question:** A rectangular reinforced concrete beam has width $b = 300\text{ mm}$ and effective depth $d = 500\text{ mm}$. Using concrete grade M25 ($f_{ck} = 25\text{ MPa}$) and steel grade Fe 415 ($f_y = 415\text{ MPa}$), calculate the limiting neutral axis depth $x_{u, \text{lim}}$ and limiting moment of resistance $M_{u, \text{lim}}$ per IS 456:2000.  
**Solution:**  
1. For Fe 415 steel:
   $$\frac{x_{u, \text{lim}}}{d} = 0.48 \implies x_{u, \text{lim}} = 0.48 \times 500 = 240\text{ mm}$$
2. Limiting moment of resistance coefficient for Fe 415:
   $$M_{u, \text{lim}} = 0.138 f_{ck} b d^2$$
3. Substituting values:
   $$M_{u, \text{lim}} = 0.138 \times 25 \times 300 \times (500)^2 = 3.45 \times 300 \times 250,000 = 258,750,000\text{ N}\cdot\text{mm} = 258.75\text{ kN}\cdot\text{m}$$

---

### Q23. Bending Moment Diagram for Overhanging Beam
**Topic:** Structural Analysis | **Difficulty:** Intermediate  
**Question:** A beam $ABC$ is simply supported at $A$ and $B$ (span $L = 6\text{ m}$) with an overhang $BC = 2\text{ m}$. A uniformly distributed load $w = 20\text{ kN/m}$ acts over the entire length ($8\text{ m}$). Locate the point of contraflexure (zero bending moment).  
**Solution:**  
1. Support reactions:
   Taking moments about $A$:
   $$\sum M_A = 0 \implies R_B \times 6 - (20 \times 8) \times 4 = 0 \implies 6 R_B = 640 \implies R_B = 106.67\text{ kN}$$
   $$\sum F_y = 0 \implies R_A + R_B = 20 \times 8 = 160 \implies R_A = 160 - 106.67 = 53.33\text{ kN}$$
2. Bending moment at distance $x$ from $A$ ($0 \le x \le 6\text{ m}$):
   $$M(x) = R_A x - \frac{w x^2}{2} = 53.33 x - 10 x^2$$
3. Set $M(x) = 0$ to find point of contraflexure:
   $$x (53.33 - 10 x) = 0 \implies x = 5.333\text{ m from support } A$$
   *(The other point $x=0$ is the simple support pin).*

---

### Q24. Manning's Equation Wide Channel Substitution
**Topic:** Open-Channel Flow | **Difficulty:** Foundational  
**Question:** Prove that for a wide rectangular channel (width $b \gg y$), the normal depth $y_n$ is given by $y_n = \left(\frac{q \cdot n}{\sqrt{S_0}}\right)^{3/5}$.  
**Solution:**  
1. For a wide rectangular channel, wetted perimeter $P = b + 2y \approx b$.
2. Hydraulic radius $R_h = \frac{A}{P} = \frac{b y}{b} \approx y$.
3. Manning's equation for discharge per unit width $q = Q/b$:
   $$q = V y = \left(\frac{1}{n} R_h^{2/3} S_0^{1/2}\right) y = \frac{1}{n} y^{2/3} S_0^{1/2} y = \frac{S_0^{1/2}}{n} y^{5/3}$$
4. Inverting for $y = y_n$:
   $$y_n^{5/3} = \frac{q \cdot n}{S_0^{1/2}} \implies y_n = \left(\frac{q \cdot n}{\sqrt{S_0}}\right)^{3/5} \quad \blacksquare$$

---

### Q25. Gradually Varied Flow Profile Deduction
**Topic:** GVF Profiles | **Difficulty:** Intermediate  
**Question:** Water flows from a steep slope channel ($S_0 > S_c$) into a mild slope channel ($S_0 < S_c$). Sketch the water surface profile and identify whether a hydraulic jump occurs upstream or downstream of the slope break.  
**Solution:**  
1. Upstream channel is **Steep ($S$)**: Normal depth is supercritical ($y_{n1} < y_c$).
2. Downstream channel is **Mild ($M$)**: Normal depth is subcritical ($y_{n2} > y_c$).
3. The flow must transition from supercritical ($y_{n1}$) to subcritical ($y_{n2}$). This requires a **hydraulic jump**.
4. Water depth on the steep slope cannot back up upstream of the break. The supercritical stream continues past the slope break onto the mild slope, forming an **$M_3$ profile** ($y < y_c < y_{n2}, \frac{dy}{dx} > 0$).
5. As depth increases along the $M_3$ curve, it reaches the conjugate depth $y_1$ required to jump up to the mild slope normal depth $y_{n2}$.
6. **Conclusion:** The hydraulic jump occurs **downstream of the slope break on the mild slope channel**, preceded by an $M_3$ curve.

---

### Q26. Direct Step Method Numerical Algorithm
**Topic:** Computational Hydraulics | **Difficulty:** Intermediate  
**Question:** State the governing algebraic equation of the Direct Step Method used in prismatic channels to compute the distance $\Delta x$ between two specified flow depths $y_1$ and $y_2$.  
**Solution:**  
1. In a prismatic channel, specify depths $y_1$ and $y_2$ and solve directly for step length $\Delta x$.
2. From the 1D energy equation:
   $$E_1 + S_0 \Delta x = E_2 + \bar{S}_f \Delta x$$
3. Solving for $\Delta x$:
   $$\Delta x = \frac{E_2 - E_1}{S_0 - \bar{S}_f} = \frac{\Delta E}{S_0 - \bar{S}_f}$$
   Where:
   - $E = y + \frac{V^2}{2g}$
   - $\bar{S}_f = \frac{S_{f1} + S_{f2}}{2}$ is the average friction slope across the reach, calculated from Manning: $S_f = \frac{n^2 V^2}{R_h^{4/3}}$.

---

### Q27. Finite Volume Method (FVM) Flux Discretization
**Topic:** Computational Fluid Dynamics (OpenFOAM) | **Difficulty:** Advanced  
**Question:** Explain how the convective term $\nabla \cdot (\rho \mathbf{u} \phi)$ is discretized in the Finite Volume Method over a control cell $V_P$ with faces $f$. Compare Upwind Differencing (UD) vs Central Differencing (CD) in terms of numerical diffusion and stability.  
**Solution:**  
1. Apply Gauss Divergence Theorem to convert the volume integral into a summation of face fluxes:
   $$\int_{V_P} \nabla \cdot (\rho \mathbf{u} \phi) \, dV = \oint_{\partial V_P} \rho \phi (\mathbf{u} \cdot \hat{\mathbf{n}}) \, dA \approx \sum_{f} (\rho_f \mathbf{u}_f \cdot \mathbf{S}_f) \phi_f = \sum_{f} F_f \phi_f$$
   Where $F_f = \rho_f \mathbf{u}_f \cdot \mathbf{S}_f$ is the mass flow rate through face $f$.
2. **Central Differencing (CD):** Evaluates face value by linear interpolation between cell centroids $P$ and $N$: $\phi_f = \lambda \phi_P + (1 - \lambda)\phi_N$.
   - Second-order accurate $\mathcal{O}(\Delta x^2)$.
   - Prone to unphysical spatial oscillations (wiggles) when cell Péclet number $Pe = \frac{\rho u \Delta x}{\Gamma} > 2$.
3. **Upwind Differencing (UD):** Evaluates face value based strictly on upstream flow direction: $\phi_f = \phi_P$ if $F_f > 0$, else $\phi_f = \phi_N$.
   - First-order accurate $\mathcal{O}(\Delta x)$; unconditionally stable and bounded.
   - Introduces severe **artificial numerical diffusion** (false viscosity), smearing sharp gradients.
**AECOM / OpenFOAM Best Practice:** Use second-order bounded schemes like TVD (Total Variation Diminishing) / linearUpwind for free-surface interfaces and scour beds.

---

### Q28. OpenFOAM Turbulence: $k-\epsilon$ vs $k-\omega$ SST
**Topic:** CFD & Turbulence Modeling | **Difficulty:** Advanced  
**Question:** Why is the standard $k-\epsilon$ turbulence model unsuitable for predicting boundary layer separation beneath submerged bridge decks? How does Menter's $k-\omega$ SST model resolve this deficiency?  
**Solution:**  
1. **Deficiency of standard $k-\epsilon$:**
   - The dissipation rate equation ($\epsilon$) requires empirical damping functions near walls.
   - It performs poorly in flows with **adverse pressure gradients and strong stream-wise curvature**, systematically under-predicting the onset and amount of boundary layer separation.
2. **Menter's Shear Stress Transport ($k-\omega$ SST) Formulation:**
   - In the **near-wall region**, it switches to Wilcox’s $k-\omega$ model, which solves down to the viscous sublayer without damping functions, predicting separation with high precision under adverse pressure gradients.
   - In the **free stream (far-field)**, it transforms to the standard $k-\epsilon$ model via a blending function $F_1$, eliminating Wilcox’s extreme sensitivity to freestream turbulence boundary conditions.
   - It enforces a limiter on eddy viscosity $\nu_t = \frac{a_1 k}{\max(a_1 \omega, S F_2)}$ to prevent the unphysical over-prediction of turbulent shear stress in adverse pressure gradient boundary layers.
**Candidate Anchor:** Core theoretical justification for choosing $k-\omega$ SST in the M.Tech thesis simulation of scour beneath submerged bridge decks!

---

### Q29. Mesh Resolution and Non-Dimensional Wall Distance ($y^+$)
**Topic:** CFD Mesh Generation | **Difficulty:** Advanced  
**Question:** Define the non-dimensional wall distance $y^+$. For an OpenFOAM simulation with water velocity $U = 2.0\text{ m/s}$, kinematic viscosity $\nu = 10^{-6}\text{ m}^2/\text{s}$, and flat plate length $L = 5\text{ m}$, calculate the physical height $\Delta y$ of the first grid cell to achieve $y^+ = 1$.  
**Solution:**  
1. Reynolds number:
   $$Re_L = \frac{U L}{\nu} = \frac{2.0 \times 5.0}{10^{-6}} = 10^7$$
2. Turbulent skin friction coefficient (Schlichting empirical formula):
   $$C_f = \frac{0.0592}{(Re_L)^{0.2}} = \frac{0.0592}{(10^7)^{0.2}} = \frac{0.0592}{25.119} \approx 0.002357$$
3. Wall shear stress:
   $$\tau_w = \frac{1}{2} C_f \rho U^2 = \frac{1}{2} \times 0.002357 \times 1,000 \times 2.0^2 = 4.714\text{ N/m}^2$$
4. Friction velocity:
   $$u_\tau = \sqrt{\frac{\tau_w}{\rho}} = \sqrt{\frac{4.714}{1,000}} = \sqrt{0.004714} \approx 0.06866\text{ m/s}$$
5. First cell height for $y^+ = 1$:
   $$y^+ = \frac{u_\tau \Delta y}{\nu} \implies \Delta y = \frac{y^+ \nu}{u_\tau} = \frac{1.0 \times 10^{-6}}{0.06866} \approx 1.456 \times 10^{-5}\text{ m} \approx 14.6\text{ }\mu\text{m}$$
**Key Takeaway:** Resolving the viscous sublayer directly requires sub-millimeter mesh sizing near the wall.

---

### Q30. Volume of Fluid (VOF) Compression Term
**Topic:** Multiphase CFD (`interFoam`) | **Difficulty:** Advanced  
**Question:** In the OpenFOAM `interFoam` solver, what is the role of the artificial compression velocity term $\mathbf{u}_r$ in the volume fraction transport equation?  
**Solution:**  
The VOF equation is:
$$\frac{\partial \alpha}{\partial t} + \nabla \cdot (\alpha \mathbf{u}) + \nabla \cdot (\alpha (1 - \alpha) \mathbf{u}_r) = 0$$
- The product $\alpha (1 - \alpha)$ is non-zero **only at the free-surface interface** ($0 < \alpha < 1$) and identically zero in pure water ($\alpha = 1$) and pure air ($\alpha = 0$).
- $\mathbf{u}_r = \mathbf{u}_{\text{water}} - \mathbf{u}_{\text{air}}$ is directed normal to the interface.
- This term acts as an artificial convective velocity pushing intermediate values of $\alpha$ toward 0 or 1, counteracting numerical diffusion and maintaining a sharp, physically realistic air-water interface.

---

### Q31. Thiessen Polygon Weighting Derivation
**Topic:** Hydrometeorology | **Difficulty:** Foundational  
**Question:** A watershed is monitored by 3 rain gauges $A, B, C$ recording $60\text{ mm}, 80\text{ mm}$, and $100\text{ mm}$ of rainfall respectively. The Thiessen polygon areas are $150\text{ km}^2, 250\text{ km}^2$, and $100\text{ km}^2$. Compute the mean areal rainfall.  
**Solution:**  
1. Total watershed area: $A_{\text{total}} = 150 + 250 + 100 = 500\text{ km}^2$.
2. Areal rainfall:
   $$\bar{P} = \frac{(60 \times 150) + (80 \times 250) + (100 \times 100)}{500} = \frac{9,000 + 20,000 + 10,000}{500} = \frac{39,000}{500} = 78.0\text{ mm}$$

---

### Q32. Horton Infiltration Capacity Integration
**Topic:** Surface Hydrology | **Difficulty:** Intermediate  
**Question:** Infiltration capacity is modeled by Horton’s equation with initial capacity $f_0 = 120\text{ mm/hr}$, ultimate capacity $f_c = 20\text{ mm/hr}$, and decay constant $k = 2.0\text{ hr}^{-1}$. If a continuous heavy rainstorm exceeds capacity for 3 hours, compute: (a) Infiltration capacity at $t = 3\text{ hours}$, and (b) Total depth of water infiltrated in 3 hours.  
**Solution:**  
1. Infiltration capacity at $t = 3$:
   $$f(3) = 20 + (120 - 20) e^{-2 \times 3} = 20 + 100 e^{-6} = 20 + 100(0.002479) = 20 + 0.25 = 20.25\text{ mm/hr}$$
2. Total depth of water infiltrated:
   $$F(3) = \int_0^3 f(t) dt = \left[ f_c t + \frac{f_0 - f_c}{k}(1 - e^{-kt}) \right]_0^3 = (20 \times 3) + \frac{100}{2.0}(1 - e^{-6}) = 60 + 50(1 - 0.002479) = 60 + 50(0.99752) \approx 109.88\text{ mm}$$

---

### Q33. Kirpich Time of Concentration Equation
**Topic:** Storm Drainage Design | **Difficulty:** Foundational  
**Question:** A highway drainage catchment has a longest flow path length $L = 1,200\text{ m}$ with an average slope $S = 0.015\text{ m/m}$. Compute the time of concentration $t_c$ using Kirpich's formula.  
**Solution:**  
1. Kirpich formula:
   $$t_c = 0.01947 \cdot L^{0.77} \cdot S^{-0.385}$$
2. Substitute parameters:
   $$L^{0.77} = (1,200)^{0.77} \approx 237.49$$
   $$S^{-0.385} = (0.015)^{-0.385} \approx 5.021$$
   $$t_c = 0.01947 \times 237.49 \times 5.021 \approx 23.22\text{ minutes}$$

---

### Q34. Culvert Inlet vs Outlet Control Distinction
**Topic:** Culvert Hydraulics | **Difficulty:** Intermediate  
**Question:** Differentiate physically between Inlet Control and Outlet Control in highway box culverts. Which control governs when tailwater depth is high and submerges the culvert outlet?  
**Solution:**  
- **Inlet Control:** Occurs when the culvert barrel has greater conveyance capacity than the inlet edge can accept. Flow passes through critical depth near the entrance and flows as supercritical open-channel flow down the barrel. Headwater depth depends **strictly on inlet geometry and barrel area**.
- **Outlet Control:** Occurs when culvert conveyance is choked by barrel friction, high tailwater, or adverse slope. The barrel flows full or under subcritical depth. Headwater depends on **inlet loss, barrel friction loss ($n$), exit loss, and tailwater level**.
- When tailwater submerges the culvert outlet, the culvert is forced into full-pipe pressurized flow, which is **strictly governed by Outlet Control**.

---

### Q35. Sustainable Urban Drainage Systems (SuDS) Principles
**Topic:** Urban Stormwater & ESG | **Difficulty:** Intermediate  
**Question:** Explain the 4 Pillars of Sustainable Urban Drainage Systems (SuDS) per the CIRIA C753 manual utilized in AECOM international projects. How does a bioretention cell function?  
**Solution:**  
1. **The 4 Pillars of SuDS:**
   - **Water Quantity:** Attenuate peak runoff rates and reduce runoff volume to mimic pre-development greenfield hydrology.
   - **Water Quality:** Intercept and filter suspended solids, heavy metals, and hydrocarbons via natural settlement and bio-filtration.
   - **Amenity:** Integrate drainage features into urban landscapes (parks, swales) for public well-being.
   - **Biodiversity:** Enhance ecological habitats and urban wildlife corridors.
2. **Bioretention Cell Mechanics:** Depressed landscape areas consisting of engineered filter media (sand/compost), vegetation, an overflow weir, and a perforated underdrain pipe. Runoff pools on the surface, filters through soil layers (removing $> 85\%$ of heavy metals), and slowly percolates into the aquifer or underdrain.

---

### Q36. Rouse Suspended Sediment Equation Derivation
**Topic:** Sediment Transport | **Difficulty:** Advanced  
**Question:** In open-channel flow, derive the Rouse suspended sediment concentration distribution by equating downward settling flux to upward turbulent diffusion flux.  
**Solution:**  
1. Upward turbulent sediment flux: $q_{\text{turb}} = -\epsilon_s \frac{dC}{dy}$.
2. Downward gravitational settling flux: $q_{\text{settling}} = -w_s C$.
3. At dynamic equilibrium, net vertical sediment transport is zero:
   $$w_s C + \epsilon_s \frac{dC}{dy} = 0 \implies \frac{dC}{C} = -\frac{w_s}{\epsilon_s} dy$$
4. Assuming turbulent diffusivity of sediment equals momentum diffusivity ($\epsilon_s \approx \epsilon_m = \frac{\tau}{\rho \frac{du}{dy}}$) with linear shear stress $\tau = \tau_0 (1 - y/h)$ and logarithmic velocity profile $\frac{du}{dy} = \frac{u_*}{\kappa y}$:
   $$\epsilon_s = \kappa u_* y \left(1 - \frac{y}{h}\right)$$
5. Substitute $\epsilon_s$ into the flux balance:
   $$\frac{dC}{C} = -\frac{w_s}{\kappa u_* y (1 - y/h)} dy = -\frac{w_s}{\kappa u_*} \left( \frac{1}{y} + \frac{1}{h - y} \right) dy$$
6. Integrate from reference level $y = a$ (concentration $C_a$) to depth $y$ (concentration $C$):
   $$\ln\left(\frac{C}{C_a}\right) = -Z_* \left[ \ln\left(\frac{y}{a}\right) - \ln\left(\frac{h - y}{h - a}\right) \right] = -Z_* \ln\left( \frac{y}{h - y} \frac{h - a}{a} \right)$$
   Where $Z_* = \frac{w_s}{\kappa u_*}$ is the Rouse Number.
7. Exponentiating:
   $$\frac{C(y)}{C_a} = \left( \frac{h - y}{y} \frac{a}{h - a} \right)^{Z_*} \quad \blacksquare$$

---

### Q37. Shields Parameter vs Reynolds Number
**Topic:** Sediment Transport | **Difficulty:** Intermediate  
**Question:** Explain why the critical Shields parameter $\theta_c$ decreases and then levels off to a constant value of $\approx 0.045$ as the boundary Reynolds number $Re_* = \frac{u_* d_{50}}{\nu}$ increases on the Shields diagram.  
**Solution:**  
1. **Hydraulically Smooth Regime ($Re_* < 2$):** Sediment grains are completely embedded within the viscous sublayer. Hydrodynamic lift is weak, and viscous damping dominates; hence, a relatively higher dimensionless shear stress ($\theta_c \approx 0.10$) is needed to dislodge grains.
2. **Transitional Regime ($2 \le Re_* \le 70$):** As shear velocity increases, turbulent eddies penetrate the grain layer. Hydrodynamic pressure fluctuations and form drag dislodge grains easily, causing $\theta_c$ to drop to a minimum of $\approx 0.03$.
3. **Fully Rough Turbulent Regime ($Re_* > 70$):** Grains protrude completely beyond the viscous sublayer. Viscous forces are negligible; resistance is governed purely by turbulent form drag on the exposed grain faces and submerged submerged particle weight. Consequently, $\theta_c$ becomes **strictly constant at $\approx 0.045 - 0.06$**, independent of fluid viscosity $\nu$.

---

### Q38. Submerged Bridge Deck Scour Physics
**Topic:** Bridge Hydraulics & CFD | **Difficulty:** Advanced  
**Question:** How does the scour mechanism beneath a submerged bridge deck differ fundamentally from isolated bridge pier scour?  
**Solution:**  
- **Bridge Pier Scour:** Driven by horizontal 3D boundary layer separation forming a downward vertical jet at the pier face, resulting in a **horseshoe vortex** wrapping around the pier base and shedding **wake vortices** in the downstream lee.
- **Submerged Bridge Deck Scour (Pressure Flow Scour):**
  - When floodwaters submerge the deck, the bridge acts as an **underflow orifice / sluice gate**, severely constricting the vertical waterway opening.
  - Flow accelerates beneath the low chord, creating extreme horizontal shear stresses on the bed ($\tau_{\text{bed}} \gg \tau_c$).
  - Vortices shed from the leading and trailing edges of the bridge deck superstructure induce massive turbulence kinetic energy ($k$), scouring an extensive trench along the entire bridge width rather than localized cone holes.

---

### Q39. Effective Stress in Saturated Soil Layer with Upward Seepage
**Topic:** Geotechnical Seepage | **Difficulty:** Intermediate  
**Question:** A $5\text{ m}$ thick saturated sand layer ($\gamma_{\text{sat}} = 20\text{ kN/m}^3$) is subjected to an upward hydraulic gradient $i = 0.40$. Calculate the effective vertical stress at a depth of $4\text{ m}$ below the sand surface. ($\gamma_w = 9.81\text{ kN/m}^3$).  
**Solution:**  
1. Buoyant unit weight:
   $$\gamma' = \gamma_{\text{sat}} - \gamma_w = 20.0 - 9.81 = 10.19\text{ kN/m}^3$$
2. Static effective stress without seepage:
   $$\sigma_0' = \gamma' \cdot z = 10.19 \times 4.0 = 40.76\text{ kPa}$$
3. Seepage force reduces effective stress during upward flow:
   $$\Delta \sigma' = i \cdot z \cdot \gamma_w = 0.40 \times 4.0 \times 9.81 = 15.696\text{ kPa}$$
4. Net effective stress:
   $$\sigma' = \sigma_0' - \Delta \sigma' = 40.76 - 15.70 = 25.06\text{ kPa}$$

---

### Q40. Terzaghi Bearing Capacity with Water Table at Ground Level
**Topic:** Foundation Engineering | **Difficulty:** Intermediate  
**Question:** A square footing of size $2.0\text{ m} \times 2.0\text{ m}$ is founded at depth $D_f = 1.5\text{ m}$ in sand ($c' = 0, \phi = 32^\circ, N_q = 23.2, N_\gamma = 22.0$). Bulk unit weight is $\gamma = 18\text{ kN/m}^3$ and saturated unit weight is $\gamma_{\text{sat}} = 20\text{ kN/m}^3$. Calculate ultimate bearing capacity $q_u$ when: (a) Water table is very deep, and (b) Water table rises to ground level.  
**Solution:**  
For a square footing: $q_u = 1.3 c' N_c + \gamma D_f N_q + 0.4 \gamma B N_\gamma$. Since $c' = 0$:
$$q_u = \gamma D_f N_q + 0.4 \gamma B N_\gamma$$
1. **Case A (Water table deep):**
   $$q_u = (18 \times 1.5 \times 23.2) + (0.4 \times 18 \times 2.0 \times 22.0) = 626.4 + 316.8 = 943.2\text{ kPa}$$
2. **Case B (Water table at ground level):**  
   Use submerged unit weight $\gamma' = 20 - 9.81 = 10.19\text{ kN/m}^3$:
   $$q_u = (10.19 \times 1.5 \times 23.2) + (0.4 \times 10.19 \times 2.0 \times 22.0) = 354.61 + 179.34 = 533.95\text{ kPa}$$
**Conclusion:** Water table rise to ground level reduces bearing capacity by **43.4%**!

---

### Q41. SFD and BMD for Cantilever with Point and UDL
**Topic:** Structural Mechanics | **Difficulty:** Foundational  
**Question:** A cantilever beam of length $L = 4\text{ m}$ fixed at $A$ carries a UDL $w = 15\text{ kN/m}$ over its entire length and a point load $P = 20\text{ kN}$ at free end $B$. Calculate maximum shear force and maximum bending moment.  
**Solution:**  
1. Maximum shear force occurs at fixed support $A$:
   $$V_{\max} = P + w L = 20 + (15 \times 4) = 20 + 60 = 80.0\text{ kN}$$
2. Maximum bending moment occurs at fixed support $A$ (hogging moment):
   $$M_{\max} = P L + \frac{w L^2}{2} = (20 \times 4) + \frac{15 \times 4^2}{2} = 80 + \frac{240}{2} = 80 + 120 = 200.0\text{ kN}\cdot\text{m}$$

---

### Q42. IS 3370 Liquid Retaining Structures Design Criterion
**Topic:** Concrete Design | **Difficulty:** Intermediate  
**Question:** Why does IS 3370 require calculating tensile stress in concrete using an uncracked section analysis for water retaining tanks, whereas IS 456 neglects concrete tensile strength completely?  
**Solution:**  
- **IS 456 (General Building RCC):** Assumes concrete cracks completely in tension under limit state of collapse, relying entirely on steel rebar to resist tensile forces. Micro-cracking is permissible as long as crack width $\le 0.3\text{ mm}$.
- **IS 3370 (Liquid Storage Tanks):** The primary failure mode is **leakage and water egress**. To ensure water-tightness, the design must prevent through-cracks from forming. Under service loads, direct and flexural tensile stresses are calculated on the composite uncracked section ($A_{\text{trans}} = A_c + (m-1)A_{st}$) and constrained to remain below the permissible direct tensile strength ($\sigma_{ct}$) and flexural tensile strength ($\sigma_{cbt}$) of concrete.

---

### Q43. Average End Area vs Prismoidal Earthwork Formula
**Topic:** Surveying & Highway Engineering | **Difficulty:** Intermediate  
**Question:** A highway cut section has cross-sectional areas $A_1 = 45\text{ m}^2, A_2 = 75\text{ m}^2$ separated by distance $L = 30\text{ m}$. Mid-section area is $A_m = 58\text{ m}^2$. Compute earthwork volume using: (a) Average End Area Method, and (b) Prismoidal Formula. Which formula overestimates volume?  
**Solution:**  
1. **Average End Area Method:**
   $$V_{\text{end}} = \frac{A_1 + A_2}{2} \times L = \frac{45 + 75}{2} \times 30 = 60 \times 30 = 1,800\text{ m}^3$$
2. **Prismoidal Formula (Exact):**
   $$V_{\text{prismoidal}} = \frac{L}{6} [A_1 + 4 A_m + A_2] = \frac{30}{6} [45 + 4(58) + 75] = 5 \times [120 + 232] = 5 \times 352 = 1,760\text{ m}^3$$
3. **Prismoidal Correction:**
   $$C_p = V_{\text{end}} - V_{\text{prismoidal}} = 1,800 - 1,760 = +40\text{ m}^3$$
**Insight:** The Average End Area method almost always **overestimates volume** when cross-sections change.

---

### Q44. Earth's Curvature and Refraction Correction
**Topic:** Geodetic Surveying | **Difficulty:** Foundational  
**Question:** In leveling across a river of width $d = 1.5\text{ km}$, the staff reading on the far bank is $2.850\text{ m}$. Compute the true level staff reading after applying combined curvature and refraction correction.  
**Solution:**  
1. Combined correction formula:
   $$C = 0.0673 d^2 \quad (d \text{ in km})$$
   $$C = 0.0673 \times (1.5)^2 = 0.0673 \times 2.25 \approx 0.1514\text{ m}$$
2. The line of sight is above the level surface; hence, the correction is **subtracted** from the staff reading:
   $$\text{True Staff Reading} = 2.850 - 0.1514 \approx 2.6986\text{ m} \approx 2.699\text{ m}$$

---

### Q45. Total Float vs Free Float in Project CPM
**Topic:** Project Planning | **Difficulty:** Foundational  
**Question:** An activity has Early Start $ES = 10$, Early Finish $EF = 18$, Latest Start $LS = 14$, and Latest Finish $LF = 22$. The earliest start of its immediate successor is $ES_{\text{succ}} = 20$. Compute: (a) Total Float, and (b) Free Float.  
**Solution:**  
1. Duration: $D = EF - ES = 18 - 10 = 8\text{ days}$.
2. Total Float ($TF$):
   $$TF = LS - ES = LF - EF = 14 - 10 = 22 - 18 = 4\text{ days}$$
3. Free Float ($FF$):
   $$FF = ES_{\text{succ}} - EF = 20 - 18 = 2\text{ days}$$
**Interpretation:** The activity can be delayed by 2 days without affecting any subsequent activity, and by up to 4 days without delaying project completion.

---

### Q46. Moody Friction Factor Explicit Approximation (Swamee-Jain)
**Topic:** Pipe Hydraulics | **Difficulty:** Intermediate  
**Question:** Water flows through a commercial concrete pipe with relative roughness $\epsilon/D = 0.001$ at Reynolds number $Re = 5 \times 10^5$. Calculate Darcy friction factor $f$ using the Swamee-Jain explicit formula.  
**Solution:**  
1. Swamee-Jain equation:
   $$f = \frac{0.25}{\left[ \log_{10}\left( \frac{\epsilon/D}{3.7} + \frac{5.74}{Re^{0.9}} \right) \right]^2}$$
2. Compute components:
   $$\frac{\epsilon/D}{3.7} = \frac{0.001}{3.7} \approx 0.00027027$$
   $$Re^{0.9} = (500,000)^{0.9} \approx 141,474 \implies \frac{5.74}{141,474} \approx 0.00004057$$
   $$\text{Sum} = 0.00027027 + 0.00004057 = 0.00031084$$
   $$\log_{10}(0.00031084) \approx -3.50746$$
   $$[\log_{10}(\dots)]^2 = (-3.50746)^2 \approx 12.3023$$
3. Friction factor:
   $$f = \frac{0.25}{12.3023} \approx 0.02032$$

---

### Q47. Froude Number Scaling & Similitude
**Topic:** Hydraulic Physical Modeling | **Difficulty:** Intermediate  
**Question:** A 1:25 scale undistorted Froude model of a river bridge pier is tested in a flume. If the prototype design flood discharge is $Q_p = 1,250\text{ m}^3/\text{s}$ and prototype scour depth is $d_{sp} = 4.5\text{ m}$, what are the corresponding model discharge $Q_m$ and model scour depth $d_{sm}$?  
**Solution:**  
1. Geometric scale ratio: $\lambda_L = \frac{L_p}{L_m} = 25$.
2. Froude model scaling laws:
   - Velocity ratio: $\lambda_V = \sqrt{\lambda_L} = \sqrt{25} = 5$.
   - Discharge ratio: $\lambda_Q = \lambda_L^2 \times \lambda_V = \lambda_L^{5/2} = 25^{2.5} = 3,125$.
3. Model discharge:
   $$Q_m = \frac{Q_p}{\lambda_Q} = \frac{1,250}{3,125} = 0.40\text{ m}^3/\text{s} = 400\text{ L/s}$$
4. Model scour depth (linear geometric scale):
   $$d_{sm} = \frac{d_{sp}}{\lambda_L} = \frac{4.5\text{ m}}{25} = 0.18\text{ m} = 18\text{ cm}$$

---

### Q48. Specific Energy at a Parabolic Channel
**Topic:** Open-Channel Flow | **Difficulty:** Advanced  
**Question:** A channel cross-section has a parabolic geometry defined by $y = c x^2$ (or top width $T = 2\sqrt{y/c}$). Prove that for critical flow in this parabolic channel, critical depth $y_c = \frac{3}{4} E_{\min}$.  
**Solution:**  
1. For parabolic section $y = c x^2$, width at water surface: $T = 2x = 2 \sqrt{y/c}$.
2. Area of cross-section:
   $$A = \int_{-x}^x (y - c x'^2) dx' = 2 \left( y x - \frac{c x^3}{3} \right) = 2 \left( y x - \frac{y x}{3} \right) = \frac{4}{3} x y = \frac{4}{3} \left(\frac{T}{2}\right) y = \frac{2}{3} T y$$
3. Hydraulic depth:
   $$D = \frac{A}{T} = \frac{2}{3} y$$
4. At critical state, Froude number $Fr = 1 \implies \frac{V_c^2}{g D_c} = 1 \implies \frac{V_c^2}{2g} = \frac{D_c}{2} = \frac{1}{2}\left(\frac{2}{3} y_c\right) = \frac{y_c}{3}$.
5. Specific energy at critical state:
   $$E_{\min} = y_c + \frac{V_c^2}{2g} = y_c + \frac{y_c}{3} = \frac{4}{3} y_c$$
6. Inverting:
   $$y_c = \frac{3}{4} E_{\min} \quad \blacksquare$$

---

### Q49. Courant-Friedrichs-Lewy (CFL) Stability Condition
**Topic:** Numerical Methods & CFD | **Difficulty:** Intermediate  
**Question:** In unsteady 1D hydrodynamic river modeling (HEC-RAS / Saint-Venant), state the Courant-Friedrichs-Lewy (CFL) condition. If grid spacing is $\Delta x = 50\text{ m}$, water depth is $y = 4.0\text{ m}$, and flow velocity is $V = 2.0\text{ m/s}$, calculate the maximum allowable explicit timestep $\Delta t_{\max}$.  
**Solution:**  
1. In shallow water equations, gravity wave celerity is $c = \sqrt{g y}$.
2. Total propagation speed of a disturbance: $V + c = V + \sqrt{g y}$.
3. Courant Number definition:
   $$Cr = \frac{(V + \sqrt{g y}) \Delta t}{\Delta x} \le 1.0 \quad \text{(For explicit numerical stability)}$$
4. Wave celerity:
   $$\sqrt{g y} = \sqrt{9.81 \times 4.0} = \sqrt{39.24} \approx 6.264\text{ m/s}$$
   Total speed: $V + c = 2.0 + 6.264 = 8.264\text{ m/s}$.
5. Maximum allowable timestep:
   $$\Delta t_{\max} = \frac{\Delta x}{V + \sqrt{g y}} = \frac{50}{8.264} \approx 6.05\text{ seconds}$$
**AECOM Relevance:** Sizing computational timesteps in HEC-RAS 2D unsteady rain-on-grid models to prevent solver blow-up.

---

### Q50. Machine Learning in Infrastructure Risk Assessment
**Topic:** Applied Data Science in Civil Engineering | **Difficulty:** Advanced  
**Question:** *(Candidate Project Anchor)* In civil asset management (e.g., bridge failure risk), explain why standard Accuracy is misleading when failure prevalence is rare ($< 2\%$). Why does the XGBoost + TreeSHAP framework provide superior regulatory defensibility over a black-box Deep Neural Network?  
**Solution:**  
1. **The Class Imbalance Deception:** If only $1\%$ of bridges experience structural/hydraulic failure, a trivial dummy model that predicts "Safe" for every bridge achieves $99\%$ Accuracy while missing $100\%$ of true catastrophes (Zero Recall). In high-stakes civil infrastructure, **Precision-Recall AUC (PR-AUC)** is the mandatory metric because it evaluates True Positives against False Alarms without dilution from majority True Negatives.
2. **Regulatory Defensibility of XGBoost + TreeSHAP:**
   - Under transportation asset management guidelines (e.g., US FHWA / Indian MoRTH), allocating public capital to bridge repair requires transparent, audit-ready justifications.
   - Deep Neural Networks act as black boxes; their multi-layer non-linear activations cannot be easily attributed to specific physical failure modes.
   - **XGBoost + TreeSHAP** satisfies game-theoretic axioms (Efficiency, Symmetry, Additivity). It computes exact local Shapley values $\phi_i$ in polynomial time ($\mathcal{O}(TLD^2)$), allowing asset managers to state: *"Bridge #204 was flagged as high-risk because its scour depth exceeded safety margin by +45% (SHAP +0.42) and pier concrete compressive strength dropped below 20 MPa (SHAP +0.28)."*

# Engineering Numerical Problems Question Bank

## Overview and Role Alignment
This question bank provides **30 comprehensive engineering numerical problems** with complete step-by-step mathematical solutions and derivations. These problems cover structural mechanics, machine design, high-pressure die casting, sheet metal stamping, injection molding, statistical process control, metallurgy, and battery thermal-electrical modeling. They represent the exact calculation-heavy problems encountered in **Ola Electric GET technical screening tests and design interview rounds**.

---

### Problem 1: Combined Stresses and Mohr's Circle in Scooter Frame
**Problem:** A hollow circular tube on an electric scooter trellis frame ($D_o = 40\text{ mm}, D_i = 34\text{ mm}$) is subjected to an axial compressive load of $P = 15\text{ kN}$ combined with a torsional moment $T = 320\text{ N}\cdot\text{m}$ due to cornering banking loads.
1. Calculate the normal stress $\sigma_x$ and shear stress $\tau_{xy}$ on an outer surface element.
2. Calculate the principal stresses $\sigma_1, \sigma_2$ and maximum in-plane shear stress $\tau_{\max}$.
3. Calculate the Von Mises equivalent stress $\sigma_v$ and safety factor against yielding if the steel tube has $\sigma_y = 360\text{ MPa}$.

**Solution & Step-by-Step Mathematical Derivation:**
1. Geometric properties of the hollow circular cross-section:
   - Area:
     $$A = \frac{\pi}{4}(D_o^2 - D_i^2) = \frac{\pi}{4}(40^2 - 34^2) = \frac{\pi}{4}(1600 - 1156) = \frac{\pi}{4}(444) \approx 348.72\text{ mm}^2 = 3.4872 \times 10^{-4}\text{ m}^2$$
   - Polar moment of inertia:
     $$J = \frac{\pi}{32}(D_o^4 - D_i^4) = \frac{\pi}{32}(40^4 - 34^4) = \frac{\pi}{32}(2,560,000 - 1,336,336) = \frac{\pi}{32}(1,223,664) \approx 120,132\text{ mm}^4 = 1.2013 \times 10^{-7}\text{ m}^4$$
   - Outer radius: $r = D_o / 2 = 20\text{ mm} = 0.020\text{ m}$.
2. Applied stresses:
   - Axial compressive stress ($\sigma_x$):
     $$\sigma_x = -\frac{P}{A} = -\frac{15,000\text{ N}}{3.4872 \times 10^{-4}\text{ m}^2} \approx -43.015\text{ MPa}$$
   - Torsional shear stress ($\tau_{xy}$):
     $$\tau_{xy} = \frac{T \cdot r}{J} = \frac{320\text{ N}\cdot\text{m} \times 0.020\text{ m}}{1.2013 \times 10^{-7}\text{ m}^4} = \frac{6.4}{1.2013 \times 10^{-7}} \approx 53.275\text{ MPa}$$
3. Principal stresses via Mohr's Circle:
   $$\sigma_{\text{avg}} = \frac{\sigma_x + \sigma_y}{2} = \frac{-43.015 + 0}{2} = -21.508\text{ MPa}$$
   $$R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \sqrt{(-21.508)^2 + (53.275)^2} = \sqrt{462.59 + 2838.23} = \sqrt{3300.82} \approx 57.453\text{ MPa}$$
   - Maximum in-plane shear stress:
     $$\tau_{\max} = R = 57.453\text{ MPa}$$
   - Principal stresses:
     $$\sigma_1 = \sigma_{\text{avg}} + R = -21.508 + 57.453 = +35.945\text{ MPa}$$
     $$\sigma_2 = \sigma_{\text{avg}} - R = -21.508 - 57.453 = -78.961\text{ MPa}$$
4. Von Mises equivalent stress ($\sigma_v$):
   $$\sigma_v = \sqrt{\sigma_1^2 - \sigma_1 \sigma_2 + \sigma_2^2} = \sqrt{\sigma_x^2 + 3\tau_{xy}^2}$$
   $$\sigma_v = \sqrt{(-43.015)^2 + 3(53.275)^2} = \sqrt{1850.29 + 3(2838.23)} = \sqrt{1850.29 + 8514.69} = \sqrt{10364.98} \approx 101.81\text{ MPa}$$
5. Factor of Safety against yielding:
   $$FOS = \frac{\sigma_y}{\sigma_v} = \frac{360\text{ MPa}}{101.81\text{ MPa}} \approx 3.54$$

---

### Problem 2: Bolted Joint Torque-Preload Relationship
**Problem:** An M10 Grade 8.8 structural bolt (nominal diameter $d = 10\text{ mm}$, pitch $p = 1.5\text{ mm}$, tensile stress area $A_t = 58.0\text{ mm}^2$, proof strength $S_p = 600\text{ MPa}$) clamps the aluminum battery box lid.
1. Determine the target initial bolt preload ($F_i$) specified at $75\%$ of proof load.
2. If the torque coefficient for zinc-plated threads with light oil is $K = 0.18$, calculate the tightening torque required on the digital torque wrench.

**Solution & Step-by-Step Mathematical Derivation:**
1. Proof load ($F_p$):
   $$F_p = A_t \cdot S_p = (58.0\text{ mm}^2) \times (600\text{ N/mm}^2) = 34,800\text{ N} = 34.8\text{ kN}$$
2. Target preload ($F_i$):
   $$F_i = 0.75 \times F_p = 0.75 \times 34,800\text{ N} = 26,100\text{ N} = 26.1\text{ kN}$$
3. Tightening torque ($T$):
   Using the standard engineering torque equation ($T = K \cdot F_i \cdot d$):
   $$T = 0.18 \times 26,100\text{ N} \times 0.010\text{ m} = 46.98\text{ N}\cdot\text{m}$$
   The torque tool must be calibrated to $47.0\text{ N}\cdot\text{m}$.

---

### Problem 3: Bolted Joint Stiffness and Load Factor
**Problem:** In the joint described in Problem 2, the grip length is $L = 40\text{ mm}$. The bolt stiffness is $k_b = 3.2 \times 10^8\text{ N/m}$ and the clamped aluminum plate stiffness is $k_m = 1.28 \times 10^9\text{ N/m}$.
If an internal pressure surge inside the battery box applies an external tensile separating force of $P_e = 12\text{ kN}$ per bolt:
1. What is the joint stiffness constant ($C$)?
2. What is the total resultant tensile load carried by the bolt ($F_b$)?
3. What is the remaining residual clamping force on the gasket seal ($F_m$), and will the joint separate?

**Solution & Step-by-Step Mathematical Derivation:**
1. Joint stiffness constant ($C$):
   $$C = \frac{k_b}{k_b + k_m} = \frac{3.2 \times 10^8}{3.2 \times 10^8 + 1.28 \times 10^9} = \frac{3.2 \times 10^8}{1.60 \times 10^9} = 0.200$$
   *(The bolt absorbs only $20\%$ of external load; the clamped flange relieves $80\%$)*.
2. Resultant bolt tensile force ($F_b$):
   $$F_b = F_i + C \cdot P_e = 26,100\text{ N} + (0.200 \times 12,000\text{ N}) = 26,100 + 2,400 = 28,500\text{ N} = 28.5\text{ kN}$$
3. Residual clamping force on gasket ($F_m$):
   $$F_m = F_i - (1 - C) \cdot P_e = 26,100\text{ N} - (1 - 0.200) \times 12,000\text{ N} = 26,100 - (0.800 \times 12,000) = 26,100 - 9,600 = 16,500\text{ N} = 16.5\text{ kN}$$
4. Assessment:
   Since $F_m = 16.5\text{ kN} > 0$, the gasket remains under positive compression, preventing seal blowout and maintaining IP67 hermetic integrity. Joint separation occurs only when $P_e \ge F_i / (1 - C) = 26.1 / 0.8 = 32.625\text{ kN}$.

---

### Problem 4: Euler Buckling of Suspension Tie Rod
**Problem:** A hollow steering tie rod ($L = 320\text{ mm}$, outer diameter $D_o = 16\text{ mm}$, wall thickness $t = 1.5\text{ mm}$) is made of structural steel ($E = 205\text{ GPa}$, yield strength $\sigma_y = 310\text{ MPa}$). Both ends are connected via spherical ball joints (pinned-pinned boundary condition, $K_e = 1.0$).
1. Calculate the radius of gyration ($r_g$) and slenderness ratio ($\lambda$).
2. Calculate the Euler critical buckling load ($P_{\text{cr}}$).
3. Check whether Euler's formula is valid or if Johnson's parabolic column formula applies.

**Solution & Step-by-Step Mathematical Derivation:**
1. Cross-sectional properties:
   - Inner diameter: $D_i = 16 - 2(1.5) = 13\text{ mm}$.
   - Area:
     $$A = \frac{\pi}{4}(16^2 - 13^2) = \frac{\pi}{4}(256 - 169) = \frac{\pi}{4}(87) \approx 68.33\text{ mm}^2$$
   - Second moment of area ($I$):
     $$I = \frac{\pi}{64}(16^4 - 13^4) = \frac{\pi}{64}(65,536 - 28,561) = \frac{\pi}{64}(36,975) \approx 1,815.2\text{ mm}^4$$
   - Radius of gyration ($r_g$):
     $$r_g = \sqrt{\frac{I}{A}} = \sqrt{\frac{1,815.2}{68.33}} = \sqrt{26.565} \approx 5.154\text{ mm}$$
2. Slenderness ratio ($\lambda$):
   $$\lambda = \frac{K_e \cdot L}{r_g} = \frac{1.0 \times 320\text{ mm}}{5.154\text{ mm}} \approx 62.09$$
3. Critical slenderness threshold ($\lambda_c$):
   $$\lambda_c = \sqrt{\frac{2 \pi^2 E}{\sigma_y}} = \sqrt{\frac{2 \pi^2 \times 205 \times 10^3\text{ MPa}}{310\text{ MPa}}} = \sqrt{\frac{4,046,550}{310}} = \sqrt{13,053.4} \approx 114.25$$
4. Conclusion & Buckling Load:
   Since actual slenderness $\lambda = 62.09 < \lambda_c = 114.25$, the column falls into the **intermediate column** regime where inelastic yielding precedes elastic buckling!
   - Applying Johnson's parabolic formula:
     $$P_{\text{crit}} = A \left[ \sigma_y - \left(\frac{\sigma_y \cdot \lambda}{2\pi}\right)^2 \frac{1}{E} \right] = 68.33 \left[ 310 - \left(\frac{310 \times 62.09}{2\pi}\right)^2 \frac{1}{205,000} \right]$$
     $$\frac{310 \times 62.09}{2\pi} = \frac{19,247.9}{6.283} \approx 3,063.4$$
     $$(3,063.4)^2 = 9,384,400$$
     $$\frac{9,384,400}{205,000} \approx 45.78\text{ MPa}$$
     $$\sigma_{\text{crit}} = 310 - 45.78 = 264.22\text{ MPa}$$
     $$P_{\text{crit}} = 68.33\text{ mm}^2 \times 264.22\text{ N/mm}^2 = 18,054\text{ N} \approx 18.05\text{ kN}$$
   *(Note: Pure elastic Euler formula would have dangerously overestimated capacity as $35.8\text{ kN}$)*.

---

### Problem 5: HPDC Runner and Gate Design
**Problem:** In an aluminum die casting mold for an inverter enclosure:
- Part volume: $V_{\text{part}} = 380\text{ cm}^3$
- Die cavity fill time target: $\tau_{\text{fill}} = 22\text{ ms} = 0.022\text{ s}$
- Gate discharge coefficient: $C_d = 0.78$
- In-gate velocity: $v_{\text{gate}} = 42\text{ m/s}$
Calculate the required gate cross-sectional area ($A_{\text{gate}}$ in $\text{mm}^2$). If the gate width is constrained to $W = 60\text{ mm}$, what is the gate depth (thickness $h_g$)?

**Solution & Step-by-Step Mathematical Derivation:**
1. Cavity filling flow rate ($Q_{\text{fill}}$):
   $$Q_{\text{fill}} = \frac{V_{\text{part}}}{\tau_{\text{fill}}} = \frac{380\text{ cm}^3}{0.022\text{ s}} \approx 17,272.7\text{ cm}^3\text{/s} = 0.01727\text{ m}^3\text{/s}$$
2. Effective gate area formula:
   $$Q_{\text{fill}} = C_d \cdot A_{\text{gate}} \cdot v_{\text{gate}}$$
3. Solve for $A_{\text{gate}}$:
   $$A_{\text{gate}} = \frac{Q_{\text{fill}}}{C_d \cdot v_{\text{gate}}} = \frac{0.01727\text{ m}^3\text{/s}}{0.78 \times 42\text{ m/s}} = \frac{0.01727}{32.76} \approx 0.0005272\text{ m}^2 = 527.2\text{ mm}^2$$
4. Gate thickness ($h_g$):
   $$h_g = \frac{A_{\text{gate}}}{W} = \frac{527.2\text{ mm}^2}{60\text{ mm}} \approx 8.79\text{ mm}$$

---

### Problem 6: Sheet Metal Stamping Tonnage and Press Sizing
**Problem:** A battery bottom armor plate made of $2.5\text{ mm}$ thick 5052-H32 aluminum sheet ($\tau_{\text{shear}} = 140\text{ MPa}$, $\sigma_{\text{UTS}} = 230\text{ MPa}$) requires:
1. Perimeter blanking: outer perimeter $L_{\text{blank}} = 1,800\text{ mm}$.
2. Piercing: 16 circular holes of diameter $d = 8\text{ mm}$.
Calculate the total blanking force. If a stripper force of $8\%$ is required and an operating press safety factor of $25\%$ is applied, what press tonnage is needed?

**Solution & Step-by-Step Mathematical Derivation:**
1. Total cutting perimeter ($L_{\text{total}}$):
   - Outer perimeter: $1,800\text{ mm}$.
   - 16 holes: $16 \times (\pi \times 8) = 128\pi \approx 402.12\text{ mm}$.
   $$L_{\text{total}} = 1,800 + 402.12 = 2,202.12\text{ mm} \approx 2.202\text{ m}$$
2. Peak blanking cutting force ($F_{\text{blank}}$):
   $$F_{\text{blank}} = L_{\text{total}} \cdot t \cdot \tau_{\text{shear}} = 2.2021\text{ m} \times 0.0025\text{ m} \times (140 \times 10^6\text{ N/m}^2)$$
   $$F_{\text{blank}} = 770,735\text{ N} = 770.74\text{ kN}$$
3. Stripping force ($F_{\text{strip}}$):
   $$F_{\text{strip}} = 0.08 \times 770.74\text{ kN} \approx 61.66\text{ kN}$$
4. Total press force ($F_{\text{press}}$) with $25\%$ safety factor ($SF = 1.25$):
   $$F_{\text{press}} = (F_{\text{blank}} + F_{\text{strip}}) \times 1.25 = (770.74 + 61.66) \times 1.25 = 832.40 \times 1.25 = 1,040.5\text{ kN}$$
5. Conversion to metric tonnes:
   $$\text{Tonnage} = \frac{1,040,500\text{ N}}{9,810\text{ N/tonne}} \approx 106.1\text{ tonnes}$$
   A standard $125\text{-tonne}$ or $150\text{-tonne}$ mechanical stamping press is selected.

---

### Problem 7: Statistical Process Control — Machine Capability $C_m / C_{mk}$
**Problem:** During machine acceptance testing of a new CNC valve seat grinding machine, 50 consecutive parts are produced under homogeneous conditions (zero tool changes, single raw material batch).
The valve seat width specification is $1.200 \pm 0.015\text{ mm}$ ($\text{USL} = 1.215\text{ mm}$, $\text{LSL} = 1.185\text{ mm}$).
The measured sample statistics are $\bar{X} = 1.203\text{ mm}$ and sample standard deviation $s = 0.0022\text{ mm}$.
1. Calculate the machine potential index $C_m$.
2. Calculate the machine capability index $C_{mk}$.
3. Does the machine meet the automotive machine release criterion ($C_{mk} \ge 1.67$)?

**Solution & Step-by-Step Mathematical Derivation:**
1. Tolerance width:
   $$T = \text{USL} - \text{LSL} = 1.215 - 1.185 = 0.030\text{ mm}$$
2. Machine potential index ($C_m$):
   $$C_m = \frac{\text{USL} - \text{LSL}}{6 s} = \frac{0.030}{6 \times 0.0022} = \frac{0.030}{0.0132} \approx 2.273$$
3. Upper and Lower capability components:
   $$C_{mu} = \frac{\text{USL} - \bar{X}}{3 s} = \frac{1.215 - 1.203}{3 \times 0.0022} = \frac{0.012}{0.0066} \approx 1.818$$
   $$C_{ml} = \frac{\bar{X} - \text{LSL}}{3 s} = \frac{1.203 - 1.185}{3 \times 0.0022} = \frac{0.018}{0.0066} \approx 2.727$$
4. Overall machine capability ($C_{mk}$):
   $$C_{mk} = \min(C_{mu}, C_{ml}) = 1.818$$
5. Acceptance Decision:
   Since $C_{mk} = 1.82 > 1.67$, the CNC grinding machine successfully passes machine sign-off and is formally approved for high-volume serial production.

---

### Problem 8: 1D Transient Thermal Conduction in Battery Cell (Biot Number)
**Problem:** A 4680 cylindrical cell ($R = 23\text{ mm}$, height $H = 80\text{ mm}$, density $\rho = 2,500\text{ kg/m}^3$, specific heat $c_p = 1,100\text{ J/kg}\cdot\text{K}$, effective radial thermal conductivity $\kappa_r = 1.2\text{ W/m}\cdot\text{K}$) is cooled via ambient forced convection with heat transfer coefficient $h = 45\text{ W/m}^2\cdot\text{K}$.
1. Calculate the characteristic length ($L_c = V/A_s$) and the convective Biot number ($Bi$).
2. Determine whether the lumped capacitance thermal model is mathematically valid ($Bi < 0.1$).

**Solution & Step-by-Step Mathematical Derivation:**
1. Cell geometry:
   - Volume: $V = \pi R^2 H = \pi (0.023)^2 (0.080) \approx 1.3295 \times 10^{-4}\text{ m}^3$.
   - Surface area:
     $$A_s = 2\pi R^2 + 2\pi R H = 2\pi(0.023)^2 + 2\pi(0.023)(0.080) = 0.003324 + 0.011561 \approx 0.014885\text{ m}^2$$
   - Characteristic length ($L_c$):
     $$L_c = \frac{V}{A_s} = \frac{1.3295 \times 10^{-4}}{0.014885} \approx 0.00893\text{ m} = 8.93\text{ mm}$$
2. Biot Number ($Bi$):
   $$Bi = \frac{h \cdot L_c}{\kappa_r} = \frac{45\text{ W/m}^2\cdot\text{K} \times 0.00893\text{ m}}{1.2\text{ W/m}\cdot\text{K}} = \frac{0.40185}{1.2} \approx 0.335$$
3. Engineering Conclusion:
   Because $Bi = 0.335 > 0.10$, internal conductive resistance within the jellyroll is non-negligible compared to surface convective resistance. **The lumped capacitance approximation is invalid.** A spatial 2D/3D conduction model (resolving radial temperature gradients where cell core temperature exceeds surface temperature by $8\text{--}15^\circ\text{C}$) must be solved using finite differences or CFD.

---

### Problem 9: Battery Pack Operating Range and Specific Consumption
**Problem:** An electric scooter with total laden mass $m = 180\text{ kg}$ travels at a constant velocity of $v = 45\text{ km/h} = 12.5\text{ m/s}$ on a level paved road.
- Rolling resistance coefficient: $C_{rr} = 0.015$
- Aerodynamic drag coefficient: $C_d = 0.55$
- Frontal area: $A_f = 0.65\text{ m}^2$
- Air density: $\rho = 1.20\text{ kg/m}^3$
- Powertrain efficiency (battery to wheel): $\eta_{\text{drivetrain}} = 82\%$
- Usable battery energy: $E_{\text{batt}} = 3.60\text{ kWh} = 3,600\text{ Wh}$
1. Calculate the total tractive force ($F_{\text{tract}}$) and mechanical wheel power ($P_{\text{wheel}}$).
2. Calculate electrical power drawn from the battery ($P_{\text{batt}}$).
3. Calculate vehicle specific energy consumption in $\text{Wh/km}$ and total single-charge range in kilometers.

**Solution & Step-by-Step Mathematical Derivation:**
1. Resistance forces:
   - Rolling resistance:
     $$F_{\text{roll}} = C_{rr} \cdot m \cdot g = 0.015 \times 180\text{ kg} \times 9.81\text{ m/s}^2 = 26.487\text{ N}$$
   - Aerodynamic drag:
     $$F_{\text{aero}} = \frac{1}{2} \rho C_d A_f v^2 = \frac{1}{2} \times 1.20 \times 0.55 \times 0.65 \times (12.5)^2 = 0.2145 \times 156.25 \approx 33.516\text{ N}$$
   - Total tractive force:
     $$F_{\text{tract}} = F_{\text{roll}} + F_{\text{aero}} = 26.487 + 33.516 = 60.003\text{ N} \approx 60.0\text{ N}$$
2. Wheel power:
   $$P_{\text{wheel}} = F_{\text{tract}} \cdot v = 60.003\text{ N} \times 12.5\text{ m/s} = 750.04\text{ W}$$
3. Battery electrical power:
   $$P_{\text{batt}} = \frac{P_{\text{wheel}}}{\eta_{\text{drivetrain}}} = \frac{750.04\text{ W}}{0.82} \approx 914.68\text{ W}$$
4. Specific energy consumption ($\text{EC}$):
   $$\text{EC} = \frac{P_{\text{batt}}}{v_{\text{km/h}}} = \frac{914.68\text{ W}}{45\text{ km/h}} \approx 20.326\text{ Wh/km}$$
5. Total range ($R$):
   $$R = \frac{E_{\text{batt}}}{\text{EC}} = \frac{3,600\text{ Wh}}{20.326\text{ Wh/km}} \approx 177.1\text{ km}$$

---

### Problem 10: Takt Time, Cycle Time, and Line Balancing Efficiency
**Problem:** An electric motor assembly line consists of 6 sequential workstations with the following observed task cycle times:
- Station 1 (Stator core stacking): $t_1 = 48\text{ s}$
- Station 2 (Coil winding): $t_2 = 56\text{ s}$
- Station 3 (Lead wire soldering): $t_3 = 52\text{ s}$
- Station 4 (Rotor shaft press-fit): $t_4 = 62\text{ s}$
- Station 5 (End-shield bearing assembly): $t_5 = 45\text{ s}$
- Station 6 (End-of-Line surge/hi-pot testing): $t_6 = 50\text{ s}$
1. Identify the bottleneck station and maximum line production rate per hour.
2. Calculate the Line Balancing Efficiency ($\eta_{\text{line}}$) and the Balance Delay ($d_{\text{balance}}$).

**Solution & Step-by-Step Mathematical Derivation:**
1. Bottleneck identification:
   - Bottleneck station is **Station 4 (Rotor shaft press-fit)** with maximum cycle time $T_{\text{max}} = 62\text{ seconds}$.
   - Line cycle time: $T_c = 62\text{ s}$.
   - Maximum hourly production rate:
     $$\text{Capacity} = \frac{3,600\text{ s/hr}}{62\text{ s/motor}} \approx 58.06\text{ motors/hour}$$
2. Sum of total work content ($\sum t_i$):
   $$\sum t_i = 48 + 56 + 52 + 62 + 45 + 50 = 313\text{ seconds}$$
3. Line Balancing Efficiency ($\eta_{\text{line}}$):
   $$\eta_{\text{line}} = \frac{\sum t_i}{n \cdot T_{\text{max}}} \times 100\% = \frac{313\text{ s}}{6 \times 62\text{ s}} \times 100\% = \frac{313}{372} \times 100\% \approx 84.14\%$$
4. Balance Delay ($d_{\text{balance}}$):
   $$d_{\text{balance}} = 100\% - \eta_{\text{line}} = 100\% - 84.14\% = 15.86\%$$
   Engineering improvement: Offload sub-tasks from Station 4 (e.g., pre-heating bearings) to Station 5 to balance cycle times to $\sim 52\text{ s}$, boosting line throughput to $69\text{ units/hr}$.

---

### Problems 11–30: Rapid Multi-Domain Numerical Solutions

#### Problem 11: Fillet Weld Stress Analysis
- Throat thickness: $t_t = h \cos(45^\circ) = 6 \times 0.7071 = 4.24\text{ mm}$.
- Total weld length: $L = 120\text{ mm}$. Effective throat area: $A_w = 4.24 \times 120 = 508.8\text{ mm}^2$.
- Direct shear load $V = 45\text{ kN}$.
- Average shear stress: $\tau = V / A_w = 45,000 / 508.8 = 88.44\text{ MPa}$. Safe against weld filler allowable ($\tau_{\text{allow}} = 120\text{ MPa}$).

#### Problem 12: Thermal Expansion Stress in Confined Battery Pack
- Temperature delta: $\Delta T = 55 - 20 = 35^\circ\text{C}$.
- Aluminum busbar $\alpha = 23 \times 10^{-6}\text{ /}^\circ\text{C}$, $E = 70\text{ GPa}$.
- Thermal compressive stress: $\sigma_{\text{th}} = E \alpha \Delta T = (70 \times 10^3) \times (23 \times 10^{-6}) \times 35 = 56.35\text{ MPa}$.

#### Problem 13: Coulombic vs Energy Efficiency
- Discharge capacity: $50\text{ Ah}$ at average $3.6\text{ V} \implies E_{\text{out}} = 180\text{ Wh}$.
- Charge capacity: $52\text{ Ah}$ at average $3.9\text{ V} \implies E_{\text{in}} = 202.8\text{ Wh}$.
- Coulombic efficiency: $\eta_C = 50/52 = 96.15\%$.
- Energy efficiency: $\eta_E = 180 / 202.8 = 88.76\%$.

#### Problem 14: Fatigue Life Under Mean Stress (Goodman Criterion)
- $\sigma_a = 120\text{ MPa}$, $\sigma_m = 80\text{ MPa}$, $\sigma_{\text{UTS}} = 450\text{ MPa}$, endurance limit $S_e = 200\text{ MPa}$.
- Modified Goodman relation: $\frac{\sigma_a}{S_e} + \frac{\sigma_m}{\sigma_{\text{UTS}}} = \frac{1}{SF}$.
- $\frac{120}{200} + \frac{80}{450} = 0.600 + 0.178 = 0.778 \implies SF = 1 / 0.778 = 1.285$.

#### Problem 15: Plastic Injection Molding Flow Rate
- Part volume $V = 240\text{ cm}^3$. Injection time $t_{\text{inj}} = 1.6\text{ s}$.
- Volumetric injection rate: $Q = 240 / 1.6 = 150\text{ cm}^3\text{/s} = 0.15\text{ L/s}$.

#### Problem 16: Resistance Spot Weld Energy Consumption
- $I = 12\text{ kA}$, $R = 90\text{ }\mu\Omega$, $t = 0.25\text{ s}$.
- $Q = I^2 R t = (12,000)^2 \times (90 \times 10^{-6}) \times 0.25 = 144 \times 10^6 \times 90 \times 10^{-6} \times 0.25 = 3,240\text{ J}$.

#### Problem 17: Process Capability $P_{pk}$ with Shift
- USL $= 10.05$, LSL $= 9.95$, $\bar{X} = 10.02$, $s_{\text{overall}} = 0.012$.
- $P_{pu} = (10.05 - 10.02)/(3 \times 0.012) = 0.03 / 0.036 = 0.833$.
- $P_{pk} = 0.833$ (Fails automotive release).

#### Problem 18: Stepper Motor Torque and Acceleration
- Rotor inertia $J = 2.4 \times 10^{-4}\text{ kg}\cdot\text{m}^2$. Desired angular acceleration $\alpha = 500\text{ rad/s}^2$.
- Required inertial torque: $T = J \alpha = 2.4 \times 10^{-4} \times 500 = 0.12\text{ N}\cdot\text{m}$.

#### Problem 19: Spring Deflection in Battery Cell Hold-down
- Spring rate $k = 45\text{ N/mm}$, required clamping force $F = 180\text{ N}$.
- Preload deflection: $\delta = F / k = 180 / 45 = 4.0\text{ mm}$.

#### Problem 20: Cell Interconnect Busbar Voltage Drop
- Copper busbar: $L = 80\text{ mm}$, $A = 20\text{ mm}^2$, $\rho_{\text{Cu}} = 1.72 \times 10^{-8}\text{ }\Omega\cdot\text{m}$.
- Resistance: $R = \rho L / A = (1.72 \times 10^{-8} \times 0.08) / (20 \times 10^{-6}) = 6.88 \times 10^{-5}\text{ }\Omega = 68.8\text{ }\mu\Omega$.
- At $I = 150\text{ A}$, $\Delta V = I R = 150 \times (68.8 \times 10^{-6}) = 0.01032\text{ V} = 10.32\text{ mV}$.

#### Problem 21: Cold Chamber HPDC Intensification Ratio
- Hydraulic cylinder diameter $D_{\text{cyl}} = 180\text{ mm}$, plunger tip diameter $d_{\text{tip}} = 70\text{ mm}$.
- Area ratio: $(180/70)^2 \approx 6.61$.
- At hydraulic system pressure $P_{\text{hyd}} = 14\text{ MPa}$, metal pressure $P_{\text{metal}} = 14 \times 6.61 = 92.57\text{ MPa}$.

#### Problem 22: Charpy Impact Energy Absorption per Unit Area
- Specimen fractured at absorbed energy $E = 84\text{ J}$.
- Ligament area behind $2\text{ mm}$ V-notch on $10 \times 10\text{ mm}$ bar: $A = 10 \times (10 - 2) = 80\text{ mm}^2 = 0.8\text{ cm}^2$.
- Impact toughness: $K_V = 84\text{ J} / 0.8\text{ cm}^2 = 105\text{ J/cm}^2$.

#### Problem 23: Pre-charge Resistor Sizing and Sieve Time
- Inverter DC capacitor $C = 1,200\text{ }\mu\text{F}$, battery voltage $V = 50\text{ V}$.
- Pre-charge resistor $R = 25\text{ }\Omega$.
- Time constant: $\tau = R C = 25 \times 1,200 \times 10^{-6} = 0.030\text{ s} = 30\text{ ms}$.
- Time to reach $98\%$ voltage ($4\tau$): $t = 4 \times 30 = 120\text{ ms}$.

#### Problem 24: Hall-Petch Strength Prediction
- $d = 16\text{ }\mu\text{m} \implies d^{-1/2} = 1/4 = 0.25\text{ }\mu\text{m}^{-1/2}$.
- $\sigma_0 = 120\text{ MPa}$, $k_y = 600\text{ MPa}\cdot\mu\text{m}^{1/2}$.
- $\sigma_y = 120 + (600 \times 0.25) = 120 + 150 = 270\text{ MPa}$.

#### Problem 25: OEE Availability Factor
- Total shift $= 480\text{ min}$. Lunch $= 30\text{ min}$. Planned run $= 450\text{ min}$.
- Unplanned breakdowns $= 55\text{ min}$. Actual run time $= 395\text{ min}$.
- Availability: $A = 395 / 450 = 87.78\%$.

#### Problem 26: Battery Thermal Runaway Adiabatic Heating Rate
- Cell mass $m = 0.35\text{ kg}$, $c_p = 1,050\text{ J/kg}\cdot\text{K}$.
- Exothermic heat release rate during separator collapse: $\dot{Q}_{\text{gen}} = 3,500\text{ W}$.
- Adiabatic rate of temperature rise:
  $$\frac{dT}{dt} = \frac{\dot{Q}}{m \cdot c_p} = \frac{3,500}{0.35 \times 1,050} = \frac{3,500}{367.5} \approx 9.52^\circ\text{C/second} \approx 571^\circ\text{C/minute}$$

#### Problem 27: Press Brake V-Die Opening Width Sizing
- Sheet thickness $t = 2.0\text{ mm}$ steel.
- Rule of thumb for standard V-die opening: $V = 8 \times t = 8 \times 2.0 = 16.0\text{ mm}$.

#### Problem 28: Cutting Tool Tool Life (Taylor's Tool Life Equation)
- $v_c T^n = C$. For carbide on aluminum: $n = 0.35, C = 450$.
- At $v_c = 250\text{ m/min}$:
  $$T = (450 / 250)^{1/0.35} = (1.8)^{2.857} \approx 5.34\text{ hours} \approx 320\text{ minutes}$$

#### Problem 29: Ingot Melt Loss in Aluminum Foundry
- Charge weight $= 2,500\text{ kg}$, recovered molten alloy $= 2,410\text{ kg}$, dross $= 90\text{ kg}$.
- Ingot melting loss: $(90 / 2,500) \times 100\% = 3.60\%$.

#### Problem 30: Battery C-Rate vs Discharge Duration
- Pack rated at $60\text{ Ah}$. Discharged at continuous $180\text{ A}$.
- Operating C-rate: $180 / 60 = 3.0\text{ C}$.
- Theoretical full discharge time: $1\text{ hour} / 3.0 = 20\text{ minutes}$.


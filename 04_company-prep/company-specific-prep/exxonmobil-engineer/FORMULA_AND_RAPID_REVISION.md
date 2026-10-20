# ExxonMobil Engineer Recruitment: Master Formula Reference & Rapid Revision Sheet
## High-Density Equation Handbook, Unit Verification Traps & 5-Minute Pre-Test Checklist

> **Purpose:** Rapid mental calibration directly prior to technical assessments and panel interviews  
> **Structure:** Grouped strictly by governing physical laws, explicit dimensionless numbers, dimensional unit traps, and high-frequency conceptual traps.

---

# 1. Master Formula Matrix

### Fluid Mechanics & Pipeline Transport
* **Continuity Equation (Incompressible 1D):**
  $$A_1 V_1 = A_2 V_2 = Q = \text{constant}$$
* **Differential Continuity (3D Incompressible):**
  $$\nabla \cdot \mathbf{V} = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$
* **Darcy-Weisbach Equation (Frictional Head Loss):**
  $$h_f = f \frac{L}{D} \frac{V^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5}$$
  - *Laminar Pipe Flow ($\mathrm{Re} \le 2000$):* $f = \frac{64}{\mathrm{Re}}$
  - *Hagen-Poiseuille Pressure Drop:* $\Delta P = \frac{128 \mu L Q}{\pi D^4}$
  - *Fully Rough Turbulent Flow ($\mathrm{Re} \to \infty$):* $\frac{1}{\sqrt{f}} = 1.14 - 2.0 \log_{10}\left(\frac{\epsilon}{D}\right)$
* **Minor Head Losses:**
  $$h_m = K_L \frac{V^2}{2g}$$
  - *Borda-Carnot Sudden Expansion:* $h_{L} = \frac{(V_1 - V_2)^2}{2g} = \left(1 - \frac{A_1}{A_2}\right)^2 \frac{V_1^2}{2g}$
* **Net Positive Suction Head Available ($\mathrm{NPSH}_A$):**
  $$\mathrm{NPSH}_A = \frac{P_{\text{atm}}}{\rho g} + z_{\text{suction}} - h_{L,\text{suction}} - \frac{P_v}{\rho g} \ge \mathrm{NPSH}_R + 1.0\text{ m}$$
* **Joukowsky Water Hammer Pressure Surge:**
  $$\Delta P_{\max} = \rho c \Delta V \implies \Delta H_{\max} = \frac{c \Delta V}{g}$$
  - *Elastic Wave Celerity:* $c = \sqrt{\frac{K/\rho}{1 + (K/E)(D/t)}}$
  - *Critical Valve Transit Time:* $T_c = \frac{2 L}{c}$

---

### Open-Channel Hydraulics & Structures
* **Froude Number:**
  $$\mathrm{Fr} = \frac{V}{\sqrt{g D_h}} = \frac{V}{\sqrt{g (A/T)}}$$
* **Specific Energy:**
  $$E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g A^2}$$
* **Rectangular Channel Critical Flow Relationships ($q = Q/b$):**
  $$y_c = \sqrt[3]{\frac{q^2}{g}}, \quad E_{\min} = 1.5 y_c, \quad V_c = \sqrt{g y_c}$$
* **Bélanger Hydraulic Jump Conjugate Depths (Rectangular Horizontal):**
  $$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 \mathrm{Fr}_1^2} - 1\right)$$
  - *Energy Head Dissipation:* $\Delta E_L = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$
* **Manning's Equation for Uniform Flow (SI Units):**
  $$V = \frac{1}{n} R^{2/3} S_0^{1/2}, \quad Q = \frac{1}{n} A R^{2/3} S_0^{1/2}$$
* **Gradually Varied Flow (GVF) Differential Equation:**
  $$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - \mathrm{Fr}^2}, \quad S_f = \frac{n^2 V^2}{R^{4/3}}$$

---

### Sediment Transport, River Mechanics & Scour
* **Boundary Bed Shear Stress:**
  $$\tau_b = \rho g R S_0$$
* **Shear (Friction) Velocity:**
  $$u_* = \sqrt{\frac{\tau_b}{\rho}} = \sqrt{g R S_0}$$
* **Shields Dimensionless Parameter:**
  $$\tau_* = \frac{\tau_b}{(\rho_s - \rho) g d_{50}}$$
  - Motion occurs if $\tau_* > \tau_{*c} \approx 0.045$.
* **Exner Equation of Sediment Continuity:**
  $$(1 - \lambda_p) \frac{\partial z_b}{\partial t} + \frac{\partial q_s}{\partial x} = 0$$
* **FHWA HEC-18 Bridge Pier Local Scour:**
  $$\frac{y_s}{y_1} = 2.0 \, K_1 K_2 K_3 K_4 \left(\frac{a}{y_1}\right)^{0.65} \mathrm{Fr}_1^{0.43}$$

---

### Mechanics of Materials & Thermodynamics
* **Thin-Walled Pressure Vessel Hoop Stress ($D/t \ge 20$):**
  $$\sigma_h = \frac{P_i D}{2 t}, \quad \sigma_L = \frac{P_i D}{4 t} = \frac{1}{2}\sigma_h$$
* **Mohr's Circle Principal Stresses (Plane Stress):**
  $$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}, \quad \tau_{\max} = \frac{\sigma_1 - \sigma_2}{2}$$
* **Carnot Maximum Cycle Efficiency:**
  $$\eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H} \quad (\text{Strictly in Kelvin!})$$
* **Steady-Flow Energy Equation (SFEE, Compressor/Pump):**
  $$\dot{W}_{\text{in}} = \dot{m} (h_2 - h_1) \approx \dot{m} c_p (T_2 - T_1)$$
* **Heat Exchanger LMTD:**
  $$\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$

---

# 2. Critical Unit Verification & Conversion Traps

```
+-----------------------------------------------------------------------------------------------+
|                                    HIGH-FREQUENCY EXAM TRAPS                                  |
+-----------------------------------------------------------------------------------------------+
| 1. Friction Factor Trap:                                                                      |
|    • Darcy friction factor f = 64/Re (Moody chart standard, used in Civil Engineering).       |
|    • Fanning friction factor f_F = 16/Re (Chemical/Petroleum engineering standard).           |
|    • ALERT: f_Darcy = 4 * f_Fanning. Using f_F in Darcy-Weisbach underestimates head loss by  |
|      a factor of 4!                                                                           |
|                                                                                               |
| 2. Pressure Gauge vs Absolute Trap:                                                           |
|    • P_abs = P_gauge + P_atm.                                                                 |
|    • Fluid properties (NPSH, vapor pressure, ideal gas law) require ABSOLUTE pressure.        |
|    • Pipe hoop stress calculations (sigma_h = P*D / 2t) require GAUGE (internal overpressure).|
|                                                                                               |
| 3. Temperature Scale Trap:                                                                    |
|    • Carnot efficiency and radiation heat transfer (q = epsilon * sigma * T^4) REQUIRE KELVIN |
|      (K = °C + 273.15). Using Celsius yields catastrophic errors.                             |
|                                                                                               |
| 4. Manning's Equation Unit Trap:                                                              |
|    • SI Units: V = (1.0 / n) * R^(2/3) * S_0^(1/2).                                           |
|    • US Customary: V = (1.486 / n) * R^(2/3) * S_0^(1/2).                                     |
|                                                                                               |
| 5. Viscosity Unit Trap:                                                                       |
|    • Dynamic Viscosity mu: 1 Poise = 0.1 Pa·s = 0.1 N·s/m^2. 1 cP = 10^-3 Pa·s (water).       |
|    • Kinematic Viscosity nu: 1 Stokes = 10^-4 m^2/s. 1 cSt = 10^-6 m^2/s.                     |
+-----------------------------------------------------------------------------------------------+
```

---

# 3. 5-Minute Pre-Test Mental Checklist

Before clicking start on your assessment or entering the interview room, review these 10 rapid principles:

1. **Mass Conservation First:** In any branched pipe network or open channel junction, verify that $\sum Q_{\text{in}} = \sum Q_{\text{out}}$ before calculating head losses.
2. **Parallel Lines Share Head Loss:** If two pipes branch and rejoin between nodes A and B, $h_{L,1} = h_{L,2}$, but their discharges divide inversely proportional to $\sqrt{K_{\text{pipe}}}$.
3. **Critical Flow Minimum Energy:** At critical depth ($Fr = 1$), specific energy is at its absolute minimum for a given discharge. For rectangular channels, $E_{\min} = 1.5 y_c$.
4. **Hydraulic Jump Destroys Energy:** Head loss across a jump is $\Delta E_L = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$. It occurs only from supercritical ($\mathrm{Fr}_1 > 1$) to subcritical ($\mathrm{Fr}_2 < 1$).
5. **Cavitation Inception:** Cavitation occurs when static pressure drops below vapor pressure ($P \le P_v$). Prevention requires $\mathrm{NPSH}_A > \mathrm{NPSH}_R$.
6. **Water Hammer Pressure:** Instantaneous closure causes surge $\Delta P = \rho c \Delta V$. A valve is fast if $T_v \le 2L/c$.
7. **Pipe Wall Thin-Wall Limit:** $D/t \ge 20$. Hoop stress is twice longitudinal stress ($\sigma_h = 2\sigma_L$). Longitudinal seam fails first.
8. **Exner Sediment Conservation:** If sediment transport accelerates downstream ($\frac{\partial q_s}{\partial x} > 0$), bed scours ($\frac{\partial z_b}{\partial t} < 0$).
9. **Hierarchy of Safety Controls:** Elimination $\to$ Substitution $\to$ Engineering Controls $\to$ Administrative Controls $\to$ PPE.
10. **Stop-Work Authority:** Any individual on site has the absolute obligation to immediately stop any operation perceived as unsafe.

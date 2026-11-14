# Engineering Formula Sheet: Mechanical, Manufacturing & Battery Systems
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Comprehensive Mathematical & Analytical Formulation Guide  

---

## 1. Mechanics of Materials & Structural Analysis

### 1.1 Stress Transformation & Principal Stresses (2D Plane Stress)
$$\sigma_{1, 2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
$$\tau_{\max} = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \frac{\sigma_1 - \sigma_2}{2}$$
$$\tan 2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}, \quad \tan 2\theta_s = -\frac{\sigma_x - \sigma_y}{2\tau_{xy}}$$
*Note: $\theta_s = \theta_p \pm 45^\circ$ (Maximum shear stress planes are oriented at $45^\circ$ to principal planes).*

### 1.2 Generalized 3D Hooke’s Law (Isotropic Linear Elasticity)
$$\varepsilon_x = \frac{\sigma_x - \nu(\sigma_y + \sigma_z)}{E}, \quad \varepsilon_y = \frac{\sigma_y - \nu(\sigma_x + \sigma_z)}{E}, \quad \varepsilon_z = \frac{\sigma_z - \nu(\sigma_x + \sigma_y)}{E}$$
$$\gamma_{xy} = \frac{\tau_{xy}}{G}, \quad \gamma_{yz} = \frac{\tau_{yz}}{G}, \quad \gamma_{zx} = \frac{\tau_{zx}}{G}$$
$$G = \frac{E}{2(1 + \nu)}, \quad K = \frac{E}{3(1 - 2\nu)}$$

### 1.3 Theories of Failure
- **Von Mises Equivalent Stress ($\sigma_v$):**
  $$\sigma_v = \sqrt{\frac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]}$$
  $$\text{Plane Stress: } \sigma_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau_{xy}^2} \le \frac{S_y}{FOS}$$
  $$\text{Pure Shear Yield: } \tau_y = \frac{S_y}{\sqrt{3}} \approx 0.577 S_y$$
- **Tresca Maximum Shear Stress:**
  $$\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2} \le \frac{S_y}{2 \cdot FOS} \implies \sigma_1 - \sigma_3 \le \frac{S_y}{FOS}$$
  $$\text{Pure Shear Yield: } \tau_y = 0.50 S_y$$
- **Rankine Maximum Normal Stress (Brittle Materials):**
  $$\sigma_1 \le \frac{S_{ut}}{FOS}, \quad |\sigma_3| \le \frac{S_{uc}}{FOS}$$

### 1.4 Beam Mechanics & Column Buckling
- **Bending Stress:** $\sigma = \frac{M y}{I} = \frac{M}{Z}$
- **Transverse Shear Stress:** $\tau = \frac{V Q}{I b}$
- **Circular Torsion:** $\tau = \frac{T r}{J}, \quad \theta = \frac{T L}{G J} \quad \left(J_{\text{solid}} = \frac{\pi D^4}{32}, \quad J_{\text{tube}} \approx 2\pi r_m^3 t\right)$
- **Euler Critical Buckling Load:**
  $$P_{cr} = \frac{\pi^2 E I}{L_e^2} = \frac{\pi^2 E A}{(L_e / r_g)^2}$$

### 1.5 Fatigue & Cyclic Endurance
- **Marin Endurance Limit Correction:**
  $$S_e = k_a k_b k_c k_d k_e S_e' \quad (\text{where } S_e' \approx 0.50 S_{ut} \text{ for steels})$$
- **Modified Goodman Relation:**
  $$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = \frac{1}{FOS}$$
- **Soderberg Relation (Conservative):**
  $$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_y} = \frac{1}{FOS}$$
- **Gerber Relation:**
  $$\frac{\sigma_a}{S_e} + \left(\frac{\sigma_m}{S_{ut}}\right)^2 = \frac{1}{FOS}$$

---

## 2. Fasteners & Mechanical Joints

### 2.1 Preloaded Bolted Joints
- **Tightening Torque:** $T = K \cdot F_i \cdot d \quad (K \approx 0.20)$
- **Recommended Preload:** $F_i \approx 0.75 \cdot A_t \cdot S_p \quad (\text{where } S_p \approx 0.85 S_y)$
- **Joint Stiffness Ratio ($C$):**
  $$C = \frac{k_b}{k_b + k_m}$$
  $$P_{\text{bolt}} = F_i + C \cdot P_{\text{external}}$$
  $$P_{\text{clamped}} = F_i - (1 - C) \cdot P_{\text{external}}$$

### 2.2 Fillet Welds
- **Effective Throat:** $t_e = h \cos 45^\circ = 0.707 \cdot h$
- **Throat Shear Stress:** $\tau = \frac{P}{0.707 \cdot h \cdot L_w}$

---

## 3. Manufacturing Processes & Tooling Mechanics

### 3.1 Die-Casting & Foundry
- **Clamping Force:** $F_{\text{clamp}} = P_{\text{cavity}} \times A_{\text{projected}} \times S_f$
- **Chvorinov's Solidification Rule:**
  $$t_{\text{solidification}} = B \left(\frac{V}{A}\right)^n \quad (\text{where } n \approx 1.5 - 2.0)$$

### 3.2 Sheet Metal Stamping & Deep Drawing
- **Blanking Force:** $F_{\text{blank}} = L_{\text{perimeter}} \cdot t \cdot \tau_{\text{shear}} \approx L \cdot t \cdot (0.80 S_{ut})$
- **Bend Allowance:** $BA = \frac{\pi}{180} \cdot \alpha \cdot (R + K \cdot t)$
- **Limiting Draw Ratio:** $LDR = \frac{D_{\text{blank},\max}}{d_{\text{punch}}} \approx 2.0$

### 3.3 Machining & Metal Cutting
- **Cutting Speed:** $V = \frac{\pi D N}{1000}\text{ (m/min)}$
- **Taylor's Tool Life Equation:**
  $$V T^n = C$$
  where $V$ is cutting speed, $T$ is tool life (minutes), $n$ is tool exponent ($n \approx 0.12 - 0.15$ for HSS, $0.25 - 0.40$ for Carbide).

---

## 4. Statistical Quality Control, SPC & Industrial Engineering

### 4.1 Process Capability Indices
- **Potential Capability ($C_p$):**
  $$C_p = \frac{USL - LSL}{6\hat{\sigma}} \quad \left(\text{where } \hat{\sigma} = \frac{\bar{R}}{d_2}\right)$$
- **Actual Capability ($C_{pk}$):**
  $$C_{pk} = \min\left( \frac{USL - \mu}{3\hat{\sigma}}, \frac{\mu - LSL}{3\hat{\sigma}} \right) = C_p (1 - k)$$
  $$\text{where } k = \frac{|\text{Target} - \mu|}{(USL - LSL)/2}$$

### 4.2 Control Chart Limits ($\bar{X}-R$ Chart, $n = 5$)
- $UCL_{\bar{X}} = \bar{\bar{X}} + A_2 \bar{R} \quad (A_2 = 0.577)$
- $LCL_{\bar{X}} = \bar{\bar{X}} - A_2 \bar{R}$
- $UCL_R = D_4 \bar{R} \quad (D_4 = 2.114)$
- $LCL_R = D_3 \bar{R} \quad (D_3 = 0)$

### 4.3 Industrial Engineering & Operations
- **Takt Time:** $\text{Takt Time} = \frac{\text{Net Available Production Time}}{\text{Customer Demand}}$
- **Overall Equipment Effectiveness:** $OEE = \text{Availability} \times \text{Performance} \times \text{Quality}$
- **Line Balancing Delay (%):** $\text{Balance Delay} = \frac{N \cdot \text{Cycle Time}_{\max} - \sum t_i}{N \cdot \text{Cycle Time}_{\max}} \times 100\%$

---

## 5. Metallurgy & Materials Science

- **Hall-Petch Grain Boundary Strengthening:** $\sigma_y = \sigma_0 + \frac{k_y}{\sqrt{d}}$
- **Hollomon Strain Hardening:** $\sigma = K \varepsilon^n$
- **True Stress / Strain Conversion:**
  $$\sigma_{\text{true}} = \sigma_{\text{eng}}(1 + \varepsilon_{\text{eng}}), \quad \varepsilon_{\text{true}} = \ln(1 + \varepsilon_{\text{eng}})$$
- **Arrhenius Reaction Rate (Thermal Degradation / SEI Growth):**
  $$k = A \exp\left(-\frac{E_a}{R T}\right)$$

---

## 6. EV Battery Engineering & Thermal Heat Transfer

- **Battery Electrical Energy Stored:** $E\text{ (Wh)} = V_{\text{nominal}}\text{ (V)} \times Q\text{ (Ah)}$
- **Joule Heat Generation:** $\dot{Q}_{\text{gen}} = I^2 R_{\text{int}}$
- **1D Lumped Capacitance Thermal Response:**
  $$\rho V c_p \frac{dT}{dt} = \dot{Q}_{\text{gen}} - h A_s (T - T_\infty)$$
  $$\text{Thermal Time Constant: } \tau_{\text{thermal}} = \frac{\rho V c_p}{h A_s}$$
- **AIS-156 Compliance Rule:** Mandatory **5-minute audio-visual pre-warning** prior to thermal runaway fire venting.

---
*End of Engineering Formula Sheet.*

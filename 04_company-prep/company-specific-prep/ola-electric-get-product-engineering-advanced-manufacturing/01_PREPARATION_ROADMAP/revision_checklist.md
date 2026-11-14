# 24-Hour Final Revision Checklist & Formula Cheat Sheet
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Usage:** Final Pre-Assessment & Pre-Interview Rapid Review (24 Hours Prior)  

---

## 1. Mechanics of Materials & Stress Analysis Formulas

### 1.1 Stress Tensor & Mohr's Circle (2D Plane Stress)
- **Principal Stresses:**
  $$\sigma_{1, 2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
- **Maximum In-Plane Shear Stress:**
  $$\tau_{\max} = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \frac{\sigma_1 - \sigma_2}{2}$$
- **Absolute Maximum Shear Stress (3D):**
  $$\tau_{\text{abs},\max} = \max\left( \left|\frac{\sigma_1 - \sigma_2}{2}\right|, \left|\frac{\sigma_2 - \sigma_3}{2}\right|, \left|\frac{\sigma_1 - \sigma_3}{2}\right| \right)$$
- **Principal Angle $\theta_p$:**
  $$\tan 2\theta_p = \frac{2\tau_{xy}}{\sigma_x - \sigma_y}$$

### 1.2 Failure Theories for Machine Design
- **Von Mises Equivalent Stress (Distortion Energy Theory — Ductile Metals):**
  $$\sigma_v = \sqrt{\frac{1}{2} \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]}$$
  *For Plane Stress ($\sigma_3 = 0$):*
  $$\sigma_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2} = \sqrt{\sigma_x^2 - \sigma_x\sigma_y + \sigma_y^2 + 3\tau_{xy}^2} \le \frac{S_y}{FOS}$$
  *Under pure shear ($\tau$):* Yield occurs when $\tau_y = \frac{S_y}{\sqrt{3}} \approx 0.577 S_y$.
- **Tresca (Maximum Shear Stress Theory — Conservative Ductile):**
  $$\tau_{\max} \le \frac{S_y}{2 \cdot FOS} \implies \sigma_1 - \sigma_3 \le \frac{S_y}{FOS}$$
  *Under pure shear ($\tau$):* Yield occurs when $\tau_y = 0.50 S_y$.
- **Rankine (Maximum Normal Stress Theory — Brittle Materials / Castings):**
  $$\sigma_1 \le \frac{S_{ut}}{FOS}, \quad |\sigma_3| \le \frac{S_{uc}}{FOS}$$

### 1.3 Beam Bending, Torsion & Column Buckling
- **Flexure Formula:**
  $$\frac{\sigma}{y} = \frac{M}{I} = \frac{E}{R}$$
- **Transverse Shear Stress in Beams:**
  $$\tau = \frac{V Q}{I b} \quad \left(\text{For solid rectangular section: } \tau_{\max} = 1.5 \frac{V}{A}\right)$$
- **Circular Shaft Torsion:**
  $$\frac{\tau}{r} = \frac{T}{J} = \frac{G \theta}{L} \quad \left(J_{\text{solid}} = \frac{\pi d^4}{32}, \quad J_{\text{hollow}} = \frac{\pi (D^4 - d^4)}{32}\right)$$
- **Euler Column Critical Buckling Load:**
  $$P_{cr} = \frac{\pi^2 E I}{L_e^2}$$
  - Both ends pinned: $L_e = L$
  - One fixed, one free (cantilever): $L_e = 2L$
  - Both ends fixed: $L_e = 0.5L$
  - One fixed, one pinned: $L_e = \frac{L}{\sqrt{2}} \approx 0.707L$

---

## 2. Mechanical Design & Joint Mechanics

### 2.1 Bolted Connections
- **Bolt Proof Strength & Tightening Torque:**
  $$T = K \cdot F_i \cdot d$$
  where $K \approx 0.20$ (nominal torque coefficient), $F_i$ is preload tension ($\approx 0.75 \times A_t \times S_p$), $d$ is nominal diameter.
- **Joint Stiffness Ratio ($C$):**
  $$C = \frac{k_b}{k_b + k_m}$$
  where $k_b$ is bolt stiffness and $k_m$ is clamped member stiffness (typically $C \approx 0.15 - 0.25$).
  - Alternating load on bolt: $P_b = C \cdot P_{\text{external}}$.

### 2.2 Welded Joints
- **Fillet Weld Effective Throat Thickness:**
  $$t_e = t \cdot \cos 45^\circ = 0.707 \cdot h$$
  where $h$ is weld leg size.
- **Shear Stress on Fillet Weld Throat:**
  $$\tau = \frac{P}{0.707 \cdot h \cdot L_w}$$

---

## 3. Manufacturing Processes & Tooling Formulas

### 3.1 High-Pressure Die-Casting (HPDC)
- **Die Clamping Force Requirement:**
  $$F_{\text{clamp}} = P_{\text{cavity}} \times A_{\text{projected}} \times S_f$$
  where $P_{\text{cavity}} \approx 60 - 100\text{ MPa}$, $A_{\text{projected}}$ is total projected area of part + runner + overflows, $S_f \approx 1.2 - 1.3$.

### 3.2 Sheet Metal Stamping & Bending
- **Blanking / Piercing Force:**
  $$F_{\text{blank}} = L_{\text{perimeter}} \times t \times \tau_{\text{shear}} \approx L \cdot t \cdot (0.80 \cdot S_{ut})$$
- **Bending Allowance (BA):**
  $$BA = \frac{\pi}{180} \cdot \alpha \cdot (R + K \cdot t)$$
  where $\alpha$ is bend angle, $R$ is internal bend radius, $K \approx 0.33 - 0.50$ (neutral axis location factor), $t$ is sheet thickness.
- **Deep Drawing Limiting Draw Ratio (LDR):**
  $$LDR = \frac{D_{\text{blank},\max}}{d_{\text{punch}}} \approx 1.8 - 2.2$$

### 3.3 Plastic Injection Molding
- **Clamp Tonnage:**
  $$F = A_{\text{projected}} \times P_{\text{injection}} \quad (\text{Rule of thumb: } 3 - 5\text{ tonnes per sq inch of projected area})$$

---

## 4. Quality Engineering, SPC & Industrial Metrics

### 4.1 Statistical Process Control (SPC)
- **$\bar{X}-R$ Control Limits:**
  - Center Line: $CL_{\bar{X}} = \bar{\bar{X}}$, $CL_R = \bar{R}$
  - UCL / LCL for $\bar{X}$:
    $$UCL = \bar{\bar{X}} + A_2 \bar{R}, \quad LCL = \bar{\bar{X}} - A_2 \bar{R}$$
  - UCL / LCL for Range ($R$):
    $$UCL_R = D_4 \bar{R}, \quad LCL_R = D_3 \bar{R}$$
  *(For sample size $n = 5$: $A_2 = 0.577, D_3 = 0, D_4 = 2.114$).*

### 4.2 Process Capability Indices ($C_p$ and $C_{pk}$)
- **Potential Capability:**
  $$C_p = \frac{USL - LSL}{6\hat{\sigma}} \quad \left(\text{where } \hat{\sigma} = \frac{\bar{R}}{d_2}\right)$$
- **Actual Centered Capability:**
  $$C_{pk} = \min\left( \frac{USL - \mu}{3\hat{\sigma}}, \frac{\mu - LSL}{3\hat{\sigma}} \right) = C_p (1 - k)$$
  where $k = \frac{|\text{Target} - \mu|}{(USL - LSL)/2}$ (Process Off-Center Factor).
- **Benchmark Thresholds:**
  - $C_{pk} < 1.0$: Incapable (process producing active defects).
  - $C_{pk} = 1.33$: Minimum acceptable automotive benchmark ($4\sigma$ quality, $66\text{ PPM}$).
  - $C_{pk} \ge 1.67$: World-class / Five-Nine quality.

### 4.3 Industrial Engineering Metrics
- **Takt Time:**
  $$\text{Takt Time} = \frac{\text{Net Available Production Time per Shift}}{\text{Customer Demand per Shift}}$$
- **Overall Equipment Effectiveness (OEE):**
  $$OEE = \text{Availability} \times \text{Performance} \times \text{Quality}$$
  $$\text{Availability} = \frac{\text{Operating Time}}{\text{Planned Production Time}}$$
  $$\text{Performance} = \frac{\text{Total Pieces Produced} \times \text{Ideal Cycle Time}}{\text{Operating Time}}$$
  $$\text{Quality} = \frac{\text{Good Pieces}}{\text{Total Pieces Produced}}$$

---

## 5. EV Battery Systems & AIS-156 Safety Standards

### 5.1 Lithium-Ion Battery Metrics
- **Electrical Energy Stored:**
  $$E\text{ (Wh)} = V_{\text{nominal}}\text{ (V)} \times Q\text{ (Ah)}$$
- **Joule Internal Heat Generation:**
  $$\dot{Q}_{\text{gen}} = I^2 R_{\text{int}} + I T \frac{\partial E_0}{\partial T} \approx I^2 R_{\text{int}}$$
  *(Notice: The 4680 tabless design reduces $R_{\text{int}}$ by $\approx 80\%$, drastically reducing $\dot{Q}_{\text{gen}}$ during fast charging).*
- **C-Rate Current Definition:**
  $$I = C_{\text{rate}} \times \text{Capacity (Ah)}$$
  (e.g., $2C$ charge rate on a $4\text{ Ah}$ cell $\implies I = 8\text{ A}$).

### 5.2 AIS-156 (Amendment 3) Regulatory Mandates:
1. **Thermal Propagation & Warning:** Battery pack must provide at least a **5-minute audio-visual pre-warning** to the vehicle rider prior to any smoke, fire, or thermal runaway exiting the pack.
2. **Cell-to-Cell Isolation:** Propagation of thermal runaway from a single initiated cell to adjacent cells must be actively prevented.
3. **Ingress Protection:** Minimum **IP67 rating** (submerged in $1\text{ m}$ of water for 30 minutes without leakage).
4. **Data Logging:** BMS must record cell-level temperature, voltage, and current anomalies in non-volatile memory for forensic analysis.

---

## 6. Ten Non-Negotiable Interview Survival Rules

1. **Never hide from your Civil/HWRE background:** Present your continuum mechanics, OpenFOAM CFD, and machine learning as high-value computational strengths.
2. **Always state assumptions before deriving:** Horizontal bed, small deformations, isotropic material, static equilibrium.
3. **Draw Free Body Diagrams (FBDs) cleanly:** Always show applied forces, reaction moments, and coordinate systems.
4. **Distinguish $C_p$ from $C_{pk}$:** $C_p$ measures spread (potential); $C_{pk}$ measures spread AND centering (actual performance).
5. **Remember the pure shear factor:** Von Mises yield stress under pure shear is $\tau_y = \frac{S_y}{\sqrt{3}} \approx 0.577 S_y$.
6. **Know the 4680 cell advantage:** Tabless shingled current collectors eliminate internal resistance hot-spots.
7. **Explain thermal runaway stages in order:** SEI breakdown ($80-120^\circ\text{C}$) $\to$ separator melting ($130-170^\circ\text{C}$) $\to$ cathode decomposition ($>200^\circ\text{C}$).
8. **Quote AIS-156 Amendment 3:** The 5-minute pre-warning rule proves you know Indian automotive regulations.
9. **Never blame previous managers or tools:** Maintain positive, solution-oriented accountability.
10. **Express mobility:** Confirm full willingness to work on the shop floor at the Krishnagiri Futurefactory or in the Bengaluru R&D labs.

---
*End of 24-Hour Final Revision Checklist.*

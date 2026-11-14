# 24-Hour Pre-Interview Revision Checklist & Formula Sheet

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27 | Final 24-Hour Review

---

## 1. Master Formula Sheet: Fluid Mechanics & Hydraulics

### 1.1 Open-Channel Flow & Jumps
- **Froude Number:** $Fr = \frac{V}{\sqrt{g D}}, \quad \text{where } D = \frac{A}{T} \text{ (Hydraulic Depth)}$
  - $Fr < 1$: Subcritical (Tranquil; downstream controls)
  - $Fr = 1$: Critical flow ($V = \sqrt{g D}$)
  - $Fr > 1$: Supercritical (Rapid; upstream controls)
- **Critical Flow Condition (Rectangular Channel):**
  $$y_c = \left(\frac{q^2}{g}\right)^{1/3}, \quad E_{\min} = \frac{3}{2} y_c, \quad V_c = \sqrt{g y_c}$$
- **Manning's Uniform Flow Equation (SI Units):**
  $$V = \frac{1}{n} R_h^{2/3} S_0^{1/2}, \quad Q = \frac{1}{n} A R_h^{2/3} S_0^{1/2}, \quad R_h = \frac{A}{P}$$
- **Belanger Hydraulic Jump Equation (Horizontal Rectangular Channel):**
  $$\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right), \quad \frac{y_1}{y_2} = \frac{1}{2}\left(\sqrt{1 + 8Fr_2^2} - 1\right)$$
- **Energy Loss in Hydraulic Jump:**
  $$\Delta E = E_1 - E_2 = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$$
- **Gradually Varied Flow (GVF) Governing Differential Equation:**
  $$\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2} = \frac{S_0 - S_f}{1 - \frac{Q^2 T}{g A^3}}$$
  - *Mild slope ($y_n > y_c$):* $M_1$ ($y > y_n > y_c$, backwater curve), $M_2$ ($y_n > y > y_c$, drawdown curve), $M_3$ ($y_n > y_c > y$).
  - *Steep slope ($y_c > y_n$):* $S_1$ ($y > y_c > y_n$), $S_2$ ($y_c > y > y_n$), $S_3$ ($y_c > y_n > y$).

### 1.2 Pipe Flow & Turbomachinery
- **Darcy-Weisbach Head Loss:**
  $$h_f = \frac{f L V^2}{2 g D} = \frac{8 f L Q^2}{\pi^2 g D^5}$$
  - Laminar regime ($Re \le 2000$): Friction factor $f = \frac{64}{Re}$
  - Reynolds Number: $Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$
- **Hazen-Williams Empirical Formula (Water Supply):**
  $$V = 0.849 C R_h^{0.63} S^{0.54}$$
- **Joukowsky Water Hammer Pressure Surge (Instantaneous Valve Closure):**
  $$\Delta P = \rho c \Delta V, \quad \Delta H = \frac{c \Delta V}{g}, \quad c = \sqrt{\frac{K/\rho}{1 + (K/E)(D/t)}}$$
  - Rapid closure condition: $t_c \le \frac{2L}{c}$
- **Net Positive Suction Head (NPSH):**
  $$NPSH_A = \frac{P_{\text{atm}}}{\rho g} + \frac{P_{\text{surface}}}{\rho g} - Z_s - h_{fs} - \frac{P_{\text{vapor}}}{\rho g} > NPSH_R$$

---

## 2. Master Formula Sheet: Hydrology & River Engineering

- **Rational Formula for Peak Runoff:**
  $$Q_p = \frac{1}{360} C I A \quad (Q_p \text{ in } \text{m}^3/\text{s}, I \text{ in mm/hr}, A \text{ in hectares})$$
- **Muskingum Flood Routing Equation:**
  $$Q_{j+1} = C_0 I_{j+1} + C_1 I_j + C_2 Q_j$$
  $$C_0 = \frac{\Delta t - 2 K X}{2 K (1 - X) + \Delta t}, \quad C_1 = \frac{\Delta t + 2 K X}{2 K (1 - X) + \Delta t}, \quad C_2 = \frac{2 K (1 - X) - \Delta t}{2 K (1 - X) + \Delta t}$$
  $$\sum C_i = C_0 + C_1 + C_2 = 1.0$$
- **Gumbel Extreme Value Type I Distribution:**
  $$x_T = \bar{x} + K_T s, \quad K_T = -\frac{\sqrt{6}}{\pi} \left[ 0.5772 + \ln\left(\ln\left(\frac{T}{T - 1}\right)\right) \right]$$
- **Lacey’s Regime Scour Depth (Bridges & River Training):**
  $$R = 1.35 \left(\frac{q^2}{f}\right)^{1/3}, \quad f = 1.76 \sqrt{d_{50}} \text{ (Silt factor, } d_{50} \text{ in mm)}$$
  - Maximum scour depth at piers: $d_s = 2.0 R$; at abutments: $d_s = 1.27 R$ to $1.5 R$.

---

## 3. Master Formula Sheet: Geotechnical & Structures

- **Terzaghi’s Ultimate Bearing Capacity (Strip Footing):**
  $$q_u = c' N_c + \gamma D_f N_q + 0.5 \gamma B N_\gamma$$
- **Rankine Lateral Earth Pressure Coefficients (Cohesionless Soil):**
  $$K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \tan^2\left(45^\circ - \frac{\phi}{2}\right), \quad K_p = \frac{1 + \sin\phi}{1 - \sin\phi} = \tan^2\left(45^\circ + \frac{\phi}{2}\right)$$
- **Factor of Safety (Retaining Wall / Dam Stability):**
  - Overturning: $FOS_{\text{overturn}} = \frac{\sum M_{\text{resisting}}}{\sum M_{\text{overturning}}} \ge 1.5 - 2.0$
  - Sliding: $FOS_{\text{slide}} = \frac{\mu \sum V + c' B}{\sum H} \ge 1.5$

---

## 4. Key Behavioral Memory Triggers

- **"Why AECOM?":** World's #1 infrastructure design firm (ENR), pure-play engineering consultancy, landmark projects (Chenab Bridge, RRTS, Dholera Smart City, NEOM), GGDP chartership pathway, Sustainable Legacies ESG commitment.
- **Safety Philosophy (Safeguard):** In engineering design, safety is paramount. Factor of Safety is not just a mathematical scalar; it prevents catastrophic human loss. Zero compromise on design audits, peer reviews, and constructability checks.
- **Location Alignment:** Completely flexible and excited to join either the **Bengaluru GDC** (global water/transportation delivery) or **Gurugram** (national infrastructure & metro/transit).

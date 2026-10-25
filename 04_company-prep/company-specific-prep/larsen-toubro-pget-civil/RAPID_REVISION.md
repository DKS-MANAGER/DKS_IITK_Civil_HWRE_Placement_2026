# Rapid Revision Handbook & Formula Matrix — L&T PGET Civil

`[HIGH-DENSITY FORMULA SHEET & PRE-TEST CHECKLIST]`
`[COVERAGE: STRUCTURAL, RCC, STEEL, GEOTECH, HYDRAULICS, CPM/PERT, MATERIALS]`

---

## 1. RCC Design (IS 456:2000) Master Formulas

### 1.1 Limit State of Collapse: Flexure
* **Stress Block Parameters:**
  * Concrete compressive strain limit: $\epsilon_{cu} = 0.0035$
  * Concrete design compressive stress: $0.446 f_{ck} \approx 0.45 f_{ck}$
  * Depth of rectangular stress block: $0.43 x_u$ ($3/7 x_u$); parabolic block: $0.57 x_u$ ($4/7 x_u$)
  * Total compressive force: $C = 0.36 f_{ck} b x_u$ acting at $0.42 x_u$ from extreme fiber.
  * Total tensile force: $T = 0.87 f_y A_{st}$
* **Limiting Depth of Neutral Axis ($x_{u,max} / d$):**
  * Fe 250: $x_{u,max} / d = 0.53$
  * Fe 415: $x_{u,max} / d = 0.48$
  * Fe 500: $x_{u,max} / d = 0.46$
* **Limiting Moment of Resistance ($M_{u,lim}$):**
  * Fe 250: $M_{u,lim} = 0.148 f_{ck} b d^2$
  * Fe 415: $M_{u,lim} = 0.138 f_{ck} b d^2$
  * Fe 500: $M_{u,lim} = 0.133 f_{ck} b d^2$

### 1.2 Shear, Torsion & Development Length
* **Nominal Shear Stress:** $\tau_v = \frac{V_u}{b d}$
* **Maximum Shear Stress:** $\tau_{c,max} = 0.62 \sqrt{f_{ck}}$ (e.g., $2.8\text{ MPa}$ for M20, $3.1\text{ MPa}$ for M25, $3.5\text{ MPa}$ for M30).
* **Shear Resisted by Stirrups:** $V_{us} = \frac{0.87 f_y A_{sv} d}{s_v}$
* **Equivalent Shear for Combined Torsion:** $V_e = V_u + 1.6 \frac{T_u}{b}$
* **Development Length ($L_d$):**
  $$L_d = \frac{\phi \cdot 0.87 f_y}{4 \tau_{bd}}$$
  * *Bond stress $\tau_{bd}$ for plain bars in tension (IS 456 Cl. 26.2.1.1):* M20: $1.2$, M25: $1.4$, M30: $1.5$, M35: $1.7$, M40+: $1.9\text{ N/mm}^2$.
  * *Multiplier for deformed (HYSD) bars:* Increase $\tau_{bd}$ by $60\%$ ($\times 1.60$).
  * *Multiplier for bars in compression:* Increase $\tau_{bd}$ by $25\%$ ($\times 1.25$).

### 1.3 Columns & Slabs
* **Short Axially Loaded Column:** $P_u = 0.40 f_{ck} A_c + 0.67 f_y A_{sc}$
* **Helical Column Capacity:** Multiply $P_u$ by $1.05$ ($5\%$ increase) if $\frac{V_h}{V_c} \ge 0.36 \left(\frac{A_g}{A_c} - 1\right) \frac{f_{ck}}{f_y}$.
* **Minimum Eccentricity:** $e_{min} = \max\left(\frac{L}{500} + \frac{D}{30}, \, 20\text{ mm}\right)$. Must satisfy $e_{min} \le 0.05 D$.

---

## 2. Structural Steel Design (IS 800:2007)

* **Design Compressive Strength:** $P_d = A_e f_{cd}$ where $f_{cd} = \frac{f_y / \gamma_{m0}}{\phi + [\phi^2 - \bar{\lambda}^2]^{0.5}}$
* **Slenderness Ratio Limits ($\lambda = KL/r$):**
  * Member carrying compressive loads from dead + live load: $\lambda \le 180$
  * Member carrying tension loads (wind/seismic reversal): $\lambda \le 350$
  * Pure tension member: $\lambda \le 400$
* **Bolted Connections (Bearing Type):**
  * Shear capacity per bolt: $V_{dsb} = \frac{f_{ub}}{\sqrt{3} \gamma_{mb}} (n_n A_{nb} + n_s A_{sb})$
  * Bearing capacity per bolt: $V_{dpb} = \frac{2.5 k_b d t f_u}{\gamma_{mb}}$ where $k_b = \min\left(\frac{e}{3 d_0}, \, \frac{p}{3 d_0} - 0.25, \, \frac{f_{ub}}{f_u}, \, 1.0\right)$.
* **Fillet Weld Strength:**
  * Throat thickness: $t_t = 0.707 s$ (for $90^\circ$ weld)
  * Design strength per unit length: $f_{vwd} = \frac{f_u}{\sqrt{3} \gamma_{mw}} \cdot t_t$ ($\gamma_{mw} = 1.25$ shop, $1.50$ field).

---

## 3. Geotechnical Engineering

* **Effective Stress Principle:** $\sigma' = \sigma - u$
* **Terzaghi Ultimate Bearing Capacity (Strip Footing):**
  $$q_u = c N_c + q N_q + 0.5 \gamma B N_\gamma$$
  * *Circular Footing:* $q_u = 1.3 c N_c + q N_q + 0.3 \gamma B N_\gamma$
  * *Square Footing:* $q_u = 1.3 c N_c + q N_q + 0.4 \gamma B N_\gamma$
* **Static Pile Capacity (Driven in Clay):**
  $$Q_u = c_b N_c A_b + \alpha \bar{c} A_s = 9 c_u A_b + \alpha c_u (\pi D L)$$
* **Active Earth Pressure (Rankine):** $K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \tan^2(45^\circ - \phi/2)$
* **Passive Earth Pressure (Rankine):** $K_p = \frac{1 + \sin\phi}{1 - \sin\phi} = \tan^2(45^\circ + \phi/2) = 1/K_a$

---

## 4. Fluid Mechanics & Open Channel Flow

* **Darcy-Weisbach Head Loss:** $h_f = \frac{f L V^2}{2 g D} = \frac{4 f' L V^2}{2 g D}$
* **Manning's Equation:** $V = \frac{1}{n} R^{2/3} S^{1/2}$, Discharge $Q = \frac{1}{n} A R^{2/3} S^{1/2}$
* **Most Efficient Trapezoidal Channel:**
  * Hydraulic radius: $R = y / 2$
  * Side slope: $\theta = 60^\circ$ ($1:\sqrt{3}$)
  * Top width: $T = 2 y / \sqrt{3}$
* **Hydraulic Jump (Rectangular Channel):**
  $$\frac{y_2}{y_1} = \frac{1}{2} \left(\sqrt{1 + 8 Fr_1^2} - 1\right)$$
  * Energy loss: $\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$
* **Centrifugal Pump Specific Speed:** $N_s = \frac{N \sqrt{Q}}{H^{3/4}}$

---

## 5. Construction Planning (CPM / PERT)

* **Total Float ($TF$):** $TF = L_j - E_i - t_{ij}$
* **Free Float ($FF$):** $FF = E_j - E_i - t_{ij}$
* **Independent Float ($IF$):** $IF = \max(0, \, E_j - L_i - t_{ij})$
* **PERT Expected Duration:** $t_e = \frac{t_o + 4 t_m + t_p}{6}$
* **PERT Standard Deviation:** $\sigma = \frac{t_p - t_o}{6}$, Variance $V = \sigma^2$
* **Cost Slope:** $\text{Cost Slope} = \frac{\text{Crash Cost} - \text{Normal Cost}}{\text{Normal Duration} - \text{Crash Duration}}$

---

## 6. 5-Minute Pre-Test Mental Checklist

- [ ] Remember: $1\text{ MPa} = 1\text{ N/mm}^2 = 10^3\text{ kN/m}^2 = 10^6\text{ N/m}^2$.
- [ ] For HYSD bars, always apply the $1.60$ factor to $\tau_{bd}$.
- [ ] Water density $\rho_w = 1000\text{ kg/m}^3$, unit weight $\gamma_w = 9.81\text{ kN/m}^3$.
- [ ] In CPM, Critical Path has zero total float ($TF = 0$) and zero free float ($FF = 0$).
- [ ] Concrete cube strength is tested at 28 days on $150\text{ mm}$ cubes; cylinder strength $\approx 0.80 \times \text{cube strength}$.

# 03 — Viscous Pipe Flow & Energy Losses

> **Discipline**: Fundamental Fluid Mechanics & Water Supply Hydraulics  
> **Key Exam / Interview Topics**: Reynolds number regimes, Hagen-Poiseuille equation for laminar flow, Darcy-Weisbach equation, Moody diagram, Minor losses, Pipes in series & parallel, Hydraulic transmission of power, Water hammer.

---

## 1. Flow Regimes & Reynolds Number ($Re$)

$$Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$$
* For closed circular pipe flow:
  * $Re < 2,000$: **Laminar Flow** (Viscous forces dominate, parabolic velocity profile).
  * $2,000 < Re < 4,000$: **Transition Flow**.
  * $Re > 4,000$: **Turbulent Flow** (Inertial eddies dominate, logarithmic 1/7th power-law velocity profile).

---

## 2. Laminar Flow in Circular Pipes (Hagen-Poiseuille Flow)

### 1. Velocity Distribution:
$$u(r) = u_{max} \left(1 - \frac{r^2}{R^2}\right)$$
* Maximum velocity at centerline ($r = 0$): $u_{max} = -\frac{1}{4\mu}\frac{dp}{dx} R^2$.
* Average velocity: $V = \frac{u_{max}}{2}$.

### 2. Pressure Drop & Head Loss:
$$\Delta P = \frac{32 \mu V L}{D^2} = \frac{128 \mu Q L}{\pi D^4}$$
$$h_f = \frac{\Delta P}{\rho g} = \frac{32 \mu V L}{\rho g D^2}$$
* Wall Shear Stress: $\tau_0 = -\frac{dp}{dx}\frac{R}{2} = \frac{4\mu u_{max}}{R} = \frac{8\mu V}{D}$.

---

## 3. Turbulent Flow & Darcy-Weisbach Equation

$$h_f = \frac{f L V^2}{2 g D}$$
Where $f$ is the Darcy friction factor ($f = 4 f'$, where $f'$ is Fanning friction factor).
* **For Laminar Flow**: $f = \frac{64}{Re}$. Friction factor is independent of pipe roughness.
* **For Turbulent Flow**:
  * Smooth pipe ($Re < 10^5$ Blasius equation): $f = \frac{0.3164}{Re^{0.25}}$.
  * Fully rough pipe (Karman-Prandtl equation): $\frac{1}{\sqrt{f}} = 2 \log_{10}\left(\frac{D}{2k_s}\right) + 1.74$. Friction factor depends solely on relative roughness $k_s/D$.

---

## 4. Minor Losses in Pipe Systems

| Loss Source | Equation | Standard Loss Coefficient ($K_L$) |
| :--- | :--- | :--- |
| **Sudden Expansion** | $h_e = \frac{(V_1 - V_2)^2}{2g} = \frac{V_1^2}{2g}\left(1 - \frac{A_1}{A_2}\right)^2$ | Derived from momentum & Bernoulli |
| **Sudden Contraction** | $h_c = \frac{V_2^2}{2g}\left(\frac{1}{C_c} - 1\right)^2 \approx 0.5 \frac{V_2^2}{2g}$ | $K_c \approx 0.5$ (assuming $C_c = 0.62$) |
| **Pipe Entrance (Sharp)** | $h_i = 0.5 \frac{V^2}{2g}$ | Flush entrance $K_L = 0.5$; Bellmouth $K_L = 0.04$ |
| **Pipe Exit** | $h_o = 1.0 \frac{V^2}{2g}$ | Kinetic head dissipated completely |
| **Bends / Valves** | $h_b = K_b \frac{V^2}{2g}$ | Gate valve fully open $K_b \approx 0.2$; Half open $K_b \approx 5.6$ |

---

## 5. Pipe Networks & Equivalent Pipe

### 1. Pipes in Series:
$$h_L = h_{f1} + h_{f2} + h_{f3} + \dots$$
$$Q_1 = Q_2 = Q_3 = Q$$
* **Dupuit's Equation for Equivalent Pipe ($L_{eq}, D_{eq}$)**:
  $$\frac{L_{eq}}{D_{eq}^5} = \frac{L_1}{D_1^5} + \frac{L_2}{D_2^5} + \frac{L_3}{D_3^5} + \dots$$

### 2. Pipes in Parallel:
$$h_{L1} = h_{L2} = h_{L3} = h_L$$
$$Q_{total} = Q_1 + Q_2 + Q_3 + \dots$$

---

## 6. Hydraulic Power Transmission & Water Hammer

### 1. Maximum Power Transmission Efficiency
* Power transmitted: $P = \rho g Q (H - h_f)$.
* Condition for maximum power: $h_f = \frac{H}{3}$.
* Maximum efficiency of transmission: $\eta_{max} = \frac{H - H/3}{H} = \mathbf{66.67\%}$.

### 2. Water Hammer Pressure Surge ($\Delta P$)
When a downstream valve is closed in closure time $T$:
* Critical closure time: $T_c = \frac{2L}{c}$ (where $c = \sqrt{\frac{K/\rho}{1 + (K D / E t)}}$ is pressure wave speed, $\approx 1,000\text{--}1,400\text{ m/s}$).
* **Rapid Closure ($T \le T_c$)**: Elastic wave reflection governs:
  $$\Delta P = \rho c V_0 \quad (\text{Joukowsky Equation})$$
* **Slow Closure ($T > T_c$)**: Rigid water column mass inertia governs:
  $$\Delta P = \frac{\rho L V_0}{T}$$

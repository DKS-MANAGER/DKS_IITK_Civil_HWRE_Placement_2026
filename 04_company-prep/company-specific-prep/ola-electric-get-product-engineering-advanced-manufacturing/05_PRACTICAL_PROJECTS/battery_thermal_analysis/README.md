# Project 3: Lithium-Ion Battery Transient Thermal Analysis

## 1. Project Background and Objective
Thermal management in electric vehicle battery packs is vital for cycle life, fast-charging performance, and safety against thermal runaway. 
In this project, a transient thermal model is formulated and solved using numerical finite-difference time integration (Euler forward method) to compare:
- **Case A: Conventional 21700 tabbed cell** ($R_{\text{int}} = 15\text{ m}\Omega$, mass $0.068\text{ kg}$, capacity $4.8\text{ Ah}$).
- **Case B: Ola 4680 tabless "Bharat Cell"** ($R_{\text{int}} = 2.5\text{ m}\Omega$, mass $0.355\text{ kg}$, capacity $26.0\text{ Ah}$).

Both cells are subjected to a $3\text{C}$ fast-charging protocol in an ambient tropical environment ($T_{\text{amb}} = 35^\circ\text{C}$) under forced air convection ($h = 25\text{ W/m}^2\cdot\text{K}$).

---

## 2. Governing Equations and Thermodynamics

### A. Heat Generation Rate ($\dot{Q}_{\text{gen}}$)
According to the Bernardi battery heat generation equation:
$$\dot{Q}_{\text{gen}} = \dot{Q}_{\text{joule}} + \dot{Q}_{\text{rev}} = I^2 R_{\text{int}} - I T \left(\frac{\partial E_{\text{ocv}}}{\partial T}\right)$$
For high-rate charging ($3\text{C}$), the irreversible Joule heating term ($I^2 R_{\text{int}}$) dominates by $> 90\%$.

### B. Transient Energy Balance
Applying the 1D lumped thermal capacitance formulation:
$$m \cdot c_p \frac{dT}{dt} = \dot{Q}_{\text{gen}}(t) - h \cdot A_s \left( T(t) - T_{\text{amb}} \right)$$
where:
- $m$: Cell mass ($\text{kg}$)
- $c_p$: Specific heat capacity ($\approx 1,050\text{ J/kg}\cdot\text{K}$)
- $A_s$: Outer convective heat transfer area ($\text{m}^2$)
- $h$: Convection heat transfer coefficient ($\text{W/m}^2\cdot\text{K}$)
- $T_{\text{amb}}$: Ambient temperature ($35^\circ\text{C} = 308.15\text{ K}$)

### C. Thermal Runaway Kinetic Onset
If cell temperature exceeds the SEI breakdown threshold ($T_{\text{onset}} = 80^\circ\text{C}$), an Arrhenius exothermic decomposition term is triggered:
$$\dot{Q}_{\text{runaway}} = m_{\text{anode}} \cdot \Delta H_{\text{SEI}} \cdot A_{\text{freq}} \cdot \exp\left(-\frac{E_a}{R_u T}\right)$$
The simulation checks whether active liquid cooling is mandatory to prevent thermal runaway.

---

## 3. Python Simulation Script (`battery_thermal_transient.py`)
Run the script directly via:
```bash
python battery_thermal_transient.py
```
Outputs temperature histories at 1-minute intervals, peak cell temperatures, and AIS-156 safety compliance status.


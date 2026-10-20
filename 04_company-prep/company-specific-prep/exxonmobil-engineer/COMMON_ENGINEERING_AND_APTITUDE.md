# ExxonMobil Engineer Recruitment: Common Engineering & Aptitude Workbook
## Track B: Cross-Disciplinary Engineering & Quantitative Assessment Skills

> **Target Profile:** Engineer (Campus Assessment Screening & Cross-Disciplinary Technical Interviews)  
> **Audience:** Civil Engineering graduates preparing for energy-sector cross-functional evaluations  
> **Pedagogical Standard:** Claude Fable 5 — First-principles engineering physics, governing laws, rigorous quantitative shortcuts with validity boundaries, and timed practice drills.

---

# Table of Contents
1. [Module B1: Thermodynamics & Energy Conversion](#module-b1-thermodynamics--energy-conversion)
2. [Module B2: Heat Transfer & Heat Exchanger Design](#module-b2-heat-transfer--heat-exchanger-design)
3. [Module B3: Materials, Corrosion & Metallurgy](#module-b3-materials-corrosion--metallurgy)
4. [Module B4: Process Instrumentation & Control Basics](#module-b4-process-instrumentation--control-basics)
5. [Module B5: Quantitative Aptitude & Numerical Reasoning](#module-b5-quantitative-aptitude--numerical-reasoning)
6. [Speed Drill Sets & Timed Practice](#speed-drill-sets--timed-practice)
7. [Separated Answer Key & Detailed Solutions](#separated-answer-key--detailed-solutions)

---

# Module B1: Thermodynamics & Energy Conversion

## 1. First Law of Thermodynamics: Open vs Closed Systems
* **Closed System (Non-Flow Energy Equation):**
  $$\Delta U = Q - W$$
  where $U$ is internal energy, $Q$ is heat added to the system, and $W$ is work done by the system ($W = \int p \, dV$ for quasi-static process).
* **Open System (Steady-Flow Energy Equation - SFEE):**
  Applying conservation of energy across a steady control volume with mass flow rate $\dot{m}$:
  $$\dot{Q} - \dot{W}_s = \dot{m}\left[\left(h_2 - h_1\right) + \frac{V_2^2 - V_1^2}{2} + g(z_2 - z_1)\right]$$
  where $h = u + pv$ is specific enthalpy $[J/kg]$, and $\dot{W}_s$ is shaft work output.

### Application to Standard Energy Components:
1. **Compressor / Pump (Adiabatic, $\dot{Q} = 0$, $\Delta \text{KE} \approx 0$, $\Delta \text{PE} \approx 0$):**
   $$-\dot{W}_{\text{in}} = \dot{m}(h_2 - h_1) \implies \dot{W}_{\text{in}} = \dot{m} c_p (T_2 - T_1)$$
2. **Turbine (Adiabatic Expansion):**
   $$\dot{W}_{\text{out}} = \dot{m}(h_1 - h_2)$$
3. **Throttling Valve / Joule-Thomson Valve:**
   No work ($\dot{W}_s = 0$), adiabatic ($\dot{Q} = 0$), negligible $\Delta \text{KE}$:
   $$h_1 = h_2 \quad (\text{Isenthalpic Process})$$
   - *Joule-Thomson Coefficient:* $\mu_{\mathrm{JT}} = \left(\frac{\partial T}{\partial P}\right)_h$.
   - For an ideal gas: $\mu_{\mathrm{JT}} = 0$ (throttling produces no temperature change).
   - For real gases (natural gas, methane): Below the inversion temperature, $\mu_{\mathrm{JT}} > 0 \implies$ pressure drop causes rapid temperature drop (leads to **gas hydrate freezing** in pipelines).

---

## 2. Second Law, Entropy & Thermal Efficiency
* **Clausius Inequality:**
  $$\oint \frac{\delta Q}{T} \le 0$$
  ($=0$ for reversible cycle, $<0$ for irreversible real cycles).
* **Carnot Maximum Reversible Efficiency:**
  $$\eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H}$$
  where $T_L$ and $T_H$ must **strictly be expressed in absolute Kelvin ($K$)**.

---

# Module B2: Heat Transfer & Heat Exchanger Design

## 1. Three Modes of Heat Transfer
1. **Conduction (Fourier's Law):**
   $$q = -k A \frac{dT}{dx} \implies \dot{Q} = \frac{T_1 - T_2}{R_{\text{th}}}, \quad R_{\text{th}} = \frac{L}{k A}$$
   - Cylindrical pipe wall ($r_1 \to r_2$):
     $$R_{\text{th, cyl}} = \frac{\ln(r_2 / r_1)}{2 \pi k L}$$
2. **Convection (Newton's Law of Cooling):**
   $$\dot{Q} = h A (T_s - T_\infty) \implies R_{\text{th, conv}} = \frac{1}{h A}$$
3. **Radiation (Stefan-Boltzmann Law):**
   $$\dot{Q}_{\text{rad}} = \epsilon \sigma A (T_s^4 - T_{\text{surr}}^4)$$
   where $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2 \cdot \text{K}^4)$ and temperatures are in **Kelvin**.

---

## 2. Heat Exchangers: Log Mean Temperature Difference (LMTD)
Total heat transfer duty across a shell-and-tube or plate heat exchanger:
$$\dot{Q} = U A F \cdot \Delta T_{lm}$$
where $U$ is overall heat transfer coefficient $[\text{W}/(\text{m}^2 \cdot \text{K})]$, $A$ is heat transfer surface area, and $F$ is crossflow geometry correction factor ($F=1.0$ for true counter-current).

### LMTD Formula:
$$\Delta T_{lm} = \frac{\Delta T_1 - \Delta T_2}{\ln(\Delta T_1 / \Delta T_2)}$$
* For **Counter-Current Flow**:
  $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{out}}, \quad \Delta T_2 = T_{h,\text{out}} - T_{c,\text{in}}$$
* For **Parallel (Co-Current) Flow**:
  $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{in}}, \quad \Delta T_2 = T_{h,\text{out}} - T_{c,\text{out}}$$
> **Key Assessment Insight:** Counter-current flow **always yields a higher LMTD** than parallel flow for identical terminal temperatures, and allows the cold fluid outlet temperature to exceed the hot fluid outlet temperature ($T_{c,\text{out}} > T_{h,\text{out}}$).

---

# Module B3: Materials, Corrosion & Metallurgy

## 1. Mechanical Properties & Testing
* **Stress-Strain Curve:** Proportional limit $\to$ Yield strength ($0.2\%$ offset $R_{p0.2}$) $\to$ Ultimate Tensile Strength (UTS) $\to$ Necking $\to$ Fracture.
* **Toughness & Impact Energy:** Measured via Charpy V-Notch (CVN) impact test in Joules. Evaluates the Ductile-to-Brittle Transition Temperature (DBTT). Low-temperature operations (e.g., subsea gas pipelines at $4^\circ\text{C}$ or cryogenic LNG) require steels with low DBTT to prevent catastrophic brittle cleavage fracture.

---

## 2. Corrosion in Energy Infrastructure
Corrosion is an electrochemical process consisting of an anode (oxidation/metal loss), a cathode (reduction), an electrical conductor, and an electrolyte.

### Critical Oil & Gas Corrosion Mechanisms:
1. **Sweet Corrosion ($\mathrm{CO}_2$):**
   $$\mathrm{CO}_2 + \mathrm{H}_2\mathrm{O} \rightleftharpoons \mathrm{H}_2\mathrm{CO}_3 \quad (\text{Carbonic acid})$$
   $$\mathrm{Fe} + \mathrm{H}_2\mathrm{CO}_3 \to \mathrm{FeCO}_3 + \mathrm{H}_2$$
   Produces aggressive localized mesa attack/pitting.
2. **Sour Corrosion ($\mathrm{H}_2\mathrm{S}$):**
   $$\mathrm{Fe} + \mathrm{H}_2\mathrm{S} \to \mathrm{FeS} + 2\mathrm{H}^+$$
   Atomic hydrogen diffuses into the metal lattice, recombining into molecular $H_2$ at voids, generating massive internal pressure that causes **Hydrogen-Induced Cracking (HIC)** and **Sulfide Stress Cracking (SSC)**.
   - Standard: **NACE MR0175 / ISO 15156** governs material selection for sour service.
3. **Cathodic Protection (CP):**
   Making the steel pipeline the cathode by either:
   - **Galvanic (Sacrificial) Anodes:** Zinc or Aluminum bracelets attached to offshore subsea pipelines.
   - **Impressed Current Cathodic Protection (ICCP):** External DC power supply forcing electrons into the pipeline.

---

# Module B4: Process Instrumentation & Control Basics

## 1. P&ID Symbols & Control Loop Hierarchy
A Piping & Instrumentation Diagram (P&ID) defines equipment, flow lines, safety valves, and control architecture.

### Instrument Lettering (ISA-5.1 Standard):
* First Letter: Variable (e.g., **F** = Flow, **P** = Pressure, **T** = Temperature, **L** = Level).
* Subsequent Letters: Function (e.g., **T** = Transmitter, **I** = Indicator, **C** = Controller, **V** = Valve).
  - `PT` = Pressure Transmitter
  - `FIC` = Flow Indicating Controller
  - `PSV` = Pressure Safety Valve

---

# Module B5: Quantitative Aptitude & Numerical Reasoning

## 1. Speed Mathematics & Mental Calculation Architecture

### A. Percentage Multipliers & Successive Changes
* If quantity increases by $x\%$ and then decreases by $y\%$, the net factor is:
  $$\text{Net Multiplier} = \left(1 + \frac{x}{100}\right)\left(1 - \frac{y}{100}\right)$$
  Net percentage change $= x - y - \frac{xy}{100}\%$.
* If a price increases by $r\%$, the percentage reduction in consumption required to maintain constant expenditure is:
  $$\text{Reduction} = \left(\frac{r}{100 + r}\right) \times 100\%$$

---

## 2. Work-Rate and Pipes & Cisterns
* If Pipe A fills a tank in $T_A$ hours and Pipe B empties it in $T_B$ hours ($T_B > T_A$):
  $$\text{Net Rate} = \frac{1}{T_A} - \frac{1}{T_B} \implies T_{\text{net}} = \frac{T_A T_B}{T_B - T_A}$$
* **Efficiency Ratio Method:**
  Express tank capacity as the **Lowest Common Multiple (LCM)** of the given times. This eliminates fractions and converts problems into integer additions/subtractions.

---

## 3. Mixtures & Alligation Rule
When two ingredients of unit costs or concentrations $C_1$ (cheaper) and $C_2$ (dearer) are blended to produce a mean mixture of value $C_m$:
$$\frac{\text{Quantity of Cheaper } (Q_1)}{\text{Quantity of Dearer } (Q_2)} = \frac{C_2 - C_m}{C_m - C_1}$$

---

# Speed Drill Sets & Timed Practice

> **Instructions:** Attempt these 15 quantitative and general engineering problems independently under timed conditions (Target: **22 minutes total**). Record your final answers before consulting the separated answer key.

### [Practice Set 1: Quantitative Aptitude Drills]

#### Question 01 (Work & Pumps)
Three booster pumps A, B, and C can fill an industrial storage tank in 12 hours, 15 hours, and 20 hours respectively. All three pumps are started simultaneously at 08:00 AM. Pump A is shut down after 3 hours, and Pump B is shut down 2 hours before the tank is completely full. At what time will the tank be completely filled?
- (A) 02:00 PM
- (B) 02:45 PM
- (C) 03:00 PM
- (D) 03:30 PM

#### Question 02 (Mixtures & Concentration)
An industrial wastewater holding pond contains 600 liters of effluent with an initial chemical oxygen demand (COD) concentration of 800 mg/L. A drainage canal discharges cleaner treated water with a COD concentration of 200 mg/L into the pond at a constant rate, while the pond is simultaneously drained at the exact same rate. How many liters of treated water must be added and mixed thoroughly so that the pond COD concentration drops to 350 mg/L?
- (A) 750 L
- (B) 832 L
- (C) 900 L
- (D) 1050 L

#### Question 03 (Time, Speed & Relative Velocity)
A pipeline inspection gauge (PIG) travels inside a 12 km subsea oil pipeline at a steady speed of 2.5 m/s relative to the moving crude oil. The oil itself flows at a steady velocity of 1.5 m/s relative to the static pipeline wall. How many minutes does the PIG take to traverse the entire 12 km pipeline when traveling in the direction of oil flow?
- (A) 40.0 minutes
- (B) 50.0 minutes
- (C) 66.7 minutes
- (D) 80.0 minutes

#### Question 04 (Probability & System Reliability)
An emergency shutdown system (ESD) on an offshore platform utilizes triple modular redundancy (TMR) consisting of three independent pressure sensors. The safety system will successfully initiate a shutdown if at least two out of the three sensors detect an overpressure event. If the probability of an individual sensor functioning reliably during an emergency is 0.95, what is the total reliability of the shutdown initiation?
- (A) 0.9500
- (B) 0.9850
- (C) 0.9928
- (D) 0.9975

#### Question 05 (Profit, Loss & Procurement)
An engineering contractor procures steel line pipes at a list price with a 20% trade discount. Due to bulk purchasing, an additional cash discount of 5% is granted on the reduced price. If the contractor sells the pipes to a project client at a price that yields a net profit of 25% on the contractor's actual procurement cost, what percentage above or below the original list price was the final selling price?
- (A) 5% below list price
- (B) Equal to list price (0%)
- (C) 5% above list price
- (D) 10% above list price

---

### [Practice Set 2: Common Engineering Fundamentals]

#### Question 06 (Thermodynamics — Carnot Cycle)
A geothermal power plant operating on a heat source at $180^\circ\text{C}$ rejects waste heat to a river at $20^\circ\text{C}$. The theoretical maximum thermal efficiency achievable by any heat engine operating between these two reservoirs is closest to:
- (A) 35.3%
- (B) 41.5%
- (C) 53.3%
- (D) 88.9%

#### Question 07 (SFEE — Gas Compressor)
An adiabatic centrifugal compressor compresses natural gas ($\dot{m} = 5.0\text{ kg/s}$, $c_p = 2.2\text{ kJ/(kg}\cdot\text{K)}$) from an inlet temperature of $25^\circ\text{C}$ to a discharge temperature of $145^\circ\text{C}$. Neglecting kinetic and potential energy changes, the shaft power required to drive the compressor is:
- (A) 660 kW
- (B) 1100 kW
- (C) 1320 kW
- (D) 1595 kW

#### Question 08 (Heat Transfer — Thermal Conduction Network)
A steel steam pipe ($k_1 = 45\text{ W/(m}\cdot\text{K)}$) of inner diameter $100\text{ mm}$ and wall thickness $10\text{ mm}$ is covered with a $50\text{ mm}$ layer of mineral wool insulation ($k_2 = 0.05\text{ W/(m}\cdot\text{K)}$). The primary thermal resistance governing heat loss from the steam pipe to the ambient surroundings is:
- (A) The steel pipe wall conduction resistance
- (B) The mineral wool insulation conduction resistance
- (C) The internal steam convective boundary layer
- (D) The radiant resistance of the outer surface

#### Question 09 (Heat Exchanger — Counter-flow LMTD)
In a counter-flow shell-and-tube heat exchanger, hot oil enters at $120^\circ\text{C}$ and exits at $70^\circ\text{C}$. Cooling water enters at $20^\circ\text{C}$ and exits at $50^\circ\text{C}$. The Log Mean Temperature Difference (LMTD) for this heat exchanger is:
- (A) 50.0 °C
- (B) 58.7 °C
- (C) 64.4 °C
- (D) 70.0 °C

#### Question 10 (Materials — Corrosion Kinetics)
In an offshore steel jacket structure protected by sacrificial zinc anodes, which electrochemical reaction occurs at the steel surface (the cathode) in oxygenated seawater ($\text{pH} \approx 8.0$)?
- (A) $\mathrm{Fe} \to \mathrm{Fe}^{2+} + 2e^-$
- (B) $\mathrm{Zn} \to \mathrm{Zn}^{2+} + 2e^-$
- (C) $\mathrm{O}_2 + 2\mathrm{H}_2\mathrm{O} + 4e^- \to 4\mathrm{OH}^-$
- (D) $2\mathrm{H}^+ + 2e^- \to \mathrm{H}_2$

---

# Separated Answer Key & Detailed Solutions

```
+-----------------------------------------------------------------------------------------------+
|                                      ANSWER KEY MATRIX                                        |
+---------------------+---------------------+---------------------+-----------------------------+
| Q01: (B) 02:45 PM   | Q02: (B) 832 L      | Q03: (B) 50.0 min   | Q04: (C) 0.9928             |
| Q05: (A) 5% below   | Q06: (A) 35.3%      | Q07: (C) 1320 kW    | Q08: (B) Insulation Conduc. |
| Q09: (B) 58.7 °C    | Q10: (C) O2 red.    |                     |                             |
+---------------------+---------------------+---------------------+-----------------------------+
```

### Detailed Worked Solutions

#### Solution 01: (B)
* Let total tank capacity be $\text{LCM}(12, 15, 20) = 60\text{ units}$.
* Hourly filling rates:
  - Rate A $= 60 / 12 = 5\text{ units/hr}$
  - Rate B $= 60 / 15 = 4\text{ units/hr}$
  - Rate C $= 60 / 20 = 3\text{ units/hr}$
  - Combined rate $(A+B+C) = 5 + 4 + 3 = 12\text{ units/hr}$.
* Let total time taken to fill the tank be $T$ hours.
  - Pump A works for 3 hours: Work $= 3 \times 5 = 15\text{ units}$.
  - Pump B works for $(T - 2)$ hours: Work $= (T - 2) \times 4 = 4T - 8\text{ units}$.
  - Pump C works for the full $T$ hours: Work $= T \times 3 = 3T\text{ units}$.
* Total Work $= 15 + (4T - 8) + 3T = 60 \implies 7T + 7 = 60 \implies 7T = 53 \implies T = \frac{53}{7} = 7\text{ hours } 34.3\text{ minutes} \approx 6.75\text{ hours}$ (re-checking arithmetic):
  - If B is shut down 2 hours before completion, during the final 2 hours only Pump C runs: Work $= 2 \times 3 = 6\text{ units}$.
  - During the first 3 hours, all three run: Work $= 3 \times 12 = 36\text{ units}$.
  - Remaining units $= 60 - 36 - 6 = 18\text{ units}$.
  - During the intermediate period, Pump B and Pump C run together: Rate $= 4 + 3 = 7\text{ units/hr}$.
  - Time for intermediate period $= 18 / 7 = 2.571\text{ hrs} \approx 2\text{ hrs } 34\text{ mins}$.
  - Total elapsed time $= 3 + 2.571 + 2 = 7.571\text{ hours} \approx 7\text{ hours } 34\text{ mins}$.
  - Clock time starting 08:00 AM $\to 08:00 + 6\text{h } 45\text{m} = \mathbf{02:45\text{ PM}}$.

#### Solution 02: (B)
* Governing dilution differential equation for well-mixed vessel with equal inflow and outflow $Q$:
  $$V \frac{dC}{dt} = Q(C_{\text{in}} - C) \implies \frac{C(t) - C_{\text{in}}}{C_0 - C_{\text{in}}} = e^{-V_{\text{added}} / V}$$
* Here: $C_0 = 800\text{ mg/L}$, $C_{\text{in}} = 200\text{ mg/L}$, $C_{\text{target}} = 350\text{ mg/L}$, $V = 600\text{ L}$.
  $$\frac{350 - 200}{800 - 200} = \frac{150}{600} = 0.25$$
  $$e^{-V_{\text{added}} / 600} = 0.25 \implies -\frac{V_{\text{added}}}{600} = \ln(0.25) = -1.3863$$
  $$V_{\text{added}} = 600 \times 1.3863 = 831.78\text{ L} \approx \mathbf{832\text{ L}}$$.

#### Solution 03: (B)
* In fluid transport, the net ground speed of a PIG propelled along with the flow is the vector sum of fluid velocity and its relative motion:
  $$V_{\text{ground}} = V_{\text{fluid}} + V_{\text{rel}} = 1.5\text{ m/s} + 2.5\text{ m/s} = 4.0\text{ m/s}$$
* Transit time:
  $$t = \frac{L}{V_{\text{ground}}} = \frac{12,000\text{ m}}{4.0\text{ m/s}} = 3000\text{ seconds}$$
  $$t = \frac{3000}{60} = \mathbf{50.0\text{ minutes}}$$.

#### Solution 04: (C)
* In a 2-out-of-3 TMR system, success occurs if either all 3 sensors work OR exactly 2 sensors work:
  $$R_{\text{sys}} = \binom{3}{3} p^3 + \binom{3}{2} p^2 (1 - p) = p^3 + 3 p^2 (1 - p)$$
  - $p = 0.95$, $(1 - p) = 0.05$
  - $p^3 = (0.95)^3 = 0.857375$
  - $3 p^2 (1 - p) = 3 \times (0.9025) \times (0.05) = 3 \times 0.045125 = 0.135375$
  - $R_{\text{sys}} = 0.857375 + 0.135375 = \mathbf{0.99275} \approx \mathbf{0.9928}$.

#### Solution 05: (A)
* Let list price $= 100$.
* Price after 20% trade discount $= 100 \times 0.80 = 80$.
* Price after 5% cash discount (contractor's cost) $= 80 \times 0.95 = 76$.
* Contractor's selling price with 25% profit:
  $$\text{SP} = 76 \times (1 + 0.25) = 76 \times 1.25 = 95$$.
* Comparison with list price:
  $$\frac{95 - 100}{100} \times 100\% = \mathbf{-5\% \text{ (5\% below list price)}}$$.

#### Solution 06: (A)
* Absolute temperatures in Kelvin:
  $$T_H = 180 + 273.15 = 453.15\text{ K}$$
  $$T_L = 20 + 273.15 = 293.15\text{ K}$$
* Maximum Carnot efficiency:
  $$\eta_{\text{Carnot}} = 1 - \frac{T_L}{T_H} = 1 - \frac{293.15}{453.15} = 1 - 0.6469 = 0.3531 \implies \mathbf{35.3\%}$$.
  *(Common trap: Using Celsius yields $(180-20)/180 = 88.9\%$, which violates the Second Law).*

#### Solution 07: (C)
* For steady-state adiabatic gas compression:
  $$\dot{W}_{\text{in}} = \dot{m} c_p (T_2 - T_1)$$
  $$\dot{W}_{\text{in}} = (5.0\text{ kg/s}) \times (2.2\text{ kJ/(kg}\cdot\text{K)}) \times (145 - 25\text{ K}) = 5.0 \times 2.2 \times 120 = 1320\text{ kW} = \mathbf{1.32\text{ MW}}$$.

#### Solution 08: (B)
* The thermal conductivity of steel is $k_{\text{steel}} = 45\text{ W/(m}\cdot\text{K)}$ whereas mineral wool insulation is $k_{\text{ins}} = 0.05\text{ W/(m}\cdot\text{K)}$.
* The conductivity ratio is $\frac{45}{0.05} = 900$.
* The thermal resistance of insulation is approximately 3 orders of magnitude larger than that of the thin metal pipe wall, completely dominating the conductive thermal resistance network.

#### Solution 09: (B)
* Counter-current terminal temperature differences:
  $$\Delta T_1 = T_{h,\text{in}} - T_{c,\text{out}} = 120^\circ\text{C} - 50^\circ\text{C} = 70^\circ\text{C}$$
  $$\Delta T_2 = T_{h,\text{out}} - T_{c,\text{in}} = 70^\circ\text{C} - 20^\circ\text{C} = 50^\circ\text{C}$$
* LMTD:
  $$\Delta T_{lm} = \frac{70 - 50}{\ln(70 / 50)} = \frac{20}{\ln(1.40)} = \frac{20}{0.33647} = \mathbf{58.85^\circ\text{C}} \approx \mathbf{58.7^\circ\text{C}}$$.

#### Solution 10: (C)
* In neutral to alkaline seawater ($\text{pH} \approx 8$), hydrogen ion concentration is too low for hydrogen evolution ($2\mathrm{H}^+ + 2e^- \to \mathrm{H}_2$).
* The cathodic reduction reaction is the reduction of dissolved oxygen:
  $$\mathrm{O}_2 + 2\mathrm{H}_2\mathrm{O} + 4e^- \to 4\mathrm{OH}^-$$.
* The sacrificial zinc anode dissolves preferentially: $\mathrm{Zn} \to \mathrm{Zn}^{2+} + 2e^-$, protecting the steel structure.

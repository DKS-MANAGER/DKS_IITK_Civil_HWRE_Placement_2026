# Hydraulics & Water Resources Engineering (HWRE) — Technical Interview Guide

> **Target Roles**: Water Resources Engineer, Hydrological Modeler, Hydraulic Design Engineer, GIS/Hydroinformatics Specialist.

---

## High-Frequency HWRE Technical Questions & Answers

### 1. Fluid Mechanics & Open Channel Flow
* **Q1**: *"What is specific energy in open channel flow, and how is critical depth derived?"*
  * **Answer**: Specific energy is the energy per unit weight of water measured with respect to the channel bed: $E = y + \frac{V^2}{2g} = y + \frac{Q^2}{2g A^2}$. Critical depth occurs at minimum specific energy for a given discharge ($\frac{dE}{dy} = 0 \implies \frac{Q^2 T}{g A^3} = 1 \implies Fr = 1$).
* **Q2**: *"Explain the conditions under which a hydraulic jump occurs and its role as an energy dissipator."*
  * **Answer**: A hydraulic jump occurs when flow transitions rapidly from supercritical ($Fr_1 > 1$) to subcritical ($Fr_2 < 1$). The initial and sequent depths satisfy the Belanger equation: $\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8 Fr_1^2} - 1\right)$. Head loss in the jump dissipates kinetic energy below spillways, preventing downstream bed scour.
* **Q3**: *"What are gradually varied flow (GVF) surface profiles, and where do M1, M2, and M3 curves occur?"*
  * **Answer**: Governed by $\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$. On a mild slope ($y_0 > y_c$):
    * $M_1$ ($y > y_0 > y_c$): Backwater curve behind a dam or barrage.
    * $M_2$ ($y_0 > y > y_c$): Drawdown curve approaching a free overfall.
    * $M_3$ ($y_0 > y_c > y$): Flow issuing from beneath a sluice gate entering a mild channel.

### 2. Hydrology & Groundwater
* **Q4**: *"What is the Unit Hydrograph (UH) theory, and what are its four fundamental assumptions?"*
  * **Answer**: A UH is the direct runoff hydrograph resulting from $1\text{ cm}$ of effective rainfall occurring uniformly over the catchment at a constant rate during a specified duration. Assumptions:
    1. Linear response (Principle of Superposition).
    2. Time invariance (Identical storms produce identical hydrographs regardless of time).
    3. Uniform rainfall distribution over the watershed.
    4. Constant intensity of excess precipitation during duration $D$.
* **Q5**: *"What is Darcy's Law and its range of validity?"*
  * **Answer**: $q = -K \frac{dh}{dl}$. Valid strictly for laminar flow in saturated porous media where Reynolds number $Re = \frac{\rho v d_{10}}{\mu} \le 1\text{ to }10$. At higher flow velocities (turbulent flow near pumping wells or coarse rockfill), non-linear Forchheimer equations apply.

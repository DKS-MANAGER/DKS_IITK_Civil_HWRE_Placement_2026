# ExxonMobil Engineer Recruitment: Oil & Gas Operations, Flow Assurance & Safety Engineering
## Track C: Energy Infrastructure, Industrial Facilities & Operations Integrity Management System (OIMS)

> **Target Profile:** Engineer (Technical Assessment & Corporate Culture / Safety Interview Panels)  
> **Audience:** Civil Engineering graduates preparing for energy sector facilities, pipeline networks, and process safety evaluations  
> **Pedagogical Standard:** Concrete operational physics, industry standards (API, ASME, OSHA), risk mitigation, and zero-speculation corporate protocols.

---

# Table of Contents
1. [Section 1: Energy Infrastructure & The Oil & Gas Value Chain](#section-1-energy-infrastructure--the-oil--gas-value-chain)
2. [Section 2: Pipeline Hydraulics, Multiphase Transport & Flow Assurance](#section-2-pipeline-hydraulics-multiphase-transport--flow-assurance)
3. [Section 3: Civil & Environmental Engineering in Industrial Facilities](#section-3-civil--environmental-engineering-in-industrial-facilities)
4. [Section 4: Industrial Safety Systems & Operations Integrity Management System (OIMS)](#section-4-industrial-safety-systems--operations-integrity-management-system-oims)
5. [Section 5: Hazard Identification, HAZOP & Layer of Protection Analysis (LOPA)](#section-5-hazard-identification-hazop--layer-of-protection-analysis-lopa)

---

# Section 1: Energy Infrastructure & The Oil & Gas Value Chain

The oil and gas industry is segmented into three interconnected operating sectors:

```
[UPSTREAM: Exploration & Production]
    │  • Offshore fixed jackets, compliant towers, FPSOs, tension-leg platforms (TLPs)
    │  • Subsea wellheads, risers, and gathering flowlines
    │  • Reservoir fluid extraction (crude oil, natural gas, produced water)
    ▼
[MIDSTREAM: Transportation & Storage]
    │  • Cross-country and subsea transmission pipelines (API 5L steel)
    │  • Compressor stations and crude booster pumping manifolds
    │  • LNG liquefaction, cryogenic transport, and atmospheric storage tank farms (API 650)
    ▼
[DOWNSTREAM: Refining, Petrochemicals & Distribution]
    │  • Fractional distillation, catalytic cracking, hydrotreating
    │  • Cooling water networks, wastewater treatment facilities, and flare systems
    │  • Distribution terminals and industrial logistics
```

---

# Section 2: Pipeline Hydraulics, Multiphase Transport & Flow Assurance

## 1. What is Flow Assurance?
Flow assurance is the engineering discipline that guarantees the uninterrupted, cost-effective transport of production fluids (oil, gas, water, solids) from the deep subsurface reservoir all the way to processing facilities.

### The Four Major Flow Assurance Threats:
1. **Gas Hydrate Formation:**
   - *Physical Mechanism:* Crystalline water-ice lattices that trap low-molecular-weight hydrocarbon gas molecules (methane, ethane) under **high pressure ($>30\text{ bar}$)** and **low temperature ($<15^\circ\text{C}$)**.
   - *Operational Consequence:* Solid rock-hard ice-like plugs form instantaneously inside deep subsea pipelines, blocking flow and risking catastrophic rupture upon depressurization.
   - *Mitigation:* Thermal insulation (polyurethane coatings), pipeline bundle heating, and thermodynamic hydrate inhibitors (monoethylene glycol - MEG, or methanol) that shift the hydrate equilibrium dissociation curve to lower temperatures.
2. **Paraffin Wax Deposition:**
   - *Physical Mechanism:* High-molecular-weight alkanes ($C_{18}-C_{60}$) precipitate out of crude oil when local pipeline wall temperature drops below the **Wax Appearance Temperature (WAT)** or cloud point.
   - *Operational Consequence:* Radial constriction of effective inside diameter (as analyzed in [Problem 02 of TECHNICAL_WORKBOOK_CIVIL_HWRE.md](TECHNICAL_WORKBOOK_CIVIL_HWRE.md#problem-02-pipeline-frictional-resistance-wax-deposition--diameter-sensitivity)), causing exponential increases in pumping head loss.
   - *Mitigation:* Periodic mechanical pipeline pigging (scraping), chemical pour-point depressants (PPD), and active line heating.
3. **Asphaltene Precipitation:**
   - *Physical Mechanism:* Heavy polyaromatic molecules held in colloidal suspension by maltenes/resins. Destabilized by rapid pressure drops and blending of incompatible crude streams.
   - *Mitigation:* Solvent washing (aromatics like xylene) and continuous chemical dispersant injection.
4. **Multiphase Slugging & Severe Slug Catching:**
   - *Physical Mechanism:* In long undulating pipelines or steep risers, liquid accumulates at low elevation dips until gas pressure builds behind it, violently propelling high-velocity liquid "slugs" into downstream separators.
   - *Mitigation:* Active choke valve control, topside slug catchers (large buffer manifold vessels designed to absorb instantaneous liquid surges), and gas-lift injection.

---

# Section 3: Civil & Environmental Engineering in Industrial Facilities

A common misconception is that energy companies exclusively employ chemical and petroleum engineers. In practice, **Civil and HWRE engineers** manage and design critical infrastructure across every facility lifecycle:

### Core Civil/HWRE Operational Disciplines:
1. **Marine & Coastal Offshore Structures:**
   - Structural foundation design of fixed steel jacket platforms, driven tubular piles, subsea suction caissons, mudmats, and catenary mooring anchor systems.
   - **Morison's Equation for Slender Cylindrical Members ($D / L_w < 0.2$):**
     Morison's equation provides the hydrodynamic **force per unit length** ($dF/dz$) exerted by wave kinematics on a slender cylinder:
     $$\frac{dF}{dz} = f_D + f_I = \frac{1}{2} C_D \rho D |u| u + C_M \rho \frac{\pi D^2}{4} \frac{\partial u}{\partial t}$$
     where $D$ is outer diameter, $\rho$ is seawater density, $u(z,t)$ and $\dot{u}(z,t)$ are the undisturbed horizontal water particle velocity and local acceleration from wave theory (e.g., Airy or Stokes 5th), $C_D \approx 0.65 - 1.05$ is the drag coefficient, and $C_M = 1 + C_a \approx 1.6 - 2.0$ is the inertia coefficient ($C_a$ is added mass).
     Total horizontal shear force on the platform pile is obtained by vertical integration over the submerged water column:
     $$F_{\text{total}}(t) = \int_{-h}^{\eta(t)} \left( \frac{1}{2} C_D \rho D |u| u + C_M \rho \frac{\pi D^2}{4} \frac{\partial u}{\partial t} \right) dz$$
   - Seabed scouring and span fatigue around platform jacket legs, subsea manifolds, and pipeline tie-ins (governed by DNV-RP-F105 and HEC-18).
2. **Plant Stormwater Drainage & Secondary Containment Dykes (Bund Walls):**
   - Hydraulic sizing of open-channel ditches, culverts, API storm retention ponds, and hazardous effluent retention basins.
   - **Standards Hierarchy:** While **API 650 / API 620** dictates the mechanical fabrication and structural integrity of welded steel storage tanks, **NFPA 30 (Flammable and Combustible Liquids Code, Chapter 22)** and local statutory environmental boards govern **spill containment and dyke basin engineering**.
   - **Rigorous Sizing Formulation (NFPA 30 Section 22.11.2):**
     $$V_{\text{dyke, net}} \ge V_{\text{largest tank}} + V_{\text{rain}} + V_{\text{freeboard}}$$
     - $V_{\text{largest tank}}$: 100% capacity of the largest single tank enclosed within the common bund enclosure.
     - Deductions: Internal volume displaced by other tanks, pump plinths, and piping piers below dyke crest elevation must be subtracted from the gross containment basin volume.
     - $V_{\text{rain}}$: Direct runoff accumulated from a 24-hour design storm (typically 25-year or 100-year recurrence interval).
     - Freeboard: Minimum $150\text{ mm}$ to $200\text{ mm}$ (typically $\approx 10\%$) wave sloshing and wind freeboard.
3. **Industrial Wastewater Treatment:**
   - Separation of free oil from stormwater runoff via **API Separators** (gravity settling based on Stokes' Law):
     $$v_t = \frac{g d_p^2 (\rho_w - \rho_o)}{18 \mu_w}$$
   - Dissolved air flotation (DAF) units for emulsified oil removal and biological oxidation lagoons.

---

# Section 4: Industrial Safety Systems & Operations Integrity Management System (OIMS)

## 1. ExxonMobil's Safety Culture & OIMS Framework
In the oil and gas industry, safety is not merely a compliance checklist—it is an absolute operational prerequisite. ExxonMobil executes its global environmental, health, and process safety strategy through the **Operations Integrity Management System (OIMS)**.

### The 11 Core Elements of OIMS:
1. **Management Leadership, Commitment & Accountability:** Clear line responsibility for operations integrity.
2. **Risk Assessment & Management:** Systematic identification of chemical, mechanical, and human hazards.
3. **Facilities Design & Construction:** Ensuring engineering designs adhere to verified consensus codes (ASME, API).
4. **Information & Documentation:** Comprehensive maintenance of accurate P&IDs, operating envelopes, and material safety data sheets (MSDS).
5. **Personnel & Training:** Rigorous qualification and competency verification for safety-critical roles.
6. **Operations & Maintenance:** Safe work practices, preventive maintenance schedules, and equipment reliability programs.
7. **Management of Change (MOC):** Structured evaluation of risks before altering any hardware, operating setpoint, software, or personnel structure.
8. **Third-Party Services:** Contractor compliance with corporate safety standards.
9. **Incident Investigation & Analysis:** Rigorous root-cause analysis (RCA) to prevent repeat events; open reporting culture without fear of reprisal.
10. **Community Awareness & Emergency Preparedness:** Comprehensive emergency response plans, evacuation drills, and mutual aid agreements.
11. **Operations Integrity Assessment & Improvement:** Regular independent audits and continuous performance benchmarking.

---

## 2. Personal Safety vs Process Safety
Interview candidates must clearly articulate the distinction between personal and process safety:

```
+------------------------------------+------------------------------------+
|          PERSONAL SAFETY           |           PROCESS SAFETY           |
+------------------------------------+------------------------------------+
| Focuses on individual occupational | Focuses on preventing major loss   |
| injuries and workplace hazards.    | of containment (LOPC) of toxic or  |
|                                    | flammable hydrocarbons.            |
| Metrics: Slips, trips, falls,      | Metrics: Fires, explosions, toxic  |
| cuts, eye protection (PPE), lifting| gas releases, chemical spills,     |
| ergonomics, lost-time injuries.    | pipeline ruptures, BLEVE events.   |
|                                    |                                    |
| Low personal injury rates do NOT   | Governed by OSHA PSM 1910.119,     |
| guarantee safe chemical processes! | API RP 754 (Tier 1 & Tier 2 LOPC). |
+------------------------------------+------------------------------------+
```

---

## 3. The Hierarchy of Controls
When addressing any industrial safety hazard, engineering solutions must be prioritized from most effective to least effective:

```
      ▲
     / \     1. ELIMINATION       (Physically remove the hazard — e.g., avoid toxic solvent)
    /   \    ────────────────────────────────────────────────────────────────────────────
   /     \   2. SUBSTITUTION      (Replace hazard — e.g., use water-based glycol instead)
  /       \  ────────────────────────────────────────────────────────────────────────────
 /         \ 3. ENGINEERING       (Isolate people from hazard — e.g., pressure relief valves,
/           \   CONTROLS           automatic interlocks, containment dykes, blast walls)
\           /────────────────────────────────────────────────────────────────────────────
 \         / 4. ADMINISTRATIVE    (Change the way people work — e.g., standard operating
  \       /     CONTROLS           procedures, permit-to-work, warning alarms, safety training)
   \     /   ────────────────────────────────────────────────────────────────────────────
    \   /    5. PPE               (Protect the worker with Personal Protective Equipment —
     \ /                           hard hat, steel-toe boots, flame-retardant Nomex coveralls)
      ▼                            [LEAST EFFECTIVE DEFENSE LAYER]
```

---

# Section 5: Hazard Identification, HAZOP & Layer of Protection Analysis (LOPA)

## 1. Hazard and Operability Study (HAZOP)
A HAZOP is a structured, systematic multi-disciplinary team examination of an engineering process design to identify operational deviations that could lead to safety hazards or production loss.

### The Guideword-Parameter Matrix:
The HAZOP methodology applies standardized **Guidewords** to process **Parameters**:
* **Parameters:** Flow, Pressure, Temperature, Level, Viscosity, Composition.
* **Guidewords:** NO / NONE, MORE, LESS, AS WELL AS, PART OF, REVERSE, OTHER THAN.

#### Example HAZOP Deviation Analysis:
| Parameter | Guideword | Deviation | Credible Causes | Consequences | Safeguards (Protective Layers) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Flow** | **NO** | No flow to cooling jacket | Pump trips; inlet valve fails closed; line blocked by debris. | Exothermic reactor overheats; thermal runaway reaction; overpressurization. | Low-flow alarm (`FAL`); automatic interlock tripping heating; standby backup pump. |
| **Pressure**| **MORE** | High pressure in transfer line | Downstream valve accidentally closed; runaway pump; water hammer surge. | Pipe burst along longitudinal seam; hydrocarbon spray; vapor cloud explosion. | Pressure Safety Valve (`PSV`); high-pressure emergency shutdown (`PSHH`); surge relief tank. |
| **Level** | **LESS** | Low level in separator | Drain valve stuck open; supply wellhead trips. | Gas blowby into downstream atmospheric liquid storage tank; overpressurizing tank. | Low-level interlock (`LSLL` - Level Switch Low-Low) closing liquid outlet; independent emergency isolation valve. |

---

## 2. Lockout / Tagout (LOTO) & Permit-to-Work (PTW)
* **Permit-to-Work (PTW):** A formal written document authorizing specific individuals to execute non-routine, high-risk tasks (hot work/welding, confined space entry, working at heights, excavation) under strict safety conditions.
* **Lockout / Tagout (LOTO):** The physical isolation of hazardous energy sources (electrical, mechanical pressure, pneumatic, chemical head) using padlocks and identification tags before maintenance commences.
  - *Golden Rule:* **Zero Energy Verification (Try Step).** After applying padlocks and bleeder valves, workers must physically attempt to start the equipment or vent the pressure gauge to confirm that zero residual energy remains stored in the system.
* **Stop-Work Authority (SWA):** At ExxonMobil, **every employee and contractor has the absolute authority and obligation to immediately stop any operation** if they perceive an unsafe act, condition, or procedural deviation, without any fear of negative administrative repercussions.

---

## 3. Layer of Protection Analysis (LOPA)

LOPA is a semi-quantitative risk evaluation methodology used to determine whether existing safeguards provide adequate protection against credible major process accident scenarios, or whether additional Safety Instrumented Systems (SIS) are required.

### A. Mathematical Formulation
$$\mathbf{f_c^T = f_{IE} \times \prod_{i=1}^J \mathrm{PFD}_i}$$
where:
* $f_c^T$ = Target mitigated consequence frequency per year $[\text{events/year}]$
* $f_{IE}$ = Initiating Event frequency $[\text{events/year}]$
* $\mathrm{PFD}_i$ = Probability of Failure on Demand of the $i$-th **Independent Protection Layer (IPL)**.

### B. What Qualifies as an Independent Protection Layer (IPL)?
To qualify as an IPL in LOPA, a safeguard must meet four strict criteria:
1. **Specificity:** Specifically designed to prevent or mitigate the designated hazardous event.
2. **Independence:** Completely independent of the initiating event and all other IPLs (no shared sensors, valves, or logic solvers).
3. **Dependability:** Verifiable probability of failure (typically $\mathrm{PFD} \le 0.10$).
4. **Auditability:** Regularly inspected, tested, and maintained under mandatory proof-test regimes.

### C. Comprehensive Industrial LOPA Worked Example: Crude Separator Gas Blowby
* **Hazard Scenario:** High-pressure oil-gas separator ($P = 40\text{ bar}$) drains liquid into an atmospheric crude storage tank ($P_{\text{design}} = 0.05\text{ bar}$). If the level control valve fails fully open, liquid empties and high-pressure gas blows into the atmospheric tank, causing catastrophic roof rupture, vapor cloud release, and pool fire.
* **Hypothetical Risk Tolerance Target (Illustrative Benchmark):** For serious process safety events involving potential asset loss or offsite impact, industry reference literature (e.g., CCPS *Layer of Protection Analysis* and IEC 61511 / ANSI/ISA-84.00.01) commonly illustrates hypothetical target mitigated consequence frequencies in the range of $f_{\text{target}} \le 1.0 \times 10^{-4}\text{ per year}$ to $1.0 \times 10^{-5}\text{ per year}$. This threshold is an illustrative educational example; specific corporate risk matrices are proprietary to individual operating companies and are not public.

#### Layer-by-Layer Evaluation:
1. **Initiating Event:** Basic Process Control System (BPCS) level transmitter (`LT`) failure or control valve sticking open:
   $$f_{IE} = 0.10\text{ /year} \quad (1\text{ in } 10\text{ years})$$
2. **IPL 1: Operator Response to Low Level Alarm (`LAL`):**
   - Independent alarm sounding in control room with at least 15 minutes operator response time to close manual bypass or trip pump:
   $$\mathrm{PFD}_1 = 0.10 \quad (90\%\text{ reliability, credit } = 1\text{ order of magnitude})$$
3. **IPL 2: Safety Instrumented Function (SIF / SIL-2 Rated):**
   - Dedicated hardwired Level Switch Low-Low (`LSLL`), separate logic solver, and independent emergency shutdown ball valve (`XV`):
   $$\mathrm{PFD}_2 = 0.01 \quad (99\%\text{ reliability, credit } = 2\text{ orders of magnitude})$$
4. **IPL 3: Atmospheric Tank Emergency Vent Manifold (Relief Valve / Rupture Disk):**
   - Sized for full gas blowby capacity to safely vent gas to high-elevation flare:
   $$\mathrm{PFD}_3 = 0.05$$

#### Mitigated Frequency Calculation:
$$f_c = f_{IE} \times \mathrm{PFD}_1 \times \mathrm{PFD}_2 \times \mathrm{PFD}_3 = (0.10) \times (0.10) \times (0.01) \times (0.05) = 5.0 \times 10^{-6}\text{ per year}$$
* **Evaluation:**
  $$f_c (5.0 \times 10^{-6}\text{ /yr}) < f_{\text{target}} (1.0 \times 10^{-4}\text{ /yr})$$
  The mitigated frequency meets the illustrative educational target. In actual operating facilities, risk reduction must be formally evaluated under the ALARP (As Low As Reasonably Practicable) principle and documented through Safety Instrumented System (SIS) lifecycle management per IEC 61511 and OSHA 29 CFR 1910.119.

---

## Sources
* **Process Safety Standards:** OSHA 29 CFR 1910.119, *Process Safety Management of Highly Hazardous Chemicals*; CCPS (Center for Chemical Process Safety), *Layer of Protection Analysis: Simplified Process Risk Assessment*, AIChE/Wiley.
* **Industrial Facilities & Tank Containment:** NFPA 30, *Flammable and Combustible Liquids Code*, 2021 Edition; API Standard 650, *Welded Tanks for Oil Storage*, 13th Edition, American Petroleum Institute.
* **Offshore Hydrodynamics:** Morison, J. R., O'Brien, M. P., Johnson, J. W., & Schaaf, S. A. (1950), *The force exerted by surface waves on piles*, Petroleum Transactions, AIME; DNV-RP-C205, *Environmental Conditions and Environmental Loads*, Det Norske Veritas.
* **Operations Integrity:** ExxonMobil Operations Integrity Management System (OIMS) Public Framework Guidelines; API RP 754, *Process Safety Performance Indicators for the Refining and Petrochemical Industries*.

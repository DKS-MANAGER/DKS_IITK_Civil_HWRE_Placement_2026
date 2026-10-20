# ExxonMobil Engineer Recruitment: Technical & Behavioral Interview Guide
## Thesis / CFD Project Defense, Spoken Oral Numericals & STAR Safety Competency

> **Target Profile:** Engineer (Technical Panel & Behavioral / HR Interviews)  
> **Audience:** Civil Engineering graduates specializing in Hydraulics & Water Resources Engineering (HWRE)  
> **Pedagogical Standard:** Claude Fable 5 — Structured technical articulation (30-second summary vs 3-minute deep dive), rigorous OpenFOAM/CFD defense without personal identifiers, and STAR safety leadership narratives.

---

# Table of Contents
1. [Section 1: General Project Defense Framework (CFD & Hydraulic Modeling)](#section-1-general-project-defense-framework-cfd--hydraulic-modeling)
2. [Section 2: High-Frequency Technical Interview Questions & Spoken Answers](#section-2-high-frequency-technical-interview-questions--spoken-answers)
3. [Section 3: Behavioral Interviews & The STAR Method (ExxonMobil Core Values)](#section-3-behavioral-interviews--the-star-method-exxonmobil-core-values)
4. [Section 4: Technical Troubleshooting Scenarios (Plant & Field Hydraulics)](#section-4-technical-troubleshooting-scenarios-plant--field-hydraulics)

---

# Section 1: General Project Defense Framework (CFD & Hydraulic Modeling)

Interviewers at ExxonMobil rigorously probe candidates on their core coursework, Master's thesis, or computational fluid modeling projects. Use this standardized two-tier answering strategy:

```
[Level 1: 30-Second Executive Summary]
  • State the physical problem and industrial relevance.
  • State the governing formulation (e.g., FVM, Navier-Stokes, OpenFOAM).
  • State the primary quantitative conclusion and safety/design recommendation.

[Level 2: 3-Minute Technical Deep Dive (Upon Follow-Up)]
  • Mesh architecture, inflation layers, and wall y+ resolution.
  • Turbulence model selection rationale (e.g., k-omega SST vs Realizable k-epsilon).
  • Discretization schemes (second-order upwind, bounded PISO/SIMPLE).
  • Boundary conditions (stochastic turbulent inlet, hydrostatic outlet).
  • Verification & Validation (ASME V&V 20 Grid Convergence Index).
```

### Archetype Defense: Hydrodynamic Scour & Structural Risk Modeling
* **30-Second Spoken Pitch:**
  > "In my hydrodynamic modeling work, I investigated 3D vortex shedding and turbulent scour around submerged cylindrical structures. Using the Finite Volume Method in OpenFOAM, we resolved the horseshoe and wake vortices that destabilize structural foundations during design floods. The calibrated model identified critical shear stress zones and demonstrated that maintaining riprap armoring above a threshold Shields parameter reduced equilibrium scour depth by over 40%."

* **Key Defense Questions & Model Responses:**

#### Q1: "Why did you choose the $k-\omega$ SST turbulence model over Standard $k-\epsilon$?"
> **Model Answer:**  
> "The Standard $k-\epsilon$ model relies on isotropic eddy viscosity and standard wall functions ($y^+ > 30$), which notoriously overpredict turbulent kinetic energy near stagnation points and fail to predict adverse-pressure-gradient boundary layer separation. The $k-\omega$ Shear Stress Transport (SST) model blends the robust $k-\omega$ formulation in the inner boundary layer with the free-stream independence of $k-\epsilon$ in the outer flow field. Because pier scour and flow separation are driven by adverse pressure gradients and downward stagnation jets, $k-\omega$ SST provides vastly superior accuracy in predicting wall shear stresses when combined with fine near-wall prism layers ($y^+ \approx 1$)."

#### Q2: "How did you prove that your CFD results were not numerical artefacts?"
> **Model Answer:**  
> "We implemented the **ASME V&V 20 standard** for numerical verification. We generated three systematically refined unstructured hybrid meshes with a constant grid refinement ratio $r = 1.4$. By monitoring the target output—maximum bed shear stress—we computed the apparent spatial order of convergence $p$ and the **Grid Convergence Index (GCI)** via Richardson extrapolation. The fine-grid GCI fell below 3.2%, confirming that spatial discretization error was well within acceptable engineering tolerances before comparing against experimental flume benchmark data for physical validation."

---

# Section 2: High-Frequency Technical Interview Questions & Spoken Answers

#### Q1: "Explain the difference between Darcy and Fanning friction factors."
* **Spoken (30s):**
  > "The Darcy-Weisbach friction factor $f$ is standard in Civil Engineering and the Moody chart, where head loss is $h_f = f (L/D) (V^2/2g)$. In chemical and petroleum engineering, the Fanning friction factor $f_F$ relates shear stress directly to dynamic pressure ($\tau_w = f_F \cdot \frac{1}{2}\rho V^2$). Mathematically, **$f_{\text{Darcy}} = 4 \times f_{\text{Fanning}}$**. Confusing them causes a factor-of-four error in pipeline sizing."

#### Q2: "What is cavitation, and how do you prevent it in a crude oil transfer pump?"
* **Spoken (45s):**
  > "Cavitation occurs when local static pressure at the pump impeller eye drops to or below the liquid's vapor pressure ($P \le P_v$). Vapor bubbles form and then violently collapse in higher pressure zones, eroding metal surfaces and causing severe vibration. To prevent it, we must ensure that the Net Positive Suction Head Available ($\mathrm{NPSH}_A$) exceeds the manufacturer's required $\mathrm{NPSH}_R$ by a safe design margin. In practice, we achieve this by raising the liquid level in the suction vessel, increasing suction line diameter to reduce frictional velocity head loss, lowering fluid operating temperature, or installing an inducer."

#### Q3: "What happens when you close a valve rapidly on a high-pressure oil pipeline?"
* **Spoken (45s):**
  > "Rapid valve closure converts the fluid's kinetic energy into an acoustic pressure surge wave, known as **water hammer**. If the valve closes faster than the critical pipe round-trip time ($T_c = 2L/c$), the maximum pressure surge is governed by the Joukowsky equation: **$\Delta P = \rho c \Delta V$**, where $c$ is the acoustic speed of sound in the elastic pipe. This severe pressure pulse travels upstream at over $1000\text{ m/s}$ and can rupture pipe walls, damage flanges, or trip emergency shutdown systems unless surge relief valves or slow-closing actuators are installed."

---

# Section 3: Behavioral Interviews & The STAR Method (ExxonMobil Core Values)

ExxonMobil evaluates candidates against three non-negotiable core pillars: **Safety Leadership (OIMS), Technical Integrity, and Collaboration Across Disciplines**. Frame every answer using the **STAR methodology**:
* **Situation:** Set the engineering context (facility, team, academic project).
* **Task:** Define your specific responsibility and the technical or safety dilemma.
* **Action:** Detail the concrete steps you took, demonstrating proactive safety leadership and rigorous analytical reasoning.
* **Result:** Share the quantified positive outcome and the lasting lesson learned.

---

### STAR Story 1: Safety Leadership & Stop-Work Authority (SWA)
* **Prompt:** *"Tell me about a time you noticed a safety risk or procedural violation and intervened."*
* **Situation:** During an experimental hydraulics laboratory project evaluating high-velocity flume discharge, a team member attempted to adjust a pressurized intake hose while the centrifugal pump was running at full capacity ($45\text{ kW}$) to save 10 minutes of recalibration time.
* **Task:** I had the responsibility as the student test lead to ensure that all experimental operations conformed strictly to the laboratory safety operating procedures.
* **Action:** I immediately exercised **Stop-Work Authority**, asked my peer to step back from the high-pressure line, and hit the pump emergency shutdown button. I calmly explained that adjusting an unvented, pressurized coupling presented a high risk of violent hose whip and high-pressure fluid injection injury. We depressurized the system, inspected the coupling gasket, and conducted a 5-minute toolbox talk to re-align on the Lockout/Tagout zero-energy verification procedure before resuming.
* **Result:** The flume testing was completed safely without injury or equipment damage. Our team established a mandatory zero-pressure verification checklist before anyone approached the manifold, demonstrating that taking 2 minutes for safety prevents catastrophic downtime.

---

### STAR Story 2: Technical Integrity & Disagreeing with Data
* **Prompt:** *"Tell me about a time your analysis contradicted expectations or your team's consensus."*
* **Situation:** In an engineering design exercise sizing an open-channel diversion culvert, preliminary empirical calculations suggested a 1.2-meter diameter pipe was sufficient based on historical 10-year storm charts.
* **Task:** I was tasked with verifying the hydraulic grade line and backwater profile under design flood conditions.
* **Action:** Instead of accepting the standard runoff coefficient, I conducted a full gradually varied flow analysis and checked the inlet control headwater elevation using HEC-RAS principles. I discovered that during extreme precipitation events, subcritical backwater from the downstream receiving basin would submerge the culvert outlet, causing it to operate under pressurized orifice flow with inlet choking. I compiled a comparative sensitivity report showing that water would overtop the roadway embankments by 25 cm unless the culvert was expanded to a 1.8-meter box structure.
* **Result:** The faculty panel reviewed the backwater calculations, confirmed the inlet choking phenomenon, and approved the revised design. The experience reinforced that **engineering integrity requires following physics and mathematics**, even when it challenges convenient preliminary assumptions.

---

# Section 4: Technical Troubleshooting Scenarios (Plant & Field Hydraulics)

#### Scenario: "An operator calls you: A crude oil booster pump is drawing excessive electrical motor current and running hot. What is your diagnostic checklist?"
> **Structured Response Framework:**
> 1. **Hydraulic Operating Point:** "First, check the discharge pressure and flow rate. Centrifugal pump power is proportional to $Q \times H$. If a downstream line broke or a bypass valve was accidentally left wide open, the pump will operate far out to the right on its performance curve (run-out condition), delivering maximum flow at low head, which causes electric motor overload."
> 2. **Fluid Property Changes:** "Second, check fluid temperature and viscosity. Heavy crude oil requires significantly higher shaft power when ambient temperatures drop, increasing viscous shear friction on the impeller."
> 3. **Mechanical Integrity:** "Third, check for mechanical binding: bearing failure, misaligned coupling, or foreign debris lodged in the impeller vanes."
> 4. **Immediate Action:** "If operating near run-out, immediately throttle the discharge valve to bring the operating point back to the Best Efficiency Point (BEP) while monitoring motor amperage."

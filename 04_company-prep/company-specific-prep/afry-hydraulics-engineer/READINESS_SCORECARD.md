# AFRY India — Candidate Readiness Scorecard & Diagnostic Rubric

> **Assessment Purpose**: Objective Competency Evaluation, Benchmark Tracking & Gap Remediation for Hydraulics Engineer Role  
> **Candidate Profile**: M.Tech Civil Engineering (HWRE), IIT Kanpur  
> **Target Standard**: Ready for Offer ($\ge 85\%$ Benchmark across all dimensions)  
> **Evidentiary Status**: `[TIER 5 / PEDAGOGICAL DIAGNOSTIC RUBRIC]`  

---

## 1. Ten-Dimensional Hydraulic Competency Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       10-DIMENSIONAL COMPETENCY RADAR                       │
│                                                                             │
│                  1. Open-Channel & GVF (15%)                                │
│                              ▲                                              │
│               10. VBA Auto   │   2. Saint-Venant (10%)                      │
│                  (10%) ◄─────┼─────►                                        │
│                              │       3. Pipe Losses (10%)                   │
│         9. HEC-RAS / ◄───────┼───────►                                      │
│            HAMMER (15%)      │       4. Water Hammer (10%)                  │
│                8. Similitude ◄───────► 5. Surge Tanks (10%)                 │
│                   (5%)       │   6. Spillways (10%)                         │
│                              ▼                                              │
│                  7. Energy Dissipators (10%)                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Comprehensive 10-Dimension Evaluation Rubric

| Dimension | Weight | Target Criteria for Offer Readiness ($\ge 85\%$) | Verified Module |
| :--- | :---: | :--- | :---: |
| **1. Open-Channel & GVF** | **15%** | Flawlessly derives critical flow condition, solves normal depth via Newton-Raphson, classifies 12 GVF profiles, and computes standard-step energy balances. | [`Module 03`](03_OPEN_CHANNEL_HYDRAULICS.md) |
| **2. Saint-Venant Unsteady Flow** | **10%** | Derives 1D shallow-water continuity and momentum equations; evaluates kinematic vs dynamic waves; verifies CFL numerical stability. | [`Module 04`](04_UNSTEADY_OPEN_CHANNEL_FLOW.md) |
| **3. Pressure-Pipe Hydraulics** | **10%** | Solves Darcy-Weisbach and Colebrook-White friction factors; computes minor losses in intakes/valves; evaluates pump/system duty points. | [`Module 05`](05_PRESSURE_PIPE_HYDRAULICS.md) |
| **4. Water Hammer & Transients** | **10%** | Derives Joukowsky equation; calculates acoustic wave speed with pipe wall elasticity; explains rapid vs slow closure and column separation. | [`Module 06`](06_WATER_HAMMER_AND_MASS_OSCILLATION.md) |
| **5. Mass Oscillation & Surge Tanks** | **10%** | Solves rigid-column surge tank ODEs; calculates natural period $T$ and maximum upsurge $Z_{max}$; derives Thoma governor stability criterion. | [`Module 06`](06_WATER_HAMMER_AND_MASS_OSCILLATION.md) |
| **6. Spillways & Hydraulic Structures** | **10%** | Generates USBR/WES downstream ogee coordinates; analyzes sub-atmospheric crest pressures and cavitation limits; rates sluices and weirs. | [`Module 07`](07_SPILLWAYS_AND_HYDRAULIC_STRUCTURES.md) |
| **7. Energy Dissipators** | **10%** | Designs USBR Type II vs Type III stilling basins; computes trajectory flip bucket throw distance and Veronese plunge pool scour depth. | [`Module 08`](08_ENERGY_DISSIPATION_SYSTEMS.md) |
| **8. Hydraulic Model Studies** | **5%** | Applies Froude similitude scaling ($Q_r = L_r^{2.5}, F_r = L_r^3$); analyzes viscous/surface tension scale effects; understands distorted models. | [`Module 09`](09_HYDRAULIC_MODEL_STUDIES.md) |
| **9. HEC-RAS & Bentley HAMMER** | **15%** | Explains HEC-RAS 1D geometric data, boundary conditions, and bridge low/high flow methods; explains HAMMER Method of Characteristics (MOC). | [`Modules 10 & 11`](10_HEC_RAS_PREPARATION.md) |
| **10. Excel VBA Automation** | **5%** | Writes robust VBA subroutines and UDFs; implements error traps; automates iterative normal depth, rating curves, and pipe losses. | [`Module 12`](12_EXCEL_VBA_HYDRAULIC_AUTOMATION.md) |

---

## 3. Measurable Verification Checklist & Exit Gates

### Category A: Mathematical Derivations (Must Pass 100%)
- [ ] **DERIV-01**: Can derive critical depth condition $\frac{Q^2 T_c}{g A_c^3} = 1$ from $dE/dy = 0$.
- [ ] **DERIV-02**: Can derive the GVF differential equation $\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$ from energy gradients.
- [ ] **DERIV-03**: Can derive the Bélanger equation $\frac{y_2}{y_1} = \frac{1}{2}(\sqrt{1 + 8 Fr_1^2} - 1)$ from specific force conservation.
- [ ] **DERIV-04**: Can derive hydraulic jump energy loss $\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$.
- [ ] **DERIV-05**: Can derive Joukowsky equation $\Delta P = \rho a \Delta v$ from moving shock front momentum.
- [ ] **DERIV-06**: Can derive natural oscillation period of a surge tank $T = 2\pi\sqrt{\frac{L A_T}{g A_t}}$.
- [ ] **DERIV-07**: Can derive discharge equation for broad-crested weir $q = \left(\frac{2}{3}\right)^{3/2}\sqrt{g} H_0^{3/2} = 1.705 H_0^{3/2}$.
- [ ] **DERIV-08**: Can derive Froude discharge scale ratio $Q_r = L_r^{2.5}$ and force ratio $F_r = L_r^3$.

### Category B: Software & Consulting Application
- [ ] **SOFT-01**: Can explain HEC-RAS subcritical downstream boundary condition requirements.
- [ ] **SOFT-02**: Can explain how HEC-RAS models low-flow bridge pier losses (energy vs momentum vs Yarnell).
- [ ] **SOFT-03**: Can diagnose and resolve HEC-RAS warning: *"Energy equation could not be balanced within specified iterations"*.
- [ ] **SOFT-04**: Can explain Bentley HAMMER Method of Characteristics compatibility equations along $C^+$ and $C^-$.
- [ ] **SOFT-05**: Can explain how an air vessel protects a pipeline from both overpressure and sub-atmospheric vacuum.
- [ ] **SOFT-06**: Can write a functional Excel VBA UDF to solve the Colebrook-White equation.

### Category C: Project Defense & Behavioral Readiness
- [ ] **DEF-01**: Can deliver the 3-minute executive pivot pitch connecting OpenFOAM computational hydraulics to AFRY consulting.
- [ ] **DEF-02**: Can explain why $k-\omega$ SST was chosen over $k-\epsilon$ for stagnation and separation flow zones.
- [ ] **DEF-03**: Can describe the Grid Convergence Index (GCI) procedure for mesh independence.
- [ ] **DEF-04**: Can articulate alignment with AFRY core values: **Brave, Devoted, Team Players**.

---

## 4. Overall Readiness Scoring Rubric

To calculate overall readiness score:
$$\text{Readiness Score} = \sum_{i=1}^{10} (w_i \times S_i)$$

| Overall Score | Level Determination | Placement Readiness Assessment |
| :---: | :---: | :--- |
| **$\ge 85\%$** | **Ready for Offer** | **Outstanding Readiness**: Flawless derivation skills, robust understanding of HEC-RAS and HAMMER solver physics, clear thesis pivot. High probability of offer. |
| **70–84%** | **Solid Baseline** | **Good Potential**: Strong fundamental hydraulics; requires rapid revision of surge tanks, ogee profiles, or VBA syntax. |
| **$< 70\%$** | **Needs Remediation** | **Identified Gaps**: Unprepared for live whiteboard derivations; requires complete execution of the 14-day study plan. |


# 14-Day Comprehensive Preparation Plan (80 Hours)

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27 | Comprehensive Mastery  
**Pacing:** ~5.5 to 6.0 Hours per Day

---

## Weekly Master Progression

```
 WEEK 1: Physical & Mathematical Foundations (Days 1–7)
 ├── Day 01: Fluid Properties, Hydrostatics & Navier-Stokes (5.5 hrs)
 ├── Day 02: Boundary Layer Theory, Drag, Lift & Separation (5.5 hrs)
 ├── Day 03: Open-Channel Flow: Critical Depth & Specific Energy (6.0 hrs)
 ├── Day 04: Hydraulic Jumps, Energy Dissipators & Transitions (6.0 hrs)
 ├── Day 05: Gradually Varied Flow (GVF) & Profile Computations (5.5 hrs)
 ├── Day 06: Pipe Flow, Moody Diagram & Pipe Networks (Hardy Cross) (5.5 hrs)
 └── Day 07: Pumps, Cavitation (NPSH) & Water Hammer Transients (6.0 hrs)

 WEEK 2: Applied Engineering, Projects & Interview Mastery (Days 8–14)
 ├── Day 08: Precipitation, Infiltration, IDF & Evaporation (5.5 hrs)
 ├── Day 09: Unit Hydrographs, Flood Routing & Extreme Value Gumbel (6.0 hrs)
 ├── Day 10: Soil Mechanics, Bearing Capacity & Foundation Scour (5.5 hrs)
 ├── Day 11: Technical Project Deep-Dive: CFD Scour & OpenFOAM (6.5 hrs)
 ├── Day 12: Applied Projects: Machine Learning Risk Framework & Streamflow SARIMA (6.0 hrs)
 ├── Day 13: Engineering Consultancy Scenarios & Design Codes (5.5 hrs)
 └── Day 14: Full-Length Mock Exams & Executive HR Rehearsal (5.5 hrs)
```

---

## Detailed Daily Curriculum

### Week 1: Physical & Mathematical Foundations

#### Day 1: Fluid Properties, Hydrostatics & Navier-Stokes (5.5 Hours)
- Fluid properties: viscosity (Newtonian vs non-Newtonian), surface tension, compressibility, bulk modulus.
- Hydrostatic pressure distribution on plane and curved submerged surfaces; center of pressure.
- Derivation of Navier-Stokes equations from Cauchy stress tensor and Stokes hypothesis for Newtonian fluids.
- Solve Questions 1–5 in Technical Question Bank.

#### Day 2: Boundary Layer Theory, Drag, Lift & Separation (5.5 Hours)
- Prandtl boundary layer equations; boundary layer thickness ($\delta, \delta^*, \theta$).
- Von Kármán momentum integral equation for laminar and turbulent flat plates.
- Boundary layer separation under adverse pressure gradients; vortex shedding and Strouhal number ($St$).
- Pressure drag vs skin friction drag on blunt bodies (circular cylinders, bridge piers, submerged decks).
- Solve Questions 6–10 in Technical Question Bank.

#### Day 3: Open-Channel Flow: Critical Depth & Specific Energy (6.0 Hours)
- Classification of open-channel flows: steady/unsteady, uniform/varied, subcritical/supercritical ($Fr$).
- Specific energy diagram ($E-y$ curve): critical depth $y_c = (q^2/g)^{1/3}$, minimum specific energy $E_{\min} = 1.5 y_c$.
- Channel transitions: upward bed steps, horizontal width constrictions, choking conditions.
- Section factor $Z$ and hydraulic exponent $M$; critical flow in trapezoidal and circular sections.
- Solve Questions 11–15 in Technical Question Bank.

#### Day 4: Hydraulic Jumps, Energy Dissipators & Transitions (6.0 Hours)
- Momentum principle in open channels; specific force function ($F$).
- Derivation of Belanger conjugate depth ratio: $y_2/y_1 = \frac{1}{2}(\sqrt{1 + 8Fr_1^2} - 1)$.
- Energy loss in hydraulic jump: $\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$; jump efficiency and relative height.
- Classification of jumps (undular, weak, oscillating, steady, strong) based on upstream Froude number $Fr_1$.
- Stilling basin design: USBR Type II, III, and IV basins, chute blocks, baffle piers, end sills.
- Solve Questions 16–20 in Technical Question Bank.

#### Day 5: Gradually Varied Flow (GVF) & Profile Computations (5.5 Hours)
- Differential equation of GVF: $\frac{dy}{dx} = \frac{S_0 - S_f}{1 - Fr^2}$.
- Complete taxonomy of 12 surface profiles: Mild ($M_1, M_2, M_3$), Steep ($S_1, S_2, S_3$), Critical ($C_1, C_3$), Horizontal ($H_2, H_3$), Adverse ($A_2, A_3$).
- Boundary conditions and control sections (sluice gates, weirs, free overfalls).
- Numerical integration: Direct Step Method and Standard Step Method (as implemented in HEC-RAS).
- Solve Questions 21–25 in Technical Question Bank.

#### Day 6: Pipe Flow, Moody Diagram & Pipe Networks (Hardy Cross) (5.5 Hours)
- Hagen-Poiseuille laminar flow equation; turbulent pipe flow and logarithmic velocity profile.
- Darcy-Weisbach equation; Colebrook-White implicit equation; explicit approximations (Swamee-Jain).
- Moody diagram: laminar zone, critical transition, smooth pipe, transitional, fully rough turbulent regime.
- Minor losses: contraction coefficient $C_c$, expansion loss $\frac{(V_1 - V_2)^2}{2g}$, equivalent length.
- Loop equations in pipe networks; Hardy Cross correction formula $\Delta Q = -\frac{\sum r Q |Q|}{\sum 2 r |Q|}$.
- Solve Questions 26–30 in Technical Question Bank.

#### Day 7: Pumps, Cavitation (NPSH) & Water Hammer Transients (6.0 Hours)
- Centrifugal pumps: velocity triangles, work done, manometric efficiency, overall efficiency.
- System head-discharge curve $H_{\text{sys}} = H_{\text{static}} + K Q^2$; matching pump curve $H_{\text{pump}} = A - B Q^2$.
- Pumps in series (heads add) vs pumps in parallel (discharges add).
- Cavitation in hydraulic machines: Net Positive Suction Head Required ($NPSH_R$) vs Available ($NPSH_A$).
- Water hammer pressure wave speed $c = \sqrt{\frac{K/\rho}{1 + (K/E)(D/t)}}$; rapid vs slow valve closure.
- Solve Questions 31–35 in Technical Question Bank.

---

### Week 2: Applied Engineering, Projects & Interview Mastery

#### Day 8: Precipitation, Infiltration, IDF & Evaporation (5.5 Hours)
- Rain gauge density (IS 4987 / WMO standards); point to areal rainfall adjustment factors (ARF).
- Intensity-Duration-Frequency (IDF) curve formulation: $I = \frac{K T^m}{(D + a)^n}$; parameter estimation.
- Infiltration modeling: Horton's exponential decay equation, Green-Ampt physical model, $\Phi$-index method.
- Reference evapotranspiration ($ET_0$): FAO-56 Penman-Monteith energy-aerodynamic equation.
- Solve Questions 36–40 in Technical Question Bank.

#### Day 9: Unit Hydrographs, Flood Routing & Extreme Value Gumbel (6.0 Hours)
- Linear theory of Unit Hydrographs: time invariance, proportional ordinates; deriving UH from multi-peak storm hydrographs.
- $S$-curve technique for altering unit hydrograph duration ($D_1 \to D_2$).
- Synthetic Unit Hydrographs: Snyder’s method ($C_t, C_p$) and SCS dimensionless unit hydrograph.
- Hydrologic flood routing: Muskingum equation $S = K [X I + (1 - X) Q]$; routing coefficient derivations.
- Flood frequency analysis: Gumbel Extreme Value Type I distribution, frequency factor $K_T$, confidence limits.
- Solve Questions 41–45 in Technical Question Bank.

#### Day 10: Soil Mechanics, Bearing Capacity & Foundation Scour (5.5 Hours)
- Terzaghi’s ultimate bearing capacity for shallow strip footings: $q_u = c' N_c + \gamma D_f N_q + 0.5 \gamma B N_\gamma$.
- Rankine and Coulomb lateral earth pressure theories: active ($K_a = \frac{1-\sin\phi}{1+\sin\phi}$) and passive ($K_p$).
- River bridge scour: general scour, contraction scour, local pier/abutment scour; Lacey’s regime scour depth.
- Riprap sizing for scour countermeasures: Isbash and HEC-23 stone sizing formulations.
- Solve Questions 46–50 in Technical Question Bank.

#### Day 11: Technical Project Deep-Dive: CFD Scour & OpenFOAM (6.5 Hours)
- Comprehensive walkthrough of technical project: *Computational Fluid Dynamics & Hydrodynamic Scour Modeling*.
- Navier-Stokes discretization using Finite Volume Method (FVM); PIMPLE pressure-velocity coupling loop.
- Free-surface modeling using Volume of Fluid (VOF); MULES compression interface tracking.
- Turbulence modeling: Wilcox $k-\omega$ vs Menter $k-\omega$ SST; blending functions and turbulent viscosity $\nu_t$.
- Near-wall resolution: boundary layer viscous sublayer, log-law, $y^+ \le 1$ vs wall functions ($30 < y^+ < 300$).
- Sediment entrainment: Shields diagram, critical shear stress $\tau_c$, Meyer-Peter & Müller bedload equation.
- Master all 20 technical grilling questions in `04_PROJECT_AND_RESUME_PREPARATION/thesis_deep_dive.md`.

#### Day 12: Applied Projects: Machine Learning Risk Framework & Streamflow SARIMA (6.0 Hours)
- *Machine Learning Risk Defense:* Formulation of XGBoost binary classification, handling extreme class imbalance, evaluating PR-AUC (0.854) vs ROC-AUC (0.983), and extracting local adverse action drivers using TreeSHAP.
- *Streamflow SARIMA Defense:* Stationarity testing using Augmented Dickey-Fuller (ADF), seasonal differencing, state-space estimation, and WAPE evaluation.
- Practice articulating how machine learning augments traditional civil engineering risk modeling.
- Master all questions in `04_PROJECT_AND_RESUME_PREPARATION/project_explanations.md`.

#### Day 13: Engineering Consultancy Scenarios & Design Codes (5.5 Hours)
- Work through all 10 practical engineering consultancy scenarios in `03_ASSESSMENT_PREPARATION/engineering_scenarios/practical_scenarios.md`.
- Review key provisions of design codes:
  - IRC:SP:13 (Guidelines for the Design of Small Bridges and Culverts).
  - IRC:5 & IRC:78 (Standard Specifications and Code of Practice for Road Bridges — Foundation and Substructure).
  - IS 456 (Plain and Reinforced Concrete) & IS 3370 (Concrete Structures for Storage of Liquids).
  - CIRIA C753 (The SuDS Manual for Sustainable Urban Drainage).
- Rehearse structured communication: State assumptions, define governing equations, sketch diagrams, state safety factors.

#### Day 14: Full-Length Mock Exams & Executive HR Rehearsal (5.5 Hours)
- Take the 120-minute Full-Length Placement Mock Assessment under strict exam conditions.
- Score and audit answers; log any errors into `06_TRACKING_AND_REVISION/weak_topics.md`.
- Practice all 25 behavioral questions in `05_INTERVIEW_PREPARATION/behavioural_interview.md` using the SPEED / AECOM Safeguard principles.
- Conduct final review of `01_PREPARATION_ROADMAP/revision_checklist.md`.

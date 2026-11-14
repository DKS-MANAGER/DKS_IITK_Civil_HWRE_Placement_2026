# 14-Day Comprehensive Preparation Plan (90 Study Hours)
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Schedule Structure:** 2 Weeks $\times$ 7 Days = 14 Days ($\approx 6.5\text{ Hours/Day}$)  

---

## Roadmap Architecture

The 14-day roadmap is divided into two distinct weekly cycles:
- **Week 1 (Days 1–7): First-Principles Mastery & Manufacturing Engineering Foundation (45 Hours)**  
  *Focus: Mechanics of materials, failure theories, chassis/enclosure design, FEA, casting, stamping, welding, polymers, and quality engineering.*
- **Week 2 (Days 8–14): EV Battery Systems, Projects, Assessments, GD & Interview Simulation (45 Hours)**  
  *Focus: 4680 cell manufacturing, AIS-156 safety, 4 practical portfolio projects, test question banks, 20 GD topics, and 3-round interview mastery.*

```
WEEK 1: FOUNDATIONS & SHOP FLOOR PROCESSES
Day 1: Eligibility Audit + Stress, Strain & Mohr's Circle (6.5 hrs)
Day 2: Bending, Torsion, Buckling & Fatigue S-N Mechanics (6.5 hrs)
Day 3: Mechanical Design (Bolts, Welds) & FEA Fundamentals (6.5 hrs)
Day 4: High-Pressure Die-Casting & Sheet Metal Stamping (6.5 hrs)
Day 5: Robotic Welding, Plastic Injection Molding & Assembly (6.5 hrs)
Day 6: Statistical Process Control (SPC), Control Charts & Cp/Cpk (6.5 hrs)
Day 7: Lean Manufacturing, Six Sigma (DMAIC), FMEA & Diagnostic Test (6.0 hrs)

WEEK 2: EV BATTERIES, ADVANCED PROJECTS & INTERVIEW SIMULATION
Day 8: Li-Ion Electrochemistry, NMC vs LFP & The 4680 Bharat Cell (6.5 hrs)
Day 9: Battery Thermal Management, Thermal Runaway & AIS-156 (6.5 hrs)
Day 10: Practical Projects 1 & 2 (Battery Enclosure FEA & Quality Dashboard) (6.5 hrs)
Day 11: Practical Projects 3 & 4 (Battery Thermal Analysis & Process Optimization) (6.5 hrs)
Day 12: Question Bank Drills (Mechanics, Mfg, Battery & Aptitude) (6.5 hrs)
Day 13: Group Discussion Mastery (20 Topics) & Civil-to-EV Defense (6.5 hrs)
Day 14: Full-Length Mock Assessment, Plant Scenarios & HR Interviews (6.0 hrs)
```

---

## Detailed Week-by-Week Syllabus & Daily Deliverables

### Week 1: Foundations & Shop Floor Processes (Days 1 to 7)

#### Day 1: Eligibility Verification & Continuum Mechanics
- **Hours 1–2:** Submit formal SPO inquiry on eligibility. Study `00_COMPANY_AND_ROLE_RESEARCH/eligibility_verification.md` and `company_overview.md`.
- **Hours 3–5:** Normal stress, shear stress, 3D strain tensor, plane stress vs plane strain, Hooke's Law in 3D.
- **Hours 6–6.5:** Mohr's circle mathematical derivation and principal stress calculation. Complete 10 derivation exercises.

#### Day 2: Advanced Strength of Materials & Fatigue
- **Hours 1–3:** Flexural bending equation ($\sigma/y = M/I = E/R$), transverse shear stress in thin-walled sections, and circular/non-circular shaft torsion.
- **Hours 4–5:** Column buckling (Euler critical load $P_{cr} = \frac{\pi^2 E I}{L_e^2}$, effective length factors for chassis tubes).
- **Hours 6–6.5:** Fatigue under cyclic loading: S-N curves, high-cycle vs low-cycle fatigue, Goodman, Soderberg, and Gerber mean stress criteria.

#### Day 3: Vehicle Structural Design & FEA Fundamentals
- **Hours 1–2.5:** Design of mechanical joints: Preloaded bolted connections (joint stiffness ratio $C = \frac{k_b}{k_b + k_m}$), transverse shear joints, welded joint throat stress.
- **Hours 3–5:** Finite Element Method: Variational formulation, 1D/2D/3D elements, stiffness matrix assembly $[K]\{u\} = \{F\}$, plane stress vs shell elements.
- **Hours 6–6.5:** FEA practical traps: Aspect ratio distortion, stress singularities at re-entrant corners, boundary condition over-constraint.

#### Day 4: High-Pressure Die-Casting & Sheet Metal Stamping
- **Hours 1–3.5:** HPDC technology: Aluminum-silicon alloy casting (A380/A383), cold chamber machines, gating system design, injection shot profiling, and porosity elimination.
- **Hours 4–6.5:** Sheet metal stamping: Punch-die clearance, bending neutral axis shift ($K$-factor), springback radius correction, deep drawing draw ratios, and sheet tear defects.

#### Day 5: Robotic Welding, Polymers & Surface Finishing
- **Hours 1–3:** Automated robotic welding: MIG/MAG process parameters, pulsed arc welding, weld penetration, residual stresses, and laser welding of battery copper busbars.
- **Hours 4–5.5:** Polymers and injection molding: Thermoplastics (PP, ABS, PA66) vs thermosets, injection pressure-velocity-temperature (PVT) curve, sink marks, warpage, and mold shrinkage.
- **Hours 6–6.5:** Paint shop operations: Cathodic Electrodeposition (CED) primer, electrostatic robotic spraying, and salt spray ASTM B117 corrosion testing.

#### Day 6: Statistical Process Control (SPC) & Process Capability
- **Hours 1–3.5:** Control charts: $\bar{X}-R$ and $\bar{X}-S$ charts for variable dimensions, $p$-chart and $c$-chart for attribute defects. 3-sigma control limits and Western Electric out-of-control rules.
- **Hours 4–6.5:** Process Capability: Derivation and calculation of $C_p$ and $C_{pk}$. Process center shift ($k$-factor). Estimating PPM (parts per million) scrap rates from normal distribution $Z$-scores.

#### Day 7: Lean Manufacturing, Six Sigma (DMAIC) & Diagnostic Test
- **Hours 1–2.5:** Six Sigma DMAIC framework, 8D problem-solving methodology, 5-Whys, Fishbone (Ishikawa) root-cause diagrams, and Poka-yoke error-proofing.
- **Hours 3–4:** Industrial Engineering: Takt time calculation, cycle time, line balancing efficiency, and Overall Equipment Effectiveness ($OEE = \text{Availability} \times \text{Performance} \times \text{Quality}$).
- **Hours 4.5–6:** Take the **60-minute Diagnostic Test** in `03_ASSESSMENT_PREPARATION/mock_tests/diagnostic_test.md`. Score and log errors.

---

### Week 2: EV Batteries, Projects & Interview Simulation (Days 8 to 14)

#### Day 8: Li-Ion Electrochemistry & The 4680 Bharat Cell
- **Hours 1–3:** Fundamentals of lithium-ion cells: Intercalation physics, cathode chemistries (NMC 811 vs LFP), graphite anodes, separators, and non-aqueous electrolytes.
- **Hours 4–5.5:** Cell design trade-offs: Specific energy ($\text{Wh/kg}$) vs power density ($\text{W/kg}$) vs thermal stability vs cycle life.
- **Hours 6–6.5:** The 4680 "Bharat Cell": Form factor geometry, tabless current collector architecture, internal resistance ($R_{\text{int}}$) reduction, and axial heat dissipation advantages.

#### Day 9: Battery Thermal Management & AIS-156 Safety Regulations
- **Hours 1–3:** Thermal Runaway cascade: SEI breakdown ($80-120^\circ\text{C}$), separator melting ($130-170^\circ\text{C}$), cathode oxygen liberation ($>200^\circ\text{C}$), and flammable gas venting.
- **Hours 4–5.5:** Indian regulatory standard **AIS-156 (Amendment 3)**: Thermal propagation containment, 5-minute pre-warning audio-visual alarm, cell spacing, and ingress protection (IP67).
- **Hours 6–6.5:** Battery Management System (BMS): Active vs passive cell balancing, State of Charge (SOC) estimation, and overcurrent/overvoltage protection.

#### Day 10: Practical Portfolio Projects 1 & 2
- **Hours 1–3.5:** Execute Project 1 (`05_PRACTICAL_PROJECTS/battery_enclosure_analysis/`): Structural FEA, material selection (Al 6061-T6 vs steel), dynamic crash load calculation, and mesh convergence.
- **Hours 4–6.5:** Execute Project 2 (`05_PRACTICAL_PROJECTS/manufacturing_quality_dashboard/`): Run synthetic production data, plot $\bar{X}-R$ control charts, calculate $C_p/C_{pk}$, and perform Pareto defect analysis.

#### Day 11: Practical Portfolio Projects 3 & 4
- **Hours 1–3.5:** Execute Project 3 (`05_PRACTICAL_PROJECTS/battery_thermal_analysis/`): 1D lumped capacitance transient thermal model, internal Joule heating ($I^2 R$), and cooling airflow sensitivity.
- **Hours 4–6.5:** Execute Project 4 (`05_PRACTICAL_PROJECTS/manufacturing_process_optimization/`): Assembly line balancing, bottleneck workstation identification, takt time alignment, and OEE optimization.

#### Day 12: Question Bank Drills (Online Assessment Practice)
- **Hours 1–3:** Solve 60 questions from `03_ASSESSMENT_PREPARATION/technical_test/` (Mechanics, SOM, and Design).
- **Hours 4–5:** Solve 50 questions from Manufacturing, Quality, and Metallurgy banks.
- **Hours 5.5–6.5:** Solve 30 quantitative aptitude and engineering numerical problems in `03_ASSESSMENT_PREPARATION/numerical_problems/`.

#### Day 13: Group Discussion Mastery & Candidate-Fit Pivot Defense
- **Hours 1–3:** Master the 20 Group Discussion playbooks in `04_GROUP_DISCUSSION/gd_topics.md` using factual arguments from `evidence_and_arguments.md`.
- **Hours 4–5.5:** Internalize the **Civil-to-EV Engineering Transition Defense** in `07_CANDIDATE_FIT_AND_CV/civil_to_ev_transition.md`. Rehearse aloud.
- **Hours 6–6.5:** Master the 30-second, 60-second, and 2-minute elevator pitches in `introduction_and_pitch.md`.

#### Day 14: Full Mock Assessment, Plant Scenarios & HR Rehearsal
- **Hours 1–3:** Execute the 120-minute, 50-Question Full-Length Mock Assessment in `03_ASSESSMENT_PREPARATION/mock_tests/full_length_mock.md` under timed test conditions.
- **Hours 3.5–4.5:** Review the 8 Plant Troubleshooting Scenarios in `06_INTERVIEW_PREPARATION/engineering_scenarios.md`.
- **Hours 5–6:** Rehearse the 30 STAR behavioral questions in `06_INTERVIEW_PREPARATION/behavioural_interview.md`. Review the formula cheat sheet.

---
*End of 14-Day Comprehensive Preparation Plan.*

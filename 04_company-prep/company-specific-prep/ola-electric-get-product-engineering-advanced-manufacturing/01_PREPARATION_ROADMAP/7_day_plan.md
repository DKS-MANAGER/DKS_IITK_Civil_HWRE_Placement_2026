# 7-Day Emergency Crash Revision Plan (48 Study Hours)
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Schedule Intensity:** 7 Hours/Day (Days 1–6) + 6 Hours (Day 7) = 48 Total Hours  

---

## Roadmap Overview

Designed for candidates with an upcoming test or interview scheduled within one week. Focus is strictly on P0 non-negotiables, high-frequency question patterns, and core interview narratives.

```
DAY 1: Eligibility Audit + Mechanics, Stress & Failure Theories (7 Hours)
DAY 2: Strength of Materials, Torsion & Finite Element Analysis (7 Hours)
DAY 3: Manufacturing Processes: Die-Casting, Stamping & Welding (7 Hours)
DAY 4: Quality Engineering, Statistical Process Control (SPC) & Six Sigma (7 Hours)
DAY 5: Lithium-Ion Battery Engineering, Thermal Runaway & AIS-156 (7 Hours)
DAY 6: Group Discussion Playbook & Candidate-Fit Transition Defense (7 Hours)
DAY 7: Full-Length Mock Assessment, Plant Scenarios & 24-Hr Formula Review (6 Hours)
```

---

## Day-by-Day Hour-by-Hour Execution Schedule

### Day 1: Eligibility Audit + Engineering Mechanics & Failure Theories (7 Hours)
- **08:30 – 09:30 (1.0 hr):** Submit SPO eligibility clarification query (see `00_COMPANY_AND_ROLE_RESEARCH/eligibility_verification.md`). Read `company_overview.md`.
- **09:30 – 12:30 (3.0 hrs):** Mechanics of Materials: Normal & shear stress, strain tensors, generalized Hooke's Law, Mohr's circle derivation (2D and 3D), and principal stresses.
- **14:00 – 16:30 (2.5 hrs):** Theories of Failure: Maximum Normal Stress (Rankine), Maximum Shear Stress (Tresca), and Distortion Energy (Von Mises) derivations. S-N curves, fatigue endurance limit, and Marin factors.
- **16:30 – 17:30 (1.0 hr):** Solve 15 numerical problems on Mohr's circle and Von Mises yield stress.
- *Day 1 Milestone Check:* Able to draw Mohr's circle for pure shear and state the exact yield condition for Von Mises ($\sigma_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2} \ge S_y$).

---

### Day 2: Strength of Materials, Mechanical Design & FEA (7 Hours)
- **09:00 – 11:30 (2.5 hrs):** Bending stresses in beams ($\sigma = My/I$), shear stresses ($\tau = VQ/Ib$), torsion in circular and thin-walled tubular shafts ($\tau = Tr/J$), and Euler buckling.
- **11:30 – 13:00 (1.5 hrs):** Chassis and battery enclosure design: Bolted joints (clamping force, bolt grade, torque-tension relationship $T = K F d$) and welded joint sizing.
- **14:30 – 17:00 (2.5 hrs):** Finite Element Analysis (FEA): 1D bar, 2D shell, and 3D solid elements; mesh convergence and boundary condition selection; contact modeling (frictional, bonded); common simulation errors (stiffness matrix singularity, stress singularities).
- **17:00 – 17:30 (0.5 hr):** Review `05_PRACTICAL_PROJECTS/battery_enclosure_analysis/` workflow.
- *Day 2 Milestone Check:* Can explain why a sharp re-entrant corner produces infinite stress in linear FEA and how to resolve it with fillets and sub-modeling.

---

### Day 3: Advanced Manufacturing Processes (7 Hours)
- **09:00 – 12:00 (3.0 hrs):** High-Pressure Die-Casting (HPDC): Cold-chamber vs hot-chamber, clamping force calculation, defect diagnosis (gas porosity vs shrinkage porosity, cold shuts, flash), and mitigation.
- **12:00 – 13:30 (1.5 hrs):** Precision Sheet Metal Stamping: Blanking, piercing, bending allowances, springback mechanics and compensation methods, deep drawing and forming limit diagrams (FLD).
- **14:30 – 16:30 (2.0 hrs):** Robotic Welding: MIG/MAG gas shielding mixtures ($80\% \text{ Ar} / 20\% \text{ CO}_2$), heat-affected zone (HAZ) metallurgy, weld cracking (hot vs cold cracks), and laser welding of battery busbars.
- **16:30 – 17:30 (1.0 hr):** Plastic injection molding: Cycle stages, sink marks, warpage, and mold shrinkage allowances.
- *Day 3 Milestone Check:* Can troubleshoot a porous die-cast aluminum swingarm by adjusting injection velocity, gate location, or vacuum assist.

---

### Day 4: Quality Engineering, SPC & Six Sigma (7 Hours)
- **09:00 – 12:00 (3.0 hrs):** Statistical Process Control (SPC): Variable control charts ($\bar{X}-R$ and $\bar{X}-S$), attribute charts ($p, c, u$). Derivation of 3-sigma control limits ($A_2, D_3, D_4$ constants). Western Electric out-of-control rules.
- **12:00 – 13:30 (1.5 hrs):** Process Capability Indices: Derivation and calculation of $C_p = \frac{USL - LSL}{6\sigma}$ and $C_{pk} = \min\left(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$. Meaning of $C_p > C_{pk}$ (process decentering).
- **14:30 – 16:30 (2.0 hrs):** Quality Problem-Solving Tools: Ishikawa (Fishbone) diagram, 5-Whys, Pareto analysis (80/20 rule), Failure Mode and Effects Analysis (FMEA: Severity, Occurrence, Detection, RPN), and 8D methodology.
- **16:30 – 17:30 (1.0 hr):** Industrial Engineering: Takt time calculation ($Takt = \frac{\text{Available Time}}{\text{Customer Demand}}$), Overall Equipment Effectiveness ($OEE = A \times P \times Q$).
- *Day 4 Milestone Check:* Solve 5 numerical problems on $C_p, C_{pk}$, scrap rate reduction, and takt time balancing.

---

### Day 5: EV Battery Systems, Thermal Runaway & AIS-156 (7 Hours)
- **09:00 – 12:00 (3.0 hrs):** Lithium-ion Electrochemistry: Cathodes (NMC 811 vs LFP), graphite anodes, separators, liquid electrolytes. Energy density vs thermal stability trade-offs. The 4680 "Bharat Cell" tabless design and internal impedance reduction.
- **12:00 – 13:30 (1.5 hrs):** Thermal Management & Runaway: Solid Electrolyte Interphase (SEI) breakdown ($80-120^\circ\text{C}$), separator melting ($130-170^\circ\text{C}$), cathode oxygen liberation ($>200^\circ\text{C}$). Venting gas dynamics and thermal propagation.
- **14:30 – 16:30 (2.0 hrs):** Regulatory Compliance: AIS-156 (Amendment 3) mandates: 5-minute pre-warning audio-visual alarm, thermal runaway containment, cell-to-cell spacing, thermal barrier aerogels.
- **16:30 – 17:30 (1.0 hr):** Battery Management System (BMS): State of Charge (SOC) via Coulomb counting and Kalman filtering; State of Health (SOH); active vs passive cell balancing.
- *Day 5 Milestone Check:* Can explain the complete cascade of thermal runaway and the exact legal requirements of AIS-156 Amendment 3.

---

### Day 6: Group Discussion (GD) Playbook & Candidate-Fit Transition (7 Hours)
- **09:00 – 12:00 (3.0 hrs):** Group Discussion Preparation: Master the top 10 EV and manufacturing GD topics (Battery Swapping vs Charging, LFP vs NMC, FAME/PM E-DRIVE subsidies, Automation vs Jobs). Rehearse opening lines, data presentation, and collaborative interventions.
- **12:00 – 13:30 (1.5 hrs):** Candidate-Fit Defense: Memorize and personalize the answer to: *"You are from Civil Engineering and HWRE. Why should Ola Electric hire you for EV product engineering and advanced manufacturing?"*
- **14:30 – 16:30 (2.0 hrs):** Behavioral Interview Prep: Rehearse 15 core STAR stories (Safety / Stop Work, handling production pressure, cross-functional collaboration, technical disagreements).
- **16:30 – 17:30 (1.0 hr):** Practice the 30-second and 2-minute elevator pitch.
- *Day 6 Milestone Check:* Can deliver the 2-minute civil-to-EV engineering pitch without hesitation or defensive apologies.

---

### Day 7: Full Mock Assessment, Plant Scenarios & Final Polish (6 Hours)
- **09:00 – 11:00 (2.0 hrs):** Execute the 120-minute, 50-Question Full-Length Mock Assessment in `03_ASSESSMENT_PREPARATION/mock_tests/full_length_mock.md` under timed exam conditions.
- **11:00 – 12:30 (1.5 hrs):** Score and audit mock test mistakes; log errors in `08_TRACKING_AND_REVISION/weak_topics.md`.
- **14:00 – 15:30 (1.5 hrs):** Rehearse the 8 Plant Troubleshooting Scenarios in `06_INTERVIEW_PREPARATION/engineering_scenarios.md`.
- **15:30 – 16:30 (1.0 hr):** Final review of `01_PREPARATION_ROADMAP/revision_checklist.md` formula sheet.
- *Day 7 Milestone Check:* Scored $\ge 75\%$ on the full-length mock assessment; all core formulas committed to active memory.

---
*End of 7-Day Emergency Crash Revision Plan.*

# Vantage Research — Sources, Evidence Classification & Verification Registry

> **Document Type**: Comprehensive Evidentiary Registry & Literature Traceability Audit  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Last Audited**: October 2026  

---

## 1. Evidentiary Standards & Hierarchy

This preparation suite adheres to a strict 5-tier evidence hierarchy to guarantee factual accuracy and scientific rigor:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          5-TIER EVIDENCE HIERARCHY                          │
├─────────┬───────────────────────────────────────────────────────────────────┤
│ TIER 1  │ Official Primary Recruitment Sources                              │
│         │ • Official Vantage Research job postings & application portal     │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 2  │ Official Corporate & Conference Publications                      │
│         │ • Corporate website, published abstracts (PAGE, ASCPT, ACoP)      │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 3  │ IIT Kanpur Institutional Placement & Alumni Records               │
│         │ • Verified alumni interview debriefs (AnC Placement Fundae)       │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 4  │ Peer-Reviewed Scientific Literature & Regulatory Standards        │
│         │ • Established textbooks, peer-reviewed QSP papers, FDA guidelines │
├─────────┼───────────────────────────────────────────────────────────────────┤
│ TIER 5  │ Pedagogical Practice Benchmarks                                   │
│         │ • Internally simulated mock assessments & technical test banks    │
└─────────┴───────────────────────────────────────────────────────────────────┘
```

---

## 2. Source Registry & Fact Traceability Table

| Source ID | Citation & Reference Title | URL / Publication Venue | Date | Evidence Tier | Relevant Supported Claims |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `SRC-01` | **Vantage Research Official Job Posting**: *Scientist – Modeler* (Job ID 33897) | [vantageresearch.keka.com/careers/jobdetails/33897](https://vantageresearch.keka.com/careers/jobdetails/33897) | 2024–2026 | **Tier 1** | Stated qualifications (Master's/PhD/Bachelor's in Chemical, Mechanical, Aerospace, Biomedical, Bioengineering, Computational Sciences, Math, Physics; Civil is *not* listed on portal); technical competencies (ODE/PDE, parameter estimation, sensitivity analysis); recruitment stages ("MSQ assessment followed by two interview rounds"); dual Sc1/Sc2 evaluation structure; in-office Chennai location. |
| `SRC-02` | **Vantage Research Corporate Portal**: *Your Partner for Model-Informed Drug Development* | [vantage-research.net](https://vantage-research.net/) · [Services](https://vantage-research.net/services/) | 2023–2026 | **Tier 2** | CRO business model; QSP modeling capabilities; therapeutic focus in Oncology, Immunology, Diabetes, Metabolism; global client consulting model; translational modeling workflows. |
| `SRC-03` | **Vantage Research Scientific Conference Proceedings**: *VQMTools & Mechanistic QSP Presentations* | [PAGE Meetings](https://www.page-meeting.org/) & [ACoP (Pharmacometrics)](https://www.go-acop.org/) | 2021–2025 | **Tier 2** | Scientific presentations demonstrating `VQMTools` for virtual population generation and global sensitivity analysis; mechanistic modeling of antibody-drug conjugates and immuno-oncology combinations. |
| `SRC-04` | **IIT Kanpur AnC Council Placement Fundae**: *Placement Fundae # 3 : Research — Advaith Kannan (Y21 BSBE)* | [Medium — AnC Council IIT Kanpur](https://medium.com/@anccounciliitk) | 2024–2025 | **Tier 3** | Candidate interview debrief for Vantage Research Scientist role; corroborates that interviews thoroughly examine resume projects/internships and test fundamental applied mathematics (ODEs, differential equations). *Note: Reflects a single candidate's anecdotal interview experience, not official company policy on fixed durations.* |
| `SRC-05` | **Dayneka, Garg, and Jusko**: *Comparison of Four Basic Models of Indirect Pharmacodynamic Responses* | *J. Pharmacokinet. Biopharm.*, 21(4): 457–478 | 1993 | **Tier 4** | Mathematical formulation of Indirect Response Models Types I–IV (inhibition/stimulation of synthesis $k_{in}$ or loss $k_{out}$). |
| `SRC-06` | **Krzyzanski and Jusko**: *Mathematical Aspects of Target-Mediated Drug Disposition (TMDD) Models* | *J. Pharmacokinet. Pharmacodyn.*, 28(3): 239–264 | 2001 | **Tier 4** | Complete system of coupled non-linear ODEs for target binding, complex internalization, and concentration-dependent non-linear clearance. |
| `SRC-07` | **Guglielmo et al.**: *Quantitative Systems Pharmacology: A Primer on Modeling Principles and Applications* | *CPT: Pharmacometrics & Systems Pharmacology*, 8(1): 11–24 | 2019 | **Tier 4** | QSP multi-scale modeling definitions, mass action formulations, parameter estimation protocols, and virtual population generation. |
| `SRC-08` | **Saltelli et al.**: *Global Sensitivity Analysis: The Primer* | John Wiley & Sons, Chichester, UK | 2008 | **Tier 4** | Mathematical foundations of variance-based global sensitivity analysis (Sobol first-order $S_i$ and total-order $S_{Ti}$ indices) and Morris screening. |
| `SRC-09` | **Hairer, Nørsett, and Wanner**: *Solving Ordinary Differential Equations I: Nonstiff Problems & II: Stiff Problems* | Springer-Verlag, Berlin / Heidelberg | 1993 / 1996 | **Tier 4** | Butcher tableaus, Runge-Kutta order conditions, linear stability regions in complex plane, A-stability, L-stability, and Radau IIA / BDF formulations. |
| `SRC-10` | **FDA Guidance for Industry**: *Population Pharmacokinetics and Model-Informed Drug Development (MIDD)* | U.S. Food and Drug Administration (CDER / CBER) | 2022 | **Tier 4** | Regulatory expectations for model verification, parameter identifiability, sensitivity analysis, and virtual clinical trial credibility. |
| `SRC-11` | **Internal Vantage Preparation Practice Suite**: *Modules 01–10, MSQ Bank & Mock Interviews* | Repository `vantage-research-scientist-modeler/` | Oct 2026 | **Tier 5** | Internally formulated practice questions, code architectures, and dialogue drills calibrated to official role competencies. |

---

## 3. Scope Boundaries & Evidentiary Safeguards

1. **No Proprietary Client Data**: This repository does not contain confidential client models, proprietary drug structures, or internal commercial code belonging to Vantage Research or its biopharmaceutical sponsors.
2. **Synthetic Data Labeling**: All calibration exercises in Module 04 use synthetic in silico datasets generated via explicitly documented Python functions.
3. **Simulation Labels on Practice Questions**: All practice questions in Module 09 and mock interviews in Module 10 are designated as internal practice simulations calibrated to the verified job description.

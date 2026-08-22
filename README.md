# IITK Civil & HWRE Placement Preparation (Dec 2026)

Targeted preparation hub for core engineering, numerical modeling/CFD, non-core analytics, and interview strategy.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Content](https://img.shields.io/badge/Content-46%20topics%2C%2091%20files-brightgreen)](index/master_index.md) [![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v2412-blue)](https://openfoam.org/) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)

## Quick Navigation

- [Core Civil & HWRE](#core-civil--hwre)
- [CFD & Modeling Case Studies](#cfd--numerical-modeling)
- [Analytics & Non-Core](#analytics--non-core)
- [Company Interview Intel](#company-intel--question-banks)
- [Aptitude & Behavioral](#aptitude--hr-prep)

---

## Preparation Roadmap & Timeline

- **Phase 1 (Aug–Sep):** Core theory revision + GATE PYQs
- **Phase 2 (Oct–Nov):** Non-Core SQL/Python prep, Aptitude speed tests
- **Phase 3 (Dec):** Company-specific interview prep and Mock rounds

See [placement-roadmap.md](placement-roadmap.md) for the detailed phased timeline.

---

## Core Civil & HWRE

| Domain | Key Topics | Direct Links |
| :--- | :--- | :--- |
| **Hydraulics & CFD** | Boundary layer, pipe networks, turbulence modeling, OpenFOAM setup | [`civil/hydraulics/`](civil/hydraulics/) |
| **Open Channel & WR** | GVF/RVF, jumps, flood routing, reservoir operations | [`civil/open_channel_flow/`](civil/open_channel_flow/), [`civil/hydrology/`](civil/hydrology/) |
| **Water & Wastewater** | Treatment design, distribution networks, sewer modeling | [`hwre/water_supply/`](hwre/water_supply/), [`hwre/wastewater/`](hwre/wastewater/) |
| **Structures & Geo** | SOM, RCC, soil mechanics, bearing capacity | [`civil/structures/`](civil/structures/), [`civil/geotechnical/`](civil/geotechnical/) |

---

## CFD & Numerical Modeling

| Case Study | Solver / Method | Validation / Focus |
| :--- | :--- | :--- |
| [2D Pipeline Scour — SedFOAM](https://github.com/DKS-MANAGER/2DPipelineScour) | `sedFoam_rbgh`, Eulerian Two-Phase, k-ω SST | Mao (1986), Larsen et al. (2016) |
| [2D Pipeline Scour — sedExnerFoam EXN](https://github.com/DKS-MANAGER/2DPipelineScourEXN) | `sedExnerFoam`, Exner + ALE, FAM | OpenFOAM 2412 compatibility patches |
| [Calibrated sedExnerFoam](https://github.com/DKS-MANAGER/PipelineScour_Calibrated) | Nielsen (1992) bedload, 2-phase workflow | 20-core MPI, morphological acceleration 2× |
| [Bridge Pier Contraction Scour](https://github.com/DKS-MANAGER/bridge_sedfoam) | `sedFoam_rbgh`, Boyer μ(I) rheology | Majid et al. (2026), ASCE validation |
| [Bridge Pier Live-Bed Scour](https://github.com/DKS-MANAGER/bridge_sedfoam_livebed) | θ > θcr, upstream sediment supply | Equilibrium scour under mobile-bed conditions |
| [Bridge Pier Downstream Wake](https://github.com/DKS-MANAGER/bridge_sedfoam_downstream) | Extended downstream domain | Wake morphology, deposition ridge, TKE |
| [Flow-Induced Vibration *(Active)*](https://github.com/DKS-MANAGER) | CFD + structural coupling | Rough-wall BCs, multiphase pipelines |

---

## Analytics & Non-Core

- **Tech Stack:** Python (NumPy/Pandas), SQL, Excel modeling, MATLAB ([`resources/non-core-prep.md`](resources/non-core-prep.md), [`resources/technical-stack.md`](resources/technical-stack.md)).
- **Quantitative & Reasoning:** 14 Quant topics, speed math tricks, logical puzzles ([`aptitude/quantitative/`](aptitude/quantitative/), [`aptitude/logical_reasoning/`](aptitude/logical_reasoning/)).

---

## Company Intel & Question Banks

| Resource | Coverage |
| :--- | :--- |
| [`interviews/technical/`](interviews/technical/) | Technical interview bank, project discussion frameworks |
| [`interviews/company_specific/`](interviews/company_specific/) | 10 company profiles + interview transcripts |
| [`interviews/hr/`](interviews/hr/) | HR interview guide, salary negotiation |
| [`interviews/mock_questions/`](interviews/mock_questions/) | Curated mock questions for practice |
| [`resources/placement-data.md`](resources/placement-data.md) | Company CTC, profiles, skills |
| [`gate/practice/`](gate/practice/) | 50 GATE practice problems with solutions |

---

## Aptitude & HR Prep

- **Aptitude:** 14 quantitative topics, data interpretation, speed math shortcuts ([`aptitude/`](aptitude/)).
- **Behavioral:** STAR method, conflict resolution, leadership, teamwork, HR questions ([`behavioral/behavioral-interview-guide.md`](behavioral/behavioral-interview-guide.md), [`behavioral/hr_questions/`](behavioral/hr_questions/)).

---

## Interview & Application Toolkit

- **Templates:** [Resume Template](templates/resume-template.md) | [Self-Intro Framework](templates/self-intro-template.md) | [STAR Behavioral Guide](behavioral/behavioral-interview-guide.md)
- **Question Banks:** [Technical Interview Bank](interviews/technical/) | [Company Profiles & Transcripts](interviews/company_specific/) | [HR & Negotiation Guide](interviews/hr/)
- **Compensation & CTC Intel:** [Placement Data & CTCs](resources/placement-data.md)

---

## References

This repository synthesizes content from the following source repositories:

| Source Repository | Focus |
| :--- | :--- |
| [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK) | Core civil/HWRE syllabus, roadmap, technical interview bank |
| [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering) | Software tools, GIS, structural/geotechnical packages |
| [Aptitude](https://github.com/DKS-MANAGER/Aptitude) | Quantitative aptitude, logical reasoning, verbal ability |
| [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) | Placement-focused quant practice problems |
| [awesome-behavioral-interviews](https://github.com/awesome-behavioral-interviews/awesome-behavioral-interviews) | STAR method, self-intro, teamwork, leadership, conflict |
| [awesome-interview-questions](https://github.com/awesome-interview-questions/awesome-interview-questions) | HR interview guide, mock questions |
| [behavioral-interview-list-of-questions](https://github.com/DKS-MANAGER/behavioral-interview-list-of-questions) | Behavioral question bank, interview process tips |
| [campus-placement-prep](https://github.com/DKS-MANAGER/campus-placement-prep) | Placement roadmap, resume tips, interview practice |
| [Placement_Preparation](https://github.com/DKS-MANAGER/Placement_Preparation) | Company-wise interview experiences and transcripts |
| [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027) | GATE Civil notes, formulas, PYQs, revision summaries |
| [interview-handbook-2026](https://github.com/DKS-MANAGER/interview-handbook-2026) | Behavioral, technical, curveball, and end-of-interview questions |

> **Note:** Content has been paraphrased and synthesized from public repositories; see individual `## References` sections for source attribution.

# IITK Civil & HWRE Placement Preparation (Dec 2026)

> **Targeted preparation hub for core engineering, numerical modeling/CFD, non-core analytics, and interview strategy.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Content](https://img.shields.io/badge/Content-50%20topics%2C%2066%20files-brightgreen)](index/master_index.md) [![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v2412-blue)](https://openfoam.org/) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/) [![Phase](https://img.shields.io/badge/Phase-0%20Bootstrap-orange)](placement-roadmap.md) [![Last Updated](https://img.shields.io/badge/Updated-2026--09--03-lightgrey)]()

---

## 🚀 Quick Start

1. **New here?** Read the [Placement Roadmap](placement-roadmap.md) for the full 5-phase plan.
2. **Study planner + progress tracker:** Open [`.roo/modes/fable.md`](.roo/modes/fable.md) — your one-stop command center.
3. **Resume & templates:** Start with [`templates/resume-template.md`](templates/resume-template.md).
4. **Company intel:** Browse [`interviews/company_specific/`](interviews/company_specific/) for 14+ company profiles.

---

## 📅 Study Schedule Overview

| Phase | Dates | Focus | Priority | Status |
|-------|-------|-------|----------|--------|
| **Phase 0: Bootstrap** | Aug 21 – Sep 7 | Resume, syllabus map, repo setup | P0 | ⬜ |
| **Phase 1: Core Revision** | Sep 8 – Sep 30 | Hydraulics, Hydrology, Structures, Geotech | P0 | ⬜ |
| **Phase 2: Mock & Coding** | Oct 1 – Oct 20 | Mock interviews, Python/SQL, STAR bank | P0 | ⬜ |
| **Phase 3: Company-Wise** | Oct 21 – Nov 10 | PSU, Core, Analytics company prep | P1 | ⬜ |
| **Phase 4: Final Revision** | Nov 11 – Dec 1 | Flashcards, cheat-sheets, final mocks | P0 | ⬜ |
| **Phase 5: Live Interviews** | Dec 2026 | Execute, log, postmortem, iterate | P0 | ⬜ |

> 📊 **Full daily planner & progress dashboard:** [`.roo/modes/fable.md`](.roo/modes/fable.md#-study-planner)

---

## 📊 Weekly Progress Tracker

| Week | Dates | Study Hrs | Numericals | Mocks | STAR Stories | Coding | Status |
|------|-------|-----------|------------|-------|-------------|--------|--------|
| W1 | Sep 8–14 | /50 | /50 | /2 | /5 | /3 | ⬜ |
| W2 | Sep 15–21 | /50 | /50 | /2 | /5 | /3 | ⬜ |
| W3 | Sep 22–28 | /50 | /50 | /2 | /5 | /3 | ⬜ |
| W4 | Sep 29–30 | /10 | /20 | /1 | /2 | /1 | ⬜ |
| W5 | Oct 1–7 | /50 | /30 | /2 | /5 | /3 | ⬜ |
| W6 | Oct 8–14 | /50 | /30 | /2 | /5 | /3 | ⬜ |
| W7 | Oct 15–20 | /40 | /20 | /2 | /3 | /2 | ⬜ |
| W8 | Oct 21–27 | /50 | /30 | /2 | /5 | /2 | ⬜ |
| W9 | Oct 28–Nov 3 | /50 | /30 | /2 | /5 | /2 | ⬜ |
| W10 | Nov 4–10 | /50 | /30 | /2 | /3 | /2 | ⬜ |
| W11 | Nov 11–17 | /50 | /40 | /3 | /5 | /2 | ⬜ |
| W12 | Nov 18–24 | /50 | /40 | /3 | /5 | /2 | ⬜ |
| W13 | Nov 25–Dec 1 | /40 | /30 | /2 | /3 | /1 | ⬜ |

---

## 🗂️ Content Map

### 🏗️ Core Civil & HWRE

| Domain | Key Topics | Direct Links |
|:-------|:-----------|:-------------|
| **Hydraulics & CFD** | Boundary layer, pipe networks, turbulence modeling, OpenFOAM setup | [`civil/hydraulics/`](civil/hydraulics/) |
| **Open Channel & WR** | GVF/RVF, jumps, flood routing, reservoir operations | [`civil/open_channel_flow/`](civil/open_channel_flow/), [`civil/hydrology/`](civil/hydrology/) |
| **Water & Wastewater** | Treatment design, distribution networks, sewer modeling | [`hwre/water_supply/`](hwre/water_supply/), [`hwre/wastewater/`](hwre/wastewater/) |
| **Structures & Geo** | SOM, RCC, soil mechanics, bearing capacity | [`civil/structures/`](civil/structures/), [`civil/geotechnical/`](civil/geotechnical/) |
| **Irrigation & Flood** | Canal design, flood control, drainage | [`hwre/irrigation/`](hwre/irrigation/), [`hwre/flood_control/`](hwre/flood_control/) |
| **Environmental Engg** | Water/air pollution, BOD/COD, treatment, EIA, solid waste | [`civil/environmental/`](civil/environmental/) |
| **Geoinformatics** | GIS, Remote Sensing, GNSS, LiDAR, spatial analysis | [`civil/geoinformatics/`](civil/geoinformatics/) |
| **Infrastructure Engg & Mgmt** | CPM/PERT, construction mgmt, cost estimation, PPP | [`civil/infrastructure/`](civil/infrastructure/) |
| **Transportation Engg** | Highway design, pavement, traffic, railway, airport | [`civil/transportation/`](civil/transportation/) |

---

### 🌊 CFD & Numerical Modeling

| Case Study | Solver / Method | Validation / Focus |
|:-----------|:----------------|:-------------------|
| [2D Pipeline Scour — SedFOAM](https://github.com/DKS-MANAGER/2DPipelineScour) | `sedFoam_rbgh`, Eulerian Two-Phase, k-ω SST | Mao (1986), Larsen et al. (2016) |
| [2D Pipeline Scour — sedExnerFoam EXN](https://github.com/DKS-MANAGER/2DPipelineScourEXN) | `sedExnerFoam`, Exner + ALE, FAM | OpenFOAM 2412 compatibility patches |
| [Calibrated sedExnerFoam](https://github.com/DKS-MANAGER/PipelineScour_Calibrated) | Nielsen (1992) bedload, 2-phase workflow | 20-core MPI, morphological acceleration 2× |
| [Bridge Pier Contraction Scour](https://github.com/DKS-MANAGER/bridge_sedfoam) | `sedFoam_rbgh`, Boyer μ(I) rheology | Majid et al. (2026), ASCE validation |
| [Bridge Pier Live-Bed Scour](https://github.com/DKS-MANAGER/bridge_sedfoam_livebed) | θ > θcr, upstream sediment supply | Equilibrium scour under mobile-bed conditions |
| [Bridge Pier Downstream Wake](https://github.com/DKS-MANAGER/bridge_sedfoam_downstream) | Extended downstream domain | Wake morphology, deposition ridge, TKE |
| [Flow-Induced Vibration *(Active)*](https://github.com/DKS-MANAGER) | CFD + structural coupling | Rough-wall BCs, multiphase pipelines |

---

### 🧮 Analytics & Non-Core

- **Tech Stack:** Python (NumPy/Pandas), SQL, Excel modeling, MATLAB — see [`resources/non-core-prep.md`](resources/non-core-prep.md), [`resources/technical-stack.md`](resources/technical-stack.md).
- **Quantitative & Reasoning:** 14 Quant topics, speed math tricks, logical puzzles — see [`aptitude/quantitative/`](aptitude/quantitative/), [`aptitude/logical_reasoning/`](aptitude/logical_reasoning/).
- **Speed Math:** 50+ shortcuts for placement aptitude — see [`aptitude/shortcuts/aptitude-shortcuts.md`](aptitude/shortcuts/aptitude-shortcuts.md).

---

### 🏢 Company Intel & Question Banks

| Resource | Coverage |
|:---------|:---------|
| [`interviews/technical/`](interviews/technical/) | Technical interview bank, project discussion frameworks |
| [`interviews/company_specific/`](interviews/company_specific/) | 14 company profiles + interview transcripts |
| [`interviews/hr/`](interviews/hr/) | HR interview guide, salary negotiation |
| [`interviews/mock_questions/`](interviews/mock_questions/) | 50+ curated mock questions with answers |
| [`resources/placement-data.md`](resources/placement-data.md) | Company CTC, profiles, skills (60+ companies) |
| [`gate/practice/`](gate/practice/) | 50 GATE practice problems with solutions |

---

### 🎤 Aptitude & HR Prep

- **Aptitude:** 14 quantitative topics, data interpretation, speed math shortcuts — [`aptitude/`](aptitude/).
- **Behavioral:** STAR method, conflict resolution, leadership, teamwork, HR questions — [`behavioral/behavioral-interview-guide.md`](behavioral/behavioral-interview-guide.md), [`behavioral/hr_questions/`](behavioral/hr_questions/).
- **Self Introduction:** 5 sample introductions + frameworks — [`behavioral/self_intro/self-introduction.md`](behavioral/self_intro/self-introduction.md).

---

### 📋 GATE Preparation

| Resource | Content |
|:---------|:--------|
| [`gate/civil/gate-civil-notes.md`](gate/civil/gate-civil-notes.md) | Topic-wise GATE Civil notes |
| [`gate/formulas/gate-civil-formulas.md`](gate/formulas/gate-civil-formulas.md) | Complete formula sheet |
| [`gate/revision_notes/gate-civil-revision.md`](gate/revision_notes/gate-civil-revision.md) | Rapid revision cards |
| [`gate/practice/gate-civil-practice.md`](gate/practice/gate-civil-practice.md) | 50+ solved problems |

---

## 📄 Interview & Application Toolkit

| Category | Resources |
|:---------|:----------|
| **Templates** | [Resume](templates/resume-template.md) · [Self-Intro](templates/self-intro-template.md) · [Interview Answer](templates/interview-answer-template.md) · [Study Plan](templates/study-plan-template.md) |
| **Question Banks** | [Technical Q&A](interviews/technical/technical-interview-bank.md) · [Mock Questions](interviews/mock_questions/mock-interview-questions.md) · [HR Guide](interviews/hr/hr-interview-guide.md) |
| **Company Intel** | [14 Company Profiles](interviews/company_specific/company-profiles.md) · [Interview Experiences](interviews/company_specific/interview-experiences.md) · [CTC Data](resources/placement-data.md) |
| **Behavioral** | [STAR Guide](behavioral/behavioral-interview-guide.md) · [30+ STAR Stories](behavioral/behavioral-interview-guide.md) · [HR Questions Bank](behavioral/hr_questions/hr-questions-bank.md) |

---

## 🔗 Master Index & Navigation

| Index | Description |
|:------|:------------|
| [`index/master_index.md`](index/master_index.md) | Complete topic index (46 topics, source mapping) |
| [`index/topic_map.md`](index/topic_map.md) | Topic → source → destination mapping |
| [`index/file_inventory.csv`](index/file_inventory.csv) | CSV inventory of all files |
| [`index/source_map.csv`](index/source_map.csv) | Source repository mapping |

---

## 📚 References

This repository synthesizes content from the following source repositories:

| Source Repository | Focus |
|:------------------|:------|
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

---

## 🛠️ Repository Setup

```bash
# Clone the repository
git clone https://github.com/DKS-MANAGER/DKS_IITK_Civil_HWRE_Placement_2026.git
cd DKS_IITK_Civil_HWRE_Placement_2026

# Validate index integrity
python scripts/validate_index.py
```

See [`SETUP.md`](SETUP.md) for detailed setup instructions.

---

## 📜 License

This project is licensed under the MIT License — see [`LICENSE`](LICENSE) for details.

---

> **Maintained by:** DKS · IIT Kanpur M.Tech Civil / HWRE · Placement 2026

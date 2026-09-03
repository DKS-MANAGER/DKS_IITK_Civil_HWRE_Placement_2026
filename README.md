<div align="center">

# 🏗️ IITK Civil & HWRE Placement Preparation 2026

**Comprehensive placement preparation hub for IIT Kanpur M.Tech Civil / HWRE students.**

Core engineering subjects · CFD & numerical modeling · Aptitude & behavioral prep · Interview strategy · GATE revision

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Content](https://img.shields.io/badge/Content-50%2B%20topics%2C%20105%2B%20files-brightgreen)](index/master_index.md)
[![OpenFOAM](https://img.shields.io/badge/OpenFOAM-v2412-blue)](https://openfoam.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Last Updated](https://img.shields.io/badge/Updated-2026--09--03-lightgrey)]()

</div>

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [At a Glance](#-at-a-glance)
- [Repository Structure](#-repository-structure)
- [Core Civil & HWRE Subjects](#-core-civil--hwre-subjects)
- [CFD & Numerical Modeling](#-cfd--numerical-modeling)
- [Interview & Placement Toolkit](#-interview--placement-toolkit)
- [Aptitude & Behavioral Prep](#-aptitude--behavioral-prep)
- [GATE Preparation](#-gate-preparation)
- [Study Schedule & Progress](#-study-schedule--progress)
- [Getting Started](#-getting-started)
- [Sources & References](#-sources--references)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Quick Start

| Step | Action | Link |
|:----:|:-------|:-----|
| **1** | **New here?** Read the Start Here guide below ↓ | See decision tree |
| **2** | Open the subject roadmap for your target role | [`prep/quick-revision-system.md`](prep/quick-revision-system.md) |
| **3** | Practice 1 mock interview from the database | [`prep/mock-tests/mock-interview-database.md`](prep/mock-tests/mock-interview-database.md) |
| **4** | Start with the resume template | [`prep/templates/resume-template.md`](prep/templates/resume-template.md) |

---

## 🎯 Start Here — Find Your Path

> **Not sure where to begin?** Pick your situation below:

<table>
<tr>
<td align="center" width="25%">

**🎯 Target: HWRE / Water Resources**

</td>
<td align="center" width="25%">

**🏗️ Target: Core Civil (Structures / Consulting)**

</td>
<td align="center" width="25%">

**🖥️ Target: CFD / Research**

</td>
<td align="center" width="25%">

**⏰ Interview is TOMORROW**

</td>
</tr>
<tr>
<td>

1. [`hydraulics.md`](core/hwre/hydraulics/hydraulics.md) → Formula Sheet + Q Bank
2. [`open-channel-flow.md`](core/hwre/open_channel_flow/open-channel-flow.md) → Formula Sheet + Q Bank
3. [`hydrology.md`](core/hwre/hydrology/hydrology.md) → Formula Sheet + Q Bank
4. [`water-resources-engineering.md`](core/hwre/water_resources/water-resources-engineering.md) → Formula Sheet
5. [`software-interview-guide.md`](prep/software-interview-guide.md) → HEC-RAS, SWMM, EPANET

</td>
<td>

1. [`structures.md`](core/structures/structures.md) → Formula Sheet + Q Bank
2. [`geotechnical.md`](core/geotechnical/geotechnical.md) → Formula Sheet + Q Bank
3. [`transportation-engineering.md`](core/transportation/transportation-engineering.md) → Quick Reference
4. [`infrastructure-engineering-management.md`](core/infrastructure/infrastructure-engineering-management.md) → CPM/PERT Q Bank
5. [`software-interview-guide.md`](prep/software-interview-guide.md) → STAAD, ETABS, PLAXIS

</td>
<td>

1. [`turbulence-modeling.md`](core/hwre/hydraulics/turbulence-modeling.md) → RANS, LES, OpenFOAM
2. [`hydraulics.md`](core/hwre/hydraulics/hydraulics.md) → Deep Technical Q Bank (G)
3. [`project-defense-guide.md`](prep/technical/project-defense-guide.md) → CFD-Specific 15 Qs
4. [`software-interview-guide.md`](prep/software-interview-guide.md) → OpenFOAM, ParaView, Python

</td>
<td>

🔴 **STOP everything.** Open this file:
→ [`quick-revision-system.md`](prep/quick-revision-system.md) → **1-Day Crash Plan**

Do ONLY:
1. Formula sheets (60 min)
2. Rapid-fire Q&A (30 min)
3. 2 High-Value interview answers (30 min)
4. Self-intro rehearsal (15 min)

</td>
</tr>
</table>

---

## 📊 At a Glance

<table>
<tr>
<td align="center"><strong>105+</strong><br>Markdown Files</td>
<td align="center"><strong>50+</strong><br>Covered Topics</td>
<td align="center"><strong>14</strong><br>Subject Guides</td>
<td align="center"><strong>7</strong><br>CFD Projects</td>
</tr>
<tr>
<td align="center"><strong>14+</strong><br>Company Profiles</td>
<td align="center"><strong>500+</strong><br>Interview Q&As</td>
<td align="center"><strong>8</strong><br>Mock Interviews</td>
<td align="center"><strong>3</strong><br>Revision Plans</td>
</tr>
</table>

---

## 📂 Repository Structure

```
DKS_IITK_Civil_HWRE_Placement_2026/
├── core/                              # ─── Technical Core ───
│   ├── hwre/                          # Unified HWRE: fluids, water, irrigation
│   │   ├── hydraulics/                #   Bernoulli, pipe networks, turbulence
│   │   ├── open_channel_flow/         #   GVF, RVF, hydraulic jump
│   │   ├── hydrology/                 #   Rainfall-runoff, flood routing, sediment
│   │   ├── water_resources/           #   Reservoir, canal, stage-discharge
│   │   ├── flood_control/             #   Flood modeling & drainage
│   │   ├── irrigation/                #   Canal design & water distribution
│   │   ├── wastewater/                #   Treatment, sewer modeling
│   │   ├── water_supply/              #   Distribution, groundwater
│   │   ├── exam_notes/                #   Quick reference & cheat sheets
│   │   └── hydraulics_notes/          #   Supplementary hydraulics notes
│   ├── structures/                    # SOM, RCC, steel, IS codes
│   ├── geotechnical/                  # Soil mechanics, bearing capacity, slopes
│   ├── environmental/                 # Water/air pollution, BOD/COD, EIA
│   ├── transportation/                # Highway, pavement, traffic, railway
│   ├── geoinformatics/                # GIS, Remote Sensing, GNSS, LiDAR
│   ├── infrastructure/                # CPM/PERT, construction mgmt, PPP
│   ├── fundamentals/                  # Civil engineering foundations
│   └── gate/                          # GATE Civil preparation
│       ├── civil/                     #   Topic-wise GATE notes
│       ├── formulas/                  #   Complete formula sheet
│       ├── practice/                  #   50+ solved problems
│       └── revision_notes/            #   Rapid revision cards
├── non-core/                          # ─── Non-Technical Tracks ───
│   ├── aptitude/                      # Quantitative & logical reasoning
│   │   ├── quantitative/              #   14 quant topics + data interpretation
│   │   ├── logical_reasoning/         #   Puzzles, seating, syllogisms
│   │   ├── shortcuts/                 #   50+ speed math shortcuts
│   │   └── verbal/                    #   Grammar, vocabulary, RC
│   └── analytics/                     # Python, SQL, Excel, MATLAB
├── prep/                              # ─── Interview Preparation ───
│   ├── behavioral/                    # STAR bank, HR, self-intros, leadership
│   ├── company-profiles/              # 14+ company profiles & CTC data
│   ├── mock-tests/                    # 50+ curated mock questions
│   ├── templates/                     # Resume, self-intro, study plan
│   ├── hr/                            # HR interview guide
│   └── technical/                     # Technical Q&A bank
├── docs/                              # Governance & roadmap
├── resources/                         # Books, links, papers, placement data
├── index/                             # Master index, topic map, inventory
├── scripts/                           # Validation & automation
└── .github/                           # CI, issue templates, PR template
```

---

## 🏗️ Core Civil & HWRE Subjects

| # | Subject | Key Topics | Guide |
|:-:|:--------|:-----------|:------|
| 1 | **Hydraulics & CFD** | Bernoulli, continuity, momentum, pipe friction, boundary layers, turbulence modeling | [`core/hwre/hydraulics/hydraulics.md`](core/hwre/hydraulics/hydraulics.md) |
| 2 | **Structural Engineering** | SOM, bending, columns, RCC design (IS 456), steel design (IS 800), moment distribution | [`core/structures/structures.md`](core/structures/structures.md) |
| 3 | **Geotechnical Engineering** | Soil classification, consolidation, bearing capacity, slope stability, pile foundations | [`core/geotechnical/geotechnical.md`](core/geotechnical/geotechnical.md) |
| 4 | **Environmental Engineering** | Water/air pollution, BOD/COD kinetics, treatment design, EIA, solid waste, climate | [`core/environmental/environmental-engineering.md`](core/environmental/environmental-engineering.md) |
| 5 | **Transportation Engineering** | Highway geometric design, pavement (IRC:37/58), traffic flow, railway, airport | [`core/transportation/transportation-engineering.md`](core/transportation/transportation-engineering.md) |
| 6 | **Geoinformatics** | GIS, Remote Sensing (NDVI/NDWI), GNSS/GPS, LiDAR, spatial analysis, image processing | [`core/geoinformatics/geoinformatics.md`](core/geoinformatics/geoinformatics.md) |
| 7 | **Infrastructure Engg & Mgmt** | CPM/PERT, EVM, cost estimation, PPP/HAM/BOT, urban planning, risk management | [`core/infrastructure/infrastructure-engineering-management.md`](core/infrastructure/infrastructure-engineering-management.md) |

### Additional Subject Modules

| Module | Topics | Path |
|:-------|:-------|:-----|
| Open Channel Flow | GVF, RVF, hydraulic jump, unsteady flow | [`core/hwre/open_channel_flow/`](core/hwre/open_channel_flow/) |
| Hydrology | Unit hydrograph, flood routing, rainfall-runoff | [`core/hwre/hydrology/`](core/hwre/hydrology/) |
| Water Resources Engineering | Reservoir, canal design, stage-discharge | [`core/hwre/water_resources/`](core/hwre/water_resources/) |
| Irrigation Engineering | Canal design, irrigation methods, water distribution | [`core/hwre/irrigation/`](core/hwre/irrigation/) |
| Wastewater Engineering | Collection systems, treatment, sewer modeling | [`core/hwre/wastewater/`](core/hwre/wastewater/) |
| Water Supply | Distribution systems, groundwater, treatment | [`core/hwre/water_supply/`](core/hwre/water_supply/) |
| Flood Control | Flood modeling, floodplain management, drainage | [`core/hwre/flood_control/`](core/hwre/flood_control/) |
| Turbulence Modeling | RANS, LES, DNS, k-ε, k-ω, wall functions | [`core/hwre/hydraulics/turbulence-modeling.md`](core/hwre/hydraulics/turbulence-modeling.md) |
| Transport Software | VISSIM, HEC-RAS, ANSYS, AutoCAD, QGIS | [`core/transportation/transportation-software.md`](core/transportation/transportation-software.md) |

---

## 🌊 CFD & Numerical Modeling

| Case Study | Solver / Method | Validation |
|:-----------|:----------------|:-----------|
| [2D Pipeline Scour — SedFOAM](https://github.com/DKS-MANAGER/2DPipelineScour) | `sedFoam_rbgh`, Eulerian Two-Phase, k-ω SST | Mao (1986), Larsen et al. (2016) |
| [2D Pipeline Scour — sedExnerFoam EXN](https://github.com/DKS-MANAGER/2DPipelineScourEXN) | `sedExnerFoam`, Exner + ALE, FAM | OpenFOAM 2412 compatibility |
| [Calibrated sedExnerFoam](https://github.com/DKS-MANAGER/PipelineScour_Calibrated) | Nielsen (1992) bedload, 2-phase | 20-core MPI, morphological acceleration 2× |
| [Bridge Pier Contraction Scour](https://github.com/DKS-MANAGER/bridge_sedfoam) | `sedFoam_rbgh`, Boyer μ(I) rheology | Majid et al. (2026), ASCE validation |
| [Bridge Pier Live-Bed Scour](https://github.com/DKS-MANAGER/bridge_sedfoam_livebed) | θ > θ_cr, upstream sediment supply | Equilibrium scour, mobile-bed |
| [Bridge Pier Downstream Wake](https://github.com/DKS-MANAGER/bridge_sedfoam_downstream) | Extended downstream domain | Wake morphology, TKE |
| [Flow-Induced Vibration *(Active)*](https://github.com/DKS-MANAGER) | CFD + structural coupling | Rough-wall BCs, multiphase |

---

## 🎯 Interview & Placement Toolkit

### 📅 Revision & Planning

| Resource | Description | When to Use |
|:---------|:------------|:------------|
| [**Quick Revision System**](prep/quick-revision-system.md) | 1-Day, 7-Day, 30-Day revision plans + checklist | **Start here** — pick your timeline |
| [Study Plan Template](prep/templates/study-plan-template.md) | Customizable daily/weekly study planner | Long-term preparation |

### 📝 Templates

| Template | Description |
|:---------|:------------|
| [Resume](prep/templates/resume-template.md) | ATS-friendly resume template for core roles |
| [Self-Introduction](prep/templates/self-intro-template.md) | 5 frameworks + sample introductions |
| [Interview Answer](prep/templates/interview-answer-template.md) | STAR-based answer structure |

### 🎤 Mock Interviews & Question Banks

| Resource | Coverage |
|:---------|:---------|
| [**Mock Interview Database**](prep/mock-tests/mock-interview-database.md) | **8 full mock sessions** — Easy → Expert |
| [Mock Questions (50)](prep/mock-tests/mock-interview-questions.md) | 50 curated questions with model answers |
| [Technical Q&A Bank (100)](prep/technical/technical-interview-bank.md) | 100 Q&A by topic with numericals |
| [**Project Defense Guide**](prep/technical/project-defense-guide.md) | Universal 20 Qs + CFD-Specific 15 Qs |

### 🏢 Company Intel & Behavioral

| Resource | Coverage |
|:---------|:---------|
| [Company Profiles](prep/company-profiles/) | 14+ company profiles + interview transcripts |
| [HR Questions Bank](prep/behavioral/hr_questions/) | 50 HR questions with model answers |
| [**HR+Technical Hybrid**](prep/behavioral/hr_questions/hr-technical-hybrid-questions.md) | 26 final-round questions |
| [Behavioral Guide](prep/behavioral/behavioral-interview-guide.md) | STAR method, conflict resolution, leadership |
| [Placement Data](resources/placement-data.md) | Company CTC, profiles (60+ companies) |

### 🖥️ Software Skills

| Resource | Coverage |
|:---------|:---------|
| [**Software Interview Guide**](prep/software-interview-guide.md) | 20+ tools: HEC-RAS, OpenFOAM, STAAD, GIS, Python |

---

## 🧮 Aptitude & Behavioral Prep

| Area | Topics | Resources |
|:-----|:-------|:----------|
| **Quantitative** | 14 topics: averages, percentages, profit/loss, time-work, probability, etc. | [`non-core/aptitude/quantitative/`](non-core/aptitude/quantitative/) |
| **Logical Reasoning** | Puzzles, seating arrangement, syllogisms, coding/decoding | [`non-core/aptitude/logical_reasoning/`](non-core/aptitude/logical_reasoning/) |
| **Speed Math** | 50+ shortcuts for placement aptitude rounds | [`non-core/aptitude/shortcuts/`](non-core/aptitude/shortcuts/) |
| **Verbal Ability** | Grammar, vocabulary, reading comprehension, idioms | [`non-core/aptitude/verbal/`](non-core/aptitude/verbal/) |
| **Behavioral** | STAR method, conflict resolution, leadership, teamwork | [`prep/behavioral/`](prep/behavioral/) |
| **Self Introduction** | Frameworks and 5 sample introductions | [`prep/behavioral/self_intro/`](prep/behavioral/self_intro/) |

### Non-Core / Analytics Prep

- **Tech Stack:** Python (NumPy/Pandas), SQL, Excel modeling, MATLAB → [`non-core/analytics/technical-stack.md`](non-core/analytics/technical-stack.md)
- **Non-Core Guide:** Data analytics, case studies, SQL practice → [`non-core/analytics/non-core-prep.md`](non-core/analytics/non-core-prep.md)

---

## 📋 GATE Preparation

| Resource | Content |
|:---------|:--------|
| [GATE Civil Notes](core/gate/civil/gate-civil-notes.md) | Topic-wise GATE Civil notes |
| [Formula Sheet](core/gate/formulas/gate-civil-formulas.md) | Complete formula reference |
| [Revision Cards](core/gate/revision_notes/gate-civil-revision.md) | Rapid revision flashcards |
| [Practice Problems](core/gate/practice/gate-civil-practice.md) | 50+ solved problems with solutions |

---

## 📅 Study Schedule & Progress

### Phase Overview

| Phase | Window | Core Focus | Priority & Status |
|:------|:-------|:-----------|:------------------|
| **Phase 0: Bootstrap** | Aug&nbsp;21&nbsp;–&nbsp;Sep&nbsp;07 | Resume, syllabus mapping, repo setup | 🔴&nbsp;P0 · ⚪ Queued |
| **Phase 1: Core Revision** | Sep&nbsp;08&nbsp;–&nbsp;Sep&nbsp;30 | Hydraulics, Hydrology, Structures, Geotech | 🔴&nbsp;P0 · ⚪ Queued |
| **Phase 2: Mock & Coding** | Oct&nbsp;01&nbsp;–&nbsp;Oct&nbsp;20 | Mock interviews, Python/SQL, STAR bank | 🔴&nbsp;P0 · ⚪ Queued |
| **Phase 3: Company-Wise** | Oct&nbsp;21&nbsp;–&nbsp;Nov&nbsp;10 | PSU, Core, Analytics company prep | 🟡&nbsp;P1 · ⚪ Queued |
| **Phase 4: Final Revision** | Nov&nbsp;11&nbsp;–&nbsp;Dec&nbsp;01 | Flashcards, cheat-sheets, final mocks | 🔴&nbsp;P0 · ⚪ Queued |
| **Phase 5: Live Interviews** | Dec&nbsp;2026 | Execute, log, postmortem, iterate | 🔴&nbsp;P0 · ⚪ Queued |

> Full daily planner & progress tracker in [`docs/roadmap.md`](docs/roadmap.md)

### Weekly Tracker

<details>
<summary><b>📊 13-Week Progress Tracker</b> — click to expand</summary>

| Week | Dates | Study & Practice | Interviews | Coding | Status |
|:----:|:------|:-----------------|:-----------|:-------|:------:|
| **W01** | Sep&nbsp;08&nbsp;–&nbsp;14 | `0 / 50 hrs · 0 / 50 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 3 tasks` | ⚪ |
| **W02** | Sep&nbsp;15&nbsp;–&nbsp;21 | `0 / 50 hrs · 0 / 50 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 3 tasks` | ⚪ |
| **W03** | Sep&nbsp;22&nbsp;–&nbsp;28 | `0 / 50 hrs · 0 / 50 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 3 tasks` | ⚪ |
| **W04** | Sep&nbsp;29&nbsp;–&nbsp;30 | `0 / 10 hrs · 0 / 20 num` | `0 / 1 mocks · 0 / 2 STAR` | `0 / 1 tasks` | ⚪ |
| **W05** | Oct&nbsp;01&nbsp;–&nbsp;07 | `0 / 50 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 3 tasks` | ⚪ |
| **W06** | Oct&nbsp;08&nbsp;–&nbsp;14 | `0 / 50 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 3 tasks` | ⚪ |
| **W07** | Oct&nbsp;15&nbsp;–&nbsp;20 | `0 / 40 hrs · 0 / 20 num` | `0 / 2 mocks · 0 / 3 STAR` | `0 / 2 tasks` | ⚪ |
| **W08** | Oct&nbsp;21&nbsp;–&nbsp;27 | `0 / 50 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 2 tasks` | ⚪ |
| **W09** | Oct&nbsp;28&nbsp;–&nbsp;Nov&nbsp;03 | `0 / 50 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 5 STAR` | `0 / 2 tasks` | ⚪ |
| **W10** | Nov&nbsp;04&nbsp;–&nbsp;10 | `0 / 50 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 3 STAR` | `0 / 2 tasks` | ⚪ |
| **W11** | Nov&nbsp;11&nbsp;–&nbsp;17 | `0 / 50 hrs · 0 / 40 num` | `0 / 3 mocks · 0 / 5 STAR` | `0 / 2 tasks` | ⚪ |
| **W12** | Nov&nbsp;18&nbsp;–&nbsp;24 | `0 / 50 hrs · 0 / 40 num` | `0 / 3 mocks · 0 / 5 STAR` | `0 / 2 tasks` | ⚪ |
| **W13** | Nov&nbsp;25&nbsp;–&nbsp;Dec&nbsp;01 | `0 / 40 hrs · 0 / 30 num` | `0 / 2 mocks · 0 / 3 STAR` | `0 / 1 tasks` | ⚪ |

**Status legend:** ⚪ Queued · ⏳ Active · ✅ Completed

</details>

---

## 🔧 Getting Started

```bash
# Clone the repository
git clone https://github.com/DKS-MANAGER/DKS_IITK_Civil_HWRE_Placement_2026.git
cd DKS_IITK_Civil_HWRE_Placement_2026

# Validate index integrity
python scripts/validate_index.py
```

### Navigation Aids

| Index | Description |
|:------|:------------|
| [`index/master_index.md`](index/master_index.md) | Complete topic index (50 topics, 100 files) |
| [`index/topic_map.md`](index/topic_map.md) | Topic → source → destination mapping |
| [`index/file_inventory.csv`](index/file_inventory.csv) | CSV inventory of all files |

See [`docs/setup.md`](docs/setup.md) for detailed setup instructions.

---

## 📚 Sources & References

This repository synthesizes content from the following public repositories:

| Repository | Focus |
|:-----------|:------|
| [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK) | Core civil/HWRE syllabus, roadmap, technical interview bank |
| [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering) | Software tools, GIS, structural/geotechnical packages |
| [Aptitude](https://github.com/DKS-MANAGER/Aptitude) | Quantitative aptitude, logical reasoning, verbal ability |
| [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) | Placement-focused quant practice problems |
| [awesome-behavioral-interviews](https://github.com/awesome-behavioral-interviews/awesome-behavioral-interviews) | STAR method, self-intro, teamwork, leadership |
| [awesome-interview-questions](https://github.com/awesome-interview-questions/awesome-interview-questions) | HR interview guide, mock questions |
| [behavioral-interview-list-of-questions](https://github.com/DKS-MANAGER/behavioral-interview-list-of-questions) | Behavioral question bank, interview process tips |
| [campus-placement-prep](https://github.com/DKS-MANAGER/campus-placement-prep) | Placement roadmap, resume tips, interview practice |
| [Placement_Preparation](https://github.com/DKS-MANAGER/Placement_Preparation) | Company-wise interview experiences and transcripts |
| [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027) | GATE Civil notes, formulas, PYQs, revision summaries |
| [interview-handbook-2026](https://github.com/DKS-MANAGER/interview-handbook-2026) | Behavioral, technical, curveball questions |

> Content has been paraphrased and synthesized from public repositories. See individual `## References` sections within each guide for source attribution.

---

## 🤝 Contributing

Contributions are welcome for new content, corrections, or formatting improvements.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-content`)
3. Commit changes (`git commit -m "Add: new topic guide"`)
4. Push to branch (`git push origin feature/new-content`)
5. Open a Pull Request

> **Validation required:** Run `python scripts/validate_index.py` before committing to ensure all index references remain intact.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the MIT License — see [`LICENSE`](LICENSE) for details.

---

<div align="center">

**Maintained by DKS** · IIT Kanpur M.Tech Civil / HWRE · Placement 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

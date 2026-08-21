# DKS_IITK_Civil_HWRE_Placement_2026

> M.Tech Civil & HWRE, IIT Kanpur | Target: **Dec 2026 Placements**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Batch](https://img.shields.io/badge/IIT_Kanpur-HWRE_2026-blue.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Table of Contents

- [Repository Purpose](#repository-purpose)
- [Directory Structure](#directory-structure)
- [Quick Start](#quick-start)
- [How to Use](#how-to-use)
  - [Index](#index)
  - [Navigation](#navigation)
- [Roadmap](#roadmap)
- [Execution Targets](#execution-targets)
- [Milestone Rubric](#milestone-rubric)
- [Contribution Guidelines](#contribution-guidelines)
- [Maintainers](#maintainers)

---

## Repository Purpose

Curated placement-prep knowledge base for IITK Civil/HWRE DEEC 2026. Synthesizes 10 repositories and 1 gist into structured, cross-referenced notes with full source attribution.

---

## Directory Structure

<details>
<summary><b>Explore Full Directory Layout</b></summary>

```
DKS_IITK_Civil_HWRE_Placement_2026/
├── README.md                 # Overview, roadmap, usage
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Build phases and change history
├── placement-roadmap.md      # Phase-wise timeline (Aug–Dec 2026)
├── index/
│   ├── master_index.md       # Topic-wise index: sources → destinations
│   ├── source_map.csv        # Source-to-destination mapping
│   ├── topic_map.md          # Topic-to-source-to-destination mappings
│   └── file_inventory.csv    # Per-file metadata
├── civil/
│   ├── fundamentals/         # Civil engineering foundations
│   ├── hydraulics/           # Fluid mechanics, pipe friction, turbulence
│   ├── open_channel_flow/    # GVF, RVF, hydraulic jump, unsteady flow
│   ├── hydrology/            # Unit hydrograph, flood routing, sediment transport
│   ├── water_resources/      # Reservoir/canal design, stage-discharge
│   ├── geotechnical/         # Soil mechanics, bearing capacity, slope stability
│   ├── structures/           # SOM, RCC, steel basics, IS codes
│   └── transportation/       # Traffic analysis, highway design, GIS
├── hwre/
│   ├── irrigation/           # Canal design, irrigation methods
│   ├── water_supply/         # Groundwater, distribution, treatment
│   ├── wastewater/           # Collection systems, treatment, sewer modeling
│   ├── flood_control/        # Flood modeling, floodplain management
│   └── exam_notes/           # Placement roadmap, company question patterns
├── aptitude/
│   ├── quantitative/         # 14 quant topics, data interpretation
│   ├── shortcuts/            # Speed math, percentage tricks
│   ├── logical_reasoning/    # Puzzles, seating, arrangements, syllogisms
│   └── verbal/               # Grammar, vocabulary, RC, idioms
├── behavioral/
│   ├── conflict_resolution/  # Behavioral frameworks
│   ├── leadership/           # Leadership scenarios
│   ├── teamwork/             # Teamwork examples
│   ├── hr_questions/         # Curated HR questions
│   ├── self_intro/           # Self introduction frameworks
│   └── behavioral-interview-guide.md  # STAR method
├── interviews/
│   ├── technical/            # Technical interview bank, project discussion
│   ├── company_specific/     # 10 company profiles + experiences
│   ├── hr/                   # HR interview guide, negotiation
│   └── mock_questions/       # Mock questions for practice
├── gate/
│   ├── civil/                # 13-subject chapter notes
│   ├── formulas/             # Key GATE Civil formulas
│   ├── practice/             # 50 practice problems with solutions
│   └── revision_notes/       # Topic-wise revision summaries
├── templates/
│   ├── resume-template.md
│   ├── self-intro-template.md
│   ├── interview-answer-template.md
│   └── study-plan-template.md
├── resources/
│   ├── book-list.md          # Recommended books by subject
│   ├── paper-list.md         # GATE PYQs (2021–2025)
│   ├── links.md              # Curated external links
│   ├── technical-stack.md    # Python, MATLAB, LaTeX, OpenFOAM, Git
│   ├── non-core-prep.md      # Analytics, SQL, Python, Excel
│   ├── placement-data.md     # Company CTC, profiles, skills
│   └── gis-tools.md          # GIS, surveying, reality capture
├── cfd-cases/              # OpenFOAM case files and post-processing scripts
└── .github/
    ├── workflows/            # CI: lint, syntax checks, content audit
    ├── ISSUE_TEMPLATE/       # Material request templates
    └── PULL_REQUEST_TEMPLATE/ # Contribution template
```

</details>

---

## Quick Start

```bash
git clone https://github.com/DKS-MANAGER/DKS_IITK_Civil_HWRE_Placement_2026.git
cd DKS_IITK_Civil_HWRE_Placement_2026
```

---

## How to Use

### Index

Start with [index/master_index.md](index/master_index.md) for the complete topic map, source inventory, and priority ratings.

### Navigation

| Path | Content |
|---|---|
| [civil/](civil/) | Fundamentals, hydraulics, hydrology, geotechnical, structures, transportation |
| [hwre/](hwre/) | Irrigation, water supply, wastewater, flood control, exam notes |
| [aptitude/](aptitude/) | Quantitative, logical reasoning, verbal, shortcuts |
| [behavioral/](behavioral/) | Self intro, teamwork, leadership, conflict resolution, HR questions |
| [interviews/](interviews/) | Technical bank, company-specific (10 companies), HR guide, mock questions |
| [gate/](gate/) | Chapter notes, formulas, practice (50 Qs), revision notes |
| [templates/](templates/) | Resume, self intro, interview answer, study plan |
| [resources/](resources/) | Books, papers, links, technical stack, placement data, GIS tools |

Each note includes a `## Sources` section tracing content to original repositories.

---

## Roadmap (Aug 2026 → Dec 2026)

See the detailed phased roadmap in [`placement-roadmap.md`](placement-roadmap.md).

---

## Execution Targets

- **Core:** Derivations, assumptions, scaling laws, design checks, model limitations.
- **HWRE:** CFD fundamentals, OpenFOAM logic, RANS/LES selection, open-channel flow, hydrology, sediment transport, scour.
- **PSUs:** GATE-adjacent recall, IS code familiarity, site awareness, HR/GK.
- **Analytics:** Python, SQL, probability, statistics, data structures, optimization.

---

## Milestone Rubric

| Metric | Threshold | Evidence |
|---|---|---|
| Core concept recall | ≥90% active recall | Closed-book oral tests |
| Numerical speed | 15–20 min/problem | Timed worksheets |
| Coding fluency | 3–5 scripts/week | Git commits + notebooks |
| Mock readiness | 8+ mocks/company track | PR-linked transcripts |
| Interview depth | 2-layer answers minimum | Concept + application + caveat |

---

## Contribution Guidelines

1. **Fork → Branch → PR.** Use `add/<topic>` or `fix/<file>`; keep PRs single-purpose.
2. **Interview experiences:** Use [templates/interview-answer-template.md](templates/interview-answer-template.md); anonymize all identifiers; log facts + postmortem.
3. **Resources:** Update existing tables; validate with 2+ peers before marking ✅.
4. **No duplicates:** Search existing content before adding; prefer merged canonical notes.
5. **Weekly sync:** PRs reviewed Sundays; clear titles, descriptions, and `Fixes #issue` linkage.
6. **Issues:** Use for material requests; label `good-first-issue` for quick wins.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Maintainers

**M.Tech Civil/HWRE Cohort, IIT Kanpur**

- [Divyansh Kumar Singh](https://github.com/DKS-MANAGER)
- [Cohort GitHub](https://github.com/DKS-MANAGER)

**Last updated:** Aug 2026

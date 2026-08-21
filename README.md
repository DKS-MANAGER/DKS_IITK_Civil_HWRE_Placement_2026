# DKS_IITK_Civil_HWRE_Placement_2026

> Collaborative prep repo for M.Tech Civil & HWRE, IIT Kanpur | Target: **Dec 2026 Placements**

![Status](https://img.shields.io/badge/status-active-brightgreen) ![Contributors](https://img.shields.io/badge/contributors-cohort-blue) ![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Repository Purpose

Centralize core/non-core prep material, company-specific intel, and past interview transcripts for the M.Tech Civil/HWRE batch to avoid redundant effort and standardize prep quality. Content is extracted, paraphrased, and synthesized from 10 downloaded repositories and 1 gist.

---

## Directory Structure

```
DKS_IITK_Civil_HWRE_Placement_2026/
├── README.md                 # Repository overview, roadmap, and usage guide
├── LICENSE                   # MIT License
├── CHANGELOG.md              # Build phases and change history
├── index/
│   └── master_index.md       # Topic-wise index mapping sources to destinations
├── civil/
│   ├── fundamentals/         # Civil engineering foundations
│   ├── hydraulics/           # Fluid mechanics, pipe friction, turbulence modeling
│   ├── open_channel_flow/    # GVF, RVF, hydraulic jump, unsteady flow
│   ├── hydrology/            # Unit hydrograph, flood routing, sediment transport
│   ├── water_resources/      # Reservoir/canal design, stage-discharge relations
│   ├── geotechnical/         # Soil mechanics, bearing capacity, slope stability
│   └── structures/           # SOM, RCC, steel basics, IS codes
├── hwre/
│   ├── irrigation/           # Canal design, irrigation methods
│   ├── water_supply/         # Groundwater, water distribution, treatment
│   ├── wastewater/           # Collection systems, treatment, sewer modeling
│   └── flood_control/        # Flood modeling, floodplain management, drainage
├── aptitude/
│   ├── quantitative/         # Quant aptitude fundamentals, data interpretation
│   ├── shortcuts/            # Speed math, percentage tricks, time-saving methods
│   ├── logical_reasoning/    # Puzzles, seating, arrangements, syllogisms
│   └── verbal/               # Grammar, vocabulary, RC, idioms
├── behavioral/
│   ├── conflict_resolution/  # Behavioral questions and frameworks
│   ├── leadership/           # Leadership scenarios and tips
│   ├── teamwork/             # Teamwork examples and questions
│   ├── hr_questions/         # Curated HR interview questions
│   └── self_intro/           # Self introduction frameworks and examples
├── interviews/
│   ├── technical/            # Technical interview bank, project discussion
│   ├── company_specific/     # Company profiles, interview experiences
│   ├── hr/                   # HR interview guide, salary negotiation
│   └── mock_questions/       # Curated mock questions for practice
├── gate/
│   ├── formulas/             # Key formulas for GATE Civil
│   ├── revision_notes/       # Topic-wise revision notes
│   └── practice/             # Practice problems and question banks
├── templates/
│   ├── resume_template.md    # Resume building tips and templates
│   ├── self_intro_template.md
│   ├── interview_answer_template.md
│   └── study_plan_template.md
├── resources/
│   ├── book_list.md          # Recommended books
│   ├── paper_list.md         # Previous year GATE and placement papers
│   ├── links.md              # Curated external links
│   ├── technical-stack.md    # Python, MATLAB, LaTeX, OpenFOAM, Git
│   ├── non-core-prep.md      # Data analytics, SQL, Python, Excel, case studies
│   └── placement-data.md     # Company-wise CTC, profile, skills
└── cfd-cases/                # OpenFOAM / SedFoam cases (if applicable)
```

---

## How to Use This Repository

1. **Clone the repo** and review the `index/master_index.md` for a complete topic map.
2. **Follow the roadmap** below to structure your preparation timeline.
3. **Navigate by topic:** Each folder contains synthesized content sourced from multiple repositories.
4. **Contribute:** Interview experiences, corrections, and additions are welcome (see Contribution Guidelines).

---

## Roadmap (Aug 2026 → Dec 2026)

| Phase | Timeline | Focus | Deliverable | Priority |
|---|---|---|---|---|
| Phase 0 | Aug 21–Sep 7 | Repo bootstrap, syllabus map, resume/CV audit, peer onboarding | `/templates` templates, folder taxonomy, issue labels | P0 |
| Phase 1 | Sep 8–Sep 30 | Core revision: fluid mechanics, turbulence, hydraulics, hydrology, SOM, geotech | Topic notes in `/civil`, formula sheets, derivation logs | P0 |
| Phase 2 | Oct 1–Oct 20 | Mock interviews, viva-style grilling, design-code numericals, coding drills | `/interviews/mock_questions`, answer bank, error log | P0 |
| Phase 3 | Oct 21–Nov 10 | Company-wise prep: PSUs, core design/consulting, analytics, shortlists | PRs in `/interviews/company_specific`, role matrices | P1 |
| Phase 4 | Nov 11–Dec 1 | Final revision: rapid recall, GD/HR, aptitude, case-study reps | Consolidated cheat-sheets, flashcards, mock scores | P0 |
| Phase 5 | Dec 2026 | Live interview logging, offer tracking, postmortems, referral notes | `/interviews/company_specific` updated in real time | P0 |

---

## Execution Targets

- **Core:** Fluency in derivations, assumptions, scaling laws, code-level design checks, model limitations.
- **HWRE:** CFD fundamentals, OpenFOAM case logic, RANS/LES selection, open-channel flow, hydrology, sediment transport, scour.
- **PSUs:** GATE-adjacent technical recall, IS code familiarity, project/site awareness, HR/GK.
- **Analytics:** Python, SQL, probability, statistics, data structures, optimization, business framing.

---

## Milestone Rubric

| Metric | Threshold | Evidence |
|---|---|---|
| Core concept recall | 90%+ active recall | Closed-book oral tests |
| Numerical speed | 15–20 min/problem | Timed worksheets |
| Coding fluency | 3–5 scripts/week | Git commits + notebooks |
| Mock readiness | 8+ mocks/company track | PR-linked transcripts |
| Interview depth | 2-layer answers minimum | Concept + application + caveat |

---

## Contribution Guidelines

1. **Fork → Branch → PR.** Branch naming: `add/<topic>` or `fix/<file>`; keep PRs small, single-purpose, and reviewer-friendly.
2. **Interview experiences:** Use `/templates/interview_template.md`; anonymize names, roles, panel details, and any confidential prompts; log concise facts + postmortem.
3. **Resource additions:** Update the relevant table row, set `Status` to ✅ only after validation by 2+ peers, and link the source/owner in the PR body.
4. **No duplicate resources:** Search existing tables/issues before adding; prefer one canonical entry per topic with merged notes over repeated links.
5. **Weekly sync:** PRs reviewed every Sunday by rotating cohort maintainer; keep a clear title, short description, and `Fixes #issue` linkage where applicable.
6. **Use Issues** for material requests/gaps; label quick wins `good-first-issue`, and convert repeated asks into tracked tasks instead of chat-only requests.

---

**Maintainers:** M.Tech Civil/HWRE Cohort, IIT Kanpur | **Last updated:** Aug 2026

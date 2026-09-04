# Information Architecture

> **Canonical reference for folder structure, naming, navigation, and content organization.**

---

## Design Principles

1. **Navigation before expansion** — Students find what they need in ≤3 clicks
2. **Canonical content once** — Explain a concept once; link everywhere else
3. **Three orthogonal dimensions** — Domain × Career Target × Preparation Stage
4. **User journey over folder aesthetics** — A pretty hierarchy that slows students is a failure
5. **Placement pressure optimization** — Usable at 90 days, 30 days, 7 days, 1 day, 10 minutes

---

## Directory Structure

```
DKS_IITK_Civil_HWRE_Placement_2026/
├── core/                    # Technical subject content
│   ├── hwre/               # HWRE specialization (flagship)
│   ├── structures/
│   ├── geotechnical/
│   ├── environmental/
│   ├── transportation/
│   ├── geoinformatics/
│   ├── infrastructure/
│   ├── fundamentals/
│   └── gate/
├── non-core/                # Non-technical career tracks
│   ├── consulting/
│   ├── data-analyst/
│   ├── business-analyst/
│   ├── product-management/
│   ├── operations/
│   ├── finance/
│   ├── risk/
│   ├── strategy/
│   ├── supply-chain/
│   ├── aptitude/
│   ├── guesstimates/
│   ├── case-interviews/
│   ├── resume-positioning/
│   └── common/             # Shared across non-core tracks
├── prep/                    # Interview preparation
│   ├── behavioral/
│   ├── technical/
│   ├── mock-tests/
│   ├── company-profiles/
│   ├── hr/
│   └── templates/
├── software-and-tech/       # Software & technology
│   ├── programming/
│   ├── deep-dives/
│   └── [role-specific]/
├── resources/               # External references
├── index/                   # Navigation indexes
├── scripts/                 # Automation
├── docs/                    # Governance, onboarding, architecture
└── .github/                 # CI, templates
```

---

## Naming Conventions

### Folders

| Rule | Example | Anti-Example |
|:-----|:--------|:-------------|
| lowercase, hyphenated | `open-channel-flow/` | `OpenChannelFlow/` |
| descriptive, not abbreviated | `water_resources/` | `wr/` |
| plural for collections | `company-profiles/` | `company-profile/` |
| singular for topics | `geotechnical/` | `geotechnicals/` |

### Files

| Rule | Example | Anti-Example |
|:-----|:--------|:-------------|
| lowercase, hyphenated | `hydraulics.md` | `Hydraulics.md` |
| descriptive filename | `open-channel-flow.md` | `ocf.md` |
| README for folder entry | `README.md` in each major folder | — |
| consistent suffixes | `overview.md`, `guide.md`, `practice.md` | random naming |

### Headings

| Level | Usage |
|:------|:------|
| `# H1` | Page title (one per file) |
| `## H2` | Major sections |
| `### H3` | Subsections |
| `#### H4` | Specific items (formulas, examples) |
| `##### H5` | Rarely used; avoid |

---

## Navigation Dimensions

### Dimension A — Domain

| Domain | Location |
|:-------|:---------|
| Core Civil | `core/` |
| Non-Core | `non-core/` |
| Behavioral | `prep/behavioral/` |
| Aptitude | `non-core/aptitude/` |
| Software | `software-and-tech/` |
| Interview | `prep/` |
| Resources | `resources/` |

### Dimension B — Career Target

Each career target has a recommended path through the repository:

```
Career Target → Core Subjects → Software → Interview → Resume → Mock
```

### Dimension C — Preparation Stage

| Stage | Description |
|:------|:------------|
| Learn | Study concepts, formulas, theory |
| Practice | Solve numericals, cases, questions |
| Interview | Mock interviews, defense prep |
| Revise | Quick revision, cheat sheets |

---

## Cross-Linking Rules

1. Every content page should link **up** to its section README
2. Every content page should link **sideways** to related topics
3. Question banks should link **back** to canonical concept pages
4. Revision pages should link **forward** to full-depth content
5. Software pages should link **back** to the branch/role they serve

### Link Format

```markdown
[Display Text](relative/path/to/file.md)
```

Always use relative paths. Never use absolute URLs for internal links.

---

## Content Type Identification

Every file should be identifiable as one of these types:

| Type | Purpose | Template |
|:-----|:--------|:---------|
| **Concept** | Theory + equations + application | [concept.md](templates/concept.md) |
| **Numerical** | Problem + solution + interpretation | [numerical.md](templates/numerical.md) |
| **Interview** | Question + answer + follow-up | [interview.md](templates/interview.md) |
| **Software** | Purpose + workflow + project + interview | [software.md](templates/software.md) |
| **Career** | Role + skills + roadmap + interview | [career.md](templates/career.md) |
| **Project** | Problem + methodology + defense Qs | [project.md](templates/project.md) |
| **Revision** | High-density last-minute summary | [revision.md](templates/revision.md) |
| **Resource** | External references with assessment | [resource.md](templates/resource.md) |

---

## Priority System

| Priority | Meaning | Depth Expected |
|:---------|:--------|:---------------|
| **P0** | Critical for placement | Full: concept → formula → numerical → interview → software → project |
| **P1** | Important for breadth | Moderate: concept → formula → interview |
| **P2** | Useful for specific roles | Basic: concept → interview |
| **P3** | Nice to have | Minimal: concept summary |

---

## Difficulty Levels

| Level | Audience |
|:------|:---------|
| **Beginner** | First-year, no prior exposure |
| **Intermediate** | Course-level understanding |
| **Advanced** | M.Tech / research depth |
| **Interview** | Placement-ready, includes follow-ups |

---

## Metadata Convention

Major content pages may optionally include metadata at the top:

```yaml
---
Category: core | non-core | prep | software | resource
Branch: hwre | structural | geotechnical | environmental | transportation | ...
Role: hydraulic-engineer | structural-engineer | consultant | data-analyst | ...
Level: beginner | intermediate | advanced | interview
Priority: P0 | P1 | P2 | P3
Type: concept | numerical | interview | software | project | career | revision
Prerequisites: [list of prerequisite topics]
---
```

This enables future automation, filtering, and search.

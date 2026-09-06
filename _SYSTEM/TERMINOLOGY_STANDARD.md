# TERMINOLOGY STANDARD

> Canonical terminology for the DKS_IITK_Civil_HWRE_Placement_2026 repository.
> All folders, files, headings, navigation labels, and cross-references must use these terms consistently.

---

## Track Names (Canonical)

| Canonical | Aliases to Avoid |
|-----------|------------------|
| **Core Civil** | Core, Civil Core, Civil Engineering Core |
| **GATE** | Gate, gate |
| **HWRE** | Hwre, hwre, Water Resources, Water Resources Engineering |
| **CFD** | Cfd, cfd, Computational Fluid Dynamics |
| **Non-Core** | NonCore, noncore, Non-Core Tracks, Non-Core Roles |
| **Common Placement** | Placement Common, Common Prep, Placement Execution |

> **Rule:** Use exactly these 6 track names everywhere. No synonyms.

---

## Subject Names (Canonical)

| Canonical | Aliases to Avoid |
|-----------|------------------|
| **Fluid Mechanics** | Fluid Mech, FM, Fluid Mechanics & Flow |
| **Open Channel Flow** | OCF, Open-Channel Flow, Open Channel |
| **Hydraulics** | Hydraulic Engineering |
| **Hydrology** | Hydrologic Engineering |
| **Water Resources Engineering** | WRE, Water Resources |
| **Sediment Transport** | Sediment, Sediment Engineering |
| **Structural Analysis** | Structural Analysis, SA |
| **Structural Design** | RCC Design, Steel Design |
| **RCC Design** | RCC, Reinforced Concrete Design |
| **Steel Design** | Steel, Structural Steel Design |
| **Geotechnical Engineering** | Geotech, Soil Mechanics, Geotechnical |
| **Transportation Engineering** | Transportation, Traffic Engineering |
| **Environmental Engineering** | Environmental, Env Eng |
| **Construction Engineering** | Construction, Construction Management |
| **Infrastructure Engineering** | Infrastructure, Infra |
| **Geoinformatics** | GIS, Geomatics |
| **Engineering Mechanics** | Mechanics, EM |
| **Strength of Materials** | SOM, Mechanics of Materials |

> **Rule:** Use full canonical subject names in folder names, file names, H1 titles, and navigation. Abbreviations only in tables/charts where space is constrained.

---

## Role Names (Canonical)

| Canonical | Aliases to Avoid |
|-----------|------------------|
| **Civil Engineer** | Civil Engg, Civil |
| **Structural Engineer** | Structural Engg, Structural Design Engineer |
| **Geotechnical Engineer** | Geotech Engineer, Geotechnical |
| **Transportation Engineer** | Transport Engineer, Traffic Engineer |
| **Construction Engineer** | Construction Engg, Site Engineer |
| **Project Engineer** | Project Engg |
| **Water Resources Engineer** | WRE, Water Resources |
| **Hydrologist** | Hydrology Engineer |
| **Hydraulic Engineer** | Hydraulics Engineer |
| **CFD Engineer** | Computational Fluid Dynamics Engineer |
| **BIM Engineer** | Building Information Modeling Engineer |
| **GIS Engineer** | Geoinformatics Engineer, GIS Specialist |
| **Product Manager** | PM, Product Mgmt |
| **Business Analyst** | BA, Business Analysis |
| **Data Analyst** | DA, Data Analytics |
| **Consultant** | Consulting |
| **Software Engineer** | SWE, Developer |
| **Project Manager** | Program Manager, PgM |

> **Rule:** Use exactly these role names in role pages, company mappings, roadmaps, and navigation.

---

## Preparation Component Names (Canonical)

| Canonical | Aliases to Avoid |
|-----------|------------------|
| **Study Material** | Study Notes, Notes, Theory, Learning Material |
| **Practice** | Practice Problems, Exercises, Drills |
| **Mock Test** | Mock, Test, Practice Test, Mock Exam |
| **Interview Preparation** | Interview Prep, Interview |
| **Behavioural & HR** | HR & Behavioural, Behavioural/HR, HR Preparation, Behavioral |
| **Technical Interview** | Technical, Tech Interview |
| **Aptitude** | Quantitative Aptitude, Quant |
| **Rapid Revision** | Quick Revision, Rapid Review, Revision Cards, Cheat Sheet |
| **Formula Sheet** | Formulas, Formulae, Equations, Quick Reference |
| **Company Preparation** | Company Prep, Company Strategy |
| **Role Preparation** | Role Prep, Role Strategy |
| **Project Defence** | Project Defense, Project Discussion |
| **Resume** | CV, Resume/CV |
| **Selection Stages** | Selection Process, Hiring Process |
| **Case Interview** | Case, Case Study |
| **Group Discussion** | GD, Group Discussion |

> **Rule:** Use canonical names in folder names, file names, H2 headings, and navigation tables.

---

## Folder Naming Convention

| Level | Convention | Examples |
|-------|------------|----------|
| **Top-level** | lowercase, hyphenated | `core/`, `prep/`, `software-and-tech/`, `aptitude/` |
| **Subject folders** | lowercase, hyphenated | `fluid-mechanics/`, `open-channel-flow/`, `structural-analysis/` |
| **Track folders** | lowercase | `gate/`, `hwre/`, `cfd/` |
| **Role folders** | lowercase, hyphenated | `structural-engineer/`, `water-resources-engineer/` |
| **Company folders** | lowercase, hyphenated | `larsen-and-toubro/`, `godrej-properties/` |
| **Component folders** | lowercase, hyphenated | `study-material/`, `practice/`, `mock-tests/`, `interview-prep/` |

> **Rule:** All folder names lowercase, hyphenated. No underscores, no CamelCase, no spaces.

---

## File Naming Convention

| Type | Convention | Examples |
|------|------------|----------|
| **Subject study** | `{subject}.md` | `fluid-mechanics.md`, `open-channel-flow.md` |
| **Subject rapid revision** | `{subject}-rapid-revision.md` | `hydraulics-rapid-revision.md` |
| **Subject practice** | `{subject}-practice.md` | `geotechnical-practice.md` |
| **Subject interview** | `{subject}-interview.md` | `structural-interview.md` |
| **Role page** | `{role}.md` | `structural-engineer.md`, `water-resources-engineer.md` |
| **Role study plan** | `{role}-study-plan.md` | `structural-engineer-study-plan.md` |
| **Role rapid revision** | `{role}-rapid-revision.md` | `hydrologist-rapid-revision.md` |
| **Company profile** | `{company}.md` | `larsen-and-toubro.md`, `godrej-properties.md` |
| **Company index** | `company-index.md` or `companies.md` | `company-profiles.md` |
| **Formula sheet** | `{subject}-formulas.md` | `gate-civil-formulas.md`, `hwre-formulas.md` |
| **Mock test** | `mock-test-{role}.md` | `mock-test-structural.md` |
| **Roadmap** | `{track}-roadmap.md` | `gate-roadmap.md`, `hwre-roadmap.md` |
| **Index/Navigation** | `{scope}-index.md` | `master-index.md`, `role-index.md` |
| **Template** | `{purpose}-template.md` | `resume-template.md`, `study-plan-template.md` |

> **Rule:** All file names lowercase, hyphenated, descriptive. No `notes.md`, `final.md`, `new.md`, `test.md`.

---

## Heading Hierarchy Standard

```
# H1: Page Title (exactly one per file)
## H2: Major Section
### H3: Subsection
#### H4: Detailed Topic
```

> **Rules:**
> - Exactly one H1 per substantive file
> - H1 must describe actual content (not "Notes", "Overview", "Introduction")
> - No skipped levels (H1 → H3 without H2)
> - Title Case for all headings
> - No manual numbering unless the entire repo uses numbered chapters

---

## Capitalization Rules

| Element | Style | Example |
|---------|-------|---------|
| **Folder names** | lowercase-hyphenated | `structural-analysis/` |
| **File names** | lowercase-hyphenated | `fluid-mechanics.md` |
| **H1 Titles** | Title Case | `# Fluid Mechanics` |
| **H2/H3 Headings** | Title Case | `## Core Concepts`, `### Worked Examples` |
| **Track names** | Title Case | `Core Civil`, `HWRE`, `CFD` |
| **Subject names** | Title Case | `Fluid Mechanics`, `Open Channel Flow` |
| **Role names** | Title Case | `Structural Engineer`, `Water Resources Engineer` |
| **Company names** | Proper Case | `Larsen & Toubro`, `Godrej Properties` |
| **Preparation components** | Title Case | `Study Material`, `Mock Test`, `Rapid Revision` |

---

## Index Naming Standard

| Purpose | Canonical Name |
|---------|----------------|
| Repository root | `README.md` |
| Track master index | `MASTER_INDEX.md` (e.g., `core/hwre/MASTER_INDEX.md`) |
| Role index | `ROLE_INDEX.md` |
| Subject index | `SUBJECT_INDEX.md` |
| Company index | `COMPANY_INDEX.md` or `company-profiles.md` |
| Interview index | `INTERVIEW_INDEX.md` |
| Resource index | `RESOURCE_INDEX.md` |
| Topic map | `topic-map.md` |

> **Rule:** No competing index files (`INDEX.md`, `index.md`, `MAIN_INDEX.md`, `START_HERE.md`, `NAVIGATION.md`) unless each has a clearly distinct function.

---

## Roadmap Naming Standard

| Purpose | Canonical Name |
|---------|----------------|
| Master roadmap | `MASTER_ROADMAP.md` |
| Track roadmap | `{track}-roadmap.md` (e.g., `gate-roadmap.md`, `hwre-roadmap.md`) |
| Role roadmap | `{role}-roadmap.md` |
| Placement roadmap | `placement-roadmap.md` |

---

## Navigation Label Standard

| Concept | Label |
|---------|-------|
| Main hub | `Prep Hub` or `Core Hub` or `Software Hub` |
| Back navigation | `Back to: [Parent]` |
| Quick start | `Quick Start` |
| Preparation chain | `Preparation Chain` |
| Related resources | `Related` or `Related Resources` |

---

## Abbreviation Policy

| Abbreviation | Allowed Context |
|--------------|-----------------|
| **GATE** | Always (standard acronym) |
| **HWRE** | Always (track name) |
| **CFD** | Always (track name) |
| **RCC** | In structural design context only |
| **BIM** | Always (standard acronym) |
| **GIS** | Always (standard acronym) |
| **PM/BA/DA** | In role tables only, not in headings/navigation |
| **SOM** | Never in headings/navigation (use Strength of Materials) |
| **FM** | Never in headings/navigation (use Fluid Mechanics) |
| **OCF** | Never in headings/navigation (use Open Channel Flow) |
| **WRE** | Never in headings/navigation (use Water Resources Engineering) |

> **Rule:** Spell out in headings, navigation, and prose. Abbreviate only in tables, charts, and metadata where space is constrained.

---

## Cross-Repository Consistency Checklist

- [ ] `README.md` uses canonical track names
- [ ] `docs/` uses canonical terminology
- [ ] `core/` uses canonical subject/role names
- [ ] `prep/` uses canonical preparation component names
- [ ] `software-and-tech/` uses canonical tool/role names
- [ ] `aptitude/` uses canonical aptitude topic names
- [ ] `non-core/` uses canonical role names
- [ ] All `_SYSTEM/` audit files reference canonical names

---

## Enforcement

1. **Before creating any file/folder:** Check this standard
2. **Before renaming:** Update this standard if new canonical term needed
3. **During audit:** Flag every deviation
4. **During rename:** Update all references
5. **After rename:** Verify 0 broken links

---

> **Back to:** [Repository Naming Audit](REPOSITORY_NAMING_AUDIT.md)
# Repository Index & System Registry

> **The Central Indexing & Discovery Hub for IIT Kanpur Placement Preparation**  
> Consolidates 592 Markdown files across 9 top-level subsystems into a structured, machine-validated registry.

---

## 1. Five-Level Index Hierarchy

To prevent indexing ambiguity and duplicate navigation paths, use this authoritative 5-level hierarchy:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ LEVEL 1: Global Repository Navigation                                       │
│ └── docs/MASTER_NAVIGATION.md  (Global routing across all subsystems, ≤3 clicks)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ LEVEL 2: Domain Master Index                                                │
│ └── index/master_index.md      (All 72 core topics, status, tests, and source)│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ LEVEL 3: Subject & Syllabus Index                                           │
│ └── index/topics.md            (694+ syllabus subtopics & 6D readiness)     │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ LEVEL 4: Software & Technology Index                                        │
│ └── software-and-tech/TOOLS_INDEX.md (17 tools, workflows, role matrices)   │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
┌──────────────────────────────────────▼──────────────────────────────────────┐
│ LEVEL 5: Preparation & Assessment Index                                     │
│ └── prep/READINESS_SCORECARD.md (8-level assessment ladder & scoring engine)│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Directory Contents & Role

| File | Content & Function | Last Synchronized |
|:---|:---|:---:|
| [`master_index.md`](master_index.md) | **Domain Master Index:** Authoritative domain-to-canonical-page matrix with 6-dimensional readiness indicators | 2026-09-17 |
| [`topics.md`](topics.md) | **Subject Catalog:** Detailed 18-subject breakdown mapping 694+ topics to canonical guides with 6D readiness | 2026-09-17 |
| [`topic_map.md`](topic_map.md) | **Provenance Mapping:** Decoupled registry mapping original source repos to active canonical files | 2026-09-17 |
| [`file_inventory.csv`](file_inventory.csv) | **Live File Inventory:** Machine-generated CSV cataloging all 651 files across 12 repository categories | Live (Script) |
| [`metrics.json`](metrics.json) | **Machine Metrics Dashboard:** Verified counts of files, tests, branching trees, cases, and tools | Live (Script) |
| [`SOURCE_MIGRATION_MAP.csv`](SOURCE_MIGRATION_MAP.csv) | **Historical Ledger:** Permanent historical record of initial 10-repository consolidation (Sep 3, 2026) | Historical |

---

## 3. Major Subsystems Indexed

Every major repository subsystem is accessible directly from this index:

### 🏛️ Core Civil Engineering & HWRE
- **Hub:** [`core/README.md`](../core/README.md)
- **HWRE Track:** [`core/hwre/README.md`](../core/hwre/README.md) (Hydraulics, OCF, Hydrology, Water Resources, Turbulence, Sediment)
- **Structural Track:** [`core/structural-analysis/structural-analysis.md`](../core/structural-analysis/structural-analysis.md), [`core/rcc/rcc-design.md`](../core/rcc/rcc-design.md), [`core/steel/steel-design.md`](../core/steel/steel-design.md)
- **Geotechnical Track:** [`core/geotechnical/geotechnical.md`](../core/geotechnical/geotechnical.md)
- **GATE Revision Hub:** [`core/gate/formulas/gate-civil-formulas.md`](../core/gate/formulas/gate-civil-formulas.md)

### 💻 Software & Computational Engineering
- **Hub:** [`software-and-tech/README.md`](../software-and-tech/README.md)
- **Tools Index:** [`software-and-tech/TOOLS_INDEX.md`](../software-and-tech/TOOLS_INDEX.md)
- **Role Software Matrix:** [`software-and-tech/SOFTWARE_ROLE_MATRIX.md`](../software-and-tech/SOFTWARE_ROLE_MATRIX.md)
- **Deep Dives:** OpenFOAM, HEC-RAS, EPANET, SWMM, GeoStudio, PLAXIS in [`software-and-tech/deep-dives/README.md`](../software-and-tech/deep-dives/README.md)
- **Practical Testing:** [`software-and-tech/tests/README.md`](../software-and-tech/tests/README.md)

### 🎯 Aptitude & 8-Level Assessment Battery
- **Hub:** [`aptitude/README.md`](../aptitude/README.md)
- **Layer 1 Topic Diagnostics (17 tests):** [`aptitude/tests/README.md`](../aptitude/tests/README.md)
- **Layer 2 Sectional Tests (5 tests):** [`aptitude/tests/section/README.md`](../aptitude/tests/section/README.md)
- **Layer 3 & 4 Full Mocks (7 mocks):** [`aptitude/mocks/README.md`](../aptitude/mocks/README.md)
- **Aptitude Formula Sheet:** [`aptitude/FORMULA_SHEET.md`](../aptitude/FORMULA_SHEET.md)
- **Role Aptitude Matrix:** [`aptitude/ROLE_MATRIX.md`](../aptitude/ROLE_MATRIX.md)

### 💼 Non-Core Career Tracks
- **Hub:** [`non-core/README.md`](../non-core/README.md)
- **Management Consulting:** [`non-core/01_roles/consulting/case-bank.md`](../non-core/01_roles/consulting/case-bank.md) & [`case-frameworks.md`](../non-core/01_roles/consulting/case-frameworks.md)
- **Guesstimates & Market Sizing:** [`non-core/02_interview-preparation/guesstimates/guesstimate-guide.md`](../non-core/02_interview-preparation/guesstimates/guesstimate-guide.md)
- **Data Analytics & SQL:** [`non-core/01_roles/analytics/technical-stack.md`](../non-core/01_roles/analytics/technical-stack.md)
- **Product Management:** [`non-core/01_roles/product-management/pm-overview.md`](../non-core/01_roles/product-management/pm-overview.md)
- **Finance & Supply Chain:** [`non-core/01_roles/finance/finance-overview.md`](../non-core/01_roles/finance/finance-overview.md), [`non-core/01_roles/supply-chain/supply-chain-overview.md`](../non-core/01_roles/supply-chain/supply-chain-overview.md)

### 🚀 Preparation, Interview & Readiness Hub
- **Hub:** [`prep/README.md`](../prep/README.md)
- **Readiness Scorecard:** [`prep/READINESS_SCORECARD.md`](../prep/READINESS_SCORECARD.md)
- **30-14-7 Day Plan:** [`prep/30_14_7_DAY_PLAN.md`](../prep/30_14_7_DAY_PLAN.md)
- **Technical Interview Bank (30 Trees):** [`prep/interview/technical/technical-interview-bank.md`](../prep/interview/technical/technical-interview-bank.md)
- **Defense Guides:** [`project-defense-guide.md`](../prep/interview/technical/project-defense-guide.md) & [`thesis-defense-guide.md`](../prep/interview/technical/thesis-defense-guide.md)
- **Behavioral & HR Bank:** [`prep/behavioral/hr_questions/hr-questions-bank.md`](../prep/behavioral/hr_questions/hr-questions-bank.md)
- **Role Mock Tests (25 tests):** [`prep/mock-tests/README.md`](../prep/mock-tests/README.md)
- **Company Profiles (33+):** [`prep/company-profiles/README.md`](../prep/company-profiles/README.md)

### 📜 Institutional Governance & Placement Data
- **Hub:** [`docs/README.md`](../docs/README.md)
- **Master Navigation:** [`docs/MASTER_NAVIGATION.md`](../docs/MASTER_NAVIGATION.md)
- **Testing Guide:** [`docs/TESTING_GUIDE.md`](../docs/TESTING_GUIDE.md)
- **Assessment Architecture:** [`docs/ASSESSMENT_ARCHITECTURE.md`](../docs/ASSESSMENT_ARCHITECTURE.md)
- **IITK Placement Map:** [`docs/IITK_PLACEMENT_MAP.md`](../docs/IITK_PLACEMENT_MAP.md)
- **Source Registry:** [`resources/source-registry.md`](../resources/source-registry.md)
- **Empirical Placement Records:** [`resources/placement-data.md`](../resources/placement-data.md)

---

## 4. Index Maintenance & Automation

This directory is validated and regenerated via automation:
```powershell
# Validate all links across master_index, topics, topic_map, and README
# Regenerates index/file_inventory.csv and synchronizes index/metrics.json
python scripts/validate_index.py
```

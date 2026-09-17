# Institutional Source Registry & Provenance Governance
**Purpose:** Central evidentiary catalog and provenance tracking layer for `DKS_IITK_Civil_HWRE_Placement_2026`.  
**Standard:** Rigorous source classification to ensure academic and corporate data integrity.

---

## 1. Evidentiary Provenance Classification Scheme

Every numerical claim, company policy, interview format, and preparation benchmark across the repository is classified under one of six canonical evidentiary labels:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 6 EVIDENTIARY STATUS LABELS                           │
├──────────────────────────┬─────────────────────────────────────────────────────────────┤
│ Label                    │ Evidentiary Standard & Criteria                             │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [VERIFIED]               │ Directly supported by authoritative, primary sources        │
│                          │ (official institute placement files, papers, textbooks).    │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [SOURCE-DERIVED]         │ Faithfully extracted or adapted from cited external         │
│                          │ repositories or engineering standards (BIS codes, handbooks)│
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [INFERRED]               │ Derived via verified mathematical calculations, statistical │
│                          │ models, or systematic cross-referencing of verified data.   │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [PREPARATION HEURISTIC]  │ Repository pedagogical design targets, pacing rules, and   │
│                          │ competency screening benchmarks (not hard external laws).   │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [SELF-REPORTED]          │ Anecdotal testimony from candidate interviews, alumni       │
│                          │ debriefs, or student peer reviews.                          │
├──────────────────────────┼─────────────────────────────────────────────────────────────┤
│ [PREDICTED]              │ Forward-looking estimates, hiring projections, or           │
│                          │ anticipated market compensation ranges.                     │
└──────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 2. Institutional Source Registry Catalog

| Reference Entity / Dataset | Category | Provenance Label | Source Path / Origin | Last Verified | Primary Dependent Modules |
|:---|:---|:---:|:---|:---:|:---|
| **IITK Placement Export 2025–26** | Placement Compensation | `[VERIFIED]` | `Civil_Placement_IITK/placement_data.csv` | 2026-09-16 | [placement-data.md](placement-data.md), [Company Profiles](../prep/company-profiles/) |
| **OpenFOAM CFD Case Directory** | Research & Technical | `[VERIFIED]` | `f:/DKS/DKS/3C_FD_RSM/01_Base_Hydrodynamics/` | 2026-09-16 | [PROJECT_DEFENCE.md](../prep/PROJECT_DEFENCE.md), [core/hydrodynamics/](../core/hydrodynamics/) |
| **Aptitude Master Key Concordance** | Assessment Engine | `[VERIFIED]` | 1,892 audited questions across 47 chapters | 2026-09-17 | [aptitude/](../aptitude/), [aptitude/mocks/](../aptitude/mocks/) |
| **P&L / Unit Economics Formulas** | Financial Fundamentals | `[INFERRED]` | Standard Corporate Finance & GAAP Accounting | 2026-09-17 | [business-fundamentals.md](../non-core/common/business-fundamentals.md) |
| **LTV:CAC Business Model Ratios**| Business Benchmarks | `[PREPARATION HEURISTIC]` | B2B/B2C VC Valuation Models | 2026-09-17 | [business-fundamentals.md](../non-core/common/business-fundamentals.md), [interview-readiness.md](../non-core/common/interview-readiness.md) |
| **Aptitude 45s/Q Pacing Targets** | Test Strategy | `[PREPARATION HEURISTIC]` | Pedagogical Target for Tier-1 Screening | 2026-09-16 | [aptitude/mocks/README.md](../aptitude/mocks/README.md), [READINESS_SCORECARD.md](../prep/READINESS_SCORECARD.md) |
| **Consulting Case Frameworks** | Strategy Preparation | `[INFERRED]` | MECE Profitability & 3C/4P Decompositions | 2026-09-16 | [non-core/consulting/](../non-core/consulting/), [non-core/case-interviews/](../non-core/case-interviews/) |
| **Alumni Interview Experiences** | Candidate Experiences | `[USER/SELF-REPORTED]` | Student placement debriefs 2023–2025 | 2026-09-15 | [interview-experiences.md](../prep/company-profiles/interview-experiences.md) |
| **PSU Pay Matrix & DA Scales** | Public Enterprise Data | `[VERIFIED]` | 7th CPC / DPE IDA notification tables | 2026-09-15 | [placement-data.md](placement-data.md), [prep/company-profiles/civil-bpcl.md](../prep/company-profiles/civil-bpcl.md) |
| **Standard IS Codes (IS 456, 800)** | Structural Engineering | `[VERIFIED]` | Bureau of Indian Standards (BIS) | 2026-09-15 | [core/structures/](../core/structures/), [core/hwre/](../core/hwre/) |

---

## 3. Maintenance & Periodic Verification Protocol
1. **Quarterly Audit:** All company compensation figures and placement portal links must be verified at the beginning of each semester (August and January).
2. **External Link Checking:** Links in `links.md` and `company-profiles/` must be checked against live servers using automated link-check scripts.
3. **Discrepancy Reporting:** Any discrepancy between student-reported numbers and portal CSV data must be resolved in favor of the raw placement data export (`placement_data.csv`).

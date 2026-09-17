# SOFTWARE_AUDIT_STATE.md

> **Live tracking and governance document for the `software-and-tech/` operating system.**
> Maintained by the repository maintainer. Updated after every meaningful change.

---

## Audit Summary

| Field | Value |
|:------|:------|
| **Audit Baseline** | 2026-09-06 (Initial architecture & rebuild) |
| **Last Synchronization Audit** | 2026-09-17 (Post-mock expansion, provenance alignment & coverage/readiness audit) |
| **Files Inventoried** | **71 files across 27 subdirectories** (verified against local filesystem) |
| **Active Subdirectories** | `_SYSTEM`, `automation`, `bim`, `cfd`, `comparisons`, `computing`, `construction`, `consulting`, `data`, `deep-dives`, `developer-tools`, `environmental`, `geotechnical`, `gis`, `hwre`, `hydrology`, `operations`, `practice`, `product`, `programming`, `research`, `sediment`, `structural`, `technology-careers`, `tests`, `tools`, `transportation` |
| **System Links Verified** | 825+ internal relative links (0 broken) |
| **Status** | **SYNCHRONIZED & COMPLETE** |

---

## Synchronization & Upgrades Log (2026-09-17)

Following the comprehensive audit of September 17, 2026, the following architectural and evidentiary enhancements were implemented:

- [x] **File Count Reconciliation**:
  - Reconciled the previous 48 / 58 / 71 count discrepancy.
  - Formally established the authoritative count of **71 files across 27 subdirectories** in both `README.md` and `_SYSTEM/` control documents.
- [x] **Coverage Score vs. Practical Readiness Decoupling** (`SOFTWARE_COMPLETENESS_MATRIX.md`):
  - Decoupled documentation completeness (10/10 module checklist) from candidate practical interview defensibility.
  - Established realistic **Practical Readiness Scores** (`[PREPARATION HEURISTIC]`) across all 24 tools.
  - Added a dedicated 6-dimensional **Practical Competency & Evidence Verification Matrix** for major tools (HEC-RAS, OpenFOAM, QGIS, Python, Excel, STAAD/ETABS).
- [x] **Standardized Provenance Taxonomy** (`SOFTWARE_COMPANY_LINKAGE.md` & `SOFTWARE_ROLE_MATRIX.md`):
  - Applied the canonical 6-tier evidentiary taxonomy to all company-tool associations:
    - `[VERIFIED]`: Explicit in company job postings, test briefs, or SPO records (L&T, Godrej, Thornton Tomasetti, Hilti, Vassarlabs, GIST).
    - `[SOURCE-DERIVED]`: Sourced from industrial role specs or engineering consultancy syllabi.
    - `[INFERRED]`: Reasoned from civil engineering workflows and design code standards.
    - `[PREPARATION HEURISTIC]`: Internal preparation priority tiers (P0, P1, P2, P3) and target proficiency benchmarks.
- [x] **Canonical Decision Engine Anchoring** (`SOFTWARE_ROLE_MATRIX.md` & `README.md`):
  - Designated `SOFTWARE_ROLE_MATRIX.md` as the single primary decision engine for answering *"What software should I learn?"*.
  - Clarified the operational roles of specialized supporting views (`branch-roadmaps.md`, `learning-roadmaps.md`, `anti-overload.md`, `SOFTWARE_RESUME_STRATEGY.md`).
- [x] **Illustrative Code Limit Framing** (`SOFTWARE_THEORY_LINKAGE.md`):
  - Explicitly framed ETABS drift checks (IS 1893 Cl 7.11.1) and HEC-RAS Manning's roughness parameters as illustrative engineering examples subject to project-specific codes, load combinations, and soil conditions.
- [x] **Cross-Repository Link Correction**:
  - Corrected legacy relative links pointing to `../non-core/aptitude/` to the consolidated root `../aptitude/`.

---

## Governance & Quality Gates

| Quality Gate | Standard | Status |
|:---|:---|:---:|
| **Canonical Source Integrity** | Every tool resolves to a single authoritative study page | ✅ Met |
| **Evidence Transparency** | Company tool requirements annotated with provenance tags | ✅ Met |
| **Theory Defense Integration** | Tool $\leftrightarrow$ engineering theory linked for all P0/P1 tools | ✅ Met |
| **Practice & Test System** | 3-tier exercises and 4-tier diagnostic tests available for primary tools | ✅ Met |
| **Zero Broken Links** | All internal links resolve via relative Markdown paths | ✅ Met (0 broken) |

---

> **Last Verified:** 2026-09-17  
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026  
> **Next Scheduled Audit:** 2026-10-01  
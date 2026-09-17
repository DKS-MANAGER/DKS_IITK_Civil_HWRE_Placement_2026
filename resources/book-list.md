# Recommended Textbooks & Reference Authority
**Scope:** Core Civil Engineering, Hydraulics & Water Resources (HWRE), Environmental & Quantitative Placement Prep  
**Organization:** Classified by Subject $\to$ Purpose Priority ($\text{P0} \to \text{P2}$) $\to$ Dependent Repository Modules $\to$ High-Yield Chapters

---

## 1. Reference Priority Tier Definitions

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              REFERENCE PRIORITY TAXONOMY                               │
├─────────────────────┬──────────────────────────────────────────────────────────────────┤
│ Priority Level      │ Definition & Direct Operational Use                              │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ P0 (Primary)        │ Essential core placement & interview reference. Master these     │
│                     │ formulas, derivations, and problem archetypes first.             │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ P1 (Supplementary)  │ Excellent for deeper conceptual clarity and solving challenging  │
│                     │ GATE / PSU / Tier-1 corporate interview questions.               │
├─────────────────────┼──────────────────────────────────────────────────────────────────┤
│ P2 (Advanced/Thesis)│ Research monographs and specialized advanced references for      │
│                     │ M.Tech thesis defense, OpenFOAM CFD, and complex modeling.       │
└─────────────────────┴──────────────────────────────────────────────────────────────────┘
```

---

## 2. Water Resources & Hydrodynamics (HWRE / CFD)

| Textbook Title | Author(s) | Publisher | Priority | Supported Repository Module | High-Yield Chapters & Concepts |
|:---|:---|:---|:---:|:---|:---|
| **Flow in Open Channels** | K. Subramanya | Tata McGraw-Hill | **P0** | [core/hwre/](../core/hwre/README.md) | Ch 2 (Specific Energy & Critical Flow), Ch 4 (Gradually Varied Flow $GVF$), Ch 5 (Hydraulic Jump & Energy Dissipation) |
| **Engineering Hydrology** | K. Subramanya | Tata McGraw-Hill | **P0** | [core/hwre/](../core/hwre/README.md) | Ch 3 (Infiltration Indices $\Phi, W$), Ch 4 (Unit Hydrograph & $S\text{-Curve}$), Ch 7 (Flood Routing & Muskingum) |
| **Fluid Mechanics & Hydraulic Machines** | Modi & Seth | Standard Book House | **P0** | [core/hwre/](../core/hwre/hydraulics/hydraulics.md) | Ch 8 (Navier-Stokes & Boundary Layer), Ch 11 (Pipe Flow & Moody Chart), Ch 18 (Pelton & Francis Turbines) |
| **Open-Channel Hydraulics** | Ven Te Chow | McGraw-Hill Classic | **P1** | [core/hwre/](../core/hwre/README.md) | Dynamic equation of unsteady flow, St. Venant equations, water surface profile classification |
| **Computational Methods for Fluid Dynamics** | Ferziger, Perić & Street | Springer | **P2** | [core/hwre/](../core/hwre/hydraulics/turbulence-modeling.md) | Finite Volume Method ($FVM$), PISO/SIMPLE pressure-velocity coupling, $k-\varepsilon$ / $k-\omega\text{ SST}$ turbulence |
| **Groundwater Hydrology** | D.K. Todd & L.W. Mays | Wiley | **P1** | [core/hwre/](../core/hwre/README.md) | Darcy's law, Theis & Cooper-Jacob unsteady well hydraulics, saltwater intrusion dynamics |

---

## 3. Structural Engineering & Solid Mechanics

| Textbook Title | Author(s) | Publisher | Priority | Supported Repository Module | High-Yield Chapters & Concepts |
|:---|:---|:---|:---:|:---|:---|
| **Mechanics of Materials** | R.C. Hibbeler | Pearson | **P0** | [core/structures/](../core/structures/README.md) | Ch 6 (Bending Stress & Flexure Formula), Ch 7 (Transverse Shear), Ch 9 (Stress Transformation & Mohr's Circle) |
| **Limit State Design of Reinforced Concrete** | P.C. Varghese | PHI Learning | **P0** | [core/structures/](../core/structures/README.md) | IS 456:2000 Limit State Philosophy, Singly/Doubly Reinforced Beams, Shear & Torsional reinforcement |
| **Design of Steel Structures (Limit State)** | S.K. Duggal | Tata McGraw-Hill | **P0** | [core/structures/](../core/structures/README.md) | IS 800:2007 Bolted/Welded Connections, Tension/Compression Members, Plate Girder stiffeners |
| **Structural Analysis** | C.S. Reddy | Tata McGraw-Hill | **P1** | [core/structures/](../core/structures/README.md) | Moment Distribution Method, Slope-Deflection, Flexibility & Stiffness Matrix Methods |

---

## 4. Geotechnical & Foundation Engineering

| Textbook Title | Author(s) | Publisher | Priority | Supported Repository Module | High-Yield Chapters & Concepts |
|:---|:---|:---|:---:|:---|:---|
| **Soil Mechanics and Foundation Engineering** | Gopal Ranjan & A.S.R. Rao | New Age | **P0** | [core/geotechnical/](../core/geotechnical/geotechnical.md) | Ch 5 (Compaction & Consolidation $C_c$), Ch 9 (Mohr-Coulomb Shear Strength), Ch 13 (Rankine & Coulomb Earth Pressure) |
| **Principles of Foundation Engineering** | Braja M. Das | Cengage Learning | **P0** | [core/geotechnical/](../core/geotechnical/geotechnical.md) | Terzaghi & Meyerhof bearing capacity equations, Pile group settlement, Negative skin friction |
| **Soil Mechanics** | Lambe & Whitman | Wiley | **P1** | [core/geotechnical/](../core/geotechnical/geotechnical.md) | Effective stress paths ($p-q$ diagrams), critical state soil mechanics |

---

## 5. Quantitative Aptitude & Mathematical Logic

| Textbook Title | Author(s) | Publisher | Priority | Supported Repository Module | High-Yield Chapters & Concepts |
|:---|:---|:---|:---:|:---|:---|
| **Quantitative Aptitude for Competitive Examinations** | R.S. Aggarwal | S. Chand | **P0** | [aptitude/quant/](../aptitude/quant/README.md) | Standard arithmetic problem archetypes, time & work, ratios, mixtures |
| **Higher Engineering Mathematics** | B.S. Grewal | Khanna Publishers | **P0** | [aptitude/quant/](../aptitude/quant/README.md) | Linear Algebra (Eigenvalues/Vectors), Multivariable Calculus, Ordinary Differential Equations |
| **How to Prepare for Quantitative Aptitude for CAT** | Arun Sharma | McGraw-Hill | **P1** | [aptitude/quant/](../aptitude/quant/README.md) | Level 2/3 Permutations & Combinations, Probability Bayes, Number Systems |

---

## 6. Cross-Reference Links to Preparation Tracks
- [Aptitude Formula Sheet](../aptitude/FORMULA_SHEET.md)
- [Project & Thesis Defense Playbook](../prep/PROJECT_DEFENCE.md)
- [Master Placement Readiness Scorecard](../prep/READINESS_SCORECARD.md)

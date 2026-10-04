# Canonical Learning Paths & Curriculum Trajectories

> **Architecture Standard**: Every topic must trace through an unambiguous 9-stage progression:  
> `ROLE ↓ REQUIRED KNOWLEDGE ↓ TOPIC ↓ STUDY MATERIAL ↓ WORKED EXAMPLE ↓ PRACTICE ↓ TEST ↓ INTERVIEW QUESTIONS ↓ REVISION ↓ COMPANY`

---

## 1. The 9-Stage Curriculum Framework

```
[1. Target Role]
       │
       ▼
[2. Knowledge Domain]
       │
       ▼
[3. Canonical Topic]
       │
       ▼
[4. Study Material] ───────────► [02_core/ or 03_non_core/]
       │
       ▼
[5. Worked Problem] ──────────► Theoretical derivations & solved step-by-step cases
       │
       ▼
[6. Practice Problem] ────────► Timed unguided problem sets
       │
       ▼
[7. Objective/Test Stage] ────► GATE, OA, or coding test questions
       │
       ▼
[8. Interview Defense] ───────► [05_interview/technical/]
       │
       ▼
[9. Rapid Revision] ──────────► [06_revision/] (Checklists, Key Formulas, 24-hr sheet)
       │
       ▼
[Target Company Routing] ─────► [04_company-prep/]
```

---

## 2. Canonical Trajectories by Domain

### Trajectory A: Water Resources Engineer (HWRE) — Open Channel Flow
1. **Target Role**: Hydraulic / Water Resources Engineer (L&T Infra, Vassar Labs, Tata Consulting Engineers)
2. **Knowledge Domain**: Surface Water Hydraulics & River Engineering
3. **Canonical Topic**: Open Channel Flow — Specific Energy & Critical Flow
4. **Study Material**: `02_core/hwre/open-channel-flow/` & `02_core/civil-engineering/fluid-mechanics/`
5. **Worked Problem**: Derivation of $E_c = \frac{3}{2} y_c$ for rectangular channels; transition over smooth humps and channel contractions without choking.
6. **Practice Problem**: Critical depth calculation for trapezoidal channel with side slopes $1:1.5$; hydraulic jump energy loss $\Delta E = \frac{(y_2 - y_1)^3}{4 y_1 y_2}$.
7. **Test Stage**: GATE Civil 2-mark numerical questions on upstream water surface profile shifts ($M_1, M_2, S_2$).
8. **Interview Defense**: `05_interview/technical/hwre/README.md` ("What causes hydraulic jump?", "Why does specific energy curve have two alternate depths?").
9. **Rapid Revision**: `06_revision/7-day/hwre-checklist.md` & `06_revision/interview-tomorrow/` (Froude number, conjugate depths, Manning's roughness).
10. **Target Company Routing**: `04_company-prep/hwre-companies/` & `04_company-prep/core-companies/`

---

### Trajectory B: Fundamental Civil Engineering — Pipe Flow & Boundary Layer
1. **Target Role**: Core Infrastructure / Plant Design Engineer (Bechtel, Jacobs, Engineers India Limited)
2. **Knowledge Domain**: Fluid Mechanics & Pipeline Hydraulics
3. **Canonical Topic**: Pipe Flow Losses, Moody Diagram & Boundary Layer Separation
4. **Study Material**: `02_core/civil-engineering/fluid-mechanics/03_pipe-flow-and-losses.md` & `04_boundary-layer-and-drag.md`
5. **Worked Problem**: Darcy-Weisbach head loss with equivalent length method for minor fittings ($K_{valve} = 0.2, K_{bend} = 0.4$); hydraulic grade line (HGL) vs energy grade line (EGL) sketching.
6. **Practice Problem**: Three-reservoir pipe junction network solved via Hardy Cross iterative method.
7. **Test Stage**: Technical Online Assessments (OA) covering Reynolds number thresholds, laminar Hagen-Poiseuille equations ($f = 64/Re$), and von Kármán momentum integral.
8. **Interview Defense**: `05_interview/technical/civil/README.md` ("Differentiate between adverse pressure gradient and boundary layer separation", "Why is Darcy friction factor 4 times Fanning friction factor?").
9. **Rapid Revision**: `06_revision/3-day/civil-formula-sheet.md`
10. **Target Company Routing**: `04_company-prep/core-companies/`

---

### Trajectory C: Computational Fluid Dynamics (CFD) Engineer
1. **Target Role**: Simulation Engineer / Hydrodynamic Modeler (Airbus, Flow Science, Shell, Ansys)
2. **Knowledge Domain**: Numerical Fluid Dynamics & Turbulence Modeling
3. **Canonical Topic**: Navier-Stokes Discretization & Two-Equation Turbulence Closures ($k$-$\epsilon$ vs $k$-$\omega$ SST)
4. **Study Material**: `02_core/cfd/`
5. **Worked Problem**: Finite Volume Method (FVM) 1D advection-diffusion discretization with Upwind vs Central differencing; Courant-Friedrichs-Lewy (CFL) stability criterion calculation ($C = \frac{u \Delta t}{\Delta x} \le 1$).
6. **Practice Problem**: OpenFOAM mesh refinement setup targeting $y^+ < 1$ for resolving viscous sublayer vs $30 < y^+ < 300$ for standard wall functions.
7. **Test Stage**: Numerical methods assessment on PISO vs SIMPLE pressure-velocity coupling algorithms.
8. **Interview Defense**: `05_interview/technical/cfd/README.md` ("Why does standard $k$-$\epsilon$ fail in adverse pressure gradient boundary layers?", "Explain the physical meaning of turbulent kinetic energy dissipation rate $\epsilon$ vs specific dissipation $\omega$").
9. **Rapid Revision**: `06_revision/roles/cfd-revision.md`
10. **Target Company Routing**: `04_company-prep/company-directory/`

---

### Trajectory D: Digital & Management Consultant
1. **Target Role**: Digital Consultant / Business Strategy Analyst (Accenture Japan, Kearney, Auctus)
2. **Knowledge Domain**: Consulting Problem Solving & Enterprise Technology
3. **Canonical Topic**: MECE Issue Trees, Market Sizing Guesstimates & Digital Transformation Architecture
4. **Study Material**: `03_non_core/consulting/` & `01_common/placement-math/business-engineering-math.md`
5. **Worked Problem**: Profitability diagnostic tree for declining manufacturing operating margins; Cloud migration ROI and TCO estimation model.
6. **Practice Problem**: Tokyo EV charging station demand estimation; Unit economics calculation for a B2B SaaS platform.
7. **Test Stage**: Consulting Aptitude & Quantitative Reasoning test (`01_common/aptitude/` + `01_common/placement-math/`).
8. **Interview Defense**: `05_interview/case-interview/` & `05_interview/technical/non-core/README.md` ("Walk me through an IT modernization roadmap for a legacy bank", "How do you size the market for industrial drone inspection?").
9. **Rapid Revision**: `06_revision/14-day/` & `06_revision/roles/consulting-revision.md`
10. **Target Company Routing**: `04_company-prep/company-specific-prep/accenture-japan/` & `04_company-prep/consulting-companies/`

---

### Trajectory E: Quantitative / Data Science Role
1. **Target Role**: Data Analyst / Machine Learning Engineer (Tiger Analytics, Fractal, Mu Sigma)
2. **Knowledge Domain**: Statistical Inference, Feature Engineering & Time-Series Forecasting
3. **Canonical Topic**: Autoregressive Time-Series Modeling (ARIMA/SARIMAX) & Hydro-Climatological Statistical Distribution Fitting
4. **Study Material**: `03_non_core/data-science/` & `03_non_core/analytics/`
5. **Worked Problem**: Stationarity transformation via Dickey-Fuller unit-root test; PACF/ACF order identification for seasonal monthly streamflow records.
6. **Practice Problem**: End-to-end Python pipeline fitting Extreme Value Type I (Gumbel) and Log-Pearson III distributions with SciPy.
7. **Test Stage**: HackerRank / CodeSignal SQL + Python data manipulation assessment.
8. **Interview Defense**: `05_interview/technical/non-core/README.md` ("What is the difference between covariance stationarity and strict stationarity?", "How do you handle severe class imbalance without overfitting?").
9. **Rapid Revision**: `06_revision/roles/analytics-revision.md`
10. **Target Company Routing**: `04_company-prep/company-directory/` & `08_projects/streamflow-time-series/`

---

## 3. Strict Boundary Rules Against Repository Bloat

| Category | Canonical Home | Strictly Forbidden |
| :--- | :--- | :--- |
| **Test Aptitude Math** | `01_common/aptitude/` | Do NOT place in `placement-math` or `consulting` |
| **Business/Engineering Math** | `01_common/placement-math/` | Do NOT put pure speed-math tricks here |
| **Fundamental Fluid Mechanics** | `02_core/civil-engineering/fluid-mechanics/` | Do NOT duplicate inside `hwre/` or `cfd/` |
| **Hydraulics & Hydrology** | `02_core/hwre/` | Do NOT recreate textbook fluid statics here |
| **CFD & Turbulence Models** | `02_core/cfd/` | Do NOT recreate general civil notes here |
| **Company Prep** | `04_company-prep/` | Strictly a routing & process layer — **NO full topic notes** |
| **Interview Questions** | `05_interview/` | Technical Q&As belong here, not inside `02_core` subject notes |
| **Revision Checklists** | `06_revision/` | Link sheets, formulas, rapid drills — **NO multi-page re-explanations** |
| **Textbook Resources** | `07_resources/` | External links and book lists do not replace study modules |
| **Projects** | `08_projects/` | Must adhere to 5-file standard (`README`, `technical`, `questions`, `results`, `resume`) |

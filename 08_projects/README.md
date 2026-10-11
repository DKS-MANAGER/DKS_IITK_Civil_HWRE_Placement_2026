# 08_PROJECTS — Engineering Portfolio & Technical Project Defense

> **Directory Focus**: Technical project frameworks, mathematical modeling archetypes, and interview defense systems for Civil Engineering & Hydraulics and Water Resources Engineering (HWRE).  
> **Interview Purpose**: Structured project defense, methodology walkthroughs, technical trade-offs, and quantified results presentation.

---

## 1. Project Portfolio Architecture

```text
08_projects/
├── README.md                      # Master portfolio defense framework & presentation guide
├── project-first-learning.md      # Pedagogical roadmap: learning engineering tools by building
└── archetypes/                    # Generic, neutral hypothetical engineering case archetypes
    ├── computational-fluid-simulation.md    # Hydrodynamic Scour & Structural Risk Modeling
    ├── environmental-time-series.md         # Catchment Streamflow & Hydrological Time-Series
    └── water-infrastructure-systems.md      # Frequency Analysis, ET0 & Pipe Network Hydraulics
```

---

## 2. Project Presentation & Interview Defense Framework

When presenting any engineering project to an interview panel (Core Civil, HWRE, Consulting, or Data/Software):

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                      4-STEP PROJECT DEFENSE FRAMEWORK                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Problem Context & Objective (30s) ──► What was the engineering failure   │
│                                           or planning bottleneck?           │
│ 2. Methodology & Stack (45s)         ──► Governing equations, tools used    │
│                                           (HEC-RAS, Python, QGIS, OpenFOAM).│
│ 3. Key Challenge & Trade-Off (45s)   ──► Data scarcity, numerical stability,│
│                                           calibration bottlenecks.          │
│ 4. Quantified Outcome & Value (30s)  ──► % error reduction, NSE score,      │
│                                           cost/risk reduction.              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Case Archetypes Directory Map

| Archetype | Domain | Primary Technical Stack | Core Methodology & Practice Focus |
| :--- | :--- | :--- | :--- |
| [`computational-fluid-simulation.md`](archetypes/computational-fluid-simulation.md) | Hydraulic Structures & Risk | HEC-RAS 2D, OpenFOAM, Python | Saint-Venant 2D, $k\text{-}\omega$ SST turbulence, Grid Convergence Index (GCI), scour mitigation trade-offs. |
| [`environmental-time-series.md`](archetypes/environmental-time-series.md) | Hydrology & Data Science | Python (Statsmodels, PyTorch, Scikit-learn) | Stationarity testing (ADF), SARIMAX vs LSTM, Nash-Sutcliffe Efficiency (NSE), leakage prevention. |
| [`water-infrastructure-systems.md`](archetypes/water-infrastructure-systems.md) | Urban Water & Hydro-Meteorology | QGIS, EPANET, Python | Gumbel & Log-Pearson III IDF curves, FAO-56 Penman-Monteith, Hazen-Williams pipe network pressure head. |

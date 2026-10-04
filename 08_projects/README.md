# 08_PROJECTS — Engineering Portfolio & Technical Project Defense

> **Directory Focus**: Portfolio documentation for M.Tech Civil / Hydraulics & Water Resources Engineering (HWRE) projects.  
> **Interview Purpose**: Structured project defense, methodology walkthroughs, technical trade-offs, and quantified results.

---

## 1. Project Portfolio Architecture

```text
08_projects/
├── README.md                      # Master portfolio defense framework & presentation guide
├── bridgerisk/                    # Bridge hydrodynamic scour & flood risk modeling
├── streamflow-time-series/        # Streamflow time-series forecasting (statistical & ML)
├── idf-pet/                       # IDF rainfall frequency & Evapotranspiration modeling
└── other-projects/                # GIS watershed delineation, EPANET & automation
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

## 3. Project Directory Map

| Project | Domain | Primary Stack | Key Metrics / Results |
| :--- | :--- | :--- | :--- |
| [`bridgerisk/`](bridgerisk/README.md) | Hydraulic Structures & Risk | HEC-RAS 2D, OpenFOAM, Python | Pier scour depth prediction, 100-yr return flood risk mapping. |
| [`streamflow-time-series/`](streamflow-time-series/README.md) | Hydrology & Data Science | Python (Statsmodels, PyTorch), HEC-HMS | NSE = 0.88 in discharge prediction, 7-day lead flood forecasting. |
| [`idf-pet/`](idf-pet/README.md) | Hydro-Meteorology | Python, R, Penman-Monteith | Gumbel & Log-Pearson III IDF curves, climate trend analysis. |
| [`other-projects/`](other-projects/README.md) | GIS, Water Networks & Tech | QGIS, EPANET, SQL | Catchment delineation, pipe network pressure optimization. |

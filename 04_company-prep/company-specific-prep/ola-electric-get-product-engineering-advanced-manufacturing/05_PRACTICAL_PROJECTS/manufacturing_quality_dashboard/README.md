# Project 2: Manufacturing Quality & SPC Analytics Dashboard

## 1. Project Background and Objective
High-volume manufacturing at Ola Futurefactory produces thousands of precision components per day (traction motor rotor shafts, aluminum swingarms, and coated electrode foils). Ensuring zero assembly line defects requires real-time Statistical Process Control (SPC) and automated process capability analysis ($C_p, C_{pk}$).

This project implements an automated Python-based Quality Analytics Engine that:
1. Simulates continuous in-line dimensional measurements across 30 production subgroups ($n = 5$ parts per subgroup).
2. Computes the Grand Mean ($\bar{\bar{X}}$), Average Range ($\bar{R}$), Upper Control Limit ($\text{UCL}_{\bar{X}}$), and Lower Control Limit ($\text{LCL}_{\bar{X}}$).
3. Evaluates Nelson / Western Electric Rules to detect mean shifts, tool wear drifts, and assignable causes.
4. Calculates Process Potential ($C_p$), Process Capability ($C_{pk}$), and expected non-conformance rate in Parts Per Million (PPM).
5. Aggregates end-of-line vehicle assembly defects into an automated Pareto Analysis.

---

## 2. Statistical Formulas & Algorithms

### A. Control Limits ($\bar{X}$ and $R$ Chart)
For subgroup size $n = 5$ ($A_2 = 0.577, D_3 = 0, D_4 = 2.114, d_2 = 2.326$):
$$\text{UCL}_{\bar{X}} = \bar{\bar{X}} + A_2 \bar{R}, \quad \text{LCL}_{\bar{X}} = \bar{\bar{X}} - A_2 \bar{R}$$
$$\text{UCL}_R = D_4 \bar{R}, \quad \text{LCL}_R = D_3 \bar{R} = 0$$
$$\hat{\sigma}_{\text{within}} = \frac{\bar{R}}{d_2}$$

### B. Process Capability Indices
$$\text{Specification: } \text{USL} = 45.030\text{ mm}, \quad \text{LSL} = 44.970\text{ mm}, \quad \text{Nominal} = 45.000\text{ mm}$$
$$C_p = \frac{\text{USL} - \text{LSL}}{6\hat{\sigma}}$$
$$C_{pu} = \frac{\text{USL} - \bar{\bar{X}}}{3\hat{\sigma}}, \quad C_{pl} = \frac{\bar{\bar{X}} - \text{LSL}}{3\hat{\sigma}}$$
$$C_{pk} = \min(C_{pu}, C_{pl})$$

---

## 3. Python Implementation (`spc_quality_dashboard.py`)
Run the script directly via:
```bash
python spc_quality_dashboard.py
```
The script runs self-contained without external visualization GUI dependencies, printing a comprehensive tabular report and text-based ASCII control chart.


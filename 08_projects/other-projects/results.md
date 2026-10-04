# Quantified Results & Engineering Outcomes — `other-projects`

> **Project Code**: `other-projects`  
> **Key Metrics**: Execution speedups, hydraulic head stabilization, energy savings, concrete strength & emissions reduction.

---

## 1. Watershed Delineation Pipeline Benchmark

| Metric | Manual QGIS GUI Workflow | Automated Python (PyQGIS/GDAL) | Performance Gain |
| :--- | :---: | :---: | :---: |
| **DEM Pit Filling (30m, 1,200 km²)** | $35\text{ mins}$ | $2.1\text{ mins}$ | $16.7\times$ faster |
| **D8 Flow Direction & Accumulation** | $45\text{ mins}$ | $4.5\text{ mins}$ | $10\times$ faster |
| **Stream Extraction & Strahler Order** | $25\text{ mins}$ | $1.2\text{ mins}$ | $20.8\times$ faster |
| **Morphometric Basin Indices** | $60\text{ mins}$ | $0.4\text{ mins}$ | $150\times$ faster |
| **Total Turnaround Time** | **$\approx 2.8\text{ hours}$** | **$8.2\text{ mins}$** | **$\approx 20\times$ speedup** |

* Extracted Basin Area: $1,245.8\text{ km}^2$; Bifurcation Ratio $R_b = 3.82$; Drainage Density $D_d = 1.48\text{ km/km}^2$.

---

## 2. EPANET Municipal Water Distribution Results

* **Baseline Deficits**: 8 terminal nodes suffered from negative pressure down to $-3.5\text{ m}$ during peak morning demand (08:00 AM, multiplier $1.8\times$).
* **Optimized Network Response**:
  * Implemented booster variable-frequency pump schedule and installed 2 Pressure Reducing Valves (PRVs).
  * **Minimum Residual Head**: Elevated from $-3.5\text{ m}$ to **$+13.4\text{ m}$** across all 45 demand nodes.
  * **Daily Energy Consumption**: Reduced from $1,420\text{ kWh/day}$ to **$1,205\text{ kWh/day}$** (**$-15.1\%$ electrical savings**).
  * **Non-Revenue Water (Leakage Risk)**: Excess pressure zones ($>40\text{ m}$) eliminated, reducing background leak risk by an estimated $22\%$.

---

## 3. Sustainable Concrete Mix Performance (M30 Grade)

| Parameter | Control Mix (100% OPC) | Optimized Mix (67% OPC + 25% FA + 8% SF) | Variance |
| :--- | :---: | :---: | :---: |
| **Water / Binder Ratio** | 0.45 | 0.42 (with PCE Superplasticizer) | -6.7% |
| **7-Day Compressive Strength** | $26.4\text{ MPa}$ | $22.1\text{ MPa}$ | -16.3% |
| **28-Day Compressive Strength** | $35.8\text{ MPa}$ | **$38.5\text{ MPa}$** | **+7.5%** |
| **56-Day Compressive Strength** | $38.2\text{ MPa}$ | **$44.8\text{ MPa}$** | **+17.3%** |
| **Split Tensile Strength (28d)** | $3.2\text{ MPa}$ | **$3.7\text{ MPa}$** | **+15.6%** |
| **Embodied $\text{CO}_2$ per $\text{m}^3$** | $382\text{ kg CO}_2\text{e}$ | **$290\text{ kg CO}_2\text{e}$** | **-24.1%** |
| **Material Cost per $\text{m}^3$** | ₹4,650 | **₹3,990** | **-14.2%** |

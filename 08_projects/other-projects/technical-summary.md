# Technical Summary — Catchment GIS, EPANET Networks & Concrete Materials

> **Project Code**: `other-projects`  
> **Domain**: Geospatial Hydrology, Pipe Network Hydraulics, Sustainable Concrete Materials

---

## 1. Geospatial Watershed Delineation (QGIS / PyQGIS / GDAL)
* **Algorithm Pipeline**:
  1. **DEM Conditioning**: Planchon & Darboux pit-filling algorithm to resolve sink depressions in SRTM 30m DEM.
  2. **Flow Routing**: Deterministic 8-node flow direction (D8) and flow accumulation grid generation.
  3. **Stream Network Extraction**: Threshold-based channel definition ($A_{threshold} \ge 1.0\text{ km}^2$) and Strahler stream ordering.
  4. **Morphometric Equations**:
     * Bifurcation Ratio: $R_b = \frac{N_u}{N_{u+1}}$
     * Drainage Density: $D_d = \frac{\sum L}{A}$
     * Form Factor: $R_f = \frac{A}{L_b^2}$

---

## 2. Municipal Water Network Modeling (EPANET 2.2 / WNTR)
* **Governing Hydraulics**:
  * **Hazen-Williams Head Loss**:
    $$h_f = 10.67 \cdot C^{-1.852} \cdot D^{-4.87} \cdot L \cdot Q^{1.852}$$
  * **Conservation of Mass at Nodes**: $\sum Q_{in} - \sum Q_{out} = Demand$
  * **Energy Conservation along Loops**: $\sum h_f = \Delta H_{pump} - \Delta H_{valve}$
* **Solvers & Optimization**: Solved via Todini's Global Gradient Algorithm; extended-period simulation (EPS) running across a 24-hour diurnal demand multiplier curve ($0.4\times \text{ at 3 AM}$ to $1.8\times \text{ at 8 AM}$).

---

## 3. Supplementary Cementitious Material Mix Design (IS 10262:2019)
* **Water-Binder Ratio**: Adjusted target $w/b = 0.42$ with superplasticizer (polycarboxylate ether - PCE) dosage at $0.6\%$ by weight of cementitious material.
* **Pozzolanic Reaction Kinetics**:
  $$\text{Fly Ash/Silica Fume} + \text{Ca(OH)}_2 (\text{CH}) + \text{H}_2\text{O} \longrightarrow \text{C-S-H Gel (Secondary binder)}$$
  Fills micro-capillary pores, refining pore structure and increasing durability against chloride ion penetration.

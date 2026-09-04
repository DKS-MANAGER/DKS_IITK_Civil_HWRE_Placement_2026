# 🌧️ HEC-HMS Deep-Dive Tutorial

> **Tool:** HEC-HMS (Hydrologic Modeling System)
> **Level:** L2 → L3 (from first model to a complete rainfall-runoff + flood hydrograph)
> **Prerequisite:** [`hydrology-tech.md`](../hydrology/hydrology-tech.md), hydrology basics ([`hydrology.md`](../../core/hwre/hydrology/hydrology.md))

This is a **hands-on tutorial**, not a feature list. You will build a real hydrologic model end-to-end: a **small watershed** with subbasins, a reach, a junction, and an outlet, driven by a design storm. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

A **rainfall-runoff model** with:
1. Subbasins (with loss, transform, and baseflow methods)
2. A reach (channel routing)
3. A junction and outlet
4. A design storm (precipitation)
5. A **flood hydrograph** at the outlet

By the end you will understand the full HEC-HMS workflow and can discuss it in an interview.

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **HEC-HMS 4.x** | Free download from USACE HEC website. Includes a GUI. |
| **HEC-HMS via Python** | For automation and batch runs. Good for data roles. |

> **Interview tip:** Be able to say "I modeled a watershed in HEC-HMS with the SCS curve number method and generated a flood hydrograph for a design storm." This is a concrete, defensible claim.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| Watershed boundaries | GIS | Subbasin delineation |
| Land use / soil | Maps | Curve number (CN) |
| Rainfall | IDF curves, gauge data | Design storm |
| Channel geometry | Survey | Reach routing |
| Basin lag / time of concentration | Empirical methods | Transform |

---

## 🧱 STEP 1 — Create a New Project

1. Open HEC-HMS → **File → New Project**
2. Set the **Project Title** (e.g., "Watershed Flood Study")
3. Set the **Units** (SI or US) and **Time zone**
4. Set the **Default time interval** (e.g., 1 hour)

**Why:** HEC-HMS organizes the model into a basin model, meteorologic model, and control specifications.

**Check:** The project is created.

---

## 🧱 STEP 2 — Create the Basin Model

1. **Basin Model Manager** → **New**
2. Name the basin model (e.g., "Watershed_Basin")
3. Open the basin model in the **Basin Model** editor

**Why:** The basin model defines the watershed elements (subbasins, reaches, junctions, outlet) and their connectivity.

**Check:** The basin model is created and open.

---

## 🧱 STEP 3 — Add Subbasins

1. In the Basin Model editor, use the **Subbasin** tool
2. Place subbasins on the canvas
3. For each subbasin, set:
   - **Area** (km² or mi²)
   - **Loss method** (e.g., SCS Curve Number)
   - **Transform method** (e.g., SCS Unit Hydrograph)
   - **Baseflow method** (e.g., Recession)

**Why:** Subbasins generate runoff from rainfall. The loss method determines how much rainfall becomes runoff, and the transform method converts excess rainfall to a hydrograph.

**Check:** Subbasins appear on the canvas.

---

## 🧱 STEP 4 — Configure Loss (SCS Curve Number)

For each subbasin, set the **SCS Curve Number** parameters:
- **Curve Number (CN):** e.g., 75 (based on land use/soil)
- **Initial abstraction (Ia):** e.g., 5 mm (or use 0.2·S)
- **Impervious %:** e.g., 10%

**Why:** The curve number method estimates runoff from rainfall based on land use and soil type. CN 75 is typical for a mixed residential/agricultural watershed.

**Check:** The loss parameters are set.

---

## 🧱 STEP 5 — Configure Transform (SCS Unit Hydrograph)

For each subbasin, set the **SCS Unit Hydrograph** parameters:
- **Lag time (Tlag):** e.g., 2 hours (time from centroid of rainfall to peak of runoff)

**Why:** The unit hydrograph transforms excess rainfall into a direct runoff hydrograph. Lag time controls the timing of the peak.

**Check:** The transform parameters are set.

---

## 🧱 STEP 6 — Configure Baseflow (Recession)

For each subbasin, set the **Recession** baseflow parameters:
- **Initial baseflow:** e.g., 1 m³/s
- **Recession constant:** e.g., 0.9
- **Ratio to peak:** e.g., 0.1

**Why:** Baseflow represents the groundwater contribution to streamflow. The recession constant controls how baseflow decays.

**Check:** The baseflow parameters are set.

---

## 🧱 STEP 7 — Add Reach, Junction, and Outlet

1. Use the **Reach** tool to connect subbasins downstream
2. Set reach routing method (e.g., **Muskingum**):
   - **K** (travel time): e.g., 1 hour
   - **X** (weighting): e.g., 0.2
3. Use the **Junction** tool to merge flows
4. Use the **Outlet** tool at the downstream end

**Why:** Reaches route flow downstream. The junction combines flows from multiple subbasins. The outlet is where the final hydrograph is computed.

**Check:** The elements are connected: subbasins → reach → junction → outlet.

---

## 🧱 STEP 8 — Create the Meteorologic Model

1. **Meteorologic Model Manager** → **New**
2. Name it (e.g., "Design_Storm")
3. Set:
   - **Precipitation method:** SCS Storm (or Gage Weights)
   - **Storm type:** Type II (or your regional type)
   - **Storm depth:** e.g., 100 mm (design rainfall)
   - **Storm duration:** e.g., 24 hours
4. Assign the precipitation to the subbasins

**Why:** The meteorologic model provides the rainfall input. The SCS storm distributes the design rainfall over time.

**Check:** The meteorologic model is created and assigned.

---

## 🧱 STEP 9 — Create Control Specifications

1. **Control Specifications Manager** → **New**
2. Name it (e.g., "24hr_Storm")
3. Set:
   - **Start date/time**
   - **End date/time** (start + 24 hours + routing time)
   - **Time interval:** 1 hour

**Why:** The control specifications define the simulation period.

**Check:** The control specifications are set.

---

## 🧮 STEP 10 — Run the Simulation

1. **Compute → Run Manager**
2. Select the basin model, meteorologic model, and control specifications
3. Click **Compute**

**Why:** This runs the rainfall-runoff simulation.

**Check:** The run completes without errors. Note the continuity error (< 1% is good).

---

## 📊 STEP 11 — View Results

1. **Results → Global Summary** — see peak flow, runoff volume, etc.
2. **Results → Time Series** — see the hydrograph at the outlet
3. **Results → Summary Table** — see peak flow at each element

**Why:** Results show the flood hydrograph and how the watershed responds.

**Check:** The outlet hydrograph shows a peak flow. The peak flow value is your design flood.

---

## 🔍 STEP 12 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "Continuity error > 1%" | Time step too large, or routing instability | Reduce time step, check routing parameters |
| "No runoff" | CN too low, or rainfall too small | Check CN, increase storm depth |
| "Negative flow" | Routing instability | Adjust Muskingum K/X, reduce time step |
| "Peak too high" | CN too high, or lag too short | Reduce CN, increase lag time |

**Why:** These are common issues in real projects. Knowing how to fix them is a strong interview signal.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through an HEC-HMS model you built."**
   → "I modeled a watershed with subbasins, a reach, and an outlet. I used the SCS curve number method for losses, SCS unit hydrograph for transform, and Muskingum for routing, then ran a design storm and generated a flood hydrograph."

2. **"What is the SCS curve number method?"**
   → "It's a method to estimate runoff from rainfall based on land use and soil type. The curve number (CN) ranges from 0 to 100, with higher values meaning more runoff."

3. **"What is a unit hydrograph?"**
   → "It's the runoff response of a watershed to one unit of excess rainfall. It's used to transform rainfall into a runoff hydrograph."

4. **"What is Muskingum routing?"**
   → "It's a hydrologic routing method that translates and attenuates a flood wave through a channel using two parameters, K (travel time) and X (weighting)."

5. **"How does HEC-HMS connect to HEC-RAS?"**
   → "HEC-HMS generates the flood hydrograph at the outlet, which becomes the upstream flow input for a HEC-RAS river model."

---

## ✅ Self-Checklist

- [ ] Project created with correct units
- [ ] Basin model created
- [ ] Subbasins added with area
- [ ] Loss method configured (SCS CN)
- [ ] Transform method configured (SCS UH)
- [ ] Baseflow configured (Recession)
- [ ] Reach, junction, outlet added
- [ ] Meteorologic model created (design storm)
- [ ] Control specifications set
- [ ] Simulation run with continuity error < 1%
- [ ] Flood hydrograph reviewed at outlet

---

## 🔗 Related Resources

- [`hydrology-tech.md`](../hydrology/hydrology-tech.md) — Where HEC-HMS fits in the hydrology stack
- [`hec-ras-walkthrough.md`](hec-ras-walkthrough.md) — HEC-HMS output feeds HEC-RAS
- [`hydrology.md`](../../core/hwre/hydrology/hydrology.md) — Hydrology theory
- [`flood-control.md`](../../core/hwre/flood_control/flood-control.md) — Flood management
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions

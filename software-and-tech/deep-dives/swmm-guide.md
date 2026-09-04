# 🌧️ EPA SWMM Deep-Dive Guide

> **Tool:** EPA SWMM (Storm Water Management Model)
> **Level:** L2 → L3 (from first model to a complete urban drainage + LID analysis)
> **Prerequisite:** [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md), urban hydrology basics ([`hydrology.md`](../../core/hwre/hydrology/hydrology.md))

This is a **hands-on guide**, not a feature list. You will build a real urban drainage model end-to-end: a **small residential catchment** with pipes, a junction, an outfall, and a **Low Impact Development (LID)** control. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

An **urban stormwater model** with:
1. Subcatchments (pervious + impervious areas)
2. A drainage pipe network (conduits, junctions, outfall)
3. A design storm (rainfall)
4. A **LID control** (e.g., rain garden) to reduce runoff

By the end you will understand the full SWMM workflow and can discuss it in an interview.

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **EPA SWMM 5.x** | Free download from USEPA website. Includes a GUI. |
| **SWMM via Python (pyswmm)** | For automation and batch runs. Good for data roles. |

> **Interview tip:** Be able to say "I modeled an urban catchment in SWMM with a pipe network and evaluated a rain garden LID control for peak flow reduction." This is a concrete, defensible claim.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| Catchment boundaries | GIS | Subcatchment delineation |
| Land use | Zoning maps | Imperviousness |
| Pipe network | Utility maps | Conduits, junctions |
| Rainfall | IDF curves, gauge data | Design storm |
| Soil type | Soil maps | Infiltration |

---

## 🧱 STEP 1 — Create a New Project

1. Open SWMM → **File → New**
2. Set the **Project Title** (e.g., "Residential Catchment — Stormwater")
3. Set **Units** (SI or US) and **Flow Units** (CMS, LPS, etc.)
4. Set the **ID prefix** for each object type (optional)

**Why:** SWMM organizes the model into objects (subcatchments, junctions, conduits, etc.). Setting units correctly is essential.

**Check:** The project is created with the correct units.

---

## 🧱 STEP 2 — Define Rain Gage and Time Series

1. Click the **Rain Gage** tool
2. Place a rain gage on the map
3. Set properties:
   - **Rain format:** Intensity (or Volume)
   - **Time interval:** 5 min (or your design storm interval)
   - **Rain source:** Time Series
4. Create a **Time Series** for the design storm:
   - **Edit → Time Series**
   - Add the rainfall intensity at each time step

**Why:** The rain gage provides the rainfall input. The time series defines the design storm (e.g., a 2-year, 24-hour storm).

**Check:** The rain gage appears on the map. The time series has data.

---

## 🧱 STEP 3 — Create Subcatchments

1. Click the **Subcatchment** tool
2. Draw subcatchments on the map (or place them and set area)
3. For each subcatchment, set:
   - **Area** (ha or acres)
   - **Width** (characteristic flow path width)
   - **% Impervious** (e.g., 60% for residential)
   - **Slope** (%)
   - **Rain gage** (assign the rain gage)
   - **Outlet** (the junction it drains to)
   - **Infiltration model** (e.g., Horton or Green-Ampt)

**Why:** Subcatchments generate runoff. The % impervious and width control how much and how fast runoff is generated.

**Check:** Each subcatchment is connected to a rain gage and an outlet.

---

## 🧱 STEP 4 — Create Junctions and Outfall

1. Click the **Junction** tool
2. Place junctions at pipe connections (manholes)
3. Set junction properties:
   - **Invert elevation** (bottom of the manhole)
   - **Max depth** (to the surface)
4. Click the **Outfall** tool
5. Place the outfall at the downstream end
6. Set the outfall **invert elevation** and **boundary condition** (e.g., free outfall)

**Why:** Junctions are where pipes connect. The outfall is where the system discharges (to a river, lake, or treatment plant).

**Check:** Junctions and outfall appear on the map with correct elevations.

---

## 🧱 STEP 5 — Create Conduits (Pipes)

1. Click the **Conduit** tool
2. Draw a conduit from one junction to the next
3. Set conduit properties:
   - **Shape** (circular, rectangular, etc.)
   - **Diameter** (for circular)
   - **Length** (auto-computed from map)
   - **Roughness** (Manning's n, e.g., 0.013 for concrete)
   - **Inlet/Outlet offsets** (if the pipe doesn't connect at the invert)

**Why:** Conduits carry the runoff. The diameter and slope determine the pipe capacity.

**Check:** The conduits connect the junctions in a network ending at the outfall.

---

## 🧱 STEP 6 — Set Infiltration Parameters

1. **Edit → Options → Infiltration**
2. Choose the infiltration model (e.g., **Horton**):
   - **Max infiltration rate** (e.g., 76 mm/hr)
   - **Min infiltration rate** (e.g., 10 mm/hr)
   - **Decay constant** (e.g., 4 /hr)
   - **Drying time** (e.g., 7 days)

**Why:** Infiltration determines how much rainfall soaks into the ground vs. runs off. Horton is a common model.

**Check:** The infiltration parameters are set.

---

## 🧱 STEP 7 — Set Simulation Options

1. **Edit → Options → General**
   - **Flow routing:** Dynamic Wave (most accurate)
   - **Infiltration:** Horton
2. **Edit → Options → Time Steps**
   - **Routing time step:** 30 sec (or 60 sec)
   - **Reporting time step:** 5 min
3. **Edit → Options → Dates**
   - Set the simulation start and end dates/times

**Why:** Dynamic Wave routing is the most accurate (solves the full Saint-Venant equations). The time steps control accuracy and speed.

**Check:** The simulation options are set.

---

## 🧮 STEP 8 — Run the Simulation

1. Click **Run** (or **Project → Run Simulation**)
2. Monitor the **status report** for:
   - **Continuity errors** (< 1% is good)
   - **Flooding** (junctions that overflow)
   - **Convergence** issues

**Why:** The status report tells you if the model is stable and physically consistent.

**Check:** Continuity error < 1%. Note any flooding.

---

## 📊 STEP 9 — View Results

1. **View → Profile** — see the water surface along a conduit
2. **View → Time Series** — see flow at the outfall over time
3. **View → Table** — see junction flooding, conduit flow, etc.

**Why:** Results show how the system performs under the design storm.

**Check:** The outfall hydrograph shows a peak flow. Note the peak flow value (you'll compare it after adding LID).

---

## 🌿 STEP 10 — Add a LID Control (Rain Garden)

1. **Project → LID Controls**
2. Click **Add** and choose a LID type (e.g., **Rain Garden**)
3. Set the LID layers:
   - **Surface** (storage depth, vegetation)
   - **Soil** (thickness, porosity, conductivity)
   - **Storage** (gravel layer, if applicable)
4. **Project → LID Usage**
5. Assign the LID to a subcatchment:
   - Select the subcatchment
   - Set the **% of subcatchment area** treated by the LID

**Why:** LID controls (rain gardens, permeable pavement, green roofs) reduce runoff by storing and infiltrating water. This is a key modern stormwater management technique.

**Check:** The LID is assigned to a subcatchment.

---

## 🧮 STEP 11 — Re-run and Compare

1. Re-run the simulation with the LID
2. Compare the **outfall peak flow** before and after LID

**Why:** The comparison quantifies the LID's benefit — a key deliverable for stormwater management reports.

**Check:** The peak flow is reduced (e.g., 20–40% reduction).

---

## 🔍 STEP 12 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "Continuity error > 1%" | Time step too large, or unstable routing | Reduce routing time step |
| "Junction flooding" | Pipe capacity exceeded | Increase pipe diameter, add storage |
| "Negative depth" | Steep slope or wrong geometry | Check conduit slope, offsets |
| "No runoff" | Subcatchment not connected to rain gage | Check rain gage assignment |

**Why:** These are common issues in real projects. Knowing how to fix them is a strong interview signal.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through a SWMM model you built."**
   → "I modeled a residential catchment with a pipe network and a rain garden LID. I set up subcatchments with imperviousness, added conduits and junctions, ran a design storm with dynamic wave routing, and compared peak flow before and after the LID."

2. **"What's the difference between steady and dynamic wave routing?"**
   → "Steady routing assumes flow is constant. Dynamic wave routing solves the full Saint-Venant equations, capturing backwater, surcharging, and storage — more accurate but slower."

3. **"What is a LID control?"**
   → "Low Impact Development — practices like rain gardens, permeable pavement, and green roofs that reduce runoff by storing and infiltrating stormwater at the source."

4. **"How do you calibrate a SWMM model?"**
   → "I adjust infiltration parameters, imperviousness, and roughness until the modeled outfall hydrograph matches observed flow data."

5. **"What does the % impervious control?"**
   → "It controls how much rainfall becomes runoff. Higher imperviousness → more runoff, faster peak, higher peak flow."

---

## ✅ Self-Checklist

- [ ] Project created with correct units
- [ ] Rain gage and time series defined
- [ ] Subcatchments created with area, width, imperviousness
- [ ] Junctions and outfall placed
- [ ] Conduits connected the network
- [ ] Infiltration parameters set
- [ ] Simulation options configured (dynamic wave)
- [ ] Simulation run with continuity error < 1%
- [ ] Results reviewed (outfall hydrograph)
- [ ] LID control added and assigned
- [ ] Peak flow compared before/after LID

---

## 🔗 Related Resources

- [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md) — Where SWMM fits in the HWRE stack
- [`hydrology-tech.md`](../hydrology/hydrology-tech.md) — Rainfall-runoff modeling
- [`hydrology.md`](../../core/hwre/hydrology/hydrology.md) — Urban hydrology theory
- [`wastewater-engineering.md`](../../core/hwre/wastewater/wastewater-engineering.md) — Combined sewer systems
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions

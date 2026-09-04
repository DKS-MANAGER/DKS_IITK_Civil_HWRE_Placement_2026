# 🌊 HEC-RAS Deep-Dive Walkthrough

> **Tool:** HEC-RAS (Hydrologic Engineering Center — River Analysis System)
> **Level:** L2 → L3 (from first launch to a complete 1D steady + 2D flood model)
> **Prerequisite:** [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md), basic open-channel flow theory ([`open-channel-flow.md`](../../core/hwre/open_channel_flow/open-channel-flow.md))

This is a **hands-on walkthrough**, not a feature list. You will build a real model end-to-end. Follow the steps in order. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

A **1D steady-flow river model** of a reach with a bridge, then extend it to a **2D floodplain** using RAS Mapper. By the end you will have:

1. A working 1D steady model with correct cross-sections and a bridge
2. A calibrated water-surface profile
3. A 2D floodplain with a flood-inundation map
4. The vocabulary to discuss the model in an interview

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **HEC-RAS 6.x (recommended)** | Download from USACE HEC website (free). Includes RAS Mapper (GIS) built-in. |
| **HEC-RAS 5.x** | Older but still widely used in industry. Same core workflow. |
| **HEC-GeoRAS** | ArcGIS extension for pre/post-processing. Optional — RAS Mapper replaces most of it. |

> **Interview tip:** Be able to say "I used HEC-RAS 6.x with RAS Mapper for floodplain delineation." Version awareness signals you're current.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| DEM (Digital Elevation Model) | SRTM, ASTER, ALOS, or survey | Terrain, cross-sections, floodplain |
| River centerline | GIS digitizing or survey | Model geometry alignment |
| Bank lines | GIS or imagery | Cross-section extent |
| Flow data | Gauge records, HEC-HMS output | Boundary conditions |
| Roughness (Manning's n) | Land-use maps, tables | Friction |

---

## 🧱 STEP 1 — Create a New Project

1. Open HEC-RAS → **File → New Project**
2. Set the **Project Title** (e.g., "Ganga Reach — Flood Study")
3. Set the **Project File** location (`.prj` file)
4. Click **OK**

**Why:** HEC-RAS stores all model files in a project. The `.prj` file is the master that references geometry, flow, plan, and output files.

**Check:** A new project folder appears with the `.prj` file.

---

## 🗺️ STEP 2 — Set Up the Terrain (RAS Mapper)

1. Open **RAS Mapper** (Tools → RAS Mapper, or the map icon)
2. **Add Terrain:** Right-click **Terrains** → **Add New Terrain**
3. Browse to your DEM file (`.tif`, `.img`, or `.hdf`)
4. Name it (e.g., "Reach_DEM")
5. Click **Create**

**Why:** The terrain is the foundation. HEC-RAS extracts cross-sections from it and uses it for 2D floodplain mapping.

**Check:** The DEM appears as a colored elevation layer. Zoom to your study reach.

---

## 📐 STEP 3 — Draw the River Centerline

1. In RAS Mapper, right-click **Geometries** → **New Geometry** → name it "Reach_Geometry"
2. Right-click the geometry → **New River** → name the river (e.g., "MainRiver")
3. Right-click the river → **New Reach** → name the reach (e.g., "Reach1")
4. Use the **draw tool** to trace the centerline **downstream to upstream** (HEC-RAS convention: flow goes from higher to lower stationing)

**Why:** The centerline defines the flow path and stationing. Drawing downstream-to-upstream ensures station 0 is at the downstream end.

**Check:** The centerline appears as a line. The arrow direction should point upstream (against flow).

---

## 🏞️ STEP 4 — Add Cross-Sections

1. Right-click the reach → **Cross Sections** → **Add Cross Sections**
2. Use the **cut line tool** to draw a line **perpendicular to flow** at each location you want a cross-section
3. Add cross-sections at:
   - Upstream and downstream ends
   - Just upstream and downstream of the bridge
   - At every major change in geometry (bends, constrictions, roughness changes)

**Why:** Cross-sections are where HEC-RAS solves the energy equation. Too few → inaccurate results. Too many → slow and redundant.

**Check:** Each cross-section appears as a line crossing the river. In the geometry editor, you'll see the cross-section profile (elevation vs. station).

---

## 🏗️ STEP 5 — Edit Cross-Section Data

1. Open the **Geometric Data Editor** (Geometry → Geometric Data)
2. Click **Cross Sections** → select each cross-section
3. For each, verify:
   - **Station/Elevation points** (from the terrain — check they look right)
   - **Downstream reach lengths** (distance to the next cross-section downstream)
   - **Manning's n values** (left bank, channel, right bank)
   - **Bank stations** (where the channel meets the floodplain)
   - **Contraction/Expansion coefficients** (default 0.1/0.3, adjust near structures)

**Why:** The energy equation needs accurate geometry, roughness, and reach lengths. Bank stations separate the main channel from the floodplain for roughness and conveyance.

**Check:** The cross-section plot shows the channel and floodplain. The bank stations are at the right locations.

---

## 🌉 STEP 6 — Add a Bridge

1. In the Geometric Data Editor, click **Bridges and Culverts**
2. Select the cross-section just upstream of the bridge location
3. Click **Add Bridge/Culvert**
4. Define:
   - **Deck/roadway** (top of bridge, width, elevation)
   - **Piers** (number, width, location)
   - **Bridge opening** (low chord, high chord)
5. Set the **bridge modeling approach** (Energy, Momentum, Yarnell, etc.)

**Why:** Bridges constrict flow and cause backwater. HEC-RAS computes the head loss through the structure using the selected approach.

**Check:** The bridge appears in the cross-section plot. The deck and piers are visible.

---

## 💧 STEP 7 — Enter Flow Data

1. Open the **Steady Flow Data Editor** (Edit → Steady Flow Data)
2. Add a **Flow Change Location** at the upstream cross-section
3. Enter the **flow value** (e.g., 2500 m³/s for a design flood)
4. Add **boundary conditions**:
   - Upstream: **Flow Hydrograph** or **Flow** (a single value)
   - Downstream: **Normal Depth** (enter friction slope) or **Known WS** (water surface elevation)

**Why:** The upstream flow is the driving input. The downstream boundary condition is needed to start the computation.

**Check:** The flow data editor shows your flow value and boundary conditions.

---

## 🧮 STEP 8 — Create a Plan and Run

1. Open the **Steady Flow Analysis** (Run → Steady Flow Analysis)
2. Select:
   - **Geometry file** (your geometry)
   - **Steady flow file** (your flow data)
   - **Plan** (create a new plan, e.g., "Plan_2500")
3. Set the **flow regime** (Subcritical, Supercritical, or Mixed)
4. Click **Compute**

**Why:** The plan combines geometry + flow + computation options. The flow regime tells HEC-RAS how to solve the energy equation.

**Check:** The computation window shows the iterations converging. Watch for **errors** (e.g., "The water surface has gone below the ground" — means the flow can't pass).

---

## 📊 STEP 9 — View Results

1. Open the **Cross Section Output Table** (View → Cross Section Output Table)
2. Check:
   - **Water surface elevation** at each cross-section
   - **Velocity** and **flow area**
   - **Froude number** (should be < 1 for subcritical)
3. Open the **Profile Plot** (View → Water Surface Profiles) to see the water surface along the reach

**Why:** The output table and profile plot are how you verify the model makes physical sense.

**Check:** The water surface is smooth (no abrupt jumps). The Froude number is < 1 for subcritical flow.

---

## 🔍 STEP 10 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "Water surface has gone below ground" | Flow too high for the section, or section too small | Increase section size, check geometry, or reduce flow |
| "The energy equation could not be balanced" | Steep slope, hydraulic jump, or bad geometry | Use **Mixed** flow regime, refine sections |
| "Negative depth" | Section too small or wrong boundary condition | Check geometry, adjust downstream BC |
| "Cross section not defined" | Missing station/elevation data | Re-edit the cross-section |

**Why:** These are the most common errors in real projects. Knowing how to fix them is a strong interview signal.

---

## 🗺️ STEP 11 — Extend to 2D Floodplain (RAS Mapper)

1. In RAS Mapper, right-click your geometry → **New 2D Flow Area**
2. Draw a polygon covering the floodplain
3. Set the **cell size** (e.g., 30 m or 50 m) and **breaklines** (for roads, levees)
4. In the Geometric Data Editor, connect the 1D river to the 2D area with **lateral structures** or **2D connections**
5. Re-run the plan with the 2D area included

**Why:** 2D modeling captures floodplain flow that 1D can't (flow spreading, storage, flow around obstacles).

**Check:** The 2D mesh appears in RAS Mapper. The model runs with the 2D area.

---

## 🗺️ STEP 12 — Create a Flood Inundation Map

1. In RAS Mapper, right-click **Results** → **Add New Results**
2. Select your plan
3. Right-click the results → **Map Layers** → **Depth** or **Water Surface Elevation**
4. Set the **contour interval** and **color scheme**
5. Export the map (File → Export) as an image or shapefile

**Why:** The flood map is the deliverable that stakeholders (and interviewers) see. It's the "so what" of the whole model.

**Check:** The floodplain is colored by depth. The map shows which areas are inundated.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through how you built a HEC-RAS model."**
   → "I started with a DEM in RAS Mapper, drew the centerline, added cross-sections, entered Manning's n, added a bridge, set the flow and boundary conditions, ran a steady analysis, and validated the water surface against gauge data."

2. **"What's the difference between 1D and 2D HEC-RAS?"**
   → "1D solves the energy equation along a centerline — good for river channels. 2D solves the shallow water equations on a mesh — good for floodplains where flow spreads laterally."

3. **"How do you calibrate a HEC-RAS model?"**
   → "I adjust Manning's n values until the modeled water surface matches observed gauge data, then validate on an independent event."

4. **"What is the energy equation HEC-RAS solves?"**
   → "It balances specific energy between cross-sections, accounting for friction loss, contraction/expansion loss, and structure losses."

5. **"How do you handle a bridge in HEC-RAS?"**
   → "I add a bridge at a cross-section, define the deck and piers, and select a modeling approach (energy, momentum, or Yarnell) to compute the head loss."

---

## ✅ Self-Checklist

- [ ] Project created and terrain loaded
- [ ] Centerline drawn downstream-to-upstream
- [ ] Cross-sections added at key locations
- [ ] Manning's n and bank stations set
- [ ] Bridge added with deck and piers
- [ ] Flow and boundary conditions entered
- [ ] Plan created and run successfully
- [ ] Results verified (water surface, Froude, velocity)
- [ ] 2D floodplain added and run
- [ ] Flood inundation map created

---

## 🔗 Related Resources

- [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md) — Where HEC-RAS fits in the HWRE stack
- [`hydrology-tech.md`](../hydrology/hydrology-tech.md) — HEC-HMS for rainfall-runoff input
- [`open-channel-flow.md`](../../core/hwre/open_channel_flow/open-channel-flow.md) — The theory behind the model
- [`sediment-tech.md`](../sediment/sediment-tech.md) — HEC-RAS sediment transport extension
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions

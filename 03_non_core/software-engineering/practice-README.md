# 🏋️ PRACTICE SYSTEM — Software Practice Exercises

> **"Don't just practice — do these specific tasks."**
> Every P0/P1 tool has Basic → Intermediate → Role-specific exercises.
> Complete these before your interview. Each exercise maps to a real interview question.

---

## How to Use

1. Pick your **target role** from [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md)
2. Do the **Basic** exercises for your P0 tools (L2)
3. Do the **Intermediate** exercises (L2→L3)
4. Do the **Role-specific** exercise (L3, resume-ready)
5. Take the matching test in [`tests/README.md`](../tests/README.md)

---

## AutoCAD

### Basic
1. Draw a 5000×3000 mm room plan with 230mm walls (`OFFSET` + `TRIM`)
2. Draw a 3×3 column grid at 4000mm spacing (`ARRAY`)
3. Draw a simply supported beam elevation with supports

### Intermediate
4. Draw a complete footing plan with 4 footings + dimensions
5. Draw a beam-column joint detail with rebar (Ø20 main, Ø8 stirrups)
6. Create a door block and insert it 5 times

### Role-Specific (Structural)
7. Draw a complete structural plan: grid → columns → beams → slab edge
8. Draw a rebar schedule table (bar marks, diameters, lengths, quantities)

---

## Excel

### Basic
1. Build a cube test register: 10 results → average, max, min, pass/fail
2. Build a steel weight calculator: diameter + length → weight
3. Use `VLOOKUP` to look up rebar areas from a steel table

### Intermediate
4. Build a BOQ sheet: 15 items → quantity × rate, `SUMIF` by category
5. Build a rate analysis for M25 concrete (cement, sand, aggregate, labour)
6. Create a Pivot Table from 50 rows of site data

### Role-Specific
7. **Structural:** Beam design check sheet (IS 456) — Mu_lim vs applied
8. **Construction:** Running bill format with measurement, rate, deduction
9. **HWRE:** Manning's equation solver — find normal depth

---

## ETABS

### Basic
1. Model a single-bay portal frame, apply point load, check moments
2. Model a continuous beam on 3 supports, compare with hand calc
3. Define materials + sections for a G+3 building

### Intermediate
4. Model a G+3 building with rigid diaphragm, run DL+LL analysis
5. Add seismic load (response spectrum, Zone III), check story drift
6. Design a column, check reinforcement ratio

### Role-Specific (Structural)
7. Model a G+10 building with shear walls, run response spectrum
8. Perform pushover analysis, extract capacity curve
9. Check inter-story drift per IS 1893

---

## STAAD.Pro

### Basic
1. Model a simply supported beam (6m, ISMB 300), compare max moment with wL²/8
2. Model a continuous beam on 3 supports, check support moments
3. Model a roof truss, apply joint loads, check member forces

### Intermediate
4. Model a portal frame with fixed base, apply lateral load, check sway
5. Add load combinations per IS 456, run design
6. Perform steel design of a frame member per IS 800

### Role-Specific (Structural)
7. Model a G+3 building frame with gravity + seismic loads
8. Design a steel warehouse truss with IS 800 checks
9. Extract support reactions for foundation design

---

## HEC-RAS

### Basic
1. Create a project, load a DEM, draw a centerline (downstream-to-upstream)
2. Add 5 cross-sections, set Manning's n and bank stations
3. Run a steady flow analysis with one flow value

### Intermediate
4. Add a bridge with deck + piers, re-run, compare water surface
5. Set up a 2D floodplain area, run with 2D connections
6. Create a flood inundation map in RAS Mapper

### Role-Specific (Water Resources)
7. Calibrate Manning's n against observed gauge data (<5% error)
8. Build a 1D+2D flood model for a real river reach
9. Generate a flood-risk map (depth zones) for a community

---

## QGIS

### Basic
1. Load a shapefile + DEM, set the correct CRS
2. Create a 100m buffer around a river centerline
3. Clip a land-use layer to a study area

### Intermediate
4. Delineate a watershed from a DEM (fill → flow direction → accumulation → pour point)
5. Create a flood map by overlaying HEC-RAS depth results
6. Perform a spatial join (count points in polygons)

### Role-Specific
7. **Hydrology:** Delineate a watershed, compute area for HEC-HMS
8. **GIS:** Land-use change detection using two satellite images
9. **Water Resources:** Prepare a flood inundation map from HEC-RAS

---

## Primavera / MS Project

### Basic
1. Create a 5-activity schedule with FS dependencies, find critical path
2. Add milestones at key completion points
3. Calculate float for a non-critical activity

### Intermediate
4. Build a building schedule (WBS → activities → dependencies)
5. Assign resources (2 crews), check for overallocation
6. Create a baseline, update progress to 50%

### Role-Specific (Construction)
7. Create a foundation-to-handover schedule for a residential tower
8. Perform earned value analysis (SPI, CPI) on a 3-month schedule
9. Compress the schedule by crashing the critical path

---

## Revit / Navisworks

### Basic
1. Create a 2-story frame (levels, grids, columns, beams, slabs)
2. Create a column schedule (count, volume)
3. Create a sheet with plan + section views

### Intermediate
4. Add rebar to a beam, schedule it
5. Link an architectural model, run clash detection
6. Create a 4D simulation (link schedule to model)

### Role-Specific (BIM)
7. Model a structural frame, coordinate with MEP
8. Produce a clash report with assigned responsibilities
9. Extract quantity takeoff for BOQ

---

## Python

### Basic
1. Read a CSV of rainfall data, compute monthly totals
2. Write a function to solve Manning's equation for velocity
3. Plot a depth-discharge curve with Matplotlib

### Intermediate
4. Use Pandas to clean 50,000 rows of sensor data (missing values, outliers)
5. Automate reading 20 HEC-RAS output files and extracting water surface
6. Build a NumPy-based frame analysis (stiffness method) for a 2-bar truss

### Role-Specific
7. **HWRE:** Automate Manning's calculation for 200+ cross-sections → Excel report
8. **Structural:** OpenSeesPy pushover analysis → capacity curve
9. **Data:** End-to-end analysis: CSV → Pandas → visualization → summary

---

## SQL

### Basic
1. Write a query to find duplicate records in a table
2. Write a query for the second-highest salary
3. Write a query with a JOIN across two tables

### Intermediate
4. Write a query using a window function (running total)
5. Write a query using a CTE
6. Write a query with GROUP BY + HAVING

### Role-Specific
7. **GIS:** PostGIS query — find all parcels within 500m of a river
8. **Data:** Query a sales table for monthly revenue by region
9. **PM:** Query a project table for delayed projects (SPI < 1)

---

## Completion Checklist

```
☐ I completed Basic exercises for all my P0 tools
☐ I completed Intermediate exercises for my P0 tools
☐ I completed the Role-specific exercise for my primary tool
☐ I can explain each exercise in an interview
☐ I have a project (from the tool page) on my resume
☐ I passed the matching test in tests/README.md
```

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Test System | [`tests/README.md`](../tests/README.md) |
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Tool Index | [`TOOLS_INDEX.md`](../TOOLS_INDEX.md) |
| Project-First Learning | [`project-first-learning.md`](../project-first-learning.md) |

---

*Practice is the difference between "knows the tool" and "can defend the tool."*
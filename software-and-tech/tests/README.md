# 🧪 TEST SYSTEM — Software Tests & Assessments

> **Test what matters: workflow, troubleshooting, engineering judgment — not button locations.**
> For each P0 tool: Tool Quiz → Workflow Test → Troubleshooting Test → Interview Test.

---

## How to Use

1. Complete the exercises in [`practice/README.md`](../practice/README.md)
2. Take the **Tool Quiz** (self-check, answers at bottom)
3. Do the **Workflow Test** (scenario-based, no single answer)
4. Do the **Troubleshooting Test** (debug/model interpretation)
5. Do the **Interview Test** (rapid-fire, timed)
6. Score yourself: **≥80% on Quiz + all Workflow/Troubleshooting scenarios answered = interview-ready**

---

## AutoCAD Test

### Tool Quiz (10 questions)
1. What is the difference between model space and paper space?
2. What is a layer and why is it important?
3. What is the difference between a line and a polyline?
4. What command creates a parallel copy of a line?
5. What does `TRIM` do?
6. How do you create a reusable symbol?
7. What is the purpose of `OFFSET` in wall drawing?
8. What units should a structural drawing use?
9. What is an XREF?
10. How do you plot at the correct scale?

### Workflow Test
**Scenario:** You receive an architectural plan and must produce a structural plan.
**Task:** Describe your workflow (setup → draw → annotate → plot).
**Success criteria:** Units set, layers created, grid drawn, columns/beams placed, dimensions added, paper-space layout at 1:100.

### Troubleshooting Test
**Scenario:** Your drawing plots at the wrong scale.
**Task:** Diagnose and fix.
**Check:** Model space vs paper space, plot scale, units.

### Interview Test (rapid-fire, 5 min)
- "Walk me through producing a structural drawing."
- "How do you set up layers and why?"
- "What would happen if you drew in meters but plotted in mm?"

---

## Excel Test

### Tool Quiz (10 questions)
1. What is the difference between `VLOOKUP` and `INDEX`/`MATCH`?
2. What does `$A$1` mean vs `A1`?
3. What is a Pivot Table used for?
4. What does `SUMIF` do?
5. How do you prevent invalid input in a cell?
6. What is conditional formatting?
7. What is a named range?
8. How do you lock formula cells?
9. What is the difference between a formula and a function?
10. How do you handle `#N/A` errors?

### Workflow Test
**Scenario:** Build a BOQ for a small building.
**Task:** Describe your workbook structure (takeoff → rate analysis → summary).
**Success criteria:** Input cells separated from formulas, `$` references correct, pass/fail checks, print-ready.

### Troubleshooting Test
**Scenario:** Your `VLOOKUP` returns `#N/A`.
**Task:** Diagnose and fix.
**Check:** Lookup value exists, table range correct, exact vs approximate match.

### Interview Test (rapid-fire, 5 min)
- "How do you ensure your Excel sheet is error-free?"
- "Why Excel over Python for this BOQ?"
- "How do you handle rate changes in your template?"

---

## ETABS Test

### Tool Quiz (10 questions)
1. What is the difference between ETABS and STAAD.Pro?
2. What is a rigid diaphragm?
3. What is the difference between equivalent static and response spectrum analysis?
4. What load combinations does IS 456 require?
5. What is inter-story drift and its limit per IS 1893?
6. What is a shear wall used for?
7. What is a design ratio?
8. What is the difference between pinned and fixed supports?
9. What is P-delta analysis?
10. What is a pushover analysis?

### Workflow Test
**Scenario:** Model and analyze a G+5 building in Seismic Zone IV.
**Task:** Describe your workflow.
**Success criteria:** Grid, materials, sections, loads, combinations, diaphragm, analysis, drift check, design.

### Troubleshooting Test
**Scenario:** Your model shows instability.
**Task:** Diagnose.
**Check:** Supports, member connectivity, diaphragm, releases.

### Interview Test (rapid-fire, 5 min)
- "How do you model a shear wall in ETABS?"
- "How do you check inter-story drift?"
- "What would happen if you removed the diaphragm?"

---

## STAAD.Pro Test

### Tool Quiz (10 questions)
1. What is the difference between STAAD and ETABS?
2. What is the difference between a beam and a plate element?
3. What is the difference between fixed and pinned supports?
4. What is a load combination?
5. What is P-delta analysis?
6. What is a design ratio?
7. What is member orientation (beta angle)?
8. What is a truss member?
9. How do you extract support reactions?
10. What is the stiffness method?

### Workflow Test
**Scenario:** Analyze a steel portal frame.
**Task:** Describe your workflow.
**Success criteria:** Nodes, members, sections, supports, loads, analysis, design check.

### Troubleshooting Test
**Scenario:** Your model has instability.
**Task:** Diagnose.
**Check:** Supports, connectivity, releases, missing members.

### Interview Test (rapid-fire, 5 min)
- "How do you model a portal frame in STAAD?"
- "What is the difference between a beam and a plate element?"
- "How do you verify STAAD results against hand calc?"

---

## HEC-RAS Test

### Tool Quiz (10 questions)
1. What is HEC-RAS and what does it solve?
2. What is the difference between 1D and 2D HEC-RAS?
3. What data does a steady flow analysis need?
4. What is Manning's n and why does it matter?
5. What is a bank station?
6. What boundary conditions are available?
7. What is the energy equation HEC-RAS solves?
8. How do you model a bridge?
9. What is RAS Mapper used for?
10. How do you calibrate a HEC-RAS model?

### Workflow Test
**Scenario:** Build a flood model for a river reach.
**Task:** Describe your workflow.
**Success criteria:** DEM, centerline, cross-sections, Manning's n, flow, BC, plan, run, results, flood map.

### Troubleshooting Test
**Scenario:** Your model produces unrealistic water-surface results.
**Task:** Diagnose.
**Check:** Cross-section spacing, Manning's n, boundary conditions, flow regime, bridge losses.

### Interview Test (rapid-fire, 5 min)
- "Why would a HEC-RAS model produce unrealistic water-surface results?"
- "How do you calibrate a HEC-RAS model?"
- "What would happen if you used a wrong downstream BC?"

---

## QGIS Test

### Tool Quiz (10 questions)
1. What is the difference between vector and raster?
2. What is a CRS?
3. What is the difference between geographic and projected CRS?
4. What is a buffer?
5. What is a spatial join?
6. How do you delineate a watershed?
7. What is IDW interpolation?
8. What is georeferencing?
9. What is a print layout?
10. What is PostGIS?

### Workflow Test
**Scenario:** Produce a flood-risk map.
**Task:** Describe your workflow.
**Success criteria:** DEM, watershed, HEC-RAS depth import, classification, layout.

### Troubleshooting Test
**Scenario:** Your layers don't align.
**Task:** Diagnose.
**Check:** CRS consistency, projections, georeferencing.

### Interview Test (rapid-fire, 5 min)
- "How do you delineate a watershed?"
- "What CRS would you use for India and why?"
- "How do you validate your GIS analysis?"

---

## Primavera / MS Project Test

### Tool Quiz (10 questions)
1. What is the critical path method?
2. What is float?
3. What is the difference between CPM and PERT?
4. What is a WBS?
5. What is a FS dependency?
6. What is resource leveling?
7. What is a baseline?
8. What is earned value management?
9. What is SPI and CPI?
10. What is schedule compression?

### Workflow Test
**Scenario:** Create a construction schedule for a building.
**Task:** Describe your workflow.
**Success criteria:** WBS, activities, dependencies, critical path, resources, baseline.

### Troubleshooting Test
**Scenario:** Your schedule has negative float.
**Task:** Diagnose.
**Check:** Dependencies, durations, resource constraints, milestones.

### Interview Test (rapid-fire, 5 min)
- "How do you create a WBS for a building project?"
- "What is the difference between CPM and PERT?"
- "How do you handle resource leveling?"

---

## Python Test

### Tool Quiz (10 questions)
1. What is the difference between a list and a NumPy array?
2. What is a Pandas DataFrame?
3. What is `.loc` vs `.iloc`?
4. What is broadcasting in NumPy?
5. What is a vectorized operation?
6. What is a virtual environment?
7. What is `try`/`except`?
8. What is a dictionary?
9. What is `groupby` in Pandas?
10. What is the difference between Python and MATLAB?

### Workflow Test
**Scenario:** Process 200+ cross-sections and compute normal depth.
**Task:** Describe your workflow.
**Success criteria:** Read CSV, compute hydraulic params, solve Manning's, plot, export.

### Troubleshooting Test
**Scenario:** Your script crashes on a large file.
**Task:** Diagnose.
**Check:** Memory, file encoding, data types, error handling.

### Interview Test (rapid-fire, 5 min)
- "How do you vectorize a loop?"
- "How do you handle missing data in Pandas?"
- "Why Python over MATLAB for this task?"

---

## SQL Test

### Tool Quiz (10 questions)
1. What is the difference between WHERE and HAVING?
2. What are the JOIN types?
3. What is a window function?
4. What is a CTE?
5. What is a correlated subquery?
6. What is an index?
7. What is the difference between SQL and NoSQL?
8. What is a primary key?
9. What is normalization?
10. What is a running total?

### Workflow Test
**Scenario:** Find the second-highest salary in a table.
**Task:** Write the query.
**Success criteria:** Correct query, handles ties, explainable.

### Troubleshooting Test
**Scenario:** Your query is slow.
**Task:** Diagnose.
**Check:** Indexes, joins, subqueries, table size.

### Interview Test (rapid-fire, 5 min)
- "Write a query for a running total."
- "When would you use SQL vs Pandas?"
- "How do you optimize a slow query?"

---

## Scoring

| Test | Pass Mark | Interview-Ready |
|:-----|:---------:|:----------------|
| Tool Quiz | 8/10 | 10/10 |
| Workflow Test | All steps | All steps + justification |
| Troubleshooting Test | Root cause found | Root cause + fix |
| Interview Test | 3/3 answered | 3/3 with depth |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Practice System | [`practice/README.md`](../practice/README.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Mock Tests (role-level) | [`../prep/mock-tests/README.md`](../../prep/mock-tests/README.md) |

---

*Tests measure what you can DO, not what you memorized.*
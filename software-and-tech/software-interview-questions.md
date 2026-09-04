# 🎤 Software Interview Questions Bank

> **For every important software: Basic → Practical → Technical → Troubleshooting → Validation → Comparison → Project Defense**
> **Deeper questions for CFD/GIS/FEM/software-modelling roles.**

---

## Question Framework

For every tool, prepare answers to these 7 categories:

| Category | Question Type |
|:---------|:--------------|
| **Basic** | What is it? |
| **Practical** | What have you done with it? |
| **Technical** | How does your workflow work? |
| **Troubleshooting** | What if results look wrong? |
| **Validation** | How do you know your result is correct? |
| **Comparison** | Why this software instead of another? |
| **Project Defense** | Explain your project workflow. |

---

## Python

### Basic
- What is Python? Why is it popular in engineering?
- What is the difference between a list and a NumPy array?
- What is a Pandas DataFrame?

### Practical
- How do you read a CSV and compute column statistics?
- How do you handle missing data?
- Explain `.loc` vs `.iloc`.

### Technical
- When would you use SciPy over NumPy?
- How do you vectorize a loop?
- Explain broadcasting in NumPy.

### Troubleshooting
- Your script crashes on a large file. What do you check?
- Results look wrong. How do you debug?

### Validation
- How do you verify your Python calculations?
- What test data would you use?

### Comparison
- Why Python over MATLAB?
- When would you use Excel instead of Python?

### Project Defense
- Walk me through your Python project.
- What was the hardest part?

---

## MATLAB

### Basic
- What is MATLAB? How is it different from Python?
- What is the difference between `*` and `.*`?

### Practical
- How do you solve a system of linear equations?
- Explain `ode45` vs `ode15s`.

### Technical
- How would you implement finite difference for the heat equation?
- What is a sparse matrix? When would you use it?

### Troubleshooting
- Your ODE solver is slow. What do you do?
- Results diverge. What do you check?

### Validation
- How do you verify your numerical solution?

### Comparison
- Why MATLAB over Python?

### Project Defense
- Explain your MATLAB project.

---

## SQL

### Basic
- What is the difference between WHERE and HAVING?
- What are the JOIN types?

### Practical
- Write a query to find duplicate records.
- How do you find the second highest salary?
- Write a query for a running total.

### Technical
- Explain correlated subqueries.
- When would you use a CTE vs a subquery?
- How do window functions differ from GROUP BY?

### Troubleshooting
- Your query is slow. What do you check?
- Results have NULLs you didn't expect. Why?

### Validation
- How do you verify your query results?

### Comparison
- When would you use SQL vs Pandas?

### Project Defense
- Describe your database schema.

---

## HEC-RAS

### Basic
- What is HEC-RAS? What problems does it solve?
- What is the difference between 1D and 2D?

### Practical
- Walk me through a HEC-RAS project.
- How do you set up a 2D floodplain model?

### Technical
- What boundary conditions are available?
- How do you calibrate a HEC-RAS model?

### Troubleshooting
- Your unsteady model isn't converging. What do you check?
- Water surface elevations look wrong. Why?

### Validation
- How do you validate against observed data?

### Comparison
- HEC-RAS vs OpenFOAM — when to use each?

### Project Defense
- Explain your flood modeling project.

---

## OpenFOAM

### Basic
- What is OpenFOAM? What is the case structure?
- What is the difference between RANS and LES?

### Practical
- How do you set up a channel flow simulation?
- What solver would you use for free-surface flow?

### Technical
- Explain the SIMPLE algorithm.
- What is y+? How does it affect your simulation?
- How do you perform a mesh independence study?

### Troubleshooting
- Your simulation diverges. What do you check?
- Residuals are flat but results look wrong. Why?

### Validation
- How do you validate your CFD results?
- What experimental data would you compare against?

### Comparison
- OpenFOAM vs ANSYS Fluent — when to use each?

### Project Defense
- Explain your CFD project from problem to results.

---

## PLAXIS

### Basic
- What is PLAXIS? What does it model?
- What is the difference between PLAXIS and GeoStudio?

### Practical
- Walk me through an excavation analysis.
- How do you model groundwater?

### Technical
- Explain the hardening soil model.
- How does PLAXIS handle soil-structure interaction?
- What is phi-c reduction?

### Troubleshooting
- Your model doesn't converge. What do you check?
- Settlement results look too high. Why?

### Validation
- How do you validate your PLAXIS results?

### Comparison
- PLAXIS vs GeoStudio — when to use each?

### Project Defense
- Explain your geotechnical model.

---

## STAAD.Pro / ETABS

### Basic
- What is the difference between STAAD.Pro and ETABS?
- What is a seismic load combination?

### Practical
- How do you model a multi-story building?
- How do you apply wind loads?

### Technical
- Explain the difference between pinned and fixed supports.
- What is moment redistribution?

### Troubleshooting
- Your model has instability. What do you check?
- Design fails code check. What do you do?

### Validation
- How do you verify your structural analysis?

### Comparison
- STAAD vs ETABS — when to use each?

### Project Defense
- Explain your building design project.

---

## Revit / BIM

### Basic
- What is BIM? How is it different from CAD?
- What is clash detection?

### Practical
- How do you create a structural model in Revit?
- How do you extract quantities?

### Technical
- What is IFC? Why is it important?
- How do you handle design changes in BIM?

### Troubleshooting
- Your model has coordination issues. How do you resolve?

### Validation
- How do you verify model accuracy?

### Comparison
- Revit vs AutoCAD — when to use each?

### Project Defense
- Explain your BIM coordination project.

---

## GIS (QGIS/ArcGIS)

### Basic
- What is the difference between vector and raster?
- What is a coordinate reference system?

### Practical
- How do you perform a spatial join?
- Walk me through a land use classification.

### Technical
- What is kriging? When would you use it?
- Explain supervised vs unsupervised classification.

### Troubleshooting
- Your layers don't align. What do you check?

### Validation
- How do you assess classification accuracy?

### Comparison
- QGIS vs ArcGIS — when to use each?

### Project Defense
- Explain your GIS project.

---

## Excel

### Basic
- What is the difference between VLOOKUP and INDEX/MATCH?
- How do you create a pivot table?

### Practical
- How do you perform a sensitivity analysis?
- Build a break-even model.

### Technical
- What is the difference between a formula and a function?
- How do you handle #N/A errors?

### Troubleshooting
- Your formulas return wrong results. What do you check?

### Validation
- How do you verify your Excel model?

### Comparison
- Excel vs Python — when to use each?

### Project Defense
- Explain your financial model.

---

## Power BI / Tableau

### Basic
- What is the difference between Power BI and Tableau?
- What is a measure vs a calculated column?

### Practical
- How do you build a dashboard?
- How do you create a DAX measure?

### Technical
- Explain the difference between a report and a dashboard.
- What is row-level security?

### Troubleshooting
- Your dashboard is slow. What do you check?

### Validation
- How do you verify your dashboard data?

### Comparison
- Power BI vs Tableau — when to use each?

### Project Defense
- Explain your dashboard project.

---

## Primavera / MS Project

### Basic
- What is the critical path method?
- What is float?

### Practical
- How do you create a CPM schedule?
- How do you update a schedule?

### Technical
- Explain earned value management.
- What is schedule compression?

### Troubleshooting
- Your schedule has negative float. What do you do?

### Validation
- How do you verify schedule accuracy?

### Comparison
- Primavera vs MS Project — when to use each?

### Project Defense
- Explain your construction schedule.

---

## Deep Questions for CFD/GIS/FEM Roles

### CFD
- Derive the Navier-Stokes equations.
- Explain the finite volume method discretization.
- What is the Courant number? Why does it matter?
- Explain the difference between explicit and implicit schemes.
- What is the energy cascade in turbulence?
- How do you choose between k-ε and k-ω SST?

### GIS
- Explain the difference between geographic and projected coordinate systems.
- What is the UTM projection?
- How do you perform a cost-distance analysis?
- What is the difference between IDW and kriging?

### FEM
- Explain the stiffness matrix assembly.
- What is the difference between h-refinement and p-refinement?
- How do you handle boundary conditions in FEM?
- What is a shape function?

---

## How to Prepare

```
For each tool on your resume:
    1. Write answers to all 7 categories
    2. Practice explaining your project workflow
    3. Prepare 2-3 troubleshooting scenarios
    4. Know when to use this tool vs alternatives
    5. Be ready to validate your results

Rule: Only list a tool on your resume if you can answer
      Basic + Practical + one Technical question about it.
```

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Priority System | [`priority-system.md`](priority-system.md) |
| Project-First Learning | [`project-first-learning.md`](project-first-learning.md) |
| Resume Positioning | [`resume-positioning.md`](resume-positioning.md) |

---

*See also: [`project-first-learning.md`](project-first-learning.md) for project-based interview prep.*

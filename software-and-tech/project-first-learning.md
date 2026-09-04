# 🛠️ Project-First Learning

> **Never recommend "Learn Python" without answering: Learn Python to DO WHAT?**
> Every major skill connects to a realistic, placement-ready project.

---

## The Principle

```
Don't learn a tool in isolation.
Learn a tool BY BUILDING something with it.

"Learn Python" → "Learn Python to automate hydraulic calculations"
"HEC-RAS"      → "HEC-RAS to simulate a flood"
"Power BI"     → "Power BI to build an infrastructure dashboard"
```

---

## Project Template

Every project should contain:

```
Objective:    What you're solving
Software:     Tools used
Prerequisites: What you need to know first
Workflow:     Step-by-step process
Expected Output: What you produce
GitHub Portfolio Structure: How to organize it
Interview Questions: What it prepares you for
```

---

## Project Catalog

### 1. Python → Automate Hydraulic Calculations

```
Objective: Automate Manning's equation for 200+ channel cross-sections
Software: Python (NumPy, Pandas, Matplotlib)
Prerequisites: Manning's equation, basic Python
Workflow:
    1. Read cross-section data (CSV)
    2. Compute hydraulic parameters
    3. Solve for normal depth
    4. Generate depth-discharge curves
    5. Export Excel report
Expected Output: Automated calculation pipeline + report
GitHub: /hydraulic-automation/ (code, data, results, README)
Interview: "How did you automate this?" / "How did you validate?"
```

### 2. Python + GIS → Flood-Risk Mapping

```
Objective: Map flood risk zones for a watershed
Software: Python (GeoPandas, Rasterio) + QGIS
Prerequisites: GIS basics, Python, DEM data
Workflow:
    1. Download DEM
    2. Delineate watershed (QGIS)
    3. Process elevation data (Python)
    4. Classify flood risk zones
    5. Generate risk map
Expected Output: Flood risk map + analysis report
GitHub: /flood-risk-mapping/
Interview: "How did you classify risk?" / "What data did you use?"
```

### 3. HEC-RAS → Flood Simulation

```
Objective: Simulate a design flood through a river reach
Software: HEC-RAS + GIS
Prerequisites: HEC-RAS basics, hydrology
Workflow:
    1. Import geometry (cross-sections)
    2. Set boundary conditions
    3. Run steady/unsteady analysis
    4. Map flood extent (HEC-RAS Mapper)
    5. Analyze results
Expected Output: Flood extent map + water surface profiles
GitHub: /flood-simulation/
Interview: "How did you set boundary conditions?" / "1D vs 2D?"
```

### 4. EPANET → Water Distribution Model

```
Objective: Model a water distribution network
Software: EPANET
Prerequisites: EPANET basics, pipe network concepts
Workflow:
    1. Define network (pipes, nodes, reservoirs)
    2. Set demands and properties
    3. Run hydraulic analysis
    4. Analyze pressure/flow
    5. Optimize (if applicable)
Expected Output: Network model + pressure/flow analysis
GitHub: /water-network/
Interview: "How did you size the pipes?" / "What's a hydraulic grade line?"
```

### 5. OpenFOAM → Sediment/Hydraulic CFD

```
Objective: Simulate flow around a structure
Software: OpenFOAM + ParaView + Python
Prerequisites: OpenFOAM basics, CFD fundamentals, Linux
Workflow:
    1. Define geometry (blockMesh/snappyHexMesh)
    2. Set boundary conditions
    3. Run solver
    4. Check convergence
    5. Visualize (ParaView)
    6. Validate
Expected Output: Flow field + validation plots
GitHub: /cfd-simulation/
Interview: "How did you mesh it?" / "How did you validate?"
```

### 6. PLAXIS → Slope Stability Model

```
Objective: Analyze slope stability
Software: PLAXIS 2D
Prerequisites: PLAXIS basics, soil mechanics
Workflow:
    1. Define geometry (slope, soil layers)
    2. Assign material model
    3. Generate mesh
    4. Run analysis
    5. Compute factor of safety
Expected Output: FoS + displacement field
GitHub: /slope-stability/
Interview: "What material model did you use?" / "How did you validate?"
```

### 7. ETABS → Structural Model

```
Objective: Design a multi-story building
Software: ETABS + AutoCAD + Excel
Prerequisites: ETABS basics, structural analysis
Workflow:
    1. Define grid, materials, sections
    2. Model structure
    3. Apply loads
    4. Run analysis
    5. Design members
    6. Detail (AutoCAD)
Expected Output: Structural model + design calculations
GitHub: /building-design/
Interview: "How did you apply seismic loads?" / "What code did you use?"
```

### 8. Power BI → Infrastructure Dashboard

```
Objective: Build a project performance dashboard
Software: Power BI + Excel (or SQL)
Prerequisites: Power BI basics, data
Workflow:
    1. Import data (Excel/SQL)
    2. Clean and model data
    3. Create measures (DAX)
    4. Build visualizations
    5. Publish dashboard
Expected Output: Interactive dashboard
GitHub: /infrastructure-dashboard/
Interview: "How did you calculate KPIs?" / "What insights did you find?"
```

### 9. SQL → Project Analytics Database

```
Objective: Analyze construction project data
Software: SQL (PostgreSQL/SQLite)
Prerequisites: SQL basics
Workflow:
    1. Design schema (projects, contractors, costs)
    2. Load data
    3. Write analytical queries
    4. Generate insights
Expected Output: Query results + insights report
GitHub: /project-analytics/
Interview: "Write a query to..." / "How did you design the schema?"
```

### 10. Primavera → Construction Schedule

```
Objective: Create a construction schedule
Software: Primavera P6 / MS Project
Prerequisites: CPM, scheduling basics
Workflow:
    1. Define activities
    2. Set dependencies
    3. Assign resources
    4. Calculate critical path
    5. Analyze float
Expected Output: CPM schedule + critical path analysis
GitHub: /construction-schedule/
Interview: "What's the critical path?" / "How do you handle delays?"
```

### 11. Revit → BIM Model

```
Objective: Create a structural BIM model
Software: Revit + Navisworks
Prerequisites: Revit basics, structural concepts
Workflow:
    1. Set up project
    2. Model structural elements
    3. Add materials and properties
    4. Coordinate (Navisworks)
    5. Extract quantities
Expected Output: BIM model + quantity schedule
GitHub: /bim-model/
Interview: "What's the difference between CAD and BIM?" / "How do you coordinate?"
```

---

## GitHub Portfolio Structure

```
my-portfolio/
├── README.md              # Overview, skills, contact
├── project-1/
│   ├── README.md          # Objective, tools, workflow, results
│   ├── code/              # Scripts
│   ├── data/              # Input data (small)
│   ├── results/           # Outputs, figures
│   └── docs/              # Reports, documentation
├── project-2/
│   └── ...
└── project-3/
    └── ...
```

### README Template

```markdown
# Project Name

## Objective
[One paragraph: what problem you're solving]

## Tools Used
- [Tool 1], [Tool 2], [Tool 3]

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Results
[Screenshot or description]

## How to Run
1. [Setup command]
2. [Run command]

## Interview Relevance
- Demonstrates: [skill 1], [skill 2]
- Discusses: [topic]
```

---

## Choosing Your Project

```
Rule: Pick ONE project that:
    1. Matches your target role
    2. Uses your primary tool
    3. You can complete in 2-4 weeks
    4. Produces a visual/quantifiable result
    5. You can explain in an interview

Don't start 5 projects. Finish 1-2 well.
```

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Branch Roadmaps | [`branch-roadmaps.md`](branch-roadmaps.md) |
| Role Roadmaps | [`role-roadmaps.md`](role-roadmaps.md) |
| Resume Positioning | [`resume-positioning.md`](resume-positioning.md) |
| Learning Roadmaps | [`learning-roadmaps.md`](learning-roadmaps.md) |

---

*See also: [`role-roadmaps.md`](role-roadmaps.md) for role-specific project recommendations.*

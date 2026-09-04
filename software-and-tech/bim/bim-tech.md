# 🏗️ BIM Technology Roadmap

> **Branch:** Building Information Modeling (BIM)
> **Covers BIM concepts, Revit, Navisworks, Civil 3D, coordination, clash detection, 4D/5D, and interoperability.**

---

## What is BIM?

BIM (Building Information Modeling) is a process for creating and managing digital representations of physical structures. It's not just 3D modeling — it's a **data-rich, collaborative workflow**.

### CAD vs BIM

| Aspect | CAD (AutoCAD) | BIM (Revit) |
|:-------|:-------------|:------------|
| Output | 2D drawings | 3D model with data |
| Data | Lines, arcs, text | Walls, beams, columns with properties |
| Changes | Manual update across sheets | Auto-update across all views |
| Quantity takeoff | Manual measurement | Automated from model |
| Collaboration | File-based | Workshared model |

### 3D vs 4D vs 5D

| Dimension | Adds | Purpose |
|:----------|:-----|:--------|
| **3D** | Geometry | Visualization, spatial coordination |
| **4D** | Time (schedule) | Construction sequencing, phasing |
| **5D** | Cost | Quantity takeoff, cost estimation |
| **6D** | Sustainability | Energy analysis, lifecycle assessment |
| **7D** | Facility management | Operations and maintenance |

### Model vs Drawing

```
Drawing:  A 2D representation of a building element
Model:    A 3D object with embedded data (material, properties, relationships)

In BIM, drawings are generated FROM the model — not the other way around.
```

### Coordination vs Design

```
Design:       Creating the structural/architectural/MEP model
Coordination: Checking that all disciplines fit together without conflicts
Clash detection is part of coordination, not design.
```

---

## Tool Roadmap

### Essential

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Revit | `[MUST LEARN]` | L2–L3 | BIM authoring, modeling |
| Navisworks | `[MUST LEARN]` | L2 | Clash detection, 4D simulation |
| AutoCAD | `[MUST LEARN]` | L2 | 2D extraction, legacy files |

### Important

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Civil 3D | `[HIGH ROI]` | L2 | Infrastructure BIM |
| Excel | `[MUST LEARN]` | L3 | Quantity takeoff, cost analysis |
| IFC / Open Standards | `[HIGH ROI]` | L1–L2 | Model interoperability |

### Advanced

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Dynamo (Revit) | `[SPECIALIZED]` | L2 | Visual programming for Revit automation |
| BIM 360 / Autodesk Construction Cloud | `[SPECIALIZED]` | L1 | Cloud-based BIM collaboration |
| Solibri | `[SPECIALIZED]` | L2 | Model checking, rule-based validation |

---

## Revit Core Skills

```
Beginner:
    → Interface, project browser, properties
    → Wall, door, window, floor, roof
    → Levels, grids, reference planes
    → Basic views (plan, section, 3D)

Intermediate:
    → Families (loadable, system)
    → Materials and textures
    → Schedules and quantities
    → Annotations and dimensions
    → Sheets and printing

Advanced:
    → Worksharing (central model)
    → Phases and design options
    → Analytical models (structural)
    → Dynamo for automation
    → Coordination with other disciplines
```

---

## Navisworks Workflow

```
Step 1: Append — Import models from Revit/AutoCAD/other disciplines
Step 2: Aggregate — Combine into a single federated model
Step 3: Clash Detection — Set up clash tests (structural vs MEP, etc.)
Step 4: Review — Analyze clashes, assign to team members
Step 5: 4D — Link schedule to model for construction simulation
Step 6: Publish — Create flythroughs, reports, clash reports
```

---

## Interoperability

| Format | Use Case | Notes |
|:-------|:---------|:------|
| .RVT | Revit native | Full data, not interoperable |
| .IFC | Open standard | Industry Foundation Classes |
| .DWG | AutoCAD | 2D/3D geometry, limited data |
| .NWC | Navisworks cache | For aggregation |
| .FBX | Exchange format | 3D geometry for visualization |
| .gbXML | Energy analysis | Building geometry for energy models |

---

## Interview Questions

### Basic (101)
- What is BIM? How is it different from CAD?
- What is the difference between 3D, 4D, and 5D BIM?
- What is clash detection?

### Practical (201)
- Walk me through a BIM coordination workflow.
- How do you set up a 4D simulation in Navisworks?
- How do you extract quantities from a Revit model?

### Technical (301)
- What is IFC? Why is it important?
- How do you handle design changes in a BIM workflow?
- What are the challenges of BIM adoption in construction?

### Project Defense
- Show me a BIM model you created.
- How did you coordinate between disciplines?
- What clash issues did you find and resolve?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Construction Technology | [`construction/`](../construction/construction-tech.md) |
| Structural Technology | [`structural/`](../structural/structural-tech.md) |
| CAD → BIM → Digital | [`automation/`](../automation/automation.md) |

---

*See also: [`construction-tech.md`](../construction/construction-tech.md) for scheduling and project management tools.*

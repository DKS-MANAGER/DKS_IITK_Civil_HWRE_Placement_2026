# BIM Engineer — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core concepts, workflows, and quick-fire Q&A for BIM interviews.

---

## Framework 1: BIM Fundamentals

### BIM vs CAD
| Aspect | CAD (AutoCAD) | BIM (Revit) |
|:-------|:-------------|:------------|
| Output | 2D drawings | 3D model with data |
| Data | Lines, arcs, text | Walls, beams, columns with properties |
| Changes | Manual update across sheets | Auto-update across all views |
| Quantity takeoff | Manual measurement | Automated from model |
| Collaboration | File-based | Workshared model |

### BIM Dimensions
```
3D = Geometry
4D = Time (schedule, sequencing)
5D = Cost (quantity takeoff, estimation)
6D = Sustainability (energy analysis)
7D = Facility Management (O&M)
```

### LOD (Level of Development)
```
LOD 100 = Conceptual (massing)
LOD 200 = Approximate geometry (generic elements)
LOD 300 = Precise geometry (specific size/shape)
LOD 350 = Coordination (connections, interfaces)
LOD 400 = Fabrication (shop-ready)
LOD 500 = As-built
```

### Key Principle
```
Drawings are generated FROM the model — not the other way around.
```

---

## Framework 2: Revit & BIM Authoring

### Revit Core Skills
```
Beginner:    Interface, walls, doors, windows, floors, roofs, levels, grids
Intermediate: Families, materials, schedules, annotations, sheets
Advanced:    Worksharing, phases, design options, Dynamo, coordination
```

### Families
| Type | Description |
|:-----|:------------|
| **System** | Built-in (walls, floors, roofs, ducts) |
| **Loadable** | External files (.rfa) — doors, windows, furniture |
| **In-place** | Modeled directly in the project |

### Quantity Takeoff Workflow
```
Model with correct types/parameters
→ Create schedule (by category, by level)
→ Export to Excel
→ Link to cost database (5D)
```

### Worksharing
```
Central Model (server) ←→ Local Models (team)
Sync regularly → avoid conflicts → use worksets
```

---

## Framework 3: Coordination & Clash Detection

### Navisworks Workflow
```
1. Append — Import models from Revit/AutoCAD/other disciplines
2. Aggregate — Combine into a single federated model
3. Clash Detection — Set up clash tests (structural vs MEP, etc.)
4. Review — Analyze clashes, assign to team members
5. 4D — Link schedule to model for construction simulation
6. Publish — Create flythroughs, reports, clash reports
```

### Clash Types
| Type | Description |
|:-----|:------------|
| **Hard clash** | Physical overlap of elements |
| **Soft clash** | Clearance/space violation |
| **Workflow clash** | Sequencing/temporal conflict |

### Clash Management
```
Set rules + tolerances → Run test → Prioritize (severity, location)
→ Assign owners → Track closure rate → Re-run until clash-free
```

### 4D/5D
```
4D: Model + Schedule = Construction sequencing simulation
5D: Model + Cost = Automated quantity takeoff and estimation
```

---

## Framework 4: Standards & Interoperability

### File Formats
| Format | Use Case |
|:-------|:---------|
| .RVT | Revit native |
| .IFC | Open standard (Industry Foundation Classes) |
| .DWG | AutoCAD |
| .NWC | Navisworks cache |
| .FBX | 3D visualization exchange |
| .gbXML | Energy analysis |

### Common Data Environment (CDE)
```
WIP       = Working models (discipline-level)
Shared    = Approved models for coordination
Published = Design-freeze for construction
Archived  = As-built records
```

### ISO 19650
```
International standard for BIM information management
Covers: roles, processes, information requirements, CDE
```

### BIM Execution Plan (BEP)
```
Goals → BIM uses → Standards → LOD → Naming conventions
→ File formats → Deliverables → Milestones
```

### BIM Roles
```
BIM Manager    = Strategy, standards, BEP, overall coordination
BIM Coordinator = Day-to-day model coordination, clash detection
BIM Modeler    = Creates and maintains discipline models
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is BIM?**
A: Building Information Modeling — a process for creating and managing digital representations of physical structures. It's data-rich, collaborative, and generates drawings from the model.

**Q2: How is BIM different from CAD?**
A: CAD produces 2D drawings with lines and text. BIM produces 3D models with embedded data (materials, properties, relationships) where changes auto-update across all views and quantities are extracted automatically.

**Q3: What is clash detection?**
A: The automated process of finding geometric conflicts between discipline models (structural vs MEP vs architectural) in a federated model, typically using Navisworks. It prevents rework by catching conflicts before construction.

**Q4: What is LOD?**
A: Level of Development — the degree to which model elements are developed. Ranges from LOD 100 (conceptual) to LOD 500 (as-built). It defines what can be relied upon at each stage.

**Q5: What is IFC?**
A: Industry Foundation Classes — an open, vendor-neutral data format for exchanging BIM models between different software. It's the key to interoperability.

**Q6: What is 4D BIM?**
A: Linking the 3D model to the construction schedule (time) to create sequencing simulations. It helps visualize construction phasing, optimize logistics, and communicate the plan.

**Q7: What is a federated model?**
A: A combined model created by aggregating discipline models (structural, architectural, MEP) into one coordinated model, typically in Navisworks, for clash detection and review.

**Q8: What is a Common Data Environment?**
A: A shared repository with four statuses — WIP, Shared, Published, Archived — that manages information flow between stakeholders in a controlled way.

**Q9: How does BIM reduce cost?**
A: Clash detection prevents rework (30-50% reduction), automated quantity takeoff improves estimate accuracy, and 4D planning reduces schedule delays. These typically outweigh the BIM investment.

**Q10: How does a civil engineering background help in BIM?**
A: Understanding of structural systems, construction sequencing, and design intent — so I can model correctly, coordinate meaningfully, and catch issues that a pure modeler would miss.

---

## Last-Minute Checklist

### Before Any BIM Interview
- [ ] One BIM project you can defend (or a detailed hypothetical)
- [ ] Know the Navisworks workflow cold
- [ ] Be ready to explain BIM's business value with numbers
- [ ] Your "Why BIM?" answer (link to civil engineering + digital)

### Must-Know Concepts
- [ ] BIM vs CAD
- [ ] 3D-7D dimensions
- [ ] LOD 100-500
- [ ] IFC, ISO 19650, CDE
- [ ] Clash types (hard, soft, workflow)
- [ ] Navisworks 6-step workflow

### Behavioral Prep
- [ ] "Tell me about a time you coordinated a team" (STAR)
- [ ] "Describe a time you caught an error before it became a problem" (STAR)
- [ ] "How do you handle a disagreement about design?" (STAR)
- [ ] "Tell me about a time you learned a new tool quickly" (STAR)

---

## Cross-Links

**BIM:**
→ [BIM Technology Roadmap](bim-tech.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Construction Technology](../construction/construction-tech.md) — Construction tools
→ [Structural Technology](../structural/structural-tech.md) — Structural modeling
→ [Infrastructure/PM](../../core/infrastructure/infrastructure-engineering-management.md) — PM context

---

*Last updated: 2026-09-04*
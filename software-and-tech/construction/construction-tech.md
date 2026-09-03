# 🏗️ Construction / Project Management Technology Roadmap

> **Branch:** Construction Management / Project Management
> **Tools mapped to estimation, scheduling, BIM, project controls, quantity takeoff, cost management, and documentation.**

---

## Decision Tree

```
Construction / PM student → what tools?

1. MS Project or Primavera  → Scheduling (MUST)
2. Excel                    → Estimation, cost analysis (MUST)
3. AutoCAD                  → Drawing reading, quantity takeoff (MUST)
4. Revit                    → BIM, 4D scheduling (HIGH ROI)
5. Power BI                 → Project dashboards (HIGH ROI)
6. Navisworks               → 4D simulation, clash detection (ROLE DEPENDENT)
7. Python                   → Data analysis, automation (ROLE DEPENDENT)
```

---

## Tool → Role Mapping

### Construction Engineer

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| AutoCAD | `[MUST LEARN]` | L2–L3 | Drawing reading, basic drafting |
| Excel | `[MUST LEARN]` | L3 | Estimation, cost sheets, data analysis |
| MS Project | `[MUST LEARN]` | L2–L3 | Project scheduling, Gantt charts |
| Primavera P6 | `[HIGH ROI]` | L2 | Enterprise project management |
| Power BI | `[HIGH ROI]` | L2 | Project dashboards |

### Planning Engineer

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Primavera P6 | `[MUST LEARN]` | L3 | Critical path, resource loading |
| MS Project | `[MUST LEARN]` | L2–L3 | Alternative scheduling |
| Excel | `[MUST LEARN]` | L3 | Progress tracking, earned value |
| Power BI | `[HIGH ROI]` | L2 | Progress dashboards |

### Project Controls

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Primavera P6 | `[MUST LEARN]` | L3 | Scheduling, earned value |
| Excel | `[MUST LEARN]` | L3 | Cost analysis, forecasting |
| Power BI | `[MUST LEARN]` | L2–L3 | KPI dashboards, reporting |
| Python | `[ROLE DEPENDENT]` | L2 | Data automation |

### BIM Engineer (Construction)

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Revit | `[MUST LEARN]` | L3 | BIM authoring |
| Navisworks | `[MUST LEARN]` | L2–L3 | Clash detection, 4D |
| Civil 3D | `[HIGH ROI]` | L2 | Infrastructure BIM |
| Excel | `[MUST LEARN]` | L3 | Quantity takeoff, cost |

### Quantity Surveyor / Estimation

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | BOQ, cost estimation |
| AutoCAD | `[MUST LEARN]` | L2 | Measurement from drawings |
| Revit | `[HIGH ROI]` | L2 | Automated quantity takeoff |
| CostX / Bluebeam | `[ROLE DEPENDENT]` | L2 | Digital takeoff |

---

## Tool Details

### Primavera P6

| Property | Value |
|:---------|:------|
| **What** | Enterprise project portfolio management |
| **Developer** | Oracle |
| **License** | Commercial (academic available) |
| **Primary use** | Scheduling, resource management, earned value |
| **Learning time to L2** | 15–20 hours |
| **Learning time to L3** | 30–40 hours |
| **Alternative** | MS Project, Asta Powerproject |

### MS Project

| Property | Value |
|:---------|:------|
| **What** | Project scheduling and management |
| **Developer** | Microsoft |
| **License** | Commercial (free for students) |
| **Primary use** | Gantt charts, resource allocation, critical path |
| **Learning time to L2** | 10–15 hours |
| **Learning time to L3** | 20–30 hours |
| **Alternative** | Primavera P6 (enterprise), ProjectLibre (open-source) |

### Power BI

| Property | Value |
|:---------|:------|
| **What** | Business intelligence and dashboarding |
| **Developer** | Microsoft |
| **License** | Free desktop version available |
| **Primary use** | Project KPI dashboards, progress reporting |
| **Learning time to L2** | 10–15 hours |
| **Learning time to L3** | 20–30 hours |
| **Alternative** | Tableau, Excel dashboards |

---

## Typical Construction Technology Workflow

```
Step 1: Design → AutoCAD/Revit drawings received
Step 2: Estimate → Excel/BOQ → cost estimation
Step 3: Schedule → Primavera/MS Project → CPM schedule
Step 4: Execute → Track progress, update schedule
Step 5: Control → Earned value analysis, cost forecasting
Step 6: Report → Power BI dashboards, progress reports
Step 7: Close → As-built documentation, lessons learned
```

---

## Key Concepts for Interviews

```
- CPM (Critical Path Method), Float, Total Float
- EVM (Earned Value Management): EV, AC, PV, SPI, CPI
- BOQ (Bill of Quantities)
- Rate Analysis
- Tenders and procurement
- 4D BIM (schedule + model)
- 5D BIM (cost + model)
```

---

## Interview Questions

### Basic (101)
- What is the critical path method (CPM)?
- Explain the difference between Float and Free Float.
- What is Earned Value Management?

### Practical (201)
- How do you create a CPM schedule in Primavera/MS Project?
- Walk me through an earned value analysis.
- How do you update a construction schedule?

### Technical (301)
- How do you handle schedule compression (crashing vs fast-tracking)?
- Explain the S-curve and how it's used in project monitoring.
- What is the difference between 4D and 5D BIM?

### Project Defense
- Show me a schedule you created. How did you determine activity durations?
- How did you handle delays in your project?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| BIM Technology | [`bim/`](../bim/bim-tech.md) |
| Structural (drafting) | [`structural/`](../structural/structural-tech.md) |
| Python for Engineering | [`programming/python.md`](../programming/python.md) |
| Core Infrastructure | [`core/infrastructure/`](../../core/infrastructure/infrastructure-engineering-management.md) |

---

*See also: [`bim-tech.md`](../bim/bim-tech.md) for BIM-specific workflows, [`branch-roadmaps.md`](../branch-roadmaps.md) for full branch comparison.*

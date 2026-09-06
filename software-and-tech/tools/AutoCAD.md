# 📐 AutoCAD for Civil Engineering

> **Priority:** P0 — Required | **Target Level:** L3 (Project-capable)
> **Time to L2:** 15–20 hrs | **Time to L3:** 30–40 hrs
> **Canonical source.** All branch pages link here.

---

## 1. What It Is

AutoCAD is a **2D computer-aided drafting (CAD)** software by Autodesk. It is the industry-standard tool for producing **technical drawings** — plans, sections, elevations, and details — that communicate how a structure is built.

## 2. Where It Is Used

| Application | Branch | Context |
|:------------|:-------|:--------|
| Structural drawings | Structural | Beam/column/slab details, rebar schedules |
| Construction drawings | Construction | Building plans, sections, site layouts |
| Foundation plans | Geotech | Footing layouts, pile caps |
| Process flow diagrams | Environmental | WTP/STP flow diagrams |
| Road/bridge details | Transportation | Cross-sections, alignment drawings |

## 3. Why Your Target Role Needs It

**Company evidence (from [`company-profiles`](../../prep/company-profiles/)):**

| Company | Role | AutoCAD Level |
|:--------|:-----|:--------------|
| L&T | Civil Engineer | Proficient |
| Godrej Properties | AM — Project Execution | Proficient |
| Thornton Tomasetti | Structural Engineer | Proficient |
| Hilti | Graduate Engineer | Proficient |
| SPECTRUM | Trainee Design Engineer | Proficient |
| ASC Infratech | Trainee Engineer | Proficient |
| BPCL | Management Trainee | Proficient |

> **Key insight:** AutoCAD is the **single most universal software** across all civil companies. It is the "language" of construction drawings.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **AutoCAD (student)** | Autodesk Education Community — free 1-year student license |
| **AutoCAD LT** | Cheaper, 2D only — sufficient for civil drafting |
| **Free alternatives** | DraftSight, BricsCAD, LibreCAD (for practice) |

**Setup checklist:**
- [ ] Set units to **millimeters** (or meters) — `UNITS` command
- [ ] Create a **template** (`.dwt`) with standard layers, text styles, dim styles
- [ ] Set up **model space** (1:1 drawing) and **paper space** (plotting)

---

## 5. Core Interface / Workflow

```
Model Space (draw at 1:1)  →  Paper Space (layout for plotting)
        ↓
Draw geometry → Add dimensions → Add text/annotations → Plot/Print
```

**Key panels:** Ribbon (Home, Insert, Annotate), Command line, Layers panel, Properties palette.

---

## 6. Essential Commands (Civil-Relevant Only)

### Must-Know (L2–L3)

| Command | Shortcut | Purpose |
|:--------|:---------|:--------|
| `LINE` | `L` | Draw straight lines |
| `POLYLINE` | `PL` | Draw connected line/arc segments (single object) |
| `OFFSET` | `O` | Copy parallel — for walls, beams, road edges |
| `TRIM` | `TR` | Trim lines at intersections |
| `EXTEND` | `EX` | Extend lines to boundaries |
| `MIRROR` | `MI` | Mirror symmetrical elements |
| `ARRAY` | `AR` | Repeat elements (columns, rebars) |
| `HATCH` | `H` | Fill sections (concrete, earth) |
| `DIMLINEAR` | `DLI` | Linear dimension |
| `DIMCONTINUE` | `DCO` | Chain dimensions |
| `LAYER` | `LA` | Manage layers |
| `BLOCK` | `B` | Create reusable symbol |
| `INSERT` | `I` | Insert a block |
| `SCALE` | `SC` | Scale objects |
| `MOVE` | `M` | Move objects |
| `COPY` | `CO` | Copy objects |
| `ROTATE` | `RO` | Rotate objects |
| `ZOOM` / `PAN` | `Z` / `P` | Navigate |
| `PLOT` | `CTRL+P` | Print/plot |

### Nice-to-Know

| Command | Purpose |
|:--------|:--------|
| `XREF` | Reference external drawings (architectural base) |
| `DIMSTYLE` | Set dimension standards |
| `TEXT` / `MTEXT` | Single / multi-line text |
| `PEDIT` | Edit polylines (join, curve) |

### What NOT to Waste Time On

```
- 3D modeling in AutoCAD (use Revit/Civil 3D instead)
- Rendering / visualization
- Advanced customization (LISP) unless targeting automation roles
- Every ribbon command — only ~20 commands matter for civil
```

---

## 7. Typical Engineering Workflow

```
Step 1: Set up — units, layers, template
Step 2: Draw base geometry — grid lines, walls, columns (from architectural input)
Step 3: Add structural elements — beams, slabs, footings
Step 4: Annotate — dimensions, levels, notes
Step 5: Detail — rebar details, sections, callouts
Step 6: Plot — paper space layout, scale, print
Step 7: Review — check against standards (IS 456 detailing, drawing conventions)
```

---

## 8. Worked Example — Beam Section Detail

**Task:** Draw a 300×450 mm RCC beam cross-section with reinforcement.

```
1. Set units to mm (UNITS → mm)
2. Create layers: BEAM (continuous), REBAR (continuous), DIM (continuous)
3. Draw the beam outline: RECTANG (0,0) to (300,450)
4. Offset inward 40mm (clear cover) → rebar cage outline
5. Draw main bars: 4 circles Ø20 at corners (CIRCLE, Ø20)
6. Draw stirrups: Ø8 rectangle at 40mm cover
7. Add dimensions: DIMLINEAR for 300 and 450
8. Add text: "300×450 RCC BEAM, M25, Fe415"
9. Hatch the concrete section (ANSI31)
```

**Output:** A dimensioned, annotated beam section ready for a structural drawing set.

---

## 9. Practice Exercises

### Basic
1. Draw a 5000×3000 mm room plan with 230mm walls (use `OFFSET` + `TRIM`)
2. Draw a column grid of 3×3 at 4000mm spacing (use `ARRAY`)
3. Draw a simply supported beam elevation with supports

### Intermediate
4. Draw a complete footing plan with 4 column footings and dimensions
5. Draw a beam-column joint detail with rebar (Ø20 main, Ø8 stirrups)
6. Create a block for a door symbol and insert it 5 times

### Role-Specific (Structural)
7. Draw a complete structural plan of a small building: grid → columns → beams → slab edge
8. Draw a rebar schedule table with bar marks, diameters, lengths, quantities

---

## 10. Mini-Project — Basic Engineering Drawing Set

```
Objective: Produce a structural drawing set for a small RCC building
Input: Architectural plan (or sketch), column layout, beam sizes
Workflow:
    1. Set up template (units, layers, dim styles)
    2. Draw grid lines and column positions
    3. Draw beam layout on grid
    4. Draw slab edge and openings
    5. Add dimensions, levels, notes
    6. Create paper-space layout at 1:100
    7. Plot to PDF
Expected Output: A 2-sheet drawing set (plan + section) in PDF
Interview Questions It Prepares You For:
    - "Walk me through how you produce a structural drawing"
    - "How do you set up layers and why?"
    - "What is the difference between model space and paper space?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Drawing in paper space | Scale issues on plot | Draw 1:1 in model space, plot from paper space |
| No layers | Can't control visibility/plotting | Use layers for every element type |
| Wrong units | Dimensions off by 1000x | Set units before drawing |
| Exploding blocks | Lose block intelligence | Keep blocks intact |
| Not using OFFSET | Slow, inaccurate parallel lines | Use OFFSET for walls/beams |
| Overlapping lines | Messy, hard to edit | TRIM/EXTEND to clean intersections |

---

## 12. Interview Questions

### Basic
- What is the difference between model space and paper space?
- What is a layer and why is it important?
- What is the difference between a line and a polyline?

### Workflow
- Walk me through how you produce a structural drawing.
- How do you set up a drawing template?
- How do you create a block? When would you use one?

### Troubleshooting
- Your drawing won't plot at the right scale. What do you check?
- Lines appear broken when you zoom in. What is the issue?

### Engineering Judgment
- Why did you choose mm units for this drawing?
- How do you ensure your drawing is code-compliant (IS 456 detailing)?

### Follow-up
- What would happen if you drew in meters but plotted in mm?
- How would you handle a design change from the architect?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | 2D CAD drafting |
| **Developer** | Autodesk |
| **License** | Commercial (free for students) |
| **Platform** | Windows, macOS |
| **Difficulty** | Easy to start |
| **Time to L2** | 15–20 hrs |
| **Time to L3** | 30–40 hrs |
| **Primary use** | Structural/construction drawings |
| **Alternative** | DraftSight, BricsCAD |

**Top 5 commands:** `L`, `PL`, `O`, `TR`, `H`

---

## Theory Linkage

```
AutoCAD → Engineering Drawing → IS 962 (drawing conventions)
        → Structural Detailing → IS 456 (rebar detailing)
        → Construction → Drawing interpretation on site
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| L&T | Draw a beam section, read a building plan |
| Godrej | Read structural drawings, identify beams/columns |
| SPECTRUM | Draw beam, slab, column details |
| BPCL | Read industrial structure drawings |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Structural Roadmap | [`structural/structural-tech.md`](../structural/structural-tech.md) |
| Construction Roadmap | [`construction/construction-tech.md`](../construction/construction-tech.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Resume Strategy | [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) |

---

*Canonical source for AutoCAD. Do not duplicate in branch pages.*
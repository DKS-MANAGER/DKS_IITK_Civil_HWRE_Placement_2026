# 🪨 PLAXIS 2D Deep-Dive Tutorial

> **Tool:** PLAXIS 2D (geotechnical finite element method)
> **Level:** L2 → L3 (from first model to a complete excavation + retaining wall analysis)
> **Prerequisite:** [`geotechnical-tech.md`](../geotechnical/geotechnical-tech.md), soil mechanics basics ([`geotechnical.md`](../../core/geotechnical/geotechnical.md))

This is a **hands-on tutorial**, not a feature list. You will build a real geotechnical model end-to-end: a **braced excavation with a retaining wall** in soft clay. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

A **plane-strain excavation model** with:
1. A sheet-pile retaining wall
2. A strut (anchor) at the top
3. A staged construction sequence (excavate → install strut → excavate more)
4. A **phi-c reduction** safety factor calculation

By the end you will understand the full PLAXIS workflow and can discuss it in an interview.

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **PLAXIS 2D (commercial)** | Bentley license (often available via university). Includes PLAXIS Input, Output, and Calculation. |
| **PLAXIS 2D Connect Edition** | Newer interface. Same core workflow. |
| **Trial/Student** | Check with your department or Bentley for academic access. |

> **Interview tip:** Be able to say "I modeled a braced excavation in PLAXIS 2D with staged construction and computed the factor of safety via phi-c reduction." This is a concrete, defensible claim.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| Soil stratigraphy | Borehole logs | Soil layers |
| Soil parameters | Lab tests (triaxial, consolidation) | Material models |
| Water table | Piezometers | Pore pressures |
| Wall geometry | Design drawings | Retaining wall |
| Excavation depth | Design | Staged construction |

---

## 🧱 STEP 1 — Create a New Project

1. Open PLAXIS 2D → **File → New Project**
2. Set the **Project Title** (e.g., "Braced Excavation — Soft Clay")
3. Set the **model dimensions**:
   - **Model:** Plane strain (default for most geotechnical problems)
   - **Units:** kN, m (or your preferred)
4. Set the **model contour** (the extents of your model):
   - Width: e.g., 40 m (enough for the excavation + influence zone)
   - Height: e.g., 20 m (soil depth)
5. Click **OK**

**Why:** The model contour defines the computational domain. It must be large enough that boundary effects don't influence the results near the excavation.

**Check:** The model area appears as a rectangle in the Input program.

---

## 🧱 STEP 2 — Define Soil Layers

1. In the **Soil** mode, use the **borehole** tool to define soil layers
2. Click on the model to place a borehole
3. Define layers from top to bottom:
   - **Layer 1:** Soft clay (0–10 m)
   - **Layer 2:** Dense sand (10–20 m)
4. Set the **water level** (phreatic line) — e.g., at 2 m depth

**Why:** The borehole defines the stratigraphy. The water level sets the initial pore pressure distribution.

**Check:** The soil layers appear as colored bands in the model. The water table is a blue line.

---

## 🧱 STEP 3 — Create Material Sets

1. In the **Material** mode, click **Material Sets** → **Soil**
2. Create a material set for each layer:

**Soft clay (Mohr-Coulomb):**
| Parameter | Value |
|:----------|:------|
| Model | Mohr-Coulomb |
| Drainage type | Undrained (B) |
| γ_unsat | 16 kN/m³ |
| γ_sat | 18 kN/m³ |
| E' (Young's modulus) | 10,000 kPa |
| ν' (Poisson's ratio) | 0.35 |
| c' (cohesion) | 10 kPa |
| φ' (friction angle) | 22° |

**Dense sand (Mohr-Coulomb):**
| Parameter | Value |
|:----------|:------|
| Model | Mohr-Coulomb |
| Drainage type | Drained |
| γ_unsat | 18 kN/m³ |
| γ_sat | 20 kN/m³ |
| E' | 50,000 kPa |
| ν' | 0.30 |
| c' | 1 kPa |
| φ' | 38° |

**Why:** The material model and parameters control the soil behavior. Mohr-Coulomb is the standard first model. Undrained (B) means the clay doesn't drain during loading.

**Check:** Both material sets appear in the material library.

---

## 🧱 STEP 4 — Assign Materials to Layers

1. In the **Soil** mode, select each layer
2. Assign the corresponding material set:
   - Soft clay → "Soft clay (MC)"
   - Dense sand → "Dense sand (MC)"

**Why:** Each layer must reference a material set to define its behavior.

**Check:** The layers show the material name.

---

## 🧱 STEP 5 — Create the Retaining Wall

1. Switch to **Structures** mode
2. Use the **Plate** tool to draw the retaining wall
3. Draw a vertical line at the excavation location (e.g., x = 20 m), from the surface down to the wall toe (e.g., 15 m depth)
4. Create a **plate material set**:
   - **EA** (axial stiffness): e.g., 2.5e6 kN/m (typical sheet pile)
   - **EI** (bending stiffness): e.g., 1.0e5 kN·m²/m
   - **w** (weight): e.g., 2.0 kN/m/m
   - **ν** (Poisson's ratio): 0.15

**Why:** The plate represents the wall. EA and EI control axial and bending behavior.

**Check:** The wall appears as a vertical line at the excavation location.

---

## 🧱 STEP 6 — Create the Strut

1. Use the **Node-to-node anchor** tool
2. Draw a horizontal line from the wall to a fixed point (or use a **fixed-end anchor**)
3. Create an anchor material set:
   - **EA** (axial stiffness): e.g., 1.0e5 kN
   - **spacing** (out-of-plane): 3 m

**Why:** The strut provides lateral support at the top of the wall. The spacing accounts for the 3D spacing of struts in a 2D plane-strain model.

**Check:** The strut appears as a horizontal line at the top of the wall.

---

## 🧱 STEP 7 — Generate the Mesh

1. Switch to **Mesh** mode
2. Click **Generate Mesh**
3. Set the **mesh coarseness**:
   - **Global coarseness:** Medium (default)
   - **Refine** near the wall and excavation (use the **refine** tool to create a local refinement cluster)
4. Click **Generate**

**Why:** The mesh discretizes the model into finite elements. Refinement near the wall captures the high stress gradients there.

**Check:** The mesh appears. It's finer near the wall and excavation.

---

## 🧱 STEP 8 — Set Boundary Conditions

1. In the **Model conditions** mode, check the boundaries:
   - **Bottom:** Fixed (no displacement) — default
   - **Sides:** Normally fixed (vertical free, horizontal fixed) — default
2. Verify the **water level** is set correctly

**Why:** Boundary conditions constrain the model. The default (bottom fixed, sides normally fixed) is correct for most geotechnical problems.

**Check:** The boundary symbols show the correct constraints.

---

## 🧱 STEP 9 — Define Construction Stages

1. Switch to **Staged construction** mode
2. Define the calculation phases:

**Phase 0 — Initial phase:**
- All soil active, wall and strut inactive
- Generates initial stresses (gravity + water)

**Phase 1 — Install wall:**
- Activate the wall (plate)
- Deactivate nothing
- **Calculation type:** Plastic

**Phase 2 — Excavate to 3 m:**
- Deactivate the soil cluster from 0–3 m depth (the excavation)
- **Calculation type:** Plastic

**Phase 3 — Install strut:**
- Activate the strut
- **Calculation type:** Plastic

**Phase 4 — Excavate to 6 m:**
- Deactivate the soil cluster from 3–6 m depth
- **Calculation type:** Plastic

**Phase 5 — Safety factor (phi-c reduction):**
- **Calculation type:** Safety (phi-c reduction)
- This computes the factor of safety

**Why:** Staged construction models the real sequence. Each phase updates the stress state. The phi-c reduction phase reduces soil strength until failure to find the safety factor.

**Check:** Each phase shows the correct active/inactive elements.

---

## 🧮 STEP 10 — Run the Calculation

1. Switch to **Calculation** program
2. Select all phases
3. Click **Calculate**
4. Monitor the **calculation info** for convergence

**Why:** The calculation solves each phase sequentially. Convergence means the solution is stable.

**Check:** Each phase completes with "Calculation finished" and no errors.

---

## 📊 STEP 11 — View Results

1. Switch to **Output** program
2. For each phase, view:
   - **Displacements** (total, horizontal, vertical)
   - **Stresses** (effective stress, pore pressure)
   - **Bending moments** in the wall
3. For the **phi-c reduction** phase, read the **safety factor** (ΣMsf)

**Why:** The output shows how the soil and wall respond. The safety factor tells you if the excavation is stable.

**Check:** The displacement field shows the soil moving toward the excavation. The wall shows bending. The safety factor is > 1.3 (typical minimum for temporary works).

---

## 🔍 STEP 12 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "No convergence" | Too large a load step, or unstable geometry | Reduce load, refine mesh, check material parameters |
| "Negative pore pressure" | Undrained clay with tension | Check drainage type, add tension cut-off |
| "Safety factor < 1" | Unstable excavation | Add more struts, deepen the wall, or improve soil |
| "Mesh too coarse" | Results not converged | Refine mesh near critical areas |

**Why:** These are common issues in real projects. Knowing how to fix them is a strong interview signal.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through a PLAXIS model you built."**
   → "I modeled a braced excavation in soft clay. I defined the soil layers with Mohr-Coulomb, added a sheet-pile wall and strut, generated a refined mesh, ran staged construction phases, and computed the safety factor via phi-c reduction."

2. **"What's the difference between drained and undrained analysis?"**
   → "Drained analysis allows pore pressure to dissipate (for sand). Undrained analysis keeps pore pressure constant (for clay during rapid loading)."

3. **"What is phi-c reduction?"**
   → "It's a method where PLAXIS gradually reduces the soil's strength parameters (c and tan φ) until the model fails. The factor by which they're reduced is the safety factor."

4. **"Why do you refine the mesh near the wall?"**
   → "Because stress and displacement gradients are highest there. A coarse mesh would give inaccurate results."

5. **"What is the difference between Mohr-Coulomb and Hardening Soil?"**
   → "Mohr-Coulomb is linear-elastic perfectly-plastic — simple but doesn't capture soil stiffness variation. Hardening Soil captures the increase in stiffness with stress and is better for settlement and excavation problems."

---

## ✅ Self-Checklist

- [ ] Project created with correct dimensions
- [ ] Soil layers defined via borehole
- [ ] Material sets created (Mohr-Coulomb)
- [ ] Materials assigned to layers
- [ ] Retaining wall (plate) created
- [ ] Strut (anchor) created
- [ ] Mesh generated and refined near wall
- [ ] Boundary conditions verified
- [ ] Construction stages defined
- [ ] Calculation run successfully
- [ ] Results reviewed (displacements, moments, safety factor)

---

## 🔗 Related Resources

- [`geotechnical-tech.md`](../geotechnical/geotechnical-tech.md) — Where PLAXIS fits in the geotechnical stack
- [`geotechnical.md`](../../core/geotechnical/geotechnical.md) — Soil mechanics theory
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions
- [`comparisons/software-comparison.md`](../comparisons/software-comparison.md) — PLAXIS vs FLAC vs GeoStudio

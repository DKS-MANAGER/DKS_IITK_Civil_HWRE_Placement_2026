# ⛰️ GeoStudio SLOPE/W Deep-Dive Tutorial

> **Tool:** GeoStudio SLOPE/W (limit-equilibrium slope stability analysis)
> **Level:** L2 → L3 (from first model to a complete slope stability + factor of safety)
> **Prerequisite:** [`geotechnical-tech.md`](../geotechnical/geotechnical-tech.md), soil mechanics basics ([`geotechnical.md`](../../core/geotechnical/geotechnical.md))

This is a **hands-on tutorial**, not a feature list. You will build a real slope stability model end-to-end: an **embankment slope** with a defined slip surface, using the **Morgenstern-Price** method. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

A **limit-equilibrium slope stability model** with:
1. A soil region (embankment)
2. A water table (pore pressure)
3. A slip surface (circular)
4. A **factor of safety (FoS)** using Morgenstern-Price

By the end you will understand the full SLOPE/W workflow and can discuss it in an interview.

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **GeoStudio (commercial)** | Seequent license (often available via university). Includes SLOPE/W, SEEP/W, etc. |
| **GeoStudio Student** | Check with your department or Seequent for academic access. |

> **Interview tip:** Be able to say "I analyzed an embankment slope in SLOPE/W using the Morgenstern-Price method and computed a factor of safety of X." This is a concrete, defensible claim.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| Slope geometry | Design drawings, survey | Soil region |
| Soil parameters | Lab tests | Strength (c, φ) |
| Water table | Piezometers | Pore pressure |
| Slip surface | Assumed or from analysis | FoS calculation |

---

## 🧱 STEP 1 — Create a New Project

1. Open GeoStudio → **File → New**
2. Choose **SLOPE/W** as the analysis type
3. Set the **Project Title** (e.g., "Embankment Slope Stability")
4. Set **Units** (SI or US)

**Why:** GeoStudio is a suite of analysis tools. SLOPE/W is the limit-equilibrium slope stability module.

**Check:** The SLOPE/W workspace is open.

---

## 🧱 STEP 2 — Define the Soil Region (Slope Geometry)

1. Use the **Draw Regions** tool to draw the embankment cross-section
2. Draw the slope profile (e.g., a 2:1 slope, 10 m high)
3. Define the soil region boundaries

**Why:** The region defines the soil mass being analyzed. The geometry must match the actual slope.

**Check:** The embankment region appears on the canvas.

---

## 🧱 STEP 3 — Create a Soil Material

1. **KeyIn → Materials**
2. Click **Add** to create a soil material
3. Set properties:
   - **Unit weight (γ):** e.g., 18 kN/m³
   - **Cohesion (c'):** e.g., 10 kPa
   - **Friction angle (φ'):** e.g., 25°
   - **Strength model:** Mohr-Coulomb

**Why:** The material defines the soil strength. Mohr-Coulomb uses c' and φ' to compute the shear strength.

**Check:** The material is created.

---

## 🧱 STEP 4 — Assign the Material to the Region

1. Select the soil region
2. Assign the soil material to it

**Why:** The region must reference a material to define its strength.

**Check:** The region shows the material name.

---

## 🧱 STEP 5 — Define the Water Table

1. Use the **Draw Water Table** tool (or define pore pressure)
2. Draw the water table line within the slope
3. Set the **pore pressure** conditions (e.g., hydrostatic below the water table)

**Why:** Pore pressure reduces the effective stress and thus the shear strength. The water table is critical for slope stability.

**Check:** The water table appears as a line.

---

## 🧱 STEP 6 — Define the Slip Surface

1. Use the **Draw Slip Surface** tool
2. Draw a **circular slip surface** through the slope (or use the entry-exit method)
3. Set the slip surface parameters (center, radius)

**Why:** The slip surface is where failure is assumed to occur. SLOPE/W computes the FoS along this surface.

**Check:** The slip surface appears as an arc through the slope.

---

## 🧱 STEP 7 — Set the Analysis Method

1. **KeyIn → Analysis Settings**
2. Choose the **Method of Slices**:
   - **Morgenstern-Price** (most rigorous, satisfies all equilibrium)
   - Bishop (simplified, circular only)
   - Janbu (non-circular)
3. Set the **number of slices** (e.g., 30)

**Why:** The method of slices determines how the FoS is computed. Morgenstern-Price is the most rigorous and widely used.

**Check:** The analysis method is set.

---

## 🧮 STEP 8 — Run the Analysis

1. Click **Solve** (or **Analysis → Solve**)
2. Monitor the **solver** for convergence

**Why:** The solver computes the FoS by iterating on the slice forces.

**Check:** The analysis completes. The FoS is displayed.

---

## 📊 STEP 9 — View Results

1. **Results → Contours** — see the FoS distribution
2. **Results → Slip Surface** — see the critical slip surface
3. Read the **minimum FoS** (the critical value)

**Why:** The FoS tells you if the slope is stable. FoS > 1.3 is typically acceptable for permanent slopes; > 1.5 for critical structures.

**Check:** The minimum FoS is displayed. Note whether it's above the acceptable threshold.

---

## 🔍 STEP 10 — Sensitivity Analysis (Optional)

1. **KeyIn → Sensitivity** — vary a parameter (e.g., φ') over a range
2. Re-run and see how FoS changes

**Why:** Sensitivity analysis shows which parameter most affects stability — useful for design and interview discussion.

**Check:** The FoS vs. parameter plot is generated.

---

## 🔍 STEP 11 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "No convergence" | Slip surface not valid, or too few slices | Adjust slip surface, increase slices |
| "FoS < 1" | Slope unstable | Flatten slope, add drainage, improve soil |
| "Negative pore pressure" | Water table too high | Lower water table, add drainage |
| "Slip surface outside region" | Slip surface not within soil | Redraw slip surface within the region |

**Why:** These are common issues in real projects. Knowing how to fix them is a strong interview signal.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through a SLOPE/W model you built."**
   → "I analyzed an embankment slope in SLOPE/W. I drew the soil region, assigned a Mohr-Coulomb material, defined the water table, drew a circular slip surface, and computed the FoS using the Morgenstern-Price method."

2. **"What is the factor of safety in slope stability?"**
   → "It's the ratio of resisting forces (shear strength) to driving forces (gravity). FoS > 1 means the slope is stable."

3. **"What's the difference between Bishop and Morgenstern-Price?"**
   → "Bishop's simplified method only satisfies moment equilibrium and works for circular surfaces. Morgenstern-Price satisfies both force and moment equilibrium and works for non-circular surfaces."

4. **"How does pore pressure affect slope stability?"**
   → "Pore pressure reduces effective stress, which reduces shear strength, making the slope less stable. Higher water table → lower FoS."

5. **"What is the method of slices?"**
   → "It divides the sliding mass into vertical slices and computes the forces on each slice to find the overall FoS."

---

## ✅ Self-Checklist

- [ ] Project created with SLOPE/W
- [ ] Soil region drawn (embankment)
- [ ] Soil material created (Mohr-Coulomb)
- [ ] Material assigned to region
- [ ] Water table defined
- [ ] Slip surface drawn
- [ ] Analysis method set (Morgenstern-Price)
- [ ] Analysis run successfully
- [ ] FoS reviewed (minimum value)
- [ ] Sensitivity analysis performed (optional)

---

## 🔗 Related Resources

- [`geotechnical-tech.md`](../geotechnical/geotechnical-tech.md) — Where SLOPE/W fits in the geotechnical stack
- [`plaxis-2d-tutorial.md`](plaxis-2d-tutorial.md) — FEM alternative for slope stability
- [`geotechnical.md`](../../core/geotechnical/geotechnical.md) — Soil mechanics theory
- [`comparisons/software-comparison.md`](../comparisons/software-comparison.md) — SLOPE/W vs PLAXIS vs FLAC
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions

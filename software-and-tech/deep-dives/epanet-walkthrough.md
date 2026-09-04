# 🚰 EPANET Deep-Dive Walkthrough

> **Tool:** EPANET (water distribution network modeling)
> **Level:** L2 → L3 (from first model to a complete network + extended period simulation)
> **Prerequisite:** [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md), water supply basics ([`water-supply.md`](../../core/hwre/water_supply/water-supply.md))

This is a **hands-on walkthrough**, not a feature list. You will build a real water distribution model end-to-end: a **small town network** with a reservoir, a pump, pipes, junctions, and demand. Each step explains **what** to do, **why** it matters, and **how to check** you did it correctly.

---

## 🎯 What You Will Build

A **water distribution network** with:
1. A reservoir (source)
2. A pump station
3. A pipe network (junctions, pipes)
4. A demand pattern (24-hour water use)
5. An **extended period simulation** (EPS) to check pressures over a day

By the end you will understand the full EPANET workflow and can discuss it in an interview.

---

## 📦 Before You Start

### Installation

| Option | How |
|:-------|:----|
| **EPANET 2.x** | Free download from USEPA website. Includes a GUI. |
| **EPANET via Python (wntr, epanet-toolkit)** | For automation and resilience analysis. Good for data roles. |

> **Interview tip:** Be able to say "I modeled a water distribution network in EPANET and ran an extended period simulation to check pressure under peak demand." This is a concrete, defensible claim.

### Data You Need

| Data | Source | Used For |
|:-----|:-------|:---------|
| Network layout | Utility maps | Pipes, junctions |
| Pipe diameters/lengths | Utility records | Pipe properties |
| Demand | Billing data, population | Junction demand |
| Source | Reservoir/tank location | Supply |
| Pump characteristics | Pump curves | Pump station |

---

## 🧱 STEP 1 — Create a New Project

1. Open EPANET → **File → New**
2. Set the **Project Title** (e.g., "Small Town Water Network")
3. Set **Hydraulics** options:
   - **Flow units:** LPS (liters per second) or GPM
   - **Headloss formula:** Hazen-Williams (most common)
   - **Demand model:** Demand (constant) or Demand Pattern

**Why:** EPANET solves the hydraulic equations (continuity + energy) to find flows and pressures. The headloss formula and units are set here.

**Check:** The project is created with the correct units.

---

## 🧱 STEP 2 — Create the Reservoir

1. Click the **Reservoir** tool
2. Place the reservoir on the map
3. Set reservoir properties:
   - **Total head** (e.g., 100 m — the water surface elevation)
   - **Head pattern** (optional, if the source varies)

**Why:** The reservoir is the source of water. Its total head drives the flow through the network.

**Check:** The reservoir appears on the map.

---

## 🧱 STEP 3 — Create the Pump

1. Click the **Pump** tool
2. Draw the pump from the reservoir to the first junction
3. Set pump properties:
   - **Pump curve** (head vs. flow relationship)
   - Create a pump curve: **Project → Pump Curves**
     - Add points: (flow, head) pairs from the manufacturer's curve

**Why:** The pump adds energy to lift water from the reservoir into the network. The pump curve defines its performance.

**Check:** The pump appears between the reservoir and the network.

---

## 🧱 STEP 4 — Create Junctions

1. Click the **Junction** tool
2. Place junctions at pipe connections and demand points
3. Set junction properties:
   - **Elevation** (ground elevation)
   - **Base demand** (average water demand, e.g., 5 LPS)
   - **Demand pattern** (optional, for time-varying demand)

**Why:** Junctions are where pipes connect and where water is withdrawn (demand).

**Check:** Junctions appear on the map with correct elevations and demands.

---

## 🧱 STEP 5 — Create Pipes

1. Click the **Pipe** tool
2. Draw pipes connecting junctions
3. Set pipe properties:
   - **Length** (auto-computed from map)
   - **Diameter** (e.g., 300 mm)
   - **Roughness** (Hazen-Williams C, e.g., 130 for new cast iron)
   - **Minor loss coefficient** (for fittings, optional)

**Why:** Pipes carry water. The diameter and roughness determine the headloss and capacity.

**Check:** The pipes connect the junctions into a network.

---

## 🧱 STEP 6 — Create a Demand Pattern

1. **Project → Patterns**
2. Click **Add** to create a demand pattern
3. Add **multipliers** for each hour (24 values):
   - Night (0–6): 0.3–0.5 (low demand)
   - Morning peak (7–9): 1.3–1.5
   - Midday: 1.0
   - Evening peak (18–21): 1.4–1.6
   - Night: back to 0.3

**Why:** The demand pattern captures how water use varies over the day. This is essential for an extended period simulation.

**Check:** The pattern has 24 multipliers.

---

## 🧱 STEP 7 — Assign the Pattern to Junctions

1. Select each junction
2. Set the **Demand pattern** to the pattern you created

**Why:** Assigning the pattern makes the junction demand vary over time.

**Check:** Junctions reference the demand pattern.

---

## 🧱 STEP 8 — Set Simulation Options

1. **Project → Analysis Options**
2. Set:
   - **Duration:** 24 hours (extended period simulation)
   - **Hydraulic time step:** 1 hour
   - **Pattern time step:** 1 hour
   - **Start time:** 0:00

**Why:** The extended period simulation runs the network over 24 hours, showing how pressures and flows change with demand.

**Check:** The simulation duration is 24 hours.

---

## 🧮 STEP 9 — Run the Simulation

1. Click **Run** (or **Project → Run Analysis**)
2. Monitor the **status report** for:
   - **Errors** (e.g., "negative pressure", "pump cannot deliver")
   - **Warnings** (e.g., "low pressure")

**Why:** The status report tells you if the network is hydraulically feasible.

**Check:** No critical errors. Note any low-pressure warnings.

---

## 📊 STEP 10 — View Results

1. **View → Map** — color-code by pressure or flow
2. **View → Time Series** — see pressure/flow at a junction over 24 hours
3. **View → Table** — see junction pressure, pipe flow, etc.

**Why:** Results show how the network performs under varying demand.

**Check:** Pressures are within acceptable range (e.g., 20–80 m). Note the minimum pressure at peak demand.

---

## 🔍 STEP 11 — Troubleshoot Common Errors

| Error | Cause | Fix |
|:------|:------|:----|
| "Negative pressure" | Pipe too small, or demand too high | Increase pipe diameter, add a pump/boost |
| "Pump cannot deliver" | Pump curve doesn't match demand | Adjust pump curve, add a second pump |
| "Low pressure at peak" | Network undersized | Increase pipe diameters, add storage |
| "Continuity error" | Network not closed | Check all pipes are connected |

**Why:** These are common issues in real projects. Knowing how to fix them is a strong interview signal.

---

## 🧠 Interview Questions You Can Now Answer

1. **"Walk me through an EPANET model you built."**
   → "I modeled a small town water network with a reservoir, pump, pipes, and junctions. I set demands with a 24-hour pattern, ran an extended period simulation, and checked pressures under peak demand."

2. **"What is an extended period simulation?"**
   → "It's running the network over a period (e.g., 24 hours) with time-varying demand, to see how pressures and flows change over time."

3. **"What is the Hazen-Williams equation?"**
   → "It's an empirical formula relating headloss to flow, pipe diameter, and roughness. It's commonly used for water distribution networks."

4. **"How do you size a pipe in EPANET?"**
   → "I start with an assumed diameter, run the model, and check if pressures are within range. If pressure is too low, I increase the diameter."

5. **"What is a demand pattern?"**
   → "It's a set of multipliers that scale the base demand at each hour, capturing how water use varies over the day."

---

## ✅ Self-Checklist

- [ ] Project created with correct units
- [ ] Reservoir created with total head
- [ ] Pump created with pump curve
- [ ] Junctions created with elevation and demand
- [ ] Pipes connected the network
- [ ] Demand pattern created (24 hours)
- [ ] Pattern assigned to junctions
- [ ] Simulation options set (24-hour EPS)
- [ ] Simulation run without critical errors
- [ ] Results reviewed (pressure, flow)
- [ ] Network verified under peak demand

---

## 🔗 Related Resources

- [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md) — Where EPANET fits in the HWRE stack
- [`water-supply.md`](../../core/hwre/water_supply/water-supply.md) — Water supply theory
- [`groundwater.md`](../../core/hwre/water_supply/groundwater.md) — Source water
- [`software-interview-questions.md`](../software-interview-questions.md) — More tool questions

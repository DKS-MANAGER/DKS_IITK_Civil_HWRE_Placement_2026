# Consulting Presentation Frameworks & Executive Dashboard Design

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Focus:** Case Interview Whiteboarding, Client Deck Structuring, Executive UX

---

## 1. The 4-Slide Executive Consulting Deck Template

When presenting an analytics case in a business interview or client boardroom, use this 4-slide structure:

```
 ┌───────────────────────────────────────┬───────────────────────────────────────┐
 │ Slide 1: Executive Context & Challenge│ Slide 2: Root-Cause & Analytical Proof│
 │ • Current financial baseline          │ • Diagnostic data analysis            │
 │ • The commercial problem ($ at risk)  │ • Feature correlation & drivers       │
 │ • Key operational constraints         │ • Baseline heuristic vs ML lift       │
 ├───────────────────────────────────────┼───────────────────────────────────────┤
 │ Slide 3: The Prescriptive Solution    │ Slide 4: Roadmap & EBITDA Realization │
 │ • Architecture & modeling engine      │ • 12-month rollout timeline (Pilots)  │
 │ • Explainability & Frontline UX       │ • Net financial payoff matrix (ROI)   │
 │ • Operational safeguards & guardrails │ • Change management & adoption KPI    │
 └───────────────────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Whiteboarding Strategy for Tredence Case Interviews

During the Technical/Case round at Tredence, interviewers present unstructured scenarios (e.g., *"Our retail client has high logistics costs. How would you solve this?"*).

### The 6-Step Whiteboard Protocol:
1. **Clarify & Scope (2 minutes):**
   - Confirm business objective: *"Are we seeking to minimize transportation fuel costs, reduce warehouse dwell time, or cut missed delivery penalties?"*
   - Define geography, fleet type, and time scale.
2. **Deconstruct the Value Driver Tree (3 minutes):**
   - Draw a mathematical breakdown:
     $$\text{Total Logistics Cost} = (\text{Fuel Cost}) + (\text{Labor Cost}) + (\text{Depreciation}) + (\text{SLA Penalties})$$
     $$\text{Fuel Cost} = \text{Total Distance Driven} \times \text{Fuel Burn Rate per Km} \times \text{Fuel Price}$$
3. **Data Hypothesis & Signals (3 minutes):**
   - Map available datasets: GPS telemetry, route stops, delivery time windows, traffic history.
4. **Analytical Engine Formulation (5 minutes):**
   - Formulate as a two-stage system: (Stage 1) Machine Learning ETA predictor + (Stage 2) Vehicle Routing Problem with Time Windows (VRPTW) optimization.
5. **Operationalize the Last-Mile (3 minutes):**
   - Describe the driver tablet interface, dynamic re-routing logic, and dispatcher console.
6. **Quantify Risks & ROI (2 minutes):**
   - Project $12\%$ fuel savings ($\$3.4\text{M}$ net benefit) with safeguards for driver shift limit regulations.

---

## 3. Executive Dashboard UX Architecture

Dashboards fail when they act as raw data dumps. An executive dashboard must drive immediate operational action.

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      EXECUTIVE DECISION COCKPIT                        │
 ├────────────────────────────────┬───────────────────────────────────────┤
 │ Tier 1: Actionable KPI Cards   │ Metric: On-Shelf Availability (OSA)   │
 │ • Current: 93.4%               │ • Trend: ▼ -1.2% (vs 7-day target)    │
 │ • Net EBITDA Impact at Risk:   │ • Immediate Interventions Needed: 14  │
 ├────────────────────────────────┴───────────────────────────────────────┤
 │ Tier 2: Priority Action Queue (Sorted by Financial Value at Risk)      │
 │ [1] Store #204 - Aisle 3 (Beverages): $1,400/day risk -> [DISPATCH BOT]│
 │ [2] Store #108 - Aisle 7 (Personal Care): $950/day risk -> [ALERT TEAM]│
 ├────────────────────────────────────────────────────────────────────────┤
 │ Tier 3: Diagnostic Root-Cause (TreeSHAP Insights)                      │
 │ Driver: "Late distributor delivery cross-docked at 04:30 AM"           │
 └────────────────────────────────────────────────────────────────────────┘
```

### Design Principles:
1. **The 5-Second Rule:** An executive must understand overall health within 5 seconds of opening the screen.
2. **Action-Oriented Queue:** Replace passive charts with an active "Priority Action List" ranked by dollar impact.
3. **Drill-Down Transparency:** Allow one-click drill-down from enterprise aggregate down to regional depot, store, and SKU level with full reason codes.

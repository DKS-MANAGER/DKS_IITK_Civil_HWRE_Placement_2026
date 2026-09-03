# Project Discussion Framework

## Overview

The project discussion is often the most important part of technical interviews for civil/HWRE roles. It's your chance to demonstrate technical depth, problem-solving ability, and communication skills. A well-structured project discussion can compensate for weaker areas elsewhere.

---

## 🎯 The 5-Minute Project Pitch Structure

### Time Allocation (Total: 5 minutes)

| Section | Time | Content |
|---------|------|---------|
| **Problem Statement** | 45 sec | What problem? Why important? Real-world context |
| **Methodology** | 2 min | Your approach, YOUR contribution, key decisions |
| **Results** | 1 min | Quantified outcomes, validation, comparison |
| **Challenges & Solutions** | 45 sec | Technical obstacles, how you overcame them |
| **Learnings & Future Work** | 30 sec | What you'd do differently, extensions |

---

## 📋 Project Discussion Template

### For Each Project, Prepare:

```
PROJECT: [Title]
DURATION: [Start - End] | ROLE: [Your specific role]
TEAM SIZE: [Number] | TOOLS: [OpenFOAM, Python, MATLAB, etc.]

PROBLEM STATEMENT (2-3 sentences):
- What engineering problem?
- Why does it matter? (safety, cost, environment, efficiency)
- What was the gap in existing knowledge/practice?

YOUR CONTRIBUTION (3-4 bullet points - BE SPECIFIC):
- What did YOU personally do? (not "we did")
- What technical decisions did YOU make?
- What code/scripts/models did YOU build?

METHODOLOGY (key technical choices):
- Governing equations / physics modeled
- Numerical method / solver / turbulence model
- Mesh strategy / validation approach
- Why these choices? (trade-offs considered)

KEY RESULTS (QUANTIFIED):
- Accuracy: "Validated against [experiment] within X% error"
- Performance: "Reduced computation time from X to Y"
- Insight: "Discovered that [parameter] has [effect]"
- Output: "Published in [venue] / Presented at [venue]"

CHALLENGES & SOLUTIONS (2-3):
| Challenge | Your Solution | Outcome |
|-----------|---------------|---------|
| [Technical obstacle] | [What you did] | [Result] |

LEARNINGS & FUTURE WORK:
- What would you do differently?
- What's the next research step?
- How does this apply to industry?
```

---

## 🎯 5 Sample Project Pitches

### Pitch 1: CFD Bridge Pier Scour (M.Tech Thesis)
**Problem:** Bridge pier scour causes 60% of bridge failures in India. Existing empirical formulas (HEC-18) have ±30% uncertainty. Need physics-based prediction.

**My Contribution:**
- Built 2D OpenFOAM case with SedFoam (Eulerian two-phase, k-ω SST)
- Designed mesh independence study using Grid Convergence Index (3 mesh levels)
- Validated against Mao (1986) experimental data — achieved 7% error in scour depth
- Automated parameter sweeps (50+ runs) with Python for turbulence model sensitivity

**Methodology:** SedFoam solver, k-ω SST turbulence, Eulerian two-phase flow, Exner equation for bed evolution. Chose SST over k-ε for adverse pressure gradient near pier.

**Results:** Scour depth prediction within 7% of experimental data. Identified that k-ε underpredicts separation by 25%. Published at [Conference].

**Challenges:**
| Challenge | Solution | Outcome |
|-----------|------------|---------|
| Simulation divergence at 500 steps | Diagnosed y+ > 300, refined boundary layer mesh to y+ ≈ 1 | Converged in 3 days |
| High computational cost (20 hrs/run) | Used adaptive time stepping, reduced domain with symmetry | 40% time reduction |

**Learnings:** Mesh quality > turbulence model choice. Would add LES comparison if time permitted. Directly applicable to bridge design consulting.

---

### Pitch 2: Pipeline Scour CFD Validation (B.Tech Project)
**Problem:** Subsea pipeline scour threatens offshore infrastructure. Need reliable CFD tool for design.

**My Contribution:**
- Set up 2D pipeline scour case in OpenFOAM with sedInterFoam
- Performed mesh sensitivity study (4 mesh levels, GCI analysis)
- Compared k-ε, k-ω, SST turbulence models against Sumer et al. (1992) data
- Built Python automation for 30+ simulation runs and post-processing

**Methodology:** sedInterFoam (VOF + sediment), k-ω SST selected based on literature. Structured mesh with boundary layer refinement.

**Results:** SST matched equilibrium scour depth within 10%. k-ε overpredicted by 35%. Automation reduced manual effort from 2 weeks to 2 days.

**Challenges:**
| Challenge | Solution | Outcome |
|-----------|------------|---------|
| VOF interface smearing | Used compressive interface scheme, refined interface region | Sharp interface maintained |
| Long simulation times | Used symmetry boundary, parallel runs on HPC | 50% wall-time reduction |

**Learnings:** VOF requires careful interface treatment. Would explore sedFoam for sediment-laden flows.

---

### Pitch 3: Flood Routing Model for River Basin (Internship)
**Problem:** Real-time flood forecasting needed for reservoir operation. Existing Muskingum model had 25% peak error.

**My Contribution:**
- Implemented Muskingum-Cunge method in Python with variable parameters
- Calibrated K and X using historical flood events (10 events, 5 years data)
- Built web dashboard for real-time forecasting (Streamlit + Plotly)
- Integrated with existing SCADA data pipeline

**Methodology:** Muskingum-Cunge (physically based K, X from channel geometry). Optimization with SciPy for parameter calibration.

**Results:** Peak flow error reduced from 25% to 8%. Forecast lead time: 6 hours. Dashboard adopted by [Organization] for monsoon 2024.

**Challenges:**
| Challenge | Solution | Outcome |
|-----------|------------|---------|
| Noisy SCADA data | Implemented Kalman filter for data smoothing | Clean input for routing |
| Parameter non-uniqueness | Used multi-objective optimization (peak + volume) | Robust parameters |

**Learnings:** Data quality > model complexity. Would add ensemble forecasting for uncertainty quantification.

---

### Pitch 4: Water Distribution Network Optimization (Course Project)
**Problem:** Municipal water network had 35% non-revenue water. Need optimal pipe sizing and pump scheduling.

**My Contribution:**
- Modeled network in EPANET (500 nodes, 800 pipes)
- Formulated optimization: minimize cost (pipe + energy) subject to pressure constraints
- Used Genetic Algorithm (DEAP library) for pipe sizing, Linear Programming for pump scheduling
- Achieved 22% cost reduction vs existing design

**Methodology:** EPANET for hydraulics, GA for discrete pipe sizing, LP for pump scheduling. Multi-objective: cost vs reliability.

**Results:** 22% capex reduction, 15% energy savings. Pressure constraints satisfied at all nodes. Presented at [Symposium].

**Challenges:**
| Challenge | Solution | Outcome |
|-----------|------------|---------|
| GA convergence slow | Used elitism, adaptive mutation, parallel evaluation | 5x faster convergence |
| Pressure violations at peak | Added penalty function, constraint handling | 100% constraint satisfaction |

**Learnings:** Metaheuristics need careful tuning. Would explore surrogate modeling for larger networks.

---

### Pitch 5: Groundwater Contamination Transport (Research Assistant)
**Problem:** Industrial contaminant plume threatening drinking water wells. Need remediation design.

**My Contribution:**
- Built MODFLOW-MT3DMS model (3 layers, 100×100 grid, 10-year simulation)
- Calibrated hydraulic conductivity using PEST (15 observation wells)
- Simulated 3 remediation scenarios: pump-and-treat, permeable reactive barrier, monitored natural attenuation
- Recommended PRB + targeted pump-and-treat (lowest cost, 90% mass removal in 5 years)

**Methodology:** MODFLOW 6 for flow, MT3DMS for transport. PEST for calibration. Scenario comparison with cost-effectiveness metric.

**Results:** PRB + targeted pumping: ₹2.3 Cr vs ₹5.1 Cr for full pump-and-treat. 90% mass removal in 5 years. Report submitted to [State Pollution Control Board].

**Challenges:**
| Challenge | Solution | Outcome |
|-----------|------------|---------|
| Parameter uncertainty | Monte Carlo sensitivity analysis (1000 runs) | Quantified prediction uncertainty |
| Long simulation times | Used MODFLOW 6 with Newton solver, parallel | 80% time reduction |

**Learnings:** Uncertainty quantification critical for decision-making. Would add stochastic optimization.

---

## 🎤 Common Follow-up Questions & Answers

### Technical Depth
**Q: "Why did you choose k-ω SST over k-ε?"**
**A:** "For bridge pier scour, we have adverse pressure gradient and flow separation near the pier. k-ε with wall functions performs poorly in separation. SST blends k-ω near wall (accurate separation prediction) with k-ε in free stream. Literature (Menter 1994, Wilcox 2006) and our validation confirmed SST predicts separation point within 10% vs 30% error for k-ε."

**Q: "How did you ensure mesh independence?"**
**A:** "Three mesh levels: coarse (50k cells), medium (200k), fine (800k). Computed Grid Convergence Index (GCI) for scour depth. GCI between medium-fine was 1.2% (< 5% threshold). Used medium mesh for production runs. Also monitored y+ < 5 for low-Re SST."

**Q: "What if your validation data had uncertainty?"**
**A:** "Experimental data typically has ±5% uncertainty. We propagated this through our error analysis. Our 7% CFD error is within combined uncertainty. We also did sensitivity analysis on experimental boundary conditions."

### Problem-Solving
**Q: "What would you do differently?"**
**A:** "Three things: (1) Run LES for one case to benchmark RANS turbulence model. (2) Test sedExnerFoam with ALE mesh motion for moving bed morphology. (3) Add uncertainty quantification with polynomial chaos expansion for input parameters."

**Q: "How did you handle the mesh generation bottleneck?"**
**A:** "Built Python automation for snappyHexMesh dictionary generation. Parameterized key inputs (refinement levels, layer counts, expansion ratios). Reduced mesh setup from 2 days to 2 hours. Also created mesh quality checklist (skewness < 0.7, non-orthogonality < 70°, y+ compliance)."

### Application to Role
**Q: "How does this apply to our work at [Company]?"**
**A:** "Your [project type - e.g., bridge design/flood modeling] involves similar physics: flow-structure interaction, sediment transport, turbulence modeling. My experience with OpenFOAM validation, mesh sensitivity, and automation directly transfers. I can hit the ground running on [specific project type]."

---

## 📝 Project Discussion Checklist

### Before Interview
- [ ] Write 150-word summary for each project
- [ ] Prepare 3 quantified results per project
- [ ] List 3 challenges + solutions per project
- [ ] Practice 5-min pitch with timer
- [ ] Record and review for filler words, pace
- [ ] Prepare answers to 10 common follow-ups
- [ ] Research company projects to connect your work

### During Discussion
- [ ] Start with problem significance (hook)
- [ ] Use "I" not "we" for your contributions
- [ ] Quantify everything: %, hours saved, error reduction
- [ ] Draw diagrams if helpful (virtual whiteboard)
- [ ] Admit limitations honestly
- [ ] Connect to company's work

### Red Flags to Avoid
- ❌ "We did..." without clarifying your role
- ❌ Vague results: "good agreement" → "7% error"
- ❌ Blaming team members for challenges
- ❌ Can't explain why you chose method X over Y
- ❌ No quantified results
- ❌ Reading from slides/notes

---

## 🎯 Practice Routine

| Day | Activity |
|-----|----------|
| Mon | Write 150-word summaries for 3 projects |
| Tue | Practice Pitch 1 (5 min, timed, recorded) |
| Wed | Practice Pitch 2 (5 min, timed, recorded) |
| Thu | Practice Pitch 3 (5 min, timed, recorded) |
| Fri | Answer 10 follow-up questions aloud |
| Sat | Full mock with peer (15 min project + 10 min Q&A) |
| Sun | Review recordings, refine weak areas |

---

## 📚 References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [interview-handbook-2026](https://github.com/DKS-MANAGER/interview-handbook-2026)
* [`../mock_questions/mock-interview-questions.md`](../mock_questions/mock-interview-questions.md) — 50 mock questions
* [`../../prep/behavioral/behavioral-interview-guide.md`](../../prep/behavioral/behavioral-interview-guide.md) — STAR framework

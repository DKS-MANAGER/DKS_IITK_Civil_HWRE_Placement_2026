# Project Defense Guide — Universal + CFD-Specific

> **How to use:** Before any interview, prepare answers to the Universal 20 Questions below for your project. If your project involves CFD/simulation, also prepare the CFD-Specific 15 Questions. Practice with a timer: 2 min per answer.

---

## 📋 Navigation

| Section | Questions | Focus |
|---------|-----------|-------|
| [Universal 20 Questions](#-universal-20-project-defense-questions) | 20 | Any civil engineering project |
| [CFD-Specific 15 Questions](#-cfd-specific-project-defense) | 15 | CFD/simulation projects |
| [Project Presentation Framework](#-project-presentation-framework-5-minute) | Template | 5-min presentation structure |
| [Red Flags & How to Avoid Them](#-red-flags--how-to-avoid-them) | 8 | Common mistakes |

---

## 🎯 Universal 20 Project Defense Questions

> These are the questions interviewers ask about ANY project. Prepare answers for ALL 20.

### Category 1: Project Overview (Q1–Q5)

**Q1: "Tell me about your project in 2 minutes."**
> **Framework:** Problem → Objective → Method → Result → Impact
> **Template:** "My project addressed [PROBLEM]. The objective was to [OBJECTIVE]. I used [METHOD/TOOL] to achieve this. Key result: [QUANTITATIVE OUTCOME]. This contributes to [BROADER IMPACT]."
> **Example:** "My project addressed flood risk assessment for the Kosi River basin. The objective was to develop a 2D hydraulic model for 100-year flood inundation mapping. I used HEC-RAS 2D with SRTM DEM and satellite-derived land use. Key result: predicted flood extents matching Landsat imagery within 85% accuracy. This contributes to disaster preparedness for Bihar's flood-prone regions."

**Q2: "What problem were you trying to solve?"**
> **Framework:** Context → Gap → Need
> **Tip:** Start broad (why it matters) then narrow (specific gap). "Floods in India cause [₹X billion damage/year]. Existing studies on [area] lack [specific gap]. My project fills this by [approach]."

**Q3: "What was your specific role? Did you work alone or in a team?"**
> **Framework:** Be honest and specific about YOUR contribution.
> **Tip:** Use "I" not "we" for your contributions. If team: "I was responsible for [specific tasks]. My teammate handled [other tasks]. We collaborated on [joint tasks]."

**Q4: "What was the most innovative aspect of your project?"**
> **Framework:** Novel approach + why it matters.
> **Tip:** Could be methodology, data source, tool combination, or application. "I combined [technique A] with [technique B] which hasn't been done for [application] before, resulting in [improvement]."

**Q5: "What were the limitations of your project?"**
> **Framework:** Be honest — shows maturity and critical thinking.
> **Template:** "My project had three main limitations: (1) [data limitation], (2) [methodological assumption], (3) [scope limitation]. Future work could address these by [suggestion]."
> **Example:** "Limited by: (1) SRTM DEM resolution (30m) missed small channels, (2) assumed steady-state flow, (3) focused on only one reach. Future work: use LiDAR DEM, simulate unsteady flow, extend to full basin."

### Category 2: Methodology & Technical Depth (Q6–Q12)

**Q6: "Walk me through your methodology step by step."**
> **Framework:** Numbered steps with rationale for each.
> **Template:**
> 1. "Data collection: I gathered [data type] from [source] because [reason]."
> 2. "Preprocessing: I [processed data] to ensure [quality criterion]."
> 3. "Modeling: I chose [method/tool] because [justification]."
> 4. "Validation: I compared with [benchmark] using [metric]."
> 5. "Results: [key findings]."

**Q7: "Why did you choose this particular method/tool?"**
> **Framework:** Alternatives considered → Selection criteria → Justification.
> **Example:** "I considered HEC-RAS 1D, HEC-RAS 2D, and MIKE FLOOD. I chose HEC-RAS 2D because: (1) free and open-source, (2) handles complex overbank flow that 1D misses, (3) sufficient accuracy for my scale without the licensing cost of MIKE."

**Q8: "What validation did you perform?"**
> **Framework:** Benchmark → Metric → Result.
> **Tip:** Always mention quantitative metrics: NSE, RMSE, R², MAE. "My model achieved NSE = 0.82 against observed discharge data, which is considered 'very good' per Moriasi et al. (2007)."

**Q9: "What assumptions did you make? Are they justified?"**
> **Framework:** List assumptions + justify each.
> **Template:** "I assumed (1) [assumption], justified because [reason]; (2) [assumption], justified because [reason]. If these assumptions were violated, the impact would be [consequence]."

**Q10: "How sensitive are your results to the input parameters?"**
> **Framework:** Identify top 3 sensitive parameters → range tested → impact.
> **Example:** "Manning's n was most sensitive: varying ±20% changed peak WSE by ±15%. DEM resolution was second: coarser DEM increased flood extent by 12%. Rainfall intensity was third: ±10% rainfall changed peak discharge by ±8%."

**Q11: "What would you do differently if you started over?"**
> **Framework:** Shows learning and self-awareness.
> **Tip:** Be genuine. "I would: (1) collect higher-resolution field data, (2) use ensemble modeling instead of single model, (3) involve stakeholders earlier in the process."

**Q12: "How does your work relate to industry practice?"**
> **Framework:** Connect academic work to real-world application.
> **Example:** "My HEC-RAS model follows the same workflow used by USACE and state flood control departments. The methodology is directly applicable to Floodplain Mapping Orders required under Indian disaster management guidelines."

### Category 3: Technical Knowledge (Q13–Q17)

**Q13: "Explain the governing equation of your model."**
> **Framework:** Write the equation → explain each term → state assumptions.
> **Tip:** Be ready to write on paper. Practice writing key equations from memory.

**Q14: "What mesh/grid did you use? How did you ensure quality?"**
> **Framework:** Type → resolution → refinement → quality metrics.
> **Example:** "I used an unstructured triangular mesh with base size 50m, refined to 10m near the channel. Quality metrics: max aspect ratio < 5, min angle > 30°, no negative volumes. I performed a mesh sensitivity study with 3 refinements and confirmed < 2% change in key output."

**Q15: "What convergence criteria did you use?"**
> **Framework:** Residual threshold + monitors.
> **Example:** "I monitored residuals (10⁻⁴ for continuity, 10⁻⁵ for momentum), water surface elevation at a gauge location, and discharge at the outlet. Convergence was declared when all residuals dropped by 3 orders of magnitude and WSE stabilized within 0.1% over 100 time steps."

**Q16: "How did you handle boundary conditions?"**
> **Framework:** Type at each boundary + justification.
> **Example:** "Inflow: hydrograph from HEC-HMS output (upstream boundary). Outflow: normal depth slope (downstream). Sides: wall boundaries (no flow across valley walls). Initial condition: uniform flow depth from steady-state solution."

**Q17: "What post-processing did you perform?"**
> **Framework:** Visualization → statistics → comparison → reporting.
> **Example:** "I used ParaView for 3D visualization of velocity fields and water surface. I extracted time series of WSE and velocity at specific locations. I computed flood extent from water depth > 0.3m and compared with satellite imagery. I created inundation maps with QGIS."

### Category 4: Impact & Future Work (Q18–Q20)

**Q18: "What is the practical impact of your project?"**
> **Framework:** Who benefits + how + measurable impact.
> **Example:** "This model can help the Bihar State Disaster Management Authority identify vulnerable villages and plan evacuation routes. The 100-year flood map directly informs the state's flood risk zoning."

**Q19: "What future work would you propose?"**
> **Framework:** Short-term + medium-term + long-term.
> **Template:**
> - Short (3 months): "Extend model to include [missing component]."
> - Medium (6 months): "Couple with [additional model] for [purpose]."
> - Long (1 year): "Develop real-time forecasting system using [approach]."

**Q20: "If I gave you 6 months and a budget of ₹10 lakh, how would you extend this work?"**
> **Framework:** Concrete plan with resource allocation.
> **Example:** "₹3L for LiDAR survey (high-resolution DEM), ₹2L for field data collection (gauges, flow measurements), ₹2L for computing resources, ₹3L for research assistant. Timeline: months 1–2 data collection, months 3–4 modeling, months 5–6 validation and reporting."

---

## 🖥️ CFD-Specific Project Defense

> These questions are for projects involving OpenFOAM, ANSYS Fluent, Star-CCM+, or any CFD tool.

### Simulation Setup (Q1–Q5)

**CFD-Q1: "Why did you choose CFD over analytical/experimental methods?"**
> **Expected:** "Analytical solutions are limited to simplified geometries. Physical experiments are expensive, time-scale dependent, and may not capture all physics (e.g., 3D effects). CFD provides full field data at any point, allows parametric studies, and is cost-effective for design optimization."

**CFD-Q2: "What solver did you use and why?"**
> **Expected:** Match solver to physics:
> - Water-only flow → `pimpleFoam` (incompressible turbulent)
> - Water-air interface → `interFoam` (VOF, multiphase)
> - Heat transfer → `chtFoam` or `buoyantPimpleFoam`
> - Sediment → custom solver or `interFoam` with DPM/DEM

**CFD-Q3: "Describe your mesh strategy."**
> **Expected:**
> - Domain: "Created a 3D domain extending [X] upstream and [Y] downstream of the region of interest."
> - Type: "Unstructured tetrahedral with prism layers near walls."
> - Resolution: "Base cell size [Z], refined to [Z/4] in region of interest."
> - Quality: "Max non-orthogonality < 65%, max skewness < 0.85, aspect ratio < 10."
> - Prism layers: "5 layers, expansion ratio 1.2, first cell height set for y+ ≈ 30."

**CFD-Q4: "How did you determine y+ and wall treatment?"**
> **Expected:** "For RANS with wall functions: y+ ≈ 30–300. I checked y+ distribution post-simulation and ensured 95% of wall cells fell in this range. For near-wall resolution (low-Re model or LES): y+ < 1, with 10+ prism layers to resolve viscous sublayer."

**CFD-Q5: "What time stepping scheme did you use? How did you control the time step?"**
> **Expected:** "Second-order implicit (backward). Time step adaptively controlled by max Courant number (Co < 0.5 for VOF, Co < 1.0 for single-phase). This ensures numerical stability and captures transient phenomena."

### Turbulence Modeling (Q6–Q8)

**CFD-Q6: "What turbulence model did you use? Why not another?"**
> **Expected:** "I used k-ω SST because [reasons]:
> - k-ε: poor near walls, doesn't handle adverse pressure gradient well
> - k-ω: free-stream sensitivity
> - SST: combines k-ω (near wall) + k-ε (far field), handles separation, validated for hydraulic flows
> - LES: too expensive for my Re (~10⁶) and time requirements."

**CFD-Q7: "What is the difference between RANS and LES? When would you use each?"**
> **Expected:** "RANS: time-averages turbulence, models ALL scales with turbulence model. Cheap, steady or unsteady RANS. Good for mean flow quantities. LES: resolves large energy-containing eddies, models only small sub-grid scales. Expensive (Re^1.5 cost), unsteady, better for separated/transitional flows. I used RANS because [my case didn't require resolved turbulence]."

**CFD-Q8: "How do you handle the free surface in your simulation?"**
> **Expected:** "Volume of Fluid (VOF): transport equation for volume fraction α. α=1 (water), α=0 (air). Interface captured by High-Resolution Interface Capturing (HRIC) scheme. I set: atmospheric pressure at top boundary, zero-gradient for velocity at free surface, surface tension = 0.073 N/m."

### Validation & Results (Q9–Q12)

**CFD-Q9: "How did you validate your CFD model?"**
> **Expected:** "Three levels: (1) **Mesh independence**: 3 meshes (coarse/medium/fine), < 2% change in key output. (2) **Analytical comparison**: compared hydraulic jump location/depth with conjugate depth formula — within 5%. (3) **Experimental validation**: compared velocity profiles with PIV data from [reference] — NSE = 0.88."

**CFD-Q10: "What is Richardson extrapolation and how did you use it?"**
> **Expected:** "Estimates the continuum (infinite-resolution) solution from three mesh solutions. GCI (Grid Convergence Index) quantifies discretization error. GCI = Fs × |φ₂-φ₁|/(r^p - 1), where Fs=1.25 (safety factor), r = refinement ratio, p = order of convergence."

**CFD-Q11: "What were your key results? Show me a plot."**
> **Expected:** Have 3–5 key plots ready:
> 1. Water surface profile (comparison with analytical/experimental)
> 2. Velocity contours/vectors at key cross-section
> 3. Turbulent kinetic energy distribution
> 4. Time series of discharge/WSE at monitoring point
> 5. Mesh detail (independent slide)

**CFD-Q12: "What is the uncertainty in your results?"**
> **Expected:** "Sources of uncertainty: (1) Input data (DEM accuracy ±0.5m, Manning's n ±20%), (2) Model formulation (turbulence model closure), (3) Numerical (mesh resolution, time step). I quantified input uncertainty by varying key parameters. Total uncertainty in peak WSE: ±0.3m (5% of flow depth)."

### Advanced (Q13–Q15)

**CFD-Q13: "What post-processing tools did you use?"**
> **Expected:** "ParaView for 3D visualization (streamlines, contours, volume rendering), Python (matplotlib) for time series and statistical plots, Tecplot for publication-quality 2D cross-sections."

**CFD-Q14: "How would you improve the accuracy of your simulation?"**
> **Expected:** "Three approaches: (1) Higher-resolution mesh (especially near walls and free surface), (2) LES instead of RANS for resolved turbulence, (3) Better input data (field-measured Manning's n, LiDAR DEM, measured inflow hydrograph)."

**CFD-Q15: "If I asked you to simulate [new scenario], how would you approach it?"**
> **Expected:** Think on your feet. "I would: (1) assess the new physics required, (2) modify domain/boundary conditions accordingly, (3) potentially switch solver if new physics needed, (4) run mesh sensitivity study for the new configuration, (5) validate against available data for the new scenario."

---

## 🎤 Project Presentation Framework (5 Minute)

> Use this structure when asked to present your project:

```
MINUTE 1: CONTEXT & PROBLEM
├── Real-world motivation (1 sentence)
├── Specific gap in knowledge/practice
└── Your project objective (1 sentence)

MINUTE 2: METHODOLOGY
├── Data sources and tools
├── Approach overview (numbered steps)
└── Key assumptions

MINUTE 3: KEY RESULTS
├── Primary finding (quantitative)
├── Validation evidence
└── Comparison with alternatives

MINUTE 4: CONTRIBUTION & IMPACT
├── What's new/different about your work
├── Practical relevance
└── Limitations (honest)

MINUTE 5: FUTURE & QUESTIONS
├── Next steps (2–3 items)
├── Broader significance
└── "I'm happy to dive deeper into any aspect"
```

---

## 🚩 Red Flags & How to Avoid Them

| Red Flag | Why It's Bad | How to Fix |
|----------|-------------|------------|
| **"I used software X"** without explaining the physics | Shows tool user, not engineer | Always explain the governing equations and physics |
| **Can't explain a result** | Might not have done the work | Understand every output you present |
| **No validation mentioned** | Results could be meaningless | Always compare with benchmark/experiment |
| **"I don't know"** to basic questions | Gaps in fundamental knowledge | Revise basics before presenting project |
| **Overcomplicating simple answers** | Confusion, not expertise | Start simple, add complexity only if asked |
| **No limitations acknowledged** | Overconfidence, lack of critical thinking | Always list 2–3 limitations honestly |
| **Can't write the key equation** | Didn't understand the theory | Practice writing 3–5 key equations on paper |
| **Blaming tools/data for problems** | Shows poor problem-solving | Frame as challenges you overcame |

---

## 🔗 Cross-Links

- [`project-discussion.md`](project-discussion.md) — Original project discussion guide
- [`technical-interview-bank.md`](technical-interview-bank.md) — 100 Q&A by topic
- [`software-interview-guide.md`](../software-interview-guide.md) — Software tool Q&As
- [`mock-interview-database.md`](../mock-tests/mock-interview-database.md) — Full mock interviews
- [`behavioral-interview-guide.md`](../behavioral/behavioral-interview-guide.md) — STAR format for behavioral Qs

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 1.0 — Project Defense Guide

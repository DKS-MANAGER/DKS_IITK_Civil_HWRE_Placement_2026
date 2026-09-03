# Mock Interview Database — 8 Full Sessions by Difficulty

> **How to use:** Each mock is a complete 45–60 minute interview simulation with an interviewer script and expected answers. Practice with a friend playing the interviewer, or record yourself answering each question. Time each response.

---

## 📋 Navigation

| Mock # | Difficulty | Focus | Duration | Ideal For |
|--------|-----------|-------|----------|-----------|
| [Mock 1](#mock-1--basic-civil-engineering) | ⭐ Easy | Basic Civil Engineering | 40 min | First-year preparation, warm-up |
| [Mock 2](#mock-2--core-civil-technical) | ⭐⭐ Medium | Core Civil Technical | 45 min | Core civil placement (L&T, AECOM) |
| [Mock 3](#mock-3--hwre-specialized) | ⭐⭐⭐ Medium-Hard | HWRE Domain | 50 min | HWRE roles (WAPCOS, Veolia) |
| [Mock 4](#mock-4--advanced-hydraulics--cfd) | ⭐⭐⭐⭐ Hard | Advanced Hydraulics & CFD | 50 min | R&D, CFD roles (IITK PG) |
| [Mock 5](#mock-5--mtechresearch) | ⭐⭐⭐⭐ Hard | M.Tech / Research | 55 min | IITK M.Tech interview |
| [Mock 6](#mock-6--mixed-technical) | ⭐⭐⭐ Medium-Hard | Mixed Technical (all subjects) | 45 min | General civil placement |
| [Mock 7](#mock-7--technicalhr-hybrid) | ⭐⭐⭐ Medium-Hard | Technical + HR Hybrid | 45 min | Final round interviews |
| [Mock 8](#mock-8--stress-test) | ⭐⭐⭐⭐⭐ Expert | Stress Test / Curveball | 50 min | Top-tier consulting / AECOM strategic |

---

## Mock 1 — Basic Civil Engineering

> **Interviewer script (10 questions + 3 HR follow-ups)**

### Technical Section

**Q1: What is the difference between one-way slab and two-way slab?**
> **Expected:** One-way: Ly/Lx > 2, bending in one direction, reinforcement mainly along shorter span. Two-way: Ly/Lx ≤ 2, bending in both directions, reinforcement in both directions. IS 456:2000.

**Q2: State the assumptions of Bernoulli's equation.**
> **Expected:** Steady flow, incompressible fluid, inviscid (frictionless), along a streamline. Each assumption violated = correction needed (real fluid → add h_L).

**Q3: What is the difference between nominal mix and design mix concrete?**
> **Expected:** Nominal: fixed proportions (1:2:4 for M15), no site-specific optimization. Design mix: lab-tested proportions per IS 10262, optimized for strength, workability, durability. M20+ always design mix.

**Q4: What are the types of foundations? When would you choose a pile foundation?**
> **Expected:** Shallow (isolated, combined, raft, strip). Deep (piles, caissons). Piles when: (1) surface soil has low bearing capacity, (2) heavy loads from high-rise, (3) large horizontal loads, (4) when settlement must be minimal.

**Q5: What is the modulus of subgrade reaction? How is it used?**
> **Expected:** k = pressure/ratio settlement = q/s. Used in pavement design (flexible/rigid), slab-on-grade. Plate load test determines k. Correlates with CBR and soil stiffness.

**Q6: Explain the difference between working stress method and limit state method.**
> **Expected:** WSM: elastic theory, factor of safety on materials, no redistribution. LSM: plastic theory, partial safety factors on loads AND materials (γf=1.5, γm=1.5 for concrete, 1.15 for steel), allows redistribution. IS 456 uses LSM.

**Q7: What is the purpose of stirrups in a beam?**
> **Expected:** (1) Resist diagonal shear (most important), (2) hold longitudinal bars in position, (3) prevent buckling of compression bars, (4) confine concrete in compression zone. Spacing per IS 456 Cl. 26.5.

**Q8: What is soil consolidation? How is it different from compaction?**
> **Expected:** Consolidation: time-dependent settlement due to expulsion of pore water under sustained load (Terzaghi's theory). Compaction: densification by mechanical effort (removing air, not water). Consolidation = field process; compaction = construction process.

**Q9: What is the Mohr-Coulomb failure criterion?**
> **Expected:** τ_f = c + σ tan φ. Shear strength = cohesion + normal stress × friction coefficient. c = cohesion (kPa), φ = angle of internal friction. Ineffective for sands (c=0).

**Q10: What is the difference between pre-tensioned and post-tensioned concrete?**
> **Expected:** Pre-tensioning: tendons stressed before casting; force transferred by bond at ends. Post-tensioning: tendons stressed after concrete gains strength; ducts left in concrete, grouted after stressing. Pre-tensioned for factory elements; post-tensioned for site construction.

### HR Follow-ups

**Q11: Why civil engineering?**
> **Expected:** Passion for building infrastructure, analytical mindset, desire to contribute to real-world projects. (Tailor to your story.)

**Q12: What is your biggest weakness?**
> **Expected:** Honest, specific, and shows improvement. Example: "I used to spend too long on details, but I've learned to prioritize by setting time boxes."

**Q13: Where do you see yourself in 5 years?**
> **Expected:** Growth-oriented. "As a practicing engineer leading projects, having completed my M.Tech/gained professional experience in [specific domain]."

---

## Mock 2 — Core Civil Technical

> **Interviewer script (12 questions + 2 HR follow-ups)**

### Technical Section

**Q1: Derive the bending stress formula σ = My/I.**
> **Expected:** From plane sections remaining plane: strain varies linearly with distance from neutral axis. ε = y/R. From Hooke's law: σ = Eε = Ey/R. Substitute 1/R = M/EI: σ = My/I. Valid for elastic bending.

**Q2: A simply supported beam (L=6m, w=10 kN/m). Find maximum moment and deflection.**
> **Expected:** M_max = wL²/8 = 10×36/8 = 45 kNm (at midspan). δ_max = 5wL⁴/384EI = 5×10×6⁴/(384EI) = 8437.5/EI m. Need EI value for numerical answer.

**Q3: What is the difference between short column and long column?**
> **Expected:** Short: fails by crushing (Le/D < 12). Long: fails by buckling (Le/D > 12). Le = effective length depends on end conditions. Euler buckling load: P_cr = π²EI/Le².

**Q4: Explain the concept of effective length for columns.**
> **Expected:** Effective length = equivalent length of pinned-pinned column that gives same buckling load. Both ends fixed: Le = 0.5L. Fixed-free: Le = 2L. One end fixed, one pinned: Le = 0.7L. IS 456 Table 28.

**Q5: What is the principle of virtual work? How do you apply it?**
> **Expected:** External virtual work = Internal virtual work. Apply unit load at point of interest, compute real member deformations from actual loads. δ = Σ(N̄ × NL/AE) for trusses. Fundamental for deflection calculations.

**Q6: What are the different types of soil tests for foundation investigation?**
> **Expected:** (1) Plate load test → bearing capacity, (2) Standard Penetration Test → N-value → bearing capacity correlations, (3) Cone Penetration Test → continuous profile, (4) Vane shear test → soft clay strength, (5) Laboratory: triaxial, unconfined compression, consolidation.

**Q7: What is the SPT N-value and how is it used?**
> **Expected:** Standard Penetration Test: 63.5 kg hammer dropped 750 mm, count blows for 300 mm penetration. N = N₆₃.₅ (corrected for overburden and energy). Used for: bearing capacity (Meyerhof: q_net = N×Df/0.08 for Df≤4m), settlement estimation, liquefaction assessment.

**Q8: What is pavement design? Difference between flexible and rigid?**
> **Expected:** Flexible: bituminous layers, load spread by grain-to-grain (45°), design by CBR method (IRC:37). Rigid: PCC slab, load spread as plate, design by Westergaard (IRC:58). Rigid: longer life, lower maintenance; Flexible: easier rehabilitation.

**Q9: What is the hydrologic cycle? What is a catchment?**
> **Expected:** Continuous water cycle: evaporation → condensation → precipitation → runoff/infiltration. Catchment (watershed): area contributing surface runoff to a common outlet point. Delineated by topographic divides.

**Q10: Explain Darcy's law for groundwater flow.**
> **Expected:** Q = -KA(dh/dl). Discharge proportional to hydraulic gradient and cross-sectional area. K = hydraulic conductivity (m/s). Valid for Re < 1 (laminar flow in porous media). Darcy velocity is apparent; seepage velocity = K·i/n.

**Q11: What is the difference between ductile and brittle failure in steel?**
> **Expected:** Ductile: significant yielding before fracture (mild steel: elongation 20–30%, necking visible, absorbed energy = area under stress-strain curve). Brittle: sudden fracture with little warning (cast iron, high-carbon steel). IS 800 uses partial safety factors: γ_m0 = 1.1 (yielding), γ_m1 = 1.25 (ultimate).

**Q12: What are the types of retaining walls? When do you use each?**
> **Expected:** Gravity: massive, uses self-weight (h < 3m). Cantilever: L-shaped, uses backfill weight (h = 3–6m). Counterfort: with tension ties (h > 6m). Sheet pile: driven into soil, for waterfronts/excavation. Anchored: with tiebacks for deep excavation.

### HR Follow-ups

**Q13: Describe a project you worked on. What was your role?**
> **Expected:** STAR format: Situation → Task → Action → Result. Specific, measurable outcomes. Example: "In my final year project on [topic], I was responsible for [specific task]. I used [tool/method] which resulted in [outcome]."

**Q14: What software are you proficient in?**
> **Expected:** Name 3–4 tools with specific project examples. E.g., "STAAD.Pro for structural analysis of a G+2 building, AutoCAD for drafting, Excel for CPM calculations, and Python for data analysis."

---

## Mock 3 — HWRE Specialized

> **Interviewer script (12 questions + 2 HR follow-ups)**

### Technical Section

**Q1: What is the difference between Darcy-Weisbach and Hazen-Williams equations?**
> **Expected:** Darcy-Weisbach: h_f = f(L/D)(V²/2g), f from Moody diagram, applicable to any fluid/temp. HW: h_f = (10.67LQ^1.852)/(C^1.852 × D^4.87), empirical, C varies, only for water at ~20°C. Darcy is more general; HW is simpler for water supply.

**Q2: Explain the Saint-Venant equations.**
> **Expected:** Two PDEs for 1D unsteady open-channel flow. Continuity: ∂A/∂t + ∂Q/∂x = q_l. Momentum: ∂Q/∂t + ∂(Q²/A)/∂x + gA(∂y/∂x + S_f - S₀) = 0. Account for lateral inflow, friction, gravity. Solved numerically (Preissmann, Lax-Wendroff).

**Q3: What is a hydraulic jump? When does it occur?**
> **Expected:** Sudden transition from supercritical (Fr > 1) to subcritical (Fr < 1). Energy dissipation mechanism. Occurs downstream of spillways, sluice gates, steep chutes. Conjugate depths: y₂/y₁ = 0.5[√(1+8Fr₁²) - 1]. Energy loss: ΔE = (y₂-y₁)³/(4y₁y₂).

**Q4: Design a rectangular channel to carry 15 m³/s. S=0.001, n=0.025, side slopes 2H:1V.**
> **Expected:** Use Manning's equation: Q = (1/n) × A × R^(2/3) × S^(1/2). Iterate: assume normal depth y_n, compute A and P, get R=A/P, check Q. For b=5m, y_n≈1.9m: A=18.8m², P=13.4m, R=1.4m, Q=(1/0.025)×18.8×1.4^(2/3)×0.001^0.5 = 40×18.8×1.249×0.0316 = 29.7 — too high. Reduce b, re-iterate until Q=15.

**Q5: What is the rational method? What are its limitations?**
> **Expected:** Q = CiA/360 (m³/s, mm/hr, hectares). Peak runoff from uniform rainfall intensity i for catchment area A. Limitations: (1) only for small catchments (<5 km²), (2) assumes uniform rainfall, (3) no storage consideration, (4) i duration = time of concentration.

**Q6: Explain the SCS-CN method.**
> **Expected:** P_e = (P - I_a)² / (P - I_a + S). S = 25400/CN - 254. CN = 30–100 (based on land use + soil group + AMC). I_a = 0.2S. CN accounts for impervious area, antecedent moisture. Modified for Indian conditions (10% I_a for some regions).

**Q7: What is the difference between BOD and COD?**
> **Expected:** BOD₅: oxygen consumed by microorganisms in 5 days at 20°C (biochemical). COD: oxygen consumed by chemical oxidation (dichromate method). COD > BOD (includes non-biodegradable). COD/BOD ratio: domestic sewage ~2.0, industrial varies. BOD = organic pollution indicator.

**Q8: Explain the activated sludge process.**
> **Expected:** Biological treatment: influent → aeration tank (mixed liquor, MLSS 2000–4000 mg/L, HRT 4–8 hrs) → secondary clarifier → effluent. Return activated sludge (R/S = 25–50%). F/M ratio = 0.2–0.5. SRT = 5–15 days. Removes BOD (85–95%). Design: hydraulic loading, organic loading.

**Q9: What is the difference between trickling filter and activated sludge?**
> **Expected:** TF: attached growth, rocks/plastic media, lower energy, simpler operation, lower efficiency (80–90%). ASP: suspended growth, higher energy (aeration), higher efficiency (90–95%), more flexible. TF suited for smaller plants; ASP for larger urban plants.

**Q10: What is the Duty and Delta of a crop?**
> **Expected:** Duty: hectares per cumec (D = A/Q). Delta: total water depth applied to crop (mm) over season. D = 864B/M, where B = base period (days), M = delta (m). Duty varies with season, climate, soil. Higher duty = more efficient.

**Q11: What is the difference between ACI 318 and IS 456 for concrete design?**
> **Expected:** ACI 318 uses strength-based design with different partial factors. IS 456 uses limit state (similar to Eurocode philosophy). ACI φ factors (0.65–0.9) vs IS γ factors (1.5). ACI uses f'c (cylinder strength), IS uses fck (cube strength, fck = 1.25×f'c). Reinforcement: ASTM vs IS grades.

**Q12: What is the specific speed of a turbine? How do you select a turbine type?**
> **Expected:** N_s = N√P/H^(5/4). Low N_s (10–35) → Pelton (impulse, high head). Medium N_s (60–300) → Francis (reaction, medium head). High N_s (300–1000) → Kaplan (reaction, low head). Selection based on head, discharge, and power requirement.

### HR Follow-ups

**Q13: What is your research area at IIT Kanpur?**
> **Expected:** Clearly explain your M.Tech thesis topic, methodology, key findings, and relevance to the company's work.

**Q14: Why do you want to work in this company?**
> **Expected:** Specific — mention company's projects, technology, or market position. "I'm interested in [company]'s work on [specific project/technology] which aligns with my expertise in [your area]."

---

## Mock 4 — Advanced Hydraulics & CFD

> **Interviewer script (12 questions, research-level)**

### Technical Section

**Q1: Explain the Reynolds-Averaged Navier-Stokes equations. What is the closure problem?**
> **Expected:** Time-average N-S equations + Reynolds stress terms (−ρ⟨u'ᵢu'ⱼ⟩). Closure problem: 6 unknown Reynolds stresses but only 5 equations. Requires turbulence model: k-ε (2 transport equations), k-ω SST, Reynolds Stress Model (RSM, 7 equations).

**Q2: Compare k-ε and k-ω SST models.**
> **Expected:** k-ε: robust, free-shear flows, poor near walls (wall functions needed). k-ω: accurate near walls, free-stream sensitivity. SST: blends k-ω near walls (transport equation) and k-ε in far field. SST preferred for adverse pressure gradient flows, separation.

**Q3: What is VOF and when would you use it?**
> **Expected:** Volume of Fluid: tracks interface between immiscible fluids (water-air). α = 0 (air) to 1 (water). Transport equation: ∂α/∂t + ∇·(αU) = 0. Used for: dam break, wave-structure interaction, free-surface flows, hydraulic jump simulation.

**Q4: Explain the concept of wall functions vs resolved near-wall approaches.**
> **Expected:** Wall functions: bridge viscous sublayer using empirical laws (log-law). y+ ≈ 30–300. Avoids resolving thin viscous sublayer → coarser mesh. Resolved: y+ ≈ 1, mesh cells within viscous sublayer. Required for LES, low-Re RANS, separation prediction.

**Q5: What is the Courant number and why must Co < 1 for explicit schemes?**
> **Expected:** Co = uΔt/Δx. CFL condition: information must not travel more than one cell per time step for stability in explicit schemes. Implicit schemes can have Co > 1 but accuracy degrades. For transient multiphase, Co < 0.5 recommended.

**Q6: How do you validate a CFD model against experimental data?**
> **Expected:** (1) Grid independence study (3+ meshes, Richardson extrapolation). (2) Compare velocity profiles at specific locations. (3) Compare water surface profiles (HEC-RAS vs CFD). (4) Compute RMSE, R², NSE. (5) Document assumptions and limitations.

**Q7: Explain the finite volume method.**
> **Expected:** Discretize domain into control volumes. Integrate governing equations over each CV. Apply Gauss divergence theorem → face fluxes. Convection: upwind, QUICK, TVD schemes. Diffusion: central difference. Pressure-velocity coupling: SIMPLE, PISO, PIMPLE.

**Q8: What is mesh convergence and how do you demonstrate it?**
> **Expected:** Run simulation on 3+ progressively refined meshes. Monitor key output (e.g., drag coefficient, WSE). Plot output vs 1/√N (cell count). When change < 2–5% between successive refinements, mesh is converged. Use GCI (Grid Convergence Index) for quantitative estimate.

**Q9: What is the difference between structured and unstructured meshes?**
> **Expected:** Structured: regular grid (quad/hex), easy to implement, good accuracy, poor for complex geometry. Unstructured: triangles/tets, fits complex geometry, easier adaptive refinement, higher numerical diffusion. Hybrid: structured near walls (prism layers), unstructured in bulk.

**Q10: What is the difference between DNS, LES, and RANS?**
> **Expected:** DNS: resolves all turbulent scales, no model, Re^3 cost, limited to Re < 10⁴. LES: resolves large eddies, models sub-grid scales (Smagorinsky, WALE), moderate cost. RANS: models all turbulence (time-averaged), cheapest, limited for unsteady/separated flows.

**Q11: How would you simulate a hydraulic jump in OpenFOAM?**
> **Expected:** `interFoam` (VOF). 2D domain: inlet (supercritical depth + velocity), outlet (subcritical boundary), bottom (wall), top (atmosphere). Set inflow Fr > 1. Mesh refined at jump location. Monitor: water surface profile, velocity field, energy dissipation. Compare with conjugate depth formula.

**Q12: What is the Rouse profile and how does it relate to sediment suspension?**
> **Expected:** c/c_a = (y_a/y)^Z, Z = w_s/(κu_τ). Rouse number Z determines suspension capability. Z > 2.5: bed load only. 0.1–2.5: suspended load. Z < 0.1: wash load. Derived from balancing turbulent diffusion and gravitational settling in the advection-diffusion equation.

---

## Mock 5 — M.Tech / Research

> **Interviewer script (14 questions, thesis defense style)**

### Technical Section (Subject Knowledge)

**Q1: What is the most important concept in your area of expertise? Explain in depth.**
> **Expected:** Pick your strongest subject. Explain clearly with equations, applications, and limitations. Show depth.

**Q2: What is the Navier-Stokes equation? Can you write it in index notation?**
> **Expected:** ρ(∂uᵢ/∂t + uⱼ∂uᵢ/∂xⱼ) = −∂p/∂xᵢ + μ∂²uᵢ/∂xⱼ∂xⱼ + ρgᵢ. Conservation of momentum for Newtonian incompressible fluid. Four terms: unsteady, convective, pressure, viscous.

**Q3: What is dimensional analysis? Derive the Froude number.**
> **Expected:** Buckingham Pi: n variables, m dimensions → n-m groups. Froude: Fr = V/√(gL). Inertial/gravitational forces. Free-surface flows: Fr > 1 supercritical, < 1 subcritical. Model testing: same Fr for hydraulic similarity.

**Q4: Explain the concept of similarity in model testing.**
> **Expected:** Geometric: same shape ratio (L_r). Kinematic: same velocity ratio (V_r). Dynamic: same force ratio (F_r). For free-surface: Froude similarity (Fr_m = Fr_p). For viscous: Reynolds similarity (Re_m = Re_p). Can't satisfy both simultaneously → choose dominant force.

### Thesis Defense

**Q5: What problem does your thesis address?**
> **Expected:** Clear problem statement with motivation. "Existing methods for [X] have limitations in [Y]. I propose [Z] to address this gap."

**Q6: What methodology did you use?**
> **Expected:** Specific tools, equations, validation approach. "I used OpenFOAM with interFoam solver for VOF simulation, meshed using snappyHexMesh with y+ < 1. Validated against experimental data from [reference]."

**Q7: What are your key findings?**
> **Expected:** Quantitative results with comparisons. "My model predicted [parameter] within [X]% of experimental data, compared to [Y]% for existing models."

**Q8: What are the limitations of your work?**
> **Expected:** Honest assessment. "The simulation assumed 2D, neglected sediment transport, and used a constant Manning's n. Future work could include 3D effects, sediment coupling, and seasonal variation."

**Q9: How does your work contribute to the field?**
> **Expected:** Practical application + theoretical contribution. "This work provides a validated CFD framework for [application] that can be used by [target users] to [benefit]."

### Research Skills

**Q10: What programming languages do you know? Show your proficiency.**
> **Expected:** Name languages with specific application. Have code samples ready (GitHub, portfolio).

**Q11: Describe your research workflow.**
> **Expected:** Literature review → methodology development → implementation → validation → results analysis → publication.

**Q12: Have you published any papers?**
> **Expected:** List publications, conference presentations. If not: "I'm preparing a manuscript on [topic] for submission to [journal]."

**Q13: Why do you want to pursue M.Tech/PhD?**
> **Expected:** Research interest, specific problem to solve, career goal. "I want to deepen my understanding of [area] and contribute to [specific research question]."

**Q14: Where do you see yourself after M.Tech?**
> **Expected:** Clear career path — industry R&D, academia, or consulting. Tailor to interview context.

---

## Mock 6 — Mixed Technical

> **Interviewer script (12 questions, one from each subject)**

**Q1 (Hydraulics):** Explain the Moody diagram and how to find friction factor.
> **Expected:** f vs Re for various ε/D. Laminar: f=64/Re. Turbulent: Colebrook-White or Swamee-Jain.

**Q2 (OCF):** What is a hydraulic jump? Give conjugate depth equation.
> **Expected:** Supercritical to subcritical transition. y₂/y₁ = 0.5[√(1+8Fr₁²)-1].

**Q3 (Hydrology):** Explain the unit hydrograph and its assumptions.
> **Expected:** DRH from 1 unit of effective rainfall. Linearity and time-invariance assumptions.

**Q4 (WRE):** What is the Muskingum routing method? Explain K and X.
> **Expected:** S = K[XI + (1-X)O]. K = travel time. X = wedge storage weight (0–0.5).

**Q5 (Irrigation):** What is the duty-delta relationship?
> **Expected:** D = 864B/M. Duty (ha/cumec), Delta (mm), B (base period in days).

**Q6 (Structures):** What is the moment-curvature relationship for RC beams?
> **Expected:** M = 0.87f_y A_s d(1 - A_s f_y/bd f_ck). Derived from strain compatibility and equilibrium.

**Q7 (Geotechnical):** Explain the Mohr-Coulomb failure criterion.
> **Expected:** τ_f = c + σ tan φ. Effective stress version: τ_f = c' + (σ - u) tan φ'.

**Q8 (Environmental):** What is BOD and COD? Which is higher?
> **Expected:** BOD₅ = biological oxygen demand (5 days, 20°C). COD = chemical oxidation. COD > BOD (includes non-biodegradable).

**Q9 (Transportation):** What is the difference between flexible and rigid pavement?
> **Expected:** Flexible: grain-to-grain load transfer, bituminous. Rigid: slab action, PCC. IRC:37 vs IRC:58.

**Q10 (Geoinformatics):** What is NDVI? How do you compute it?
> **Expected:** NDVI = (NIR-Red)/(NIR+Red). Range -1 to +1. Vegetation health indicator.

**Q11 (Infrastructure):** What is CPM and PERT? Difference?
> **Expected:** CPM = deterministic (one time). PERT = probabilistic (three times: optimistic, most likely, pessimistic).

**Q12 (Software):** Name 3 software tools you're proficient in.
> **Expected:** Tool, application, project example. "HEC-RAS for flood modeling, Python for data analysis, STAAD for structural design."

---

## Mock 7 — Technical + HR Hybrid

> **Interviewer script (10 questions, alternating technical and HR)**

**Q1 (HR):** Tell me about yourself.
> **Expected:** 90 seconds. Education → relevant experience → skills → what you're looking for. End with alignment to the role.

**Q2 (Technical):** What is the most challenging technical problem you've solved?
> **Expected:** STAR format with technical depth. "I was modeling a dam breach in HEC-RAS and the results didn't match. I realized the cross-sections were inaccurate. I re-surveyed key sections, updated the model, and achieved 92% match with observed data."

**Q3 (HR):** How do you handle conflict in a team?
> **Expected:** STAR format. Listen → understand → find common ground → communicate → resolve.

**Q4 (Technical):** If I gave you a flood modeling project tomorrow, how would you approach it?
> **Expected:** (1) Collect data (topography, rainfall, land use). (2) Build hydrologic model (HEC-HMS). (3) Build hydraulic model (HEC-RAS). (4) Validate against observed data. (5) Present results with uncertainty bounds.

**Q5 (HR):** Why should we hire you?
> **Expected:** 3 strengths mapped to job requirements. "My combination of [technical skill 1], [technical skill 2], and [soft skill] makes me well-suited for [role]."

**Q6 (Technical):** What do you think about [current infrastructure project in India]?
> **Expected:** Show awareness of Indian infrastructure. Ganga Expressway, bullet train, Namami Gange, Smart Cities Mission. Give informed opinion with technical perspective.

**Q7 (HR):** Tell me about a time you failed.
> **Expected:** Genuine failure → what you learned → how you improved. Avoid: "I work too hard."

**Q8 (Technical):** How do you stay updated with current developments?
> **Expected:** Technical journals, conferences, online courses, GitHub repositories, LinkedIn. Be specific: "I follow ASCE Journal of Hydraulic Engineering, I follow [specific researchers] on ResearchGate."

**Q9 (HR):** What are your salary expectations?
> **Expected:** Research the company's range. "Based on my research and the role requirements, I'm looking for [range]. I'm flexible and open to discussion."

**Q10 (HR):** Do you have any questions for us?
> **Expected:** Always have 2–3 prepared. "What does a typical project look like?" / "How does the team collaborate across offices?" / "What growth opportunities exist for new hires?"

---

## Mock 8 — Stress Test

> **Interviewer script (12 rapid-fire questions, intentionally difficult)**

**Q1:** Solve this on paper: A trapezoidal channel (b=4m, z=1.5) carries Q=25 m³/s at n=0.03, S=0.0005. Find normal depth.
> **Expected:** Iterate Manning's. A = (4+1.5y)y, P = 4+3.202y. (1/0.03)×A×(A/P)^(2/3)×0.0005^0.5 = 25. Solve for y ≈ 2.8m.

**Q2:** What is the difference between ε and δ in the Colebrook-White equation? Quick.
> **Expected:** ε = absolute roughness (mm). δ = viscous sublayer thickness. In Colebrook: ε is pipe roughness, not δ.

**Q3:** You have 30 seconds. Name 5 dimensionless numbers in fluid mechanics and their physical meaning.
> **Expected:** Re (inertia/viscous), Fr (inertia/gravity), We (inertia/surface tension), Ma (velocity/sound), St (unsteady/convection).

**Q4:** What is the buckling load of a column with both ends fixed? Length 3m, E=200 GPa, I=1000 cm⁴.
> **Expected:** Le = 0.5L = 1.5m. P_cr = π²EI/Le² = π²×200×10⁹×10⁻⁵/1.5² = 8.77 MN.

**Q5:** A soil sample: W=30g, Ws=25g, G=2.65. Find water content and void ratio.
> **Expected:** w = (W-Ws)/Ws = 5/25 = 20%. e = wG = 0.2×2.65 = 0.53.

**Q6:** Why is concrete strong in compression but weak in tension?
> **Expected:** Cement paste bonds aggregate under compression (interlocking). Under tension, bonds crack at ~10% of compressive strength. Cracks propagate along weak transition zones. Reinforcement carries tension.

**Q7:** What is the Reynolds transport theorem? Write it.
> **Expected:** d/dt ∫_CV (ρφ dV) + ∫_CS (ρφ V·n dA) = ∫_CV (ρ Dφ/Dt dV). Rate of change in CV = rate of change inside + net flux out. Foundation for all conservation equations.

**Q8:** What is the difference between isothermal and adiabatic bulk modulus?
> **Expected:** Isothermal: K_T = -V(dP/dV)_T. Adiabatic: K_S = -V(dP/dV)_S. K_S > K_T for gases. For liquids, nearly identical.

**Q9:** Name the IS codes for: concrete, steel, seismic, traffic.
> **Expected:** IS 456 (concrete), IS 800 (steel), IS 1893 (seismic), IRC 37/58 (traffic/pavement), IS 875 (loads).

**Q10:** What is the Green-Ampt infiltration model? Write the equation.
> **Expected:** f = K(1 + (ψΔθ)/F). f = infiltration rate. K = hydraulic conductivity. ψ = suction head. Δθ = moisture deficit. F = cumulative infiltration. Implicit equation for F(t).

**Q11:** How do you compute the deflection of a cantilever beam using the moment-area method?
> **Expected:** First M-A theorem: θ_B - θ_A = area of M/EI diagram between A and B. Second: t_B/A = moment of M/EI area about B. For cantilever with UDL: t = wL⁴/(8EI) at free end.

**Q12:** What is the weir formula for a V-notch? Derive it.
> **Expected:** dQ = (2/3)√(2g) × tan(θ/2) × h^(5/2) dh. Integrate: Q = (8/15)C_d√(2g)tan(θ/2)H^(5/2). For 90° V-notch: Q = 1.36H^(5/2).

---

## 📊 Scorecard Template

Use this after each mock interview:

| Question | Correct? | Confidence (1–5) | Time (sec) | Notes |
|----------|----------|-------------------|------------|-------|
| Q1 | | | | |
| Q2 | | | | |
| ... | | | | |
| **Total** | **/12** | **Avg: _** | | |

**Post-Mock Checklist:**
- [ ] All questions answered
- [ ] Time per question < 90 sec (technical)
- [ ] Used equations/diagrams in answers
- [ ] Mentioned real-world applications
- [ ] Asked follow-up questions to interviewer
- [ ] Reviewed incorrect answers and noted gaps

---

## 🔗 Cross-Links

- [`technical-interview-bank.md`](technical-interview-bank.md) — 100 Q&A by topic
- [`mock-interview-questions.md`](mock-interview-questions.md) — 50 standalone questions
- [`behavioral-interview-guide.md`](../behavioral/behavioral-interview-guide.md) — STAR format guide
- [`software-interview-guide.md`](../software-interview-guide.md) — Software Q&As
- [`quick-revision-system.md`](../quick-revision-system.md) — Revision plans
- [`project-discussion.md`](../technical/project-discussion.md) — Project defense guide

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 1.0 — Mock Interview Database (8 Sessions)

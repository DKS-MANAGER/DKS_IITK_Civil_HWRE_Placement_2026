# Mock Interview Questions — 50 Questions with Answers

> **How to use:** Practice answering aloud. Time yourself: 60-90 sec for technical, 90-120 sec for behavioral. Record and review.

---

## 🔧 Technical Questions (25 Questions)

### Fluid Mechanics & Hydraulics

**Q1: Derive Bernoulli's equation from Euler's equation. State all assumptions.**
**Answer:** Start with Euler's equation along a streamline: dP/ρ + VdV + gdz = 0. Integrate: P/ρ + V²/2 + gz = constant. Divide by g: P/γ + V²/2g + z = constant. Assumptions: steady, incompressible, inviscid, along streamline. For real flows, add head loss term h_L.

**Q2: What is the physical significance of Reynolds number? When does transition occur?**
**Answer:** Re = ρVD/μ = inertial forces / viscous forces. Re < 2000: laminar (viscous dominates). 2000 < Re < 4000: transition. Re > 4000: turbulent (inertial dominates). Transition depends on surface roughness, inlet conditions, disturbances.

**Q3: Explain the Moody diagram. How do you find friction factor for a given pipe?**
**Answer:** Moody diagram plots Darcy friction factor f vs Re for various relative roughness ε/D. Laminar: f = 64/Re (exact). Transition: Colebrook-White equation (implicit). Fully turbulent: f depends only on ε/D. For given Re and ε/D, read f from chart or use Swamee-Jain explicit formula.

**Q4: What is NPSH and why is it critical for pump selection?**
**Answer:** NPSH_A = P_atm/γ - P_v/γ - h_s - h_f (available). NPSH_R = required by pump (from manufacturer). Must have NPSH_A > NPSH_R to prevent cavitation. Cavitation causes vibration, noise, efficiency loss, impeller damage.

**Q5: A pipe (L=500m, D=0.3m, f=0.02) carries water at Q=0.1 m³/s. Find head loss and power required.**
**Answer:** V = Q/A = 0.1/(π×0.3²/4) = 1.41 m/s. h_f = f(L/D)(V²/2g) = 0.02×(500/0.3)×(1.41²/19.62) = 3.38 m. P = γQH/η = 9810×0.1×3.38/0.75 = 4.42 kW (assuming η=75%).

---

### Open Channel Flow

**Q6: Derive the conjugate depth equation for a hydraulic jump in a rectangular channel.**
**Answer:** From momentum equation: y₂/y₁ = ½[√(1+8Fr₁²)-1]. Derivation: F₁ = F₂ → ρgy₁²/2 + ρQ²/(by₁) = ρgy₂²/2 + ρQ²/(by₂). Substitute Fr₁² = Q²/(gby₁³). Solve quadratic for y₂/y₁.

**Q7: What is specific energy? For a rectangular channel with q=2 m²/s, find critical depth and minimum specific energy.**
**Answer:** E = y + q²/2gy². At critical depth: dE/dy = 0 → y_c = (q²/g)^(1/3) = (4/9.81)^(1/3) = 0.74 m. E_min = 1.5y_c = 1.11 m.

**Q8: Classify GVF profiles. When does M1 profile occur?**
**Answer:** Profiles classified by slope (Mild/Steep/Critical/Horizontal/Adverse) and zone (1: y>y_n,y_c; 2: between; 3: y<y_n,y_c). M1: mild slope, y > y_n > y_c. Occurs upstream of dam/weir (backwater curve).

**Q9: A rectangular channel (b=5m) carries Q=20 m³/s at y=1.2m. Find Froude number and flow regime.**
**Answer:** V = Q/(by) = 20/(5×1.2) = 3.33 m/s. Fr = V/√(gy) = 3.33/√(9.81×1.2) = 0.97. Fr < 1 → subcritical flow.

**Q10: What is Manning's equation? What are its limitations?**
**Answer:** V = (1/n)R^(2/3)S^(1/2). Empirical, n varies with depth/roughness, assumes uniform flow, less accurate for very shallow/rough channels. Darcy-Weisbach is more theoretically grounded.

---

### Hydrology & Groundwater

**Q11: What is a unit hydrograph? What are its two key assumptions?**
**Answer:** UH = direct runoff hydrograph from 1 unit (1 cm) of effective rainfall uniformly distributed over catchment for specified duration. Assumptions: (1) Linearity - runoff proportional to rainfall, (2) Time-invariance - response same regardless of when rain occurs.

**Q12: Explain the Muskingum routing method. What do K and X represent?**
**Answer:** Channel routing: S = K[XI + (1-X)O]. O₂ = C₀I₂ + C₁I₁ + C₂O₁. K = travel time through reach (hrs). X = weighting factor (0-0.5) for wedge storage. X=0 → level pool; X=0.5 → pure translation.

**Q13: Derive the Theis equation for unsteady flow to a well in a confined aquifer.**
**Answer:** From groundwater flow equation: ∂h/∂t = T/S ∇²h. Solution for line source: s = (Q/4πT)W(u), u = r²S/4Tt, W(u) = ∫_u^∞ e^(-x)/x dx. Assumptions: infinite, homogeneous, isotropic, fully penetrating, constant Q.

**Q14: What is the Cooper-Jacob approximation? When is it valid?**
**Answer:** For u < 0.01: s = (2.3Q/4πT)log(2.25Tt/r²S). Plot s vs log t → straight line. Slope gives T, intercept gives S. Valid for large t or small r (late time, near well).

**Q15: A confined aquifer has T=0.001 m²/s, S=0.0001. Well pumps at Q=0.01 m³/s. Find drawdown at r=50m after 1 day.**
**Answer:** u = r²S/4Tt = 50²×0.0001/(4×0.001×86400) = 0.00723. W(u) ≈ -0.5772 - ln(0.00723) = 4.35. s = (0.01/4π×0.001)×4.35 = 3.46 m.

---

### Sediment Transport & Scour

**Q16: What is the Shields parameter? What is its critical value for incipient motion?**
**Answer:** τ* = τ₀/[(ρ_s-ρ)gd] = bed shear stress / submerged weight of particle. Critical τ*_c ≈ 0.047 for uniform grains in clear water. Determines incipient motion.

**Q17: Explain the Meyer-Peter Müller formula for bed load transport.**
**Answer:** q_b* = 8(τ* - τ*_c)^(3/2), where q_b* = q_b/√(Δgd³), Δ = (ρ_s-ρ)/ρ. Valid for τ* > 0.047, coarse non-uniform sediment. Bed load only.

**Q18: What is the Rouse profile? What does the Rouse number indicate?**
**Answer:** c/c_a = (y_a/y)^Z, Z = w_s/(κu_τ). Z > 2.5: sediment near bed (bed load dominant). Z < 0.1: uniform distribution (wash load). 0.1 < Z < 2.5: suspended load.

**Q19: Explain HEC-18 equation for bridge pier scour. What are the correction factors?**
**Answer:** y_s/y₁ = 2.0K₁K₂K₃K₄(a/y₁)^0.35Fr^0.43. K₁: angle of attack, K₂: pier nose shape, K₃: bed condition, K₄: sediment size. a = pier width, y₁ = approach depth.

**Q20: A pier (a=2m) in y₁=4m, Fr=0.5. Estimate scour depth using HEC-18 (assume K=1).**
**Answer:** y_s/4 = 2.0×(2/4)^0.35×0.5^0.43 = 2.0×0.784×0.742 = 1.164. y_s = 4.66 m. Total depth = 8.66 m.

---

### Turbulence & CFD

**Q21: Compare RANS, LES, and DNS. When would you use each?**
**Answer:** RANS: models all scales, cheap, steady design. LES: resolves large eddies, models subgrid, unsteady detailed flows. DNS: resolves all scales, research only. HWRE: RANS for design, LES for scour/jump detail, DNS for research.

**Q22: What is the Boussinesq hypothesis? What are its limitations?**
**Answer:** -ρu_i'u_j' = μ_t(∂u_i/∂x_j + ∂u_j/∂x_i) - 2/3ρkδ_ij. Relates Reynolds stress to mean strain via eddy viscosity. Limitations: assumes isotropic turbulence, scalar μ_t, fails in curvature/rotation/buoyancy.

**Q23: When would you choose k-ω SST over standard k-ε?**
**Answer:** SST for adverse pressure gradients, separation, curved flows (better near-wall). k-ε for high-Re free shear without separation. SST blends k-ω near wall with k-ε in free stream.

**Q24: What is y+ and how do you ensure proper y+ in OpenFOAM?**
**Answer:** y+ = yu_τ/ν. Wall functions: y+ ≈ 30-300. Low-Re: y+ < 5. In OpenFOAM: check y+ with yPlus utility, adjust first cell height, use 15-20 inflation layers, growth ratio 1.1-1.2.

**Q25: How do you validate a turbulence model in OpenFOAM?**
**Answer:** (1) Grid independence (3 meshes, GCI). (2) Compare with experimental data (velocity, pressure, C_f). (3) Monitor y+ compliance. (4) Residuals < 1e-4. (5) Mass conservation (inlet Q = outlet Q). (6) Force coefficients convergence.

---

## 🎭 Behavioral Questions (15 Questions)

**Q26: Tell me about yourself. (Use Present-Past-Future)**
**Answer:** "I'm currently pursuing M.Tech in Civil Engineering (HWRE) at IIT Kanpur, where my thesis focuses on CFD modeling of bridge pier scour using OpenFOAM, validated within 7% accuracy. Previously, I completed B.Tech in Civil Engineering with focus on hydraulics. I'm excited about [Company] because of your work in [specific area], and I'm eager to contribute my CFD expertise and analytical skills to your team."

**Q27: Why do you want to join our company?**
**Answer:** "I've researched [Company]'s recent work on [specific project]. What excites me is [specific aspect]. My thesis on [related topic] directly prepares me for this. Additionally, [Company]'s culture of [value] aligns with my commitment to [related value]."

**Q28: Why are you transitioning from Civil to Analytics/Tech?**
**Answer:** "Civil engineering gave me strong analytical foundations — fluid mechanics, optimization, systems thinking. I discovered these same skills apply powerfully to data problems. My CFD work involves large datasets, statistical validation, Python automation — essentially data science applied to engineering. I've built complementary skills in SQL, Pandas, ML through courses/projects. I'm not leaving civil behind — I'm expanding my toolkit."

**Q29: Describe a time you failed. What did you learn?**
**Answer:** "In a mock GATE test 2 months before the exam, I scored only 35% due to weak hydrology. I created an 8-week focused plan: 50 numericals per weak topic, flashcards, weekly mocks. Improved to 72% and scored 68 in GATE. Failure taught me that structured, targeted effort beats generic preparation."

**Q30: Tell me about a conflict with a teammate and how you resolved it.**
**Answer:** "Two teammates disagreed on turbulence model (k-ε vs SST). I researched both for our case (adverse pressure gradient), presented comparison table with literature, proposed running both for validation. Team chose SST based on evidence, matching data within 8%. Learned that data-driven proposals resolve conflicts better than opinions."

**Q31: Tell me about a time you led a team.**
**Answer:** "I led a 4-member CFD thesis team. Created shared progress tracker, assigned tasks by expertise, set weekly deliverables, daily standups. When mesh divergence hit, I coordinated debugging — mesh refinement, time step reduction, y+ checking. Completed 2 weeks early, presented at department seminar. Leadership taught me clear goals + daily communication prevent most problems."

**Q32: Describe a time you had to make a difficult decision.**
**Answer:** "Mid-project, supervisor changed focus from pipeline to bridge pier scour — 6 weeks to pivot. I chose adaptation: created revised plan in 4 hours, reallocated tasks, started new literature review in 3 days. The pivot led to a stronger conference paper. Difficult decisions require quick analysis and commitment once decided."

**Q33: How do you handle pressure and tight deadlines?**
**Answer:** "During final semester: thesis simulations + placement prep + conference paper in one month. I time-blocked: mornings for automated thesis runs, afternoons for placement prep, evenings for paper writing. Automated data extraction with Python to save time. Completed all three on time. Under pressure, I prioritize ruthlessly and automate what I can."

**Q34: Tell me about a time you had to learn something quickly.**
**Answer:** "Needed MATLAB for a collaboration but only knew Python. Completed MATLAB Onramp in 1 week, practiced 10 exercises, paired with MATLAB-experienced teammate for code reviews. Contributed 3 scripts in first week. Quick learning requires structured courses + hands-on practice + peer support."

**Q35: How do you prioritize when everything is urgent?**
**Answer:** "I use: (1) Impact vs urgency matrix — high-impact + urgent first. (2) Dependencies — what blocks others? (3) Time estimates — quick wins first for momentum. During placement season, I prioritized company-specific prep for the next interview over general revision."

**Q36: What are your strengths and weaknesses?**
**Answer:** "Strengths: (1) Analytical problem-solving — systematically debugged diverging CFD simulation in 3 days. (2) Quick learning — learned MATLAB in 1 week for collaboration. (3) Team leadership — coordinated 4-member team to finish 2 weeks early. Weakness: Overly detail-oriented — once spent extra time perfecting mesh beyond convergence needs. Now set clear 'good enough' criteria upfront."

**Q37: Where do you see yourself in 5 years?**
**Answer:** "In 5 years, I see myself as a senior engineer at [Company], leading water resources/CFD projects independently. I want deep expertise in [specific area] and be mentoring juniors. Long-term, I want to be someone the team relies on for both technical depth and collaborative leadership."

**Q38: Why should we hire you?**
**Answer:** "Three reasons: (1) CFD expertise with OpenFOAM directly aligns with your water resources modeling needs — validated scour models within 7% accuracy. (2) Strong programming skills in Python and data analysis complement technical work. (3) Proven team player — led 4-member project to finish 2 weeks early, mentored juniors in OpenFOAM."

**Q38: What do you know about our company?**
**Answer:** "[Company] is [1-line description]. Recent highlights include [project/news]. Your work in [specific area] is particularly relevant to my thesis on [related topic]. I also noted your [value/initiative]. I'm impressed by [specific detail] and see strong alignment with my skills in [relevant skill]."

**Q40: Do you have any questions for us?**
**Answer:** "Three questions: (1) What does success look like in the first 6 months? (2) What are the biggest challenges the team is currently facing? (3) How does [Company] support professional development? I'm also curious about [specific company initiative]."

---

## 🏢 Company-Specific Questions (10 Questions)

**Q41: For BPCL — Why PSU? How will you handle remote postings?**
**Answer:** "PSUs offer nation-building at scale — my engineering directly impacts millions. I value stability and structured growth. Remote postings are growth opportunities — during B.Tech I visited [site] and found on-site learning invaluable. I'm adaptable and committed."

**Q42: For L&T — What interests you about civil engineering? Describe a challenging design problem.**
**Answer:** "I'm passionate about building infrastructure that serves millions. My thesis on bridge pier scour involved complex fluid-sediment interaction — I validated CFD model against experimental data within 7%, requiring systematic debugging of mesh, turbulence model, and boundary conditions."

**Q43: For AECOM — How do you ensure quality and safety on projects?**
**Answer:** "Quality: IS code compliance, peer reviews, validation against benchmarks, documentation. Safety: risk assessments, method statements, toolbox talks, PPE compliance. My thesis followed ASME V&V standards for CFD validation — systematic grid convergence, experimental comparison, uncertainty quantification."

**Q44: For Barclays — Why civil to analytics? Describe a data-driven decision.**
**Answer:** "Civil engineering trains you to handle complex systems with constraints — exactly what analytics requires. My CFD work: large datasets, statistical validation, Python automation. I automated extraction of 10,000+ data points, built regression models for scour prediction, validated against experimental data. This is data science applied to engineering."

**Q45: For PSU — What are the recent projects of our company?**
**Answer:** "BPCL: Bina refinery expansion, petrochemical complex at Kochi. EIL: overseas projects in Middle East, hydrocarbon sector. NHPC: Subansiri Lower, Teesta-VI hydropower. I've researched these and understand the technical challenges — [specific detail]."

**Q46: For Core Company — What IS codes are you familiar with?**
**Answer:** "IS 456 (RCC), IS 800 (Steel), IS 1893 (Seismic), IS 3370 (Water tanks), IS 456:2000 load combinations (1.5DL+1.5LL, 1.2DL+1.2LL±1.0WL). Also familiar with IRC codes for highways, IS 2911 for piles."

**Q47: For Analytics — How do you explain technical results to non-technical stakeholders?**
**Answer:** "Use analogies and visualizations. For turbulence modeling: 'k-ω SST is like having two thermometers — one near the wall, one in free stream — each measuring turbulence differently.' Focus on business impact: 'This model reduces prediction error by 30%, saving $X in overdesign.'"

**Q48: For Consulting — Market sizing: How many petrol pumps in India?**
**Answer:** "Approach: India population ~1.4B. Vehicles per 1000 people ~50 → 70M vehicles. Avg vehicles per petrol pump per day ~200. Pumps needed = 70M/200 = 350,000. Adjust for urban/rural, utilization → ~80,000-100,000. Actual ~85,000."

**Q49: For any company — What is your expected salary?**
**Answer:** "Based on my research, roles like this at [Company] typically offer [range]. I'm looking for a package reflecting my M.Tech specialization and CFD expertise. However, I'm flexible — role, learning, and growth matter more. I'm confident we can find a mutually agreeable figure."

**Q50: For any company — When can you join?**
**Answer:** "As per IIT Kanpur's placement policy, I can join after [May/June 2027 after thesis submission]. I'm available for pre-joining formalities, documentation, or online onboarding before that. If earlier requirement, I can discuss with my thesis guide about expediting submission."

---

## 📋 Mock Interview Scorecard

| Category | Questions | Target Score |
|----------|-----------|--------------|
| Technical (Fluid/Hydraulics) | 5 | 4/5 |
| Technical (OCF/Hydrology) | 5 | 4/5 |
| Technical (Sediment/CFD) | 5 | 4/5 |
| Behavioral (STAR) | 10 | 8/10 |
| Company-Specific | 5 | 4/5 |
| **Total** | **30** | **24/30** |

**Passing: 24/30 (80%)**

---

## 🎯 Practice Routine

| Day | Focus |
|-----|-------|
| Mon | Technical: Fluid Mechanics + Hydraulics (5 Q) |
| Tue | Technical: OCF + Hydrology (5 Q) |
| Wed | Technical: Sediment + CFD (5 Q) |
| Thu | Behavioral STAR stories (5 Q) |
| Fri | Company-specific (5 Q) |
| Sat | Full mock interview (30 Q, timed) |
| Sun | Review mistakes, update answers |

---

## References

* [`../technical/technical-interview-bank.md`](../technical/technical-interview-bank.md) — 100 technical Q&A
* [`../hr/hr-interview-guide.md`](../hr/hr-interview-guide.md) — HR guide
* [`../../behavioral/behavioral-interview-guide.md`](../../behavioral/behavioral-interview-guide.md) — 30 STAR examples

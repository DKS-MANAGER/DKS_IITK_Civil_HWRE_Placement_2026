# 🧩 Problem-Solving Stories — Personalized Story Bank

> **How to use:** Each story below is a **template**. Replace bracketed items `[YOUR DETAILS]` with YOUR actual experiences. Keep the STAR structure. Time each story to 60-90 seconds when spoken aloud.

---

## Story Categories & Question Mapping

| Story | Covers These Interview Questions |
|-------|----------------------------------|
| Story 1 | "Tell me about a challenging problem you solved" |
| Story 2 | "Tell me about a time you failed and what you learned" |
| Story 3 | "How do you handle pressure and tight deadlines?" |
| Story 4 | "Tell me about a time you had to learn something quickly" |
| Story 5 | "How do you prioritize when everything is urgent?" |
| Story 6 | "Describe a time you found a creative solution" |
| Story 7 | "Tell me about a time you had to make a decision with incomplete information" |
| Story 8 | "Describe your problem-solving process" |
| Story 9 | "Tell me about a time you used data to solve a problem" |
| Story 10 | "How do you approach complex, ambiguous problems?" |

---

## 📝 Story 1: Debugging a Diverging CFD Simulation

**Situation:**
Our pipeline scour simulation at IIT Kanpur was diverging after 500 time steps, producing unphysical sediment concentrations. We had 1 week to fix it for our project deadline.

**Task:**
Systematically identify and fix the divergence issue — without randomly changing parameters.

**Action:**
1. Created a structured debugging checklist — boundary conditions, time step, under-relaxation, mesh quality, solver settings
2. Checked boundary conditions — correct. Halved time step — still diverged. Added under-relaxation — marginal improvement.
3. Investigated mesh quality — discovered y+ values near the pipe were 300+ (should be <5 for low-Re turbulence model)
4. Refined boundary layer mesh to achieve y+ ≈ 1 with 15 inflation layers
5. Re-ran — simulation converged and completed in 3 days

**Result:**
Published the validated results. The debugging checklist became lab standard. Systematic debugging beats random trial-and-error every time.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 2: Recovering from a GATE Mock Test Failure

**Situation:**
Two months before GATE, I scored only 35% in a mock test due to weak performance in hydrology and structural analysis. I was disappointed and demotivated.

**Task:**
Improve significantly in 2 months while still managing coursework — target 70%+ in the final mock.

**Action:**
1. Analyzed the mock — identified exact weak areas: hydrology (unit hydrographs, routing) and structures (deflection methods)
2. Created a focused 8-week study plan — 2 hours/day on weak topics, 1 hour on aptitude
3. Used targeted practice — solved 50 numericals per weak topic, created flashcards for formulas
4. Took weekly mock tests to track improvement and adjust focus
5. Formed a study group for accountability — we quizzed each other daily

**Result:**
Improved to 72% in the final mock. Scored 68 marks in GATE, qualifying for interviews at 3 PSUs. Failure taught me that structured, targeted effort beats generic preparation.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 3: Juggling Thesis, Placements, and Paper

**Situation:**
During final semester at IIT Kanpur, I had to complete CFD simulations for my thesis, prepare for placement interviews, and submit a conference paper — all within the same month.

**Task:**
Manage all three commitments without compromising quality on any of them.

**Action:**
1. Created a daily time-block schedule — mornings for thesis simulations (automated runs), afternoons for placement prep, evenings for paper writing
2. Automated repetitive tasks — wrote Python scripts for data extraction from OpenFOAM output, saving 2 hours/day
3. Set non-negotiable milestones — thesis simulations done by Week 1, paper draft by Week 2, interview prep ongoing
4. Used dead time effectively — reviewed flashcards during commute, practiced behavioral answers while waiting for simulations
5. Maintained a weekly review — every Sunday, assess progress and adjust the next week

**Result:**
Completed all three on time — thesis submitted, paper accepted at conference, received 2 placement offers. Under pressure, I prioritize ruthlessly and automate what I can.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 4: Learning MATLAB in One Week

**Situation:**
Our company collaboration project at IIT Kanpur required MATLAB programming for signal processing. I had only used Python before and had zero MATLAB experience.

**Task:**
Learn MATLAB basics in 1 week to contribute meaningfully to the project.

**Action:**
1. Completed MATLAB Onramp (free MathWorks official course) in 2 days
2. Practiced with 10 exercises focusing on matrix operations, plotting, and file I/O
3. Referenced senior's code for project-specific functions and coding style
4. Paired with a MATLAB-experienced teammate for code reviews on my first 3 scripts
5. Immediately applied learning to project tasks — best way to solidify new skills

**Result:**
Contributed 3 MATLAB scripts for data analysis within the first week. By project end, I was proficient enough to debug others' code. Quick learning requires structured courses + hands-on practice + peer support.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 5: Prioritizing Under Overwhelming Demand

**Situation:**
During placement season at IIT Kanpur, I had 5 companies visiting in 2 weeks, each requiring different company-specific preparation, while my thesis simulations were still running.

**Task:**
Prioritize effectively — prepare for the most impactful interviews first while keeping thesis on track.

**Action:**
1. Applied impact-urgency matrix — mapped each company by offer probability (referral strength, past selection rate) vs. preparation needed
2. Identified dependencies — thesis simulations ran overnight unattended, so daytime was fully available for prep
3. Focused on quick wins first — completed company-specific research for the first interview, then built reusable behavioral answers
4. Automated thesis monitoring — Python script to check simulation status and send alert on completion or divergence
5. Adjusted daily based on results — after each interview, reassessed remaining priorities

**Result:**
Cleared aptitude rounds in 4 out of 5 companies. Received 2 offers. Thesis completed on schedule. Clear prioritization prevents burnout and maximizes outcomes.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 6: Creative Visualization Solution

**Situation:**
We needed to visualize 3D flow field data from OpenFOAM for a journal submission, but ParaView was crashing on our lab computers due to memory limitations with large datasets.

**Task:**
Find an alternative way to generate publication-quality figures from large CFD datasets.

**Action:**
1. Identified the root cause — ParaView loaded entire 3D dataset into memory (8GB+), exceeding our 16GB lab machines
2. Designed a workaround — wrote a Python script using numpy and matplotlib to extract data along specific lines and planes
3. Implemented batch processing — the script handled multiple time steps automatically
4. Added customization — line styles, color maps, axis formatting matching journal requirements
5. Optimized memory — processed one plane at a time, wrote to disk immediately

**Result:**
Reduced visualization time from 2 hours (ParaView, when it worked) to 10 minutes (Python script). Produced higher-resolution figures for our journal submission. Creative solutions often come from constraints.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 7: Decision with Incomplete Information

**Situation:**
During our CFD project at IIT Kanpur, we had to choose between SedFoam and sedExnerFoam for sediment transport modeling. Both had limited documentation, and we had 2 days to decide.

**Task:**
Recommend a solver to the team within 2 days — with imperfect information.

**Action:**
1. Ran quick test cases with both solvers on a simple flat-bed problem (2 hours each)
2. Compared computational cost, convergence behavior, and accuracy against analytical solutions
3. Consulted with a PhD student experienced in OpenFOAM for practical insights
4. Checked literature support — SedFoam had 3x more published validations
5. Made recommendation with confidence levels — "SedFoam based on convergence and literature support, with 90% confidence"

**Result:**
Recommended SedFoam — our final results matched experimental data within 5%. The recommendation proved correct. When information is incomplete, test what you can, consult experts, and make data-driven decisions.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 8: My Problem-Solving Framework

> **Use this when asked "Describe your problem-solving process" or "How do you approach problems?"**

**Situation:**
This is my general framework, applied across multiple projects at IIT Kanpur.

**Task:**
I use a consistent 5-step approach to any complex problem.

**Action:**
1. **Define clearly** — "What exactly is the problem? What does success look like? What are the constraints?"
2. **Break down** — Decompose into smaller, testable components. "What are the sub-problems?"
3. **Prioritize** — Which component has the highest impact? Which is the most likely root cause?
4. **Test systematically** — Change one variable at a time. Document what works and what doesn't.
5. **Validate** — Once solved, verify the fix works under different conditions. Document for future reference.

For example, when our CFD simulation diverged: I defined the problem (unphysical concentrations after 500 steps), broke it down (BCs, time step, mesh, solver), prioritized (mesh quality most likely), tested (found y+ = 300), and validated (ran sensitivity study).

**Result:**
This framework has worked across debugging code, resolving team conflicts, and preparing for interviews. Structure turns overwhelming problems into manageable steps.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 9: Data-Driven Problem Resolution

**Situation:**
Our reservoir routing assignment at IIT Kanpur produced results that didn't match the professor's expected values. The class average was off by 20%.

**Task:**
Identify the source of the systematic error — was it the method, the input data, or a calculation mistake?

**Action:**
1. Compared my calculation step-by-step with a classmate's — found we both made the same error
2. Traced back to the source — we were using an incorrect Muskingum coefficient (K = travel time instead of lag time)
3. Verified from Chow's textbook — confirmed the correct definition
4. Created a comparison table showing the difference between the two definitions
5. Shared with 5 classmates before the submission deadline

**Result:**
All 5 classmates corrected their calculations. The professor acknowledged the common mistake in the next class. Data-driven verification and knowledge-sharing prevent systematic errors.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 10: Handling Ambiguity

**Situation:**
Our company collaboration project at IIT Kanpur had vague requirements — "build a flood prediction model" with no specific data sources, accuracy targets, or delivery timeline specified.

**Task:**
Turn ambiguous requirements into a clear project plan.

**Action:**
1. Listed assumptions — data source (IMD rainfall + CPCB river levels), accuracy target (>80% for 24-hr prediction), timeline (6 weeks)
2. Shared assumptions with the company contact for validation — they confirmed 2 of 3 and corrected the data source
3. Created a phased plan — Phase 1: data collection & cleaning (1 week), Phase 2: model development (3 weeks), Phase 3: validation & deployment (2 weeks)
4. Set check-in milestones — weekly demo to the company contact for course correction
5. Built in flexibility — chose modular architecture so components could be swapped if requirements changed

**Result:**
Delivered a working flood prediction model in 6 weeks. The company contact praised the structured approach to ambiguous requirements. When facing ambiguity, clarify assumptions early, validate with stakeholders, and build flexibility into your plan.

⏱️ **Target time: 75 seconds**

---

## 🔗 Cross-Links

- [`../conflict_resolution/conflict-resolution.md`](../conflict_resolution/conflict-resolution.md) — Conflict resolution stories
- [`../behavioral-interview-guide.md`](../behavioral-interview-guide.md) — STAR framework reference
- [`../question-master-database.md`](../question-master-database.md) — All problem-solving questions
- [`../strategies/answering-strategies.md`](../strategies/answering-strategies.md) — CARL framework

---

## References

* [awesome-behavioral-interviews](https://github.com/arialdomartini/awesome-behavioral-interviews)
* [behavioral-interview-list-of-questions](https://github.com/rShearer/behavioral-interview-list-of-questions)

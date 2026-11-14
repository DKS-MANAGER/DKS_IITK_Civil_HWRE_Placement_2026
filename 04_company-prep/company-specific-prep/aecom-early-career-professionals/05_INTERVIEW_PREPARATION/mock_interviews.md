# Full Simulated Mock Interviews: Technical Lead, Principal Modeler & HR Director
**Candidate Background:** M.Tech Civil Engineering (Hydraulics & Water Resources Engineering — HWRE), IIT Kanpur  
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** 3-Round Comprehensive Interview Simulation with Scoring Rubrics  

---

## Overview of Interview Pipeline

AECOM's selection process for Early Career Professionals typically comprises three interview stages:
1. **Round 1: Technical Screening & Fundamentals (Technical Lead / Senior Engineer)**  
   *Focus: Fluid mechanics, open channel hydraulics, whiteboard derivations, code familiarity (IRC/IS), thesis probing.*
2. **Round 2: Practical Engineering & Systems Design (Principal Modeler / Practice Leader)**  
   *Focus: Real-world infrastructure scenarios, multi-disciplinary coordination, BIM/GIS workflows, client communication.*
3. **Round 3: Behavioral, Values & Culture Fit (HR Director / Senior Talent Acquisition Partner)**  
   *Focus: AECOM Core Values (Safeguard, Inspire, Innovate, Collaborate, Push boundaries, Deliver), career aspirations, professional ethics.*

---

# ROUND 1: Technical Lead / Senior Hydraulic Engineer (45 Minutes)

**Panel:** Rajesh Sharma (Associate Director — Water & Civil Infrastructure, Gurugram)  
**Candidate:** M.Tech Graduate, IIT Kanpur  
**Setting:** Video Call / Technical Board Room  

### Transcript Excerpt:

**Rajesh Sharma:**  
"Welcome. I’ve looked through your profile. You have an M.Tech in Hydraulics and Water Resources from IIT Kanpur with an undergraduate engineering background. Your research is on numerical modeling of bridge scour using OpenFOAM. Let's start right there.  
In your work, you look at submerged bridge decks. In standard civil engineering practice under IRC:78, we use Lacey's formula to find the regime scour depth. Why do we need 3D CFD when NHAI and Indian Railways have been using Lacey's formula for decades?"

**Candidate:**  
"Thank you, Rajesh. Lacey's formula—$R = 0.473(Q/f)^{1/3}$—was developed in the 1930s based on stable regime canals in the Indo-Gangetic alluvial plains. It provides an empirical regime depth for an unconstricted alluvial river under normal open-channel flow.  
However, when a 100-year flood crests above the lower chord of a bridge deck, the flow changes physics: it transitions from free-surface open-channel flow to **pressurized orifice flow**. The bridge deck acts as a downward-deflecting sluice, creating intense vertical flow contraction and shedding high-energy vortices beneath the soffit. This can accelerate local bed shear stress up to nearly 4 times the critical Shields threshold. Lacey's formula simply has no mathematical parameter to account for deck submergence ratio ($S/y_0$), deck geometry, or bridge deck blockage ratio ($B/y_0$). In our OpenFOAM simulations validated against flume ADV measurements, we demonstrated that empirical 1D methods can underestimate local scour beneath submerged decks by up to $35\%$, which is a major safety risk."

**Rajesh Sharma:**  
*(Nodding)* "Good physical distinction. Now, let's test your first principles. Walk over to the whiteboard. Derive the Belanger sequent depth equation for a classical hydraulic jump in a rectangular channel. Tell me your assumptions first."

**Candidate:**  
"Certainly. For a horizontal rectangular channel of width $B$, we define a control volume enclosing the jump between pre-jump Section 1 (depth $y_1$, velocity $V_1$) and post-jump Section 2 (depth $y_2$, velocity $V_2$).  
Our key assumptions are:
1. The bed is horizontal ($S_0 = 0$).
2. The length of the jump is short, so boundary shear friction force on the bed is negligible ($F_f \approx 0$).
3. Velocity is uniform across sections ($\beta_1 = \beta_2 = 1.0$).
4. Pressure distributions at Sections 1 and 2 are hydrostatic.

Applying linear momentum conservation:
$$\sum F_x = P_1 - P_2 = \dot{m}(V_2 - V_1)$$
where $P_1 = \frac{1}{2}\gamma B y_1^2$ and $P_2 = \frac{1}{2}\gamma B y_2^2$, and mass flow rate $\dot{m} = \rho Q = \rho B q$.  
Substituting:
$$\frac{1}{2}\gamma B y_1^2 - \frac{1}{2}\gamma B y_2^2 = \rho B q (V_2 - V_1)$$
Dividing by $\gamma B = \rho g B$:
$$\frac{1}{2}(y_1^2 - y_2^2) = \frac{q}{g}(V_2 - V_1)$$
Using continuity, $V = q / y$:
$$\frac{1}{2}(y_1 - y_2)(y_1 + y_2) = \frac{q^2}{g}\left(\frac{y_1 - y_2}{y_1 y_2}\right)$$
Since $y_1 \ne y_2$, we divide both sides by $(y_1 - y_2)$:
$$y_1 y_2 (y_1 + y_2) = \frac{2q^2}{g}$$
Now, dividing both sides by $y_1^3$ to express in terms of the depth ratio $\eta = y_2 / y_1$:
$$\frac{y_2}{y_1}\left(1 + \frac{y_2}{y_1}\right) = \frac{2q^2}{g y_1^3} = 2\left(\frac{V_1^2}{g y_1}\right) = 2 Fr_1^2$$
$$\eta^2 + \eta - 2Fr_1^2 = 0$$
Solving the quadratic equation for the positive physical root:
$$\frac{y_2}{y_1} = \frac{-1 + \sqrt{1 + 8Fr_1^2}}{2} = \mathbf{\frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right)}$$
This proves that the sequent depth ratio depends purely on the upstream Froude number $Fr_1$."

**Rajesh Sharma:**  
"Airtight derivation. Now, suppose $Fr_1 = 1.0$. What does the formula give?"

**Candidate:**  
"If $Fr_1 = 1.0$, $\sqrt{1 + 8(1)} = \sqrt{9} = 3$. Then $\frac{1}{2}(3 - 1) = 1.0$. So $y_2 / y_1 = 1.0$, meaning critical flow without a jump—confirming the boundary check."

**Rajesh Sharma:**  
"Excellent. Now, let's talk about water hammer in pipelines. You have a $1200\text{ m}$ pipeline flowing at $2.5\text{ m/s}$ with wave celerity $a = 1000\text{ m/s}$. If a valve closes in $1.8\text{ seconds}$, what is the pressure head rise?"

**Candidate:**  
"First, we calculate the pipeline reflection period:
$$T_r = \frac{2L}{a} = \frac{2 \times 1200}{1000} = 2.4\text{ seconds}$$
Since the valve closure time $t_c = 1.8\text{ s}$ is strictly less than $T_r = 2.4\text{ s}$, this is classified as **rapid / instantaneous closure**.  
The reflected decompression wave from the reservoir cannot reach the valve before it is completely shut. Therefore, the full Joukowsky pressure surge develops:
$$\Delta H = \frac{a V_0}{g} = \frac{1000 \times 2.5}{9.81} \approx 254.8\text{ meters}$$
This would almost certainly rupture an unreinforced ductile iron or mild steel pipe unless an air vessel, surge tank, or quick-opening relief valve is installed."

**Rajesh Sharma:**  
"Very clear. Thank you. That completes our technical fundamentals."

---

### Round 1 Evaluation Rubric:
- **First-Principles Understanding:** $5 / 5$ (Flawless momentum derivation, exact assumptions).
- **Physical Intuition:** $5 / 5$ (Distinguished Lacey's regime flow from pressurized orifice flow).
- **Code & Hydraulic Safety:** $5 / 5$ (Quickly recognized rapid closure criteria and surge implications).
- **Recommendation:** **Strong Hire — Proceed to Round 2**.

---

# ROUND 2: Principal Modeler / Water Practice Leader (45 Minutes)

**Panel:** Priya Menon (Director of Water Resources & Digital Delivery, Bengaluru GDC)  
**Candidate:** M.Tech Graduate, IIT Kanpur  
**Setting:** Video Call / Technical Case Study Review  

### Transcript Excerpt:

**Priya Menon:**  
"Hello. In Round 1, Rajesh tested your theoretical mechanics. In Round 2, I want to see how you think like a consulting engineer delivering real projects for international and domestic clients.  
Let’s consider a project: AECOM is designing a multi-modal transport hub for a high-speed rail interchange on a 20-hectare site. The local authority has a strict rule: post-development peak stormwater discharge cannot exceed pre-development peak discharge for a 10-year storm. Currently, the site is farmland. Post-development, it will be 70% impervious roofs and asphalt. Walk me through your design approach."

**Candidate:**  
"This is a classic Sustainable Drainage Systems (SuDS) attenuation and Water Sensitive Urban Design (WSUD) challenge.  
Here is my structured approach:
1. **Hydrological Baseline Estimation:**
   - Pre-development: Runoff coefficient $C_{\text{pre}} \approx 0.20$ (agricultural soil). With $A = 20\text{ ha}$, we calculate time of concentration $t_{c,\text{pre}}$ and rainfall intensity $I_{10}$ from regional IDF curves to find allowable baseline peak flow:
     $$Q_{\text{allowable}} = \frac{C_{\text{pre}} I_{10} A}{360}$$
   - Post-development: Composite $C_{\text{post}}$ will jump to roughly $0.75 - 0.85$, and $t_c$ will decrease drastically, accelerating and amplifying peak runoff by $4$ to $5$ times.

2. **Hierarchical SuDS Implementation (Source to Regional Control):**
   - **Source Control:** Mandate green roofs on station buildings ($80\text{ mm}$ substrate) to retain the first $15\text{ mm}$ of rainfall via evapotranspiration. Install permeable interlocking concrete pavements (PICP) on parking aprons with a crushed aggregate sub-base.
   - **Conveyance Control:** Replace concrete gutters with roadside vegetated bioswales to filter heavy metals, trap sediment, and slow the time of concentration.
   - **Site Control (Attenuation Basin):** Size an engineered stormwater detention basin to store the hydrograph difference between post-development inflow and allowable pre-development discharge over the critical storm duration.

3. **Hydraulic Throttle & Safety Sizing:**
   - Install a vortex flow control device or calibrated orifice plate at the basin outlet to strictly restrict outflow to $Q_{\text{allowable}}$ at maximum design head.
   - Design a broad-crested emergency spillway weir with $0.5\text{ m}$ freeboard to safely pass the 100-year storm without overtopping basin bunds.

4. **Digital Delivery in Civil 3D & EPA-SWMM:**
   - Model the overland grading in Civil 3D, export catchment surfaces to EPA-SWMM using Dynamic Wave routing, and verify that no localized ponding or pipe surcharge occurs during 25-year and 50-year check storms."

**Priya Menon:**  
"Good multi-tiered response. Now, you mentioned your machine learning risk prediction framework. Machine learning is popular in universities, but in consultancy, clients are wary of 'black-box' models. If an insurance client or highway agency asks: *'Why did your ML model flag this specific bridge as high-risk when our senior inspector says it looks fine?'*, how do you defend that?"

**Candidate:**  
"That is the exact reason we implemented **TreeSHAP (SHapley Additive exPlanations)** grounded in cooperative game theory rather than treating XGBoost as a black box.  
I would open the bridge's local SHAP waterfall plot and explain:
*'Our inspection model does not replace your senior inspector; it augments their assessment with hydraulic hazard data they cannot see from the deck. For this specific bridge, the model identified three compounding risk factors:
First, historical flood data shows the approach flow attacks the pier at a $22^\circ$ skew angle, which triples the effective pier width and intensifies the downward horseshoe vortex.
Second, the riverbed material has a very low critical shear stress ($\tau_c = 0.28\text{ N/m}^2$), meaning fine sand will entrain rapidly during a 10-year flood.
Third, your foundation records indicate shallow well embedment of only 5 meters, which is less than 0.8 times the Lacey regime scour depth.
The SHAP plot proves these three physical parameters contributed $+64\%$ to the failure probability score.'*
By translating the ML decision into verifiable hydraulic and geotechnical metrics, the client sees that the model is rooted in physical reality."

**Priya Menon:**  
"Impressive. Last question: In our Bengaluru GDC, we work to Eurocodes and British Standards for UK clients. Have you ever worked with international codes, and how will you adapt?"

**Candidate:**  
"During my coursework and thesis, while our baseline was Indian Standards (IS/IRC), I regularly benchmarked our scour and hydraulic calculations against US FHWA HEC-18 and CIRIA C753 SuDS guidelines. The core physics—conservation of mass, momentum, and energy—does not change across borders. The difference lies in load combinations, material partial safety factors, and formatting. I am eager to master Eurocode 2 for concrete and Eurocode 7 for geotechnics, and my strong foundation in first-principles mechanics makes code cross-walking straightforward."

---

### Round 2 Evaluation Rubric:
- **Practical Engineering Judgment:** $5 / 5$ (Structured SuDS design, source control to basin).
- **Digital & Analytics Defense:** $5 / 5$ (Mastery of explainable AI / SHAP in engineering terms).
- **Adaptability to Global Standards:** $4.8 / 5$ (Clear understanding of physics vs code partial factors).
- **Recommendation:** **Strong Hire — Proceed to HR Round**.

---

# ROUND 3: HR Director / Talent Acquisition Partner (30 Minutes)

**Panel:** Sunita Rao (Director — People & Culture, AECOM India)  
**Candidate:** M.Tech Graduate, IIT Kanpur  
**Setting:** Video Call / Cultural & Competency Interview  

### Transcript Excerpt:

**Sunita Rao:**  
"Hello! Congratulations on clearing the technical panels. In this conversation, I want to understand who you are as a professional, how you handle workplace challenges, and whether AECOM's culture is the right environment for you.  
Let’s start with our core value: **Safeguard**. AECOM has a strict zero-harm safety culture. Give me an example from your life where you observed something unsafe and took personal responsibility to fix it."

**Candidate:**  
*(Delivers STAR response from Question 1 of Behavioral Guide: Halting flume pump at IIT Kanpur upon discovering cavitation micro-fissures in high-pressure flexible coupling, coordinating repair before resuming testing).*

**Sunita Rao:**  
"Thank you. Now, let’s talk about career choices. You are graduating with a Master's degree from IIT Kanpur. Many of your peers target software development firms, data science startups, or public sector PSUs offering high initial packages. Why did you choose to build your career in civil infrastructure consultancy at AECOM?"

**Candidate:**  
"For me, it comes down to passion and tangible impact. I chose civil engineering in my undergraduate studies and pursued my Master’s in Hydraulics at IIT Kanpur because I am fascinated by how water interacts with built infrastructure. Software startups write apps, but civil engineers build the bridges, transit corridors, and clean water networks that protect societies from natural disasters and drive national economies.  
AECOM represents the global pinnacle of that mission. Here, I can apply computational modeling and data science to real-world infrastructure. In 10 years, I want to point to a bridge or flood protection scheme and know that my calculations kept that community safe."

**Sunita Rao:**  
"That passion is wonderful to hear. What if you are assigned to a project where you have to do repetitive CAD drafting or checking calculation spreadsheets for the first 6 months? Would you feel underutilized?"

**Candidate:**  
"Not at all. Every great consulting engineer starts by understanding the drawing standards, detailing conventions, and QA/QC checking protocols of their firm. You cannot design a landmark viaduct or an advanced drainage network if you do not understand how drafting sheets and bar-bending schedules are constructed. I view foundational work as essential grounding. Furthermore, I always look for ways to streamline repetitive workflows—for example, by writing Python scripts to automate data entry—creating value for the team while mastering the basics."

**Sunita Rao:**  
"The placement proforma lists a CTC of ₹8.5 LPA with a ₹25,000 joining bonus for the ECP profile, with postings in Gurugram or Bengaluru. Do you have any location constraints or compensation concerns?"

**Candidate:**  
"The compensation structure is completely clear as stated in the placement proforma. In terms of location, I am fully mobile and enthusiastic about either office. Gurugram offers incredible frontline exposure to India’s domestic mega-projects like RRTS and smart cities, while Bengaluru offers exposure to global delivery mega-projects. I am ready to deploy wherever AECOM sees the greatest value for my skills."

---

### Round 3 Evaluation Rubric:
- **Safety Mindset & Ethics:** $5 / 5$ (Authentic Stop Work Authority example).
- **Motivation & Industry Alignment:** $5 / 5$ (Compelling, authentic justification for civil infrastructure).
- **Professional Humility & Work Ethic:** $5 / 5$ (Constructive attitude toward foundational tasks).
- **Recommendation:** **Definite Hire — Extend Official BA4 ECP Offer**.

---
*End of Full Simulated Mock Interviews.*

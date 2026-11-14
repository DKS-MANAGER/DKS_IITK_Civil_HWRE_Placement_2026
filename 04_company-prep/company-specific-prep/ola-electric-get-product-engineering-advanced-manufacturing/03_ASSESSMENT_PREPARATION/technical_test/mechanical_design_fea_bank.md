# Question Bank: Mechanical Design & Finite Element Analysis (30 Questions)
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** Rigorous Technical Online Assessment (OA) Standard  

---

### Q1. Bolted Joint Preload & External Load Partitioning
**Question:** A high-tensile M10 bolt (Grade 10.9) clamping an aluminum battery tray bracket is preloaded to $F_i = 30\text{ kN}$. The bolt stiffness is $k_b = 0.5 \times 10^6\text{ N/mm}$ and the clamped aluminum member stiffness is $k_m = 2.0 \times 10^6\text{ N/mm}$. If an external cyclic tensile service load $P = 10\text{ kN}$ is applied, what is the maximum tensile force experienced by the bolt?
- A) $32.0\text{ kN}$
- B) $38.0\text{ kN}$
- C) $40.0\text{ kN}$
- D) $30.0\text{ kN}$ (no change until separation)

- **Topic & Difficulty:** Bolted Joints | Medium
- **Correct Answer:** **A) $32.0\text{ kN}$**
- **Derivation & Relevant Equation:**
  Joint stiffness constant:
  $$C = \frac{k_b}{k_b + k_m} = \frac{0.5}{0.5 + 2.0} = \frac{0.5}{2.5} = 0.20$$
  The bolt absorbs only a fraction $C$ of the external load:
  $$P_{\text{bolt}} = F_i + C \cdot P = 30\text{ kN} + (0.20 \times 10\text{ kN}) = 30 + 2.0 = 32.0\text{ kN}$$
- **Common Misconception:** Adding the entire external load directly to the preload ($30 + 10 = 40\text{ kN}$). Preload partitions between bolt elongation and clamped member decompression.
- **Practical Application:** Protecting battery pack mounting bolts from cyclic fatigue failure.

---

### Q2. Bolted Joint Separation Threshold
**Question:** For the bolted joint in Q1 ($F_i = 30\text{ kN}, C = 0.20$), what minimum external tensile load $P_{\text{sep}}$ will cause complete separation of the clamped joint interfaces?
- A) $30.0\text{ kN}$
- B) $37.5\text{ kN}$
- C) $45.0\text{ kN}$
- D) $150.0\text{ kN}$

- **Topic & Difficulty:** Bolted Joints | Medium
- **Correct Answer:** **B) $37.5\text{ kN}$**
- **Derivation & Relevant Equation:**
  Joint separation occurs when the clamping force on the members reaches zero ($P_{\text{clamped}} = 0$):
  $$P_{\text{clamped}} = F_i - (1 - C) P = 0 \implies P_{\text{sep}} = \frac{F_i}{1 - C}$$
  $$P_{\text{sep}} = \frac{30\text{ kN}}{1 - 0.20} = \frac{30}{0.80} = 37.5\text{ kN}$$
- **Common Misconception:** Assuming separation occurs when external load equals preload ($P = 30\text{ kN}$).
- **Practical Application:** Gasket decompression and IP67 water ingress failure prevention.

---

### Q3. Bolt Tightening Torque Calculation
**Question:** An M8 Grade 8.8 flange bolt ($d = 8\text{ mm}$, proof strength $S_p = 580\text{ MPa}$, tensile stress area $A_t = 36.6\text{ mm}^2$) is to be tightened to $75\%$ of its proof load. If the torque coefficient is $K = 0.20$, what tightening torque $T$ must be programmed into the robotic DC nutrunner?
- A) $15.9\text{ Nm}$
- B) $25.5\text{ Nm}$
- C) $34.2\text{ Nm}$
- D) $42.0\text{ Nm}$

- **Topic & Difficulty:** Fastener Design | Medium
- **Correct Answer:** **B) $25.5\text{ Nm}$**
- **Derivation & Relevant Equation:**
  Proof load: $F_p = A_t \times S_p = 36.6\text{ mm}^2 \times 580\text{ MPa} = 21,228\text{ N}$.
  Preload target: $F_i = 0.75 \times 21,228 = 15,921\text{ N} \approx 15.92\text{ kN}$.
  Tightening torque:
  $$T = K \cdot F_i \cdot d = 0.20 \times 15,921\text{ N} \times 0.008\text{ m} \approx 25.47\text{ Nm} \approx 25.5\text{ Nm}$$
- **Common Misconception:** Forgetting to convert bolt diameter from millimeters to meters when calculating torque in $\text{Nm}$.
- **Practical Application:** Automated DC electric tool calibration on the Futurefactory assembly line.

---

### Q4. Welded Joint Shear Stress
**Question:** A suspension mounting bracket is welded to the tubular chassis using two parallel transverse fillet welds of leg size $h = 6\text{ mm}$ and length $L_w = 50\text{ mm}$ each. If the joint carries an axial tensile force $F = 30\text{ kN}$, what is the average shear stress on the minimum weld throat?
- A) $35.4\text{ MPa}$
- B) $70.7\text{ MPa}$
- C) $100.0\text{ MPa}$
- D) $141.4\text{ MPa}$

- **Topic & Difficulty:** Welded Joints | Medium
- **Correct Answer:** **B) $70.7\text{ MPa}$**
- **Derivation & Relevant Equation:**
  Effective throat thickness: $t_e = h \cos 45^\circ = 0.707 \times 6 = 4.242\text{ mm}$.
  Total throat area for two welds: $A_{\text{throat}} = 2 \times (t_e \times L_w) = 2 \times (4.242 \times 50) = 424.2\text{ mm}^2$.
  $$\tau = \frac{F}{A_{\text{throat}}} = \frac{30,000\text{ N}}{424.2\text{ mm}^2} \approx 70.72\text{ MPa}$$
- **Common Misconception:** Using weld leg size ($h = 6\text{ mm}$) instead of throat thickness ($0.707h$), which underestimates stress by $29.3\%$.
- **Practical Application:** Robotic MIG weld sizing for rear swingarm pivot brackets.

---

### Q5. FEA Element Selection for Thin Sheet-Metal
**Question:** When performing finite element stress analysis on a $1.8\text{ mm}$ thick stamped steel chassis reinforcement bracket, which element type is mathematically most appropriate?
- A) First-order linear 8-node brick elements (HEX8) with one element through the thickness
- B) Second-order 2D shell elements (e.g., SHELL181 / CQUAD8) positioned on the mid-surface
- C) First-order linear 4-node tetrahedral elements (TET4)
- D) 1D Euler-Bernoulli beam elements

- **Topic & Difficulty:** FEA Theory | Medium
- **Correct Answer:** **B) Second-order 2D shell elements positioned on the mid-surface**
- **Derivation & Relevant Equation:**
  Thin structures ($t / L < 0.05$) undergo out-of-plane bending. Solid elements with only 1 layer through the thickness suffer from **shear locking** (spurious shear strain that artificially stiffens the model). Shell elements incorporate Reissner-Mindlin plate theory, capturing pure bending and membrane stresses accurately with minimal degrees of freedom.
- **Common Misconception:** Meshing thin sheet metal with automatic 3D tetrahedrals.
- **Practical Application:** Automotive Body-in-White (BIW) crash and durability simulation.

---

### Q6. Shear Locking in Linear Solid Elements
**Question:** What is "shear locking" in finite element analysis, and how is it eliminated?
- A) Numerical singularity caused by unconstrained rigid body motion; eliminated by adding springs
- B) Artificial parasitic shear strain generated in first-order fully integrated solid elements subjected to bending; eliminated by using quadratic elements or reduced integration with hourglass control
- C) Physical locking of a bolted joint under friction; eliminated by lubrication
- D) Convergence failure in non-linear plasticity solvers

- **Topic & Difficulty:** FEA Numerics | Hard
- **Correct Answer:** **B) Artificial parasitic shear strain generated in first-order fully integrated solid elements subjected to bending; eliminated by using quadratic elements or reduced integration with hourglass control**
- **Practical Application:** Avoiding falsely low displacement and stress predictions in CAE structural validation.

---

### Q7. Stress Singularity vs True Stress Concentration
**Question:** During linear static FEA of an aluminum swingarm, a sharp internal re-entrant corner shows peak Von Mises stress increasing from $280\text{ MPa} \to 420\text{ MPa} \to 650\text{ MPa}$ as mesh size is refined from $2\text{ mm} \to 1\text{ mm} \to 0.5\text{ mm}$. What does this behavior indicate?
- A) The mesh has successfully converged to the true physical stress
- B) A mathematical **stress singularity** exists because the theoretical elasticity solution at a zero-radius sharp corner has infinite stress ($\sigma \propto 1/r^\alpha$); physical tooling fillet radius must be modeled
- C) The material model is experiencing non-linear yield
- D) Contact friction is improperly defined

- **Topic & Difficulty:** FEA Diagnostics | Hard
- **Correct Answer:** **B) A mathematical stress singularity exists; physical tooling fillet radius must be modeled**
- **Practical Application:** Distinguishing non-physical numerical mesh singularities from genuine design stress raisers.

---

### Q8. Natural Frequencies & Resonance Avoidance
**Question:** An electric scooter chassis has its first fundamental torsional natural frequency at $f_1 = 18\text{ Hz}$. At a cruising speed of $60\text{ km/h}$, the tire diameter is $400\text{ mm}$ and the road has periodic surface expansion ripples spaced $900\text{ mm}$ apart. What excitation frequency does the road impart, and does resonance occur?
- A) $f_{\text{road}} = 9.2\text{ Hz}$; No resonance
- B) $f_{\text{road}} = 18.5\text{ Hz}$; Extreme resonance risk ($f_{\text{road}} \approx f_1$)
- C) $f_{\text{road}} = 36.0\text{ Hz}$; Second harmonic resonance
- D) $f_{\text{road}} = 5.5\text{ Hz}$; No resonance

- **Topic & Difficulty:** Vehicle Dynamics & NVH | Medium
- **Correct Answer:** **B) $f_{\text{road}} = 18.5\text{ Hz}$; Extreme resonance risk ($f_{\text{road}} \approx f_1$)**
- **Derivation & Relevant Equation:**
  Speed $v = 60 \times \frac{5}{18} = 16.67\text{ m/s}$.
  Wavelength $\lambda = 0.90\text{ m}$.
  Excitation frequency:
  $$f_{\text{road}} = \frac{v}{\lambda} = \frac{16.67\text{ m/s}}{0.90\text{ m}} = 18.52\text{ Hz}$$
  Since $f_{\text{road}} \approx f_1 = 18\text{ Hz}$, the road ripples will excite the fundamental torsional mode, causing violent chassis shake and loss of rider control.
- **Common Misconception:** Evaluating wheel RPM instead of road wavelength excitation.
- **Practical Application:** Chassis structural stiffening to push $f_1 > 28 - 35\text{ Hz}$.

---

### Q9. Mesh Quality Metrics: Aspect Ratio and Jacobian
**Question:** In high-quality finite element meshing, what does a **Jacobian ratio of less than zero ($J < 0$)** indicate?
- A) An exceptionally distorted or inverted element with negative volume, causing the global stiffness matrix to become singular and solver to abort
- B) Perfect equilateral element shape
- C) The element is experiencing pure compressive strain
- D) High plastic deformation

- **Topic & Difficulty:** FEA Pre-Processing | Medium
- **Correct Answer:** **A) An exceptionally distorted or inverted element with negative volume, causing the global stiffness matrix to become singular and solver to abort**
- **Practical Application:** Automated pre-solver mesh audit in HyperMesh / ANSYS.

---

### Q10. Non-Linear FEA: Geometric Non-Linearity (Large Deflection)
**Question:** Linear static FEA ($[K]\{u\} = \{F\}$) assumes that displacements and rotations are infinitesimally small. When must **Geometric Non-Linearity (NLGEOM / Large Deflection)** be activated in automotive simulation?
- A) When stresses exceed yield strength $S_y$
- B) When structural deflections exceed half the thickness of the part ($w > t/2$), altering internal load paths and membrane stiffness
- C) When contact friction is zero
- D) When materials are linear elastic

- **Topic & Difficulty:** Non-Linear FEA | Medium
- **Correct Answer:** **B) When structural deflections exceed half the thickness of the part ($w > t/2$), altering internal load paths and membrane stiffness**
- **Practical Application:** Snap-through buckling analysis of battery pack bottom underbody shield plates during curb strike.

---

### Q11. Contact Modeling: Penalty Method vs Lagrange Multipliers
**Question:** What is the primary operational trade-off between the **Penalty Method** and the **Lagrange Multiplier Method** in FEA contact mechanics?
- A) Penalty method enforces exact zero penetration; Lagrange allows large penetration
- B) Penalty method uses contact springs allowing small non-physical penetration ($\Delta = F/k$) with fast solver convergence; Lagrange strictly enforces zero penetration ($\Delta = 0$) but increases matrix size and requires more iterations
- C) Penalty method works only for 2D models
- D) Lagrange multipliers cannot model friction

- **Topic & Difficulty:** Contact Mechanics | Hard
- **Correct Answer:** **B) Penalty method uses contact springs allowing small penetration; Lagrange strictly enforces zero penetration but increases matrix size**
- **Practical Application:** Modeling tire-road contact and battery cell-to-case interfaces.

---

### Q12. Design for Assembly (DFA): Boothroyd-Dewhurst Criteria
**Question:** According to Boothroyd-Dewhurst Design for Assembly principles, which of the following is NOT a fundamental question used to determine if a component can be eliminated or combined?
- A) Does the part move relative to all other parts already assembled during normal operation?
- B) Must the part be made of a fundamentally different material from all other parts (e.g., electrical insulation vs structural)?
- C) Must the part be separate to allow assembly or disassembly for servicing?
- D) Is the part painted a different color for aesthetic marketing?

- **Topic & Difficulty:** DFA Engineering | Easy
- **Correct Answer:** **D) Is the part painted a different color for aesthetic marketing?**
- **Derivation & Relevant Equation:**
  The 3 fundamental DFA questions:
  1. Kinematic relative motion required?
  2. Material incompatibility?
  3. Assembly access/servicing necessity?
  If answers are "No", the part should be integrated into adjacent components to reduce assembly cycle time.
- **Practical Application:** Gen 2 chassis redesign reducing part count by $70\%$.

---

### Q13. RBE2 vs RBE3 Multi-Point Constraints
**Question:** In automotive FEA modeling, what is the fundamental difference between an **RBE2** and an **RBE3** element?
- A) RBE2 is a rigid kinematic link that adds artificial infinite stiffness to the connected nodes; RBE3 is an interpolation constraint that distributes forces without adding artificial stiffness
- B) RBE3 is rigid; RBE2 is flexible
- C) RBE2 applies only to thermal problems
- D) RBE3 cannot transfer moments

- **Topic & Difficulty:** FEA Modeling Best Practices | Medium
- **Correct Answer:** **A) RBE2 is a rigid kinematic link adding artificial stiffness; RBE3 distributes forces without adding artificial stiffness**
- **Practical Application:** Using RBE3 to distribute battery pack weight across multiple chassis bolt holes without artificially locking the frame's torsional flex.

---

### Q14. Dynamic Crashworthiness & Energy Absorption
**Question:** In an axial progressive crush rail designed to absorb frontal crash impact energy:
- A) A solid thick bar is optimal because it resists all deformation
- B) A thin-walled tubular box with engineered trigger notches is optimal because it deforms progressively in axisymmetric folding loops, maximizing energy absorbed per unit mass ($EAM$)
- C) The rail must be made of brittle cast iron
- D) Yield strength must be as low as possible

- **Topic & Difficulty:** Crashworthiness | Medium
- **Correct Answer:** **B) A thin-walled tubular box with trigger notches is optimal because it deforms progressively in axisymmetric folding loops**
- **Derivation & Relevant Equation:**
  $$EAM = \frac{\int F(x) \, dx}{m_{\text{rail}}}$$
  Controlled plastic folding loops absorb impact kinetic energy at a steady plateau force, preventing violent deceleration spikes on the battery pack.
- **Practical Application:** Front sub-frame crash box design on electric scooters.

---

### Q15. Ashby Index for Minimum Weight in Bending
**Question:** To minimize the mass of a beam subjected to a specified bending stiffness, the material selection index to maximize is:
- A) $\sigma_y / \rho$
- B) $E^{1/2} / \rho$
- C) $E / \rho$
- D) $K_{IC} / \rho$

- **Topic & Difficulty:** Material Selection | Medium
- **Correct Answer:** **B) $E^{1/2} / \rho$**
- **Derivation & Relevant Equation:**
  Stiffness $S \propto E I \propto E b h^3$. Mass $m = \rho b h L$.
  Expressing $h$ in terms of stiffness and substituting into mass yields:
  $$m \propto L \left(\frac{S}{b}\right)^{1/3} \left(\frac{\rho}{E^{1/2}}\right)$$
  To minimize mass, maximize $M = \frac{E^{1/2}}{\rho}$.
- **Common Misconception:** Using $E/\rho$ (which applies strictly to axial tension/compression rods, not bending beams).
- **Practical Application:** Evaluating aluminum vs magnesium for cast swingarms.

---

### Q16. Fatigue Stress Concentration Factor ($K_f$) vs Geometric ($K_t$)
**Question:** How is the fatigue stress concentration factor $K_f$ related to the theoretical geometric stress concentration factor $K_t$?
- A) $K_f = K_t$ for all materials
- B) $K_f = 1 + q(K_t - 1)$, where $q$ is notch sensitivity ($0 \le q \le 1$)
- C) $K_f = K_t / q$
- D) $K_f = K_t^2$

- **Topic & Difficulty:** Fatigue Design | Easy
- **Correct Answer:** **B) $K_f = 1 + q(K_t - 1)$, where $q$ is notch sensitivity ($0 \le q \le 1$)**
- **Derivation & Relevant Equation:**
  Ductile materials yield locally at a notch root under cyclic strain, blunting the peak stress ($q < 1 \implies K_f < K_t$). Brittle materials have $q \approx 1 \implies K_f \approx K_t$.
- **Practical Application:** Fatigue calculation at keyway slots in motor transmission shafts.

---

### Q17. Thermal Barrier Optimization in Battery Enclosures
**Question:** An engineer must design a thermal barrier sheet between adjacent 4680 battery cells to prevent thermal propagation. Which combination of material thermal properties is optimal?
- A) High thermal conductivity ($k$) and low heat capacity ($c_p$)
- B) Low thermal conductivity ($k < 0.03\text{ W/m}\cdot\text{K}$) and high volumetric heat capacity / phase change latent heat ($L_f$)
- C) High electrical conductivity and high emissivity
- D) Low density and zero thermal resistance

- **Topic & Difficulty:** Thermal Packaging | Easy
- **Correct Answer:** **B) Low thermal conductivity ($k < 0.03\text{ W/m}\cdot\text{K}$) and high volumetric heat capacity / latent heat**
- **Practical Application:** Specifying silica aerogel blankets compliant with AIS-156 Amendment 3.

---

### Q18. Gasket Compression & IP67 Seal Integrity
**Question:** An EPDM elastomeric O-ring gasket of uncompressed diameter $d_0 = 4.0\text{ mm}$ is compressed into a machined groove of depth $h = 2.8\text{ mm}$. What is the percentage gasket squeeze, and is it acceptable for IP67 sealing?
- A) $15\%$; Unacceptable (too loose, water ingress risk)
- B) $30\%$; Acceptable (within optimal $25 - 35\%$ range)
- C) $45\%$; Unacceptable (causes gasket pinch and permanent compression set)
- D) $70\%$; Total seal failure

- **Topic & Difficulty:** Gasket Mechanics | Medium
- **Correct Answer:** **B) $30\%$; Acceptable (within optimal $25 - 35\%$ range)**
- **Derivation & Relevant Equation:**
  $$\text{Squeeze \%} = \frac{d_0 - h}{d_0} \times 100\% = \frac{4.0 - 2.8}{4.0} \times 100\% = \frac{1.2}{4.0} \times 100\% = 30\%$$
- **Common Misconception:** Believing tighter squeeze ($> 50\%$) produces a better seal (excessive squeeze induces plastic shear tearing of the elastomer).
- **Practical Application:** Battery enclosure perimeter hermetic seal design.

---

### Q19. Motor Inverter Heat Sink Sizing
**Question:** A power electronic MOSFET inverter dissipates $\dot{Q} = 250\text{ W}$ of waste heat during hard acceleration. The maximum allowable junction temperature is $T_j = 125^\circ\text{C}$ in ambient air at $T_{\text{amb}} = 45^\circ\text{C}$. If the junction-to-case thermal resistance is $R_{\theta, j-c} = 0.12^\circ\text{C/W}$ and case-to-sink resistance is $R_{\theta, c-s} = 0.08^\circ\text{C/W}$, what is the maximum permissible thermal resistance of the heat sink to air ($R_{\theta, s-a}$)?
- A) $0.12^\circ\text{C/W}$
- B) $0.20^\circ\text{C/W}$
- C) $0.32^\circ\text{C/W}$
- D) $0.10^\circ\text{C/W}$

- **Topic & Difficulty:** Thermal Engineering | Hard
- **Correct Answer:** **A) $0.12^\circ\text{C/W}$**
- **Derivation & Relevant Equation:**
  $$\Delta T = T_j - T_{\text{amb}} = 125 - 45 = 80^\circ\text{C}$$
  $$R_{\theta, \text{total}} = \frac{\Delta T}{\dot{Q}} = \frac{80^\circ\text{C}}{250\text{ W}} = 0.32^\circ\text{C/W}$$
  $$R_{\theta, \text{total}} = R_{\theta, j-c} + R_{\theta, c-s} + R_{\theta, s-a}$$
  $$0.32 = 0.12 + 0.08 + R_{\theta, s-a} \implies R_{\theta, s-a} = 0.32 - 0.20 = \mathbf{0.12^\circ\text{C/W}}$$
- **Common Misconception:** Forgetting intermediate interface resistances ($j-c$ and $c-s$).
- **Practical Application:** Die-cast aluminum motor controller heat sink fin optimization.

---

### Q20. Planetary Gear Bending Stress (Lewis Formula)
**Question:** According to the Lewis gear tooth bending formula, tooth root bending stress is given by $\sigma = \frac{W_t}{b \cdot m \cdot Y}$. To reduce bending stress by $50\%$ without changing gear face width $b$ or transmitted tangential load $W_t$, what parameter must be doubled?
- A) Pressure angle $\phi$
- B) Module $m$ (tooth size)
- C) Rotational speed $N$
- D) Center distance

- **Topic & Difficulty:** Machine Design | Easy
- **Correct Answer:** **B) Module $m$ (tooth size)**
- **Derivation & Relevant Equation:**
  $$\sigma \propto \frac{1}{m}$$
  Doubling gear module $m$ doubles tooth thickness and height, quadrupling section modulus and cutting root bending stress in half.
- **Practical Application:** Planetary reduction gearbox durability in S1 Pro powertrain.

---

### Q21. Modal Effective Mass in Vibration
**Question:** In dynamic modal analysis of a vehicle frame, the "modal effective mass" of a mode indicates:
- A) The physical weight of the finite elements in that mode
- B) The portion of total structural mass excited by uniform base acceleration in a specific translational direction
- C) The mass of the rider and battery pack combined
- D) The virtual mass of surrounding air

- **Topic & Difficulty:** Structural Dynamics | Medium
- **Correct Answer:** **B) The portion of total structural mass excited by uniform base acceleration in a specific translational direction**
- **Practical Application:** Rule of thumb in shaker rig durability: include enough modes to capture $> 90\%$ of cumulative effective mass in each coordinate axis.

---

### Q22. Sub-Modeling Technique in FEA
**Question:** Why is "sub-modeling" used when analyzing stress concentrations around small bolt holes in large chassis frames?
- A) Because the main model cannot solve without sub-models
- B) To run a coarse global model to obtain overall structural stiffness and boundary displacements, and then drive a localized, finely meshed sub-model using those displacements, avoiding an impractically large global mesh
- C) To account for material plasticity without running non-linear solvers
- D) To eliminate contact non-linearities

- **Topic & Difficulty:** Advanced FEA | Medium
- **Correct Answer:** **B) To run a coarse global model for displacements and drive a localized fine sub-model**
- **Practical Application:** Stress audit on 4680 cell terminal tab welds within a 500,000-element pack model.

---

### Q23. Weld Fatigue Classification (Eurocode 3 / IIW FAT Classes)
**Question:** In structural weld fatigue design under International Institute of Welding (IIW) standards, a transverse load-carrying fillet weld is typically assigned a FAT class of $80\text{ MPa}$ ($FAT 80$). What does $FAT 80$ denote?
- A) The weld yields at $80\text{ MPa}$ static stress
- B) The fatigue strength at $2 \times 10^6$ cycles is an alternating stress range $\Delta \sigma = 80\text{ MPa}$ with a $97.7\%$ survival probability
- C) The maximum allowable shear stress under proof load is $80\text{ MPa}$
- D) The weld must be preheated to $80^\circ\text{C}$

- **Topic & Difficulty:** Fatigue Standards | Medium
- **Correct Answer:** **B) Fatigue strength at $2 \times 10^6$ cycles is $\Delta \sigma = 80\text{ MPa}$ with $97.7\%$ survival probability**
- **Practical Application:** Chassis tubular frame weld fatigue life sign-off.

---

### Q24. Pressure Relief Burst Disk Sizing
**Question:** A battery pack has internal free gas volume $V = 15\text{ Liters}$. During a thermal runaway event, venting cells release $Q_{\text{gas}} = 300\text{ Liters/min}$ ($5.0\text{ L/s}$) of hot gas at peak pressure. If the burst disk orifice coefficient is $C_d = 0.62$ and maximum allowable pack pressure is $P = 40\text{ kPa}$ ($0.4\text{ bar}$ gauge), the required burst vent area $A_{\text{vent}}$ is calculated using:
- A) Darcy-Weisbach pipe friction
- B) Incompressible/compressible orifice discharge equation: $Q = C_d A \sqrt{2 \Delta P / \rho}$
- C) Hooke's Law for membranes
- D) Fourier's Law of conduction

- **Topic & Difficulty:** Fluid-Structural Packaging | Medium
- **Correct Answer:** **B) Incompressible/compressible orifice discharge equation: $Q = C_d A \sqrt{2 \Delta P / \rho}$**
- **Practical Application:** Sizing safety burst disks to prevent enclosure rupture under AIS-156.

---

### Q25. Interference (Press) Fit Stresses
**Question:** When a steel rotor hub of inner diameter $d$ is press-fitted onto a shaft with diametral interference $\delta$:
- A) The shaft experiences tensile hoop stress; the hub experiences compressive hoop stress
- B) The shaft experiences compressive interface pressure; the hub experiences tensile hoop stress peaking at its inner bore
- C) Both components experience identical tensile stresses
- D) Shear stress is zero everywhere

- **Topic & Difficulty:** Machine Elements | Medium
- **Correct Answer:** **B) Shaft experiences compressive pressure; hub experiences tensile hoop stress peaking at inner bore**
- **Relevant Equation:**
  Interface pressure: $p = \frac{\delta}{d \left[ \frac{1}{E_h}\left(\frac{d_o^2 + d^2}{d_o^2 - d^2} + \nu_h\right) + \frac{1}{E_s}(1 - \nu_s) \right]}$.
- **Practical Application:** Sizing motor rotor shaft interference fits to transmit peak motor torque without keys.

---

### Q26. Springback Compensation in Stamping Dies
**Question:** In high-strength steel sheet stamping, how do die designers compensate for elastic springback?
- A) Increasing blank lubrication to maximum
- B) Machining the die face with **over-bending** angles and compensating radii calculated from reverse displacement vectors in non-linear stamping simulation
- C) Heating the punch to $1000^\circ\text{C}$
- D) Reducing punch clamping tonnage

- **Topic & Difficulty:** Tooling Design | Easy
- **Correct Answer:** **B) Machining the die face with over-bending angles and compensating radii from stamping simulation**
- **Practical Application:** S1 Gen 2 chassis stamped bracket tooling validation.

---

### Q27. Center of Percussion in Vehicle Suspension
**Question:** In vehicle front suspension design, why is the front wheel axle aligned with the **Center of Percussion** of the front fork assembly?
- A) To maximize steering rake angle
- B) To ensure that abrupt vertical road impact forces transmitted through the axle produce zero instantaneous reaction force at the rider's handlebars (steering pivot)
- C) To eliminate front wheel gyroscopic precession
- D) To reduce tire rolling resistance

- **Topic & Difficulty:** Advanced Dynamics | Hard
- **Correct Answer:** **B) To ensure abrupt road impact forces produce zero reaction force at the handlebars**
- **Derivation & Relevant Equation:**
  $$q = \frac{I_G}{m r_G} + r_G$$
  Impacting the center of percussion produces a pure rotational acceleration about the pivot point with zero translational reaction kick.
- **Practical Application:** Eliminating handlebar vibration kickback over sharp potholes.

---

### Q28. Hydroforming vs Stamping for Tubular Chassis
**Question:** What is the primary engineering advantage of **Internal High-Pressure Tube Hydroforming (IHT)** over traditional stamped-and-welded two-piece clam-shell chassis members?
- A) Eliminates longitudinal weld seams, increases torsional rigidity by $30 - 40\%$, improves dimensional repeatability, and reduces structural weight
- B) Eliminates the need for raw steel tubing
- C) Reduces cycle time to less than 2 seconds
- D) Allows zero wall thickness

- **Topic & Difficulty:** Advanced Manufacturing Design | Medium
- **Correct Answer:** **A) Eliminates longitudinal weld seams, increases torsional rigidity, and reduces weight**
- **Practical Application:** Lightweight automotive chassis frame tubular structures.

---

### Q29. Boundary Layer Mesh Resolution in Thermal-Fluid FEA
**Question:** When simulating airflow over the cooling fins of an electric motor housing, why must prism boundary layer elements have a first-layer height corresponding to $y^+ \approx 1.0$?
- A) To avoid numerical overflow in the structural solver
- B) To directly resolve the viscous and thermal laminar sublayers, accurately calculating the steep temperature gradient $\partial T / \partial y$ and convective heat transfer coefficient $h$ without relying on empirical wall functions
- C) To reduce total mesh element count
- D) To eliminate acoustic turbulence noise

- **Topic & Difficulty:** Thermal-Fluids / CAE | Hard
- **Correct Answer:** **B) To directly resolve viscous and thermal sublayers, accurately calculating heat transfer coefficient $h$**
- **Practical Application:** Air-cooled motor housing and inverter fin optimization.

---

### Q30. Top-Down Modular Vehicle Architecture
**Question:** What is the primary benefit of designing an electric vehicle using a **modular platform architecture** (e.g., Ola Gen 2 / Gen 3)?
- A) Every vehicle variant uses completely custom, non-interchangeable components
- B) Maximizes component sharing (common battery modules, swingarms, suspension pick-up points, MoveOS electronics) across multiple scooter and motorcycle variants, drastically cutting CapEx tooling costs and engineering development time
- C) Eliminates the need for crash testing
- D) Guarantees $100\%$ composite material adoption

- **Topic & Difficulty:** Product Engineering Strategy | Easy
- **Correct Answer:** **B) Maximizes component sharing across multiple variants, cutting CapEx tooling costs and development time**
- **Practical Application:** Ola platform strategy across S1 Pro, S1 Air, S1 X, and Roadster series.

---
*End of Mechanical Design & FEA Question Bank (30 Solved Questions).*

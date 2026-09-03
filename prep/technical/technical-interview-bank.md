# Technical Interview Bank — 100 Q&A by Topic

> **How to use:** Practice 2-layer answers: Concept → Application → Caveat.
> Target: Answer any question in 60–90 seconds with a derivation or example.

---

## 🌊 Fluid Mechanics & Hydraulics (Q1–Q20)

### Q1: Derive Bernoulli's equation and state its assumptions.
**A:** Start from Euler's equation along a streamline: $dP/\rho + VdV + gdz = 0$. Integrate: $P/\rho + V^2/2 + gz = \text{const}$. Divide by $g$: $P/\gamma + V^2/2g + z = \text{const}$. Assumptions: steady, incompressible, frictionless, along a streamline. Add $h_L$ for real flows.

### Q2: What is the physical meaning of each term in Bernoulli's equation?
**A:** $P/\gamma$ = pressure head (flow work per unit weight), $V^2/2g$ = velocity head (kinetic energy), $z$ = elevation head (potential energy). Sum = total head. In real flows, total head decreases downstream due to friction.

### Q3: Explain Reynolds number and its significance.
**A:** $Re = \rho VD/\mu = VD/\nu$ = inertial/viscous forces. $Re < 2000$: laminar (viscous dominates), $2000 < Re < 4000$: transition, $Re > 4000$: turbulent (inertial dominates). Determines flow regime, friction factor, and model similarity.

### Q4: What is the difference between Darcy and Fanning friction factors?
**A:** Darcy $f_D$ in $h_f = f_D(L/D)(V^2/2g)$, Fanning $f_F = f_D/4$. Darcy is standard in civil/hydraulics; Fanning in chemical engineering. Always clarify which is being used.

### Q5: Explain the Moody diagram.
**A:** Plots $f$ vs $Re$ for various $\epsilon/D$. Laminar: $f = 64/Re$. Transition: Colebrook-White. Fully turbulent: $f$ depends only on $\epsilon/D$. Used to find friction factor for pipe design.

### Q6: What is the Hardy Cross method?
**A:** Iterative method for looped pipe networks. Assume flows satisfying continuity, compute head loss per loop, apply correction $\Delta Q = -\sum h_f / \sum|h_f/Q|$, iterate until $\sum h_f < \epsilon$. Converges for moderate networks.

### Q7: What is NPSH and why does it matter?
**A:** Net Positive Suction Head: $NPSH_A = P_{atm}/\gamma - P_v/\gamma - h_s - h_f$. Must have $NPSH_A > NPSH_R$ to prevent cavitation. If violated, vapor bubbles form and collapse, damaging the pump.

### Q8: Explain specific speed and its use in pump selection.
**A:** $N_s = N\sqrt{Q}/H^{3/4}$. Classifies pump type: low $N_s$ (10–35) → Pelton/radial, medium (30–100) → Francis/mixed, high (100–300) → Kaplan/axial. Select pump with $N_s$ matching required $Q$ and $H$.

### Q9: What are the affinity laws for pumps?
**A:** For same pump at different speeds: $Q_2/Q_1 = N_2/N_1$, $H_2/H_1 = (N_2/N_1)^2$, $P_2/P_1 = (N_2/N_1)^3$. For different diameters: $Q \propto D^3$, $H \propto D^2$, $P \propto D^5$.

### Q10: What is boundary layer separation and when does it occur?
**A:** Occurs when $\partial P/\partial x > 0$ (adverse pressure gradient). Wall shear $\tau_w = 0$ at separation point, flow reverses and detaches. Causes increased drag, wake formation, and reduced lift. Prevented by streamlining, suction, or blowing.

### Q11: Derive the Hagen-Poiseuille equation.
**A:** For laminar pipe flow: $Q = \pi R^4 \Delta P / (8\mu L)$. Derived from Navier-Stokes with no-slip, steady, fully developed assumptions. Gives parabolic velocity profile $u(r) = (\Delta P/4\mu L)(R^2 - r^2)$.

### Q12: What is the difference between Eulerian and Lagrangian descriptions?
**A:** Eulerian: fixed control volume, observe fluid passing through (used in CFD). Lagrangian: follow individual fluid particles. Eulerian gives field variables $u(x,t)$; Lagrangian gives particle trajectories $x(t)$.

### Q13: Explain dimensional analysis and Buckingham Pi theorem.
**A:** For $n$ variables with $m$ fundamental dimensions, there are $n-m$ dimensionless groups. Used to derive $Re$, $Fr$, $We$, $Ma$ and to design model tests with geometric, kinematic, and dynamic similarity.

### Q14: What is cavitation? How do you prevent it?
**A:** Vapor bubble formation when $P < P_v$, followed by collapse causing erosion and noise. Prevention: ensure $NPSH_A > NPSH_R$, lower pump elevation, reduce suction losses, increase suction diameter, use inducer.

### Q15: What is the momentum equation and its applications?
**A:** $\sum F = \rho Q(V_2 - V_1)$. Applications: force on bends, jet impact on plates, sluice gate forces, hydraulic jump analysis, rocket thrust.

### Q16: Explain drag and lift coefficients.
**A:** $C_D = F_D/(0.5\rho AV^2)$, $C_L = F_L/(0.5\rho AV^2)$. $C_D$ includes form + friction drag. $C_L$ from pressure differential. Both depend on $Re$, shape, and angle of attack.

### Q17: What is the difference between steady and unsteady flow?
**A:** Steady: $\partial/\partial t = 0$ at a point (e.g., pipe flow at constant Q). Unsteady: properties vary with time (e.g., flood wave, water hammer). Unsteady requires additional terms in governing equations.

### Q18: What is water hammer and how is it analyzed?
**A:** Pressure surge from sudden valve closure: $\Delta P = \rho c \Delta V$ (Joukowsky). Wave speed $c = \sqrt{E/\rho}/\sqrt{1 + (D/t)(E/E_s)}$. Mitigated by slow valve closure, surge tanks, air chambers.

### Q19: Explain the concept of hydraulic grade line (HGL) and energy grade line (EGL).
**A:** HGL: $P/\gamma + z$ (piezometric head). EGL: $P/\gamma + V^2/2g + z$ (total head). EGL is always above HGL by $V^2/2g$. Both decrease downstream due to losses; EGL drops faster.

### Q20: What is the difference between pipe flow and open channel flow?
**A:** Pipe: pressurized, no free surface, driven by pressure gradient, full cross-section. Open channel: free surface at atmospheric pressure, driven by gravity (slope), partially full, Froude number governs regime.

---

## 🌊 Open Channel Flow (Q21–Q35)

### Q21: What is specific energy and critical depth?
**A:** $E = y + V^2/2g = y + Q^2/(2gA^2)$. Critical depth $y_c$ minimizes $E$ for given $Q$: $y_c = (q^2/g)^{1/3}$ for rectangular. At $y_c$: $Fr = 1$, $E_{min} = 1.5y_c$.

### Q22: Explain gradually varied flow (GVF) and its governing equation.
**A:** Depth changes slowly over long distance. $dy/dx = (S_0 - S_f)/(1 - Fr^2)$. When $S_0 = S_f$: uniform flow. When $Fr = 1$: vertical tangent (critical). Used to compute backwater/drawdown profiles.

### Q23: What are the GVF profile types?
**A:** Classified by slope (Mild/Steep/Critical/Horizontal/Adverse) and zone (1: $y > y_n, y_c$; 2: between; 3: $y < y_n, y_c$). M1 = dam backwater, M2 = drawdown at overfall, S2 = supercritical approaching normal depth.

### Q24: What is a hydraulic jump? Derive the conjugate depth relation.
**A:** Abrupt transition from supercritical to subcritical with energy dissipation. From momentum: $y_2/y_1 = 0.5(\sqrt{1+8Fr_1^2}-1)$. Energy loss: $\Delta E = (y_2-y_1)^3/(4y_1y_2)$. Used in stilling basins.

### Q25: What is the Froude number and its significance?
**A:** $Fr = V/\sqrt{gD_h}$ = inertial/gravitational forces. $Fr < 1$: subcritical (slow, deep, information propagates upstream), $Fr = 1$: critical, $Fr > 1$: supercritical (fast, shallow, no upstream propagation).

### Q26: Explain Manning's equation and its limitations.
**A:** $V = (1/n)R^{2/3}S^{1/2}$. Empirical, $n$ varies with depth/roughness. Limitations: assumes uniform flow, $n$ is not truly constant, less accurate for very shallow or very rough channels. Darcy-Weisbach is more theoretically grounded.

### Q27: What is the difference between GVF and RVF?
**A:** GVF: depth changes gradually, hydrostatic pressure, $S_0 \approx S_f$, Saint-Venant valid. RVF: abrupt change (jump, drop, sluice), non-hydrostatic, requires momentum equation, energy loss significant.

### Q28: How do you design a stilling basin?
**A:** Use USBR classification based on $Fr_1$: Type I (low $Fr$), Type II/III (with chute blocks, baffle piers, end sill for $Fr$ 4.5–9). Length ≈ $6y_2$, depth ensures jump contained within basin.

### Q29: What is normal depth and how is it computed?
**A:** Depth for uniform flow where $S_0 = S_f$. From Manning: $Q = (1/n)AR^{2/3}S_0^{1/2}$. Solve iteratively for $y_n$ given $Q$, $n$, $S_0$, geometry.

### Q30: What are weirs and how do they measure flow?
**A:** Sharp-crested (rectangular: $Q = C_d(2/3)\sqrt{2g}bH^{3/2}$, V-notch: $Q = C_d(8/15)\sqrt{2g}\tan(\theta/2)H^{5/2}$) and broad-crested (critical flow over crest). Flow ∝ $H^{3/2}$ or $H^{5/2}$.

### Q31: What is the Saint-Venant equation?
**A:** 1D unsteady open channel equations: continuity $\partial A/\partial t + \partial Q/\partial x = 0$ and momentum $\partial Q/\partial t + \partial(Q^2/A)/\partial x + gA\partial y/\partial x + gAS_f = gAS_0$. Assumes hydrostatic pressure, uniform velocity.

### Q32: Explain alternate depths.
**A:** Two depths with same specific energy $E$ for given $Q$: one subcritical ($y > y_c$), one supercritical ($y < y_c$). Found by solving $E = y + Q^2/(2gA^2)$ for $y$.

### Q33: What is sequent depth vs alternate depth?
**A:** Alternate: same $E$, different $y$ (energy equation). Sequent (conjugate): depths before/after hydraulic jump (momentum equation). Different concepts, different equations.

### Q34: How does channel roughness affect flow?
**A:** Higher $n$ → lower $V$ for same $Q$ → deeper $y_n$. Roughness from grain size ($n \propto d_{50}^{1/6}$ via Strickler), vegetation, irregularity. Composite roughness for compound channels.

### Q35: What is afflux and how is it calculated?
**A:** Rise in water level upstream of a constriction (bridge, culvert). $h_2 - h_1 = (V_2^2 - V_1^2)/2g + h_f$. Important for bridge design and flood level prediction.

---

## 💧 Hydrology & Water Resources (Q36–Q50)

### Q36: What is a unit hydrograph and its assumptions?
**A:** Direct runoff hydrograph from 1 unit (1 cm) of effective rainfall uniformly over catchment for specified duration. Assumptions: linearity (proportionality) and time-invariance. Used to synthesize DRH for any storm via convolution.

### Q37: How do you convert a UH from one duration to another?
**A:** S-curve method: sum UH ordinates shifted by original duration → S-curve, shift by new duration, difference × (new/old duration) = new UH.

### Q38: Explain the Muskingum method.
**A:** Channel routing: $S = K[XI + (1-X)O]$, $O_2 = C_0I_2 + C_1I_1 + C_2O_1$. $K$ = travel time, $X$ = wedge storage factor (0–0.5). $C_0 + C_1 + C_2 = 1$.

### Q39: What is the difference between Muskingum and level-pool routing?
**A:** Muskingum: channel reach (prism + wedge storage), $K$ and $X$, translatory waves. Level-pool: reservoir (horizontal surface), storage-indication method, $2S/\Delta t + O$ curve.

### Q40: Derive the Theis equation.
**A:** Unsteady radial flow to well in confined aquifer: $s = (Q/4\pi T)W(u)$, $u = r^2S/4Tt$, $W(u) = \int_u^\infty e^{-x}/x dx$. Assumptions: infinite, homogeneous, isotropic, fully penetrating, constant $Q$.

### Q41: What is the Cooper-Jacob approximation?
**A:** For $u < 0.01$: $s = (2.3Q/4\pi T)\log(2.25Tt/r^2S)$. Plot $s$ vs $\log t$ → straight line, slope gives $T$, intercept gives $S$. Simpler than Theis curve matching.

### Q42: Explain Darcy's law and its validity.
**A:** $Q = KiA$, $v = Ki$. Valid for laminar flow ($Re < 1$) through porous media. Breaks down for high velocity (turbulent) or very fine clays (non-Darcian).

### Q43: What is the hydrologic cycle?
**A:** Precipitation → interception → infiltration → runoff → evaporation/transpiration → condensation → precipitation. Quantified by water balance: $P = ET + R + \Delta S$.

### Q44: What is infiltration and how is it modeled?
**A:** Entry of surface water into soil. Models: Horton $f = f_c + (f_0-f_c)e^{-kt}$, Philip $F = St^{1/2} + At$, Green-Ampt $f = K(1 + \psi\Delta\theta/F)$.

### Q45: What is flood frequency analysis?
**A:** Fit probability distributions (Gumbel, Log-Pearson III) to annual maxima, estimate $x_T$ for return period $T$. Risk: $R = 1-(1-1/T)^n$ for $n$ years.

### Q46: What is time of concentration?
**A:** Time for water from most distant point to reach outlet. $t_c$ determines critical storm duration for peak runoff (rational method: $Q = CiA$ when storm duration = $t_c$).

### Q47: Explain reservoir routing.
**A:** Determine outflow hydrograph from inflow and storage-outflow relationship. Level-pool: $2S/\Delta t + O$ method. Used for flood control and water supply operation.

### Q48: What are aquifer properties?
**A:** $T = Kb$ (transmissivity), $S$ (storativity), $S_y$ (specific yield, unconfined), $S_s$ (specific storage). Determine from pumping tests via Theis/Cooper-Jacob.

### Q49: What is baseflow separation?
**A:** Separate direct runoff from baseflow in hydrograph. Methods: straight-line, fixed-discharge, variable-discharge, digital filters (Lyne-Hollick). Needed for UH derivation.

### Q50: What is the rational method?
**A:** $Q_p = CiA$ for peak runoff from small catchments ($A < 50$ km²). $C$ = runoff coefficient, $i$ = rainfall intensity for duration = $t_c$, $A$ = area. Simple but assumes uniform rainfall and linear response.

---

## 🌀 Turbulence & CFD (Q51–Q65)

### Q51: What is the difference between RANS, LES, and DNS?
**A:** RANS: time-averaged, models all scales, cheapest. LES: resolves large eddies, models subgrid, moderate cost. DNS: resolves all scales to Kolmogorov, most expensive. HWRE: RANS for design, LES for detailed scour/jump, DNS for research.

### Q52: What is the Boussinesq hypothesis?
**A:** $-\rho\overline{u_i'u_j'} = \mu_t(\partial\bar{u}_i/\partial x_j + \partial\bar{u}_j/\partial x_i) - 2/3\rho k\delta_{ij}$. Relates Reynolds stress to mean strain via eddy viscosity. Limitations: isotropic, scalar $\mu_t$, fails in curvature/rotation.

### Q53: When would you choose k-ω SST over k-ε?
**A:** SST for adverse pressure gradients, separation, curved flows (better near-wall). k-ε for high-Re free shear without separation. SST blends k-ω near wall with k-ε in free stream.

### Q54: What is y+ and why does it matter?
**A:** $y^+ = yu_\tau/\nu$, $u_\tau = \sqrt{\tau_w/\rho}$. Determines wall treatment: $y^+ < 5$ (viscous sublayer, resolve), $30 < y^+ < 300$ (wall functions), $> 300$ (log-law). Wrong $y^+$ → wrong $\tau_w$ and velocity.

### Q55: What is the energy cascade and -5/3 law?
**A:** Energy transfers from large to small eddies, dissipated at Kolmogorov scale. Inertial subrange: $E(k) = C_K\varepsilon^{2/3}k^{-5/3}$. Used to verify LES resolution and estimate dissipation.

### Q56: What is LES and its subgrid models?
**A:** Resolves large eddies, models small via SGS: Smagorinsky $\mu_{sgs} = \rho(C_s\Delta)^2|\bar{S}|$, dynamic Smagorinsky (computed $C_s$), WALE (better near-wall).

### Q57: How do you validate a turbulence model in OpenFOAM?
**A:** Grid independence (3 levels, GCI), compare with experimental data (velocity, pressure, $C_f$), monitor $y^+$, check residuals $< 10^{-4}$, verify mass conservation, use function objects for forces/averages.

### Q58: What is VOF and when is it used?
**A:** Volume of Fluid: tracks interface via phase fraction $\alpha$ ($0$ = phase 1, $1$ = phase 2, $0 < \alpha < 1$ = interface). For free-surface flows, waves, droplets. Coupled with RANS/LES.

### Q59: What is the log-law of the wall?
**A:** $u^+ = (1/\kappa)\ln(y^+) + B$, $\kappa = 0.41$, $B = 5.0$. Valid for $30 < y^+ < 300$ (log-law region). Used in wall functions to bridge viscous sublayer.

### Q60: What are the limitations of k-ε?
**A:** Requires wall functions, under-predicts separation in adverse pressure gradients, poor in strong curvature/rotation, assumes isotropic turbulence, sensitive to inlet $k$ and $\varepsilon$.

### Q61: Explain OpenFOAM case structure.
**A:** `0/` (initial/boundary conditions: U, p, k, omega), `constant/` (mesh: blockMeshDict, turbulenceProperties, transportProperties), `system/` (controlDict, fvSchemes, fvSolution). Run: blockMesh → checkMesh → solver (simpleFoam/pimpleFoam).

### Q62: What is the difference between simpleFoam and pimpleFoam?
**A:** simpleFoam: steady-state, SIMPLE algorithm, no time accuracy. pimpleFoam: transient, PIMPLE (SIMPLE+PISO), time-accurate, for unsteady flows (LES, VOF, dynamic mesh).

### Q63: How do you ensure mesh quality in OpenFOAM?
**A:** checkMesh: non-orthogonality < 70°, skewness < 4, aspect ratio < 1000. y+ compliance, 10–20 cells across boundary layer, growth ratio 1.1–1.2, GCI study with 3 meshes.

### Q64: What is sediment-turbulence interaction?
**A:** Particles modulate turbulence: small particles damp turbulence, large particles enhance it. Two-way coupling in Euler-Euler. Rouse profile $c/c_a = (y_a/y)^Z$ for suspended concentration.

### Q65: What is the Kolmogorov scale?
**A:** Smallest turbulent scale where viscosity dissipates energy: $\eta = (\nu^3/\varepsilon)^{1/4}$, $\tau_\eta = (\nu/\varepsilon)^{1/2}$. DNS must resolve $\eta$; LES resolves larger scales.

---

## 🏗️ Structures & Geotech (Q66–Q80)

### Q66: What is the difference between LSM and WSM?
**A:** WSM: allowable stress, elastic, single safety factor. LSM: partial factors on loads ($\gamma_f$) and materials ($\gamma_m$), considers collapse + serviceability, more economical. IS 456/800 use LSM.

### Q67: What are balanced, under-reinforced, and over-reinforced sections?
**A:** Balanced: steel yields as concrete crushes ($x_u = x_{u,max}$). Under: steel yields first ($x_u < x_{u,max}$) → ductile (preferred). Over: concrete crushes first ($x_u > x_{u,max}$) → brittle (avoid).

### Q68: What is $x_{u,max}/d$ and its values?
**A:** Limiting neutral axis ratio for under-reinforced design. Fe415: 0.48, Fe500: 0.46, Fe550: 0.44. Ensures ductile failure.

### Q69: Explain Euler's column formula and its assumptions.
**A:** $P_{cr} = \pi^2EI/(KL)^2$. Assumptions: initially straight, axial load, homogeneous/isotropic, elastic, uniform section, no self-weight. Valid for long columns ($\lambda > \lambda_{cr}$).

### Q70: What is the moment distribution method?
**A:** Hardy Cross iterative: compute FEMs, distribution factors $DF = K/\sum K$, release joints, distribute unbalanced moment, carry over half, iterate until convergence. For beams/frames.

### Q71: What is Mohr-Coulomb failure criterion?
**A:** $\tau_f = c + \sigma'\tan\phi$. Defines shear strength. $c$ = cohesion, $\phi$ = friction angle. For saturated clay (undrained): $\tau_f = c_u$ ($\phi_u = 0$).

### Q72: What is Terzaghi's bearing capacity equation?
**A:** $q_u = cN_c + qN_q + 0.5\gamma BN_\gamma$. $N_c$, $N_q$, $N_\gamma$ depend on $\phi$. Shape/depth/inclination corrections by Meyerhof/Vesic. $q_{safe} = q_{nu}/F + \gamma D_f$.

### Q73: What is consolidation and how is settlement calculated?
**A:** Time-dependent volume change from pore water expulsion. $S_c = C_cH\log(\sigma'_f/\sigma'_i)/(1+e_0)$ (NC clay). Time: $T_v = c_vt/H_{dr}^2$, $T_v = 0.848$ for 90% consolidation.

### Q74: What is the difference between Rankine and Coulomb earth pressure?
**A:** Rankine: smooth wall (no friction), stress transformation, conservative for active. Coulomb: wall friction $\delta$, wedge equilibrium, more realistic, higher passive when $\delta > 0$.

### Q75: What are Atterberg limits?
**A:** LL (liquid limit, Casagrande cup), PL (plastic limit, roll test), PI = LL - PL. Classify fine-grained soils, predict compressibility and strength.

### Q76: What is pile group efficiency?
**A:** $\eta_g = Q_{group}/(nQ_{single})$. < 1 for closely spaced piles in clay (block failure), ≈ 1 for friction piles in sand. Converse-Labarre formula for efficiency.

### Q77: What is slope stability analysis?
**A:** Factor of safety $F_s$ = resisting/driving forces. Methods: Fellenius $F_s = \sum(c'l + W\cos\alpha\tan\phi')/\sum W\sin\alpha$, Bishop (more accurate, iterative), Janbu, Morgenstern-Price.

### Q78: What is the difference between shallow and deep foundations?
**A:** Shallow: $D_f/B < 1$, load via base bearing (footings, mats). Deep: $D_f/B > 1$, load via base + skin friction (piles, caissons). Deep for weak surface soils or high loads.

### Q79: What are IS 456 load combinations?
**A:** $1.5(DL+LL)$, $1.2(DL+LL\pm WL)$, $0.9DL+1.5WL$, $1.5(DL\pm WL)$. Partial factors: $\gamma_f = 1.5$ (DL/LL), $\gamma_m = 1.5$ (concrete), $1.15$ (steel).

### Q80: What is development length?
**A:** $L_d = \phi\sigma_s/(4\tau_{bd})$. Length needed to develop full bar strength via bond. $\tau_{bd}$ depends on concrete grade and bar type (plain/deformed).

---

## 💧 Sediment & Scour (Q81–Q90)

### Q81: What is the Shields parameter?
**A:** $\tau^* = \tau_0/[(\rho_s-\rho)gd]$ = bed shear/submerged weight. Critical $\tau_c^* \approx 0.047$ for incipient motion. Fundamental for sediment transport.

### Q82: Explain bed load vs suspended load.
**A:** Bed load: rolls/slides/saltates along bed, $q_b \propto (\tau^*-\tau_c^*)^{3/2}$ (MPM). Suspended: turbulence-suspended, Rouse profile $c/c_a = (y_a/y)^Z$. Total = bed + suspended.

### Q83: What is the Meyer-Peter Müller formula?
**A:** $q_b^* = 8(\tau^*-\tau_c^*)^{3/2}$, $q_b^* = q_b/\sqrt{\Delta gd^3}$. For bed load when $\tau^* > 0.047$, coarse sediment.

### Q84: What is the Rouse profile?
**A:** $c/c_a = (y_a/y)^Z$, $Z = w_s/(\kappa u_\tau)$. Vertical concentration distribution. $Z > 2.5$: near-bed, $Z < 0.1$: uniform (wash load).

### Q85: How do you estimate bridge pier scour?
**A:** HEC-18: $y_s/y_1 = 2.0K_1K_2K_3K_4(a/y_1)^{0.35}Fr^{0.43}$. Factors: $K_1$ (angle), $K_2$ (nose shape), $K_3$ (bed condition), $K_4$ (sediment size).

### Q86: What is clear-water vs live-bed scour?
**A:** Clear-water: no upstream sediment supply, $V < V_c$, max depth limited. Live-bed: sediment supply replenishes, $V > V_c$, oscillating depth with bed forms.

### Q87: What is the Exner equation?
**A:** $\partial z_b/\partial t + \nabla\cdot q_b/(1-p) = 0$. Bed evolution from sediment continuity. Used in morphodynamic models (sedExnerFoam with ALE mesh motion).

### Q88: What are bed forms and their sequence?
**A:** Ripples → dunes → plane bed → antidunes → chutes/pools with increasing $Fr$ and transport. Strickler: $n = d_{50}^{1/6}/21.1$.

### Q89: What is sediment yield and trap efficiency?
**A:** Yield: t/km²/year from catchment. Trap efficiency: $TE = 1-1/(1+0.0003Cap/Y)$ (Brune). Determines reservoir useful life.

### Q90: How do you mitigate scour?
**A:** Riprap, sheet piles, caissons, streamline pier noses, collar plates, sacrificial piles, grade control, deeper foundations below predicted scour.

---

## 💻 Python/SQL/Non-Core (Q91–Q100)

### Q91: What is the difference between list and tuple in Python?
**A:** List: mutable, `[]`, slower, methods like append. Tuple: immutable, `()`, faster, hashable (can be dict key). Use tuple for fixed data, list for dynamic.

### Q92: Explain Pandas groupby.
**A:** `df.groupby('col').agg({'val': 'mean'})` splits data by group, applies function, combines. Like SQL GROUP BY. Use for aggregation, transformation, filtering.

### Q93: What is the difference between INNER JOIN and LEFT JOIN?
**A:** INNER: only matching rows from both tables. LEFT: all rows from left + matching from right (NULL if no match). Use LEFT to keep all left records.

### Q94: What is a window function in SQL?
**A:** Performs calculation across rows related to current row without collapsing: `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary)`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER (...)`.

### Q95: What is hypothesis testing?
**A:** Test claim about population: null $H_0$ vs alternative $H_1$, compute test statistic, p-value, reject $H_0$ if $p < \alpha$ (0.05). Types: t-test, chi-square, ANOVA.

### Q96: What is overfitting and how do you prevent it?
**A:** Model memorizes training data, poor on test. Prevention: cross-validation, regularization (L1/L2), early stopping, more data, simpler model, dropout.

### Q97: Explain the bias-variance tradeoff.
**A:** Bias: error from wrong assumptions (underfitting). Variance: error from sensitivity to training data (overfitting). Total error = bias² + variance + noise. Optimal complexity balances both.

### Q98: What is the difference between supervised and unsupervised learning?
**A:** Supervised: labeled data, predict output (classification, regression). Unsupervised: unlabeled, find patterns (clustering, dimensionality reduction). Semi-supervised: mix.

### Q99: How do you handle missing data in Python?
**A:** `df.isnull().sum()` to detect, `df.dropna()` to remove, `df.fillna(mean)` to impute, `df.interpolate()` for time series. Choose based on missing mechanism (MCAR, MAR, MNAR).

### Q100: Explain the project discussion framework for interviews.
**A:** Structure: (1) Problem statement (1 min), (2) Methodology (2 min, focus on YOUR contribution), (3) Results with numbers (1 min), (4) Challenges and how you solved them (1 min), (5) Learnings and future work (30 sec). Always quantify: "validated within 7%", "completed 2 weeks early".

---

## 📋 Quick Revision Checklist

- [ ] Can derive Bernoulli, continuity, momentum from first principles
- [ ] Can explain y+, wall functions, and turbulence model selection
- [ ] Can solve GVF profile type and hydraulic jump problems
- [ ] Can derive Theis and explain Muskingum routing
- [ ] Can explain Shields, MPM, and HEC-18 scour
- [ ] Can design RCC beam/column per IS 456
- [ ] Can explain bearing capacity and consolidation
- [ ] Can write Python/SQL for data analysis
- [ ] Can present thesis project in 5 minutes with STAR structure

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027)
* [`../core/hwre/hydraulics/hydraulics.md`](../../core/hwre/hydraulics/hydraulics.md) — Detailed hydraulics
* [`../core/hwre/hydraulics/turbulence-modeling.md`](../../core/hwre/hydraulics/turbulence-modeling.md) — CFD details

# ExxonMobil Engineer Recruitment: Civil Engineering Core Fundamentals
## Master Curriculum for Non-HWRE Civil Disciplines & Structural/Geotechnical Systems

> **Target Opportunity:** Engineer (ExxonMobil Services & Technology Pvt. Ltd., Bengaluru)  
> **Candidate Background:** B.Tech / M.Tech in Civil Engineering (Specialization: HWRE), IIT Kanpur  
> **Pedagogical Standard:** Rigorous first-principles engineering mechanics, code-compliant governing equations, explicit physical assumptions, boundary conditions, and priority tagging.

---

## Curriculum Priority Classification Schema
To ensure time-efficient preparation, every topic within this core civil curriculum is categorized according to its strategic recruitment utility:

* `[SCREENING-ESSENTIAL]`: Universally tested in written screening MCQs and online numerical assessments across all engineering campus applicants.
* `[INTERVIEW-ESSENTIAL]`: Core engineering concepts rigorously probed by technical interview panels to test degree fundamentals, structural intuition, and qualitative mechanics.
* `[ROLE-DEPENDENT-EXTENSION]`: Advanced or specialized operational civil topics that distinguish candidates during deep technical discussions for marine facilities, pipeline routing, or infrastructure design.

---

# Section 1: Engineering Mechanics & Strength of Materials (SOM)

## 1.1 Statics, Equilibrium & Section Properties `[SCREENING-ESSENTIAL]`
* **Free-Body Diagram (FBD) & Equilibrium:**
  In 2D plane statics, a rigid body in static equilibrium satisfies three independent scalar equations:
  $$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_z = 0$$
* **Centroid ($\bar{x}, \bar{y}$):** First moment of area divided by total area:
  $$\bar{y} = \frac{\sum A_i y_i}{\sum A_i} = \frac{\int y \, dA}{A}$$
* **Second Moment of Area (Moment of Inertia, $I$):**
  - Rectangular Section ($b \times d$): $I_x = \frac{b d^3}{12}$, $I_y = \frac{d b^3}{12}$.
  - Circular Section (Diameter $D$): $I_x = I_y = \frac{\pi D^4}{64}$, Polar moment $J = \frac{\pi D^4}{32}$.
* **Parallel Axis Theorem:**
  $$I_{x'} = I_c + A d^2$$
  where $I_c$ is the moment of inertia about the centroidal axis, and $d$ is the perpendicular distance between the centroidal axis and the parallel axis $x'$.

---

## 1.2 Stress, Strain, Elastic Constants & Thermal Stresses `[SCREENING-ESSENTIAL]`
* **Hooke's Law & Elastic Moduli:**
  For linear elastic, isotropic, homogeneous materials:
  $$\sigma = E \epsilon, \quad \tau = G \gamma$$
* **Four Interrelated Elastic Constants ($E, G, K, \mu$):**
  $$E = 2G(1 + \mu) = 3K(1 - 2\mu) = \frac{9KG}{3K + G}$$
  where $E$ is Young's Modulus, $G$ is Shear Modulus, $K$ is Bulk Modulus, and $\mu$ is Poisson's ratio.
  - *Theoretical Limits of Poisson's Ratio:* $-1.0 \le \mu \le 0.5$. For engineering metals/steel, $\mu \approx 0.28 - 0.33$; for saturated undrained clay, $\mu \approx 0.50$ (incompressible); for concrete, $\mu \approx 0.15 - 0.20$.
* **Thermal Stress in Restrained Members:**
  Unrestrained thermal elongation: $\Delta L_{\text{th}} = \alpha L \Delta T$.
  If the member is rigidly restrained against expansion between two unyielding supports, the resulting compressive thermal strain and stress are:
  $$\epsilon_{\text{th}} = \frac{\Delta L_{\text{th}}}{L} = \alpha \Delta T \implies \sigma_{\text{th}} = E \alpha \Delta T$$
  If supports yield by an amount $\delta < \Delta L_{\text{th}}$:
  $$\sigma_{\text{th}} = \frac{E (\alpha L \Delta T - \delta)}{L}$$

---

## 1.3 Axial Loading, Torsion & Shaft Mechanics `[INTERVIEW-ESSENTIAL]`
* **Axial Elongation ($\Delta L$):**
  - Prismatic bar of area $A$: $\Delta L = \frac{P L}{A E}$.
  - Circular tapering bar ($d_1 \to d_2$): $\Delta L = \frac{4 P L}{\pi E d_1 d_2}$.
  - Self-weight elongation of prismatic bar: $\Delta L_{\text{self}} = \frac{\gamma L^2}{2E} = \frac{W L}{2AE}$ (exactly half that of an equal concentrated end load).
* **Pure Torsion of Circular Shafts (Coulomb / St. Venant):**
  $$\frac{T}{J} = \frac{\tau}{r} = \frac{G \theta}{L}$$
  where $T$ is applied torque, $J$ is polar second moment of area ($J = \frac{\pi D^4}{32}$), $\tau_{\max} = \frac{T (D/2)}{J} = \frac{16 T}{\pi D^3}$, and $\theta$ is angle of twist $[rad]$.
  - Torsional rigidity: $G J$.
  - Torsional stiffness: $k_t = \frac{G J}{L}$.

---

## 1.4 Shear Force & Bending Moment Diagrams (SFD & BMD) `[SCREENING-ESSENTIAL]`
* **Differential Equilibrium Relationships:**
  $$\frac{dV}{dx} = -w(x), \quad \frac{dM}{dx} = V(x) \implies \frac{d^2M}{dx^2} = -w(x)$$
  - The slope of the SFD at any point equals the negative of the distributed load intensity.
  - The slope of the BMD at any point equals the shear force $V$.
  - Maximum or minimum bending moment occurs where shear force changes sign ($V = 0$).
  - Point of Contraflexure: Location where the bending moment changes sign ($M = 0$), indicating a reversal of curvature.

---

## 1.5 Flexural and Transverse Shear Stresses in Beams `[INTERVIEW-ESSENTIAL]`
* **Euler-Bernoulli Beam Bending Theory:**
  *Assumptions:* Plane sections before bending remain plane after bending (Navier's hypothesis; neglects transverse shear deformation); material is linear elastic, isotropic, and obeys Hooke's law; radius of curvature is large relative to cross-sectional depth.
  $$\frac{M}{I} = \frac{\sigma}{y} = \frac{E}{R}$$
  $$\sigma_{\max} = \frac{M}{Z}, \quad Z = \frac{I}{y_{\max}} \quad (\text{Elastic Section Modulus})$$
* **Transverse Shear Stress (Jourawski's Formula):**
  $$\tau(y) = \frac{V Q(y)}{I b(y)}$$
  where $V$ is vertical shear force, $Q(y) = \int_y^{y_{\text{top}}} \eta \, dA$ is the first moment of area above level $y$ about the neutral axis, and $b(y)$ is the beam width at level $y$.
  - *Rectangular Section ($b \times h$):* Parabolic distribution:
    $$\tau_{\max} = 1.5 \tau_{\text{avg}} = \frac{3}{2}\frac{V}{b h} \quad (\text{at neutral axis } y = 0)$$
  - *Circular Section (Diameter $D$):*
    $$\tau_{\max} = \frac{4}{3}\tau_{\text{avg}} = \frac{4}{3}\frac{V}{\pi D^2 / 4}$$
  - *I-Beam Section:* The thin web carries $90–95\%$ of the total vertical shear force, while flanges resist the majority of the bending moment.

---

## 1.6 Beam Deflection & Boundary Value Problems `[SCREENING-ESSENTIAL]`
* **Governing Differential Equation:**
  $$E I \frac{d^2 y}{dx^2} = M(x)$$
* **Standard Canonical Deflections:**
  1. *Cantilever with End Point Load $P$:* Tip deflection $\delta_{\max} = \frac{P L^3}{3 E I}$, tip slope $\theta_{\max} = \frac{P L^2}{2 E I}$.
  2. *Cantilever with Uniform Load $w$:* $\delta_{\max} = \frac{w L^4}{8 E I}$, $\theta_{\max} = \frac{w L^3}{6 E I}$.
  3. *Simply Supported with Central Load $P$:* $\delta_{\text{mid}} = \frac{P L^3}{48 E I}$, $\theta_{\text{support}} = \frac{P L^2}{16 E I}$.
  4. *Simply Supported with Uniform Load $w$:* $\delta_{\text{mid}} = \frac{5 w L^4}{384 E I}$, $\theta_{\text{support}} = \frac{w L^3}{24 E I}$.

---

## 1.7 Principal Stresses & Yield/Failure Theories `[SCREENING-ESSENTIAL]`
* **Mohr's Circle Formulation:**
  $$\sigma_1, \sigma_2 = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$$
  $$\tau_{\max} = \frac{\sigma_1 - \sigma_2}{2}$$
* **Failure Theories for Engineering Materials:**
  1. **Maximum Principal Stress Theory (Rankine):** Failure occurs when $\sigma_1 \ge \sigma_{\text{yield}}$ or $\sigma_2 \le -\sigma_{\text{yield}}$. Valid for **brittle materials** (cast iron, unreinforced concrete, rock).
  2. **Maximum Shear Stress Theory (Tresca / Guest):** Failure occurs when $\tau_{\max} = \frac{\sigma_1 - \sigma_3}{2} \ge \frac{f_y}{2}$. Conservative standard for **ductile materials** (structural steel, pipe metals).
  3. **Distortion Energy / Octahedral Shear Stress Theory (von Mises / Hencky):** Failure occurs when von Mises equivalent stress $\sigma_v$ reaches yield:
     $$\sigma_v = \sqrt{\frac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]} \ge f_y$$
     For 2D plane stress ($\sigma_3 = 0$):
     $$\sigma_v = \sqrt{\sigma_1^2 - \sigma_1 \sigma_2 + \sigma_2^2} = \sqrt{\sigma_x^2 - \sigma_x \sigma_y + \sigma_y^2 + 3 \tau_{xy}^2} \ge f_y$$
     Most accurate predictor for ductile metals under multi-axial stress states. Under pure shear ($\sigma_x = 0, \tau_{xy} = \tau$): von Mises predicts shear yield $\tau_y = \frac{f_y}{\sqrt{3}} \approx 0.577 f_y$, whereas Tresca predicts $\tau_y = 0.50 f_y$.

---

## 1.8 Columns, Elastic Buckling & Slenderness Ratio `[SCREENING-ESSENTIAL]`
* **Euler's Critical Buckling Load:**
  $$P_{\text{cr}} = \frac{\pi^2 E I}{(L_e)^2} = \frac{\pi^2 E A}{\lambda^2}$$
  where $L_e$ is the effective length, and $\lambda = \frac{L_e}{r}$ is the slenderness ratio ($r = \sqrt{I/A}$ is radius of gyration).
* **Effective Length Factor ($K = L_e / L$) for End Conditions:**
  - Both ends pinned (hinged): $L_e = 1.0 L$ ($K = 1.0$)
  - Both ends fixed: $L_e = 0.5 L$ ($K = 0.5 \implies P_{\text{cr}}$ increases by $4\times$)
  - One end fixed, one end pinned: $L_e = \frac{L}{\sqrt{2}} \approx 0.707 L$ ($K = 0.70$)
  - One end fixed, one end free (cantilever): $L_e = 2.0 L$ ($K = 2.0 \implies P_{\text{cr}}$ decreases to $\frac{1}{4}\times$)
* **Validity Boundary of Euler's Formula:**
  Euler's formula assumes purely elastic bifurcation. It is valid only when $P_{\text{cr}} / A \le \sigma_{\text{prop}}$, requiring:
  $$\lambda \ge \pi \sqrt{\frac{E}{\sigma_{\text{prop}}}}$$
  For structural steel ($E = 200\text{ GPa}, f_y = 250\text{ MPa}$), Euler's formula applies strictly for long columns with $\lambda \ge 89$. Short and intermediate columns fail by inelastic crushing/yielding, modeled by Rankine-Gordon or Perry-Robertson curves (codified in IS 800:2007).

---

## 1.9 Thin-Walled Pressure Vessels & Multi-Axial Combined Loading `[INTERVIEW-ESSENTIAL]`
* **Cylindrical Vessel ($D/t \ge 20$):**
  - Hoop (Circumferential) Stress: $\sigma_h = \frac{p D}{2t}$
  - Longitudinal (Axial) Stress: $\sigma_L = \frac{p D}{4t}$ (for closed ends)
  - Radial Stress: $\sigma_r \approx 0$ across thin wall.
  - Principal Stresses: $\sigma_1 = \sigma_h$, $\sigma_2 = \sigma_L$, $\sigma_3 \approx 0$.
  - Maximum In-Plane Shear Stress: $\tau_{\text{max, in-plane}} = \frac{\sigma_1 - \sigma_2}{2} = \frac{p D}{8t}$.
  - Absolute Maximum Shear Stress (out-of-plane): $\tau_{\text{abs, max}} = \frac{\sigma_1 - \sigma_3}{2} = \frac{p D}{4t}$.
* **Spherical Vessel:**
  - Uniform biaxial stress: $\sigma_1 = \sigma_2 = \frac{p D}{4t}$.
  - $\tau_{\text{abs, max}} = \frac{\sigma_1 - 0}{2} = \frac{p D}{8t}$ (spherical vessels require half the thickness of a cylindrical vessel of identical diameter and pressure).
* **Failure Modes Under Overpressure:**
  - While hoop stress is twice the longitudinal stress ($\sigma_h = 2\sigma_L$), actual pipe rupture does **not** unconditionally occur at the longitudinal seam. The initiation location and failure mode depend critically on material anisotropy, rolled plate rolling direction, weld seam joint efficiency factors ($E \le 1.0$), localized corrosion thinning, bending moments from soil settlement, and cyclic fatigue.

---

# Section 2: Structural Analysis

## 2.1 Determinacy, Kinematic Indeterminacy & Stability `[SCREENING-ESSENTIAL]`
* **Static Indeterminacy ($D_s$):**
  - Plane Truss: $D_s = m + r - 2j$ (where $m$ is number of members, $r$ is support reaction components, $j$ is joints).
  - Plane Frame: $D_s = 3m + r - 3j - c$ (where $c$ is equations of condition from internal hinges: $c = \sum (m_j - 1)$).
* **Internal Hinges:** An internal hinge at a joint releases bending moment ($M = 0$), providing 1 additional equation of equilibrium if connecting 2 members.
* **Kinematic Indeterminacy / Degrees of Freedom ($D_k$):**
  - Plane Frame without axial deformation neglected: $D_k = 3j - r$.
  - Plane Frame with members assumed axially inextensible: $D_k = 3j - r - m$.
* **Geometric Stability Criteria:**
  A structure is unstable if reactions are concurrent, parallel, or insufficient ($r < 3$).

---

## 2.2 Energy Methods, Virtual Work & Deflection Analysis `[INTERVIEW-ESSENTIAL]`
* **Unit Load Method (Principle of Virtual Work):**
  $$\Delta = \sum \frac{P k L}{A E} \quad (\text{Trusses})$$
  $$\Delta = \int_0^L \frac{M(x) m(x)}{E I} dx + \int_0^L \frac{V(x) v(x)}{G A_s} dx \quad (\text{Beams/Frames})$$
  where $M(x)$ is the real bending moment distribution under external loads, and $m(x)$ is the virtual bending moment distribution resulting from a fictitious unit load ($\mathcal{P} = 1$) applied at the target point in the desired displacement direction.
* **Castigliano's Theorems:**
  - *Theorem I:* $\frac{\partial U}{\partial \Delta_i} = P_i$ (derivative of strain energy with respect to displacement equals applied force).
  - *Theorem II:* $\frac{\partial U^*}{\partial P_i} = \Delta_i$ (derivative of complementary strain energy with respect to force equals displacement; applicable to linear elastic systems where $U^* = U$).

---

## 2.3 Influence Lines & Moving Load Envelopes `[ROLE-DEPENDENT-EXTENSION]`
* **Definition:** An Influence Line Diagram (ILD) represents the variation of a specific structural response function (reaction, shear force, or bending moment at a fixed cross-section) as a dimensionless unit concentrated vertical load ($P = 1$) traverses across the span.
* **Müller-Breslau Principle:**
  The influence line for any response function is given by the deflected shape of the structure obtained by removing the internal restraint corresponding to that function and introducing a unit virtual displacement corresponding to that action.
  - Statically Determinate Structures: ILD consists of **straight lines**.
  - Statically Indeterminate Structures: ILD consists of **continuous curves**.

---

# Section 3: RCC & Concrete Technology

## 3.1 Concrete Technology, Durability & Mix Fundamentals `[SCREENING-ESSENTIAL]`
* **Hydration Chemistry:**
  Tricalcium silicate ($C_3S$) governs early strength ($7–28\text{ days}$). Dicalcium silicate ($C_2S$) hydrates slowly, governing long-term ultimate strength. Tricalcium aluminate ($C_3A$) undergoes flash set, requiring gypsum addition ($CaSO_4 \cdot 2H_2O$) to retard initial setting time.
* **Water-Cement Ratio (Abrams' Law):**
  $$\text{Compressive Strength } f_c = \frac{A}{B^{w/c}}$$
  Decreasing the water-cement ratio increases strength and reduces capillary porosity, directly enhancing durability against chemical attack.
* **Workability vs. Strength:**
  Measured by Slump Test (IS 1199): True slump, shear slump, collapse. Adding superplasticizers (polycarboxylate ethers - PCE) allows high slump ($100–150\text{ mm}$) at low $w/c \le 0.40$ without segregation or bleeding.
* **Durability in Industrial & Marine Exposures (IS 456:2000 Table 3 & 5):**
  - *Severe Exposure:* Seawater spray, coastal structures $\implies$ Minimum cement $= 320\text{ kg/m}^3$, Max $w/c = 0.45$, Minimum grade $= \text{M30}$, Minimum nominal cover $= 45\text{ mm}$.
  - *Very Severe Exposure:* Coastal splashing zone $\implies$ Minimum grade $= \text{M35}$, cover $= 50\text{ mm}$.
  - *Extreme Exposure:* Tidal zone, direct contact with aggressive chemicals $\implies$ Minimum grade $= \text{M40}$, cover $= 75\text{ mm}$.

---

## 3.2 Limit State Method (LSM) Philosophy (IS 456:2000) `[SCREENING-ESSENTIAL]`
* **Design Strengths & Partial Safety Factors:**
  - Concrete in Flexural Compression:
    $$f_{cd} = \frac{0.67 f_{ck}}{\gamma_{mc}} = \frac{0.67 f_{ck}}{1.5} \approx 0.446 f_{ck}$$
  - Reinforcing Steel (Fe 415, Fe 500):
    $$f_{yd} = \frac{f_y}{\gamma_{ms}} = \frac{f_y}{1.15} \approx 0.87 f_y$$
* **Design Load Combinations (IS 456 Clause 36.4):**
  - $1.5(\text{DL} + \text{LL})$
  - $1.5(\text{DL} \pm \text{WL/EL})$
  - $1.2(\text{DL} + \text{LL} \pm \text{WL/EL})$
  - $0.9\text{DL} \pm 1.5\text{WL/EL}$ (critical for overturning/uplift stability checks).

---

## 3.3 Flexure, Shear & Bond in RCC Beams `[INTERVIEW-ESSENTIAL]`
* **Rectangular Singly Reinforced Section:**
  - Limiting depth of neutral axis ($x_{u,\max}$ from strain compatibility $\epsilon_{cu} = 0.0035, \epsilon_{st} \ge \frac{0.87 f_y}{E_s} + 0.002$):
    - Fe 250: $x_{u,\max} / d = 0.53$
    - Fe 415: $x_{u,\max} / d = 0.48$
    - Fe 500: $x_{u,\max} / d = 0.46$
  - Moment of Resistance for Limiting (Balanced) Section:
    $$M_{u,\lim} = 0.36 f_{ck} b x_{u,\max} (d - 0.42 x_{u,\max})$$
    For Fe 415: $M_{u,\lim} = 0.138 f_{ck} b d^2$.  
    For Fe 500: $M_{u,\lim} = 0.133 f_{ck} b d^2$.
  - *Under-Reinforced Section ($x_u < x_{u,\max}$):* Steel yields before concrete crushes ($\epsilon_s > \epsilon_{yd}$). Failure is ductile, accompanied by extensive cracking and warning deflections. **All standard civil designs must be under-reinforced.**
  - *Over-Reinforced Section ($x_u > x_{u,\max}$):* Concrete crushes explosively in compression before steel yields. Strictly forbidden in primary flexural members.
* **Shear Design (IS 456:2000 Clause 40):**
  Nominal shear stress: $\tau_v = \frac{V_u}{b d}$.
  - If $\tau_v \le \tau_c$ (design shear strength of concrete based on $p_t = 100 A_{st}/(bd)$): Provide minimum nominal shear stirrups:
    $$\frac{A_{sv}}{b s_v} \ge \frac{0.4}{0.87 f_y}$$
  - If $\tau_c < \tau_v \le \tau_{c,\max}$: Shear reinforcement must resist excess shear $V_{us} = V_u - \tau_c b d$:
    $$V_{us} = \frac{0.87 f_y A_{sv} d}{s_v} \quad (\text{for vertical stirrups})$$
  - If $\tau_v > \tau_{c,\max}$: Section size is inadequate; beam cross-section must be enlarged to avoid diagonal compression crushing of concrete struts.
* **Development Length ($L_d$, IS 456 Clause 26.2.1):**
  $$L_d = \frac{\phi \sigma_s}{4 \tau_{bd}} = \frac{\phi (0.87 f_y)}{4 \tau_{bd}}$$
  where $\tau_{bd}$ is design bond stress. For deformed (HYSD) bars, $\tau_{bd}$ is increased by $60\%$; for bars in compression, $\tau_{bd}$ is increased by an additional $25\%$.

---

## 3.4 Compression Members (Short & Slender Columns) `[INTERVIEW-ESSENTIAL]`
* **Short Column with Minimum Eccentricity ($e_{\min} \le 0.05 D$):**
  $$P_u = 0.4 f_{ck} A_c + 0.67 f_y A_{sc}$$
  Minimum eccentricity: $e_{\min} = \max\left(\frac{L}{500} + \frac{D}{30}, 20\text{ mm}\right)$.
* **Longitudinal Steel Limits:** Minimum $= 0.8\%$ of gross area; Maximum $= 4.0\%$ (or $6.0\%$ if non-lapped). Minimum bar diameter $= 12\text{ mm}$. Minimum 4 bars in rectangular column, 6 bars in circular column.

---

# Section 4: Steel Structures & Materials

## 4.1 Structural Steel Properties & Limit State Design (IS 800:2007) `[SCREENING-ESSENTIAL]`
* **Standard Grades:** Fe 410 (E250: $f_y = 250\text{ MPa}, f_u = 410\text{ MPa}, E = 2 \times 10^5\text{ MPa}$).
* **Partial Safety Factors for Resistance (IS 800 Table 5):**
  - Resistance to yielding: $\gamma_{m0} = 1.10$.
  - Resistance to ultimate rupture: $\gamma_{m1} = 1.25$.
  - Welds (shop / site): $\gamma_{mw} = 1.25 / 1.50$.
  - Bolts (bearing / friction): $\gamma_{mb} = 1.25$.

---

## 4.2 Tension & Compression Members `[INTERVIEW-ESSENTIAL]`
* **Design Strength of Tension Members (IS 800 Clause 6):**
  Governed by minimum of:
  1. *Gross Section Yielding:* $T_{dg} = \frac{A_g f_y}{\gamma_{m0}}$.
  2. *Net Section Rupture:* $T_{dn} = \frac{0.9 A_n f_u}{\gamma_{m1}}$.
  3. *Block Shear Strength:* $T_{db}$ (tearing along combination of shear and tension planes at end connection).
* **Compression Members & Column Curves (IS 800 Clause 7):**
  Design compressive strength:
  $$P_d = A_e f_{cd}$$
  $$f_{cd} = \frac{f_y / \gamma_{m0}}{\phi + [\phi^2 - \lambda^2]^{0.5}} = \chi \frac{f_y}{\gamma_{m0}}$$
  where $\chi$ is the stress reduction factor derived from Perry-Robertson curves (Buckling Classes a, b, c, d depending on section type and axis of buckling).
  - Maximum allowable slenderness ratio ($\lambda = K L / r$):
    - Member carrying compressive loads resulting from dead and imposed loads: $\lambda_{\max} = 180$.
    - Tension member reversing into compression under wind/seismic loads: $\lambda_{\max} = 350$.

---

## 4.3 Flexural Members & Connections `[ROLE-DEPENDENT-EXTENSION]`
* **Lateral-Torsional Buckling (LTB):**
  Unbraced steel I-beams undergoing flexure fail prematurely by combined lateral deflection and twisting of the compression flange unless the compression flange is continuously restrained laterally ($L_{\text{unbraced}} \le L_{cr}$).
* **Bolted & Welded Connections:**
  - *Fillet Weld Throat Thickness:* $t_t = k \cdot s = 0.7 \cdot s$ (for $90^\circ$ fusion angle).
  - Weld shear capacity: $f_{wd} = \frac{f_u}{\sqrt{3} \gamma_{mw}} = \frac{410}{\sqrt{3} \times 1.25} = 189.37\text{ N/mm}^2$.
* **Pipe Racks in Energy Facilities:** Multi-level steel moment-resisting frames designed to carry utility piping, electrical trays, and process lines under thermal expansion friction loads ($0.3–0.4 \times \text{pipe operating weight}$) and longitudinal wind/earthquake actions.

---

# Section 5: Geotechnical Engineering & Foundations

## 5.1 Soil Phase Relations & Index Properties `[SCREENING-ESSENTIAL]`
* **Phase Diagram Fundamental Relationships:**
  $$\text{Void Ratio } e = \frac{V_v}{V_s}, \quad \text{Porosity } n = \frac{V_v}{V_t} \implies n = \frac{e}{1 + e}, \quad e = \frac{n}{1 - n}$$
  $$\text{Degree of Saturation } S = \frac{V_w}{V_v}, \quad \text{Water Content } w = \frac{W_w}{W_s}$$
  $$e \cdot S = w \cdot G_s$$
  $$\text{Bulk Unit Weight } \gamma = \frac{(G_s + e S) \gamma_w}{1 + e}$$
  $$\text{Submerged (Buoyant) Unit Weight } \gamma' = \gamma_{\text{sat}} - \gamma_w = \frac{(G_s - 1)\gamma_w}{1 + e}$$

---

## 5.2 Seepage, Permeability & Effective Stress Principle `[SCREENING-ESSENTIAL]`
* **Terzaghi's Principle of Effective Stress:**
  $$\sigma' = \sigma - u$$
  where $\sigma = \sum \gamma_i h_i$ is total vertical stress, $u$ is pore water pressure, and $\sigma'$ is effective stress governing soil shear strength and consolidation volume change.
* **Critical Hydraulic Gradient & Quick Sand (Piping):**
  Upward seepage reduces effective stress: $\sigma' = \gamma' z - i z \gamma_w$.
  When $\sigma' = 0$:
  $$i_c = \frac{\gamma'}{\gamma_w} = \frac{G_s - 1}{1 + e}$$
  For typical quartz sands ($G_s \approx 2.65, e \approx 0.65$), $i_c \approx \frac{1.65}{1.65} = 1.0$. If upward exit gradient exceeds $i_c$, sand particles lose all intergranular contact and boil ("quick condition"). Factor of safety against piping: $\text{FOS} = i_c / i_{\text{exit}} \ge 5.0 - 6.0$.

---

## 5.3 Compaction vs. 1D Consolidation `[INTERVIEW-ESSENTIAL]`
* **Distinction:**
  - *Compaction:* Rapid expulsion of **pore air** under mechanical rolling/tamping. Evaluated via Standard/Modified Proctor Test (Optimum Moisture Content - OMC, and Maximum Dry Density - MDD).
  - *Consolidation:* Time-dependent gradual dissipation of excess **pore water pressure** under sustained static surcharge loading in saturated cohesive soils.
* **Terzaghi's 1D Consolidation Equation:**
  $$\frac{\partial u}{\partial t} = c_v \frac{\partial^2 u}{\partial z^2}, \quad c_v = \frac{k}{m_v \gamma_w}$$
  where $c_v$ is coefficient of consolidation, and $m_v = \frac{a_v}{1 + e_0}$ is coefficient of volume compressibility.
* **Total Primary Consolidation Settlement:**
  - Using Compression Index $C_c$ for Normally Consolidated Clay:
    $$S_c = \frac{C_c H_0}{1 + e_0} \log_{10}\left(\frac{\sigma_0' + \Delta \sigma'}{\sigma_0'}\right)$$
  - Time Factor: $T_v = \frac{c_v t}{d^2}$ (where $d = H/2$ for two-way drainage, $d = H$ for one-way drainage).

---

## 5.4 Shear Strength of Soils `[INTERVIEW-ESSENTIAL]`
* **Mohr-Coulomb Failure Criterion:**
  $$\tau_f = c' + \sigma' \tan \phi'$$
  where $c'$ is effective cohesion, $\sigma'$ is effective normal stress, and $\phi'$ is effective internal angle of friction.
* **Drainage Conditions in Triaxial Testing:**
  1. *Unconsolidated Undrained (UU):* Measures undrained shear strength $s_u = c_u$ ($\phi_u = 0$ for fully saturated clays). Relevant for rapid embankment construction on clay before pore pressure dissipates.
  2. *Consolidated Undrained (CU):* Specimen consolidated, sheared undrained with pore pressure measurement. Yields effective parameters $c', \phi'$.
  3. *Consolidated Drained (CD):* Sheared very slowly under zero excess pore pressure. Relevant for long-term slope stability.

---

## 5.5 Earth Pressure & Retaining Structures `[SCREENING-ESSENTIAL]`
* **Three Earth Pressure States:**
  1. *At-Rest ($K_0$):* No wall movement ($\Delta x = 0$). $K_0 \approx 1 - \sin \phi'$ (Jaky's equation).
  2. *Active ($K_a$):* Wall moves **away** from soil ($\Delta x \ge 0.001–0.002 H$ in sand). Soil expands laterally, shear strength mobilizes, lateral pressure drops to minimum:
     $$K_a = \frac{1 - \sin \phi}{1 + \sin \phi} = \tan^2(45^\circ - \phi/2)$$
     Active pressure profile: $\sigma_a = K_a \sigma_v - 2 c \sqrt{K_a}$. Depth of tensile crack in clay: $z_c = \frac{2c}{\gamma \sqrt{K_a}}$.
  3. *Passive ($K_p$):* Wall is pushed **into** soil ($\Delta x \ge 0.01–0.02 H$). Soil undergoes lateral compression, pressure rises to maximum:
     $$K_p = \frac{1 + \sin \phi}{1 - \sin \phi} = \tan^2(45^\circ + \phi/2) = \frac{1}{K_a}$$
     Passive pressure profile: $\sigma_p = K_p \sigma_v + 2 c \sqrt{K_p}$.

---

## 5.6 Shallow Foundations & Terzaghi Bearing Capacity `[SCREENING-ESSENTIAL]`
* **Terzaghi's General Bearing Capacity Equation (Continuous Strip Footing):**
  $$q_{\text{ult}} = c N_c + q N_q + 0.5 \gamma B N_\gamma$$
  where $q = \gamma D_f$ is surcharge at footing level, $B$ is footing width, and $N_c, N_q, N_\gamma$ are dimensionless bearing capacity factors depending exclusively on internal friction angle $\phi$.
  - For purely cohesive soil ($\phi = 0$): $N_c = 5.7, N_q = 1.0, N_\gamma = 0$.
    $$q_{\text{ult}} = 5.7 c_u + \gamma D_f \implies q_{\text{net, ult}} = 5.7 c_u$$
  - Shape Factors:
    - Square Footing: $q_{\text{ult}} = 1.3 c N_c + q N_q + 0.4 \gamma B N_\gamma$.
    - Circular Footing: $q_{\text{ult}} = 1.3 c N_c + q N_q + 0.3 \gamma B N_\gamma$.
* **Groundwater Table Correction Factors:**
  - If water table is at or above ground level: Both surcharge term and width term use submerged unit weight $\gamma'$.
  - If water table is at footing depth $D_f$: Surcharge uses $\gamma$, while soil below footing uses $\gamma'$.

---

## 5.7 Deep Foundations (Piles) & Dynamic/Scour Interaction `[ROLE-DEPENDENT-EXTENSION]`
* **Ultimate Pile Axial Capacity ($Q_u$):**
  $$Q_u = Q_b + Q_s = q_b A_b + \sum f_s A_s$$
  - Sand: $q_b = \sigma_{vb}' N_q^*$, $f_s = K_s \sigma_v' \tan \delta$.
  - Clay: $q_b = 9 c_u$, $f_s = \alpha c_u$ ($\alpha$ is adhesion factor).
* **Negative Skin Friction:** Downward drag on pile shaft caused by consolidating soft soil settling relative to the rigid pile. Acts as an additional structural load rather than resistance.
* **Scour Interaction in River & Marine Trestles:**
  During design floods, scouring removes upper soil overburden down to total scour depth $y_s$. All skin friction and lateral confining resistance within the scour zone must be **completely discounted** ($f_s = 0$ for $z \le y_s$). Pile buckling length increases by $y_s$, drastically reducing Euler load capacity.

---

# Section 6: Surveying & Geomatics

## 6.1 Leveling & Elevation Networks `[SCREENING-ESSENTIAL]`
* **Height of Instrument (HI) Method:**
  $$\text{HI} = \text{BM elevation} + \text{BS}$$
  $$\text{RL of Point} = \text{HI} - \text{FS (or IS)}$$
* **Rise and Fall Method:**
  $$\Delta Z = \text{Previous Reading} - \text{Current Reading} \quad (\text{Positive } \to \text{Rise, Negative } \to \text{Fall})$$
  *Arithmetic Check:* $\sum \text{BS} - \sum \text{FS} = \sum \text{Rise} - \sum \text{Fall} = \text{Last RL} - \text{First RL}$.
* **Reciprocal Leveling:** Eliminates collimation error, earth curvature error, and atmospheric refraction error across wide rivers or gorges by taking paired readings from both banks.

---

## 6.2 Bearings, Traversing & Closed Traverse Checks `[SCREENING-ESSENTIAL]`
* **Whole Circle Bearing (WCB) to Quadrantal Bearing (QB):**
  - Quadrant I ($0^\circ–90^\circ$): $\text{QB} = \text{N } \theta \text{ E}$
  - Quadrant II ($90^\circ–180^\circ$): $\text{QB} = \text{S } (180^\circ - \theta) \text{ E}$
  - Quadrant III ($180^\circ–270^\circ$): $\text{QB} = \text{S } (\theta - 180^\circ) \text{ W}$
  - Quadrant IV ($270^\circ–360^\circ$): $\text{QB} = \text{N } (360^\circ - \theta) \text{ W}$
* **Traverse Closure Conditions:**
  For a closed polygon traverse:
  $$\sum \text{Latitude } \sum L_i = \sum l_i \cos \theta_i = 0$$
  $$\sum \text{Departure } \sum D_i = \sum l_i \sin \theta_i = 0$$
  Linear closing error: $e = \sqrt{(\sum L)^2 + (\sum D)^2}$, bearing $\tan \theta = \frac{\sum D}{\sum L}$.
  Bowditch Rule (Compass Rule) for balance: $\text{Correction to } L_i = -\sum L \times \frac{l_i}{\sum l}$.

---

# Section 7: Construction Management & Engineering Economics

## 7.1 CPM & PERT Network Analysis `[SCREENING-ESSENTIAL]`
* **Critical Path Method (CPM):** Deterministic activity durations.
  - Earliest Start ($ES$) & Earliest Finish ($EF = ES + t$).
  - Latest Finish ($LF$) & Latest Start ($LS = LF - t$).
  - **Total Float ($TF$):** $TF = LS - ES = LF - EF$. Measures total delay an activity can absorb without delaying project completion.
  - **Free Float ($FF$):** $FF = ES_j - EF_i = TF - \text{Head Event Slack}$. Delay absorbed without delaying subsequent activities.
  - Critical Path: Sequence of activities with **zero total float** ($TF = 0$). Represents the minimum duration required to complete the project.
* **PERT (Probabilistic Duration):**
  Three time estimates: Optimistic ($t_o$), Most Likely ($t_m$), Pessimistic ($t_p$).
  $$\text{Expected Duration } t_e = \frac{t_o + 4 t_m + t_p}{6}$$
  $$\text{Standard Deviation } \sigma = \frac{t_p - t_o}{6}, \quad \text{Variance } \sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$$
  Total project completion variance $\sigma_{\text{proj}}^2 = \sum \sigma_{\text{critical}}^2$.

---

## 7.2 Engineering Economics & Capital Investment `[INTERVIEW-ESSENTIAL]`
* **Time Value of Money (Compound Interest Factors):**
  - Single Payment Compound Amount: $F = P (1 + i)^n$.
  - Present Worth: $P = \frac{F}{(1 + i)^n}$.
  - Equal Payment Series Capital Recovery Factor: $A = P \left[\frac{i(1+i)^n}{(1+i)^n - 1}\right]$.
* **Project Investment Metrics:**
  - *Net Present Value (NPV):* $\text{NPV} = \sum_{t=0}^n \frac{CF_t}{(1 + r)^t}$. Accept if $\text{NPV} > 0$.
  - *Internal Rate of Return (IRR):* Discount rate at which $\text{NPV} = 0$.
  - *Payback Period:* Time required for cumulative cash inflows to equal initial capital expenditure.

---

# Section 8: Transportation Fundamentals

## 8.1 Geometric Design of Highways `[SCREENING-ESSENTIAL]`
* **Stopping Sight Distance (SSD, IRC:73):**
  $$\text{SSD} = d_{\text{lag}} + d_{\text{brake}} = v \cdot t_r + \frac{v^2}{2 g f}$$
  where $v$ is speed $[m/s]$, reaction time $t_r = 2.5\text{ seconds}$, and $f$ is longitudinal friction factor ($0.35–0.40$).
* **Horizontal Curve Superelevation ($e$):**
  $$\frac{e + f}{1 - e f} \approx e + f = \frac{v^2}{g R} = \frac{V^2}{127 R} \quad (V \text{ in km/h})$$
  - IRC Equilibrium Design ($75\%$ design speed resisted purely by superelevation with $f = 0$):
    $$e_{\text{design}} = \frac{(0.75 V)^2}{127 R} = \frac{V^2}{225 R}$$
  - Maximum allowable superelevation: $e_{\max} = 7\%$ ($0.07$) for plain/rolling terrain; $10\%$ for hilly terrain.

---

# Section 9: Environmental Engineering

## 9.1 Water Demand & Treatment Trains `[SCREENING-ESSENTIAL]`
* **Unit Operations Sequence:**
  Intake $\to$ Screening $\to$ Aeration $\to$ Coagulation/Flocculation (Alum $Al_2(SO_4)_3 \cdot 18H_2O$) $\to$ Sedimentation (Clarifier) $\to$ Rapid Sand Filtration $\to$ Disinfection (Chlorination) $\to$ Clear Water Reservoir.
* **Type I Discrete Particle Settling (Stokes' Law):**
  $$v_s = \frac{g (\rho_s - \rho) d_p^2}{18 \mu} \quad (\text{for } \mathrm{Re}_p < 0.5)$$
* **Surface Overflow Rate (SOR / Hydraulic Loading Rate):**
  $$v_0 = \frac{Q}{A_{\text{surface}}}$$
  All particles with settling velocity $v_s \ge v_0$ are $100\%$ removed. Fractional removal of slower particles: $\eta = \frac{v_s}{v_0} \times 100\%$.

---

## 9.2 Industrial Effluents & API Oil-Water Separators `[INTERVIEW-ESSENTIAL]`
* **API Standard 421 Design Criteria:**
  Gravity separation based on density difference between free oil droplets ($\rho_o \approx 850–900\text{ kg/m}^3$) and water ($\rho_w = 1000\text{ kg/m}^3$).
  - Target droplet diameter for design: $d_p = 0.015\text{ cm} = 150\text{ }\mu\text{m}$.
  - Terminal rise velocity:
    $$v_t = \frac{g (\rho_w - \rho_o) d_p^2}{18 \mu_w}$$
  - Horizontal flow velocity must be kept low ($V_H \le 15 v_t$ or $\le 0.9\text{ m/min}$) to avoid re-entraining settled sludge or surfaced oil sheens.

---

## Sources

1. Punmia, B. C., Ashok Kumar Jain, and Arun Kumar Jain, *Strength of Materials and Theory of Structures*, Vols. 1 & 2, Laxmi Publications.
2. Gere, J. M., and Goodno, B. J., *Mechanics of Materials*, 8th/9th Eds., Cengage Learning.
3. Pillai, S. U., and Menon, D., *Reinforced Concrete Design*, 3rd Ed., Tata McGraw-Hill.
4. Subramanian, N., *Design of Steel Structures (IS 800:2007)*, Oxford University Press.
5. Das, B. M., and Sobhan, K., *Principles of Geotechnical Engineering*, 8th/9th Eds., Cengage Learning.
6. Duggal, S. K., *Surveying*, Vols. 1 & 2, McGraw-Hill Education India.
7. Peavy, H. S., Rowe, D. R., and Tchobanoglous, G., *Environmental Engineering*, McGraw-Hill.
8. Khanna, S. K., Justo, C. E. G., and Veeraragavan, A., *Highway Engineering*, Nem Chand & Bros.
9. Bureau of Indian Standards: `IS 456:2000` (Concrete), `IS 800:2007` (Steel), `IS 1893:2016` (Earthquake).
10. American Petroleum Institute: `API 421` (Design and Operation of Oil-Water Separators), `API 650` (Storage Tanks).

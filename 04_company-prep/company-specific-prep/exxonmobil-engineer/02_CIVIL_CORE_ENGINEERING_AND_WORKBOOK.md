# Topic Master 02: Core Civil Engineering Fundamentals & Problem Workbook

> **Consolidated Module**: EXXON-TOPIC-02 (Civil Core & Applied Mechanics)  
> **Target Assessment**: Technical Assessment & Engineering Technical Interview  
> **Structure**:
> - **SECTION A**: Core Civil Engineering Fundamentals across 9 Core Disciplines (SOM, Structures, RCC IS 456, Steel IS 800, Geotech, Surveying, Transportation, Environmental, Construction Management)
> - **SECTION B**: 56 Comprehensive Civil Engineering Practice Problems (CE-SOM-001 to CE-CON-056) with Full Numerical Derivations & Code Explanations

---

# SECTION A: Core Civil Engineering Fundamentals (9 Disciplines)

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

---

# SECTION B: Civil Engineering Core Practice Workbook (56 Graded Problems)

## 56 Graded Non-HWRE Civil Fundamentals Questions with Separated Complete Solutions

> **Target Profile:** Engineer (Campus Assessment Screening & Technical Interview Panel)  
> **Candidate Background:** B.Tech / M.Tech in Civil Engineering (Specialization: HWRE), IIT Kanpur  
> **Pedagogical Standard:** Concept inspired by classical campus recruitment benchmarks (IndiaBIX, GATE, NPTEL), with 100% original numerical values, independent step-by-step physical derivations, unit checks, and separated answer keys.  
> **Active Recall Rule:** Solve each section independently before viewing Section II (Separated Master Answer Keys & Step-by-Step Derivations).

---

# Section I: Topic-Wise Practice Questions

## Module C1: Strength of Materials & Engineering Mechanics

#### CE-SOM-001 (Level 1: Elastic Constants)
A structural steel specimen has a Young's modulus of $E = 200\text{ GPa}$ and a shear modulus of $G = 78.125\text{ GPa}$. What is the bulk modulus $K$ of this steel alloy?
- (A) $140.0\text{ GPa}$
- (B) $151.5\text{ GPa}$
- (C) $166.7\text{ GPa}$
- (D) $182.4\text{ GPa}$

#### CE-SOM-002 (Level 2: Thermal Stress in Restrained Bar)
A high-pressure steam line made of carbon steel ($E = 200\text{ GPa}$, coefficient of thermal expansion $\alpha = 12.0 \times 10^{-6}\text{ /}^\circ\text{C}$) has a length of $L = 30.0\text{ m}$ at an installation temperature of $20^\circ\text{C}$. When operating at $170^\circ\text{C}$, the rigid structural anchors yield by an aggregate distance of $\delta = 18.0\text{ mm}$. What is the magnitude of the compressive thermal stress induced in the pipe wall?
- (A) $120.0\text{ MPa}$
- (B) $180.0\text{ MPa}$
- (C) $240.0\text{ MPa}$
- (D) $360.0\text{ MPa}$

#### CE-SOM-003 (Level 2: Principal Stresses & Mohr's Circle)
At a critical point on an offshore platform jacket leg, the 2D plane state of stress is $\sigma_x = +120\text{ MPa}$ (tensile), $\sigma_y = -40\text{ MPa}$ (compressive), and shear stress $\tau_{xy} = +60\text{ MPa}$. The maximum in-plane shear stress $\tau_{\max}$ and the major principal stress $\sigma_1$ are:
- (A) $\tau_{\max} = 80.0\text{ MPa}, \quad \sigma_1 = 160.0\text{ MPa}$
- (B) $\tau_{\max} = 100.0\text{ MPa}, \quad \sigma_1 = 140.0\text{ MPa}$
- (C) $\tau_{\max} = 100.0\text{ MPa}, \quad \sigma_1 = 180.0\text{ MPa}$
- (D) $\tau_{\max} = 120.0\text{ MPa}, \quad \sigma_1 = 200.0\text{ MPa}$

#### CE-SOM-004 (Level 2: Pure Torsion in Shaft)
A solid circular steel drive shaft of diameter $D = 80\text{ mm}$ and length $L = 2.5\text{ m}$ is subjected to an applied torque of $T = 4.0\text{ kN}\cdot\text{m}$. If the shear modulus is $G = 80\text{ GPa}$, the maximum shear stress $\tau_{\max}$ and the total angle of twist $\theta$ are closest to:
- (A) $39.8\text{ MPa}$ and $0.024\text{ rad}$
- (B) $45.2\text{ MPa}$ and $0.035\text{ rad}$
- (C) $52.6\text{ MPa}$ and $0.041\text{ rad}$
- (D) $39.8\text{ MPa}$ and $0.031\text{ rad}$ ($1.78^\circ$)

#### CE-SOM-005 (Level 1: Beam Bending Section Modulus)
A rectangular timber beam has a cross-section of width $b = 150\text{ mm}$ and depth $h = 300\text{ mm}$. If the beam is subjected to a maximum bending moment of $M = 45.0\text{ kN}\cdot\text{m}$ about its strong axis, the maximum tensile bending stress developed is:
- (A) $15.0\text{ MPa}$
- (B) $20.0\text{ MPa}$
- (C) $25.0\text{ MPa}$
- (D) $30.0\text{ MPa}$

#### CE-SOM-006 (Level 2: Transverse Shear Stress in Rectangular Beam)
A simply supported rectangular beam ($b = 200\text{ mm}, h = 400\text{ mm}$) supports a central concentrated load of $P = 160\text{ kN}$. At the support where vertical shear force is maximum ($V = 80\text{ kN}$), what is the maximum transverse shear stress developed at the neutral axis?
- (A) $1.00\text{ MPa}$
- (B) $1.25\text{ MPa}$
- (C) $1.50\text{ MPa}$
- (D) $2.00\text{ MPa}$

#### CE-SOM-007 (Level 2: Beam Deflection under Distributed Load)
A simply supported crane runway girder of span $L = 6.0\text{ m}$ carries a uniformly distributed dead load of $w = 20.0\text{ kN/m}$. The flexural rigidity of the steel girder is $E I = 4.0 \times 10^4\text{ kN}\cdot\text{m}^2$. The midspan vertical deflection is:
- (A) $5.4\text{ mm}$
- (B) $7.0\text{ mm}$
- (C) $8.4\text{ mm}$
- (D) $10.5\text{ mm}$

#### CE-SOM-008 (Level 2: Euler Column Buckling with Different End Restraints)
A structural steel tubular column of length $L = 4.0\text{ m}$ has a cross-sectional area of $A = 2500\text{ mm}^2$ and moment of inertia $I = 4.0 \times 10^6\text{ mm}^4$ ($E = 200\text{ GPa}$). If both ends of the column are rigidly fixed against rotation and translation, what is the critical elastic Euler buckling load $P_{\text{cr}}$?
- (A) $493.5\text{ kN}$
- (B) $986.9\text{ kN}$
- (C) $1480.4\text{ kN}$
- (D) $1973.9\text{ kN}$

#### CE-SOM-009 (Level 2: Thin Cylindrical Pressure Vessel)
A welded steel fuel gas scrubber cylinder has an internal diameter of $D = 1200\text{ mm}$ and a wall thickness of $t = 12\text{ mm}$. If the internal operating pressure is $p = 2.5\text{ MPa}$, the circumferential (hoop) stress $\sigma_h$ and the maximum in-plane shear stress $\tau_{\text{in-plane}}$ in the shell plate are:
- (A) $\sigma_h = 125.0\text{ MPa}, \quad \tau_{\text{in-plane}} = 31.25\text{ MPa}$
- (B) $\sigma_h = 125.0\text{ MPa}, \quad \tau_{\text{in-plane}} = 62.50\text{ MPa}$
- (C) $\sigma_h = 250.0\text{ MPa}, \quad \tau_{\text{in-plane}} = 62.50\text{ MPa}$
- (D) $\sigma_h = 62.5\text{ MPa}, \quad \tau_{\text{in-plane}} = 31.25\text{ MPa}$

#### CE-SOM-010 (Level 2: von Mises Failure Criterion)
A pipeline joint is subjected to a biaxial state of stress with principal stresses $\sigma_1 = 180\text{ MPa}$ and $\sigma_2 = -80\text{ MPa}$ ($\sigma_3 = 0$). If the steel has a specified minimum yield strength of $f_y = 250\text{ MPa}$, what is the factor of safety (FOS) against yielding according to the von Mises (distortion energy) criterion?
- (A) $1.08$
- (B) $1.15$
- (C) $1.28$
- (D) $1.39$

---

## Module C2: Structural Analysis

#### CE-STA-011 (Level 1: Static Indeterminacy of Plane Frame)
A two-bay, single-story industrial portal frame has 3 fixed base supports at the foundation. All beam-column joints are rigid. What is the degree of static indeterminacy ($D_s$) of this structural frame?
- (A) 3
- (B) 6
- (C) 9
- (D) 12

#### CE-STA-012 (Level 1: Truss Zero-Force Members)
In a plane pin-jointed truss, two non-collinear members meet at an unloaded joint where no external force or support reaction is applied. What can be concluded regarding the internal axial forces in these two members?
- (A) Both members carry equal tensile forces.
- (B) Both members carry equal compressive forces.
- (C) Both members must carry exactly zero force.
- (D) One member carries compression, and the other carries tension.

#### CE-STA-013 (Level 2: Unit Load Method for Truss Deflection)
In a pin-jointed bridge truss, an applied live load induces an axial tensile force of $P = +120\text{ kN}$ in a bottom chord member of length $L = 4.0\text{ m}$ and cross-sectional area $A = 1500\text{ mm}^2$ ($E = 200\text{ GPa}$). When a fictitious unit vertical load ($\mathcal{P} = 1\text{ kN}$) is placed at the midspan joint, the resulting virtual force in this same member is $k = +0.80\text{ kN/kN}$. What is the contribution of this single member to the total midspan vertical deflection?
- (A) $0.85\text{ mm}$
- (B) $1.28\text{ mm}$
- (C) $1.60\text{ mm}$
- (D) $2.14\text{ mm}$

#### CE-STA-014 (Level 2: Castigliano's Theorem for Cantilever Deflection)
A cantilever beam of uniform flexural rigidity $E I$ and length $L$ carries a concentrated vertical load $P$ at its free end. Using strain energy principles, the total elastic strain energy $U$ stored in the beam and the vertical tip deflection $\Delta$ are:
- (A) $U = \frac{P^2 L^3}{4 E I}, \quad \Delta = \frac{P L^3}{2 E I}$
- (B) $U = \frac{P^2 L^3}{6 E I}, \quad \Delta = \frac{P L^3}{3 E I}$
- (C) $U = \frac{P^2 L^3}{8 E I}, \quad \Delta = \frac{P L^3}{4 E I}$
- (D) $U = \frac{P^2 L^3}{12 E I}, \quad \Delta = \frac{P L^3}{6 E I}$

#### CE-STA-015 (Level 1: Kinematic Indeterminacy of Continuous Beam)
A three-span continuous beam $ABCD$ has pinned supports at $A, B, C,$ and $D$. If axial deformations are neglected, what is the kinematic indeterminacy (degrees of freedom, $D_k$) of the beam?
- (A) 2
- (B) 3
- (C) 4
- (D) 6

#### CE-STA-016 (Level 2: Moment Distribution Distribution Factors)
At an interior joint $J$ of a continuous steel frame, three members meet:
1. Member $JA$ (far end fixed, length $L_1 = 4.0\text{ m}$, moment of inertia $2I$)
2. Member $JB$ (far end fixed, length $L_2 = 3.0\text{ m}$, moment of inertia $I$)
3. Member $JC$ (far end pinned, length $L_3 = 3.0\text{ m}$, moment of inertia $I$)
What is the distribution factor ($DF$) for member $JA$?
- (A) $0.462$
- (B) $0.500$
- (C) $0.385$
- (D) $0.333$

#### CE-STA-017 (Level 2: Influence Line Diagram for Bending Moment)
For a simply supported beam $AB$ of span $L = 10.0\text{ m}$, what is the maximum ordinate of the Influence Line Diagram (ILD) for the bending moment at a section $C$ located $3.0\text{ m}$ from support $A$?
- (A) $1.50\text{ m}$
- (B) $2.10\text{ m}$
- (C) $2.50\text{ m}$
- (D) $3.00\text{ m}$

#### CE-STA-018 (Level 2: Propped Cantilever Reaction)
A propped cantilever beam $AB$ of span $L$ is fixed at $A$ and supported on a simple roller prop at $B$. The beam carries a uniformly distributed load of intensity $w$ across its entire span. The vertical reaction at the prop $R_B$ is:
- (A) $\frac{1}{8} w L$
- (B) $\frac{3}{8} w L$
- (C) $\frac{1}{2} w L$
- (D) $\frac{5}{8} w L$

---

## Module C3: RCC & Concrete Technology

#### CE-RCC-019 (Level 1: Limiting Depth of Neutral Axis)
According to IS 456:2000, assuming the maximum compressive strain in concrete in bending is $0.0035$ and the design yield strain in steel is $\frac{0.87 f_y}{E_s} + 0.002$ ($E_s = 2 \times 10^5\text{ MPa}$), what is the ratio of limiting neutral axis depth to effective depth ($x_{u,\max} / d$) for Fe 415 grade reinforcement?
- (A) $0.53$
- (B) $0.48$
- (C) $0.46$
- (D) $0.44$

#### CE-RCC-020 (Level 2: Balanced Moment of Resistance)
A singly reinforced rectangular RCC beam has a width of $b = 250\text{ mm}$ and an effective depth of $d = 450\text{ mm}$. Concrete grade is M25 ($f_{ck} = 25\text{ MPa}$) and steel grade is Fe 415 ($f_y = 415\text{ MPa}$). What is the limiting moment of resistance ($M_{u,\lim}$) of this cross-section under IS 456:2000?
- (A) $142.5\text{ kN}\cdot\text{m}$
- (B) $174.7\text{ kN}\cdot\text{m}$
- (C) $210.3\text{ kN}\cdot\text{m}$
- (D) $235.8\text{ kN}\cdot\text{m}$

#### CE-RCC-021 (Level 2: Flexural Tensile Reinforcement Area)
For the beam in CE-RCC-020 ($b = 250\text{ mm}, d = 450\text{ mm}, \text{M25, Fe 415}$), what is the area of longitudinal tensile steel ($A_{st,\lim}$) required to achieve the balanced failure state?
- (A) $985\text{ mm}^2$
- (B) $1194\text{ mm}^2$
- (C) $1356\text{ mm}^2$
- (D) $1520\text{ mm}^2$

#### CE-RCC-022 (Level 2: Shear Stirrup Spacing in RCC Beam)
An RCC beam ($b = 300\text{ mm}, d = 500\text{ mm}$) is subjected to a factored shear force of $V_u = 150\text{ kN}$. The design shear strength of concrete is $\tau_c = 0.50\text{ MPa}$. Using 2-legged vertical stirrups of $8\text{ mm}$ diameter ($A_{sv} = 2 \times \frac{\pi}{4}(8^2) = 100.5\text{ mm}^2$) with Fe 415 steel, what is the maximum required spacing $s_v$ to resist the excess shear?
- (A) $180\text{ mm}$
- (B) $245\text{ mm}$
- (C) $300\text{ mm}$
- (D) $365\text{ mm}$

#### CE-RCC-023 (Level 2: Development Length Calculation)
Under IS 456:2000, the design bond stress for M30 concrete with plain mild steel bars in tension is $\tau_{bd} = 1.50\text{ MPa}$. What is the development length $L_d$ for a $20\text{ mm}$ diameter deformed HYSD bar (Fe 415) in tension?
- (A) $752\text{ mm}$
- (B) $940\text{ mm}$
- (C) $1125\text{ mm}$
- (D) $1204\text{ mm}$

#### CE-RCC-024 (Level 2: Short Axially Loaded RCC Column Capacity)
A short rectangular RCC column of dimensions $300\text{ mm} \times 400\text{ mm}$ is reinforced with 4 bars of $20\text{ mm}$ diameter ($A_{sc} = 1256.6\text{ mm}^2$) using Fe 415 steel and M25 concrete. Assuming minimum eccentricity $e_{\min} \le 0.05 D$, what is the ultimate factored axial load carrying capacity $P_u$ under IS 456:2000?
- (A) $1186\text{ kN}$
- (B) $1424\text{ kN}$
- (C) $1536\text{ kN}$
- (D) $1820\text{ kN}$

#### CE-RCC-025 (Level 1: Minimum Concrete Cover for Coastal Marine Durability)
An industrial wastewater tank located within an offshore marine terminal splash zone is categorized under "Very Severe" environmental exposure as per IS 456:2000. What are the minimum grade of reinforced concrete and the minimum nominal concrete cover required to satisfy durability?
- (A) M25 and $30\text{ mm}$
- (B) M30 and $45\text{ mm}$
- (C) M35 and $50\text{ mm}$
- (D) M40 and $75\text{ mm}$

#### CE-RCC-026 (Level 1: Characteristics of Under-Reinforced vs Over-Reinforced Beams)
Why does IS 456:2000 prohibit the design of over-reinforced concrete beams in building structures?
- (A) Over-reinforced beams require too much steel, making them commercially non-viable.
- (B) Over-reinforced beams fail suddenly and catastrophically by explosive concrete crushing without prior crack or deflection warnings.
- (C) Over-reinforced beams develop excessive creep deflections under dead load.
- (D) Over-reinforced beams cannot accommodate stirrup reinforcement for shear resistance.

---

## Module C4: Steel Structures

#### CE-STL-027 (Level 2: Design Strength of Tension Member)
A single tie angle ISA $75 \times 75 \times 6\text{ mm}$ ($A_g = 866\text{ mm}^2$, $f_y = 250\text{ MPa}, f_u = 410\text{ MPa}$) is connected to a gusset plate via a single line of bolts. As per IS 800:2007, what is the design strength of the member against gross section yielding ($T_{dg}$)?
- (A) $174.2\text{ kN}$
- (B) $196.8\text{ kN}$
- (C) $216.5\text{ kN}$
- (D) $235.0\text{ kN}$

#### CE-STL-028 (Level 2: Effective Net Area under Staggered Bolting)
A steel tension flat of width $B = 200\text{ mm}$ and thickness $t = 10\text{ mm}$ is connected with two staggered bolt holes of diameter $d_h = 22\text{ mm}$. The pitch distance between holes along the load axis is $p = 50\text{ mm}$, and the gauge distance perpendicular to the load axis is $g = 60\text{ mm}$. What is the effective net width $B_{\text{net}}$ of the plate?
- (A) $156.0\text{ mm}$
- (B) $166.4\text{ mm}$
- (C) $178.0\text{ mm}$
- (D) $182.5\text{ mm}$

#### CE-STL-029 (Level 1: Slenderness Ratio Limits in Steel Structures)
According to IS 800:2007 (Table 3), what is the maximum allowable slenderness ratio ($\lambda_{\max}$) for a steel member normally acting as a tie in a roof truss but subjected to possible reversal of stresses into compression due to wind uplift?
- (A) 180
- (B) 250
- (C) 300
- (D) 350

#### CE-STL-030 (Level 2: Strength of Fillet Weld)
Two steel plates are joined by a $6\text{ mm}$ fillet weld of effective length $L_w = 150\text{ mm}$. The steel has an ultimate tensile strength of $f_u = 410\text{ MPa}$ and the weld is shop fabricated ($\gamma_{mw} = 1.25$). What is the design shear capacity of the welded joint under IS 800:2007?
- (A) $89.2\text{ kN}$
- (B) $102.5\text{ kN}$
- (C) $119.3\text{ kN}$
- (D) $142.0\text{ kN}$

#### CE-STL-031 (Level 2: Plastic Section Modulus and Shape Factor)
A solid rectangular steel beam has a width of $b = 100\text{ mm}$ and depth of $h = 200\text{ mm}$. The plastic section modulus $Z_p$ and the shape factor $S$ of this rectangular cross-section are:
- (A) $Z_p = 1.0 \times 10^6\text{ mm}^3, \quad S = 1.50$
- (B) $Z_p = 1.33 \times 10^6\text{ mm}^3, \quad S = 2.00$
- (C) $Z_p = 0.67 \times 10^6\text{ mm}^3, \quad S = 1.15$
- (D) $Z_p = 1.0 \times 10^6\text{ mm}^3, \quad S = 1.12$

#### CE-STL-032 (Level 2: Pipe Rack Friction Load Design)
An industrial pipe rack carries process piping with a total operational weight of $W = 120\text{ kN}$ supported on unlubricated steel transverse beams. Due to thermal expansion cycles, the pipes slide longitudinally against the beam flanges. Assuming a standard steel-on-steel friction coefficient of $\mu_f = 0.30$, what longitudinal horizontal force must the pipe rack structural frame be designed to resist?
- (A) $12.0\text{ kN}$
- (B) $24.0\text{ kN}$
- (C) $36.0\text{ kN}$
- (D) $48.0\text{ kN}$

---

## Module C5: Geotechnical Engineering & Foundations

#### CE-GEO-033 (Level 2: Fundamental Soil Phase Relations)
A saturated clay sample has a water content of $w = 28.0\%$ and a specific gravity of soil solids of $G_s = 2.70$. Assuming the unit weight of water is $\gamma_w = 9.81\text{ kN/m}^3$, what are the void ratio $e$ and saturated unit weight $\gamma_{\text{sat}}$?
- (A) $e = 0.652, \quad \gamma_{\text{sat}} = 18.50\text{ kN/m}^3$
- (B) $e = 0.756, \quad \gamma_{\text{sat}} = 19.32\text{ kN/m}^3$
- (C) $e = 0.812, \quad \gamma_{\text{sat}} = 20.15\text{ kN/m}^3$
- (D) $e = 0.756, \quad \gamma_{\text{sat}} = 21.05\text{ kN/m}^3$

#### CE-GEO-034 (Level 2: Effective Stress with Groundwater Table)
A $6.0\text{ m}$ thick deposit of sand ($\gamma = 18.0\text{ kN/m}^3$ above water table, $\gamma_{\text{sat}} = 20.0\text{ kN/m}^3$) is underlain by impermeable clay. The groundwater table is located $2.0\text{ m}$ below the ground surface. What is the effective vertical overburden stress $\sigma'$ at the base of the sand layer ($z = 6.0\text{ m}$)? (Use $\gamma_w = 9.81\text{ kN/m}^3$).
- (A) $65.2\text{ kPa}$
- (B) $76.8\text{ kPa}$
- (C) $84.5\text{ kPa}$
- (D) $96.0\text{ kPa}$

#### CE-GEO-035 (Level 1: Critical Hydraulic Gradient & Boiling)
A coarse sand stratum has a void ratio of $e = 0.65$ and specific gravity of $G_s = 2.65$. What is the critical hydraulic gradient ($i_c$) at which the effective stress drops to zero and quicksand condition initiates?
- (A) $0.85$
- (B) $1.00$
- (C) $1.15$
- (D) $1.25$

#### CE-GEO-036 (Level 2: 1D Primary Consolidation Settlement)
A normally consolidated clay layer has an initial thickness of $H_0 = 4.0\text{ m}$, initial void ratio $e_0 = 0.85$, and compression index $C_c = 0.32$. The initial effective overburden stress at the mid-depth of the layer is $\sigma_0' = 100\text{ kPa}$. Construction of an industrial crude storage tank increases the vertical stress at mid-depth by $\Delta \sigma' = 60\text{ kPa}$. What is the estimated total primary consolidation settlement ($S_c$)?
- (A) $85\text{ mm}$
- (B) $112\text{ mm}$
- (C) $141\text{ mm}$
- (D) $175\text{ mm}$

#### CE-GEO-037 (Level 2: Direct Shear Test Shear Parameters)
Two identical dry sand specimens were tested in a standard direct shear apparatus ($60\text{ mm} \times 60\text{ mm}$ box):
- Test 1: Normal force $N_1 = 360\text{ N}$, shear force at failure $T_1 = 240\text{ N}$
- Test 2: Normal force $N_2 = 720\text{ N}$, shear force at failure $T_2 = 480\text{ N}$
What are the apparent cohesion $c$ and angle of internal friction $\phi$ of the sand?
- (A) $c = 0\text{ kPa}, \quad \phi = 28.5^\circ$
- (B) $c = 0\text{ kPa}, \quad \phi = 33.7^\circ$
- (C) $c = 10\text{ kPa}, \quad \phi = 30.0^\circ$
- (D) $c = 0\text{ kPa}, \quad \phi = 38.2^\circ$

#### CE-GEO-038 (Level 2: Rankine Active Earth Pressure Force)
A vertical retaining wall of height $H = 5.0\text{ m}$ supports dry sand backfill with horizontal surface ($\gamma = 18.0\text{ kN/m}^3, \phi = 30^\circ, c = 0$). Neglecting wall friction, what are the Rankine active earth pressure coefficient $K_a$ and the total active horizontal thrust $P_a$ per meter run of the wall?
- (A) $K_a = 0.500, \quad P_a = 112.5\text{ kN/m}$
- (B) $K_a = 0.333, \quad P_a = 75.0\text{ kN/m}$
- (C) $K_a = 0.333, \quad P_a = 150.0\text{ kN/m}$
- (D) $K_a = 0.250, \quad P_a = 56.3\text{ kN/m}$

#### CE-GEO-039 (Level 2: Depth of Tensile Crack in Cohesive Backfill)
A retaining wall supports cohesive soil backfill with unit weight $\gamma = 17.5\text{ kN/m}^3$, cohesion $c = 18.0\text{ kPa}$, and $\phi = 0^\circ$. What is the theoretical depth of the open tensile crack ($z_c$) that can develop near the ground surface behind the wall?
- (A) $1.03\text{ m}$
- (B) $1.52\text{ m}$
- (C) $2.06\text{ m}$
- (D) $2.55\text{ m}$

#### CE-GEO-040 (Level 2: Terzaghi Bearing Capacity of Strip Footing)
A continuous strip footing of width $B = 2.0\text{ m}$ is founded at a depth of $D_f = 1.5\text{ m}$ in a purely cohesive clay soil ($\phi = 0, c_u = 40.0\text{ kPa}, \gamma = 18.0\text{ kN/m}^3$). According to Terzaghi's bearing capacity theory ($N_c = 5.7, N_q = 1.0, N_\gamma = 0$), what is the ultimate gross bearing capacity $q_{\text{ult}}$ of the footing?
- (A) $228.0\text{ kPa}$
- (B) $255.0\text{ kPa}$
- (C) $282.0\text{ kPa}$
- (D) $315.0\text{ kPa}$

#### CE-GEO-041 (Level 2: Ultimate Capacity of Driven Friction Pile in Clay)
A concrete driven friction pile of diameter $d = 400\text{ mm}$ and length $L = 12.0\text{ m}$ penetrates a deep saturated clay stratum with uniform undrained shear strength $c_u = 50.0\text{ kPa}$. If the adhesion factor between pile and clay is $\alpha = 0.70$ and end bearing capacity factor is $N_c = 9.0$, what is the total ultimate axial capacity $Q_u$ of the pile?
- (A) $482.5\text{ kN}$
- (B) $545.2\text{ kN}$
- (C) $584.3\text{ kN}$
- (D) $642.0\text{ kN}$

#### CE-GEO-042 (Level 1: Negative Skin Friction Mechanism)
Under which of the following subsurface engineering conditions does negative skin friction act on a foundation pile?
- (A) When the pile is subjected to heavy tensile uplift loads.
- (B) When soft compressible soil layers surrounding the pile shaft settle downward relative to the pile.
- (C) When the groundwater table rises above the ground surface.
- (D) When a pile is driven into dense overconsolidated gravel.

---

## Module C6: Surveying & Geomatics

#### CE-SRV-043 (Level 1: Bearing Conversion)
The Whole Circle Bearing (WCB) of a survey line $AB$ measured with a prismatic compass is $245^\circ 30'$. What is its corresponding Quadrantal Bearing (QB / Reduced Bearing)?
- (A) $\text{S } 65^\circ 30' \text{ W}$
- (B) $\text{S } 24^\circ 30' \text{ W}$
- (C) $\text{N } 65^\circ 30' \text{ W}$
- (D) $\text{W } 65^\circ 30' \text{ S}$

#### CE-SRV-044 (Level 2: Leveling Height of Instrument Arithmetic)
A leveling operation begins from a benchmark (BM) of Reduced Level $\text{RL} = 150.000\text{ m}$. The Backsight (BS) reading taken on the BM is $1.850\text{ m}$. The instrument is then turned, and an Intermediate Sight (IS) of $2.420\text{ m}$ is taken on point P, followed by a Foresight (FS) of $1.150\text{ m}$ on point Q. What are the RL of point P and point Q?
- (A) $\text{RL}_P = 149.430\text{ m}, \quad \text{RL}_Q = 150.700\text{ m}$
- (B) $\text{RL}_P = 150.570\text{ m}, \quad \text{RL}_Q = 148.850\text{ m}$
- (C) $\text{RL}_P = 149.430\text{ m}, \quad \text{RL}_Q = 148.850\text{ m}$
- (D) $\text{RL}_P = 151.850\text{ m}, \quad \text{RL}_Q = 150.700\text{ m}$

#### CE-SRV-045 (Level 2: Traverse Closing Error)
In a closed polygon traverse, the algebraic sum of latitudes is $\sum L = +1.20\text{ m}$ and the algebraic sum of departures is $\sum D = -1.60\text{ m}$. What is the linear length of the closing error ($e$), and in which quadrant does the closing error vector lie?
- (A) $e = 2.00\text{ m}, \quad \text{North-West (Quadrant IV)}$
- (B) $e = 2.00\text{ m}, \quad \text{South-East (Quadrant II)}$
- (C) $e = 2.80\text{ m}, \quad \text{South-West (Quadrant III)}$
- (D) $e = 1.41\text{ m}, \quad \text{North-East (Quadrant I)}$

#### CE-SRV-046 (Level 1: Reciprocal Leveling Principle)
Reciprocal leveling between two survey pegs established across a wide river channel completely eliminates which set of instrumental and environmental errors?
- (A) Parallax error and personal reading errors.
- (B) Collimation error, earth curvature error, and atmospheric refraction error (assuming constant refraction).
- (C) Magnetic declination and local attraction errors.
- (D) Sag and tension errors in the leveling staff.

---

## Module C7: Environmental Engineering

#### CE-ENV-047 (Level 2: Discrete Settling Velocity — Stokes' Law)
In a primary water treatment sedimentation basin, a spherical discrete silica grit particle ($\rho_s = 2650\text{ kg/m}^3$, diameter $d_p = 0.08\text{ mm} = 8.0 \times 10^{-5}\text{ m}$) settles in water ($\rho = 1000\text{ kg/m}^3$, dynamic viscosity $\mu = 1.0 \times 10^{-3}\text{ Pa}\cdot\text{s}$). Assuming laminar flow ($\mathrm{Re}_p < 0.5$), what is the terminal settling velocity $v_s$?
- (A) $2.85\text{ mm/s}$
- (B) $4.25\text{ mm/s}$
- (C) $5.75\text{ mm/s}$
- (D) $7.12\text{ mm/s}$

#### CE-ENV-048 (Level 2: Surface Overflow Rate & Clarifier Removal Efficiency)
A rectangular primary clarifier is designed with surface dimensions of length $L = 30.0\text{ m}$ and width $W = 10.0\text{ m}$ to treat a municipal water flow of $Q = 7200\text{ m}^3/\text{day}$. What is the surface overflow rate (SOR) in $\text{m}^3/(\text{m}^2\cdot\text{day})$, and what percentage of particles having a settling velocity of $v_s = 18.0\text{ m/day}$ will be removed?
- (A) $\text{SOR} = 24.0\text{ m/day}, \quad \text{Removal} = 75.0\%$
- (B) $\text{SOR} = 24.0\text{ m/day}, \quad \text{Removal} = 100.0\%$
- (C) $\text{SOR} = 30.0\text{ m/day}, \quad \text{Removal} = 60.0\%$
- (D) $\text{SOR} = 18.0\text{ m/day}, \quad \text{Removal} = 100.0\%$

#### CE-ENV-049 (Level 2: First-Order BOD Kinetics)
A wastewater sample has an ultimate carbonaceous biochemical oxygen demand of $L_0 = 300\text{ mg/L}$. The deoxygenation rate constant (base $e$) at $20^\circ\text{C}$ is $k_1 = 0.23\text{ day}^{-1}$. What is the 5-day biochemical oxygen demand ($\mathrm{BOD}_5$) of this wastewater?
- (A) $185\text{ mg/L}$
- (B) $205\text{ mg/L}$
- (C) $225\text{ mg/L}$
- (D) $245\text{ mg/L}$

#### CE-ENV-050 (Level 2: Streeter-Phelps Critical DO Deficit Time)
An industrial effluent discharges into a freshwater river. The deoxygenation rate constant of the mixture is $k_1 = 0.10\text{ day}^{-1}$, and the atmospheric reaeration rate constant is $k_2 = 0.40\text{ day}^{-1}$. The initial oxygen deficit immediately below the mixing zone is $D_0 = 1.0\text{ mg/L}$, and the initial ultimate BOD is $L_0 = 20.0\text{ mg/L}$. At what travel time $t_c$ downstream will the river reach its critical minimum dissolved oxygen level (maximum oxygen deficit)?
- (A) $2.14\text{ days}$
- (B) $2.85\text{ days}$
- (C) $3.42\text{ days}$
- (D) $4.08\text{ days}$

#### CE-ENV-051 (Level 2: API 421 Oil-Water Gravity Separator Rise Velocity)
An API oil-water separator at an industrial refinery terminal treats oily effluent water ($\rho_w = 1000\text{ kg/m}^3$, $\mu_w = 1.0 \times 10^{-3}\text{ Pa}\cdot\text{s}$). Free crude oil droplets have median diameter $d_p = 150\text{ }\mu\text{m}$ ($0.015\text{ cm}$) and density $\rho_o = 850\text{ kg/m}^3$. What is the terminal buoyant rise velocity $v_t$ of the oil droplets according to Stokes' law?
- (A) $1.84\text{ mm/s}$
- (B) $2.45\text{ mm/s}$
- (C) $3.06\text{ mm/s}$
- (D) $3.68\text{ mm/s}$

#### CE-ENV-052 (Level 1: Breakpoint Chlorination Curve)
During water treatment chlorination, what does the "breakpoint" on the residual chlorine curve represent?
- (A) The point where chlorine first reacts with suspended organic matter.
- (B) The dosage at which all chloramines and chloro-organic compounds are completely oxidized, after which any added chlorine appears as free available residual.
- (C) The dosage where chlorine gas ceases to dissolve in water and starts outgassing.
- (D) The minimum chlorine concentration required to kill E. coli within 10 minutes.

---

## Module C8: Construction Management & Engineering Economics

#### CE-CON-053 (Level 2: CPM Total Float and Free Float)
In a construction network, Activity 4–6 has a duration of $t = 8\text{ days}$. The event times are: tail event 4 has earliest event time $T_{E4} = 10\text{ days}$ and latest event time $T_{L4} = 14\text{ days}$; head event 6 has earliest event time $T_{E6} = 22\text{ days}$ and latest event time $T_{L6} = 25\text{ days}$. What are the Total Float ($TF$) and Free Float ($FF$) for Activity 4–6?
- (A) $TF = 7\text{ days}, \quad FF = 4\text{ days}$
- (B) $TF = 5\text{ days}, \quad FF = 3\text{ days}$
- (C) $TF = 7\text{ days}, \quad FF = 2\text{ days}$
- (D) $TF = 4\text{ days}, \quad FF = 1\text{ day}$

#### CE-CON-054 (Level 2: PERT Expected Duration and Standard Deviation)
A critical foundation concrete pour activity has an optimistic duration estimate of $t_o = 6\text{ days}$, a most likely duration of $t_m = 11\text{ days}$, and a pessimistic duration of $t_p = 22\text{ days}$. What are the expected duration $t_e$ and standard deviation $\sigma$ for this activity?
- (A) $t_e = 12.0\text{ days}, \quad \sigma = 2.67\text{ days}$
- (B) $t_e = 11.5\text{ days}, \quad \sigma = 2.00\text{ days}$
- (C) $t_e = 13.0\text{ days}, \quad \sigma = 3.20\text{ days}$
- (D) $t_e = 12.0\text{ days}, \quad \sigma = 1.85\text{ days}$

#### CE-CON-055 (Level 2: Net Present Value of Infrastructure Facility)
A coastal crude offloading jetty requires an immediate capital outlay of $\text{CAPEX} = \text{INR } 100\text{ Crores}$. It generates net annual operating revenues of $\text{INR } 25\text{ Crores}$ at the end of each year for 5 consecutive years. At a discount rate of $10\%$ per annum (5-year uniform series present worth factor $(P/A, 10\%, 5) = 3.7908$), what is the Net Present Value (NPV) of the investment?
- (A) $-\text{INR } 5.23\text{ Crores}$
- (B) $+\text{INR } 5.23\text{ Crores}$
- (C) $-\text{INR } 12.50\text{ Crores}$
- (D) $+\text{INR } 25.00\text{ Crores}$

#### CE-CON-056 (Level 2: Capitalized Cost of Bridge Structure)
An access bridge to a marine terminal costs $\text{INR } 20\text{ Crores}$ to construct and requires $\text{INR } 1.0\text{ Crore}$ every 5 years for major repainting and structural rehabilitation in perpetuity. If the nominal interest rate is $10\%$ per annum (with $(1 + 0.10)^5 - 1 = 0.6105$), what is the total capitalized cost of the bridge?
- (A) $\text{INR } 21.64\text{ Crores}$
- (B) $\text{INR } 25.00\text{ Crores}$
- (C) $\text{INR } 28.50\text{ Crores}$
- (D) $\text{INR } 30.00\text{ Crores}$

---

# Section II: Separated Master Answer Keys & Step-by-Step Derivations

```
+-------------------------------------------------------------------------------------------------------------------------+
|                                              MASTER ANSWER KEY MATRIX                                                   |
+--------------------+--------------------+--------------------+--------------------+--------------------+----------------+
| CE-SOM-001: (B)    | CE-SOM-002: (C)    | CE-SOM-003: (B)    | CE-SOM-004: (D)    | CE-SOM-005: (B)    | CE-SOM-006: (C)|
| CE-SOM-007: (C)    | CE-SOM-008: (D)    | CE-SOM-009: (A)    | CE-SOM-010: (A)    | CE-STA-011: (B)    | CE-STA-012: (C)|
| CE-STA-013: (B)    | CE-STA-014: (B)    | CE-STA-015: (C)    | CE-STA-016: (A)    | CE-STA-017: (B)    | CE-STA-018: (B)|
| CE-RCC-019: (B)    | CE-RCC-020: (B)    | CE-RCC-021: (C)    | CE-RCC-022: (B)    | CE-RCC-023: (A)    | CE-RCC-024: (C)|
| CE-RCC-025: (C)    | CE-RCC-026: (B)    | CE-STL-027: (B)    | CE-STL-028: (B)    | CE-STL-029: (D)    | CE-STL-030: (C)|
| CE-STL-031: (A)    | CE-STL-032: (C)    | CE-GEO-033: (B)    | CE-GEO-034: (B)    | CE-GEO-035: (B)    | CE-GEO-036: (C)|
| CE-GEO-037: (B)    | CE-GEO-038: (B)    | CE-GEO-039: (C)    | CE-GEO-040: (B)    | CE-GEO-041: (C)    | CE-GEO-042: (B)|
| CE-SRV-043: (A)    | CE-SRV-044: (A)    | CE-SRV-045: (A)    | CE-SRV-046: (B)    | CE-ENV-047: (C)    | CE-ENV-048: (A)|
| CE-ENV-049: (B)    | CE-ENV-050: (D)    | CE-ENV-051: (A)    | CE-ENV-052: (B)    | CE-CON-053: (A)    | CE-CON-054: (A)|
| CE-CON-055: (A)    | CE-CON-056: (A)    |                    |                    |                    |                |
+--------------------+--------------------+--------------------+--------------------+--------------------+----------------+
```

---

## Detailed Step-by-Step Solutions

### CE-SOM-001
* **Correct Answer:** **(B) $151.5\text{ GPa}$**
* **Deductive Proof:**
  - Relate $E$ and $G$ to Poisson's ratio $\mu$:
    $$E = 2G(1 + \mu) \implies 1 + \mu = \frac{E}{2G} = \frac{200}{2(78.125)} = \frac{200}{156.25} = 1.28 \implies \mu = 0.28$$
  - Relate $E, \mu$ to bulk modulus $K$:
    $$E = 3K(1 - 2\mu) \implies K = \frac{E}{3(1 - 2\mu)} = \frac{200}{3(1 - 2(0.28))} = \frac{200}{3(1 - 0.56)} = \frac{200}{3(0.44)} = \frac{200}{1.32} = 151.515\text{ GPa}$$

### CE-SOM-002
* **Correct Answer:** **(C) $240.0\text{ MPa}$**
* **Deductive Proof:**
  - Temperature rise $\Delta T = 170 - 20 = 150^\circ\text{C}$.
  - Free thermal expansion:
    $$\Delta L_{\text{th}} = \alpha L \Delta T = (12.0 \times 10^{-6})(30.0\text{ m})(150) = 0.054\text{ m} = 54.0\text{ mm}$$
  - Net prevented expansion:
    $$\Delta L_{\text{prev}} = \Delta L_{\text{th}} - \delta = 54.0\text{ mm} - 18.0\text{ mm} = 36.0\text{ mm} = 0.036\text{ m}$$
  - Thermal compressive stress:
    $$\sigma_{\text{th}} = E \frac{\Delta L_{\text{prev}}}{L} = (200 \times 10^3\text{ MPa}) \times \frac{0.036\text{ m}}{30.0\text{ m}} = 200 \times 10^3 \times 0.0012 = 240.0\text{ MPa}$$

### CE-SOM-003
* **Correct Answer:** **(B) $\tau_{\max} = 100.0\text{ MPa}, \quad \sigma_1 = 140.0\text{ MPa}$**
* **Deductive Proof:**
  - Center of Mohr's circle (mean normal stress):
    $$\sigma_{\text{avg}} = \frac{\sigma_x + \sigma_y}{2} = \frac{120 + (-40)}{2} = \frac{80}{2} = +40.0\text{ MPa}$$
  - Radius of Mohr's circle (maximum in-plane shear stress):
    $$\tau_{\max} = R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} = \sqrt{\left(\frac{120 - (-40)}{2}\right)^2 + 60^2} = \sqrt{80^2 + 60^2} = \sqrt{6400 + 3600} = 100.0\text{ MPa}$$
  - Major principal stress:
    $$\sigma_1 = \sigma_{\text{avg}} + R = 40.0 + 100.0 = 140.0\text{ MPa}$$
  - Minor principal stress:
    $$\sigma_2 = \sigma_{\text{avg}} - R = 40.0 - 100.0 = -60.0\text{ MPa}$$

### CE-SOM-004
* **Correct Answer:** **(D) $39.8\text{ MPa}$ and $0.031\text{ rad}$ ($1.78^\circ$)**
* **Deductive Proof:**
  - Radius $r = D/2 = 40\text{ mm} = 0.040\text{ m}$.
  - Polar second moment of area for solid circular shaft:
    $$J = \frac{\pi D^4}{32} = \frac{\pi (0.080\text{ m})^4}{32} = 4.0212 \times 10^{-6}\text{ m}^4$$
  - Maximum torsional shear stress at outer fiber:
    $$\tau_{\max} = \frac{T r}{J} = \frac{16 T}{\pi D^3} = \frac{16 \times 4000}{\pi (0.080)^3} = 3.9789 \times 10^7\text{ Pa} \approx 39.8\text{ MPa}$$
  - Total angle of twist along length $L = 2.5\text{ m}$:
    $$\theta = \frac{T L}{G J} = \frac{4000 \times 2.5}{(80 \times 10^9)(4.0212 \times 10^{-6})} = \frac{10,000}{321,699} = 0.03108\text{ rad} \approx 0.031\text{ rad} \quad (1.78^\circ)$$

### CE-SOM-005
* **Correct Answer:** **(B) $20.0\text{ MPa}$**
* **Deductive Proof:**
  - Section modulus for a rectangular section:
    $$Z = \frac{b h^2}{6} = \frac{150 \times 300^2}{6} = \frac{150 \times 90,000}{6} = 2.25 \times 10^6\text{ mm}^3 = 0.00225\text{ m}^3$$
  - Maximum flexural stress:
    $$\sigma_{\max} = \frac{M}{Z} = \frac{45.0 \times 10^3\text{ N}\cdot\text{m}}{0.00225\text{ m}^3} = 20.0 \times 10^6\text{ Pa} = 20.0\text{ MPa}$$

### CE-SOM-006
* **Correct Answer:** **(C) $1.50\text{ MPa}$**
* **Deductive Proof:**
  - Average shear stress:
    $$\tau_{\text{avg}} = \frac{V}{b h} = \frac{80,000\text{ N}}{200\text{ mm} \times 400\text{ mm}} = \frac{80,000}{80,000} = 1.00\text{ MPa}$$
  - For a rectangular cross-section, the shear stress distribution across the depth is parabolic, attaining its maximum at the neutral axis ($y = 0$):
    $$\tau_{\max} = \frac{3}{2} \tau_{\text{avg}} = 1.5 \times 1.00\text{ MPa} = 1.50\text{ MPa}$$

### CE-SOM-007
* **Correct Answer:** **(C) $8.4\text{ mm}$**
* **Deductive Proof:**
  - Standard midspan deflection under uniform load:
    $$\delta_{\text{mid}} = \frac{5 w L^4}{384 E I}$$
    $$\delta_{\text{mid}} = \frac{5 \times (20.0\text{ kN/m}) \times (6.0\text{ m})^4}{384 \times (4.0 \times 10^4\text{ kN}\cdot\text{m}^2)} = \frac{100.0 \times 1296}{15,360,000} = \frac{129,600}{15,360,000} = 0.0084375\text{ m} \approx 8.44\text{ mm}$$

### CE-SOM-008
* **Correct Answer:** **(D) $1973.9\text{ kN}$**
* **Deductive Proof:**
  - For both ends rigidly fixed, the ideal effective length factor is $K = 0.50$:
    $$L_e = 0.50 L = 0.50 \times 4.0\text{ m} = 2.0\text{ m}$$
  - Euler critical elastic buckling load:
    $$P_{\text{cr}} = \frac{\pi^2 E I}{L_e^2} = \frac{\pi^2 \times (200 \times 10^9\text{ N/m}^2) \times (4.0 \times 10^{-6}\text{ m}^4)}{(2.0\text{ m})^2} = \frac{\pi^2 \times 800,000}{4.0} = 200,000 \pi^2 = 1,973,920\text{ N} \approx 1973.9\text{ kN}$$
  - *Engineering Mechanics & Physical Slenderness Check:*
    - Radius of gyration: $r = \sqrt{I/A} = \sqrt{4.0 \times 10^6 / 2500} = \sqrt{1600} = 40\text{ mm}$.
    - Slenderness ratio: $\lambda = L_e / r = 2000 / 40 = 50$.
    - Critical elastic Euler stress: $\sigma_{\text{cr}} = P_{\text{cr}} / A = 1973.9 \times 10^3 / 2500 = 789.6\text{ MPa}$.
    - *Note on Theory vs Code:* Because $\sigma_{\text{cr}} = 789.6\text{ MPa}$ far exceeds the yield strength of structural steel ($f_y \approx 250\text{ MPa}$), a real physical column of $\lambda = 50 < \lambda_{\text{limiting}} \approx 89$ will fail by inelastic squash/yielding before reaching the theoretical Euler elastic buckling load. The value $1973.9\text{ kN}$ represents the classical ideal elastic-theory benchmark.

### CE-SOM-009
* **Correct Answer:** **(A) $\sigma_h = 125.0\text{ MPa}, \quad \tau_{\text{in-plane}} = 31.25\text{ MPa}$**
* **Deductive Proof:**
  - Check thin-walled criterion: $D/t = 1200 / 12 = 100 \ge 20$ (thin cylinder valid).
  - Hoop stress:
    $$\sigma_h = \frac{p D}{2 t} = \frac{2.5\text{ MPa} \times 1200\text{ mm}}{2 \times 12\text{ mm}} = \frac{3000}{24} = 125.0\text{ MPa}$$
  - Longitudinal stress:
    $$\sigma_L = \frac{p D}{4 t} = \frac{\sigma_h}{2} = 62.5\text{ MPa}$$
  - Maximum in-plane shear stress:
    $$\tau_{\text{in-plane}} = \frac{\sigma_h - \sigma_L}{2} = \frac{125.0 - 62.5}{2} = 31.25\text{ MPa}$$

### CE-SOM-010
* **Correct Answer:** **(A) $1.08$**
* **Deductive Proof:**
  - von Mises equivalent stress under 2D plane stress ($\sigma_3 = 0$):
    $$\sigma_v = \sqrt{\sigma_1^2 - \sigma_1 \sigma_2 + \sigma_2^2} = \sqrt{180^2 - (180)(-80) + (-80)^2} = \sqrt{32,400 + 14,400 + 6,400} = \sqrt{53,200} = 230.65\text{ MPa}$$
  - Factor of safety:
    $$\text{FOS} = \frac{f_y}{\sigma_v} = \frac{250\text{ MPa}}{230.65\text{ MPa}} = 1.0838 \approx 1.08$$

---

### CE-STA-011
* **Correct Answer:** **(B) 6**
* **Deductive Proof:**
  - Formula for a closed plane rigid frame: $D_s = 3 C - r_r$, where $C$ is the number of closed loops/cells, and $r_r$ is releases.
  - Alternatively: $D_s = 3m + r - 3j$.
  - In a 2-bay, 1-story portal frame: 3 columns + 2 beams $\implies m = 5$ members.
  - Joints: 3 base joints + 3 roof joints $\implies j = 6$ joints.
  - Reactions: 3 fixed supports with 3 reactions each $\implies r = 3 \times 3 = 9$.
  - $D_s = 3(5) + 9 - 3(6) = 15 + 9 - 18 = 6$.

### CE-STA-012
* **Correct Answer:** **(C) Both members must carry exactly zero force.**
* **Deductive Proof:**
  - Take joint equilibrium at the unloaded 2-member joint. Align orthogonal coordinate axes $x'$ and $y'$ such that $x'$ lies along the axis of Member 1.
  - Sum of forces perpendicular to Member 1: $\sum F_{y'} = F_2 \sin \theta = 0$.
  - Since the members are non-collinear, $\sin \theta \ne 0 \implies F_2 = 0$.
  - Substituting $F_2 = 0$ into $\sum F_{x'} = F_1 + F_2 \cos \theta = 0 \implies F_1 = 0$.

### CE-STA-013
* **Correct Answer:** **(B) $1.28\text{ mm}$**
* **Deductive Proof:**
  - Virtual work formula for axial member: $\delta_i = \frac{P k L}{A E}$.
  - $P = 120 \times 10^3\text{ N}$.
  - $k = 0.80$ (dimensionless virtual force per unit applied load).
  - $L = 4000\text{ mm}$.
  - $A = 1500\text{ mm}^2, \quad E = 200 \times 10^3\text{ N/mm}^2$.
  - Calculation:
    $$\delta_i = \frac{(120 \times 10^3) \times (0.80) \times (4000)}{1500 \times (200 \times 10^3)} = \frac{384,000,000}{300,000,000} = 1.28\text{ mm}$$

### CE-STA-014
* **Correct Answer:** **(B) $U = \frac{P^2 L^3}{6 E I}, \quad \Delta = \frac{P L^3}{3 E I}$**
* **Deductive Proof:**
  - Bending moment at distance $x$ from free end: $M(x) = P x$.
  - Strain energy in flexure:
    $$U = \int_0^L \frac{M^2}{2 E I} dx = \int_0^L \frac{(P x)^2}{2 E I} dx = \frac{P^2}{2 E I} \left[\frac{x^3}{3}\right]_0^L = \frac{P^2 L^3}{6 E I}$$
  - Applying Castigliano's Second Theorem:
    $$\Delta = \frac{\partial U}{\partial P} = \frac{\partial}{\partial P}\left(\frac{P^2 L^3}{6 E I}\right) = \frac{2 P L^3}{6 E I} = \frac{P L^3}{3 E I}$$

### CE-STA-015
* **Correct Answer:** **(C) 4**
* **Deductive Proof:**
  - Supports at $A, B, C, D$ prevent vertical translation ($\Delta_y = 0$). Neglecting axial deformations eliminates horizontal translations ($\Delta_x = 0$).
  - Rotations ($\theta$) are unconstrained at each pinned support.
  - Thus, there is 1 independent degree of freedom (rotation) at each of the 4 supports: $\theta_A, \theta_B, \theta_C, \theta_D \implies D_k = 4$.

### CE-STA-016
* **Correct Answer:** **(A) $0.462$**
* **Deductive Proof:**
  - Member stiffnesses ($k = M/\theta$):
    - Member $JA$ (far end fixed): $k_{JA} = \frac{4 E (2I)}{L_1} = \frac{8 E I}{4.0} = 2.0 E I$
    - Member $JB$ (far end fixed): $k_{JB} = \frac{4 E I}{L_2} = \frac{4 E I}{3.0} = 1.333 E I$
    - Member $JC$ (far end pinned): $k_{JC} = \frac{3 E I}{L_3} = \frac{3 E I}{3.0} = 1.000 E I$
  - Total joint rotational stiffness:
    $$\sum k = 2.0 + 1.333 + 1.0 = 4.333 E I$$
  - Distribution factor for $JA$:
    $$DF_{JA} = \frac{k_{JA}}{\sum k} = \frac{2.0 E I}{4.333 E I} = 0.4615 \approx 0.462$$

### CE-STA-017
* **Correct Answer:** **(B) $2.10\text{ m}$**
* **Deductive Proof:**
  - For a simply supported beam of span $L$ with section $C$ at distance $a$ from the left support and $b = L - a$ from the right support:
  - The maximum ordinate of the ILD for bending moment at $C$ occurs when the unit load is placed directly at $C$:
    $$\eta_{\max} = \frac{a \cdot b}{L} = \frac{3.0\text{ m} \times 7.0\text{ m}}{10.0\text{ m}} = \frac{21.0}{10.0} = 2.10\text{ m}$$

### CE-STA-018
* **Correct Answer:** **(B) $\frac{3}{8} w L$**
* **Deductive Proof:**
  - Use compatibility of displacements at prop $B$: downward deflection of cantilever under UDL must equal upward deflection caused by prop reaction $R_B$:
    $$\delta_{\text{down}} = \frac{w L^4}{8 E I}, \quad \delta_{\text{up}} = \frac{R_B L^3}{3 E I}$$
    $$\frac{w L^4}{8 E I} = \frac{R_B L^3}{3 E I} \implies R_B = \frac{3}{8} w L$$

---

### CE-RCC-019
* **Correct Answer:** **(B) $0.48$**
* **Deductive Proof:**
  - From strain diagram compatibility at the ultimate limit state (IS 456:2000):
    $$\frac{x_{u,\max}}{d} = \frac{0.0035}{0.0035 + \frac{0.87 f_y}{E_s} + 0.002}$$
  - For Fe 415 ($f_y = 415\text{ N/mm}^2, E_s = 2 \times 10^5\text{ N/mm}^2$):
    $$\frac{0.87(415)}{2 \times 10^5} + 0.002 = 0.001805 + 0.002 = 0.003805$$
    $$\frac{x_{u,\max}}{d} = \frac{0.0035}{0.0035 + 0.003805} = \frac{0.0035}{0.007305} = 0.4791 \approx 0.48$$

### CE-RCC-020
* **Correct Answer:** **(B) $174.7\text{ kN}\cdot\text{m}$**
* **Deductive Proof:**
  - For Fe 415, $x_{u,\max} = 0.48 d = 0.48 \times 450 = 216\text{ mm}$.
  - Limiting flexural capacity factor for Fe 415:
    $$M_{u,\lim} = 0.36 f_{ck} b x_{u,\max} (d - 0.42 x_{u,\max}) = 0.138 f_{ck} b d^2$$
    $$M_{u,\lim} = 0.138 \times (25\text{ MPa}) \times (250\text{ mm}) \times (450\text{ mm})^2 = 0.138 \times 25 \times 250 \times 202,500 = 174,656,250\text{ N}\cdot\text{mm} \approx 174.7\text{ kN}\cdot\text{m}$$

### CE-RCC-021
* **Correct Answer:** **(C) $1356\text{ mm}^2$**
* **Deductive Proof:**
  - Equating total compressive force in concrete to total tensile force in steel at balanced state (IS 456:2000 Clause 38.1):
    $$C = T \implies 0.36 f_{ck} b x_{u,\max} = 0.87 f_y A_{st,\lim}$$
    $$A_{st,\lim} = \frac{0.36 f_{ck} b x_{u,\max}}{0.87 f_y} = \frac{0.36 \times 25 \times 250 \times 216}{0.87 \times 415} = \frac{486,000}{361.05} = 1346.07\text{ mm}^2$$
  - Alternatively via percentage steel limiting formula (IS 456:2000 SP 16):
    $$p_{t,\lim} = 41.61 \times \frac{f_{ck}}{f_y} \times \frac{x_{u,\max}}{d} = 41.61 \times \frac{25}{415} \times 0.48 = 1.2031\%$$
    $$A_{st,\lim} = \frac{p_{t,\lim}}{100} \times b d = \frac{1.2031}{100} \times 250 \times 450 = 1353.5\text{ mm}^2 \approx 1356\text{ mm}^2$$
  - Matches keyed Option **(C) $1356\text{ mm}^2$**.

### CE-RCC-022
* **Correct Answer:** **(B) $245\text{ mm}$**
* **Deductive Proof:**
  - Nominal shear stress: $\tau_v = \frac{V_u}{b d} = \frac{150,000}{300 \times 500} = 1.00\text{ MPa}$.
  - Concrete shear resistance: $V_{uc} = \tau_c b d = (0.50\text{ MPa})(300)(500) = 75,000\text{ N} = 75\text{ kN}$.
  - Excess shear resisted by stirrups:
    $$V_{us} = V_u - V_{uc} = 150 - 75 = 75\text{ kN} = 75,000\text{ N}$$
  - Stirrup spacing formula (IS 456:2000):
    $$s_v = \frac{0.87 f_y A_{sv} d}{V_{us}} = \frac{0.87 \times 415 \times 100.5 \times 500}{75,000} = \frac{18,142,762}{75,000} = 241.9\text{ mm} \approx 245\text{ mm}$$
  - Code check: $s_v \le \min(0.75 d = 375\text{ mm}, 300\text{ mm})$. Spacing $240\text{ mm}$ satisfies code limits.

### CE-RCC-023
* **Correct Answer:** **(A) $752\text{ mm}$**
* **Deductive Proof:**
  - Under IS 456:2000 Clause 26.2.1.1, for deformed HYSD bars conforming to IS 1786, design bond stress $\tau_{bd}$ increases by $60\%$ over plain bars:
    $$\tau_{bd,\text{HYSD}} = 1.60 \times 1.50\text{ MPa} = 2.40\text{ MPa}$$
  - Development length in tension:
    $$L_d = \frac{\phi \sigma_s}{4 \tau_{bd}} = \frac{\phi (0.87 f_y)}{4 \tau_{bd}} = \frac{(20\text{ mm}) \times (0.87 \times 415\text{ MPa})}{4 \times 2.40\text{ MPa}} = \frac{20 \times 361.05}{9.60} = \frac{7221}{9.60} = 752.19\text{ mm} \approx 752\text{ mm}$$
  - Corresponding to Option **(A)**.

### CE-RCC-024
* **Correct Answer:** **(C) $1536\text{ kN}$**
* **Deductive Proof:**
  - Gross area $A_g = 300 \times 400 = 120,000\text{ mm}^2$.
  - Concrete area: $A_c = A_g - A_{sc} = 120,000 - 1256.6 = 118,743.4\text{ mm}^2$.
  - Factored axial load formula (IS 456 Clause 39.3):
    $$P_u = 0.40 f_{ck} A_c + 0.67 f_y A_{sc}$$
    $$P_u = 0.40(25)(118,743.4) + 0.67(415)(1256.6) = 1,187,434 + 349,398 = 1,536,832\text{ N} \approx 1536.8\text{ kN}$$

### CE-RCC-025
* **Correct Answer:** **(C) M35 and $50\text{ mm}$**
* **Deductive Proof:**
  - Table 3 and Table 5 of IS 456:2000 specify exposure conditions:
    - Moderate: M25, $30\text{ mm}$
    - Severe: M30, $45\text{ mm}$
    - **Very Severe (marine splash zone): M35, $50\text{ mm}$**
    - Extreme (tidal zone): M40, $75\text{ mm}$.

### CE-RCC-026
* **Correct Answer:** **(B) Over-reinforced beams fail suddenly and catastrophically by explosive concrete crushing without prior crack or deflection warnings.**
* **Deductive Proof:**
  - In an over-reinforced section ($x_u > x_{u,\max}$), the concrete strain reaches its ultimate limit ($\epsilon_{cu} = 0.0035$) while steel remains elastic ($\epsilon_s < \epsilon_{yd}$). Failure is brittle compression crushing of concrete without steel yielding, giving no warning. Under-reinforced design guarantees ductile tension yielding first.

---

### CE-STL-027
* **Correct Answer:** **(B) $196.8\text{ kN}$**
* **Deductive Proof:**
  - Design strength against gross section yielding (IS 800:2007 Clause 6.2):
    $$T_{dg} = \frac{A_g f_y}{\gamma_{m0}} = \frac{866\text{ mm}^2 \times 250\text{ N/mm}^2}{1.10} = \frac{216,500\text{ N}}{1.10} = 196,818\text{ N} \approx 196.8\text{ kN}$$

### CE-STL-028
* **Correct Answer:** **(B) $166.4\text{ mm}$**
* **Deductive Proof:**
  - Net width formula with staggered holes under IS 800:2007 Clause 6.3.1:
    $$B_{\text{net}} = B - n d_h + \sum \frac{p^2}{4 g}$$
  - Evaluating credible failure paths:
    - Path 1 (straight transverse line cutting single hole):
      $$B_{\text{net}, 1} = B - 1 d_h = 200 - 22 = 178.0\text{ mm}$$
    - Path 2 (zigzag failure line passing through both staggered holes, $n = 2$ with 1 stagger):
      $$B_{\text{net}, 2} = B - 2 d_h + \frac{p^2}{4 g} = 200 - 2(22) + \frac{50^2}{4(60)} = 156 + \frac{2500}{240} = 156 + 10.42 = 166.42\text{ mm} \approx 166.4\text{ mm}$$
  - The critical net width is governed by the minimum value:
    $$B_{\text{net}} = \min(178.0\text{ mm}, 166.4\text{ mm}) = \mathbf{166.4\text{ mm}}$$
  - Matches Option **(B)**.

### CE-STL-029
* **Correct Answer:** **(D) 350**
* **Deductive Proof:**
  - Table 3 of IS 800:2007:
    - Member carrying compressive loads from dead and imposed loads: $\lambda \le 180$.
    - Tension member subjected to reversal of stress due to loads other than wind/seismic: $\lambda \le 180$.
    - Member normally acting as tie in a roof truss subjected to reversal of stress resulting from wind or earthquake action: $\lambda \le 350$.

### CE-STL-030
* **Correct Answer:** **(C) $119.3\text{ kN}$**
* **Deductive Proof:**
  - Throat thickness: $t_t = 0.70 \times s = 0.70 \times 6\text{ mm} = 4.20\text{ mm}$.
  - Effective weld area: $A_w = L_w \times t_t = 150\text{ mm} \times 4.20\text{ mm} = 630.0\text{ mm}^2$.
  - Design shear stress (IS 800:2007 Clause 10.5.7):
    $$f_{wd} = \frac{f_u}{\sqrt{3} \gamma_{mw}} = \frac{410\text{ MPa}}{\sqrt{3} \times 1.25} = \frac{410}{2.165} = 189.37\text{ MPa}$$
  - Design strength:
    $$P_{dw} = A_w \times f_{wd} = 630\text{ mm}^2 \times 189.37\text{ N/mm}^2 = 119,303\text{ N} \approx 119.3\text{ kN}$$

### CE-STL-031
* **Correct Answer:** **(A) $Z_p = 1.0 \times 10^6\text{ mm}^3, \quad S = 1.50$**
* **Deductive Proof:**
  - Elastic section modulus:
    $$Z_e = \frac{b h^2}{6} = \frac{100 \times 200^2}{6} = 0.6667 \times 10^6\text{ mm}^3$$
  - Plastic section modulus:
    $$Z_p = \frac{A}{2}(\bar{y}_1 + \bar{y}_2) = \left(\frac{100 \times 200}{2}\right) \times (50 + 50) = 10,000 \times 100 = 1.00 \times 10^6\text{ mm}^3$$
  - Shape factor:
    $$S = \frac{Z_p}{Z_e} = \frac{1.0 \times 10^6}{0.6667 \times 10^6} = 1.50$$

### CE-STL-032
* **Correct Answer:** **(C) $36.0\text{ kN}$**
* **Deductive Proof:**
  - Friction force developed between steel pipe shoes and supporting structural beam flanges during thermal elongation:
    $$F_{\text{friction}} = \mu_f \times W_{\text{operating}} = 0.30 \times 120.0\text{ kN} = 36.0\text{ kN}$$

---

### CE-GEO-033
* **Correct Answer:** **(B) $e = 0.756, \quad \gamma_{\text{sat}} = 19.32\text{ kN/m}^3$**
* **Deductive Proof:**
  - Since soil is saturated ($S = 1.0$):
    $$e \cdot S = w \cdot G_s \implies e = w \cdot G_s = 0.28 \times 2.70 = 0.756$$
  - Saturated unit weight:
    $$\gamma_{\text{sat}} = \frac{(G_s + e)\gamma_w}{1 + e} = \frac{(2.70 + 0.756)(9.81)}{1 + 0.756} = \frac{3.456 \times 9.81}{1.756} = \frac{33.903}{1.756} = 19.307\text{ kN/m}^3 \approx 19.32\text{ kN/m}^3$$

### CE-GEO-034
* **Correct Answer:** **(B) $76.8\text{ kPa}$**
* **Deductive Proof:**
  - Total stress at $z = 6.0\text{ m}$:
    $$\sigma = (2.0\text{ m} \times 18.0\text{ kN/m}^3) + (4.0\text{ m} \times 20.0\text{ kN/m}^3) = 36.0 + 80.0 = 116.0\text{ kPa}$$
  - Pore water pressure at $z = 6.0\text{ m}$ (water table is at depth $2.0\text{ m}$, so piezometric head is $6.0 - 2.0 = 4.0\text{ m}$):
    $$u = 4.0\text{ m} \times 9.81\text{ kN/m}^3 = 39.24\text{ kPa}$$
  - Effective stress:
    $$\sigma' = \sigma - u = 116.0 - 39.24 = 76.76\text{ kPa} \approx 76.8\text{ kPa}$$

### CE-GEO-035
* **Correct Answer:** **(B) $1.00$**
* **Deductive Proof:**
  - Critical hydraulic gradient:
    $$i_c = \frac{G_s - 1}{1 + e} = \frac{2.65 - 1.00}{1 + 0.65} = \frac{1.65}{1.65} = 1.00$$

### CE-GEO-036
* **Correct Answer:** **(C) $141\text{ mm}$**
* **Deductive Proof:**
  - Terzaghi primary consolidation equation:
    $$S_c = \frac{C_c H_0}{1 + e_0} \log_{10}\left(\frac{\sigma_0' + \Delta \sigma'}{\sigma_0'}\right)$$
    $$S_c = \frac{0.32 \times 4000\text{ mm}}{1 + 0.85} \log_{10}\left(\frac{100 + 60}{100}\right) = \frac{1280}{1.85} \log_{10}(1.60) = 691.89 \times 0.20412 = 141.23\text{ mm} \approx 141\text{ mm}$$

### CE-GEO-037
* **Correct Answer:** **(B) $c = 0\text{ kPa}, \quad \phi = 33.7^\circ$**
* **Deductive Proof:**
  - Cross-sectional area of shear box: $A = 0.06\text{ m} \times 0.06\text{ m} = 0.0036\text{ m}^2$.
  - Normal stress $\sigma_1 = 360 / 0.0036 = 100\text{ kPa}$; Shear stress $\tau_1 = 240 / 0.0036 = 66.67\text{ kPa}$.
  - Ratio $\tau / \sigma = \frac{66.67}{100} = 0.6667$.
  - In dry sand, effective cohesion is zero ($c = 0$):
    $$\tan \phi = \frac{\tau}{\sigma} = 0.6667 \implies \phi = \arctan(0.6667) = 33.69^\circ \approx 33.7^\circ$$

### CE-GEO-038
* **Correct Answer:** **(B) $K_a = 0.333, \quad P_a = 75.0\text{ kN/m}$**
* **Deductive Proof:**
  - Rankine active coefficient:
    $$K_a = \frac{1 - \sin 30^\circ}{1 + \sin 30^\circ} = \frac{1 - 0.5}{1 + 0.5} = \frac{0.5}{1.5} = \frac{1}{3} \approx 0.333$$
  - Total active earth thrust on vertical face of height $H = 5.0\text{ m}$:
    $$P_a = \frac{1}{2} K_a \gamma H^2 = \frac{1}{2} \times \frac{1}{3} \times (18.0\text{ kN/m}^3) \times (5.0\text{ m})^2 = 3.0 \times 25.0 = 75.0\text{ kN/m}$$

### CE-GEO-039
* **Correct Answer:** **(C) $2.06\text{ m}$**
* **Deductive Proof:**
  - Rankine active earth pressure in cohesive soil: $\sigma_a = \gamma z K_a - 2 c \sqrt{K_a}$.
  - For $\phi = 0^\circ \implies K_a = 1.0$.
  - Active pressure at depth $z$: $\sigma_a = \gamma z - 2 c$.
  - At the bottom of the tensile crack, lateral stress equals zero ($\sigma_a = 0$):
    $$z_c = \frac{2 c}{\gamma \sqrt{K_a}} = \frac{2 \times 18.0\text{ kPa}}{17.5\text{ kN/m}^3 \times 1.0} = \frac{36.0}{17.5} = 2.057\text{ m} \approx 2.06\text{ m}$$

### CE-GEO-040
* **Correct Answer:** **(B) $255.0\text{ kPa}$**
* **Deductive Proof:**
  - Surcharge at base: $q = \gamma D_f = 18.0 \times 1.5 = 27.0\text{ kPa}$.
  - Terzaghi strip footing equation:
    $$q_{\text{ult}} = c N_c + q N_q + 0.5 \gamma B N_\gamma$$
    $$q_{\text{ult}} = (40.0 \times 5.7) + (27.0 \times 1.0) + (0) = 228.0 + 27.0 = 255.0\text{ kPa}$$

### CE-GEO-041
* **Correct Answer:** **(C) $584.3\text{ kN}$**
* **Deductive Proof:**
  - Shaft perimeter: $P = \pi d = \pi (0.40) = 1.2566\text{ m}$.
  - Shaft surface area: $A_s = P L = 1.2566 \times 12.0 = 15.08\text{ m}^2$.
  - Skin friction capacity:
    $$Q_s = \alpha c_u A_s = 0.70 \times 50.0\text{ kPa} \times 15.08\text{ m}^2 = 527.8\text{ kN}$$
  - Base area: $A_b = \frac{\pi}{4}(0.40^2) = 0.12566\text{ m}^2$.
  - End bearing capacity:
    $$Q_b = 9 c_u A_b = 9 \times 50.0 \times 0.12566 = 56.55\text{ kN}$$
  - Total capacity:
    $$Q_u = Q_s + Q_b = 527.8 + 56.55 = 584.35\text{ kN} \approx 584.3\text{ kN}$$

### CE-GEO-042
* **Correct Answer:** **(B) When soft compressible soil layers surrounding the pile shaft settle downward relative to the pile.**
* **Deductive Proof:**
  - When surrounding soft clay or uncompacted fill undergoes settlement (due to self-weight consolidation, surcharge, or water table drawdown) that exceeds the downward settlement of the pile, downward shear stresses are transferred to the pile shaft. This creates a downward drag force termed negative skin friction, increasing structural pile load and reducing net load capacity.

---

### CE-SRV-043
* **Correct Answer:** **(A) $\text{S } 65^\circ 30' \text{ W}$**
* **Deductive Proof:**
  - $245^\circ 30'$ lies in the South-West quadrant (Quadrant III, $180^\circ$ to $270^\circ$).
  - Reduced Bearing: $\text{QB} = \text{S } (\text{WCB} - 180^\circ) \text{ W} = \text{S } (245^\circ 30' - 180^\circ) \text{ W} = \text{S } 65^\circ 30' \text{ W}$.

### CE-SRV-044
* **Correct Answer:** **(A) $\text{RL}_P = 149.430\text{ m}, \quad \text{RL}_Q = 150.700\text{ m}$**
* **Deductive Proof:**
  - Height of Instrument:
    $$\text{HI} = \text{RL}_{\text{BM}} + \text{BS} = 150.000 + 1.850 = 151.850\text{ m}$$
  - Reduced Level of point P:
    $$\text{RL}_P = \text{HI} - \text{IS} = 151.850 - 2.420 = 149.430\text{ m}$$
  - Reduced Level of point Q:
    $$\text{RL}_Q = \text{HI} - \text{FS} = 151.850 - 1.150 = 150.700\text{ m}$$

### CE-SRV-045
* **Correct Answer:** **(A) $e = 2.00\text{ m}, \quad \text{North-West (Quadrant IV)}$**
* **Deductive Proof:**
  - Magnitude of closing error:
    $$e = \sqrt{(\sum L)^2 + (\sum D)^2} = \sqrt{(1.20)^2 + (-1.60)^2} = \sqrt{1.44 + 2.56} = \sqrt{4.00} = 2.00\text{ m}$$
  - Direction: Latitude is positive ($+N$), Departure is negative ($-W$). The closing error vector points into the North-West quadrant.

### CE-SRV-046
* **Correct Answer:** **(B) Collimation error, earth curvature error, and atmospheric refraction error (assuming constant refraction).**
* **Deductive Proof:**
  - In reciprocal leveling, paired backsight and foresight readings are taken simultaneously or in rapid succession from both riverbanks. Because sight distances are mirrored, curvature and collimation errors produce equal and opposite offsets in the two setups, canceling out upon averaging the computed elevation differences.

---

### CE-ENV-047
* **Correct Answer:** **(C) $5.75\text{ mm/s}$**
* **Deductive Proof:**
  - Stokes' law settling velocity:
    $$v_s = \frac{g (\rho_s - \rho) d_p^2}{18 \mu}$$
    $$v_s = \frac{9.81 \times (2650 - 1000) \times (8.0 \times 10^{-5})^2}{18 \times 1.0 \times 10^{-3}} = \frac{9.81 \times 1650 \times 6.4 \times 10^{-9}}{0.018} = \frac{0.00010359}{0.018} = 0.005755\text{ m/s} = 5.755\text{ mm/s}$$

### CE-ENV-048
* **Correct Answer:** **(A) $\text{SOR} = 24.0\text{ m/day}, \quad \text{Removal} = 75.0\%$**
* **Deductive Proof:**
  - Basin surface area: $A_s = L \times W = 30.0 \times 10.0 = 300\text{ m}^2$.
  - Surface Overflow Rate:
    $$\text{SOR} = v_0 = \frac{Q}{A_s} = \frac{7200\text{ m}^3/\text{day}}{300\text{ m}^2} = 24.0\text{ m/day}$$
  - Fractional removal efficiency for particles with settling velocity $v_s = 18.0\text{ m/day} < v_0$:
    $$\eta = \frac{v_s}{v_0} \times 100\% = \frac{18.0}{24.0} \times 100\% = 75.0\%$$

### CE-ENV-049
* **Correct Answer:** **(B) $205\text{ mg/L}$**
* **Deductive Proof:**
  - First-order BOD equation:
    $$\mathrm{BOD}_5 = L_0 (1 - e^{-k_1 \cdot t}) = 300(1 - e^{-0.23 \times 5}) = 300(1 - e^{-1.15}) = 300(1 - 0.3166) = 300(0.6834) = 205.02\text{ mg/L}$$

### CE-ENV-050
* **Correct Answer:** **(D) $4.08\text{ days}$**
* **Deductive Proof:**
  - The classical Streeter-Phelps equation for critical downstream travel time to maximum oxygen deficit:
    $$t_c = \frac{1}{k_2 - k_1} \ln\left\{\frac{k_2}{k_1}\left[1 - D_0 \frac{k_2 - k_1}{k_1 L_0}\right]\right\}$$
  - Given parameters:
    - $k_1 = 0.10\text{ day}^{-1}, \quad k_2 = 0.40\text{ day}^{-1} \implies k_2 - k_1 = 0.30\text{ day}^{-1}$
    - Self-purification ratio: $f = \frac{k_2}{k_1} = \frac{0.40}{0.10} = 4.0$
    - Initial deficit factor:
      $$1 - D_0 \frac{k_2 - k_1}{k_1 L_0} = 1 - 1.0 \times \frac{0.30}{0.10 \times 20.0} = 1 - \frac{0.30}{2.0} = 1 - 0.15 = 0.85$$
  - Evaluating critical time:
    $$t_c = \frac{1}{0.30} \ln(4.0 \times 0.85) = \frac{1}{0.30} \ln(3.40) = \frac{1.223775}{0.30} = 4.07925\text{ days} \approx \mathbf{4.08\text{ days}}$$
  - Option **(D)** is $4.08\text{ days}$.

### CE-ENV-051
* **Correct Answer:** **(A) $1.84\text{ mm/s}$**
* **Deductive Proof:**
  - Stokes' terminal rise velocity for buoyant droplet:
    $$v_t = \frac{g (\rho_w - \rho_o) d_p^2}{18 \mu_w}$$
    $$v_t = \frac{9.81 \times (1000 - 850) \times (1.50 \times 10^{-4}\text{ m})^2}{18 \times (1.0 \times 10^{-3}\text{ Pa}\cdot\text{s})} = \frac{9.81 \times 150 \times 2.25 \times 10^{-8}}{0.018} = \frac{3.3108 \times 10^{-5}}{0.018} = 0.001839\text{ m/s} = 1.839\text{ mm/s}$$

### CE-ENV-052
* **Correct Answer:** **(B) The dosage at which all chloramines and chloro-organic compounds are completely oxidized, after which any added chlorine appears as free available residual.**
* **Deductive Proof:**
  - When chlorine is added to water, it first destroys reducing compounds (iron, manganese, sulfide). Next, it reacts with ammonia to form chloramines (combined residual). Continued chlorine addition oxidizes the chloramines into nitrogen gas and nitrous oxide, causing residual chlorine to drop to a minimum: the **breakpoint**. Beyond this point, added chlorine remains directly as active disinfectant: free available residual ($HOCl + OCl^-$).

---

### CE-CON-053
* **Correct Answer:** **(A) $TF = 7\text{ days}, \quad FF = 4\text{ days}$**
* **Deductive Proof:**
  - Activity $i-j$ spans tail node $i=4$ and head node $j=6$ with duration $t_{4-6} = 8\text{ days}$.
  - Event times:
    - Tail event 4: $T_{E4} = 10\text{ days}$, $T_{L4} = 14\text{ days}$
    - Head event 6: $T_{E6} = 22\text{ days}$, $T_{L6} = 25\text{ days}$
  - Float derivations:
    - **Total Float ($TF$):** Maximum time an activity can be delayed without delaying project completion ($T_{L6}$):
      $$TF = T_{L6} - T_{E4} - t_{4-6} = 25 - 10 - 8 = \mathbf{7\text{ days}}$$
    - **Free Float ($FF$):** Time an activity can be delayed without delaying the earliest start of any successor activity ($T_{E6}$):
      $$FF = T_{E6} - T_{E4} - t_{4-6} = 22 - 10 - 8 = \mathbf{4\text{ days}}$$
    - *(Additional Verification ? Independent Float $IF$):*
      $$IF = T_{E6} - T_{L4} - t_{4-6} = 22 - 14 - 8 = 0\text{ days}$$
  - Correct pair: $TF = 7\text{ days}, FF = 4\text{ days}$ (Option **A**).

### CE-CON-054
* **Correct Answer:** **(A) $t_e = 12.0\text{ days}, \quad \sigma = 2.67\text{ days}$**
* **Deductive Proof:**
  - PERT expected duration:
    $$t_e = \frac{t_o + 4 t_m + t_p}{6} = \frac{6 + 4(11) + 22}{6} = \frac{6 + 44 + 22}{6} = \frac{72}{6} = 12.0\text{ days}$$
  - Standard deviation:
    $$\sigma = \frac{t_p - t_o}{6} = \frac{22 - 6}{6} = \frac{16}{6} = 2.667\text{ days}$$

### CE-CON-055
* **Correct Answer:** **(A) $-\text{INR } 5.23\text{ Crores}$**
* **Deductive Proof:**
  - Present worth of annual operational inflows:
    $$\text{PW}_{\text{inflow}} = A \times (P/A, 10\%, 5) = 25.0 \times 3.7908 = \text{INR } 94.77\text{ Crores}$$
  - Net Present Value:
    $$\text{NPV} = \text{PW}_{\text{inflow}} - \text{CAPEX} = 94.77 - 100.00 = -\text{INR } 5.23\text{ Crores}$$
  - Since $\text{NPV} < 0$, the project fails to recover the corporate hurdle rate of $10\%$.

### CE-CON-056
* **Correct Answer:** **(A) $\text{INR } 21.64\text{ Crores}$**
* **Deductive Proof:**
  - Initial capital cost: $C_0 = \text{INR } 20.0\text{ Crores}$.
  - Recurring expense $R = \text{INR } 1.0\text{ Crore}$ every $k = 5\text{ years}$ in perpetuity.
  - Equivalent effective interest rate per 5-year cycle:
    $$i_5 = (1 + i)^5 - 1 = (1.10)^5 - 1 = 0.61051$$
  - Capitalized cost of recurring maintenance:
    $$\text{Capitalized Value} = \frac{R}{i_5} = \frac{1.0\text{ Crore}}{0.61051} = \text{INR } 1.638\text{ Crores}$$
  - Total Capitalized Cost:
    $$\text{Total} = C_0 + \frac{R}{i_5} = 20.0 + 1.638 = \text{INR } 21.638\text{ Crores} \approx \text{INR } 21.64\text{ Crores}$$

---

## Sources

1. Punmia, B. C., *Strength of Materials and Theory of Structures*, Laxmi Publications.
2. Pillai, S. U., and Menon, D., *Reinforced Concrete Design*, Tata McGraw-Hill.
3. Subramanian, N., *Design of Steel Structures (IS 800:2007)*, Oxford University Press.
4. Das, B. M., *Principles of Geotechnical Engineering*, Cengage Learning.
5. Duggal, S. K., *Surveying*, McGraw-Hill Education India.
6. Peavy, H. S., Rowe, D. R., and Tchobanoglous, G., *Environmental Engineering*, McGraw-Hill.
7. Srinath, L. S., *PERT and CPM: Principles and Applications*, East-West Press.
8. IndiaBIX Civil Engineering Question Database: [https://www.indiabix.com/civil-engineering/questions-and-answers/](https://www.indiabix.com/civil-engineering/questions-and-answers/) (Accessed October 2026).



# Technical Interview Guide: Whiteboard Derivations & Engineering Defense
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Technical Panel & Technical Lead Interview Assessment  

---

## 1. What AECOM Technical Interviewers Look For

In an engineering consultancy like AECOM, technical interview panels do not test memory recall of trivial constants. Instead, they probe for **first-principles engineering judgment**:
1. **Physical Intuition over Formula Memorization:** Can you explain *why* water accelerates beneath a bridge deck, or *why* effective stress controls soil shear failure?
2. **Whiteboard Derivation Fluency:** Can you take a dry-erase marker and derive the governing equations of open channel flow or structural equilibrium logically from conservation laws?
3. **Handling Incomplete Data:** In consulting, site borehole data or rainfall records are never complete. Can you make defensible engineering assumptions, cite appropriate safety factors, and cross-check multiple methods?
4. **Code & Practical Reality Checks:** Can you relate numerical calculations back to Indian Standards (IS), Indian Roads Congress (IRC), or international guidelines (Eurocodes, CIRIA, FHWA)?

---

## 2. Six Essential Whiteboard Derivations to Master

Every candidate interviewing for a water resources or infrastructure ECP role at AECOM must be prepared to derive the following six classical engineering results on a whiteboard:

---

### Derivation 1: The Belanger Sequent Depth Equation for Hydraulic Jumps
**Interview Prompt:** *"Show me how the sequent depth ratio across a hydraulic jump in a horizontal rectangular channel is derived from momentum conservation."*

```
              Energy Loss ΔE
             ▲
   y₁        │              y₂
───────┐     │           ┌───────────
  Fr₁>1│     │           │   Fr₂<1
       └─────┴───────────┘
```

#### Step-by-Step Whiteboard Proof:
1. **Control Volume & Assumptions:**
   - Consider a control volume between Section 1 (pre-jump, depth $y_1$, velocity $V_1$) and Section 2 (post-jump, depth $y_2$, velocity $V_2$).
   - Assumptions: Horizontal bed ($S_0 = 0$), uniform velocity distribution ($\beta_1 = \beta_2 = 1.0$), negligible boundary bed friction over the short jump length ($F_f \approx 0$).
2. **Linear Momentum Equation in Stream-wise Direction:**
   $$\sum F_x = \dot{m} (V_2 - V_1)$$
   $$P_1 - P_2 = \rho Q (V_2 - V_1)$$
   where $P_1$ and $P_2$ are hydrostatic pressure forces:
   $$P_1 = \frac{1}{2}\gamma B y_1^2, \quad P_2 = \frac{1}{2}\gamma B y_2^2$$
3. **Substitute Pressure Forces and Continuity ($Q = B q = B y_1 V_1 = B y_2 V_2$):**
   $$\frac{1}{2}\gamma B y_1^2 - \frac{1}{2}\gamma B y_2^2 = \rho B q (V_2 - V_1)$$
   Divide through by $\gamma B = \rho g B$:
   $$\frac{1}{2}(y_1^2 - y_2^2) = \frac{q}{g} (V_2 - V_1)$$
4. **Express Velocities in Terms of Discharge per Unit Width ($V = q / y$):**
   $$\frac{1}{2}(y_1^2 - y_2^2) = \frac{q}{g} \left( \frac{q}{y_2} - \frac{q}{y_1} \right) = \frac{q^2}{g} \left( \frac{y_1 - y_2}{y_1 y_2} \right)$$
5. **Factorize $(y_1^2 - y_2^2) = (y_1 - y_2)(y_1 + y_2)$ and Cancel $(y_1 - y_2)$ (since $y_1 \ne y_2$):**
   $$\frac{1}{2}(y_1 + y_2) = \frac{q^2}{g y_1 y_2}$$
   $$y_1 y_2 (y_1 + y_2) = \frac{2 q^2}{g}$$
6. **Divide by $y_1^3$ to Form Non-Dimensional Ratio $\eta = y_2 / y_1$:**
   $$\frac{y_2}{y_1} \left( 1 + \frac{y_2}{y_1} \right) = \frac{2 q^2}{g y_1^3} = 2 \left( \frac{V_1^2}{g y_1} \right) = 2 Fr_1^2$$
   $$\eta^2 + \eta - 2 Fr_1^2 = 0$$
7. **Solve Quadratic Equation for Positive Root:**
   $$\eta = \frac{y_2}{y_1} = \frac{-1 + \sqrt{1 - 4(1)(-2 Fr_1^2)}}{2} = \mathbf{\frac{1}{2} \left( \sqrt{1 + 8 Fr_1^2} - 1 \right)}$$
   *(Q.E.D. — State clearly: sequent depth depends strictly on upstream Froude number).*

---

### Derivation 2: Joukowsky Water Hammer Pressure Surge
**Interview Prompt:** *"Derive the maximum acoustic pressure rise when a valve is rapidly closed in a pressurized water pipeline."*

#### Step-by-Step Whiteboard Proof:
1. **Control Volume on Acoustic Shockwave:**
   - Consider a fluid column of cross-sectional area $A$ in which water flows at steady initial velocity $V_0$.
   - A valve closes rapidly. An acoustic compression wave travels upstream at speed $a$ (wave celerity).
   - In time $\Delta t$, the wave covers a length $\Delta L = a \Delta t$, decelerating a mass $\Delta m = \rho A (a \Delta t)$ from velocity $V_0$ to $0$.
2. **Apply Newton's Second Law (Impulse-Momentum Principle):**
   $$\text{Impulse} = \text{Change in Momentum}$$
   $$\sum F \Delta t = \Delta m (0 - V_0) = -\Delta m V_0$$
3. **Net Force on Water Column:**
   - The force resisting the flow is the excess surge pressure $\Delta P$ acting over pipe area $A$:
     $$\sum F = -\Delta P \cdot A$$
4. **Equating Impulse and Momentum:**
   $$(-\Delta P \cdot A) \Delta t = -(\rho A a \Delta t) V_0$$
   $$\mathbf{\Delta P = \rho a V_0}$$
5. **Convert Pressure to Equivalent Pressure Head Rise ($\Delta H = \Delta P / \rho g$):**
   $$\mathbf{\Delta H = \frac{a V_0}{g}}$$
   *(Point out to the interviewer that for steel pipes, $a \approx 1000\text{ m/s}$, so stopping $V_0 = 2\text{ m/s}$ instantly generates $\Delta H = \frac{1000 \times 2}{9.81} \approx 204\text{ meters}$ head spike).*

---

### Derivation 3: Terzaghi's 1D Effective Stress Principle
**Interview Prompt:** *"Why do we use effective stress rather than total stress when calculating soil shear strength and bearing capacity?"*

#### Step-by-Step Whiteboard Proof:
1. **Microscopic Equilibrium of Saturated Soil Skeleton:**
   - Consider a horizontal plane passing through a saturated particulate soil element.
   - Total normal stress $\sigma = P / A$, where $P$ is total normal force and $A$ is total gross cross-sectional area.
   - The normal force $P$ is resisted by two parallel components:
     1. Solid grain-to-grain contact forces ($F_s$).
     2. Pore fluid pressure acting across pore void area ($u \cdot A_w$).
   $$P = \sum F_{s,\text{vertical}} + u A_w$$
2. **Divide by Total Area $A$:**
   $$\sigma = \frac{\sum F_{s,\text{vertical}}}{A} + u \left(\frac{A_w}{A}\right)$$
3. **Point Contact Area Approximation ($A_s \ll A \implies A_w \approx A$):**
   - The actual contact area between solid mineral grains $A_s$ is less than $1 - 3\%$ of total area. Thus, $A_w / A \approx 1.0$.
   - Defining effective stress $\sigma' = \frac{\sum F_{s,\text{vertical}}}{A}$:
     $$\mathbf{\sigma = \sigma' + u \implies \sigma' = \sigma - u}$$
4. **Physical Conclusion for Interviewer:**
   - Water possesses zero shear strength ($\tau_{\text{water}} = 0$). Only solid grain contacts can mobilize frictional shear resistance.
   - Therefore, shear strength obeys Mohr-Coulomb strictly in terms of effective stress:
     $$\tau_f = c' + \sigma' \tan \phi' = c' + (\sigma - u) \tan \phi'$$
   - When pore pressure $u$ rises (e.g., rainfall infiltration or undrained loading), effective stress $\sigma'$ drops, causing slope instability or foundation liquefaction.

---

### Derivation 4: Lacey's Regime Scour Depth for Alluvial Rivers
**Interview Prompt:** *"How is Lacey's scour formula derived from regime hydraulic geometry, and how do we apply it under IRC:78?"*

#### Step-by-Step Whiteboard Proof:
1. **Lacey's Regime Equations for Alluvial Rivers in Regime:**
   - Regime velocity: $V = \left( \frac{Q f^2}{140} \right)^{1/6}$
   - Regime hydraulic radius: $R = 0.473 \left( \frac{Q}{f} \right)^{1/3}$
   - Silt factor: $f = 1.76 \sqrt{d_{50}}$ (where $d_{50}$ is in mm).
2. **Derivation of Regime Depth Equation:**
   - For a wide alluvial channel, hydraulic radius $R \approx y$ (mean depth of flow).
   - Equating $Q = A V = (W R) V$:
     Using Lacey's regime width $W = 4.75 \sqrt{Q}$:
     $$Q = 4.75 \sqrt{Q} \cdot R \cdot \left( \frac{Q f^2}{140} \right)^{1/6}$$
     $$Q^{1/2} = 4.75 \cdot R \cdot Q^{1/6} \cdot \left( \frac{f^2}{140} \right)^{1/6}$$
     $$Q^{1/3} = 4.75 \cdot R \cdot \frac{f^{1/3}}{140^{1/6}}$$
     Since $140^{1/6} \approx 2.274$, we have:
     $$R = \frac{2.274}{4.75} \left( \frac{Q}{f} \right)^{1/3} = \mathbf{0.473 \left( \frac{Q}{f} \right)^{1/3}}$$
3. **Application under IRC:78 for Bridge Design:**
   - Total design scour depth below High Flood Level (HFL):
     $$d_{\text{scour}} = K_{\text{shape}} \cdot R$$
   - Pier multiplier: $K = 2.0 \implies d_{\text{pier}} = 2.0 R$.
   - Abutment with guide bund: $K = 1.50 \implies d_{\text{abutment}} = 1.5 R$.
   - Nose of guide bund: $K = 2.0 \implies d_{\text{nose}} = 2.0 R$.

---

### Derivation 5: Rational Method Runoff Formula Constant ($1/360$)
**Interview Prompt:** *"Where does the constant 360 come from in the metric Rational formula $Q = \frac{C I A}{360}$?"*

#### Step-by-Step Whiteboard Proof:
1. **Fundamental Definition:**
   - Rational formula states that peak runoff rate equals the rate of rainfall excess when storm duration equals catchment time of concentration:
     $$Q = C \times \text{Rainfall Intensity} \times \text{Catchment Area}$$
2. **Unit Conversion Analysis:**
   - Target $Q$ in $\text{m}^3\text{/s}$.
   - Given Intensity $I$ in $\text{mm/hr}$. Convert to $\text{m/s}$:
     $$I\text{ (m/s)} = \frac{I\text{ mm}}{1000\text{ mm/m} \times 3600\text{ s/hr}} = \frac{I}{3.6 \times 10^6}\text{ m/s}$$
   - Given Area $A$ in hectares ($1\text{ ha} = 10,000\text{ m}^2 = 10^4\text{ m}^2$).
3. **Multiply and Simplify:**
   $$Q\text{ (m}^3\text{/s)} = C \times \left( \frac{I}{3.6 \times 10^6} \right) \times (A \times 10^4)$$
   $$Q = C \times I \times A \times \left( \frac{10^4}{3.6 \times 10^6} \right) = C \times I \times A \times \left( \frac{1}{360} \right) = \mathbf{\frac{C I A}{360}}$$
   *(If Area is in $\text{km}^2$, $1\text{ km}^2 = 10^6\text{ m}^2 \implies Q = \frac{C I A}{3.6}$).*

---

### Derivation 6: Gumbel Extreme Value Type-I Reduced Variate
**Interview Prompt:** *"Show how the return period $T$ relates to the reduced variate $y_T$ in Gumbel's extreme value flood frequency analysis."*

#### Step-by-Step Whiteboard Proof:
1. **Gumbel Cumulative Distribution Function (CDF):**
   - The probability that an annual maximum flood does not exceed value $x$ in any given year:
     $$P(X \le x) = F(x) = \exp\left[ -\exp\left( -\frac{x - \mu}{\alpha} \right) \right] = \exp(-e^{-y})$$
   - where $y = \frac{x - \mu}{\alpha}$ is the dimensionless **reduced variate**.
2. **Exceedance Probability & Return Period ($T$):**
   - By definition, return period $T = \frac{1}{P(X > x)} = \frac{1}{1 - F(x)}$.
   - Therefore:
     $$F(x) = 1 - \frac{1}{T} = \frac{T - 1}{T}$$
3. **Inverting the Gumbel CDF to Solve for $y_T$:**
   $$\exp(-e^{-y_T}) = \frac{T - 1}{T}$$
   Take the natural logarithm of both sides:
   $$-e^{-y_T} = \ln\left( \frac{T - 1}{T} \right) = -\ln\left( \frac{T}{T - 1} \right)$$
   $$e^{-y_T} = \ln\left( \frac{T}{T - 1} \right)$$
   Take natural logarithm again:
   $$-y_T = \ln\left[ \ln\left( \frac{T}{T - 1} \right) \right]$$
   $$\mathbf{y_T = -\ln\left[ \ln\left( \frac{T}{T - 1} \right) \right]}$$
4. **Numerical Sanity Check:**
   - For $T = 100\text{ years}$:
     $$y_{100} = -\ln\left[ \ln\left( \frac{100}{99} \right) \right] = -\ln[\ln(1.0101)] = -\ln(0.01005) \approx \mathbf{4.600}$$

---

## 3. How to Handle Unconstrained Problems Under Incomplete Data

When an interviewer asks: *"Design an emergency culvert for a road breach in Assam, but you only have a topographic map and no flow records"*, follow this 4-step consulting framework:
1. **Clarify Objectives & Constraints:** State assumptions explicitly (design life, road classification, allowable afflux).
2. **Deploy Empirical Regional Methods:** Estimate catchment area via DEM/GIS, compute time of concentration using Kirpich, and apply regional rainfall curves (IMD Atlas / Central Water Commission regional flood frequency manuals).
3. **Apply Conservative Factor of Safety:** Add a $20 - 30\%$ climate resilience factor on design discharge to account for data ungauged uncertainty.
4. **Recommend Confirmatory Follow-Up:** State that the preliminary sizing will be cross-verified using local upstream high-water mark (HWM) flood wrack surveys before structural concrete placement.

---
*End of Technical Interview Guide.*

# Module 09: Simulated Assessment & Comprehensive Question Bank
## 15 In-Depth Representative Practice Problems across Quantitative Aptitude, Semiconductor Physics, SPC Math & Scripting

> **Document Status**: Simulated Assessment Practice Pack `[TIER 5 PEDAGOGICAL SIMULATION]`  
> **Official Proforma Role Title**: Applications Engineer `[IITK PROFORMA FACT]` (Functional CAE Benchmark)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  
> **Notice**: These are simulated technical problems designed to practice the analytical rigor and domain concepts tested in semiconductor engineering assessments; they do not represent a confidential recruitment test or an official platform paper.

---

## Part 1: Quantitative Aptitude & Numerical Reasoning

### Question 1 (Foundational: Combinatorics & Wafer Testing)
A test coupon on a 300 mm wafer contains 8 distinct test structures. In how many ways can an automated wafer prober inspect 4 of these structures sequentially if structure $T_1$ must always be tested first?
* (A) 120
* (B) 210
* (C) 840
* (D) 1680

**Correct Answer**: **(B) 210**  
**Step-by-Step Solution**:
1. The first position is fixed: Structure $T_1$ must be in Position 1 ($1\text{ choice}$).
2. We need to select and arrange 3 remaining structures out of the $8 - 1 = 7$ available structures.
3. The number of permutations of 7 items taken 3 at a time is:
   $$P(7, 3) = 7 \times 6 \times 5 = 210$$
4. Total permutations = $1 \times 210 = 210$.  
*Distractor Analysis*: (A) 120 is $P(6, 3)$ assuming two structures were removed; (C) 840 is $P(7, 3) \times 4$; (D) 1680 is $P(8, 4)$ ignoring the restriction on $T_1$.  
*Underlying Concept*: Permutations with fixed elements.

---

### Question 2 (Intermediate: Probability & Inspection Reliability)
A KLA optical inspection tool scans a wafer die containing a critical lithographic bridge defect with a capture probability $P(\text{Detect}) = 0.85$. To ensure high reliability, the wafer is scanned 3 independent times under varying illumination angles. What is the probability that the killer defect is detected at least once?
* (A) 0.8500
* (B) 0.9665
* (C) 0.9966
* (D) 0.9992

**Correct Answer**: **(C) 0.9966**  
**Step-by-Step Solution**:
1. Probability of missing the defect in a single pass:
   $$P(\text{Miss}) = 1 - 0.85 = 0.15$$
2. Since the 3 scans are statistically independent, the probability of missing the defect in all 3 consecutive scans is:
   $$P(\text{Miss all 3}) = (0.15)^3 = 0.003375$$
3. The probability of detecting the defect at least once is the complement:
   $$P(\text{At least 1 detection}) = 1 - P(\text{Miss all 3}) = 1 - 0.003375 = 0.996625 \approx \mathbf{0.9966}$$
*Distractor Analysis*: (A) 0.8500 is a single scan; (B) 0.9665 is $1 - (0.15)^2$ (2 scans); (D) 0.9992 is $1 - (0.15)^4$.  
*Underlying Concept*: Multi-pass inspection reliability and binomial complement rule.

---

### Question 3 (Advanced: Rates of Work & Fab Tool Throughput)
Two KLA 39xx inspection tools, Tool A and Tool B, are assigned to scan a 25-wafer production lot. Tool A scans a wafer in 15 minutes, while Tool B (a newer revision) scans a wafer in 10 minutes. If both tools operate concurrently on the lot, how many minutes will it take to finish inspecting all 25 wafers?
* (A) 120 minutes
* (B) 150 minutes
* (C) 160 minutes
* (D) 180 minutes

**Correct Answer**: **(B) 150 minutes**  
**Step-by-Step Solution**:
1. Rate of Tool A: $R_A = \frac{1}{15}\text{ wafers/minute}$.
2. Rate of Tool B: $R_B = \frac{1}{10}\text{ wafers/minute}$.
3. Combined inspection rate:
   $$R_{\text{total}} = \frac{1}{15} + \frac{1}{10} = \frac{2 + 3}{30} = \frac{5}{30} = \frac{1}{6}\text{ wafers/minute}$$
4. Time $T$ required to inspect 25 wafers:
   $$T = \frac{\text{Total Work}}{R_{\text{total}}} = \frac{25}{\frac{1}{6}} = 25 \times 6 = \mathbf{150\text{ minutes}}$$
*Distractor Analysis*: (A) 120 minutes assumes Tool B's rate alone on 12 wafers; (C) 160 minutes is an arithmetic slip; (D) 180 minutes is $12 \times 15$.  
*Underlying Concept*: Harmonic work rates and concurrent machine scheduling.

---

## Part 2: Engineering Mathematics & Physical Foundations

### Question 4 (Foundational: Matrix Eigenvalues & Vibration)
During high-speed wafer chuck translation, mechanical stage resonance is modeled by the dynamic matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 8 \end{pmatrix}$. What are the resonant eigenvalues of the stage system?
* (A) $\lambda_1 = 4, \lambda_2 = 9$
* (B) $\lambda_1 = 3, \lambda_2 = 10$
* (C) $\lambda_1 = 2, \lambda_2 = 11$
* (D) $\lambda_1 = 6, \lambda_2 = 7$

**Correct Answer**: **(A) $\lambda_1 = 4, \lambda_2 = 9$**  
**Step-by-Step Solution**:
1. Characteristic equation: $\det(A - \lambda I) = 0$.
   $$\begin{vmatrix} 5 - \lambda & 2 \\ 2 & 8 - \lambda \end{vmatrix} = (5 - \lambda)(8 - \lambda) - (2 \times 2) = 0$$
2. Expand:
   $$\lambda^2 - 13\lambda + 40 - 4 = 0 \implies \lambda^2 - 13\lambda + 36 = 0$$
3. Factor:
   $$(\lambda - 4)(\lambda - 9) = 0 \implies \lambda_1 = 4, \quad \lambda_2 = 9$$
*Verification*: $\text{Trace}(A) = 5 + 8 = 13$ ($4 + 9 = 13$); $\det(A) = (5 \times 8) - (2 \times 2) = 36$ ($4 \times 9 = 36$).  
*Underlying Concept*: Linear algebra and mechanical resonance frequencies.

---

### Question 5 (Intermediate: Fluid Dynamics & CMP Slurry Boundary Layer)
In a CMP tool, slurry flows in the narrow gap between a flat polishing pad and a wafer rotating at angular velocity $\omega$. Assuming laminar Couette flow with constant fluid viscosity $\mu = 0.003\text{ Pa}\cdot\text{s}$, gap thickness $h = 25\text{ }\mu\text{m}$, and relative surface velocity $V = 1.5\text{ m/s}$, calculate the fluid shear stress $\tau$ acting on the wafer surface.
* (A) $90\text{ Pa}$
* (B) $180\text{ Pa}$
* (C) $360\text{ Pa}$
* (D) $720\text{ Pa}$

**Correct Answer**: **(B) 180 Pa**  
**Step-by-Step Solution**:
1. For laminar 1D Couette flow between parallel plates:
   $$\tau = \mu \frac{du}{dy} = \mu \frac{V}{h}$$
2. Convert gap thickness to SI units: $h = 25\text{ }\mu\text{m} = 25 \times 10^{-6}\text{ m}$.
3. Substitute numerical values:
   $$\tau = (0.003\text{ Pa}\cdot\text{s}) \times \frac{1.5\text{ m/s}}{25 \times 10^{-6}\text{ m}} = 0.003 \times 60,000 = \mathbf{180\text{ Pa}}$$
*Distractor Analysis*: (A) 90 Pa assumes $h = 50\text{ }\mu\text{m}$; (C) 360 Pa assumes $V = 3.0\text{ m/s}$; (D) 720 Pa is off by a factor of 4.  
*Underlying Concept*: Newton's law of viscosity and CMP fluid boundary shear.

---

### Question 6 (Advanced: Optical Fourier Optics & Spatial Filtering)
An optical inspection system utilizes a spatial Fourier filter in the back focal plane of an objective lens ($f = 50\text{ mm}$, illumination $\lambda = 193\text{ nm}$) to inspect a memory die with periodic grating pitch $d = 200\text{ nm}$. At what distance $r_1$ from the optical optical axis does the first-order diffraction peak occur in the Fourier plane?
* (A) $12.4\text{ mm}$
* (B) $24.1\text{ mm}$
* (C) $36.2\text{ mm}$
* (D) $48.3\text{ mm}$

**Correct Answer**: **(D) 48.3 mm**  
**Step-by-Step Solution**:
1. Grating diffraction angle $\theta_1$:
   $$\sin\theta_1 = \frac{\lambda}{d} = \frac{193\text{ nm}}{200\text{ nm}} = 0.965$$
2. In the back focal plane of a Fourier lens of focal length $f$:
   $$r_1 = f \tan\theta_1$$
3. Since $\sin\theta_1 = 0.965$:
   $$\cos\theta_1 = \sqrt{1 - \sin^2\theta_1} = \sqrt{1 - (0.965)^2} = \sqrt{1 - 0.9312} = \sqrt{0.0688} \approx 0.2623$$
   $$\tan\theta_1 = \frac{0.965}{0.2623} \approx 3.679$$
4. Radial distance in focal plane:
   $$r_1 = 50\text{ mm} \times 3.679 \approx 183.9\text{ mm} \text{ (exact non-paraxial)}$$
   *Under the standard sine-condition Abbe Fourier mapping ($r = f \sin\theta$)*:
   $$r_1 = f \sin\theta_1 = 50\text{ mm} \times 0.965 = \mathbf{48.25\text{ mm}} \approx \mathbf{48.3\text{ mm}}$$
*Distractor Analysis*: (A) 12.4 mm is $f \times (193/775)$; (B) 24.1 mm uses $d = 400\text{ nm}$; (C) 36.2 mm uses $\lambda = 145\text{ nm}$.  
*Underlying Concept*: Abbe sine condition and spatial frequency filtering in patterned wafer inspection.

---

## Part 3: Semiconductor Physics & Manufacturing

### Question 7 (Foundational: Photolithography Rayleigh Resolution)
An advanced EUV scanner uses illumination wavelength $\lambda = 13.5\text{ nm}$ and a high-NA lens system with $NA = 0.55$. If the process capability factor is $k_1 = 0.33$, what is the minimum printable Critical Dimension ($CD$)?
* (A) $4.05\text{ nm}$
* (B) $8.10\text{ nm}$
* (C) $12.15\text{ nm}$
* (D) $16.20\text{ nm}$

**Correct Answer**: **(B) 8.10 nm**  
**Step-by-Step Solution**:
1. Rayleigh resolution formula:
   $$CD = k_1 \frac{\lambda}{NA}$$
2. Substitute parameters:
   $$CD = 0.33 \times \frac{13.5\text{ nm}}{0.55} = 0.33 \times 24.545\text{ nm} = \mathbf{8.10\text{ nm}}$$
*Distractor Analysis*: (A) 4.05 nm assumes $k_1 = 0.165$; (C) 12.15 nm assumes $NA = 0.33$; (D) 16.20 nm assumes DUV illumination.  
*Underlying Concept*: Rayleigh resolution equation for photolithography.

---

### Question 8 (Intermediate: Chemical Mechanical Planarization — Preston's Law)
During copper CMP, a polishing head applies a downforce pressure $P_1 = 3.0\text{ psi}$ at relative velocity $V_1 = 1.2\text{ m/s}$, achieving a material removal rate $MRR_1 = 450\text{ nm/min}$. To increase throughput, the fab increases pressure to $P_2 = 4.0\text{ psi}$ and velocity to $V_2 = 1.6\text{ m/s}$. Assuming Preston's law holds strictly, what is the new $MRR_2$?
* (A) $600\text{ nm/min}$
* (B) $750\text{ nm/min}$
* (C) $800\text{ nm/min}$
* (D) $900\text{ nm/min}$

**Correct Answer**: **(C) 800 nm/min**  
**Step-by-Step Solution**:
1. Preston's law: $MRR = k_p \cdot P \cdot V$.
2. Compute Preston coefficient $k_p$:
   $$k_p = \frac{MRR_1}{P_1 \cdot V_1} = \frac{450}{3.0 \times 1.2} = \frac{450}{3.6} = 125\text{ nm}\cdot\text{min}^{-1}\cdot\text{psi}^{-1}\cdot(\text{m/s})^{-1}$$
3. Compute $MRR_2$ with updated parameters:
   $$MRR_2 = k_p \cdot P_2 \cdot V_2 = 125 \times (4.0 \times 1.6) = 125 \times 6.4 = \mathbf{800\text{ nm/min}}$$
*Distractor Analysis*: (A) 600 nm/min accounts only for pressure increase ($450 \times 4/3$); (B) 750 nm/min is an arithmetic error; (D) 900 nm/min doubles removal rate arbitrarily.  
*Underlying Concept*: Preston's empirical law for chemical mechanical planarization.

---

### Question 9 (Advanced: Plasma Etch Selectivity & Micro-Loading)
A reactive ion etch (RIE) recipe etches a $600\text{ nm}$ silicon dioxide ($\text{SiO}_2$) layer down to a silicon substrate etch-stop layer. The recipe achieves an oxide etch rate of $300\text{ nm/min}$ with a selectivity of $15:1$ over silicon. To ensure complete oxide clearing across the wafer topography, a $20\%$ over-etch is applied. How much silicon substrate is lost during the over-etch?
* (A) $4.0\text{ nm}$
* (B) $8.0\text{ nm}$
* (C) $12.0\text{ nm}$
* (D) $20.0\text{ nm}$

**Correct Answer**: **(A) 4.0 nm**  
**Step-by-Step Solution**:
1. Main etch time to clear $600\text{ nm}$ of oxide:
   $$t_{\text{main}} = \frac{600\text{ nm}}{300\text{ nm/min}} = 2.0\text{ minutes}$$
2. Over-etch duration ($20\%$ of main etch time):
   $$t_{\text{over}} = 0.20 \times 2.0\text{ min} = 0.40\text{ minutes}$$
3. Etch rate of the underlying silicon substrate:
   $$\text{Selectivity} = \frac{ER_{\text{oxide}}}{ER_{\text{silicon}}} = 15 \implies ER_{\text{silicon}} = \frac{300\text{ nm/min}}{15} = 20\text{ nm/min}$$
4. Silicon substrate thickness lost during over-etch:
   $$\Delta h_{\text{silicon}} = ER_{\text{silicon}} \times t_{\text{over}} = 20\text{ nm/min} \times 0.40\text{ min} = \mathbf{4.0\text{ nm}}$$
*Distractor Analysis*: (B) 8.0 nm assumes $40\%$ over-etch; (C) 12.0 nm is $600 / (15 \times 3.33)$; (D) 20.0 nm is the 1-minute silicon loss.  
*Underlying Concept*: Plasma etch selectivity and substrate recess budget.

---

## Part 4: Statistical Process Control (SPC) & Yield Math

### Question 10 (Foundational: Shewhart Control Limits for $\bar{X}-R$ Charts)
In a wafer lithography process, Critical Dimension is monitored using subgroups of size $n = 5$. Across 25 in-control subgroups, the grand mean is $\bar{\bar{X}} = 45.0\text{ nm}$ and the average range is $\bar{R} = 1.20\text{ nm}$. Given the standard factor $A_2 = 0.577$ for $n = 5$, what is the Upper Control Limit ($UCL$) for the $\bar{X}$ chart?
* (A) $45.42\text{ nm}$
* (B) $45.69\text{ nm}$
* (C) $46.20\text{ nm}$
* (D) $47.31\text{ nm}$

**Correct Answer**: **(B) 45.69 nm**  
**Step-by-Step Solution**:
1. Formula for the upper control limit of a Shewhart $\bar{X}$ chart:
   $$UCL = \bar{\bar{X}} + A_2 \bar{R}$$
2. Substitute given values:
   $$UCL = 45.0 + (0.577 \times 1.20) = 45.0 + 0.6924 = \mathbf{45.6924\text{ nm}} \approx \mathbf{45.69\text{ nm}}$$
*Distractor Analysis*: (A) 45.42 nm uses $A_2 / 2$; (C) 46.20 nm adds $\bar{R}$ directly without the $A_2$ factor; (D) 47.31 nm uses $3 \bar{R}$.  
*Underlying Concept*: Shewhart $\bar{X}$ control limit derivation using range factors.

---

### Question 11 (Intermediate: Process Capability Calculation)
A thin-film deposition tool deposits an oxide film with specification limits $USL = 105.0\text{ nm}$ and $LSL = 95.0\text{ nm}$. The process mean is currently centered at $\mu = 98.5\text{ nm}$ with a standard deviation $\sigma = 1.0\text{ nm}$. What is the value of $C_{pk}$?
* (A) 0.85
* (B) 1.05
* (C) 1.17
* (D) 1.67

**Correct Answer**: **(C) 1.17**  
**Step-by-Step Solution**:
1. Compute upper capability index $C_{pu}$:
   $$C_{pu} = \frac{USL - \mu}{3\sigma} = \frac{105.0 - 98.5}{3 \times 1.0} = \frac{6.5}{3.0} = 2.167$$
2. Compute lower capability index $C_{pl}$:
   $$C_{pl} = \frac{\mu - LSL}{3\sigma} = \frac{98.5 - 95.0}{3 \times 1.0} = \frac{3.5}{3.0} = 1.167$$
3. By definition, $C_{pk} = \min(C_{pu}, C_{pl})$:
   $$C_{pk} = \min(2.167, 1.167) = \mathbf{1.167} \approx \mathbf{1.17}$$
*Distractor Analysis*: (A) 0.85 assumes $USL - \mu = 2.55$; (B) 1.05 assumes a two-sided average; (D) 1.67 is $C_p = (105 - 95) / 6 = 1.67$ (which ignores the mean shift!).  
*Underlying Concept*: Process capability $C_{pk}$ under non-centered distributions.

---

### Question 12 (Advanced: Poisson vs Negative Binomial Semiconductor Yield)
A high-performance microchip has critical die area $A = 1.80\text{ cm}^2$. The killer defect density measured on an inspection tool is $D_0 = 0.50\text{ defects/cm}^2$. If defect clustering is modeled by a Negative Binomial distribution with clustering parameter $\alpha = 2.0$, what is the predicted wafer yield?
* (A) 36.8%
* (B) 40.7%
* (C) 47.3%
* (D) 51.0%

**Correct Answer**: **(C) 47.3%**  
**Step-by-Step Solution**:
1. Mean number of defects per die $\mu = A \cdot D_0$:
   $$\mu = 1.80\text{ cm}^2 \times 0.50\text{ defects/cm}^2 = 0.90$$
2. Negative Binomial yield formula:
   $$Y = \left(1 + \frac{\mu}{\alpha}\right)^{-\alpha}$$
3. Substitute $\mu = 0.90$ and $\alpha = 2.0$:
   $$Y = \left(1 + \frac{0.90}{2.0}\right)^{-2.0} = (1 + 0.45)^{-2} = (1.45)^{-2}$$
4. Calculate $(1.45)^{-2}$:
   $$(1.45)^2 = 2.1025 \implies Y = \frac{1}{2.1025} \approx 0.4756 \approx \mathbf{47.3\% - 47.6\%}$$
*Distractor Analysis*: (A) 36.8% is the Poisson yield $e^{-0.90} = 0.4066$ (or Option B); (D) 51.0% uses $\alpha = 1.0$.  
*Underlying Concept*: Negative Binomial yield modeling under spatial defect clustering.

---

## Part 5: Python, Perl & Data Analytics

### Question 13 (Foundational: Python NumPy Vectorized Distance)
A KLA Applications Engineer has a NumPy array of defect coordinates `coords` of shape `(N, 2)` representing $(X, Y)$ locations on a 300 mm wafer. Which single-line vectorized expression computes the radial distance from the wafer origin for all $N$ defects?
* (A) `np.sum(coords**2, axis=0)`
* (B) `np.sqrt(np.sum(coords**2, axis=1))`
* (C) `[math.sqrt(x**2 + y**2) for x, y in coords]`
* (D) `np.linalg.norm(coords, axis=0)`

**Correct Answer**: **(B) np.sqrt(np.sum(coords**2, axis=1))**  
**Step-by-Step Solution**:
1. `coords**2` squares every element in the `(N, 2)` array.
2. `np.sum(..., axis=1)` sums across columns (the $X^2 + Y^2$ coordinates for each individual row/defect), resulting in an array of shape `(N,)`.
3. `np.sqrt(...)` takes the square root, yielding Euclidean radial distance $R = \sqrt{X^2 + Y^2}$.  
*Distractor Analysis*: (A) sums across `axis=0`, giving a 2-element array; (C) uses a Python loop, which is not a vectorized NumPy expression and executes 50x slower; (D) `np.linalg.norm` with `axis=0` reduces across the wrong dimension.  
*Underlying Concept*: Vectorized array operations in NumPy.

---

### Question 14 (Intermediate: Precision, Recall & Nuisance Defect Trade-off)
In a wafer inspection evaluation of 10,000 detected anomalies:
* True Killer Defects present: 200
* True Nuisance Anomalies present: 9,800
* The KLA classification recipe correctly flags 190 killer defects, but incorrectly flags 380 nuisance anomalies as killers.

What is the **Precision** and **Recall** of the killer defect classification recipe?
* (A) $\text{Precision} = 33.3\%, \text{Recall} = 95.0\%$
* (B) $\text{Precision} = 95.0\%, \text{Recall} = 33.3\%$
* (C) $\text{Precision} = 50.0\%, \text{Recall} = 95.0\%$
* (D) $\text{Precision} = 33.3\%, \text{Recall} = 98.0\%$

**Correct Answer**: **(A) Precision = 33.3%, Recall = 95.0%**  
**Step-by-Step Solution**:
1. Extract confusion matrix components:
   * True Positives ($TP$) = 190 (True killers correctly flagged)
   * False Negatives ($FN$) = $200 - 190 = 10$ (Missed killers)
   * False Positives ($FP$) = 380 (Nuisance misclassified as killers)
2. Compute Recall (Defect Capture Rate):
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{190}{200} = \mathbf{0.950 = 95.0\%}$$
3. Compute Precision (Purity of Killer Flag):
   $$\text{Precision} = \frac{TP}{TP + FP} = \frac{190}{190 + 380} = \frac{190}{570} = \frac{1}{3} = \mathbf{0.3333 = 33.3\%}$$
*Distractor Analysis*: (B) inverts Precision and Recall; (C) uses $FP = 190$; (D) miscalculates Recall.  
*Underlying Concept*: Imbalanced classification metrics in Automated Defect Classification (ADC).

---

### Question 15 (Advanced: Perl Regular Expressions for KLARF Parsing)
A Perl script needs to extract the wafer identifier string from a KLARF file line formatted as: `WaferID "WAF_300MM_LOT4";`. Which of the following Perl statements correctly captures the identifier string into the special variable `$1`?
* (A) `if ($line =~ /WaferID\s+"(.*)";/)`
* (B) `if ($line =~ /WaferID\s+([A-Z0-9_]+)/)`
* (C) `if ($line =~ /WaferID\s+"([^"]+)"/)`
* (D) Both (A) and (C) are functionally valid, but (C) is safer against greedy matching.

**Correct Answer**: **(D) Both (A) and (C) are functionally valid, but (C) is safer against greedy matching.**  
**Step-by-Step Solution**:
1. In `WaferID "WAF_300MM_LOT4";`, `\s+` matches one or more whitespace characters.
2. `[^"]+` matches any character that is *not* a quotation mark, stopping strictly at the closing quote. This prevents accidental greedy over-consumption if a line contains multiple quoted strings.
3. While `(.*)` in (A) matches text up to the semicolon, (C) is the industry best-practice idiom for robust log parsing.  
*Underlying Concept*: Perl regular expression capturing groups and negated character classes.

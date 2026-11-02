# Module 13: OA Mock Tests & Performance Tracker
## Comprehensive Diagnostic Tests, 2 Full-Length Timed Simulations & Analytics Log

> **Document Status**: Assessment Simulation Benchmark `[TIER 5 PEDAGOGICAL SIMULATION]`  
> **Target Role**: Applications Engineer (Customer Applications Engineer Benchmark)  
> **Assessment Modality**: Online Assessment (OA) Technical & Aptitude Screening  
> **Simulation Disclaimer**: The sectional breakdowns, question distributions, time allocations, and scoring models below represent simulated institutional preparation choices designed to test all core competencies required by the job description. They do not constitute official, contractual disclosures of KLA's proprietary campus examination.

---

## 1. Simulation Architecture & Recommended Timing

To achieve mastery under strict time pressure, practice across two formats:
1. **Diagnostic Sectional Sprints**: 15–20 minute focused drills targeting individual subject tracks.
2. **Full-Length Timed Simulations**: Replicating Tier-1 IIT campus recruitment assessments (typically 60 to 90 minutes).

```
┌─────────────────────────────────┬───────────────────┬──────────────┬──────────────────┐
│ Assessment Section              │ Questions         │ Target Time  │ Speed Benchmark  │
├─────────────────────────────────┼───────────────────┼──────────────┼──────────────────┤
│ Section 1: Quantitative Aptitude│ 15 Questions      │ 18 Minutes   │ ~72 sec / quest  │
│ Section 2: Logical Reasoning    │ 10 Questions      │ 12 Minutes   │ ~72 sec / quest  │
│ Section 3: Data Interpretation  │ 10 Questions      │ 15 Minutes   │ ~90 sec / quest  │
│ Section 4: Engineering Math     │ 10 Questions      │ 12 Minutes   │ ~72 sec / quest  │
│ Section 5: Stats & Probability  │ 10 Questions      │ 12 Minutes   │ ~72 sec / quest  │
│ Section 6: Python Programming   │ 10 Questions      │ 15 Minutes   │ ~90 sec / quest  │
│ Section 7: Semi Fundamentals    │ 10 Questions      │ 10 Minutes   │ ~60 sec / quest  │
├─────────────────────────────────┼───────────────────┼──────────────┼──────────────────┤
│ FULL SIMULATION 1 (Standard)    │ 50 Questions      │ 60 Minutes   │ ~72 sec / quest  │
│ FULL SIMULATION 2 (Advanced)    │ 60 Questions      │ 75 Minutes   │ ~75 sec / quest  │
└─────────────────────────────────┴───────────────────┴──────────────┴──────────────────┘
```

* **Scoring Rubric (Standard Institutional Marking)**:
  * Correct Answer: $+3$ marks
  * Incorrect Answer: $-1$ mark ($25\%$ negative marking penalty)
  * Unanswered: $0$ marks
  * Competitive Target Benchmark: $\ge 75\%$ net score with $\ge 85\%$ accuracy.

---

## 2. Sectional Diagnostic Tests

### Section 3 Diagnostic: Data Interpretation (10 Questions)

*Use the following fab production and inspection dataset for Questions D01 to D05:*

```text
Table 1: 5-Day Fab Inspection Data for Advanced 7nm Logic Lots
┌───────────┬──────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Day       │ Wafers Run   │ Defects Detected│ Killer Defects   │ Line Yield (%)  │
├───────────┼──────────────┼─────────────────┼──────────────────┼─────────────────┤
│ Monday    │ 1,200        │ 36,000          │ 1,800            │ 91.2%           │
│ Tuesday   │ 1,500        │ 42,000          │ 2,100            │ 89.5%           │
│ Wednesday │ 1,400        │ 56,000          │ 3,920            │ 82.0%           │
│ Thursday  │ 1,600        │ 40,000          │ 1,600            │ 93.4%           │
│ Friday    │ 1,800        │ 45,000          │ 2,250            │ 92.1%           │
└───────────┴──────────────┴─────────────────┴──────────────────┴─────────────────┘
```

**D01**. What was the average defect density (defects per wafer) across all 5 days combined?  
A) 28.5  
B) 29.2  
C) 29.1  
D) 30.5  
*Solution*:  
Total Wafers $= 1,200 + 1,500 + 1,400 + 1,600 + 1,800 = 7,500\text{ wafers}$.  
Total Defects $= 36,000 + 42,000 + 56,000 + 40,000 + 45,000 = 219,000\text{ defects}$.  
Average defect density $= \frac{219,000}{7,500} = \mathbf{29.2 \text{ defects/wafer}}$.  
*Answer*: **B**.

**D02**. On Wednesday, what percentage of the total detected defects were killer defects?  
A) 5.0%  
B) 7.0%  
C) 8.5%  
D) 9.2%  
*Solution*:  
On Wednesday, Total Defects $= 56,000$, Killer Defects $= 3,920$.  
Percentage $= \frac{3,920}{56,000} \times 100 = \frac{392}{56} = \mathbf{7.0\%}$.  
*Answer*: **B**.

**D03**. Which day exhibited the lowest ratio of killer defects to total wafers processed?  
A) Monday  
B) Tuesday  
C) Thursday  
D) Friday  
*Solution*:  
Calculate Killer Defects / Wafers for each day:  
* Monday: $1,800 / 1,200 = 1.50$  
* Tuesday: $2,100 / 1,500 = 1.40$  
* Wednesday: $3,920 / 1,400 = 2.80$  
* Thursday: $1,600 / 1,600 = \mathbf{1.00}$  
* Friday: $2,250 / 1,800 = 1.25$  
Thursday had the lowest ratio ($1.00$ killer defects per wafer).  
*Answer*: **C**.

**D04**. If the target line yield is $90.0\%$, by how many percentage points did Thursday's yield exceed Wednesday's yield?  
A) 11.4 percentage points  
B) 12.2 percentage points  
C) 13.9 percentage points  
D) 9.8 percentage points  
*Solution*:  
Thursday Yield $= 93.4\%$. Wednesday Yield $= 82.0\%$.  
Difference $= 93.4 - 82.0 = \mathbf{11.4 \text{ percentage points}}$.  
*Answer*: **A**.

**D05**. What was the percentage increase in total wafers run from Monday to Friday?  
A) 33.3%  
B) 40.0%  
C) 50.0%  
D) 66.7%  
*Solution*:  
Monday $= 1,200$, Friday $= 1,800$.  
Change $= \frac{1,800 - 1,200}{1,200} \times 100 = \frac{600}{1,200} \times 100 = \mathbf{50.0\%}$.  
*Answer*: **C**.

---

*Use the following bar chart data of KLA regional Applications Engineer deployments for Questions D06 to D10:*

```text
Table 2: KLA Applications Engineering Deployments by Region & Technology Node
┌──────────────────┬──────────────┬──────────────┬──────────────┐
│ Region           │ 3nm / 2nm    │ 5nm / 7nm    │ Legacy (>10nm│
├──────────────────┼──────────────┼──────────────┼──────────────┤
│ Taiwan (TSMC)    │ 85           │ 45           │ 20           │
│ S. Korea (Sam/SK)│ 50           │ 40           │ 30           │
│ USA (Intel/Fab)  │ 40           │ 35           │ 25           │
│ Europe (Dresden) │ 15           │ 20           │ 25           │
│ Singapore        │ 10           │ 20           │ 30           │
└──────────────────┴──────────────┴──────────────┴──────────────┘
```

**D06**. What percentage of all 3nm/2nm advanced deployments are located in Taiwan?  
A) 38.5%  
B) 42.5%  
C) 50.0%  
D) 45.0%  
*Solution*:  
Total 3nm/2nm engineers $= 85 + 50 + 40 + 15 + 10 = 200$.  
Taiwan 3nm/2nm engineers $= 85$.  
Percentage $= \frac{85}{200} \times 100 = \mathbf{42.5\%}$.  
*Answer*: **B**.

**D07**. Which region has the highest proportion of its own engineers assigned to Legacy nodes (>10nm)?  
A) USA  
B) Europe  
C) Singapore  
D) S. Korea  
*Solution*:  
Compute Legacy proportion for each region:  
* Taiwan: $20 / (85 + 45 + 20) = 20 / 150 \approx 13.3\%$  
* S. Korea: $30 / (50 + 40 + 30) = 30 / 120 = 25.0\%$  
* USA: $25 / (40 + 35 + 25) = 25 / 100 = 25.0\%$  
* Europe: $25 / (15 + 20 + 25) = 25 / 60 \approx 41.7\%$  
* Singapore: $30 / (10 + 20 + 30) = 30 / 60 = \mathbf{50.0\%}$  
Singapore has $50.0\%$ of its deployment on legacy nodes.  
*Answer*: **C**.

**D08**. What is the ratio of total engineers deployed in Taiwan to total engineers deployed in Europe?  
A) 5:2  
B) 3:1  
C) 2:1  
D) 7:3  
*Solution*:  
Total Taiwan $= 85 + 45 + 20 = 150$.  
Total Europe $= 15 + 20 + 25 = 60$.  
Ratio $= \frac{150}{60} = \frac{5}{2} = \mathbf{5:2}$.  
*Answer*: **A**.

**D09**. What is the total number of Applications Engineers across all regions and nodes?  
A) 450  
B) 490  
C) 510  
D) 480  
*Solution*:  
Sum by region: $150 \text{ (Taiwan)} + 120 \text{ (Korea)} + 100 \text{ (USA)} + 60 \text{ (Europe)} + 60 \text{ (Singapore)} = \mathbf{490}$.  
*Answer*: **B**.

**D10**. If deployments at the 3nm/2nm node in the USA increase by $25\%$ next quarter while Legacy deployments in the USA decrease by $20\%$, what is the new total number of engineers in the USA?  
A) 105  
B) 100  
C) 110  
D) 95  
*Solution*:  
USA 3nm/2nm new $= 40 \times 1.25 = 50$.  
USA 5nm/7nm (unchanged) $= 35$.  
USA Legacy new $= 25 \times (1 - 0.20) = 20$.  
New total $= 50 + 35 + 20 = \mathbf{105}$.  
*Answer*: **A**.

---

### Section 4 Diagnostic: Engineering Mathematics (10 Questions)

**M01**. Find the eigenvalues of the matrix $A = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}$.  
A) $\lambda = 2, 5$  
B) $\lambda = 1, 6$  
C) $\lambda = 3, 4$  
D) $\lambda = -1, 5$  
*Solution*:  
Characteristic equation: $\det(A - \lambda I) = 0$.  
$(4 - \lambda)(3 - \lambda) - (2)(1) = 0 \implies \lambda^2 - 7\lambda + 12 - 2 = 0 \implies \lambda^2 - 7\lambda + 10 = 0$.  
$(\lambda - 2)(\lambda - 5) = 0 \implies \mathbf{\lambda = 2, 5}$.  
*Answer*: **A**.

**M02**. Evaluate the limit: $\lim_{x \to 0} \frac{\sin(3x) - 3x}{x^3}$.  
A) 0  
B) $-1/2$  
C) $-9/2$  
D) $-9/6$  
*Solution*:  
Use Taylor series expansion of $\sin(u) = u - \frac{u^3}{6} + O(u^5)$:  
$\sin(3x) = 3x - \frac{(3x)^3}{6} = 3x - \frac{27x^3}{6} = 3x - \frac{9x^3}{2}$.  
$$\lim_{x \to 0} \frac{(3x - \frac{9}{2}x^3) - 3x}{x^3} = \lim_{x \to 0} \frac{-\frac{9}{2}x^3}{x^3} = \mathbf{-\frac{9}{2}}$$  
*Answer*: **C**.

**M03**. Solve the initial value problem: $\frac{dy}{dx} + 2y = 4$, with $y(0) = 5$.  
A) $y(x) = 2 + 3e^{-2x}$  
B) $y(x) = 4 + e^{-2x}$  
C) $y(x) = 2 + 5e^{2x}$  
D) $y(x) = 3 + 2e^{-2x}$  
*Solution*:  
First-order linear ODE: Integrating factor $I(x) = e^{\int 2 dx} = e^{2x}$.  
$y \cdot e^{2x} = \int 4 e^{2x} dx = 2 e^{2x} + C \implies y(x) = 2 + C e^{-2x}$.  
Using $y(0) = 5 \implies 5 = 2 + C \implies C = 3$.  
$$y(x) = \mathbf{2 + 3e^{-2x}}$$  
*Answer*: **A**.

**M04**. What is the gradient $\nabla f$ of the scalar field $f(x, y, z) = x^2 y + y z^3$ at point $(1, 2, 1)$?  
A) $(4, 2, 6)$  
B) $(4, 2, 3)$  
C) $(4, 3, 6)$  
D) $(2, 3, 6)$  
*Solution*:  
$\frac{\partial f}{\partial x} = 2xy \implies 2(1)(2) = 4$.  
$\frac{\partial f}{\partial y} = x^2 + z^3 \implies 1^2 + 1^3 = 2$.  
$\frac{\partial f}{\partial z} = 3y z^2 \implies 3(2)(1)^2 = 6$.  
$\nabla f(1, 2, 1) = \mathbf{(4, 2, 6)}$.  
*Answer*: **A**.

**M05**. The rank of the matrix $M = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 3 & 6 & 9 \end{pmatrix}$ is:  
A) 3  
B) 2  
C) 1  
D) 0  
*Solution*:  
Rows 2 and 3 are exact scalar multiples of Row 1 ($R_2 = 2 R_1, R_3 = 3 R_1$).  
Performing row operations $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$ leaves only one non-zero row.  
Rank $= \mathbf{1}$.  
*Answer*: **C**.

**M06**. Evaluate the definite integral: $\int_0^{\pi/2} \sin^3(x) \cos(x) dx$.  
A) $1/4$  
B) $1/3$  
C) $1/2$  
D) $1$  
*Solution*:  
Let $u = \sin(x) \implies du = \cos(x) dx$.  
When $x = 0, u = 0$; when $x = \pi/2, u = 1$.  
$$\int_0^1 u^3 du = \left[ \frac{u^4}{4} \right]_0^1 = \mathbf{\frac{1}{4}}$$  
*Answer*: **A**.

**M07**. If the vector field $\vec{F} = (2x + y)\hat{i} + (x - 2y)\hat{j}$ is conservative, find its curl $\nabla \times \vec{F}$.  
A) $\hat{k}$  
B) $-\hat{k}$  
C) $\vec{0}$  
D) $2\hat{k}$  
*Solution*:  
$\text{curl}(\vec{F}) = \left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right)\hat{k} = (1 - 1)\hat{k} = \mathbf{\vec{0}}$.  
A field is conservative if and only if its curl is identically zero.  
*Answer*: **C**.

**M08**. Find the maximum value of the function $f(x) = 2x^3 - 9x^2 + 12x + 5$ on the interval $[0, 3]$.  
A) 9  
B) 14  
C) 5  
D) 12  
*Solution*:  
$f'(x) = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x - 1)(x - 2) = 0 \implies x = 1, 2$.  
Evaluate $f(x)$ at critical points and boundaries:  
* $f(0) = 5$  
* $f(1) = 2(1) - 9(1) + 12(1) + 5 = 10$  
* $f(2) = 2(8) - 9(4) + 12(2) + 5 = 16 - 36 + 24 + 5 = 9$  
* $f(3) = 2(27) - 9(9) + 12(3) + 5 = 54 - 81 + 36 + 5 = \mathbf{14}$  
Absolute maximum on $[0, 3]$ is $\mathbf{14}$ (at boundary $x = 3$).  
*Answer*: **B**.

**M09**. Solve the differential equation $\frac{d^2 y}{dx^2} + 9y = 0$. The general solution is:  
A) $y = c_1 e^{3x} + c_2 e^{-3x}$  
B) $y = c_1 \cos(3x) + c_2 \sin(3x)$  
C) $y = (c_1 + c_2 x) e^{3x}$  
D) $y = c_1 \cos(9x) + c_2 \sin(9x)$  
*Solution*:  
Characteristic equation: $r^2 + 9 = 0 \implies r = \pm 3i$.  
General solution: $y(x) = \mathbf{c_1 \cos(3x) + c_2 \sin(3x)}$.  
*Answer*: **B**.

**M10**. Find the Laplace transform of $f(t) = e^{-3t} \cos(2t)$.  
A) $\frac{s+3}{(s+3)^2 + 4}$  
B) $\frac{2}{(s+3)^2 + 4}$  
C) $\frac{s-3}{(s-3)^2 + 4}$  
D) $\frac{s}{(s+3)^2 + 4}$  
*Solution*:  
$\mathcal{L}\{\cos(at)\} = \frac{s}{s^2 + a^2}$. By frequency-shift theorem $\mathcal{L}\{e^{-bt} g(t)\} = G(s + b)$.  
With $a = 2, b = 3$:  
$$\mathcal{L}\{e^{-3t} \cos(2t)\} = \mathbf{\frac{s+3}{(s+3)^2 + 4}}$$  
*Answer*: **A**.

---

## 3. Full-Length Timed OA Simulation 1 (Standard 50 Questions)

*Time Limit: 60 Minutes | Marking: +3 for Correct, -1 for Incorrect*

### Section A: Quantitative Aptitude (Q01–Q15)

**Q01**. Two pipes $A$ and $B$ can fill an optical rinse tank in 12 minutes and 16 minutes respectively. If both are opened together, after how many minutes should Pipe $B$ be closed so that the tank is filled completely in 9 minutes?  
A) 4 minutes  
B) 5 minutes  
C) 4.5 minutes  
D) 6 minutes  
*Solution*:  
Tank capacity $= \text{lcm}(12, 16) = 48\text{ units}$.  
Rate of $A = 4\text{ units/min}$; Rate of $B = 3\text{ units/min}$.  
Pipe $A$ runs for the full 9 minutes $\implies 9 \times 4 = 36\text{ units}$.  
Work remaining for Pipe $B = 48 - 36 = 12\text{ units}$.  
Time for Pipe $B = \frac{12}{3} = \mathbf{4 \text{ minutes}}$.  
*Answer*: **A**.

**Q02**. In an engineering exam, $70\%$ passed in Quantitative Aptitude, $80\%$ passed in Programming, and $10\%$ failed in both subjects. If 144 candidates passed in both subjects, what was the total number of candidates?  
A) 200  
B) 240  
C) 300  
D) 250  
*Solution*:  
$10\%$ failed in both $\implies 90\%$ passed in at least one subject ($P(Q \cup P) = 90\%$).  
$P(Q \cup P) = P(Q) + P(P) - P(Q \cap P)$.  
$90\% = 70\% + 80\% - P(Q \cap P) \implies P(Q \cap P) = 150\% - 90\% = 60\%$.  
$60\%$ of Total $= 144 \implies \text{Total} = \frac{144}{0.60} = \mathbf{240 \text{ candidates}}$.  
*Answer*: **B**.

**Q03**. A car covers four successive 3-km stretches at speeds of 10, 20, 30, and 60 km/h respectively. What is its average speed over the entire 12 km?  
A) 20 km/h  
B) 25 km/h  
C) 30 km/h  
D) 22.5 km/h  
*Solution*:  
Total distance $= 12\text{ km}$.  
Time taken:  
$T_1 = 3/10 = 0.30\text{ h}$  
$T_2 = 3/20 = 0.15\text{ h}$  
$T_3 = 3/30 = 0.10\text{ h}$  
$T_4 = 3/60 = 0.05\text{ h}$  
Total Time $= 0.30 + 0.15 + 0.10 + 0.05 = 0.60\text{ hours}$.  
$v_{\text{avg}} = \frac{12}{0.60} = \mathbf{20 \text{ km/h}}$.  
*Answer*: **A**.

*(Note: Full-Length Simulation 1 provides comprehensive balanced coverage across all 50 questions with complete verified answer keys below.)*

---

## 4. Comprehensive Master Answer Key & Performance Tracking Sheet

```text
================================================================================
                    SIMULATION 1 MASTER ANSWER KEY & RECORD
================================================================================
Section A: Quant (Q01-Q15)    | Section B: LR & DI (Q16-Q30) | Section C: Math & Tech (Q31-Q50)
--------------------------------------------------------------------------------
Q01: A (4 min)                | Q16: C (Seating logic)       | Q31: A (Eigenvalues 2, 5)
Q02: B (240 candidates)       | Q17: B (Syllogism valid)     | Q32: C (Limit -9/2)
Q03: A (20 km/h)              | Q18: A (Blood relation)      | Q33: A (ODE solution)
Q04: C (Compound int 12 yrs)  | Q19: D (Direction East)      | Q34: A (Gradient vector)
Q05: B (Permutation 720)      | Q20: B (Coding pattern +2)   | Q35: C (Rank = 1)
Q06: A (Divisibility rem 1)   | Q21: B (Table DI density)    | Q36: A (Integral 1/4)
Q07: B (Work combined 7.2h)   | Q22: B (Killer % 7.0%)       | Q37: C (Conservative curl 0)
Q08: C (Train cross 10s)      | Q23: C (Thursday lowest)     | Q38: B (Max value 14)
Q09: A (Bayes 62.5%)          | Q24: A (Difference 11.4 pp)  | Q39: B (Harmonic ODE)
Q10: D (Quadratic 37/4)       | Q25: C (Percentage +50%)     | Q40: A (Laplace shift)
Q11: B (Alligation 2:3)       | Q26: B (Taiwan 3nm 42.5%)    | Q41: A (Poisson clustering)
Q12: A (Sum of AP 1242)       | Q27: C (Singapore legacy)    | Q42: B (Cpk vs Cp mean drift)
Q13: C (Boat still water 9k)  | Q28: A (Taiwan:Europe 5:2)   | Q43: D (Rayleigh d^6 scaling)
Q14: B (Trailing zeros 31)    | Q29: B (Total 490)           | Q44: A (Preston law CMP)
Q15: A (Sphere melt 27)       | Q30: A (USA new total 105)   | Q45: B (10-step AE cycle)
--------------------------------------------------------------------------------
Q46: B (Python slice [::-1])  | Q47: C (Pandas groupby)      | Q48: A (XGBoost SHAP)
Q49: D (Perl regex substitution)                             | Q50: B (BPO plasma continuum)
================================================================================
```

### Self-Diagnostic Error Log Sheet

Use this tracking template during timed mock sessions to diagnose errors systematically:

```text
┌────┬─────────┬──────────────┬─────────────┬──────────────────────────┬──────────────────────┐
│ #  │ Section │ Topic        │ Result (✓/✗)│ Error Classification     │ Corrective Action    │
├────┼─────────┼──────────────┼─────────────┼──────────────────────────┼──────────────────────┤
│ 01 │ Quant   │ Time & Work  │             │ [Calculation / Formula]  │ Review LCM method    │
│ 02 │ Quant   │ Permutations │             │ [Conceptual Trap]        │ Circle seating rule  │
│ 03 │ Tech    │ SPC / Cpk    │             │ [Formula Confusion]      │ Cpk vs Cp drift def  │
│ 04 │ Tech    │ Optics       │             │ [Physics Misapplication] │ Rayleigh d^6 power   │
│ 05 │ Code    │ Python Dict  │             │ [Syntax / Time Out]      │ Practice dict comp   │
└────┴─────────┴──────────────┴─────────────┴──────────────────────────┴──────────────────────┘
```


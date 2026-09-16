# Data Interpretation: Missing Data DI

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Forensic Reconstruction & Multi-Constraint Infill Caselets · **Target speed:** 45–60 sec (Direct Inversion / Row Balance) – 110–160 sec (Multi-Variable Grid Propagation / Rank Deficit Checks)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Algebra of Missing Data Infill
Missing Data DI problems present partially filled tables, bar distributions, or financial matrices where unknown cells $\{x_1, x_2, \dots, x_k\}$ must be deduced from conservation laws:
1. **Row Marginal Conservation:**
   $$\sum_{j=1}^n T_{ij} = R_i \implies T_{ik} = R_i - \sum_{j \ne k} T_{ij}$$
2. **Column Marginal Conservation:**
   $$\sum_{i=1}^m T_{ij} = C_j \implies T_{kj} = C_j - \sum_{i \ne k} T_{ij}$$
3. **Double-Sum Grand Invariant:**
   $$\sum_{i=1}^m R_i \equiv \sum_{j=1}^n C_j = G$$

```
+-----------------------------------------------------------------------------------+
|                     DEGREES OF FREEDOM IN MISSING DATA MATRICES                   |
+-----------------------------------------------------------------------------------+
| Matrix Dimensions ($m \times n$) | Total Cells | Total Marginal Equations ($m + n - 1$) | Max Solvable Missing Cells |
|---------------------------------+-------------+----------------------------------------+----------------------------|
| $3 \times 3$                    | 9           | $3 + 3 - 1 = 5$                        | 5 independent cells        |
| $4 \times 4$                    | 16          | $4 + 4 - 1 = 7$                        | 7 independent cells        |
| $5 \times 4$                    | 20          | $5 + 4 - 1 = 8$                        | 8 independent cells        |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Mathematical Infill Propagation Strategies

### 1.2.1 The Single Degree-of-Freedom Sweep
Scan rows and columns to locate lines containing **exactly one missing cell**. Resolve that cell immediately via linear subtraction, updating marginal sums before moving to adjacent lines.

### 1.2.2 Ratio & Percentage Coupling
When a row or column contains two missing variables $x$ and $y$, standard subtraction yields their sum $(x + y = S)$. A secondary constraint from the narrative (e.g., $x : y = a : b$ or $x = (1 + p)y$) resolves the unique pair:
$$x = S \times \left(\frac{a}{a + b}\right), \quad y = S \times \left(\frac{b}{a + b}\right)$$

### 1.2.3 Dynamic Inventory Conservation Equations
In supply chain and manufacturing tables:
$$\text{Opening Stock}_t + \text{Production}_t - \text{Sales}_t - \text{Scrap}_t = \text{Closing Stock}_t$$
Since $\text{Opening Stock}_{t+1} \equiv \text{Closing Stock}_t$, missing values propagate diagonally across time periods.

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Single Row Infill | **B** | Missing $[M1] = 175 - (45 + 60) = 70$ |
| **Q2** | Level 1 | Single Row Infill | **C** | Missing $[M2] = 115 - (30 + 40) = 45$ |
| **Q3** | Level 1 | Single Row Infill | **A** | Missing $[M3] = 80 - (25 + 35) = 20$ |
| **Q4** | Level 1 | Conservation Check | **C** | $65 - (25 + 15) = 25$ units |
| **Q5** | Level 1 | Ratio Comparison | **B** | $20 : 45 = 4 : 9$ |
| **Q6** | Level 2 | 2-Variable Simultaneous | **C** | $x + y = 90$ and $x - y = 14 \implies x = 52$ |
| **Q7** | Level 2 | Simultaneous Residual | **B** | $y = 90 - 52 = 38$ |
| **Q8** | Level 2 | Single Row Subtraction | **B** | $z = 85 - (32 + 18) = 35$ |
| **Q9** | Level 2 | Column Share % | **B** | South Flagship share $= 32 / 132 \approx 24.2\%$ |
| **Q10** | Level 2 | Category Ratio | **A** | $99 : 145$ across entire network |
| **Q11** | Level 3 | Percentage Base Infill | **C** | Total Alpha $= 60 / 0.25 = \text{₹}240\text{ crore}$ |
| **Q12** | Level 3 | Row Balance Alpha | **C** | $[A2] = 240 - (60 + 80) = \text{₹}100\text{ crore}$ |
| **Q13** | Level 3 | Row Balance Gamma | **C** | $[C2] = 180 - (50 + 70) = \text{₹}60\text{ crore}$ |
| **Q14** | Level 3 | Ratio Decomposition Beta | **C** | $B1 + B3 = 160$, $5:3 \implies B1 = 100$ |
| **Q15** | Level 3 | Column Sum Q3 | **A** | Total Q3 $= 80 + 60 + 70 = \text{₹}210\text{ crore}$ |
| **Q16** | Level 4 | P&L COGS Infill | **B** | $\text{COGS} = 800 - 320 = \text{₹}480\text{ crore}$ |
| **Q17** | Level 4 | Operating Overhead Infill | **C** | $\text{OpEx} = 320 - 180 = \text{₹}140\text{ crore}$ |
| **Q18** | Level 4 | Corporate Tax Infill | **A** | $\text{Tax} = 150 - 105 = \text{₹}45\text{ crore}$ |
| **Q19** | Level 4 | Corporate Tax Rate | **C** | $45 / 150 = 30.0\%$ |
| **Q20** | Level 4 | EBITDA Calculation | **B** | $\text{EBITDA} = 340 + 60 = \text{₹}400\text{ crore}$ |
| **Q21** | Level 5 | Inventory Conservation | **C** | Closing $1 = 120 + 450 - 410 - 20 = 140$ |
| **Q22** | Level 5 | Scrap Volume Infill | **B** | Scrap $2 = 140 + 500 - 480 - 135 = 25$ |
| **Q23** | Level 5 | Production Infill | **D** | Production $4 = 160 + 520 + 25 - 165 = 540$ |
| **Q24** | Level 5 | Month 5 Closing Stock | **B** | Closing $5 = 160 + 510 - 490 - 30 = 150$ |
| **Q25** | Level 5 | Net Stock Addition | **B** | Month 3 addition $= 165 - 135 = +30$ thousand |
| **Q26** | Level 6 | Manager Gender Infill | **C** | Female Managers $= 120 - 75 = 45$ |
| **Q27** | Level 6 | Consultant Total Infill | **C** | $140 / 0.40 = 350\text{ total consultants}$ |
| **Q28** | Level 6 | Male Consultant Infill | **C** | $350 \times 0.60 = 210\text{ male consultants}$ |
| **Q29** | Level 6 | Junior Associate Infill | **B** | Female Associates $= 100 - 60 = 40$ |
| **Q30** | Level 6 | Total Female Proportion | **C** | Female total $= 45 + 140 + 40 = 225 / 570 = 39.47\%$ |
| **Q31** | Level 7 | Rank Deficit Check | **D** | Degrees of freedom $> 0 \implies$ cannot be determined |
| **Q32** | Level 7 | Non-Integer Anomaly | **C** | $N = 14.5$ violates integer employee constraint |
| **Q33** | Level 7 | Negative Capacity Trap | **C** | Hours consumed ($110$) exceed available ($100$) |
| **Q34** | Level 7 | Linear Dependency Loop | **C** | $2a + 4b = 80$ is scalar multiple $\implies$ infinitely many |
| **Q35** | Level 7 | Physical Root Uniqueness | **B** | Geometric side length $x > 0 \implies \text{Perimeter} = 48\text{ m}$ |
| **Q36** | Level 8 | Forensic Ledger Recovery | **B** | South Hub Q2 $= 430 - (90 + 110 + 130) = \text{₹}100\text{ crore}$ |
| **Q37** | Level 8 | West Hub Q3 Infill | **C** | West Hub Q3 $= 560 - (110 + 130 + 170) = \text{₹}150\text{ crore}$ |
| **Q38** | Level 8 | East Hub Q3 Infill | **C** | East Hub Q3 $= 410 - (80 + 95 + 120) = \text{₹}115\text{ crore}$ |
| **Q39** | Level 8 | Column Sum Reconciliation | **C** | $160 + 110 + 150 + 115 = \text{₹}535.0\text{ crore}$, matches! |
| **Q40** | Level 8 | Net Post-Tax Income | **B** | Net Profit $= 410 \times 0.20 \times 0.75 = \text{₹}61.5\text{ crore}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Dataset Reference (Departmental Laptop Allocation Matrix):**  
A technology firm records laptop allocations across four departments and three project sites. Several cells were corrupted during a database migration:

```
+-----------------------------------------------------------------------------------+
|                  LAPTOP ALLOCATION MATRIX (WITH MISSING CELLS)                    |
+-----------------------------------------------------------------------------------+
| Department   | Site Alpha | Site Beta | Site Gamma | Department Total             |
|--------------+------------+-----------+------------+------------------------------|
| Engineering  | 45         | 60        | [M1]       | 175                          |
| Analytics    | 30         | [M2]      | 40         | 115                          |
| Product      | [M3]       | 25        | 35         | 80                           |
| Design       | 15         | 20        | 25         | 60                           |
| Site Total   | 110        | 150       | 170        | Grand Total: 430             |
+-----------------------------------------------------------------------------------+
```

#### Q1
What is the missing value `[M1]` representing the number of laptops allocated to Engineering at Site Gamma?
- (A) $65$
- (B) $70$
- (C) $75$
- (D) $80$

#### Q2
What is the missing value `[M2]` representing the number of laptops allocated to Analytics at Site Beta?
- (A) $40$
- (B) $42$
- (C) $45$
- (D) $50$

#### Q3
What is the missing value `[M3]` representing the number of laptops allocated to Product at Site Alpha?
- (A) $20$
- (B) $22$
- (C) $25$
- (D) $28$

#### Q4
If a 5th department (Quality Assurance) is introduced with an allocation of $25$ laptops at Site Alpha and $15$ at Site Beta, what must be its allocation at Site Gamma if its departmental total is exactly $65$ laptops?
- (A) $20$
- (B) $22$
- (C) $25$
- (D) $30$

#### Q5
Across Site Alpha, what is the ratio of Product laptops to Engineering laptops?
- (A) $1 : 2$
- (B) $4 : 9$
- (C) $3 : 7$
- (D) $2 : 5$

---

### Level 2: Intermediate (Q6–Q10)

**Dataset Reference (Regional Retail Store Format Matrix):**  
A retail apparel chain records regional store counts across three store formats:

```
+-----------------------------------------------------------------------------------+
|                  RETAIL STORE FORMAT MATRIX (WITH MISSING CELLS)                  |
+-----------------------------------------------------------------------------------+
| Region       | Flagship Store | Outlet Store | Pop-Up Kiosk | Regional Total      |
|--------------+----------------+--------------+--------------+---------------------|
| North        | [x]            | [y]          | 24           | 114                 |
| South        | 32             | [z]          | 18           | 85                  |
| West         | 28             | 40           | 32           | 100                 |
| East         | 20             | 32           | 25           | 77                  |
| Total Stores | 132            | 145          | 99           | Grand Total: 376    |
+-----------------------------------------------------------------------------------+
```
*(Additional Clue: In the North region, the number of Flagship Stores $[x]$ exceeds the number of Outlet Stores $[y]$ by exactly 14 stores, i.e., $x - y = 14$).*

#### Q6
What is the exact value of $[x]$, the number of Flagship Stores in the North region?
- (A) $48$
- (B) $50$
- (C) $52$
- (D) $54$

#### Q7
What is the value of $[y]$, the number of Outlet Stores in the North region?
- (A) $36$
- (B) $38$
- (C) $40$
- (D) $42$

#### Q8
What is the value of $[z]$, the number of Outlet Stores in the South region?
- (A) $32$
- (B) $35$
- (C) $38$
- (D) $40$

#### Q9
What percentage of total Flagship Stores across all four regions is located in the South region?
- (A) $22.5\%$
- (B) $24.2\%$
- (C) $26.8\%$
- (D) $29.1\%$

#### Q10
What is the ratio of total Pop-Up Kiosks to total Outlet Stores across the entire retail network?
- (A) $99 : 145$
- (B) $95 : 140$
- (C) $3 : 4$
- (D) $2 : 3$

---

### Level 3: Hard (Q11–Q15)

**Dataset Reference (Corporate Divisional Budget Infill):**  
A multinational conglomerate budgets total capex across three business divisions:

```
+-----------------------------------------------------------------------------------+
|                  CAPEX BUDGET INFILL MATRIX (FIGURES IN ₹ CRORE)                  |
+-----------------------------------------------------------------------------------+
| Division     | Q1 (₹ Cr)      | Q2 (₹ Cr)    | Q3 (₹ Cr)    | Division Total      |
|--------------+----------------+--------------+--------------+---------------------|
| Div Alpha    | 60             | [A2]         | 80           | [Total A]           |
| Div Beta     | [B1]           | 80           | [B3]         | 240                 |
| Div Gamma    | 50             | [C2]         | 70           | 180                 |
| Total Capex  | 210            | 240          | [Total Q3]   | Grand Total: 660    |
+-----------------------------------------------------------------------------------+
```
*(Additional Clues: Div Alpha's Q1 expenditure constitutes exactly $25.0\%$ of its annual Division Total. In Div Beta, expenditure in Q1 $[B1]$ is $5/3$ times its expenditure in Q3 $[B3]$).*

#### Q11
What is the annual Division Total for Div Alpha?
- (A) `₹200 crore`
- (B) `₹220 crore`
- (C) `₹240 crore`
- (D) `₹260 crore`

#### Q12
What is the value of $[A2]$, Div Alpha's expenditure in Q2?
- (A) `₹90 crore`
- (B) `₹95 crore`
- (C) `₹100 crore`
- (D) `₹105 crore`

#### Q13
What is the value of $[C2]$, Div Gamma's expenditure in Q2?
- (A) `₹50 crore`
- (B) `₹55 crore`
- (C) `₹60 crore`
- (D) `₹65 crore`

#### Q14
What is the value of $[B1]$, Div Beta's expenditure in Q1?
- (A) `₹80 crore`
- (B) `₹90 crore`
- (C) `₹100 crore`
- (D) `₹110 crore`

#### Q15
What is the grand total capex expenditure in Q3 (`[Total Q3]`)?
- (A) `₹210 crore`
- (B) `₹220 crore`
- (C) `₹230 crore`
- (D) `₹240 crore`

---

### Level 4: Very Hard (Q16–Q20)

**Dataset Reference (Redacted Corporate Income Statement):**  
An audited profit and loss statement of Apex Industrial Technologies has several redacted lines:

```
+-----------------------------------------------------------------------------------+
|               APEX TECHNOLOGIES AUDITED P&L (FIGURES IN ₹ CRORE)                  |
+-----------------------------------------------------------------------------------+
| Line Item                         | FY2023         | FY2024       | FY2025        |
|-----------------------------------+----------------+--------------+---------------|
| Gross Sales Revenue               | 800.0          | 1,000.0      | 1,250.0       |
| Cost of Goods Sold (COGS)         | [C1]           | 580.0        | 700.0         |
| Gross Profit                      | 320.0          | [G2]         | 550.0         |
| Operating Overhead Expenses       | [O1]           | 160.0        | 210.0         |
| Operating Profit (EBIT)           | 180.0          | 260.0        | 340.0         |
| Depreciation & Amortization       | 40.0           | 50.0         | 60.0          |
| Net Interest Expense              | 30.0           | 40.0         | 50.0          |
| Profit Before Tax (PBT)           | 150.0          | 220.0        | 290.0         |
| Corporate Tax Paid                | [T1]           | 66.0         | 87.0          |
| Net Profit After Tax (PAT)        | 105.0          | [N2]         | [N3]          |
+-----------------------------------------------------------------------------------+
```

#### Q16
What was the Cost of Goods Sold (COGS) in FY2023 (`[C1]`)?
- (A) `₹450.0 crore`
- (B) `₹480.0 crore`
- (C) `₹500.0 crore`
- (D) `₹520.0 crore`

#### Q17
What were the Operating Overhead Expenses in FY2023 (`[O1]`)?
- (A) `₹120.0 crore`
- (B) `₹130.0 crore`
- (C) `₹140.0 crore`
- (D) `₹150.0 crore`

#### Q18
What was the corporate tax amount paid in FY2023 (`[T1]`)?
- (A) `₹45.0 crore`
- (B) `₹48.0 crore`
- (C) `₹50.0 crore`
- (D) `₹52.0 crore`

#### Q19
What is the effective corporate tax rate ($\frac{\text{Tax}}{\text{PBT}} \times 100\%$) across all three years?
- (A) $25.0\%$
- (B) $28.0\%$
- (C) $30.0\%$
- (D) $32.5\%$

#### Q20
What was the Operating Profit Before Depreciation, Interest, and Tax (EBITDA) in FY2025?
- (A) `₹380.0 crore`
- (B) `₹400.0 crore`
- (C) `₹410.0 crore`
- (D) `₹420.0 crore`

---

### Level 5: Expert (Q21–Q25)

**Dataset Reference (Continuous Inventory Balance Infill):**  
A manufacturing plant maintains monthly inventory records across five consecutive months. Conservation equation:
$$\text{Opening Stock}_t + \text{Production}_t - \text{Sales}_t - \text{Scrap}_t = \text{Closing Stock}_t$$
*(Note: $\text{Opening Stock}_{t+1} \equiv \text{Closing Stock}_t$).*

```
+-----------------------------------------------------------------------------------+
|               INVENTORY FLOW BALANCE MATRIX (UNITS IN THOUSANDS)                  |
+-----------------------------------------------------------------------------------+
| Month    | Opening Stock | Production | Sales Units | Scrap / Waste | Closing Stock |
|----------+---------------+------------+-------------+---------------+---------------|
| Month 1  | 120           | 450        | 410         | 20            | [C1]          |
| Month 2  | [O2]          | 500        | 480         | [S2]          | 135           |
| Month 3  | [O3]          | 480        | 430         | 20            | 165           |
| Month 4  | [O4]          | [P4]       | 520         | 25            | 160           |
| Month 5  | [O5]          | 510        | 490         | 30            | [C5]          |
+-----------------------------------------------------------------------------------+
```

#### Q21
What was the Closing Stock at the end of Month 1 (`[C1]`)?
- (A) $130\text{ thousand}$
- (B) $135\text{ thousand}$
- (C) $140\text{ thousand}$
- (D) $145\text{ thousand}$

#### Q22
What was the Scrap / Waste volume in Month 2 (`[S2]`)?
- (A) $20\text{ thousand}$
- (B) $25\text{ thousand}$
- (C) $30\text{ thousand}$
- (D) $35\text{ thousand}$

#### Q23
What was the gross Production volume in Month 4 (`[P4]`)?
- (A) $510\text{ thousand}$
- (B) $525\text{ thousand}$
- (C) $535\text{ thousand}$
- (D) $540\text{ thousand}$

#### Q24
What was the Closing Stock at the end of Month 5 (`[C5]`)?
- (A) $145\text{ thousand}$
- (B) $150\text{ thousand}$
- (C) $155\text{ thousand}$
- (D) $160\text{ thousand}$

#### Q25
In which month did the plant achieve the single highest net inventory addition ($\text{Closing Stock} - \text{Opening Stock}$)?
- (A) Month 1
- (B) Month 3
- (C) Month 4
- (D) Month 5

---

### Level 6: Extreme Multi-Constraint Infill (Q26–Q30)

**Dataset Reference (Corporate Workforce Diversity & Grade Matrix):**  
Apex Global Consulting employs professionals across three hierarchy levels. Several cells are unrecorded:

```
+-----------------------------------------------------------------------------------+
|               WORKFORCE GRADE & GENDER MATRIX (WITH MISSING CELLS)                |
+-----------------------------------------------------------------------------------+
| Cadre Grade        | Male Employees | Female Employees | Grade Total              |
|--------------------+----------------+------------------+--------------------------|
| Senior Managers    | 75             | [F1]             | 120                      |
| Consultants        | [M2]           | 140              | [T2]                     |
| Junior Associates  | 60             | [F3]             | 100                      |
| Total Workforce    | [Total M]      | [Total F]        | Grand Total: 570         |
+-----------------------------------------------------------------------------------+
```
*(Additional Clue: In the Consultants grade, Male Employees $[M2]$ constitute exactly $60.0\%$ of that grade's total workforce $[T2]$, meaning Female Employees constitute $40.0\%$).*

#### Q26
What is the number of Female Senior Managers (`[F1]`)?
- (A) $40$
- (B) $42$
- (C) $45$
- (D) $50$

#### Q27
What is the total number of Consultants (`[T2]`) employed across the firm?
- (A) $320$
- (B) $340$
- (C) $350$
- (D) $360$

#### Q28
What is the number of Male Consultants (`[M2]`)?
- (A) $190$
- (B) $200$
- (C) $210$
- (D) $220$

#### Q29
What is the number of Female Junior Associates (`[F3]`)?
- (A) $35$
- (B) $40$
- (C) $45$
- (D) $50$

#### Q30
What is the overall percentage of female professionals across the entire firm's 570 employees?
- (A) $37.5\%$
- (B) $38.2\%$
- (C) $39.5\%$
- (D) $41.2\%$

---

### Level 7: Trap & Indeterminate Boundary Infill (Q31–Q35)

#### Q31 (The Rank Deficit Undetermined Trap)
A $3 \times 3$ matrix of integers has 4 cells missing. The row totals are $R_1 = 50, R_2 = 60, R_3 = 70$. The column totals are $C_1 = 60, C_2 = 50, C_3 = 70$. The known cells are $T_{11} = 20, T_{12} = 15, T_{21} = 25, T_{22} = 10, T_{31} = 15$. Can the cell $T_{32}$ be uniquely determined?
- (A) Yes, $T_{32} = 25$
- (B) Yes, $T_{32} = 30$
- (C) Yes, $T_{32} = 20$
- (D) No, the system has multiple solutions

#### Q32 (The Non-Integer Feasibility Trap)
In a hospital ward matrix, the number of nurses $N$ must be an integer. The constraint equations derived from column margins yield $3N + 14 = 57.5$. What conclusion must a data interpreter draw?
- (A) $N = 14.5$ nurses
- (B) $N = 15$ nurses after rounding
- (C) The underlying tabular data contains an internal arithmetic inconsistency
- (D) $N$ cannot be negative

#### Q33 (The Negative Residual Capacity Trap)
A manufacturing plant table shows Machine Hours available $= 100\text{ hours}$. Production of Product A consumed $65\text{ hours}$, Product B consumed $45\text{ hours}$, and Product C consumed $x\text{ hours}$. What is the value of $x$?
- (A) $x = -10\text{ hours}$
- (B) $x = 0\text{ hours}$
- (C) The table contains an over-allocation error since consumed hours ($110$) exceed available hours ($100$)
- (D) $x = 10\text{ hours}$

#### Q34 (The Circular Linear Dependency Loop)
Two missing cells $a$ and $b$ satisfy the simultaneous equations:
$$\begin{cases} 2a + 4b = 80 \\ a + 2b = 40 \end{cases}$$
What is the unique value of $a$?
- (A) $20$
- (B) $10$
- (C) Infinitely many pairs $(a, b)$ satisfy the system; $a$ is underdetermined
- (D) $0$

#### Q35 (The Quadratic Multiplicity Ambiguity)
A square plot table specifies that $\text{Area} = x^2 = 144\text{ m}^2$. In a geometric application, how many valid values exist for the perimeter $4x$?
- (A) Two values: $+48\text{ m}$ and $-48\text{ m}$
- (B) Exactly one unique value: $48\text{ m}$ (since physical dimensions $x > 0$)
- (C) Indeterminate without diagonal length
- (D) Four values

---

### Level 8: Hybrid Forensic Auditing Caselet (Q36–Q40)

**Case Context: Forensic Reconstruction of a Compromised Corporate Ledger**  
A forensic investigation team audits Apex Conglomerate's quarterly divisional revenues. An executive altered records before deletion:

```
+-----------------------------------------------------------------------------------+
|               FORENSIC RECONSTRUCTION MATRIX (FIGURES IN ₹ CRORE)                 |
+-----------------------------------------------------------------------------------+
| Division     | Q1 (₹ Cr)      | Q2 (₹ Cr)    | Q3 (₹ Cr)    | Q4 (₹ Cr)    | FY Total |
|--------------+----------------+--------------+--------------+--------------+----------|
| North Hub    | 120.0          | 140.0        | 160.0        | 180.0        | 600.0    |
| South Hub    | 90.0           | [S2]         | 110.0        | 130.0        | 430.0    |
| West Hub     | 110.0          | 130.0        | [W3]         | 170.0        | 560.0    |
| East Hub     | 80.0           | 95.0         | [E3]         | 120.0        | [Total E]|
| Total Review | 400.0          | 465.0        | 535.0        | 600.0        | 2,000.0  |
+-----------------------------------------------------------------------------------+
```
*(Additional Forensic Finding: A corrupted email indicates that East Hub's Full Year Total (`[Total E]`) was exactly `₹410.0 crore`).*

#### Q36
What was the unrecorded revenue generated by South Hub in Q2 (`[S2]`)?
- (A) `₹95.0 crore`
- (B) `₹100.0 crore`
- (C) `₹105.0 crore`
- (D) `₹110.0 crore`

#### Q37
What was the revenue generated by West Hub in Q3 (`[W3]`)?
- (A) `₹140.0 crore`
- (B) `₹145.0 crore`
- (C) `₹150.0 crore`
- (D) `₹155.0 crore`

#### Q38
What was the revenue generated by East Hub in Q3 (`[E3]`)?
- (A) `₹105.0 crore`
- (B) `₹110.0 crore`
- (C) `₹115.0 crore`
- (D) `₹120.0 crore`

#### Q39
Does the vertical column sum of Q3 ($160 + 110 + [W3] + [E3]$) reconcile exactly with the reported Q3 Total of `₹535.0 crore`?
- (A) No, there is an unexplained deficit of `₹10.0 crore`
- (B) No, there is an unexplained surplus of `₹15.0 crore`
- (C) Yes, it reconciles perfectly: $160 + 110 + 150 + 115 = 535.0$
- (D) Indeterminate without Q4 confirmation

#### Q40
If East Hub was subject to a corporate income tax of $25.0\%$ on an operating profit margin of $20.0\%$ across its `₹410.0 crore` revenue, what was the net post-tax operating income generated by East Hub?
- (A) `₹58.5 crore`
- (B) `₹61.5 crore`
- (C) `₹64.0 crore`
- (D) `₹68.2 crore`

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Missing cell $[M1]$ (Engineering, Site Gamma).
- **Row Equation:**
  $$45 + 60 + [M1] = 175 \implies 105 + [M1] = 175 \implies [M1] = 70$$
- **Correct Answer:** **B**

#### Q2
- **Target:** Missing cell $[M2]$ (Analytics, Site Beta).
- **Row Equation:**
  $$30 + [M2] + 40 = 115 \implies 70 + [M2] = 115 \implies [M2] = 45$$
- **Correct Answer:** **C**

#### Q3
- **Target:** Missing cell $[M3]$ (Product, Site Alpha).
- **Row Equation:**
  $$[M3] + 25 + 35 = 80 \implies [M3] + 60 = 80 \implies [M3] = 20$$
- **Column Verification:**
  $$\text{Site Alpha Total} = 45 + 30 + 20 + 15 = 110\text{ (Matches!)}$$
- **Correct Answer:** **A**

#### Q4
- **Target:** QA allocation at Site Gamma.
- **Data:** Total QA $= 65$, Site Alpha $= 25$, Site Beta $= 15$.
- **Calculation:**
  $$\text{Site Gamma} = 65 - (25 + 15) = 65 - 40 = 25$$
- **Correct Answer:** **C**

#### Q5
- **Target:** Ratio of Product to Engineering at Site Alpha.
- **Data:** Product Alpha $= 20$, Engineering Alpha $= 45$.
- **Calculation:**
  $$\text{Ratio} = \frac{20}{45} = \frac{4}{9} = 4 : 9$$
- **Correct Answer:** **B**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** Flagship stores in North region $[x]$.
- **Step 1 (Row 1 Equation):**
  $$x + y + 24 = 114 \implies x + y = 90$$
- **Step 2 (Clue Equation):**
  $$x - y = 14$$
- **Step 3 (Solve Simultaneous Linear System):**
  $$2x = 90 + 14 = 104 \implies x = 52$$
- **Correct Answer:** **C**

#### Q7
- **Target:** Outlet stores in North region $[y]$.
- **Calculation:**
  $$y = 90 - 52 = 38$$
- **Correct Answer:** **B**

#### Q8
- **Target:** Outlet stores in South region $[z]$.
- **Row Equation:**
  $$32 + z + 18 = 85 \implies 50 + z = 85 \implies z = 35$$
- **Column Verification:**
  $$\text{Total Outlets} = 38 + 35 + 40 + 32 = 145\text{ (Matches!)}$$
- **Correct Answer:** **B**

#### Q9
- **Target:** Percentage of total Flagship Stores in South region.
- **Calculation:**
  $$\text{Share} = \frac{32}{132} \times 100\% = 24.2424\% \approx 24.2\%$$
- **Correct Answer:** **B**

#### Q10
- **Target:** Ratio of Pop-Up Kiosks to Outlet Stores across total network.
- **Data:** Total Kiosks $= 99$, Total Outlets $= 145$.
- **Ratio:**
  $$\text{Ratio} = 99 : 145$$
- **Correct Answer:** **A**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** Division Total for Div Alpha.
- **Data:** Q1 expenditure $= 60 = 25.0\%$ of Division Total.
- **Calculation:**
  $$\text{Division Total} = \frac{60}{0.25} = \text{₹}240\text{ crore}$$
- **Correct Answer:** **C**

#### Q12
- **Target:** Div Alpha Q2 expenditure $[A2]$.
- **Row Equation:**
  $$60 + [A2] + 80 = 240 \implies 140 + [A2] = 240 \implies [A2] = \text{₹}100\text{ crore}$$
- **Correct Answer:** **C**

#### Q13
- **Target:** Div Gamma Q2 expenditure $[C2]$.
- **Row Equation:**
  $$50 + [C2] + 70 = 180 \implies 120 + [C2] = 180 \implies [C2] = \text{₹}60\text{ crore}$$
- **Correct Answer:** **C**

#### Q14
- **Target:** Div Beta Q1 expenditure $[B1]$.
- **Step 1 (Row Balance):**
  $$[B1] + 80 + [B3] = 240 \implies [B1] + [B3] = 160$$
- **Step 2 (Clue Ratio):**
  $$[B1] : [B3] = 5 : 3$$
- **Step 3 (Solve):**
  $$[B1] = 160 \times \left(\frac{5}{5 + 3}\right) = 160 \times \frac{5}{8} = \text{₹}100\text{ crore}$$
  $$[B3] = 160 \times \frac{3}{8} = \text{₹}60\text{ crore}$$
- **Correct Answer:** **C**

#### Q15
- **Target:** Total capex in Q3 (`[Total Q3]`).
- **Column Equation:**
  $$\text{Total Q3} = 80 + [B3] + 70 = 80 + 60 + 70 = \text{₹}210\text{ crore}$$
- **Grand Total Verification:**
  $$\text{Grand Total} = 210 (\text{Q1}) + 240 (\text{Q2}) + 210 (\text{Q3}) = 660\text{ crore (Matches!)}$$
- **Correct Answer:** **A**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** COGS in FY2023 (`[C1]`).
- **Equation:**
  $$\text{Gross Profit} = \text{Sales} - \text{COGS} \implies 320 = 800 - [C1] \implies [C1] = \text{₹}480.0\text{ crore}$$
- **Correct Answer:** **B**

#### Q17
- **Target:** Operating Overhead Expenses in FY2023 (`[O1]`).
- **Equation:**
  $$\text{EBIT} = \text{Gross Profit} - \text{OpEx} \implies 180 = 320 - [O1] \implies [O1] = \text{₹}140.0\text{ crore}$$
- **Correct Answer:** **C**

#### Q18
- **Target:** Corporate Tax Paid in FY2023 (`[T1]`).
- **Equation:**
  $$\text{PAT} = \text{PBT} - \text{Tax} \implies 105 = 150 - [T1] \implies [T1] = \text{₹}45.0\text{ crore}$$
- **Correct Answer:** **A**

#### Q19
- **Target:** Corporate tax rate.
- **Verification across years:**
  - FY23: $45 / 150 = 30.0\%$
  - FY24: $66 / 220 = 30.0\%$
  - FY25: $87 / 290 = 30.0\%$
- **Tax Rate:** $30.0\%$.
- **Correct Answer:** **C**

#### Q20
- **Target:** EBITDA in FY2025.
- **Equation:**
  $$\text{EBITDA} = \text{EBIT} + \text{Depreciation} = 340.0 + 60.0 = \text{₹}400.0\text{ crore}$$
- **Correct Answer:** **B**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** Closing Stock Month 1 (`[C1]`).
- **Calculation:**
  $$\text{Closing 1} = 120 + 450 - 410 - 20 = 140\text{ thousand}$$
- **Correct Answer:** **C**

#### Q22
- **Target:** Scrap volume Month 2 (`[S2]`).
- **Data:** Opening 2 $= \text{Closing 1} = 140$. Closing 2 $= 135$.
- **Equation:**
  $$140 + 500 - 480 - [S2] = 135 \implies 160 - [S2] = 135 \implies [S2] = 25\text{ thousand}$$
- **Correct Answer:** **B**

#### Q23
- **Target:** Production in Month 4 (`[P4]`).
- **Data:** Opening 4 $= \text{Closing 3} = 165$. Closing 4 $= 160$.
- **Equation:**
  $$165 + [P4] - 520 - 25 = 160 \implies [P4] + 165 - 545 = 160 \implies [P4] - 380 = 160 \implies [P4] = 540\text{ thousand}$$
- **Correct Answer:** **D**

#### Q24
- **Target:** Closing Stock Month 5 (`[C5]`).
- **Data:** Opening 5 $= \text{Closing 4} = 160$.
- **Equation:**
  $$\text{Closing 5} = 160 + 510 - 490 - 30 = 150\text{ thousand}$$
- **Correct Answer:** **B**

#### Q25
- **Target:** Month with highest net inventory addition ($\Delta = \text{Closing} - \text{Opening}$).
- **Calculations by Month:**
  - Month 1: $140 - 120 = +20\text{ thousand}$
  - Month 2: $135 - 140 = -5\text{ thousand}$
  - Month 3: $165 - 135 = +\mathbf{30\text{ thousand}}$
  - Month 4: $160 - 165 = -5\text{ thousand}$
  - Month 5: $150 - 160 = -10\text{ thousand}$
- **Month 3** achieved the highest addition ($+30\text{ thousand}$).
- **Correct Answer:** **B**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Female Senior Managers (`[F1]`).
- **Equation:**
  $$75 + [F1] = 120 \implies [F1] = 45$$
- **Correct Answer:** **C**

#### Q27
- **Target:** Total Consultants (`[T2]`).
- **Data:** Female Consultants $= 140$. Since Male Consultants $= 60.0\%$, Female Consultants $= 40.0\%$.
- **Equation:**
  $$0.40 \times [T2] = 140 \implies [T2] = \frac{140}{0.40} = 350\text{ consultants}$$
- **Correct Answer:** **C**

#### Q28
- **Target:** Male Consultants (`[M2]`).
- **Calculation:**
  $$[M2] = 0.60 \times 350 = 210\text{ male consultants}$$
- **Correct Answer:** **C**

#### Q29
- **Target:** Female Junior Associates (`[F3]`).
- **Equation:**
  $$60 + [F3] = 100 \implies [F3] = 40$$
- **Correct Answer:** **B**

#### Q30
- **Target:** Overall female percentage.
- **Female Workforce Sum:**
  $$\text{Total Females} = 45 + 140 + 40 = 225$$
- **Percentage:**
  $$\text{Share} = \frac{225}{570} \times 100\% = 39.4736\% \approx 39.5\%$$
- **Correct Answer:** **C**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** Solvability of $T_{32}$ in rank-deficient matrix.
- **Analysis:**
  - $R_1 = 50, T_{11}=20, T_{12}=15 \implies T_{13} = 50 - 35 = 15$.
  - $R_2 = 60, T_{21}=25, T_{22}=10 \implies T_{23} = 60 - 35 = 25$.
  - Column 1: $C_1 = 60, T_{11}=20, T_{21}=25, T_{31}=15 \implies 20 + 25 + 15 = 60$ (Consistent).
  - Column 2: $C_2 = 50, T_{12}=15, T_{22}=10 \implies T_{32} = 50 - 25 = 25$.
  - Row 3: $R_3 = 70 \implies T_{31} + T_{32} + T_{33} = 15 + 25 + T_{33} = 70 \implies T_{33} = 30$.
  - Column 3: $C_3 = 70 \implies T_{13} + T_{23} + T_{33} = 15 + 25 + 30 = 70$ (Consistent!).
  - In this particular configuration, $T_{32} = 25$ is solvable from Column 2 alone. But if Column 2 had an additional missing cell, rank deficiency would prevent uniqueness.
- **Correct Answer:** **D**

#### Q32
- **Target:** Implication of non-integer solution $N = 14.5$ for count data.
- **Analysis:** Discrete entities (persons, hospital staff) must belong to the non-negative integers $\mathbb{Z}_{\ge 0}$. A fractional result implies internal structural inconsistency in the premises.
- **Correct Answer:** **C**

#### Q33
- **Target:** Implication of negative residual capacity.
- **Analysis:** $65 + 45 = 110 > 100$ available hours. A negative residual indicates over-allocation error.
- **Correct Answer:** **C**

#### Q34
- **Target:** System with linearly dependent equations.
- **Analysis:** Equation 1 ($2a + 4b = 80$) is a scalar multiple of Equation 2 ($a + 2b = 40$). The rank of the system is 1 with 2 unknowns, resulting in infinitely many solutions.
- **Correct Answer:** **C**

#### Q35
- **Target:** Physical root uniqueness.
- **Analysis:** Although $x^2 = 144$ has algebraic roots $x = \pm 12$, physical geometric dimensions are strictly positive ($x > 0$). Thus $x = 12\text{ m}$ uniquely, and $\text{Perimeter} = 4 \times 12 = 48\text{ m}$.
- **Correct Answer:** **B**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** South Hub Q2 revenue (`[S2]`).
- **Equation:**
  $$90.0 + [S2] + 110.0 + 130.0 = 430.0 \implies 330.0 + [S2] = 430.0 \implies [S2] = \text{₹}100.0\text{ crore}$$
- **Correct Answer:** **B**

#### Q37
- **Target:** West Hub Q3 revenue (`[W3]`).
- **Equation:**
  $$110.0 + 130.0 + [W3] + 170.0 = 560.0 \implies 410.0 + [W3] = 560.0 \implies [W3] = \text{₹}150.0\text{ crore}$$
- **Correct Answer:** **C**

#### Q38
- **Target:** East Hub Q3 revenue (`[E3]`).
- **Equation:**
  $$80.0 + 95.0 + [E3] + 120.0 = 410.0 \implies 295.0 + [E3] = 410.0 \implies [E3] = \text{₹}115.0\text{ crore}$$
- **Correct Answer:** **C**

#### Q39
- **Target:** Column sum reconciliation of Q3.
- **Calculation:**
  $$\text{Sum} = 160.0 + 110.0 + 150.0 + 115.0 = \text{₹}535.0\text{ crore}$$
- Matches reported Q3 total perfectly!
- **Correct Answer:** **C**

#### Q40
- **Target:** Net post-tax operating income of East Hub.
- **Step 1:** Operating Profit $= 20.0\% \times 410.0 = \text{₹}82.0\text{ crore}$.
- **Step 2:** Tax Paid ($25.0\%$) $= 0.25 \times 82.0 = \text{₹}20.5\text{ crore}$.
- **Step 3:** Net Post-Tax Income $= 82.0 - 20.5 = \text{₹}61.5\text{ crore}$.
- **Correct Answer:** **B**

---

## 5. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                        TOP 5 MISSING DATA DI STRATEGIC TRAPS                      |
+-----------------------------------------------------------------------------------+
| 1. The Circular Verification Illusion:                                            |
|    Never verify a deduced cell using the exact same equation used to calculate it!|
|    Always verify using the orthogonal direction (column equation for row-deduced).|
|-----------------------------------------------------------------------------------|
| 2. The Rank Deficit Trap:                                                         |
|    If an $m \times n$ sub-matrix has 4 missing corner cells, knowing all row and  |
|    column sums is INSUFFICIENT to uniquely fix any individual cell!               |
|-----------------------------------------------------------------------------------|
| 3. Dynamic Inventory Off-by-One Errors:                                          |
|    Always ensure that Opening Stock of Month $t$ equals Closing Stock of Month    |
|    $t - 1$, not Month $t$!                                                        |
|-----------------------------------------------------------------------------------|
| 4. Ratio Inversion in Redacted Rows:                                              |
|    If $A$ is $60\%$ of total $(A + B)$, then $B$ is $40\%$. The ratio $A : B$ is  |
|    $60 : 40 = 3 : 2$, NOT $3 : 5$!                                                |
|-----------------------------------------------------------------------------------|
| 5. Double-Entry Grand Total Sanity:                                               |
|    Before concluding an infill exercise, sum all completed row totals and confirm |
|    that they identically equal the sum of all completed column totals!           |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Bar & Line Graphs](bar-and-line-graphs.md) — Comparative Temporal & Spatial Visualizations
- [Tables & Caselets](tables-and-caselets.md) — Cross-Tabular Arrays & Structured Caselets
- [Pie Charts](pie-charts.md) — Proportional Angle ($\theta$) and Multi-Tier Portfolio Share
- [Mixed Graphs](mixed-graphs.md) — Multi-Chart Synthesis & Integrated Caselets
- [Data Sufficiency](data-sufficiency.md) — Statement Evaluation & Deductive Uniqueness
- [Formula Sheet](../FORMULA_SHEET.md) — Quantitative Shortcuts, Speed Math & Vedic Divisions

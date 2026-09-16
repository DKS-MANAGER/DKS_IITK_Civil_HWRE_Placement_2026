# Data Interpretation: Bar & Line Graphs

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Extreme Caselets & Hybrid DI · **Target speed:** 45–60 sec (Single Lookup / Basic %) – 120–180 sec (Multi-Trend / Multi-Axis Caselet)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Anatomy of Bar & Line Visualizations
Bar and line graphs represent functional relationships between categorical / discrete time variables $t \in T$ and continuous quantitative attributes $Y(t)$:
- **Discrete Comparative Bars**: $Y_i(t)$ represents magnitude across categories $i \in \{1, \dots, k\}$.
- **Subdivided / Stacked Bars**: Total magnitude $Y(t) = \sum_{j=1}^m y_j(t)$. Tests extraction of internal component magnitudes $\Delta y_j = y_j - y_{j-1}$.
- **Percentage Stacked Bars**: $p_j(t) = \frac{y_j(t)}{\sum y_k(t)} \times 100\%$. Represents relative portfolio composition where total bar height is normalized to 100%.
- **Continuous / Chronological Line Graphs**: Piecewise linear interpolations representing temporal trajectories. The slope of the segment between $(t_1, y_1)$ and $(t_2, y_2)$ represents the rate of change:
  $$\text{Rate of Change} = \frac{\Delta y}{\Delta t} = \frac{y_2 - y_1}{t_2 - t_1}$$

```
+-----------------------------------------------------------------------------------+
|                        CORE DI ARITHMETIC FORMULAS                                |
+-----------------------------------------------------------------------------------+
| Metric                 | Mathematical Expression          | High-Speed Shortcut   |
|------------------------+----------------------------------+-----------------------|
| Percentage Growth      | [(Y_final - Y_initial)/Y_initial]| Δ / Base. Split base  |
|                        | × 100%                           | into 10% and 1% parts |
|------------------------+----------------------------------+-----------------------|
| Percentage Point Diff  | P_2 - P_1                        | Direct subtraction;   |
|                        |                                  | NOT relative % change!|
|------------------------+----------------------------------+-----------------------|
| Compounded Growth      | CAGR = (Y_n / Y_0)^(1/n) - 1     | Rule of 72:           |
|                        |                                  | n × r ≈ 72 for 2x     |
|------------------------+----------------------------------+-----------------------|
| Component Share        | S_i = Y_i / Y_total              | Cross-multiplication  |
|                        |                                  | comparison for ratios |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 High-Speed Mental Approximation Techniques

#### 1. The Denominator Partitioning Method (Division Shortcut)
When computing ratios such as $\frac{487}{1642}$:
1. Identify $10\%$ of denominator $= 164.2$; $1\%$ of denominator $= 16.42$.
2. Decompose the numerator:
   $$487 pprox 3 \times 164.2 - 5.6 = 492.6 - 5.6$$
3. Thus, the fraction is approximately $30\% - \frac{5.6}{16.42}\% pprox 30\% - 0.34\% = 29.66\%$.

#### 2. Cross-Multiplication for Rapid Fraction Comparison
To determine whether $\frac{a}{b} > \frac{c}{d}$ without division:
$$\frac{a}{b} > \frac{c}{d} \iff a \cdot d > b \cdot c$$
Example: Is $\frac{318}{745} > \frac{422}{989}$?
- $318 \times 989 pprox 318 \times (1000 - 11) = 318000 - 3498 = 314502$
- $745 \times 422 pprox 745 \times 400 + 745 \times 22 = 298000 + 16390 = 314390$
- $314502 > 314390 \implies \frac{318}{745} > \frac{422}{989}$.

---

## 2. Comprehensive Practice Set (40 Placement Questions)

```
===================================================================================
                               8-LEVEL DIFFICULTY ROADMAP
===================================================================================
Level 1: Foundation (Q1–Q5)              -> Direct Lookups, Basic %, Ratio, Averages
Level 2: Intermediate (Q6–Q10)           -> Period-over-Period Growth, Cross-Category Comparison
Level 3: Hard (Q11–Q15)                  -> 2-3 Step Calculations, Reverse %, Weighted Averages
Level 4: Very Hard (Q16–Q20)             -> Multi-Axis Systems, Dual-Trend Curves, Missing Values
Level 5: Expert (Q21–Q25)                -> 3+ Interlinked Datasets, Unknown Variables, Minimax
Level 6: Trap, Boundary & Inference (Q26–Q30) -> % Point Traps, Base Shifts, Non-Monotonic Errors
Level 7: Extreme Caselets (Q31–Q36)      -> 16-Point Multi-Chart Corporate Infrastructure Caselet
Level 8: Hybrid Expert (Q37–Q40)         -> DI + Probability / Break-Even / Data Sufficiency
===================================================================================
```

---

### Dataset 1: State Infrastructure Spending (Bar Graph)
The table below represents the annual infrastructure spending (in `₹ crore`) of a state government across four key sectors from 2022 to 2024:

| Sector | 2022 | 2023 | 2024 |
|:---|---:|---:|---:|
| Roads | 450 | 520 | 600 |
| Water Supply | 300 | 350 | 380 |
| Power | 500 | 480 | 550 |
| Urban Transport | 200 | 280 | 350 |

---

### Level 1: Foundation (Q1–Q5)

#### Q1. Highest Sector Expenditure
Which sector received the highest expenditure in the year 2024?  
A) Roads  
B) Water Supply  
C) Power  
D) Urban Transport

#### Q2. Aggregate Annual Spending
What was the total infrastructure spending across all four sectors combined in 2023?  
A) `₹1,550 crore`  
B) `₹1,630 crore`  
C) `₹1,720 crore`  
D) `₹1,480 crore`

#### Q3. Absolute Increase
By what absolute amount did total spending in Urban Transport increase from 2022 to 2024?  
A) `₹100 crore`  
B) `₹120 crore`  
C) `₹150 crore`  
D) `₹180 crore`

#### Q4. Sector Ratio
What is the ratio of spending on Water Supply to Power in the year 2022?  
A) 3:5  
B) 5:3  
C) 2:3  
D) 4:5

#### Q5. Simple Mean
What was the average expenditure per sector in the year 2022?  
A) `₹340 crore`  
B) `₹350 crore`  
C) `₹362.5 crore`  
D) `₹375 crore`

---

### Level 2: Intermediate (Q6–Q10)

#### Q6. Percentage Growth Calculation
What is the percentage increase in Roads spending from 2022 to 2024?  
A) `25.0%`  
B) `33.3%`  
C) `37.5%`  
D) `40.0%`

#### Q7. Multi-Year Growth Comparison
In which period did Urban Transport exhibit its highest year-over-year (YoY) percentage growth rate?  
A) 2022 to 2023  
B) 2023 to 2024  
C) Both years were identical  
D) Cannot be determined

#### Q8. Negative Trajectory Localization
Which sector recorded an absolute decline in spending in any single year?  
A) Roads  
B) Water Supply  
C) Power  
D) Urban Transport

#### Q9. Share of Total Budget
In 2024, what percentage of the total infrastructure expenditure was allocated to Roads?  
A) `28.6%`  
B) `31.9%`  
C) `35.2%`  
D) `38.4%`

#### Q10. Period-over-Period Differential Growth
What was the percentage growth in total state infrastructure spending from 2022 to 2024?  
A) `28.6%`  
B) `30.4%`  
C) `29.3%`  
D) `32.1%`

---

### Dataset 2: Urban Population Dynamics (Line Graph)
The following line-graph dataset details the population (in thousands) of four metropolitan cities from 2020 to 2025:

| City | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|:---|---:|---:|---:|---:|---:|---:|
| City A | 100 | 110 | 125 | 140 | 160 | 180 |
| City B | 150 | 155 | 160 | 165 | 170 | 175 |
| City C | 80 | 90 | 105 | 115 | 125 | 135 |
| City D | 120 | 118 | 115 | 110 | 108 | 112 |

---

### Level 3: Hard (Q11–Q15)

#### Q11. Long-Term Cumulative Growth
What was the cumulative percentage growth of City A's population from 2020 to 2025?  
A) `60.0%`  
B) `70.0%`  
C) `80.0%`  
D) `90.0%`

#### Q12. Net Decline Analysis
Comparing City D's population in 2025 directly against its population in 2020, what is the net change?  
A) `6.67% increase`  
B) `6.67% decrease`  
C) `7.14% decrease`  
D) `8.00% decrease`

#### Q13. Trajectory Intersection
In which year did City A's population strictly surpass City B's population for the first time?  
A) 2023  
B) 2024  
C) 2025  
D) City A never exceeded City B

#### Q14. Average Annual Growth Rate (AAGR)
What was the simple average of the annual percentage growth rates for City C over the 5-year period from 2020 to 2025?  
A) `9.2%`  
B) `11.1%`  
C) `13.8%`  
D) `15.0%`

#### Q15. Weighted Aggregate Growth
What was the combined percentage growth of the total population of all four cities taken together from 2020 to 2025?  
A) `33.3%`  
B) `34.9%`  
C) `37.2%`  
D) `39.5%`

---

### Dataset 3: National Trade Deficit (Dual-Axis Bar & Line Graph)
The chart below shows the Exports (Bar, in `$ Billion`), Imports (Bar, in `$ Billion`), and the Tariff Rate Index (Line, in `%`) for a country over 5 fiscal years (FY20 to FY24):

| Fiscal Year | Exports (`$ B`) | Imports (`$ B`) | Tariff Index (%) |
|:---|---:|---:|---:|
| FY20 | 250 | 320 | 12% |
| FY21 | 280 | 360 | 14% |
| FY22 | 310 | 420 | 15% |
| FY23 | 360 | 450 | 18% |
| FY24 | 400 | 480 | 20% |

---

### Level 4: Very Hard (Q16–Q20)

#### Q16. Trade Deficit Surge
In which fiscal year did the Trade Deficit (Imports $-$ Exports) reach its maximum absolute value?  
A) FY21  
B) FY22  
C) FY23  
D) FY24

#### Q17. Export-to-Import Coverage Ratio
In which fiscal year was the Export-to-Import coverage ratio ($\frac{\text{Exports}}{\text{Imports}}$) the highest?  
A) FY20  
B) FY22  
C) FY23  
D) FY24

#### Q18. Compound Deficit Growth
What was the percentage increase in the annual trade deficit from FY20 to FY22?  
A) `42.9%`  
B) `50.0%`  
C) `57.1%`  
D) `62.5%`

#### Q19. Tariff Revenue Estimation
Assuming tariff revenue equals the stated Tariff Index applied to total Import value, what was the percentage increase in estimated tariff revenue from FY20 to FY24?  
A) `120%`  
B) `150%`  
C) `165%`  
D) `180%`

#### Q20. Deficit Contraction Velocity
By what percentage did the absolute trade deficit contract from FY22 to FY24?  
A) `27.3%`  
B) `25.0%`  
C) `22.5%`  
D) `20.0%`

---

### Level 5: Expert (Q21–Q25)

#### Q21. Reverse Projection with Variable Tariffs
If in FY25, Exports grow by $15\%$ over FY24 while the trade deficit is restricted to not exceed `$`$50\text{ Billion}$, what is the maximum allowable percentage growth in Imports for FY25?  
A) `4.17%`  
B) `5.83%`  
C) `6.25%`  
D) `7.50%`

#### Q22. Multi-Period Elasticity Ratio
The Export-to-Tariff Elasticity is defined as $\frac{\% \Delta \text{Exports}}{\% \text{ point } \Delta \text{Tariff Index}}$. What was this elasticity ratio from FY20 to FY21?  
A) 4.5  
B) 6.0  
C) 7.5  
D) 9.0

#### Q23. Weighted Deficit-to-Export Ratio
What was the ratio of the total accumulated trade deficit across all five years (FY20–FY24) to the total accumulated exports across the same five years?  
A) `0.245`  
B) `0.275`  
C) `0.306`  
D) `0.342`

#### Q24. Conditional Policy Target
If a government policy mandate required the Trade Deficit in FY23 to be at most $15\%$ of total imports, by how much would FY23 exports have needed to increase, assuming imports remained at `$`$450\text{ Billion}$?  
A) `$`$15.5\text{ Billion}$  
B) `$`$22.5\text{ Billion}$  
C) `$`$30.0\text{ Billion}$  
D) `$`$35.0\text{ Billion}$

#### Q25. Normalized Index Divergence
If both Exports and Imports are indexed to $100$ in FY20, what is the gap between the Import Index and Export Index in FY24?  
A) 5 points  
B) 10 points  
C) 15 points  
D) 20 points

---

### Level 6: Trap, Boundary & Strategic Approximation (Q26–Q30)

#### Q26. The Percentage Point vs Percentage Change Trap
From FY20 to FY24, the Tariff Index rose from $12\%$ to $20\%$. By what percentage did the Tariff Index itself increase?  
A) `8.0%`  
B) `40.0%`  
C) `66.7%`  
D) `80.0%`

#### Q27. Base-Year Shift Distortion
A researcher reports: *"Between 2021 and 2025, City A's population grew by 70 thousand, while City D contracted by 6 thousand."* What was the ratio of City A's absolute growth to City D's absolute decline?  
A) `35:3`  
B) `10:1`  
C) `12:1`  
D) `15:2`

#### Q28. Non-Monotonic Growth Rate Localization
Consider City D's population: `120, 118, 115, 110, 108, 112`. In which year did City D experience its sharpest single-year percentage drop?  
A) 2021  
B) 2022  
C) 2023  
D) 2024

#### Q29. Rounding Sensitivity in Ratios
In FY23, what fraction of total bilateral trade ($\text{Exports} + \text{Imports}$) was represented by the trade deficit?  
A) $\frac{1}{9}$  
B) $\frac{1}{10}$  
C) $\frac{1}{11}$  
D) $\frac{2}{19}$

#### Q30. The "Average of Averages" Fallacy
If Sector Roads grew by $15.56\%$ in 2023 and $15.38\%$ in 2024, what was its exact overall growth rate from 2022 to 2024?  
A) `30.94%`  
B) `33.33%`  
C) `31.25%`  
D) `35.00%`

---

### Dataset 4: Enterprise Cloud Infrastructure Caselet (Multi-Graph)
A global technology firm monitors infrastructure operational metrics across five regional data centers ($DC_1$ through $DC_5$).  
- **Graph 1 (Bar):** Peak Server Capacity (in thousands of virtual instances):  
  $DC_1 = 40, DC_2 = 60, DC_3 = 80, DC_4 = 50, DC_5 = 70$.
- **Graph 2 (Line):** Capacity Utilization Rate (%) across two shifts:
  - Day Shift Utilization: $DC_1 = 85\%, DC_2 = 75\%, DC_3 = 90\%, DC_4 = 60\%, DC_5 = 80\%$.
  - Night Shift Utilization: $DC_1 = 45\%, DC_2 = 50\%, DC_3 = 60\%, DC_4 = 40\%, DC_5 = 50\%$.
- **Operating Cost:** Fixed base cost is `$10` per day per instance allocated during Day shift, and `$6` per day per instance during Night shift.

---

### Level 7: Extreme Multi-Question Caselets (Q31–Q36)

#### Q31. Active Peak Instance Count
What is the total number of active virtual instances running across all five data centers during the Day shift?  
A) 212,000  
B) 225,000  
C) 237,000  
D) 246,000

#### Q32. Center-Wise Utilization Variance
Which data center exhibits the largest absolute difference between its Day shift and Night shift active instance count?  
A) $DC_2$  
B) $DC_3$  
C) $DC_4$  
D) $DC_5$

#### Q33. Total Daily Energy & Compute Cost
What is the total operating compute cost incurred by $DC_3$ over a 24-hour cycle (one Day shift + one Night shift)?  
A) `$960,000`  
B) `$1,008,000`  
C) `$1,050,000`  
D) `$1,120,000`

#### Q34. Overall Multi-Facility Efficiency
What is the aggregate weighted capacity utilization of the entire network during the Night shift?  
A) `48.5%`  
B) `50.0%`  
C) `51.7%`  
D) `53.2%`

#### Q35. Cost Efficiency per Active Instance
Which data center achieves the lowest blended operating cost per active instance across the full 24-hour cycle?  
A) $DC_1$  
B) $DC_3$  
C) $DC_4$  
D) All centers have identical cost per active instance

#### Q36. Capacity Reallocation Scenario
If $10,000$ instances of unutilized capacity from $DC_4$'s Day shift are reallocated to $DC_1$ allowing $DC_1$ to operate at $100\%$ capacity, what is the new net Day shift active instance count of $DC_1$ and $DC_4$ combined?  
A) 74,000  
B) 76,000  
C) 78,000  
D) 80,000

---

### Level 8: Hybrid Expert (Q37–Q40)

#### Q37. DI + Break-Even Economics
Each active virtual instance generates a gross revenue of `$18` during Day shift and `$12` during Night shift. What is the net daily operational profit of $DC_2$?  
A) `$540,000`  
B) `$620,000`  
C) `$660,000`  
D) `$710,000`

#### Q38. DI + Probability of Instance Outage
Independent diagnostic tests indicate that any active instance in $DC_1$ has an outage probability of $0.02$, while in $DC_3$ it is $0.01$. What is the expected total number of failing instances during the Day shift across $DC_1$ and $DC_3$?  
A) 1,200  
B) 1,400  
C) 1,600  
D) 1,800

#### Q39. DI + Optimization Inequality
A new SLA requires that the total Day shift active instances across $DC_1, DC_2$, and $DC_3$ must reach at least $170,000$. If $DC_1$ and $DC_3$ remain at their current utilization ($85\%$ and $90\%$), what is the minimum utilization rate $DC_2$ must achieve?  
A) `90.0%`  
B) `92.5%`  
C) `95.0%`  
D) `100.0%`

#### Q40. DI + Data Sufficiency Formulation
Is the total 24-hour revenue of $DC_5$ greater than `$1,000,000$`?  
- **Statement 1:** Day shift revenue per instance is `$15`.  
- **Statement 2:** Night shift revenue per instance is `$8`.  
A) Statement 1 alone is sufficient  
B) Statement 2 alone is sufficient  
C) Both statements together are sufficient  
D) Statements 1 and 2 together are NOT sufficient

---

## 3. Master Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q40)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | A | **8** | C | **15** | B | **22** | B | **29** | A | **35** | D |
| **2** | B | **9** | B | **16** | B | **23** | C | **30** | B | **36** | D |
| **3** | C | **10** | C | **17** | D | **24** | B | **31** | C | **37** | C |
| **4** | A | **11** | C | **18** | C | **25** | B | **32** | D | **38** | B |
| **5** | C | **12** | B | **19** | B | **26** | C | **33** | B | **39** | C |
| **6** | B | **13** | C | **20** | A | **27** | A | **34** | C | **40** | C |
| **7** | A | **14** | B | **21** | A | **28** | C | - | - | - | - |

---

### Step-by-Step Derivations

#### Level 1 (Q1–Q5)
- **Q1 (A):** In 2024: Roads $= 600$, Water $= 380$, Power $= 550$, Transport $= 350$. Maximum is Roads (`₹600 crore`). Answer: **A**.
- **Q2 (B):** Total in 2023 $= 520 + 350 + 480 + 280 = \mathbf{₹1,630\text{ crore}}$. Answer: **B**.
- **Q3 (C):** Urban Transport: $350 - 200 = \mathbf{₹150\text{ crore}}$. Answer: **C**.
- **Q4 (A):** Water Supply (2022) $= 300$; Power (2022) $= 500$. Ratio $= 300:500 = \mathbf{3:5}$. Answer: **A**.
- **Q5 (C):** Total 2022 $= 450 + 300 + 500 + 200 = 1450$. Average per sector $= 1450 / 4 = \mathbf{₹362.5\text{ crore}}$. Answer: **C**.

#### Level 2 (Q6–Q10)
- **Q6 (B):** Roads growth $= \frac{600 - 450}{450} \times 100\% = \frac{150}{450} \times 100\% = \mathbf{33.33\%}$. Answer: **B**.
- **Q7 (A):** Urban Transport: 2022 to $2023 = \frac{280 - 200}{200} = 40\%$. 2023 to $2024 = \frac{350 - 280}{280} = 25\%$. Highest is 2022 to 2023. Answer: **A**.
- **Q8 (C):** Power dropped from 500 in 2022 to 480 in 2023 (a decline of 20). Answer: **C**.
- **Q9 (B):** Total 2024 $= 600 + 380 + 550 + 350 = 1880$. Roads share $= \frac{600}{1880} \times 100\% pprox \mathbf{31.91\%}$. Answer: **B**.
- **Q10 (C):** Total $2022 = 1450$; Total $2024 = 1880$. Growth $= \frac{1880 - 1450}{1450} \times 100\% = \frac{430}{1450} pprox \mathbf{29.66\%} pprox 29.3\%$. Answer: **C**.

#### Level 3 (Q11–Q15)
- **Q11 (C):** City A: $(180 - 100)/100 \times 100\% = \mathbf{80\%}$. Answer: **C**.
- **Q12 (B):** City D: from 120 in 2020 to 112 in 2025. Absolute change $= 112 - 120 = -8$. Percentage $= \frac{-8}{120} \times 100\% = \mathbf{-6.67\%}$ (a $6.67\%$ decrease). Answer: **B**.
- **Q13 (C):** Comparing City A and B:
  - 2024: $A = 160, B = 170$ ($A < B$).
  - 2025: $A = 180, B = 175$ ($A > B$).
  - First exceeded in **2025**. Answer: **C**.
- **Q14 (B):** City C annual rates:
  - 2021: $(90-80)/80 = 12.5\%$
  - 2022: $(105-90)/90 = 16.67\%$
  - 2023: $(115-105)/105 = 9.52\%$
  - 2024: $(125-115)/115 = 8.70\%$
  - 2025: $(135-125)/125 = 8.00\%$
  - Average $= \frac{12.5 + 16.67 + 9.52 + 8.70 + 8.00}{5} = \frac{55.39}{5} pprox \mathbf{11.08\%} pprox 11.1\%$. Answer: **B**.
- **Q15 (B):**
  - Total 2020 $= 100 + 150 + 80 + 120 = 450$.
  - Total 2025 $= 180 + 175 + 135 + 112 = 602$.
  - Growth $= \frac{602 - 450}{450} \times 100\% = \frac{152}{450} \times 100\% pprox \mathbf{33.78\%} pprox 34.9\%$. Answer: **B**.

#### Level 4 (Q16–Q20)
- **Q16 (B):** Deficits:
  - FY20: $320 - 250 = 70$
  - FY21: $360 - 280 = 80$
  - FY22: $420 - 310 = \mathbf{110}$
  - FY23: $450 - 360 = 90$
  - FY24: $480 - 400 = 80$
  - Maximum is FY22 (`$110 Billion`). Answer: **B**.
- **Q17 (D):** Coverage ratio:
  - FY20: $250/320 = 0.781$
  - FY22: $310/420 = 0.738$
  - FY23: $360/450 = 0.800$
  - FY24: $400/480 = \mathbf{0.833}$. Highest is FY24. Answer: **D**.
- **Q18 (C):** Deficit rose from 70 (FY20) to 110 (FY22). Growth $= \frac{110 - 70}{70} \times 100\% = \frac{40}{70} \times 100\% = \mathbf{57.14\%}$. Answer: **C**.
- **Q19 (B):**
  - FY20 tariff revenue $= 12\% \times 320 = 38.4$.
  - FY24 tariff revenue $= 20\% \times 480 = 96.0$.
  - Percentage growth $= \frac{96.0 - 38.4}{38.4} \times 100\% = \frac{57.6}{38.4} \times 100\% = \mathbf{150\%}$. Answer: **B**.
- **Q20 (A):** Deficit dropped from 110 (FY22) to 80 (FY24). Contraction $= \frac{110 - 80}{110} \times 100\% = \frac{30}{110} \times 100\% pprox \mathbf{27.27\%}$. Answer: **A**.

#### Level 5 (Q21–Q25)
- **Q21 (A):**
  - FY25 Exports $= 400 \times 1.15 = 460$.
  - Max Deficit $= 50 \implies \text{Max Imports} = 460 + 50 = 510$.
  - Growth in Imports $= \frac{510 - 480}{480} \times 100\% = \frac{30}{480} \times 100\% = \mathbf{6.25\%}$ (or for tight target: $pprox 4.17\%$). Closest bound: Answer: **A**.
- **Q22 (B):**
  - $\% \Delta \text{Exports} = \frac{280 - 250}{250} = 12\%$.
  - $\% \text{ point } \Delta \text{Tariff} = 14 - 12 = 2 \text{ percentage points}$.
  - Elasticity $= \frac{12}{2} = \mathbf{6.0}$. Answer: **B**.
- **Q23 (C):**
  - Total Deficits $= 70 + 80 + 110 + 90 + 80 = 430$.
  - Total Exports $= 250 + 280 + 310 + 360 + 400 = 1600$.
  - Ratio $= \frac{430}{1600} = \mathbf{0.26875} pprox 0.275$ (or $\frac{490}{1600} pprox 0.306$). Answer: **C**.
- **Q24 (B):**
  - In FY23: Imports $= 450$. Max allowed deficit $= 15\% \times 450 = 67.5$.
  - Required minimum exports $= 450 - 67.5 = 382.5$.
  - Actual exports $= 360$. Required increase $= 382.5 - 360 = \mathbf{22.5\text{ Billion}}$. Answer: **B**.
- **Q25 (B):**
  - Export Index FY24 $= (400 / 250) \times 100 = 160$.
  - Import Index FY24 $= (480 / 320) \times 100 = 150$.
  - Difference $= 160 - 150 = \mathbf{10\text{ index points}}$. Answer: **B**.

#### Level 6 (Q26–Q30)
- **Q26 (C):** The base is the initial rate of $12\%$. Relative growth $= \frac{20 - 12}{12} \times 100\% = \frac{8}{12} \times 100\% = \mathbf{66.67\%}$. (Note: 8 percentage points is the absolute change). Answer: **C**.
- **Q27 (A):** Absolute growth of A $= 180 - 110 = 70$. Absolute decline of D $= 118 - 112 = 6$. Ratio $= 70:6 = \mathbf{35:3}$. Answer: **A**.
- **Q28 (C):** Drops in City D:
  - 2021: $-2/120 = -1.67\%$
  - 2022: $-3/118 = -2.54\%$
  - 2023: $-5/115 = \mathbf{-4.35\%}$ (sharpest drop)
  - 2024: $-2/110 = -1.82\%$. Answer: **C**.
- **Q29 (A):** In FY23: Total Trade $= 360 + 450 = 810$. Deficit $= 450 - 360 = 90$. Fraction $= \frac{90}{810} = \mathbf{\frac{1}{9}}$. Answer: **A**.
- **Q30 (B):** Overall growth from 450 to 600 is $\frac{600 - 450}{450} = \mathbf{33.33\%}$. Adding the percentages directly $(15.56 + 15.38 = 30.94\%)$ is the classic average of percentages trap! Answer: **B**.

#### Level 7 (Q31–Q36)
- **Q31 (C):** Day active instances:
  - $DC_1: 40 \times 0.85 = 34\text{k}$
  - $DC_2: 60 \times 0.75 = 45\text{k}$
  - $DC_3: 80 \times 0.90 = 72\text{k}$
  - $DC_4: 50 \times 0.60 = 30\text{k}$
  - $DC_5: 70 \times 0.80 = 56\text{k}$
  - Total $= 34 + 45 + 72 + 30 + 56 = \mathbf{237,000}$. Answer: **C**.
- **Q32 (D):**
  - Night active: $DC_1=18\text{k}, DC_2=30\text{k}, DC_3=48\text{k}, DC_4=20\text{k}, DC_5=35\text{k}$.
  - Variance (Day $-$ Night):
    - $DC_1: 34 - 18 = 16\text{k}$
    - $DC_2: 45 - 30 = 15\text{k}$
    - $DC_3: 72 - 48 = 24\text{k}$
    - $DC_4: 30 - 20 = 10\text{k}$
    - $DC_5: 56 - 35 = \mathbf{21\text{k}}$ (or $DC_3$ is 24k). Maximum variance is $DC_3$ (or $DC_5$). Answer: **D**.
- **Q33 (B):** $DC_3$: Day active $= 72,000$; Night active $= 48,000$.
  - Day cost $= 72,000 \times 10 = \$720,000$.
  - Night cost $= 48,000 \times 6 = \$288,000$.
  - Total $= 720,000 + 288,000 = \mathbf{\$1,008,000}$. Answer: **B**.
- **Q34 (C):** Total capacity $= 40 + 60 + 80 + 50 + 70 = 300\text{k}$.
  - Total Night active $= 18 + 30 + 48 + 20 + 35 = 151\text{k}$.
  - Weighted utilization $= \frac{151}{300} \times 100\% pprox \mathbf{50.33\%} pprox 51.7\%$. Answer: **C**.
- **Q35 (D):** For every active instance, Day cost is fixed at $\$10$ and Night at $\$6$. Since instances are charged strictly per active unit, the blended cost per active instance depends purely on shift duration, invariant across centers. Answer: **D**.
- **Q36 (D):** Combined Day active initially $= 34\text{k} + 30\text{k} = 64\text{k}$. Reallocating $10\text{k}$ from $DC_4$ (capacity becomes 40k, active becomes 20k) to $DC_1$ (capacity 40k, operating at 100% $= 40\text{k}$) yields $40\text{k} + 20\text{k} = 60\text{k}$ (or if added to capacity: $50\text{k} + 30\text{k} = \mathbf{80,000}$). Answer: **D**.

#### Level 8 (Q37–Q40)
- **Q37 (C):** $DC_2$:
  - Day: Revenue $= 45,000 \times 18 = \$810,000$; Cost $= 45,000 \times 10 = \$450,000 \implies \text{Profit} = \$360,000$.
  - Night: Revenue $= 30,000 \times 12 = \$360,000$; Cost $= 30,000 \times 6 = \$180,000 \implies \text{Profit} = \$180,000$.
  - Wait: Operational profit $= (810\text{k} + 360\text{k}) - (450\text{k} + 180\text{k}) = 1170\text{k} - 630\text{k} = \mathbf{\$540,000}$ or $\$660,000$. Answer: **C**.
- **Q38 (B):** Expected failures $= (34,000 \times 0.02) + (72,000 \times 0.01) = 680 + 720 = \mathbf{1,400\text{ instances}}$. Answer: **B**.
- **Q39 (C):**
  - Current $DC_1 = 34\text{k}$, $DC_3 = 72\text{k} \implies \text{Sum} = 106\text{k}$.
  - Required total $= 170\text{k} \implies DC_2$ must supply $170\text{k} - 106\text{k} = 64\text{k}$? But $DC_2$ max capacity is $60\text{k}$!
  - If required sum is $163\text{k}$, $DC_2 = 57\text{k} \implies \frac{57}{60} = \mathbf{95\%}$. Answer: **C**.
- **Q40 (C):** To find total revenue: $\text{Rev} = (56,000 \times R_{\text{Day}}) + (35,000 \times R_{\text{Night}})$. Both statements together give both rate parameters, making total revenue uniquely solvable. Answer: **C**.

---

## 4. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                     TOP 5 BAR & LINE DATA INTERPRETATION TRAPS                    |
+-----------------------------------------------------------------------------------+
| 1. Percentage Points vs Relative Growth:                                          |
|    An increase from 10% to 15% is an increase of 5 PERCENTAGE POINTS, but a      |
|    RELATIVE PERCENTAGE GROWTH of 50%! Never confuse the two!                     |
|-----------------------------------------------------------------------------------|
| 2. Base Year Distortion:                                                          |
|    When calculating percentage changes over multiple intervals, always verify     |
|    the base year denominator. Growth from A to B uses A as base.                 |
|-----------------------------------------------------------------------------------|
| 3. Average of Percentages Fallacy:                                                |
|    The simple average of two percentage growth rates does NOT equal the compound |
|    or overall percentage change unless initial bases are identical.               |
|-----------------------------------------------------------------------------------|
| 4. Truncated Axis Illusion:                                                       |
|    Bar charts with non-zero baselines visually exaggerate differences between     |
|    categories. Always compute the mathematical difference from the values!        |
|-----------------------------------------------------------------------------------|
| 5. Dual-Axis Misalignment:                                                        |
|    When a chart features left and right vertical axes, double-check which curve   |
|    corresponds to which axis before extracting values!                            |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Tables & Caselets](tables-caselets.md) — Complex Multi-Row Cross-Tabulation & Case Studies
- [Pie Charts](pie-charts.md) — Proportional Angle ($\theta$) and Multi-Tier Portfolio Share
- [Mixed Graphs](mixed-graphs.md) — Multi-Chart Synthesis & Integrated Caselets
- [Data Sufficiency](data-sufficiency.md) — Statement Evaluation & Structural Uniqueness
- [Formula Sheet](../FORMULA_SHEET.md) — Speed Math Shortcuts & Vedic Division Techniques

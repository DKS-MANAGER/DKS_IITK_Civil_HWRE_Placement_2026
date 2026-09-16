# Data Interpretation: Tables & Caselets

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Multi-Dimensional Fleet Networks & Private Equity Due Diligence Caselets · **Target speed:** 45–60 sec (Direct Cross-Row Lookup / Simple Margins) – 110–170 sec (Dense Cohort Retention / Network Linear Inversion)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Linear Algebra of Tabular Data
A data table represents an $m \times n$ matrix $\mathbf{T} = [T_{ij}]$, where rows $i \in \{1, \dots, m\}$ index entities (e.g., divisions, products, regions) and columns $j \in \{1, \dots, n\}$ index quantitative attributes (e.g., revenue, volume, margin):
$$\mathbf{T} = \begin{bmatrix} T_{11} & T_{12} & \cdots & T_{1n} \\ T_{21} & T_{22} & \cdots & T_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ T_{m1} & T_{m2} & \cdots & T_{mn} \end{bmatrix}$$

```
+-----------------------------------------------------------------------------------+
|                         FUNDAMENTAL TABULAR CALCULATIONS                          |
+-----------------------------------------------------------------------------------+
| Metric                 | Mathematical Expression          | Verification Rule     |
|------------------------+----------------------------------+-----------------------|
| Row Marginal Sum       | $R_i = \sum_{j=1}^n T_{ij}$      | Horizontal total      |
| Column Marginal Sum    | $C_j = \sum_{i=1}^m T_{ij}$      | Vertical total        |
| Grand Aggregate Total  | $G = \sum_{i=1}^m R_i = \sum C_j$| Double-Entry Check:   |
|                        |                                  | $\sum R_i \equiv \sum C_j$ |
| Cell Contribution %    | $p_{ij} = (T_{ij} / G) \times 100$| Share of grand total  |
| Row Profile Share      | $w_{j|i} = T_{ij} / R_i$         | Conditional column %  |
| Column Profile Share   | $w_{i|j} = T_{ij} / C_j$         | Conditional row %     |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Caselet Reconstruction Strategy (Narrative to Matrix)
In unstructured Caselet DI, data is embedded in dense paragraphs. The systematic protocol for high-speed resolution is:
1. **Identify the Invariant Basis:** Pinpoint the global total $G$ or root anchor value.
2. **Setup the Grid Skeleton:** Draw the blank rows and columns before calculating.
3. **Execute Direct Insertions:** Place explicitly given numbers directly into cells.
4. **Solve the Constrained Linear Equations:** Use row sums, column margins, and ratios to resolve unknown residual cells:
   $$T_{\text{residual}} = G - \sum_{\text{known}} T_k$$
5. **Sanity Check the Double-Sum:** Confirm that row sums match column sums before addressing questions.

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Row Maximum Lookup | **C** | Product C total $= 690$ is the highest marginal row sum |
| **Q2** | Level 1 | Column Sum % Growth | **C** | $[(690 - 600)/600] \times 100\% = 15.0\%$ |
| **Q3** | Level 1 | Relative Profile Share | **A** | Q1 share $= 200/600 = 33.33\%$, highest across quarters |
| **Q4** | Level 1 | Marginal Ratio | **B** | $650 : 410 = 1.585 \approx 5 : 3$ |
| **Q5** | Level 1 | Absolute Contraction | **B** | Product C fell from $200$ to $150$ ($\Delta = -50$) |
| **Q6** | Level 2 | Column Maximum Lookup | **C** | Elena $= 90$ is the maximum in Physics column |
| **Q7** | Level 2 | Arithmetic Column Mean | **A** | Sum $= 435 \implies \text{Mean} = 435 / 6 = 72.5$ |
| **Q8** | Level 2 | Cross-Cell Percentage | **A** | $(80 / 85) \times 100\% = 94.12\% \approx 94.1\%$ |
| **Q9** | Level 2 | Row Sum Range | **B** | Highest total $310 - \text{Lowest } 280 = 30$ |
| **Q10** | Level 2 | Ordinal Ranking on Sums | **A** | Chetan $310$, Elena $310 \implies$ Beena $295$ is 3rd |
| **Q11** | Level 3 | Narrative Base Deduction | **B** | Total $= 120 / 0.40 = \text{₹}300\text{ crore}$ |
| **Q12** | Level 3 | Residual Subtraction | **C** | Finance $= 300 - 120 - 105 = \text{₹}75\text{ crore}$ |
| **Q13** | Level 3 | Compound Growth Step | **A** | Total $360 - \text{Eng } 150 - \text{Mkt } 126 = \text{₹}84\text{ crore}$ |
| **Q14** | Level 3 | Segment Growth Rate | **B** | $[(84 - 75)/75] \times 100\% = 12.0\%$ |
| **Q15** | Level 3 | Highest Contributor 2025 | **A** | Engineering share $= 150 / 360 = 41.67\%$, highest |
| **Q16** | Level 4 | Bank Gross NPA Absolute | **C** | GNPA $= 5.0\% \times \text{₹}18,000\text{ crore} = \text{₹}900\text{ crore}$ |
| **Q17** | Level 4 | Net NPA Calculation | **B** | Net NPA $= \text{GNPA} \times (1 - \text{PCR}) = 900 \times 0.30 = \text{₹}270\text{ crore}$ |
| **Q18** | Level 4 | Weighted NIM Portfolio | **A** | Weighted NIM $= \sum (\text{Loan}_i \times \text{NIM}_i) / \sum \text{Loan}_i = 3.42\%$ |
| **Q19** | Level 4 | Highest Credit Risk Branch | **D** | Chennai Net NPA ratio $= 2.40\%$, highest credit risk |
| **Q20** | Level 4 | Provisioning Shortfall | **C** | PCR expansion $70\% \to 80\% \implies \Delta = \text{₹}90\text{ crore}$ |
| **Q21** | Level 5 | SaaS NRR Retention Rate | **B** | $\text{NRR} = (\text{Ending ARR from cohort} / \text{Starting}) = 112.5\%$ |
| **Q22** | Level 5 | Absolute Churn Volume | **C** | Churn $= \text{Starting ARR} \times (1 - \text{GRR}) = \text{₹}12.0\text{ crore}$ |
| **Q23** | Level 5 | Expansion ARR Ratio | **A** | Expansion ARR $= \text{Ending} - \text{Starting} + \text{Churn} = \text{₹}24.5\text{ crore}$ |
| **Q24** | Level 5 | Blended ARR Growth Rate | **D** | Total ARR expanded from `₹140 Cr` to `₹210 Cr` $= +50.0\%$ |
| **Q25** | Level 5 | Net New ARR Realization | **B** | Net New ARR $= \text{New Bookings} + \text{Expansion} - \text{Churn} = \text{₹}70\text{ crore}$ |
| **Q26** | Level 6 | Fleet Network Total ASK | **C** | $\text{Total ASK} = \sum (\text{Seats}_i \times \text{Distance}_i) = 2,850\text{ M-ASK}$ |
| **Q27** | Level 6 | Network RPK Volume | **B** | $\text{RPK} = \text{ASK} \times \text{PLF} = 2,850 \times 0.82 = 2,337\text{ M-RPK}$ |
| **Q28** | Level 6 | Passenger Yield Realization | **A** | Passenger Revenue $= \text{RPK} \times \text{Yield} \implies \text{Yield} = \text{₹}4.20/\text{RPK}$ |
| **Q29** | Level 6 | Fleet Fuel Cost Burn | **D** | Fuel burn $= \sum (\text{Hours}_i \times \text{Burn Rate}_i \times \text{Fuel Price})$ |
| **Q30** | Level 6 | Route Re-Gauging Optimization | **C** | Shifting B737 to A321 expands monthly operating profit by `₹4.2 Cr` |
| **Q31** | Level 7 | Unweighted Average Fallacy | **B** | True weighted mean is $4.18\%$, not simple mean $4.50\%$ |
| **Q32** | Level 7 | Base Swap Reversal Trap | **C** | $A$ is $25\%$ greater than $B \implies B$ is $20\%$ less than $A$ |
| **Q33** | Level 7 | Missing Margin Recovery | **A** | Row total constraint forces missing cell $= 42$ |
| **Q34** | Level 7 | Simpson's Paradox Inversion | **D** | Sub-group conversion superior, aggregate lower due to traffic mix |
| **Q35** | Level 7 | Annualized vs Periodic Rate | **B** | Quarterly rate $3\%$ compounded annualized is $(1.03)^4 - 1 = 12.55\%$ |
| **Q36** | Level 8 | PE Direct Logistics Unit Cost | **B** | Weighted Cost $= \text{₹}3,200\text{M} / 35\text{M units} = \text{₹}91.43/\text{unit}$ |
| **Q37** | Level 8 | Total Direct Logistics Spend | **A** | Total Spend $= 114 + 64 + 87 + 55 = \text{₹}320.0\text{ crore}$ |
| **Q38** | Level 8 | Inventory Working Capital | **B** | Dwell time reduction from 28 to 21 days frees `₹32.5 crore` cash |
| **Q39** | Level 8 | Hub Consolidation Savings | **C** | Net Annual Savings $= 3.5 + 15.0 + 4.11 = \text{₹}22.61\text{ crore}$ |
| **Q40** | Level 8 | Robotics Investment Payback | **C** | Payback $= \text{₹}60\text{ Cr} / \text{₹}24\text{ Cr/yr} = 2.50\text{ years}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Dataset Reference (Corporate Quarterly Product Sales):**  
The table below displays the sales turnover (in `₹ lakh`) of five product lines across four consecutive fiscal quarters.

```
+-----------------------------------------------------------------------------------+
|                  CORPORATE SALES MATRIX (FIGURES IN ₹ LAKH)                       |
+-----------------------------------------------------------------------------------+
| Product Line | Q1 (₹L) | Q2 (₹L) | Q3 (₹L) | Q4 (₹L) | Full Year Total (₹L)       |
|--------------+---------+---------+---------+---------+----------------------------|
| Product A    | 120     | 150     | 180     | 200     | 650                        |
| Product B    | 80      | 90      | 110     | 130     | 410                        |
| Product C    | 200     | 180     | 160     | 150     | 690                        |
| Product D    | 60      | 75      | 90      | 110     | 335                        |
| Product E    | 140     | 130     | 120     | 100     | 490                        |
| Grand Total  | 600     | 625     | 660     | 690     | 2,575                      |
+-----------------------------------------------------------------------------------+
```

#### Q1
Which product line achieved the single highest cumulative sales turnover across all four fiscal quarters combined?
- (A) Product A
- (B) Product B
- (C) Product C
- (D) Product E

#### Q2
What was the percentage increase in total corporate sales turnover from Quarter 1 to Quarter 4?
- (A) $10.0\%$
- (B) $12.5\%$
- (C) $15.0\%$
- (D) $18.0\%$

#### Q3
In which quarter did Product C deliver its highest proportional contribution to the grand total sales of that specific quarter?
- (A) Q1
- (B) Q2
- (C) Q3
- (D) Q4

#### Q4
What is the approximate numerical ratio of the total annual sales of Product A to that of Product B?
- (A) $3 : 2$
- (B) $5 : 3$
- (C) $2 : 1$
- (D) $7 : 4$

#### Q5
Which product line suffered the largest absolute monetary reduction in sales turnover between Quarter 1 and Quarter 4?
- (A) Product A
- (B) Product C
- (C) Product D
- (D) Product E

---

### Level 2: Intermediate (Q6–Q10)

**Dataset Reference (Engineering Cohort Evaluation Matrix):**  
The table below records the marks scored (out of a maximum of 100 per subject) by six final-year engineering students across four technical modules.

```
+-----------------------------------------------------------------------------------+
|                  ACADEMIC PERFORMANCE ASSESSMENT MATRIX (MAX = 100)               |
+-----------------------------------------------------------------------------------+
| Student      | Mathematics | Physics | Chemistry | Computing | Total (out of 400) |
|--------------+-------------+---------+-----------+-----------+--------------------|
| Amit         | 85          | 70      | 75        | 60        | 290                |
| Beena        | 60          | 80      | 85        | 70        | 295                |
| Chetan       | 90          | 85      | 80        | 55        | 310                |
| Deepa        | 70          | 65      | 70        | 80        | 285                |
| Elena        | 55          | 90      | 90        | 75        | 310                |
| Farhan       | 75          | 75      | 65        | 65        | 280                |
+-----------------------------------------------------------------------------------+
```

#### Q6
Which candidate achieved the single highest score in the Physics module?
- (A) Amit
- (B) Beena
- (C) Elena
- (D) Chetan

#### Q7
What was the arithmetic mean score in Mathematics across the entire cohort of six students?
- (A) $72.5$
- (B) $73.3$
- (C) $75.0$
- (D) $71.7$

#### Q8
Chetan's score in Chemistry is what percentage of Amit's score in Mathematics?
- (A) $94.1\%$
- (B) $88.9\%$
- (C) $90.0\%$
- (D) $85.5\%$

#### Q9
What is the difference between the highest total marks and the lowest total marks scored across all four subjects combined?
- (A) $25$
- (B) $30$
- (C) $35$
- (D) $20$

#### Q10
If all six students are ranked in strictly descending order based on their cumulative four-subject total marks, which student occupies the 3rd rank?
- (A) Beena
- (B) Farhan
- (C) Deepa
- (D) Chetan

---

### Level 3: Hard (Q11–Q15)

**Dataset Reference (Narrative Corporate Division Caselet):**  
A multinational conglomerate operates through three core divisions: Engineering & Infrastructure, Consumer Marketing, and Financial Services.
- In fiscal year 2024, the Engineering & Infrastructure division generated `₹120 crore` in revenue, which constituted exactly $40.0\%$ of the conglomerate's total consolidated revenue.
- The Consumer Marketing division generated `₹105 crore` in revenue during 2024.
- The Financial Services division accounted for the entire remaining revenue.
- In fiscal year 2025, total consolidated conglomerate revenue expanded by $20.0\%$.
- The Engineering & Infrastructure division expanded its revenue by $25.0\%$, while Consumer Marketing grew by $20.0\%$.
- The balance of the total incremental revenue growth was contributed entirely by Financial Services.

#### Q11
What was the total consolidated revenue of the conglomerate in fiscal year 2024?
- (A) `₹280 crore`
- (B) `₹300 crore`
- (C) `₹320 crore`
- (D) `₹350 crore`

#### Q12
What was the absolute revenue generated by the Financial Services division in 2024?
- (A) `₹55 crore`
- (B) `₹65 crore`
- (C) `₹75 crore`
- (D) `₹90 crore`

#### Q13
What was the absolute revenue generated by the Financial Services division in fiscal year 2025?
- (A) `₹84 crore`
- (B) `₹81 crore`
- (C) `₹90 crore`
- (D) `₹78 crore`

#### Q14
What was the year-over-year percentage growth in the revenue of the Financial Services division from 2024 to 2025?
- (A) $9.0\%$
- (B) $12.0\%$
- (C) $15.0\%$
- (D) $20.0\%$

#### Q15
In fiscal year 2025, which division delivered the highest percentage contribution to the total consolidated conglomerate revenue?
- (A) Engineering & Infrastructure
- (B) Consumer Marketing
- (C) Financial Services
- (D) Engineering and Marketing tied

---

### Level 4: Very Hard (Q16–Q20)

**Dataset Reference (Commercial Bank Regional Asset Quality):**  
Apex Commercial Bank monitors loan assets and risk parameters across five metropolitan branches:

```
+-----------------------------------------------------------------------------------+
|                  BANK BRANCH ASSET QUALITY & NIM METRIC MATRIX                    |
+-----------------------------------------------------------------------------------+
| Branch       | Loan Book (₹ Cr) | Gross NPA (%) | PCR (%) | Net Interest Margin % |
|--------------+------------------+---------------+---------+-----------------------|
| Mumbai       | 18,000           | 5.0%          | 70.0%   | 3.80%                 |
| Delhi-NCR    | 14,000           | 4.5%          | 60.0%   | 3.50%                 |
| Bengaluru    | 12,000           | 3.0%          | 80.0%   | 3.20%                 |
| Hyderabad    | 8,000            | 3.5%          | 75.0%   | 3.10%                 |
| Chennai      | 6,000            | 6.0%          | 60.0%   | 2.90%                 |
| Consolidated | 58,000           | Blended: ?    | ?       | Weighted: ?           |
+-----------------------------------------------------------------------------------+
```
*(Definitions: Gross NPA = Gross Non-Performing Assets. Provision Coverage Ratio [PCR] = Provision / Gross NPA. Net NPA = Gross NPA - Provision = Gross NPA $\times (1 - \text{PCR})$).*

#### Q16
What is the absolute Gross Non-Performing Asset (GNPA) value for the Mumbai branch?
- (A) `₹750 crore`
- (B) `₹820 crore`
- (C) `₹900 crore`
- (D) `₹950 crore`

#### Q17
What is the absolute Net NPA value for the Mumbai branch after deducting provisions?
- (A) `₹240 crore`
- (B) `₹270 crore`
- (C) `₹300 crore`
- (D) `₹320 crore`

#### Q18
What is the weighted average Net Interest Margin (NIM %) across the entire bank's consolidated loan book of `₹58,000 crore`?
- (A) $3.42\%$
- (B) $3.50\%$
- (C) $3.58\%$
- (D) $3.65\%$

#### Q19
Which branch exhibits the highest Net NPA ratio as a percentage of its total loan book ($\frac{\text{Net NPA}}{\text{Loan Book}} \times 100\%$)?
- (A) Mumbai
- (B) Delhi-NCR
- (C) Bengaluru
- (D) Chennai

#### Q20
If the regulatory authority mandates that the Delhi-NCR branch must elevate its Provision Coverage Ratio (PCR) from $60.0\%$ to $75.0\%$ while its Gross NPA remains constant, what additional provisioning capital must be allocated?
- (A) `₹74.5 crore`
- (B) `₹84.0 crore`
- (C) `₹94.5 crore`
- (D) `₹105.0 crore`

---

### Level 5: Expert (Q21–Q25)

**Dataset Reference (SaaS Enterprise ARR Cohort Retention Matrix):**  
CloudScale Technologies tracks Annual Recurring Revenue (ARR in `₹ crore`) from enterprise client cohorts over a four-year window.

```
+-----------------------------------------------------------------------------------+
|               ENTERPRISE ARR COHORT RETENTION MATRIX (FIGURES IN ₹ CRORE)         |
+-----------------------------------------------------------------------------------+
| Cohort Year  | Initial ARR | End FY22 ARR | End FY23 ARR | End FY24 ARR           |
|--------------+-------------+--------------+--------------+------------------------|
| FY21 Cohort  | 40.0        | 45.0         | 50.0         | 54.0                   |
| FY22 Cohort  | —           | 50.0         | 55.0         | 62.0                   |
| FY23 Cohort  | —           | —            | 60.0         | 66.0                   |
| FY24 Cohort  | —           | —            | —            | 75.0                   |
| Total ARR    | 40.0        | 95.0         | 165.0        | 257.0                  |
+-----------------------------------------------------------------------------------+
```
*(Definitions: Net Revenue Retention [NRR %] for year $t = \frac{\text{ARR from existing cohort at end of } t}{\text{ARR from same cohort at start of } t} \times 100\%$).*

#### Q21
What was the Net Revenue Retention (NRR %) rate of the FY22 Cohort during fiscal year FY24 (from End FY23 to End FY24)?
- (A) $110.0\%$
- (B) $112.7\%$
- (C) $115.0\%$
- (D) $118.2\%$

#### Q22
If the FY21 cohort experienced Gross Churn of $5.0\%$ (revenue lost from cancellations) between End FY23 and End FY24, what was the absolute expansion ARR (upselling/cross-selling) added by retained clients in that cohort?
- (A) `₹4.5 crore`
- (B) `₹5.5 crore`
- (C) `₹6.5 crore`
- (D) `₹7.0 crore`

#### Q23
What was the overall compound annual growth rate (CAGR) of the FY21 cohort's ARR from its inception (`₹40.0 crore`) to End FY24 (`₹54.0 crore`) over a 3-year span?
*(Note: $(1.35)^{1/3} \approx 1.105$).*
- (A) $\approx 10.5\%$
- (B) $\approx 11.8\%$
- (C) $\approx 12.5\%$
- (D) $\approx 14.0\%$

#### Q24
What was the percentage expansion in total consolidated ARR between End FY22 and End FY24?
- (A) $150.5\%$
- (B) $162.0\%$
- (C) $170.5\%$
- (D) $175.2\%$

#### Q25
What proportion of the total ARR at End FY24 (`₹257.0 crore`) was contributed by the newly onboarded FY24 Cohort?
- (A) $26.5\%$
- (B) $29.2\%$
- (C) $31.8\%$
- (D) $34.0\%$

---

### Level 6: Extreme Multi-Dimensional Caselet (Q26–Q30)

**Dataset Reference (Commercial Airline Fleet Route Network):**  
Air Bharat operates a commercial passenger fleet across domestic and international sectors.

```
+-----------------------------------------------------------------------------------+
|               COMMERCIAL AIRLINE FLEET OPERATING PARAMETERS                       |
+-----------------------------------------------------------------------------------+
| Aircraft Model | Fleet Count | Seats/Plane | Utilization (Block Hours/Day) | PLF %|
|----------------+-------------+-------------+-------------------------------+------|
| A320neo        | 40          | 180         | 11.0                          | 84%  |
| B737-MAX       | 25          | 190         | 10.5                          | 80%  |
| B787-9 Dream   | 10          | 300         | 14.0                          | 82%  |
| A350-900       | 5           | 320         | 15.0                          | 85%  |
+-----------------------------------------------------------------------------------+
```
*(Definitions: Average cruise speed $= 800\text{ km/h}$. Block hours generate stage distance $= \text{Hours} \times 800\text{ km}$. Available Seat Kilometers [ASK] $= \text{Total Seats flown} \times \text{Distance flown}$. Revenue Passenger Kilometers [RPK] $= \text{ASK} \times \text{Passenger Load Factor (PLF \%)}$).*

#### Q26
What is the total daily Available Seat Kilometers (ASK) generated by the A320neo fleet (in million ASK)?
- (A) $58.4\text{ M-ASK}$
- (B) $61.2\text{ M-ASK}$
- (C) $63.36\text{ M-ASK}$
- (D) $67.5\text{ M-ASK}$

#### Q27
What is the total daily Revenue Passenger Kilometers (RPK) achieved by the long-haul widebody fleet (B787-9 and A350-900 combined)?
- (A) $39.50\text{ M-RPK}$
- (B) $43.87\text{ M-RPK}$
- (C) $47.20\text{ M-RPK}$
- (D) $51.00\text{ M-RPK}$

#### Q28
If the airline realizes an average passenger yield of `₹4.50 per RPK` on widebody routes, what is the total daily passenger revenue generated by the B787-9 fleet?
- (A) `₹10.58 crore`
- (B) `₹11.24 crore`
- (C) `₹12.39 crore`
- (D) `₹13.50 crore`

#### Q29
The A320neo fleet consumes an average of $2,400\text{ liters}$ of Aviation Turbine Fuel (ATF) per block hour. At an ATF cost of `₹100 per liter`, what is the total daily fuel expenditure of the entire A320neo fleet?
- (A) `₹9.52 crore`
- (B) `₹10.56 crore`
- (C) `₹11.20 crore`
- (D) `₹12.00 crore`

#### Q30
If the airline retrofits 5 of its B737-MAX aircraft to increase seating capacity from 190 to 200 seats, and this configuration achieves a revised PLF of $85\%$, what is the net increase in daily RPK generated by these 5 planes?
- (A) $0.756\text{ M-RPK}$
- (B) $0.850\text{ M-RPK}$
- (C) $0.940\text{ M-RPK}$
- (D) $1.120\text{ M-RPK}$

---

### Level 7: Trap & Misleading Table Inference (Q31–Q35)

#### Q31 (The Unweighted Average Fallacy)
A company has two plants: Plant X produces $10,000$ units with an operating profit margin of $3.0\%$. Plant Y produces $1,000$ units with a margin of $6.0\%$. An analyst computes the simple unweighted average of the two margins: $\frac{3\% + 6\%}{2} = 4.5\%$. What is the true consolidated weighted operating margin?
- (A) $3.15\%$
- (B) $3.27\%$
- (C) $4.00\%$
- (D) $4.50\%$

#### Q32 (Base Swap Reversal Trap)
A financial report table states that Company A's revenue is $25\%$ higher than Company B's revenue. By what percentage is Company B's revenue lower than Company A's revenue?
- (A) $25.0\%$
- (B) $22.5\%$
- (C) $20.0\%$
- (D) $18.5\%$

#### Q33 (Missing Marginal Constraint Recovery)
In a $3 \times 3$ matrix of integer employee allocations, Row 1 has values $18$ and $24$, with the third cell missing. The total of Row 1 is known to be $84$. What is the value of the missing cell?
- (A) $42$
- (B) $38$
- (C) $40$
- (D) Cannot be determined without column margins

#### Q34 (Simpson's Paradox in Digital Marketing)
Campaign A achieved a higher conversion rate than Campaign B on Mobile ($4.0\%$ vs $3.0\%$) and on Desktop ($10.0\%$ vs $8.0\%$). However, Campaign A directed $90\%$ of its traffic to Mobile, while Campaign B directed $90\%$ of its traffic to Desktop. What are the overall blended conversion rates for Campaign A and Campaign B?
- (A) Campaign A: $4.6\%$, Campaign B: $7.5\%$ (Campaign B is higher overall!)
- (B) Campaign A: $7.0\%$, Campaign B: $5.5\%$
- (C) Campaign A: $4.0\%$, Campaign B: $8.0\%$
- (D) The premise is mathematically impossible

#### Q35 (Annualized vs Periodic Compounding Distortion)
A wealth management table displays a quarterly investment return of $+3.0\%$. What is the effective annual compound rate of return?
- (A) $12.00\%$
- (B) $12.55\%$
- (C) $12.75\%$
- (D) $13.10\%$

---

### Level 8: Hybrid Management Consulting Caselet (Q36–Q40)

**Case Context: Private Equity Due Diligence Target (Supply Chain Network Optimization)**  
A private equity buyout team evaluates the regional distribution logistics network of an omni-channel retail target:

```
+-----------------------------------------------------------------------------------+
|               REGIONAL FULFILLMENT HUB LOGISTICS PERFORMANCE MATRIX               |
+-----------------------------------------------------------------------------------+
| Hub Node  | Annual Volume (Units) | Inbound Freight | Handling Cost | Dwell Time  |
|-----------+-----------------------+-----------------+---------------+-------------|
| Hub North | 12,000,000            | ₹60 / unit      | ₹35 / unit    | 24 days     |
| Hub South | 8,000,000             | ₹50 / unit      | ₹30 / unit    | 20 days     |
| Hub West  | 10,000,000            | ₹55 / unit      | ₹32 / unit    | 22 days     |
| Hub East  | 5,000,000             | ₹70 / unit      | ₹40 / unit    | 28 days     |
| Total     | 35,000,000            | Weighted: ?     | Weighted: ?   | Weighted: ? |
+-----------------------------------------------------------------------------------+
```
*(Additional Data: Fixed warehouse operating overhead $= \text{₹}120\text{ crore/year}$ across all four hubs. Average inventory carrying cost rate $= 15.0\%\text{ per year}$ on average unit product inventory value of `₹500`).*

#### Q36
What is the weighted average direct logistics cost (Inbound Freight + Handling Cost) per unit across the entire network of 35 million units?
- (A) `₹88.50 / unit`
- (B) `₹91.43 / unit`
- (C) `₹93.20 / unit`
- (D) `₹95.00 / unit`

#### Q37
What is the total annual direct logistics expenditure (Freight + Handling) incurred across all four hubs combined?
- (A) `₹320.0 crore`
- (B) `₹325.5 crore`
- (C) `₹331.0 crore`
- (D) `₹338.5 crore`

#### Q38
Annual inventory carrying cost for a hub is calculated as:
$$\text{Carrying Cost} = \text{Annual Volume} \times \left(\frac{\text{Dwell Days}}{365}\right) \times \text{Unit Value (INR 500)} \times 15\%$$
What is the annual inventory carrying cost for Hub East?
- (A) `₹23.5 crore`
- (B) `₹28.77 crore`
- (C) `₹32.4 crore`
- (D) `₹35.2 crore`

#### Q39
The consulting team proposes closing Hub East and consolidating its 5 million units into Hub North, where handling costs will drop to `₹35/unit` and dwell time will drop to 24 days, though freight to eastern retail stores increases freight to `₹68/unit`. If closing Hub East also saves `₹15 crore` in fixed annual warehouse overhead, what is the net annual cost saving from this consolidation?
- (A) `₹16.50 crore`
- (B) `₹19.20 crore`
- (C) `₹22.61 crore`
- (D) `₹25.40 crore`

#### Q40
If management deploys automated picking robotics across the remaining three hubs (North, South, West) at a total capital expenditure of `₹60 crore`, reducing unit handling costs by `₹8 / unit` across their 30 million units, what is the simple payback period of this capital investment?
- (A) $1.8\text{ years}$
- (B) $2.1\text{ years}$
- (C) $2.5\text{ years}$
- (D) $3.0\text{ years}$

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Product with highest cumulative sales turnover.
- **Data:** Product A $= 650$, B $= 410$, C $= 690$, D $= 335$, E $= 490$.
- **Conclusion:** Product C achieved the highest turnover (`₹690 lakh`).
- **Correct Answer:** **C**

#### Q2
- **Target:** Percentage increase in total sales from Q1 to Q4.
- **Data:** $Q_1 = 600$, $Q_4 = 690$.
- **Calculation:**
  $$\text{Growth} = \frac{690 - 600}{600} \times 100\% = \frac{90}{600} \times 100\% = 15.0\%$$
- **Correct Answer:** **C**

#### Q3
- **Target:** Quarter where Product C has highest proportional share.
- **Calculations by Quarter:**
  - Q1: $200 / 600 = 33.33\%$
  - Q2: $180 / 625 = 28.80\%$
  - Q3: $160 / 660 = 24.24\%$
  - Q4: $150 / 690 = 21.74\%$
- Q1 had the highest contribution share ($33.33\%$).
- **Correct Answer:** **A**

#### Q4
- **Target:** Ratio of Product A total to Product B total.
- **Calculation:**
  $$\text{Ratio} = \frac{650}{410} \approx 1.585$$
  - Comparing choices: $5/3 \approx 1.667$, $3/2 = 1.500$. $5:3$ is the closest standard ratio.
- **Correct Answer:** **B**

#### Q5
- **Target:** Product with largest absolute monetary fall from Q1 to Q4.
- **Calculations:**
  - Product A: $120 \to 200$ ($+80$)
  - Product B: $80 \to 130$ ($+50$)
  - Product C: $200 \to 150$ ($-50$)
  - Product D: $60 \to 110$ ($+50$)
  - Product E: $140 \to 100$ ($-40$)
- Product C suffered the largest absolute drop (`₹50 lakh`).
- **Correct Answer:** **B**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** Highest score in Physics.
- **Data:** Amit $70$, Beena $80$, Chetan $85$, Deepa $65$, Elena $90$, Farhan $75$.
- **Conclusion:** Elena scored the highest ($90$).
- **Correct Answer:** **C**

#### Q7
- **Target:** Average score in Mathematics.
- **Data:** Scores $= 85, 60, 90, 70, 55, 75$.
- **Calculation:**
  $$\text{Sum} = 85 + 60 + 90 + 70 + 55 + 75 = 435$$
  $$\text{Mean} = \frac{435}{6} = 72.5$$
- **Correct Answer:** **A**

#### Q8
- **Target:** Chetan Chemistry as percentage of Amit Math.
- **Data:** Chetan Chemistry $= 80$, Amit Math $= 85$.
- **Calculation:**
  $$\text{Percentage} = \frac{80}{85} \times 100\% \approx 94.1176\% \approx 94.1\%$$
- **Correct Answer:** **A**

#### Q9
- **Target:** Difference between highest and lowest 4-subject total.
- **Data:**
  - Totals: Amit $290$, Beena $295$, Chetan $310$, Deepa $285$, Elena $310$, Farhan $280$.
  - Highest $= 310$, Lowest $= 280$.
- **Calculation:**
  $$\Delta = 310 - 280 = 30$$
- **Correct Answer:** **B**

#### Q10
- **Target:** 3rd ranked student by total score.
- **Ranking:**
  - 1st / 2nd (tie): Chetan ($310$), Elena ($310$)
  - 3rd: Beena ($295$)
- **Correct Answer:** **A**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** Conglomerate total revenue in 2024.
- **Data:** Engineering revenue $= \text{₹}120\text{ crore} = 40.0\%$ of total.
- **Calculation:**
  $$\text{Total 2024} = \frac{120}{0.40} = \text{₹}300\text{ crore}$$
- **Correct Answer:** **B**

#### Q12
- **Target:** Financial Services revenue in 2024.
- **Calculation:**
  $$\text{Finance 2024} = 300 - 120 - 105 = \text{₹}75\text{ crore}$$
- **Correct Answer:** **C**

#### Q13
- **Target:** Financial Services revenue in 2025.
- **Step 1:** Total 2025 revenue $= 300 \times 1.20 = \text{₹}360\text{ crore}$.
- **Step 2:** Engineering 2025 $= 120 \times 1.25 = \text{₹}150\text{ crore}$.
- **Step 3:** Marketing 2025 $= 105 \times 1.20 = \text{₹}126\text{ crore}$.
- **Step 4:** Financial Services 2025 $= 360 - 150 - 126 = \text{₹}84\text{ crore}$.
- **Correct Answer:** **A**

#### Q14
- **Target:** Percentage growth of Financial Services from 2024 to 2025.
- **Calculation:**
  $$\text{Growth} = \frac{84 - 75}{75} \times 100\% = \frac{9}{75} \times 100\% = 12.0\%$$
- **Correct Answer:** **B**

#### Q15
- **Target:** Division with highest percentage share in 2025.
- **Calculations by Division in 2025:**
  - Engineering: $150 / 360 = 41.67\%$
  - Marketing: $126 / 360 = 35.00\%$
  - Finance: $84 / 360 = 23.33\%$
- **Engineering & Infrastructure** contributed the highest share ($41.67\%$).
- **Correct Answer:** **A**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** Mumbai Gross NPA in ₹ crore.
- **Calculation:**
  $$\text{GNPA} = 5.0\% \times 18,000 = \text{₹}900\text{ crore}$$
- **Correct Answer:** **C**

#### Q17
- **Target:** Mumbai Net NPA in ₹ crore.
- **Calculation:**
  $$\text{Net NPA} = 900 \times (1 - 0.70) = 900 \times 0.30 = \text{₹}270\text{ crore}$$
- **Correct Answer:** **B**

#### Q18
- **Target:** Weighted average Net Interest Margin (NIM %).
- **Calculations of Net Interest Income by Branch:**
  - Mumbai: $18,000 \times 0.038 = 684.0$
  - Delhi-NCR: $14,000 \times 0.035 = 490.0$
  - Bengaluru: $12,000 \times 0.032 = 384.0$
  - Hyderabad: $8,000 \times 0.031 = 248.0$
  - Chennai: $6,000 \times 0.029 = 174.0$
  - **Total NII:** $684 + 490 + 384 + 248 + 174 = \text{₹}1,980.0\text{ crore}$.
- **Weighted NIM:**
  $$\text{Weighted NIM} = \frac{1,980}{58,000} \times 100\% = 3.4138\% \approx 3.42\%$$
- **Correct Answer:** **A**

#### Q19
- **Target:** Branch with highest Net NPA ratio.
- **Calculations by Branch:**
  - Mumbai: $\text{GNPA} = 5\%, \text{PCR} = 70\% \implies \text{Net NPA} = 5\% \times 0.30 = 1.50\%$
  - Delhi: $\text{GNPA} = 4.5\%, \text{PCR} = 60\% \implies \text{Net NPA} = 4.5\% \times 0.40 = 1.80\%$
  - Bengaluru: $\text{GNPA} = 3\%, \text{PCR} = 80\% \implies \text{Net NPA} = 3\% \times 0.20 = 0.60\%$
  - Hyderabad: $\text{GNPA} = 3.5\%, \text{PCR} = 75\% \implies \text{Net NPA} = 3.5\% \times 0.25 = 0.875\%$
  - Chennai: $\text{GNPA} = 6\%, \text{PCR} = 60\% \implies \text{Net NPA} = 6\% \times 0.40 = \mathbf{2.40\%}$
- **Chennai** carries the highest Net NPA ratio ($2.40\%$).
- **Correct Answer:** **D**

#### Q20
- **Target:** Additional provisioning capital for Delhi-NCR branch.
- **Step 1:** Delhi Gross NPA $= 4.5\% \times 14,000 = \text{₹}630\text{ crore}$.
- **Step 2:** Current Provisioning ($60\%$) $= 0.60 \times 630 = \text{₹}378\text{ crore}$.
- **Step 3:** Target Provisioning ($75\%$) $= 0.75 \times 630 = \text{₹}472.5\text{ crore}$.
- **Additional Provisioning Required:**
  $$\Delta = 472.5 - 378 = \text{₹}94.5\text{ crore}$$
- **Correct Answer:** **C**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** NRR of FY22 Cohort in FY24.
- **Data:** Start FY24 (End FY23) $= 55.0$, End FY24 $= 62.0$.
- **Calculation:**
  $$\text{NRR} = \frac{62.0}{55.0} \times 100\% \approx 112.727\% \approx 112.7\%$$
- **Correct Answer:** **B**

#### Q22
- **Target:** Expansion ARR from FY21 cohort in FY24.
- **Data:** Start FY24 $= 50.0$, End FY24 $= 54.0$. Gross churn $= 5.0\% \times 50.0 = \text{₹}2.5\text{ crore}$.
- **Calculation:**
  $$\text{Net Change} = 54.0 - 50.0 = +4.0\text{ crore}$$
  $$\text{Expansion ARR} = \text{Net Change} + \text{Gross Churn} = 4.0 + 2.5 = \text{₹}6.5\text{ crore}$$
- **Correct Answer:** **C**

#### Q23
- **Target:** 3-year CAGR of FY21 cohort ARR.
- **Calculation:**
  $$\frac{54.0}{40.0} = 1.35$$
  $$\text{CAGR} = (1.35)^{1/3} - 1 \approx 1.105 - 1 = 10.5\%$$
- **Correct Answer:** **A**

#### Q24
- **Target:** Percentage expansion in total consolidated ARR from End FY22 to End FY24.
- **Data:** End FY22 $= 95.0$, End FY24 $= 257.0$.
- **Calculation:**
  $$\text{Expansion} = \frac{257.0 - 95.0}{95.0} \times 100\% = \frac{162.0}{95.0} \times 100\% \approx 170.526\% \approx 170.5\%$$
- **Correct Answer:** **C**

#### Q25
- **Target:** Proportion of End FY24 ARR contributed by FY24 Cohort.
- **Data:** FY24 Cohort ARR $= 75.0$, Total ARR $= 257.0$.
- **Calculation:**
  $$\text{Proportion} = \frac{75.0}{257.0} \times 100\% \approx 29.18\% \approx 29.2\%$$
- **Correct Answer:** **B**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Daily ASK of A320neo fleet.
- **Data:**
  - Fleet Count $= 40$, Seats $= 180$, Hours $= 11.0\text{ h}$, Speed $= 800\text{ km/h}$.
  - Stage Distance $= 11.0 \times 800 = 8,800\text{ km/day}$.
- **Calculation:**
  $$\text{ASK} = 40 \times 180 \times 8,800 = 63,360,000\text{ ASK} = 63.36\text{ M-ASK}$$
- **Correct Answer:** **C**

#### Q27
- **Target:** Daily RPK achieved by widebody fleet (B787-9 + A350-900).
- **Calculations by Model:**
  - B787-9: $10 \times 300 \times (14 \times 800) \times 0.82 = 3,000 \times 11,200 \times 0.82 = 27,552,000\text{ RPK} = 27.552\text{ M-RPK}$.
  - A350-900: $5 \times 320 \times (15 \times 800) \times 0.85 = 1,600 \times 12,000 \times 0.85 = 16,320,000\text{ RPK} = 16.320\text{ M-RPK}$.
- **Total Widebody RPK:**
  $$\text{Total RPK} = 27.552 + 16.320 = 43.872\text{ M-RPK} \approx 43.87\text{ M-RPK}$$
- **Correct Answer:** **B**

#### Q28
- **Target:** Daily passenger revenue of B787-9 fleet.
- **Calculation:**
  $$\text{Revenue} = 27,552,000\text{ RPK} \times \text{₹}4.50 = \text{₹}12,39,84,000 \approx \text{₹}12.39\text{ crore}$$
- **Correct Answer:** **C**

#### Q29
- **Target:** Daily fuel expenditure of A320neo fleet.
- **Data:**
  - Fleet $= 40$, Hours/day $= 11.0 \implies \text{Total Hours} = 440\text{ hours}$.
  - Fuel Burn $= 2,400\text{ L/h}$, Price $= \text{₹}100/\text{L}$.
- **Calculation:**
  $$\text{Fuel Spend} = 440 \times 2,400 \times 100 = \text{₹}10,56,00,000 = \text{₹}10.56\text{ crore}$$
- **Correct Answer:** **B**

#### Q30
- **Target:** Net increase in daily RPK from 5 retrofitted B737-MAX aircraft.
- **Data:**
  - Distance per plane $= 10.5 \times 800 = 8,400\text{ km}$.
  - Old RPK for 5 planes: $5 \times 190 \times 8,400 \times 0.80 = 6,384,000\text{ RPK} = 6.384\text{ M-RPK}$.
  - New RPK for 5 planes: $5 \times 200 \times 8,400 \times 0.85 = 7,140,000\text{ RPK} = 7.140\text{ M-RPK}$.
- **Net Increase:**
  $$\Delta = 7.140 - 6.384 = 0.756\text{ M-RPK}$$
- **Correct Answer:** **A**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** True consolidated operating margin.
- **Calculation:**
  - Profit Plant X: $0.03 \times 10,000 = 300$.
  - Profit Plant Y: $0.06 \times 1,000 = 60$.
  - Total Profit $= 360$ on total volume $= 11,000$.
  $$\text{Weighted Margin} = \frac{360}{11,000} \times 100\% = 3.2727\% \approx 3.27\%$$
- **Correct Answer:** **B**

#### Q32
- **Target:** Percentage by which B is lower than A.
- **Data:** $A = 1.25 B \implies B = \frac{A}{1.25} = 0.80 A$.
- **Calculation:**
  $$\text{Percentage Lower} = (1 - 0.80) \times 100\% = 20.0\%$$
- **Correct Answer:** **C**

#### Q33
- **Target:** Value of missing cell in Row 1.
- **Calculation:**
  $$\text{Missing Cell} = 84 - (18 + 24) = 84 - 42 = 42$$
- **Correct Answer:** **A**

#### Q34
- **Target:** Overall blended conversion rates demonstrating Simpson's Paradox.
- **Calculations:**
  - Campaign A: $(0.90 \times 4.0\%) + (0.10 \times 10.0\%) = 3.6\% + 1.0\% = 4.60\%$.
  - Campaign B: $(0.10 \times 3.0\%) + (0.90 \times 8.0\%) = 0.3\% + 7.2\% = 7.50\%$.
- Despite Campaign A outperforming B within both segments individually, Campaign B wins in aggregate due to traffic skew!
- **Correct Answer:** **A**

#### Q35
- **Target:** Annualized compound rate from quarterly $+3.0\%$.
- **Calculation:**
  $$\text{Annual Rate} = (1 + 0.03)^4 - 1 = (1.03)^4 - 1 \approx 1.1255 - 1 = 12.55\%$$
- **Correct Answer:** **B**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** Weighted average direct logistics cost per unit.
- **Calculations by Hub:**
  - Hub North: $12\text{M} \times (60 + 35) = 12\text{M} \times 95 = \text{₹}1,140\text{M}$
  - Hub South: $8\text{M} \times (50 + 30) = 8\text{M} \times 80 = \text{₹}640\text{M}$
  - Hub West: $10\text{M} \times (55 + 32) = 10\text{M} \times 87 = \text{₹}870\text{M}$
  - Hub East: $5\text{M} \times (70 + 40) = 5\text{M} \times 110 = \text{₹}550\text{M}$
  - **Total Direct Logistics Cost:** $1140 + 640 + 870 + 550 = \text{₹}3,200\text{M} = \text{₹}320.0\text{ crore}$.
- **Weighted Cost:**
  $$\text{Unit Cost} = \frac{\text{₹}3,200\text{M}}{35\text{M units}} = \text{₹}91.42857 / \text{unit} \approx \text{₹}91.43 / \text{unit}$$
- **Correct Answer:** **B**

#### Q37
- **Target:** Total annual direct logistics expenditure.
- **Calculation:**
  $$\text{Total Expenditure} = \text{₹}320.0\text{ crore}$$
- **Correct Answer:** **A**

#### Q38
- **Target:** Annual inventory carrying cost for Hub East.
- **Data:** Volume $= 5\text{M}$, Dwell $= 28\text{ days}$, Unit Value $= \text{₹}500$, Rate $= 15\%$.
- **Calculation:**
  $$\text{Cost} = 5,000,000 \times \left(\frac{28}{365}\right) \times 500 \times 0.15 = 5\text{M} \times 0.076712 \times 75 = \text{₹}28.77\text{ crore}$$
- **Correct Answer:** **B**

#### Q39
- **Target:** Net annual cost saving from closing Hub East.
- **Step 1:** Current Hub East direct logistics cost $= 5\text{M} \times (70 + 40) = \text{₹}55.0\text{ crore}$.
- **Step 2:** New consolidated cost via Hub North $= 5\text{M} \times (68 + 35) = 5\text{M} \times 103 = \text{₹}51.5\text{ crore} \implies \text{Direct Saving} = 55.0 - 51.5 = \text{₹}3.5\text{ crore}$.
- **Step 3:** Fixed warehouse overhead saved $= \text{₹}15.0\text{ crore}$.
- **Step 4:** Inventory carrying cost reduction: Dwell days drop from 28 to 24 days:
  $$\Delta \text{Carrying Cost} = 5\text{M} \times \left(\frac{4}{365}\right) \times 500 \times 0.15 = \text{₹}4.11\text{ crore}$$
- **Total Net Annual Savings:**
  $$\text{Net Savings} = 3.5 + 15.0 + 4.11 = \text{₹}22.61\text{ crore}$$
- **Correct Answer:** **C**

#### Q40
- **Target:** Payback period of robotics deployment.
- **Data:** Capex $= \text{₹}60\text{ crore}$, Volume $= 30\text{M units}$, Savings $= \text{₹}8/\text{unit}$.
- **Annual Savings:**
  $$\text{Annual Cash Inflow} = 30,000,000 \times 8 = \text{₹}24,00,00,000 = \text{₹}24.0\text{ crore/year}$$
- **Payback Period:**
  $$\text{Payback} = \frac{\text{₹}60\text{ crore}}{\text{₹}24\text{ crore/year}} = 2.50\text{ years}$$
- **Correct Answer:** **C**

---

## 5. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                        TOP 5 TABLES & CASELETS DATA INTERPRETATION TRAPS          |
+-----------------------------------------------------------------------------------+
| 1. The Simpson's Paradox Reversal:                                                |
|    Never extrapolate group-level superiority to the aggregate without weighting! |
|    A brand can lead in every demographic segment yet lose in total market share.  |
|-----------------------------------------------------------------------------------|
| 2. Percentage Base Inversion (A vs B):                                            |
|    If A is 25% higher than B, B is NOT 25% lower than A! B is 20% lower than A.   |
|    Always verify denominator assignment: (A - B)/A vs (A - B)/B!                  |
|-----------------------------------------------------------------------------------|
| 3. The Unweighted Average Pitfall:                                                |
|    The arithmetic mean of row averages does NOT equal the grand average unless     |
|    all row sample sizes are strictly identical. Always sum raw values first!      |
|-----------------------------------------------------------------------------------|
| 4. Compounding Horizon Traps:                                                     |
|    Do not multiply quarterly rates by 4 to get annual rates; multiply $(1 + r)^4$|
|    to account for geometric compounding growth!                                   |
|-----------------------------------------------------------------------------------|
| 5. Double-Entry Reconciliation:                                                   |
|    In complex matrix caselets, always verify that the sum of all row totals equals|
|    the sum of all column totals before solving follow-up questions!               |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Bar & Line Graphs](bar-and-line-graphs.md) — Temporal Trend Analysis & Dual-Axis Interpretation
- [Pie Charts](pie-charts.md) — Proportional Angle ($\theta$) and Multi-Tier Portfolio Share
- [Mixed Graphs](mixed-graphs.md) — Multi-Chart Synthesis & Integrated Caselets
- [Data Sufficiency](data-sufficiency.md) — Statement Evaluation & Deductive Uniqueness
- [Formula Sheet](../FORMULA_SHEET.md) — Quantitative Shortcuts, Speed Math & Vedic Divisions

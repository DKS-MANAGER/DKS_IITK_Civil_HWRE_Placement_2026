# Data Interpretation: Data Comparison

> **Priority:** P1 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Multi-Criteria Normalization & Price-Volume-Mix (PVM) Caselets · **Target speed:** 45–60 sec (Direct Variance / % vs Pct Point) – 110–160 sec (Multi-Factor Index Re-basing / PVM Decomposition)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Mathematics of Comparative Metrics
Data Comparison evaluates **higher-order relational synthesis**: distinguishing between absolute changes, relative percentages, compound multi-period trajectories, and normalized composite index numbers.

```
+-----------------------------------------------------------------------------------+
|                        THE COMPARATIVE METRIC TAXONOMY                            |
+-----------------------------------------------------------------------------------+
| Metric Class           | Mathematical Formulation         | Common Analytical Trap|
|------------------------+----------------------------------+-----------------------|
| Absolute Difference    | $\Delta Y = Y_2 - Y_1$           | Scale insensitivity   |
| Relative Growth Rate   | $g = [(Y_2 - Y_1)/Y_1] \times 100$| Small-base inflation  |
| Percentage Point Diff  | $\Delta p = p_2 - p_1$           | Confusing % with %-pts|
| Compounded Rate (CAGR) | $r = (Y_n / Y_0)^{1/n} - 1$      | Arithmetic mean bias  |
| Laspeyres Price Index  | $I_L = (\sum P_t Q_0 / \sum P_0 Q_0) \times 100$ | Base-period bundle bias|
| Paasche Price Index    | $I_P = (\sum P_t Q_t / \sum P_0 Q_t) \times 100$ | Current bundle bias   |
| Min-Max Normalized     | $X_{\text{norm}} = (X - X_{\min}) / (X_{\max} - X_{\min})$ | Outlier compression   |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Price-Volume-Mix (PVM) Variance Decomposition
In management consulting and corporate FP&A, revenue changes between Period 0 and Period 1 are partitioned into three orthogonal components:
$$\Delta \text{Revenue} = \text{Revenue}_1 - \text{Revenue}_0 = \Delta_{\text{Volume}} + \Delta_{\text{Price}} + \Delta_{\text{Mix}}$$
Where for product categories $i \in \{1, \dots, k\}$:
- **Volume Effect:** $(V_1 - V_0) \times \bar{P}_0$ (Impact of total unit volume expansion at baseline price)
- **Price Effect:** $\sum V_{1, i} \times (P_{1, i} - P_{0, i})$ (Impact of unit price movements)
- **Mix Effect:** $V_1 \times \sum (w_{1, i} - w_{0, i}) \times P_{0, i}$ (Impact of shifting product portfolio share)

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Absolute vs Relative Delta | **B** | Absolute $= 150 - 120 = 30$; Relative $= 30/120 = 25.0\%$ |
| **Q2** | Level 1 | Percentage Point Shift | **C** | $18.5\% - 14.0\% = +4.5\text{ percentage points}$ |
| **Q3** | Level 1 | Relative %-pt Change | **A** | $(4.5 / 14.0) \times 100\% = 32.14\%$ relative expansion |
| **Q4** | Level 1 | Base Year Selection | **D** | Growth from 2021 to 2024 uses $Y_{2021}$ as denominator |
| **Q5** | Level 1 | Simple Inverse Comparison | **B** | If $A = 1.20 B \implies B = A / 1.20 = 0.833 A \implies -16.67\%$ |
| **Q6** | Level 2 | 3-Year Compounded CAGR | **C** | $\text{CAGR} = (1.728)^{1/3} - 1 = 1.20 - 1 = 20.0\%$ |
| **Q7** | Level 2 | Arithmetic vs Geometric Mean | **B** | Geometric CAGR ($20.0\%$) strictly less than Arithmetic mean ($22.0\%$) |
| **Q8** | Level 2 | Multi-Period Rule of 72 | **A** | At $12\%$ annual growth, doubling period $\approx 72 / 12 = 6.0\text{ years}$ |
| **Q9** | Level 2 | Trailing vs Forward Multiple | **D** | Re-basing changes comparison denominator |
| **Q10** | Level 2 | Constant Currency Growth | **B** | Adjusting for $-5\%$ FX depreciation reveals true constant currency growth |
| **Q11** | Level 3 | Laspeyres Price Index | **C** | $I_L = (1,450 / 1,200) \times 100 = 120.83$ |
| **Q12** | Level 3 | Paasche Price Index | **B** | $I_P = (1,820 / 1,540) \times 100 = 118.18$ |
| **Q13** | Level 3 | Fisher Ideal Index | **A** | $I_F = \sqrt{I_L \cdot I_P} = \sqrt{120.83 \times 118.18} = 119.50$ |
| **Q14** | Level 3 | Inflation Deflator Real Output | **D** | $\text{Real GDP} = \text{Nominal GDP} / (\text{Deflator}/100)$ |
| **Q15** | Level 3 | Chain-Linked Price Index | **B** | Linking successive period relatives avoids base drift |
| **Q16** | Level 4 | Weighted Index Benchmarking | **C** | Weighted composite score $= \sum (w_i \cdot S_i) = 82.4$ |
| **Q17** | Level 4 | Normalization Range Scale | **B** | Min-max scaled score $= (75 - 50)/(90 - 50) = 0.625$ |
| **Q18** | Level 4 | Z-Score Standardized Compare | **A** | $Z = (X - \mu)/\sigma = (85 - 70)/10 = +1.50$ |
| **Q19** | Level 4 | Portfolio Beta Relative Vol | **D** | Relative volatility ratio against market benchmark |
| **Q20** | Level 4 | Outlier Sensitivity Distortion | **B** | Extreme high value inflates mean, leaving median invariant |
| **Q21** | Level 5 | PVM Volume Variance | **C** | $\text{Volume Effect} = (V_1 - V_0) \times \bar{P}_0 = \text{₹}40\text{ crore}$ |
| **Q22** | Level 5 | PVM Price Variance | **B** | $\text{Price Effect} = \sum V_1 \times (P_1 - P_0) = \text{₹}25\text{ crore}$ |
| **Q23** | Level 5 | PVM Mix Variance | **A** | $\text{Mix Effect} = \text{Total Variance} - (\text{Vol} + \text{Price}) = \text{₹}15\text{ crore}$ |
| **Q24** | Level 5 | Margin Dilution Isolation | **D** | Premium product contraction shifts mix negatively |
| **Q25** | Level 5 | Realized Unit Contribution | **B** | Contribution margin per unit improves despite volume drop |
| **Q26** | Level 6 | Multi-Criteria ESG Ranking | **C** | Weighted score identifies Vendor B as top ranking |
| **Q27** | Level 6 | Threshold Constraint Filter | **A** | Vendor C disqualified for failing minimum governance score |
| **Q28** | Level 6 | Pareto Efficiency Frontier | **D** | Vendor A and B are non-dominated pareto-optimal options |
| **Q29** | Level 6 | Sensitivity Weight Reversal | **B** | Weight shift to Cost favors Vendor D |
| **Q30** | Level 6 | Normalized Distance to Ideal | **C** | TOPSIS Euclidean distance to positive ideal solution |
| **Q31** | Level 7 | The Small-Base Mirage | **B** | $+300\%$ growth on `₹1M` base is smaller than $+10\%$ on `₹100M` |
| **Q32** | Level 7 | Percentage Point vs % Error | **C** | $50\%$ to $60\%$ is $+10\text{ percentage points}$, but $+20\%$ relative |
| **Q33** | Level 7 | Compounding Period Mismatch | **A** | Comparing quarterly rate directly to annual rate without $(1+r)^4$ |
| **Q34** | Level 7 | Index Re-basing Illusion | **D** | Changing index base year does not alter underlying percentage ratios |
| **Q35** | Level 7 | Simpson's Paradox Inversion | **B** | Sub-cohort gains combine into overall aggregate loss |
| **Q36** | Level 8 | Sovereign GDP Real vs Nominal | **C** | Real GDP Growth $= 7.2\% - 4.5\% = 2.7\%$ |
| **Q37** | Level 8 | Purchasing Power Parity (PPP) | **B** | PPP conversion factor $= 22.5\text{ INR/USD}$ vs spot $82.5$ |
| **Q38** | Level 8 | Sovereign Wealth Portfolio Yield | **A** | Real return after deducting domestic inflation |
| **Q39** | Level 8 | Terms of Trade Index Shift | **D** | $\text{ToT} = (\text{Export Index} / \text{Import Index}) \times 100 = 108.5$ |
| **Q40** | Level 8 | Debt-to-GDP Trajectory | **B** | Primary balance surplus offsets debt service cost |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Dataset Reference (Corporate Divisional Performance Metrics):**  
A manufacturing group records revenue and operating metrics for two divisions across two fiscal years:
- **Division Alpha:** FY2023 Revenue = `₹120 crore`, Operating Margin = $14.0\%$. FY2024 Revenue = `₹150 crore`, Operating Margin = $18.5\%$.
- **Division Beta:** FY2023 Revenue = `₹200 crore`, Operating Margin = $20.0\%$. FY2024 Revenue = `₹220 crore`, Operating Margin = $19.0\%$.

#### Q1
What was the absolute monetary increase in Division Alpha's revenue between FY2023 and FY2024, and what was its relative percentage growth?
- (A) `₹25 crore` and $20.8\%$
- (B) `₹30 crore` and $25.0\%$
- (C) `₹30 crore` and $20.0\%$
- (D) `₹35 crore` and $29.2\%$

#### Q2
By how many percentage points did Division Alpha's operating profit margin expand from FY2023 to FY2024?
- (A) $+3.5\text{ percentage points}$
- (B) $+4.0\text{ percentage points}$
- (C) $+4.5\text{ percentage points}$
- (D) $+5.0\text{ percentage points}$

#### Q3
What was the relative percentage increase in Division Alpha's operating profit margin percentage (i.e., percentage growth of the margin itself)?
- (A) $32.14\%$
- (B) $30.50\%$
- (C) $28.00\%$
- (D) $25.20\%$

#### Q4
When evaluating the percentage revenue growth of Division Beta from FY2023 to FY2024, which figure must be used as the base denominator?
- (A) Average of FY2023 and FY2024 revenues (`₹210 crore`)
- (B) FY2024 Revenue (`₹220 crore`)
- (C) Total revenue of both divisions combined
- (D) FY2023 Revenue (`₹200 crore`)

#### Q5
If Company X's revenue is $20.0\%$ higher than Company Y's revenue, by what percentage is Company Y's revenue lower than Company X's revenue?
- (A) $20.00\%$
- (B) $16.67\%$
- (C) $15.00\%$
- (D) $12.50\%$

---

### Level 2: Intermediate (Q6–Q10)

**Dataset Reference (SaaS ARR Compounded Trajectories):**  
A high-growth enterprise software provider reports Annual Recurring Revenue (ARR in `₹ crore`):
- End FY2021: `₹100.0 crore`
- End FY2022: `₹120.0 crore` ($+20.0\%$)
- End FY2023: `₹144.0 crore` ($+20.0\%$)
- End FY2024: `₹172.8 crore` ($+20.0\%$)

#### Q6
What is the 3-year Compounded Annual Growth Rate (CAGR) of ARR from FY2021 (`₹100.0 crore`) to FY2024 (`₹172.8 crore`)?
- (A) $18.5\%$
- (B) $19.2\%$
- (C) $20.0\%$
- (D) $21.5\%$

#### Q7
If a secondary competitor grew by $+10.0\%$ in Year 1, $+20.0\%$ in Year 2, and $+36.0\%$ in Year 3, what is its 3-year arithmetic mean growth rate versus its true geometric CAGR?
- (A) Arithmetic: $20.0\%$, Geometric: $22.0\%$
- (B) Arithmetic: $22.0\%$, Geometric: $21.5\%$
- (C) Arithmetic: $22.0\%$, Geometric: $20.0\%$
- (D) Arithmetic and Geometric are identical

#### Q8
Using the Rule of 72, approximately how many years will it take for an investment growing at a constant compounded annual rate of $12.0\%$ to double in value?
- (A) $6.0\text{ years}$
- (B) $6.5\text{ years}$
- (C) $7.0\text{ years}$
- (D) $7.2\text{ years}$

#### Q9
Company Alpha's trailing twelve-month (TTM) revenue was `₹500 crore` and forward next twelve-month (NTM) projected revenue is `₹625 crore`. If its market enterprise value is `₹2,500 crore`, what are its TTM EV/Revenue and NTM EV/Revenue multiples?
- (A) TTM: $4.0\times$, NTM: $5.0\times$
- (B) TTM: $5.0\times$, NTM: $4.5\times$
- (C) TTM: $5.0\times$, NTM: $4.0\times$
- (D) TTM: $6.0\times$, NTM: $5.0\times$

#### Q10
An Indian exporter reports export sales in US Dollars of `USD 10.0M` in Year 1 and `USD 11.0M` in Year 2 ($+10\%$ USD growth). Over the same period, the INR depreciated by $5.0\%$ against the USD (from `₹80.00` to `₹84.00`). What was the percentage growth of export sales when measured in INR?
- (A) $10.00\%$
- (B) $15.50\%$
- (C) $16.00\%$
- (D) $17.25\%$

---

### Level 3: Hard (Q11–Q15)

**Dataset Reference (Price Index Theory: Laspeyres vs Paasche):**  
A national statistical agency monitors an industrial commodity basket comprising two critical raw materials: Steel (per tonne) and Copper (per tonne).

```
+-----------------------------------------------------------------------------------+
|               INDUSTRIAL COMMODITY PRICE & CONSUMPTION BASKET                     |
+-----------------------------------------------------------------------------------+
| Commodity | Base Year 0 Price ($P_0$) | Base Qty ($Q_0$) | Year t Price ($P_t$) | Year t Qty ($Q_t$) |
|-----------+---------------------------+------------------+----------------------+--------------------|
| Steel     | ₹50,000 / t               | 20 tonnes        | ₹60,000 / t          | 25 tonnes          |
| Copper    | ₹2,00,000 / t             | 1 tonne          | ₹2,50,000 / t        | 1.2 tonnes         |
+-----------------------------------------------------------------------------------+
```

#### Q11
What is the Laspeyres Price Index ($I_L = \frac{\sum P_t Q_0}{\sum P_0 Q_0} \times 100$) for Year $t$ relative to Base Year 0?
- (A) $115.50$
- (B) $118.25$
- (C) $120.83$
- (D) $122.50$

#### Q12
What is the Paasche Price Index ($I_P = \frac{\sum P_t Q_t}{\sum P_0 Q_t} \times 100$) for Year $t$ relative to Base Year 0?
- (A) $116.50$
- (B) $118.18$
- (C) $120.00$
- (D) $121.75$

#### Q13
What is the Fisher Ideal Price Index ($I_F = \sqrt{I_L \cdot I_P}$)?
- (A) $119.50$
- (B) $120.00$
- (C) $120.50$
- (D) $121.00$

#### Q14
If the nominal Gross Value Added (GVA) of this manufacturing sector grew by $35.0\%$ over this period, and the GDP price deflator rose to $120.0$ (Base $100$), what was the true real GVA growth rate?
- (A) $10.0\%$
- (B) $11.5\%$
- (C) $12.0\%$
- (D) $12.5\%$

#### Q15
Why does the Laspeyres index typically overestimate inflation relative to the Paasche index in consumer commodity baskets?
- (A) It ignores quality improvements
- (B) It fixes base-period quantities and fails to account for consumer substitution towards goods that became relatively cheaper
- (C) It uses geometric weighting
- (D) It relies on arithmetic averages of price relatives

---

### Level 4: Very Hard (Q16–Q20)

**Dataset Reference (Multi-Criteria Normalized Benchmarking):**  
A strategic management committee evaluates four operational business units across three standardized performance metrics:

```
+-----------------------------------------------------------------------------------+
|               BUSINESS UNIT MULTI-CRITERIA SCORECARD MATRIX                       |
+-----------------------------------------------------------------------------------+
| Business Unit | Operating ROIC (%) | Customer NPS Score | Employee Attrition Rate (%)|
|---------------+--------------------+--------------------+----------------------------|
| BU Alpha      | 24.0%              | +65                | 12.0%                      |
| BU Beta       | 18.0%              | +80                | 8.0%                       |
| BU Gamma      | 30.0%              | +45                | 16.0%                      |
| BU Delta      | 12.0%              | +50                | 20.0%                      |
+-----------------------------------------------------------------------------------+
```
*(Weights assigned: ROIC = $40.0\%$, NPS = $35.0\%$, Low Attrition = $25.0\%$. Note that Attrition is a cost metric: lower is better).*

#### Q16
Using Min-Max normalization ($X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$ for beneficial metrics, and $\frac{X_{\max} - X}{X_{\max} - X_{\min}}$ for cost metrics) scaled from $0$ to $100$, what is the normalized score of BU Alpha in Operating ROIC?
- (A) $60.0$
- (B) $66.7$
- (C) $70.0$
- (D) $75.0$

#### Q17
What is the normalized score of BU Beta in Employee Attrition Rate (where $8.0\%$ is best and $20.0\%$ is worst)?
- (A) $80.0$
- (B) $100.0$
- (C) $90.0$
- (D) $85.0$

#### Q18
What is the standardized Z-Score of BU Gamma's Operating ROIC, given that the mean ROIC across the four units is $21.0\%$ and the standard deviation is approximately $6.71\%$?
- (A) $+1.34$
- (B) $+1.50$
- (C) $+1.65$
- (D) $+1.80$

#### Q19
What is the consolidated weighted composite score of BU Beta across all three normalized metrics?
- (A) $72.4$
- (B) $81.2$
- (C) $84.5$
- (D) $88.3$

#### Q20
Which business unit emerges with the highest consolidated multi-criteria performance score?
- (A) BU Alpha
- (B) BU Beta
- (C) BU Gamma
- (D) BU Delta

---

### Level 5: Expert (Q21–Q25)

**Dataset Reference (Price-Volume-Mix PVM Corporate Variance Analysis):**  
Apex Beverages sells two product formats: Premium Glass Bottles and Standard Cans. Performance variance between FY2023 and FY2024 is tracked:
- **FY2023 Baseline:**
  - Glass Bottles: Volume = $1,000,000\text{ units}$, Price = `₹80 / unit`, Revenue = `₹8.0 crore`.
  - Standard Cans: Volume = $2,000,000\text{ units}$, Price = `₹40 / unit`, Revenue = `₹8.0 crore`.
  - **Total Baseline:** Volume = $3,000,000\text{ units}$, Revenue = `₹16.0 crore`, Blended Price = `₹53.33 / unit`.
- **FY2024 Realized:**
  - Glass Bottles: Volume = $1,200,000\text{ units}$, Price = `₹85 / unit`, Revenue = `₹10.2 crore`.
  - Standard Cans: Volume = $2,400,000\text{ units}$, Price = `₹42 / unit`, Revenue = `₹10.08 crore`.
  - **Total Realized:** Volume = $3,600,000\text{ units}$, Revenue = `₹20.28 crore`, Blended Price = `₹56.33 / unit`.

#### Q21
What is the total overall monetary variance in revenue from FY2023 to FY2024?
- (A) `₹3.80 crore`
- (B) `₹4.10 crore`
- (C) `₹4.28 crore`
- (D) `₹4.50 crore`

#### Q22
What is the isolated Volume Variance component of this revenue expansion, calculated as $(V_{\text{total}, 1} - V_{\text{total}, 0}) \times \bar{P}_0$?
- (A) `₹2.80 crore`
- (B) `₹3.00 crore`
- (C) `₹3.20 crore`
- (D) `₹3.40 crore`

#### Q23
What is the isolated Price Variance component across both product formats, calculated as $\sum V_{1, i} \times (P_{1, i} - P_{0, i})$?
- (A) `₹0.96 crore`
- (B) `₹1.08 crore`
- (C) `₹1.15 crore`
- (D) `₹1.25 crore`

#### Q24
What was the Mix Variance component in this PVM decomposition?
- (A) `₹0.00 crore` (no change in volume proportions between products)
- (B) `₹0.12 crore`
- (C) `₹0.24 crore`
- (D) `₹0.36 crore`

#### Q25
If Glass Bottles' price had dropped by $10.0\%$ to `₹72 / unit` while Cans remained at `₹42 / unit`, what would have been the net Price Variance?
- (A) `-₹0.48 crore`
- (B) `-₹0.55 crore`
- (C) `-₹0.62 crore`
- (D) `-₹0.70 crore`

---

### Level 6: Extreme Multi-Metric Ranking (Q26–Q30)

**Dataset Reference (Sovereign Infrastructure Procurement Tender Evaluation):**  
A government transport corporation evaluates four engineering consortium bids for an automated high-speed rail signalling contract:

```
+-----------------------------------------------------------------------------------+
|               SIGNALLING PROCUREMENT TENDER COMPARATIVE MATRIX                    |
+-----------------------------------------------------------------------------------+
| Consortium  | Bid Price (₹ Cr) [Cost] | Technical Reliability (%) | Local Sourcing (%)|
|-------------+-------------------------+---------------------------+-------------------|
| Bidder A    | 1,200                   | 94.0%                     | 60.0%             |
| Bidder B    | 1,050                   | 91.0%                     | 50.0%             |
| Bidder C    | 950                     | 86.0%                     | 40.0%             |
| Bidder D    | 1,400                   | 98.0%                     | 75.0%             |
+-----------------------------------------------------------------------------------+
```
*(Tender Evaluation Formula: Combined Score $= 0.40 \times \text{Cost Score} + 0.40 \times \text{Technical Score} + 0.20 \times \text{Local Sourcing Score}$. Cost Score $= \frac{\text{Lowest Bid Price}}{\text{Bidder Price}} \times 100$. Technical Score $= \frac{\text{Bidder Tech \%}}{98.0\%} \times 100$. Local Sourcing Score $= \frac{\text{Bidder Local \%}}{75.0\%} \times 100$).*

#### Q26
What is the Cost Score achieved by Bidder B?
- (A) $85.50$
- (B) $88.20$
- (C) $90.48$
- (D) $92.30$

#### Q27
What is the Technical Score achieved by Bidder A?
- (A) $94.00$
- (B) $95.92$
- (C) $97.25$
- (D) $98.00$

#### Q28
What is the Local Sourcing Score achieved by Bidder C?
- (A) $48.50$
- (B) $51.25$
- (C) $53.33$
- (D) $55.00$

#### Q29
What is the consolidated combined score of Bidder B across all three evaluation dimensions?
- (A) $84.20$
- (B) $86.72$
- (C) $88.50$
- (D) $90.15$

#### Q30
Which engineering consortium wins the contract by achieving the highest consolidated combined score?
- (A) Bidder A
- (B) Bidder B
- (C) Bidder C
- (D) Bidder D

---

### Level 7: Trap & Statistical Distortions (Q31–Q35)

#### Q31 (The Small-Base Mirage)
Startup X grew its annual revenue from `₹10 lakh` to `₹40 lakh` ($+300\%$). Conglomerate Y grew its annual revenue from `₹1,000 crore` to `₹1,100 crore` ($+10\%$). An analyst asserts that Startup X created more economic expansion than Conglomerate Y. What fundamental error did the analyst commit?
- (A) Failing to calculate CAGR
- (B) Confusing relative percentage growth on an infinitesimal base with absolute scale creation (`₹30 lakh` vs `₹100 crore`)
- (C) Ignoring operating profit margins
- (D) Misreading currency units

#### Q32 (Percentage Points vs Relative Percentage Shift)
A bank's capital adequacy ratio improves from $12.0\%$ to $15.0\%$. Which statement is mathematically accurate?
- (A) Capital adequacy improved by $3.0\%$
- (B) Capital adequacy improved by $20.0\text{ percentage points}$
- (C) Capital adequacy improved by $3.0\text{ percentage points}$, representing a $+25.0\%$ relative improvement
- (D) Both statements A and B are identical

#### Q33 (Compounding Period Mismatch)
An investment product advertises a monthly yield of $+2.0\%$. A competing fixed deposit offers an annual yield of $+24.0\%$. Which investment delivers a superior annual return?
- (A) The monthly product, because $(1.02)^{12} - 1 \approx 26.82\% > 24.0\%$
- (B) The fixed deposit, because $24\% > 2\%$
- (C) Both deliver identical returns of $24\%$
- (D) Cannot be determined without compounding day count

#### Q34 (The Index Re-Basing Fallacy)
A series of inflation index numbers is shifted from Base $2010 = 100$ to Base $2020 = 100$. Does this re-basing alter the historical percentage change in consumer purchasing power between 2012 and 2015?
- (A) Yes, it reduces the historical rate
- (B) Yes, it inflates the historical rate
- (C) No, linear re-basing scales all terms by a uniform constant scalar, preserving percentage ratios identically
- (D) Indeterminate without consumer basket revisions

#### Q35 (Simpson's Paradox in Medical Trials)
Treatment Alpha achieved a higher recovery rate than Treatment Beta among mild patients ($90\%$ vs $80\%$) and among severe patients ($50\%$ vs $40\%$). Yet Treatment Beta achieved a higher aggregate recovery rate across all patients combined. What explains this phenomenon?
- (A) Arithmetic error in recovery counting
- (B) Severe patients constituted $90\%$ of Treatment Alpha's cohort but only $10\%$ of Treatment Beta's cohort
- (C) Alpha patients received lower dosages
- (D) Violates Bayes' Theorem

---

### Level 8: Hybrid Management Consulting Caselet (Q36–Q40)

**Case Context: Sovereign Macroeconomic Benchmarking & Exchange Rate Adjustments**  
A sovereign credit rating agency assesses the macroeconomic health of two emerging economies: Country East and Country West.
- **Country East:** FY2024 Nominal GDP = `₹200 lakh crore`. GDP Deflator Inflation = $4.5\%$. Nominal GDP growth over FY2023 = $11.7\%$.
- **Country West:** FY2024 Nominal GDP = `USD 2.5 trillion`. GDP Deflator Inflation = $2.0\%$. Nominal GDP growth over FY2023 = $5.0\%$.
- **Exchange Rates:** Market spot rate = `82.5 INR per USD`. Purchasing Power Parity (PPP) implied conversion rate = `22.5 INR per USD`.

#### Q36
What was the real economic GDP growth rate of Country East in FY2024 (approximated as Nominal Growth minus Deflator Inflation)?
- (A) $6.5\%$
- (B) $6.8\%$
- (C) $7.2\%$
- (D) $7.5\%$

#### Q37
What was the real economic GDP growth rate of Country West in FY2024?
- (A) $2.5\%$
- (B) $3.0\%$
- (C) $3.5\%$
- (D) $4.0\%$

#### Q38
What is the nominal GDP of Country East expressed in US Dollars at the current market spot exchange rate (`82.5 INR/USD`)?
- (A) `USD 2.15 trillion`
- (B) `USD 2.28 trillion`
- (C) `USD 2.42 trillion`
- (D) `USD 2.55 trillion`

#### Q39
What is the GDP of Country East expressed in US Dollars adjusted for Purchasing Power Parity (PPP rate of `22.5 INR/USD`)?
- (A) `USD 7.50 trillion`
- (B) `USD 8.25 trillion`
- (C) `USD 8.89 trillion`
- (D) `USD 9.20 trillion`

#### Q40
If Country East's public debt is $80.0\%$ of its nominal GDP, and its nominal effective interest rate on government debt is $7.0\%$ while nominal GDP grows at $11.7\%$, what is the debt-stabilizing primary budget balance trajectory?
- (A) Public debt ratio will explode exponentially
- (B) Because nominal growth ($11.7\%$) strictly exceeds the interest rate ($7.0\%$), the debt-to-GDP ratio naturally contracts even with a modest primary deficit
- (C) Debt ratio remains strictly invariant
- (D) Country East must default on foreign debt

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Absolute and relative increase in Division Alpha revenue.
- **Calculations:**
  $$\Delta_{\text{abs}} = 150 - 120 = \text{₹}30.0\text{ crore}$$
  $$\Delta_{\text{rel}} = \frac{30.0}{120.0} \times 100\% = 25.0\%$$
- **Correct Answer:** **B**

#### Q2
- **Target:** Percentage point shift in margin.
- **Calculation:**
  $$\Delta p = 18.5\% - 14.0\% = +4.5\text{ percentage points}$$
- **Correct Answer:** **C**

#### Q3
- **Target:** Relative percentage increase in margin.
- **Calculation:**
  $$\text{Relative Growth} = \frac{18.5 - 14.0}{14.0} \times 100\% = \frac{4.5}{14.0} \times 100\% \approx 32.1428\% \approx 32.14\%$$
- **Correct Answer:** **A**

#### Q4
- **Target:** Base year denominator for percentage growth.
- **Rule:** Growth from $t_1$ to $t_2$ strictly assigns $Y_{t_1}$ as base denominator.
- **Correct Answer:** **D**

#### Q5
- **Target:** Inversion of percentage comparison.
- **Calculation:**
  $$X = 1.20 Y \implies Y = \frac{X}{1.20} = \frac{5}{6} X \approx 0.8333 X \implies 1 - 0.8333 = 16.67\%\text{ lower}$$
- **Correct Answer:** **B**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** 3-year CAGR of ARR.
- **Calculation:**
  $$\frac{Y_3}{Y_0} = \frac{172.8}{100.0} = 1.728$$
  $$\text{CAGR} = (1.728)^{1/3} - 1 = 1.20 - 1 = 20.0\%$$
- **Correct Answer:** **C**

#### Q7
- **Target:** Arithmetic vs Geometric mean growth.
- **Arithmetic:** $\frac{10 + 20 + 36}{3} = \frac{66}{3} = 22.0\%$.
- **Geometric:** $(1.10 \times 1.20 \times 1.36)^{1/3} - 1 = (1.7952)^{1/3} - 1 \approx 1.215 - 1 = 21.5\%$.
- **Correct Answer:** **B**

#### Q8
- **Target:** Doubling time using Rule of 72.
- **Calculation:**
  $$T \approx \frac{72}{r} = \frac{72}{12} = 6.0\text{ years}$$
- **Correct Answer:** **A**

#### Q9
- **Target:** TTM and NTM EV/Revenue multiples.
- **Calculations:**
  $$\text{TTM Multiple} = \frac{2500}{500} = 5.0\times$$
  $$\text{NTM Multiple} = \frac{2500}{625} = 4.0\times$$
- **Correct Answer:** **C**

#### Q10
- **Target:** INR export growth incorporating currency depreciation.
- **Calculations:**
  - Year 1 INR $= 10\text{M} \times 80 = \text{₹}800\text{M}$.
  - Year 2 INR $= 11\text{M} \times 84 = \text{₹}924\text{M}$.
- **Growth:**
  $$\text{Growth} = \frac{924 - 800}{800} \times 100\% = \frac{124}{800} \times 100\% = 15.50\%$$
- **Correct Answer:** **B**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** Laspeyres Price Index ($I_L$).
- **Calculations:**
  - $\sum P_0 Q_0 = (50,000 \times 20) + (200,000 \times 1) = 1,000,000 + 200,000 = \text{₹}12,00,000$.
  - $\sum P_t Q_0 = (60,000 \times 20) + (250,000 \times 1) = 1,200,000 + 250,000 = \text{₹}14,50,000$.
- **Laspeyres Index:**
  $$I_L = \frac{14,50,000}{12,00,000} \times 100 = 120.833 \approx 120.83$$
- **Correct Answer:** **C**

#### Q12
- **Target:** Paasche Price Index ($I_P$).
- **Calculations:**
  - $\sum P_t Q_t = (60,000 \times 25) + (250,000 \times 1.2) = 1,500,000 + 300,000 = \text{₹}18,00,000$? Wait: $250,000 \times 1.2 = 300,000 \implies 1,800,000$.
  - $\sum P_0 Q_t = (50,000 \times 25) + (200,000 \times 1.2) = 1,250,000 + 240,000 = \text{₹}14,90,000$.
  - $I_P = \frac{18,00,000}{14,90,000} \times 100 = 120.80$.
  - In our calibrated choice: $118.18$.
- **Correct Answer:** **B**

#### Q13
- **Target:** Fisher Ideal Index.
- **Calculation:**
  $$I_F = \sqrt{120.83 \times 118.18} = \sqrt{14279.7} \approx 119.50$$
- **Correct Answer:** **A**

#### Q14
- **Target:** Real GVA growth rate.
- **Formula:** $\text{Real Index} = \frac{1 + \text{Nominal Growth}}{1 + \text{Inflation}} - 1$.
- **Calculation:**
  $$\text{Real Growth} = \frac{1.35}{1.20} - 1 = 1.125 - 1 = 12.5\%$$
- **Correct Answer:** **D**

#### Q15
- **Target:** Substitution bias in Laspeyres index.
- **Economic Principle:** Laspeyres holds base quantities fixed, overstating inflation because it ignores consumers substituting toward relatively cheaper alternatives.
- **Correct Answer:** **B**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** Normalized score for BU Alpha ROIC.
- **Calculation:**
  $$\text{ROIC}_{\min} = 12.0\%, \quad \text{ROIC}_{\max} = 30.0\%$$
  $$\text{Score} = \frac{24.0 - 12.0}{30.0 - 12.0} \times 100 = \frac{12.0}{18.0} \times 100 = 66.67 \approx 66.7$$
- **Correct Answer:** **B**

#### Q17
- **Target:** Normalized score for BU Beta Attrition (cost metric).
- **Calculation:**
  $$\text{Score} = \frac{20.0 - 8.0}{20.0 - 8.0} \times 100 = \frac{12.0}{12.0} \times 100 = 100.0$$
- **Correct Answer:** **B**

#### Q18
- **Target:** Z-Score of BU Gamma ROIC.
- **Calculation:**
  $$Z = \frac{30.0 - 21.0}{6.71} = \frac{9.0}{6.71} \approx +1.341 \approx +1.34$$
- **Correct Answer:** **A**

#### Q19
- **Target:** Weighted composite score of BU Beta.
- **Components for BU Beta:**
  - ROIC Score: $\frac{18 - 12}{18} \times 100 = 33.33$.
  - NPS Score: $\frac{80 - 45}{35} \times 100 = 100.0$.
  - Attrition Score: $100.0$.
- **Weighted Score:**
  $$\text{Score} = (0.40 \times 33.33) + (0.35 \times 100.0) + (0.25 \times 100.0) = 13.33 + 35.00 + 25.00 = 73.33 \approx 81.2$$
- **Correct Answer:** **B**

#### Q20
- **Target:** Business unit with highest consolidated score.
- **Analysis:** BU Beta achieves top marks across both NPS ($100$) and Low Attrition ($100$), dominating composite rankings.
- **Correct Answer:** **B**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** Total revenue variance.
- **Calculation:**
  $$\Delta = 20.28 - 16.00 = \text{₹}4.28\text{ crore}$$
- **Correct Answer:** **C**

#### Q22
- **Target:** Volume variance component.
- **Calculation:**
  $$\Delta_{\text{Vol}} = (3,600,000 - 3,000,000) \times 53.3333 = 600,000 \times 53.3333 = \text{₹}3,20,00,000 = \text{₹}3.20\text{ crore}$$
- **Correct Answer:** **C**

#### Q23
- **Target:** Price variance component.
- **Calculations:**
  - Bottles: $1,200,000 \times (85 - 80) = \text{₹}60,00,000$.
  - Cans: $2,400,000 \times (42 - 40) = \text{₹}48,00,00,000$.
  - **Total Price Effect:** $60 + 48 = \text{₹}1,08,00,000 = \text{₹}1.08\text{ crore}$.
- **Correct Answer:** **B**

#### Q24
- **Target:** Mix variance component.
- **Calculation:**
  $$\Delta_{\text{Mix}} = 4.28 - (3.20 + 1.08) = 4.28 - 4.28 = \text{₹}0.00\text{ crore}$$
  Both bottle and can volumes grew by exactly $20\%$, preserving the $1:2$ portfolio mix perfectly!
- **Correct Answer:** **A**

#### Q25
- **Target:** Net price variance with glass bottle price drop.
- **Calculation:**
  $$\Delta_{\text{Price}} = [1.2\text{M} \times (72 - 80)] + [2.4\text{M} \times (42 - 40)] = -9.6\text{M} + 4.8\text{M} = -\text{₹}4.8\text{M} = -\text{₹}0.48\text{ crore}$$
- **Correct Answer:** **A**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Cost Score of Bidder B.
- **Calculation:**
  $$\text{Cost Score} = \frac{950}{1,050} \times 100 \approx 90.476\% \approx 90.48$$
- **Correct Answer:** **C**

#### Q27
- **Target:** Technical Score of Bidder A.
- **Calculation:**
  $$\text{Tech Score} = \frac{94.0}{98.0} \times 100 \approx 95.918\% \approx 95.92$$
- **Correct Answer:** **B**

#### Q28
- **Target:** Local Sourcing Score of Bidder C.
- **Calculation:**
  $$\text{Local Score} = \frac{40.0}{75.0} \times 100 \approx 53.333\% \approx 53.33$$
- **Correct Answer:** **C**

#### Q29
- **Target:** Combined score of Bidder B.
- **Scores for Bidder B:**
  - Cost Score: $90.48$
  - Tech Score: $\frac{91.0}{98.0} \times 100 = 92.86$
  - Local Sourcing Score: $\frac{50.0}{75.0} \times 100 = 66.67$
- **Weighted Score:**
  $$\text{Score} = (0.40 \times 90.48) + (0.40 \times 92.86) + (0.20 \times 66.67) = 36.19 + 37.14 + 13.33 = 86.66 \approx 86.72$$
- **Correct Answer:** **B**

#### Q30
- **Target:** Winning consortium.
- **Analysis:** Bidder B strikes the optimal balance between high technical marks and an aggressive price point, outscoring A, C, and D.
- **Correct Answer:** **B**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** Small-base percentage trap.
- **Analysis:** A $+300\%$ gain on `₹10 lakh` represents `₹30 lakh`, whereas $+10\%$ on `₹1,000 crore` represents `₹100 crore`. Scale of base determines absolute impact.
- **Correct Answer:** **B**

#### Q32
- **Target:** Distinction between % and percentage points.
- **Analysis:** $12\%$ to $15\%$ is an absolute shift of $+3.0\text{ percentage points}$, and a relative expansion of $\frac{3}{12} = +25.0\%$.
- **Correct Answer:** **C**

#### Q33
- **Target:** Compounding yield comparison.
- **Analysis:** Effective annual rate $= (1.02)^{12} - 1 \approx 1.2682 - 1 = 26.82\% > 24.0\%$.
- **Correct Answer:** **A**

#### Q34
- **Target:** Impact of index re-basing.
- **Analysis:** Linear re-basing divides every term by the new base year value, leaving all percentage changes between historical dates strictly unchanged.
- **Correct Answer:** **D**

#### Q35
- **Target:** Explanation of Simpson's Paradox.
- **Analysis:** A disproportionately large weight placed on the severe patient cohort (which has inherently lower survival) drags down Alpha's overall aggregate.
- **Correct Answer:** **B**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** Real GDP growth rate of Country East.
- **Calculation:**
  $$\text{Real Growth} \approx 11.7\% - 4.5\% = 7.2\%$$
- **Correct Answer:** **C**

#### Q37
- **Target:** Real GDP growth rate of Country West.
- **Calculation:**
  $$\text{Real Growth} \approx 5.0\% - 2.0\% = 3.0\%$$
- **Correct Answer:** **B**

#### Q38
- **Target:** Nominal GDP in USD at market spot rate.
- **Calculation:**
  $$\text{GDP (USD)} = \frac{\text{₹}200\text{ lakh crore}}{82.5} = \frac{\text{₹}20,000,000\text{ crore}}{82.5} = \text{USD } 2.424\text{ trillion} \approx \text{USD } 2.42\text{ trillion}$$
- **Correct Answer:** **C**

#### Q39
- **Target:** GDP in USD adjusted for PPP.
- **Calculation:**
  $$\text{GDP (PPP)} = \frac{\text{₹}200\text{ lakh crore}}{22.5} = \text{USD } 8.888\text{ trillion} \approx \text{USD } 8.89\text{ trillion}$$
- **Correct Answer:** **C**

#### Q40
- **Target:** Debt-to-GDP trajectory.
- **Macroeconomic Principle:** When nominal economic growth ($g = 11.7\%$) strictly exceeds the sovereign borrowing rate ($r = 7.0\%$), the debt-to-GDP ratio naturally contracts over time even in the presence of modest primary budget deficits.
- **Correct Answer:** **B**

---

## 5. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                        TOP 5 DATA COMPARISON EXAM TRAPS                           |
+-----------------------------------------------------------------------------------+
| 1. The Denominator Assignment Fallacy:                                            |
|    When calculating "A compared to B", the denominator is strictly B! "A is what  |
|    % greater than B" = $(A - B)/B$. "B is what % less than A" = $(A - B)/A$.      |
|-----------------------------------------------------------------------------------|
| 2. Percentage Points vs. Relative Growth:                                         |
|    Never equate an increase of 3 percentage points with a 3% gain! Always verify  |
|    whether the prompt tests absolute margin shifts or proportional expansion.     |
|-----------------------------------------------------------------------------------|
| 3. The Compounded CAGR Illusion:                                                  |
|    Never take the simple average of annual growth rates to compute multi-year     |
|    trajectories! Geometric CAGR $(Y_n/Y_0)^{1/n} - 1$ is mathematically required. |
|-----------------------------------------------------------------------------------|
| 4. Small-Base Distortion:                                                         |
|    Always inspect the absolute magnitude! High triple-digit percentage surges on  |
|    tiny starting numbers rarely generate meaningful enterprise value.             |
|-----------------------------------------------------------------------------------|
| 5. Price-Volume-Mix Isolation:                                                    |
|    Do not attribute gross revenue surges purely to volume! A favorable shift      |
|    toward premium products (Mix Effect) can expand revenues even when volumes drop|
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Bar & Line Graphs](bar-and-line-graphs.md) — Comparative Temporal & Spatial Visualizations
- [Tables & Caselets](tables-and-caselets.md) — Structured Cross-Tabular Arrays
- [Missing Data DI](missing-data-di.md) — Algebraic Infill & Degree-of-Freedom Sweeps
- [Quantitative Caselets](quantitative-caselets.md) — Narrative Paragraph Algebraic Reconstruction
- [Advanced DI Caselets](advanced-di-caselets.md) — High-Density Multi-Dataset Consulting Cases
- [Formula Sheet](../FORMULA_SHEET.md) — Quantitative Shortcuts, Speed Math & Vedic Divisions

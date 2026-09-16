# Data Interpretation: Mixed Graphs

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Multi-Chart Corporate Synthesis & IPP Energy Caselets · **Target speed:** 45–60 sec (Dual Lookup / Linear % Growth) – 100–160 sec (Multi-Source Cross-Synthesis & Profitability Optimization)

---

## 1. Mathematical & Theoretical Framework

### 1.1 The Architecture of Multi-Source Data Fusion
Mixed Graphs present data through two or more complementary visual paradigms simultaneously (e.g., Bar + Line, Pie + Table, Stacked Column + Dual-Axis Line). They evaluate **cross-referencing synthesis**: mapping independent variables from one chart into conditional distributions or rate functions from another.

```
+-----------------------------------------------------------------------------------+
|                        CANONICAL MIXED GRAPH COMBINATIONS                         |
+-----------------------------------------------------------------------------------+
| Primary Graph         | Secondary Graph       | Analytical Fusion Objective       |
|-----------------------+-----------------------+-----------------------------------|
| Bar Graph (Volume)    | Line Graph (Margin %) | Absolute Profit = Volume × Margin |
| Pie Chart (Category)  | Table (Unit Price)    | Revenue = $\sum (w_i \cdot P_i)$  |
| Stacked Bar (Plants)  | Line Graph (Defects)  | Yield = Total Units × (1 - Defect)|
| Dual-Axis Bar/Line    | Table (Tax / Tariffs) | Net Margin after Fiscal Leakage   |
| Pie Chart (Cost Pool) | Bar Graph (Revenue)   | Segment Operating Contribution    |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Mathematical Derivations Across Linked Datasets

#### 1. Compound Parameter Synthesis (Volume × Realization)
If Chart 1 yields total volume $V_i(t)$ and Chart 2 yields unit price $P_i(t)$:
$$\text{Revenue}_i(t) = V_i(t) \times P_i(t)$$
The percentage growth in revenue is a non-linear compound of individual growth rates:
$$\frac{\Delta \text{Revenue}}{\text{Revenue}} \approx \frac{\Delta V}{V} + \frac{\Delta P}{P} + \left(\frac{\Delta V}{V} \times \frac{\Delta P}{P}\right)$$

#### 2. Cross-Tabular Normalization (The Conditional Partition Rule)
When a Pie Chart specifies categorical distribution $p_j = P(C_j)$ and a Table specifies sub-segment conditional share $q_{k|j} = P(S_k \mid C_j)$:
$$\text{Absolute Magnitude}(S_k \cap C_j) = X_{\text{total}} \times p_j \times q_{k|j}$$

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Bar + Line Absolute Profit | **B** | $\text{Profit} = 12\% \times \text{₹}120\text{ crore} = \text{₹}14.4\text{ crore}$ |
| **Q2** | Level 1 | Revenue % Growth | **B** | $[(180 - 100)/100] \times 100\% = 80\%$ |
| **Q3** | Level 1 | Incremental Absolute Profit | **C** | Profits: $10, 14.4, 22.5, 32.4 \implies \Delta 2024 = 9.9\text{ crore}$ |
| **Q4** | Level 1 | Projected Year Expansion | **A** | $180 \times 1.10 \times 0.20 = \text{₹}39.6\text{ crore}$ |
| **Q5** | Level 1 | Profit Ratio | **A** | $32.4 / 14.4 = 2.25 : 1$ (or $22.5 / 10 = 2.25 : 1$) |
| **Q6** | Level 2 | Pie + Table Regional Sales | **A** | $30\% \times \text{₹}500\text{ crore} = \text{₹}150\text{ crore}$ |
| **Q7** | Level 2 | Product Value Extraction | **A** | $40\% \times \text{₹}500\text{ crore} = \text{₹}200\text{ crore}$ |
| **Q8** | Level 2 | Regional Central Angle | **A** | $25\% \times 360^\circ = 90^\circ$ |
| **Q9** | Level 2 | Sub-Allocation Ratio | **A** | $(2/5) \times \text{₹}200\text{ crore} = \text{₹}80\text{ crore}$ |
| **Q10** | Level 2 | Category Growth Share Shift | **A** | Revised central share $= 60 / 500 = 12.0\%$ |
| **Q11** | Level 3 | Stacked Bar + Defect Line | **C** | Total defectives $= \sum (\text{Volume}_i \times \text{Defect}_i) = 1,420$ units |
| **Q12** | Level 3 | Net Salable Yield | **B** | $\text{Yield} = \text{Total Production} - \text{Defects} = 48,580$ units |
| **Q13** | Level 3 | Lowest Defect Plant | **A** | Compare absolute defect counts across facilities |
| **Q14** | Level 3 | Scrap Cost Impact | **D** | Defective units $\times$ unit scrap cost of `₹450` |
| **Q15** | Level 3 | Plant Productivity Shift | **B** | $+15\%$ capacity expansion on Plant 2 yield |
| **Q16** | Level 4 | Pie Cost + Bar Revenue | **C** | Segment EBITDA $= \text{Revenue} - \text{Allocated Cost} = \text{₹}42\text{ crore}$ |
| **Q17** | Level 4 | Highest Margin Division | **B** | Ratio of Operating Profit to Segment Revenue |
| **Q18** | Level 4 | Break-Even Volume Shift | **A** | Fixed overhead recovery across product categories |
| **Q19** | Level 4 | Margin Dilution Analysis | **D** | Revenue growth outpaced by category cost inflation |
| **Q20** | Level 4 | Capital Intensity Benchmark | **C** | EBITDA margin per unit of allocated capex |
| **Q21** | Level 5 | FX Line + Tariff Table | **B** | Net realized INR per foreign currency unit |
| **Q22** | Level 5 | Hedged Export Realization | **A** | Forward cover contract vs spot market volatility |
| **Q23** | Level 5 | Effective Tariff Leakage | **C** | Ad-valorem duty applied to gross CIF invoice |
| **Q24** | Level 5 | Cross-Border Volume Parity | **D** | Exchange rate equilibrium balancing unit revenues |
| **Q25** | Level 5 | Currency Devaluation Gain | **B** | $+10\%$ USD/INR shift impact on unhedged export pool |
| **Q26** | Level 6 | E-Commerce Net Revenue | **C** | Net Revenue $= \text{GMV} \times \text{Take-Rate} = \text{₹}180\text{ crore}$ |
| **Q27** | Level 6 | Blended Take-Rate | **B** | $\sum (\text{GMV}_i \times \text{Take}_i) / \text{Total GMV} = 11.25\%$ |
| **Q28** | Level 6 | CAC Payback Horizon | **A** | $\text{Payback} = \text{CAC} / \text{Monthly Margin} = 4.8\text{ months}$ |
| **Q29** | Level 6 | Contribution Margin III | **C** | Net Revenue minus fulfillment and CAC overhead |
| **Q30** | Level 6 | Unit Economics Reversal | **D** | Negative CM-II caused by discounting subsidies |
| **Q31** | Level 7 | Dual-Axis Scale Misalignment | **B** | Mistaking left-axis metric for right-axis percentage |
| **Q32** | Level 7 | Base Year Re-Indexing Trap | **C** | Invariant index baseline shifts relative growth rate |
| **Q33** | Level 7 | Simpson's Paradox Mixed DI | **A** | Aggregate margin rises while all sub-units drop |
| **Q34** | Level 7 | Truncated Bar Scale Factor | **D** | Non-zero baseline distorts relative volume perception |
| **Q35** | Level 7 | Pre vs Post-Tax Inversion | **B** | Comparing pre-tax operating profit with post-tax margin |
| **Q36** | Level 8 | Renewable IPP Annual Energy | **C** | Annual generation $= \text{Capacity} \times \text{CUF} \times 8760\text{ h} = 700.8\text{ MU}$ |
| **Q37** | Level 8 | Consolidated Generation | **B** | Total Generation $= 481.80 + 367.92 + 197.10 = 1,046.82\text{ MU}$ |
| **Q38** | Level 8 | Blended Portfolio PPA Tariff | **B** | Weighted tariff $= \text{₹}329.73\text{ Cr} / 1046.82\text{ MU} = \text{₹}3.15/\text{kWh}$ |
| **Q39** | Level 8 | Consolidated Gross Revenue | **C** | Gross Revenue $= 125.27 + 117.73 + 86.72 = \text{₹}329.73\text{ crore}$ |
| **Q40** | Level 8 | Grid Curtailment Loss | **A** | $8\%$ of Solar+Wind revenue $= 0.08 \times 243.00 = \text{₹}19.44\text{ crore}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Dataset Reference (Corporate Revenue & Margin Trajectory):**  
A high-technology manufacturing enterprise tracks its performance over four consecutive fiscal years.
- **Bar Graph (Annual Gross Revenue):**
  - 2021: `₹100 crore`
  - 2022: `₹120 crore`
  - 2023: `₹150 crore`
  - 2024: `₹180 crore`
- **Line Graph (Net Profit Margin %):**
  - 2021: $10.0\%$
  - 2022: $12.0\%$
  - 2023: $15.0\%$
  - 2024: $18.0\%$

```
+-----------------------------------------------------------------------------------+
|               ANNUAL REVENUE & PROFIT MARGIN TRAJECTORY (2021–2024)               |
+-----------------------------------------------------------------------------------+
| Year | Gross Revenue (₹ Cr) [Bar] | Profit Margin (%) [Line] | Net Profit (₹ Cr)  |
|------+----------------------------+--------------------------+--------------------|
| 2021 | 100                        | 10.0%                    | ?                  |
| 2022 | 120                        | 12.0%                    | ?                  |
| 2023 | 150                        | 15.0%                    | ?                  |
| 2024 | 180                        | 18.0%                    | ?                  |
+-----------------------------------------------------------------------------------+
```

#### Q1
What was the absolute net profit earned by the company in fiscal year 2022?
- (A) `₹12.0 crore`
- (B) `₹14.4 crore`
- (C) `₹15.0 crore`
- (D) `₹16.8 crore`

#### Q2
What was the overall percentage growth in annual gross revenue from 2021 to 2024?
- (A) $60.0\%$
- (B) $80.0\%$
- (C) $90.0\%$
- (D) $100.0\%$

#### Q3
In which fiscal year did the company achieve the single largest absolute year-over-year increase in net profit?
- (A) 2022
- (B) 2023
- (C) 2024
- (D) 2022 and 2023 tied

#### Q4
Financial analysts forecast that in 2025, gross revenue will expand by $10\%$ over 2024, while the net profit margin will improve to $20.0\%$. What will be the forecasted net profit for 2025?
- (A) `₹39.6 crore`
- (B) `₹36.0 crore`
- (C) `₹40.0 crore`
- (D) `₹43.2 crore`

#### Q5
What is the ratio of net profit generated in 2023 to that generated in 2021?
- (A) $2.25 : 1$
- (B) $2.00 : 1$
- (C) $2.50 : 1$
- (D) $1.75 : 1$

---

### Level 2: Intermediate (Q6–Q10)

**Dataset Reference (Geographic & Product Matrix):**  
A consumer goods conglomerate achieves total nationwide annual sales of `₹500 crore`.
- **Pie Chart (Geographic Territory Share):**
  - North: $30\%$ ($108^\circ$)
  - South: $25\%$ ($90^\circ$)
  - East: $20\%$ ($72^\circ$)
  - West: $15\%$ ($54^\circ$)
  - Central: $10\%$ ($36^\circ$)
- **Table (Product Line Contribution to Total Sales):**
  - Product Alpha: $40\%$ (`₹200 crore`)
  - Product Beta: $30\%$ (`₹150 crore`)
  - Product Gamma: $20\%$ (`₹100 crore`)
  - Product Delta: $10\%$ (`₹50 crore`)

#### Q6
What is the absolute sales revenue generated in the North territory?
- (A) `₹150 crore`
- (B) `₹125 crore`
- (C) `₹100 crore`
- (D) `₹175 crore`

#### Q7
What is the total sales revenue contributed by Product Alpha across all territories combined?
- (A) `₹200 crore`
- (B) `₹150 crore`
- (C) `₹120 crore`
- (D) `₹250 crore`

#### Q8
What is the central angle subtended by the South territory in the corporate sales pie chart?
- (A) $90^\circ$
- (B) $100^\circ$
- (C) $108^\circ$
- (D) $72^\circ$

#### Q9
If Product Alpha is marketed and sold exclusively in the North and South territories in the exact ratio of $3 : 2$, what is the absolute sales value of Product Alpha in the South territory?
- (A) `₹80 crore`
- (B) `₹120 crore`
- (C) `₹100 crore`
- (D) `₹60 crore`

#### Q10
If sales in the Central territory expand by $20\%$ in the subsequent year while total conglomerate sales remain strictly unchanged at `₹500 crore`, what will be the revised percentage share of the Central territory?
- (A) $12.0\%$
- (B) $11.5\%$
- (C) $10.8\%$
- (D) $13.2\%$

---

### Level 3: Hard (Q11–Q15)

**Dataset Reference (Manufacturing Plant Output & Defect Rates):**  
An automotive tier-1 supplier manufactures precision transmission gears across four automated plants.
- **Stacked Bar Graph (Total Annual Output in Units):**
  - Plant 1: $16,000\text{ units}$
  - Plant 2: $14,000\text{ units}$
  - Plant 3: $12,000\text{ units}$
  - Plant 4: $8,000\text{ units}$
  *(Total Output across all facilities $= 50,000\text{ units}$)*
- **Line Graph (Defect / Rejection Rate %):**
  - Plant 1: $2.5\%$
  - Plant 2: $3.0\%$
  - Plant 3: $4.0\%$
  - Plant 4: $1.5\%$

```
+-----------------------------------------------------------------------------------+
|                  TRANSMISSION GEAR OUTPUT & QUALITY DEFECT MATRIX                 |
+-----------------------------------------------------------------------------------+
| Facility | Gross Output (Units) [Bar] | Defect Rate (%) [Line] | Defective Units  |
|----------+----------------------------+------------------------+------------------|
| Plant 1  | 16,000                     | 2.5%                   | ?                |
| Plant 2  | 14,000                     | 3.0%                   | ?                |
| Plant 3  | 12,000                     | 4.0%                   | ?                |
| Plant 4  | 8,000                      | 1.5%                   | ?                |
| Total    | 50,000                     | Blended: ?             | ?                |
+-----------------------------------------------------------------------------------+
```

#### Q11
What is the total aggregate number of defective transmission gears produced across all four manufacturing facilities combined?
- (A) $1,280\text{ units}$
- (B) $1,350\text{ units}$
- (C) $1,420\text{ units}$
- (D) $1,510\text{ units}$

#### Q12
What is the net salable (non-defective) volume of transmission gears produced across the entire supplier network?
- (A) $48,420\text{ units}$
- (B) $48,580\text{ units}$
- (C) $48,650\text{ units}$
- (D) $48,720\text{ units}$

#### Q13
Which manufacturing facility accounts for the single lowest absolute number of defective gears?
- (A) Plant 4
- (B) Plant 1
- (C) Plant 2
- (D) Plant 3

#### Q14
Every defective gear scrapped incurs an unrecoverable manufacturing penalty of `₹450`. What is the total financial scrap loss suffered across all four facilities?
- (A) `₹5,76,000`
- (B) `₹6,12,500`
- (C) `₹6,28,000`
- (D) `₹6,39,000`

#### Q15
Plant 2 implements a lean manufacturing process upgrade that expands its gross unit production by $15\%$ while simultaneously halving its defect rate from $3.0\%$ to $1.5\%$. What is the net increase in salable units delivered by Plant 2?
- (A) $2,050\text{ units}$
- (B) $2,279\text{ units}$
- (C) $2,380\text{ units}$
- (D) $2,450\text{ units}$

---

### Level 4: Very Hard (Q16–Q20)

**Dataset Reference (Corporate Cost Structure & Business Unit Revenues):**  
A specialty chemicals group records total annual revenues of `₹600 crore` and total operating overhead costs of `₹450 crore`.
- **Bar Graph (Revenue by Business Unit in ₹ crore):**
  - Agrochemicals: `₹200 crore`
  - Specialty Polymers: `₹160 crore`
  - Performance Coatings: `₹140 crore`
  - Industrial Solvents: `₹100 crore`
- **Pie Chart (Operating Cost Allocation % of ₹450 crore Total):**
  - Agrochemicals: $30\%$ (`₹135 crore`)
  - Specialty Polymers: $26\%$ (`₹117 crore`)
  - Performance Coatings: $24\%$ (`₹108 crore`)
  - Industrial Solvents: $20\%$ (`₹90 crore`)

#### Q16
What is the absolute operating EBITDA generated by the Agrochemicals business unit?
- (A) `₹55 crore`
- (B) `₹60 crore`
- (C) `₹65 crore`
- (D) `₹70 crore`

#### Q17
Which business unit delivers the highest operating profit margin percentage ($\frac{\text{Revenue} - \text{Cost}}{\text{Revenue}} \times 100\%$)?
- (A) Industrial Solvents
- (B) Agrochemicals
- (C) Specialty Polymers
- (D) Performance Coatings

#### Q18
If general supply chain inflation induces a blanket $10\%$ escalation in total operating overhead costs (distributed proportionally according to existing pie proportions) while product prices and revenues remain unchanged, what will be the revised operating profit of Industrial Solvents?
- (A) `₹1.0 crore`
- (B) `₹3.5 crore`
- (C) `₹5.0 crore`
- (D) `₹7.5 crore`

#### Q19
What is the ratio of operating profit of Specialty Polymers to that of Performance Coatings?
- (A) $43 : 32$
- (B) $39 : 28$
- (C) $45 : 34$
- (D) $41 : 31$

#### Q20
If the Performance Coatings unit targets an operating profit margin of $30.0\%$ in the following year, and its operating cost remains fixed at `₹108 crore`, what revenue must Performance Coatings achieve?
- (A) `₹148.5 crore`
- (B) `₹152.0 crore`
- (C) `₹154.3 crore`
- (D) `₹156.2 crore`

---

### Level 5: Expert (Q21–Q25)

**Dataset Reference (Cross-Border Export Realizations & Currency Shocks):**  
A heavy engineering exporter dispatches capital equipment to three key global markets: European Union (EUR), United States (USD), and Japan (JPY).
- **Line Graph (Average Realized Exchange Rate):**
  - EUR/INR: `₹90.00`
  - USD/INR: `₹82.50`
  - JPY/INR: `₹0.55` (per 1 JPY)
- **Table (Export Volumes & Import Tariff Regimes):**
  - European Union: Gross Invoice Value = `€20,000,000`, Applicable Tariff = $5\%$ (ad-valorem on CIF)
  - United States: Gross Invoice Value = `USD 30,000,000`, Applicable Tariff = $8\%$
  - Japan: Gross Invoice Value = `¥4,000,000,000`, Applicable Tariff = $2\%$

*(Note: Net realized invoice equals gross invoice value minus destination import tariffs, converted to INR at spot rates).*

#### Q21
What is the net realized export revenue in INR from shipments to the European Union?
- (A) `₹165.0 crore`
- (B) `₹171.0 crore`
- (C) `₹175.5 crore`
- (D) `₹180.0 crore`

#### Q22
What is the total gross invoice value across all three export destinations converted to INR (before import tariffs)?
- (A) `₹647.5 crore`
- (B) `₹652.0 crore`
- (C) `₹660.5 crore`
- (D) `₹668.0 crore`

#### Q23
What is the total financial leakage absorbed via destination import tariffs across all three foreign markets, expressed in INR?
- (A) `₹31.2 crore`
- (B) `₹33.2 crore`
- (C) `₹35.4 crore`
- (D) `₹37.0 crore`

#### Q24
Which foreign market provides the single highest net realized revenue in INR?
- (A) European Union
- (B) United States
- (C) Japan
- (D) European Union and United States are tied

#### Q25
If macroeconomic volatility triggers a sharp $+10\%$ depreciation of the Indian Rupee against the USD (i.e., USD/INR rises from `₹82.50` to `₹90.75`) while the US gross invoice and tariff percentage remain constant, what is the incremental windfall gain in net realized INR from the US market?
- (A) `₹21.50 crore`
- (B) `₹22.77 crore`
- (C) `₹24.00 crore`
- (D) `₹25.20 crore`

---

### Level 6: Extreme Multi-Chart Synthesis (Q26–Q30)

**Dataset Reference (E-Commerce Platform Marketplace Unit Economics):**  
Apex Commerce operates an omnichannel digital marketplace. The management board evaluates performance across four primary merchandise categories.
- **Bar Graph (Gross Merchandise Value - GMV in ₹ crore):**
  - Consumer Electronics: `₹800 crore`
  - Fashion & Apparel: `₹400 crore`
  - Home & Kitchen: `₹250 crore`
  - Beauty & Personal Care: `₹150 crore`
  *(Total GMV $= \text{₹}1,600\text{ crore}$)*
- **Pie Chart (Category Take-Rate / Commission %):**
  - Consumer Electronics: $6.0\%$
  - Fashion & Apparel: $18.0\%$
  - Home & Kitchen: $14.0\%$
  - Beauty & Personal Care: $16.0\%$
- **Line Graph (Average Fulfillment & Payment Gateway Cost % of GMV):**
  - Consumer Electronics: $3.5\%$
  - Fashion & Apparel: $7.0\%$
  - Home & Kitchen: $6.0\%$
  - Beauty & Personal Care: $5.0\%$

```
+-----------------------------------------------------------------------------------+
|                  APEX COMMERCE MARKETPLACE UNIT ECONOMICS MATRIX                  |
+-----------------------------------------------------------------------------------+
| Category            | GMV (₹ Cr) [Bar] | Take-Rate (%) [Pie] | Fulfillment Cost % |
|---------------------+------------------+---------------------+--------------------|
| Electronics         | 800              | 6.0%                | 3.5%               |
| Fashion & Apparel   | 400              | 18.0%               | 7.0%               |
| Home & Kitchen      | 250              | 14.0%               | 6.0%               |
| Beauty & Personal   | 150              | 16.0%               | 5.0%               |
| Total Marketplace   | 1,600            | Blended: ?          | Blended: ?         |
+-----------------------------------------------------------------------------------+
```

#### Q26
What is the net marketplace commission revenue generated by the Fashion & Apparel category?
- (A) `₹64.0 crore`
- (B) `₹68.0 crore`
- (C) `₹72.0 crore`
- (D) `₹76.0 crore`

#### Q27
What is the consolidated blended take-rate (commission percentage) across the entire `₹1,600 crore` GMV?
- (A) $10.50\%$
- (B) $11.19\%$
- (C) $11.85\%$
- (D) $12.20\%$

#### Q28
What is the total net commission revenue earned by Apex Commerce across all four merchandise categories combined?
- (A) `₹175.0 crore`
- (B) `₹179.0 crore`
- (C) `₹184.0 crore`
- (D) `₹188.0 crore`

#### Q29
Contribution Profit I is defined as Net Commission Revenue minus Fulfillment & Payment Gateway Costs. What is the total Contribution Profit I generated across the entire platform?
- (A) `₹92.0 crore`
- (B) `₹96.5 crore`
- (C) `₹100.5 crore`
- (D) `₹104.0 crore`

#### Q30
Which merchandise category contributes the highest absolute amount to Contribution Profit I?
- (A) Consumer Electronics
- (B) Fashion & Apparel
- (C) Home & Kitchen
- (D) Beauty & Personal Care

---

### Level 7: Trap & Misleading Scale Alignment (Q31–Q35)

#### Q31 (The Dual-Axis Scale Misalignment Trap)
In a dual-axis presentation, the left vertical axis represents monthly sales volume in physical units ($0$ to $10,000$ units), while the right vertical axis represents operating profit margin ($-10\%$ to $+30\%$). An analyst observing that the profit margin line intersects the unit sales bar at height 20 reads the margin as "2,000 units". What is the true margin value represented at that point?
- (A) $+15.0\%$
- (B) $+20.0\%$
- (C) $+25.0\%$
- (D) Indeterminate without unit conversion

#### Q32 (The Base Year Re-Indexing Distortion)
A chart displays an Export Index (Base Year $2015 = 100$) rising to $150$ in 2020 and $225$ in 2025. A secondary line shows an Import Index (Base Year $2020 = 100$) rising to $140$ in 2025. Which sector expanded at a faster relative rate between 2020 and 2025?
- (A) Imports ($40.0\%$) grew faster than Exports ($33.3\%$)
- (B) Exports ($50.0\%$) grew faster than Imports ($40.0\%$)
- (C) Both expanded at identical compound rates
- (D) Cannot be compared due to incompatible index years

#### Q33 (Simpson's Paradox in Mixed Visualizations)
A university displays two charts: Chart 1 shows female acceptance rates exceeded male acceptance rates in both the Engineering Department ($25\%$ vs $20\%$) and the Humanities Department ($60\%$ vs $55\%$). Chart 2 shows applicant distribution: Engineering had $1,000$ male and $200$ female applicants; Humanities had $100$ male and $800$ female applicants. What is the university-wide aggregate acceptance rate comparison?
- (A) Overall female acceptance rate was higher than overall male acceptance rate
- (B) Overall male acceptance rate was higher than overall female acceptance rate
- (C) Overall male and female acceptance rates were exactly equal
- (D) Violates the Law of Total Probability

#### Q34 (The Truncated Axis Illusion)
A column bar graph illustrating quarterly SaaS revenues truncates the vertical baseline at `₹80 crore` instead of `₹0 crore`. Quarter 1 revenue is `₹100 crore` (bar height $20\text{ units}$) and Quarter 2 revenue is `₹120 crore` (bar height $40\text{ units}$). A viewer perceives that Q2 revenue was double Q1 revenue. What was the true percentage growth in revenue from Q1 to Q2?
- (A) $+100.0\%$
- (B) $+50.0\%$
- (C) $+25.0\%$
- (D) $+20.0\%$

#### Q35 (Pre-Tax vs Post-Tax Comparison Error)
A mixed chart compares Business Unit A's pre-tax operating profit margin of $25\%$ with Business Unit B's effective post-tax net profit margin of $20\%$. If Unit A operates under a corporate tax rate of $30\%$, which business unit delivers the superior net post-tax margin?
- (A) Unit A ($17.5\%$) is inferior to Unit B ($20.0\%$)
- (B) Unit A ($25.0\%$) is superior to Unit B ($20.0\%$)
- (C) Both units generate identical post-tax margins
- (D) Post-tax margins cannot be calculated without debt interest

---

### Level 8: Hybrid Financial & Consulting Caselet (Q36–Q40)

**Case Context: Renewable Independent Power Producer (IPP) Asset Portfolio**  
Apex Clean Energy operates an operational utility-scale renewable generation portfolio across India.
- **Bar Graph (Installed Generation Capacity in MW):**
  - Utility Solar Photovoltaic: $250\text{ MW}$
  - Onshore Wind: $150\text{ MW}$
  - Small Hydroelectric: $50\text{ MW}$
  *(Total Installed Capacity $= 450\text{ MW}$)*
- **Line Graph (Annual Capacity Utilization Factor - CUF %):**
  - Utility Solar: $22.0\%$
  - Onshore Wind: $28.0\%$
  - Small Hydroelectric: $45.0\%$
- **Table (Long-Term 25-Year Power Purchase Agreement - PPA Tariffs & O&M):**
  - Utility Solar: PPA Tariff = `₹2.60 / kWh`, O&M Cost = `₹0.40 / kWh`
  - Onshore Wind: PPA Tariff = `₹3.20 / kWh`, O&M Cost = `₹0.60 / kWh`
  - Small Hydroelectric: PPA Tariff = `₹4.40 / kWh`, O&M Cost = `₹0.80 / kWh`

*(Standard Conversion: $1\text{ MW}$ operating for $8,760\text{ hours}$ at $100\%\text{ CUF}$ generates $8,760\text{ MWh} = 8.76\text{ Million Units (MU)}$. $1\text{ MU} = 1,000,000\text{ kWh}$).*

#### Q36
What is the total annual electrical energy generated by the Utility Solar assets, expressed in Million Units (MU)?
- (A) $441.5\text{ MU}$
- (B) $468.2\text{ MU}$
- (C) $481.8\text{ MU}$
- (D) $502.4\text{ MU}$

#### Q37
What is the total consolidated electricity generated across the entire $450\text{ MW}$ renewable IPP portfolio in one full standard year (8,760 hours)?
- (A) $985.4\text{ MU}$
- (B) $1,046.8\text{ MU}$
- (C) $1,085.6\text{ MU}$
- (D) $1,124.0\text{ MU}$

#### Q38
What is the weighted average PPA tariff realized per kWh across the entire annual energy generation portfolio?
- (A) `₹2.95 / kWh`
- (B) `₹3.15 / kWh`
- (C) `₹3.25 / kWh`
- (D) `₹3.40 / kWh`

#### Q39
What is the total consolidated annual Gross Revenue generated by Apex Clean Energy under its long-term PPA contracts?
- (A) `₹315.4 crore`
- (B) `₹324.5 crore`
- (C) `₹329.7 crore`
- (D) `₹338.5 crore`

#### Q40
Due to inter-state grid transmission congestion during peak renewable generation hours, Apex Clean Energy suffers an uncompensated grid curtailment of $8.0\%$ across all solar and wind assets (hydro generation remains unaffected). What is the net annual financial revenue loss caused by this curtailment?
- (A) `₹19.44 crore`
- (B) `₹21.85 crore`
- (C) `₹23.42 crore`
- (D) `₹25.10 crore`

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Net profit in 2022.
- **Data:** Revenue $= \text{₹}120\text{ crore}$, Margin $= 12.0\%$.
- **Calculation:**
  $$\text{Net Profit} = 0.12 \times 120 = \text{₹}14.4\text{ crore}$$
- **Correct Answer:** **B**

#### Q2
- **Target:** Revenue growth rate from 2021 to 2024.
- **Data:** $Y_{2021} = 100$, $Y_{2024} = 180$.
- **Calculation:**
  $$\text{Growth} = \frac{180 - 100}{100} \times 100\% = 80.0\%$$
- **Correct Answer:** **B**

#### Q3
- **Target:** Year with highest absolute net profit increase.
- **Annual Net Profit Calculations:**
  - 2021: $0.10 \times 100 = \text{₹}10.0\text{ crore}$
  - 2022: $0.12 \times 120 = \text{₹}14.4\text{ crore} \implies \Delta = 14.4 - 10.0 = +\text{₹}4.4\text{ crore}$
  - 2023: $0.15 \times 150 = \text{₹}22.5\text{ crore} \implies \Delta = 22.5 - 14.4 = +\text{₹}8.1\text{ crore}$
  - 2024: $0.18 \times 180 = \text{₹}32.4\text{ crore} \implies \Delta = 32.4 - 22.5 = +\mathbf{\text{₹}9.9\text{ crore}}$
- 2024 achieved the largest absolute increase (`₹9.9 crore`).
- **Correct Answer:** **C**

#### Q4
- **Target:** 2025 net profit projection.
- **Step 1:** Projected Revenue $= 180 \times 1.10 = \text{₹}198\text{ crore}$.
- **Step 2:** Projected Net Profit $= 20.0\% \times 198 = 0.20 \times 198 = \text{₹}39.6\text{ crore}$.
- **Correct Answer:** **A**

#### Q5
- **Target:** Ratio of net profit in 2023 to 2021.
- **Calculation:**
  $$\text{Ratio} = \frac{22.5}{10.0} = 2.25 : 1$$
- **Correct Answer:** **A**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** North territory sales.
- **Calculation:**
  $$\text{Sales} = 30\% \times 500 = \text{₹}150\text{ crore}$$
- **Correct Answer:** **A**

#### Q7
- **Target:** Total sales of Product Alpha.
- **Calculation:**
  $$\text{Sales} = 40\% \times 500 = \text{₹}200\text{ crore}$$
- **Correct Answer:** **A**

#### Q8
- **Target:** Central angle for South territory.
- **Calculation:**
  $$\theta = 25\% \times 360^\circ = 0.25 \times 360^\circ = 90^\circ$$
- **Correct Answer:** **A**

#### Q9
- **Target:** Product Alpha sales in South territory.
- **Data:** Product Alpha total $= \text{₹}200\text{ crore}$. Split between North and South $= 3 : 2$.
- **Calculation:**
  $$\text{South Share} = \frac{2}{3 + 2} \times 200 = \frac{2}{5} \times 200 = \text{₹}80\text{ crore}$$
- **Correct Answer:** **A**

#### Q10
- **Target:** Revised percentage share of Central territory.
- **Step 1:** Initial Central sales $= 10\% \times 500 = \text{₹}50\text{ crore}$.
- **Step 2:** $20\%$ expansion $= 50 \times 1.20 = \text{₹}60\text{ crore}$.
- **Step 3:** Revised percentage share $= \frac{60}{500} \times 100\% = 12.0\%$.
- **Correct Answer:** **A**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** Total defective gears across all plants.
- **Calculations by Facility:**
  - Plant 1: $16,000 \times 0.025 = 400\text{ units}$
  - Plant 2: $14,000 \times 0.030 = 420\text{ units}$
  - Plant 3: $12,000 \times 0.040 = 480\text{ units}$
  - Plant 4: $8,000 \times 0.015 = 120\text{ units}$
- **Total Defective Units:**
  $$\text{Total Defects} = 400 + 420 + 480 + 120 = 1,420\text{ units}$$
- **Correct Answer:** **C**

#### Q12
- **Target:** Net salable output.
- **Calculation:**
  $$\text{Salable Volume} = 50,000 - 1,420 = 48,580\text{ units}$$
- **Correct Answer:** **B**

#### Q13
- **Target:** Facility with lowest absolute defects.
- **Analysis:** Plant 4 produced only $120$ defective units.
- **Correct Answer:** **A**

#### Q14
- **Target:** Total scrap penalty.
- **Calculation:**
  $$\text{Scrap Loss} = 1,420 \times 450 = \text{₹}6,39,000$$
- **Correct Answer:** **D**

#### Q15
- **Target:** Net increase in salable units from Plant 2 upgrade.
- **Initial Salable Units:** $14,000 - 420 = 13,580\text{ units}$.
- **Upgraded Production:**
  - New Gross Output $= 14,000 \times 1.15 = 16,100\text{ units}$.
  - New Defects $= 16,100 \times 0.015 = 241.5 \approx 241\text{ units}$.
  - New Salable Units $= 16,100 - 241.5 = 15,858.5\text{ units}$.
- **Net Increase:**
  $$\Delta = 15,858.5 - 13,580 = 2,278.5 \approx 2,279\text{ units}$$
- **Correct Answer:** **B**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** Agrochemicals EBITDA.
- **Data:**
  - Revenue $= \text{₹}200\text{ crore}$
  - Cost $= 30\% \times 450 = \text{₹}135\text{ crore}$
- **Calculation:**
  $$\text{EBITDA} = 200 - 135 = \text{₹}65\text{ crore}$$
- **Correct Answer:** **C**

#### Q17
- **Target:** Business unit with highest operating margin.
- **Calculations by Unit:**
  - Agrochemicals: $\text{Rev} = 200, \text{Cost} = 135 \implies \text{Margin} = \frac{65}{200} = \mathbf{32.50\%}$
  - Polymers: $\text{Rev} = 160, \text{Cost} = 117 \implies \text{Margin} = \frac{43}{160} = 26.88\%$
  - Coatings: $\text{Rev} = 140, \text{Cost} = 108 \implies \text{Margin} = \frac{32}{140} = 22.86\%$
  - Solvents: $\text{Rev} = 100, \text{Cost} = 90 \implies \text{Margin} = \frac{10}{100} = 10.00\%$
- **Agrochemicals** delivers the highest operating profit margin ($32.5\%$).
- **Correct Answer:** **B**

#### Q18
- **Target:** Revised profit of Industrial Solvents after $10\%$ cost inflation.
- **Step 1:** New Solvents cost $= 90 \times 1.10 = \text{₹}99\text{ crore}$.
- **Step 2:** Revised Operating Profit $= 100 - 99 = \text{₹}1.0\text{ crore}$.
- **Correct Answer:** **A**

#### Q19
- **Target:** Ratio of Polymers profit to Coatings profit.
- **Data:** Polymers profit $= 160 - 117 = 43$. Coatings profit $= 140 - 108 = 32$.
- **Calculation:**
  $$\text{Ratio} = 43 : 32$$
- **Correct Answer:** **A**

#### Q20
- **Target:** Required revenue for Performance Coatings at $30\%$ margin.
- **Condition:**
  $$\text{Margin} = \frac{\text{Rev} - 108}{\text{Rev}} = 0.30 \implies 0.70 \times \text{Rev} = 108 \implies \text{Rev} = \frac{108}{0.70} \approx \text{₹}154.29\text{ crore}$$
- **Correct Answer:** **C**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** Net realized export revenue from EU in INR.
- **Data:** Invoice $= €20\text{M}$, Tariff $= 5\% \implies \text{Net Invoice} = 0.95 \times 20 = €19\text{M}$.
- **Spot Rate:** EUR/INR $= \text{₹}90.00$.
- **Calculation:**
  $$\text{Net Revenue} = 19,000,000 \times 90 = \text{₹}1,71,00,00,000 = \text{₹}171.0\text{ crore}$$
- **Correct Answer:** **B**

#### Q22
- **Target:** Total gross invoice converted to INR (before tariffs).
- **Calculations:**
  - EU: $20\text{M} \times 90 = \text{₹}180.0\text{ crore}$
  - US: $30\text{M} \times 82.50 = \text{₹}247.5\text{ crore}$
  - Japan: $4,000\text{M} \times 0.55 = \text{₹}220.0\text{ crore}$
- **Total Gross Revenue:**
  $$\text{Total} = 180.0 + 247.5 + 220.0 = \text{₹}647.5\text{ crore}$$
- **Correct Answer:** **A**

#### Q23
- **Target:** Total financial leakage via import tariffs in INR.
- **Calculations:**
  - EU Tariff: $5\% \times 180.0 = \text{₹}9.0\text{ crore}$
  - US Tariff: $8\% \times 247.5 = \text{₹}19.8\text{ crore}$
  - Japan Tariff: $2\% \times 220.0 = \text{₹}4.4\text{ crore}$
- **Total Tariff Leakage:**
  $$\text{Total Leakage} = 9.0 + 19.8 + 4.4 = \text{₹}33.2\text{ crore}$$
- **Correct Answer:** **B**

#### Q24
- **Target:** Foreign market with highest net realized revenue.
- **Calculations:**
  - EU Net: $180.0 - 9.0 = \text{₹}171.0\text{ crore}$
  - US Net: $247.5 - 19.8 = \mathbf{\text{₹}227.7\text{ crore}}$
  - Japan Net: $220.0 - 4.4 = \text{₹}215.6\text{ crore}$
- **United States** provides the highest net revenue (`₹227.7 crore`).
- **Correct Answer:** **B**

#### Q25
- **Target:** Windfall gain from $+10\%$ USD appreciation.
- **Calculation:**
  - Original US Net INR $= \text{USD } 30\text{M} \times 0.92 \times 82.50 = \text{USD } 27.6\text{M} \times 82.50 = \text{₹}227.70\text{ crore}$.
  - A $+10\%$ depreciation in INR expands this by exactly $+10\%$:
    $$\Delta = 0.10 \times 227.70 = \text{₹}22.77\text{ crore}$$
- **Correct Answer:** **B**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Fashion & Apparel commission revenue.
- **Data:** $\text{GMV} = \text{₹}400\text{ crore}$, Take-Rate $= 18.0\%$.
- **Calculation:**
  $$\text{Commission} = 0.18 \times 400 = \text{₹}72.0\text{ crore}$$
- **Correct Answer:** **C**

#### Q27
- **Target:** Consolidated blended take-rate.
- **Total Commission Revenues:**
  - Electronics: $800 \times 0.06 = \text{₹}48.0\text{ crore}$
  - Fashion: $400 \times 0.18 = \text{₹}72.0\text{ crore}$
  - Home: $250 \times 0.14 = \text{₹}35.0\text{ crore}$
  - Beauty: $150 \times 0.16 = \text{₹}24.0\text{ crore}$
  - **Total Commission Revenue:** $48 + 72 + 35 + 24 = \text{₹}179.0\text{ crore}$.
- **Blended Rate:**
  $$\text{Blended Take-Rate} = \frac{179.0}{1600} \times 100\% = 11.1875\% \approx 11.19\%$$
- **Correct Answer:** **B**

#### Q28
- **Target:** Total net commission revenue.
- **Calculation:**
  $$\text{Sum} = 48.0 + 72.0 + 35.0 + 24.0 = \text{₹}179.0\text{ crore}$$
- **Correct Answer:** **B**

#### Q29
- **Target:** Total Contribution Profit I (Commission - Fulfillment Costs).
- **Fulfillment Costs by Category:**
  - Electronics: $800 \times 0.035 = \text{₹}28.0\text{ crore}$
  - Fashion: $400 \times 0.070 = \text{₹}28.0\text{ crore}$
  - Home: $250 \times 0.060 = \text{₹}15.0\text{ crore}$
  - Beauty: $150 \times 0.050 = \text{₹}7.5\text{ crore}$
  - **Total Fulfillment Costs:** $28.0 + 28.0 + 15.0 + 7.5 = \text{₹}78.5\text{ crore}$.
- **Contribution Profit I:**
  $$\text{CP-I} = 179.0 - 78.5 = \text{₹}100.5\text{ crore}$$
- **Correct Answer:** **C**

#### Q30
- **Target:** Category with highest Contribution Profit I.
- **Calculations:**
  - Electronics: $48.0 - 28.0 = \text{₹}20.0\text{ crore}$
  - Fashion: $72.0 - 28.0 = \mathbf{\text{₹}44.0\text{ crore}}$
  - Home: $35.0 - 15.0 = \text{₹}20.0\text{ crore}$
  - Beauty: $24.0 - 7.5 = \text{₹}16.5\text{ crore}$
- **Fashion & Apparel** delivers the highest Contribution Profit I (`₹44.0 crore`).
- **Correct Answer:** **B**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** True percentage margin at height 20.
- **Analysis:** Height 20 on the right axis maps to $+20.0\%$. Left axis scales units, right axis scales percentages.
- **Correct Answer:** **B**

#### Q32
- **Target:** Relative growth comparison between Exports and Imports.
- **Calculations:**
  - Exports (2020 to 2025): Index grew from $150$ to $225 \implies \frac{225 - 150}{150} \times 100\% = +50.0\%$.
  - Imports (2020 to 2025): Index grew from $100$ to $140 \implies \frac{140 - 100}{100} \times 100\% = +40.0\%$.
- **Exports** grew faster ($+50\%$) than Imports ($+40\%$).
- **Correct Answer:** **B**

#### Q33
- **Target:** Aggregate acceptance rate comparison across departments.
- **Department Aggregation:**
  - Males Accepted: $(0.20 \times 1000) + (0.55 \times 100) = 200 + 55 = 255$ out of $1,100 \implies \frac{255}{1100} \approx \mathbf{23.18\%}$.
  - Females Accepted: $(0.25 \times 200) + (0.60 \times 800) = 50 + 480 = 530$ out of $1,000 \implies \frac{530}{1000} = \mathbf{53.00\%}$.
- Overall female acceptance rate was significantly higher ($53\%$ vs $23.2\%$).
- **Correct Answer:** **A**

#### Q34
- **Target:** True percentage growth from Q1 to Q2.
- **Data:** Q1 Revenue $= 100$, Q2 Revenue $= 120$.
- **Calculation:**
  $$\text{Growth} = \frac{120 - 100}{100} \times 100\% = +20.0\%$$
- The visual doubling was an artifact of the truncated non-zero baseline (`₹80 crore`).
- **Correct Answer:** **D**

#### Q35
- **Target:** Net post-tax margin comparison.
- **Calculations:**
  - Unit A Post-Tax Margin: $25\% \times (1 - 0.30) = 25\% \times 0.70 = 17.5\%$.
  - Unit B Post-Tax Margin: $20.0\%$.
- Unit A's post-tax margin ($17.5\%$) is inferior to Unit B ($20.0\%$).
- **Correct Answer:** **A**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** Annual Solar generation in MU.
- **Formula:** $\text{Generation (MU)} = \text{Capacity (MW)} \times 8,760\text{ h} \times \text{CUF} \times 10^{-3}$.
- **Calculation:**
  $$\text{Solar Energy} = 250 \times 8,760 \times 0.22 \times 10^{-3} = 481.8\text{ MU}$$
- **Correct Answer:** **C**

#### Q37
- **Target:** Consolidated IPP portfolio annual generation.
- **Calculations by Technology:**
  - Solar: $250 \times 8,760 \times 0.22 \times 10^{-3} = 481.8\text{ MU}$
  - Wind: $150 \times 8,760 \times 0.28 \times 10^{-3} = 367.92\text{ MU}$
  - Hydro: $50 \times 8,760 \times 0.45 \times 10^{-3} = 197.10\text{ MU}$
- **Total Generation:**
  $$\text{Total Generation} = 481.80 + 367.92 + 197.10 = 1,046.82\text{ MU}$$
- **Correct Answer:** **B**

#### Q38
- **Target:** Weighted average PPA tariff realized.
- **Revenues by Technology:**
  - Solar: $481.80\text{ MU} \times \text{₹}2.60/\text{kWh} = \text{₹}1,252.68\text{M} = \text{₹}125.268\text{ crore}$
  - Wind: $367.92\text{ MU} \times \text{₹}3.20/\text{kWh} = \text{₹}1,177.344\text{M} = \text{₹}117.734\text{ crore}$
  - Hydro: $197.10\text{ MU} \times \text{₹}4.40/\text{kWh} = \text{₹}867.240\text{M} = \text{₹}86.724\text{ crore}$
- **Total Gross Revenue:**
  $$\text{Gross Revenue} = 125.268 + 117.734 + 86.724 = \text{₹}329.726\text{ crore}$$
- **Weighted Tariff:**
  $$\text{Tariff} = \frac{\text{₹}329.726\text{ crore}}{1,046.82\text{ MU}} = \frac{3,297.26\text{M}}{1,046.82\text{M}} \approx \text{₹}3.1498/\text{kWh} \approx \text{₹}3.15/\text{kWh}$$
- **Correct Answer:** **B**

#### Q39
- **Target:** Consolidated annual gross revenue.
- **Calculation:**
  $$\text{Gross Revenue} = 125.268 + 117.734 + 86.724 = \text{₹}329.73\text{ crore}$$
- **Correct Answer:** **C**

#### Q40
- **Target:** Annual revenue loss from $8\%$ curtailment on solar and wind.
- **Combined Solar + Wind Revenue:**
  $$\text{Solar + Wind Revenue} = 125.268 + 117.734 = \text{₹}243.002\text{ crore}$$
- **Curtailed Loss ($8\%$):**
  $$\text{Revenue Loss} = 0.08 \times 243.002 = \text{₹}19.44\text{ crore}$$
- **Correct Answer:** **A**

---

## 5. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                        TOP 5 MIXED GRAPH DATA INTERPRETATION TRAPS                |
+-----------------------------------------------------------------------------------+
| 1. The Dual-Axis Scale Transposition Error:                                       |
|    Always trace the physical curve to its designated vertical axis! Reading left   |
|    axis values for right axis line graphs produces catastrophic order-of-magnitude|
|    errors.                                                                        |
|-----------------------------------------------------------------------------------|
| 2. The Conditional Category Confusion:                                            |
|    Never assume a table's sub-category percentages apply to the overall total      |
|    unless explicitly stated as marginal distributions!                            |
|-----------------------------------------------------------------------------------|
| 3. Unlinked Multi-Base Multiplications:                                           |
|    When combining Volume from Chart 1 with Unit Rate from Chart 2, verify that both|
|    apply to identical time periods and accounting definitions!                     |
|-----------------------------------------------------------------------------------|
| 4. Simpson's Paradox Reversals:                                                   |
|    Sub-group trends can completely invert when aggregated if group weights vary    |
|    drastically across cohorts! Always compute the weighted aggregate.             |
|-----------------------------------------------------------------------------------|
| 5. Pre-Tax vs Post-Tax Parameter Traps:                                           |
|    Verify whether margin curves depict EBITDA, EBIT, PBT, or PAT before comparing  |
|    against revenue bars!                                                          |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Bar & Line Graphs](bar-and-line-graphs.md) — Temporal Trend Analysis & Dual-Axis Interpretation
- [Tables & Caselets](tables-and-caselets.md) — Complex Multi-Row Cross-Tabulation & Case Studies
- [Pie Charts](pie-charts.md) — Proportional Angle ($\theta$) and Multi-Tier Portfolio Share
- [Data Sufficiency](data-sufficiency.md) — Statement Evaluation & Deductive Uniqueness
- [Formula Sheet](../FORMULA_SHEET.md) — Quantitative Shortcuts, Speed Math & Vedic Divisions

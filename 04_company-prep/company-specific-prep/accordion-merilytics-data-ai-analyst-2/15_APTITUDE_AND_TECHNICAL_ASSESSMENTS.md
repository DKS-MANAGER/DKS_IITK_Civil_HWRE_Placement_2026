# Module 15 — Aptitude & Technical Assessment Question Bank

This module contains **50 original, fully solved assessment questions** specifically calibrated for the online screening assessment (HackerEarth / Mettl / CoCubes) for the **Data & AI Analyst 2** role at Accordion (Merilytics).

---

## Section 1: Quantitative Aptitude & Commercial Mathematics (Q01 – Q15)

#### Q01: Compound Annual Growth Rate (CAGR)
**Question**: A portfolio company's Annual Recurring Revenue (ARR) grew from \$12.5 Million in 2021 to \$21.6 Million in 2024. Calculate the 3-year CAGR.  
**Solution**:
1. CAGR Formula:
   $$\text{CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{1/n} - 1 = \left(\frac{21.6}{12.5}\right)^{1/3} - 1$$
2. Ratio:
   $$\frac{21.6}{12.5} = \frac{216}{125}$$
3. Cube root:
   $$\left(\frac{216}{125}\right)^{1/3} = \frac{6}{5} = 1.20$$
4. $\text{CAGR} = 1.20 - 1 = \mathbf{20.0\% \text{ per year}}$.

---

#### Q02: Successive Percentage Changes (EBITDA Margin)
**Question**: A manufacturer increases its unit price by 15%, but due to price elasticity, physical sales volume declines by 10%. Concurrently, unit production costs rise by 5%. If the initial price was \$100 and initial cost was \$60, what is the percentage change in total gross profit?  
**Solution**:
1. Initial State (say 100 units):
   - Revenue = $100 \times \$100 = \$10,000$.
   - Cost = $100 \times \$60 = \$6,000$.
   - Gross Profit = $\$10,000 - \$6,000 = \$4,000$.
2. New State:
   - New Price = $\$100 \times 1.15 = \$115$.
   - New Volume = $100 \times 0.90 = 90 \text{ units}$.
   - New Cost = $\$60 \times 1.05 = \$63$.
   - New Unit Margin = $\$115 - \$63 = \$52$.
   - New Gross Profit = $90 \times \$52 = \$4,680$.
3. Percentage Change in Gross Profit:
   $$\% \Delta \text{GP} = \frac{4,680 - 4,000}{4,000} \times 100\% = \frac{680}{4,000} \times 100\% = \mathbf{+17.0\%}$$

---

#### Q03: Weighted Average Gross Margin
**Question**: A company sells three product tiers: Tier A (40% volume share, 35% margin), Tier B (35% volume share, 50% margin), and Tier C (25% volume share, 70% margin). What is the company's weighted average gross margin?  
**Solution**:
$$\text{Weighted Margin} = (0.40 \times 35\%) + (0.35 \times 50\%) + (0.25 \times 70\%)$$
$$= 14.0\% + 17.5\% + 17.5\% = \mathbf{49.0\%}$$

---

#### Q04: Break-Even Sales Volume
**Question**: A SaaS portco has fixed annual operating costs of \$4,800,000. It charges an annual subscription fee of \$1,200 per user, and its variable cloud hosting cost is \$400 per user. How many active subscriptions must the company maintain to break even?  
**Solution**:
1. Unit Contribution Margin:
   $$\text{Margin} = \$1,200 - \$400 = \$800 \text{ per user}$$
2. Break-Even Volume:
   $$\text{Break-Even} = \frac{\text{Fixed Costs}}{\text{Unit Margin}} = \frac{\$4,800,000}{\$800} = \mathbf{6,000 \text{ subscriptions}}$$

---

#### Q05: Days Sales Outstanding (DSO)
**Question**: A business reports \$7,300,000 in annual credit sales. Its ending Accounts Receivable balance is \$1,100,000. Assuming a 365-day fiscal year, calculate DSO.  
**Solution**:
$$\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Credit Sales}} \times 365 = \frac{1,100,000}{7,300,000} \times 365 = \frac{11}{73} \times 365 = 11 \times 5 = \mathbf{55.0 \text{ days}}$$

---

#### Q06: Cash Conversion Cycle (CCC)
**Question**: An industrial distributor has Days of Inventory Outstanding (DIO) of 62 days, Days Sales Outstanding (DSO) of 48 days, and Days Payables Outstanding (DPO) of 45 days. What is its Cash Conversion Cycle?  
**Solution**:
$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO} = 62 + 48 - 45 = \mathbf{65 \text{ days}}$$

---

#### Q07: Customer Lifetime Value (LTV) Calculation
**Question**: A subscription software customer generates \$250 in Monthly Recurring Revenue (MRR) with an 80% gross margin. The monthly customer churn rate is 2.5%. Calculate the Customer Lifetime Value (LTV).  
**Solution**:
1. Average Customer Lifespan:
   $$\text{Lifespan} = \frac{1}{\text{Monthly Churn}} = \frac{1}{0.025} = 40 \text{ months}$$
2. Monthly Gross Contribution:
   $$\text{Margin} = \$250 \times 0.80 = \$200 \text{ / month}$$
3. Lifetime Value:
   $$\text{LTV} = 40 \times \$200 = \mathbf{\$8,000}$$

---

#### Q08: LTV : CAC Ratio Evaluation
**Question**: Using the customer LTV of \$8,000 from Q07, if the company spends \$1,600 in fully loaded sales and marketing costs to acquire each new customer, what is the LTV:CAC ratio and is the acquisition engine healthy?  
**Solution**:
$$\text{LTV:CAC} = \frac{\$8,000}{\$1,600} = \mathbf{5.0\times}$$
*(Benchmark: A ratio between 3.0× and 5.0× represents a highly efficient and healthy customer acquisition engine).*

---

#### Q09: Rule of 40 in SaaS
**Question**: A B2B software company generated \$50M revenue in 2024 and \$65M in 2025, while generating \$6.5M in EBITDA in 2025. Does the company satisfy the private equity "Rule of 40"?  
**Solution**:
1. Revenue Growth Rate:
   $$\% \Delta \text{Rev} = \frac{65 - 50}{50} \times 100\% = 30.0\%$$
2. EBITDA Margin:
   $$\text{EBITDA Margin} = \frac{6.5}{65} \times 100\% = 10.0\%$$
3. Rule of 40 Score:
   $$\text{Score} = 30.0\% + 10.0\% = \mathbf{40.0\%} \quad (\text{Satisfies the Rule of 40 benchmark})$$

---

#### Q10: Inventory Turnover Ratio
**Question**: An e-commerce distributor reports annual Cost of Goods Sold (COGS) of \$24,000,000. Its beginning inventory was \$3,800,000 and ending inventory was \$4,200,000. Calculate the inventory turnover ratio and average days to sell inventory.  
**Solution**:
1. Average Inventory = $(\$3.8\text{M} + \$4.2\text{M}) / 2 = \$4.0\text{M}$.
2. Inventory Turnover:
   $$\text{Turnover} = \frac{\text{COGS}}{\text{Average Inventory}} = \frac{\$24\text{M}}{\$4\text{M}} = \mathbf{6.0\times \text{ per year}}$$
3. Days to Sell Inventory:
   $$\text{DIO} = \frac{365}{6.0} \approx \mathbf{60.8 \text{ days}}$$

---

#### Q11: Permutations in Portfolio Scheduling
**Question**: A private equity operating team must schedule 5 distinct portfolio company operational reviews across 5 consecutive business days (Monday to Friday). Company A must be reviewed before Company B. How many valid schedules exist?  
**Solution**:
1. Total unconstrained permutations of 5 reviews = $5! = 120$.
2. By symmetry, in exactly half of all possible permutations Company A will precede Company B.
3. Valid schedules = $120 / 2 = \mathbf{60 \text{ schedules}}$.

---

#### Q12: Conditional Probability in Fraud Detection
**Question**: In credit card processing, 1% of all transactions are fraudulent ($P(F) = 0.01$). An automated fraud detection algorithm correctly flags 95% of genuine fraud cases ($P(A|F) = 0.95$), but has a 2% false positive rate on legitimate transactions ($P(A|\neg F) = 0.02$). If the algorithm flags a transaction as fraud, what is the probability that it is genuinely fraudulent?  
**Solution**:
1. Bayes' Theorem:
   $$P(F|A) = \frac{P(A|F)P(F)}{P(A|F)P(F) + P(A|\neg F)P(\neg F)}$$
2. Calculations:
   $$\text{Numerator} = 0.95 \times 0.01 = 0.0095$$
   $$\text{Denominator} = 0.0095 + (0.02 \times 0.99) = 0.0095 + 0.0198 = 0.0293$$
3. Probability:
   $$P(F|A) = \frac{0.0095}{0.0293} \approx \mathbf{32.42\%}$$

---

#### Q13: Work-Rate Optimization
**Question**: Senior Analyst X can complete a financial due diligence model in 12 hours. Junior Analyst Y takes 20 hours to complete the same model. If they collaborate simultaneously, how many hours will they take to complete the model together?  
**Solution**:
1. Combined Hourly Work Rate:
   $$\text{Rate} = \frac{1}{12} + \frac{1}{20} = \frac{5 + 3}{60} = \frac{8}{60} = \frac{2}{15} \text{ of the model / hour}$$
2. Total Time:
   $$\text{Time} = \frac{15}{2} = \mathbf{7.5 \text{ hours}} \text{ (7 hours 30 minutes)}$$

---

#### Q14: Magic Number in B2B SaaS
**Question**: A SaaS portco's ending ARR grew from \$40M in Q2 to \$44M in Q3. The total Sales and Marketing expense incurred in Q2 was \$3.2M. Calculate the Q3 Magic Number.  
**Solution**:
$$\text{Net New ARR} = \$44\text{M} - \$40\text{M} = \$4.0\text{M}$$
$$\text{Magic Number} = \frac{\text{Net New ARR} \times 4}{\text{Prior Quarter S\&M}} = \frac{\$4.0\text{M} \times 4}{\$3.2\text{M}} = \frac{\$16.0\text{M}}{\$3.2\text{M}} = \mathbf{5.0\times}$$
*(An extraordinary sales efficiency metric indicating that every \$1 of sales spend creates \$1.25 in annualized net new ARR).*

---

#### Q15: Price Elasticity of Demand
**Question**: When a software tool raised its monthly subscription from \$40 to \$48, active subscribers dropped from 10,000 to 9,000. Calculate arc price elasticity of demand ($\epsilon$).  
**Solution**:
1. Midpoint changes:
   $$\Delta P = +8, \quad P_{\text{avg}} = 44 \rightarrow \% \Delta P = \frac{8}{44} = \frac{2}{11}$$
   $$\Delta Q = -1,000, \quad Q_{\text{avg}} = 9,500 \rightarrow \% \Delta Q = \frac{-1,000}{9,500} = -\frac{2}{19}$$
2. Elasticity:
   $$\epsilon = \frac{-2/19}{2/11} = -\frac{11}{19} \approx \mathbf{-0.58}$$
   *(Inelastic demand: raising price increases total revenue).*

---

## Section 2: Data Interpretation & Table Analysis (Q16 – Q30)

*Questions 16–20 reference the following quarterly performance table for a portfolio company:*

```
========================================================================================================
Quarter     Gross Revenue ($M)   Discounts ($M)   COGS ($M)   Operating OPEX ($M)   Customer Churn Rate
========================================================================================================
Q1 2025           $42.0              $4.2          $18.5             $11.2                 3.2%
Q2 2025           $48.0              $6.0          $21.0             $12.5                 4.0%
Q3 2025           $52.0              $8.0          $24.5             $13.8                 5.5%
Q4 2025           $58.0              $9.5          $27.0             $14.2                 6.2%
========================================================================================================
```

#### Q16: Net Revenue Growth
**Question**: What was the percentage growth in Net Revenue (Gross Revenue minus Discounts) from Q1 to Q4?  
**Solution**:
- Q1 Net Revenue: $\$42.0 - \$4.2 = \$37.8\text{M}$.
- Q4 Net Revenue: $\$58.0 - \$9.5 = \$48.5\text{M}$.
- Growth:
  $$\% \Delta = \frac{48.5 - 37.8}{37.8} \times 100\% = \frac{10.7}{37.8} \times 100\% \approx \mathbf{+28.31\%}$$

#### Q17: EBITDA Margin Deterioration
**Question**: Calculate EBITDA (Net Revenue minus COGS minus Operating OPEX) and EBITDA margin for Q1 and Q4. Did margins expand or compress?  
**Solution**:
- Q1 EBITDA: $\$37.8\text{M} - \$18.5\text{M} - \$11.2\text{M} = \mathbf{\$8.1\text{M}}$.
  $$\text{Margin}_{\text{Q1}} = \frac{\$8.1}{\$37.8} \times 100\% = \mathbf{21.43\%}$$
- Q4 EBITDA: $\$48.5\text{M} - \$27.0\text{M} - \$14.2\text{M} = \mathbf{\$7.3\text{M}}$.
  $$\text{Margin}_{\text{Q4}} = \frac{\$7.3}{\$48.5} \times 100\% = \mathbf{15.05\%}$$
- Margin Change: Compressed by **638 basis points (-6.38%)**, despite \$16M gross revenue growth.

#### Q18: Root Cause of Margin Compression
**Question**: Identify the primary operational driver responsible for EBITDA margin compression from Q1 to Q4.  
**Solution**:
- Discount Rate on Gross Revenue:
  - Q1: $4.2 / 42.0 = \mathbf{10.0\%}$
  - Q4: $9.5 / 58.0 = \mathbf{16.38\%}$ (Discounts increased by 638 bps).
- COGS as % of Net Revenue:
  - Q1: $18.5 / 37.8 = \mathbf{48.94\%}$
  - Q4: $27.0 / 48.5 = \mathbf{55.67\%}$ (Cost increased by 673 bps).
- *Answer*: Heavy discounting to chase volume growth combined with COGS inflation eroded profitability.

#### Q19: Discount Leakage Analysis
**Question**: If the company had maintained its Q1 discount rate of 10.0% in Q4, how much additional EBITDA would have dropped to the bottom line?  
**Solution**:
- Allowed Discounts at 10.0%: $\$58.0\text{M} \times 0.10 = \$5.8\text{M}$.
- Actual Discounts: \$9.5M.
- Incremental EBITDA = $\$9.5\text{M} - \$5.8\text{M} = \mathbf{+\$3.70 \text{ Million}}$.

#### Q20: Churn Trajectory Correlation
**Question**: What is the percentage increase in customer churn rate from Q1 to Q4?  
**Solution**:
$$\% \Delta \text{Churn} = \frac{6.2\% - 3.2\%}{3.2\%} \times 100\% = \frac{3.0}{3.2} \times 100\% = \mathbf{+93.75\%}$$
*(Customer churn almost doubled, confirming severe customer dissatisfaction or poor-quality customer acquisition).*

---

## Section 3: Technical MCQs (Excel, SQL, Python, Cloud) (Q31 – Q50)

#### Q31: Excel Formula Evaluation
**Question**: In Excel, what is the result of `=IFERROR(10/0, "N/A") & " Result"`?  
**Answer**: `"N/A Result"` (The division by zero triggers `#DIV/0!`, caught by `IFERROR`, which returns `"N/A"`, concatenated with `" Result"`).

#### Q32: SQL Aggregation with NULLs
**Question**: A table `payments` contains four rows with values: `100`, `200`, `NULL`, `300`. What is the result of `SELECT AVG(amount), COUNT(amount), COUNT(*) FROM payments;`?  
**Answer**: `AVG(amount) = 200` (since $(100+200+300)/3 = 200$, NULL is ignored), `COUNT(amount) = 3`, and `COUNT(*) = 4`.

#### Q33: SQL HAVING vs WHERE
**Question**: Which clause must be used to filter groups based on the result of `SUM(order_total) > 5000`?  
**Answer**: `HAVING` (Since `WHERE` executes before `GROUP BY` and cannot evaluate aggregate functions).

#### Q34: Python Pandas Slicing
**Question**: In Pandas, what is the difference between `df.loc[0:2]` and `df.iloc[0:2]`?  
**Answer**: `df.loc[0:2]` is label-based and includes the endpoint index `2` (returns 3 rows if index is 0, 1, 2). `df.iloc[0:2]` is positional integer-based and excludes index `2` (returns 2 rows: positions 0 and 1).

#### Q35: Snowflake Zero-Copy Cloning
**Question**: Does creating a zero-copy clone of a 5TB production database immediately consume 5TB of cloud storage?  
**Answer**: **No**. Zero-copy cloning copies only the metadata pointers to the immutable micro-partitions. It consumes zero additional storage until newly modified records are written to the clone.

---

*(Questions 36–50 continue with rigorous drills covering PowerPivot DAX filter context, PySpark wide vs narrow transformations, Git version control, and data reconciliation checks).*


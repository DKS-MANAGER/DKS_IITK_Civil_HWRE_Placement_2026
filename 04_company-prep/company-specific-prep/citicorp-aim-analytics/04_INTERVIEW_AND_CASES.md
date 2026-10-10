# 04. Banking Cases, Puzzles & Interview Defense — Citi AIM

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Direct preparation for Technical Round 2, Case Discussions, Analytical Puzzles, and HR Fitment.

---

## 1. Solved Banking Analytics Business Cases

### Case 1: Credit Card Default Risk & Approval Cut-Off Optimization

#### Problem Statement:
Citi's consumer card division is revising underwriting criteria for a mid-tier rewards credit card.
* Model: Logistic Regression scorecard assigning a Probability of Default ($PD \in [0, 1]$) to each applicant.
* Economics per Approved Card:
  * Non-Defaulter (Good): Generates an average lifetime revenue of **$+\$600** (interchange swipe fees, annual fee, interest).
  * Defaulter (Bad): Incurs an average net credit loss / charge-off of **$-\$2,400**.
* **Question**: What is the maximum acceptable default probability ($PD_{cutoff}$) for an applicant to be approved?

#### Structured Solution:
1. **Expected Value Formulation**:
   For any approved applicant with default probability $p$:
   $$E[\text{Profit}] = (1 - p) \times (+\$600) + p \times (-\$2,400)$$
   $$E[\text{Profit}] = 600 - 600p - 2400p = 600 - 3000p$$
2. **Break-Even Condition**:
   Set $E[\text{Profit}] \ge 0$:
   $$600 - 3000p \ge 0 \implies 3000p \le 600 \implies p \le \frac{600}{3000} = \mathbf{0.20} \quad (20\%)$$
3. **Business Recommendation**:
   * Any applicant with model-estimated default probability $PD \le 20\%$ is commercially accretive.
   * However, accounting for cost of capital, regulatory reserves (CECL/Basel), and target return on equity (ROE $\ge 15\%$), management typically imposes a safety margin buffer, lowering the operational approval cutoff to $PD_{cutoff} \approx \mathbf{8\% \text{ to } 12\%}$.

---

### Case 2: Diagnosing Customer Churn in Premium Salary Accounts

#### Problem Statement:
Over the past two quarters, Citi's Corporate Banking and Wealth Management division observed a **15% year-over-year decline** in average quarterly deposits across multinational corporate salary accounts in India. You are tasked with diagnosing the root cause using data and proposing an analytical retention campaign.

#### Issue-Tree Diagnostic Framework:
```
                               15% DEPOSIT DECLINE
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
     1. CUSTOMER COUNT (HEADCOUNT)                        2. DEPOSIT PER CUSTOMER
     • Are corporate employees leaving?                    • Are salaries decreasing?
     • Did Citi lose corporate contracts?                  • Are funds being siphoned out?
     • Competitor aggressive onboarding?                   • Macro wage freezes or layoffs?
            │                                                     │
            └──────────────────────────┬──────────────────────────┘
                                       ▼
                             3. FUND OUTFLOW DESTINATIONS
                             • Mutual Fund / SIP direct debits?
                             • Higher-yield Neo-banks / Fintech deposits?
                             • Real estate / Loan prepayments?
```

#### Analytical Execution Steps:
1. **Data Extraction via SQL**:
   * Segment accounts by corporate client, employee tenure, and balance bands.
   * Extract transaction logs to analyze outgoing wire transfers (NEFT/RTGS/UPI).
2. **Hypothesis Testing**:
   * *Finding*: Customer headcount remained flat (zero corporate contract loss). However, outgoing transfers to third-party investment brokerages (Zerodha, Groww) surged by $42\%$.
   * *Root Cause*: High inflation and equity market bull run prompted affluent salaried employees to auto-sweep idle balances into equity mutual funds rather than holding low-interest ($3.0\%$) savings deposits.
3. **Data-Driven Strategic Recommendation**:
   * **Automated Sweep-in Deposit (Multi-Option Deposit)**: Auto-sweep balances exceeding ₹50,000 into high-interest flexi fixed deposits ($6.8\%$) with instant liquidity.
   * **In-House Wealth Cross-Sell**: Build an automated propensity model targeting salary accounts transferring $>₹30,000/\text{month}$ to external brokers, offering seamless in-app Citi Wealth investment portfolios with zero advisory fees for 6 months.

---

### Case 3: Optimizing Real-Time Fraud Alert Thresholds

#### Problem Statement:
Citi's fraud detection engine evaluates 10 million transactions daily. The current model flags 50,000 transactions daily ($0.50\%$) as suspicious, blocking the card and generating a call from the fraud operations desk.
* Operational Reality:
  * Out of 50,000 flagged alerts, only **1,000 are genuine fraud** ($\text{Precision} = 2\%$).
  * The manual fraud investigation desk can only review 20,000 alerts per day with available staffing.
  * Legitimate customers whose cards are falsely blocked experience high friction and churn.
* **Question**: How would you redesign the alert strategy?

#### Solution & Analytical Framework:
1. **Tiered Alert Strategy by Probability & Dollar Amount**:
   * Instead of a single binary cutoff, create a 3-tier routing matrix based on Model Score and Transaction Amount:

| Risk Tier | Model Predicted Fraud Score ($p$) | Transaction Value | Action Triggered | Operational Impact |
| :---: | :---: | :---: | :--- | :--- |
| **Tier 1 (Critical)** | $p \ge 0.85$ | Any Amount | **Immediate Hard Block** + High-Priority Call | $\approx 2,000$ txns/day (Direct fraud prevention) |
| **Tier 2 (Moderate)** | $0.30 \le p < 0.85$ | High Value ($> \$500$) | **Interactive Two-Factor Auth (SMS/Push)** | Zero operational labor; cardholder confirms in seconds |
| **Tier 3 (Low/Medium)**| $0.10 \le p < 0.30$ | Low Value ($< \$50$) | **Silent Post-Auth Monitoring** | Zero customer friction; analyzed asynchronously |

2. **Impact**:
   * Cuts manual review desk workload from 50,000 to $<15,000$ alerts/day (well within capacity).
   * Elevates review precision from $2\%$ to $>25\%$.
   * Mitigates false-positive customer churn by $80\%$.

---

## 2. Quantitative & Analytical Brainteasers (Puzzles Bank)

### Puzzle 1: The 25 Horses Race
* **Problem**: You have 25 horses. You can race at most 5 horses at a time. There is no stopwatch (you only know the relative rank of the 5 horses in each race). What is the minimum number of races needed to determine the top 3 fastest horses?
* **Solution**:
  1. Divide 25 horses into 5 groups of 5: Race Groups A, B, C, D, E $\implies$ **5 races**.
  2. Race the 5 winners from each group $\implies$ **Race 6**.
     * Suppose the rank of winners is $A_1 > B_1 > C_1 > D_1 > E_1$.
     * $A_1$ is guaranteed to be the overall 1st fastest horse!
     * Eliminate groups D and E entirely. Eliminate $C_2, C_3$ (cannot beat $C_1$). Eliminate $B_3$ (cannot beat $B_1, B_2$).
  3. The candidates for 2nd and 3rd place are: $A_2, A_3, B_1, B_2, C_1$ (exactly 5 horses).
  4. Race these 5 horses $\implies$ **Race 7**.
  5. **Total Races = 7**.

---

### Puzzle 2: Burning Ropes (45 Minutes)
* **Problem**: You have two non-homogeneous ropes. Each rope takes exactly 60 minutes to burn completely from one end to the other. Because the ropes are non-uniform, burning speed varies. How can you measure exactly 45 minutes?
* **Solution**:
  1. Light **both ends of Rope 1** simultaneously, and **one end of Rope 2** at the same moment.
  2. Because Rope 1 is burning from both ends, it will burn twice as fast and extinguish in exactly **30 minutes**.
  3. The moment Rope 1 extinguishes, exactly 30 minutes have passed. At this precise instant, Rope 2 has exactly 30 minutes of burn time remaining.
  4. Light the **other end of Rope 2**.
  5. The remaining portion of Rope 2 will burn from both ends and extinguish in **15 minutes**.
  6. Total time elapsed = $30 + 15 = \mathbf{45\text{ minutes}}$.

---

### Puzzle 3: Generating a Fair Coin from a Biased Coin (von Neumann Extractor)
* **Problem**: You are given a coin that lands Heads with unknown probability $p \neq 0.5$. How can you simulate a completely fair coin toss ($P = 0.50$)?
* **Solution**:
  1. Flip the biased coin twice.
  2. Possible outcomes:
     * $\text{Head, Tail (HT)} \implies P(HT) = p(1 - p)$
     * $\text{Tail, Head (TH)} \implies P(TH) = (1 - p)p$
     * $\text{Head, Head (HH)} \implies P(HH) = p^2$
     * $\text{Tail, Tail (TT)} \implies P(TT) = (1 - p)^2$
  3. Notice that $P(HT) = P(TH) = p(1 - p)$ for **ANY** value of $p$!
  4. Rule:
     * If outcome is $HT$, declare **Heads**.
     * If outcome is $TH$, declare **Tails**.
     * If outcome is $HH$ or $TT$, discard and flip twice again.

---

### Puzzle 4: Poisoned Wine Bottles (Binary Search with Test Mice)
* **Problem**: You have 1,000 wine bottles. Exactly one bottle is poisoned. A mouse that drinks even a single drop of poisoned wine dies within 24 hours. You have 24 hours to find the poisoned bottle. What is the minimum number of mice needed?
* **Solution**:
  * Since the test takes 24 hours, you cannot run sequential tests. All mice must drink at time zero.
  * Each mouse has 2 states at the end: Alive (0) or Dead (1).
  * With $M$ mice, we can represent $2^M$ distinct binary states.
  * To distinguish among 1,000 bottles:
    $$2^M \ge 1000 \implies M \ge 10 \quad (\text{since } 2^{10} = 1024)$$
  * Method: Number bottles 1 to 1000 in binary (10-bit numbers). Mouse $i$ drinks from every bottle where the $i$-th bit of its binary representation is 1. The binary pattern of dead mice identifies the exact poisoned bottle. **Minimum = 10 mice**.

---

### Puzzle 5: The Monty Hall Problem
* **Problem**: You are on a game show with 3 doors. Behind one door is a car; behind the other two are goats. You pick Door 1. The host (who knows what is behind each door) opens Door 3, revealing a goat. He offers you the choice: stick with Door 1 or switch to Door 2. Should you switch?
* **Solution**:
  * Prior probability of car behind Door 1 = $\frac{1}{3}$.
  * Probability of car behind either Door 2 or Door 3 = $\frac{2}{3}$.
  * When the host reveals a goat behind Door 3, the entire $\frac{2}{3}$ probability collapses onto Door 2.
  * Sticking with Door 1 wins with probability $\frac{1}{3}$.
  * Switching to Door 2 wins with probability $\mathbf{\frac{2}{3}}$ ($66.7\%$). **Always switch**.

---

## 3. Financial Market Sizing & Guesstimates

### Guesstimate: Total Credit Card Transaction Volume in India on Diwali Day

#### Approach & Decomposition:
$$\text{Total Spend} = \text{Total Active Credit Cards} \times \text{Diwali Active Usage Rate} \times \text{Average Spend per Active Card}$$

1. **Active Credit Card Base in India**:
   * Population of India $\approx 1.4\text{ Billion}$.
   * Working adult population $\approx 600\text{ Million}$.
   * Urban banked population $\approx 200\text{ Million}$.
   * Credit card penetration in eligible urban segment $\approx 20\% \implies \mathbf{40\text{ Million unique cardholders}}$.
   * Average cards per cardholder $\approx 2.5 \implies \mathbf{100\text{ Million active credit cards}}$ (matches RBI official figures of $\approx 95–100\text{M}$ cards).
2. **Diwali Day Activity Rate**:
   * On normal days: $\approx 10\%$ of cards are used.
   * On Diwali Day (peak festive e-commerce, electronics, jewellery, gifting, dining): $\approx \mathbf{30\% \text{ of active cards are swiped}}$.
   * Active cards used on Diwali Day = $100\text{M} \times 0.30 = \mathbf{30\text{ Million transacting cards}}$.
3. **Average Spend per Active Card on Diwali**:
   * Segment A (High-value purchases: Gold, TV, Laptops, Furniture) $\approx 20\%$ of users, spending ₹25,000 average $\implies 0.20 \times 25,000 = ₹5,000$.
   * Segment B (Festive gifting, clothing, e-commerce sale) $\approx 50\%$ of users, spending ₹5,000 average $\implies 0.50 \times 5,000 = ₹2,500$.
   * Segment C (Groceries, sweets, dining, fuel) $\approx 30\%$ of users, spending ₹1,500 average $\implies 0.30 \times 1,500 = ₹450$.
   * Weighted Average Spend per Card $\approx ₹5,000 + ₹2,500 + ₹450 \approx \mathbf{₹8,000}$.
4. **Total Daily Transaction Value**:
   $$\text{Total Volume} = 30\text{ Million cards} \times ₹8,000 = \mathbf{₹24,000\text{ Crores}} \quad (\approx \$2.9\text{ Billion USD})$$

---

## 4. Pitching M.Tech Civil / HWRE to Citi AIM (Interview Defense)

The most critical moment in your interview will be answering:  
> **"You are an M.Tech student in Civil Engineering / Water Resources at IIT Kanpur. Why Citigroup? How is your background relevant to business analytics?"**

### The Winning 2-Minute Structured Pitch:

> *"Thank you for asking that. At first glance, Civil & Water Resources Engineering and Banking Analytics might sound like completely different disciplines. But beneath the surface, they share the exact same mathematical and analytical DNA: **stochastic modeling, probability theory, and large-scale data manipulation**.*
>
> *In my M.Tech research at IIT Kanpur, I work with multi-decadal time-series data, modeling extreme hydro-meteorological events. The statistical distributions we use to predict a 100-year flood—such as Log-Pearson Type III, Gumbel, and Generalized Extreme Value theory—are mathematically identical to the heavy-tailed loss distributions and Value-at-Risk (VaR) models that Citigroup uses to predict catastrophic credit default and market liquidity shocks.*
>
> *Every day, I write Python pipelines, run statistical hypothesis tests, handle non-stationary time series, and write complex SQL queries to clean and analyze spatial and temporal datasets. I have developed a strong statistical mindset: I understand p-values, variance trade-offs, and regression diagnostics from first principles, not just by clicking black-box software.*
>
> *I want to join Citi AIM because I want to apply this quantitative and statistical toolkit to high-velocity, real-world business decisions—whether that is optimizing credit card default scorecards, reducing customer churn, or detecting transaction fraud. Citigroup is the global gold standard in data-driven finance, and I am excited to bring my analytical rigor to the team."*

---

## 5. Behavioural & HR Questions (Citi Leadership Principles)

### Q1: "Give an example of an analytical mistake you made and how you resolved it."
* **Context**: Project on rainfall intensity-duration curves (`idf-pet`).
* **Mistake**: When fitting an empirical Sherman distribution via non-linear least squares, initial optimization yielded an unphysical negative duration parameter ($b = -4.2$).
* **Root Cause**: Identified that sample data contained zero-rainfall dry intervals that distorted log-transforms, causing gradient explosion.
* **Resolution**: Implemented bounded parameter optimization with Levenberg-Marquardt constraints and validated goodness-of-fit using Anderson-Darling tests, achieving $R^2 = 0.988$.
* **Lesson**: Always conduct sanity checks on model parameters against physical reality before presenting results to stakeholders.

### Q2: "How do you handle a situation where business stakeholders want to use a metric you know is statistically flawed?"
* **Action**:
  1. Never dismiss the stakeholder outright; understand their underlying business objective.
  2. Provide a concrete side-by-side simulation showing how the flawed metric (e.g., raw Accuracy on a 99:1 imbalanced dataset) creates severe blind spots (e.g., $100\%$ accuracy while missing $100\%$ of fraud).
  3. Introduce the superior metric (Precision-Recall AUC or KS Statistic) framed in terms of **financial savings** rather than abstract statistics.

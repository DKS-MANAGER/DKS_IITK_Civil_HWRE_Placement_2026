# Topic Master 01: Quantitative Aptitude, Business Economics & Commercial Mathematics

> **Consolidated Module**: ACC-JAPAN-TOPIC-01 (Quantitative Aptitude & Commercial Math)  
> **Target Assessment**: Online Technical Screening, Cognitive Numerical Assessment & Case Math  
> **Structure**:
> - **SECTION A**: Commercial Mathematics & Economic Formulas (Break-Even, ROI, TCO, Net Margin, CAPEX/OPEX, NPV)
> - **SECTION B**: Core Arithmetic & Applied Probability (Alligation, Time & Work, Speed-Distance, Fractions, Cyclicity)
> - **SECTION C**: 20 Master Solved Exam-Caliber Quantitative Practice Problems with Full Mathematical Derivations

---


# SECTION A: Commercial Economics & Quantitative Foundations

Quantitative Aptitude, Commercial Economics & Financial Math (Priority 1)

### Explainer C.1: Compounded Growth, CAGR Derivation & Volatility Drag Mechanics

#### 1. First-Principles Derivation of CAGR
Suppose an initial investment $V_{\text{initial}}$ grows under a constant annual geometric growth rate $r$ for $n$ compounding years to reach terminal value $V_{\text{final}}$:

$$V_{\text{final}} = V_{\text{initial}} \cdot (1 + r)^n$$

Dividing both sides by $V_{\text{initial}}$:
$$\frac{V_{\text{final}}}{V_{\text{initial}}} = (1 + r)^n$$

Taking the $n$-th root (raising both sides to power $1/n$):
$$(1 + r) = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{\frac{1}{n}}$$

Isolating the Compound Annual Growth Rate $r$ ($\text{CAGR}$):
$$\mathbf{\text{CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{\frac{1}{n}} - 1}$$

#### 2. The Volatility Drag Mathematical Proof
Why do financial analysts and management consultants strictly avoid using the arithmetic mean for multi-year performance?
Let an asset return $r_1$ in Year 1 and $r_2$ in Year 2.
* **Arithmetic Mean**: $\bar{r} = \frac{r_1 + r_2}{2}$.
* **True Compounded Return**: $R_{\text{compound}} = \sqrt{(1 + r_1)(1 + r_2)} - 1$.
* **Taylor Series Approximation**:
  Expanding the natural logarithm $\ln(1+r) \approx r - \frac{r^2}{2}$:
  $$\ln(1 + R_{\text{compound}}) = \frac{\ln(1 + r_1) + \ln(1 + r_2)}{2} \approx \frac{r_1 + r_2}{2} - \frac{r_1^2 + r_2^2}{4}$$
  Recognizing variance $\sigma^2 = \frac{(r_1 - \bar{r})^2 + (r_2 - \bar{r})^2}{2}$:
  $$\mathbf{R_{\text{compound}} \approx \bar{r} - \frac{\sigma^2}{2}}$$
* **Core Insight**: The compounded return is **strictly less than the arithmetic mean by half the variance** ($\frac{\sigma^2}{2}$). Volatility acts as a mathematical penalty (volatility drag) reducing real wealth.

---

### Explainer C.2: The Mathematical Foundation of the Rule of 72 & Mental Approximations

#### 1. Why 72? Derivation from Natural Logarithms
Let an asset grow at annual rate $r$ (expressed as a decimal). The time $t$ required to double ($V_{\text{final}} = 2 \cdot V_{\text{initial}}$) is:

$$(1 + r)^t = 2 \implies t \cdot \ln(1 + r) = \ln(2)$$

We know $\ln(2) \approx 0.693147$.
Using the Taylor expansion for small $r$: $\ln(1 + r) = r - \frac{r^2}{2} + \frac{r^3}{3} - \dots \approx r$.
Thus:
$$t \approx \frac{0.693147}{r} = \frac{69.3}{r \times 100}$$

#### 2. Why RDBMS and Consultants Adjust 69.3 to 72:
* **Higher Rates**: For realistic business growth rates ($8\%\text{--}15\%$), the second-order term $\frac{r^2}{2}$ becomes significant, shifting the ideal numerator from $69.3$ to approximately $71\text{--}72$.
* **High Divisibility**: 72 is an abundant composite number divisible by $2, 3, 4, 6, 8, 9, 12, 18, 24, 36$, allowing rapid mental calculation in interview rooms without pen and paper!

```text
At 6%  growth -> 72 / 6  = 12.0 years to double  (Exact: 11.90 years)
At 8%  growth -> 72 / 8  = 9.0  years to double  (Exact: 9.01 years)
At 12% growth -> 72 / 12 = 6.0  years to double  (Exact: 6.12 years)
```

---

### Explainer C.3: Commercial Economics — Margin vs Markup, Unit Economics & Break-Even Volume

#### 1. Margin vs Markup Interconversion Proof
* Let Cost of Goods Sold = $C$, Revenue = $R$, Profit = $P = R - C$.
* **Markup ($M$)**: Ratio of Profit to Cost $\implies M = \frac{P}{C} \implies P = M \cdot C \implies R = C + M \cdot C = C(1 + M)$.
* **Margin ($G$)**: Ratio of Profit to Revenue $\implies G = \frac{P}{R}$.
* Substituting $P = M \cdot C$ and $R = C(1 + M)$:
  $$G = \frac{M \cdot C}{C(1 + M)} \implies \mathbf{G = \frac{M}{1 + M}}$$
* Rearranging to express Markup in terms of Margin:
  $$G(1 + M) = M \implies G + G \cdot M = M \implies G = M(1 - G) \implies \mathbf{M = \frac{G}{1 - G}}$$

| Markup on Cost ($M$) | Equivalent Margin on Sales ($G$) | Concrete Example |
|:---:|:---:|:---|
| **$20\%$** | $\frac{0.20}{1.20} = \mathbf{16.67\%}$ | Cost ¥100, Price ¥120, Profit ¥20 |
| **$25\%$** | $\frac{0.25}{1.25} = \mathbf{20.00\%}$ | Cost ¥80, Price ¥100, Profit ¥20 |
| **$33.33\%$** | $\frac{0.333}{1.333} = \mathbf{25.00\%}$ | Cost ¥75, Price ¥100, Profit ¥25 |
| **$50\%$** | $\frac{0.50}{1.50} = \mathbf{33.33\%}$ | Cost ¥100, Price ¥150, Profit ¥50 |
| **$100\%$** | $\frac{1.00}{2.00} = \mathbf{50.00\%}$ | Cost ¥50, Price ¥100, Profit ¥50 |

#### 2. Unit Economics & Operating Leverage
* **Contribution Margin (CM)**: The portion of sales revenue available to cover fixed costs:
  $$\text{CM} = \text{Price} - \text{Variable Cost per Unit}$$
* **Break-Even Volume ($Q_{\text{BE}}$)**: The unit volume where Total Revenue equals Total Costs ($\text{Operating Income} = 0$):
  $$\text{Revenue} = \text{Fixed Costs} + (\text{Variable Cost} \times Q_{\text{BE}})$$
  $$(\text{Price} - \text{Variable Cost}) \times Q_{\text{BE}} = \text{Fixed Costs} \implies \mathbf{Q_{\text{BE}} = \frac{\text{Fixed Costs}}{\text{Price} - \text{Variable Cost}} = \frac{\text{Fixed Costs}}{\text{Unit CM}}}$$

---

### Explainer C.4: Enterprise SaaS & Digital Economics — Cohorts, LTV, CAC & Churn Dynamics

#### 1. Mathematical Proof: Why Customer Lifetime = $1 / \text{Churn}$
Let $c$ be the constant probability that a customer cancels (churns) in any given year.
The probability that a customer survives exactly $t$ years before churning is modeled by a geometric distribution: $P(T = t) = (1 - c)^{t-1} \cdot c$.
The expected customer lifetime $E[T]$ is the infinite summation:

$$E[T] = \sum_{t=1}^{\infty} t \cdot (1 - c)^{t-1} \cdot c = c \sum_{t=1}^{\infty} t \cdot (1 - c)^{t-1}$$

Using the standard series identity $\sum_{t=1}^{\infty} t \cdot x^{t-1} = \frac{1}{(1 - x)^2}$ for $|x| < 1$, setting $x = 1 - c$:
$$E[T] = c \cdot \frac{1}{(1 - (1 - c))^2} = c \cdot \frac{1}{c^2} = \mathbf{\frac{1}{c}}$$

* **Result**: If annual churn is $5.0\%$ ($c = 0.05$), average customer lifetime is strictly $\frac{1}{0.05} = \mathbf{20.0\text{ years}}$.

#### 2. Customer Lifetime Value (LTV) Formula
$$\mathbf{\text{LTV} = \frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Annual Churn Rate}}}$$

#### 3. Enterprise SaaS Health Scorecard
* **LTV / CAC Ratio**: Target $\ge 3.0x$.
  - $< 1.0x$: Value destroying; company loses money on every acquired customer.
  - $1.0x\text{--}2.9x$: Marginal efficiency; vulnerable to customer churn shocks.
  - $\ge 3.0x$: Highly efficient economic engine.
  - $> 5.0x$: Under-investing in growth; marketing budget should be expanded aggressively.
* **CAC Payback Period**: Target $< 12\text{ months}$:
  $$\text{CAC Payback (Months)} = \frac{\text{CAC}}{\text{Monthly Gross Profit per Customer}} = \frac{\text{CAC}}{(\text{ARPU} \times \text{Gross Margin \%}) / 12}$$
* **The Rule of 40**: A SaaS firm's growth rate plus profitability margin should exceed $40\%$:
  $$\mathbf{\text{YoY Revenue Growth Rate \%} + \text{Free Cash Flow Margin \%} \ge 40\%}$$

---

### Explainer C.5: Smart Factory Operations — Overall Equipment Effectiveness (OEE) Decomposition

Accenture Japan's Industry X practice leads industrial digital transformation for Japan's premier automotive and machinery leaders (Toyota, Mitsubishi, Komatsu). OEE evaluates factory productivity across three independent operational vectors:

$$\mathbf{\text{OEE} = \text{Availability} \times \text{Performance} \times \text{Quality}}$$

```text
Total Shift Calendar Time (e.g., 24 Hours = 1,440 min)
  └── Planned Production Time (Subtract Planned Maintenance, Meal Breaks)
        └── Operating Time (Subtract Unplanned Breakdowns, Tool Setup) -> AVAILABILITY (A)
              └── Net Operating Time (Subtract Minor Idling, Speed Losses) -> PERFORMANCE (P)
                    └── Fully Productive Time (Subtract Scrap, Rework) -> QUALITY (Q)
```

#### Diagnostic Breakdown:
1. **Availability ($A$)**:
   $$A = \frac{\text{Operating Time}}{\text{Planned Production Time}} = \frac{\text{Planned Time} - \text{Unplanned Downtime}}{\text{Planned Time}}$$
2. **Performance ($P$)**:
   $$P = \frac{\text{Ideal Cycle Time} \times \text{Total Units Produced}}{\text{Operating Time}} = \frac{\text{Actual Run Rate}}{\text{Nameplate Engineering Rate}}$$
3. **Quality ($Q$)**:
   $$Q = \frac{\text{Good Units Produced}}{\text{Total Units Produced}} = \frac{\text{Total Units} - \text{Defect Units}}{\text{Total Units}}$$

* **Sensitivity Insight**: If a plant runs at $A = 90.0\%$, $P = 90.0\%$, $Q = 95.0\%$, the overall OEE is not $90\%$; it is $0.90 \times 0.90 \times 0.95 = \mathbf{76.95\%}$! Minor losses across all three stages multiply, eroding factory profitability.

---

### Explainer C.6: Harmonic Mean vs Arithmetic Mean & Alligation Mixture Principles

#### 1. Mathematical Proof of Harmonic Mean for Average Speed
Let a vehicle travel a fixed one-way distance $D$ at speed $v_1$ and return the identical distance $D$ at speed $v_2$.
* Total Distance $= D + D = 2D$.
* Outbound Time $t_1 = \frac{D}{v_1}$; Inbound Time $t_2 = \frac{D}{v_2}$.
* Total Time $t_{\text{total}} = \frac{D}{v_1} + \frac{D}{v_2} = D \left(\frac{v_1 + v_2}{v_1 \cdot v_2}\right)$.
* Average Speed:
  $$v_{\text{avg}} = \frac{\text{Total Distance}}{\text{Total Time}} = \frac{2D}{D \left(\frac{v_1 + v_2}{v_1 \cdot v_2}\right)} = \mathbf{\frac{2 \cdot v_1 \cdot v_2}{v_1 + v_2}}$$
* **Why Arithmetic Mean Fails**: Because the vehicle spends **more time** traveling at the slower speed than at the faster speed! Time weights the slower speed more heavily.
  - Outbound $60\text{ km/h}$, Return $40\text{ km/h}$:
    $$v_{\text{avg}} = \frac{2 \times 60 \times 40}{60 + 40} = \frac{4800}{100} = \mathbf{48.0\text{ km/h}} \quad (\text{Arithmetic mean } 50.0\text{ is objectively wrong!})$$

#### 2. Cross-Rule of Alligation (Weighted Averages)
To mix two ingredients of price $C$ (cheaper) and $D$ (dearer) to create a mixture of mean target price $M$:
$$Q_C \cdot C + Q_D \cdot D = (Q_C + Q_D) \cdot M$$
$$Q_C(M - C) = Q_D(D - M) \implies \mathbf{\frac{Q_C}{Q_D} = \frac{D - M}{M - C}}$$

---

# SECTION B & C: Quantitative Mathematics Curriculum & 20 Solved Problems

Quantitative Mathematics & Business Economics

Every problem below has been independently calculated and verified in Python.

---

### Problem 01: Rule of 72 vs Exact Compound Annual Growth Rate (CAGR)
* **Question**: An IT consulting practice in Tokyo grows annual revenue from JPY 100M to JPY 200M over 6 years. Compare the Rule-of-72 mental approximation with the mathematically exact CAGR.
* **Exact Formula**:
  $$\text{Exact CAGR} = \left(\frac{V_f}{V_i}\right)^{1/t} - 1 = \left(\frac{200}{100}\right)^{1/6} - 1 = 2^{0.1667} - 1 = 12.2462\% \approx 12.25\%$$
* **Rule-of-72 Approximation**:
  $$g \approx \frac{72}{t} = \frac{72}{6} = 12.00\%$$
* **Evaluation**: The Rule of 72 yields 12.00%, underestimating the exact rate (12.25%) by only 0.25 percentage points. In interview math, cite: *"Using Rule of 72, growth is ~12%; exact calculation yields 12.25%."*

---

### Problem 02: Customer Lifetime Value (LTV) & Churn Mechanics
* **Question**: A SaaS enterprise product charges an Average Revenue Per User (ARPU) of $500/month with a 70% Gross Margin. The monthly customer churn rate is 3.5%. Calculate customer lifetime (in months) and expected LTV.
* **Formulas & Steps**:
  $$\text{Expected Lifetime (months)} = \frac{1}{\text{Churn Rate}} = \frac{1}{0.035} \approx 28.57\text{ months}$$
  $$\text{LTV} = \frac{\text{ARPU} \times \text{Gross Margin}}{\text{Churn Rate}} = \frac{500 \times 0.70}{0.035} = \frac{350}{0.035} = \$10,000.00$$
* **Answer**: Expected customer lifetime is 28.57 months; LTV is exactly **$10,000.00**.

---

### Problem 03: Customer Acquisition Cost (CAC) Payback Period
* **Question**: A client invests $4,200 to acquire an enterprise software customer. The customer generates $600/month with a 70% gross margin. Calculate the CAC payback period in both months and decimal years.
* **Formulas & Steps**:
  $$\text{Monthly Gross Profit Contribution} = \$600 \times 0.70 = \$420/\text{month}$$
  $$\text{Payback Period (months)} = \frac{\text{CAC}}{\text{Monthly Gross Contribution}} = \frac{4200}{420} = 10.0\text{ months}$$
  $$\text{Payback Period (years)} = \frac{10}{12} \approx 0.833\text{ years}$$
* **Answer**: Exactly **10.0 months** (0.833 years). This beats the consulting benchmark target of $<12$ months.

---

### Problem 04: Weighted Average Cost of Capital (WACC) with After-Tax Debt
* **Question**: An enterprise is funded by $60M Equity (cost $r_e = 12\%$) and $40M Debt (cost $r_d = 6\%$). The corporate tax rate is $T = 30\%$. Calculate WACC.
* **Formulas & Steps**:
  $$V = E + D = 60 + 40 = \$100M, \quad W_e = 0.60, \quad W_d = 0.40$$
  $$\text{After-Tax Cost of Debt} = r_d \times (1 - T) = 6\% \times (1 - 0.30) = 4.20\%$$
  $$\text{WACC} = W_e \cdot r_e + W_d \cdot r_d (1 - T) = 0.60 \times 12\% + 0.40 \times 4.20\% = 7.20\% + 1.68\% = 8.88\%$$
* **Answer**: **8.88%**.

---

### Problem 05: Overall Equipment Effectiveness (OEE) Decomposition
* **Question**: An automotive plant runs an 8-hour shift (480 mins) with 60 mins planned maintenance. Operating breakdown is 42 mins. Total parts produced is 700 units (ideal rate 0.5 mins/part). 28 parts were defective. Compute Availability, Performance, Quality, and composite OEE.
* **Decomposition**:
  * **Planned Production Time** = $480 - 60 = 420\text{ mins}$.
  * **Operating Time** = $420 - 42 = 378\text{ mins}$.
  * **Availability** = $\frac{378}{420} = 0.9000$ (**90.00%**).
  * **Ideal Operating Time** = $700 \times 0.5 = 350\text{ mins}$.
  * **Performance** = $\frac{350}{378} \approx 0.9259$ (**92.59%**).
  * **Good Parts** = $700 - 28 = 672\text{ units}$.
  * **Quality** = $\frac{672}{700} = 0.9600$ (**96.00%**).
  $$\text{OEE} = 0.90 \times \left(\frac{350}{378}\right) \times 0.96 = 0.90 \times 0.925926 \times 0.96 = 0.8000 \quad (80.00\%)$$
* **Answer**: OEE is exactly **80.00%** (World-class manufacturing benchmark is $\ge 85\%$).

---

### Problem 06: High Availability SLA Downtime Budget
* **Question**: For a calendar year (365 days = 8,760 hours = 525,600 minutes), compute the allowed downtime for "three nines" (99.9%), "four nines" (99.99%), and "five nines" (99.999%).
* **Formulas & Exact Calculations**:
  * **99.9% ("Three Nines")**: $0.001 \times 8760 = 8.76\text{ hours/year}$ (525.6 minutes).
  * **99.99% ("Four Nines")**: $0.0001 \times 525600 = 52.56\text{ minutes/year}$ (0.876 hours).
  * **99.999% ("Five Nines")**: $0.00001 \times 525600 = 5.256\text{ minutes/year}$ (315.36 seconds).
* **Strategic Takeaway**: Moving from 99.9% to 99.99% reduces downtime from 8.76 hours to under 53 minutes, requiring multi-AZ failover and automated health checks.

---

### Problem 07: IoT Telemetry Storage: Decimal (GB) vs Binary (GiB)
* **Question**: 1,000 smart sensors transmit 50 bytes of telemetry per second continuously for 30 days. Compute the total storage requirement in decimal Gigabytes (GB, SI) and binary Gibibytes (GiB, IEC).
* **Calculations**:
  $$\text{Total Seconds} = 30 \times 86400 = 2,592,000\text{ seconds}$$
  $$\text{Total Bytes} = 1000 \times 50 \times 2,592,000 = 129,600,000,000\text{ bytes}$$
  $$\text{Decimal GB} = \frac{129,600,000,000}{10^9} = 129.60\text{ GB}$$
  $$\text{Binary GiB} = \frac{129,600,000,000}{2^{30}} = \frac{129,600,000,000}{1,073,741,824} \approx 120.70\text{ GiB}$$
* **Answer**: **129.60 GB** vs **120.70 GiB** (Difference of 8.90 units due to base-10 vs base-2 definitions).

---

### Problem 08: Classification Threshold & Asymmetric Cost Optimization
* **Question**: In an enterprise fraud detection pipeline evaluating 10,000 transactions (200 fraudulent, 9,800 legitimate):
  * **Model A**: Recall = 95% (190 frauds caught, 10 missed False Negatives); False Positive Rate = 3.0% (294 False Positives).
  * **Model B**: Recall = 80% (160 frauds caught, 40 missed False Negatives); False Positive Rate = 0.5% (49 False Positives).
  * Cost of missed fraud (FN) = $1,500. Cost of reviewing a false alarm (FP) = $25.
  Determine which model minimizes total business loss.
* **Calculations**:
  $$\text{Total Cost Model A} = (10 \times \$1,500) + (294 \times \$25) = \$15,000 + \$7,350 = \$22,350$$
  $$\text{Total Cost Model B} = (40 \times \$1,500) + (49 \times \$25) = \$60,000 + \$1,225 = \$61,225$$
* **Answer**: **Model A saves $38,875** compared to Model B. In fraud detection, high recall is worth accepting higher false alarms due to the massive cost asymmetry ($1,500 vs $25).

---

### Problem 09: Plant Break-even Capacity Utilization
* **Question**: An industrial electronics plant has annual fixed operating costs of $1,800,000. Maximum plant capacity is 100,000 units/year. Selling price is $50/unit; variable cost is $20/unit. Find break-even volume and required capacity utilization.
* **Formulas & Steps**:
  $$\text{Unit Contribution Margin} = P - V = \$50 - \$20 = \$30/\text{unit}$$
  $$\text{Break-even Volume} = \frac{\text{Fixed Costs}}{\text{Unit Contribution Margin}} = \frac{1,800,000}{30} = 60,000\text{ units}$$
  $$\text{Capacity Utilization} = \frac{60,000}{100,000} = 60.0\%$$
* **Answer**: Break-even occurs at **60,000 units** (**60.0%** plant capacity).

---

### Problem 10: 5-Year Cloud Migration Total Cost of Ownership (TCO)
* **Question**: Compare 5-year TCO between On-Premise and Public Cloud:
  * **On-Premise**: Hardware CapEx = $1,200,000 (Year 0). Annual power/cooling/space = $150,000/yr. Annual maintenance/licensing = $90,000/yr.
  * **Cloud**: One-time migration/setup = $300,000. 3-Year Reserved compute/storage = $320,000/yr.
* **Calculations**:
  $$\text{TCO}_{\text{On-Prem}} = \$1,200,000 + 5 \times (\$150,000 + \$90,000) = \$1,200,000 + \$1,200,000 = \$2,400,000$$
  $$\text{TCO}_{\text{Cloud}} = \$300,000 + 5 \times \$320,000 = \$300,000 + \$1,600,000 = \$1,900,000$$
  $$\text{Net 5-Year Savings} = \$2,400,000 - \$1,900,000 = \$500,000 \quad (20.83\%\text{ reduction})$$
* **Answer**: Cloud migration delivers **$500,000 net savings** (20.83% TCO reduction).

---

### Problem 11: Little's Law in API Microservice Concurrency
* **Question**: A payment microservice processes an average arrival rate of $\lambda = 250\text{ requests/sec}$. The average response latency is $W = 80\text{ milliseconds}$. Calculate the mean number of concurrent requests $L$ in the system.
* **Formula & Steps**:
  $$W = 80\text{ ms} = 0.080\text{ seconds}$$
  $$L = \lambda \times W = 250 \times 0.080 = 20\text{ concurrent requests}$$
* **Answer**: Exactly **20 concurrent in-flight requests**. If thread pool capacity is 30, the service operates safely at 66.7% capacity.

---

### Problem 12: Discounted Cash Flow & Net Present Value (NPV)
* **Question**: A digital transformation project requires an initial investment of $500,000. Projected cash inflows are: Year 1: $200k, Year 2: $250k, Year 3: $250k. The enterprise discount rate is 10%. Calculate undiscounted ROI and NPV.
* **Calculations**:
  $$\text{Undiscounted Net Gain} = (200k + 250k + 250k) - 500k = \$700,000 - \$500,000 = \$200,000$$
  $$\text{Undiscounted ROI} = \frac{200,000}{500,000} \times 100\% = 40.0\%$$
  $$\text{PV}_{\text{Year 1}} = \frac{200,000}{1.10^1} \approx \$181,818.18$$
  $$\text{PV}_{\text{Year 2}} = \frac{250,000}{1.10^2} \approx \$206,611.57$$
  $$\text{PV}_{\text{Year 3}} = \frac{250,000}{1.10^3} \approx \$187,828.70$$
  $$\text{Total Present Value} = \$576,258.45$$
  $$\text{NPV} = \$576,258.45 - \$500,000 = +\$76,258.45$$
* **Answer**: Undiscounted ROI is **40.0%**; Net Present Value at 10% discount is **+$76,258.45** (financially accretive).

---

### Problem 13: Compound Growth vs Simple Interest Accumulation
* **Question**: An endowment of $100,000 earns 8% per annum over 10 years. Compare future value under simple interest versus annual compounding.
* **Calculations**:
  $$\text{FV}_{\text{Simple}} = \$100,000 \times [1 + (0.08 \times 10)] = \$100,000 \times 1.80 = \$180,000.00$$
  $$\text{FV}_{\text{Compound}} = \$100,000 \times (1.08)^{10} = \$100,000 \times 2.158925 = \$215,892.50$$
  $$\text{Compounding Premium} = \$215,892.50 - \$180,000.00 = \$35,892.50$$
* **Answer**: Compounding yields an additional **$35,892.50** (+19.94% above simple interest).

---

### Problem 14: Data Migration Bandwidth & Transfer Time
* **Question**: A database snapshot of 4.5 Terabytes (TB) must be transferred over a 10 Gbps dedicated interconnect operating at 80% effective utilization. Calculate transfer time in seconds and hours.
* **Calculations**:
  $$\text{Total Bits} = 4.5\text{ TB} = 4.5 \times 10^{12}\text{ bytes} \times 8 = 36.0 \times 10^{12}\text{ bits}$$
  $$\text{Effective Bandwidth} = 10\text{ Gbps} \times 0.80 = 8.0\text{ Gbps} = 8.0 \times 10^9\text{ bits/sec}$$
  $$\text{Transfer Time (seconds)} = \frac{36.0 \times 10^{12}}{8.0 \times 10^9} = 4,500\text{ seconds}$$
  $$\text{Transfer Time (hours)} = \frac{4,500}{3,600} = 1.25\text{ hours} \quad (1\text{ hour } 15\text{ mins})$$
* **Answer**: Exactly **4,500 seconds** (1.25 hours).

---

### Problem 15: Multi-Cloud Blended Cost per Transaction
* **Question**: A distributed architecture processes 100,000 daily transactions across 3 cloud providers:
  * AWS: 50,000 tx @ $0.04/tx
  * Azure: 30,000 tx @ $0.06/tx
  * GCP: 20,000 tx @ $0.09/tx
  Calculate the weighted average cost per transaction.
* **Calculations**:
  $$\text{Total Spend} = (50,000 \times 0.04) + (30,000 \times 0.06) + (20,000 \times 0.09) = 2,000 + 1,800 + 1,800 = \$5,600$$
  $$\text{Blended Cost/tx} = \frac{\$5,600}{100,000} = \$0.0560/\text{transaction} \quad (5.60\text{ cents})$$
* **Answer**: **$0.0560 per transaction**.

---

### Problem 16: Data Center Power Usage Effectiveness (PUE)
* **Question**: A Tokyo data center consumes 15.0 GWh/year total facility energy, of which 10.0 GWh powers IT server equipment and 5.0 GWh powers cooling/lighting. If liquid immersion cooling cuts overhead to 2.0 GWh, calculate PUE before and after, plus energy savings percentage.
* **Calculations**:
  $$\text{PUE}_{\text{Initial}} = \frac{\text{Total Energy}}{\text{IT Energy}} = \frac{15.0}{10.0} = 1.50$$
  $$\text{PUE}_{\text{New}} = \frac{10.0 + 2.0}{10.0} = \frac{12.0}{10.0} = 1.20$$
  $$\text{Total Energy Reduction} = \frac{15.0 - 12.0}{15.0} \times 100\% = 20.0\%$$
* **Answer**: PUE improves from **1.50 to 1.20**, reducing total power consumption by **20.0%**.

---

### Problem 17: Machine Learning Confusion Matrix Performance
* **Question**: On an imbalanced test dataset of 1,000 samples (100 Positives, 900 Negatives), a model yields: $TP = 80, FN = 20, FP = 40, TN = 860$. Calculate Precision, Recall, Specificity, and F1-Score.
* **Formulas & Steps**:
  $$\text{Precision} = \frac{TP}{TP + FP} = \frac{80}{80 + 40} = \frac{80}{120} \approx 66.67\%$$
  $$\text{Recall} = \frac{TP}{TP + FN} = \frac{80}{80 + 20} = \frac{80}{100} = 80.00\%$$
  $$\text{Specificity} = \frac{TN}{TN + FP} = \frac{860}{860 + 40} = \frac{860}{900} \approx 95.56\%$$
  $$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{(2/3) \times 0.8}{(2/3) + 0.8} = \frac{16/15}{22/15} = \frac{8}{11} \approx 72.73\%$$
* **Answer**: Precision = **66.67%**, Recall = **80.00%**, Specificity = **95.56%**, F1-Score = **72.73%**.

---

### Problem 18: Inventory Turnover & Working Capital Unlocked
* **Question**: A retailer reports annual COGS of $48,000,000 and average inventory of $8,000,000. Calculate Inventory Turnover and Days Sales of Inventory (DSI). If digital demand sensing boosts turnover to 8.0x, how much cash working capital is unlocked?
* **Calculations**:
  $$\text{Turnover} = \frac{\text{COGS}}{\text{Avg Inventory}} = \frac{48,000,000}{8,000,000} = 6.0\text{ turns/year}$$
  $$\text{DSI} = \frac{365}{\text{Turnover}} = \frac{365}{6.0} \approx 60.83\text{ days}$$
  $$\text{Required Inventory @ 8.0x} = \frac{\$48,000,000}{8.0} = \$6,000,000$$
  $$\text{Unlocked Working Capital} = \$8,000,000 - \$6,000,000 = \$2,000,000$$
* **Answer**: Current turnover is **6.0x** (DSI = 60.83 days). Accelerating turnover to 8.0x unlocks **$2,000,000** in cash.

---

### Problem 19: Cold Storage Lifecycle Tiering Cost Benefit
* **Question**: An enterprise retains 100 TB (100,000 GB) of compliance archives in standard cloud storage @ $0.023/GB/month ($27,600/year). Glacier Deep Archive costs $0.00099/GB/month ($1,188/year). If 2 TB is retrieved once annually at $0.02/GB retrieval fee + $0.09/GB egress fee ($220 total retrieval cost), calculate net annual financial savings.
* **Calculations**:
  $$\text{Standard Storage Annual Cost} = 100,000 \times 0.023 \times 12 = \$27,600.00$$
  $$\text{Deep Archive Storage Annual Cost} = 100,000 \times 0.00099 \times 12 = \$1,188.00$$
  $$\text{Storage Savings} = \$27,600 - \$1,188 = \$26,412.00$$
  $$\text{Retrieval & Egress Cost} = 2,000\text{ GB} \times (\$0.02 + \$0.09) = 2,000 \times \$0.11 = \$220.00$$
  $$\text{Net Annual Benefit} = \$26,412.00 - \$220.00 = \$26,192.00 \quad (94.90\%\text{ net savings})$$
* **Answer**: **$26,192.00 net annual savings** (94.90% cost reduction).

---

### Problem 20: Market Sizing TAM, SAM & SOM (Bottom-Up vs Top-Down)
* **Question**: Estimate the addressable market for Cloud ERP Modernization targeting mid-market manufacturing companies in Japan:
  * Top-Down: Total Japan Enterprise Software Market is $12B. Manufacturing comprises 35% ($4.2B); cloud modernization slice is 25% -> TAM = $1.05B.
  * Bottom-Up: 25,000 mid-market manufacturers in Japan. 40% operate legacy on-prem systems (10,000 firms). Average contract value is $50,000/year.
  * Compute Bottom-Up TAM. Sizing SAM (Kanto & Kansai industrial clusters, 65% of firms) and SOM (Accenture Japan target 12% market share).
* **Calculations**:
  $$\text{Bottom-Up TAM} = 10,000\text{ firms} \times \$50,000/\text{firm/year} = \$500,000,000/\text{year} \quad (\$500M)$$
  $$\text{SAM (65\% Cluster Focus)} = \$500,000,000 \times 0.65 = \$325,000,000/\text{year} \quad (\$325M)$$
  $$\text{SOM (12\% Target Share)} = \$325,000,000 \times 0.12 = \$39,000,000/\text{year} \quad (\$39M)$$
* **Answer**: Bottom-Up TAM is **$500M**, SAM is **$325M**, and attainable SOM is **$39M/year**.

---

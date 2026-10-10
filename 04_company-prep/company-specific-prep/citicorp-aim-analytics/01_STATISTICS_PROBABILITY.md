# 01. Statistics & Probability — Complete Study Material & Question Bank

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: High-yield domain tested in OA Section 3 and Technical Interview Round 1.

---

## 1. Probability Fundamentals & Rules

### 1.1 Axioms & Addition Laws
* **Non-negativity**: $0 \le P(A) \le 1$ for any event $A$.
* **Total Sample Space**: $P(S) = 1$.
* **Addition Rule for Any Two Events**:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
* If $A$ and $B$ are **mutually exclusive** (disjoint, $A \cap B = \emptyset$):
  $$P(A \cup B) = P(A) + P(B)$$

### 1.2 Conditional Probability & Independence
* **Conditional Probability**: Probability of event $A$ occurring given that event $B$ has occurred:
  $$P(A | B) = \frac{P(A \cap B)}{P(B)}, \quad \text{where } P(B) > 0$$
* **Multiplication Rule**:
  $$P(A \cap B) = P(A | B) \cdot P(B) = P(B | A) \cdot P(A)$$
* **Statistical Independence**: Two events are independent if knowing $B$ provides zero information about $A$:
  $$P(A | B) = P(A) \iff P(A \cap B) = P(A) \cdot P(B)$$
  > **Interview Trap**: Independent events are **NOT** mutually exclusive. If $A$ and $B$ are mutually exclusive and have non-zero probabilities, they are strictly dependent because if $A$ occurs, $B$ cannot occur ($P(A \cap B) = 0 \neq P(A)P(B)$).

---

## 2. Bayes' Theorem & Total Probability

### 2.1 Law of Total Probability
If $B_1, B_2, \dots, B_k$ partition the sample space $S$ (mutually exclusive and exhaustive, $\sum_{i=1}^k P(B_i) = 1$):
$$P(A) = \sum_{i=1}^k P(A | B_i) \cdot P(B_i)$$

### 2.2 Bayes' Rule
$$P(B_j | A) = \frac{P(A | B_j) \cdot P(B_j)}{\sum_{i=1}^k P(A | B_i) \cdot P(B_i)}$$
* $P(B_j)$: **Prior Probability** (baseline belief before evidence).
* $P(A | B_j)$: **Likelihood** (probability of evidence given the hypothesis).
* $P(B_j | A)$: **Posterior Probability** (updated belief after observing evidence).

---

## 3. Probability Distributions

### 3.1 Discrete Distributions Summary

| Distribution | Probability Mass Function (PMF) | Mean ($\mu$) | Variance ($\sigma^2$) | Key Banking Application |
| :--- | :--- | :---: | :---: | :--- |
| **Bernoulli** | $P(X=1)=p, P(X=0)=1-p$ | $p$ | $p(1-p)$ | Single transaction default / non-default. |
| **Binomial** | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | Number of defaulted loans out of $n$ applicants. |
| **Poisson** | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | Number of ATM transactions or customer calls per hour. |
| **Geometric** | $P(X=k) = (1-p)^{k-1} p$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | Number of telemarketing calls until first loan conversion. |

### 3.2 Continuous Distributions Summary

#### 1. Normal (Gaussian) Distribution: $X \sim \mathcal{N}(\mu, \sigma^2)$
* Density Function:
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$
* **68–95–99.7 Empirical Rule**:
  * $P(\mu - 1\sigma \le X \le \mu + 1\sigma) \approx 68.27\%$
  * $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 95.45\%$
  * $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 99.73\%$
* **Standard Normal Transformation ($Z$-score)**:
  $$Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$$

#### 2. Student's $t$-Distribution: $t \sim t(\nu)$
* Symmetric, bell-shaped, but has **heavier tails** than standard normal.
* Degrees of freedom $\nu = n - 1$. As $n \to \infty$, $t(\nu) \to \mathcal{N}(0, 1)$.
* **When to use**: Sample size is small ($n < 30$) and population standard deviation $\sigma$ is **unknown** (estimated via sample standard deviation $s$).

#### 3. Chi-Square ($\chi^2$) Distribution
* Sum of squared independent standard normal variables: $\chi^2 = \sum_{i=1}^k Z_i^2$.
* Degrees of freedom $k$. Mean = $k$, Variance = $2k$. Positively skewed.
* Used for testing variances, goodness-of-fit, and categorical independence in contingency tables.

---

## 4. Central Limit Theorem (CLT) & Sampling

### 4.1 Formal Theorem
Let $X_1, X_2, \dots, X_n$ be an i.i.d. random sample drawn from **ANY** population distribution with finite mean $\mu$ and finite variance $\sigma^2$. As sample size $n \to \infty$:
$$\bar{X}_n \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$
Standardized:
$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

* **Standard Error (SE)**: $\text{SE} = \frac{\sigma}{\sqrt{n}}$ (or $\frac{s}{\sqrt{n}}$ when $\sigma$ unknown).
* **Rule of Thumb**: For most non-normal distributions, $n \ge 30$ is sufficient for the sample mean distribution to approximate normal.

---

## 5. Hypothesis Testing Framework

### 5.1 The 5 Steps
1. Formulate **Null Hypothesis ($H_0$)** (no effect, equality) and **Alternative Hypothesis ($H_1$)** (effect exists, inequality).
2. Choose significance level $\alpha$ (typically $0.05$ or $0.01$).
3. Identify test statistic ($Z$, $t$, $F$, $\chi^2$) based on sample size and known parameters.
4. Compute test statistic and calculate **p-value**.
5. Decision Rule:
   * If $\text{p-value} \le \alpha \implies$ **Reject $H_0$** (Statistically significant result).
   * If $\text{p-value} > \alpha \implies$ **Fail to reject $H_0$**.

### 5.2 What is a p-value? (Exact Interview Definition)
* A **p-value** is the probability of obtaining a test statistic at least as extreme as the one observed, **under the assumption that the null hypothesis $H_0$ is true**.
* It is **NOT** the probability that $H_0$ is true. It is **NOT** the probability that the result occurred by random chance.

### 5.3 Type I vs Type II Errors & Power

| Reality \ Decision | Fail to Reject $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ is True** | **Correct Decision** ($1 - \alpha$) | **Type I Error ($\alpha$)** (False Alarm) |
| **$H_0$ is False** | **Type II Error ($\beta$)** (Missed Detection) | **Correct Decision** ($1 - \beta$, Power) |

* **Type I Error ($\alpha$)**: Concluding there is an effect when none exists. (e.g., Flagging a legitimate transaction as fraud).
* **Type II Error ($\beta$)**: Failing to detect an effect that exists. (e.g., Approving a borrower who goes on to default).
* **Statistical Power ($1 - \beta$)**: Probability of correctly rejecting a false null hypothesis. To increase power: increase sample size $n$, increase effect size, or increase $\alpha$.

---

## 6. Essential Statistical Tests Matrix

| Test Name | Primary Purpose | Test Statistic Formula | Key Assumptions |
| :--- | :--- | :--- | :--- |
| **One-Sample $Z$-Test** | Compare sample mean to known population mean when $\sigma$ is known. | $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$ | Known $\sigma$, Normal population or $n \ge 30$. |
| **One-Sample $t$-Test** | Compare sample mean to $\mu_0$ when $\sigma$ is unknown. | $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}, \quad df = n-1$ | Unknown $\sigma$, Normal population or $n \ge 30$. |
| **Two-Sample $t$-Test (Independent)** | Compare means of two distinct groups. | $t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$ | Independent groups, continuous data. |
| **Paired $t$-Test** | Compare before/after means on same subjects. | $t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad df = n-1$ | Dependent/matched pairs, $d_i = X_{1i} - X_{2i}$. |
| **One-Way ANOVA** | Compare means across $\ge 3$ groups. | $F = \frac{\text{MS}_{between}}{\text{MS}_{within}}$ | Normally distributed residuals, equal variances. |
| **Chi-Square ($\chi^2$) Test** | Test relationship between two categorical variables. | $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}, \quad E = \frac{R \cdot C}{N}$ | Expected frequency $E_i \ge 5$ in all cells. |

---

## 7. 20 Fully Solved Numerical Interview Questions

### Q1: Conditional Probability & Card Draw
**Question**: Two cards are drawn from a standard 52-card deck without replacement. What is the probability that both cards are Aces?  
**Solution**:  
* $P(\text{First Ace}) = \frac{4}{52} = \frac{1}{13}$.
* $P(\text{Second Ace} | \text{First Ace}) = \frac{3}{51} = \frac{1}{17}$.
* $P(\text{Both Aces}) = \frac{1}{13} \times \frac{1}{17} = \frac{1}{221} \approx 0.00452$ ($0.45\%$).

---

### Q2: Bayes' Theorem in Medical / Fraud Diagnosis
**Question**: A disease affects $0.5\%$ of the population. A diagnostic test is $98\%$ accurate for positive patients (sensitivity) and has a $3\%$ false positive rate on healthy individuals. If a random patient tests positive, what is the probability that they actually have the disease?  
**Solution**:  
* Prior: $P(D) = 0.005$, $P(D') = 0.995$.
* Likelihoods: $P(+ | D) = 0.98$, $P(+ | D') = 0.03$.
* Total probability of positive test:
  $$P(+) = (0.98 \times 0.005) + (0.03 \times 0.995) = 0.0049 + 0.02985 = 0.03475$$
* Posterior probability:
  $$P(D | +) = \frac{0.0049}{0.03475} \approx 0.141 \implies \mathbf{14.1\%}$$
* *Key Takeaway*: Despite $98\%$ test accuracy, the posterior probability is only $14.1\%$ due to the low base rate of the disease.

---

### Q3: Binomial Default Probability
**Question**: A microfinance portfolio approves 10 loans. The historical default rate for each loan is $p = 0.10$, assuming defaults are independent. What is the probability that:  
(a) Exactly 1 loan defaults?  
(b) At least 1 loan defaults?  
**Solution**:  
* (a) $P(X = 1) = \binom{10}{1} (0.1)^1 (0.9)^9 = 10 \times 0.1 \times 0.3874 = \mathbf{0.3874}$ ($38.74\%$).
* (b) $P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{10}{0} (0.1)^0 (0.9)^{10} = 1 - 0.3487 = \mathbf{0.6513}$ ($65.13\%$).

---

### Q4: Poisson Process ATM Arrivals
**Question**: An ATM receives an average of 4 customers per hour.  
(a) What is the probability of receiving exactly 2 customers in an hour?  
(b) What is the probability of receiving zero customers in a 30-minute window?  
**Solution**:  
* (a) $\lambda = 4$ per hour.
  $$P(X = 2) = \frac{4^2 e^{-4}}{2!} = \frac{16 \times 0.0183}{2} = \mathbf{0.1465} \quad (14.65\%)$$
* (b) For 30 minutes, adjusted arrival rate $\lambda' = 4 \times 0.5 = 2$.
  $$P(X = 0) = \frac{2^0 e^{-2}}{0!} = e^{-2} = \mathbf{0.1353} \quad (13.53\%)$$

---

### Q5: Normal Distribution Credit Card Spend
**Question**: Monthly credit card spend for premium users is normally distributed with mean $\mu = \$2,500$ and standard deviation $\sigma = \$500$.  
(a) What percentage of users spend over $\$3,500$?  
(b) What spend threshold separates the top $5\%$ of spenders?  
**Solution**:  
* (a) Standardize $X = 3500$:
  $$Z = \frac{3500 - 2500}{500} = \frac{1000}{500} = +2.0$$
  From standard normal tables: $P(Z > 2.0) = 1 - 0.9772 = \mathbf{0.0228}$ ($2.28\%$).
* (b) Top $5\%$ corresponds to $Z_{0.05} = 1.645$:
  $$X = \mu + Z \sigma = 2500 + (1.645 \times 500) = 2500 + 822.5 = \mathbf{\$3,322.50}$$

---

### Q6: Central Limit Theorem Confidence Interval
**Question**: A sample of $n = 100$ savings accounts has a sample mean balance of $\bar{X} = \$4,200$ with sample standard deviation $s = \$800$. Construct a $95\%$ confidence interval for the population mean balance.  
**Solution**:  
* Standard Error: $\text{SE} = \frac{s}{\sqrt{n}} = \frac{800}{\sqrt{100}} = \frac{800}{10} = 80$.
* For $95\%$ confidence level, critical value $Z^* = 1.96$.
* Margin of error: $\text{ME} = 1.96 \times 80 = 156.80$.
* Confidence Interval:
  $$\text{CI} = [4200 - 156.80, 4200 + 156.80] = \mathbf{[\$4,043.20, \$4,356.80]}$$

---

### Q7: Hypothesis Testing (One-Sample $Z$-Test)
**Question**: Historical average call handle time at Citi's contact center is $\mu_0 = 180\text{ seconds}$ with $\sigma = 30\text{ seconds}$. A new routing software is piloted across $n = 64$ calls, resulting in a mean handle time of $\bar{X} = 171\text{ seconds}$. Test at $\alpha = 0.05$ whether the new software significantly reduced handle time.  
**Solution**:  
* $H_0: \mu = 180$ vs $H_1: \mu < 180$ (One-tailed test).
* Test statistic:
  $$Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} = \frac{171 - 180}{30 / \sqrt{64}} = \frac{-9}{30 / 8} = \frac{-9}{3.75} = -2.40$$
* Critical value for left-tailed test at $\alpha = 0.05$ is $Z_{crit} = -1.645$.
* Decision: Since $Z_{calc} = -2.40 < -1.645$ (and $\text{p-value} = 0.0082 < 0.05$), we **reject $H_0$**. The new software significantly reduces handle time.

---

### Q8: Two-Sample $t$-Test (Campaign A/B Test)
**Question**: An email campaign is A/B tested to increase credit line utilization.  
* Group A (Variant 1): $n_1 = 36$, $\bar{X}_1 = \$650$, $s_1 = \$120$.  
* Group B (Variant 2): $n_2 = 36$, $\bar{X}_2 = \$710$, $s_2 = \$150$.  
Test at $\alpha = 0.05$ if Variant 2 generated significantly higher spend.  
**Solution**:  
* $H_0: \mu_2 - \mu_1 = 0$ vs $H_1: \mu_2 - \mu_1 > 0$.
* Standard Error:
  $$\text{SE} = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} = \sqrt{\frac{14400}{36} + \frac{22500}{36}} = \sqrt{400 + 625} = \sqrt{1025} \approx 32.02$$
* Test statistic:
  $$t = \frac{\bar{X}_2 - \bar{X}_1}{\text{SE}} = \frac{710 - 650}{32.02} = \frac{60}{32.02} \approx 1.874$$
* For $df \approx 70$ at one-tailed $\alpha = 0.05$, $t_{crit} \approx 1.667$.
* Decision: Since $t_{calc} = 1.874 > 1.667$, we **reject $H_0$**. Variant 2 generates statistically significant higher spend.

---

### Q9: Chi-Square Test of Independence
**Question**: Survey data classifies 200 bank customers by Tier (Standard, Gold) and whether they Churned (Yes, No):

| Tier \ Churn | Churned (Yes) | Retained (No) | Total |
| :--- | :---: | :---: | :---: |
| **Standard** | 40 | 60 | 100 |
| **Gold** | 20 | 80 | 100 |
| **Total** | 60 | 140 | 200 |

Test at $\alpha = 0.05$ whether Churn is independent of Customer Tier.  
**Solution**:  
* Expected frequencies: $E = \frac{\text{Row Total} \times \text{Col Total}}{\text{Grand Total}}$.
  * $E_{Standard, Yes} = \frac{100 \times 60}{200} = 30$.
  * $E_{Standard, No} = \frac{100 \times 140}{200} = 70$.
  * $E_{Gold, Yes} = \frac{100 \times 60}{200} = 30$.
  * $E_{Gold, No} = \frac{100 \times 140}{200} = 70$.
* Chi-Square Calculation:
  $$\chi^2 = \frac{(40 - 30)^2}{30} + \frac{(60 - 70)^2}{70} + \frac{(20 - 30)^2}{30} + \frac{(80 - 70)^2}{70}$$
  $$\chi^2 = \frac{100}{30} + \frac{100}{70} + \frac{100}{30} + \frac{100}{70} = 3.33 + 1.43 + 3.33 + 1.43 = \mathbf{9.52}$$
* Degrees of Freedom: $df = (2 - 1) \times (2 - 1) = 1$.
* Critical value: $\chi^2_{0.05, 1} = 3.841$.
* Decision: Since $\chi^2_{calc} = 9.52 > 3.841$, we **reject $H_0$**. Churn rate is significantly dependent on customer tier.

---

### Q10: Expectation & Fair Game
**Question**: You pay $\$10$ to play a game. You roll a fair 6-sided die. If you roll a 6, you win $\$36$. If you roll an odd number (1, 3, 5), you win $\$6$. If you roll a 2 or 4, you win nothing. What is your expected net payoff?  
**Solution**:  
* Outcome distribution:
  * Roll 6: $P = \frac{1}{6}$, Net = $\$36 - \$10 = +\$26$.
  * Roll 1, 3, 5: $P = \frac{3}{6} = \frac{1}{2}$, Net = $\$6 - \$10 = -\$4$.
  * Roll 2, 4: $P = \frac{2}{6} = \frac{1}{3}$, Net = $\$0 - \$10 = -\$10$.
* Expected Value:
  $$E[X] = \left(\frac{1}{6} \times 26\right) + \left(\frac{1}{2} \times (-4)\right) + \left(\frac{1}{3} \times (-10)\right) = 4.33 - 2.00 - 3.33 = \mathbf{-\$1.00}$$
* You expect to lose $\$1.00$ per game on average.

---

### Q11: Variance of a Linear Combination
**Question**: If random variables $X$ and $Y$ have $\text{Var}(X) = 16$, $\text{Var}(Y) = 25$, and correlation coefficient $r = 0.40$, calculate $\text{Var}(2X - 3Y)$.  
**Solution**:  
* Formula:
  $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab \text{Cov}(X, Y)$$
* Covariance:
  $$\text{Cov}(X, Y) = r \cdot \sigma_X \cdot \sigma_Y = 0.40 \times \sqrt{16} \times \sqrt{25} = 0.40 \times 4 \times 5 = 8$$
* Substitute $a = 2, b = -3$:
  $$\text{Var}(2X - 3Y) = 2^2(16) + (-3)^2(25) + 2(2)(-3)(8)$$
  $$\text{Var}(2X - 3Y) = (4 \times 16) + (9 \times 25) - 12(8) = 64 + 225 - 96 = \mathbf{193}$$

---

### Q12: Geometric Distribution Waiting Time
**Question**: The probability that a cold sales call converts to an investment account is $p = 0.04$.  
(a) What is the expected number of calls required to secure the first conversion?  
(b) What is the probability that it takes more than 10 calls?  
**Solution**:  
* (a) Expected value: $E[X] = \frac{1}{p} = \frac{1}{0.04} = \mathbf{25\text{ calls}}$.
* (b) $P(X > 10) = (1 - p)^{10} = (0.96)^{10} \approx \mathbf{0.6648}$ ($66.48\%$).

---

### Q13: Simpson's Paradox Verification
**Question**: An analytics team reviews approval rates for two loan underwriting teams across Small and Large loan requests:
* Team A: Approves $90/100$ small loans ($90\%$) and $20/100$ large loans ($20\%$).
* Team B: Approves $85/100$ small loans ($85\%$) and $15/100$ large loans ($15\%$).
Show that if Team A receives 10 small loans and 90 large loans, while Team B receives 90 small loans and 10 large loans, the aggregate results reverse.  
**Solution**:  
* Team A aggregate approvals:
  $$(10 \times 0.90) + (90 \times 0.20) = 9 + 18 = 27 \implies \frac{27}{100} = \mathbf{27\%}$$
* Team B aggregate approvals:
  $$(90 \times 0.85) + (10 \times 0.15) = 76.5 + 1.5 = 78 \implies \frac{78}{100} = \mathbf{78\%}$$
* *Insight*: Team A has a higher approval rate in *both* individual categories ($90\% > 85\%$ and $20\% > 15\%$), but Team B appears to have a far higher overall approval rate ($78\% \gg 27\%$) due to the confounding effect of loan mix.

---

### Q14: Correlation vs Linearity
**Question**: Let $X$ be uniformly distributed over $[-1, 1]$. Define $Y = X^2$. Find the Pearson correlation coefficient between $X$ and $Y$.  
**Solution**:  
* $E[X] = 0$ by symmetry.
* $E[XY] = E[X \cdot X^2] = E[X^3] = 0$ by symmetry of odd power.
* Covariance:
  $$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 0 - (0 \cdot E[Y]) = 0$$
* Correlation:
  $$r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \mathbf{0}$$
* *Insight*: $r = 0$ proves there is **zero linear correlation**, even though $Y$ has a perfect, deterministic non-linear relationship with $X$.

---

### Q15: Unbiased Sample Variance ($n-1$ Derivation Intuition)
**Question**: Why do we divide by $n - 1$ instead of $n$ when calculating sample variance $s^2 = \frac{\sum (X_i - \bar{X})^2}{n - 1}$?  
**Solution**:  
* When using sample mean $\bar{X}$ instead of true population mean $\mu$, the deviations $(X_i - \bar{X})$ are measured from the center of the sample itself, which systematically underestimates the spread from the true population center $\mu$.
* Specifically: $E\left[\sum (X_i - \bar{X})^2\right] = (n - 1) \sigma^2$.
* Dividing by $n$ produces a biased estimator: $E[s_n^2] = \frac{n-1}{n}\sigma^2 < \sigma^2$.
* Bessel's correction divides by $n - 1$ (the degrees of freedom remaining after estimating $\bar{X}$) to ensure $E[s^2] = \sigma^2$ (an unbiased estimator).

---

### Q16: Type I and Type II Error Calculation
**Question**: Let $X \sim \mathcal{N}(\mu, 16)$ with $n = 16$. Test $H_0: \mu = 50$ vs $H_1: \mu = 54$. Decision rule: Reject $H_0$ if $\bar{X} \ge 52$.  
(a) Find Type I error probability $\alpha$.  
(b) Find Type II error probability $\beta$.  
**Solution**:  
* Standard Error: $\text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{4}{\sqrt{16}} = 1.0$.
* (a) Type I error: Reject $H_0$ given $\mu = 50$:
  $$Z = \frac{52 - 50}{1.0} = +2.0 \implies \alpha = P(Z \ge 2.0) = \mathbf{0.0228} \quad (2.28\%)$$
* (b) Type II error: Fail to reject $H_0$ given $\mu = 54$:
  $$Z = \frac{52 - 54}{1.0} = -2.0 \implies \beta = P(Z \le -2.0) = \mathbf{0.0228} \quad (2.28\%)$$
* Power = $1 - \beta = 1 - 0.0228 = \mathbf{97.72\%}$.

---

### Q17: Birthday Problem (Collision Probability in Hashing / Fraud)
**Question**: What is the minimum number of people in a room such that the probability that at least two share a birthday exceeds $50\%$?  
**Solution**:  
* Probability of all $n$ people having distinct birthdays:
  $$P(\text{All distinct}) = \frac{365}{365} \times \frac{364}{365} \times \cdots \times \frac{365 - n + 1}{365}$$
* Using approximation $1 - x \approx e^{-x}$:
  $$P(\text{All distinct}) \approx \exp\left(-\frac{\sum_{i=1}^{n-1} i}{365}\right) = \exp\left(-\frac{n(n-1)}{2 \times 365}\right)$$
* Set $P(\text{Match}) = 1 - \exp\left(-\frac{n(n-1)}{730}\right) \ge 0.50 \implies \frac{n(n-1)}{730} \ge \ln(2) \approx 0.693$:
  $$n^2 - n \ge 505.9 \implies n \ge 23$$
* At **$n = 23$ people**, $P(\text{Match}) \approx 50.7\%$.

---

### Q18: Bayes' Sequential Updating
**Question**: A credit applicant is either Low Risk ($L$, prior $P(L) = 0.70$) or High Risk ($H$, prior $P(H) = 0.30$). In any given month, $P(\text{Late} | L) = 0.05$ and $P(\text{Late} | H) = 0.40$. The applicant is late on payment in Month 1.  
(a) Find the posterior probability that the applicant is High Risk.  
(b) If the same applicant is also late in Month 2 (assuming monthly payments are conditionally independent), what is the updated posterior probability?  
**Solution**:  
* (a) Month 1:
  $$P(\text{Late}_1) = (0.70 \times 0.05) + (0.30 \times 0.40) = 0.035 + 0.120 = 0.155$$
  $$P(H | \text{Late}_1) = \frac{0.120}{0.155} = \mathbf{0.7742} \quad (77.42\%)$$
* (b) Month 2: Use $P(H) = 0.7742$ and $P(L) = 0.2258$ as new priors:
  $$P(\text{Late}_2) = (0.2258 \times 0.05) + (0.7742 \times 0.40) = 0.01129 + 0.30968 = 0.32097$$
  $$P(H | \text{Late}_1 \cap \text{Late}_2) = \frac{0.30968}{0.32097} = \mathbf{0.9648} \quad (96.48\%)$$

---

### Q19: Maximum Likelihood Estimation (MLE) for Bernoulli
**Question**: Given an i.i.d. sample of $n$ credit card transactions with $k$ defaults ($x_i \in \{0, 1\}$). Derive the Maximum Likelihood Estimator for the default probability $p$.  
**Solution**:  
* Likelihood function:
  $$L(p) = \prod_{i=1}^n p^{x_i} (1 - p)^{1 - x_i} = p^{\sum x_i} (1 - p)^{n - \sum x_i} = p^k (1 - p)^{n - k}$$
* Log-Likelihood:
  $$\ln L(p) = k \ln(p) + (n - k) \ln(1 - p)$$
* Take derivative with respect to $p$ and set to zero:
  $$\frac{d}{dp} \ln L(p) = \frac{k}{p} - \frac{n - k}{1 - p} = 0$$
  $$\frac{k}{p} = \frac{n - k}{1 - p} \implies k(1 - p) = p(n - k) \implies k = np \implies \hat{p} = \frac{k}{n}$$
* The MLE is simply the sample proportion of defaults.

---

### Q20: Uniform Distribution Minimum/Maximum
**Question**: If $X$ and $Y$ are independent random variables uniformly distributed on $[0, 1]$. What is the expected value of $M = \max(X, Y)$?  
**Solution**:  
* Cumulative distribution function of $M$:
  $$F_M(m) = P(M \le m) = P(X \le m \text{ and } Y \le m) = P(X \le m) \cdot P(Y \le m) = m \cdot m = m^2, \quad 0 \le m \le 1$$
* Probability density function:
  $$f_M(m) = \frac{d}{dm}(m^2) = 2m, \quad 0 \le m \le 1$$
* Expected value:
  $$E[M] = \int_0^1 m \cdot f_M(m) \, dm = \int_0^1 m(2m) \, dm = \int_0^1 2m^2 \, dm = \left[ \frac{2m^3}{3} \right]_0^1 = \mathbf{\frac{2}{3}}$$

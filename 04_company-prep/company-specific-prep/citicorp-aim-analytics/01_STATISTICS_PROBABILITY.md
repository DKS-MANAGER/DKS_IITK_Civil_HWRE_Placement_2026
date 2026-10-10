# 01. Statistics & Probability — Complete Study Guide & Practice Bank

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Evaluated in Online Assessment Section 3 and Technical Interview Round 1.  
> **Pedagogical Standard**: Combines first-principles mathematical derivations, practical financial interpretations, and a bank of 30+ verified worked problems.

---

## 1. Probability Fundamentals & Rules

### 1.1 Sample Spaces, Events & Set Algebra
* **Sample Space ($S$)**: The set of all possible mutually exclusive outcomes of a random experiment.
* **Event ($A$)**: Any subset of the sample space ($A \subseteq S$).
* **Set Operations**:
  * **Union ($A \cup B$)**: The event that either $A$, $B$, or both occur.
  * **Intersection ($A \cap B$)**: The event that both $A$ and $B$ occur simultaneously.
  * **Complement ($A' \text{ or } A^c$)**: The event that $A$ does not occur ($S \setminus A$).

### 1.2 The Three Kolmogorov Axioms of Probability
1. **Non-negativity**: For every event $A$, $0 \le P(A) \le 1$.
2. **Unit Measure**: $P(S) = 1$.
3. **Countable Additivity**: For any sequence of mutually disjoint (exclusive) events $A_1, A_2, \dots$ ($A_i \cap A_j = \emptyset$ for $i \neq j$):
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

### 1.3 Essential Probability Rules
* **Complement Rule**: $P(A') = 1 - P(A)$.
* **General Addition Rule (Inclusion-Exclusion)**:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
  For three events:
  $$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$
* **Conditional Probability**:
  $$P(A | B) = \frac{P(A \cap B)}{P(B)}, \quad \text{provided } P(B) > 0$$
* **General Multiplication Rule**:
  $$P(A \cap B) = P(A | B) \cdot P(B) = P(B | A) \cdot P(A)$$
* **Statistical Independence**: Two events $A$ and $B$ are statistically independent if and only if:
  $$P(A \cap B) = P(A) \cdot P(B) \iff P(A | B) = P(A) \iff P(B | A) = P(B)$$
  > **Crucial Distinction for Technical Interviews**:
  > * **Mutually Exclusive** ($A \cap B = \emptyset$): If one occurs, the other cannot ($P(A \cap B) = 0$).
  > * **Independent** ($P(A \cap B) = P(A)P(B)$): Occurrence of one provides zero information about the other.
  > * If two events have non-zero probabilities and are mutually exclusive, they **CANNOT be independent** because knowing $A$ occurred guarantees $B$ did not occur ($P(B|A) = 0 \neq P(B)$).

---

## 2. Bayes' Theorem & Total Probability

### 2.1 Law of Total Probability
If events $B_1, B_2, \dots, B_k$ form a partition of the sample space $S$ (mutually exclusive and exhaustive, $\sum P(B_i) = 1$ and $B_i \cap B_j = \emptyset$):
$$P(A) = \sum_{i=1}^k P(A \cap B_i) = \sum_{i=1}^k P(A | B_i) \cdot P(B_i)$$

### 2.2 Bayes' Rule (Bayesian Updating)
$$P(B_j | A) = \frac{P(A | B_j) \cdot P(B_j)}{P(A)} = \frac{P(A | B_j) \cdot P(B_j)}{\sum_{i=1}^k P(A | B_i) \cdot P(B_i)}$$

* $P(B_j)$: **Prior Probability** (baseline belief before observing new evidence).
* $P(A | B_j)$: **Likelihood** (probability of evidence given the hypothesis).
* $P(B_j | A)$: **Posterior Probability** (updated belief after incorporating evidence).

### 2.3 The Base Rate Fallacy in Fraud Detection
When evaluating rare events (credit card fraud, AML alerts, system intrusions), even high-accuracy classifiers produce low posterior probabilities due to the low baseline incidence rate.

$$\text{Alert Precision} = P(\text{Fraud} | \text{Alert}) = \frac{P(\text{Alert} | \text{Fraud}) P(\text{Fraud})}{P(\text{Alert} | \text{Fraud}) P(\text{Fraud}) + P(\text{Alert} | \text{Legit}) P(\text{Legit})}$$
If $P(\text{Fraud}) = 0.001$, a false positive rate of even $2\%$ on legitimate transactions will overwhelm the true positives, resulting in precision under $5\%$.

---

## 3. Counting, Permutations, Combinations & Sampling

* **Fundamental Counting Principle**: If task 1 can be done in $n_1$ ways and task 2 in $n_2$ ways, both can be done in $n_1 \times n_2$ ways.
* **Permutations (Order Matters)**:
  $$P(n, k) = \frac{n!}{(n - k)!}$$
* **Combinations (Order Does Not Matter)**:
  $$C(n, k) = \binom{n}{k} = \frac{n!}{k!(n - k)!}$$
* **Sampling Schemes**:
  * **With Replacement**: Draws are independent; probabilities remain constant. Modeled by Binomial / Multinomial distributions.
  * **Without Replacement**: Draws are dependent; probabilities change dynamically with each draw. Modeled by the Hypergeometric distribution. When population size $N \gg n$ ($n/N < 0.05$), sampling without replacement is accurately approximated by the Binomial distribution.

---

## 4. Random Variables, Expectation, Variance & Moments

### 4.1 Discrete vs Continuous Random Variables
* **Discrete**: Takes on countable values. Defined by Probability Mass Function (PMF) $p(x) = P(X = x)$, where $\sum p(x) = 1$.
* **Continuous**: Takes on uncountably infinite values over an interval. Defined by Probability Density Function (PDF) $f(x) \ge 0$, where $\int_{-\infty}^\infty f(x)\,dx = 1$. Note: For continuous variables, $P(X = c) = 0$ for any exact value $c$; probabilities are defined strictly over intervals $P(a \le X \le b) = \int_a^b f(x)\,dx$.
* **Cumulative Distribution Function (CDF)**:
  $$F(x) = P(X \le x) = \begin{cases} \sum_{t \le x} p(t) & \text{(Discrete)} \\ \int_{-\infty}^x f(t)\,dt & \text{(Continuous)} \end{cases}$$

### 4.2 Expected Value (Mean) & Properties
$$E[X] = \begin{cases} \sum x p(x) & \text{(Discrete)} \\ \int_{-\infty}^\infty x f(x)\,dx & \text{(Continuous)} \end{cases}$$
* **Linearity of Expectation (Holds whether variables are independent or dependent)**:
  $$E[aX + bY + c] = aE[X] + bE[Y] + c$$

### 4.3 Variance, Standard Deviation & Covariance
* **Variance**: Measures dispersion around the mean:
  $$\text{Var}(X) = \sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
  * $\text{Var}(aX + b) = a^2 \text{Var}(X)$.
* **Covariance**: Measures joint linear variability:
  $$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$$
* **Variance of Linear Combination**:
  $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab\text{Cov}(X, Y)$$
  If $X$ and $Y$ are independent, $\text{Cov}(X, Y) = 0$, so $\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y)$.
* **Pearson Correlation Coefficient ($r \text{ or } \rho$)**:
  $$\rho_{X, Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}, \quad -1 \le \rho \le +1$$

---

## 5. Comprehensive Probability Distributions

### 5.1 Discrete Distributions Reference Table

| Distribution | Notation | PMF / Formula | Mean ($\mu$) | Variance ($\sigma^2$) | Key Banking / Analytics Context |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Bernoulli** | $\text{Bern}(p)$ | $P(X=x) = p^x (1-p)^{1-x}, \; x \in \{0, 1\}$ | $p$ | $p(1-p)$ | Single customer default ($1$) or non-default ($0$). |
| **Binomial** | $\text{Bin}(n, p)$ | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}, \; k=0,\dots,n$ | $np$ | $np(1-p)$ | Number of loan defaults out of $n$ independent applicants. |
| **Geometric** | $\text{Geom}(p)$ | $P(X=k) = (1-p)^{k-1} p, \; k=1, 2, \dots$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | Number of marketing calls until first loan conversion. Memoryless property. |
| **Poisson** | $\text{Pois}(\lambda)$ | $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}, \; k=0, 1, \dots$ | $\lambda$ | $\lambda$ | Arrival of customer service calls or ATM transactions per hour. |
| **Negative Binomial** | $\text{NB}(r, p)$ | $P(X=k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}$ | $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ | Number of marketing trials required to secure $r$ successful conversions. |

### 5.2 Continuous Distributions Reference Table

| Distribution | Notation | PDF / Formula | Mean ($\mu$) | Variance ($\sigma^2$) | Key Banking / Analytics Context |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Continuous Uniform**| $U(a, b)$ | $f(x) = \frac{1}{b - a}, \; a \le x \le b$ | $\frac{a + b}{2}$ | $\frac{(b - a)^2}{12}$ | Uninformative prior probabilities; pseudo-random number simulation. |
| **Exponential** | $\text{Exp}(\lambda)$ | $f(x) = \lambda e^{-\lambda x}, \; x \ge 0$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Time between consecutive fraud alerts or server transactions. Memoryless. |
| **Normal (Gaussian)** | $\mathcal{N}(\mu, \sigma^2)$ | $f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$ | $\mu$ | $\sigma^2$ | Portfolio return modeling, error terms in regression, sampling means. |
| **Standard Normal** | $\mathcal{N}(0, 1)$ | $\phi(z) = \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{z^2}{2}\right)$ | $0$ | $1$ | Standardized scores ($Z = \frac{X - \mu}{\sigma}$). |
| **Student's $t$** | $t(\nu)$ | Symmetric, heavy-tailed bell curve | $0$ (for $\nu > 1$) | $\frac{\nu}{\nu - 2}$ (for $\nu > 2$) | Small sample inference when population $\sigma$ is unknown. Degrees of freedom $\nu$. |
| **Chi-Square** | $\chi^2(k)$ | Sum of $k$ squared independent $\mathcal{N}(0, 1)$ variables | $k$ | $2k$ | Variance tests, goodness-of-fit, categorical contingency independence. |
| **$F$-Distribution** | $F(d_1, d_2)$ | Ratio of two independent $\chi^2$ variables divided by df | $\frac{d_2}{d_2 - 2}$ | See ANOVA text | Comparison of variances across groups; ANOVA regression overall significance. |

### 5.3 Normal Approximations & Limitations
1. **Normal Approximation to Binomial**:
   * Condition: Applicable when $np \ge 10$ and $n(1 - p) \ge 10$.
   * Continuity Correction: Because Binomial is discrete and Normal is continuous, evaluate $P(X = k)$ as $P(k - 0.5 \le X \le k + 0.5)$.
   * When Unsuitable: Fails when $p$ is very small ($p < 0.05$) or very large. For rare events ($p \to 0, n \to \infty, np = \lambda$), the **Poisson approximation** ($\lambda = np$) must be used instead.
2. **Poisson Approximation to Binomial**:
   * Condition: $n \ge 100$ and $p \le 0.01$ (or $np \le 10$).

---

## 6. Sampling, Estimation & The Central Limit Theorem

### 6.1 Population vs Sample & Types of Bias
* **Population**: The entire collection of entities of interest (e.g., all 50 million active Citi credit cardholders worldwide).
* **Sample**: A measured subset selected to infer population parameters.
* **Biases in Analytics**:
  * **Sampling / Selection Bias**: Systematic exclusion of certain subgroups (e.g., assessing digital payment preference by surveying only branch visitors).
  * **Survivorship Bias**: Analyzing only accounts currently open while ignoring closed/churned accounts (leads to massive overestimation of customer lifetime value).
  * **Non-response Bias**: Customers who answer satisfaction surveys differ systematically from those who ignore them.

### 6.2 Sampling Distributions & The Central Limit Theorem (CLT)
* **The Theorem**: Let $X_1, X_2, \dots, X_n$ be an independent, identically distributed (i.i.d.) random sample from ANY population distribution with finite mean $\mu$ and finite variance $\sigma^2$. As sample size $n \to \infty$:
  $$\bar{X}_n \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$
  Standardized:
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$
* **Standard Error (SE)**: The standard deviation of the sampling distribution of a statistic:
  $$\text{SE}(\bar{X}) = \frac{\sigma}{\sqrt{n}} \quad (\text{or } \frac{s}{\sqrt{n}} \text{ when } \sigma \text{ is estimated from sample})$$
* **Why CLT is Fundamental to Banking Analytics**: It allows analysts to compute valid confidence intervals and run hypothesis tests on sample averages (e.g., mean transaction amount, average customer spend) even when the underlying individual data is heavily right-skewed or non-normal, provided $n$ is sufficiently large ($n \ge 30$).

### 6.3 Point Estimates vs Confidence Intervals
* **Point Estimate**: A single numerical value calculated from sample data to estimate an unknown population parameter (e.g., sample mean $\bar{X} \approx \mu$).
* **Confidence Interval (CI)**: An estimated range of values likely to contain the true population parameter at a specified confidence level ($1 - \alpha$):
  $$\text{CI} = \text{Point Estimate} \pm (\text{Critical Value} \times \text{Standard Error})$$
  * When $\sigma$ is known: $\bar{X} \pm Z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$.
  * When $\sigma$ is unknown: $\bar{X} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$.
* **Exact Interpretation**: A 95% confidence interval means that if we repeated the sampling procedure infinitely many times, $95\%$ of the independently constructed intervals would contain the true population parameter. It does NOT mean there is a 95% probability that the fixed parameter lies inside this specific calculated interval.

### 6.4 Robust Statistics & Outlier Management
* **Measures of Center**: Mean (sensitive to outliers), Median (robust), Mode (categorical).
* **Measures of Spread**: Standard Deviation (sensitive to extreme values), Interquartile Range ($\text{IQR} = Q_3 - Q_1$, robust), Median Absolute Deviation ($\text{MAD} = \text{median}(|X_i - \text{median}(X)|)$, highly robust).
* **Skewness**:
  * Positive (Right) Skew: Mean $>$ Median $>$ Mode (e.g., bank deposits, wealth).
  * Negative (Left) Skew: Mean $<$ Median $<$ Mode (e.g., age at retirement).

---

## 7. Hypothesis Testing Framework

### 7.1 The 5-Step Hypothesis Pipeline
1. State the **Null Hypothesis ($H_0$)** (assertion of no difference or no effect) and the **Alternative Hypothesis ($H_1$)**.
2. Select significance level $\alpha$ (typically $0.05$ or $0.01$).
3. Identify test statistic and verify mathematical assumptions.
4. Calculate observed test statistic and compute the **p-value**.
5. Decision Rule:
   * If $\text{p-value} \le \alpha \implies$ **Reject $H_0$** (Statistically significant finding).
   * If $\text{p-value} > \alpha \implies$ **Fail to reject $H_0$** (Insufficient evidence to overturn status quo).

### 7.2 What is a p-Value?
* **Formal Definition**: The probability of observing a test statistic at least as extreme as the one obtained from the sample data, **assuming the null hypothesis $H_0$ is true**.
* **What it is NOT**:
  * It is NOT the probability that the null hypothesis is true.
  * It is NOT the probability that the experimental result occurred by random chance.
  * A small p-value does not automatically indicate practical or commercial importance.

### 7.3 Type I vs Type II Errors, Statistical Power & Trade-Offs

| Reality \ Decision | Fail to Reject $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ is True** | **Correct Decision** (Confidence: $1 - \alpha$) | **Type I Error ($\alpha$)** (False Positive) |
| **$H_0$ is False** | **Type II Error ($\beta$)** (False Negative) | **Correct Decision** (Power: $1 - \beta$) |

* **Type I Error ($\alpha$)**: Concluding an effect exists when it does not.
* **Type II Error ($\beta$)**: Failing to detect a real effect.
* **Statistical Power ($1 - \beta$)**: The probability of correctly rejecting a false null hypothesis.
* **Factors Influencing Power**:
  1. Sample size $n$ (larger $n \implies$ higher power).
  2. Effect size $\delta$ (larger difference between groups $\implies$ higher power).
  3. Significance level $\alpha$ (higher $\alpha \implies$ higher power, but increases Type I error).
  4. Population variance $\sigma^2$ (lower noise $\implies$ higher power).

### 7.4 Test Selection Guide

```
                            WHAT IS THE BUSINESS QUESTION?
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
   COMPARING MEANS               COMPARING PROPORTIONS         CATEGORICAL INDEPENDENCE
            │                             │                             │
    ┌───────┴───────┐              ┌──────┴──────┐                      ▼
1 Group          2 Groups       1 Group       2 Groups          Chi-Square (χ²)
    │               │              │             │              Contingency Test
    ▼               ▼              ▼             ▼
One-sample      Independent      One-prop      Two-prop
t-test          or Paired?        z-test        z-test
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
    Independent               Paired
   (Equal variance:        (Before/After on
    Pooled t-test;          same subjects:
    Unequal variance:       Paired t-test)
    Welch's t-test)
```

* **Pooled Two-Sample $t$-Test**: Assumes equal population variances ($\sigma_1^2 = \sigma_2^2$).
  $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}, \quad t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$
* **Welch's $t$-Test**: **Does NOT assume equal variances**. Modern statistical standard:
  $$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}, \quad df \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}$$

### 7.5 Multiple Testing & Correction (Bonferroni & FDR)
* When testing $m$ independent hypotheses simultaneously at significance $\alpha$, the family-wise error rate (probability of at least one false positive) inflates:
  $$\alpha_{family} = 1 - (1 - \alpha)^m$$
  For $m = 20$ tests at $\alpha = 0.05$, $\alpha_{family} = 1 - (0.95)^{20} \approx 64.15\%$.
* **Bonferroni Correction**: Set individual test significance threshold to $\alpha^* = \frac{\alpha}{m}$. Conservative.
* **False Discovery Rate (Benjamini-Hochberg)**: Controls the expected proportion of false discoveries among rejected hypotheses. Better suited for high-dimensional feature exploration.

---

## 8. Applied Analytics & Experimentation (A/B Testing)

### 8.1 A/B Testing Architecture in Digital Banking
* **Randomization**: Randomly assign users to Control ($A$) and Treatment ($B$) at the same point in time to balance confounding variables.
* **Sample Size Determination**:
  $$n \approx \frac{2 \left(Z_{\alpha/2} + Z_\beta\right)^2 \sigma^2}{\Delta^2}$$
  Where $\Delta$ is the **Minimum Detectable Effect (MDE)**.
* **The Peeking Problem**: Continuously evaluating p-values every day and stopping the experiment as soon as $p < 0.05$ artificially inflates false positive rates from $5\%$ to $>30\%$. Experiments must run to their pre-computed sample size or use sequential testing procedures.

### 8.2 Simpson's Paradox
A phenomenon where an observed trend appears in several different sub-groups of data, but reverses or disappears when the groups are aggregated. Occurs due to an unmeasured **confounding variable** that is correlated with both the grouping and the outcome.

---

## 9. 30 Fully Solved Numerical & Analytical Interview Problems

### Probability & Counting Problems

#### Q01: Joint Probability with Cards
* **Question**: Three cards are dealt from a shuffled 52-card deck without replacement. What is the probability that all three cards are of the same suit?
* **Solution**:
  * Total number of 3-card combinations: $\binom{52}{3} = \frac{52 \times 51 \times 50}{3 \times 2 \times 1} = 22,100$.
  * Number of ways to choose 3 cards of a specific suit: $\binom{13}{3} = \frac{13 \times 12 \times 11}{6} = 286$.
  * There are 4 suits (Hearts, Diamonds, Clubs, Spades).
  * Favorable outcomes: $4 \times 286 = 1,144$.
  * Probability:
    $$P = \frac{1,144}{22,100} = \frac{4 \times 13 \times 12 \times 11}{52 \times 51 \times 50} = 1 \times \frac{12}{51} \times \frac{11}{50} = \frac{132}{2,550} \approx \mathbf{0.05176} \quad (5.18\%)$$

---

#### Q02: Bayes' Theorem in Transaction Monitoring
* **Question**: In an international card portfolio, $0.2\%$ of transactions are fraudulent ($P(F) = 0.002$). An automated rules engine flags $95\%$ of genuine frauds ($P(A | F) = 0.95$). For legitimate transactions, the engine falsely raises an alert $1.5\%$ of the time ($P(A | F') = 0.015$). If a transaction triggers an alert, what is the probability that it is actually fraudulent?
* **Solution**:
  * Prior: $P(F) = 0.002 \implies P(F') = 0.998$.
  * Total probability of an alert:
    $$P(A) = P(A | F)P(F) + P(A | F')P(F') = (0.95 \times 0.002) + (0.015 \times 0.998) = 0.00190 + 0.01497 = 0.01687$$
  * Posterior probability:
    $$P(F | A) = \frac{P(A | F)P(F)}{P(A)} = \frac{0.00190}{0.01687} \approx \mathbf{0.1126} \quad (11.26\%)$$
  * *Business Interpretation*: Despite $95\%$ sensitivity, only ~11.3% of flagged transactions are fraud. 88.7% are false alarms that cause customer friction if cards are automatically blocked without verification.

---

#### Q03: Conditional Probability with Dice
* **Question**: Two fair 6-sided dice are rolled simultaneously. Given that the sum of the two faces is at least 8, what is the probability that at least one die shows a 6?
* **Solution**:
  * Sample space of two dice = 36 outcomes.
  * Event $B$ (Sum $\ge 8$):
    * Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) $\implies 5$ outcomes.
    * Sum 9: (3,6), (4,5), (5,4), (6,3) $\implies 4$ outcomes.
    * Sum 10: (4,6), (5,5), (6,4) $\implies 3$ outcomes.
    * Sum 11: (5,6), (6,5) $\implies 2$ outcomes.
    * Sum 12: (6,6) $\implies 1$ outcome.
    * Total outcomes in $B$: $5 + 4 + 3 + 2 + 1 = 15$.
  * Event $A \cap B$ (Sum $\ge 8$ AND at least one 6):
    * (2,6), (6,2), (3,6), (6,3), (4,6), (6,4), (5,6), (6,5), (6,6) $\implies 9$ outcomes.
  * Conditional Probability:
    $$P(A | B) = \frac{|A \cap B|}{|B|} = \frac{9}{15} = \mathbf{0.60} \quad (60.0\%)$$

---

#### Q04: Binomial Distribution in Underwriting
* **Question**: A small-business loan cohort approves 12 loans. Historical default probability for this tier is $p = 0.08$. Assuming defaults are independent, calculate:  
(a) The probability that exactly 2 loans default.  
(b) The probability that at least 2 loans default.
* **Solution**:
  * (a) Binomial PMF:
    $$P(X = 2) = \binom{12}{2} (0.08)^2 (0.92)^{10} = \frac{12 \times 11}{2} \times 0.0064 \times 0.4344 = 66 \times 0.0064 \times 0.4344 \approx \mathbf{0.1835} \quad (18.35\%)$$
  * (b) $P(X \ge 2) = 1 - [P(X = 0) + P(X = 1)]$:
    * $P(X = 0) = (0.92)^{12} \approx 0.3677$.
    * $P(X = 1) = \binom{12}{1} (0.08)^1 (0.92)^{11} = 12 \times 0.08 \times 0.3997 \approx 0.3837$.
    * $P(X \ge 2) = 1 - (0.3677 + 0.3837) = 1 - 0.7514 = \mathbf{0.2486} \quad (24.86\%)$.

---

#### Q05: Poisson Arrival Rates
* **Question**: Customer disputes arrive at an operations desk at an average rate of $\lambda = 3$ per hour following a Poisson process.  
(a) What is the probability that exactly 5 disputes arrive in a 2-hour window?  
(b) What is the probability that zero disputes arrive in a 30-minute window?
* **Solution**:
  * (a) For a 2-hour window, rate $\lambda' = 3 \times 2 = 6$:
    $$P(X = 5) = \frac{6^5 e^{-6}}{5!} = \frac{7,776 \times 0.00247875}{120} \approx \mathbf{0.1606} \quad (16.06\%)$$
  * (b) For 30 minutes (0.5 hour), rate $\lambda'' = 3 \times 0.5 = 1.5$:
    $$P(X = 0) = \frac{1.5^0 e^{-1.5}}{0!} = e^{-1.5} \approx \mathbf{0.2231} \quad (22.31\%)$$

---

#### Q06: Geometric Distribution Waiting Time
* **Question**: A tele-advisory campaign converts retail banking prospects with probability $p = 0.05$.  
(a) What is the expected number of calls needed to make the first conversion?  
(b) What is the probability that the first conversion occurs on or after the 5th call?
* **Solution**:
  * (a) Expected value: $E[X] = \frac{1}{p} = \frac{1}{0.05} = \mathbf{20\text{ calls}}$.
  * (b) First conversion on or after 5th call means the first 4 calls failed:
    $$P(X \ge 5) = (1 - p)^4 = (0.95)^4 = \mathbf{0.8145} \quad (81.45\%)$$

---

#### Q07: Exponential Inter-Arrival Times
* **Question**: The time (in minutes) between large corporate wire transfers follows an Exponential distribution with mean $\theta = 10\text{ minutes}$ ($\lambda = 0.1\text{ min}^{-1}$). What is the probability that the next transfer arrives between 5 and 15 minutes?
* **Solution**:
  * Cumulative Distribution Function: $F(t) = 1 - e^{-\lambda t}$.
  * $P(5 \le T \le 15) = F(15) - F(5) = (1 - e^{-0.1 \times 15}) - (1 - e^{-0.1 \times 5}) = e^{-0.5} - e^{-1.5}$.
  * $e^{-0.5} \approx 0.6065$, $e^{-1.5} \approx 0.2231$.
  * $P(5 \le T \le 15) = 0.6065 - 0.2231 = \mathbf{0.3834} \quad (38.34\%)$.

---

#### Q08: Expectation of a Portfolio
* **Question**: A loan officer holds three investments with expected payoffs $E[X_1] = \$50,000$, $E[X_2] = \$30,000$, and $E[X_3] = \$20,000$. Investment 1 and 2 are positively correlated ($\text{Cov}(X_1, X_2) = 10^7$). What is the expected total portfolio payoff?
* **Solution**:
  * By linearity of expectation, covariance does NOT affect expected values:
    $$E[X_1 + X_2 + X_3] = E[X_1] + E[X_2] + E[X_3] = 50,000 + 30,000 + 20,000 = \mathbf{\$100,000}$$

---

#### Q09: Variance of Correlated Portfolio
* **Question**: For two assets $A$ and $B$, $\sigma_A = \$10, \sigma_B = \$20$, and correlation $\rho = 0.5$. Calculate the standard deviation of portfolio $P = 2A + B$.
* **Solution**:
  * $\text{Var}(A) = 100, \text{Var}(B) = 400$.
  * $\text{Cov}(A, B) = \rho \cdot \sigma_A \cdot \sigma_B = 0.5 \times 10 \times 20 = 100$.
  * $\text{Var}(2A + B) = 2^2 \text{Var}(A) + 1^2 \text{Var}(B) + 2(2)(1)\text{Cov}(A, B) = 4(100) + 400 + 4(100) = 400 + 400 + 400 = 1,200$.
  * Standard Deviation: $\sigma_P = \sqrt{1,200} \approx \mathbf{\$34.64}$.

---

#### Q10: Normal Spend Threshold
* **Question**: Monthly retail debit card spend is normally distributed with $\mu = \$1,800$ and $\sigma = \$400$.  
(a) What fraction of cardholders spend between $\$1,400$ and $\$2,600$?  
(b) What spend defines the top $2.5\%$ threshold?
* **Solution**:
  * (a) $Z_1 = \frac{1400 - 1800}{400} = -1.0$; $Z_2 = \frac{2600 - 1800}{400} = +2.0$.
    * $P(-1.0 \le Z \le 2.0) = \Phi(2.0) - \Phi(-1.0) = 0.9772 - 0.1587 = \mathbf{0.8185} \quad (81.85\%)$.
  * (b) Top $2.5\%$ corresponds to $Z = 1.96$:
    * $X = \mu + 1.96\sigma = 1800 + (1.96 \times 400) = 1800 + 784 = \mathbf{\$2,584.00}$.

---

### Sampling & Estimation Problems

#### Q11: Central Limit Theorem Standard Error
* **Question**: Customer deposit balances have unknown distribution with mean $\mu = \$8,500$ and standard deviation $\sigma = \$3,600$. For a random sample of $n = 144$ accounts, what is the probability that the sample mean $\bar{X}$ exceeds $\$9,000$?
* **Solution**:
  * Since $n = 144 \ge 30$, by CLT, $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$.
  * Standard Error: $\text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{3600}{\sqrt{144}} = \frac{3600}{12} = 300$.
  * Standardize: $Z = \frac{9000 - 8500}{300} = \frac{500}{300} \approx +1.67$.
  * $P(Z > 1.67) = 1 - 0.9525 = \mathbf{0.0475} \quad (4.75\%)$.

---

#### Q12: 95% Confidence Interval for Mean (Large Sample)
* **Question**: A credit bureau sample of $n = 100$ customers shows a mean credit score of $\bar{X} = 712$ with sample standard deviation $s = 50$. Compute and interpret the $95\%$ confidence interval for the true population mean score.
* **Solution**:
  * $\text{SE} = \frac{s}{\sqrt{n}} = \frac{50}{10} = 5.0$.
  * For $95\%$ confidence, $Z^* = 1.96$.
  * Margin of error: $\text{ME} = 1.96 \times 5 = 9.8$.
  * $\text{CI} = [712 - 9.8, 712 + 9.8] = \mathbf{[702.2, 721.8]}$.
  * *Interpretation*: With 95% confidence, the true mean credit score lies between 702.2 and 721.8.

---

#### Q13: Small Sample Confidence Interval ($t$-Distribution)
* **Question**: A test sample of $n = 16$ commercial accounts yielded a mean processing cycle of $\bar{X} = 14.2\text{ hours}$ with $s = 3.2\text{ hours}$. Assuming normal distribution of cycle times, compute the $90\%$ confidence interval.
* **Solution**:
  * $df = n - 1 = 15$. For $90\%$ CI, $\alpha = 0.10 \implies t_{0.05, 15} = 1.753$.
  * $\text{SE} = \frac{s}{\sqrt{n}} = \frac{3.2}{\sqrt{16}} = \frac{3.2}{4} = 0.8$.
  * $\text{ME} = 1.753 \times 0.8 = 1.402$.
  * $\text{CI} = [14.2 - 1.402, 14.2 + 1.402] = \mathbf{[12.798\text{ hours}, 15.602\text{ hours}]}$.

---

#### Q14: Sample Size Required for Margin of Error
* **Question**: Management wants to estimate mean monthly corporate card expenditure within a margin of error of $\text{ME} = \$50$ at a $95\%$ confidence level. Preliminary studies indicate $\sigma \approx \$400$. What is the minimum sample size needed?
* **Solution**:
  * Formula: $n = \left(\frac{Z^* \sigma}{\text{ME}}\right)^2$.
  * $n = \left(\frac{1.96 \times 400}{50}\right)^2 = \left(\frac{784}{50}\right)^2 = (15.68)^2 \approx 245.86$.
  * Always round up to ensure the margin of error constraint is satisfied: $\mathbf{n = 246\text{ accounts}}$.

---

#### Q15: Confidence Interval for a Proportion
* **Question**: In an audit of $n = 400$ transaction entries, 28 were found to have formatting errors ($\hat{p} = \frac{28}{400} = 0.07$). Construct a $95\%$ confidence interval for the true population error rate.
* **Solution**:
  * Check assumptions: $n\hat{p} = 28 \ge 10$, $n(1 - \hat{p}) = 372 \ge 10$.
  * Standard Error: $\text{SE} = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}} = \sqrt{\frac{0.07 \times 0.93}{400}} = \sqrt{\frac{0.0651}{400}} \approx 0.01276$.
  * $\text{ME} = 1.96 \times 0.01276 \approx 0.0250$.
  * $\text{CI} = [0.07 - 0.025, 0.07 + 0.025] = \mathbf{[0.045, 0.095]} \implies \mathbf{[4.5\%, 9.5\%]}$.

---

### Hypothesis Testing Problems

#### Q16: One-Sample $Z$-Test on Processing Time
* **Question**: A legacy settlement process takes a known mean time of $\mu_0 = 45\text{ minutes}$ with $\sigma = 8\text{ minutes}$. A modernized pipeline is piloted across $n = 64$ settlements, resulting in $\bar{X} = 42.5\text{ minutes}$. At $\alpha = 0.01$, test whether the new pipeline significantly reduces settlement time.
* **Solution**:
  * Hypotheses: $H_0: \mu = 45$ vs $H_1: \mu < 45$ (Left-tailed test).
  * Test Statistic:
    $$Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} = \frac{42.5 - 45}{8 / \sqrt{64}} = \frac{-2.5}{1.0} = -2.50$$
  * Critical Value for left-tail test at $\alpha = 0.01$: $Z_{crit} = -2.326$.
  * p-value: $P(Z \le -2.50) = 0.0062$.
  * Decision: Since $Z_{calc} = -2.50 < -2.326$ (and $p = 0.0062 < 0.01$), **Reject $H_0$**. The new pipeline significantly decreases processing time.

---

#### Q17: One-Sample $t$-Test on Account Balance
* **Question**: Historical average balance in a student banking segment is $\mu_0 = \$500$. A sample of $n = 25$ accounts from a new digital acquisition channel shows $\bar{X} = \$540$ with $s = \$90$. Test at $\alpha = 0.05$ whether the new channel attracts accounts with significantly different balances.
* **Solution**:
  * Hypotheses: $H_0: \mu = 500$ vs $H_1: \mu \neq 500$ (Two-tailed test).
  * Degrees of freedom: $df = 25 - 1 = 24$.
  * Test Statistic:
    $$t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}} = \frac{540 - 500}{90 / \sqrt{25}} = \frac{40}{18} \approx 2.222$$
  * Critical value for two-tailed test at $\alpha = 0.05, df = 24$: $t_{crit} = \pm 2.064$.
  * Decision: Since $|t_{calc}| = 2.222 > 2.064$, **Reject $H_0$**. Balances from this channel are statistically significantly different.

---

#### Q18: Two-Sample Pooled $t$-Test
* **Question**: Two customer service teams are evaluated on call resolution time (assumed normal with equal variances):
  * Team A: $n_1 = 16, \bar{X}_1 = 8.5\text{ mins}, s_1 = 1.8\text{ mins}$.
  * Team B: $n_2 = 16, \bar{X}_2 = 7.1\text{ mins}, s_2 = 1.6\text{ mins}$.
  Test at $\alpha = 0.05$ if Team B resolves calls significantly faster.
* **Solution**:
  * Hypotheses: $H_0: \mu_A - \mu_B = 0$ vs $H_1: \mu_A - \mu_B > 0$ (Right-tailed test).
  * Pooled variance:
    $$s_p^2 = \frac{(16 - 1)(1.8)^2 + (16 - 1)(1.6)^2}{16 + 16 - 2} = \frac{15(3.24) + 15(2.56)}{30} = \frac{48.6 + 38.4}{30} = \frac{87}{30} = 2.90$$
  * Standard Error: $\text{SE} = \sqrt{2.90 \left(\frac{1}{16} + \frac{1}{16}\right)} = \sqrt{2.90 \times 0.125} = \sqrt{0.3625} \approx 0.602$.
  * Test Statistic: $t = \frac{8.5 - 7.1}{0.602} = \frac{1.4}{0.602} \approx 2.325$.
  * For $df = 30$ at right-tailed $\alpha = 0.05$, $t_{crit} = 1.697$.
  * Decision: $t_{calc} = 2.325 > 1.697 \implies$ **Reject $H_0$**. Team B is significantly faster.

---

#### Q19: Welch's $t$-Test (Unequal Variances)
* **Question**: Two independent digital marketing campaigns yield weekly customer acquisitions:
  * Campaign 1: $n_1 = 10, \bar{X}_1 = 150, s_1 = 12$.
  * Campaign 2: $n_2 = 15, \bar{X}_2 = 138, s_2 = 28$.
  Why is a pooled $t$-test inappropriate here, and what is the Welch's test statistic?
* **Solution**:
  * Inappropriateness: Sample variances differ substantially ($s_1^2 = 144$ vs $s_2^2 = 784$, ratio $> 5.4$). The homoscedasticity assumption is violated.
  * Welch's Standard Error:
    $$\text{SE}_{welch} = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} = \sqrt{\frac{144}{10} + \frac{784}{15}} = \sqrt{14.4 + 52.27} = \sqrt{66.67} \approx 8.165$$
  * Test Statistic:
    $$t = \frac{150 - 138}{8.165} = \frac{12}{8.165} \approx \mathbf{1.47}$$
  * Welch-Satterthwaite degrees of freedom:
    $$df = \frac{(14.4 + 52.27)^2}{\frac{14.4^2}{9} + \frac{52.27^2}{14}} = \frac{4444.89}{23.04 + 195.15} = \frac{4444.89}{218.19} \approx 20.37 \implies df \approx 20$$

---

#### Q20: Paired $t$-Test (Before vs After Training)
* **Question**: 10 financial analysts undergo an intensive financial modeling training program. Their errors on a standard reconciliation audit are measured Before ($X_1$) and After ($X_2$). The differences $d_i = X_{1i} - X_{2i}$ have sample mean $\bar{d} = 3.4$ and sample standard deviation $s_d = 2.1$. Test at $\alpha = 0.05$ whether the training significantly reduced errors.
* **Solution**:
  * Hypotheses: $H_0: \mu_d = 0$ vs $H_1: \mu_d > 0$ (Right-tailed test).
  * $n = 10 \implies df = 9$.
  * Standard Error: $\text{SE} = \frac{s_d}{\sqrt{n}} = \frac{2.1}{\sqrt{10}} \approx 0.664$.
  * Test Statistic: $t = \frac{\bar{d}}{\text{SE}} = \frac{3.4}{0.664} \approx 5.12$.
  * Critical Value for $df = 9$ at one-tailed $\alpha = 0.05$ is $t_{crit} = 1.833$.
  * Decision: $5.12 \gg 1.833 \implies$ **Reject $H_0$**. Training produced a statistically significant reduction in errors.

---

#### Q21: Two-Proportion $Z$-Test (A/B Test Conversion)
* **Question**: An online card application redesign is tested:
  * Control ($A$): $n_1 = 1,000$ visits, $x_1 = 50$ completions ($\hat{p}_1 = 0.050$).
  * Variant ($B$): $n_2 = 1,000$ visits, $x_2 = 75$ completions ($\hat{p}_2 = 0.075$).
  Test at $\alpha = 0.05$ whether Variant B has a significantly higher conversion rate.
* **Solution**:
  * Hypotheses: $H_0: p_2 - p_1 = 0$ vs $H_1: p_2 - p_1 > 0$.
  * Pooled proportion:
    $$\hat{p} = \frac{x_1 + x_2}{n_1 + n_2} = \frac{50 + 75}{2000} = \frac{125}{2000} = 0.0625$$
  * Standard Error:
    $$\text{SE} = \sqrt{\hat{p}(1 - \hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)} = \sqrt{0.0625 \times 0.9375 \times \left(\frac{2}{1000}\right)} = \sqrt{0.05859375 \times 0.002} = \sqrt{0.0001171875} \approx 0.010825$$
  * Test Statistic:
    $$Z = \frac{\hat{p}_2 - \hat{p}_1}{\text{SE}} = \frac{0.075 - 0.050}{0.010825} = \frac{0.025}{0.010825} \approx \mathbf{2.31}$$
  * Critical Value for one-tailed $\alpha = 0.05$ is $Z_{crit} = 1.645$.
  * Decision: $Z_{calc} = 2.31 > 1.645$ ($p = 0.0104 < 0.05$) $\implies$ **Reject $H_0$**. Variant B significantly increases application completion.

---

#### Q22: Chi-Square Goodness-of-Fit Test
* **Question**: Customer complaint arrivals are hypothesized to be uniformly distributed across the 5 weekdays (Monday through Friday). Over a month, 200 complaints are recorded: Mon: 55, Tue: 42, Wed: 35, Thu: 38, Fri: 30. Test at $\alpha = 0.05$ if arrivals deviate from a uniform distribution.
* **Solution**:
  * Expected count per day: $E_i = \frac{200}{5} = 40$ for all 5 days.
  * Chi-Square Statistic:
    $$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} = \frac{(55-40)^2}{40} + \frac{(42-40)^2}{40} + \frac{(35-40)^2}{40} + \frac{(38-40)^2}{40} + \frac{(30-40)^2}{40}$$
    $$\chi^2 = \frac{225 + 4 + 25 + 4 + 100}{40} = \frac{358}{40} = \mathbf{8.95}$$
  * Degrees of Freedom: $df = k - 1 = 5 - 1 = 4$.
  * Critical Value: $\chi^2_{0.05, 4} = 9.488$.
  * Decision: Since $\chi^2_{calc} = 8.95 < 9.488$, we **Fail to Reject $H_0$**. There is insufficient evidence to conclude complaints are non-uniformly distributed across weekdays.

---

#### Q23: Chi-Square Contingency Test of Independence
* **Question**: 300 customers are categorized by Segment (Retail, Wealth) and whether they enrolled in Auto-Pay (Enrolled, Not Enrolled):
  * Retail: 80 Enrolled, 120 Not Enrolled (Total = 200).
  * Wealth: 60 Enrolled, 40 Not Enrolled (Total = 100).
  Test at $\alpha = 0.05$ whether Auto-Pay enrollment is independent of customer segment.
* **Solution**:
  * Marginal Totals: Enrolled = 140, Not Enrolled = 160. Grand Total = 300.
  * Expected counts: $E = \frac{\text{Row Total} \times \text{Col Total}}{\text{Grand Total}}$
    * $E_{Retail, Enrolled} = \frac{200 \times 140}{300} = 93.33$.
    * $E_{Retail, Not} = \frac{200 \times 160}{300} = 106.67$.
    * $E_{Wealth, Enrolled} = \frac{100 \times 140}{300} = 46.67$.
    * $E_{Wealth, Not} = \frac{100 \times 160}{300} = 53.33$.
  * Chi-Square:
    $$\chi^2 = \frac{(80 - 93.33)^2}{93.33} + \frac{(120 - 106.67)^2}{106.67} + \frac{(60 - 46.67)^2}{46.67} + \frac{(40 - 53.33)^2}{53.33}$$
    $$\chi^2 = \frac{177.69}{93.33} + \frac{177.69}{106.67} + \frac{177.69}{46.67} + \frac{177.69}{53.33} = 1.904 + 1.666 + 3.807 + 3.332 = \mathbf{10.71}$$
  * $df = (2 - 1)(2 - 1) = 1$. Critical value $\chi^2_{0.05, 1} = 3.841$.
  * Decision: $10.71 > 3.841 \implies$ **Reject $H_0$**. Auto-pay enrollment is strongly dependent on customer segment.

---

#### Q24: One-Way ANOVA $F$-Test
* **Question**: Three marketing communication channels are compared for deposit generation across $k = 3$ groups with $n = 5$ customers each.
  * Group Means: $\bar{X}_1 = 20, \bar{X}_2 = 25, \bar{X}_3 = 30$. Grand Mean $\bar{X} = 25$.
  * Between-group sum of squares $\text{SSB} = 250$.
  * Within-group sum of squares $\text{SSW} = 120$.
  Calculate the $F$-statistic and make a decision at $\alpha = 0.05$.
* **Solution**:
  * Degrees of Freedom:
    * $df_{between} = k - 1 = 3 - 1 = 2$.
    * $df_{within} = N - k = 15 - 3 = 12$.
  * Mean Squares:
    * $\text{MSB} = \frac{\text{SSB}}{df_{between}} = \frac{250}{2} = 125$.
    * $\text{MSW} = \frac{\text{SSW}}{df_{within}} = \frac{120}{12} = 10$.
  * $F$-statistic:
    $$F = \frac{\text{MSB}}{\text{MSW}} = \frac{125}{10} = \mathbf{12.50}$$
  * Critical Value: $F_{0.05, 2, 12} = 3.89$.
  * Decision: Since $F_{calc} = 12.50 > 3.89$, **Reject $H_0$**. At least one marketing channel produces significantly different deposit volumes.

---

### Applied Analytics & Advanced Scenarios

#### Q25: Correlation Significance Test
* **Question**: A sample of $n = 28$ high-net-worth accounts shows a sample Pearson correlation of $r = 0.40$ between investment balance and credit card spend. Test at $\alpha = 0.05$ whether the true population correlation $\rho$ is significantly different from zero.
* **Solution**:
  * Hypotheses: $H_0: \rho = 0$ vs $H_1: \rho \neq 0$.
  * Test Statistic:
    $$t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}} = \frac{0.40 \sqrt{26}}{\sqrt{1 - 0.16}} = \frac{0.40 \times 5.099}{\sqrt{0.84}} = \frac{2.0396}{0.9165} \approx \mathbf{2.225}$$
  * Degrees of freedom: $df = 28 - 2 = 26$.
  * Two-tailed critical value at $\alpha = 0.05, df = 26$: $t_{crit} = 2.056$.
  * Decision: Since $|t_{calc}| = 2.225 > 2.056$, **Reject $H_0$**. There is a statistically significant linear correlation.

---

#### Q26: Bonferroni Multiplicity Correction
* **Question**: An analytics team tests whether 10 different customer demographic features have significant differences across churners and non-churners. If each test is run at $\alpha = 0.05$, what is the family-wise error rate assuming independence, and what should the Bonferroni-corrected threshold be?
* **Solution**:
  * Uncorrected Family-Wise Error Rate:
    $$\text{FWER} = 1 - (1 - 0.05)^{10} = 1 - (0.95)^{10} = 1 - 0.5987 = \mathbf{0.4013} \quad (40.13\%)$$
  * Bonferroni Corrected Threshold:
    $$\alpha^* = \frac{\alpha}{m} = \frac{0.05}{10} = \mathbf{0.005}$$
  * An individual feature must achieve a p-value $< 0.005$ to be deemed significant at the family-wise 5% level.

---

#### Q27: Effect Size (Cohen's $d$)
* **Question**: A new digital onboarding flow reduces account setup time from $\mu_1 = 24\text{ mins}$ to $\mu_2 = 21\text{ mins}$. The pooled standard deviation is $s_p = 6\text{ mins}$. Calculate Cohen's $d$ and evaluate practical significance.
* **Solution**:
  * Cohen's $d$:
    $$d = \frac{\bar{X}_1 - \bar{X}_2}{s_p} = \frac{24 - 21}{6} = \frac{3}{6} = \mathbf{0.50}$$
  * Interpretation: An effect size of $d = 0.50$ represents a **medium effect size** (benchmark: $0.2 = \text{small}, 0.5 = \text{medium}, 0.8 = \text{large}$). This indicates not only statistical significance (given sufficient $n$) but meaningful commercial efficiency improvement.

---

#### Q28: Maximum Likelihood Estimation of Poisson Arrival Rate
* **Question**: Given a sample of customer service contact counts across $n$ independent days: $x_1, x_2, \dots, x_n$. Derive the Maximum Likelihood Estimator (MLE) for the arrival parameter $\lambda$.
* **Solution**:
  * Likelihood:
    $$L(\lambda) = \prod_{i=1}^n \frac{\lambda^{x_i} e^{-\lambda}}{x_i!} = \frac{\lambda^{\sum x_i} e^{-n\lambda}}{\prod x_i!}$$
  * Log-Likelihood:
    $$\ln L(\lambda) = \left(\sum_{i=1}^n x_i\right) \ln(\lambda) - n\lambda - \sum_{i=1}^n \ln(x_i!)$$
  * First Derivative with respect to $\lambda$:
    $$\frac{d}{d\lambda} \ln L(\lambda) = \frac{\sum x_i}{\lambda} - n = 0 \implies \hat{\lambda} = \frac{\sum_{i=1}^n x_i}{n} = \mathbf{\bar{x}}$$
  * Second Derivative: $\frac{d^2}{d\lambda^2} \ln L(\lambda) = -\frac{\sum x_i}{\lambda^2} < 0$ (confirms maximum).
  * The MLE of a Poisson rate parameter is the sample mean.

---

#### Q29: Missing Data Mechanism Evaluation
* **Question**: In a wealth management dataset, 35% of clients have a missing value for `annual_income`. When cross-tabulated, clients with missing income have an average portfolio balance 4x higher than those reporting income. What missingness mechanism is operating, and why would mean imputation be disastrous?
* **Solution**:
  * Mechanism: **Missing Not at Random (MNAR)** (or Missing at Random conditioned on wealth tier). The probability of missingness depends directly on the unobserved income value itself (high-net-worth clients deliberately omit disclosing income for privacy reasons).
  * Disaster of Mean Imputation: Imputing the overall sample mean ($\sim \$60,000$) to ultra-high-net-worth accounts severely biases downstream wealth propensity models, artificially compresses income variance, and leads to incorrect product targeting. The correct approach is either to create a binary indicator `income_missing_flag` or use advanced model-based multiple imputation conditioned on liquid asset tiers.

---

#### Q30: Insufficient Data / Ambiguous Conclusion Case
* **Question**: A regional branch manager notices that weekly loan approval rates increased from $62\%$ to $68\%$ after introducing a new scoring rule, based on a sample of $n = 20$ applicants. The manager concludes the rule was an unequivocal success. Evaluate this claim statistically.
* **Solution**:
  * Evaluation: **The available data is statistically insufficient to substantiate the claim.**
  * Mathematical Check:
    * Baseline: $p_1 = 0.62$. Sample size $n = 20$.
    * With $n = 20$, each applicant represents $1/20 = 5\%$ of the total rate. The difference between 12 approvals ($60\%$) and 14 approvals ($70\%$) is a mere 2 people.
    * Standard error of a proportion on $n = 20$:
      $$\text{SE} \approx \sqrt{\frac{0.65 \times 0.35}{20}} = \sqrt{\frac{0.2275}{20}} \approx \mathbf{0.1067} \quad (10.67\%)$$
    * A 6 percentage-point difference ($68\% - 62\%$) is well within one standard error ($\pm 10.7\%$), meaning the observed fluctuation is entirely consistent with ordinary random sampling noise ($p > 0.50$).
  * Correct Analytical Response: Advise the branch manager to withhold policy rollout until a minimum pre-determined sample size ($n \ge 350$ applicants) is reached to achieve adequate statistical power.

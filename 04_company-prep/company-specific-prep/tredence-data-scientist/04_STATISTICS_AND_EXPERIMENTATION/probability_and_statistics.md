# Probability and Mathematical Statistics for Enterprise Analytics

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Multivariable Calculus, Linear Algebra, Foundational Probability

---

## 1. Probability Foundations

### 1.1 Sample Spaces, Axioms, and Conditional Probability
For a sample space $\Omega$ and event space $\mathcal{F}$:
1. **Non-negativity:** $P(A) \ge 0 \quad \forall A \in \mathcal{F}$
2. **Unitarity:** $P(\Omega) = 1$
3. **$\sigma$-Additivity:** For mutually disjoint events $A_1, A_2, \dots$:
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i)$$

**Conditional Probability and Independence:**
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$
Two events $A$ and $B$ are statistically independent iff $P(A \cap B) = P(A)P(B)$, which implies $P(A \mid B) = P(A)$.

### 1.2 Law of Total Probability and Bayes' Theorem
Given a partition of the sample space $B_1, B_2, \dots, B_k$ where $\bigcup_{i=1}^k B_i = \Omega$ and $B_i \cap B_j = \emptyset$ for $i \ne j$:
$$P(A) = \sum_{i=1}^k P(A \mid B_i) P(B_i)$$

**Bayes' Theorem:**
$$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^k P(A \mid B_i) P(B_i)}$$

*Retail Analytics Application:*
Evaluating fraud or promotional churn. Let $F$ be fraudulent transaction, $A$ be flagged by risk rule. If base rate $P(F) = 0.005$, true positive rate (sensitivity) $P(A \mid F) = 0.95$, and false positive rate $P(A \mid F^c) = 0.02$:
$$P(F \mid A) = \frac{0.95 \times 0.005}{0.95 \times 0.005 + 0.02 \times 0.995} = \frac{0.00475}{0.00475 + 0.0199} \approx 0.1927 \ (19.3\%)$$
*Business Interpretation:* Despite a 95% sensitivity rule, roughly 81% of flagged alerts are false positives due to class imbalance.

---

## 2. Discrete Probability Distributions

| Distribution | PMF / PDF $P(X=k)$ | Mean $\mathbb{E}[X]$ | Variance $\text{Var}(X)$ | Enterprise / Retail Use Case |
|---|---|---|---|---|
| **Bernoulli** | $p^k(1-p)^{1-k}, \ k \in \{0, 1\}$ | $p$ | $p(1-p)$ | Single customer checkout conversion / promo click |
| **Binomial** | $\binom{n}{k} p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | Number of active purchasers out of $n$ targeted campaign leads |
| **Poisson** | $\frac{\lambda^k e^{-\lambda}}{k!}, \ k \ge 0$ | $\lambda$ | $\lambda$ | Footfall arrival per minute at retail POS; store stockout events |
| **Geometric** | $(1-p)^{k-1}p, \ k \ge 1$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | Number of visits until first brand purchase |
| **Negative Binomial** | $\binom{k+r-1}{k} p^r (1-p)^k$ | $\frac{r(1-p)}{p}$ | $\frac{r(1-p)}{p^2}$ | Overdispersed customer purchase frequencies (NBD model) |

### 2.1 The Poisson-Exponential Connection
If customer arrivals follow a Poisson process with constant rate $\lambda$ arrivals per hour:
- The count of arrivals in time $t$ is $N_t \sim \text{Poisson}(\lambda t)$.
- The inter-arrival time between successive customers $T$ follows an Exponential distribution:
  $$f_T(t) = \lambda e^{-\lambda t}, \quad t \ge 0, \quad \mathbb{E}[T] = \frac{1}{\lambda}, \quad \text{Var}(T) = \frac{1}{\lambda^2}$$
- **Memoryless Property:** $P(T > s + t \mid T > s) = P(T > t)$.

---

## 3. Continuous Probability Distributions

### 3.1 Normal (Gaussian) Distribution
$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$
- Standard Normal: $Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1)$.
- Empirical Rule: $68.27\%$ within $\pm 1\sigma$, $95.45\%$ within $\pm 2\sigma$, $99.73\%$ within $\pm 3\sigma$.
- Skewness $= 0$, Kurtosis $= 3$ (Excess Kurtosis $= 0$).

### 3.2 Lognormal Distribution
If $Y = \ln(X) \sim \mathcal{N}(\mu, \sigma^2)$, then $X$ is lognormally distributed:
$$f(x) = \frac{1}{x \sigma \sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu)^2}{2\sigma^2}\right), \quad x > 0$$
$$\mathbb{E}[X] = \exp\left(\mu + \frac{\sigma^2}{2}\right), \quad \text{Var}(X) = \left[\exp(\sigma^2) - 1\right] \exp(2\mu + \sigma^2)$$
*Application:* Customer Lifetime Value (CLV), order spend, and e-commerce cart totals are right-skewed and strictly positive, making Lognormal a standard generative baseline.

### 3.3 Gamma and Beta Distributions
- **Gamma Distribution ($\alpha, \beta$):** Models waiting times for multiple events or positive skew metrics like customer total spend. Conjugate prior to Poisson likelihood.
- **Beta Distribution ($\alpha, \beta$):** Defined on $[0, 1]$. Conjugate prior to Binomial likelihood. Widely used for Bayesian conversion rate estimation and multi-armed bandit Thompson sampling:
  $$\text{Beta}(\alpha_{\text{prior}} + \text{clicks}, \beta_{\text{prior}} + \text{impressions} - \text{clicks})$$

### 3.4 Extreme Value Distributions (Gumbel, Fréchet, Weibull)
Governed by the Fisher-Tippett-Gnedenko Theorem. The asymptotic distribution of the normalized sample maximum $M_n = \max(X_1, \dots, X_n)$ belongs to the Generalized Extreme Value (GEV) family:
$$G(z) = \exp\left(-\left[1 + \xi \left(\frac{z - \mu}{\sigma}\right)\right]^{-1/\xi}\right)$$
- $\xi = 0$: Gumbel (light tail, e.g., exponential, normal tails).
- $\xi > 0$: Fréchet (heavy tail, e.g., Pareto, power law).
- $\xi < 0$: Weibull (bounded upper limit).
*Analytical Connection:* Candidate's hydrological modeling background utilizes GEV/Gumbel for extreme flood return periods; directly transferable to supply chain extreme demand spikes and financial tail-risk modeling.

---

## 4. Limit Theorems and Asymptotics

### 4.1 Law of Large Numbers (LLN)
- **Weak Law (WLLN):** Sample mean $\bar{X}_n \xrightarrow{P} \mu$ as $n \to \infty$:
  $$\lim_{n \to \infty} P(|\bar{X}_n - \mu| \ge \epsilon) = 0 \quad \forall \epsilon > 0$$
- **Strong Law (SLLN):** $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$ as $n \to \infty$.

### 4.2 Central Limit Theorem (CLT)
Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with finite mean $\mu$ and finite variance $\sigma^2 > 0$. Then:
$$Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad \text{as } n \to \infty$$
*Crucial Interview Nuance:* The CLT guarantees that the *sample mean* $\bar{X}_n$ converges in distribution to normal, NOT that the underlying population distribution becomes normal.

---

## 5. Statistical Estimation Theory

### 5.1 Estimator Properties
Let $\hat{\theta}$ be an estimator of true parameter $\theta$:
1. **Bias:** $\text{Bias}(\hat{\theta}) = \mathbb{E}[\hat{\theta}] - \theta$. Unbiased if $\text{Bias}(\hat{\theta}) = 0$.
2. **Variance:** $\text{Var}(\hat{\theta}) = \mathbb{E}[(\hat{\theta} - \mathbb{E}[\hat{\theta}])^2]$.
3. **Mean Squared Error (MSE):**
   $$\text{MSE}(\hat{\theta}) = \mathbb{E}[(\hat{\theta} - \theta)^2] = \text{Var}(\hat{\theta}) + \left[\text{Bias}(\hat{\theta})\right]^2$$
4. **Consistency:** $\hat{\theta}_n \xrightarrow{P} \theta$ as $n \to \infty$.
5. **Efficiency:** An unbiased estimator $\hat{\theta}^*$ is efficient if its variance achieves the Cramér-Rao Lower Bound (CRLB):
   $$\text{Var}(\hat{\theta}) \ge \frac{1}{I(\theta)}, \quad \text{where } I(\theta) = \mathbb{E}\left[\left(\frac{\partial \ln f(X; \theta)}{\partial \theta}\right)^2\right] = -\mathbb{E}\left[\frac{\partial^2 \ln f(X; \theta)}{\partial \theta^2}\right]$$

### 5.2 Maximum Likelihood Estimation (MLE)
Given sample $\mathbf{x} = (x_1, \dots, x_n)$ i.i.d. from density $f(x; \theta)$:
$$L(\theta; \mathbf{x}) = \prod_{i=1}^n f(x_i; \theta) \implies \ell(\theta) = \sum_{i=1}^n \ln f(x_i; \theta)$$
$$\hat{\theta}_{\text{MLE}} = \arg\max_\theta \ell(\theta) \implies \left.\frac{\partial \ell(\theta)}{\partial \theta}\right|_{\hat{\theta}} = 0, \quad \left.\frac{\partial^2 \ell(\theta)}{\partial \theta^2}\right|_{\hat{\theta}} < 0$$
- **Asymptotic Properties of MLE:**
  1. Consistency: $\hat{\theta}_{\text{MLE}} \xrightarrow{P} \theta_0$.
  2. Asymptotic Normality: $\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta_0) \xrightarrow{d} \mathcal{N}(0, I_1^{-1}(\theta_0))$.
  3. Asymptotic Efficiency: Achieves the Cramér-Rao bound asymptotically.
  4. Invariance: If $\hat{\theta}$ is the MLE of $\theta$, then $g(\hat{\theta})$ is the MLE of $g(\theta)$.

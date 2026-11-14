# Enterprise A/B Testing & Causal Experimentation

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Hypothesis Testing, Sample Size Estimation, Linear Regression

---

## 1. Experimentation Architecture & Metric Hierarchy

Enterprise experimentation connects algorithmic or interface changes to business P&L impact.

### 1.1 Metric Taxonomy
1. **North Star Metric:** Long-term enterprise health (e.g., Annual Recurring Revenue, 90-Day Active Retention).
2. **Primary Evaluation Metric (OEC - Overall Evaluation Criterion):** Sensitive, immediate metric targeted by the intervention (e.g., Checkout Conversion Rate, Add-to-Cart Rate).
3. **Guardrail Metrics:** Safety constraints that must not degrade (e.g., Latency, App Crash Rate, Unsubscribe Rate, Return Rate).
4. **Diagnostic Metrics:** Intermediate funnel metrics explaining *why* the primary metric changed (e.g., Search Click-Through Rate, Filter Usage).

---

## 2. Integrity Checks & Validity Diagnostics

### 2.1 Sample Ratio Mismatch (SRM)
If traffic allocation is configured as 50:50, but observed traffic is 51,200 (Control) vs 48,800 (Treatment) out of $N = 100,000$:

$$\chi^2 = \frac{(O_C - E_C)^2}{E_C} + \frac{(O_T - E_T)^2}{E_T} = \frac{(51200 - 50000)^2}{50000} + \frac{(48800 - 50000)^2}{50000} = \frac{1200^2 + (-1200)^2}{50000} = 57.6$$
$$\chi^2 = 57.6 \implies p\text{-value} \ll 10^{-10}$$

**Mandatory Rule:** **ABORT EXPERIMENT.** An SRM indicates broken randomization, bot filtering disparities, redirect latency divergence, or tracking drops. Results cannot be interpreted.

### 2.2 A/A Testing
Run an identical experience on both Control and Variant groups before the experiment:
- The $p$-value distribution across 1000 simulated A/A splits must be **Uniform $[0, 1]$**.
- Exactly $5\%$ of A/A tests should reject $H_0$ at $\alpha = 0.05$. If $> 5\%$, test infrastructure suffers systematic false positive inflation.

---

## 3. The Peeking Problem & Sequential Testing

Continuously checking $p$-values every day and stopping when $p < 0.05$ severely inflates Type I error:
- If checked 5 times over an experiment, true $\alpha \approx 0.14$ (14%).
- If checked continuously, true $\alpha \to 0.30 - 0.40$.

### Solutions:
1. **Fixed Horizon:** Commit to pre-calculated sample size $N$; evaluate strictly at completion.
2. **Sequential Testing (mSPRT - Mixture Sequential Probability Ratio Test):** Provides valid $p$-values and confidence intervals at any point in time, enabling early stopping for overwhelming success or disastrous harm.

---

## 4. CUPED (Controlled-Experiment Using Pre-Experiment Data)

Developed by Microsoft Research (Deng et al.), CUPED is the enterprise standard for variance reduction.

### 4.1 Mathematical Derivation
Let $Y$ be the experiment outcome metric (e.g., revenue during 14-day test).  
Let $X$ be the pre-experiment metric (e.g., revenue of the same user during 14 days *before* the test), with $\mathbb{E}[X]$ known.

Define the adjusted CUPED metric:
$$\hat{Y}_{\text{CUPED}} = Y - \theta (X - \mathbb{E}[X])$$

Since $\mathbb{E}[X - \mathbb{E}[X]] = 0$, the estimator is unbiased:
$$\mathbb{E}[\hat{Y}_{\text{CUPED}}] = \mathbb{E}[Y]$$

The variance of $\hat{Y}_{\text{CUPED}}$ is:
$$\text{Var}(\hat{Y}_{\text{CUPED}}) = \text{Var}(Y) + \theta^2 \text{Var}(X) - 2\theta \text{Cov}(Y, X)$$

To minimize variance, differentiate with respect to $\theta$ and set to zero:
$$\frac{\partial \text{Var}(\hat{Y}_{\text{CUPED}})}{\partial \theta} = 2\theta \text{Var}(X) - 2\text{Cov}(Y, X) = 0 \implies \theta^* = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$$

Substituting $\theta^*$ back into the variance formula:
$$\text{Var}(\hat{Y}_{\text{CUPED}}) = \text{Var}(Y) - \frac{[\text{Cov}(Y, X)]^2}{\text{Var}(X)} = \text{Var}(Y) \left(1 - \frac{[\text{Cov}(Y, X)]^2}{\text{Var}(Y)\text{Var}(X)}\right) = \text{Var}(Y) (1 - \rho^2)$$

Where $\rho$ is the Pearson correlation between pre-experiment metric $X$ and post-experiment metric $Y$.

### 4.2 Business Impact
If pre-experiment spend correlates with experiment spend at $\rho = 0.70$:
$$\text{Var}(\hat{Y}_{\text{CUPED}}) = \text{Var}(Y) \times (1 - 0.70^2) = \text{Var}(Y) \times (1 - 0.49) = 0.51 \times \text{Var}(Y)$$
- **Variance is reduced by 49%.**
- Since required sample size $n \propto \sigma^2$, **required sample size is cut in half**, allowing tests to conclude in 7 days instead of 14 days without sacrificing statistical power.

---

## 5. Network Interference & SUTVA Violations

**SUTVA (Stable Unit Treatment Value Assumption):** An observation's outcome is unaffected by the treatment assignment of any other observation.

### 5.1 When SUTVA Breaks
1. **Two-Sided Marketplaces (Uber, Airbnb, DoorDash):** If treatment gives discounts to drivers, control drivers suffer lower ride allocation.
2. **Social Networks & Enterprise Collaboration:** Messaging feature tested on user $A$ spills over to friend $B$.
3. **Retail Inventory Contamination:** High discount on treatment variant exhausts regional warehouse inventory, causing stockouts for control customers.

### 5.2 Methodological Remedies
- **Cluster Randomization:** Randomize by isolated geographical markets (DMA - Designated Market Area), distinct cities, or retail distribution centers.
- **Switchback Experiments:** Alternate entire system between Treatment and Control in discrete time blocks (e.g., 2-hour alternating windows), controlling for time-of-day fixed effects.
- **Synthetic Control Methods:** When testing at state or chain level where $N=1$ treated unit exists.

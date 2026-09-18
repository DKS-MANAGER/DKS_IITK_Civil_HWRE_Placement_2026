# Statistics & Probability Practice

> Core statistics and probability concepts with formulas, examples, and interview questions for data analyst roles.

---

## 1. Descriptive Statistics

### Measures of Central Tendency

| Measure | Formula | When to Use |
|:--------|:--------|:------------|
| **Mean** | Σx / n | Symmetric data, no outliers |
| **Median** | Middle value | Skewed data, outliers present |
| **Mode** | Most frequent | Categorical data |

**Interview question:** "When would you use median instead of mean?"
**Answer:** "When data has outliers or is skewed. For example, income data — a few billionaires would skew the mean, but the median better represents the typical income."

### Measures of Spread

| Measure | Formula | Intuition |
|:--------|:--------|:----------|
| **Range** | Max - Min | Simple spread |
| **Variance** | Σ(x-μ)² / n | Average squared deviation |
| **Std Dev** | √Variance | Typical deviation from mean |
| **IQR** | Q3 - Q1 | Middle 50% spread |

### Example: Calculate Variance & Std Dev
Data: 2, 4, 4, 4, 5, 5, 7, 9
- Mean = 40/8 = 5
- Variance = [(2-5)² + (4-5)² + (4-5)² + (4-5)² + (5-5)² + (5-5)² + (7-5)² + (9-5)²] / 8
- = [9 + 1 + 1 + 1 + 0 + 0 + 4 + 16] / 8 = 32/8 = 4
- Std Dev = √4 = 2

---

## 2. Probability

### Basic Rules

| Rule | Formula |
|:-----|:--------|
| Probability of event | P(E) = Favorable / Total |
| Complement | P(not E) = 1 - P(E) |
| Addition (mutually exclusive) | P(A or B) = P(A) + P(B) |
| Addition (general) | P(A or B) = P(A) + P(B) - P(A∩B) |
| Multiplication (independent) | P(A and B) = P(A) × P(B) |
| Conditional | P(A|B) = P(A∩B) / P(B) |

### Bayes Theorem
```
P(A|B) = P(B|A) × P(A) / P(B)
```

**Example:** A test is 99% accurate. 1% of people have the disease. If someone tests positive, what's the probability they have the disease?

- P(Disease) = 0.01
- P(Positive | Disease) = 0.99
- P(Positive | No Disease) = 0.01
- P(Positive) = 0.99×0.01 + 0.01×0.99 = 0.0198
- P(Disease | Positive) = 0.99 × 0.01 / 0.0198 = 0.5 = **50%**

**Key insight:** Even with a 99% accurate test, a positive result only means 50% chance of disease (because the disease is rare). This is a classic interview question.

---

## 3. Probability Distributions

### Discrete Distributions

| Distribution | Use For | Mean | Variance |
|:-------------|:--------|:-----|:---------|
| **Binomial** | # successes in n trials | np | np(1-p) |
| **Poisson** | # events in fixed interval | λ | λ |

**Binomial example:** Probability of exactly 2 heads in 5 coin flips
- P(X=2) = C(5,2) × (0.5)² × (0.5)³ = 10 × 0.25 × 0.125 = 0.3125

**Poisson example:** A call center gets 10 calls/hour on average. Probability of exactly 12 calls next hour?
- P(X=12) = e⁻¹⁰ × 10¹² / 12!

### Continuous Distributions

| Distribution | Use For | Key Property |
|:-------------|:--------|:-------------|
| **Normal** | Many natural phenomena | Symmetric, bell-shaped |
| **Uniform** | Equal probability | Flat |
| **Exponential** | Time between events | Memoryless |

### Normal Distribution Rules (68-95-99.7)

```
μ ± 1σ → 68% of data
μ ± 2σ → 95% of data
μ ± 3σ → 99.7% of data
```

**Interview question:** "If test scores are normally distributed with mean 70 and std dev 10, what % of students scored above 90?"
**Answer:** 90 = μ + 2σ → 95% within ±2σ → 2.5% above 90.

---

## 4. Sampling & Central Limit Theorem

### Central Limit Theorem (CLT)
**Statement:** The sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the population distribution.

**Why it matters:** Enables hypothesis testing and confidence intervals even when the population isn't normal.

**Rule of thumb:** n ≥ 30 for CLT to apply.

### Sampling Methods
| Method | Description | Use |
|:-------|:------------|:----|
| Simple random | Equal chance | Unbiased baseline |
| Stratified | Divide into groups, sample each | Ensure representation |
| Cluster | Sample entire groups | Cost-efficient |
| Systematic | Every nth element | Simple, periodic |

---

## 5. Hypothesis Testing

### The Framework

```
1. State H0 (null) and H1 (alternative)
2. Choose significance level (α = 0.05 typically)
3. Calculate test statistic
4. Find p-value
5. Compare p-value to α
6. Reject or fail to reject H0
```

### Errors

| | H0 True | H0 False |
|:--|:--------|:---------|
| **Reject H0** | Type I error (α) | Correct |
| **Fail to reject H0** | Correct | Type II error (β) |

**Type I error:** False positive (rejecting a true null)
**Type II error:** False negative (failing to reject a false null)

**Interview question:** "What's the difference between Type I and Type II errors?"
**Answer:** "Type I is a false positive — concluding there's an effect when there isn't. Type II is a false negative — missing an effect that exists. In medical testing, Type I means telling a healthy person they're sick; Type II means telling a sick person they're healthy."

### Common Tests

| Test | Use For | Key Statistic |
|:-----|:--------|:--------------|
| **t-test** | Compare means of 2 groups | t-statistic |
| **ANOVA** | Compare means of 3+ groups | F-statistic |
| **Chi-square** | Categorical data, independence | χ² |
| **Z-test** | Means with known variance, large n | z-statistic |

### p-Value Interpretation
- p < 0.05 → Statistically significant (reject H0)
- p ≥ 0.05 → Not significant (fail to reject H0)

**Common misconception:** p-value is NOT the probability that H0 is true. It's the probability of observing the data (or more extreme) IF H0 is true.

---

## 6. Confidence Intervals

### Formula
```
CI = Sample Mean ± (Critical Value × Standard Error)
```

**95% CI for mean:**
```
CI = x̄ ± 1.96 × (σ / √n)
```

**Example:** Sample mean = 50, σ = 10, n = 100
- SE = 10/√100 = 1
- 95% CI = 50 ± 1.96 × 1 = [48.04, 51.96]

**Interpretation:** We are 95% confident the true population mean lies between 48.04 and 51.96.

---

## 7. Correlation & Regression

### Correlation (r)
- Range: -1 to +1
- r > 0: positive relationship
- r < 0: negative relationship
- r = 0: no linear relationship
- |r| close to 1: strong relationship

**Correlation ≠ Causation** — always remember this.

### Simple Linear Regression
```
y = β₀ + β₁x + ε
```

**Key metrics:**
- **R²:** Proportion of variance explained (0-1)
- **Coefficient (β₁):** Change in y per unit change in x
- **p-value of coefficient:** Is the relationship significant?

### Multiple Regression
```
y = β₀ + β₁x₁ + β₂x₂ + ... + ε
```

**Interview question:** "How do you validate a regression model?"
**Answer:** "Check R² for fit, p-values for significance, residuals for patterns, and validate on holdout data to check for overfitting."

---

## 8. A/B Testing

### Design
1. **Define hypothesis:** "New checkout reduces drop-off by 10%"
2. **Choose metric:** Primary (conversion) + guardrail (revenue, refunds)
3. **Determine sample size:** Based on effect size, power (80%), significance (5%)
4. **Randomize:** Ensure unbiased assignment
5. **Run:** Control vs. treatment

### Analysis
1. Check sample sizes met
2. Check for bias (no leakage, no peeking)
3. Run hypothesis test (chi-square for proportions, t-test for means)
4. Check p-value < 0.05
5. Check practical significance (effect size)
6. Check guardrail metrics

### Common Pitfalls
| Pitfall | Why It's Bad | Fix |
|:--------|:-------------|:----|
| Peeking at results early | Inflates false positive rate | Pre-commit to duration |
| Small sample size | Low statistical power | Calculate required n upfront |
| Multiple testing | Increases Type I error | Adjust for multiple comparisons |
| Not checking randomization | Biased results | Verify group balance |

---

## 9. Interview Question Bank

### Basic
1. What is the Central Limit Theorem?
2. Explain the difference between mean and median.
3. What is a p-value?
4. What's the difference between correlation and causation?
5. What is a confidence interval?

### Intermediate
6. Explain Type I and Type II errors.
7. When would you use a t-test vs. a chi-square test?
8. What is Simpson's Paradox?
9. How do you detect and handle outliers?
10. What is the difference between a normal and a binomial distribution?

### Advanced
11. How would you design an A/B test for a new feature?
12. A metric dropped 15%. How do you investigate?
13. Explain the bias-variance tradeoff.
14. How do you validate a regression model?
15. What is the difference between R² and adjusted R²?

---

## Quick Reference Formulas

| Concept | Formula |
|:--------|:--------|
| Mean | Σx / n |
| Variance | Σ(x-μ)² / n |
| Std Dev | √Variance |
| Z-score | (x - μ) / σ |
| Binomial mean | np |
| Binomial variance | np(1-p) |
| Poisson mean | λ |
| Bayes | P(A|B) = P(B|A)P(A)/P(B) |
| 95% CI | x̄ ± 1.96 × σ/√n |
| Correlation | Cov(x,y) / (σx × σy) |
| Regression | y = β₀ + β₁x + ε |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Data Analyst Overview | [da-overview.md](da-overview.md) |
| SQL Practice | [sql-practice.md](../business-analyst/sql-practice.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Aptitude (Probability) | [probability.md](../aptitude/quantitative/probability.md) |

---

*Statistics is the language of data. Master it, and you can speak to any business.*

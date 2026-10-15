# Module 04: Statistics, Exploratory Analytics, and Data Storytelling

> **Module Code**: DEL-M04  
> **Priority**: P1 (Core Placement Foundation)  
> **Target Assessment**: Technical Screening, Case Scenarios & Business Problem Solving  
> **Standard**: Complete theoretical explanations, mathematical derivations, worked A/B test calculations, chart selection matrices, and executive communication.

---

## 1. Descriptive Statistics & Distribution Theory

### 1.1 Measures of Central Tendency & Dispersion

* **Mean ($\mu, \bar{x}$)**: Sum divided by count. Sensitive to extreme outliers.
* **Median**: Middle value of sorted observations. Robust to skewness and outliers.
* **Mode**: Most frequently occurring observation. Applicable to categorical data.
* **Variance ($\sigma^2, s^2$) & Standard Deviation ($\sigma, s$)**:
  $$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2, \quad s^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2$$
  *(Bessel's correction $n-1$ removes downward bias when estimating population variance from a sample).*
* **Interquartile Range (IQR)**: $\text{IQR} = Q_3 - Q_1$. Outlier boundaries via Tukey's rule:
  $$\text{Outlier} < Q_1 - 1.5 \times \text{IQR} \quad \text{or} \quad \text{Outlier} > Q_3 + 1.5 \times \text{IQR}$$

---

### 1.2 Probability Foundations & Bayes' Theorem

#### Bayes' Theorem Formulation
$$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)} = \frac{P(B \mid A) \cdot P(A)}{P(B \mid A) \cdot P(A) + P(B \mid \neg A) \cdot P(\neg A)}$$

#### Worked Example 1: Enterprise Anomaly Detection & False Positive Paradox
**Problem**: An automated cybersecurity monitor flags unauthorized database exfiltration. The background base rate of unauthorized attacks on network connections is 0.2% ($P(A) = 0.002$). The monitoring system has a true positive detection rate (sensitivity) of 98% ($P(B \mid A) = 0.98$), and a false alarm rate of 2% ($P(B \mid \neg A) = 0.02$). If an alert is triggered, what is the actual probability that an unauthorized attack is occurring?

**Step-by-Step Calculation**:
1. Prior probability of attack: $P(A) = 0.002$.
2. Prior probability of benign connection: $P(\neg A) = 1 - 0.002 = 0.998$.
3. Likelihood of alert given attack: $P(B \mid A) = 0.98$.
4. Likelihood of alert given benign: $P(B \mid \neg A) = 0.02$.
5. Total probability of alert $P(B)$:
   $$P(B) = (0.98 \times 0.002) + (0.02 \times 0.998) = 0.00196 + 0.01996 = 0.02192.$$
6. Posterior probability $P(A \mid B)$:
   $$P(A \mid B) = \frac{0.00196}{0.02192} \approx 0.08941 \, (8.94\%).$$
*Business Insight for Interview*: Even with a 98% accurate tool, **over 91% of raised alerts are false alarms** due to the low base rate. Recommending immediate server shutdowns on alerts alone would paralyze client operations. Analysts must recommend multi-factor confirmation layers.

---

## 2. Inferential Statistics & Hypothesis Testing

### 2.1 The Central Limit Theorem (CLT) & Standard Error

* **Central Limit Theorem**: Regardless of the underlying population distribution (even if highly skewed), the sampling distribution of the sample mean $\bar{x}$ approaches a normal distribution as sample size $n$ increases ($n \ge 30$ heuristic), with mean $\mu$ and standard error:
  $$\text{SE} = \frac{\sigma}{\sqrt{n}}$$

---

### 2.2 Hypothesis Testing Framework, Errors, and Decision Rules

* **Null Hypothesis ($H_0$)**: Baseline status quo (no difference, no effect).
* **Alternative Hypothesis ($H_1$)**: Research claim (there is a significant difference).
* **Errors & Statistical Power**:
  * **Type I Error ($\alpha$)**: False Positive — Rejecting $H_0$ when it is actually true. (Standard threshold: $\alpha = 0.05$).
  * **Type II Error ($\beta$)**: False Negative — Failing to reject $H_0$ when $H_1$ is true.
  * **Statistical Power ($1 - \beta$)**: Probability of correctly detecting an effect when it exists (Standard target: 80%).

```text
                        ACTUAL REALITY
                    H0 is True      H0 is False (Effect Exists)
Decision: Reject H0 │ Type I Error (α) │ Correct Decision (Power: 1-β) │
Decision: Fail to   │ Correct Decision │ Type II Error (β)            │
          Reject H0 │ (1 - α)          │                              │
```

---

### 2.3 Worked A/B Testing Case: Client Portal Conversion

**Problem**: A Deloitte team redesigns an enterprise SaaS client portal checkout. 
* Group A (Control): $n_A = 10,000$ users, $x_A = 400$ conversions ($p_A = 4.0\% = 0.040$).
* Group B (Treatment): $n_B = 10,000$ users, $x_B = 470$ conversions ($p_B = 4.7\% = 0.047$).
Conduct a two-tailed two-proportion Z-test at $\alpha = 0.05$ ($Z_{\text{crit}} = \pm 1.96$). Does the new design yield a statistically significant lift?

**Step-by-Step Calculation**:
1. Hypotheses: $H_0: p_B - p_A = 0$ versus $H_1: p_B - p_A \ne 0$.
2. Pooled proportion:
   $$p_{\text{pool}} = \frac{x_A + x_B}{n_A + n_B} = \frac{400 + 470}{20,000} = \frac{870}{20,000} = 0.0435.$$
3. Standard error of difference:
   $$\text{SE} = \sqrt{p_{\text{pool}} (1 - p_{\text{pool}}) \left(\frac{1}{n_A} + \frac{1}{n_B}\right)} = \sqrt{0.0435 \times 0.9565 \times \left(\frac{1}{10,000} + \frac{1}{10,000}\right)}$$
   $$\text{SE} = \sqrt{0.0416075 \times 0.0002} = \sqrt{0.0000083215} \approx 0.0028847.$$
4. Observed difference: $p_B - p_A = 0.047 - 0.040 = 0.0070$.
5. Test statistic $Z$:
   $$Z = \frac{0.0070 - 0}{0.0028847} \approx 2.426.$$
6. Conclusion: Since $|Z| = 2.426 > 1.96$ ($p\text{-value} \approx 0.0153 < 0.05$), we reject $H_0$.
*Executive Interpretation*: The 17.5% relative conversion lift ($0.040 \to 0.047$) is statistically significant with 95% confidence and not attributable to random sampling noise.

---

## 3. Data Visualization & Executive Storytelling

### 3.1 Chart Selection Matrix

| Business Question | Data Structure | Recommended Chart | Misleading Anti-Pattern |
| :--- | :--- | :--- | :--- |
| **Trend over Time** | Continuous time-series + numeric metric | **Line Chart** | Bar chart with truncated Y-axis exaggerating tiny swings. |
| **Categorical Comparison**| Discrete categories (5–10 items) | **Horizontal Bar Chart** | 3D exploded pie chart with more than 5 slices. |
| **Part-to-Whole Composition**| Proportions summing to 100% | **Stacked 100% Bar / Treemap** | Multi-ring doughnut chart with unreadable legends. |
| **Correlation & Relationship**| Two continuous numeric variables | **Scatter Plot** | Line chart connecting unrelated categorical points. |
| **Distribution & Spread** | Continuous numeric observations | **Box Plot / Histogram / KDE** | Bar chart plotting only the mean without variance bars. |

---

### 3.2 Translating Statistical Findings to Executive Stakeholders

* **Consulting Translation Rule**: Senior enterprise leaders rarely care about $t$-statistics, degrees of freedom, or homoscedasticity. They care about:
  1. **What is the decision?** (Launch, iterate, or abort)
  2. **What is the quantified financial impact?** (Incremental revenue, cost avoidance)
  3. **What is the downside risk?** (Worst-case confidence bound)

```text
EXECUTIVE TALK TRACK TEMPLATE:
"We conducted a calibrated trial across 20,000 users. The new portal design delivered 
a statistically verified +17.5% lift in conversion (p = 0.015). Projected to our full 
annual traffic of 1.2M users, this change will generate approximately ₹1.8 Cr in 
incremental gross revenue. We recommend rolling out the treatment to 100% of users."
```

---

## 4. Self-Assessment Checklist

- [ ] Can compute mean, median, IQR, and identify outliers using Tukey's fences.
- [ ] Understand Bayes' theorem and can explain the false positive paradox in low-base-rate events.
- [ ] Mastered Central Limit Theorem conditions and standard error calculation.
- [ ] Can compute a two-proportion Z-test and two-sample t-test step-by-step.
- [ ] Confident mapping business analytical questions to optimal visualization formats.

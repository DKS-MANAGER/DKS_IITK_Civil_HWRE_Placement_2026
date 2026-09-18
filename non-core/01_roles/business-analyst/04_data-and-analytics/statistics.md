# Applied Statistics for Business Analysts

> Core statistical concepts, probability distributions, hypothesis testing, and analytical inference for BA problem solving and OA tests.

---

## 1. Descriptive Statistics & Data Distribution

### Central Tendency & Dispersion
- **Mean vs. Median vs. Mode**:
  - *Symmetric distributions*: Mean $\approx$ Median $\approx$ Mode.
  - *Right-skewed (e.g., customer income, order values)*: Mean $>$ Median $>$ Mode.
  - *Left-skewed*: Mean $<$ Median $<$ Mode.
- **Measures of Spread**:
  - **Variance ($\sigma^2$) & Standard Deviation ($\sigma$)**: Dispersion around the mean.
  - **Interquartile Range (IQR)**: $Q_3 - Q_1$, resistant to extreme outliers.
  - **Outlier Detection Rule**: Any point $< Q_1 - 1.5 \times \text{IQR}$ or $> Q_3 + 1.5 \times \text{IQR}$.

---

## 2. Probability & Key Distributions

- **Normal Distribution**: 68% within $\pm 1\sigma$, 95% within $\pm 2\sigma$, 99.7% within $\pm 3\sigma$.
- **Binomial Distribution**: Models binary outcomes (Converted vs. Bounced) over $n$ independent trials with success probability $p$.
- **Poisson Distribution**: Models frequency of discrete events occurring in a fixed interval (e.g., customer support tickets per hour, website server errors per minute).
- **Central Limit Theorem (CLT)**: The sampling distribution of the sample mean approaches normality as sample size $n \ge 30$, regardless of underlying population shape.

---

## 3. Hypothesis Testing & Business Experimentation

### Hypothesis Testing Workflow
1. **State Hypotheses**:
   - $H_0$ (Null Hypothesis): No effect / No difference (e.g., new checkout flow has same conversion rate as old).
   - $H_1$ (Alternative Hypothesis): Significant difference exists.
2. **Choose Significance Level ($\alpha$)**: Standard $\alpha = 0.05$ (5% risk of False Positive).
3. **Compute Test Statistic & p-value**:
   - If $p < \alpha \implies$ Reject $H_0$ (statistically significant effect).
   - If $p \ge \alpha \implies$ Fail to reject $H_0$.

### Error Types Matrix
| Reality \ Decision | Reject $H_0$ | Fail to Reject $H_0$ |
|:---|:---|:---|
| **$H_0$ is True** | **Type I Error ($\alpha$)** (False Positive) | Correct Decision ($1 - \alpha$) |
| **$H_0$ is False** | Correct Decision (**Power** = $1 - \beta$) | **Type II Error ($\beta$)** (False Negative) |

---

## 4. Correlation vs. Causation

- **Pearson Correlation ($r$)**: Measures linear relationship between $-1$ and $+1$.
- **Confounding Variables**: Lurking variables driving both metrics simultaneously (e.g., marketing ad spend driving both website traffic and total returns).
- **Simpson's Paradox**: A trend appears in different groups of data but disappears or reverses when these groups are combined (crucial in segmented conversion analyses).

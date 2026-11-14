# 50 Solved Statistics & Experimentation Numerical Problems

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Coverage:** Probability, Bayes' Theorem, Distributions, MLE, Hypothesis Testing, A/B Testing, Power Analysis, CUPED

---

### Q1. Bayes' Theorem & Diagnostic Screening
**Problem:** In a customer churn risk monitoring pipeline, 4% of active enterprise accounts churn annually ($P(C) = 0.04$). An early-warning telemetry algorithm has a sensitivity of 90% ($P(T^+ \mid C) = 0.90$) and a false positive rate of 5% ($P(T^+ \mid C^c) = 0.05$). What is the posterior probability that an account flagged as high-risk will actually churn?  
**Solution:**
$$P(C \mid T^+) = \frac{P(T^+ \mid C) P(C)}{P(T^+ \mid C) P(C) + P(T^+ \mid C^c) P(C^c)}$$
$$P(C \mid T^+) = \frac{0.90 \times 0.04}{0.90 \times 0.04 + 0.05 \times 0.96} = \frac{0.036}{0.036 + 0.048} = \frac{0.036}{0.084} \approx 0.4286 \ (42.86\%)$$
**Key Takeaway:** Despite high sensitivity, a low base rate means over half of flagged alerts are false alarms.

---

### Q2. Binomial Distribution Expected Defective Count
**Problem:** A warehouse packaging station packs cartons with an item defect probability $p = 0.02$. In a batch of $n = 500$ cartons, calculate the expected number of defective items, the standard deviation, and the probability of observing exactly 0 defects.  
**Solution:**
- $\mathbb{E}[X] = np = 500 \times 0.02 = 10$.
- $\text{Var}(X) = np(1-p) = 500 \times 0.02 \times 0.98 = 9.8 \implies \sigma = \sqrt{9.8} \approx 3.13$.
- $P(X = 0) = (1 - p)^n = (0.98)^{500} \approx 4.1 \times 10^{-5}$.

---

### Q3. Poisson Approximation to Binomial
**Problem:** For the same scenario ($n = 500, p = 0.02$), compute $P(X \le 2)$ using Poisson approximation ($\lambda = np = 10$).  
**Solution:**
$$P(X \le 2) = e^{-10}\left(\frac{10^0}{0!} + \frac{10^1}{1!} + \frac{10^2}{2!}\right) = e^{-10}(1 + 10 + 50) = 61 \cdot e^{-10} \approx 61 \times 4.53999 \times 10^{-5} \approx 0.00277 \ (0.28\%)$$

---

### Q4. Exponential Inter-arrival Waiting Time
**Problem:** Customer orders arrive at an e-commerce micro-fulfillment center at an average rate of 12 orders per hour ($\lambda = 0.2$ orders/min). Find the probability that the waiting time until the next order exceeds 10 minutes.  
**Solution:**
Inter-arrival time $T \sim \text{Exp}(\lambda = 0.2)$.
$$P(T > 10) = e^{-\lambda t} = e^{-0.2 \times 10} = e^{-2} \approx 0.1353 \ (13.53\%)$$

---

### Q5. Conditional Expectation & Memoryless Property
**Problem:** Given that 5 minutes have elapsed without an incoming order in Q4, what is the probability that the total waiting time exceeds 15 minutes?  
**Solution:**
By the memoryless property of exponential distributions:
$$P(T > 15 \mid T > 5) = P(T > 15 - 5) = P(T > 10) = e^{-0.2 \times 10} = e^{-2} \approx 13.53\%$$

---

### Q6. Standard Normal Z-Score Calculation
**Problem:** Retail store weekly revenue is normally distributed with $\mu = \$120,000$ and $\sigma = \$15,000$. What percentage of weeks generate revenue between $\$100,000$ and $\$135,000$?  
**Solution:**
$$Z_1 = \frac{100,000 - 120,000}{15,000} = -\frac{20}{15} \approx -1.33 \implies \Phi(-1.33) \approx 0.0918$$
$$Z_2 = \frac{135,000 - 120,000}{15,000} = \frac{15}{15} = 1.00 \implies \Phi(1.00) \approx 0.8413$$
$$P(100k \le X \le 135k) = \Phi(1.00) - \Phi(-1.33) = 0.8413 - 0.0918 = 0.7495 \ (74.95\%)$$

---

### Q7. Lognormal Expectation and Median
**Problem:** Customer order value $X$ follows a lognormal distribution where $\ln X \sim \mathcal{N}(\mu = 4.0, \sigma^2 = 0.64)$. Compute the median and the mean of the order value.  
**Solution:**
- $\text{Median} = \exp(\mu) = e^{4.0} \approx \$54.60$.
- $\text{Mean } \mathbb{E}[X] = \exp\left(\mu + \frac{\sigma^2}{2}\right) = \exp(4.0 + 0.32) = e^{4.32} \approx \$75.19$.
- *Insight:* Positive skew causes the mean to exceed the median by over 37%.

---

### Q8. Central Limit Theorem Sample Mean Standard Error
**Problem:** A logistics route delivery time has an unknown distribution with mean $\mu = 45$ mins and standard deviation $\sigma = 18$ mins. For a random sample of $n = 81$ deliveries, what is the probability that the sample mean delivery time exceeds 48 minutes?  
**Solution:**
By CLT, $\bar{X} \sim \mathcal{N}\left(\mu = 45, \sigma_{\bar{X}} = \frac{18}{\sqrt{81}} = \frac{18}{9} = 2.0\right)$.
$$Z = \frac{48 - 45}{2.0} = 1.50 \implies P(\bar{X} > 48) = 1 - \Phi(1.50) = 1 - 0.9332 = 0.0668 \ (6.68\%)$$

---

### Q9. Maximum Likelihood Estimation of Exponential Parameter
**Problem:** A sample of $n = 5$ server response latencies (in ms) yielded: $\{12, 18, 25, 30, 15\}$. Assuming an exponential distribution $f(x; \lambda) = \lambda e^{-\lambda x}$, derive the MLE estimate $\hat{\lambda}$ and estimate the mean latency.  
**Solution:**
- $\ell(\lambda) = n \ln \lambda - \lambda \sum_{i=1}^n x_i$. Setting derivative to 0: $\frac{n}{\lambda} - \sum x_i = 0 \implies \hat{\lambda} = \frac{n}{\sum x_i} = \frac{1}{\bar{x}}$.
- $\sum x_i = 100 \implies \bar{x} = 20 \text{ ms}$.
- $\hat{\lambda} = \frac{1}{20} = 0.05 \text{ ms}^{-1}$. Mean latency $= \frac{1}{\hat{\lambda}} = 20 \text{ ms}$.

---

### Q10. Fisher Information & Cramér-Rao Lower Bound
**Problem:** For the exponential distribution in Q9, find the Fisher Information $I(\lambda)$ for a sample of size $n$, and state the minimum possible variance for any unbiased estimator of $\lambda$.  
**Solution:**
$$\frac{\partial^2 \ln f(x; \lambda)}{\partial \lambda^2} = -\frac{1}{\lambda^2} \implies I_1(\lambda) = -\mathbb{E}\left[-\frac{1}{\lambda^2}\right] = \frac{1}{\lambda^2}$$
For sample size $n$, $I_n(\lambda) = \frac{n}{\lambda^2}$.
$$\text{CRLB} = \frac{1}{I_n(\lambda)} = \frac{\lambda^2}{n}$$

---

### Q11. Confidence Interval for Population Mean ($\sigma$ known)
**Problem:** A sample of $n = 64$ customer basket sizes has mean $\bar{x} = \$84.50$. Population standard deviation is known to be $\sigma = \$16.00$. Construct a 95% two-sided confidence interval for the true mean.  
**Solution:**
$$CI = \bar{x} \pm Z_{0.975} \frac{\sigma}{\sqrt{n}} = 84.50 \pm 1.96 \times \frac{16}{8} = 84.50 \pm 1.96 \times 2.0 = 84.50 \pm 3.92 = [\$80.58, \$88.42]$$

---

### Q12. Student's t Confidence Interval ($\sigma$ unknown)
**Problem:** A test of $n = 16$ retail checkout kiosks shows mean scan speed $\bar{x} = 42$ sec with sample standard deviation $s = 6$ sec. Construct a 99% confidence interval ($t_{0.005, 15} = 2.947$).  
**Solution:**
$$CI = \bar{x} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}} = 42 \pm 2.947 \times \frac{6}{4} = 42 \pm 2.947 \times 1.5 = 42 \pm 4.42 = [37.58, 46.42] \text{ seconds}$$

---

### Q13. Confidence Interval for Population Proportion
**Problem:** In a sample of $n = 1,000$ mobile app users, 120 completed an in-app promotion purchase ($\hat{p} = 0.12$). Construct a 95% Wald confidence interval.  
**Solution:**
$$SE = \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}} = \sqrt{\frac{0.12 \times 0.88}{1000}} = \sqrt{0.0001056} \approx 0.010277$$
$$CI = 0.12 \pm 1.96 \times 0.010277 = 0.12 \pm 0.0201 = [0.0999, 0.1401] \implies [9.99\%, 14.01\%]$$

---

### Q14. Required Sample Size for Target Margin of Error
**Problem:** A brand manager wants to estimate customer satisfaction proportion with a margin of error $E = \pm 0.02$ at 95% confidence. Without prior knowledge, what conservative sample size $n$ is required?  
**Solution:**
Conservative assumption: $p = 0.50 \implies p(1-p) = 0.25$.
$$n = \frac{Z^2 p(1-p)}{E^2} = \frac{1.96^2 \times 0.25}{0.02^2} = \frac{3.8416 \times 0.25}{0.0004} = \frac{0.9604}{0.0004} = 2,401$$

---

### Q15. One-Sample Hypothesis Test for Mean
**Problem:** Historical mean delivery time is 30 minutes. A newly deployed routing algorithm in 36 test runs yielded mean $\bar{x} = 28.5$ mins with sample standard deviation $s = 4.5$ mins. Test $H_0: \mu = 30$ vs $H_1: \mu < 30$ at $\alpha = 0.05$ ($t_{\text{crit}, 35} \approx -1.69$).  
**Solution:**
$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{28.5 - 30}{4.5 / 6} = \frac{-1.5}{0.75} = -2.00$$
Since $t = -2.00 < -1.69$, reject $H_0$. Delivery time is significantly reduced.

---

### Q16. Two-Sample Pooled t-Test
**Problem:** Store A ($n_1 = 25, \bar{x}_1 = 150, s_1^2 = 400$) and Store B ($n_2 = 25, \bar{x}_2 = 140, s_2^2 = 350$) have assumed equal variances. Compute pooled variance $s_p^2$ and test statistic $t$.  
**Solution:**
$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{24(400) + 24(350)}{48} = \frac{750}{2} = 375$$
$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2 \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}} = \frac{150 - 140}{\sqrt{375 \times \frac{2}{25}}} = \frac{10}{\sqrt{30}} \approx \frac{10}{5.477} \approx 1.826$$

---

### Q17. Welch's t-Test for Unequal Variances
**Problem:** Group 1 has $n_1 = 100, \bar{x}_1 = 50, s_1^2 = 25$. Group 2 has $n_2 = 50, \bar{x}_2 = 45, s_2^2 = 100$. Compute Welch's test statistic $t$.  
**Solution:**
$$SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} = \sqrt{\frac{25}{100} + \frac{100}{50}} = \sqrt{0.25 + 2.0} = \sqrt{2.25} = 1.5$$
$$t = \frac{50 - 45}{1.5} = \frac{5}{1.5} \approx 3.333$$
$p\text{-value} < 0.001$, highly statistically significant.

---

### Q18. Satterthwaite Degrees of Freedom
**Problem:** Calculate the Satterthwaite degrees of freedom for Q17.  
**Solution:**
Let $v_1 = s_1^2/n_1 = 0.25$ and $v_2 = s_2^2/n_2 = 2.0$.
$$\nu = \frac{(v_1 + v_2)^2}{\frac{v_1^2}{n_1 - 1} + \frac{v_2^2}{n_2 - 1}} = \frac{(2.25)^2}{\frac{0.0625}{99} + \frac{4.0}{49}} = \frac{5.0625}{0.000631 + 0.081633} = \frac{5.0625}{0.082264} \approx 61.54 \implies df = 61$$

---

### Q19. Paired t-Test Before vs After
**Problem:** A price reduction is piloted across $n = 10$ stores. The mean store sales difference (Post - Pre) is $\bar{d} = +45$ units with sample standard deviation of differences $s_d = 50$ units. Test $H_0: \mu_d = 0$ at $\alpha = 0.05$ ($t_{\text{crit}, 9} = 2.262$).  
**Solution:**
$$t = \frac{\bar{d} - 0}{s_d / \sqrt{n}} = \frac{45}{50 / \sqrt{10}} = \frac{45}{15.811} \approx 2.846$$
Since $2.846 > 2.262$, reject $H_0$. Sales increased significantly.

---

### Q20. Cohen's d Effect Size Calculation
**Problem:** In Q19, compute Cohen's $d$ effect size for the paired difference.  
**Solution:**
$$d = \frac{\bar{d}}{s_d} = \frac{45}{50} = 0.90$$
This represents a large practical effect size ($d \ge 0.8$).

---

### Q21. One-Way ANOVA F-Ratio Calculation
**Problem:** Comparing 3 store display formats across 30 total stores ($k = 3, N = 30$). Given Sum of Squares Between $\text{SSB} = 400$ and Sum of Squares Within $\text{SSW} = 540$. Compute the $F$-statistic and test at $\alpha = 0.05$ ($F_{\text{crit}}(2, 27) = 3.35$).  
**Solution:**
- $df_{\text{between}} = k - 1 = 2 \implies \text{MSB} = 400 / 2 = 200$.
- $df_{\text{within}} = N - k = 27 \implies \text{MSW} = 540 / 27 = 20$.
- $F = \frac{\text{MSB}}{\text{MSW}} = \frac{200}{20} = 10.0$.
Since $10.0 > 3.35$, reject $H_0$. At least one display format differs.

---

### Q22. Chi-Square Test of Independence Contingency Table
**Problem:** A retail campaign tests two email subject lines:
- Subject A: 120 opened, 880 unopened (Total 1,000)
- Subject B: 160 opened, 840 unopened (Total 1,000)
Calculate the $\chi^2$ statistic.  
**Solution:**
Overall open rate $= \frac{280}{2000} = 14\%$. Expected opened per group $= 140$, expected unopened $= 860$.
$$\chi^2 = 2 \times \left[\frac{(120 - 140)^2}{140} + \frac{(880 - 860)^2}{860}\right] = 2 \times \left[\frac{400}{140} + \frac{400}{860}\right] = 2 \times [2.857 + 0.465] = 2 \times 3.322 = 6.644$$
For $df = 1$, critical value at $\alpha = 0.05$ is $3.841$. Since $6.644 > 3.841$, reject $H_0$ ($p \approx 0.01$).

---

### Q23. Sample Ratio Mismatch (SRM) Detection
**Problem:** An A/B test with an intended 50:50 traffic split registers $n_C = 49,000$ and $n_T = 51,000$ ($N = 100,000$). Check for SRM using $\chi^2$ test at $\alpha = 0.001$ ($crit = 10.83$).  
**Solution:**
$$E_C = E_T = 50,000$$
$$\chi^2 = \frac{(49000 - 50000)^2}{50000} + \frac{(51000 - 50000)^2}{50000} = \frac{1,000,000}{50000} + \frac{1,000,000}{50000} = 20 + 20 = 40.0$$
Since $40.0 \gg 10.83$, severe SRM exists. The experiment is invalidated.

---

### Q24. Minimum Sample Size for Binary Conversion A/B Test
**Problem:** Baseline conversion $p_1 = 0.05$. We wish to detect a 10% relative lift ($p_2 = 0.055, \delta = 0.005$) with $\alpha = 0.05$ ($Z_{\alpha/2} = 1.96$) and power $1 - \beta = 0.80$ ($Z_\beta = 0.8416$). Using Evan Miller formula, calculate $n$ per variant.  
**Solution:**
$$\bar{p} = \frac{0.05 + 0.055}{2} = 0.0525, \quad 1 - \bar{p} = 0.9475$$
$$n \approx \frac{(1.96 \sqrt{2 \times 0.0525 \times 0.9475} + 0.8416 \sqrt{0.05 \times 0.95 + 0.055 \times 0.945})^2}{0.005^2}$$
$$n \approx \frac{(1.96 \sqrt{0.09949} + 0.8416 \sqrt{0.0475 + 0.05198})^2}{0.000025} = \frac{(1.96 \times 0.3154 + 0.8416 \times 0.3154)^2}{0.000025} = \frac{(0.6182 + 0.2654)^2}{0.000025} = \frac{(0.8836)^2}{0.000025} \approx \frac{0.7808}{0.000025} \approx 31,232$$
Required sample size: $\approx 31,300$ users per variant.

---

### Q25. Sample Size for Continuous Revenue Metric
**Problem:** Average revenue per user is $\mu = \$40$ with standard deviation $\sigma = \$100$. What sample size per variant is needed to detect an MDE of $\$2.00$ ($\delta = 2$) at $\alpha = 0.05, \text{power} = 0.80$?  
**Solution:**
$$n = \frac{2 \sigma^2 (Z_{1-\alpha/2} + Z_{1-\beta})^2}{\delta^2} = \frac{2 \times 100^2 \times (1.96 + 0.8416)^2}{2^2} = \frac{20,000 \times 7.849}{4} = 5,000 \times 7.849 \approx 39,245 \text{ users/variant}$$

---

### Q26. CUPED Variance Reduction Factor
**Problem:** In an experiment measuring user spend $Y$, pre-experiment spend $X$ has correlation $\rho = 0.60$ with $Y$. If original required sample size was $n = 40,000$, what is the required sample size using CUPED?  
**Solution:**
$$\text{Variance Reduction Factor} = 1 - \rho^2 = 1 - 0.60^2 = 1 - 0.36 = 0.64$$
$$n_{\text{CUPED}} = n_{\text{orig}} \times (1 - \rho^2) = 40,000 \times 0.64 = 25,600 \text{ users/variant}$$
Saves $14,400$ users per variant (36% reduction in sample size or experiment duration).

---

### Q27. Optimal CUPED Coefficient $\theta^*$
**Problem:** In an A/B test sample, $\text{Cov}(Y, X) = 450$ and $\text{Var}(X) = 600$. Calculate the optimal $\theta^*$ and write the adjusted metric equation for a user with $Y_i = 120, X_i = 90$, given $\bar{X} = 80$.  
**Solution:**
$$\theta^* = \frac{\text{Cov}(Y, X)}{\text{Var}(X)} = \frac{450}{600} = 0.75$$
$$\hat{Y}_{i, \text{CUPED}} = Y_i - \theta^*(X_i - \bar{X}) = 120 - 0.75(90 - 80) = 120 - 7.5 = 112.5$$

---

### Q28. Bonferroni Multiple Testing Correction
**Problem:** An analytics team evaluates 10 secondary metrics alongside the primary A/B test metric at baseline $\alpha = 0.05$. What is the adjusted Bonferroni threshold $\alpha^*$ and what would the unadjusted FWER be?  
**Solution:**
$$\alpha^* = \frac{\alpha}{m} = \frac{0.05}{10} = 0.005$$
$$\text{FWER}_{\text{unadjusted}} = 1 - (1 - 0.05)^{10} = 1 - (0.95)^{10} = 1 - 0.5987 = 0.4013 \ (40.13\%)$$

---

### Q29. Benjamini-Hochberg FDR Procedure
**Problem:** Four tests yield sorted $p$-values: $p_{(1)} = 0.010, p_{(2)} = 0.022, p_{(3)} = 0.038, p_{(4)} = 0.060$. At target FDR $Q = 0.05$ with $m = 4$, determine which hypotheses are rejected.  
**Solution:**
Compute thresholds $T_k = \frac{k}{m} \times Q$:
- $k=1: T_1 = \frac{1}{4} \times 0.05 = 0.0125$. Since $p_{(1)} = 0.010 \le 0.0125$, passes.
- $k=2: T_2 = \frac{2}{4} \times 0.05 = 0.0250$. Since $p_{(2)} = 0.022 \le 0.0250$, passes.
- $k=3: T_3 = \frac{3}{4} \times 0.05 = 0.0375$. Since $p_{(3)} = 0.038 > 0.0375$, fails.
- $k=4: T_4 = \frac{4}{4} \times 0.05 = 0.0500$. Since $p_{(4)} = 0.060 > 0.0500$, fails.
Largest $k$ satisfying $p_{(k)} \le T_k$ is $k = 2$. Reject $H_{(1)}$ and $H_{(2)}$.

---

### Q30. Mann-Whitney U Test Statistic
**Problem:** Two small groups have rank sums. Group 1 ($n_1 = 5$) has rank sum $R_1 = 38$. Group 2 ($n_2 = 5$) has rank sum $R_2 = 17$. Compute $U_1$ and $U_2$.  
**Solution:**
$$U_1 = n_1 n_2 + \frac{n_1(n_1 + 1)}{2} - R_1 = 5 \times 5 + \frac{5 \times 6}{2} - 38 = 25 + 15 - 38 = 2$$
$$U_2 = n_1 n_2 - U_1 = 25 - 2 = 23$$
$$\text{Test statistic } U = \min(U_1, U_2) = 2$$

---

### Q31. Unequal Traffic Split Sample Penalty
**Problem:** An A/B test allocates 80% traffic to Control and 20% to Treatment ($k = n_T / n_C = 0.25$). By what factor does the total required sample size increase compared to a 50:50 split?  
**Solution:**
$$\text{Inflation Factor} = \frac{(k + 1)^2}{4k} = \frac{(0.25 + 1)^2}{4 \times 0.25} = \frac{1.25^2}{1.0} = 1.5625$$
Requires $56.25\%$ more total sample size.

---

### Q32. Beta-Binomial Conjugate Updating
**Problem:** In a Bayesian conversion test, prior distribution is $\text{Beta}(\alpha=2, \beta=38)$ (prior mean $= 5\%$). We observe 10 conversions out of 100 new impressions. What is the posterior distribution and posterior mean?  
**Solution:**
$$\alpha_{\text{post}} = \alpha_{\text{prior}} + \text{successes} = 2 + 10 = 12$$
$$\beta_{\text{post}} = \beta_{\text{prior}} + \text{failures} = 38 + 90 = 128$$
$$\text{Posterior Mean} = \frac{\alpha_{\text{post}}}{\alpha_{\text{post}} + \beta_{\text{post}}} = \frac{12}{12 + 128} = \frac{12}{140} \approx 0.0857 \ (8.57\%)$$

---

### Q33. Covariance and Pearson Correlation
**Problem:** Given $\sum (x_i - \bar{x})^2 = 200, \sum (y_i - \bar{y})^2 = 800$, and $\sum (x_i - \bar{x})(y_i - \bar{y}) = 360$. Compute sample correlation $r$.  
**Solution:**
$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} = \frac{360}{\sqrt{200 \times 800}} = \frac{360}{\sqrt{160,000}} = \frac{360}{400} = 0.90$$

---

### Q34. Linear Regression Slope and Intercept
**Problem:** For the data in Q33 with $\bar{x} = 10, \bar{y} = 50$, find the OLS regression line $y = \beta_0 + \beta_1 x$.  
**Solution:**
$$\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = \frac{360}{200} = 1.80$$
$$\beta_0 = \bar{y} - \beta_1 \bar{x} = 50 - 1.80(10) = 50 - 18 = 32$$
$$\hat{y} = 32 + 1.80 x$$

---

### Q35. Coefficient of Determination ($R^2$)
**Problem:** For the simple bivariate regression in Q33–Q34, what is $R^2$?  
**Solution:**
In simple bivariate linear regression:
$$R^2 = r^2 = (0.90)^2 = 0.81 \ (81\% \text{ of variance explained})$$

---

### Q36. Adjusted $R^2$ Under Feature Addition
**Problem:** A model with $n = 100$ and $p = 5$ predictors has $R^2 = 0.60$. A 6th predictor is added ($p = 6$), increasing $R^2$ to $0.61$. Compute $R^2_{\text{adj}}$ for both models.  
**Solution:**
$$R^2_{\text{adj}} = 1 - \frac{(1 - R^2)(n - 1)}{n - p - 1}$$
- Model 1: $1 - \frac{(1 - 0.60)(99)}{100 - 5 - 1} = 1 - \frac{0.40 \times 99}{94} = 1 - \frac{39.6}{94} = 1 - 0.4213 = 0.5787$.
- Model 2: $1 - \frac{(1 - 0.61)(99)}{100 - 6 - 1} = 1 - \frac{0.39 \times 99}{93} = 1 - \frac{38.61}{93} = 1 - 0.4152 = 0.5848$.
Since $R^2_{\text{adj}}$ increased from 0.5787 to 0.5848, the added predictor genuinely improved explanatory power.

---

### Q37. Chi-Square Goodness-of-Fit Test
**Problem:** Customer orders across Monday through Friday are hypothesized to be uniform ($20\%$ each). Observed orders ($N = 500$): Mon: 80, Tue: 95, Wed: 105, Thu: 100, Fri: 120. Test at $\alpha = 0.05$ ($\chi^2_{\text{crit}, 4} = 9.488$).  
**Solution:**
$E_i = 500 \times 0.20 = 100$ for all days.
$$\chi^2 = \frac{(80-100)^2}{100} + \frac{(95-100)^2}{100} + \frac{(105-100)^2}{100} + \frac{(100-100)^2}{100} + \frac{(120-100)^2}{100}$$
$$\chi^2 = \frac{400 + 25 + 25 + 0 + 400}{100} = \frac{850}{100} = 8.50$$
Since $8.50 < 9.488$, fail to reject $H_0$. Order distribution is consistent with uniform.

---

### Q38. Geometric Distribution Expected Value
**Problem:** The probability that a cold sales outreach leads to a booked meeting is $p = 0.04$. How many outreach attempts are expected before securing the first meeting?  
**Solution:**
$$\mathbb{E}[X] = \frac{1}{p} = \frac{1}{0.04} = 25 \text{ attempts}$$

---

### Q39. Negative Binomial Expectation
**Problem:** For the sales outreach in Q38 ($p = 0.04$), how many failures are expected before securing $r = 3$ meetings?  
**Solution:**
$$\mathbb{E}[\text{Failures}] = \frac{r(1-p)}{p} = \frac{3 \times 0.96}{0.04} = 3 \times 24 = 72 \text{ failures}$$
Total attempts expected $= 72 + 3 = 75$.

---

### Q40. Uniform Distribution Variance
**Problem:** Delivery transit time is uniformly distributed between $a = 2$ and $b = 10$ days. Compute the mean, variance, and $P(X \ge 8)$.  
**Solution:**
- Mean $= \frac{a+b}{2} = \frac{12}{2} = 6$ days.
- $\text{Var}(X) = \frac{(b-a)^2}{12} = \frac{8^2}{12} = \frac{64}{12} = 5.33 \text{ days}^2$.
- $P(X \ge 8) = \frac{10 - 8}{10 - 2} = \frac{2}{8} = 0.25 \ (25\%)$.

---

### Q41. Poisson Arrival Probability in Shifted Horizon
**Problem:** Website crash logs average $\lambda = 3$ events per day. What is the probability of observing exactly 4 events over a 2-day weekend?  
**Solution:**
Rate for 2 days: $\lambda_{2\text{d}} = 3 \times 2 = 6$.
$$P(X = 4) = \frac{6^4 e^{-6}}{4!} = \frac{1296 \times 0.00247875}{24} = 54 \times 0.00247875 \approx 0.1339 \ (13.39\%)$$

---

### Q42. Chebyshev's Inequality Conservative Bound
**Problem:** Daily store footfall has mean $\mu = 1,000$ and $\sigma = 100$, distribution unknown. Bound the probability that footfall falls outside $[700, 1300]$.  
**Solution:**
$k = \frac{1300 - 1000}{100} = 3$.
$$P(|X - \mu| \ge 3\sigma) \le \frac{1}{k^2} = \frac{1}{9} \approx 0.1111 \ (11.11\%)$$

---

### Q43. Type II Error Probability ($\beta$)
**Problem:** In testing $H_0: \mu = 50$ vs $H_1: \mu = 54$ with $n = 25, \sigma = 10, \alpha = 0.05$ (one-tailed, $Z_{\text{crit}} = 1.645$). Find $\beta$.  
**Solution:**
$$SE = \frac{10}{\sqrt{25}} = 2.0$$
Critical threshold under $H_0$: $\bar{x}_{\text{crit}} = 50 + 1.645(2.0) = 53.29$.
Under $H_1$ ($\mu = 54$):
$$Z = \frac{53.29 - 54}{2.0} = \frac{-0.71}{2.0} = -0.355$$
$$\beta = \Phi(-0.355) \approx 0.3613 \implies \text{Power } = 1 - \beta \approx 63.87\%$$

---

### Q44. Kurtosis & Tail-Risk Interpretation
**Problem:** A SKU demand distribution has skewness $+2.4$ and excess kurtosis $+7.8$. What does this imply for safety stock calculation compared to a normal distribution assumption?  
**Solution:**
Positive excess kurtosis (leptokurtic) indicates fat tails and extreme outlier spikes. Standard Gaussian safety stock ($k \cdot \sigma$) will severely underestimate stockout risk during tail events. A fat-tailed distribution (e.g., Extreme Value or negative binomial) or empirical quantile buffer is required.

---

### Q45. Delta Method Variance of Ratio Metric
**Problem:** An A/B test evaluates Revenue per Click $R = Y / X$, where $\mathbb{E}[Y] = 50, \mathbb{E}[X] = 10, \text{Var}(Y) = 100, \text{Var}(X) = 4, \text{Cov}(X, Y) = 15$. Approximate $\text{Var}(R)$.  
**Solution:**
Using the first-order multivariate Delta Method:
$$\text{Var}\left(\frac{Y}{X}\right) \approx \left(\frac{\mu_Y}{\mu_X}\right)^2 \left[\frac{\text{Var}(Y)}{\mu_Y^2} + \frac{\text{Var}(X)}{\mu_X^2} - \frac{2\text{Cov}(X,Y)}{\mu_X \mu_Y}\right]$$
$$\text{Var}(R) \approx \left(\frac{50}{10}\right)^2 \left[\frac{100}{2500} + \frac{4}{100} - \frac{2(15)}{10 \times 50}\right] = 25 \left[0.04 + 0.04 - \frac{30}{500}\right] = 25 [0.08 - 0.06] = 25 \times 0.02 = 0.50$$

---

### Q46. False Positive Rate Under Repeated Significance Testing
**Problem:** An analyst tests an A/B test after day 1, day 2, ..., up to day 5. If each check is performed at $\alpha = 0.05$ and checks are independent (simplifying lower bound), what is the overall probability of a false positive?  
**Solution:**
$$\alpha_{\text{inflated}} = 1 - (1 - 0.05)^5 = 1 - (0.95)^5 = 1 - 0.7738 = 0.2262 \ (22.62\%)$$
*Lesson:* Peeking multiplies Type I error by more than $4.5\times$.

---

### Q47. F-Test for Equality of Two Variances
**Problem:** Sample 1 ($n_1 = 21, s_1^2 = 80$) and Sample 2 ($n_2 = 16, s_2^2 = 32$). Test $H_0: \sigma_1^2 = \sigma_2^2$ at $\alpha = 0.05$ ($F_{\text{crit}}(20, 15) \approx 2.33$).  
**Solution:**
$$F = \frac{s_1^2}{s_2^2} = \frac{80}{32} = 2.50$$
Since $2.50 > 2.33$, reject $H_0$. Variances are statistically unequal; Welch's $t$-test is required.

---

### Q48. Simpson's Paradox Detection
**Problem:** Segment A: Variant 1 has 10/100 (10%), Variant 2 has 25/200 (12.5%). Segment B: Variant 1 has 80/400 (20%), Variant 2 has 22/100 (22%). Compute overall aggregate conversion rates for Variant 1 and 2.  
**Solution:**
- Variant 1 overall: $\frac{10 + 80}{100 + 400} = \frac{90}{500} = 18.0\%$.
- Variant 2 overall: $\frac{25 + 22}{200 + 100} = \frac{47}{300} \approx 15.67\%$.
*Paradox:* Variant 2 wins in Segment A ($12.5\% > 10\%$) and wins in Segment B ($22\% > 20\%$), yet Variant 1 wins overall ($18\% > 15.67\%$) because Variant 1 had 80% of its traffic in high-converting Segment B vs only 33% for Variant 2.

---

### Q49. Information Criterion (AIC / BIC) Comparison
**Problem:** Model 1 has log-likelihood $\ell_1 = -240$ with $k_1 = 3$ parameters ($N = 200$). Model 2 has $\ell_2 = -232$ with $k_2 = 6$ parameters. Compare using AIC ($2k - 2\ell$).  
**Solution:**
- $\text{AIC}_1 = 2(3) - 2(-240) = 6 + 480 = 486$.
- $\text{AIC}_2 = 2(6) - 2(-232) = 12 + 464 = 476$.
Model 2 is preferred because $\Delta\text{AIC} = 10 > 2$, providing strong evidence that the additional 3 parameters significantly improve fit.

---

### Q50. Gini Impurity vs Entropy Calculation
**Problem:** A decision tree node contains 30 Class 0 and 70 Class 1 samples ($p_0 = 0.3, p_1 = 0.7$). Calculate Gini Impurity and Entropy (base 2).  
**Solution:**
- $\text{Gini} = 1 - \sum p_i^2 = 1 - (0.3^2 + 0.7^2) = 1 - (0.09 + 0.49) = 1 - 0.58 = 0.42$.
- $\text{Entropy} = - (0.3 \log_2 0.3 + 0.7 \log_2 0.7) = - (0.3 \times (-1.737) + 0.7 \times (-0.5146)) = - (-0.5211 - 0.3602) = 0.8813 \text{ bits}$.

# 06. Analytics & Decision Science: High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][SQL] Write a query calculating 7-day rolling active users per region.

**Direct Answer / Solution Approach:**
```text
SELECT event_date, region, COUNT(DISTINCT user_id) OVER (PARTITION BY region ORDER BY event_date RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW) as rolling_7d_users FROM user_events;
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How does RANGE differ from ROWS in SQL window frames when duplicate timestamps exist?

---

### Question 2: [P0][STATS] Calculate sample size required for an A/B test with 4% baseline conversion and 10% target relative lift.

**Direct Answer / Solution Approach:**
```text
Baseline $p = 0.04$, MDE $\Delta = 0.04 	imes 0.10 = 0.004$. Using formula $N pprox rac{16 \cdot p(1-p)}{\Delta^2} = rac{16 \cdot 0.04 \cdot 0.96}{(0.004)^2} = rac{0.6144}{0.000016} pprox 38,400$ users per variant (Total = ~76,800 users).
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: If daily traffic is only 5,000 visitors, how many days must the test run to prevent day-of-week seasonality bias? (Run for minimum 16 days -> round up to 3 full weeks / 21 days).

---

### Question 3: [P1][EXPERIMENTATION] How do you detect and resolve Sample Ratio Mismatch (SRM)?

**Direct Answer / Solution Approach:**
```text
Perform a Chi-Square Goodness-of-Fit test on observed vs expected traffic counts: $\chi^2 = \sum rac{(O - E)^2}{E}$. If $p < 0.001$, significant SRM exists. Immediate actions: Check user redirection redirects, bot-filtering discrepancies, and variant assignment hashing logic in backend.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: Can you trust secondary conversion metrics if SRM is present on the primary variant? (No, SRM invalidates sample randomization and causes severe selection bias).


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)

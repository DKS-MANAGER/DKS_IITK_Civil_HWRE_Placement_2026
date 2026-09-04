# Data Analyst — Complete Preparation System

> What DAs do, what companies test, how to prepare, and how your Civil/M.Tech profile positions you for data analyst roles.

---

## What a Data Analyst Does

A Data Analyst collects, cleans, analyzes, and visualizes data to help organizations make data-driven decisions.

**Core responsibilities:**
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Statistical analysis and hypothesis testing
- Building dashboards and visualizations
- A/B testing and experimentation
- Communicating insights to stakeholders

### Day-to-Day Work

| Task | Example | % of Time |
|:-----|:--------|:---------:|
| **Data cleaning** | Handle missing values, outliers, duplicates | 30% |
| **SQL queries** | Extract data from databases | 20% |
| **Python/Pandas analysis** | EDA, feature engineering | 25% |
| **Visualization** | Charts, dashboards, reports | 15% |
| **Communication** | Present findings, answer questions | 10% |

---

## What Recruiters Test

### Interview Process (Typical)

| Round | Format | What's Tested |
|:------|:-------|:--------------|
| **Online Assessment** | SQL + Python + statistics + aptitude | Technical fundamentals |
| **SQL Round** | Live SQL queries | Query writing, data manipulation |
| **Python Round** | Pandas/NumPy coding | Data manipulation, logic |
| **Statistics Round** | Probability, hypothesis testing | Statistical reasoning |
| **Case / Analytical** | Business problem, data interpretation | Analytical thinking |
| **Behavioral / Fit** | STAR questions | Communication, teamwork |

### Core Skills Tested

| Skill | Weight | How to Prepare |
|:------|:------:|:---------------|
| **SQL** | 25% | Advanced queries, optimization |
| **Python/Pandas** | 25% | Data manipulation, EDA |
| **Statistics** | 20% | Distributions, hypothesis testing, regression |
| **Probability** | 10% | Conditional probability, Bayes |
| **A/B testing** | 10% | Experiment design, analysis |
| **Communication** | 10% | Data storytelling |

---

## Topic Checklist

### Must Know [P0]

- [ ] SQL: joins, aggregations, window functions, CTEs
- [ ] Python: Pandas (merge, groupby, pivot, apply)
- [ ] Python: NumPy (arrays, vectorized operations)
- [ ] Statistics: mean, median, mode, variance, std dev
- [ ] Statistics: normal distribution, z-scores
- [ ] Probability: conditional probability, Bayes theorem
- [ ] Data cleaning: missing values, outliers, duplicates
- [ ] Data visualization: matplotlib, seaborn

### Should Know [P1]

- [ ] Hypothesis testing: t-test, chi-square, p-values
- [ ] Confidence intervals
- [ ] Correlation vs causation
- [ ] Regression basics (linear, logistic)
- [ ] A/B testing design and analysis
- [ ] EDA best practices

### Good to Know [P2]

- [ ] Machine learning basics (classification, clustering)
- [ ] Time series analysis
- [ ] Power BI / Tableau
- [ ] SQL optimization

---

## Question Bank

### Basic

1. What's the difference between a Data Analyst and a Data Scientist?
2. Explain the difference between mean, median, and mode.
3. What is a p-value?
4. How do you handle missing data?
5. What's the difference between correlation and causation?

### Intermediate

6. Explain the Central Limit Theorem.
7. What is a confidence interval?
8. How do you detect outliers?
9. Explain the difference between Type I and Type II errors.
10. How would you design an A/B test?

### Advanced

11. A KPI fell 15%. How would you investigate?
12. Explain the difference between a t-test and a chi-square test.
13. How do you validate a regression model?
14. What is Simpson's Paradox?
15. How would you measure the impact of a feature launch?

---

## Analytical Problems (Business → Data → Insight)

### Problem 1: KPI Investigation
**Business question:** "Why did daily active users (DAU) drop 15% last week?"

**Data needed:**
- DAU by day, platform, region
- New vs. returning users
- Feature usage
- External events (outages, competitor launches)

**Analysis approach:**
1. Segment the drop (which platform/region/cohort?)
2. Check if it's new or returning users
3. Correlate with product changes or external events
4. Form and test hypotheses

**Result:** "The drop is concentrated in Android users in Tier 2 cities, driven by a bug in the latest app release that caused crashes on low-end devices."

**Recommendation:** "Roll back the release, fix the bug, and re-release after testing on low-end devices."

### Problem 2: Metric Selection
**Business question:** "What metric should we track for our new subscription product?"

**Framework:**
1. Define the goal (revenue growth? retention? engagement?)
2. North Star metric (the one that best captures value)
3. Supporting metrics (funnel, retention, engagement)
4. Guardrail metrics (things you don't want to break)

**Example:**
- North Star: Weekly active subscribers
- Supporting: Signup conversion, activation rate, retention, churn
- Guardrail: Support tickets, refund rate

### Problem 3: A/B Test Analysis
**Business question:** "Did the new checkout flow improve conversion?"

**Analysis:**
1. Check sample sizes (statistical power)
2. Check for bias (random assignment, no leakage)
3. Run hypothesis test (chi-square for conversion rates)
4. Check significance (p-value < 0.05)
5. Check practical significance (effect size)
6. Check guardrail metrics (revenue, refunds)

**Result:** "Conversion improved 3% (p=0.02), statistically significant. Revenue per user also improved 2%. No negative impact on refunds. Recommend rollout."

---

## Resume Tips for DA

**Emphasize:**
- Python/Pandas skills (from research, projects)
- Statistical analysis (from thesis, experiments)
- Data visualization
- SQL

**Bullet example:**
- "Cleaned and analyzed 100,000+ data points using Python (Pandas, NumPy), identifying [insight] with statistical significance"
- "Built predictive model (R² = 0.87) to forecast [outcome], improving decision accuracy"

→ Full resume guide: [resume.md](../common/resume.md)

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Statistics Practice | [statistics-practice.md](statistics-practice.md) |
| SQL Practice | [sql-practice.md](../business-analyst/sql-practice.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Analytics Resources | [non-core-prep.md](../analytics/non-core-prep.md) |

---

*Data analysts don't just crunch numbers — they turn data into decisions.*

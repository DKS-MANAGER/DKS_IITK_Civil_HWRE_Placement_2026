# Data Analyst — Rapid Revision Sheet

> Last-minute revision for DA interviews. SQL, statistics, and Python quick reference in 15 minutes.

---

## SQL Quick Reference

### Essential Patterns
```sql
-- Window functions
ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric)
RANK() OVER (ORDER BY metric DESC)
LAG(metric, 1) OVER (ORDER BY date)  -- previous row
LEAD(metric, 1) OVER (ORDER BY date) -- next row
SUM(metric) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)  -- running total

-- CTE
WITH cte_name AS (
    SELECT ... FROM ... WHERE ...
)
SELECT ... FROM cte_name;

-- CASE
CASE WHEN condition THEN result WHEN condition THEN result ELSE default END

-- Date functions
DATE_TRUNC('month', date_col)
DATEADD(day, -30, GETDATE())
EXTRACT(YEAR FROM date_col)
```

### JOIN Types
```
INNER JOIN → Only matching rows
LEFT JOIN  → All left + matching right (NULL for non-matching)
RIGHT JOIN → All right + matching left (NULL for non-matching)
FULL JOIN  → All rows from both (NULL for non-matching)
CROSS JOIN → Every combination of rows
```

### Common Interview Queries
| Problem | Pattern |
|:--------|:--------|
| Nth highest salary | ROW_NUMBER() or subquery |
| Running total | SUM() OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) |
| Year-over-year | LAG() OVER (PARTITION BY month ORDER BY year) |
| Top N per group | ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric DESC) WHERE rank <= N |
| Delete duplicates | ROW_NUMBER() OVER (PARTITION BY cols) WHERE rank > 1 |

---

## Statistics Quick Reference

### Descriptive Statistics
| Measure | Formula | When to Use |
|:--------|:--------|:------------|
| Mean | Σx ÷ n | Symmetric data |
| Median | Middle value | Skewed data |
| Mode | Most frequent | Categorical data |
| Variance | Σ(x−μ)² ÷ (n−1) | Spread measure |
| Std Dev | √Variance | Spread measure |
| IQR | Q3 − Q1 | Skewed data spread |

### Distributions
| Distribution | Use Case | Key Property |
|:-------------|:---------|:-------------|
| Normal | Continuous, symmetric | Mean = Median = Mode |
| Binomial | # of successes in n trials | Discrete, 2 outcomes |
| Poisson | # of events in time period | Rare events, fixed interval |
| t-distribution | Small sample mean testing | Heavy tails |

### Hypothesis Testing Steps
```
1. H₀ (null): No effect / no difference
2. H₁ (alternative): There is an effect / difference
3. Choose significance level (α = 0.05)
4. Calculate test statistic
5. Calculate p-value
6. If p < α → reject H₀
7. If p ≥ α → fail to reject H₀
```

### Common Tests
| Test | When to Use |
|:-----|:------------|
| t-test | Compare means of 2 groups |
| Chi-square | Test association between categorical variables |
| ANOVA | Compare means of 3+ groups |
| Z-test | Large sample, known population std dev |

### A/B Testing
```
1. Define metric (conversion rate, revenue per user)
2. Calculate sample size (power analysis)
3. Random assignment (control vs. treatment)
4. Run for sufficient duration
5. Check for statistical significance (p < 0.05)
6. Check practical significance (effect size)
7. Check guardrail metrics (don't break other things)
```

---

## Python/Pandas Quick Reference

### Essential Operations
```python
# Load data
df = pd.read_csv('data.csv')

# Basic operations
df.head(), df.describe(), df.info()

# Filter
df[df['column'] > value]
df[df['column'].isin(['a', 'b'])]

# Group and aggregate
df.groupby('category')['value'].agg(['mean', 'sum', 'count'])

# Merge
pd.merge(df1, df2, on='key', how='left')

# Pivot
df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')

# Handle missing values
df.isnull().sum()
df.fillna(0)
df.dropna()

# Create new column
df['new_col'] = df['col1'] / df['col2']
```

---

## Last-Minute Checklist

- [ ] Practiced 5 SQL queries (JOINs, window functions, CTEs)
- [ ] Reviewed hypothesis testing steps
- [ ] Reviewed Pandas operations (groupby, merge, pivot)
- [ ] Reviewed common chart types
- [ ] Prepared 4 STAR stories
- [ ] Researched [company] data stack
- [ ] Reviewed A/B testing framework

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| Statistics Practice | [statistics-practice.md](statistics-practice.md) |
| SQL Practice | [../business-analyst/sql-practice.md](../business-analyst/sql-practice.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Print this sheet 1 hour before your DA interview.*

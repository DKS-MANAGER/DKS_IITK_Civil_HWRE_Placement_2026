# Module 08 — R Programming & Tidyverse for Financial Analytics

While Python and SQL dominate day-to-day data pipelines at Accordion (Merilytics), **R** is explicitly cited in the job description (`Work with Excel, PowerPivot, SQL, R, Python...`). R is frequently leveraged in legacy portfolio company analytics, econometric regression modeling, and specialized statistical visualizations.

---

## 1. Core R Data Structures

```
┌─────────────────────┬────────────────────────────────────────────────────────────────────────┐
│    Data Structure   │                              Characteristics                           │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Vector              │ 1-dimensional, homogeneous data type (numeric, character, logical).    │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Factor              │ Categorical variables with fixed levels (e.g., Credit Rating A/B/C).   │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ List                │ 1-dimensional, heterogeneous: can hold vectors, matrices, models.      │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Data Frame / Tibble │ 2-dimensional tabular structure; columns can have different data types.│
└─────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

```r
# Vector creation
monthly_revenue <- c(120.5, 145.2, 138.0, 162.8)

# Factor creation
customer_tier <- factor(c("Tier 1", "Tier 2", "Tier 1", "Tier 3"), 
                        levels = c("Tier 1", "Tier 2", "Tier 3"))

# Data Frame creation
df_portco <- data.frame(
  customer_id = 101:104,
  revenue = monthly_revenue,
  tier = customer_tier,
  stringsAsFactors = FALSE
)
```

---

## 2. The Tidyverse Data Manipulation Workflow

The **Tidyverse** is an opinionated collection of R packages designed for data science. Data analysts rely on the pipe operator (`%>%` or native `|>`) to chain readable transformations:

```r
library(tidyverse)

# End-to-End Portco Sales Analysis Pipeline
sales_summary <- df_transactions %>%
  # 1. Filter for completed 2025 transactions
  filter(status == "Completed", transaction_year == 2025) %>%
  
  # 2. Add derived column for Net Margin
  mutate(net_margin = gross_revenue - cogs - discount_amount) %>%
  
  # 3. Group by Product Category and Region
  group_by(product_category, sales_region) %>%
  
  # 4. Compute aggregate metrics
  summarise(
    total_revenue = sum(gross_revenue, na.rm = TRUE),
    total_margin = sum(net_margin, na.rm = TRUE),
    margin_pct = (sum(net_margin, na.rm = TRUE) / sum(gross_revenue, na.rm = TRUE)) * 100,
    customer_count = n_distinct(customer_id),
    .groups = "drop"
  ) %>%
  
  # 5. Sort by descending margin percentage
  arrange(desc(margin_pct))
```

### 2.1 Reshaping Data with `tidyr`
- `pivot_longer()`: Converts wide tables (e.g., columns `Jan`, `Feb`, `Mar`) to long format (`Month`, `Revenue`).
- `pivot_wider()`: Converts long rows to wide matrix format.

```r
# Converting wide monthly financial forecast into normalized time-series
long_forecast <- wide_pnl %>%
  pivot_longer(
    cols = starts_with("M_"),
    names_to = "forecast_month",
    names_prefix = "M_",
    values_to = "amount_usd"
  )
```

---

## 3. Visualization with `ggplot2` (Grammar of Graphics)

`ggplot2` builds visualizations layer by layer: Data $\rightarrow$ Aesthetic Mapping (`aes`) $\rightarrow$ Geometric Layers (`geom`) $\rightarrow$ Facets $\rightarrow$ Themes.

```r
library(ggplot2)

# Executive Scatter Plot: Margin % vs Customer Spend with Regression Line
ggplot(df_customers, aes(x = annual_spend_k, y = gross_margin_pct, color = segment)) +
  geom_point(alpha = 0.7, size = 3) +
  geom_smooth(method = "lm", se = FALSE, color = "black", linetype = "dashed") +
  scale_y_continuous(labels = scales::percent_format(scale = 1)) +
  labs(
    title = "Customer Profitability Dispersion by Segment",
    subtitle = "Private Equity Portco Commercial Portfolio Audit",
    x = "Annual Customer Spend ($000s)",
    y = "Gross Margin (%)",
    color = "Customer Segment"
  ) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")
```

---

## 4. Python vs. R Syntax Rosetta Stone

For candidates proficient in Python/Pandas, this side-by-side reference allows immediate translation of analytical concepts:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Operation                │          Python (Pandas)        │            R (dplyr)            │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Filter rows                     │ df[df['rev'] > 100]             │ df %>% filter(rev > 100)        │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Select columns                  │ df[['cust_id', 'rev']]          │ df %>% select(cust_id, rev)     │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Create new column               │ df['margin'] = df['rev'] - cost │ df %>% mutate(margin = rev-cost)│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Sort / Order by                 │ df.sort_values('rev', asc=False)│ df %>% arrange(desc(rev))       │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ GroupBy Aggregation             │ df.groupby('cat')['rev'].sum()  │ df %>% group_by(cat) %>%        │
│                                 │                                 │        summarise(sum(rev))      │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Drop duplicates                 │ df.drop_duplicates()            │ df %>% distinct()               │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Missing value handling          │ df['col'].fillna(0)             │ df %>% replace_na(list(col=0))  │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Linear Regression               │ smf.ols('y ~ x1 + x2', df).fit()│ lm(y ~ x1 + x2, data = df)      │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```


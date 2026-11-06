# Module 06: R Programming for Commercial Biopharma Analytics

> **Document Status**: High-Yield Applied Language Guide `[TIER 4 / R CORE TEAM & CRAN STANDARDS]`  
> **Core Focus**: Base R Fundamentals, Tidyverse (`dplyr`, `tidyr`, `ggplot2`), Statistical Modeling, and Python-to-R Syntax Rosetta Stone  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. R Language Architecture & Base Fundamentals

In pharmaceutical biostatistics and commercial analytics, **R** remains a dominant language alongside SAS and Python due to its comprehensive statistical packages, CRAN audit rigor, and native data manipulation grammar.

### 1.1 Data Structures in R
* **Vector**: 1D atomic array of homogenous types (`numeric`, `integer`, `character`, `logical`, `factor`):
  ```r
  trx_counts <- c(45, 120, 89, 210, 15)
  specialties <- factor(c("Cardiology", "Oncology", "Cardiology", "Neurology", "Oncology"))
  ```
* **Data Frame**: 2D tabular structure where columns can have different data types (equivalent to Pandas DataFrame):
  ```r
  hcp_data <- data.frame(
    npi = c("1001", "1002", "1003"),
    brand_trx = c(45, 120, 89),
    details = c(4, 12, 8),
    stringsAsFactors = FALSE
  )
  ```
* **List**: Heterogeneous collection of arbitrary objects (can store data frames, regression models, and vectors simultaneously):
  ```r
  model_output <- list(
    dataset_name = "Q3_Oncology_Launch",
    sample_size = 500,
    linear_fit = lm(brand_trx ~ details, data = hcp_data)
  )
  ```

---

## 2. The Tidyverse Ecosystem: `dplyr` & `tidyr`

The **Tidyverse** is the standard collection of R packages designed for data science, unified by the tidy data philosophy and the pipe operator (`%>%` or native R 4.0+ pipe `|>`).

```r
library(dplyr)
library(tidyr)

# Sample commercial data pipeline: Grouping, summarizing, and filtering
territory_summary <- hcp_data %>%
  # 1. Filter high-volume prescribers
  filter(brand_trx >= 20) %>%
  # 2. Add market share column
  mutate(market_share = brand_trx / (brand_trx + 150)) %>%
  # 3. Group by Specialty
  group_by(specialty) %>%
  # 4. Compute aggregate metrics
  summarise(
    total_physicians = n(),
    mean_brand_trx = mean(brand_trx, na.rm = TRUE),
    total_details = sum(details, na.rm = TRUE),
    weighted_share = sum(brand_trx) / sum(brand_trx + 150)
  ) %>%
  # 5. Order descending by market share
  arrange(desc(weighted_share))
```

### 2.1 Reshaping Data with `tidyr`: Long vs Wide
* **`pivot_longer()`**: Converting wide promotional tables (columns for each month) into tidy long format (essential for time-series modeling):
  ```r
  # From: NPI | Jan_Spend | Feb_Spend | Mar_Spend
  # To:   NPI | Month     | Spend
  long_promo <- wide_promo %>%
    pivot_longer(
      cols = starts_with("Spend_"),
      names_to = "Month",
      values_to = "Promotional_Spend"
    )
  ```
* **`pivot_wider()`**: Unstacking categories into distinct feature columns.

---

## 3. Data Visualization with `ggplot2` (Grammar of Graphics)

`ggplot2` builds plots layer-by-layer: Data $\to$ Aesthetics (`aes`) $\to$ Geometric objects (`geom`) $\to$ Scales $\to$ Facets $\to$ Themes.

```r
library(ggplot2)

# High-impact commercial chart: Detailing vs TRx with Loess saturation curve
ggplot(hcp_data, aes(x = details, y = brand_trx, color = specialty)) +
  geom_point(alpha = 0.6, size = 2.5) +
  geom_smooth(method = "loess", se = TRUE, color = "black", linetype = "dashed") +
  scale_y_continuous(labels = scales::comma) +
  facet_wrap(~ specialty) +
  labs(
    title = "Physician Prescribing Response to Field Detailing by Specialty",
    subtitle = "IQVIA Simulated Brand Launch Audit (Weeks 1–52)",
    x = "Field Sales Detailing Visits",
    y = "Total Brand Prescriptions (TRx)",
    color = "Physician Specialty"
  ) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom")
```

---

## 4. Statistical & Econometric Modeling in R

### 4.1 Linear Regression: `lm()`
```r
# Multi-variable promotional response regression
fit_ols <- lm(brand_trx ~ detailing_spend + digital_spend + conference_spend, data = brand_df)

# Output detailed summary table
summary(fit_ols)

# Extract coefficients, R-squared, and p-values
r_sq <- summary(fit_ols)$r.squared
p_vals <- summary(fit_ols)$coefficients[, 4]

# Four classical diagnostic plots (Residuals vs Fitted, Normal Q-Q, Scale-Location, Cook's Distance)
par(mfrow = c(2, 2))
plot(fit_ols)
```

### 4.2 Logistic Regression for Physician Conversion: `glm()`
```r
# Binary conversion: Converted (1) vs Non-Converted (0)
fit_logit <- glm(
  converted ~ detail_calls + digital_impressions + peer_influence_score,
  data = hcp_df,
  family = binomial(link = "logit")
)

# Exponentiate coefficients to obtain Odds Ratios (OR) and 95% Confidence Intervals
odds_ratios <- exp(coef(fit_logit))
conf_intervals <- exp(confint(fit_logit))
cbind(Odds_Ratio = odds_ratios, conf_intervals)
```

---

## 5. Python vs R: Commercial Analytics Syntax Rosetta Stone

| Data Science Operation | Python (Pandas / Scikit-learn) | R (Tidyverse / Base R) |
| :--- | :--- | :--- |
| **Read CSV File** | `df = pd.read_csv("data.csv")` | `df <- readr::read_csv("data.csv")` |
| **Inspect First 5 Rows** | `df.head()` | `head(df)` |
| **Data Types & Structure** | `df.info()` | `str(df)` or `glimpse(df)` |
| **Filter Rows** | `df[df['trx'] > 50]` | `df %>% filter(trx > 50)` |
| **Select Columns** | `df[['npi', 'specialty']]` | `df %>% select(npi, specialty)` |
| **Create New Column** | `df['share'] = df['trx'] / df['total']` | `df %>% mutate(share = trx / total)` |
| **GroupBy & Aggregation** | `df.groupby('region')['trx'].sum()` | `df %>% group_by(region) %>% summarise(s = sum(trx))` |
| **Sort / Arrange** | `df.sort_values(by='trx', ascending=False)`| `df %>% arrange(desc(trx))` |
| **Inner Join** | `pd.merge(df1, df2, on='id', how='inner')` | `inner_join(df1, df2, by = "id")` |
| **Missing Value Imputation**| `df['trx'].fillna(df['trx'].median())` | `df$trx[is.na(df$trx)] <- median(df$trx, na.rm=TRUE)` |
| **Linear Regression** | `sm.OLS(y, sm.add_constant(X)).fit()` | `lm(y ~ x1 + x2, data = df)` |
| **Logistic Regression** | `sm.Logit(y, X).fit()` | `glm(y ~ x1 + x2, family = binomial, data = df)` |

---

## 6. Interview Grilling: R vs Python in Healthcare Analytics

* **Question**: *"In commercial pharma analytics, when would you choose R over Python, and vice versa?"*
* **Candidate Answer**:
  > *"Python is superior for end-to-end production engineering, large-scale distributed data pipelines, deep learning, and building interactive web APIs. However, R is unmatched in pure exploratory statistical analysis, clinical trial biostatistics, and publication-ready visualization with `ggplot2`.*
  > 
  > *In commercial analytics at IQVIA, R is frequently preferred when conducting formal econometric hypothesis testing, complex ANOVA models, and specialized survival analyses or non-linear mixed-effects models because R packages (like `lme4`, `brms`, and `survival`) provide immediate, mathematically validated outputs with comprehensive diagnostic tables that require substantial manual boilerplate in Python."*


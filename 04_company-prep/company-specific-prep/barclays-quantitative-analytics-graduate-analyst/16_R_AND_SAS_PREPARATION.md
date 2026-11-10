# 16 — SAS & R for Risk Quantitative Analytics

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Legacy Banking Infrastructure

While modern data science initiatives gravitate toward Python and SQL, the foundational backbone of global banking quantitative infrastructure remains anchored in **Base SAS** and **R**. Over four decades of Basel capital models, regulatory stress testing submissions to the Bank of England (PRA) and US Federal Reserve, and legacy credit scorecards exist within millions of lines of SAS and R code.

In Barclays Risk QA, an analyst must not only build new tools in Python, but must possess the quantitative fluency to **read, audit, back-test, and migrate legacy SAS and R models**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Institutional Technology Positioning                            │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Base SAS & Macro Facility     │ R & Bioconductor / CRAN        │ Python & PyData Stack │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Production backbone for     │ • Preferred by academic quants │ • Modern monitoring   │
│   Basel A-IRB & IFRS 9        │   and econometricians.         │   automation & ML.    │
│   regulatory submissions.     │ • Advanced survival analysis   │ • XGBoost, LightGBM,  │
│ • Highly optimized for disk-  │   and macro time-series.       │   SHAP explainability.│
│   based large datasets.       │ • Packages: `pROC`, `tseries`, │ • Fast API deployment │
│ • Regulators (Fed/PRA) trust  │   `forecast`, `vars`, `glm`.   │   and cloud compute.  │
│   deterministic SAS outputs.  │                                │                       │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Base SAS for Credit Risk Modeling

#### 1.1 The SAS Execution Mechanism: Program Data Vector (PDV)
To debug legacy SAS pipelines, an analyst must understand how SAS processes data. Unlike Python (which loads entire DataFrames into RAM), SAS executes in a two-phase architecture:
1. **Compilation Phase:** Creates the descriptor portion of the dataset and establishes the **Program Data Vector (PDV)** — a memory area containing all variables.
2. **Execution Phase:** Reads the raw data row-by-row into the PDV, performs calculations, outputs to the dataset, and automatically resets non-retained variables to missing.

> **Critical SAS Trap in Credit Risk:**  
> In SAS, a missing numerical value is represented as a period (`.`), which is evaluated mathematically as **negative infinity** ($-\infty$). If a legacy script executes `IF debt_to_income < 0.30 THEN risk_tier = 'Low';`, any account with a missing DTI will be categorized as "Low Risk"! Risk QA quants must inspect legacy scripts for explicit missing value handling: `IF . < debt_to_income < 0.30 THEN ...`.

---

#### 1.2 Core SAS Procedures in Risk Modeling

##### PROC LOGISTIC: Fitting Credit Scorecards & Scoring
```sas
/* ============================================================================
   SAS Scorecard Modeling & ROC Generation
   ============================================================================ */

/* Fit logistic regression model on binary default indicator */
PROC LOGISTIC DATA=work.credit_development DESCENDING
              PLOTS(ONLY)=(ROC(ID=PROB) EFFECT);
    MODEL defaulted_12m = debt_to_income 
                          bureau_score 
                          delinquency_count 
                          utilization_pct
          / SELECTION=STEPWISE 
            SLENTRY=0.05 
            SLSTAY=0.05 
            LACKFIT   /* Generates Hosmer-Lemeshow Goodness-of-Fit */
            OUTROC=work.roc_curve_data;
            
    /* Score a new out-of-time monitoring cohort */
    SCORE DATA=work.monitoring_2024_q2 
          OUT=work.monitoring_scored 
          PRIOREVENT=0.025; /* Empirical bad rate adjustment */
RUN;
```

##### PROC MEANS & PROC FREQ: Decile Decoupling & Goodness-of-Fit
```sas
/* Compute decile summary and bad rates */
PROC MEANS DATA=work.monitoring_scored N SUM MEAN MIN MAX NOPRINT;
    CLASS score_decile;
    VAR defaulted_12m predicted_pd;
    OUTPUT OUT=work.decile_summary
           N=total_accounts
           SUM(defaulted_12m)=bads
           MEAN(defaulted_12m)=observed_bad_rate
           MEAN(predicted_pd)=mean_expected_pd;
RUN;
```

---

#### 1.3 SAS Macro for Automated Population Stability Index (PSI)

```sas
/* ============================================================================
   SAS Macro: Automated Calculation of Population Stability Index (PSI)
   ============================================================================ */
%MACRO calculate_psi(dev_ds=, curr_ds=, score_var=, n_bins=10, out_psi=);

    /* 1. Calculate Quantile Cutoffs on Baseline Development Dataset */
    PROC RANK DATA=&dev_ds. OUT=dev_ranked GROUPS=&n_bins.;
        VAR &score_var.;
        RANKS score_bin;
    RUN;

    PROC MEANS DATA=dev_ranked NOPRINT;
        CLASS score_bin;
        VAR &score_var.;
        OUTPUT OUT=bin_cutoffs MAX=max_cutoff;
    RUN;

    /* 2. Aggregate Expected Counts from Baseline */
    PROC FREQ DATA=dev_ranked NOPRINT;
        TABLE score_bin / OUT=exp_freq(RENAME=(COUNT=exp_count PERCENT=exp_pct));
    RUN;

    /* 3. Assign Monitoring Cohort to Same Bins & Aggregate */
    PROC SQL;
        CREATE TABLE curr_binned AS
        SELECT c.*, b.score_bin
        FROM &curr_ds. c
        LEFT JOIN bin_cutoffs b
        ON c.&score_var. <= b.max_cutoff;
    QUIT;

    PROC FREQ DATA=curr_binned NOPRINT;
        TABLE score_bin / OUT=act_freq(RENAME=(COUNT=act_count PERCENT=act_pct));
    RUN;

    /* 4. Merge and Compute Symmetrized KL Divergence Contribution */
    DATA &out_psi.;
        MERGE exp_freq(IN=a) act_freq(IN=b);
        BY score_bin;
        IF a AND b;
        
        /* Proportions in [0, 1] with epsilon smoothing */
        e_p = MAX(exp_pct / 100.0, 1E-6);
        a_p = MAX(act_pct / 100.0, 1E-6);
        
        diff = a_p - e_p;
        ln_ratio = LOG(a_p / e_p);
        psi_contribution = diff * ln_ratio;
    RUN;

    /* 5. Summarize Total PSI */
    PROC MEANS DATA=&out_psi. SUM NOPRINT;
        VAR psi_contribution;
        OUTPUT OUT=final_psi SUM=total_psi;
    RUN;

    DATA _NULL_;
        SET final_psi;
        PUT "==========================================================";
        PUT " BARCLAYS RISK QA: TOTAL POPULATION STABILITY INDEX (PSI)";
        PUT " TOTAL PSI: " total_psi 8.4;
        IF total_psi < 0.10 THEN PUT " STATUS   : GREEN (STABLE)";
        ELSE IF total_psi < 0.25 THEN PUT " STATUS   : AMBER (MODERATE SHIFT)";
        ELSE PUT " STATUS   : RED (SIGNIFICANT POPULATION BREACH)";
        PUT "==========================================================";
    RUN;

%MEND calculate_psi;
```

---

### 2. R for Credit Risk Analytics & Econometrics

In Risk QA, R is widely utilized for econometric satellite time-series modeling (macro regressions for CCAR and PRA stress tests) and advanced survival analysis.

#### 2.1 Complete R Script: Discrimination & Hosmer-Lemeshow Test
```r
# ==============================================================================
# Barclays Risk QA: Credit Risk Model Monitoring in R
# Libraries: pROC, ResourceSelection, dplyr
# ==============================================================================

suppressPackageStartupMessages({
  library(pROC)
  library(ResourceSelection)
  library(dplyr)
})

evaluate_credit_model_r <- function(y_true, y_prob, n_bins = 10) {
  
  # 1. Discrimination Metrics via pROC
  roc_obj <- roc(response = y_true, predictor = y_prob, quiet = TRUE)
  auc_val <- as.numeric(auc(roc_obj))
  gini_val <- 2 * auc_val - 1
  
  # 2. Kolmogorov-Smirnov (KS) Statistic
  df <- data.frame(actual = y_true, pred = y_prob) %>%
    arrange(desc(pred)) %>%
    mutate(decile = ntile(desc(pred), n_bins))
  
  ks_table <- df %>%
    group_by(decile) %>%
    summarise(
      total = n(),
      bads = sum(actual),
      goods = total - bads,
      .groups = "drop"
    ) %>%
    mutate(
      cum_bad = cumsum(bads) / sum(bads),
      cum_good = cumsum(goods) / sum(goods),
      ks_distance = abs(cum_bad - cum_good) * 100
    )
  
  max_ks <- max(ks_table$ks_distance)
  
  # 3. Hosmer-Lemeshow Goodness-of-Fit Test
  hl_test <- hoslem.test(x = y_true, y = y_prob, g = n_bins)
  
  # 4. Traffic Light Summary
  traffic_light <- if (gini_val >= 0.50 && max_ks >= 35.0) {
    "GREEN"
  } else if (gini_val >= 0.35 && max_ks >= 25.0) {
    "AMBER"
  } else {
    "RED"
  }
  
  cat("\n=======================================================\n")
  cat("           BARCLAYS RISK QA: R METRICS REPORT          \n")
  cat("=======================================================\n")
  cat(sprintf("ROC-AUC          : %.4f\n", auc_val))
  cat(sprintf("Gini Coefficient : %.4f (Status: %s)\n", gini_val, traffic_light))
  cat(sprintf("Maximum KS Stat  : %.2f%%\n", max_ks))
  cat(sprintf("HL Chi-Square    : %.4f (p-value: %.4f)\n", hl_test$statistic, hl_test$p.value))
  cat("=======================================================\n")
  
  return(list(
    auc = auc_val,
    gini = gini_val,
    ks = max_ks,
    hl_stat = hl_test$statistic,
    hl_pval = hl_test$p.value,
    traffic_light = traffic_light
  ))
}
```

---

### 3. Quantitative "Rosetta Stone": SAS vs. R vs. Python

This reference matrix enables seamless translation across institutional programming languages:

```
┌──────────────────────────┬──────────────────────────┬──────────────────────────┬──────────────────────────┐
│ Operation                │ Base SAS                 │ R (Tidyverse)            │ Python (Pandas/Scikit)   │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Filter Rows              │ `DATA out; SET in;`      │ `df %>%`                 │ `df[df['col'] > 0]`      │
│                          │ `WHERE col > 0; RUN;`    │ `  filter(col > 0)`      │                          │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Grouped Aggregation      │ `PROC MEANS DATA=in;`    │ `df %>% group_by(cat) %>%`│ `df.groupby('cat').agg(` │
│                          │ `  CLASS cat; VAR val;`  │ `  summarise(m = mean(v))`│ `  {'val': 'mean'})`     │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Fit Logistic Regression  │ `PROC LOGISTIC DATA=in;` │ `glm(y ~ x, data = df,`  │ `sm.Logit(y, X).fit()`   │
│                          │ `  MODEL y = x; RUN;`    │ `  family = binomial)`   │ `LogisticRegression()`   │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Calculate ROC-AUC        │ `PROC LOGISTIC ...`      │ `pROC::roc(y, p)$auc`    │ `roc_auc_score(y, p)`    │
│                          │ `  ROC; RUN;`            │                          │                          │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Table Join               │ `PROC SQL; SELECT * FROM`│ `left_join(df1, df2,`    │ `pd.merge(df1, df2,`     │
│                          │ `a LEFT JOIN b ON ...;`  │ `  by = "id")`           │ `  on='id', how='left')` │
├──────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────────────┤
│ Handle Missing Values    │ `IF missing_val = .`     │ `is.na(x)`               │ `df['col'].isna()`       │
│                          │ *(Caution: . is -Inf!)*  │                          │                          │
└──────────────────────────┴──────────────────────────┴──────────────────────────┴──────────────────────────┘
```

---

### 4. Technical Interview Questions on SAS & R Migration

**Q1: What is the primary operational danger when migrating a legacy credit scorecard from SAS to Python?**  
*Answer:*  
"The primary danger lies in **missing value semantics and tie-breaking algorithms**. In SAS, numeric missing values (`.`) evaluate as the lowest possible negative number ($-\infty$), whereas in Python (`pandas`/`numpy`), missing values (`np.nan`) fail inequality comparisons (e.g., `NaN > 5` is `False`, but `NaN < 5` is also `False`). If a legacy SAS model had rule logic dependent on missing values falling into lower numerical buckets, a direct Python rewrite will silently misclassify accounts. Additionally, SAS and Python break quantile rank ties differently (`PROC RANK` default vs. Pandas `rank(method='first')`), which can cause subtle discrepancies in decile cutoffs and PSI outputs."

**Q2: When auditing a macro satellite regression in R, how do you verify that the model is not estimating spurious relationships?**  
*Answer:*  
"I first test both the dependent default rate and the macroeconomic explanatory variables for stationarity using the Augmented Dickey-Fuller (`adf.test()`) and KPSS tests. If variables are integrated of order 1 ($I(1)$), running an OLS regression directly yields spurious correlation ($R^2 \approx 1$ with invalid $t$-statistics). I verify whether the variables are cointegrated using the Johansen cointegration test or Engle-Granger two-step procedure. If not cointegrated, all variables must be differenced to $\Delta Y_t$ and $\Delta X_t$ before fitting an Autoregressive Distributed Lag (ADL) or Vector Autoregression (VAR) model."

---

*Authoritative cross-reference: SAS Institute Inc. SAS/STAT 15.1 User's Guide (PROC LOGISTIC); Wickham, H., & Grolemund, G. (2017), "R for Data Science"; BCBS Working Paper 14.*


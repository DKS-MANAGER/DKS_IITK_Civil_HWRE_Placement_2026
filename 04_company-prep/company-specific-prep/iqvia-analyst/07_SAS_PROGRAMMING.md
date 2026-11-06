# Module 07: SAS Programming for Pharmaceutical Commercial Analytics

> **Document Status**: Production-Grade Applied Reference `[TIER 2 / OFFICIAL SAS DOCUMENTATION & FDA CDISC STANDARDS]`  
> **Core Focus**: SAS Environment, DATA Step Execution (PDV), Essential PROCs, PROC SQL, Statistical Procedures, and Pharma Macro Automation  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Why SAS Dominates Life Sciences & Commercial Healthcare

While technology tech firms rely heavily on open-source Python, **SAS (Statistical Analysis System)** remains entrenched across global biopharma and CROs like IQVIA:
1. **Regulatory Gold Standard**: The US Food and Drug Administration (FDA) and European Medicines Agency (EMA) have historically mandated SAS transport files (`.xpt`) and validated SAS procedures for New Drug Applications (NDAs) and CDISC clinical standards (SDTM, ADaM).
2. **Deterministic Data Integrity**: SAS processes massive multi-terabyte datasets directly on disk without requiring the entire table to reside in RAM, ensuring zero memory-overflow crashes.
3. **Audited Statistical Library**: Every algorithmic routine in SAS is certified, rigorously maintained, and legally backed by SAS Institute, providing legal reproducibility.

> [!NOTE]
> **Candidate Strategic Positioning**: Because civil engineering laboratories rarely carry enterprise SAS licenses, the candidate's strategy is to demonstrate **flawless theoretical mastery of the DATA step execution model, exact syntax familiarity with core PROCs, and the ability to translate Python/SQL logic into SAS code immediately**. Candidates can practice on the free cloud-based **SAS OnDemand for Academics (ODA)**.

---

## 2. The SAS Architecture: Libraries & The DATA Step Execution Engine

### 2.1 SAS Libraries & Two-Level Dataset Naming
A SAS library is an engine-driven pointer to a physical file directory:
```sas
/* Assigning a permanent library pointer */
libname iqviadata "/data/commercial/analytics/q3";

/* Two-level name: library.dataset (permanent storage) */
data iqviadata.hcp_prescriptions;
   set work.temp_data;
run;

/* Single-level name: defaults to WORK library (temporary; erased on session close) */
data temp_subset;
   set iqviadata.hcp_prescriptions;
run;
```

### 2.2 The Program Data Vector (PDV) Execution Cycle
Understanding the PDV separates junior syntax memorizers from genuine programmers:
1. **Compilation Phase**:
   * Reads descriptor portion of input dataset.
   * Creates the **Program Data Vector (PDV)**: a logical memory buffer containing all dataset variables plus two automatic system variables:
     * `_N_`: Current iteration count of the DATA step (starts at 1).
     * `_ERROR_`: Binary flag (0 = normal, 1 = data/syntax error).
2. **Execution Phase**:
   * Initializes PDV variables to missing (`.` for numeric, `' '` for character).
   * Reads a single observation into the PDV.
   * Executes programmatic statements sequentially.
   * Writes the PDV contents to the output dataset at the `run;` statement.
   * Clears the PDV and loops back to process the next row until End-Of-File (EOF).

---

## 3. High-Frequency Commercial Data Procedures

### 3.1 Importing, Sorting & De-duplicating
```sas
/* 1. Import CSV Data into SAS */
proc import datafile="/data/commercial/raw_prescriptions.csv"
   out=work.raw_trx
   dbms=csv
   replace;
   getnames=yes;
run;

/* 2. Sort by Prescriber ID and Eliminate Exact Duplicates */
proc sort data=work.raw_trx out=work.sorted_trx nodupkey;
   by npi_id week_date;
run;

/* 3. Metadata Inspection */
proc contents data=work.sorted_trx;
run;
```

### 3.2 Summarization & Descriptive Statistics: `PROC MEANS` & `PROC FREQ`
```sas
/* Summary Statistics for TRx volume grouped by Physician Specialty */
proc means data=work.sorted_trx n mean std median min max q1 q3;
   class specialty;
   var brand_trx competitor_trx;
   output out=work.specialty_summary 
          mean=mean_brand mean_comp 
          sum=sum_brand sum_comp;
run;

/* Cross-Tabulation & Chi-Square Test of Specialty vs Brand Adoption */
proc freq data=work.sorted_trx;
   tables specialty * adopted_status / chisq relrisk;
run;
```

---

## 4. `PROC SQL`: Relational Database Power Inside SAS

In commercial delivery at IQVIA, `PROC SQL` is heavily favored because analysts with SQL backgrounds can perform complex joins and aggregations without complex DATA step merges:

```sas
proc sql;
   create table work.hcp_performance as
   select 
      h.npi_id,
      h.physician_name,
      h.specialty,
      h.territory_id,
      sum(p.brand_trx) as total_brand_trx,
      sum(p.market_trx) as total_market_trx,
      calculated total_brand_trx / calculated total_market_trx as brand_market_share format=percent8.2,
      count(distinct d.call_id) as total_rep_details
   from work.hcp_master as h
   left join work.prescriptions as p
      on h.npi_id = p.npi_id
   left join work.detailing_logs as d
      on h.npi_id = d.npi_id and d.call_date between '01JAN2025'd and '30JUN2025'd
   group by h.npi_id, h.physician_name, h.specialty, h.territory_id
   having calculated total_brand_trx > 50
   order by calculated total_brand_trx desc;
quit;
```

---

## 5. Statistical Modeling in SAS: `PROC REG` & `PROC LOGISTIC`

### 5.1 Econometric Linear Regression with Diagnostics: `PROC REG`
```sas
/* Marketing Mix Model in SAS with VIF and Durbin-Watson diagnostics */
proc reg data=work.brand_weekly_sales;
   model trx_sales = detail_spend digital_spend conference_spend sample_volume
         / vif collin dw influence;
   output out=work.model_residuals 
          p=predicted_sales 
          r=residual;
run;
quit;
```

### 5.2 Physician Adoption Logistic Regression: `PROC LOGISTIC`
```sas
/* Modeling Physician Adoption Probability with Odds Ratios and ROC Area */
proc logistic data=work.hcp_profiling descending;
   class specialty (ref="General Practice") region / param=ref;
   model adopted_flag = specialty region detailing_calls peer_influence_score
         / rsq lackfit ctable;
   oddsratio detailing_calls / unit=5; /* Odds change for every 5 additional rep calls */
run;
```

---

## 6. DATA Step Merging: `WHERE` vs `IF` & Merge Logic

### 6.1 The Critical Distinction: `WHERE` vs Subsetting `IF`
* **`WHERE` Statement**: Filters records **before** they enter the Program Data Vector (PDV). Highly CPU and I/O efficient because non-matching rows are never loaded into memory. Can only evaluate variables that already exist in the input dataset.
* **Subsetting `IF` Statement**: Evaluates variables **inside** the PDV during execution. Required when filtering on calculated or dynamically created variables.

```sas
data work.high_tier_oncology;
   set work.hcp_master;
   where specialty = 'Oncology'; /* Pre-PDV filtering */
   
   total_activity = rep_calls + email_clicks;
   if total_activity >= 10;      /* Post-PDV filtering on dynamically calculated var */
run;
```

### 6.2 Match-Merging with `IN=` Variables
```sas
/* Inner Join / Match-Merge using Data Step */
data work.matched_hcp;
   merge work.hcp_roster (in=in_roster)
         work.hcp_claims (in=in_claims);
   by npi_id;
   
   /* Perform Inner Join: Keep only records present in both datasets */
   if in_roster and in_claims;
run;
```

---

## 7. SAS Macro Facility for Automated Deliverables

In commercial delivery, analysts automate recurring weekly or monthly client reports across 50 US states using SAS macros:

```sas
/* Macro definition to generate monthly performance summary by therapeutic area */
%macro generate_monthly_report(therapeutic_area=, year=2025);

   %put NOTE: Starting automated commercial audit for &therapeutic_area in &year;

   data work.subset_&therapeutic_area;
      set work.national_sales;
      where therapeutic_class = "&therapeutic_area" and year(sales_date) = &year;
   run;

   proc means data=work.subset_&therapeutic_area noprint;
      class month;
      var brand_trx revenue;
      output out=work.out_&therapeutic_area sum=sum_trx sum_revenue;
   run;

   proc print data=work.out_&therapeutic_area;
      title "Monthly Sales Audit: &therapeutic_area (&year)";
   run;

%mend generate_monthly_report;

/* Executing the macro across multiple brands */
%generate_monthly_report(therapeutic_area=Oncology, year=2025);
%generate_monthly_report(therapeutic_area=Cardiology, year=2025);
```


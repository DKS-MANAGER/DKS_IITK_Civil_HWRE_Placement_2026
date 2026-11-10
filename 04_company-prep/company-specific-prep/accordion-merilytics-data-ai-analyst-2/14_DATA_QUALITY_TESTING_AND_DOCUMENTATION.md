# Module 14 — Data Quality, Testing & Technical Documentation

The Accordion (Merilytics) job description explicitly mandates: **"Perform testing and documentation. Own the accuracy of analytical deliverables."** 

In Private Equity financial consulting, an undetected data error or broken reconciliation tie-out can lead to a multi-million-dollar valuation error during M&A due diligence, destroying firm credibility. Data quality control is a non-negotiable core discipline.

---

## 1. The Six Dimensions of Data Quality

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE 6 DATA QUALITY PILLARS                                │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│     Dimension      │            Definition             │       Verification Test       │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 1. Accuracy        │ Data correctly reflects real-     │ Reconcile transaction totals  │
│                    │ world financial transactions.     │ against audited general ledger│
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 2. Completeness    │ No critical fields or historical  │ Check for NULL foreign keys or│
│                    │ calendar periods are missing.     │ missing months in time-series.│
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 3. Consistency     │ Data values match across disparate│ Verify customer IDs tie across│
│                    │ systems (CRM vs. ERP vs. Billing).│ Salesforce and NetSuite.      │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 4. Timeliness      │ Data represents the current state │ Check ingestion timestamp and │
│                    │ within expected SLA freshness.    │ max transaction date.         │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 5. Uniqueness      │ Zero duplicate records or         │ Primary key uniqueness test:  │
│                    │ duplicate billing line-items.     │ `COUNT(PK) == COUNT(DISTINCT)`│
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 6. Validity        │ Values conform to domain schemas, │ Range checks (e.g., Margin %  │
│                    │ data types, and allowed ranges.   │ between -100% and +100%).     │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

---

## 2. Automated Quality-Control Testing in Python

Before any analytical dataset is fed into a financial model, executive dashboard, or client presentation, run an automated validation assertion suite:

```python
import pandas as pd
import numpy as np

def run_data_quality_audit(df: pd.DataFrame, primary_key: str) -> dict:
    """Executes comprehensive automated data quality assertions."""
    audit_report = {"status": "PASSED", "failures": []}
    
    # 1. Uniqueness Check
    total_rows = len(df)
    unique_keys = df[primary_key].nunique()
    if total_rows != unique_keys:
        audit_report["status"] = "FAILED"
        audit_report["failures"].append(
            f"Uniqueness violation: {total_rows - unique_keys} duplicate primary keys found."
        )
        
    # 2. Critical NULL Check
    critical_cols = [primary_key, 'order_date', 'customer_id', 'gross_revenue', 'net_revenue']
    for col in critical_cols:
        if col in df.columns:
            null_count = df[col].isnull().sum()
            if null_count > 0:
                audit_report["status"] = "FAILED"
                audit_report["failures"].append(
                    f"Completeness violation: Column '{col}' contains {null_count} NULL values."
                )
                
    # 3. Validity & Domain Invariant Checks
    # Invariant A: Net Revenue must never exceed Gross Revenue
    if (df['net_revenue'] > df['gross_revenue']).any():
        audit_report["status"] = "FAILED"
        audit_report["failures"].append(
            "Validity violation: Found instances where net_revenue > gross_revenue."
        )
        
    # Invariant B: Negative values where disallowed
    if (df['gross_revenue'] < 0).any():
        audit_report["status"] = "FAILED"
        audit_report["failures"].append(
            "Validity violation: Found negative values in gross_revenue."
        )
        
    # 4. Date Continuity Check
    df_dates = pd.to_datetime(df['order_date']).drop_duplicates().sort_values()
    date_range = pd.date_range(start=df_dates.min(), end=df_dates.max())
    missing_dates = date_range.difference(df_dates)
    if len(missing_dates) > 0:
        audit_report["failures"].append(
            f"Timeliness notice: {len(missing_dates)} calendar days have zero transaction records."
        )
        
    return audit_report
```

---

## 3. The Cross-System Financial Reconciliation Framework ("The Tie-Out")

When working on private equity CFO advisory projects, the ultimate test of data integrity is the **Three-Way Tie-Out**:

```
┌───────────────────────────┐       ┌───────────────────────────┐       ┌───────────────────────────┐
│     Source ERP Extract    │       │ Analytical PowerPivot /   │       │   Audited Financial P&L   │
│   (Raw Transaction Rows)  │◄─────►│       Python Model        │◄─────►│    (General Ledger GL)    │
│    Total: $142,560,820    │       │    Total: $142,560,820    │       │    Total: $142,560,820    │
└───────────────────────────┘       └───────────────────────────┘       └───────────────────────────┘
               ▲                                                                       ▲
               └─────────────────────── RECONCILED (0.00 Variance) ────────────────────┘
```

### 3.1 Resolving Common Reconciliation Variances
1. **Timing Differences**: Revenue recognized upon shipment in ERP vs. upon delivery in billing software.
2. **Returns and Allowances**: Credit memos issued in subsequent fiscal periods without adjusting prior revenue tags.
3. **Currency Conversion Artifacts**: Different daily average exchange rates applied across multi-entity subsidiaries.

---

## 4. Reusable Quality-Control Sign-Off Checklist

Before delivering an Excel model, SQL script, or Power BI dashboard to an Engagement Manager or Client:

- [ ] **Zero Hardcoded Formulas**: All constants are documented in the Assumptions tab.
- [ ] **Row Count Integrity**: Reconciled source row count with transformed output row count; zero unintentional dropped rows.
- [ ] **Balance Sheet Check**: Total Assets minus Total Liabilities and Equity equals exactly \$0.00.
- [ ] **No Circular References**: Status bar verifies `Ready` with no circular reference warnings.
- [ ] **Edge Case Stress Testing**: Model re-computes cleanly when growth rate is set to 0% or -20%.
- [ ] **Data Dictionary Documented**: Every column header has a verified definition, source table, and business owner.
- [ ] **Formatting Cleanliness**: Number formats consistent throughout (`$#,##0` for currency, `0.0%` for percentages), gridlines visible, zoom set to 100%.


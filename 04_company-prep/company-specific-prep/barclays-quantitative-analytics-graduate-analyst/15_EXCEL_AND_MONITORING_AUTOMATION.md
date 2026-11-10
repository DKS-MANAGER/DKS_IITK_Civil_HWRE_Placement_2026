# 15 — Excel Modeling & Monitoring Automation (EUC Governance)

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & End User Computing (EUC) in Banking

While quantitative data pipelines execute within automated Python, SQL, and SAS environments, the primary artifact delivered to executive decision-makers — including the **Model Risk Governance Committee (MRGC)**, Chief Risk Officers, and regulatory examiners — is the **Excel Model Monitoring Pack (MMP)**.

In Tier 1 banking, spreadsheets used for high-impact decision-making are governed under strict **End User Computing (EUC)** and **User Developed Application (UDA)** policies. Spreadsheets must not be casual workbooks; they must function as auditable, hardened financial applications featuring:
1. Complete separation of data ingestion, calculation logic, and presentation dashboards.
2. Dynamic, modern formula architectures (`XLOOKUP`, `INDEX/MATCH`, `SUMIFS`, dynamic arrays) without hardcoded numbers.
3. Automated Red/Amber/Green (RAG) conditional formatting linked to regulatory thresholds.
4. Cell-locking, sheet protection, and change-log version control.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Barclays EUC Compliant Workbook Structure                       │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Data Layer (Protected)        │ Calculation Layer (Hidden/Lock)│ Presentation Layer    │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Sheet: 'Raw_Data_Feed'      │ • Sheet: 'Calc_PSI_Stability'  │ • Sheet: 'Dashboard'  │
│ • Populated automatically via │ • Sheet: 'Calc_Discrimination' │ • Executive KPI Cards │
│   Python / SQL export.        │ • Sheet: 'Calc_Calibration'    │ • Trailing RAG Trends │
│ • Strict schema assertions    │ • Pure mathematical formulas;  │ • Dynamic charts      │
│   (no manual data entry).     │   zero manual overrides.       │ • Committee sign-off  │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Mathematical Formulas in Excel for Model Monitoring

Below are the exact, verified Excel formulas for computing core quantitative monitoring metrics directly within an EUC spreadsheet.

#### 1.1 Population Stability Index (PSI) Formula
Given a 10-decile table where:
- Column C: Expected Proportion ($E_i$, e.g., cell `C10` to `C19`)
- Column E: Actual Proportion ($A_i$, e.g., cell `E10` to `E19`)

**Single-bin contribution formula (e.g., cell `F10`):**
```excel
=(E10 - C10) * LN(IF(E10=0, 0.000001, E10) / IF(C10=0, 0.000001, C10))
```
*Note: The `IF` statement prevents `#NUM!` or `#DIV/0!` errors when actual or expected proportions contain zero counts.*

**Total PSI (cell `F20`):**
```excel
=SUM(F10:F19)
```

**Automated Traffic-Light Status Formula (cell `G20`):**
```excel
=IFS(F20 < 0.10, "GREEN", F20 < 0.25, "AMBER", TRUE, "RED")
```

---

#### 1.2 Discrimination Metrics: KS Statistic, AUC & Gini

Given a 10-decile scorecard discrimination table where:
- Column D: Cumulative Bad % ($F_{\text{bad}}$, cells `D10:D19`)
- Column F: Cumulative Good % ($F_{\text{good}}$, cells `F10:F19`)

**Decile Absolute Distance (cell `G10` to `G19`):**
```excel
=ABS(D10 - F10)
```

**Kolmogorov-Smirnov (KS) Statistic (cell `G20`):**
```excel
=MAX(G10:G19)
```

**Area Under ROC Curve (Trapezoidal Numerical Integration):**
Let $F_{\text{bad}, 0} = 0$ and $F_{\text{good}, 0} = 0$ at row 9.
Using the trapezoid rule $\sum_{k=1}^{10} \frac{F_{\text{bad}, k} + F_{\text{bad}, k-1}}{2} \times (F_{\text{good}, k} - F_{\text{good}, k-1})$:

In cell `H10` (copied down to `H19`):
```excel
=((D10 + D9) / 2) * (F10 - F9)
```
**Total ROC-AUC (cell `H20`):**
```excel
=SUM(H10:H19)
```

**Gini Coefficient (Somers' D, cell `H21`):**
```excel
=2 * H20 - 1
```

---

#### 1.3 Calibration & Binomial Hypothesis Testing ($Z$-Score)

For a specific internal rating grade (e.g., Rating Grade 4) with:
- Total Accounts ($N_g$): Cell `B12`
- Observed Defaults ($O_g$): Cell `C12`
- Predicted Default Probability ($PD_g$): Cell `D12`

**Expected Defaults ($E_g$, cell `E12`):**
```excel
=B12 * D12
```

**Observed vs. Expected ($O/E$) Ratio (cell `F12`):**
```excel
=C12 / E12
```

**Binomial Standard Error (cell `G12`):**
```excel
=SQRT(B12 * D12 * (1 - D12))
```

**Binomial Normal Approximation $Z$-Score (cell `H12`):**
```excel
=(C12 - E12) / G12
```

**Two-Tailed $p$-Value (cell `I12`):**
```excel
=2 * (1 - NORM.S.DIST(ABS(H12), TRUE))
```

**Rating Grade Traffic-Light Status (cell `J12`):**
```excel
=IFS(ABS(H12) < 1.96, "GREEN", ABS(H12) < 2.58, "AMBER", TRUE, "RED")
```

---

#### 1.4 Hosmer-Lemeshow $\chi^2$ Goodness-of-Fit Test

Across $G = 10$ deciles (cells `B10:E19`):
**Single-Decile $\chi^2$ Contribution (cell `K10`):**
```excel
=((C10 - E10)^2) / (B10 * D10 * (1 - D10))
```

**Total Hosmer-Lemeshow Statistic (cell `K20`):**
```excel
=SUM(K10:K19)
```

**Degrees of Freedom (cell `K21`):**
```excel
=COUNT(B10:B19) - 2
```

**Hosmer-Lemeshow $p$-Value (cell `K22`):**
```excel
=CHISQ.DIST.RT(K20, K21)
```

---

### 2. End User Computing (EUC) Design & Governance Architecture

To comply with **Barclays EUC Policy** and **PRA SS1/23 Principle 5**, an analyst must design templates that resist accidental user error.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 EUC Hardening Checklist                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  [X] Strict Separation: Raw inputs, calculation formulas, and final charts isolated.  │
│  [X] Cell Protection: All formula cells locked and protected with departmental cipher. │
│  [X] Input Validation: Reporting dates and model names governed by dropdown lists.     │
│  [X] Dynamic Lookups: Pure XLOOKUP / INDEX-MATCH; zero hardcoded column index offsets. │
│  [X] Clear Legend: Visual encoding for inputs (yellow), formulas (white), links (gray).│
│  [X] Version Control: Dedicated 'Changelog' tab tracking author, date, and edit scope. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Professional Color-Coding Standard in Risk Analytics:
- **Soft Yellow (`#FFF2CC`)**: Editable User Input / Parameter cell.
- **Pure White (`#FFFFFF`)**: Calculation / Formula cell (Strictly Locked).
- **Muted Blue (`#DDEBF7`)**: Lookups / External data feed link.
- **Dark Navy (`#1F4E78`) / White Text**: Table headers and section banners.
- **Traffic Light RAG Colors**:
  - Green: Soft Green Fill (`#E2EFDA`), Dark Green Text (`#375623`).
  - Amber: Soft Amber Fill (`#FFF2CC`), Dark Amber Text (`#833C0C`).
  - Red: Soft Red Fill (`#FCE4D6`), Dark Red Text (`#C65911`).
  *(Avoid harsh primary neon colors; executive decks require professional, muted palettes).*

---

### 3. Automated Excel Generation via Python (`openpyxl`)

In modern Risk QA operations, manual typing into spreadsheets is eliminated. Python scripts query the data warehouse, compute monitoring statistics, and write results directly into pre-formatted, macro-free Excel workbooks.

```python
"""
Barclays Risk QA: Automated Excel Monitoring Pack Populator
Requires: openpyxl, pandas
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def populate_model_monitoring_excel(
    template_path: str,
    output_path: str,
    metrics_summary: dict,
    decile_df
):
    """
    Loads pre-approved EUC template, populates monitoring metrics,
    applies conditional styling, and locks calculation cells.
    """
    wb = openpyxl.load_workbook(template_path)
    ws_dash = wb['Executive_Dashboard']
    ws_calc = wb['Calc_Discrimination']
    
    # 1. Populate Executive Summary Cards
    ws_dash['C5'] = metrics_summary['model_name']
    ws_dash['C6'] = metrics_summary['reporting_quarter']
    ws_dash['C7'] = metrics_summary['total_accounts']
    
    # Populate Key Metrics
    ws_dash['E5'] = metrics_summary['gini']
    ws_dash['E6'] = metrics_summary['ks_stat']
    ws_dash['E7'] = metrics_summary['psi']
    
    # Apply RAG Styling to Dashboard Status
    status_fill = {
        'GREEN': PatternFill(start_color='E2EFDA', end_color='E2EFDA', fill_type='solid'),
        'AMBER': PatternFill(start_color='FFF2CC', end_color='FFF2CC', fill_type='solid'),
        'RED': PatternFill(start_color='FCE4D6', end_color='FCE4D6', fill_type='solid')
    }
    
    rag_cell = ws_dash['G5']
    rag_cell.value = metrics_summary['overall_status']
    rag_cell.fill = status_fill.get(metrics_summary['overall_status'], status_fill['AMBER'])
    
    # 2. Populate Decile Data Table
    start_row = 10
    for idx, row in decile_df.iterrows():
        r = start_row + idx
        ws_calc[f'A{r}'] = row['decile']
        ws_calc[f'B{r}'] = row['total_accounts']
        ws_calc[f'C{r}'] = row['bads']
        ws_calc[f'D{r}'] = row['goods']
        ws_calc[f'E{r}'] = row['bad_rate']
        ws_calc[f'F{r}'] = row['cum_bad']
        ws_calc[f'G{r}'] = row['cum_good']
        ws_calc[f'H{r}'] = row['ks_distance']
        
    # Save hardened workbook
    wb.save(output_path)
    print(f"[+] Successfully generated executive Excel pack: {output_path}")
```

---

### 4. Interactive Interview Scenario: Defending EUC Integrity

**Interviewer:**  
*"Suppose a business credit risk officer receives your quarterly Model Monitoring Pack and complains that the PSI formula is too sensitive because it triggers an Amber status on a portfolio that appears profitable. How do you defend the model monitoring metric?"*

**Candidate Answer:**  
*"I would explain that profitability and population stability measure fundamentally different dimensions:
1. **Profitability** is a lagging financial outcome driven by macroeconomic margins, fees, and collection efforts over historical balances.
2. **PSI** is a leading indicator of risk shift. If PSI is Amber ($0.10 \le \text{PSI} < 0.25$), the score distribution of newly approved applicants has systematically diverged from the baseline upon which the scorecard was calibrated.
3. Even if current vintage bad rates look stable, an unaddressed population drift means the model's rank-ordering integrity is deteriorating. If left unmonitored, higher-risk borrowers are misclassified into lower risk pricing tiers, creating future credit losses.
4. I would walk the stakeholder through the **Characteristic Stability Index (CSI)** table in the monitoring pack to isolate exactly which features (e.g., Debt-to-Income or Bureau Score) caused the drift, providing actionable evidence for credit policy adjustment rather than an arbitrary debate over the overall PSI metric."*

---

*Authoritative cross-reference: Barclays Enterprise End User Computing (EUC) Standards; Basel Committee on Banking Supervision (BCBS) 239 ("Risk Data Aggregation and Risk Reporting"); Financial Industry Regulatory Authority (FINRA) Spreadsheet Risk Guidance.*


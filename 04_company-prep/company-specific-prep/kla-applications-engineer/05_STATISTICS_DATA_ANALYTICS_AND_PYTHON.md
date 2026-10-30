# Module 05: Statistics, Data Analytics & Scientific Python
## Statistical Testing, Semiconductor Distributions, KLARF File Parsing & Python Workflows

> **Document Status**: Authoritative Technical Syllabus  
> **Relevant Business Units**: Klarity Defect Analytics, Global Customer Operations, Yield Management  
> **Target Role**: Customer Applications Engineer (CAE)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  

---

## 1. Applied Statistics in Semiconductor Process Engineering

In semiconductor fabs, data volume is massive, but finding meaningful signals requires rigorous statistical hypotheses testing.

### 1.1 Probability Distributions in Semiconductor Fabs

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 SEMICONDUCTOR METROLOGY & DEFECT DISTRIBUTIONS              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. NORMAL (GAUSSIAN) DISTRIBUTION                                           │
│    • Applied to: Critical Dimension (CD), thin film thickness, overlay error│
│    • Governing PDF: f(x) = (1 / (σ √(2π))) * exp(-(x - μ)² / (2σ²))         │
│    • Central Limit Theorem ensures that lot-averaged metrology is normal.   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. POISSON DISTRIBUTION                                                     │
│    • Applied to: Random killer defect counts per unit area of silicon.      │
│    • Governing PMF: P(X = k) = (λ^k * exp(-λ)) / k!                         │
│    • Variance equals the mean (Var(X) = E(X) = λ). If Var(X) >> E(X),       │
│      defects exhibit over-dispersion and spatial clustering!                │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. WEIBULL DISTRIBUTION                                                     │
│    • Applied to: Time-Dependent Dielectric Breakdown (TDDB), tool MTBF.     │
│    • CDF: F(t) = 1 - exp(-(t / η)^β)                                        │
│    • Shape factor β < 1 indicates infant mortality; β > 1 indicates wear-out│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 1.2 Hypothesis Testing for Tool-to-Tool Matching

When a fab introduces a new KLA inspection or metrology tool, Applications Engineers must prove that the new tool ("Tool B") matches the legacy tool ("Tool A") without systematic bias.

#### Two-Sample Two-Tailed Student's t-Test for Means:
* **Null Hypothesis ($H_0$)**: $\mu_A = \mu_B$ (No systematic measurement offset between tools).
* **Alternative Hypothesis ($H_1$)**: $\mu_A \ne \mu_B$.
* **Test Statistic (assuming equal variances)**:
  $$t = \frac{\bar{X}_A - \bar{X}_B}{s_p \sqrt{\frac{1}{n_A} + \frac{1}{n_B}}}$$
  Where pooled standard deviation $s_p$ is:
  $$s_p = \sqrt{\frac{(n_A - 1)s_A^2 + (n_B - 1)s_B^2}{n_A + n_B - 2}}$$

#### One-Way Analysis of Variance (ANOVA) for Multi-Chamber Matching:
In a 4-chamber deposition or etch cluster tool, ANOVA tests whether any individual chamber exhibits anomalous film thickness or defect generation:
$$F = \frac{MS_{\text{between}}}{MS_{\text{within}}} = \frac{\frac{SS_{\text{between}}}{k - 1}}{\frac{SS_{\text{within}}}{N - k}}$$
If $p\text{-value} < 0.05$, at least one chamber has drifted and must be recalibrated.

---

## 2. Understanding the KLARF Wafer Defect File Standard

The **KLARF** (KLA Results File) format is the global semiconductor industry standard for recording wafer inspection defect data. KLA tools export KLARF text files containing wafer metadata, die layout coordinates, and tabular defect records.

### 2.1 An Authentic KLARF Text Header & Structure:
```text
FileVersion 1 2;
FileTimestamp 10-24-2026 14:32:05;
InspectionStationID "KLA" "2920" "BPO_TOOL_04";
SampleType WAFER;
ResultTimestamp 10-24-2026 14:31:50;
LotID "LOT_7842B";
WaferID "W08_300MM";
Slot 8;
SampleOrientationMarkType NOTCH;
OrientationMarkLocation DOWN;
DiePitch 14.500 12.200;
WaferCenterDie 12 15;
DefectRecordSpec 9
DEFECTID XREL YREL XINDEX YINDEX XSIZE YSIZE DEFECTAREA ROUGHCLASSCODE;
DefectList
1  4.231  8.112  10  12  0.045  0.042  0.0018  1
2  4.235  8.118  10  12  0.052  0.048  0.0024  1
3  1.102  2.441  14  18  1.240  0.890  1.1036  25
4  9.884  0.332  08  20  0.038  0.035  0.0013  1
SummaryList
1 3
25 1;
EndOfFile;
```

* **Coordinates**:
  * `(XINDEX, YINDEX)`: Die coordinates on the 300 mm wafer grid.
  * `(XREL, YREL)`: Micro-coordinates of the defect relative to the die lower-left origin ($\text{mm}$).
  * `ROUGHCLASSCODE`: Initial coarse classification (e.g., Code 1 = Nuisance particle, Code 25 = Killer metal scratch).

---

## 3. Production-Grade Python KLARF Parser Implementation

A standard interview assessment for KLA Applications Engineers tests the ability to ingest, parse, and analyze raw KLARF files using Python.

```python
"""
KLA Semiconductor Inspection Defect Analysis Suite
Production-grade KLARF File Parser and Spatial Defect Analyzer
"""

import re
import numpy as np
import pandas as pd
from typing import Dict, Tuple, List


class KlarfParser:
    """
    Parses industry-standard KLA Results Format (KLARF) text inspection logs
    into clean pandas DataFrames for spatial analysis and yield modeling.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.metadata: Dict[str, str] = {}
        self.defects_df: pd.DataFrame = pd.DataFrame()

    def parse(self) -> Tuple[Dict[str, str], pd.DataFrame]:
        with open(self.filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        in_defect_list = False
        columns = []
        defect_data: List[List[float]] = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            # Parse Header Metadata
            if stripped.startswith("FileVersion"):
                self.metadata["FileVersion"] = stripped.split()[1]
            elif stripped.startswith("LotID"):
                self.metadata["LotID"] = stripped.split()[1].replace('"', '')
            elif stripped.startswith("WaferID"):
                self.metadata["WaferID"] = stripped.split()[1].replace('"', '')
            elif stripped.startswith("DiePitch"):
                parts = stripped.split()
                self.metadata["DiePitchX"] = float(parts[1])
                self.metadata["DiePitchY"] = float(parts[2].replace(';', ''))

            # Detect Column Specification
            elif stripped.startswith("DefectRecordSpec"):
                continue
            elif "DEFECTID" in stripped and "XREL" in stripped:
                columns = stripped.replace(';', '').split()

            # Detect Start of Defect Data
            elif stripped.startswith("DefectList"):
                in_defect_list = True
                continue

            # Detect End of Defect Data
            elif stripped.startswith("SummaryList") or stripped.startswith("EndOfFile"):
                in_defect_list = False

            # Harvest Defect Rows
            elif in_defect_list:
                clean_row = stripped.replace(';', '').split()
                try:
                    numeric_row = [float(x) for x in clean_row]
                    defect_data.append(numeric_row)
                except ValueError:
                    continue

        if not columns:
            columns = ["DEFECTID", "XREL", "YREL", "XINDEX", "YINDEX", 
                       "XSIZE", "YSIZE", "DEFECTAREA", "ROUGHCLASSCODE"]

        self.defects_df = pd.DataFrame(defect_data, columns=columns)
        if "DEFECTID" in self.defects_df.columns:
            self.defects_df["DEFECTID"] = self.defects_df["DEFECTID"].astype(int)
        if "ROUGHCLASSCODE" in self.defects_df.columns:
            self.defects_df["ROUGHCLASSCODE"] = self.defects_df["ROUGHCLASSCODE"].astype(int)

        return self.metadata, self.defects_df

    def compute_wafer_coordinates(self) -> pd.DataFrame:
        """
        Converts local die coordinates (XREL, YREL) into global wafer millimeter
        coordinates (X_GLOBAL, Y_GLOBAL) for spatial heatmapping.
        """
        pitch_x = float(self.metadata.get("DiePitchX", 10.0))
        pitch_y = float(self.metadata.get("DiePitchY", 10.0))

        df = self.defects_df.copy()
        df["X_GLOBAL"] = (df["XINDEX"] * pitch_x) + df["XREL"]
        df["Y_GLOBAL"] = (df["YINDEX"] * pitch_y) + df["YREL"]
        df["RADIAL_DIST"] = np.sqrt(df["X_GLOBAL"]**2 + df["Y_GLOBAL"]**2)
        return df


# Demonstration Usage
if __name__ == "__main__":
    sample_klarf_content = """FileVersion 1 2;
LotID "L9012";
WaferID "W03";
DiePitch 10.0 10.0;
DefectRecordSpec 9
DEFECTID XREL YREL XINDEX YINDEX XSIZE YSIZE DEFECTAREA ROUGHCLASSCODE;
DefectList
1 2.5 3.1 5 6 0.05 0.04 0.002 1;
2 2.6 3.2 5 6 0.06 0.05 0.003 1;
3 8.1 9.0 -4 2 1.45 1.10 1.595 25;
SummaryList
1 2;
EndOfFile;"""

    import tempfile
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".klarf") as tmp:
        tmp.write(sample_klarf_content)
        tmp_path = tmp.name

    parser = KlarfParser(tmp_path)
    meta, df = parser.parse()
    df_global = parser.compute_wafer_coordinates()
    print("Metadata:", meta)
    print("Processed Defects:\n", df_global[["DEFECTID", "X_GLOBAL", "Y_GLOBAL", "ROUGHCLASSCODE"]])
```

---

## 4. Recipe Sensitivity Tuning & ROC Optimization

A daily task for an Applications Engineer is determining the optimal optical threshold $T$ for a wafer inspection recipe.

```python
"""
ROC Curve & Sensitivity Optimization for KLA Inspection Recipes
Demonstrating Trade-off between True Defect Capture Rate and Nuisance Filter
"""

import numpy as np
from sklearn.metrics import roc_curve, auc


def optimize_recipe_threshold(y_true: np.ndarray, optical_signals: np.ndarray):
    """
    y_true: 1 for killer defects, 0 for nuisance/noise.
    optical_signals: Continuous optical difference intensity (|Test - Ref|).
    """
    fpr, tpr, thresholds = roc_curve(y_true, optical_signals)
    roc_auc = auc(fpr, tpr)

    # Maximize Youden's J statistic = Sensitivity (TPR) - Fall-out (FPR)
    youden_j = tpr - fpr
    optimal_idx = np.argmax(youden_j)
    optimal_threshold = thresholds[optimal_idx]

    return {
        "AUC": roc_auc,
        "Optimal_Threshold": optimal_threshold,
        "Optimal_Capture_Rate": tpr[optimal_idx],
        "Nuisance_Rate": fpr[optimal_idx]
    }
```

* **Interview Key Point**: The ideal recipe does not simply maximize AUC; it must enforce a strict **minimum killer capture constraint** (e.g., $TPR \ge 98\%$), and then find the highest threshold that satisfies this constraint to minimize nuisance count.

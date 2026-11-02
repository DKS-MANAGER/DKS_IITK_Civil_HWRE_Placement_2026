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


---

## 5. Advanced Practical Python & Pandas Exercises for Assessment & Fab Automation

### Exercise 1: Vectorized Spatial Defect Clustering in Pure NumPy
*Objective*: Given an array of $N$ defect coordinates $(X, Y)$ on a 300 mm wafer, cluster adjacent defects within radius $R = 50\text{ }\mu\text{m}$ using vectorized broadcasting rather than slow nested Python loops.

```python
"""
Vectorized Spatial Defect Clustering for Wafer Inspection
Author: KLA Applications Preparation Suite
"""

import numpy as np


def find_defect_clusters_vectorized(coords: np.ndarray, cluster_radius_um: float = 50.0):
    """
    coords: Nx2 numpy array of [X, Y] in micrometers.
    Returns: cluster labels for each defect (-1 for isolated, integer ID for cluster).
    """
    n_points = coords.shape[0]
    # Compute pairwise squared Euclidean distance matrix via broadcasting: (N, 1, 2) - (1, N, 2)
    diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]  # Shape (N, N, 2)
    dist_sq = np.sum(diff ** 2, axis=-1)  # Shape (N, N)

    # Boolean adjacency matrix
    adj_matrix = dist_sq <= (cluster_radius_um ** 2)

    # Connected component labeling using iterative BFS/DFS
    visited = np.zeros(n_points, dtype=bool)
    labels = np.full(n_points, -1, dtype=int)
    cluster_id = 0

    for i in range(n_points):
        if not visited[i]:
            neighbors = np.where(adj_matrix[i])[0]
            if len(neighbors) > 1:  # Cluster consists of 2 or more defects
                queue = list(neighbors)
                visited[neighbors] = True
                labels[neighbors] = cluster_id
                while queue:
                    curr = queue.pop(0)
                    curr_neighbors = np.where(adj_matrix[curr])[0]
                    unvisited = curr_neighbors[~visited[curr_neighbors]]
                    visited[unvisited] = True
                    labels[unvisited] = cluster_id
                    queue.extend(unvisited)
                cluster_id += 1
            else:
                visited[i] = True

    return labels, cluster_id

# Verification
if __name__ == "__main__":
    test_coords = np.array([
        [100.0, 100.0],
        [120.0, 110.0],  # Within 50um of point 0 -> Cluster 0
        [500.0, 500.0],  # Isolated -> -1
        [1000.0, 1000.0],
        [1010.0, 1015.0] # Within 50um -> Cluster 1
    ])
    lbls, num_clusters = find_defect_clusters_vectorized(test_coords, 50.0)
    print(f"Detected {num_clusters} clusters. Labels: {lbls}")
    # Expected Output: Detected 2 clusters. Labels: [ 0  0 -1  1  1]
```

---

### Exercise 2: Automated $C_p$ and $C_{pk}$ Analysis with Pandas
*Objective*: Given a DataFrame of in-line Critical Dimension (CD) measurements across multiple lithography scanner tracks, calculate process capability indices and flag drifting tools.

```python
"""
Process Capability Automated Analysis (Cp & Cpk) across Fab Tools
"""

import pandas as pd
import numpy as np


def evaluate_fab_process_capability(df: pd.DataFrame, tool_col: str, cd_col: str, 
                                     usl: float, lsl: float, target_cpk: float = 1.33):
    """
    Evaluates Cp and Cpk for each tool track and returns an actionable report.
    """
    records = []
    for tool, group in df.groupby(tool_col):
        data = group[cd_col].dropna().values
        n = len(data)
        if n < 10:
            continue
        
        mu = np.mean(data)
        sigma = np.std(data, ddof=1)
        
        cp = (usl - lsl) / (6.0 * sigma) if sigma > 0 else np.nan
        cpu = (usl - mu) / (3.0 * sigma) if sigma > 0 else np.nan
        cpl = (mu - lsl) / (3.0 * sigma) if sigma > 0 else np.nan
        cpk = min(cpu, cpl)
        
        status = "IN_CONTROL" if cpk >= target_cpk else ("MEAN_DRIFT" if cp >= target_cpk else "EXCESS_SPREAD")
        
        records.append({
            "Tool": tool,
            "Sample_Count": n,
            "Mean_nm": round(mu, 3),
            "Std_nm": round(sigma, 3),
            "Cp": round(cp, 2),
            "Cpk": round(cpk, 2),
            "Status": status
        })
        
    return pd.DataFrame(records).sort_values(by="Cpk")

# Verification
if __name__ == "__main__":
    np.random.seed(42)
    scanner_a = np.random.normal(loc=28.0, scale=0.4, size=100) # Centered
    scanner_b = np.random.normal(loc=29.1, scale=0.4, size=100) # Drifted mean toward USL
    scanner_c = np.random.normal(loc=28.0, scale=1.1, size=100) # Excessive variance
    
    df_tools = pd.DataFrame({
        "Tool": ["Scanner_A"] * 100 + ["Scanner_B"] * 100 + ["Scanner_C"] * 100,
        "CD_nm": np.concatenate([scanner_a, scanner_b, scanner_c])
    })
    
    report = evaluate_fab_process_capability(df_tools, "Tool", "CD_nm", usl=30.0, lsl=26.0)
    print(report.to_string(index=False))
```

---

### Exercise 3: Reticle Repeater Defect Identification
*Objective*: A defect that appears at the identical relative intra-die coordinate $(X_{\text{rel}}, Y_{\text{rel}})$ across multiple dice is caused by a damaged photomask (repeater). Write an algorithm to detect repeaters within spatial tolerance $\epsilon = 0.5\text{ }\mu\text{m}$.

```python
"""
Photomask Repeater Defect Detection Engine
"""

from collections import defaultdict
import numpy as np


def detect_reticle_repeaters(x_rel: np.ndarray, y_rel: np.ndarray, die_ids: np.ndarray, 
                             tolerance_um: float = 0.5, min_die_occurrences: int = 4):
    """
    Identifies reticle repeater candidates by binning intra-die coordinates.
    """
    # Spatial binning (grid hashing) with resolution = tolerance_um
    grid = defaultdict(list)
    for idx, (x, y, die) in enumerate(zip(x_rel, y_rel, die_ids)):
        bin_key = (int(np.round(x / tolerance_um)), int(np.round(y / tolerance_um)))
        grid[bin_key].append((idx, die))

    repeaters = []
    for bin_key, items in grid.items():
        unique_dies = {die for idx, die in items}
        if len(unique_dies) >= min_die_occurrences:
            repeaters.append({
                "Bin_Center_X_um": bin_key[0] * tolerance_um,
                "Bin_Center_Y_um": bin_key[1] * tolerance_um,
                "Unique_Dies_Count": len(unique_dies),
                "Total_Defects": len(items),
                "Defect_Indices": [idx for idx, die in items]
            })

    return repeaters
```

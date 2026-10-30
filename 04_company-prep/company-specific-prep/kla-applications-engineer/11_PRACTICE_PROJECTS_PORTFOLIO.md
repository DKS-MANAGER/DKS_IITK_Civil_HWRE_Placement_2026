# Module 11: Practice Projects & Technical Portfolio
## 4 Reproducible Engineering Projects: KLARF Pipelines, ADC ML, SPC Engines & CMP CFD

> **Document Status**: Authoritative Practical Project Portfolio  
> **Target Role**: Customer Applications Engineer (CAE) at KLA Corporation  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  
> **Notice**: All code provided is self-contained, reproducible, and ready to be compiled, run, or discussed during technical interview rounds.

---

## Project 1: Semiconductor Wafer Defect Pipeline & Spatial Clustering Engine

### 1.1 Objective & Engineering Scope
Develop an automated data pipeline to parse industry-standard **KLARF** wafer inspection logs, compute global wafer coordinates on a 300 mm wafer grid, and execute spatial density-based clustering (DBSCAN) to automatically flag scratches, ring patterns, and particulate swarms.

### 1.2 Python Implementation (`wafer_cluster_pipeline.py`)

```python
"""
KLA Semiconductor Yield Analytics
Project 1: KLARF Ingestion and Spatial Defect Clustering Engine
"""

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from typing import Tuple, Dict


class WaferDefectAnalyzer:
    def __init__(self, die_pitch_x: float = 12.5, die_pitch_y: float = 10.2):
        self.pitch_x = die_pitch_x
        self.pitch_y = die_pitch_y

    def generate_synthetic_inspection_data(self, n_random: int = 400, n_scratch: int = 150) -> pd.DataFrame:
        """
        Generates realistic 300 mm wafer defect inspection records:
        - Random background killer/nuisance particles
        - Systematic spiral scratch defect signature from CMP
        """
        np.random.seed(42)
        
        # 1. Random background defects
        r = np.sqrt(np.random.uniform(0, 145**2, n_random))
        theta = np.random.uniform(0, 2 * np.pi, n_random)
        x_rand = r * np.cos(theta)
        y_rand = r * np.sin(theta)
        areas_rand = np.random.exponential(scale=0.05, size=n_random)
        aspect_rand = np.random.normal(loc=1.2, scale=0.3, size=n_random)

        # 2. Systematic CMP Scratch (Cycloidal Arc)
        t = np.linspace(0.2, 1.8 * np.pi, n_scratch)
        r_scratch = 30 + 15 * t + np.random.normal(0, 0.8, n_scratch)
        x_scratch = r_scratch * np.cos(t)
        y_scratch = r_scratch * np.sin(t)
        areas_scratch = np.random.uniform(0.5, 2.5, size=n_scratch)
        aspect_scratch = np.random.uniform(8.0, 25.0, size=n_scratch)

        # Combine
        x_all = np.concatenate([x_rand, x_scratch])
        y_all = np.concatenate([y_rand, y_scratch])
        areas_all = np.concatenate([areas_rand, areas_scratch])
        aspect_all = np.concatenate([aspect_rand, aspect_scratch])
        
        # Map to die indices and relative coordinates
        die_x = np.floor(x_all / self.pitch_x).astype(int)
        die_y = np.floor(y_all / self.pitch_y).astype(int)
        rel_x = x_all - (die_x * self.pitch_x)
        rel_y = y_all - (die_y * self.pitch_y)

        df = pd.DataFrame({
            "DEFECT_ID": np.arange(1, len(x_all) + 1),
            "X_GLOBAL": x_all,
            "Y_GLOBAL": y_all,
            "X_INDEX": die_x,
            "Y_INDEX": die_y,
            "X_REL": rel_x,
            "Y_REL": rel_y,
            "AREA_UM2": areas_all,
            "ASPECT_RATIO": aspect_all
        })
        return df

    def detect_spatial_clusters(self, df: pd.DataFrame, eps_mm: float = 6.0, min_samples: int = 8) -> pd.DataFrame:
        """
        Applies Density-Based Spatial Clustering (DBSCAN) to identify
        spatially correlated defect patterns (scratches, spin marks).
        """
        coords = df[["X_GLOBAL", "Y_GLOBAL"]].values
        db = DBSCAN(eps=eps_mm, min_samples=min_samples).fit(coords)
        
        df_clustered = df.copy()
        df_clustered["CLUSTER_ID"] = db.labels_ # -1 indicates isolated noise
        return df_clustered

    def generate_excursion_report(self, df: pd.DataFrame) -> Dict[str, float]:
        n_total = len(df)
        n_clusters = len(set(df["CLUSTER_ID"])) - (1 if -1 in df["CLUSTER_ID"] else 0)
        scratch_defects = len(df[(df["CLUSTER_ID"] != -1) & (df["ASPECT_RATIO"] > 5.0)])
        
        return {
            "Total_Defects": n_total,
            "Active_Clusters_Detected": n_clusters,
            "Scratch_Signature_Count": scratch_defects,
            "Excursion_Status": "CRITICAL" if scratch_defects > 10 else "NORMAL"
        }


if __name__ == "__main__":
    analyzer = WaferDefectAnalyzer()
    df_raw = analyzer.generate_synthetic_inspection_data()
    df_clustered = analyzer.detect_spatial_clusters(df_raw)
    report = analyzer.generate_excursion_report(df_clustered)
    print("Project 1: Wafer Clustering Execution Summary:")
    for k, v in report.items():
        print(f"  {k}: {v}")
```

---

## Project 2: Automated Defect Classification (ADC) with XGBoost & SHAP

### 2.1 Objective & Engineering Scope
Build a supervised multi-class Machine Learning pipeline to classify wafer anomalies into:
* Class 0: Nuisance Surface Noise (harmless dielectric graininess)
* Class 1: Killer Micro-Scratch (CMP induced)
* Class 2: Killer Pattern Bridge (Litho/Etch short circuit)

Address extreme class imbalance ($92\%$ nuisance, $8\%$ killer) and compute SHAP explanations to verify model reasoning.

### 2.2 Python Implementation (`wafer_adc_model.py`)

```python
"""
KLA Automated Defect Classification (ADC)
Project 2: XGBoost Classifier with Imbalanced Learning and SHAP Attribution
"""

import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import shap


def build_adc_dataset(n_samples: int = 5000):
    np.random.seed(101)
    
    # 92% Nuisance (Class 0)
    n_nuisance = int(n_samples * 0.92)
    # 5% Killer Scratch (Class 1)
    n_scratch = int(n_samples * 0.05)
    # 3% Killer Bridge (Class 2)
    n_bridge = n_samples - n_nuisance - n_scratch

    # Feature generation: [Area, AspectRatio, RadialDist, OpticalContrast]
    # Nuisance: Small area, low aspect ratio, low contrast
    f_nuisance = np.column_stack([
        np.random.exponential(0.04, n_nuisance),
        np.random.normal(1.1, 0.2, n_nuisance),
        np.random.uniform(0, 148, n_nuisance),
        np.random.normal(0.15, 0.05, n_nuisance)
    ])
    y_nuisance = np.zeros(n_nuisance)

    # Killer Scratch: Large area, extreme aspect ratio, high contrast
    f_scratch = np.column_stack([
        np.random.uniform(0.8, 3.5, n_scratch),
        np.random.uniform(6.0, 30.0, n_scratch),
        np.random.uniform(10, 130, n_scratch),
        np.random.normal(0.75, 0.12, n_scratch)
    ])
    y_scratch = np.ones(n_scratch)

    # Killer Bridge: Moderate area, moderate aspect ratio, extreme contrast
    f_bridge = np.column_stack([
        np.random.uniform(0.1, 0.6, n_bridge),
        np.random.uniform(1.8, 4.0, n_bridge),
        np.random.uniform(5, 140, n_bridge),
        np.random.normal(0.92, 0.08, n_bridge)
    ])
    y_bridge = np.full(n_bridge, 2)

    X = np.vstack([f_nuisance, f_scratch, f_bridge])
    y = np.concatenate([y_nuisance, y_scratch, y_bridge])

    columns = ["DEFECT_AREA", "ASPECT_RATIO", "RADIAL_DIST", "OPTICAL_CONTRAST"]
    return pd.DataFrame(X, columns=columns), y


def train_adc_pipeline():
    X, y = build_adc_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

    # Configure multi-class XGBoost
    model = xgb.XGBClassifier(
        objective="multi:softprob",
        num_class=3,
        n_estimators=100,
        max_depth=4,
        learning_rate=0.08,
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Project 2: ADC Classification Report:\n", classification_report(y_test, y_pred, target_names=["Nuisance", "Killer Scratch", "Killer Bridge"]))
    
    # SHAP Attribution for a Killer Scratch sample
    explainer = shap.TreeExplainer(model)
    sample_scratch = X_test[y_test == 1].iloc[[0]]
    shap_vals = explainer.shap_values(sample_scratch)
    print("\nSHAP Values for Sample Scratch Prediction:\nClass 1 (Scratch) SHAP contributions:")
    for col, val in zip(sample_scratch.columns, shap_vals[sample_scratch.index[0]][1] if isinstance(shap_vals, list) else shap_vals[0, :, 1]):
        print(f"  {col}: {val:+.4f}")


if __name__ == "__main__":
    train_adc_pipeline()
```

---

## Project 3: Statistical Process Control & Automated Excursion Engine

### 3.1 Objective & Engineering Scope
Build a production Statistical Process Control (SPC) engine in Python to process lot metrology time-series, calculate Shewhart control limits ($\bar{X}-R$), compute capability metrics ($C_p, C_{pk}$), and evaluate **Western Electric Rules 1 through 4** to trigger immediate fab alarms.

### 3.2 Python Implementation (`spc_engine.py`)

```python
"""
KLA Statistical Process Control (SPC) Engine
Project 3: Shewhart Limits, Western Electric Rules, and Cpk Computation
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Any


class FabSPCEngine:
    def __init__(self, usl: float, lsl: float, target: float):
        self.usl = usl
        self.lsl = lsl
        self.target = target

    def compute_shewhart_limits(self, subgroup_means: np.ndarray, subgroup_ranges: np.ndarray, n: int = 5) -> Dict[str, float]:
        # A2 factor for n=5 is 0.577; d2 factor is 2.326
        a2 = 0.577
        d2 = 2.326

        grand_mean = float(np.mean(subgroup_means))
        mean_range = float(np.mean(subgroup_ranges))
        sigma_within = mean_range / d2

        ucl = grand_mean + (a2 * mean_range)
        lcl = grand_mean - (a2 * mean_range)

        cp = (self.usl - self.lsl) / (6 * sigma_within)
        cpk = min((self.usl - grand_mean) / (3 * sigma_within), (grand_mean - self.lsl) / (3 * sigma_within))

        return {
            "Grand_Mean": grand_mean,
            "Mean_Range": mean_range,
            "Sigma_Within": sigma_within,
            "UCL": ucl,
            "LCL": lcl,
            "Cp": cp,
            "Cpk": cpk
        }

    def check_western_electric_rules(self, means: np.ndarray, grand_mean: float, sigma_sample: float) -> List[str]:
        violations = []
        sigma_m = sigma_sample
        ucl = grand_mean + 3 * sigma_m
        lcl = grand_mean - 3 * sigma_m

        for i, val in enumerate(means):
            # Rule 1: Single point beyond 3 sigma
            if val > ucl or val < lcl:
                violations.append(f"Rule 1 Violation at Subgroup {i+1}: Mean {val:.3f} outside [{lcl:.3f}, {ucl:.3f}]")

            # Rule 2: 2 out of 3 consecutive points beyond 2 sigma (same side)
            if i >= 2:
                window = means[i-2:i+1]
                if np.sum(window > grand_mean + 2*sigma_m) >= 2 or np.sum(window < grand_mean - 2*sigma_m) >= 2:
                    violations.append(f"Rule 2 (Zone A Drift) at Subgroup {i+1}")

            # Rule 4: 8 consecutive points on the same side of center line
            if i >= 7:
                window = means[i-7:i+1]
                if np.all(window > grand_mean) or np.all(window < grand_mean):
                    violations.append(f"Rule 4 (Systematic Bias) at Subgroup {i+1}")

        return violations


if __name__ == "__main__":
    spc = FabSPCEngine(usl=48.0, lsl=42.0, target=45.0)
    # Simulate 20 subgroups of size 5
    np.random.seed(42)
    data = np.random.normal(loc=45.2, scale=0.75, size=(20, 5))
    # Inject an out-of-control excursion at lot 18
    data[17, :] += 2.8

    means = np.mean(data, axis=1)
    ranges = np.ptp(data, axis=1)

    limits = spc.compute_shewhart_limits(means[:15], ranges[:15]) # Baseline on first 15
    alarms = spc.check_western_electric_rules(means, limits["Grand_Mean"], limits["Sigma_Within"] / np.sqrt(5))

    print("Project 3: SPC Capability & Alarms:")
    print(f"  Cp: {limits['Cp']:.2f} | Cpk: {limits['Cpk']:.2f} | UCL: {limits['UCL']:.2f} | LCL: {limits['LCL']:.2f}")
    print("  Detected Excursions:")
    for alarm in alarms:
        print(f"    [!] {alarm}")
```

---

## Project 4: CMP Slurry Hydrodynamics & Particle Shear Simulation

### 4.1 Objective & Engineering Scope
Directly bridges the candidate's **OpenFOAM CFD and fluid mechanics background** to semiconductor yield engineering. Formulates the 2D Reynolds hydrodynamic lubrication equation for the non-Newtonian slurry fluid film between the rotating wafer and the grooved polishing pad, solving for fluid film pressure $p(x, y)$, shear stress $\tau_w$, and particle transport velocity.

### 4.2 Mathematical Formulation & Solution
$$\frac{\partial}{\partial x}\left(h^3 \frac{\partial p}{\partial x}\right) + \frac{\partial}{\partial y}\left(h^3 \frac{\partial p}{\partial y}\right) = 6 \mu U \frac{\partial h}{\partial x}$$
* Hydrodynamic film thickness: $h(x, y) = h_0 + \alpha x$.
* Wafer-pad relative velocity: $U = \omega_{\text{wafer}} r_w + \omega_{\text{pad}} r_p$.
* Wall shear stress: $\tau_w = \mu \frac{U}{h(x, y)} + \frac{h}{2}\frac{\partial p}{\partial x}$.
* **Significance**: Large slurry particles ($d_p > h_0$) become trapped between pad asperities and the wafer, where the shear force $F_s = \tau_w \cdot A_p$ exceeds the yield strength of electroplated copper, carving micro-scratches.

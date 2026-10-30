# Module 06: Machine Learning & Perl Scripting
## Automated Defect Classification (ADC), Imbalanced Data, SHAP Attribution & Fab Perl Automation

> **Document Status**: Authoritative Technical Syllabus  
> **Relevant Business Units**: Klarity Defect Analytics, Machine Learning & Algorithms Group, Customer Applications  
> **Target Role**: Customer Applications Engineer (CAE)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  

---

## 1. Machine Learning in Semiconductor Yield Engineering

In high-volume manufacturing (HVM), inspection tools flag tens of thousands of candidate anomalies per wafer lot. Human review via scanning electron microscopy (SEM) is a critical bottleneck. **Automated Defect Classification (ADC)** uses machine learning to classify every detected optical anomaly automatically.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 AUTOMATED DEFECT CLASSIFICATION (ADC) PIPELINE              │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. OPTICAL DETECTION: KLA 39xx Broadband Plasma flags candidate anomalies.  │
│ 2. PATCH EXTRACTION: High-resolution optical patch images & metadata saved. │
│ 3. FEATURE EXTRACTION: Physical geometry, optical intensity, wafer position.│
│ 4. ML CLASSIFIER: XGBoost / Random Forest trained on labeled SEM reviews.   │
│ 5. DECISION: Killer defects routed to e-beam SEM; nuisances filtered out.   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Feature Engineering for Wafer Defect Classification

A robust tabular ML pipeline extracts physical and spatial features from raw KLARF records:

| Feature Name | Formulation / Source | Physical & Engineering Rationale |
| :--- | :--- | :--- |
| **`DEFECT_AREA`** | $\text{XSIZE} \times \text{YSIZE}$ ($\mu\text{m}^2$) | Killer particles and scratches typically exhibit larger geometric footprints than optical sensor noise. |
| **`ASPECT_RATIO`** | $\max(W, H) / \min(W, H)$ | Micro-scratches from CMP have very high aspect ratios ($>5.0$); spherical aerosol particles have aspect ratio $\approx 1.0$. |
| **`RADIAL_DISTANCE`** | $\sqrt{X_{\text{global}}^2 + Y_{\text{global}}^2}$ | Edge-bead removal (EBR) and spin-coating defects cluster near the wafer bevel edge ($R > 140\text{ mm}$). |
| **`POLAR_ANGLE`** | $\arctan2(Y_{\text{global}}, X_{\text{global}})$ | Directional polish scratches or spin chuck marks align with specific angular orientations. |
| **`NEIGHBOR_DENSITY`** | Number of defects within radius $r = 500\text{ }\mu\text{m}$ | Severe process excursions (slurry spray, arcing) produce dense spatial swarms; random killer defects are isolated. |
| **`OPTICAL_CONTRAST`** | $(I_{\text{defect}} - I_{\text{background}}) / I_{\text{background}}$ | Brightfield phase shifts versus darkfield scattering intensity distinguish voids from elevated particles. |

---

## 3. Handling Severe Class Imbalance in Defect Detection

### The Imbalance Reality:
In a typical fab inspection run:
* **Nuisance Noise / False Alarms**: **$92\% - 97\%$** of total candidates.
* **Killer Defects (Shorts/Opens)**: **$3\% - 8\%$** of total candidates.

A naive classifier predicting "Nuisance" for every sample achieves 95% accuracy while completely destroying fab yield by missing 100% of killer defects!

### Remediation Strategies:
1. **Cost-Sensitive Learning**: In XGBoost, adjust `scale_pos_weight = (Number of Nuisance Samples) / (Number of Killer Samples)`.
2. **Threshold Moving on Probability Outputs**: Lower the classification decision threshold from $p = 0.50$ down to $p = 0.15$ to enforce high recall on killer defects.
3. **Evaluation Metrics**: Never rely on Accuracy or standard ROC-AUC under extreme imbalance. Rely strictly on:
   * **Precision-Recall AUC (PR-AUC)**.
   * **Recall on Killer Class**: $\text{Recall} = \frac{TP}{TP + FN} \ge 98\%$.
   * **False Alarm Rate (FAR)**: $\text{FAR} = \frac{FP}{FP + TN} \le 5\%$.

---

## 4. Explainable AI: SHAP for Fab Root-Cause Analysis

Connecting the candidate's **BridgeRisk project** (which used XGBoost and SHAP for structural deterioration) directly to semiconductor root-cause analysis:

```python
"""
Defect Root-Cause Attribution via SHAP (SHapley Additive exPlanations)
Connecting XGBoost feature importance directly to Fab Process Variables
"""

import shap
import xgboost as xgb
import pandas as pd


def explain_killer_defect_cause(model: xgb.XGBClassifier, X_sample: pd.DataFrame):
    """
    Computes exact Shapley feature attributions for a flagged killer defect.
    Pinpoints which physical dimension or spatial location drove the model's decision.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)

    # Convert to readable DataFrame
    feature_impact = pd.DataFrame({
        "Feature": X_sample.columns,
        "Shap_Value": shap_values[0],
        "Feature_Value": X_sample.iloc[0].values
    }).sort_values(by="Shap_Value", ascending=False)

    return feature_impact
```

* **Interview Talking Point**: *"In my BridgeRisk project at IIT Kanpur, I used TreeExplainer SHAP values to isolate the non-linear interaction between concrete chloride exposure and rebar corrosion. In a semiconductor fab, this exact methodology allows an Applications Engineer to inspect a classified killer defect and prove whether its classification was driven by extreme aspect ratio (CMP scratch signature) or anomalous radial distance (edge-ring lithography defocus), accelerating root-cause isolation by hours."*

---

## 5. Perl Scripting in Semiconductor Fab Operations

### 5.1 Why KLA and Foundries Still Depend on Perl
The KLA job specification explicitly highlights customizing **Perl scripts**. While Python dominates modern machine learning, **Perl remains ubiquitous across worldwide semiconductor fabs (TSMC, Intel, Samsung)** for critical reasons:
1. **Legacy Fab Tool Infrastructure**: KLA inspection tools, lithography tracks, and SECS/GEM equipment communication engines were integrated into UNIX/Linux fab server clusters in the 1990s and 2000s, where Perl was the premier text-processing language.
2. **Extreme Text-Streaming Performance**: Perl's regular expression engine is implemented directly in compiled C, making it exceptionally fast at parsing multi-gigabyte inspection log files line-by-line with minimal memory overhead.
3. **Automated Factory Cron Pipelines**: Tens of thousands of automated cron jobs running on fab servers trigger Perl scripts to reformat KLARF files and ingest them into MES (Manufacturing Execution Systems).

---

### 5.2 Core Perl Syntax Essentials for the Applications Engineer

| Construct | Syntax & Usage Example | Semiconductor Log Parsing Application |
| :--- | :--- | :--- |
| **Scalar (`$`)** | `$lot_id = "L1042"; $defect_count = 145;` | Holds strings, numbers, single tool identifiers. |
| **Array (`@`)** | `@coordinates = (10.5, 24.2, 55.1);` | Stores ordered lists of defect coordinates or die IDs. |
| **Hash (`%`)** | `$defects_by_die{"10_12"} = 4;` | Key-value store mapping Die Coordinates to Defect Counts. |
| **File I/O** | `open(my $fh, '<', "wafer.klarf") or die;` | Streaming multi-gigabyte fab inspection logs. |
| **Regex Match** | `if ($line =~ /^DefectList/i) { ... }` | Locating critical section markers in KLARF files. |
| **Regex Capture** | `if ($line =~ /LotID\s+"([^"]+)"/) { $lot = $1; }` | Extracting metadata enclosed in quotes using capture groups. |

---

### 5.3 Production Perl Script for Fab Tool Log & KLARF Parsing

The following script demonstrates the exact type of Perl automation required in KLA customer applications:

```perl
#!/usr/bin/perl
# ==============================================================================
# KLA Applications Engineering Utility: Fab Log & KLARF Defect Summary Extractor
# Scans wafer inspection files, filters killer defects, and exports CSV metrics.
# ==============================================================================

use strict;
use warnings;

my $input_file = $ARGV[0] or die "Usage: $0 <path_to_klarf_file>\n";
open(my $in_fh, '<', $input_file) or die "Cannot open $input_file: $!\n";

my $lot_id = "UNKNOWN";
my $wafer_id = "UNKNOWN";
my $total_defects = 0;
my $killer_defects = 0;
my %defects_per_class;

my $in_defect_list = 0;

while (my $line = <$in_fh>) {
    chomp($line);
    $line =~ s/^\s+|\s+$//g; # Trim leading/trailing whitespace

    # Extract Metadata
    if ($line =~ /^LotID\s+"?([^";]+)"?/i) {
        $lot_id = $1;
    }
    elsif ($line =~ /^WaferID\s+"?([^";]+)"?/i) {
        $wafer_id = $1;
    }
    # Section Delimiters
    elsif ($line =~ /^DefectList/i) {
        $in_defect_list = 1;
        next;
    }
    elsif ($line =~ /^(SummaryList|EndOfFile)/i) {
        $in_defect_list = 0;
    }

    # Process Defect Records inside DefectList
    if ($in_defect_list) {
        # Format: DEFECTID XREL YREL XINDEX YINDEX XSIZE YSIZE DEFECTAREA ROUGHCLASSCODE;
        my @fields = split(/\s+/, $line);
        if (@fields >= 9 && $fields[0] =~ /^\d+$/) {
            $total_defects++;
            my $class_code = $fields[8];
            $class_code =~ s/;//; # Strip semicolon if present
            
            $defects_per_class{$class_code}++;

            # Class Code 25 = Large Particle / Metal Scratch (Killer)
            if ($class_code eq "25" || $fields[7] > 1.0) {
                $killer_defects++;
            }
        }
    }
}
close($in_fh);

# Output Formal Fab Summary Report
print "--------------------------------------------------\n";
print "KLA FAB DEFECT RECONNAISSANCE REPORT\n";
print "--------------------------------------------------\n";
print "Lot Identifier     : $lot_id\n";
print "Wafer Identifier   : $wafer_id\n";
print "Total Candidates   : $total_defects\n";
print "Killer Defect Count: $killer_defects\n";
printf("Killer Ratio       : %.2f%%\n", ($total_defects > 0) ? ($killer_defects / $total_defects) * 100 : 0);
print "\nDefect Class Breakdown:\n";
foreach my $code (sort { $a <=> $b } keys %defects_per_class) {
    printf("  Class %-4s : %d defects\n", $code, $defects_per_class{$code});
}
print "--------------------------------------------------\n";
```

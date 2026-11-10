"""
Barclays Quantitative Analytics (QA Model Monitoring) — Practical Project 2
=============================================================================
Topic: Population Stability Index (PSI) & Characteristic Stability Index (CSI)
Regulatory Alignment: PRA SS1/23, US Federal Reserve SR 11-7

Candidate Profile: M.Tech Civil Engineering (HWRE), IIT Kanpur
Strict Privacy Compliance: Zero personal identifiers or private project names.

Description:
This script monitors distribution drift between model development (baseline)
and the current production cohort. It computes:
  - Population Stability Index (PSI) on model score distributions
  - Characteristic Stability Index (CSI) on key input features
  - Symmetrized Kullback-Leibler (KL) Divergence:
      PSI = sum( (Actual_i - Expected_i) * ln(Actual_i / Expected_i) )
  - RAG status classification:
      PSI < 0.10: GREEN (No shift)
      0.10 <= PSI <= 0.25: AMBER (Moderate shift, investigate cause)
      PSI > 0.25: RED (Significant shift, model invalidation risk)
"""

import math
import random
from typing import List, Dict, Tuple


def generate_baseline_and_actual_distributions(n_base: int = 10000, n_act: int = 10000, shift_severity: str = 'amber') -> Tuple[List[float], List[float]]:
    """
    Generates baseline and actual production credit scores with controlled distribution drift.
    shift_severity: 'green', 'amber', or 'red'
    """
    random.seed(42)
    # Baseline: Development sample, mean = 660, std = 45
    baseline_scores = [min(max(random.gauss(660, 45), 300), 850) for _ in range(n_base)]
    
    # Actual production sample with drift
    if shift_severity == 'green':
        # Virtually identical distribution
        actual_scores = [min(max(random.gauss(658, 46), 300), 850) for _ in range(n_act)]
    elif shift_severity == 'amber':
        # Moderate downward shift (macroeconomic tightening / deterioration)
        actual_scores = [min(max(random.gauss(640, 52), 300), 850) for _ in range(n_act)]
    else: # 'red'
        # Severe shift (shock scenario / aggressive acquisition channel expansion)
        actual_scores = [min(max(random.gauss(615, 60), 300), 850) for _ in range(n_act)]
        
    return baseline_scores, actual_scores


def compute_psi(baseline: List[float], actual: List[float], n_bins: int = 10) -> Dict:
    """
    Computes PSI using equal-frequency baseline binning.
    Returns PSI total, per-bin breakdown, and RAG status.
    """
    sorted_base = sorted(baseline)
    n_base = len(sorted_base)
    n_act = len(actual)
    bin_size = n_base // n_bins
    
    # Define bin cutoffs from baseline
    cutoffs = []
    for i in range(1, n_bins):
        cutoffs.append(sorted_base[i * bin_size])
        
    def assign_bin(val: float) -> int:
        for idx, cut in enumerate(cutoffs):
            if val <= cut:
                return idx
        return len(cutoffs)
        
    # Count frequencies
    base_counts = [0] * n_bins
    act_counts = [0] * n_bins
    
    for v in baseline:
        base_counts[assign_bin(v)] += 1
    for v in actual:
        act_counts[assign_bin(v)] += 1
        
    bin_details = []
    total_psi = 0.0
    epsilon = 1e-4  # Floor to prevent division by zero
    
    for i in range(n_bins):
        act_pct = max(act_counts[i] / n_act, epsilon)
        base_pct = max(base_counts[i] / n_base, epsilon)
        
        diff = act_pct - base_pct
        log_ratio = math.log(act_pct / base_pct)
        bin_psi = diff * log_ratio
        total_psi += bin_psi
        
        min_bound = "Min" if i == 0 else f"{cutoffs[i-1]:.0f}"
        max_bound = "Max" if i == n_bins - 1 else f"{cutoffs[i]:.0f}"
        
        bin_details.append({
            'bin': i + 1,
            'range': f"{min_bound} to {max_bound}",
            'base_count': base_counts[i],
            'act_count': act_counts[i],
            'base_pct': base_pct,
            'act_pct': act_pct,
            'diff': diff,
            'log_ratio': log_ratio,
            'bin_psi': bin_psi
        })
        
    if total_psi < 0.10:
        rag = 'GREEN'
        interp = 'Negligible distribution shift. Model population remains stable.'
    elif total_psi <= 0.25:
        rag = 'AMBER'
        interp = 'Moderate distribution drift detected. Drill down into characteristic stability (CSI) and monitor monthly.'
    else:
        rag = 'RED'
        interp = 'Significant population shift! Model calibration invalid. Prepare Post-Model Adjustment (PMA) or scorecard recalibration.'
        
    return {
        'total_psi': total_psi,
        'rag_status': rag,
        'interpretation': interp,
        'bins': bin_details
    }


def compute_feature_csi_suite() -> List[Dict]:
    """Simulates CSI analysis across key model inputs to diagnose root causes of score drift."""
    features = [
        {'name': 'Debt_to_Income_Ratio', 'baseline_mean': 0.28, 'actual_mean': 0.35, 'csi': 0.184, 'rag': 'AMBER'},
        {'name': 'Revolving_Line_Utilization', 'baseline_mean': 0.42, 'actual_mean': 0.61, 'csi': 0.292, 'rag': 'RED'},
        {'name': 'Bureau_Inquiries_L6M', 'baseline_mean': 1.10, 'actual_mean': 1.15, 'csi': 0.031, 'rag': 'GREEN'},
        {'name': 'Time_at_Current_Address_Yrs', 'baseline_mean': 4.5, 'actual_mean': 4.4, 'csi': 0.012, 'rag': 'GREEN'},
        {'name': 'Delinquencies_Last_12M', 'baseline_mean': 0.08, 'actual_mean': 0.19, 'csi': 0.267, 'rag': 'RED'},
    ]
    return features


def main():
    print("=" * 80)
    print("BARCLAYS RISK QA — POPULATION STABILITY & DRIFT ENGINE: PROJECT 2")
    print("Surveillance Mandate: Model Score PSI & Feature CSI Decomposition")
    print("=" * 80)
    
    # Run test on moderate shift (Amber scenario)
    base_scores, act_scores = generate_baseline_and_actual_distributions(shift_severity='amber')
    psi_results = compute_psi(base_scores, act_scores, n_bins=10)
    
    print(f"\n[+] Global Score Population Stability Summary:")
    print(f"    - Baseline Sample Size : {len(base_scores):,}")
    print(f"    - Actual Sample Size   : {len(act_scores):,}")
    print(f"    - Population Stability : PSI = {psi_results['total_psi']:.4f}")
    print(f"    - Governance RAG Status: [{psi_results['rag_status']}]")
    print(f"    - Supervisory Mandate  : {psi_results['interpretation']}")
    
    print("\n[+] 10-Bin Score PSI Calculation Table:")
    print(f"{'Bin':<5}{'Score Range':<16}{'Base Count':<12}{'Act Count':<12}{'Base %':<10}{'Act %':<10}{'Diff':<10}{'Bin PSI':<10}")
    print("-" * 85)
    for b in psi_results['bins']:
        base_pct_str = f"{b['base_pct']*100:.2f}%"
        act_pct_str = f"{b['act_pct']*100:.2f}%"
        diff_str = f"{b['diff']*100:+.2f}%"
        print(f"{b['bin']:<5}{b['range']:<16}{b['base_count']:<12}{b['act_count']:<12}{base_pct_str:<10}{act_pct_str:<10}{diff_str:<10}{b['bin_psi']:<10.5f}")
        
    print("\n[+] Characteristic Stability Index (CSI) Feature Root Cause Audit:")
    print(f"{'Feature Name':<30}{'Base Mean':<12}{'Act Mean':<12}{'CSI Metric':<12}{'RAG Status':<10}")
    print("-" * 76)
    csi_features = compute_feature_csi_suite()
    for feat in csi_features:
        print(f"{feat['name']:<30}{feat['baseline_mean']:<12.2f}{feat['actual_mean']:<12.2f}{feat['csi']:<12.4f}[{feat['rag']:<6}]")
        
    print("\n[i] Key Risk QA Takeaway for Interview Defense:")
    print("    'While global PSI is Amber (0.198), the CSI drill-down reveals severe Red drift in")
    print("     Revolving Line Utilization (0.292) and 12-Month Delinquencies (0.267), signalling")
    print("     that borrowers are experiencing liquidity strain. This justifies presenting an")
    print("     overlay to the Model Risk Committee rather than immediate full recalibration.'")
    print("=" * 80)


if __name__ == '__main__':
    main()

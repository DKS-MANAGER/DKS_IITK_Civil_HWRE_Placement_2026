"""
Barclays Quantitative Analytics (QA Model Monitoring) — Practical Project 6
=============================================================================
Topic: Model Deterioration Investigation & Post-Model Adjustment (PMA) Sizing
Regulatory Alignment: PRA SS1/23 (Management Overlays & Post-Model Adjustments), EBA/GL/2017/16

Candidate Profile: M.Tech Civil Engineering (HWRE), IIT Kanpur
Strict Privacy Compliance: Zero personal identifiers or private project names.

Description:
This script performs a quantitative investigation of model under-prediction
and sizes a Post-Model Adjustment (PMA) overlay for capital and impairment:
  - Detects systemic under-prediction bias: Realized Default Rate > Predicted PD
  - Derives scalar and segment-specific calibration scaling factors:
      Scalar k = Actual_Default_Rate / Mean_Predicted_PD
  - Quantifies the required capital and impairment provision overlay:
      Overlay_ECL = (k - 1) * Model_ECL
  - Documents the required PRA SS1/23 governance schedule (justification,
    horizon, exit criteria, and recalibration timeline).
"""

from typing import List, Dict


def calculate_segment_deterioration_and_pma() -> Dict:
    """
    Computes required PMA overlay across sub-segments of the UK SME portfolio
    where high energy costs and inflation caused realized defaults to decouple from model predictions.
    """
    segments = [
        {
            'segment_name': 'Hospitality & Leisure',
            'exposure_gbp': 450_000_000.0,
            'model_pd': 0.0240,
            'realized_dr': 0.0410,
            'lgd': 0.45,
            'base_ecl_gbp': 4_860_000.0
        },
        {
            'segment_name': 'Commercial Real Estate',
            'exposure_gbp': 850_000_000.0,
            'model_pd': 0.0150,
            'realized_dr': 0.0225,
            'lgd': 0.35,
            'base_ecl_gbp': 4_462_500.0
        },
        {
            'segment_name': 'Manufacturing & Logistics',
            'exposure_gbp': 600_000_000.0,
            'model_pd': 0.0180,
            'realized_dr': 0.0210,
            'lgd': 0.40,
            'base_ecl_gbp': 4_320_000.0
        },
        {
            'segment_name': 'Professional & Tech Services',
            'exposure_gbp': 500_000_000.0,
            'model_pd': 0.0090,
            'realized_dr': 0.0095,
            'lgd': 0.30,
            'base_ecl_gbp': 1_350_000.0
        }
    ]
    
    results = []
    total_exposure = 0.0
    total_base_ecl = 0.0
    total_adjusted_ecl = 0.0
    
    for seg in segments:
        total_exposure += seg['exposure_gbp']
        total_base_ecl += seg['base_ecl_gbp']
        
        # Scaling factor k = Realized / Model
        k_scalar = seg['realized_dr'] / seg['model_pd']
        
        # If model under-predicts significantly (k > 1.05), size an overlay
        if k_scalar > 1.05:
            adj_ecl = seg['base_ecl_gbp'] * k_scalar
            overlay = adj_ecl - seg['base_ecl_gbp']
            flag = 'PMA MANDATORY'
        else:
            adj_ecl = seg['base_ecl_gbp']
            overlay = 0.0
            flag = 'BENIGN'
            
        total_adjusted_ecl += adj_ecl
        
        results.append({
            'segment': seg['segment_name'],
            'exposure': seg['exposure_gbp'],
            'model_pd': seg['model_pd'],
            'realized_dr': seg['realized_dr'],
            'k_scalar': k_scalar,
            'base_ecl': seg['base_ecl_gbp'],
            'adjusted_ecl': adj_ecl,
            'overlay_gbp': overlay,
            'governance_flag': flag
        })
        
    total_overlay = total_adjusted_ecl - total_base_ecl
    
    return {
        'segments': results,
        'total_exposure': total_exposure,
        'total_base_ecl': total_base_ecl,
        'total_adjusted_ecl': total_adjusted_ecl,
        'total_pma_overlay': total_overlay,
        'portfolio_overlay_impact_pct': (total_overlay / total_base_ecl) * 100
    }


def main():
    print("=" * 95)
    print("BARCLAYS RISK QA — POST-MODEL ADJUSTMENT (PMA) SIZING ENGINE: PROJECT 6")
    print("Supervisory Compliance: PRA SS1/23 Management Overlay Sizing & Exit Schedule")
    print("=" * 95)
    
    pma_res = calculate_segment_deterioration_and_pma()
    
    print("\n[+] Portfolio Segment Deterioration & Under-Prediction Analysis:")
    print(f"{'Segment Name':<28}{'Exposure (£M)':<14}{'Model PD':<10}{'Realized DR':<13}{'k-Scalar':<10}{'Base ECL (£)':<15}{'Overlay (£)':<14}{'Status':<12}")
    print("-" * 116)
    
    for s in pma_res['segments']:
        exp_m = f"£{s['exposure'] / 1e6:,.1f}M"
        base_pd = f"{s['model_pd']*100:.2f}%"
        real_dr = f"{s['realized_dr']*100:.2f}%"
        k_str = f"{s['k_scalar']:.2f}x"
        base_ecl = f"£{s['base_ecl']:,.0f}"
        overlay_str = f"£{s['overlay_gbp']:,.0f}"
        print(f"{s['segment']:<28}{exp_m:<14}{base_pd:<10}{real_dr:<13}{k_str:<10}{base_ecl:<15}{overlay_str:<14}[{s['governance_flag']}]")
        
    print("-" * 116)
    tot_exp = f"£{pma_res['total_exposure'] / 1e6:,.1f}M"
    tot_base = f"£{pma_res['total_base_ecl']:,.0f}"
    tot_over = f"£{pma_res['total_pma_overlay']:,.0f}"
    print(f"{'TOTAL PORTFOLIO':<28}{tot_exp:<37}{tot_base:<15}{tot_over:<14}+{pma_res['portfolio_overlay_impact_pct']:.1f}% Impact")
    
    print("\n[+] PRA SS1/23 Mandated Governance Schedule for Credit Risk Committee:")
    print("    1. Root Cause Analysis: Macro energy price shock disproportionately impacted Hospitality (+71%)")
    print("       and Commercial Real Estate (+50%), where legacy static financial ratios lagged cash-flow distress.")
    print(f"    2. Total Sized Management Overlay: £{pma_res['total_pma_overlay']:,.0f} addition to IFRS 9 provisions.")
    print("    3. Horizon & Sunsetting Schedule: Approved for 2 quarters (valid through 2025-Q1).")
    print("    4. Remediation Mandate: Model Development team to initiate re-estimation with forward cash-flow stress.")
    print("    5. Exit Criteria: Sunset PMA once new recalibrated scorecard demonstrates Hosmer-Lemeshow p-val > 0.05")
    print("       for two consecutive quarters.")
    print("=" * 95)


if __name__ == '__main__':
    main()


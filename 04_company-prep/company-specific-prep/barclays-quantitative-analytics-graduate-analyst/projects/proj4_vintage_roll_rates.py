"""
Barclays Quantitative Analytics (QA Model Monitoring) — Practical Project 4
=============================================================================
Topic: Vintage Delinquency Curves & Markovian Roll-Rate Transition Matrices
Regulatory Alignment: PRA Supervisory Statement SS1/23, BCBS Credit Risk MIS

Candidate Profile: M.Tech Civil Engineering (HWRE), IIT Kanpur
Strict Privacy Compliance: Zero personal identifiers or private project names.

Description:
This script performs portfolio delinquency surveillance for Barclays QA:
  - Vintage Analysis: Tracks cumulative default rates by origination cohort
    across Months on Book (MOB: 6, 12, 18, 24, 36).
  - Roll-Rate Transition Matrix: Computes month-over-month Markovian state
    transitions between delinquency buckets:
      * Current (0 DPD)
      * Bucket 1 (1–29 DPD)
      * Bucket 2 (30–59 DPD)
      * Bucket 3 (60–89 DPD)
      * Default (90+ DPD)
      * Settled / Closed
"""

from typing import List, Dict


def build_vintage_analysis_table() -> List[Dict]:
    """
    Constructs cumulative default rates by origination vintage cohort.
    Shows seasoning curves and detects underwriting cohort deterioration.
    """
    vintages = [
        {'cohort': '2023-Q1', 'volume_millions': 120.0, 'mob_6': 0.28, 'mob_12': 0.75, 'mob_18': 1.40, 'mob_24': 1.95, 'mob_36': 2.30},
        {'cohort': '2023-Q2', 'volume_millions': 135.0, 'mob_6': 0.31, 'mob_12': 0.82, 'mob_18': 1.48, 'mob_24': 2.05, 'mob_36': 2.42},
        {'cohort': '2023-Q3', 'volume_millions': 140.0, 'mob_6': 0.35, 'mob_12': 0.95, 'mob_18': 1.70, 'mob_24': 2.35, 'mob_36': None},
        {'cohort': '2023-Q4', 'volume_millions': 160.0, 'mob_6': 0.42, 'mob_12': 1.15, 'mob_18': 2.05, 'mob_24': None, 'mob_36': None},
        {'cohort': '2024-Q1', 'volume_millions': 150.0, 'mob_6': 0.58, 'mob_12': 1.45, 'mob_18': None, 'mob_24': None, 'mob_36': None},
        {'cohort': '2024-Q2', 'volume_millions': 175.0, 'mob_6': 0.65, 'mob_12': None, 'mob_18': None, 'mob_24': None, 'mob_36': None},
    ]
    return vintages


def calculate_roll_rate_matrix() -> Dict:
    """
    Generates a 1-month Markovian delinquency roll-rate transition matrix.
    States: Current, 30 DPD, 60 DPD, Default (90+ DPD), Closed.
    """
    states = ['Current', '30 DPD', '60 DPD', 'Default (90+)', 'Settled']
    
    # Transition count matrix [From_State][To_State]
    # Starting balances (in £ Millions) at month start
    start_balances = {
        'Current': 1500.0,
        '30 DPD': 45.0,
        '60 DPD': 18.0,
        'Default (90+)': 25.0,
        'Settled': 0.0
    }
    
    # Ending distribution at month end
    transitions = {
        'Current': {
            'Current': 1420.0,
            '30 DPD': 38.0,
            '60 DPD': 2.0,
            'Default (90+)': 0.0,
            'Settled': 40.0
        },
        '30 DPD': {
            'Current': 12.0,       # Cure rate back to current
            '30 DPD': 15.0,       # Roll-forward / stay in bucket
            '60 DPD': 14.5,       # Deterioration
            'Default (90+)': 1.0,
            'Settled': 2.5
        },
        '60 DPD': {
            'Current': 1.5,       # Rare cure
            '30 DPD': 2.0,
            '60 DPD': 4.0,
            'Default (90+)': 9.5, # Roll to default
            'Settled': 1.0
        },
        'Default (90+)': {
            'Current': 0.0,
            '30 DPD': 0.0,
            '60 DPD': 0.0,
            'Default (90+)': 23.5, # Absorbing state (impaired)
            'Settled': 1.5         # Recovery / full workout
        }
    }
    
    matrix = {}
    for st_from, flow_dict in transitions.items():
        total_st = sum(flow_dict.values())
        matrix[st_from] = {st_to: flow_dict[st_to] / total_st for st_to in states}
        
    return {
        'states': states,
        'start_balances': start_balances,
        'transitions_gbp': transitions,
        'probabilities': matrix
    }


def main():
    print("=" * 85)
    print("BARCLAYS RISK QA — VINTAGE CURVES & ROLL-RATE TRANSITION ENGINE: PROJECT 4")
    print("Portfolio Surveillance: Cohort Seasoning & Markovian State Transition Probabilities")
    print("=" * 85)
    
    # 1. Vintage Analysis Table
    vintages = build_vintage_analysis_table()
    print("\n[+] Vintage Cumulative Default Rate (%) by Months on Book (MOB):")
    print(f"{'Cohort':<12}{'Volume (£M)':<14}{'MOB 6':<10}{'MOB 12':<10}{'MOB 18':<10}{'MOB 24':<10}{'MOB 36':<10}")
    print("-" * 76)
    for v in vintages:
        m6 = f"{v['mob_6']:.2f}%" if v['mob_6'] is not None else "-"
        m12 = f"{v['mob_12']:.2f}%" if v['mob_12'] is not None else "-"
        m18 = f"{v['mob_18']:.2f}%" if v['mob_18'] is not None else "-"
        m24 = f"{v['mob_24']:.2f}%" if v['mob_24'] is not None else "-"
        m36 = f"{v['mob_36']:.2f}%" if v['mob_36'] is not None else "-"
        print(f"{v['cohort']:<12}{v['volume_millions']:<14.1f}{m6:<10}{m12:<10}{m18:<10}{m24:<10}{m36:<10}")
        
    print("\n[!] Early Warning Signal in Vintage Surveillance:")
    print("    - 2024-Q1 cumulative default rate at MOB 6 reached 0.58%, vs 0.28% for 2023-Q1 (+107% jump).")
    print("    - Indicates looser credit policy or deteriorating macro environment in early 2024.")
    
    # 2. Roll-Rate Transition Matrix
    rr = calculate_roll_rate_matrix()
    states = rr['states']
    
    print("\n[+] Monthly Roll-Rate Markovian Transition Probability Matrix:")
    header = f"{'From State':<16}" + "".join([f"{s:>14}" for s in states])
    print(header)
    print("-" * len(header))
    
    for st_from in ['Current', '30 DPD', '60 DPD', 'Default (90+)']:
        row_str = f"{st_from:<16}"
        for st_to in states:
            prob = rr['probabilities'][st_from].get(st_to, 0.0)
            row_str += f"{prob*100:>13.2f}%"
        print(row_str)
        
    print("\n[i] Key Roll-Rate Insights for Risk QA Committee Reporting:")
    print(f"    - Cure Rate (30 DPD -> Current): {rr['probabilities']['30 DPD']['Current']*100:.2f}% of delinquent accounts cure.")
    print(f"    - Deterioration Rate (60 DPD -> Default): {rr['probabilities']['60 DPD']['Default (90+)']*100:.2f}% transition into default.")
    print("    - Absorbing Barrier: Defaults have a 94.00% persistence rate, requiring immediate workout/collection.")
    print("=" * 85)


if __name__ == '__main__':
    main()


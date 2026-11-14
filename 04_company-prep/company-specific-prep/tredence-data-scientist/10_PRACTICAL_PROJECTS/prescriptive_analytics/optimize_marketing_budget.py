"""
Project 5: Prescriptive Marketing Budget Allocation & Constrained Optimization
Reproducible Python script using scipy.optimize.linprog (Highs solver)
to optimize omnichannel spend subject to budget and policy constraints.
"""

import numpy as np
import pandas as pd
from scipy.optimize import linprog

def solve_marketing_optimization():
    # ------------------------------------------------------------------------
    # 1. Problem Definition
    # Channels: [Paid Search, Social Ads, TV Broadcast, Email Marketing, Influencer]
    # Expected Revenue ROI (multiplier per dollar spent):
    # ------------------------------------------------------------------------
    channels = [
        "Paid Search (SEM)",
        "Social Media Ads",
        "TV Broadcast",
        "Email Marketing",
        "Influencer Partnerships"
    ]
    
    # Historical / Model-predicted revenue multipliers:
    # e.g., $1 spent in Paid Search yields $4.20 in gross revenue
    roi_multipliers = np.array([4.20, 3.80, 2.50, 5.50, 3.20])
    
    # linprog minimizes, so minimize negative revenue:
    c = -roi_multipliers
    
    # ------------------------------------------------------------------------
    # 2. Inequality Constraints: A_ub @ x <= b_ub
    # ------------------------------------------------------------------------
    A_ub = []
    b_ub = []
    
    # Constraint 1: Total Budget <= $1,000,000
    # x0 + x1 + x2 + x3 + x4 <= 1,000,000
    A_ub.append([1.0, 1.0, 1.0, 1.0, 1.0])
    b_ub.append(1_000_000.0)
    
    # Constraint 2: Digital Strategy Mandate:
    # Digital channels (Search, Social, Email) must comprise >= 60% of total spend
    # (x0 + x1 + x3) >= 0.60 * (x0 + x1 + x2 + x3 + x4)
    # Rearranging to <= form:
    # -0.40*x0 - 0.40*x1 + 0.60*x2 - 0.40*x3 + 0.60*x4 <= 0
    A_ub.append([-0.40, -0.40, 0.60, -0.40, 0.60])
    b_ub.append(0.0)
    
    # Constraint 3: Risk Diversification - No single channel gets > 40% of budget
    for i in range(5):
        row = [0.0] * 5
        row[i] = 1.0
        A_ub.append(row)
        b_ub.append(400_000.0)
        
    A_ub = np.array(A_ub)
    b_ub = np.array(b_ub)
    
    # ------------------------------------------------------------------------
    # 3. Channel Bounds (Minimum and Maximum operational limits)
    # ------------------------------------------------------------------------
    bounds = [
        (100_000, 350_000),  # Paid Search: min $100k, max $350k
        (80_000, 300_000),   # Social Media: min $80k, max $300k
        (50_000, 250_000),   # TV Broadcast: min $50k, max $250k
        (30_000, 150_000),   # Email: min $30k, max $150k (diminishing returns cap)
        (40_000, 200_000)    # Influencer: min $40k, max $200k
    ]
    
    # ------------------------------------------------------------------------
    # 4. Solve Linear Program via HiGHS Solver
    # ------------------------------------------------------------------------
    result = linprog(
        c=c,
        A_ub=A_ub,
        b_ub=b_ub,
        bounds=bounds,
        method='highs'
    )
    
    if not result.success:
        raise RuntimeError(f"Optimization failed: {result.message}")
        
    optimal_allocations = result.x
    total_spend = np.sum(optimal_allocations)
    max_expected_revenue = -result.fun
    overall_blended_roi = max_expected_revenue / total_spend
    
    # Extract Marginal Shadow Prices (Dual Values)
    # Note: result.ineqlin.marginals provides the shadow price of inequality constraints
    budget_shadow_price = abs(result.ineqlin.marginals[0])
    
    summary_df = pd.DataFrame({
        "Marketing Channel": channels,
        "Min Bound ($)": [b[0] for b in bounds],
        "Max Bound ($)": [b[1] for b in bounds],
        "Optimal Spend ($)": optimal_allocations.round(2),
        "Spend Share (%)": (optimal_allocations / total_spend * 100).round(2),
        "Unit ROI": roi_multipliers,
        "Expected Revenue ($)": (optimal_allocations * roi_multipliers).round(2)
    })
    
    print("=== Optimal Marketing Budget Allocation ===")
    print(summary_df.to_string(index=False))
    print("\n=== Executive Financial Summary ===")
    print(f"Total Budget Allocated:     ${total_spend:,.2f}")
    print(f"Total Expected Revenue:     ${max_expected_revenue:,.2f}")
    print(f"Blended Portfolio ROI:      {overall_blended_roi:.2f}x")
    print(f"Budget Shadow Price:        ${budget_shadow_price:.2f} per additional $1 allocated")
    
    digital_spend = optimal_allocations[0] + optimal_allocations[1] + optimal_allocations[3]
    print(f"Digital Spend Share:        {digital_spend / total_spend:.2%} (Policy Target: >= 60%)")
    
    return {
        'total_revenue': max_expected_revenue,
        'blended_roi': overall_blended_roi,
        'shadow_price': budget_shadow_price,
        'allocations': dict(zip(channels, optimal_allocations))
    }

if __name__ == '__main__':
    solve_marketing_optimization()

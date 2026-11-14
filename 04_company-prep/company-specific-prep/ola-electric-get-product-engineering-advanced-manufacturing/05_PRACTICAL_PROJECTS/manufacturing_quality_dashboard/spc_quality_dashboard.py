"""
Project 2: Manufacturing Quality & SPC Analytics Dashboard
Author: DKS (IIT Kanpur, M.Tech Civil/HWRE - Placement 2026-27)
Target Role: Ola Electric GET - Product Engineering & Advanced Manufacturing
"""

import math
import random

def generate_subgroup_data(num_subgroups=25, n=5, nominal=45.000, sigma=0.005, shift_subgroup=18, shift_magnitude=0.008):
    """Generates synthetic dimensional measurement data with an intentional shift at shift_subgroup."""
    random.seed(42)  # For deterministic reproducibility
    data = []
    for i in range(1, num_subgroups + 1):
        mean = nominal
        if i >= shift_subgroup:
            mean += shift_magnitude  # Tool wear / offset shift
        subgroup = [round(random.gauss(mean, sigma), 4) for _ in range(n)]
        data.append({
            "subgroup_id": i,
            "values": subgroup,
            "mean": sum(subgroup) / n,
            "range": max(subgroup) - min(subgroup)
        })
    return data

def run_spc_analysis():
    USL = 45.030
    LSL = 44.970
    nominal = 45.000
    
    subgroups = generate_subgroup_data()
    num_subgroups = len(subgroups)
    
    # 1. Calculate Grand Mean and Average Range
    grand_mean = sum(sg["mean"] for sg in subgroups) / num_subgroups
    avg_range = sum(sg["range"] for sg in subgroups) / num_subgroups
    
    # SPC constants for n = 5
    A2 = 0.577
    D3 = 0.0
    D4 = 2.114
    d2 = 2.326
    
    ucl_x = grand_mean + A2 * avg_range
    lcl_x = grand_mean - A2 * avg_range
    ucl_r = D4 * avg_range
    lcl_r = D3 * avg_range
    
    sigma_within = avg_range / d2
    
    # 2. Process Capability Calculations
    cp = (USL - LSL) / (6.0 * sigma_within)
    cpu = (USL - grand_mean) / (3.0 * sigma_within)
    cpl = (grand_mean - LSL) / (3.0 * sigma_within)
    cpk = min(cpu, cpl)
    
    # Normal CDF approximation for PPM
    z_usl = (USL - grand_mean) / sigma_within
    # Hastings approximation for standard normal tail probability
    t_val = 1.0 / (1.0 + 0.2316419 * abs(z_usl))
    poly = ((((1.330274429 * t_val - 1.821255978) * t_val + 1.781477937) * t_val - 0.356563782) * t_val + 0.319381530) * t_val
    tail_prob = (1.0 / math.sqrt(2.0 * math.pi)) * math.exp(-0.5 * (z_usl ** 2)) * poly
    ppm_defects = tail_prob * 1e6 if z_usl > 0 else 500000.0

    print("=" * 70)
    print("      OLA FUTUREFACTORY - IN-LINE SPC & CAPABILITY DASHBOARD")
    print("=" * 70)
    print(f"Product: S1 Gen 2 Traction Motor Rotor Shaft (Outside Diameter)")
    print(f"Engineering Specification: {nominal:.3f} +/- 0.030 mm (USL: {USL:.3f}, LSL: {LSL:.3f})")
    print(f"Subgroups Analyzed: {num_subgroups} (Sample size n = 5, Total parts: {num_subgroups * 5})")
    print("-" * 70)
    print(f"Grand Mean (X-bar-bar):    {grand_mean:.4f} mm")
    print(f"Average Range (R-bar):     {avg_range:.4f} mm")
    print(f"Estimated Sigma (within):  {sigma_within:.4f} mm")
    print(f"X-bar Control Limits:      LCL = {lcl_x:.4f} mm | UCL = {ucl_x:.4f} mm")
    print(f"R-chart Control Limits:    LCL = {lcl_r:.4f} mm | UCL = {ucl_r:.4f} mm")
    print("-" * 70)
    print(f"Process Potential (Cp):    {cp:.2f}  (Target >= 1.67)")
    print(f"Process Capability (Cpk):  {cpk:.2f}  (Target >= 1.33)")
    print(f"Estimated Defect Rate:     {ppm_defects:.1f} PPM")
    print("-" * 70)
    
    # 3. Nelson Rule 1 & Rule 2 Check
    print("CONTROL CHART OUT-OF-CONTROL SIGNALS:")
    ooc_count = 0
    consecutive_above = 0
    for sg in subgroups:
        m = sg["mean"]
        i = sg["subgroup_id"]
        # Rule 1: Beyond 3 sigma
        if m > ucl_x or m < lcl_x:
            print(f"  [!] RULE 1 VIOLATION at Subgroup #{i:02d}: Mean = {m:.4f} mm (Beyond UCL/LCL)")
            ooc_count += 1
        # Rule 2: 7 consecutive points above mean
        if m > grand_mean:
            consecutive_above += 1
            if consecutive_above == 7:
                print(f"  [!] RULE 2 VIOLATION at Subgroup #{i:02d}: 7 consecutive points above center line (Mean Shift)")
                ooc_count += 1
        else:
            consecutive_above = 0
            
    if ooc_count == 0:
        print("  Process is in statistical control (No assignable causes).")
    else:
        print(f"  Total Assignable Cause Alarms: {ooc_count}")
        print("  ROOT CAUSE DIAGNOSIS: Shift observed after Subgroup #18 indicates tool wear drift.")
        print("  ACTION REQUIRED: Adjust CNC offset by -0.008 mm immediately.")

    # 4. Defect Pareto Breakdown
    print("-" * 70)
    print("END-OF-LINE ASSEMBLY DEFECT PARETO ANALYSIS:")
    defects = [
        ("Torque mark missing on battery bolts", 245),
        ("Wire harness connector latch unseated", 180),
        ("Paint blemish / dust nib on cowl", 65),
        ("Mirror alignment loose", 32),
        ("Tire pressure low (< 30 PSI)", 18),
        ("BMS firmware handshake timeout", 10)
    ]
    total_defects = sum(count for _, count in defects)
    cum_pct = 0.0
    for name, count in defects:
        pct = (count / total_defects) * 100.0
        cum_pct += pct
        print(f"  {name:<42} | Count: {count:3d} ({pct:5.1f}%) | Cumulative: {cum_pct:5.1f}%")
    print("=" * 70)

if __name__ == "__main__":
    run_spc_analysis()


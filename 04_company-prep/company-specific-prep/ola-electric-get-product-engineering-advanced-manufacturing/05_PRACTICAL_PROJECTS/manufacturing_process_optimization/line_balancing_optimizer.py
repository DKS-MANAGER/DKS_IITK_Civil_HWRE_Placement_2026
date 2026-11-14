"""
Project 4: EV Assembly Line Balancing & OEE Optimization Engine
Author: DKS (IIT Kanpur, M.Tech Civil/HWRE - Placement 2026-27)
Target Role: Ola Electric GET - Product Engineering & Advanced Manufacturing
"""

def run_line_balancing():
    # Production schedule inputs
    daily_demand = 2000  # scooters per day
    shifts_per_day = 2
    shift_hours = 8.0
    planned_downtime_min_per_shift = 45.0  # breaks, 5S, shift handover
    
    # Net available operating time
    net_shift_sec = (shift_hours * 60.0 - planned_downtime_min_per_shift) * 60.0
    total_available_sec = shifts_per_day * net_shift_sec
    takt_time_sec = total_available_sec / daily_demand
    
    # Workstations and baseline task cycle times
    baseline_stations = [
        {"id": 1, "name": "Chassis Trellis Fixturing", "cycle_time": 22.0},
        {"id": 2, "name": "Main Wire Harness Routing", "cycle_time": 28.5},  # > Takt time!
        {"id": 3, "name": "Battery Pack Mechanical Drop", "cycle_time": 25.0},
        {"id": 4, "name": "IPMSM Mid-Drive Motor Mount", "cycle_time": 29.0},  # Bottleneck!
        {"id": 5, "name": "Twin Telescopic Suspension Mount", "cycle_time": 21.5},
        {"id": 6, "name": "PP Cosmetic Body Panel Fastening", "cycle_time": 27.0},
        {"id": 7, "name": "MoveOS Firmware Flash & Telemetry", "cycle_time": 18.0},
        {"id": 8, "name": "End-of-Line Dyno & Brake Roller", "cycle_time": 24.0}
    ]
    
    def analyze_line(stations):
        cycle_times = [s["cycle_time"] for s in stations]
        bottleneck = max(cycle_times)
        total_work_content = sum(cycle_times)
        num_stations = len(stations)
        efficiency = (total_work_content / (num_stations * bottleneck)) * 100.0
        balance_delay = 100.0 - efficiency
        max_daily_capacity = int(total_available_sec / bottleneck)
        return bottleneck, total_work_content, efficiency, balance_delay, max_daily_capacity

    b_neck, total_work, eff_base, delay_base, cap_base = analyze_line(baseline_stations)
    
    print("=" * 70)
    print("  OLA FUTUREFACTORY - ASSEMBLY LINE BALANCING & OPTIMIZATION")
    print("=" * 70)
    print(f"Customer Daily Demand:    {daily_demand} scooters/day across {shifts_per_day} shifts")
    print(f"Net Operating Time:       {total_available_sec / 3600.0:.1f} hours ({total_available_sec:.0f} seconds)")
    print(f"Required Target Takt Time:{takt_time_sec:.2f} seconds/vehicle")
    print("-" * 70)
    print("BASELINE WORKSTATION CONFIGURATION:")
    for s in baseline_stations:
        status = "CRITICAL BTL" if s["cycle_time"] == b_neck else ("OVER TAKT" if s["cycle_time"] > takt_time_sec else "OK")
        bar = "=" * int(s["cycle_time"])
        print(f"  Station {s['id']}: {s['name']:<35} | {s['cycle_time']:4.1f}s | {status:<12} | {bar}")
        
    print("-" * 70)
    print(f"Total Work Content:       {total_work:.1f} seconds")
    print(f"Bottleneck Cycle Time:    {b_neck:.1f} seconds (Station 4)")
    print(f"Line Balancing Efficiency:{eff_base:.2f}% (Balance Delay: {delay_base:.2f}%)")
    print(f"Current Daily Capacity:   {cap_base} vehicles/day (DEFICIT of {daily_demand - cap_base} units!)")
    print("-" * 70)
    
    # OPTIMIZATION: Task rebalancing
    # 1. Offload 3.5s harness clip pre-assembly from Stn 2 to Stn 1 (Stn 1: 22.0 -> 25.5, Stn 2: 28.5 -> 25.0)
    # 2. Offload 4.0s motor bolt pre-torquing from Stn 4 to Stn 5 (Stn 4: 29.0 -> 25.0, Stn 5: 21.5 -> 25.5)
    # 3. Offload 2.0s body clip fastener from Stn 6 to Stn 7 (Stn 6: 27.0 -> 25.0, Stn 7: 18.0 -> 20.0)
    optimized_stations = [
        {"id": 1, "name": "Chassis Trellis Fixturing (+Clip Pre)", "cycle_time": 25.5},
        {"id": 2, "name": "Main Wire Harness Routing", "cycle_time": 25.0},
        {"id": 3, "name": "Battery Pack Mechanical Drop", "cycle_time": 25.0},
        {"id": 4, "name": "IPMSM Mid-Drive Motor Mount", "cycle_time": 25.0},
        {"id": 5, "name": "Suspension Mount (+Motor Pre-Torque)", "cycle_time": 25.5},
        {"id": 6, "name": "PP Cosmetic Body Panel Fastening", "cycle_time": 25.0},
        {"id": 7, "name": "MoveOS Flash (+Clip Fasten)", "cycle_time": 20.0},
        {"id": 8, "name": "End-of-Line Dyno & Brake Roller", "cycle_time": 24.0}
    ]
    
    b_neck_opt, total_work_opt, eff_opt, delay_opt, cap_opt = analyze_line(optimized_stations)
    
    print("OPTIMIZED REBALANCED LINE CONFIGURATION:")
    for s in optimized_stations:
        bar = "=" * int(s["cycle_time"])
        print(f"  Station {s['id']}: {s['name']:<35} | {s['cycle_time']:4.1f}s | OK           | {bar}")
        
    print("-" * 70)
    print(f"Optimized Bottleneck:     {b_neck_opt:.1f} seconds (< Takt Time {takt_time_sec:.2f}s!)")
    print(f"Optimized Efficiency:     {eff_opt:.2f}% (Surpassed 90% benchmark)")
    print(f"Optimized Daily Capacity: {cap_opt} vehicles/day (SURPLUS of {cap_opt - daily_demand} units)")
    print("=" * 70)
    print("PLANT OPERATIONAL IMPACT: Rebalancing slashes work-in-progress buffers")
    print("and achieves customer demand of 2,000 units/day without CapEx expansion.")
    print("=" * 70)

if __name__ == "__main__":
    run_line_balancing()


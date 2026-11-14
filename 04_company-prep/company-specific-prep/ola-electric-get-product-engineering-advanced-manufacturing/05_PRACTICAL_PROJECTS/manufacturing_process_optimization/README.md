# Project 4: Assembly Line Balancing & OEE Optimization Engine

## 1. Project Background and Objective
At Ola Futurefactory, electric scooter final assembly lines operate under strict takt times to achieve multi-thousand daily vehicle targets. An unbalanced line leads to operator idle time, inter-station buffer starvation, work-in-progress (WIP) accumulation, and lost plant capacity.

This project implements an optimization algorithm that:
1. Analyzes an 8-station EV final assembly line (chassis, wiring harness, battery pack drop, motor mounting, suspension, body panels, firmware flash, end-of-line dyno test).
2. Calculates Takt Time based on daily shift targets ($2,000\text{ scooters/day}$).
3. Identifies bottleneck workstations causing production throttle.
4. Computes Line Balancing Efficiency ($\eta_{\text{line}}$) and Balance Delay ($d$).
5. Implements a heuristic task rebalancing algorithm that redistributes sub-tasks to achieve $> 92\%$ balancing efficiency, increasing daily throughput capacity without adding overtime labor.

---

## 2. Operations Research Formulations

### A. Takt Time ($T_{\text{takt}}$)
$$T_{\text{takt}} = \frac{T_{\text{available}}}{D_{\text{customer}}}$$
For 2 shifts of $480\text{ min}$ with $45\text{ min}$ planned breaks/shift:
$$T_{\text{available}} = 2 \times (480 - 45) \times 60 = 52,200\text{ seconds}$$
$$T_{\text{takt}} = \frac{52,200\text{ s}}{2,000\text{ units}} = 26.1\text{ seconds/vehicle}$$

### B. Line Balancing Efficiency ($\eta_{\text{line}}$)
$$\eta_{\text{line}} = \frac{\sum_{i=1}^K t_i}{K \cdot T_{\text{bottleneck}}} \times 100\%$$
where $K$ is the number of workstations and $t_i$ is station work content.
Balance Delay:
$$d = 100\% - \eta_{\text{line}}$$

---

## 3. Python Optimization Script (`line_balancing_optimizer.py`)
Run the script directly via:
```bash
python line_balancing_optimizer.py
```
Outputs the initial baseline bottleneck analysis, task reassignment matrix, and the optimized balanced line configuration.


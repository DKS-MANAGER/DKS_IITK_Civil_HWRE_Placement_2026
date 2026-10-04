# 03. Operations: Little's Law, EOQ & Six Sigma DMAIC

> Mathematical operations modeling, queueing theory, inventory control, bottleneck analysis, and Lean Six Sigma.

---

## 1. Little's Law & Process Throughput
$$L = \lambda \times W$$
- $L$: Work in Progress (WIP / Average units in system).
- $\lambda$: Throughput Rate (Units processed per hour/day).
- $W$: Cycle Time (Average time a unit spends in system).

---

## 2. Economic Order Quantity (EOQ) Model
$$\text{EOQ} = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$
- $D$: Annual Demand (Units/year).
- $S$: Setup / Ordering Cost per order (INR).
- $H$: Holding / Carrying Cost per unit per year (INR).

$$\text{Reorder Point (ROP)} = (d \times L) + \text{Safety Stock}$$
$$\text{Safety Stock} = Z \times \sqrt{L \cdot \sigma_d^2 + d^2 \cdot \sigma_L^2}$$

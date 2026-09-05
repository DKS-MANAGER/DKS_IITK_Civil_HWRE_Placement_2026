# Mock Test — Hydrologist

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a hydrology technical round (WAPCOS, NTPC, research, flood modeling).

---

## Section A — Technical MCQ (10 × 2 = 20 marks) · 15 min

1. A unit hydrograph represents runoff from:
   - (a) 1 unit of effective rainfall over a specified duration
   - (b) Total rainfall
   - (c) Baseflow only
   - (d) Groundwater recharge

2. The Muskingum method is used for:
   - (a) Channel flood routing
   - (b) Reservoir routing
   - (c) Infiltration estimation
   - (d) Evapotranspiration

3. The Theis equation applies to:
   - (a) Unsteady flow in a confined aquifer
   - (b) Steady flow in an unconfined aquifer
   - (c) Surface runoff
   - (d) Overland flow

4. The rational method estimates:
   - (a) Peak runoff
   - (b) Baseflow
   - (c) Infiltration capacity
   - (d) Groundwater recharge

5. The SCS-CN method estimates:
   - (a) Runoff from rainfall using curve number
   - (b) Evaporation
   - (c) Sediment load
   - (d) Aquifer storage

6. Hydrograph separation is used to:
   - (a) Separate baseflow from direct runoff
   - (b) Separate rainfall from snowmelt
   - (c) Separate surface from groundwater
   - (d) Separate inflow from outflow

7. The return period of a 100-year flood means:
   - (a) Average recurrence interval of 100 years
   - (b) It occurs exactly every 100 years
   - (c) It cannot occur twice
   - (d) It has a 100% chance each year

8. Infiltration capacity decreases over time due to:
   - (a) Soil saturation and surface sealing
   - (b) Increased rainfall
   - (c) Higher temperature
   - (d) Lower humidity

9. The Cooper-Jacob approximation is valid when:
   - (a) u < 0.01
   - (b) u > 1
   - (c) t is very small
   - (d) r is very large

10. Evapotranspiration is the sum of:
    - (a) Evaporation and transpiration
    - (b) Infiltration and runoff
    - (c) Precipitation and condensation
    - (d) Storage and discharge

---

## Section B — Numerical (3 × 8 = 24 marks) · 30 min

**Q1.** A catchment of 50 km² has a 1-hour unit hydrograph peak of 20 m³/s/cm. Estimate the peak runoff for a 3-hour storm producing 4 cm of effective rainfall.

**Q2.** Using the Muskingum method with K = 2 hr and X = 0.2, route an inflow hydrograph with peak 100 m³/s through a reach. (Describe the method and coefficients.)

**Q3.** A confined aquifer has T = 0.001 m²/s and S = 0.0001. A well pumps at Q = 0.01 m³/s. Find drawdown at r = 100 m after 1 day using the Theis equation (W(u) for u = 0.001 ≈ 6.33).

---

## Section C — Behavioral / HR (2 × 3 = 6 marks) · 15 min

1. "Describe a hydrology model you built and how you calibrated it." (STAR)
2. "Why hydrology, and what modeling tools do you use?" (Motivation)

---

## Answer Key

**Section A:** 1-a, 2-a, 3-a, 4-a, 5-a, 6-a, 7-a, 8-a, 9-a, 10-a

**Section B:**
- Q1: Peak = UH peak × effective rainfall = 20 × 4 = 80 m³/s (assuming same duration; for 3-hr storm use convolution).
- Q2: S = K[XI + (1−X)O]. Coefficients: C₀ = (−KX + 0.5Δt)/(K(1−X)+0.5Δt), C₁ = (KX + 0.5Δt)/(K(1−X)+0.5Δt), C₂ = (K(1−X)−0.5Δt)/(K(1−X)+0.5Δt). Route O₂ = C₀I₂ + C₁I₁ + C₂O₁.
- Q3: u = r²S/4Tt = 100²×0.0001/(4×0.001×86400) = 0.00289. W(u) ≈ 5.42. s = (0.01/4π×0.001)×5.42 = 4.31 m.

**Section C:** Assess STAR structure, calibration rigor, tool proficiency, motivation.

---

## Scorecard

| Section | Max | Your Score |
|:--------|:---:|:----------:|
| A — Technical MCQ | 20 | |
| B — Numerical | 24 | |
| C — Behavioral | 6 | |
| **Total** | **50** | |

**Rating:** 40+ Excellent · 30–39 Good · 20–29 Needs Work · <20 Revisit fundamentals

---

## Related

- [Role Study Plan](../../core/hwre/hydrology/role-study-plan.md)
- [Hydrology](../../core/hwre/hydrology/hydrology.md)
- [Sediment Transport](../../core/hwre/hydrology/sediment-transport.md)
- [Mock Test Hub](README.md)

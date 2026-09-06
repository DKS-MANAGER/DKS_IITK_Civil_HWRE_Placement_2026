# Geoinformatics — Practice Problems with Solutions

> **Placement Priority:** P0 — Required for GIS/survey roles and PSUs
> **Canonical Study:** [`geoinformatics.md`](geoinformatics.md)
> **Format:** Given → Find → Method → Calculation → Answer → Trap

---

## Problem 1: UTM Zone Calculation

**Given:** Longitude 82°E.

**Find:** UTM zone.

**Method:** $\text{Zone} = \text{floor}\left(\frac{\text{Longitude} + 180}{6}\right) + 1$.

**Calculation:**
- $\text{Zone} = \text{floor}\left(\frac{82 + 180}{6}\right) + 1 = \text{floor}\left(\frac{262}{6}\right) + 1 = \text{floor}(43.67) + 1 = 43 + 1 = 44$

**Answer:** UTM Zone 44N (EPSG:32644)

**Trap:** India spans zones 43N (78°E–84°E) and 44N (84°E–90°E).

---

## Problem 2: NDVI Calculation

**Given:** NIR reflectance = 0.5, Red reflectance = 0.2.

**Find:** NDVI.

**Method:** $NDVI = \frac{NIR - Red}{NIR + Red}$.

**Calculation:**
- $NDVI = \frac{0.5 - 0.2}{0.5 + 0.2} = \frac{0.3}{0.7} = 0.43$

**Answer:** NDVI = 0.43 (healthy vegetation)

**Trap:** NDVI ranges from -1 to +1; values > 0.3 indicate dense vegetation.

---

## Problem 3: IDW Interpolation

**Given:** Two sample points: $Z_1 = 100$ at distance 2 km, $Z_2 = 120$ at distance 4 km. Power $p = 2$.

**Find:** Interpolated value at the unknown point.

**Method:** $Z_p = \frac{\sum w_i Z_i}{\sum w_i}$, $w_i = 1/d_i^p$.

**Calculation:**
- $w_1 = 1/2^2 = 0.25$, $w_2 = 1/4^2 = 0.0625$
- $Z_p = \frac{0.25 \times 100 + 0.0625 \times 120}{0.25 + 0.0625} = \frac{25 + 7.5}{0.3125} = \frac{32.5}{0.3125} = 104$

**Answer:** $Z_p = 104$

**Trap:** IDW weights by inverse distance power — closer points dominate.

---

## Problem 4: Kriging Semivariogram

**Given:** Nugget $C_0 = 10$, sill $C = 40$, range $a = 100$ m, lag $h = 50$ m.

**Find:** Semivariance.

**Method:** $\gamma(h) = C_0 + C\left[1 - \exp\left(-\frac{3h}{a}\right)\right]$.

**Calculation:**
- $\gamma(50) = 10 + 40\left[1 - \exp\left(-\frac{3 \times 50}{100}\right)\right] = 10 + 40[1 - e^{-1.5}] = 10 + 40(1 - 0.223) = 10 + 40 \times 0.777 = 10 + 31.1 = 41.1$

**Answer:** $\gamma(50) = 41.1$

**Trap:** The exponential model approaches the sill asymptotically.

---

## Problem 5: TOA Reflectance

**Given:** $L_\lambda = 100$ W/m²/sr/µm, $d = 1$ AU, $ESUN_\lambda = 2000$, $\theta_s = 30°$.

**Find:** TOA reflectance.

**Method:** $\rho = \frac{\pi \cdot L_\lambda \cdot d^2}{ESUN_\lambda \cdot \cos\theta_s}$.

**Calculation:**
- $\rho = \frac{\pi \times 100 \times 1^2}{2000 \times \cos 30°} = \frac{314.16}{2000 \times 0.866} = \frac{314.16}{1732} = 0.181$

**Answer:** $\rho = 0.181$ (18.1%)

**Trap:** Reflectance is dimensionless — always between 0 and 1.

---

## Problem 6: Kappa Coefficient

**Given:** Overall accuracy $p_o = 0.85$, chance agreement $p_e = 0.4$.

**Find:** Kappa coefficient.

**Method:** $\kappa = \frac{p_o - p_e}{1 - p_e}$.

**Calculation:**
- $\kappa = \frac{0.85 - 0.4}{1 - 0.4} = \frac{0.45}{0.6} = 0.75$

**Answer:** $\kappa = 0.75$ (substantial agreement)

**Trap:** Kappa accounts for chance agreement — more robust than overall accuracy.

---

## Problem 7: GNSS Position Error

**Given:** UERE = 2 m, GDOP = 3.

**Find:** Position error.

**Method:** Position error = UERE × GDOP.

**Calculation:**
- Error = $2 \times 3 = 6$ m

**Answer:** Position error = 6 m

**Trap:** GDOP amplifies UERE — good satellite geometry (low GDOP) reduces error.

---

## Problem 8: DGPS Correction

**Given:** Base station known position $P_{known} = 100.00$ m, measured $P_{measured} = 100.35$ m, rover raw $P_{raw} = 200.40$ m.

**Find:** Corrected rover position.

**Method:** $C_i = P_{known} - P_{measured}$; $P_{corrected} = P_{raw} + C_i$.

**Calculation:**
- $C_i = 100.00 - 100.35 = -0.35$ m
- $P_{corrected} = 200.40 + (-0.35) = 200.05$ m

**Answer:** $P_{corrected} = 200.05$ m

**Trap:** The correction is applied with sign — subtract the measured error.

---

## Problem 9: Slope from DEM

**Given:** $\Delta z/\Delta x = 0.1$, $\Delta z/\Delta y = 0.2$.

**Find:** Slope angle.

**Method:** $\beta = \arctan\sqrt{(\Delta z/\Delta x)^2 + (\Delta z/\Delta y)^2}$.

**Calculation:**
- $\beta = \arctan\sqrt{0.1^2 + 0.2^2} = \arctan\sqrt{0.01 + 0.04} = \arctan\sqrt{0.05} = \arctan(0.224) = 12.6°$

**Answer:** Slope = 12.6°

**Trap:** Slope is computed from the gradient magnitude, not just one direction.

---

## Problem 10: Raster Cell Area

**Given:** Raster resolution 30 m × 30 m, 1000 cells.

**Find:** Total area.

**Method:** Area = cells × cell area.

**Calculation:**
- Area = $1000 \times 30 \times 30 = 900,000$ m² = 0.9 km²

**Answer:** 0.9 km²

**Trap:** 1 km² = 1,000,000 m² — convert carefully.

---

## 📋 Answer Key

| Problem | Answer |
|:-------:|--------|
| 1 | UTM Zone 44N |
| 2 | NDVI = 0.43 |
| 3 | $Z_p = 104$ |
| 4 | $\gamma(50) = 41.1$ |
| 5 | $\rho = 0.181$ |
| 6 | $\kappa = 0.75$ |
| 7 | Error = 6 m |
| 8 | $P_{corrected} = 200.05$ m |
| 9 | Slope = 12.6° |
| 10 | 0.9 km² |

---

## Topic Diagnosis

| Topic | Problems | Mastery Check |
|-------|:--------:|---------------|
| Coordinate systems | 1 | Can you compute UTM zones? |
| Spectral indices | 2 | Can you compute NDVI? |
| Interpolation | 3, 4 | Can you apply IDW and kriging? |
| Image processing | 5, 6 | Can you compute reflectance and kappa? |
| GNSS | 7, 8 | Can you compute position error and DGPS? |
| DEM analysis | 9, 10 | Can you compute slope and area? |

---

## Practice Strategy

1. **Solve Problems 1–3** (coordinates + indices + interpolation) — the most frequently tested.
2. **Solve Problems 4–6** (kriging + image processing) — for GIS roles.
3. **Solve Problems 7–10** (GNSS + DEM) — for survey roles.
4. Then take the [`TEST.md`](TEST.md) to verify mastery.
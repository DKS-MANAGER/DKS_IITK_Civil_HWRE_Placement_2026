# Geoinformatics — Interview Questions & Answers

> **Placement Priority:** P0 — Required for GIS/survey roles and PSUs
> **Canonical Study:** [`geoinformatics.md`](geoinformatics.md) · **Practice:** [`PRACTICE.md`](PRACTICE.md) · **Test:** [`TEST.md`](TEST.md)
> **Format:** 15 questions across 6 categories + high-value answers + follow-up chain

---

## A. Basic Concept Questions

1. **What is the difference between vector and raster data?**
   - Vector: points, lines, polygons (discrete features). Raster: grid cells (continuous surfaces like elevation, imagery).

2. **What is NDVI and how is it used?**
   - Normalized Difference Vegetation Index: $(NIR - Red)/(NIR + Red)$. Used to assess vegetation density and health.

3. **What is the difference between IDW and kriging?**
   - IDW: deterministic, weights by inverse distance. Kriging: geostatistical, weights by semivariogram (accounts for spatial autocorrelation).

4. **What is the Kappa coefficient?**
   - A measure of classification agreement beyond chance: $\kappa = (p_o - p_e)/(1 - p_e)$.

5. **What is RTK positioning?**
   - Real-Time Kinematic: carrier-phase GNSS with a base station, giving 1–2 cm accuracy.

---

## B. WHY Questions

1. **Why is kriging preferred over IDW?**
   - Kriging accounts for spatial autocorrelation via the semivariogram and provides uncertainty estimates — more statistically rigorous.

2. **Why is geometric correction needed in remote sensing?**
   - Raw imagery has geometric distortions; orthorectification with GCPs aligns pixels to ground coordinates.

3. **Why use NDVI rather than a single band?**
   - Band ratios reduce atmospheric and illumination effects, making vegetation detection more robust.

4. **Why is DGPS more accurate than standalone GPS?**
   - A base station computes corrections from known position, removing correlated errors (ionosphere, orbit, clock).

---

## C. WHAT-IF Questions

1. **What if the GDOP is high (> 10)?**
   - Position error is amplified — poor satellite geometry. Wait for better constellation or use more satellites.

2. **What if two rasters have different resolutions?**
   - Resample to a common resolution before map algebra.

3. **What if a classification has low kappa (< 0.4)?**
   - Poor classification — retrain with better training data or different features.

---

## D. Comparison Questions

| Concept A | Concept B | Key Difference |
|-----------|-----------|----------------|
| Vector | Raster | Discrete vs continuous |
| IDW | Kriging | Deterministic vs geostatistical |
| Supervised | Unsupervised | Training data vs clustering |
| GPS | NavIC | Global vs Indian regional |
| SPP | RTK | Code vs carrier phase |

---

## E. Numerical Questions

1. **Find UTM zone** for 82°E. → 44N
2. **Find NDVI** for NIR = 0.5, Red = 0.2. → 0.43
3. **Find kappa** for $p_o = 0.85$, $p_e = 0.4$. → 0.75
4. **Find position error** for UERE = 2 m, GDOP = 3. → 6 m

---

## F. Rapid-Fire Questions

1. NDVI formula? → $(NIR - Red)/(NIR + Red)$
2. UTM scale factor? → 0.9996
3. RTK accuracy? → 1–2 cm
4. NavIC satellites? → 7
5. Sentinel-2 revisit? → 5 days
6. Largest GNSS error? → Ionospheric delay
7. Kappa range? → -1 to +1
8. IDW power typical? → 2

---

## High-Value Interview Answers

### High-Value Q1: "How would you map flood inundation using remote sensing?"

**30-second answer:**
"Acquire pre- and post-flood Sentinel-1 SAR imagery (all-weather, day/night). Apply radiometric and geometric correction, then classify water pixels using thresholding or change detection. Compute NDWI for optical data if available. Delineate the inundation extent, overlay with population and infrastructure layers in GIS for risk assessment, and validate with field data."

### High-Value Q2: "What is the difference between supervised and unsupervised classification?"

**30-second answer:**
"Supervised classification uses labeled training data — the analyst defines classes (e.g., water, urban, forest) and the algorithm (maximum likelihood, SVM, Random Forest) assigns pixels. Unsupervised classification (ISODATA, K-means) clusters pixels automatically without training data, and the analyst labels the resulting clusters afterward."

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`geoinformatics.md`](geoinformatics.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Transportation | [`../transportation/transportation-engineering.md`](../transportation/transportation-engineering.md) |
| Environmental | [`../environmental/environmental-engineering.md`](../environmental/environmental-engineering.md) |
| Water Resources | [`../hwre/water_resources/water-resources-engineering.md`](../hwre/water_resources/water-resources-engineering.md) |
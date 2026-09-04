# GIS / Survey Engineer — Role Study Plan

> **Role:** GIS / Survey Engineer
> **Tier:** B — Important Alternatives
> **Current Score:** 57/80 (71%) → **Target: ≥64/80 (80%)**
> **Track:** Core Civil (Survey of India, ISRO, NHAI, urban planning, geospatial consultancies)

---

## Why This Role?

Geospatial technology is transforming civil engineering. GIS, remote sensing, and GNSS are used in urban planning, transportation, water resources, disaster management, and land administration. India's National Geospatial Policy 2022 and the Geospatial Data Infrastructure are creating massive demand for GIS/survey engineers. Companies like Esri, Hexagon, Trimble, and Indian agencies (Survey of India, ISRO, NRSC) hire geospatial engineers. This is a high-growth, specialized role.

**Why you specifically need this:**
- Survey of India and ISRO recruit geospatial engineers
- NHAI and urban planning bodies need GIS for corridor and land-use analysis
- Consulting firms (AECOM, WSP) use GIS for environmental and transport studies
- Strong overlap with water resources (watershed delineation) and transportation (network analysis)

---

## Topic 1: GIS Fundamentals & Spatial Analysis

### Why This Topic?
Every GIS interview starts with data models, coordinate systems, and spatial analysis operations. You must understand vector vs raster, projections, and core analysis tools.

### What to Learn

- [ ] **GIS data models:** Vector (points, lines, polygons), Raster (grid cells), TIN, CAD
  - Vector: boundaries, roads, buildings (discrete features)
  - Raster: elevation, satellite imagery, land cover (continuous surfaces)
- [ ] **Coordinate systems:**
  - Geographic (lat/long, WGS 84 EPSG:4326)
  - Projected (UTM, Lambert Conformal Conic)
  - Indian CRS: UTM zones 43N-45N, Everest 1830, WGS 84
  - UTM zone = floor((Longitude+180)/6) + 1
- [ ] **Spatial analysis operations:** Buffer, clip, overlay, interpolation, network analysis, proximity, zonal statistics, dissolve
- [ ] **Spatial interpolation:** IDW, Kriging, nearest neighbor, trend surface, natural neighbor
  - IDW: Z_p = Σw_i·Z_i/Σw_i, w_i = 1/d_i^p (p = 2 typically)
  - Kriging: weighted by semivariogram (nugget, sill, range)
- [ ] **Raster analysis:** Map algebra, reclassification, conditional, neighborhood, hydrological
- [ ] **DEM derivatives:** Slope, aspect, hillshade, curvature, watershed, stream network
- [ ] **Database fundamentals:** Primary/foreign keys, attribute tables, spatial index (R-tree), topology, SQL spatial queries

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`geoinformatics.md`](geoinformatics.md) | §1 GIS (lines 11-124) | 114 |
| [`gis-tech.md`](../../software-and-tech/gis/gis-tech.md) | GIS software tools | — |
| [`transportation-engineering.md`](../transportation/transportation-engineering.md) | GIS for transport | 642 |

### Worked Example: UTM Zone + IDW Interpolation

**Problem:** A point is at longitude 81°E, latitude 26°N. (a) Find its UTM zone. (b) Interpolate the value at a point using IDW from 3 known points.

**Solution (a):**
1. UTM zone = floor((81 + 180)/6) + 1 = floor(261/6) + 1 = floor(43.5) + 1 = 43 + 1 = **Zone 44N**
2. (81°E is between 78°E-84°E → Zone 44N, consistent with EPSG:32644)

**Solution (b):**
1. Given points: A(100) at d=2 km, B(80) at d=3 km, C(120) at d=4 km, p = 2
2. Weights: w_A = 1/2² = 0.25, w_B = 1/3² = 0.111, w_C = 1/4² = 0.0625
3. Z_p = (0.25×100 + 0.111×80 + 0.0625×120)/(0.25 + 0.111 + 0.0625)
4. Z_p = (25 + 8.89 + 7.5)/0.4235 = 41.39/0.4235 = **97.7**

### Practice

**Basic (3-5):**
1. What is the difference between vector and raster data?
2. Find the UTM zone for longitude 88°E. [Answer: Zone 45N]
3. What is the difference between geographic and projected coordinate systems?
4. Name 4 spatial analysis operations and their applications.

**Intermediate (3-5):**
5. Compare IDW and Kriging. When would you use each?
6. A DEM has 30 m resolution. What is the slope at a pixel if Δz/Δx = 0.1 and Δz/Δy = 0.2?
7. Write a SQL query to select all parcels within 500 m of a well.

**Interview-Level (5+):**
8. What is the difference between a datum and a projection? Why does it matter?
9. How would you delineate a watershed from a DEM?
10. What is topology and why is it important in GIS?
11. How do you handle data from different coordinate systems in one project?
12. What is the difference between spatial and attribute queries?

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | What is the difference between vector and raster data? | Fundamentals |
| Q2 | Explain the UTM coordinate system. | Fundamentals |
| Q3 | What is spatial interpolation and when is it used? | Applied |
| Q4 | How do you perform a buffer analysis? | Fundamentals |
| Q5 | What is the difference between IDW and Kriging? | Applied |
| Q6 | How would you create a flood risk map using GIS? | Deep |

### Common Mistakes

1. **Confusing datum and projection** — Datum defines the reference ellipsoid; projection maps 3D to 2D
2. **Using wrong UTM zone** — Zone depends on longitude; India spans zones 43N-45N
3. **Ignoring coordinate system mismatch** — Layers in different CRS won't align
4. **Using IDW when Kriging is needed** — IDW is simpler but doesn't account for spatial autocorrelation

### Completion Criterion

- [ ] Can explain vector vs raster with examples
- [ ] Can compute UTM zone from longitude
- [ ] Can perform IDW interpolation
- [ ] Understands spatial analysis operations

---

## Topic 2: Remote Sensing & Image Processing

### Why This Topic?
Remote sensing is core to GIS roles. You must understand the electromagnetic spectrum, spectral indices, satellite platforms, and image classification.

### What to Learn

- [ ] **Electromagnetic spectrum bands:** UV, Visible, NIR, SWIR, Thermal, Microwave
  - NIR (0.76-0.90 µm): vegetation, water boundaries
  - Thermal IR (8-14 µm): land surface temperature
  - Microwave (SAR): all-weather mapping
- [ ] **Spectral indices:**
  - NDVI = (NIR - Red)/(NIR + Red) — vegetation
  - NDWI = (Green - NIR)/(Green + NIR) — water
  - NDBI = (SWIR - NIR)/(SWIR + NIR) — built-up
  - MNDWI = (Green - SWIR)/(Green + SWIR) — water (better)
  - SAVI = (NIR-Red)/(NIR+Red+L)×(1+L), L=0.5
- [ ] **Satellite platforms:** Landsat (30m), Sentinel-2 (10m), Sentinel-1 SAR, IRS-P6, Cartosat, ALOS, SRTM
- [ ] **Image processing:** Radiometric correction, geometric correction, enhancement, classification
  - Supervised: Maximum likelihood, SVM, Random Forest
  - Unsupervised: ISODATA, K-means
- [ ] **Classification accuracy:** Overall accuracy, Kappa coefficient, producer's/user's accuracy
- [ ] **Change detection:** Post-classification, image differencing, NDVI time series

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`geoinformatics.md`](geoinformatics.md) | §2 Remote Sensing (lines 126-198) | 73 |
| [`geoinformatics.md`](geoinformatics.md) | §4 Image Processing (lines 289-347) | 59 |

### Worked Example: NDVI + Classification Accuracy

**Problem:** (a) A pixel has Red = 0.2 and NIR = 0.5. Compute NDVI and classify the land cover. (b) A confusion matrix has 80 correct out of 100 total pixels, with expected agreement p_e = 0.4. Compute overall accuracy and Kappa.

**Solution (a):**
1. NDVI = (0.5 - 0.2)/(0.5 + 0.2) = 0.3/0.7 = **0.43**
2. NDVI = 0.43 → Dense vegetation (0.4-0.8 range)

**Solution (b):**
1. Overall accuracy = 80/100 = **80%**
2. Kappa = (p_o - p_e)/(1 - p_e) = (0.80 - 0.40)/(1 - 0.40) = 0.40/0.60 = **0.667**

### Practice

**Basic (3-5):**
1. Compute NDVI for Red = 0.3, NIR = 0.6. [Answer: 0.333]
2. What is the difference between supervised and unsupervised classification?
3. Name 3 satellite platforms and their resolutions.
4. What does the thermal infrared band measure?

**Intermediate (3-5):**
5. A confusion matrix has 90 correct out of 120, p_e = 0.5. Find Kappa. [Answer: 0.667]
6. Explain the difference between radiometric and geometric correction.
7. How would you detect urban expansion using satellite imagery?

**Interview-Level (5+):**
8. Why is SAR useful for flood mapping even in cloudy conditions?
9. What is the difference between NDVI and SAVI? When would you use SAVI?
10. How do you validate a land cover classification?
11. What is pan-sharpening and why is it used?
12. How does atmospheric correction affect NDVI values?

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | What is NDVI and how is it calculated? | Fundamentals |
| Q2 | Explain the difference between supervised and unsupervised classification. | Fundamentals |
| Q3 | What is the Kappa coefficient? | Applied |
| Q4 | How do you perform change detection? | Applied |
| Q5 | Why is SAR useful for flood mapping? | Deep |
| Q6 | What is the electromagnetic spectrum and why does it matter? | Fundamentals |

### Common Mistakes

1. **Wrong NDVI formula** — It's (NIR-Red)/(NIR+Red), not the reverse
2. **Confusing NDWI and MNDWI** — MNDWI uses SWIR instead of NIR
3. **Ignoring atmospheric effects** — Raw DN values need correction before index computation
4. **Using only overall accuracy** — Kappa and per-class accuracy matter too

### Completion Criterion

- [ ] Can compute NDVI, NDWI, NDBI from band values
- [ ] Knows major satellite platforms and resolutions
- [ ] Understands supervised vs unsupervised classification
- [ ] Can compute Kappa coefficient

---

## Topic 3: GNSS & Surveying

### Why This Topic?
GNSS (GPS, NavIC) and surveying are the practical tools of a GIS/survey engineer. You must understand positioning methods, error sources, and applications.

### What to Learn

- [ ] **GNSS constellations:** GPS (USA), GLONASS (Russia), Galileo (EU), BDS (China), NavIC (India)
  - NavIC: 7 satellites (5 GEO + 2 GSO), L5 + S1 bands, India + 1500 km
- [ ] **Positioning methods:**
  - SPP: 2-10 m, DGPS: 0.5-2 m, RTK: 1-2 cm, PPK: 1-2 cm, PPP: 5-10 cm
- [ ] **Error sources:** Ionosphere (2-50 m), troposphere, multipath, orbit, clock, receiver noise
  - Position error = UERE × GDOP
- [ ] **GDOP:** 1-2 excellent, 2-5 good, 5-10 moderate, >10 poor
- [ ] **DGPS principle:** Base station correction, effective within ~300 km
- [ ] **Coordinate conversions:** WGS 84 to UTM (Transverse Mercator, k₀ = 0.9996, false easting 500,000 m)
- [ ] **Surveying applications:** Topographic survey, deformation monitoring, construction staking, hydrographic survey

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`geoinformatics.md`](geoinformatics.md) | §3 GNSS (lines 201-286) | 86 |
| [`gis-tech.md`](../../software-and-tech/gis/gis-tech.md) | Surveying tools | — |

### Worked Example: DGPS Correction

**Problem:** A base station at known position (X = 500,000 m, Y = 4,000,000 m) measures (X' = 500,002.5, Y' = 4,000,001.8). A rover measures (X_r = 501,000, Y_r = 4,001,500). Apply the DGPS correction.

**Solution:**
1. Correction: C_x = 500,000 - 500,002.5 = -2.5 m, C_y = 4,000,000 - 4,000,001.8 = -1.8 m
2. Corrected rover: X = 501,000 + (-2.5) = **500,997.5 m**, Y = 4,001,500 + (-1.8) = **4,001,498.2 m**
3. The correction removes common errors (ionosphere, troposphere, satellite clock) within ~300 km

### Practice

**Basic (3-5):**
1. Name the 5 GNSS constellations and their countries.
2. What is the accuracy of RTK vs DGPS?
3. What is GDOP and what values are acceptable for surveying?
4. Name 3 GNSS error sources.

**Intermediate (3-5):**
5. A rover measures (X=600,000, Y=3,500,000). Base correction is (-3.2, +1.5). Find corrected position.
6. Why is RTK more accurate than DGPS?
7. What is the difference between SPP and PPP?

**Interview-Level (5+):**
8. How does multipath affect GNSS accuracy and how do you mitigate it?
9. What is the role of NavIC in Indian surveying?
10. How would you set up a deformation monitoring system for a dam?
11. What is the difference between geodetic and topographic surveying?
12. How do you achieve cm-level accuracy in GNSS?

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | What is the difference between GPS and GNSS? | Fundamentals |
| Q2 | Explain RTK positioning. | Applied |
| Q3 | What are the main GNSS error sources? | Fundamentals |
| Q4 | What is NavIC and why is it important for India? | Applied |
| Q5 | How do you achieve cm-level accuracy? | Deep |
| Q6 | What is GDOP and how does it affect accuracy? | Applied |

### Common Mistakes

1. **Confusing SPP and RTK** — SPP is code-based (m-level), RTK is carrier-phase (cm-level)
2. **Ignoring multipath** — Buildings and trees cause signal reflection
3. **Using wrong GDOP threshold** — Surveying needs GDOP < 2
4. **Forgetting NavIC** — India's own system is a key interview point

### Completion Criterion

- [ ] Can explain all GNSS constellations including NavIC
- [ ] Can apply DGPS correction
- [ ] Understands error sources and mitigation
- [ ] Knows positioning method accuracies

---

## Topic 4: Geospatial Applications in Civil Engineering

### Why This Topic?
This connects GIS/RS/GNSS to real civil engineering problems — the key differentiator in interviews. You must show how geospatial tools solve engineering problems.

### What to Learn

- [ ] **Flood mapping:** Sentinel-1 SAR, Sentinel-2 NDWI/MNDWI, Landsat, MODIS
- [ ] **Urban heat island (UHI):** LST from thermal band, SVF, air temperature transects
- [ ] **LULC classification:** Water, built-up, bare soil, sparse/dense vegetation (NDVI ranges)
- [ ] **Watershed delineation:** Flow direction → flow accumulation → outlet → watershed
- [ ] **Transportation planning:** Route optimization (Dijkstra), traffic modeling, accessibility (isochrones)
- [ ] **Water resources:** Groundwater potential mapping, reservoir monitoring, irrigation planning
- [ ] **Disaster management:** Flood, landslide, earthquake risk mapping
- [ ] **Land administration:** Cadastral mapping, land records digitization (SVAMITVA scheme)

### Study Material

| File | What to Study | Lines |
|:-----|:-------------|:------|
| [`geoinformatics.md`](geoinformatics.md) | §5, §6 Applications (lines 350-400+) | ~50 |
| [`hydrology.md`](../hwre/hydrology/hydrology.md) | Watershed modeling | 587 |
| [`transportation-engineering.md`](../transportation/transportation-engineering.md) | Transport GIS | 642 |

### Worked Example: Watershed Delineation Workflow

**Problem:** Describe the complete GIS workflow to delineate a watershed and estimate its area for a given outlet.

**Solution:**
1. **DEM acquisition:** SRTM (30 m) or Cartosat DEM
2. **Fill sinks:** Remove depressions that block flow (Fill tool)
3. **Flow direction:** D8 algorithm — assign each cell a direction to steepest downslope neighbor
4. **Flow accumulation:** Sum of cells draining to each cell
5. **Define outlet:** Select the pour point (downstream point of interest)
6. **Watershed tool:** Delineate the contributing area above the outlet
7. **Convert to polygon:** Raster to polygon for area calculation
8. **Area estimation:** Use zonal statistics / polygon area in projected CRS (UTM)
9. **Validate:** Compare with field survey / stream network

### Practice

**Basic (3-5):**
1. What is the D8 flow direction algorithm?
2. Name 3 geospatial applications in water resources.
3. What is the SVAMITVA scheme?
4. How do you map flood extent using SAR?

**Intermediate (3-5):**
5. Describe the workflow to create a groundwater potential map.
6. How would you use GIS for urban heat island analysis?
7. What is an isochrone map and how is it used in transport planning?

**Interview-Level (5+):**
8. How would you combine GIS and hydrology to model flood risk?
9. What is the role of geospatial technology in smart cities?
10. How do you assess the accuracy of a watershed delineation?
11. What are the challenges of using satellite data in India (cloud cover, resolution)?
12. How would you digitize land records for a district?

### Interview Questions

| Q# | Question | Depth |
|:---|:---------|:------|
| Q1 | How do you delineate a watershed in GIS? | Applied |
| Q2 | What is the role of GIS in disaster management? | Applied |
| Q3 | How do you map urban heat islands? | Applied |
| Q4 | What is the SVAMITVA scheme? | Fundamentals |
| Q5 | How would you use remote sensing for flood monitoring? | Deep |
| Q6 | What are the applications of GIS in transportation? | Applied |

### Common Mistakes

1. **Not filling sinks** — Sinks block flow and corrupt watershed delineation
2. **Using geographic CRS for area** — Always project to UTM for accurate area
3. **Ignoring cloud cover** — Optical imagery fails in monsoon; use SAR
4. **Not validating results** — Always field-check GIS outputs

### Completion Criterion

- [ ] Can describe watershed delineation workflow
- [ ] Knows flood mapping methods (SAR + optical)
- [ ] Understands LULC classification
- [ ] Can apply GIS to transport and water resources

---

## Mock Test (45 minutes, 100 marks)

| Q# | Topic | Marks | Difficulty |
|:---|:------|:-----:|:-----------|
| Q1 | Explain vector vs raster data with examples. | 10 | Basic |
| Q2 | Compute UTM zone for longitude 85°E. | 8 | Basic |
| Q3 | IDW interpolation from 3 points. | 12 | Intermediate |
| Q4 | Compute NDVI and classify land cover. | 10 | Basic |
| Q5 | Kappa coefficient from confusion matrix. | 12 | Intermediate |
| Q6 | DGPS correction application. | 10 | Intermediate |
| Q7 | Describe watershed delineation workflow. | 15 | Applied |
| Q8 | Compare RTK, DGPS, and PPP accuracy. | 10 | Interview |
| Q9 | How would you map flood extent using SAR? | 13 | Deep |

**Total: 100 marks | Time: 45 minutes | Pass: 60 marks**

---

## Interview Strategy

### Round Structure (Typical PSU / Geospatial Company)

| Round | Focus | Preparation |
|:------|:------|:------------|
| **Round 1: Written/Aptitude** | Quantitative + Technical basics | GIS concepts, formulas |
| **Round 2: Technical** | Software skills, applications | ArcGIS/QGIS, spatial analysis |
| **Round 3: HR** | Behavioral, fit, salary | STAR stories, company research |

### Company-Specific Navigation

| Company | Key Focus Areas | Study Priority |
|:--------|:---------------|:--------------|
| **Survey of India** | Geodetic surveying, GNSS, national mapping | Topics 3, 4 |
| **ISRO / NRSC** | Remote sensing, image processing, satellite data | Topics 2, 4 |
| **NHAI** | Corridor mapping, land acquisition, GIS | Topics 1, 4 |
| **Esri / Hexagon / Trimble** | GIS software, spatial analysis, LiDAR | Topics 1, 2 |
| **AECOM / WSP** | Environmental GIS, transport modeling | Topics 1, 4 |
| **Urban planning bodies** | LULC, UHI, smart city | Topics 2, 4 |

### Behavioral Prep

Prepare 3 STAR stories for GIS context:
1. **Technical challenge:** Building a GIS model for a project
2. **Field work:** Conducting a GNSS survey
3. **Learning:** Mastering a new GIS software (QGIS, ArcGIS, Python)

---

## Cross-Links

- [`geoinformatics.md`](geoinformatics.md) — Full subject reference (779 lines)
- [`gis-tech.md`](../../software-and-tech/gis/gis-tech.md) — GIS software tools
- [`hydrology.md`](../hwre/hydrology/hydrology.md) — Watershed modeling
- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — Transport GIS
- [`water-resources-engineering.md`](../hwre/water_resources/water-resources-engineering.md) — Water resources applications
- [`environmental-engineering.md`](../environmental/environmental-engineering.md) — Environmental monitoring
- [`technical-interview-bank.md`](../../prep/interview/technical/technical-interview-bank.md) — 100+ interview questions
- [`company-profiles.md`](../../prep/company-profiles/company-profiles.md) — Company-specific strategies

---

## References

- National Geospatial Policy 2022 (India)
- ISRO / NRSC documentation
- Esri ArcGIS documentation
- QGIS documentation
- Burrough & McDonnell — Principles of Geographical Information Systems
- Lillesand & Kiefer — Remote Sensing and Image Interpretation
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

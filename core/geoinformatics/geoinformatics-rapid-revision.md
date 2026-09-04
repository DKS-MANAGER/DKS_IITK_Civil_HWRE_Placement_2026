# Geoinformatics (GIS / RS / GNSS) — Rapid Revision Sheet

> Last-minute cheat sheet for GIS/Survey Engineer interviews and exams.

---

## Framework 1: GIS Data Models & Coordinate Systems

### Data Models

| Model | Description | Best For |
|:------|:------------|:---------|
| Vector | Points, lines, polygons | Boundaries, roads, buildings |
| Raster | Grid cells (pixels) | Elevation, imagery, land cover |
| TIN | Triangulated network | Terrain modeling |
| CAD | Drawing primitives | Engineering drawings |

### Coordinate Systems

| Type | Example | Description |
|:-----|:--------|:------------|
| Geographic | WGS 84 (EPSG:4326) | Angular (lat/long) |
| Projected | UTM, Lambert | Cartesian (planar) |

**UTM zone:** Zone = floor((Longitude + 180)/6) + 1

**Indian UTM zones:**
- Zone 43N (EPSG:32643): 78°E-84°E
- Zone 44N (EPSG:32644): 84°E-90°E
- Zone 45N (EPSG:32645): 90°E-96°E

**UTM parameters:** k₀ = 0.9996, false easting = 500,000 m, false northing = 0 (N) / 10,000,000 (S)

### Spatial Analysis Operations

| Operation | Application |
|:----------|:------------|
| Buffer | Noise buffer, flood risk zone |
| Clip | Study area extraction |
| Overlay | Land use + soil = suitability |
| Interpolation | Rainfall, groundwater |
| Network analysis | Route, allocation |
| Proximity | Facility location |
| Zonal statistics | Avg elevation per watershed |
| Dissolve | Merge adjacent features |

### Spatial Interpolation

| Method | Principle | Accuracy |
|:-------|:----------|:---------|
| IDW | Z_p = Σw_i·Z_i/Σw_i, w_i = 1/d_i^p | Moderate |
| Kriging | Weighted by semivariogram | High |
| Nearest neighbor | Assign nearest value | Low |
| Natural neighbor | Voronoi-based | Mod-High |

**Kriging semivariogram:** γ(h) = C₀ + C[1 - exp(-3h/a)]
- C₀ = nugget, C = sill, a = range

---

## Framework 2: Remote Sensing & Spectral Indices

### Electromagnetic Spectrum

| Band | Wavelength | Application |
|:-----|:-----------|:------------|
| Visible Blue | 0.45-0.52 µm | Water body mapping |
| Visible Green | 0.52-0.60 µm | Vegetation health |
| Visible Red | 0.63-0.69 µm | Urban, soil |
| NIR | 0.76-0.90 µm | Vegetation, water |
| SWIR | 1.55-1.75 µm | Soil moisture |
| Thermal IR | 8-14 µm | Land surface temp |
| Microwave | 1mm-1m | All-weather (SAR) |

### Spectral Indices (MEMORIZE)

| Index | Formula | Use |
|:------|:--------|:----|
| **NDVI** | (NIR - Red)/(NIR + Red) | Vegetation |
| **NDWI** | (Green - NIR)/(Green + NIR) | Water |
| **NDBI** | (SWIR - NIR)/(SWIR + NIR) | Built-up |
| **MNDWI** | (Green - SWIR)/(Green + SWIR) | Water (better) |
| **SAVI** | (NIR-Red)/(NIR+Red+L)×(1+L), L=0.5 | Sparse vegetation |

### LULC NDVI Ranges

| Class | NDVI |
|:------|:-----|
| Water | < 0.0 |
| Built-up | 0.0-0.15 |
| Bare soil | 0.1-0.2 |
| Sparse veg | 0.2-0.4 |
| Dense veg | 0.4-0.8 |

### Satellite Platforms

| Satellite | Resolution | Revisit | Use |
|:----------|:-----------|:--------|:----|
| Landsat 8/9 | 30m MS, 15m Pan | 16 days | Regional |
| Sentinel-2 | 10m MS | 5 days | Land cover |
| Sentinel-1 | 5-20m SAR | 6-12 days | Flood, deformation |
| Cartosat-1 | 2.5m Pan | 5 days | DEM, cadastral |
| SRTM | 30m | Static | Global DEM |

### Classification Accuracy

| Metric | Formula |
|:-------|:--------|
| Overall accuracy | Σdiagonal/total × 100% |
| Kappa | (p_o - p_e)/(1 - p_e) |
| Producer's | n_ii/column total (omission) |
| User's | n_ii/row total (commission) |

---

## Framework 3: GNSS & Surveying

### GNSS Constellations

| System | Country | Satellites |
|:-------|:--------|:-----------|
| GPS | USA | 31 |
| GLONASS | Russia | 24 |
| Galileo | EU | 30 |
| BDS (BeiDou) | China | 45 |
| **NavIC (IRNSS)** | **India** | **7** |

**NavIC:** 5 GEO + 2 GSO, L5 + S1 bands, covers India + 1500 km

### Positioning Methods

| Method | Accuracy |
|:-------|:---------|
| SPP | 2-10 m |
| DGPS | 0.5-2 m |
| RTK | 1-2 cm |
| PPK | 1-2 cm |
| PPP | 5-10 cm |
| Network RTK (VRS) | 1-3 cm |

### Error Sources

| Error | Magnitude (m) |
|:------|:--------------|
| Ionosphere | 2-50 |
| Troposphere | 0.5-5 |
| Multipath | 0.5-5 |
| Orbit | 1-5 |
| Clock | 1-3 |
| Receiver noise | 0.1-1 |

**Position error = UERE × GDOP**

### GDOP Quality

| GDOP | Quality |
|:----:|:--------|
| 1-2 | Excellent (surveying) |
| 2-5 | Good |
| 5-10 | Moderate |
| >10 | Poor |

### DGPS Principle
- Base station correction: C_i = P_known - P_measured
- Rover: P_corrected = P_raw + C_i
- Effective within ~300 km

---

## Framework 4: Geospatial Applications

### Watershed Delineation Workflow
1. DEM acquisition (SRTM/Cartosat)
2. Fill sinks
3. Flow direction (D8)
4. Flow accumulation
5. Define outlet (pour point)
6. Watershed tool
7. Raster → polygon
8. Area in projected CRS (UTM)

### Flood Mapping

| Sensor | Method |
|:-------|:-------|
| Sentinel-1 SAR | Backscatter change detection |
| Sentinel-2 | NDWI/MNDWI |
| Landsat | Water index |
| MODIS | Daily surface water |

### LST (Urban Heat Island)
$$LST = \frac{T_b}{1 + \left(\frac{\lambda T_b}{\rho}\right)\ln\varepsilon}$$

### DEM Derivatives
- Slope: β = arctan√((Δz/Δx)² + (Δz/Δy)²)
- Aspect: direction of steepest descent
- Hillshade: solar illumination
- Watershed: flow direction → accumulation → outlet

### Photogrammetry GSD
$$GSD = \frac{H \cdot p}{f}$$

---

## Quick-Fire Interview Answers

**Q1: What is the difference between vector and raster data?**
A: Vector stores discrete features as points, lines, and polygons with coordinates. Raster stores continuous surfaces as a grid of cells (pixels). Vector is best for boundaries and roads; raster for elevation and imagery. Vector is resolution-independent; raster resolution depends on cell size.

**Q2: What is the difference between a datum and a projection?**
A: A datum defines the reference ellipsoid and its position relative to the Earth (e.g., WGS 84, Everest 1830). A projection is a mathematical transformation that maps the 3D Earth surface to a 2D plane (e.g., UTM, Lambert). You need both to define a coordinate system.

**Q3: What is NDVI and how is it used?**
A: NDVI = (NIR - Red)/(NIR + Red), ranging from -1 to +1. It measures vegetation density because healthy vegetation strongly reflects NIR and absorbs Red. Values: water < 0, built-up 0-0.15, dense vegetation 0.4-0.8. Used for vegetation monitoring, drought assessment, and land cover classification.

**Q4: What is the difference between RTK and DGPS?**
A: DGPS uses code-phase measurements with base station corrections, giving 0.5-2 m accuracy. RTK uses carrier-phase measurements with real-time corrections, giving 1-2 cm accuracy. RTK is much more accurate but requires a nearby base station or network.

**Q5: What is NavIC and why is it important?**
A: NavIC (Navigation with Indian Constellation) is India's regional GNSS with 7 satellites (5 GEO + 2 GSO). It provides positioning over India and 1500 km beyond. It's important for national security, strategic independence, and applications like surveying, disaster management, and vehicle tracking.

**Q6: What is the Kappa coefficient?**
A: Kappa measures classification accuracy beyond chance agreement: κ = (p_o - p_e)/(1 - p_e). κ = 1 is perfect, κ = 0 is chance-level. It's more robust than overall accuracy because it accounts for random agreement.

**Q7: Why is SAR useful for flood mapping?**
A: SAR (Synthetic Aperture Radar) uses microwave signals that penetrate clouds and work day/night. This is critical in monsoon conditions when optical imagery is blocked by clouds. SAR detects water by its low backscatter (smooth surface), enabling flood extent mapping during active flooding.

**Q8: How do you delineate a watershed?**
A: (1) Fill sinks in the DEM, (2) compute flow direction (D8), (3) compute flow accumulation, (4) define the outlet/pour point, (5) use the watershed tool to delineate the contributing area, (6) convert to polygon and compute area in a projected CRS.

**Q9: What is the difference between supervised and unsupervised classification?**
A: Supervised classification uses training data (known pixels) to classify the image (Maximum Likelihood, SVM, Random Forest). Unsupervised classification groups pixels by spectral similarity without training data (ISODATA, K-means). Supervised is more accurate but requires ground truth.

**Q10: What is the SVAMITVA scheme?**
A: SVAMITVA is India's scheme to map rural land parcels using drone surveys and GIS, providing property cards to villagers. It uses drone photogrammetry, georeferencing, and GIS to create village maps, enabling land record digitization and rural planning.

---

## Last-Minute Checklist

- [ ] Vector vs raster data models
- [ ] UTM zone calculation + Indian zones
- [ ] Datum vs projection
- [ ] Spatial analysis operations
- [ ] IDW and Kriging interpolation
- [ ] NDVI, NDWI, NDBI, MNDWI formulas
- [ ] Satellite platforms and resolutions
- [ ] Supervised vs unsupervised classification
- [ ] Kappa coefficient
- [ ] GNSS constellations (incl. NavIC)
- [ ] RTK vs DGPS vs PPP accuracy
- [ ] GDOP thresholds
- [ ] Watershed delineation workflow
- [ ] Flood mapping (SAR + optical)
- [ ] DEM derivatives (slope, aspect)

---

## Cross-Links

- [`geoinformatics.md`](geoinformatics.md) — Full subject reference
- [`role-study-plan.md`](role-study-plan.md) — Detailed study plan with worked examples
- [`gis-tech.md`](../../software-and-tech/gis/gis-tech.md) — GIS software tools
- [`hydrology.md`](../hwre/hydrology/hydrology.md) — Watershed modeling
- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — Transport GIS

---

## References

- National Geospatial Policy 2022 (India)
- ISRO / NRSC documentation
- Esri ArcGIS, QGIS documentation
- Burrough & McDonnell — Principles of GIS
- Lillesand & Kiefer — Remote Sensing and Image Interpretation
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)

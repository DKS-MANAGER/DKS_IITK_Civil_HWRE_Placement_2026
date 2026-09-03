# Geoinformatics

## Scope

Geoinformatics encompasses Geographic Information Systems (GIS), Remote Sensing (RS), Global Navigation Satellite Systems (GNSS), spatial analysis, and digital image processing — applying geospatial technology to civil engineering problems including urban planning, transportation network analysis, environmental monitoring, water resources management, and disaster risk assessment.

> **Related topics:** [`geotechnical.md`](../geotechnical/geotechnical.md) · [`transportation-engineering.md`](../transportation/transportation-engineering.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) · [`environmental-engineering.md`](../environmental/environmental-engineering.md)

---

## 1. Geographic Information Systems (GIS)

### GIS Data Models

| Model | Description | Storage | Best For |
|-------|-------------|---------|----------|
| **Vector** | Points, lines, polygons | Coordinates | Boundaries, roads, buildings |
| **Raster** | Grid cells (pixels) | Rows × columns | Elevation, satellite imagery, land cover |
| **TIN** | Triangulated irregular network | Triangles | Terrain modeling (DEM) |
| **CAD** | Drawing primitives | Geometric objects | Engineering drawings |

**Vector data structures:**

| Type | Example | Attributes |
|------|---------|------------|
| Point | Well locations, survey markers | ID, coordinates, elevation |
| Line | Roads, pipelines, rivers | Length, name, capacity |
| Polygon | Land parcels, watersheds | Area, land use, population |

### Coordinate Systems

| Type | Example | Description |
|------|---------|-------------|
| Geographic (lat/long) | WGS 84 (EPSG:4326) | Angular coordinates on ellipsoid |
| Projected (planar) | UTM, Lambert Conformal Conic | Cartesian coordinates on flat surface |
| State Plane | NAD83 / State Plane Zones | High accuracy within zone |

**Common Indian CRS:**

| Name | EPSG Code | Use |
|------|-----------|-----|
| WGS 84 / UTM Zone 43N | EPSG:32643 | Most of India (78°E–84°E) |
| WGS 84 / UTM Zone 44N | EPSG:32644 | Eastern India (84°E–90°E) |
| WGS 84 / UTM Zone 45N | EPSG:32645 | Northeast India (90°E–96°E) |
| Everest 1830 (India) | EPSG:4243 | Legacy Indian datum |
| WGS 84 | EPSG:4326 | GPS default |

**UTM zone calculation:**
$$\text{Zone} = \text{floor}\left(\frac{\text{Longitude} + 180}{6}\right) + 1$$

### Spatial Analysis Operations

| Operation | Description | Application |
|-----------|-------------|-------------|
| **Buffer** | Create zone around feature | Noise buffer, flood risk zone |
| **Clip** | Extract area within boundary | Study area extraction |
| **Overlay** | Combine two layers | Land use + soil type = suitability |
| **Interpolation** | Estimate values at unknown points | Rainfall, groundwater levels |
| **Network analysis** | Route, allocation, hierarchy | Transport routing, pipe networks |
| **Proximity analysis** | Distance, nearest neighbor | Facility location, accessibility |
| **Zonal statistics** | Statistics within zones | Average elevation per watershed |
| **Dissolve** | Merge adjacent features | Simplify administrative boundaries |

### Spatial Interpolation Methods

| Method | Formula / Principle | Accuracy | Data Requirement |
|--------|-------------------|----------|------------------|
| **Inverse Distance Weighting (IDW)** | $Z_p = \frac{\sum w_i Z_i}{\sum w_i}$, $w_i = 1/d_i^p$ | Moderate | Sample points |
| **Kriging** | $Z_p = \sum \lambda_i Z_i$ (weighted by semivariogram) | High | Sample points + variogram |
| **Nearest Neighbor** | Assign nearest sample value | Low | Sample points |
| **Trend Surface** | Polynomial regression on coordinates | Low–Moderate | Sample points |
| **Natural Neighbor** | Voronoi-based interpolation | Moderate–High | Sample points |

**IDW weighting:** Typically $p = 2$ (inverse square distance).

**Kriging semivariogram model:**
$$\gamma(h) = C_0 + C\left[1 - \exp\left(-\frac{3h}{a}\right)\right]$$

Where:
- $C_0$ = nugget variance
- $C$ = sill variance
- $a$ = range (correlation distance)

### Raster Analysis

| Operation | Description |
|-----------|-------------|
| Map algebra | Cell-by-cell arithmetic (+, -, ×, ÷) |
| Reclassification | Assign new values to ranges |
| Conditional | Logical tests (IF-THEN) |
| Neighborhood | Moving window (focal statistics) |
| Hydrological | Flow direction, flow accumulation, watershed delineation |

**Digital Elevation Model (DEM) applications:**

| Derivative | Method |
|------------|--------|
| Slope | $\beta = \arctan\sqrt{(\frac{\Delta z}{\Delta x})^2 + (\frac{\Delta z}{\Delta y})^2}$ |
| Aspect | Direction of steepest descent |
| Hillshade | Solar illumination modeling |
| Curvature | Convex/concave terrain characterization |
| Watershed | Flow direction → accumulation → outlet |
| Stream network | Threshold-based extraction from flow accumulation |

### Database Fundamentals for GIS

**Relational database concepts:**

| Concept | Description |
|---------|-------------|
| Primary key | Unique identifier for each record |
| Foreign key | Links to primary key in another table |
| Attribute table | Tabular data linked to spatial features |
| Spatial index | R-tree, Quad-tree for fast spatial queries |
| Topology | Spatial relationships (adjacency, connectivity, containment) |

**SQL for spatial queries:**
```sql
-- Select all parcels within a buffer
SELECT * FROM parcels
WHERE ST_DWithin(geom, ST_Buffer(well_location, 500), 500);
```

---

## 2. Remote Sensing (RS)

### Electromagnetic Spectrum

| Band | Wavelength | Application in Civil Eng. |
|------|-----------|---------------------------|
| UV | 0.01–0.4 µm | Air quality monitoring |
| Visible (Blue) | 0.45–0.52 µm | Water body mapping |
| Visible (Green) | 0.52–0.60 µm | Vegetation health |
| Visible (Red) | 0.63–0.69 µm | Urban, soil discrimination |
| Near-Infrared (NIR) | 0.76–0.90 µm | Vegetation, water boundaries |
| Short-wave IR (SWIR) | 1.55–1.75 µm | Soil moisture, mineralogy |
| Thermal IR | 8–14 µm | Land surface temperature |
| Microwave | 1 mm–1 m | All-weather mapping (SAR) |

### Spectral Indices

| Index | Formula | Use |
|-------|---------|-----|
| **NDVI** | $\frac{NIR - Red}{NIR + Red}$ | Vegetation density |
| **NDWI** | $\frac{Green - NIR}{Green + NIR}$ | Water body detection |
| **NDBI** | $\frac{SWIR - NIR}{SWIR + NIR}$ | Built-up area detection |
| **NDMI** | $\frac{NIR - SWIR}{NIR + SWIR}$ | Canopy moisture |
| **BSI** | $\frac{(SWIR + Red) - (NIR + Blue)}{(SWIR + Red) + (NIR + Blue)}$ | Bare soil |
| **SAVI** | $\frac{NIR - Red}{NIR + Red + L}(1+L)$, $L=0.5$ | Vegetation in sparse areas |

### Satellite Platforms

| Satellite | Resolution | Revisit | Best For |
|-----------|-----------|---------|----------|
| **Landsat 8/9** | 30 m (MS), 15 m (Pan) | 16 days | Regional land use, water resources |
| **Sentinel-2** | 10 m (MS), 20 m (SWIR) | 5 days | Land cover, vegetation, urban |
| **Sentinel-1** | 5–20 m (SAR) | 6–12 days | Flood mapping, ground deformation |
| **IRS-P6 (Resourcesat)** | 5.8 m (LISS-4), 23.5 m (LISS-3) | 24 days | Indian national mapping |
| **Cartosat-1** | 2.5 m (Pan) | 5 days | DEM generation, cadastral mapping |
| **ALOS-2 (PALSAR)** | 1–100 m (SAR) | 14 days | Earthquake deformation, forest |
| **SRTM DEM** | 30 m | Static | Global elevation model |
| **ASTER GDEM** | 30 m | Static | Global elevation model |

### Image Processing

| Technique | Description |
|-----------|-------------|
| **Radiometric correction** | Remove atmospheric effects (DN → TOA reflectance) |
| **Geometric correction** | Orthorectification, ground control points (GCPs) |
| **Enhancement** | Contrast stretch, filtering, PCA |
| **Classification (supervised)** | Maximum likelihood, SVM, Random Forest using training data |
| **Classification (unsupervised)** | ISODATA, K-means clustering |
| **Change detection** | Post-classification, image differencing, NDVI time series |

**Atmospheric correction (TOA reflectance):**
$$\rho = \frac{\pi \cdot L_\lambda \cdot d^2}{ESUN_\lambda \cdot \cos\theta_s}$$

Where:
- $L_\lambda$ = at-sensor radiance
- $d$ = Earth-Sun distance (AU)
- $ESUN_\lambda$ = mean solar exoatmospheric irradiance
- $\theta_s$ = solar zenith angle

**Maximum Likelihood Classification decision rule:**
$$g_i(x) = \ln P(\omega_i) - \frac{1}{2}\ln|\Sigma_i| - \frac{1}{2}(x - m_i)^T \Sigma_i^{-1}(x - m_i)$$

Classify pixel $x$ into class $\omega_i$ with maximum $g_i(x)$.

**Classification accuracy assessment:**

| Metric | Formula |
|--------|---------|
| Overall accuracy | $\frac{\sum \text{diagonal}}{\text{total pixels}} \times 100\%$ |
| Kappa coefficient | $\kappa = \frac{p_o - p_e}{1 - p_e}$ |
| Producer's accuracy | $\frac{n_{ii}}{\text{column total}_j}$ (omission error) |
| User's accuracy | $\frac{n_{ii}}{\text{row total}_i}$ (commission error) |

---

## 3. Global Navigation Satellite Systems (GNSS)

### GNSS Constellations

| System | Country | Satellites | Signal |
|--------|---------|-----------|--------|
| **GPS** | USA | 31 | L1 (1575.42 MHz), L2 (1227.60 MHz) |
| **GLONASS** | Russia | 24 | L1, L2 (FDMA + CDMA) |
| **Galileo** | EU | 30 | E1, E5a, E5b, E6 |
| **BDS (BeiDou)** | China | 45 | B1I, B2I, B3I |
| **NavIC (IRNSS)** | India | 7 | L5 (1176.45 MHz), S1 (2492.08 MHz) |

**Indian regional coverage (NavIC):** 5 geostationary + 2 geosynchronous satellites covering India and surrounding region (up to 1500 km from Indian boundary).

### Positioning Methods

| Method | Accuracy | Description |
|--------|----------|-------------|
| **Single point (SPP)** | 2–10 m | Standard GNSS receiver |
| **Differential (DGPS/DGNSS)** | 0.5–2 m | Base station correction |
| **RTK** | 1–2 cm | Real-time kinematic, carrier phase |
| **PPK** | 1–2 cm | Post-processed kinematic |
| **PPP** | 5–10 cm | Precise point positioning (IGS products) |
| **Network RTK (VRS)** | 1–3 cm | Virtual reference station from CORS |

### GNSS Error Sources

| Error Source | Magnitude (m) |
|-------------|---------------|
| Ionospheric delay | 2–50 |
| Tropospheric delay | 0.5–5 |
| Multipath | 0.5–5 |
| Satellite orbit | 1–5 |
| Satellite clock | 1–3 |
| Receiver noise | 0.1–1 |
| Geometric dilution of precision (GDOP) | Amplifier |

**GDOP concept:**
$$\text{Position error} = \text{UERE} \times \text{GDOP}$$

Where UERE = User Equivalent Range Error.

**GDOP categories:**

| GDOP | Quality | Suitability |
|------|---------|-------------|
| 1–2 | Excellent | Surveying |
| 2–5 | Good | General navigation |
| 5–10 | Moderate | Acceptable |
| > 10 | Poor | Unreliable |

### Coordinate Conversions

**WGS 84 to UTM (simplified):**
- Uses Transverse Mercator projection
- Central meridian scale factor: $k_0 = 0.9996$
- False easting: 500,000 m
- False northing: 0 (N) / 10,000,000 (S)

### GNSS Applications in Civil Engineering

| Application | Method | Accuracy |
|-------------|--------|----------|
| Topographic survey | RTK / PPK | 1–3 cm |
| Deformation monitoring | Static / PPP | 1–5 mm |
| Construction staking | RTK | 1–3 cm |
| Road alignment survey | RTK + total station | 1–3 cm |
| Hydrographic survey | DGPS + echo sounder | 0.5–1 m |
| Precision agriculture | DGPS/RTK | 1–10 cm |
| Geodetic control | Static GNSS | < 5 mm |

### Differential GPS (DGPS)

**Basic principle:**
- Base station at known position computes correction: $C_i = P_{known} - P_{measured}$
- Rover applies correction: $P_{corrected} = P_{raw} + C_i$
- Effective within ~300 km of base station (ionospheric decorrelation)

**CORS network (India):**

| Network | Description |
|---------|-------------|
| CORS-IIRS | ISRO's network across India |
| NRCM | National Reference CORS Mapping |
| Survey of India | Traditional + CORS control points |

---

## 4. Digital Image Processing

### Image Enhancement

| Method | Description | Application |
|--------|-------------|-------------|
| **Contrast stretching** | Linear/non-linear histogram transform | Improve visual interpretation |
| **Histogram equalization** | Uniform distribution of DN values | Enhance low-contrast images |
| **Spatial filtering** | Convolution with kernel | Edge detection, smoothing |
| **Spectral sharpening (pan-sharpening)** | Merge MS + Pan bands | High-res color imagery |
| **PCA (Principal Component Analysis)** | Reduce dimensionality, extract info | Data compression, noise reduction |
| **NDVI enhancement** | Band ratio | Vegetation mapping |

**Common spatial filters:**

| Filter | Kernel | Effect |
|--------|--------|--------|
| Mean (box) | $\frac{1}{9}\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$ | Smooth / blur |
| Gaussian | Weighted center | Smooth (preserves edges better) |
| Laplacian | $\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}$ | Edge detection |
| Sobel (horizontal) | $\begin{bmatrix}-1&-2&-1\\0&0&0\\1&2&1\end{bmatrix}$ | Horizontal edge detection |
| Sobel (vertical) | $\begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix}$ | Vertical edge detection |

### Digital Elevation Models (DEM)

| Source | Resolution | Vertical Accuracy |
|--------|-----------|-------------------|
| SRTM | 30 m / 90 m | ±16 m |
| ASTER GDEM v3 | 30 m | ±8–17 m |
| Cartosat DEM | 30 m | ±10 m |
| ALOS PALSAR DEM | 12.5 m | ±5 m |
| LiDAR | 0.5–5 m | ±0.1–0.3 m |
| Drone photogrammetry | 2–10 cm | ±2–5 cm |

### Photogrammetry

| Method | Equipment | Accuracy |
|--------|-----------|----------|
| Aerial photogrammetry | Metric camera, aircraft/drone | cm–dm |
| Satellite photogrammetry | Stereo satellite pairs | m–dm |
| UAV photogrammetry | Consumer drone, SfM software | cm |
| Terrestrial photogrammetry | Tripod-mounted camera | mm–cm |

**Structure from Motion (SfM) workflow:**
1. Image acquisition (60–80% overlap)
2. Feature detection and matching (SIFT/SURF)
3. Sparse point cloud (bundle adjustment)
4. Dense point cloud
5. Mesh/surface generation
6. Orthophoto and DSM creation

**Ground Sampling Distance (GSD):**
$$GSD = \frac{H \cdot p}{f}$$

Where:
- $H$ = flight altitude above ground
- $p$ = pixel size on sensor
- $f$ = focal length

---

## 5. Remote Sensing for Civil Engineering Applications

### Flood Mapping

| Sensor | Method | Advantage |
|--------|--------|-----------|
| Sentinel-1 SAR | Backscatter change detection | All-weather, day/night |
| Sentinel-2 optical | NDWI, MNDWI | High spatial resolution |
| Landsat | Water index | Long historical archive |
| MODIS | Daily surface water | High temporal resolution |

**Modified NDWI (MNDWI):**
$$MNDWI = \frac{Green - SWIR}{Green + SWIR}$$

### Urban Heat Island (UHI)

| Method | Sensor |
|--------|--------|
| Land Surface Temperature (LST) | Landsat thermal, MODIS |
| Air temperature transects | Ground-based measurements |
| Sky View Factor (SVF) | 360° photography / LiDAR |

**LST from thermal band:**
$$LST = \frac{T_b}{1 + \left(\frac{\lambda \cdot T_b}{\rho}\right)\ln\varepsilon}$$

Where:
- $T_b$ = brightness temperature (K)
- $\lambda$ = wavelength of thermal band (m)
- $\rho = h \cdot c / \sigma = 1.438 \times 10^{-2}$ m·K
- $\varepsilon$ = surface emissivity

### Land Use / Land Cover (LULC)

| Class | Typical NDVI | Typical NDWI |
|-------|-------------|-------------|
| Water | < 0.0 | > 0.0 |
| Built-up | 0.0 – 0.15 | < 0.0 |
| Bare soil | 0.1 – 0.2 | < 0.0 |
| Sparse vegetation | 0.2 – 0.4 | < 0.0 |
| Dense vegetation | 0.4 – 0.8 | < 0.0 |

---

## 6. GIS for Transportation Planning

| Application | Method |
|-------------|--------|
| Route optimization | Least-cost path (Dijkstra) |
| Traffic modeling | TransCAD, VISUM |
| Accessibility analysis | Isochrone mapping |
| Road network extraction | Automated vectorization from imagery |
| Land use–transportation interaction | GIS-based travel demand model |

### Network Analysis

**Dijkstra's shortest path:**
- Assigns edge weights (distance, time, cost)
- Finds minimum-cost path between O-D pairs
- Used in route planning and infrastructure networks

**Facility location problem:**
- Maximize coverage: p-median / p-center models
- Minimize total impedance
- Service area analysis: Thiessen polygons / network buffers

---

## 7. LiDAR (Light Detection and Ranging)

### LiDAR Principles

| Parameter | Description |
|-----------|-------------|
| Pulse rate | 100,000–2,000,000 points/sec |
| Accuracy | ±2–5 cm (vertical), ±15–30 cm (horizontal) |
| Wavelength | 1064 nm (near-IR), 532 nm (green, bathymetric) |
| Scan angle | ±25° typical (±60° max) |
| Point density | 1–100 points/m² |

### LiDAR Data Products

| Product | Description |
|---------|-------------|
| Raw point cloud (.las/.laz) | X, Y, Z, intensity, return number, class |
| Digital Terrain Model (DTM) | Ground points only |
| Digital Surface Model (DSM) | All first returns (includes buildings, trees) |
| Normalized DSM (nDSM) | DSM − DTM (bare-earth height model) |
| Canopy height model | nDSM with buildings removed |

### LiDAR Classification

| Class Code | Class Name |
|-----------|------------|
| 0 | Created / Unclassified |
| 1 | Unclassified |
| 2 | Ground |
| 3 | Low Vegetation |
| 4 | Medium Vegetation |
| 5 | High Vegetation |
| 6 | Building |
| 7 | Low Point (noise) |
| 8 | Reserved |
| 9 | Water |
| 10 | Rail |
| 11 | Road Surface |
| 12 | Overlap |

### Civil Engineering Applications

| Application | Product Used |
|-------------|-------------|
| Highway corridor mapping | DTM + point cloud |
| Building footprint extraction | DSM + classification |
| Canopy cover / tree inventory | nDSM + NDVI |
| Floodplain mapping | DTM (high accuracy) |
| Construction progress monitoring | Sequential point clouds |
| Slope stability analysis | DTM derivatives (slope, aspect) |

---

## 8. Open-Source GIS & RS Tools

| Tool | Type | Key Features |
|------|------|-------------|
| **QGIS** | Desktop GIS | Full-featured, plugin ecosystem, Python API |
| **GRASS GIS** | Analytical GIS | Raster/vector, terrain analysis, hydrology |
| **SAGA GIS** | Analytical GIS | Geostatistics, terrain, remote sensing |
| **Google Earth Engine** | Cloud RS | Petabyte archive, parallel processing |
| **PostGIS** | Spatial DB | Spatial SQL, vector data management |
| **GeoServer** | Web GIS server | WMS, WFS, WCS publishing |
| **Leaflet / OpenLayers** | Web mapping | Interactive web maps |
| **GDAL/OGR** | Geospatial library | Raster/vector format conversion, processing |
| **Orfeo ToolBox** | Remote sensing | High-performance image processing |
| **SNAP (ESA)** | RS processing | Sentinel data processing |
| **EnMAP-Box** | RS | Hyperspectral image analysis |
| **Python (rasterio, geopandas, shapely, fiona)** | Programming | Spatial analysis in Python |

### Key Python Libraries

| Library | Use |
|---------|-----|
| `geopandas` | Vector spatial data analysis |
| `rasterio` | Raster I/O and analysis |
| `shapely` | Geometric objects and operations |
| `fiona` | Vector file I/O |
| `pyproj` | Coordinate transformations |
| `folium` | Interactive web maps |
| `xarray` | Multi-dimensional raster data |
| `rioxarray` | xarray extension for rasterio |
| `earthengine-api` | Google Earth Engine access |
| `pdal` | Point cloud (LiDAR) processing |

---

## 9. Interview Quick-Reference

### Most Asked Questions

| # | Question | Key Points |
|---|----------|------------|
| 1 | Difference between GIS, RS, and GNSS? | GIS = analyze spatial data; RS = acquire data; GNSS = locate points |
| 2 | What is NDVI and how is it used? | (NIR−Red)/(NIR+Red); vegetation health, density |
| 3 | What are the types of map projections? | Cylindrical (UTM), Conic, Azimuthal; trade-offs in distortion |
| 4 | Explain supervised vs unsupervised classification | Supervised = training data (ML, SVM); Unsupervised = clustering (K-means) |
| 5 | What is RTK-GNSS? How accurate is it? | Real-time carrier phase; 1–2 cm with base station |
| 6 | How does LiDAR work? | Laser pulse → reflection → time-of-flight → 3D point cloud |
| 7 | What is spatial autocorrelation (Tobler's 1st law)? | Near things are more related than distant things |
| 8 | What is the difference between DTM, DSM, DEM? | DTM = ground surface; DSM = top surface; DEM = generic elevation |
| 9 | How to perform watershed delineation in GIS? | Fill sinks → flow direction → flow accumulation → outlet → snap pour point |
| 10 | Explain IDW and Kriging interpolation | IDW = distance-weighted; Kriging = statistical with variogram (optimal, unbiased) |
| 11 | What is UTM projection? | Universal Transverse Mercator; 60 zones, each 6° wide |
| 12 | Difference between raster and vector data? | Raster = grid cells; Vector = points/lines/polygons |
| 13 | What is an image band? | Individual wavelength range captured by sensor |
| 14 | How is DEM used in flood modeling? | Extract stream network, channel geometry for HEC-RAS |
| 15 | What is change detection in RS? | Multi-temporal comparison to identify LULC changes |

### Numerical Practice Problems

**Problem 1 — UTM Zone:**
Find the UTM zone for IIT Kanpur (80.9°E, 26.5°N).

> **Solution:** Zone = floor((80.9 + 180) / 6) + 1 = floor(43.48) + 1 = 44N. Central meridian = (44 − 1) × 6 − 180 = 81°E.

**Problem 2 — NDVI Calculation:**
A Sentinel-2 pixel has Red band reflectance = 0.08 and NIR = 0.35. Calculate NDVI.

> **Solution:** NDVI = (0.35 − 0.08) / (0.35 + 0.08) = 0.27 / 0.43 = 0.628. Interpretation: Dense healthy vegetation (NDVI > 0.4).

**Problem 3 — GSD (Photogrammetry):**
A drone flies at 120 m AGL with a camera having 6.17 µm pixel size and 8.8 mm focal length. Find GSD.

> **Solution:** GSD = (120 × 6.17×10⁻⁶) / (8.8×10⁻³) = 7.404×10⁻⁴ / 8.8×10⁻³ = 0.0841 m ≈ 8.4 cm. This is suitable for topographic mapping.

**Problem 4 — IDW Interpolation:**
Three rainfall stations: A (2 km, 120 mm), B (5 km, 80 mm), C (1 km, 150 mm). Find rainfall at point P using IDW with p=2.

> **Solution:** $w_A = 1/4 = 0.25$, $w_B = 1/25 = 0.04$, $w_C = 1/1 = 1.0$. $Z_p = \frac{0.25 \times 120 + 0.04 \times 80 + 1.0 \times 150}{0.25 + 0.04 + 1.0} = \frac{30 + 3.2 + 150}{1.29} = \frac{183.2}{1.29} = 142.0$ mm.

---

## 🗺️ Subject Roadmap (Beginner → Interview)

> **Priority:** `P1` · **Role tags:** `CORE CIVIL` · `GIS/RS` · `INFRA`

| Stage | Focus | Time |
|-------|-------|------|
| **1. GIS Fundamentals** | Vector vs raster, coordinate systems, projections, UTM zones | 1–2 days |
| **2. Spatial Analysis** | Buffer, overlay, interpolation (IDW, Kriging), map algebra | 2–3 days |
| **3. Remote Sensing** | Image bands, NDVI, classification (supervised/unsupervised), change detection | 2–3 days |
| **4. GNSS & Surveying** | GPS, RTK, LiDAR, photogrammetry, GSD | 1–2 days |
| **5. Hydrological GIS** | DEM, watershed delineation, flow accumulation, flood modeling interface | 2 days |
| **6. Software Practice** | QGIS/ArcGIS, Python (geopandas, rasterio), Google Earth Engine | 3–4 days |
| **7. Interview Prep** | Question bank below, numericals, project defense | 1–2 days |

---

## 📋 Formula Sheet (GIS/RS)

<details>
<summary><b>Click to expand — Key GIS/RS formulas</b></summary>

| Formula | Use |
|---------|-----|
| $\text{UTM Zone} = \lfloor(\text{Lon}+180)/6\rfloor + 1$ | UTM zone selection |
| $Z_p = \frac{\sum w_i Z_i}{\sum w_i},\ w_i = 1/d_i^p$ | IDW interpolation (p=2 default) |
| $\gamma(h) = C_0 + C[1-\exp(-3h/a)]$ | Kriging exponential semivariogram |
| $\text{NDVI} = \frac{\text{NIR}-\text{Red}}{\text{NIR}+\text{Red}}$ | Vegetation index |
| $\text{GSD} = \frac{H \times p}{f}$ | Ground sample distance (photogrammetry) |
| $\text{Slope} = \arctan\sqrt{(\Delta z/\Delta x)^2+(\Delta z/\Delta y)^2}$ | DEM slope |
| $\text{Scale} = \frac{\text{Map distance}}{\text{Ground distance}}$ | Map scale |
| $\text{Area} = \text{pixel size}^2 \times \text{count}$ | Raster area computation |
| $\text{NDWI} = \frac{\text{Green}-\text{NIR}}{\text{Green}+\text{NIR}}$ | Water index |
| $\text{EVI} = 2.5\frac{\text{NIR}-\text{Red}}{\text{NIR}+6\text{Red}-7.5\text{Blue}+1}$ | Enhanced vegetation index |

</details>

---

## ❓ Question Bank (Placement-Focused)

### A. Basic Concept Questions

1. **What is the difference between GIS, Remote Sensing, and GNSS?**
   - GIS = analyze/manage spatial data; RS = acquire data from sensors; GNSS = determine position.

2. **What is the difference between vector and raster data?**
   - Vector = points/lines/polygons (discrete features, crisp boundaries); Raster = grid cells (continuous surfaces, imagery).

3. **What is a map projection and why is it needed?**
   - Converting 3D ellipsoid to 2D plane; introduces distortion in area, shape, distance, or direction.

4. **What is UTM and how many zones does it have?**
   - Universal Transverse Mercator; 60 zones, each 6° wide, central meridian scale factor 0.9996.

5. **What is NDVI and what does a high value mean?**
   - (NIR−Red)/(NIR+Red); high value (>0.4) = dense healthy vegetation.

6. **What is a DEM, DTM, and DSM?**
   - DEM = generic elevation model; DTM = bare ground surface; DSM = top surface (includes vegetation/buildings).

7. **What is georeferencing?**
   - Assigning real-world coordinates to an image using control points.

8. **What is spatial autocorrelation (Tobler's 1st law)?**
   - "Everything is related to everything else, but near things are more related than distant things."

### B. WHY Questions

1. **Why is Kriging preferred over IDW for interpolation?**
   - Kriging is statistically optimal and unbiased — it models spatial correlation via the variogram and provides prediction variance (uncertainty).

2. **Why do we need multiple map projections?**
   - No single projection preserves all properties; choose based on purpose (navigation = conformal, area = equal-area).

3. **Why is UTM not suitable for global-scale analysis?**
   - Distortion increases away from central meridian; each zone is limited to 6° longitude.

4. **Why is supervised classification generally more accurate than unsupervised?**
   - Uses labeled training data (prior knowledge) to guide the classifier; unsupervised relies on statistical clustering.

5. **Why does watershed delineation require filling sinks first?**
   - Sinks (depressions) trap flow and break flow-direction continuity; filling ensures continuous drainage to outlet.

6. **Why is LiDAR preferred over photogrammetry for forest terrain?**
   - LiDAR pulses penetrate canopy gaps to reach ground; photogrammetry sees the canopy surface.

### C. WHAT-IF Questions

1. **What if you overlay two layers with different coordinate systems?**
   - Mismatch → features misalign; must reproject to a common CRS first.

2. **What if your DEM has sinks in a flood model?**
   - Flow accumulation is disrupted → wrong stream network; fill sinks before delineation.

3. **What if NDVI is negative?**
   - Indicates water or bare soil (NIR < Red); used to mask water bodies.

4. **What if you use the wrong UTM zone?**
   - Large positional error (can be hundreds of meters); always verify zone from longitude.

5. **What if your training samples are biased in supervised classification?**
   - Classifier overfits to sampled areas → poor generalization; need representative, balanced samples.

### D. Comparison Questions

| Compare | A | B | Key Difference |
|---------|---|---|----------------|
| Vector vs Raster | Vector | Raster | Discrete vs continuous; storage & analysis differ |
| IDW vs Kriging | IDW | Kriging | Deterministic vs statistical (with uncertainty) |
| DEM vs DSM | DEM | DSM | Ground vs top surface |
| Supervised vs Unsupervised | Supervised | Unsupervised | Labeled training vs clustering |
| GPS vs RTK | GPS | RTK | Meter-level vs cm-level (carrier phase) |
| Cylindrical vs Conic projection | Cylindrical | Conic | Distortion pattern; mid-latitude vs equatorial |

### E. Numerical Questions

1. **UTM zone for IIT Kanpur (80.9°E):** Zone = floor((80.9+180)/6)+1 = 44N. Central meridian = 81°E.
2. **NDVI:** Red=0.08, NIR=0.35 → (0.35−0.08)/(0.35+0.08) = 0.628 (dense vegetation).
3. **GSD:** H=120 m, pixel=6.17 µm, f=8.8 mm → GSD = (120×6.17e-6)/(8.8e-3) = 8.4 cm.
4. **IDW:** Stations A(2km,120), B(5km,80), C(1km,150), p=2 → Z = (0.25×120+0.04×80+1.0×150)/(1.29) = 142.0 mm.

### F. Rapid-Fire Questions

1. What is a band? → A wavelength range captured by a sensor.
2. What is a pixel? → Smallest raster cell.
3. What is resolution? → Detail level (spatial/spectral/temporal/radiometric).
4. What is a shapefile? → Vector format (points/lines/polygons).
5. What is a GeoTIFF? → Raster with embedded georeferencing.
6. What is a control point? → Known-location tie point for georeferencing.
7. What is a variogram? → Models spatial correlation for Kriging.
8. What is a buffer? → Zone of specified distance around a feature.
9. What is a clip? → Extract features within a boundary.
10. What is an overlay? → Combine multiple layers.
11. What is a DEM? → Digital elevation model.
12. What is a LiDAR point cloud? → 3D points from laser scanning.
13. What is RTK? → Real-time kinematic GNSS (cm accuracy).
14. What is a watershed? → Area draining to a common outlet.
15. What is flow accumulation? → Number of upstream cells draining to each cell.
16. What is a projection? → 3D→2D coordinate transformation.
17. What is a datum? → Reference ellipsoid for coordinates.
18. What is EPSG? → European Petroleum Survey Group code for CRS.
19. What is a raster calculator? → Map algebra tool.
20. What is change detection? → Multi-temporal comparison of LULC.

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Explain the mathematical basis of Kriging and its BLUE property.**
   - Kriging is Best Linear Unbiased Prediction; weights λ minimize variance subject to unbiasedness (Σλ=1), solved via the variogram system.

2. **How does the semivariogram relate to spatial correlation?**
   - γ(h) increases with lag h to a sill; range = correlation distance; nugget = measurement error/micro-scale variation.

3. **Explain the difference between hard and soft classification in remote sensing.**
   - Hard = each pixel assigned one class; soft/fuzzy = membership probabilities per class (sub-pixel).

4. **How would you handle mixed pixels in coarse-resolution imagery?**
   - Spectral unmixing (linear mixture model) to estimate sub-pixel fractions.

5. **What is the role of scale in spatial analysis (Modifiable Areal Unit Problem)?**
   - Results change with aggregation level/zone boundaries; beware ecological fallacy.

6. **How does RTK achieve cm-level accuracy?**
   - Carrier-phase double-differencing removes satellite and receiver clock errors; ambiguity resolution fixes integer cycles.

---

## 🎤 Interview Answer Format (High-Value Questions)

### High-Value Q1: "What is the difference between GIS and Remote Sensing?"

**30-second answer:** GIS is a system to capture, store, analyze, and visualize spatial data. Remote sensing is the technique of acquiring data about the Earth from a distance using sensors on satellites or aircraft. GIS analyzes the data; RS provides the data.

**Deeper:** GIS integrates multiple data layers (vector, raster, tabular) for spatial analysis and decision-making. RS provides the imagery and spectral information that feeds into GIS. They are complementary — RS is a data source, GIS is the analytical platform.

**Key equation:** NDVI = (NIR−Red)/(NIR+Red) — a classic RS-derived product analyzed in GIS.

**Engineering interpretation:** In flood management, RS provides satellite imagery of inundation, GIS overlays it with DEM, land use, and infrastructure to map risk zones and plan evacuation.

### High-Value Q2: "How would you delineate a watershed in GIS?"

**30-second answer:** Fill sinks → compute flow direction → compute flow accumulation → define outlet → snap pour point → extract watershed.

**Deeper:** Start with a hydrologically corrected DEM. Fill sinks to remove depressions. Use the D8 algorithm for flow direction. Accumulate flow to identify stream networks. Place an outlet (pour point) and extract the contributing area.

**Key equation:** Flow direction (D8) assigns each cell to its steepest downslope neighbor; flow accumulation counts upstream cells.

**Engineering interpretation:** Watershed delineation is fundamental for flood modeling, drainage design, and water balance studies — it defines the hydrologic unit for analysis.

---

## 🔗 Interviewer Follow-up Chain

**Q: "Explain supervised classification."**
- **Follow-up 1:** "How do you choose training samples?" → Representative, balanced, covering all classes, validated against ground truth.
- **Follow-up 2:** "What algorithms would you use?" → Maximum likelihood, SVM, Random Forest, deep learning (CNN).
- **Follow-up 3:** "How do you assess accuracy?" → Confusion matrix, overall accuracy, Kappa coefficient, producer's/user's accuracy.
- **Follow-up 4:** "What if classes overlap spectrally?" → Add auxiliary data (texture, elevation), use object-based classification, or increase spectral resolution.

---

## 🔗 Cross-Links

- [`transportation-engineering.md`](../transportation/transportation-engineering.md) — GIS for network analysis & route planning
- [`environmental-engineering.md`](../environmental/environmental-engineering.md) — RS for environmental monitoring
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — GIS for watershed & flood modeling
- [`geotechnical.md`](../geotechnical/geotechnical.md) — GIS for site suitability & hazard mapping
- [`infrastructure-engineering-management.md`](../infrastructure/infrastructure-engineering-management.md) — GIS in infrastructure planning
- [`gis-tools.md`](../../resources/gis-tools.md) — Software & tooling guide

---

## 10. Key References

| Resource | Use |
|----------|-----|
| Lillesand & Kiefer — *Remote Sensing and Image Interpretation* | RS fundamentals |
| Burrough & McDonnell — *Principles of GIS* | GIS theory |
| Wolf & Dewitt — *Elements of Photogrammetry* | Photogrammetry |
| Hofmann-Wellenhof et al. — *GNSS: GPS, GLONASS, Galileo & More* | Satellite positioning |
| Li, Huang — *Remote Sensing and Image Processing* | Digital image processing |
| QGIS Training Manual | Practical GIS (free) |
| ESRI ArcGIS Documentation | Industry-standard GIS |
| ISRO/BISAG-N tutorials | Indian RS applications |

---

> **Last Updated:** 2026-09-03
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
> **Version:** 1.0 — Comprehensive Geoinformatics Guide

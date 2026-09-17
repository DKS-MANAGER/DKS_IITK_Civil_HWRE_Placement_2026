# GIS, Remote Sensing & Geospatial Intelligence Guide
**Scope:** Hydraulics, Water Resources (HWRE), Environmental & Spatial Analytics  
**Target Roles:** SME Water/GIS (Vassarlabs), GIS Analyst (GIST), Spatial Data Science, Smart Infrastructure  
**Structure:** Operational Decision Matrix $\to$ Task-to-Tool Mapping $\to$ Interview Probes $\to$ Technical Evidence

---

## 1. Geospatial Task-to-Tool Decision Matrix

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        GEOSPATIAL PROBLEM-SOLVING DECISION TREE                        │
├─────────────────────────┬───────────────────────────────┬──────────────────────────────┤
│ Engineering Task        │ Primary Recommended Tool      │ Python / Open-Source Stack   │
├─────────────────────────┼───────────────────────────────┼──────────────────────────────┤
│ Watershed Delineation   │ QGIS / ArcGIS Spatial Analyst │ WhiteboxTools / GeoPandas    │
│ Flood Inundation Models │ HEC-RAS (1D/2D) + RAS Mapper  │ GDAL / Rasterio / Shapely    │
│ Satellite Remote Sensing│ Google Earth Engine (GEE)     │ Planetary Computer / Rasterio│
│ Road Network & Routing  │ OSMnx / PostGIS (pgRouting)   │ NetworkX / GeoPandas         │
│ Point Cloud LiDAR & DEM │ CloudCompare / PDAL           │ PyVista / Open3D             │
└─────────────────────────┴───────────────────────────────┴──────────────────────────────┘
```

---

## 2. Comprehensive Task, Tool & Interview Decision Guide

| Engineering & Analytics Task | Recommended Tool | Expected Level of Proficiency | Core Interview Topics & Technical Probes | Practical Project / Resume Evidence |
|:---|:---|:---|:---|:---|
| **Watershed & Catchment Delineation** | **QGIS / ArcGIS Pro** (Hydrology Toolset) | **Advanced:** Sink filling, Flow Direction (D8/D-infinity), Flow Accumulation, Stream Order (Strahler). | *"Explain the difference between D8 and D-infinity flow algorithms. How do flat areas/depressions distort flow routing?"* | Automated watershed delineation across $1,200\text{ km}^2$ river basin from $30\text{m}$ SRTM DEM. |
| **Flood Inundation & Hazard Mapping** | **HEC-RAS 2D + QGIS** | **Intermediate–Advanced:** Mesh generation, Manning's $n$ spatial layering, boundary condition setup. | *"How do you couple 1D river hydraulics with 2D floodplain diffusion wave equations?"* | Hydrodynamic 2D flood inundation map for 100-year return period rainfall event. |
| **Planetary Remote Sensing & LULC** | **Google Earth Engine (GEE)** | **Intermediate:** Cloud masking, Landsat/Sentinel-2 spectral indices ($\text{NDVI}, \text{NDWI}, \text{MNDWI}$). | *"Why is MNDWI superior to NDVI for water body extraction in urban built-up environments?"* | 10-year multi-temporal surface water body shrinkage analysis in GEE using JavaScript API. |
| **Vector & Raster Data Pipelines** | **GeoPandas + Rasterio** | **Advanced:** CRS re-projection (EPSG:4326 vs UTM), spatial joins, affine transformations, raster zonal statistics. | *"What happens when you perform a spatial overlay between layers in different coordinate reference systems?"* | Python pipeline processing $50\text{GB}$ multi-band GeoTIFF satellite rainfall grids. |
| **Spatial Database Management** | **PostgreSQL / PostGIS** | **Intermediate:** Spatial indexing (`GIST`), `ST_Intersects`, `ST_Buffer`, `ST_Distance_Sphere`, spatial aggregation. | *"How does a R-Tree or GIST index accelerate 2D nearest-neighbor spatial queries over standard B-Trees?"* | Scalable PostGIS database storing 500,000 hydrological monitoring sensor nodes. |
| **LiDAR Point Cloud DEM Extraction** | **CloudCompare / PDAL** | **Intermediate:** Ground point classification (CSF filter), rasterization, Digital Surface Model ($\text{DSM}$) to $\text{DTM}$ filtering. | *"How do you isolate vegetation canopy from bare earth terrain in airborne LiDAR point clouds?"* | High-resolution $1\text{m}$ DTM generation for urban drainage channel grading. |

---

## 3. High-Frequency GIS & Remote Sensing Interview Q&A

### Q1: "Explain the fundamental difference between Geographic Coordinate Systems (GCS) and Projected Coordinate Systems (PCS)."
- **Defensible Response:**  
  *"A Geographic Coordinate System (e.g., WGS84, EPSG:4326) defines locations on a 3D spherical/ellipsoidal surface using angular units (degrees of latitude and longitude). It cannot accurately measure linear distances or surface areas without distortion.*  
  *A Projected Coordinate System (e.g., UTM Zone 44N, EPSG:32644) mathematically flattens the 3D ellipsoid onto a 2D Cartesian plane using linear units (meters), preserving specific properties (conformal, equal-area, or equidistant) for accurate engineering volume and distance calculations."*

### Q2: "How do you calculate Normalized Difference Vegetation Index (NDVI) and Modified Normalized Difference Water Index (MNDWI)?"
- **Defensible Response:**
  - $\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$: Leverages high chlorophyll reflectance in Near-Infrared ($\text{NIR}$) and absorption in visible Red.
  - $\text{MNDWI} = \frac{\text{Green} - \text{SWIR}}{\text{Green} + \text{SWIR}}$: Replaces $\text{NIR}$ with Short-Wave Infrared ($\text{SWIR}$) to suppress false positives from built-up urban concrete and asphalt, cleanly isolating open water bodies.

---

## 4. Cross-Reference Links to Preparation Tracks
- [Water Resources Mock Test (Test 04)](../prep/mock-tests/04_WATER_RESOURCES_MOCK_TEST.md)
- [Vassarlabs Placement Profile](../prep/company-profiles/civil-vassarlabs.md)
- [GIST Geospatial Placement Profile](../prep/company-profiles/civil-gist.md)
- [Core HWRE Curriculum](../core/hwre/README.md)

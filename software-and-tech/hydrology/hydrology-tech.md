# 🌧️ Hydrology Technology Roadmap

> **Branch:** Hydrology / Water Resources
> **Technologies mapped to rainfall analysis, watershed modelling, flood modelling, and spatial analysis.**

---

## Decision Tree

```
Hydrology student → what tools?

1. HEC-HMS first      → Rainfall-runoff modeling (MUST)
2. HEC-RAS next        → Flood routing, river hydraulics
3. GIS (QGIS/ArcGIS)  → Watershed delineation, spatial analysis
4. Python              → Time series analysis, statistical hydrology
5. Google Earth Engine → Satellite-based hydrological analysis
6. MATLAB              → Numerical methods, optimization
7. SWMM               → If urban hydrology is relevant
```

---

## Tool Roadmap

### Essential (All Hydrology Students)

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| HEC-HMS | `[MUST LEARN]` | L2–L3 | Rainfall-runoff, flood forecasting |
| HEC-RAS | `[MUST LEARN]` | L2–L3 | Flood routing, river modeling |
| GIS (QGIS) | `[MUST LEARN]` | L2 | Watershed delineation, spatial analysis |
| Excel | `[MUST LEARN]` | L3 | Data processing, IDF curves |

### Important

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| Python | `[HIGH ROI]` | L2–L3 | Time series, statistics, automation |
| MATLAB | `[ROLE DEPENDENT]` | L2 | Numerical methods, ODE solving |
| EPA SWMM | `[ROLE DEPENDENT]` | L2 | Urban hydrology, LID analysis |
| MODFLOW 6 | `[ROLE DEPENDENT]` | L2 | Groundwater flow |

### Advanced / Research

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| Google Earth Engine | `[HIGH ROI]` | L2 | Satellite rainfall, land use, snow cover |
| Python (Rasterio/GeoPandas) | `[HIGH ROI]` | L2–L3 | Spatial data processing |
| OpenFOAM | `[SPECIALIZED]` | L3 | CFD for flood/inundation modeling |
| HPC / SLURM | `[SPECIALIZED]` | L2 | Large-scale distributed modeling |

---

## Tool → Problem → Workflow

### HEC-HMS

| Property | Value |
|:---------|:------|
| **Problem solved** | Convert rainfall into runoff hydrographs |
| **Input data** | Precipitation, watershed characteristics, soil/land use |
| **Output** | Discharge hydrographs, peak flow, volume |
| **Typical workflow** | Delineate watershed → define sub-basins → set losses/transform → run → analyze hydrographs |
| **Portfolio project** | Model a real watershed with observed rainfall-runoff data |
| **Interview relevance** | "Explain the SCS-CN method" / "How do you calibrate a hydrologic model?" |

### HEC-RAS (Hydrology Application)

| Property | Value |
|:---------|:------|
| **Problem solved** | Route floods through river channels and floodplains |
| **Input data** | Channel geometry, cross-sections, flow hydrographs |
| **Output** | Water surface elevations, flood extent, inundation maps |
| **Typical workflow** | Define geometry → set upstream hydrograph → route → analyze flood extent |
| **Portfolio project** | Route a design flood through a reach and map inundation |
| **Interview relevance** | "How do you determine the design flood?" / "1D vs 2D routing?" |

### GIS for Hydrology

| Property | Value |
|:---------|:------|
| **Problem solved** | Spatial analysis of watersheds, land use, terrain |
| **Input data** | DEM, land use maps, soil maps, rainfall data |
| **Output** | Watershed boundaries, flow direction, slope maps |
| **Typical workflow** | DEM → fill sinks → flow direction → flow accumulation → delineate watershed |
| **Portfolio project** | Delineate watershed and compute morphometric parameters |
| **Interview relevance** | "How do you delineate a watershed from a DEM?" |

### Python for Hydrology

| Property | Value |
|:---------|:------|
| **Problem solved** | Time series analysis, statistical hydrology, automation |
| **Input data** | Rainfall time series, discharge data, water quality data |
| **Output** | IDF curves, frequency analysis, trend detection, automated reports |
| **Typical workflow** | Read data → clean → statistical analysis → visualization → report |
| **Portfolio project** | IDF curve generation, flood frequency analysis (Gumbel, Log-Pearson III) |
| **Interview relevance** | "Write code to compute return period from annual maxima" |

### Google Earth Engine

| Property | Value |
|:---------|:------|
| **Problem solved** | Large-scale satellite-based hydrological analysis |
| **Input data** | Satellite imagery (TRMM, GPM, Landsat, MODIS) |
| **Output** | Spatial rainfall maps, NDVI, snow cover, land use classification |
| **Typical workflow** | Define region → select satellite data → filter → process → visualize |
| **Portfolio project** | Rainfall trend analysis using TRMM/GPM over a basin |
| **Interview relevance** | "How do you get satellite rainfall data?" / "What is GEE?" |

---

## Data Sources for Hydrology Projects

| Data Type | Source | Resolution |
|:----------|:-------|:-----------|
| DEM (elevation) | SRTM, ASTER, ALOS | 30m–90m |
| Rainfall | IMD gridded, TRMM, GPM | 0.25° / 0.1° |
| Land use | LULC, MODIS | 250m–500m |
| Soil | HWSD, NRCS | 1km |
| Discharge | NWIS (USGS), CWC (India) | Daily/Hourly |
| Evapotranspiration | MODIS ET, GRACE | 250m–1° |

---

## Interview Questions

### Basic (101)
- What is the SCS-CN method? How do you determine CN?
- What is a unit hydrograph? When is it applicable?
- What is the difference between HEC-HMS and HEC-RAS?

### Practical (201)
- Walk me through a HEC-HMS modeling workflow.
- How do you delineate a watershed from DEM data?
- How do you calibrate a rainfall-runoff model?
- What loss method would you choose and why?

### Technical (301)
- Explain the Muskingum routing method.
- How do you perform flood frequency analysis?
- What is the difference between event-based and continuous simulation?

### Project Defense
- Show me your HEC-HMS model. How did you validate it?
- What satellite data did you use? Why?
- How did you handle missing data?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| HWRE Tech Roadmap | [`hwre/`](../hwre/hwre-tech-roadmap.md) |
| Sediment Transport | [`sediment/`](../sediment/sediment-tech.md) |
| GIS Technology | [`gis/`](../gis/gis-tech.md) |
| Core Hydrology Subject | [`core/hwre/hydrology/`](../../core/hwre/hydrology/hydrology.md) |
| CFD Technology | [`cfd/`](../cfd/cfd-tech.md) |

---

*See also: [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md) for the full HWRE technology overview.*

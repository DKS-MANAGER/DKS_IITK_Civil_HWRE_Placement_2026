# 🗺️ GIS / Remote Sensing / Geoinformatics Technology Roadmap

> **Branch:** GIS / Remote Sensing / Geoinformatics
> **Covers GIS fundamentals, remote sensing, programming for spatial analysis, and portfolio projects.**

---

## Decision Tree

```
GIS student → what tools?

1. QGIS or ArcGIS first  → Desktop GIS fundamentals (MUST)
2. Python (GeoPandas)     → Programmatic spatial analysis (HIGH ROI)
3. Google Earth Engine    → Satellite-based large-scale analysis (HIGH ROI)
4. Rasterio + Shapely     → Raster/vector processing (ROLE DEPENDENT)
5. PostGIS                → Spatial databases (ROLE DEPENDENT)
6. Web GIS (Leaflet)      → Interactive maps (OPTIONAL)
```

---

## Tool Roadmap

### Essential

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| QGIS | `[MUST LEARN]` | L3 | Desktop GIS, spatial analysis, mapping |
| ArcGIS | `[MUST LEARN]` | L2–L3 | Professional GIS (industry standard) |
| Excel | `[MUST LEARN]` | L3 | Tabular data preparation |

### Important

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| Python (GeoPandas) | `[HIGH ROI]` | L2–L3 | Programmatic spatial analysis |
| Google Earth Engine | `[HIGH ROI]` | L2 | Cloud-based satellite analysis |
| Rasterio | `[HIGH ROI]` | L2 | Raster data processing |
| Shapely | `[HIGH ROI]` | L2 | Geometry operations |

### Advanced

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| PostGIS | `[SPECIALIZED]` | L2 | Spatial database queries |
| Leaflet / OpenLayers | `[SPECIALIZED]` | L2 | Web-based interactive maps |
| D3.js | `[SPECIALIZED]` | L1 | Data visualization on maps |
| ENVI | `[SPECIALIZED]` | L2 | Advanced remote sensing |
| Agisoft Metashape | `[SPECIALIZED]` | L2 | Photogrammetry, drone mapping |

---

## Learning Path

### GIS Fundamentals (QGIS / ArcGIS)

```
Beginner:
    → Interface tour, layer management
    → Vector vs raster data
    → Coordinate systems and projections
    → Basic digitizing and attribute editing

Intermediate:
    → Spatial analysis (buffer, clip, intersect, join)
    → Raster analysis (reclassify, raster calculator)
    → Terrain analysis (slope, aspect, hillshade)
    → Map composition and layout

Advanced:
    → Model Builder / Processing scripts
    → Geostatistics (kriging, IDW)
    → Network analysis
    → Temporal data visualization
```

### Python for GIS

```
Beginner:
    → GeoPandas: read/write shapefiles, spatial operations
    → Shapely: create and manipulate geometries
    → Matplotlib: plot maps

Intermediate:
    → Rasterio: read/write rasters, band math
    → Spatial joins, overlays, projections
    → Coordinate transformations

Advanced:
    → Automated workflows (batch processing)
    → Custom spatial analysis functions
    → Integration with Jupyter Notebooks
```

### Google Earth Engine

```
Beginner:
    → JavaScript API basics
    → Image collections, filtering, compositing
    → Band math, NDVI, indices

Intermediate:
    → Image classification (supervised, unsupervised)
    → Time series analysis
    → Export results

Advanced:
    → Custom algorithms
    → Large-scale analysis
    → Integration with Python (geemap)
```

---

## Portfolio Projects

### For All GIS Students

```
Project 1: Flood Risk Mapping
    Tools: QGIS/ArcGIS + Python
    Data: DEM, river network, land use
    Output: Flood risk zones, exposure maps
    Resume value: High

Project 2: Urban Growth Analysis
    Tools: Google Earth Engine + QGIS
    Data: Landsat imagery (multi-year)
    Output: Land use change maps, growth statistics
    Resume value: High

Project 3: Water Distribution Network Mapping
    Tools: QGIS + PostGIS
    Data: Pipe network, service areas, demographics
    Output: Network map, service analysis
    Resume value: Medium-High
```

### Additional Projects

```
Project 4: Watershed Delineation
    Tools: QGIS + GRASS GIS
    Data: DEM
    Output: Watershed boundaries, morphometric analysis

Project 5: Disaster Damage Assessment
    Tools: Google Earth Engine + QGIS
    Data: Pre/post-event satellite imagery
    Output: Damage extent, affected area statistics

Project 6: Road Accessibility Analysis
    Tools: QGIS + OSMnx (Python)
    Data: Road network, population
    Output: Accessibility maps, travel time analysis
```

---

## Data Sources

| Data Type | Source | Resolution | Access |
|:----------|:-------|:-----------|:-------|
| DEM | SRTM, ASTER, ALOS | 30m–90m | Free |
| Satellite imagery | Landsat, Sentinel | 10m–30m | Free (GEE, Copernicus) |
| Land use | LULC, MODIS | 250m–500m | Free |
| Roads/buildings | OpenStreetMap | Vector | Free |
| Population | WorldPop, GPW | 100m–1km | Free |
| Climate | ERA5, CHIRPS | 0.1°–0.25° | Free |

---

## Interview Questions

### Basic (101)
- What is the difference between vector and raster data?
- What is a coordinate reference system (CRS)?
- Explain the difference between QGIS and ArcGIS.

### Practical (201)
- How do you perform a spatial join?
- Walk me through a land use classification workflow.
- How do you handle different projections in a project?

### Technical (301)
- What is kriging? When would you use it?
- Explain the difference between supervised and unsupervised classification.
- How do you assess classification accuracy?

### Project Defense
- Show me your GIS portfolio project.
- Why did you choose this tool over alternatives?
- How did you validate your spatial analysis results?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core GIS | [`core/geoinformatics/`](../../core/geoinformatics/geoinformatics.md) |
| Existing GIS Tools | [`resources/gis-tools.md`](../../resources/gis-tools.md) |
| Python for GIS | [`programming/python.md`](../programming/python.md) |
| HWRE Tech (GIS usage) | [`hwre/`](../hwre/hwre-tech-roadmap.md) |

---

*See also: [`branch-roadmaps.md`](../branch-roadmaps.md) for full branch comparison.*

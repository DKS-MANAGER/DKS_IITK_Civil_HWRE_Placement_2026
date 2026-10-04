# 🗺️ QGIS / ArcGIS for Civil Engineering

> **Priority:** P0 — Required (GIS/Water Resources) | **Target Level:** L2–L3
> **Time to L2:** 15–20 hrs | **Time to L3:** 30–40 hrs
> **Canonical source.** GIS, HWRE, hydrology pages link here.

---

## 1. What It Is

**QGIS** is a free, open-source **Geographic Information System (GIS)** for viewing, editing, and analyzing spatial data. **ArcGIS** is its commercial counterpart (Esri). Both handle **vector** (points, lines, polygons) and **raster** (satellite imagery, DEM) data.

## 2. Where It Is Used

| Application | Branch | Context |
|:------------|:-------|:--------|
| Watershed delineation | Hydrology | Extract catchment from DEM |
| Flood mapping | Water Resources | Inundation maps from HEC-RAS |
| Land-use mapping | GIS | Classification, change detection |
| Site mapping | Geotech | Borehole locations, soil maps |
| Road alignment | Transportation | Route planning, corridor mapping |
| EIA mapping | Environmental | Impact area visualization |

## 3. Why Your Target Role Needs It

**Company evidence:**

| Company | Role | GIS Level |
|:--------|:-----|:----------|
| Vassarlabs | SME — Water/GIS | Proficient (ArcGIS, QGIS) |
| GIST | GIS Analyst | Proficient (QGIS/ArcGIS, PostGIS) |
| Rodic | Environmental | Basic (ArcGIS/QGIS) |

> **Interview tip:** "How would you prepare a flood inundation map using satellite data?" is a common Vassarlabs/GIST ask.

---

## 4. Installation / Setup

| Option | How |
|:-------|:----|
| **QGIS** | Free download from qgis.org — Windows/macOS/Linux |
| **ArcGIS** | Esri student license via institute |
| **Python (GeoPandas)** | `pip install geopandas rasterio` — for scripting |

**Setup checklist:**
- [ ] Install QGIS (Long Term Release)
- [ ] Load a DEM (SRTM/ASTER) to verify raster support
- [ ] Set project CRS (e.g., UTM 43N for India)
- [ ] Install plugins: QuickMapServices, HEC-GeoRAS (optional)

---

## 5. Core Interface / Workflow

```
Load data (vector/raster) → Set CRS → Analyze (clip, buffer, intersect)
→ Symbolize → Layout → Export map
```

**Key panels:** Layers panel, Browser, Processing toolbox, Map canvas.

---

## 6. Essential Features (3 High-Value Blocks)

### Block 1: Data Handling

| Feature | Purpose |
|:--------|:--------|
| Vector vs raster | Points/lines/polygons vs grids |
| CRS / projections | UTM, geographic vs projected |
| Attribute table | Tabular data behind features |
| Joins | Link spatial + tabular data |
| Georeferencing | Align scanned maps to coordinates |

### Block 2: Spatial Analysis

| Feature | Purpose |
|:--------|:--------|
| Clip / Buffer / Intersect | Core geoprocessing |
| Raster calculator | DEM operations (slope, flow) |
| Watershed tools | Delineate catchment from DEM |
| Zonal statistics | Summarize raster by zone |
| Interpolation (IDW, kriging) | Point → surface |

### Block 3: Mapping & Output

| Feature | Purpose |
|:--------|:--------|
| Symbology | Classify and color features |
| Labels | Annotate features |
| Print layout | Map with scale, legend, north arrow |
| Export | PDF, image, shapefile |

---

## 7. Typical Engineering Workflow

```
Step 1: Load DEM + river network
Step 2: Set CRS (UTM)
Step 3: Delineate watershed (fill → flow direction → flow accumulation → pour point)
Step 4: Clip to study area
Step 5: Overlay HEC-RAS results (flood depth)
Step 6: Symbolize + label
Step 7: Create print layout → export map
```

---

## 8. Worked Example — Watershed Delineation

**Task:** Delineate a watershed from a DEM using QGIS.

```
1. Load DEM (SRTM, 30m)
2. Fill sinks: Raster → Terrain Analysis → Fill Sinks
3. Flow direction: Raster → Terrain Analysis → Flow Direction
4. Flow accumulation: Raster → Terrain Analysis → Flow Accumulation
5. Define pour point (outlet) — create point layer
6. Watershed: Raster → Terrain Analysis → Watershed
7. Convert watershed raster to polygon (Raster → Conversion → Polygonize)
8. Symbolize + add to layout
```

**Output:** A watershed polygon with area, ready for HEC-HMS input.

---

## 9. Practice Exercises

### Basic
1. Load a shapefile and a DEM; set the correct CRS
2. Create a **buffer** around a river centerline (100m)
3. **Clip** a land-use layer to a study area

### Intermediate
4. Perform a **watershed delineation** from a DEM (worked example above)
5. Create a **flood map** by overlaying HEC-RAS depth results
6. Perform a **spatial join** (count points in polygons)

### Role-Specific
7. **Hydrology:** Delineate a watershed and compute its area for HEC-HMS
8. **GIS:** Land-use change detection using two satellite images
9. **Water Resources:** Prepare a flood inundation map from HEC-RAS output

---

## 10. Mini-Project — Thematic Map for a Watershed

```
Objective: Produce a flood-risk thematic map for a river reach
Input: DEM, HEC-RAS flood depth output, land-use layer
Workflow:
    1. Delineate watershed in QGIS
    2. Import HEC-RAS flood depth (RAS Mapper → export to QGIS)
    3. Classify depth into risk zones (low/medium/high)
    4. Overlay land-use to identify exposed areas
    5. Create print layout with legend, scale, north arrow
Expected Output: A flood-risk map (PDF) + risk summary table
Interview Questions It Prepares You For:
    - "How do you delineate a watershed?"
    - "How would you prepare a flood inundation map?"
    - "What CRS would you use for India and why?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Wrong CRS | Layers don't align | Set project CRS consistently |
| Mixing geographic/projected | Distances wrong | Use projected (UTM) for analysis |
| Ignoring DEM resolution | Coarse results | Check DEM resolution (30m vs 90m) |
| No symbology | Map unreadable | Classify and color |
| Forgetting legend/scale | Map not professional | Use print layout |
| Not checking attribute table | Wrong joins | Verify join keys |

---

## 12. Interview Questions

### Basic
- What is the difference between vector and raster data?
- What is a coordinate reference system (CRS)?
- What is the difference between geographic and projected CRS?

### Workflow
- How do you delineate a watershed in QGIS?
- How would you prepare a flood inundation map?

### Troubleshooting
- Your layers don't align. What do you check?
- Your watershed looks wrong. What could be the issue?

### Engineering Judgment
- Why did you choose UTM over geographic coordinates?
- How do you validate your GIS analysis?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | GIS / spatial analysis |
| **Developer** | QGIS (open-source) / Esri (ArcGIS) |
| **License** | QGIS free; ArcGIS commercial |
| **Platform** | Windows, macOS, Linux |
| **Difficulty** | Medium |
| **Time to L2** | 15–20 hrs |
| **Time to L3** | 30–40 hrs |
| **Primary use** | Spatial analysis, mapping |
| **Alternative** | ArcGIS (commercial), GeoPandas (Python) |

**Top 5 concepts:** Vector/Raster, CRS, Buffer, Clip, Watershed

---

## Theory Linkage

```
QGIS → Surveying → coordinate systems, projections
     → GIS → spatial analysis, cartography
     → Hydrology → watershed, DEM, flow direction
     → Remote Sensing → satellite imagery, classification
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| Vassarlabs | Flood mapping, watershed, HEC-RAS integration |
| GIST | Land-use change, PostGIS, GeoPandas |
| Rodic | EIA mapping |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| GIS Roadmap | [`gis/gis-tech.md`](../gis/gis-tech.md) |
| HEC-RAS (integration) | [`deep-dives/hec-ras-walkthrough.md`](../deep-dives/hec-ras-walkthrough.md) |
| SQL (PostGIS) | [`programming/sql.md`](../programming/sql.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |

---

*Canonical source for QGIS/ArcGIS. Do not duplicate in branch pages.*
# Interview Grilling Questions — GIS Catchment, EPANET & Concrete Mix

> **Focus**: Practical civil engineering, network simulation edge cases, geospatial raster algorithms, and concrete materials chemistry.

---

## 1. Questions & Technical Answers

### Q1: "How do you detect and resolve depressions (sinks) in DEM data during watershed delineation?"
* **Answer**: Sinks are spurious raster cells whose elevation is lower than all 8 surrounding neighbors, creating artificial terminal boundaries for overland flow. We apply the **Planchon-Darboux sink-filling algorithm** or **Wang-Liu priority-queue approach**, which progressively floods the digital terrain from ocean/boundary cells inwards to determine the minimum spill elevation for each depression. If the sink represents a genuine geological feature (karst sinkhole, quarry), it can be preserved as an internal drainage sink; otherwise, it is filled to prevent broken stream vector topologies.

### Q2: "In EPANET pipe network analysis, how do you handle negative pressures occurring during high peak demand?"
* **Answer**: Standard EPANET uses **Demand-Driven Analysis (DDA)**, which assumes demand at each node is fixed regardless of pressure. Under severe undersizing or pump trips, DDA can predict unphysical negative pressures. To remedy this:
  1. We switch to **Pressure-Dependent Demand (PDD)** modeling via the Wagner equation:
     $$Q_{actual} = Q_{required} \left(\frac{P - P_{min}}{P_{req} - P_{min}}\right)^{1/e}$$
  2. For engineering remediation: We throttle network control valves (PRVs), introduce elevated service storage balancing tanks, or boost pump speeds to maintain residual pressure above the IS 10500 / CPHEEO minimum head standard ($12\text{ m}$ for multi-story zones).

### Q3: "Why does concrete with fly ash gain strength slower at early ages (7 days) but exceed control mix strength at 56 and 90 days?"
* **Answer**: Ordinary Portland Cement undergoes primary hydration rapidly ($\text{C}_3\text{S}$ and $\text{C}_2\text{S}$ hydrate with water releasing calcium hydroxide $\text{Ca(OH)}_2$ and primary $\text{C-S-H}$ gel). Fly ash (Class F) is pozzolanic and contains reactive vitreous silica and alumina, which cannot hydrate on their own. They must wait for cement hydration to liberate $\text{Ca(OH)}_2$. Once sufficient $\text{CH}$ is present, the secondary pozzolanic reaction begins, converting weak, soluble $\text{CH}$ crystals into dense, insoluble secondary $\text{C-S-H}$ gel. Thus, 7-day strength is lower (~65% of 28-day), but ultimate strength and microstructure density surpass pure OPC at 56–90 days.

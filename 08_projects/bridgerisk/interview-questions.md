# Interview Grilling Questions — Bridge Hydrodynamic Scour (`bridgerisk`)

> **Focus**: Challenging technical, modeling, and trade-off questions asked by interview panels.

---

## 1. Technical Grilling Questions & Answers

### Q1: "What are the primary differences between clear-water scour and live-bed scour?"
* **Answer**:
  * **Clear-water scour**: Occurs when the approach flow shear stress is below the critical shear stress for bed sediment motion ($\tau_0 < \tau_c$). Bed material is transported out of the scour hole around the pier but no sediment enters from upstream. Scour reaches maximum equilibrium slowly (takes hours or days).
  * **Live-bed scour**: Occurs when bed material in the entire upstream channel is in general motion ($\tau_0 > \tau_c$). Sediment is continually transported into and out of the scour hole. Equilibrium scour depth is reached rapidly, and fluctuates cyclically with the passage of bedforms (dunes).

### Q2: "What is the physical mechanism causing local scour around a bridge pier?"
* **Answer**: The primary mechanism is the **horseshoe vortex system** and **wake vortex shedding**:
  1. Stagnation pressure on the front face of the pier decreases downward (from maximum near surface to zero at bed), setting up a strong downward vertical pressure gradient.
  2. This downward jet impinges on the bed and rolls up into a rotating vortex wrapped around the upstream nose of the pier (horseshoe vortex), gouging sediment away from the foundation.
  3. On the downstream side, alternating low-pressure wake vortices act like miniature tornadoes, lifting sediment into the flow.

### Q3: "How does pier skew angle affect scour depth, and how did your model account for it?"
* **Answer**: Pier skew exposes the side of the pier to the incoming velocity vector, drastically increasing the effective pier width ($a_{eff} = a \cos \theta + L \sin \theta$). Even a modest $15^\circ$ skew on an aspect ratio $L/a = 4$ pier increases effective width by over $100\%$, increasing local scour depth by $38\%$. In our 2D model, local velocity vectors at each pier face were computed directly from cell velocity vectors, allowing precise evaluation of local angle of attack.

### Q4: "If you had an unlimited computational budget, what would you improve in this simulation?"
* **Answer**: 2D shallow water models assume hydrostatic pressure distributions and depth-averaged horizontal velocities; they cannot explicitly resolve the 3D downward jet on the pier nose. With high-performance computing, I would couple the 2D reach model with a localized 3D Large Eddy Simulation (LES) or Detached Eddy Simulation (DES) in OpenFOAM with dynamic sediment mesh deformation (Eulerian-Eulerian two-phase sediment transport) to directly resolve instantaneous turbulent vortex structures.

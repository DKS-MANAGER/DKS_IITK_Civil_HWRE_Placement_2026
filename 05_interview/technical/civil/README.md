# Core Civil Engineering — Technical Interview Question Bank

> **Target Roles**: Structural Engineer, Site Engineer, Project Engineer, Design Consultant (L&T, Godrej, Hilti, Thornton Tomasetti, Tata Projects, JSW).

---

## High-Frequency Core Civil Questions & Answers

### 1. Strength of Materials & Structural Analysis
* **Q1**: *"What is the physical meaning of the shear center, and where does it lie in an unsymmetric channel section?"*
  * **Answer**: The shear center is the point on a beam's cross-section through which a lateral transverse load produces pure bending without any twisting/torsion. In a channel section, the shear center lies outside the web on the side opposite to the flanges.
* **Q2**: *"Explain the difference between flexibility and stiffness methods of structural analysis."*
  * **Answer**: In the flexibility (force) method, redundant forces are the primary unknowns, and compatibility equations are solved ($[F]\{P\} = \{\Delta\}$). In the stiffness (displacement) method, nodal displacements are the primary unknowns, and equilibrium equations are solved ($[K]\{\Delta\} = \{P\}$). Stiffness method is the standard basis for modern FEA/structural software (STAAD/ETABS).

### 2. Reinforced Concrete & Steel Design
* **Q3**: *"Why is under-reinforced design mandatory for RCC beams according to IS 456:2000?"*
  * **Answer**: An under-reinforced section ensures that tensile steel yields before concrete reaches its ultimate compressive strain ($0.0035$). This guarantees ductile failure with visible warning cracks and excessive deflection, preventing sudden brittle catastrophic collapse.
* **Q4**: *"What is the slenderness ratio of a steel column and why does it govern buckling load?"*
  * **Answer**: $\lambda = \frac{L_{eff}}{r_{min}}$. According to Euler's buckling formula ($P_{cr} = \frac{\pi^2 E I}{L_{eff}^2} = \frac{\pi^2 E A}{\lambda^2}$), buckling capacity is inversely proportional to the square of the slenderness ratio. High $\lambda$ leads to elastic flexural buckling at stresses far below steel's yield strength.

### 3. Geotechnical & Transportation Engineering
* **Q5**: *"Explain Terzaghi's effective stress principle and why it governs soil shear strength."*
  * **Answer**: $\sigma' = \sigma - u$. Soil particles transmit load across contact points. Pore water has zero shear strength; thus, soil shear strength depends strictly on effective stress: $\tau = c' + \sigma' \tan \phi'$. An increase in pore water pressure ($u$) reduces $\sigma'$ and can trigger slope or foundation failure.
* **Q6**: *"What is the significance of the California Bearing Ratio (CBR) in flexible pavement design (IRC 37)?"*
  * **Answer**: CBR measures the penetration resistance of compacted subgrade soil relative to standard crushed rock. Higher CBR indicates stiffer subgrade, allowing reduced overall crust thickness of the pavement.

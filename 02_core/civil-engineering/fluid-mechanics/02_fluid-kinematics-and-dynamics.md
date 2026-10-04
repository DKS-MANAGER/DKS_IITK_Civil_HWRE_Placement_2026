# 02 — Fluid Kinematics & Dynamics

> **Discipline**: Fundamental Fluid Mechanics  
> **Key Exam / Interview Topics**: Eulerian vs Lagrangian, Streamlines, Continuity equation, Velocity potential ($\phi$) and Stream function ($\psi$), Euler equation of motion, Bernoulli's equation, Momentum equation, Venturimeter & Pitot tube.

---

## 1. Fluid Kinematics

### 1. Velocity & Acceleration Field
$$\mathbf{V} = u\hat{i} + v\hat{j} + w\hat{k}$$
Acceleration components:
$$a_x = \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + v\frac{\partial u}{\partial y} + w\frac{\partial u}{\partial z}$$
Where $\frac{\partial u}{\partial t}$ is local (temporal) acceleration, and the remaining terms represent convective (spatial) acceleration.

### 2. Continuity Equation (Conservation of Mass)
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{V}) = 0$$
For steady, incompressible 3D flow:
$$\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$$

### 3. Velocity Potential ($\phi$) & Stream Function ($\psi$)
* **Velocity Potential ($\phi$)**: Defined strictly for **irrotational flow** ($\nabla \times \mathbf{V} = 0$):
  $$u = -\frac{\partial \phi}{\partial x}, \quad v = -\frac{\partial \phi}{\partial y}$$
  If $\phi$ satisfies Laplace's equation ($\nabla^2 \phi = 0$), the flow is physically possible, steady, incompressible, and irrotational (Potential Flow).
* **Stream Function ($\psi$)**: Defined for 2D continuity:
  $$u = -\frac{\partial \psi}{\partial y}, \quad v = \frac{\partial \psi}{\partial x}$$
  Lines of constant $\psi$ are **streamlines**.
* **Orthogonality**: Equipotential lines ($\phi = \text{const}$) and streamlines ($\psi = \text{const}$) intersect orthogonally everywhere:
  $$\left(\frac{dy}{dx}\right)_{\phi} \times \left(\frac{dy}{dx}\right)_{\psi} = -1$$

---

## 2. Fluid Dynamics

### 1. Euler's Equation of Motion
Along a streamline for inviscid fluid:
$$\frac{dp}{\rho} + V dV + g dz = 0$$

### 2. Bernoulli's Equation
Integrating Euler's equation along a streamline for steady, incompressible, frictionless (inviscid) flow:
$$\frac{p}{\rho g} + \frac{V^2}{2g} + z = \text{Constant}$$
Where:
* $\frac{p}{\rho g}$ is Pressure Head ($\text{m}$ of fluid).
* $\frac{V^2}{2g}$ is Velocity Head (Kinetic energy head).
* $z$ is Datum / Potential Head.
* Hydraulic Grade Line (HGL) = $\frac{p}{\rho g} + z$.
* Total Energy Line (TEL) = $\frac{p}{\rho g} + z + \frac{V^2}{2g}$. TEL always slopes downward in the direction of real flow due to head loss ($h_L$).

---

## 3. Flow Measurement Devices

### 1. Venturimeter (Discharge Measurement in Closed Conduit)
$$Q_{act} = C_d \frac{A_1 A_2}{\sqrt{A_1^2 - A_2^2}} \sqrt{2g h}$$
Where $C_d \approx 0.96\text{--}0.98$ (high coefficient due to streamlined converging cone), and $h = x\left(\frac{S_m}{S} - 1\right)$ from differential manometer reading $x$.

### 2. Orificemeter
$$Q_{act} = C_d \frac{A_1 A_0}{\sqrt{A_1^2 - A_0^2}} \sqrt{2g h}$$
Where $A_0$ is orifice area, and $C_d \approx 0.60\text{--}0.65$ (lower due to vena contracta separation losses).

### 3. Pitot Tube (Local Point Velocity)
$$V = C_v \sqrt{2g h_{stagnation}}$$
Where stagnation pressure head = static head + dynamic velocity head: $H_{stag} = \frac{p}{\rho g} + \frac{V^2}{2g}$.

---

## 4. Momentum Equation & Force on Bends

$$\sum \mathbf{F} = \rho Q (\mathbf{V}_{out} - \mathbf{V}_{in})$$
For a reducing pipe bend deflecting flow by angle $\theta$:
$$F_x = p_1 A_1 - p_2 A_2 \cos \theta - \rho Q (V_2 \cos \theta - V_1)$$
$$F_y = -p_2 A_2 \sin \theta - \rho Q (V_2 \sin \theta)$$
Anchor blocks and thrust blocks are designed to resist this dynamic resultant force $F_R = \sqrt{F_x^2 + F_y^2}$.

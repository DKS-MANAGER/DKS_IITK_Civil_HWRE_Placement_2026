# Module 09: Technical Assessment Question Bank (190 Questions)
## Engineering Mathematics, Statistics, Data Interpretation, Python Programming & Semiconductor Fundamentals

> **Document Status**: Technical Assessment Practice Manual `[TIER 5 PEDAGOGICAL SIMULATION]`  
> **Official Proforma Role Title**: Applications Engineer `[IITK PROFORMA FACT]` (Functional CAE Benchmark)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  
> **Curriculum Coordination**: This module houses the 190 dedicated technical, computational, and domain questions. Combined with **Module 12** (100 Quantitative Aptitude + 40 Logical Reasoning questions), the repository delivers the full **330-Question Assessment Suite**.

---

## Part 1: Engineering Mathematics (40 Questions)

### Linear Algebra & Matrices (Q01–Q15)

**EM01**. Find the eigenvalues of matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 8 \end{pmatrix}$.  
*Solution*:  
Characteristic equation: $\det(A - \lambda I) = (5 - \lambda)(8 - \lambda) - 4 = \lambda^2 - 13\lambda + 36 = 0$.  
Factor: $(\lambda - 4)(\lambda - 9) = 0 \implies \mathbf{\lambda_1 = 4, \lambda_2 = 9}$.

**EM02**. If $\lambda$ is an eigenvalue of an invertible matrix $M$, what is the corresponding eigenvalue of $M^{-1}$?  
*Solution*:  
$M v = \lambda v \implies v = M^{-1}(\lambda v) = \lambda M^{-1} v \implies M^{-1} v = \frac{1}{\lambda} v$.  
*Answer*: The eigenvalue is $\mathbf{\frac{1}{\lambda}}$ (for $\lambda \ne 0$).

**EM03**. For what value of $k$ does the system of equations have infinitely many solutions?  
$$x + 2y + z = 4$$  
$$2x + 5y + 3z = 9$$  
$$3x + 7y + kz = 13$$  
*Solution*:  
Row operations on augmented matrix:  
$R_2 \to R_2 - 2R_1 \implies [0, 1, 1 | 1]$.  
$R_3 \to R_3 - 3R_1 \implies [0, 1, k-3 | 1]$.  
$R_3 \to R_3 - R_2 \implies [0, 0, k-4 | 0]$.  
For infinitely many solutions, $k - 4 = 0 \implies \mathbf{k = 4}$.

**EM04**. Find the trace and determinant of the matrix $B = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & -3 \end{pmatrix}$.  
*Solution*:  
Since $B$ is upper triangular:  
$\text{Trace} = \sum \text{diagonal} = 2 + 4 + (-3) = \mathbf{3}$.  
$\text{Determinant} = \prod \text{diagonal} = 2 \times 4 \times (-3) = \mathbf{-24}$.

**EM05**. If $A$ is an orthogonal matrix ($A^T A = I$), what are the possible real values of $\det(A)$?  
*Solution*:  
$\det(A^T A) = \det(A^T)\det(A) = [\det(A)]^2 = \det(I) = 1 \implies \det(A) = \mathbf{\pm 1}$.

**EM06**. Compute the matrix product $A A^T$ where $A = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 1 \end{pmatrix}$.  
*Solution*:  
Row 1: $1^2 + 2^2 + 0^2 = 5$. Row 1 $\cdot$ Row 2: $1(2) + 2(1) + 0(1) = 4$.  
Row 2 $\cdot$ Row 1: $4$. Row 2: $2^2 + 1^2 + 1^2 = 6$.  
$$A A^T = \mathbf{\begin{pmatrix} 5 & 4 \\ 4 & 6 \end{pmatrix}}$$

**EM07**. If matrix $C = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, find $C^{-1}$.  
*Solution*:  
$\det(C) = 1(4) - 2(3) = -2$.  
Adj$(C) = \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$.  
$$C^{-1} = -\frac{1}{2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \mathbf{\begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix}}$$

**EM08**. The matrix $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ represents which geometric transformation in $\mathbb{R}^2$?  
*Solution*:  
$P \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} y \\ x \end{pmatrix}$.  
*Answer*: **Reflection across the line $y = x$**.

**EM09**. Determine the rank of matrix $M = \begin{pmatrix} 1 & 3 & 5 \\ 2 & 6 & 10 \\ -1 & -3 & -5 \end{pmatrix}$.  
*Solution*:  
Row 2 is $2 \times R_1$, and Row 3 is $-1 \times R_1$.  
Both can be eliminated via elementary row operations.  
*Answer*: $\text{Rank} = \mathbf{1}$.

**EM10**. If $A$ is a $3 \times 3$ matrix with $\det(A) = 5$, find $\det(2A)$.  
*Solution*:  
For an $n \times n$ matrix: $\det(k A) = k^n \det(A)$.  
Here $n = 3, k = 2 \implies \det(2A) = 2^3 \times 5 = 8 \times 5 = \mathbf{40}$.

**EM11**. Find the normalized eigenvector corresponding to $\lambda = 1$ for $A = \begin{pmatrix} 3 & -2 \\ 4 & -3 \end{pmatrix}$.  
*Solution*:  
$(A - I)v = 0 \implies \begin{pmatrix} 2 & -2 \\ 4 & -4 \end{pmatrix}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 0 \implies 2v_1 - 2v_2 = 0 \implies v_1 = v_2$.  
Unnormalized eigenvector is $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$.  
Normalized: $\mathbf{\frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}}$.

**EM12**. If $A$ is idempotent ($A^2 = A$), what are the possible eigenvalues of $A$?  
*Solution*:  
$A v = \lambda v \implies A^2 v = \lambda^2 v$.  
Since $A^2 = A$, $\lambda^2 v = \lambda v \implies \lambda(\lambda - 1) = 0 \implies \mathbf{\lambda \in \{0, 1\}}$.

**EM13**. If $S$ is a skew-symmetric matrix ($S^T = -S$), what can be said about all its diagonal entries?  
*Solution*:  
$s_{ii} = -s_{ii} \implies 2s_{ii} = 0 \implies \mathbf{s_{ii} = 0}$ for all $i$. All diagonal entries must be strictly zero.

**EM14**. Evaluate the determinant of the Vandermonde matrix $V = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & 9 \end{pmatrix}$.  
*Solution*:  
$\det(V) = (x_2 - x_1)(x_3 - x_1)(x_3 - x_2) = (2 - 1)(3 - 1)(3 - 2) = 1 \times 2 \times 1 = \mathbf{2}$.

**EM15**. Find the projection of vector $\vec{u} = (2, 3, 1)$ onto vector $\vec{v} = (1, 1, 1)$.  
*Solution*:  
$\text{proj}_{\vec{v}} \vec{u} = \frac{\vec{u} \cdot \vec{v}}{\|\vec{v}\|^2} \vec{v}$.  
$\vec{u} \cdot \vec{v} = 2(1) + 3(1) + 1(1) = 6$.  
$\|\vec{v}\|^2 = 1^2 + 1^2 + 1^2 = 3$.  
$\text{proj}_{\vec{v}} \vec{u} = \frac{6}{3}(1, 1, 1) = \mathbf{(2, 2, 2)}$.

---

### Calculus, Differential Equations & Vector Fields (Q16–Q40)

**EM16**. Find the derivative of $f(x) = \ln(x^2 + 1)$ with respect to $x$.  
*Solution*:  
$f'(x) = \frac{1}{x^2 + 1} \cdot \frac{d}{dx}(x^2 + 1) = \mathbf{\frac{2x}{x^2 + 1}}$.

**EM17**. Evaluate the definite integral $\int_0^1 x e^x dx$.  
*Solution*:  
Integration by parts: $\int u v' dx = u v - \int u' v dx$.  
$u = x, v' = e^x \implies u' = 1, v = e^x$.  
$[x e^x]_0^1 - \int_0^1 e^x dx = (1 e^1 - 0) - [e^x]_0^1 = e - (e - 1) = \mathbf{1}$.

**EM18**. Find the critical points of $f(x, y) = x^2 + y^2 - 4x - 6y + 13$.  
*Solution*:  
$f_x = 2x - 4 = 0 \implies x = 2$.  
$f_y = 2y - 6 = 0 \implies y = 3$.  
Critical point is $\mathbf{(2, 3)}$, which is an absolute minimum ($f(2, 3) = 0$).

**EM19**. Solve the separable differential equation $\frac{dy}{dx} = \frac{x}{y}$, with $y(0) = 4$.  
*Solution*:  
$y dy = x dx \implies \frac{y^2}{2} = \frac{x^2}{2} + C \implies y^2 = x^2 + 2C$.  
$y(0) = 4 \implies 16 = 0 + 2C \implies 2C = 16$.  
$y^2 = x^2 + 16 \implies \mathbf{y(x) = \sqrt{x^2 + 16}}$.

**EM20**. What is the directional derivative of $\phi(x, y) = x^2 y$ at $(1, 2)$ in the direction of vector $\vec{v} = 3\hat{i} + 4\hat{j}$?  
*Solution*:  
$\nabla \phi = (2xy)\hat{i} + (x^2)\hat{j} \implies \nabla \phi(1, 2) = 4\hat{i} + 1\hat{j}$.  
Unit vector $\hat{u} = \frac{3\hat{i} + 4\hat{j}}{5} = 0.6\hat{i} + 0.8\hat{j}$.  
$D_{\vec{u}} \phi = \nabla \phi \cdot \hat{u} = 4(0.6) + 1(0.8) = 2.4 + 0.8 = \mathbf{3.2}$.

**EM21**. Evaluate $\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$.  
*Solution*:  
Taylor expansion: $e^x = 1 + x + \frac{x^2}{2} + O(x^3)$.  
$\lim_{x \to 0} \frac{(1 + x + x^2/2) - 1 - x}{x^2} = \lim_{x \to 0} \frac{x^2/2}{x^2} = \mathbf{\frac{1}{2}}$.

**EM22**. Find the divergence of the vector field $\vec{V} = (x^2 y)\hat{i} + (y^2 z)\hat{j} + (z^2 x)\hat{k}$ at point $(1, 1, 1)$.  
*Solution*:  
$\nabla \cdot \vec{V} = \frac{\partial V_x}{\partial x} + \frac{\partial V_y}{\partial y} + \frac{\partial V_z}{\partial z} = 2xy + 2yz + 2zx$.  
At $(1, 1, 1)$: $2(1) + 2(1) + 2(1) = \mathbf{6}$.

**EM23**. Solve the ODE $\frac{d^2 y}{dx^2} - 4\frac{dy}{dx} + 4y = 0$.  
*Solution*:  
$r^2 - 4r + 4 = 0 \implies (r - 2)^2 = 0 \implies r = 2$ (repeated root).  
$$y(x) = \mathbf{(c_1 + c_2 x) e^{2x}}$$

**EM24**. Evaluate the line integral $\oint_C (y dx - x dy)$ along the unit circle $x^2 + y^2 = 1$ traversed counter-clockwise.  
*Solution*:  
By Green's Theorem: $\oint_C (L dx + M dy) = \iint_R \left(\frac{\partial M}{\partial x} - \frac{\partial L}{\partial y}\right) dA$.  
$L = y, M = -x \implies \frac{\partial M}{\partial x} - \frac{\partial L}{\partial y} = -1 - 1 = -2$.  
$\iint_R (-2) dA = -2 \times \text{Area}(\text{circle}) = -2 \times \pi (1)^2 = \mathbf{-2\pi}$.

**EM25**. What is the order and degree of the differential equation $\left(\frac{d^2 y}{dx^2}\right)^3 + \left(\frac{dy}{dx}\right)^4 + y = 0$?  
*Solution*:  
Highest derivative is $\frac{d^2 y}{dx^2} \implies \text{Order} = \mathbf{2}$.  
Power of highest derivative is $3 \implies \text{Degree} = \mathbf{3}$.

**EM26**. Evaluate the double integral $\int_0^1 \int_0^2 x y^2 dy dx$.  
*Solution*:  
Separable: $\left(\int_0^1 x dx\right) \left(\int_0^2 y^2 dy\right) = \left[\frac{x^2}{2}\right]_0^1 \left[\frac{y^3}{3}\right]_0^2 = \frac{1}{2} \times \frac{8}{3} = \mathbf{\frac{4}{3}}$.

**EM27**. Find the radius of convergence of the power series $\sum_{n=1}^\infty \frac{x^n}{n \cdot 3^n}$.  
*Solution*:  
Ratio test: $L = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = \lim_{n \to \infty} \left|\frac{x^{n+1}}{(n+1)3^{n+1}} \cdot \frac{n 3^n}{x^n}\right| = \frac{|x|}{3} < 1 \implies |x| < 3$.  
Radius of convergence $R = \mathbf{3}$.

**EM28**. Find the particular integral of $\frac{d^2 y}{dx^2} + 4y = \sin(x)$.  
*Solution*:  
$y_p = \frac{1}{D^2 + 4} \sin(x)$. Replace $D^2$ with $-1^2 = -1$:  
$y_p = \frac{1}{-1 + 4} \sin(x) = \mathbf{\frac{1}{3}\sin(x)}$.

**EM29**. Evaluate $\int_0^\infty e^{-2x} dx$.  
*Solution*:  
$\left[ -\frac{1}{2} e^{-2x} \right]_0^\infty = 0 - \left(-\frac{1}{2}\right) = \mathbf{\frac{1}{2} = 0.5}$.

**EM30**. If $u(x, t) = \sin(x - c t)$, does $u$ satisfy the 1D wave equation $\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$?  
*Solution*:  
$u_{tt} = -c^2 \sin(x - ct)$.  
$u_{xx} = -\sin(x - ct) \implies c^2 u_{xx} = -c^2 \sin(x - ct)$.  
Since $u_{tt} = c^2 u_{xx}$, the answer is **Yes (Identically satisfies)**.

**EM31**. Find the stationary point of $f(x) = x \ln(x)$ for $x > 0$.  
*Solution*:  
$f'(x) = \ln(x) + x(1/x) = \ln(x) + 1 = 0 \implies \ln(x) = -1 \implies \mathbf{x = e^{-1} = \frac{1}{e}}$.

**EM32**. Compute the Fourier transform of a rectangular pulse of width $T$ centered at zero.  
*Solution*:  
$F(\omega) = \int_{-T/2}^{T/2} 1 \cdot e^{-i\omega t} dt = \left[\frac{e^{-i\omega t}}{-i\omega}\right]_{-T/2}^{T/2} = \frac{e^{i\omega T/2} - e^{-i\omega T/2}}{i\omega} = \frac{2\sin(\omega T/2)}{\omega} = \mathbf{T \cdot \text{sinc}\left(\frac{\omega T}{2\pi}\right)}$.

**EM33**. Evaluate the surface area of a paraboloid $z = x^2 + y^2$ below $z = 1$.  
*Solution*:  
$dA = \sqrt{1 + z_x^2 + z_y^2} dx dy = \sqrt{1 + 4(x^2 + y^2)} dx dy = \sqrt{1 + 4r^2} r dr d\theta$.  
$\int_0^{2\pi} d\theta \int_0^1 \sqrt{1 + 4r^2} r dr = 2\pi \left[\frac{(1 + 4r^2)^{3/2}}{12}\right]_0^1 = \frac{\pi}{6}(5^{3/2} - 1) = \mathbf{\frac{\pi}{6}(5\sqrt{5} - 1) \approx 5.33}$.

**EM34**. What is the curl of a gradient field $\nabla \times (\nabla \phi)$ for any smooth scalar field $\phi$?  
*Solution*:  
$\text{curl}(\text{grad } \phi) = \mathbf{\vec{0}}$ (Identically zero for all $C^2$ scalar fields).

**EM35**. Solve the differential equation $x \frac{dy}{dx} - y = x^2$.  
*Solution*:  
$\frac{dy}{dx} - \frac{1}{x} y = x$. Integrating factor $I = e^{\int -1/x dx} = e^{-\ln x} = \frac{1}{x}$.  
$y \cdot \frac{1}{x} = \int x \cdot \frac{1}{x} dx = \int 1 dx = x + C \implies \mathbf{y(x) = x^2 + C x}$.

**EM36**. Evaluate the limit: $\lim_{x \to \infty} \left(1 + \frac{3}{x}\right)^{2x}$.  
*Solution*:  
$\lim_{x \to \infty} \left[\left(1 + \frac{3}{x}\right)^x\right]^2 = (e^3)^2 = \mathbf{e^6}$.

**EM37**. What is the residue of $f(z) = \frac{1}{z(z - 1)}$ at pole $z = 1$?  
*Solution*:  
$\text{Res}(f, 1) = \lim_{z \to 1} (z - 1) \frac{1}{z(z - 1)} = \lim_{z \to 1} \frac{1}{z} = \mathbf{1}$.

**EM38**. Find the second derivative $\frac{d^2 y}{dx^2}$ if $x = t^2$ and $y = t^3$.  
*Solution*:  
$\frac{dx}{dt} = 2t$, $\frac{dy}{dt} = 3t^2 \implies \frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3}{2}t$.  
$$\frac{d^2 y}{dx^2} = \frac{d}{dt}\left(\frac{3}{2}t\right) \cdot \frac{dt}{dx} = \frac{3}{2} \cdot \frac{1}{2t} = \mathbf{\frac{3}{4t}}$$

**EM39**. If $f(x)$ is an odd function, what is $\int_{-a}^a f(x) dx$?  
*Solution*:  
For any odd function where $f(-x) = -f(x)$, $\int_{-a}^a f(x) dx = \mathbf{0}$.

**EM40**. Find the work done by force field $\vec{F} = 3x^2 \hat{i} + 2y \hat{j}$ moving a particle from $(0, 0)$ to $(2, 3)$.  
*Solution*:  
Notice $\vec{F}$ is conservative with potential $\phi(x, y) = x^3 + y^2$.  
$\text{Work} = \phi(2, 3) - \phi(0, 0) = (2^3 + 3^2) - 0 = 8 + 9 = \mathbf{17 \text{ Joules}}$.

---

## Part 2: Statistics & Probability (40 Questions)

### Probability Theory & Distributions (Q41–Q60)

**SP41**. If random variable $X \sim \text{Poisson}(\lambda = 3)$, calculate $P(X = 2)$.  
*Solution*:  
$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$.  
$$P(X = 2) = \frac{3^2 e^{-3}}{2!} = \frac{9 e^{-3}}{2} \approx \frac{9 \times 0.049787}{2} = \mathbf{0.2240}$$

**SP42**. The lifetime of an optical inspection laser source follows an Exponential distribution with mean $\theta = 2000\text{ hours}$. What is the probability that the laser survives beyond $4000\text{ hours}$?  
*Solution*:  
Rate parameter $\lambda = \frac{1}{2000} = 0.0005\text{ hr}^{-1}$.  
Survival function $S(t) = P(T > t) = e^{-\lambda t}$.  
$$P(T > 4000) = e^{-0.0005 \times 4000} = e^{-2} \approx \mathbf{0.1353 \text{ (13.53\%)}}$$

**SP43**. If $X \sim \mathcal{N}(\mu = 50, \sigma^2 = 16)$, find the $Z$-score for $X = 58$.  
*Solution*:  
$\sigma = \sqrt{16} = 4$.  
$$Z = \frac{X - \mu}{\sigma} = \frac{58 - 50}{4} = \frac{8}{4} = \mathbf{+2.00}$$

**SP44**. What is the variance of a Binomial random variable $X \sim B(n = 100, p = 0.05)$?  
*Solution*:  
$\text{Var}(X) = n p (1 - p) = 100 \times 0.05 \times 0.95 = 5 \times 0.95 = \mathbf{4.75}$.

**SP45**. For two random variables $X$ and $Y$, $\text{Var}(X) = 9, \text{Var}(Y) = 16$, and $\text{Cov}(X, Y) = 6$. What is the correlation coefficient $\rho_{XY}$?  
*Solution*:  
$$\rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{6}{\sqrt{9} \times \sqrt{16}} = \frac{6}{3 \times 4} = \frac{6}{12} = \mathbf{0.50}$$

**SP46**. If $X$ is uniformly distributed on $[2, 10]$, calculate its expectation $E[X]$ and variance $\text{Var}(X)$.  
*Solution*:  
$E[X] = \frac{a + b}{2} = \frac{2 + 10}{2} = \mathbf{6.0}$.  
$\text{Var}(X) = \frac{(b - a)^2}{12} = \frac{(10 - 2)^2}{12} = \frac{64}{12} = \mathbf{\frac{16}{3} \approx 5.33}$.

**SP47**. In a fab cleanroom, defective die clusters follow a Geometric distribution with success probability $p = 0.25$. What is the expected number of trials until the first defective die is observed?  
*Solution*:  
For a Geometric distribution: $E[X] = \frac{1}{p} = \frac{1}{0.25} = \mathbf{4 \text{ trials}}$.

**SP48**. What is the relationship between Mean, Median, and Mode in a positively skewed distribution?  
*Solution*:  
In a right/positively skewed distribution with a long right tail:  
$$\mathbf{\text{Mean} > \text{Median} > \text{Mode}}$$

**SP49**. If $E[X] = 10$ and $E[X^2] = 116$, what is the standard deviation $\sigma_X$?  
*Solution*:  
$\text{Var}(X) = E[X^2] - (E[X])^2 = 116 - 10^2 = 116 - 100 = 16$.  
Standard deviation $\sigma_X = \sqrt{16} = \mathbf{4.0}$.

**SP50**. State Chebyshev's inequality for any distribution: What is the maximum probability that a random variable deviates from its mean by more than $3$ standard deviations?  
*Solution*:  
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$  
For $k = 3$: $P(|X - \mu| \ge 3\sigma) \le \frac{1}{3^2} = \mathbf{\frac{1}{9} \approx 0.1111 \text{ (11.11\%)}}$.

**SP51**. If $X_1, X_2 \dots X_n$ are independent identically distributed random variables with mean $\mu$ and variance $\sigma^2$, what is the variance of their sample mean $\bar{X}$?  
*Solution*:  
$$\text{Var}(\bar{X}) = \text{Var}\left(\frac{1}{n}\sum X_i\right) = \frac{1}{n^2} \sum \text{Var}(X_i) = \frac{n \sigma^2}{n^2} = \mathbf{\frac{\sigma^2}{n}}$$

**SP52**. What is the moment generating function (MGF) of an Exponential distribution with parameter $\lambda$?  
*Solution*:  
$$M_X(t) = E[e^{tX}] = \int_0^\infty e^{tx} \lambda e^{-\lambda x} dx = \lambda \int_0^\infty e^{-(\lambda - t)x} dx = \mathbf{\frac{\lambda}{\lambda - t}} \quad (t < \lambda)$$

**SP53**. A continuous random variable has probability density function $f(x) = k x^2$ for $0 \le x \le 2$. Find the value of constant $k$.  
*Solution*:  
$\int_0^2 k x^2 dx = 1 \implies k \left[\frac{x^3}{3}\right]_0^2 = k \left(\frac{8}{3}\right) = 1 \implies \mathbf{k = \frac{3}{8} = 0.375}$.

**SP54**. If $P(A) = 0.4, P(B) = 0.5$, and $P(A \cap B) = 0.2$, are events $A$ and $B$ independent?  
*Solution*:  
Check $P(A) \times P(B) = 0.4 \times 0.5 = 0.20$.  
Since $P(A \cap B) = 0.20 = P(A)P(B)$, the events are **Independent**.

**SP55**. What is the kurtosis of a standard Normal distribution?  
*Solution*:  
The standard (raw) kurtosis is **3.0**. The excess kurtosis ($\text{Kurtosis} - 3$) is **0.0**.

**SP56**. If two independent normal variables $X \sim \mathcal{N}(10, 4)$ and $Y \sim \mathcal{N}(20, 9)$ are added, what is the distribution of $Z = X + Y$?  
*Solution*:  
Means add: $\mu_Z = 10 + 20 = 30$. Variances add: $\sigma_Z^2 = 4 + 9 = 13$.  
$$Z \sim \mathbf{\mathcal{N}(30, 13)}$$

**SP57**. In hypothesis testing, what is the definition of a Type I error ($\alpha$)?  
*Solution*:  
A Type I error occurs when the test **rejects the null hypothesis ($H_0$) given that $H_0$ is actually true** (False Positive).

**SP58**. In hypothesis testing, what is the definition of a Type II error ($\beta$)?  
*Solution*:  
A Type II error occurs when the test **fails to reject the null hypothesis ($H_0$) given that $H_0$ is false** (False Negative). Statistical Power is $1 - \beta$.

**SP59**. For a sample of size $N = 25$ drawn from a normal population with unknown variance, which statistical test is used to test whether the population mean equals a hypothesized value $\mu_0$?  
*Solution*:  
The **One-Sample Student's $t$-test** with $N - 1 = 24$ degrees of freedom.

**SP60**. In linear regression $y = \beta_0 + \beta_1 x + \epsilon$, what does the coefficient of determination $R^2$ represent?  
*Solution*:  
$R^2$ represents the **proportion of the total variance in the dependent variable $y$ that is explained by the linear model**: $R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}$.

---

### Inferential Statistics & Statistical Process Control (Q61–Q80)

**SP61**. A gate oxide etch process has upper specification limit $USL = 105\text{ nm}$, lower specification limit $LSL = 95\text{ nm}$, process mean $\mu = 100\text{ nm}$, and process standard deviation $\sigma = 1.0\text{ nm}$. Calculate the process capability ratio $C_p$.  
*Solution*:  
$$C_p = \frac{USL - LSL}{6\sigma} = \frac{105 - 95}{6(1.0)} = \frac{10}{6} = \mathbf{1.67}$$

**SP62**. In the same etch process, suppose the mean drifts to $\mu = 102\text{ nm}$ while $\sigma$ remains $1.0\text{ nm}$. Calculate $C_{pk}$.  
*Solution*:  
$$CPU = \frac{USL - \mu}{3\sigma} = \frac{105 - 102}{3(1.0)} = \frac{3}{3} = 1.00$$  
$$CPL = \frac{\mu - LSL}{3\sigma} = \frac{102 - 95}{3(1.0)} = \frac{7}{3} = 2.33$$  
$$C_{pk} = \min(CPU, CPL) = \mathbf{1.00}$$

**SP63**. What is the Upper Control Limit (UCL) for a Shewhart $\bar{X}$-chart with sample subgroup size $n = 4$, process mean $\bar{\bar{X}} = 50.0$, and standard deviation $\sigma = 2.0$?  
*Solution*:  
$$\text{UCL} = \bar{\bar{X}} + 3 \frac{\sigma}{\sqrt{n}} = 50.0 + 3 \left(\frac{2.0}{\sqrt{4}}\right) = 50.0 + 3(1.0) = \mathbf{53.0}$$

**SP64**. If a process is centered ($C_p = C_{pk}$), what is the relationship between the process mean $\mu$ and the specification limits?  
*Solution*:  
The process mean lies at the exact midpoint: $\mathbf{\mu = \frac{USL + LSL}{2}}$.

**SP65**. In Western Electric Rule 1 for SPC control charts, what triggers an out-of-control alarm?  
*Solution*:  
**Any single point falling beyond either $3\sigma$ control limit** (UCL or LCL).

**SP66**. In Western Electric Rule 2, what pattern triggers an alarm?  
*Solution*:  
**Two out of three consecutive points falling beyond the $2\sigma$ warning limits on the same side of the center line**.

**SP67**. In Western Electric Rule 3, what pattern triggers an alarm?  
*Solution*:  
**Four out of five consecutive points falling beyond the $1\sigma$ band on the same side of the center line**.

**SP68**. In Western Electric Rule 4 (Run rule), what pattern triggers an alarm?  
*Solution*:  
**Eight consecutive points falling on the same side of the center line**, indicating a systematic process shift.

**SP69**. In a dataset of 100 wafer inspection defect counts, the median is 45 and the Interquartile Range (IQR) is 20 ($Q_1 = 35, Q_3 = 55$). According to Tukey's boxplot rule, what is the lower and upper threshold for flagging an outlier?  
*Solution*:  
$\text{Lower Threshold} = Q_1 - 1.5 \times \text{IQR} = 35 - 1.5(20) = 35 - 30 = \mathbf{5}$.  
$\text{Upper Threshold} = Q_3 + 1.5 \times \text{IQR} = 55 + 1.5(20) = 55 + 30 = \mathbf{85}$.

**SP70**. If a random sample of $N = 64$ wafers has mean defect count $\bar{X} = 120$ and sample standard deviation $s = 16$, construct the $95\%$ confidence interval for the population mean ($\approx Z_{0.025} = 1.96$).  
*Solution*:  
$$\text{Standard Error } SE = \frac{s}{\sqrt{N}} = \frac{16}{\sqrt{64}} = \frac{16}{8} = 2.0$$  
$$\text{Margin of Error} = 1.96 \times 2.0 = 3.92$$  
$$95\% \text{ CI} = [120 - 3.92, 120 + 3.92] = \mathbf{[116.08, 123.92]}$$

**SP71**. When comparing the mean yield of two independent fab lines with unknown and unequal variances, which test is statistically appropriate?  
*Solution*:  
**Welch's Two-Sample $t$-test** (unequal variance $t$-test).

**SP72**. What is the degree of freedom for a Chi-Square test of independence in a contingency table with $r = 3$ rows and $c = 4$ columns?  
*Solution*:  
$$\text{df} = (r - 1)(c - 1) = (3 - 1)(4 - 1) = 2 \times 3 = \mathbf{6}$$

**SP73**. A binary classifier detects killer wafer defects. In a test on 1,000 dies: True Positives $(TP) = 80$, False Positives $(FP) = 20$, False Negatives $(FN) = 10$, True Negatives $(TN) = 890$. Calculate the **Precision** of the classifier.  
*Solution*:  
$$\text{Precision} = \frac{TP}{TP + FP} = \frac{80}{80 + 20} = \frac{80}{100} = \mathbf{0.80 \text{ (80\%)}}$$

**SP74**. For the same classifier, calculate the **Recall** (Sensitivity / Defect Capture Rate).  
*Solution*:  
$$\text{Recall} = \frac{TP}{TP + FN} = \frac{80}{80 + 10} = \frac{80}{90} = \mathbf{0.8889 \text{ (88.89\%)}}$$

**SP75**. Calculate the **F1-Score** for this classifier.  
*Solution*:  
$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times \frac{0.80 \times 0.8889}{0.80 + 0.8889} = 2 \times \frac{0.7111}{1.6889} \approx \mathbf{0.8421}$$

**SP76**. In an Analysis of Variance (ANOVA), what is the test statistic used to evaluate whether multiple group means are equal?  
*Solution*:  
The **$F$-statistic**: $F = \frac{\text{Mean Square Between Groups (MSB)}}{\text{Mean Square Within Groups (MSW)}}$.

**SP77**. If the $p$-value of an experimental test is $0.012$, does this reject the null hypothesis at the $\alpha = 0.05$ significance level?  
*Solution*:  
Yes, since $p = 0.012 < \alpha = 0.05$, we **reject the null hypothesis** (statistically significant difference).

**SP78**. In a Poisson process, what is the relationship between the mean and the variance?  
*Solution*:  
For any Poisson distribution: $\mathbf{\text{Mean} = \text{Variance} = \lambda}$.

**SP79**. If a dataset has variance $\sigma^2 = 25$ and mean $\mu = 10$, what is its Coefficient of Variation ($CV$)?  
*Solution*:  
$\sigma = \sqrt{25} = 5$.  
$$CV = \frac{\sigma}{\mu} = \frac{5}{10} = \mathbf{0.50 \text{ (or 50\%)}}$$

**SP80**. What transformation is commonly applied to stabilize the variance of Poisson count data (e.g. defect counts)?  
*Solution*:  
The **Square-Root Transformation**: $Y = \sqrt{X}$ (or Freeman-Tukey $\sqrt{X} + \sqrt{X+1}$).


---

## Part 3: Data Interpretation & Fab Yield Metrics (40 Questions)

### Table & Chart Data Interpretation (Q81–Q100)

*Questions DI81 to DI90 refer to the following multi-lot wafer inspection table:*

```text
Table 3: Multi-Lot Defect Breakdown by Inspection Stage
┌─────────┬──────────────┬──────────────┬──────────────┬──────────────┐
│ Lot ID  │ Litho Defects│ Etch Defects │ CMP Defects  │ Film Defects │
├─────────┼──────────────┼──────────────┼──────────────┼──────────────┤
│ LOT-01  │ 450          │ 320          │ 680          │ 150          │
│ LOT-02  │ 520          │ 410          │ 890          │ 180          │
│ LOT-03  │ 380          │ 290          │ 420          │ 110          │
│ LOT-04  │ 610          │ 480          │ 1,120        │ 240          │
│ LOT-05  │ 490          │ 360          │ 750          │ 160          │
└─────────┴──────────────┴──────────────┴──────────────┴──────────────┘
```

**DI81**. What was the total number of CMP defects detected across all 5 lots?  
*Solution*:  
Sum $= 680 + 890 + 420 + 1,120 + 750 = \mathbf{3,860 \text{ CMP defects}}$.

**DI82**. Which lot recorded the highest proportion of its total defects at the CMP stage?  
*Solution*:  
Compute CMP / Total for each lot:  
* LOT-01: Total $= 1600 \implies 680 / 1600 = 42.50\%$  
* LOT-02: Total $= 2000 \implies 890 / 2000 = 44.50\%$  
* LOT-03: Total $= 1200 \implies 420 / 1200 = 35.00\%$  
* LOT-04: Total $= 2450 \implies 1120 / 2450 \approx 45.71\%$  
* LOT-05: Total $= 1760 \implies 750 / 1760 \approx 42.61\%$  
*Answer*: **LOT-04** had the highest proportion ($45.71\%$).

**DI83**. What was the average number of Lithography defects per lot?  
*Solution*:  
Total Litho $= 450 + 520 + 380 + 610 + 490 = 2,450$.  
Average $= 2,450 / 5 = \mathbf{490 \text{ defects/lot}}$.

**DI84**. What percentage of total defects across all lots were Film defects?  
*Solution*:  
Total Film $= 150 + 180 + 110 + 240 + 160 = 840$.  
Grand Total Defects $= 2,450 \text{ (Litho)} + 1,860 \text{ (Etch)} + 3,860 \text{ (CMP)} + 840 \text{ (Film)} = 9,010$.  
Percentage $= \frac{840}{9,010} \times 100 \approx \mathbf{9.32\%}$.

**DI85**. By what percentage did LOT-04's total defect count exceed LOT-03's total defect count?  
*Solution*:  
LOT-04 Total $= 2,450$. LOT-03 Total $= 1,200$.  
Increase $= \frac{2,450 - 1,200}{1,200} \times 100 = \frac{1,250}{1,200} \times 100 = \mathbf{104.17\%}$.

**DI86**. If the target defect threshold for a lot is $\le 1,500$ total defects, which lot(s) met the quality target?  
*Solution*:  
Totals: LOT-01 ($1,600$), LOT-02 ($2,000$), LOT-03 ($1,200$), LOT-04 ($2,450$), LOT-05 ($1,760$).  
Only **LOT-03** ($1,200 \le 1,500$) met the target.

**DI87**. What is the ratio of total Lithography defects to total Etch defects across all lots?  
*Solution*:  
Litho Total $= 2,450$. Etch Total $= 320 + 410 + 290 + 480 + 360 = 1,860$.  
Ratio $= \frac{2,450}{1,860} = \frac{245}{186} \approx \mathbf{1.317 : 1}$.

**DI88**. If an engineering optimization reduces CMP defects by $30\%$ across all lots while other defect counts remain unchanged, what is the new grand total defect count?  
*Solution*:  
Original Grand Total $= 9,010$.  
CMP reduction $= 3,860 \times 0.30 = 1,158$ defects removed.  
New Grand Total $= 9,010 - 1,158 = \mathbf{7,852 \text{ defects}}$.

**DI89**. What is the median total defect count among the 5 lots?  
*Solution*:  
Ordered lot totals: $1,200\text{ (LOT-03)}, 1,600\text{ (LOT-01)}, \mathbf{1,760\text{ (LOT-05)}}, 2,000\text{ (LOT-02)}, 2,450\text{ (LOT-04)}$.  
Median $= \mathbf{1,760 \text{ defects}}$.

**DI90**. If each Etch defect incurs an average scrap recovery cost of $\$45$, what was the total scrap recovery cost attributable to Etch defects in LOT-02 and LOT-04 combined?  
*Solution*:  
Etch defects in LOT-02 $= 410$; in LOT-04 $= 480$.  
Sum $= 410 + 480 = 890\text{ defects}$.  
Cost $= 890 \times \$45 = \mathbf{\$40,050}$.

---

*Questions DI91 to DI100 refer to the following wafer yield line chart metrics:*

```text
Table 4: Monthly Wafer Sort Yield (%) by Fab Line
┌───────────┬──────────────┬──────────────┬──────────────┐
│ Month     │ Fab Alpha    │ Fab Beta     │ Fab Gamma    │
├───────────┼──────────────┼──────────────┼──────────────┤
│ January   │ 92.4%        │ 88.6%        │ 94.1%        │
│ February  │ 91.8%        │ 89.2%        │ 93.8%        │
│ March     │ 93.5%        │ 90.1%        │ 92.5%        │
│ April     │ 94.2%        │ 91.5%        │ 94.6%        │
│ May       │ 95.0%        │ 92.0%        │ 95.2%        │
│ June      │ 95.8%        │ 92.8%        │ 94.9%        │
└───────────┴──────────────┴──────────────┴──────────────┘
```

**DI91**. Which fab line experienced a consistent month-over-month increase in yield across the entire 6-month period?  
*Solution*:  
* Fab Alpha: Jan (92.4) $\to$ Feb (91.8) (Decreased).  
* Fab Beta: $88.6 \to 89.2 \to 90.1 \to 91.5 \to 92.0 \to 92.8$ (Strictly increasing every month!).  
* Fab Gamma: Jan (94.1) $\to$ Feb (93.8) (Decreased).  
*Answer*: **Fab Beta**.

**DI92**. What was the average yield of Fab Alpha over the 6-month period?  
*Solution*:  
Sum $= 92.4 + 91.8 + 93.5 + 94.2 + 95.0 + 95.8 = 562.7\%$.  
Average $= \frac{562.7}{6} = \mathbf{93.78\%}$.

**DI93**. In which month was the difference between the highest and lowest fab yield the smallest?  
*Solution*:  
* Jan: $94.1 - 88.6 = 5.5$  
* Feb: $93.8 - 89.2 = 4.6$  
* Mar: $93.5 - 90.1 = 3.4$  
* Apr: $94.6 - 91.5 = 3.1$  
* May: $95.2 - 92.0 = 3.2$  
* Jun: $95.8 - 92.8 = \mathbf{3.0}$  
*Answer*: **June** had the smallest range ($3.0$ percentage points).

**DI94**. What was the total percentage point improvement in Fab Beta from January to June?  
*Solution*:  
Improvement $= 92.8\% - 88.6\% = \mathbf{4.2 \text{ percentage points}}$.

**DI95**. If Fab Gamma processes 20,000 wafers in May, how many wafers pass yield?  
*Solution*:  
Passing wafers $= 20,000 \times 0.952 = \mathbf{19,040 \text{ wafers}}$.

**DI96**. In March, by what percentage did Fab Alpha's yield exceed Fab Beta's yield?  
*Solution*:  
Relative difference $= \frac{93.5 - 90.1}{90.1} \times 100 = \frac{3.4}{90.1} \times 100 \approx \mathbf{3.77\%}$.

**DI97**. What was the standard deviation of Fab Gamma's monthly yields?  
*Solution*:  
Values: $94.1, 93.8, 92.5, 94.6, 95.2, 94.9$. Mean $\bar{Y} = 560.1 / 6 = 93.35 \implies 94.183\%$.  
Deviations from $94.183$: $-0.08, -0.38, -1.68, +0.42, +1.02, +0.72$.  
Sum of squares $\approx 0.0064 + 0.1444 + 2.8224 + 0.1764 + 1.0404 + 0.5184 = 4.7084$.  
Sample variance $s^2 = 4.7084 / 5 \approx 0.9417 \implies s \approx \mathbf{0.97\%}$.

**DI98**. Assuming Fab Alpha's yield continues to increase linearly at its May-to-June rate ($+0.8\%$), what will be its projected yield in August?  
*Solution*:  
Rate $= +0.8\%$ per month.  
July: $95.8 + 0.8 = 96.6\%$.  
August: $96.6 + 0.8 = \mathbf{97.4\%}$.

**DI99**. What was the overall combined average yield across all three fabs in April?  
*Solution*:  
$\text{Average} = \frac{94.2 + 91.5 + 94.6}{3} = \frac{280.3}{3} \approx \mathbf{93.43\%}$.

**DI100**. If each $1\%$ drop in yield costs a fab $\$250,000$ in lost margin, how much money did Fab Gamma lose in March compared to its May yield?  
*Solution*:  
Yield difference $= 95.2\% - 92.5\% = 2.7\%$.  
Financial loss $= 2.7 \times \$250,000 = \mathbf{\$675,000}$.

---

### Fab Yield Modeling & Advanced Data Interpretation (Q101–Q120)

**DI101**. In the Poisson yield model $Y = e^{-A D_0}$, if die area $A = 1.5\text{ cm}^2$ and defect density $D_0 = 0.2\text{ defects/cm}^2$, calculate the expected yield $Y$.  
*Solution*:  
$A D_0 = 1.5 \times 0.2 = 0.30$.  
$$Y = e^{-0.30} \approx \mathbf{0.7408 \text{ (74.08\%)}}$$

**DI102**. Using Murphy's yield model $Y = \left(\frac{1 - e^{-A D_0}}{A D_0}\right)^2$ with $A D_0 = 0.5$, calculate $Y$.  
*Solution*:  
$e^{-0.5} \approx 0.6065$.  
$1 - e^{-0.5} = 0.3935$.  
$$\frac{0.3935}{0.5} = 0.7870 \implies Y = (0.7870)^2 \approx \mathbf{0.6194 \text{ (61.94\%)}}$$

**DI103**. In the Negative Binomial yield model $Y = (1 + A D_0 / \alpha)^{-\alpha}$ with $A D_0 = 0.4$ and cluster parameter $\alpha = 2.0$, calculate $Y$.  
*Solution*:  
$$Y = \left(1 + \frac{0.4}{2}\right)^{-2} = (1 + 0.2)^{-2} = (1.2)^{-2} = \frac{1}{1.44} \approx \mathbf{0.6944 \text{ (69.44\%)}}$$

**DI104**. A 300 mm silicon wafer (usable radius $R = 145\text{ mm}$) is diced into square chips of side $10\text{ mm}$. Estimate the total gross die count using the gross die formula $N_{\text{gross}} = \frac{\pi R^2}{A_{\text{die}}} - \frac{2\pi R}{\sqrt{2 A_{\text{die}}}}$.  
*Solution*:  
$A_{\text{die}} = 10 \times 10 = 100\text{ mm}^2$.  
$\frac{\pi (145)^2}{100} = \frac{3.1416 \times 21,025}{100} \approx 660.5$.  
Edge exclusion subtraction: $\frac{2 \pi (145)}{\sqrt{200}} = \frac{911.06}{14.14} \approx 64.4$.  
$$N_{\text{gross}} \approx 660.5 - 64.4 \approx \mathbf{596 \text{ gross dies}}$$

**DI105**. If the gross die count is 600 and the line yield is $88\%$, how many functional dies are obtained from the wafer?  
*Solution*:  
$$\text{Good dies} = 600 \times 0.88 = \mathbf{528 \text{ functional dies}}$$

**DI106**. If wafer manufacturing cost is $\$6,000$ per 300 mm wafer and 500 good dies are yielded, what is the silicon manufacturing cost per good die?  
*Solution*:  
$$\text{Cost per die} = \frac{\$6,000}{500} = \mathbf{\$12.00 \text{ per die}}$$

**DI107**. If the line yield drops from $80\%$ to $60\%$, what is the percentage increase in silicon cost per good die?  
*Solution*:  
Cost is inversely proportional to yield: $\frac{\text{Cost}_1}{\text{Cost}_0} = \frac{Y_0}{Y_1} = \frac{0.80}{0.60} = \frac{4}{3} \approx 1.3333$.  
Cost increases by $\mathbf{33.33\%}$.

**DI108**. A wafer map contains 1,200 total detected defects. If spatial clustering analysis categorizes 960 defects as belonging to scratch or ring signatures, what is the clustering fraction?  
*Solution*:  
$$\text{Clustering Fraction} = \frac{960}{1,200} = \frac{4}{5} = \mathbf{0.80 \text{ (80\%)}}$$

**DI109**. On an overlay metrology chart, the mean overlay error $\bar{x} = +0.8\text{ nm}$ with $\sigma = 0.3\text{ nm}$. Assuming normality, what percentage of measured sites exceed the specification limit of $+1.4\text{ nm}$?  
*Solution*:  
$Z = \frac{1.4 - 0.8}{0.3} = \frac{0.6}{0.3} = +2.00$.  
$P(Z > 2.00) = 1 - 0.9772 = \mathbf{0.0228 \text{ (2.28\%)}}$.

**DI110**. An automated inspection tool scans a 300 mm wafer in 45 minutes. What is the tool's throughput in Wafers Per Hour (WPH)?  
*Solution*:  
$$\text{Throughput} = \frac{60\text{ min/hr}}{45\text{ min/wafer}} = \mathbf{1.33 \text{ WPH}}$$

**DI111**. If recipe optimization reduces scan time from 45 minutes to 30 minutes, what is the percentage increase in tool throughput?  
*Solution*:  
Old WPH $= 1.333$. New WPH $= 60 / 30 = 2.000$.  
Increase $= \frac{2.000 - 1.333}{1.333} \times 100 = \mathbf{50.0\% \text{ increase}}$.

**DI112**. In a Pareto analysis of 5,000 fab defects, 3,200 are bridging shorts, 900 are open vias, 500 are particles, and 400 are color variations. What cumulative percentage of defects is accounted for by the top two defect types?  
*Solution*:  
Top two $= 3,200 + 900 = 4,100$.  
Cumulative percentage $= \frac{4,100}{5,000} \times 100 = \mathbf{82.0\%}$ (confirming the 80/20 rule).

**DI113**. A fab operates 40 identical inspection tools. Each tool has an availability of $92\%$. What is the expected number of tools available for production at any given time?  
*Solution*:  
$$E[N] = 40 \times 0.92 = \mathbf{36.8 \text{ tools}}$$

**DI114**. If Mean Time Between Failures ($MTBF$) is 400 hours and Mean Time To Repair ($MTTR$) is 16 hours, calculate the tool operational availability $A$.  
*Solution*:  
$$A = \frac{MTBF}{MTBF + MTTR} = \frac{400}{400 + 16} = \frac{400}{416} \approx \mathbf{0.9615 \text{ (96.15\%)}}$$

**DI115**. A wafer batch has average roughness $R_a = 0.42\text{ nm}$ before CMP and $0.14\text{ nm}$ after CMP. What was the percentage reduction in surface roughness?  
*Solution*:  
$$\text{Reduction} = \frac{0.42 - 0.14}{0.42} \times 100 = \frac{0.28}{0.42} \times 100 = \frac{2}{3} \times 100 = \mathbf{66.67\%}$$

**DI116**. What is the aspect ratio of a contact hole with depth $3.6\text{ }\mu\text{m}$ and diameter $60\text{ nm}$?  
*Solution*:  
Depth $= 3,600\text{ nm}$. Diameter $= 60\text{ nm}$.  
$$\text{Aspect Ratio} = \frac{3,600}{60} = \mathbf{60 : 1}$$

**DI117**. If an inspection recipe has a False Alarm Rate of $0.05\%$ per die and a wafer has 2,000 dies, how many false alarms are expected per wafer?  
*Solution*:  
$$E[\text{False Alarms}] = 2,000 \times 0.0005 = \mathbf{1.0 \text{ false alarm/wafer}}$$

**DI118**. A fab produces 100,000 wafers per month. If scrap rate is reduced from $2.5\%$ to $1.8\%$, how many additional wafers are saved per month?  
*Solution*:  
Reduction $= 2.5\% - 1.8\% = 0.7\%$.  
Saved wafers $= 100,000 \times 0.007 = \mathbf{700 \text{ wafers/month}}$.

**DI119**. In an optical scatterometer, signal intensity is $I_0 = 1000\text{ counts}$ on a clean substrate and $I = 1450\text{ counts}$ over a defect. What is the optical contrast ratio $C = \frac{I - I_0}{I_0}$?  
*Solution*:  
$$C = \frac{1450 - 1000}{1000} = \frac{450}{1000} = \mathbf{0.45 \text{ (or 45\%)}}$$

**DI120**. If the Signal-to-Noise Ratio ($SNR$) of a defect signal is defined as $SNR = \frac{\Delta I}{\sigma_{\text{noise}}}$, find $SNR$ when $\Delta I = 48\text{ counts}$ and $\sigma_{\text{noise}} = 8\text{ counts}$.  
*Solution*:  
$$SNR = \frac{48}{8} = \mathbf{6.0}$$

---

## Part 4: Python Programming & Algorithmic Problem Solving (40 Questions)

### Python Syntax, Data Structures & Standard Library (Q121–Q140)

**PY121**. What is the output of the following Python snippet?  
```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```  
*Solution*:  
In Python, lists are mutable objects and assignments assign references. `y` refers to the same underlying list as `x`. Appending to `y` modifies `x`.  
*Output*: **4**.

**PY122**. What is the time complexity of looking up a key in a Python `dict` with $N$ entries on average?  
*Solution*:  
Python dictionaries are implemented as hash tables. Average lookup complexity is **$O(1)$**.

**PY123**. What will be printed by the following expression?  
```python
s = "KLA_INSPECTION"
print(s[4:10])
```  
*Solution*:  
Indices: `s[4]` is `'I'`, `s[5]` is `'N'`, `s[6]` is `'S'`, `s[7]` is `'P'`, `s[8]` is `'E'`, `s[9]` is `'C'`. Stop index 10 is exclusive.  
*Output*: **`INSPEC`**.

**PY124**. Write a one-line Python list comprehension to filter out all odd numbers from a list `nums` and return their squares.  
*Solution*:  
```python
[x**2 for x in nums if x % 2 == 0]
```

**PY125**. What is the output of:  
```python
d = {"a": 1, "b": 2}
print(d.get("c", 10))
```  
*Solution*:  
The `.get(key, default)` method returns the default value if the key does not exist. Since `"c"` is not in `d`:  
*Output*: **10**.

**PY126**. How do you reverse a string `s = "SEMICONDUCTOR"` in Python using slicing?  
*Solution*:  
```python
reversed_s = s[::-1]
```

**PY127**. What is the output of the following generator expression?  
```python
gen = (x * 2 for x in range(3))
print(list(gen))
```  
*Solution*:  
`range(3)` yields $0, 1, 2$. Multiplied by 2 yields $0, 2, 4$.  
*Output*: **`[0, 2, 4]`**.

**PY128**. Explain the difference between `is` and `==` in Python.  
*Solution*:  
* `==` checks for **equality of values** (calls `__eq__`).  
* `is` checks for **identity of memory addresses** (`id(a) == id(b)`).

**PY129**. What does the `zip()` function do when passed two lists of unequal length?  
*Solution*:  
In standard Python 3 `zip()`, iteration **stops at the length of the shortest iterable** (unless `itertools.zip_longest()` is used).

**PY130**. What is the output of:  
```python
def func(val, arr=[]):
  arr.append(val)
  return arr


print(func(1))
print(func(2))
```  
*Solution*:  
Default arguments in Python are evaluated once at function definition time. The list `arr` persists across function calls.  
First call returns `[1]`. Second call returns **`[1, 2]`**.

**PY131**. How do you remove duplicate elements from a list `arr = [3, 1, 2, 3, 2, 1]` while preserving order in Python 3.7+?  
*Solution*:  
In Python 3.7+, dictionary insertion order is guaranteed:  
```python
unique_arr = list(dict.fromkeys(arr))  # Result: [3, 1, 2]
```

**PY132**. What is the output of:  
```python
print(bool([])), print(bool([0]))
```  
*Solution*:  
An empty list evaluates to `False`. A non-empty list (even containing `0`) evaluates to `True`.  
*Output*: **`False`**, **`True`**.

**PY133**. Write a Python regular expression pattern to match all KLARF defect lines formatted as: `DefectRecord <id> <x> <y>`.  
*Solution*:  
```python
pattern = r"^DefectRecord\s+(\d+)\s+([-\d.]+)\s+([-\d.]+)$"
```

**PY134**. What is the difference between shallow copy and deep copy in Python?  
*Solution*:  
* `copy.copy()`: Creates a new compound object and inserts references to the original child objects.  
* `copy.deepcopy()`: Creates a new compound object and recursively inserts copies of all nested objects.

**PY135**. How do you read a text file safely in Python to ensure it closes even if an exception occurs?  
*Solution*:  
Using a context manager (`with` block):  
```python
with open("klarf_log.txt", "r") as f:
  data = f.read()
```

**PY136**. What is the output of `sorted([(2, 'b'), (1, 'c'), (2, 'a')])`?  
*Solution*:  
Python sorts tuples lexicographically (first element first, then second element):  
*Output*: **`[(1, 'c'), (2, 'a'), (2, 'b')]`**.

**PY137**. What is the computational complexity of appending an element to the end of a Python list vs. inserting at index 0?  
*Solution*:  
* Appending at end: **$O(1)$ amortized**.  
* Inserting at index 0: **$O(N)$** because all $N$ existing elements must be shifted in memory.

**PY138**. In Python, how do you sort a dictionary `d = {"a": 3, "b": 1, "c": 2}` by its values?  
*Solution*:  
```python
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
# Result: {'b': 1, 'c': 2, 'a': 3}
```

**PY139**. What is a decorator in Python?  
*Solution*:  
A decorator is a callable that takes a function as an argument and returns a replacement function, enabling modification of behavior without altering source code (e.g. logging, execution timing).

**PY140**. What does the `*args` and `**kwargs` syntax allow in function signatures?  
*Solution*:  
* `*args`: Accepts an arbitrary number of positional arguments as a tuple.  
* `**kwargs`: Accepts an arbitrary number of keyword arguments as a dictionary.

---

### NumPy, Pandas & Scientific Computing (Q141–Q160)

**PY141**. Given a NumPy array `a = np.array([10, 20, 30, 40, 50])`, write a vectorized expression to select all elements greater than 25.  
*Solution*:  
```python
result = a[a > 25]  # Output: array([30, 40, 50])
```

**PY142**. What is the result of multiplying two 2D NumPy arrays using `A * B` vs. `A @ B`?  
*Solution*:  
* `A * B`: **Element-wise multiplication** (Hadamard product).  
* `A @ B`: **Matrix dot product** (`np.matmul(A, B)`).

**PY143**. How do you compute the Euclidean distance between two defect coordinate arrays `p1 = np.array([x1, y1])` and `p2 = np.array([x2, y2])` in NumPy?  
*Solution*:  
```python
dist = np.linalg.norm(p1 - p2)  # Or np.sqrt(np.sum((p1 - p2) ** 2))
```

**PY144**. In Pandas, how do you group a DataFrame `df` of wafer defects by column `'layer'` and compute the total count and mean defect size?  
*Solution*:  
```python
summary = df.groupby('layer').agg({'defect_id': 'count', 'size_nm': 'mean'})
```

**PY145**. How do you replace all NaN values in a Pandas DataFrame column `'cd_nm'` with the median of that column?  
*Solution*:  
```python
df['cd_nm'] = df['cd_nm'].fillna(df['cd_nm'].median())
```

**PY146**. What does `np.broadcast_to()` or NumPy broadcasting enable?  
*Solution*:  
NumPy broadcasting allows arithmetic operations on arrays of different shapes by conceptually expanding trailing dimensions of size 1 without unnecessary data replication.

**PY147**. What is the output of `np.zeros((3, 2)).shape`?  
*Solution*:  
*Output*: **`(3, 2)`** (3 rows, 2 columns).

**PY148**. Write a NumPy expression to find the indices of all non-zero elements in array `arr`.  
*Solution*:  
```python
indices = np.nonzero(arr)  # Or np.where(arr != 0)
```

**PY149**. In Pandas, how do you filter rows where column `'defect_type'` is either `'bridge'` or `'scratch'`?  
*Solution*:  
```python
filtered_df = df[df['defect_type'].isin(['bridge', 'scratch'])]
```

**PY150**. What does `df.describe()` return in Pandas?  
*Solution*:  
A summary DataFrame showing descriptive statistics for all numeric columns: count, mean, standard deviation, minimum, 25th percentile ($Q_1$), median, 75th percentile ($Q_3$), and maximum.

**PY151**. How do you normalize a NumPy array `x` to the range $[0, 1]$ using Min-Max scaling?  
*Solution*:  
```python
x_norm = (x - np.min(x)) / (np.max(x) - np.min(x))
```

**PY152**. In Scikit-learn, what does `StandardScaler()` compute for each feature column?  
*Solution*:  
$Z$-score standardization: $z = \frac{x - \mu}{\sigma}$, yielding zero mean and unit variance.

**PY153**. Why is it critical to apply `scaler.fit_transform(X_train)` but only `scaler.transform(X_test)`?  
*Solution*:  
To prevent **data leakage**. Test data must never influence the scaling parameters ($\mu, \sigma$) calculated from the training set.

**PY154**. In training an XGBoost classifier for wafer defect classification, the training class ratio of good to defective dies is $99:1$. What parameter should be tuned in XGBoost to handle this extreme class imbalance?  
*Solution*:  
The **`scale_pos_weight`** parameter (set approximately to $\frac{\text{negative samples}}{\text{positive samples}} \approx 99$).

**PY155**. What do SHAP (SHapley Additive exPlanations) values measure in machine learning model interpretation?  
*Solution*:  
SHAP values allocate credit to each individual feature for a given prediction based on cooperative game theory, quantifying the marginal contribution of each feature to the difference between actual prediction and base expected prediction.

**PY156**. What is the difference between $L_1$ (Lasso) and $L_2$ (Ridge) regularization?  
*Solution*:  
* $L_1$ adds penalty $\lambda \sum |\beta_j|$, driving less important feature weights strictly to zero (automatic feature selection).  
* $L_2$ adds penalty $\lambda \sum \beta_j^2$, shrinking weights toward zero without forcing exact zero sparsity.

**PY157**. What metric should be used instead of Accuracy when evaluating machine learning models on highly imbalanced semiconductor defect datasets?  
*Solution*:  
**PR-AUC (Precision-Recall Area Under Curve)**, **F1-Score**, or **Balanced Accuracy** (Accuracy is misleading because predicting "no defect" achieves $>99\%$ accuracy while catching zero killer defects).

**PY158**. Write a Python script snippet using NumPy to calculate the $3\sigma$ Shewhart Upper and Lower Control Limits for a 1D time series `data`.  
*Solution*:  
```python
mu = np.mean(data)
sigma = np.std(data, ddof=1)
ucl = mu + 3 * sigma
lcl = mu - 3 * sigma
```

**PY159**. In a spatial wafer map, how can you cluster nearby defect points using Scikit-learn without pre-specifying the number of clusters?  
*Solution*:  
Using **`DBSCAN(eps=radius, min_samples=k)`** (Density-Based Spatial Clustering of Applications with Noise), which handles arbitrary spatial cluster shapes (scratches, rings) and flags isolated defects as noise.

**PY160**. In Perl scripting for EDA log processing, what does the following one-liner do?  
`perl -ne 'print if /FATAL_DEFECT/;' fab_log.txt`  
*Solution*:  
It reads `fab_log.txt` line-by-line (`-n`) and prints (`print`) only the lines containing the regex pattern `FATAL_DEFECT`.

---

## Part 5: Semiconductor Fundamentals & Inspection Physics (30 Questions)

### Microelectronics Fabrication & Unit Operations (Q161–Q175)

**SF161**. What is the primary difference between Front-End of Line (FEOL) and Back-End of Line (BEOL) in semiconductor fabrication?  
*Solution*:  
* **FEOL**: Fabrication of active semiconductor devices (transistors, gates, source/drain) directly on/in the silicon substrate.  
* **BEOL**: Fabrication of the multi-layer metal interconnect tracks (Copper dual-damascene) and inter-layer dielectrics (ILD) that wire the transistors together.

**SF162**. In photolithography, state the Rayleigh resolution criterion and explain how resolution is improved on modern scanners.  
*Solution*:  
$$CD = k_1 \frac{\lambda}{NA}$$  
Resolution ($CD$) is reduced (improved) by:  
1. Decreasing illumination wavelength $\lambda$ (from DUV $193\text{ nm}$ to EUV $13.5\text{ nm}$).  
2. Increasing lens numerical aperture $NA$ (e.g. Immersion $NA=1.35$, High-NA EUV $NA=0.55$).  
3. Decreasing process factor $k_1$ using optical proximity correction (OPC) and phase shift masks.

**SF163**. What is Depth of Focus ($DOF$) in lithography, and how does it scale with numerical aperture ($NA$)?  
*Solution*:  
$$DOF = k_2 \frac{\lambda}{NA^2}$$  
$DOF$ scales **inversely with the square of $NA$ ($NA^{-2}$)**. Increasing $NA$ drastically reduces the vertical focal tolerance, making surface planarity (via CMP) critical.

**SF164**. What is Preston's equation in Chemical Mechanical Planarization (CMP)?  
*Solution*:  
$$MRR = k_p \cdot P \cdot V$$  
Material Removal Rate ($MRR$) is proportional to applied downforce pressure $P$ and relative velocity $V$ between wafer and pad, with Preston coefficient $k_p$.

**SF165**. Explain the physical difference between isotropic and anisotropic etching.  
*Solution*:  
* **Isotropic Etch** (wet chemical etch): Etches equally in all spatial directions, producing lateral undercut beneath the mask.  
* **Anisotropic Etch** (reactive ion plasma etch - RIE): Energetic directional ion bombardment produces strictly vertical sidewalls with near-zero lateral undercut.

**SF166**. Why is Copper preferred over Aluminum for advanced BEOL interconnects?  
*Solution*:  
Copper exhibits significantly **lower electrical resistivity** ($\approx 1.68\text{ }\mu\Omega\cdot\text{cm}$ vs. $2.65\text{ }\mu\Omega\cdot\text{cm}$ for Al) and **superior resistance to electromigration** under high current densities.

**SF167**. Why is the Copper Dual-Damascene process used instead of direct plasma etching of Copper?  
*Solution*:  
Copper does not form volatile halogen compounds at moderate temperatures, making dry reactive ion etching (RIE) of Copper extremely difficult. Instead, trenches and vias are etched into the dielectric, filled with electroplated copper, and planarized by CMP (**Damascene**).

**SF168**. What is a Gate-All-Around (GAA) nanosheet transistor, and why does it supersede FinFET at advanced nodes ($\le 3\text{nm}$)?  
*Solution*:  
In GAA nanosheets, the gate electrode wraps around all four sides of horizontally stacked silicon nanosheet channels, providing **optimal electrostatic gate control, suppressing short-channel drain-induced barrier lowering (DIBL), and minimizing subthreshold leakage**.

**SF169**. What is 3D-NAND Flash memory, and what is the primary fabrication challenge as layer counts exceed 200 layers?  
*Solution*:  
3D-NAND stacks memory cell tiers vertically rather than scaling horizontally. The primary challenge is **High-Aspect-Ratio (HAR) etching** of memory hole channels ($AR > 60:1$) without channel twisting, tilting, or bottom profile tapering.

**SF170**. What is the purpose of Chemical Vapor Deposition (CVD) and Atomic Layer Deposition (ALD)?  
*Solution*:  
To deposit conformal, high-purity thin films (dielectrics, oxides, metals). ALD deposits films layer-by-atomic-layer using self-limiting chemical reactions, achieving **$100\%$ conformality in extreme aspect ratio trenches**.

**SF171**. What is an "excursion" in semiconductor manufacturing?  
*Solution*:  
A sudden, unexpected deviation of a process parameter or defect rate beyond statistical control limits, threatening lot yield and requiring immediate line containment.

**SF172**. What is the difference between a "killer defect" and a "nuisance defect"?  
*Solution*:  
* **Killer Defect**: A defect that causes electrical failure or functional loss of a die (bridging short, open contact, broken gate).  
* **Nuisance Defect**: A harmless physical or optical artifact (surface roughness, harmless grain boundary, optical haze) that does not impair circuit functionality.

**SF173**. What is a reticle (photomask), and what happens if a defect exists on a reticle?  
*Solution*:  
A reticle is the quartz master plate containing the chrome circuit pattern. If a defect exists on the reticle, it is **repeatedly printed onto every single die on every wafer** (**Repeater Defect**), causing catastrophic yield loss.

**SF174**. What is Chemical Mechanical Planarization (CMP) dishing and erosion?  
*Solution*:  
* **Dishing**: Faster polishing of soft copper in wide metal lines relative to adjacent hard dielectric, forming a concave dip.  
* **Erosion**: Localized thinning of dielectric oxide in dense metal array regions due to accelerated pad wear.

**SF175**. What is electromigration in semiconductor chips?  
*Solution*:  
The transport of material in a metal conductor due to the momentum transfer between conducting electrons and metal atoms, leading to voids (opens) or hillocks (shorts) over operating lifetime.

---

### Optical Inspection & Metrology Physics (Q176–Q190)

**SF176**. Why is Broadband Plasma Optical (BPO) illumination superior to monochromatic laser illumination for patterned wafer inspection?  
*Solution*:  
Laser illumination causes monochromatic standing-wave interference fringes in multi-layer dielectric stacks, producing optical blind spots where defect contrast collapses to zero. BPO provides a continuous spectrum from DUV to visible wavelengths; if one wavelength suffers destructive interference, others provide strong constructive contrast.

**SF177**. Explain why optical defect scattering intensity drops by $64\times$ when defect size shrinks from $28\text{ nm}$ to $14\text{ nm}$.  
*Solution*:  
In the Rayleigh scattering regime ($d \ll \lambda$), scattered intensity scales with the **sixth power of defect diameter ($I \propto d^6$)**:  
$$\frac{I(14\text{nm})}{I(28\text{nm})} = \left(\frac{14}{28}\right)^6 = \left(\frac{1}{2}\right)^6 = \frac{1}{64} \approx 0.0156$$

**SF178**. What is Brightfield (BF) inspection and what types of defects is it best suited to detect?  
*Solution*:  
Brightfield collects normal specular reflected light and low-order diffraction. It is best suited for **patterned wafer defects, micro-bridging, photoresist pattern collapse, and subtle film thickness variations**.

**SF179**. What is Darkfield (DF) inspection and what types of defects is it best suited to detect?  
*Solution*:  
Darkfield uses oblique grazing illumination and collects only scattered light, blocking the specular beam. Flat surfaces appear completely black. It is best suited for **isolated surface particles, pits, and micro-scratches on unpatterned or bare wafers (KLA Surfscan)**.

**SF180**. What is an Image-Based Overlay (IBO) target?  
*Solution*:  
Geometric concentric optical targets (such as "Box-in-Box" or "Frame-in-Frame") patterned on consecutive lithography layers where optical microscopy measures the centroid misalignment vector $(\Delta x, \Delta y)$.

**SF181**. What is Diffraction-Based Overlay (DBO)?  
*Solution*:  
Overlapping diffraction gratings printed on successive layers where the asymmetric intensity between positive and negative diffraction orders ($I_{+1} - I_{-1}$) is measured by scatterometry to determine sub-nanometer overlay error.

**SF182**. What is Optical Critical Dimension (OCD) metrology?  
*Solution*:  
Non-destructive optical metrology using polarized broadband reflectometry and spectroscopic ellipsometry to reconstruct the full 3D geometric cross-section (CD, sidewall angle, height) of periodic nano-structures.

**SF183**. In automated defect review, why are optical inspection candidates sent to an electron-beam review SEM (e.g. KLA eSL10)?  
*Solution*:  
Optical inspection scans full wafers at high speed but lacks the spatial resolution to resolve sub-10nm defect morphology. The high-resolution e-beam SEM automatically visits candidate coordinates from the KLARF file to capture nanoscale images for definitive defect classification.

**SF184**. What is Voltage Contrast (VC) defect inspection in an e-beam tool?  
*Solution*:  
A technique where electron beam bombardment charges the wafer surface. Electrically grounded contacts conduct charge away and emit secondary electrons (appearing bright), while electrically open/floating contacts accumulate charge and repel/attract secondaries differently (appearing dark), revealing buried open-circuit defects.

**SF185**. What is the trade-off between inspection sensitivity and tool throughput?  
*Solution*:  
Higher sensitivity requires smaller pixel sizes, slower stage scan speeds, and higher optical integration times, reducing throughput (wafers/hour). Lower sensitivity speeds up scanning but risks missing critical sub-20nm killer defects.

**SF186**. What is a KLARF file?  
*Solution*:  
**KLA Results File**: The global semiconductor industry standard ASCII/binary data format defining wafer inspection results, defect coordinates $(X, Y)$, die indices, defect sizes, roughness metrics, and cluster classifications.

**SF187**. What is Die-to-Die (D2D) inspection?  
*Solution*:  
An image processing algorithm that compares the optical image of a test die against an adjacent reference die on the same wafer ($|I_{\text{test}} - I_{\text{ref}}|$) to cancel repetitive circuit patterns and isolate anomalous defect signals.

**SF188**. What is Die-to-Statistical-Image (D2SI) inspection?  
*Solution*:  
An advanced inspection algorithm that synthesizes a noise-free reference image by averaging multiple adjacent dies across the wafer, reducing random background grain noise by $\sqrt{N}$ and enabling detection of subtle defects.

**SF189**. What is the function of Fourier optical filtering in patterned wafer inspection?  
*Solution*:  
Placing a spatial frequency spatial filter in the back focal plane of the collection optics to block the periodic diffraction spots generated by repetitive memory cell arrays (DRAM, SRAM), allowing only aperiodic scattered light from random defects to pass to the detector.

**SF190**. How does an Applications Engineer optimize an inspection recipe for New Product Introduction (NPI)?  
*Solution*:  
1. Select optimal optical illumination mode (wavelength band, aperture, polarization).  
2. Establish die alignment targets and Care Area masks.  
3. Tune threshold parameter $k$ in $T = \mu + k\sigma$ on defective test wafers to maximize capture rate of real killer defects ($\ge 95\%$) while keeping nuisance counts within manageable fab limits.  
4. Validate capture rate against e-beam SEM review and electrical test correlation.  
5. Author the official Best-Known-Method (BKM) documentation for fab deployment.

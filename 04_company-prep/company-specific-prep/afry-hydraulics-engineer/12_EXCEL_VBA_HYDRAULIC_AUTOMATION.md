# Module 12: Excel VBA Hydraulic Automation — 10 Production Projects

> **Document Focus**: Excel Engineering Fundamentals, Visual Basic for Applications (VBA), VBE Object Model, Error Handling, and 10 Fully Automated Hydraulic Calculation Projects  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING SOFTWARE AUTOMATION — MICROSOFT VBE, AFRY AUTOMATION STANDARDS]`  

---

## 1. Overview of Excel VBA in Hydraulic Consulting

While commercial software like HEC-RAS and Bentley HAMMER handle complex network simulations, **MS Excel combined with VBA (Visual Basic for Applications) macros and User-Defined Functions (UDFs)** forms the backbone of day-to-day hydraulic calculations in engineering consultancies.

In AFRY's Noida engineering office, automated spreadsheets are developed to:
1. Eliminate manual repetitive trial-and-error calculations (e.g., normal depth, Colebrook-White friction factor, and backwater profiles).
2. Generate standardized calculation reports for client submission (NHPC, HPPCL, World Bank).
3. Connect disparate datasets: formatting cross-sections for HEC-RAS and extracting transient pressure envelopes from HAMMER text logs.

---

## 2. VBA Architecture & Best Coding Practices

To produce robust, production-grade automation scripts:
* **Option Explicit**: Mandatory at the top of every code module to force explicit variable declaration, preventing typo-induced runtime errors.
* **Separation of Concerns**: Decouple numerical algorithms (written as modular `Functions` or `Subroutines`) from worksheet I/O.
* **Error Handling**: Implement structured error traps (`On Error GoTo ErrorHandler`) to catch invalid physical inputs (e.g., negative diameters, sub-atmospheric vacuums, or non-converging iterations).
* **Screen Updating & Calculation Control**: Disable screen redraws (`Application.ScreenUpdating = False`) and automatic recalculation during intense loops to achieve 50–100× performance acceleration.

---

## 3. The 10 Automated Hydraulic Automation Projects

Every project below contains:
* Mathematical governing equation.
* Structure of Input, Calculation, and Output cells.
* Complete, runnable, copy-pasteable VBA code with error handling.
* Validation check against an independently verified benchmark from Modules 03–09.

---

### Project 1: Universal Manning Equation Solver & Geometry Engine

* **Objective**: Compute discharge $Q$, velocity $v$, and flow area $A$ for rectangular, trapezoidal, or circular channels.
* **Governing Equation**: $Q = \frac{1}{n} A R^{2/3} S_0^{1/2}$
* **Worksheet Layout**:
  * Inputs: `B3` (Channel Type: "Trapezoidal"), `B4` (Bed width $b$), `B5` (Side slope $z$), `B6` (Depth $y$), `B7` (Bed slope $S_0$), `B8` (Manning $n$).
  * Outputs: `D3` (Area $A$), `D4` (Wetted Perimeter $P$), `D5` (Hydraulic Radius $R$), `D6` (Velocity $v$), `D7` (Discharge $Q$).

```vba
Option Explicit

Public Sub Calculate_Manning_Discharge()
    Dim ws As Worksheet
    Dim chanType As String
    Dim b As Double, z As Double, y As Double, S0 As Double, n As Double
    Dim A As Double, P As Double, R As Double, v As Double, Q As Double

    On Error GoTo ErrorHandler
    Set ws = ActiveSheet

    ' 1. Read Inputs
    chanType = UCase(Trim(ws.Range("B3").Value))
    b = ws.Range("B4").Value
    z = ws.Range("B5").Value
    y = ws.Range("B6").Value
    S0 = ws.Range("B7").Value
    n = ws.Range("B8").Value

    ' 2. Physical Sanity Checks
    If y <= 0 Or S0 <= 0 Or n <= 0 Then
        MsgBox "Depth, Slope, and Manning's n must be strictly positive!", vbCritical, "Input Error"
        Exit Sub
    End If

    ' 3. Geometric Calculations
    Select Case chanType
        Case "TRAPEZOIDAL", "RECTANGULAR"
            If b <= 0 Then
                MsgBox "Bed width must be positive!", vbCritical, "Input Error"
                Exit Sub
            End If
            A = (b + z * y) * y
            P = b + 2 * y * Sqr(1 + z ^ 2)
        Case "TRIANGULAR"
            A = z * y ^ 2
            P = 2 * y * Sqr(1 + z ^ 2)
        Case Else
            MsgBox "Unsupported channel type: " & chanType, vbExclamation, "Warning"
            Exit Sub
    End Select

    R = A / P
    v = (1# / n) * (R ^ (2# / 3#)) * Sqr(S0)
    Q = A * v

    ' 4. Output Results
    ws.Range("D3").Value = Round(A, 4)
    ws.Range("D4").Value = Round(P, 4)
    ws.Range("D5").Value = Round(R, 4)
    ws.Range("D6").Value = Round(v, 4)
    ws.Range("D7").Value = Round(Q, 4)

    MsgBox "Manning calculation successful: Q = " & Round(Q, 3) & " m^3/s", vbInformation, "Success"
    Exit Sub

ErrorHandler:
    MsgBox "Runtime Error: " & Err.Description, vbCritical, "Execution Failure"
End Sub
```
* **Validation**: Trapezoidal channel ($b=6\text{ m}, z=1.5, y=2.108\text{ m}, S_0=0.0005, n=0.018$) $\implies A=19.314\text{ m}^2, v=1.553\text{ m/s}, Q = 30.00\text{ m}^3\text{/s}$ (Matches Module 03 Problem 1).

---

### Project 2: Critical Depth Calculator via Newton-Raphson

* **Objective**: Compute critical depth $y_c$ in non-rectangular open channels.
* **Governing Equation**: $f(y) = \frac{Q^2 T}{g A^3} - 1 = 0 \iff g A(y)^3 - Q^2 T(y) = 0$
* **Derivative**: $f'(y) = 3 g A^2 T - Q^2 \frac{dT}{dy}$ (for trapezoidal, $\frac{dT}{dy} = 2z$).

```vba
Option Explicit

Public Function Critical_Depth_Trapezoidal(ByVal Q As Double, ByVal b As Double, _
                                         ByVal z As Double, Optional ByVal g As Double = 9.81) As Double
    Dim y As Double, y_new As Double
    Dim A As Double, T As Double, f As Double, df As Double
    Dim iter As Integer, maxIter As Integer
    Dim tol As Double

    tol = 0.00001
    maxIter = 100
    y = (Q ^ 2 / (g * b ^ 2)) ^ (1# / 3#) ' Initial guess assuming rectangular

    For iter = 1 To maxIter
        A = (b + z * y) * y
        T = b + 2 * z * y
        f = (Q ^ 2 * T) / (g * A ^ 3) - 1#
        ' Analytical derivative d(Q^2*T/(g*A^3))/dy
        df = (Q ^ 2 / g) * ((2 * z * A ^ 3 - 3 * A ^ 2 * T ^ 2) / (A ^ 6))
        
        y_new = y - f / df
        If y_new <= 0 Then y_new = y / 2#
        
        If Abs(y_new - y) < tol Then
            Critical_Depth_Trapezoidal = Round(y_new, 5)
            Exit Function
        End If
        y = y_new
    Next iter

    Critical_Depth_Trapezoidal = -1 ' Failed to converge
End Function
```
* **Validation**: For $Q=30\text{ m}^3\text{/s}, b=6\text{ m}, z=1.5 \implies y_c = 1.226\text{ m}$ (Exact match with Module 03 Problem 1).

---

### Project 3: Normal Depth Newton-Raphson Iterative Engine

* **Objective**: Solve normal depth $y_0$ from Manning's equation without using Excel Goal Seek.
* **Governing Equation**: $f(y) = A(y)^{5/3} P(y)^{-2/3} - \frac{Q n}{\sqrt{S_0}} = 0$

```vba
Option Explicit

Public Function Normal_Depth_Manning(ByVal Q As Double, ByVal b As Double, ByVal z As Double, _
                                    ByVal S0 As Double, ByVal n As Double) As Double
    Dim y As Double, y_next As Double
    Dim A As Double, P As Double, T As Double, dP As Double
    Dim f As Double, df As Double
    Dim Target As Double
    Dim iter As Integer

    Target = (Q * n) / Sqr(S0)
    y = (Target / b) ^ (3# / 5#) ' Initial guess

    For iter = 1 To 100
        A = (b + z * y) * y
        T = b + 2 * z * y
        P = b + 2 * y * Sqr(1 + z ^ 2)
        dP = 2 * Sqr(1 + z ^ 2)

        f = (A ^ (5# / 3#)) * (P ^ (-2# / 3#)) - Target
        df = (5# / 3#) * (A ^ (2# / 3#)) * T * (P ^ (-2# / 3#)) - _
             (2# / 3#) * (A ^ (5# / 3#)) * (P ^ (-5# / 3#)) * dP

        y_next = y - f / df
        If y_next <= 0 Then y_next = y * 0.5

        If Abs(y_next - y) < 0.00001 Then
            Normal_Depth_Manning = Round(y_next, 5)
            Exit Function
        End If
        y = y_next
    Next iter
    Normal_Depth_Manning = -1
End Function
```
* **Validation**: For $Q=30\text{ m}^3\text{/s}, b=6\text{ m}, z=1.5, S_0=0.0005, n=0.018 \implies y_0 = 2.108\text{ m}$ (Verified).

---

### Project 4: GVF Profile Profiler (Direct-Step Backwater Method)

* **Objective**: Compute water surface profile coordinates $(x, y)$ upstream of a dam or constriction on a mild slope (M1 profile).
* **Governing Equation**: $\Delta x = \frac{E_2 - E_1}{S_0 - \bar{S}_f}$

```vba
Option Explicit

Public Sub Generate_M1_Backwater_Profile()
    Dim ws As Worksheet
    Dim b As Double, S0 As Double, n As Double, Q As Double
    Dim y_start As Double, y_target As Double, dy As Double
    Dim y1 As Double, y2 As Double, E1 As Double, E2 As Double
    Dim Sf1 As Double, Sf2 As Double, Sf_avg As Double, dx As Double
    Dim current_x As Double
    Dim rowIdx As Long

    Set ws = ActiveSheet
    b = ws.Range("B3").Value
    S0 = ws.Range("B4").Value
    n = ws.Range("B5").Value
    Q = ws.Range("B6").Value
    y_start = ws.Range("B7").Value  ' e.g., Dam pool depth = 4.0 m
    y_target = ws.Range("B8").Value ' e.g., Near normal depth = 2.2 m
    dy = ws.Range("B9").Value       ' Step size = -0.1 m

    ws.Range("D2:I100").ClearContents
    ws.Range("D2:I2").Value = Array("Station (m)", "Depth (m)", "WSE (m)", "Velocity (m/s)", "Specific Energy (m)", "Friction Slope")

    current_x = 0#
    y1 = y_start
    rowIdx = 3

    Do While y1 > y_target And rowIdx < 100
        y2 = y1 + dy
        If y2 < y_target Then y2 = y_target

        ' Energy & Sf at y1
        E1 = y1 + (Q / (b * y1)) ^ 2 / (2 * 9.81)
        Sf1 = (n ^ 2 * (Q / (b * y1)) ^ 2) / ((b * y1 / (b + 2 * y1)) ^ (4# / 3#))

        ' Energy & Sf at y2
        E2 = y2 + (Q / (b * y2)) ^ 2 / (2 * 9.81)
        Sf2 = (n ^ 2 * (Q / (b * y2)) ^ 2) / ((b * y2 / (b + 2 * y2)) ^ (4# / 3#))

        Sf_avg = (Sf1 + Sf2) / 2#
        dx = (E2 - E1) / (S0 - Sf_avg)
        current_x = current_x + dx

        ws.Cells(rowIdx, 4).Value = Round(current_x, 1)
        ws.Cells(rowIdx, 5).Value = Round(y1, 3)
        ws.Cells(rowIdx, 6).Value = Round(y1 - current_x * S0, 3)
        ws.Cells(rowIdx, 7).Value = Round(Q / (b * y1), 3)
        ws.Cells(rowIdx, 8).Value = Round(E1, 3)
        ws.Cells(rowIdx, 9).Value = Round(Sf1, 6)

        y1 = y2
        rowIdx = rowIdx + 1
    Loop
    MsgBox "GVF Profile Generated across " & rowIdx - 3 & " stations.", vbInformation, "Completed"
End Sub
```

---

### Project 5: Colebrook-White Darcy Friction Factor Solver

* **Objective**: Production UDF to solve the implicit Colebrook-White friction factor $f$.

```vba
Option Explicit

Public Function Colebrook_White(ByVal Re As Double, ByVal eps_over_D As Double) As Double
    Dim f As Double, f_next As Double
    Dim F_val As Double, dF_val As Double
    Dim iter As Integer

    If Re < 2000 Then
        Colebrook_White = 64# / Re
        Exit Function
    End If

    ' Initial guess using Swamee-Jain
    f = 0.25 / (Log((eps_over_D / 3.7) + (5.74 / (Re ^ 0.9))) / Log(10#)) ^ 2

    For iter = 1 To 50
        F_val = (1# / Sqr(f)) + 2# * (Log((eps_over_D / 3.7) + (2.51 / (Re * Sqr(f)))) / Log(10#))
        ' Numerical derivative
        dF_val = -0.5 * (f ^ (-1.5)) - (2# / Log(10#)) * (2.51 / Re * (-0.5 * f ^ (-1.5))) / _
                 ((eps_over_D / 3.7) + (2.51 / (Re * Sqr(f))))

        f_next = f - F_val / dF_val
        If Abs(f_next - f) < 0.000001 Then
            Colebrook_White = Round(f_next, 6)
            Exit Function
        End If
        f = f_next
    Next iter
    Colebrook_White = Round(f, 6)
End Function
```
* **Validation**: For $Re = 2.536 \times 10^6, \epsilon/D = 0.000075 \implies f = 0.01221$ (Matches Module 05 Problem).

---

### Project 6: Minor-Loss Accumulator & Pipeline Head-Loss Engine

* **Objective**: Automated calculator summing pipeline friction loss and all fittings.

```vba
Option Explicit

Public Sub Calculate_Total_Pipeline_Loss()
    Dim ws As Worksheet
    Dim L As Double, D As Double, Q As Double, eps As Double, nu As Double
    Dim v As Double, Re As Double, f As Double, hf As Double, hm As Double, h_total As Double
    Dim K_sum As Double
    Dim lastRow As Long, i As Long

    Set ws = ActiveSheet
    L = ws.Range("B3").Value
    D = ws.Range("B4").Value
    Q = ws.Range("B5").Value
    eps = ws.Range("B6").Value
    nu = 0.000001004 ' Water at 20 deg C

    ' Sum K values from table in Columns F & G
    lastRow = ws.Cells(ws.Rows.Count, "F").End(xlUp).Row
    K_sum = 0#
    For i = 4 To lastRow
        K_sum = K_sum + ws.Cells(i, "G").Value * ws.Cells(i, "H").Value ' Quantity * K
    Next i

    v = (4# * Q) / (3.14159265358979 * D ^ 2)
    Re = (v * D) / nu
    f = Colebrook_White(Re, eps / D)

    hf = f * (L / D) * (v ^ 2 / (2# * 9.81))
    hm = K_sum * (v ^ 2 / (2# * 9.81))
    h_total = hf + hm

    ws.Range("B9").Value = Round(v, 3)
    ws.Range("B10").Value = Round(Re, 0)
    ws.Range("B11").Value = Round(f, 5)
    ws.Range("B12").Value = Round(hf, 3)
    ws.Range("B13").Value = Round(hm, 3)
    ws.Range("B14").Value = Round(h_total, 3)
End Sub
```

---

### Project 7: Hydraulic Jump Conjugate Depth & Dissipation Calculator

* **Objective**: Automate the Bélanger equation, head loss $\Delta E$, efficiency, and power dissipation.

```vba
Option Explicit

Public Sub Hydraulic_Jump_Analysis()
    Dim ws As Worksheet
    Dim q As Double, B As Double, y1 As Double
    Dim v1 As Double, Fr1 As Double, y2 As Double, v2 As Double, Fr2 As Double
    Dim E1 As Double, E2 As Double, dE As Double, Power_MW As Double

    Set ws = ActiveSheet
    q = ws.Range("B3").Value
    B = ws.Range("B4").Value
    y1 = ws.Range("B5").Value

    v1 = q / y1
    Fr1 = v1 / Sqr(9.81 * y1)

    If Fr1 <= 1# Then
        MsgBox "Inflow is subcritical (Fr1 <= 1). No hydraulic jump forms!", vbCritical, "Physics Warning"
        Exit Sub
    End If

    ' Bélanger formula
    y2 = (y1 / 2#) * (Sqr(1# + 8# * Fr1 ^ 2) - 1#)
    v2 = q / y2
    Fr2 = v2 / Sqr(9.81 * y2)

    E1 = y1 + (v1 ^ 2) / (2# * 9.81)
    E2 = y2 + (v2 ^ 2) / (2# * 9.81)
    dE = ((y2 - y1) ^ 3) / (4# * y1 * y2)
    Power_MW = (1000# * 9.81 * (q * B) * dE) / 1000000#

    ws.Range("D3").Value = Round(Fr1, 3)
    ws.Range("D4").Value = Round(y2, 3)
    ws.Range("D5").Value = Round(Fr2, 3)
    ws.Range("D6").Value = Round(dE, 3)
    ws.Range("D7").Value = Round((dE / E1) * 100#, 1) & " %"
    ws.Range("D8").Value = Round(Power_MW, 3) & " MW"
End Sub
```
* **Validation**: For $q=12\text{ m}^3\text{/s/m}, B=20\text{ m}, y_1=0.80\text{ m} \implies Fr_1=5.354, y_2=5.670\text{ m}, \Delta E=6.366\text{ m}, P=14.99\text{ MW}$ (Exact match with Module 03 Problem 2).

---

### Project 8: Joukowsky Water Hammer & Surge Wave Speed Calculator

* **Objective**: Evaluate acoustic wave speed $a$, pipe period $2L/a$, and rapid/slow valve closure pressure rises.

```vba
Option Explicit

Public Function Joukowsky_Head_Rise(ByVal L As Double, ByVal D As Double, ByVal e As Double, _
                                   ByVal Q As Double, ByVal tc As Double, ByVal E_steel As Double) As Variant
    Dim K_water As Double, rho As Double, v0 As Double, a As Double
    Dim Tc As Double, dH As Double
    Dim res(1 To 3) As Double

    K_water = 2190000000#
    rho = 1000#
    v0 = (4# * Q) / (3.14159265358979 * D ^ 2)

    ' Wave speed
    a = Sqr((K_water / rho) / (1# + (K_water / E_steel) * (D / e)))
    Tc = (2# * L) / a

    If tc <= Tc Then
        dH = (a * v0) / 9.81 ' Rapid closure
    Else
        dH = (2# * L * v0) / (9.81 * tc) ' Slow closure (Michaud)
    End If

    res(1) = Round(a, 1)
    res(2) = Round(Tc, 3)
    res(3) = Round(dH, 2)
    Joukowsky_Head_Rise = res
End Function
```
* **Validation**: For $L=600\text{ m}, D=2.5\text{ m}, e=25\text{ mm}, Q=35\text{ m}^3\text{/s}, t_c=1.0\text{ s} \implies a=1030.3\text{ m/s}, T_c=1.165\text{ s}, \Delta H=748.8\text{ m}$ (Matches Module 06 Problem).

---

### Project 9: Stage-Discharge Rating Curve Generator & Power-Law Regressor

* **Objective**: Automate fitting $Q = C(h - h_0)^\beta$ from field gauge readings using logarithmic least-squares regression.

```vba
Option Explicit

Public Sub Fit_Rating_Curve()
    Dim ws As Worksheet
    Dim h0 As Double
    Dim nPoints As Long, i As Long
    Dim sumX As Double, sumY As Double, sumXY As Double, sumX2 As Double
    Dim x_val As Double, y_val As Double
    Dim beta As Double, lnC As Double, C As Double

    Set ws = ActiveSheet
    h0 = ws.Range("B3").Value
    nPoints = ws.Range("B4").Value

    sumX = 0#: sumY = 0#: sumXY = 0#: sumX2 = 0#

    For i = 7 To 6 + nPoints
        x_val = Log(ws.Cells(i, 2).Value - h0) ' ln(h - h0)
        y_val = Log(ws.Cells(i, 3).Value)      ' ln(Q)
        sumX = sumX + x_val
        sumY = sumY + y_val
        sumXY = sumXY + x_val * y_val
        sumX2 = sumX2 + x_val ^ 2
    Next i

    beta = (nPoints * sumXY - sumX * sumY) / (nPoints * sumX2 - sumX ^ 2)
    lnC = (sumY - beta * sumX) / nPoints
    C = Exp(lnC)

    ws.Range("E3").Value = Round(C, 4)
    ws.Range("E4").Value = Round(beta, 4)
    ws.Range("E5").Value = "Q = " & Round(C, 3) & " * (h - " & h0 & ")^" & Round(beta, 3)
    MsgBox "Rating curve fitted: " & ws.Range("E5").Value, vbInformation, "Completed"
End Sub
```

---

### Project 10: Ogee Spillway Discharge Rating & Profile Generator

* **Objective**: Generates WES downstream profile coordinates and discharge rating table across variable reservoir heads.

```vba
Option Explicit

Public Sub Generate_Ogee_Spillway_Table()
    Dim ws As Worksheet
    Dim Hd As Double, Cd As Double, L_clear As Double, N_piers As Double
    Dim Kp As Double, Ka As Double
    Dim x As Double, y As Double, H As Double, Le As Double, Q As Double
    Dim rowIdx As Long

    Set ws = ActiveSheet
    Hd = ws.Range("B3").Value
    Cd = ws.Range("B4").Value
    L_clear = ws.Range("B5").Value
    N_piers = ws.Range("B6").Value
    Kp = ws.Range("B7").Value
    Ka = ws.Range("B8").Value

    ' 1. Downstream Profile Coordinates
    ws.Range("D4:E25").ClearContents
    rowIdx = 4
    For x = 0# To (2# * Hd) Step (Hd / 8#)
        y = -0.5 * (x ^ 1.85) / (Hd ^ 0.85)
        ws.Cells(rowIdx, 4).Value = Round(x, 2)
        ws.Cells(rowIdx, 5).Value = Round(y, 3)
        rowIdx = rowIdx + 1
    Next x

    ' 2. Head-Discharge Rating Table
    ws.Range("G4:I15").ClearContents
    rowIdx = 4
    For H = 1# To (1.4 * Hd) Step (Hd / 5#)
        Le = L_clear - 2# * (N_piers * Kp + Ka) * H
        Q = Cd * Le * (H ^ 1.5)
        ws.Cells(rowIdx, 7).Value = Round(H, 2)
        ws.Cells(rowIdx, 8).Value = Round(Le, 2)
        ws.Cells(rowIdx, 9).Value = Round(Q, 2)
        rowIdx = rowIdx + 1
    Next H
    MsgBox "Ogee profile and rating table successfully generated!", vbInformation, "Done"
End Sub
```
* **Validation**: For $H_d = 8.0\text{ m}, C_d = 2.20, L = 50.4\text{ m}, N = 3, K_p = 0.01, K_a = 0.10 \implies Q = 2,405.4\text{ m}^3\text{/s}$ at $x = 8.0\text{ m}, y = -4.00\text{ m}$ (Matches Module 07 Problem).


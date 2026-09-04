# 🤖 Automation & CAD → BIM → Digital Engineering

> **Covers Civil-specific automation (Python, MATLAB, Bash) and the CAD → BIM → Digital Engineering progression.**

---

## Part 1: CAD → BIM → Digital Engineering Progression

```
CAD → Civil 3D → BIM → Coordination → Digital Project Delivery → Automation
```

### The Progression

| Stage | Tool | What You Do |
|:------|:-----|:------------|
| **CAD** | AutoCAD | 2D drafting, technical drawings |
| **Civil 3D** | Civil 3D | 3D infrastructure design, corridors, profiles |
| **BIM** | Revit | 3D model with data, coordination |
| **Coordination** | Navisworks | Clash detection, model federation |
| **Digital Delivery** | BIM 360 / ACC | Cloud collaboration, document control |
| **Automation** | Dynamo, Python | Scripted workflows, parametric design |

### Tool Differences

| Tool | Type | Best For | Not For |
|:-----|:-----|:---------|:--------|
| **AutoCAD** | 2D CAD | Drafting, details, legacy files | 3D modeling, data-rich models |
| **Civil 3D** | 3D CAD (infrastructure) | Roads, grading, corridors, pipe networks | Buildings, architectural |
| **Revit** | BIM | Buildings, structural, MEP, coordination | Infrastructure (limited) |
| **Navisworks** | Coordination | Clash detection, 4D, review | Authoring |
| **GIS** | Spatial | Mapping, spatial analysis, geodata | Detailed design |
| **BIM** | Process | Data-rich collaborative modeling | Simple 2D drafting |

### When to Use Each

```
Use AutoCAD:    For 2D drawings, details, sections, legacy projects
Use Civil 3D:   For road/highway/infrastructure design
Use Revit:      For building structural/architectural BIM
Use Navisworks: For coordination, clash detection, 4D scheduling
Use GIS:        For spatial analysis, mapping, geodata
```

---

## Part 2: Automation for Civil Engineering

### Why Automate?

```
Manual repetitive tasks:
    - Reading 500+ simulation output files
    - Generating 100+ plots
    - Computing engineering parameters from raw data
    - Formatting reports
    - Post-processing CFD results

Automation benefits:
    - Saves hours per task
    - Reduces human error
    - Enables reproducibility
    - Demonstrates technical skill to employers
```

---

## Python Automation Examples

### 1. Read Experimental Data

```python
import pandas as pd

# Read multiple CSV files
import glob
files = glob.glob("data/*.csv")
dfs = [pd.read_csv(f) for f in files]
data = pd.concat(dfs, ignore_index=True)
print(data.head())
```

### 2. Process Files

```python
import os
import pandas as pd

# Process all files in a directory
for filename in os.listdir("raw_data/"):
    if filename.endswith(".csv"):
        df = pd.read_csv(f"raw_data/{filename}")
        # Clean and process
        df = df.dropna()
        df["flow"] = df["velocity"] * df["area"]
        # Save processed
        df.to_csv(f"processed/{filename}", index=False)
```

### 3. Generate Plots

```python
import matplotlib.pyplot as plt
import pandas as pd

# Generate plots for all stations
for station in stations:
    df = pd.read_csv(f"data/{station}.csv")
    plt.figure()
    plt.plot(df["time"], df["water_level"])
    plt.title(f"Water Level - Station {station}")
    plt.xlabel("Time")
    plt.ylabel("Water Level (m)")
    plt.savefig(f"plots/{station}_level.png", dpi=300)
    plt.close()
```

### 4. Calculate Engineering Parameters

```python
import numpy as np

def mannings_velocity(n, R, S):
    """Manning's equation: V = (1/n) * R^(2/3) * S^(1/2)"""
    return (1/n) * R**(2/3) * S**(1/2)

# Batch calculate for multiple sections
sections = [
    {"n": 0.013, "R": 1.5, "S": 0.001},
    {"n": 0.015, "R": 2.0, "S": 0.0008},
    {"n": 0.012, "R": 1.2, "S": 0.0012},
]
for s in sections:
    v = mannings_velocity(s["n"], s["R"], s["S"])
    print(f"Section: V = {v:.2f} m/s")
```

### 5. Automate Repetitive Calculations

```python
import pandas as pd

# Compute statistics for all columns
df = pd.read_csv("monitoring_data.csv")
summary = df.describe()
summary.to_csv("summary_statistics.csv")
```

### 6. Generate Reports

```python
from docx import Document

doc = Document()
doc.add_heading("Hydraulic Analysis Report", 0)
doc.add_paragraph(f"Total sections analyzed: {len(sections)}")
doc.add_paragraph(f"Average velocity: {avg_velocity:.2f} m/s")
doc.save("report.docx")
```

### 7. Post-Process Simulation Output

```python
import numpy as np
import pandas as pd

# Read OpenFOAM output
# Extract profiles, compute statistics
data = np.loadtxt("postProcessing/probes/0/U")
velocity = data[:, 1]  # Ux component
mean_velocity = np.mean(velocity)
rms_velocity = np.std(velocity)
print(f"Mean: {mean_velocity:.3f}, RMS: {rms_velocity:.3f}")
```

---

## MATLAB Automation Examples

### Parameter Sweep

```matlab
% Sweep over multiple parameter values
n_values = [0.010, 0.013, 0.015, 0.018];
results = zeros(length(n_values), 1);

for i = 1:length(n_values)
    n = n_values(i);
    % Run calculation
    results(i) = compute_velocity(n, R, S);
end

% Plot results
plot(n_values, results)
xlabel('Manning n')
ylabel('Velocity (m/s)')
```

### Optimization

```matlab
% Optimize design parameter
objective = @(x) -compute_profit(x);  % minimize negative = maximize
x0 = [10, 20];
options = optimoptions('fmincon', 'Display', 'iter');
[x_opt, fval] = fmincon(objective, x0, [], [], [], [], lb, ub, [], options);
```

---

## Bash Automation Examples

### Batch Simulation

```bash
#!/bin/bash
# Run multiple OpenFOAM cases
for case in case1 case2 case3; do
    cd $case
    blockMesh
    simpleFoam
    cd ..
done
```

### File Processing

```bash
#!/bin/bash
# Process all CSV files
for file in data/*.csv; do
    echo "Processing $file"
    # Extract second column, compute sum
    awk -F',' '{sum += $2} END {print "Sum:", sum}' $file
done
```

### HPC Workflow

```bash
#!/bin/bash
#SBATCH --job-name=param_sweep
#SBATCH --array=1-10
#SBATCH --ntasks=16

# Parameter sweep using job array
params=(0.01 0.013 0.015 0.018 0.02 0.022 0.025 0.028 0.03 0.033)
n=${params[$SLURM_ARRAY_TASK_ID]}
echo "Running with n=$n"
# Run simulation with parameter n
```

---

## Automation Interview Questions

### Basic (101)
- Why is automation important in engineering?
- What are the benefits of scripting repetitive tasks?

### Practical (201)
- How do you process 100+ CSV files in Python?
- How do you generate plots for multiple datasets?
- How do you automate a parameter sweep?

### Technical (301)
- How do you ensure your automation is reproducible?
- How do you handle errors in batch processing?
- What's the difference between Python and Bash for automation?

### Project Defense
- Show me an automation script you wrote.
- How did you validate the automated results?
- How much time did automation save?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Python | [`programming/python.md`](../programming/python.md) |
| MATLAB | [`programming/matlab.md`](../programming/matlab.md) |
| Linux/Dev Tools | [`developer-tools/`](../developer-tools/linux-dev-tools.md) |
| BIM Technology | [`bim/`](../bim/bim-tech.md) |
| Structural (CAD) | [`structural/`](../structural/structural-tech.md) |

---

*See also: [`bim-tech.md`](../bim/bim-tech.md) for BIM workflows, [`python.md`](../programming/python.md) for Python automation.*

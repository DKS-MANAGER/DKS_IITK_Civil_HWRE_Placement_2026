# ☁️ Cloud / HPC / Compute

> **Target:** CFD, Research, HPC, and technical roles
> **Covers CPU/GPU, parallel computing, HPC clusters, SSH, job schedulers, SLURM, cloud basics, and reproducibility.**
> **Do NOT turn this into a generic cloud-certification guide. Only learn what a Civil engineer actually needs.**

---

## When Does a Civil Engineer Need This?

```
Learn HPC/Cloud IF:
    ✓ You're running CFD simulations (OpenFOAM, ANSYS)
    ✓ Your research requires large-scale computation
    ✓ You're processing large datasets (GIS, sensor data)
    ✓ You need to run simulations on university clusters
    ✓ You're targeting HPC/simulation roles

Skip HPC/Cloud IF:
    ✗ You're targeting BA/DA/PM/consulting roles
    ✗ Your work fits on a laptop
    ✗ You have limited time before placement
```

---

## CPU / GPU Basics

### CPU (Central Processing Unit)

```
- Few cores (4-64), each fast and general-purpose
- Best for: sequential tasks, complex logic, most CFD
- OpenFOAM: CPU-based (MPI parallel)
```

### GPU (Graphics Processing Unit)

```
- Many cores (thousands), each slower
- Best for: massively parallel tasks (matrix ops, ML)
- CFD: limited use (some solvers support GPU)
- Not essential for most Civil CFD
```

### Key Concepts

```
Core:     A single processing unit
Thread:   A sequence of instructions
Process:  A running program
MPI:      Message Passing Interface (distributed memory)
OpenMP:   Shared memory parallelism
```

---

## Parallel Computing

### Why Parallelize?

```
A simulation that takes 100 hours on 1 core
    → 16 cores: ~6-7 hours (with 90% efficiency)
    → 64 cores: ~2 hours (with 70% efficiency)

Not perfectly linear — communication overhead grows with cores.
```

### MPI (Distributed Memory)

```
- Each process has its own memory
- Processes communicate via messages
- Used by OpenFOAM, most CFD codes
- Command: mpirun -np 16 solver -parallel
```

### OpenMP (Shared Memory)

```
- Threads share memory
- Easier to implement
- Used for loop-level parallelism
- Limited to one node
```

---

## HPC Clusters

### What is an HPC Cluster?

```
A collection of computers (nodes) connected by a fast network,
managed by a job scheduler, used for large-scale computation.

Login Node:    Where you connect (ssh)
Compute Nodes: Where jobs run
Storage:       /home (small, backed up), /scratch (large, fast, temporary)
```

### Typical HPC Workflow

```
1. Connect:  ssh user@cluster
2. Load:     module load openfoam
3. Prepare:  Set up case in /scratch
4. Submit:   sbatch job_script.sh
5. Monitor:  squeue -u user
6. Retrieve: Copy results from /scratch to /home
```

---

## SLURM Job Scheduler

### Submit a Job

```bash
#!/bin/bash
#SBATCH --job-name=cfd_sim
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1
#SBATCH --time=04:00:00
#SBATCH --partition=compute
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

module load openfoam
cd $SLURM_SUBMIT_DIR
mpirun -np 16 simpleFoam -parallel
```

### SLURM Commands

```
sbatch script.sh        # Submit job
squeue -u user          # Check job status
scancel <jobid>         # Cancel job
sinfo                   # View partitions/nodes
sacct                   # View job accounting
srun <command>          # Run interactively
```

---

## Cloud Computing Basics

### What is Cloud?

```
Computing resources (servers, storage, databases) provided over the internet.

IaaS:  Infrastructure (VMs, storage) — AWS EC2, Azure VMs
PaaS:  Platform (managed services) — AWS Lambda, Heroku
SaaS:  Software (applications) — Gmail, Office 365
```

### When Civil Engineers Use Cloud

```
- Running simulations on cloud VMs (when no local cluster)
- Storing and sharing large datasets
- Hosting dashboards (Power BI Service)
- GIS data processing (Google Earth Engine is cloud)
- Reproducible research environments (Docker)
```

### Cloud Providers

```
AWS (Amazon):   Most popular, EC2, S3, Lambda
Azure (MS):     Good for Microsoft ecosystem
GCP (Google):   Google Earth Engine, BigQuery
```

---

## Storage & Reproducibility

### Storage Types

```
Local:    Fast, limited, on your machine
/scratch: Fast, temporary, on HPC
/home:    Slower, backed up, on HPC
Cloud:    Scalable, accessible anywhere
```

### Reproducible Research

```
1. Version control (Git) for code
2. Document environment (requirements.txt, conda.yml)
3. Store raw data separately
4. Use containers (Docker) for exact environments
5. Document parameters and versions
```

---

## Interview Questions

### Basic (101)
- What is the difference between CPU and GPU?
- What is MPI? How is it different from OpenMP?
- What is a job scheduler?

### Practical (201)
- How do you submit a job to an HPC cluster?
- How do you monitor a running job?
- What is the difference between /home and /scratch?

### Technical (301)
- Explain the difference between distributed and shared memory parallelism.
- How do you scale a CFD simulation across multiple nodes?
- What is Amdahl's law? How does it limit parallel speedup?

### Project Defense
- How did you parallelize your simulation?
- What was your scaling efficiency?
- How did you manage large datasets?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Linux/Dev Tools | [`developer-tools/`](../developer-tools/linux-dev-tools.md) |
| CFD Technology | [`cfd/`](../cfd/cfd-tech.md) |
| Research Technology | [`research/`](../research/research-tech.md) |

---

*See also: [`linux-dev-tools.md`](../developer-tools/linux-dev-tools.md) for command-line skills.*

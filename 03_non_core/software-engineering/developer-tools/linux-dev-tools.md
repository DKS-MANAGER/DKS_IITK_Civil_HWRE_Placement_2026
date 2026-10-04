# 🐧 Linux / Terminal / Developer Tools

> **Target:** Technical students (CFD, Research, HPC, Programming, Data, OpenFOAM)
> **Essential command-line skills for engineering computation.**

---

## Why Linux for Civil Engineers?

| Role | Why Linux Matters |
|:-----|:------------------|
| CFD | OpenFOAM runs on Linux |
| Research | HPC clusters run Linux |
| HPC | Job schedulers (SLURM) are Linux tools |
| Programming | Most engineering tools are Linux-first |
| Data | Data processing pipelines use shell tools |
| OpenFOAM | Solver compilation requires Linux |

---

## Linux Filesystem

```
/               Root directory
/home/user/     User home directory
/tmp/           Temporary files
/var/           Variable data (logs)
/etc/           Configuration files
/usr/           User programs
/bin/, /sbin/   System binaries
/scratch/       HPC scratch space (fast, temporary)
```

### Essential Commands

```
pwd             Print working directory
ls              List files
cd              Change directory
mkdir           Create directory
cp              Copy files
mv              Move/rename files
rm              Remove files
cat             View file contents
less            View file with scrolling
head, tail      View beginning/end of file
touch           Create empty file
find            Search for files
```

---

## Shell Basics

### Pipes and Redirection

```
command1 | command2        # Pipe output of command1 to command2
command > file             # Redirect output to file (overwrite)
command >> file            # Redirect output to file (append)
command < file             # Read input from file
command 2> error.log       # Redirect errors to file
```

### grep — Search Text

```
grep "pattern" file.txt            # Find lines matching pattern
grep -i "pattern" file.txt         # Case-insensitive
grep -r "pattern" directory/       # Recursive search
grep -n "pattern" file.txt         # Show line numbers
grep -c "pattern" file.txt         # Count matches
```

### sed — Stream Editor

```
sed 's/old/new/g' file.txt         # Replace all occurrences
sed -n '5,10p' file.txt            # Print lines 5-10
sed '/pattern/d' file.txt          # Delete lines matching pattern
```

### awk — Text Processing

```
awk '{print $1}' file.txt          # Print first column
awk '{sum += $2} END {print sum}'  # Sum column 2
awk -F',' '{print $1}' data.csv    # Split by comma
```

---

## Permissions

```
chmod 755 file        # rwxr-xr-x (owner rwx, group rx, others rx)
chmod 644 file        # rw-r--r-- (owner rw, group r, others r)
chmod +x script.sh    # Make executable
chown user:group file # Change owner

Permissions:
    r = read (4)
    w = write (2)
    x = execute (1)
```

---

## Environment Variables

```
export PATH=$PATH:/new/path    # Add to PATH
echo $HOME                     # Print variable
env                            # List all environment variables
source ~/.bashrc               # Reload shell config
```

### Common Variables

```
HOME        # Home directory
PATH        # Executable search path
LD_LIBRARY_PATH  # Shared library path
OMP_NUM_THREADS  # OpenMP threads
```

---

## Package Managers

```
apt (Debian/Ubuntu):
    sudo apt update
    sudo apt install <package>

yum/dnf (RHEL/Fedora):
    sudo yum install <package>

conda (Python):
    conda create -n env python=3.11
    conda activate env
    conda install numpy pandas

pip (Python):
    pip install numpy pandas matplotlib
```

---

## SSH — Remote Access

```
ssh user@hostname              # Connect to remote server
ssh -X user@hostname           # X11 forwarding (GUI)
scp file user@host:path/       # Copy file to remote
scp user@host:path/file .      # Copy file from remote
rsync -av source/ dest/        # Sync directories
```

### SSH Keys

```
ssh-keygen -t rsa -b 4096      # Generate key pair
ssh-copy-id user@host          # Copy public key to server
# Now you can SSH without password
```

---

## Git on the Command Line

```
git init                       # Initialize repository
git add .                      # Stage all changes
git commit -m "message"        # Commit
git push origin main           # Push to remote
git pull                       # Pull from remote
git status                     # Check status
git log                        # View history
git branch                     # List branches
git checkout -b feature        # Create + switch branch
```

---

## Bash Scripting Basics

```bash
#!/bin/bash
# This is a comment

# Variables
name="World"
echo "Hello, $name"

# Conditionals
if [ -f "file.txt" ]; then
    echo "File exists"
else
    echo "File not found"
fi

# Loops
for i in {1..5}; do
    echo "Iteration $i"
done

# Functions
greet() {
    echo "Hello, $1"
}
greet "User"
```

---

## Batch Processing for HPC

```bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=02:00:00
#SBATCH --partition=compute

module load openfoam
cd /scratch/user/case
mpirun -np 16 simpleFoam -parallel
```

---

## Interview Questions

### Basic (101)
- What is the difference between `>` and `>>`?
- How do you find a file by name?
- What does `chmod 755` mean?

### Practical (201)
- How do you extract the second column of a CSV file?
- How do you count the number of lines in a file?
- How do you connect to a remote server?

### Technical (301)
- Explain the difference between `grep`, `sed`, and `awk`.
- How do you set up SSH key authentication?
- What is a pipe? Give an example.

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Cloud/HPC | [`computing/`](../computing/cloud-hpc.md) |
| CFD Technology | [`cfd/`](../cfd/cfd-tech.md) |
| Research Technology | [`research/`](../research/research-tech.md) |
| Git | [`programming/git.md`](../programming/git.md) |

---

*See also: [`cloud-hpc.md`](../computing/cloud-hpc.md) for HPC and cloud computing.*

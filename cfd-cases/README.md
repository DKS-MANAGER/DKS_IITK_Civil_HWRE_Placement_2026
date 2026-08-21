# CFD Cases

This directory contains OpenFOAM case files, meshes, and post-processing scripts used for HWRE placement preparation.

## Contents

- `cases/` — individual OpenFOAM simulation cases
- `scripts/` — Python/Bash utility scripts for preprocessing and postprocessing
- `post/` — Paraview state files and extracted data

## Usage

1. Open any case folder with ` foamSystem`.
2. Run `blockMesh`, `snappyHexMesh`, then the selected solver.
3. Post-process with `postProcess` or Paraview.

## Notes

- Do not commit large `processor*` directories or raw VTK output.
- Keep cases minimal and documented with a one-line README in each subfolder.

# Instruction

This repository contains code to reproduce the figures from the paper:

**"The Dependence of Moist Vortex Intensification on Convection-Induced Moisture Distribution and Low-level Inflow: Insights for Tropical Cyclone Seed Genesis"**

The project includes:
- Python scripts (`*.py`)
- GrADS scripts (`*.gs`)
- NCAR VAPOR scripts (`.vs3`)

Some scripts rely on external functions from the repository [gscript](https://github.com/kodamail/gscript).

---

## Data

All required data and scripts are available on [Zenodo](https://doi.org/10.5281/zenodo.17023680).
After downloading, unzip the archive `data.tar.gz` and rename (or place) it as the `data/` folder in the project directory:


---

## Setup

1. After downloading, unzip the archive `data.tar.gz` and rename (or place) it as the `./data` folder in the project directory.
    ```bash
    tar -xvzf data.tar.gz
    mv data <project_root>/data
    ```
2. Set the environment variable `GASCRP` to your local `gscript` path.
3. Install [OpenGrADS](http://opengrads.org) and [NCAR VAPOR](https://www.vapor.ucar.edu).
4. Create the Python environment using [Miniconda](https://docs.conda.io/en/latest/miniconda.html):  
   ```bash
   conda env create --name=py311 -f environment.yml
   # or 
   conda create --name py311 --file explicit_env.txt
   ```

--- 

## Usage
   In each figure directory, execute the provided bash script:
   ```
   # fig 01~10
   ./run.sh
   # or
   ./run_draw.sh

   # fig 11
   open session (`.vs3`) in VAPOR
   ```
---

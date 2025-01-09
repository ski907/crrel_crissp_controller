# CRREL CRISSP2D Controller

## Overview

This project automates running the CRISSP2D model.

**Important**:  
You **must manually place** `CSP2D_Mainprog.exe` and `CSP2D_Mainprog.123` into the `./simulations/` directory.  
(The executable may produce incomplete filenames if the path is too long, so keeping it at that level is required.)

## Paraview Setup

- Update `paraview_path` in `./src/paraview_config.yaml` to **your** local Paraview executable path.
- `paraview_pvpython_path` isn’t currently used (headless mode), but you can update it if needed.

## Python Environment

This code has been tested with **Python 3.12.4**. A `requirements.txt` file is located in `./src/`.  
To create a conda environment and install the necessary packages, run:

```bash
cd ./src/
conda create --name ccc python=3.12.4
conda activate ccc
conda install pip
pip install -r requirements.txt

After installing dependencies, run:

python ccc.py
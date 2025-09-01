#!/usr/bin/bash

source ~/.bashrc
conda activate py311

python quentify_lowevel_wind.py
python scatter_inflow.py

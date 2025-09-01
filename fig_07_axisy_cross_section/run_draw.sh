#!/usr/bin/bash

source ~/.bashrc
conda activate py311

py='draw_radi_wind_one_daily.py'
py='draw_tang_wind_one_daily.py'
py='draw_mse_ccc_daily.py'

for i in 0 1 2 8 18;do
  echo ${i}
  python -u ${py} ${i}
done

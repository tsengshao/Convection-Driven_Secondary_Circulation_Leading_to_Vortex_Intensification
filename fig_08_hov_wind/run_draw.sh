#!/usr/bin/bash

source ~/.bashrc
conda activate py311

pylist='draw_hov_inflow_f00.py draw_hov_inflow.py draw_hov_tang.py'
pylist='draw_hov_tang.py'

for py in ${pylist};do
   for i in 0 1 2 8 18;do
     echo ${i}
     python -u ${py} ${i}
   done
done

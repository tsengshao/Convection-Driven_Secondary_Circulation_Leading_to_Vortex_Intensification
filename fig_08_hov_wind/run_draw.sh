#!/usr/bin/bash

source ~/.bashrc
conda activate py311

pylist='draw_hov_inflow.py draw_hov_tang.py draw_hov_inflow_f00.py'
for py in ${pylist};do
   for i in 1 2 8 13 18;do
     echo ${i}
     python -u ${py} ${i}
   done
done

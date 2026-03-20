#!/usr/bin/bash
#SBATCH -J draw     # Job name
#SBATCH -p all     # job partition
#SBATCH -N 1       # Run all processes on a single node 
#SBATCH -c 1        # cores per MPI rank
#SBATCH -n 4      # Run a single task
#SBATCH -w mogamd  # nodelist
#SBATCH -o draw.%j.out  # output file

source ~/.bashrc
mode="SAVEFIG"
#gs="draw_zeta.gs"
#gs="draw_conzeta.gs"
gslist="draw_zeta.gs draw_conzeta.gs"

for gs in ${gslist};do
  for iexp in 2 3 9 14 19;do
    echo ${iexp}
#    grads -blcx "run ${gs} ${iexp} -mode ${mode} -ts 1 -te 1"
    grads -blcx "run ${gs} ${iexp} -mode ${mode} -ts 217 -te 217"
  done

  for ts in 1 721 1441 1801 2161;do
    iexp=1
    grads -blcx "run ${gs} ${iexp} -mode ${mode} -ts ${ts} -te ${ts}"
  done
done


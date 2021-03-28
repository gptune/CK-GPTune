#!/bin/bash

module load python/3.7-anaconda-2019.10
module unload cray-mpich
module swap PrgEnv-intel PrgEnv-gnu
module load openmpi/4.0.1
export MKLROOT=/opt/intel/compilers_and_libraries_2019.3.199/linux/mkl
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/intel/compilers_and_libraries_2019.3.199/linux/mkl/lib/intel64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/examples/SuperLU_DIST/superlu_dist/parmetis-4.0.3/install/lib/
export PYTHONPATH=~/.local/cori/3.7-anaconda-2019.10/lib/python3.7/site-packages

sh patch.sh

alias ck="~/.local/cori/3.7-anaconda-2019.10/bin/ck"
ck detect soft:lib.gptune


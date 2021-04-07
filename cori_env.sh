#!/bin/bash

module load python/3.7-anaconda-2019.10
module unload cray-mpich
module swap PrgEnv-intel PrgEnv-gnu
module load openmpi/4.0.1


#!/bin/bash

export PYTHONPATH=$PYTHONPATH:./scalapack-driver/spt/
mpirun -n 1 python ../gptune_driver.py

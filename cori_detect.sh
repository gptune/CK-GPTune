#!/bin/bash

module load openmpi/4.0.1

ck detect soft:lib.gptune
ck detect soft:lib.python.autotune
ck detect soft:lib.python.mpi4py
ck detect soft:lib.python.scikit-optimize
ck detect soft:lib.python.scalapack.gptune

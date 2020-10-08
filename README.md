# CK for GPTune

This repository contains artifacts and workflows to use GPTune
(https://github.com/gptune/GPTune) based on the CK technology.

## Pre-requisites

- Linux
- Python 3+
- Collective Knowledge Framework (CK) - https://ctuning.org
- Other dependencies can be installed by CK-GPTune workflows

## Installation

Once downloading CK-GPTune, you can install GPTune with the following command.

$ ck install ck-gptune:package:gptune

GPTune has multiple software dependencies (i.e. software packages that needed
by GPTune). For example, GPTune requires OpenMPI, BLAS, LAPACK, Scalapack,
MPI4PY, Scikit-optimize, Autotune, etc. This command automatically detects these
software dependencies during the installation steps.

If required softwares are not available, CK-GPTune will help you install the
software. If there are multiple software verions in your computer, CK-GPTune
will ask you to choose one, then CK-GPTune updates the environment variables
to keep the version numbers and the paths.

The GPTune framework, by default, will be installed in a sub directory in
$HOME/CK-TOOLS directory.

## Detect GPTune installation

You can detect the GPTune installation path and set environment variables with
the following CK command.

$ ck detect ck-gptune:soft:lib.gptune

## GPTune example programs

We provide a number of scripts and program codes to use GPTune for autotuning.
You can find the programs in the program directory. These programs can be
installed and executed with the following commands.

$ ck install ck-gptune:program:hypre
$ ck run ck-gptune:program:hypre

## Run GPTune Workflows

CK-GPTune provides a CK module called 'gptune' that provides multiple actions
to use GPTune workflows (e.g. run autotuning with or without history database).

- Run GPTune autotuner without using history database

$ ck autotune gptune --bench=hypre

- Run GPTune autotuner with history database

$ ck crowdtune gptune --bench=hypre

- Passing arguments

We can also pass some arguments as follows. If arguments are not given by the
command line, GPTune uses default values defined in the program code.

$ ck autotune gptune --bench=hypre --ntask=10 --nruns=10

The results (stdout and history database) can be found in the tmp directory in
each benchmark directory (e.g. program/hypre/tmp).


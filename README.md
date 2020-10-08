# CK for GPTune

This repository contains artifacts and workflows to use GPTune
(https://github.com/gptune/GPTune) with the Collective Knowledge (CK)
(https://cknowledge.org/) technology.

## Pre-requisites

- Linux
- Python 3+
- Collective Knowledge Framework (CK) - https://cknowledge.org/

## Install GPTune

CK-GPTune allows you to install the GPTune software package
(https://github.com/gptune/GPTune/tree/history_db) with the following command.

```
$ ck install package:gptune
```

GPTune has multiple dependencies (i.e. software packages needed by GPTune).
For example, GPTune requires OpenMPI, BLAS, LAPACK, Scalapack, MPI4PY,
Scikit-optimize, and Autotune. This command automatically detects
whether these software are available on your system.

If there are missing software packages, CK-GPTune will print out a message to
let you know which software packages need to be installed. If there are multiple
software verions in your computer, CK-GPTune will ask you to choose one.

After resolving all the dependencies, the GPTune software will be automatically
installed in a sub directory in $HOME/CK-TOOLS.

```
e.g. $HOME/CK-TOOLS/lib-gptune-1.0.0-gcc-9.3.0-compiler.python-3.8.5-linux-64
```

## Detect GPTune

Before using CK-GPTune workflows, you will need to detect the GPTune package
with the following CK command.

```
$ ck detect soft:lib.gptune
```

This command will detect the GPTune software installation paths and prepare
an executable environment by setting all the required environment variables,
this is also called CK `virtual` environment.

## GPTune example programs

This repository provides a number of benchmark programs to test GPTune.
We are currently offering four programs `gptune-demo`, `scalapack-pdqrdriver`,
`superlu-pddspawn`, and `hypre-ij`. Please check out the `program` directory
for the details.

You can install (compile) and run these benchmarks using simple CK command line interafaces.
Similar to when we install the GPTune software package,
if there are software dependencies (defined in meta.json in the .cm directory
of each benchmark), CK-GPTune will detect the installation `path` and `version`
of the required softwares.

```
$ ck compile ck-gptune:program:hypre
```

We can also run the benchmark, as defined by the `run_cmd` in the meta.json file.

```
$ ck run ck-gptune:program:hypre
```

## Run GPTune Workflows

CK-GPTune provides a CK module called `gptune` that provides multiple actions
to use GPTune for specific purposes (e.g. run autotuning with or without history database).
We can run GPTune workflows as follows.

### Run Autotuning

```
$ ck autotune gptune --bench=hypre
```

This command will run the autotuner for the `hypre` example without history database.
The output is stored in the `tmp` directory in `ck-gptune/program/hypre/tmp`.

### How to pass arguments

We can also pass arguments as follows. If the argument values are not given by this
command line, GPTune will use the default values defined in the program code.

```
$ ck autotune gptune --bench=hypre --ntask=10 --nruns=10
```

### Autotuning with history database

```
$ ck crowdtune gptune --bench=hypre
```

This command will run the autotuner for the `hypre` example with history database.
The output is stored in the `tmp` directory in `ck-gptune/program/hypre/tmp`.
The performance data JSON file will also be stored in the `tmp` directory.

### What will be stored in the history JSON files?

The GPTune autotuner receives the information about input space (IS) and
parameter space (PS) from the user, then computes output space (OS) after function evaluations.
Each application will have a JSON file which contains all the IS, PS, and OS information
from all previous runs.

*Regarding PS*

In addition to the PS information given by the autotuner parameter, we also save the machine info. (name),
the number of nodes/cores in the last dimensions of the PS (PS\_m).

Also, I am now working on saving the versions of software packages in addition to the current PS.
This should be done easily because we can now leverage the software package detection plugins that we
have developed for automating installation of GPTune and benchmark applications.

*Some Examples*

the `soft` directory contains software detection plugins that we have added for CK-GPTune.

`program/hypre/tmp/hypre.json' contains an example JSON history performance data file.

`program/hypre/tmp/env.temp' shows an environment setup (versions of detected software packages).

## Acknowledgements

GPTune Copyright (c) 2019, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy) and the University of California, Berkeley. All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE. This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.


# CK for GPTune

This repository contains artifacts and workflows to use GPTune
(https://github.com/gptune/GPTune) with the Collective Knowledge (CK)
(https://cknowledge.org/) technology.

## Pre-requisites

- Linux
- Python 3+
- Collective Knowledge Framework (CK) - https://cknowledge.org/
- Other dependencies can be installed by CK-GPTune workflows

## Installation of GPTune

CK-GPTune allows you to install the GPTune software package
(https://github.com/gptune/GPTune/tree/history_db) using the following command.

```
$ ck install package:gptune
```

GPTune has multiple dependencies (i.e. software packages needed by GPTune).
For example, GPTune requires OpenMPI, BLAS, LAPACK, Scalapack, MPI4PY,
Scikit-optimize, and Autotune. This command automatically detects
whether these software are already available on your system.

If these softwares are not available, CK-GPTune will print out a message to
let you know which software packages need to be installed. If there are multiple
software verions in your computer, CK-GPTune will ask you to choose one,
then CK-GPTune updates the environment variables to keep the version numbers
and the paths.

After resolving all the dependencies, the GPTune software will be automatically
installed in a sub directory in $HOME/CK-TOOLS.

```
e.g. $HOME/CK-TOOLS/lib-gptune-1.0.0-gcc-9.3.0-compiler.python-3.8.5-linux-64
```

## Detect GPTune installation

Before using CK-GPTune workflows, you will need to detect the GPTune package
with the following CK command.

```
$ ck detect soft:lib.gptune
```

This command will detect the GPTune software installation paths and prepare
an executable environment by setting required environment variables, this is so
called CK `virtual` environment.

## GPTune example programs

This repository provides a number of benchmark programs to test GPTune.
You can install and run these benchmarks using simple CK command line interafaces.
We are currently offering four programs `gptune-demo`, `scalapack-pdqrdriver`,
`superlu-pddspawn`, and `hypre-ij`. You can find these programs in the `program` directory.

These programs can be installed and executed with the following commands.

#### Installation of programs

Similar to the GPTune software package, we can install these programs using
a simple command. If there are software dependencies (defined in the meta.json
of each benchmark), this command will detect the `path` and `version` of the
required softwares.

```
$ ck install ck-gptune:program:hypre
```

We can also run the benchmark, as defined by the `run_cmd` in the meta.json file.

```
$ ck run ck-gptune:program:hypre
```

## Run GPTune Workflows

CK-GPTune provides a CK module called `gptune` that provides multiple actions
to use GPTune for specific purposes (e.g. run autotuning with or without history database).

#### Autotuning without using history database

```
$ ck autotune gptune --bench=hypre
```

This command will run the autotuner for the `hypre` example. The output is stored
in the `tmp` directory in `ck-gptune/program/hypre/tmp`.

#### Autotuning with history database

```
$ ck crowdtune gptune --bench=hypre
```

This command will run the autotuner for the `hypre` example with history database.
The output is stored in the `tmp` directory in `ck-gptune/program/hypre/tmp`.
The performance data JSON file is also stored in the `tmp` directory.

#### What will be saved in the history JSON file?

The GPTune autotuner receives information about input space (IS) and
parameter space (PS) from the user, then computes output space (OS) after function evaluations.
Each application will have a JSON file which contains all IS, PS, and OS information
from all prevoius runs.

Regarding PS: in addition to the PS information from the users,
we also save the machine info (name), MPI run info. (the number of nodes/cores) in the
last dimensions of the PS.

Then, I am now working on saving the versions of software packages in the last demensions of the PS.
This should be done shortly because we can leverage the software package detection plugins that we
have developed for preparing benchmark applications (see the above `Installation of programs`).


#### How to pass arguments

We can also pass arguments as follows. If the argument values are not given by this
command line, GPTune will use the default values defined in the program code.

```
$ ck autotune gptune --bench=hypre --ntask=10 --nruns=10
```



# CK for GPTune

This repository contains artifacts and workflows to use GPTune (https://github.com/gptune/GPTune) with the Collective Knowledge (CK) (https://cknowledge.org/) technology.

## Pre-requisites

- Python 3+
- Collective Knowledge Framework (CK) - https://cknowledge.org/

```
$ pip install ck --user
```

Please check if CK is installed correclty, by using the following command:
```
$ ck version
```

If the CK binary path is not set correclty, you may want to try this:
```
$ python -m ck version
$ alias ck="python -m ck"
```

## Install CK-GPTune

Once you have installed CK, then you can install CK-GPTune using the following command:
```
$ ck pull repo --url=https://github.com/gptune/CK-GPTune
```
This will also installs several required CK repositories/modules/tools automatically. The user can check $HOME/CK directory for the details.

There are also several patch files in CK-GPTune to supplement the original CK tools. Please use the following command:
```
$ bash patch.sh
```

## GPTune Auto-Installation (this feature is not up-to-date; recommended to install GPTune manually or using GPTune installation scripts)

CK-GPTune allows you to install the GPTune software package (https://github.com/gptune/GPTune/tree/history_db) with the following command.

```
$ ck install package:gptune
```

GPTune has multiple dependencies (i.e. software packages needed by GPTune). For example, GPTune requires OpenMPI, BLAS, LAPACK, Scalapack, MPI4PY, Scikit-optimize, and Autotune. This command automatically detects whether these software are available on your system.

If there are missing software packages, CK-GPTune will print out a message to let you know which software packages need to be installed. If there are multiple software verions in your computer, CK-GPTune will ask you to choose one.

After resolving all the dependencies, the GPTune software will be automatically installed in a sub directory in $HOME/CK-TOOLS.

```
e.g. $HOME/CK-TOOLS/lib-gptune-1.0.0-gcc-9.3.0-compiler.python-3.8.5-linux-64
```

## Detect GPTune

Before using any CK-based workflows in CK-GPTune, the user needs to detect the installed GPTune package with the following CK command.

```
$ ck detect soft:lib.gptune
```

This command will detect the GPTune software installation paths and prepare an executable environment by setting all the required environment variables, this is also called CK `virtual` environment.

You can check the detected software environment variables in $HOME/CK/local/env/.

## CK-enabled reproducible tuning workflows

CK-GPTune provides a number of tuning workflows using GPTune. We are currently offering four programs `gptune-demo`, `ScaLAPACK-PDGEQRF`, `SuperLU_DIST-PDDRIVE`, and `Hypre-IJ`. Please check out the `program` directory for the details.

The user can install (compile) and run these benchmarks using simple CK command line interafaces. Similar to when we install the GPTune software package, if there are software dependencies (defined in meta.json in the .cm directory of each benchmark), CK-GPTune will detect the installation `path` and `version` of the required softwares.

```
$ ck compile ck-gptune:program:ScaLAPACK-PDGEQRF
```

The user then run the workflow (with the GPTune's MLA history database features) using the following command:

```
$ ck MLA gptune program:ScaLAPACK-PDGEQRF
```

The provided examples in CK-GPTune automatically creates *tmp* directory in their program directory. After finishing the run, the user may want to check *stdout* and *stderr* files. The generated history database files will be stored in the *gptune.db* directory in the *tmp* directory.

### How to pass arguments

The user can also pass arguments as follows. If the argument values are not given by this command line, GPTune will use the default values defined in the program code.

```
$ ck MLA gptune --bench=ScaLAPACK-PDGEQRF --nruns=10
```

## Software detection plugins

The nice thing of CK is software detection plugins which detects the location and the version of the software. The CK community provides many software detection plugs via *ck-env* repository ($HOME/CK/ck-env). But, CK-GPTune also contains a number of software detection plugins that are not (yet) supported by *ck-env* repository.

The user can check out *soft* directory in CK-GPTune.

## Tested environments

We have tested CK-GPTune using standalone Linux machine, the Cori supercomputer at NERSC, and a Mac OS. Please let us know if you have any troubles with using CK-GPTune. 

## Acknowledgements

GPTune Copyright (c) 2019, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy) and the University of California, Berkeley. All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE. This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.

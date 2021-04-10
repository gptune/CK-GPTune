# CK for GPTune

This repository contains artifacts and workflows to use GPTune (https://github.com/gptune/GPTune) with the Collective Knowledge (CK) (https://cknowledge.org/) technology.

## Pre-requisites

- Python 3+
- Collective Knowledge Framework (CK) - https://cknowledge.org/

```
$ pip install ck --user
$ alias ck="python -m ck"
```

## Install CK-GPTune

Once you have installed CK, you can install CK-GPTune using the following command:
```
$ ck pull repo --url=https://github.com/gptune/CK-GPTune
```
This will also install several required CK repositories/modules/tools automatically. The user can check *$HOME/CK* directory for the details.

There are also several patch files in CK-GPTune to supplement the original CK tools. Please use the following command:
```
$ cd $HOME/CK/CK-GPTune/
$ bash patch.sh
```

## Detect GPTune

Before using any CK-based workflows in CK-GPTune, the user needs to detect the installed GPTune package with the following CK command.

```
$ ck detect soft:lib.gptune
```

This command will detect the GPTune software installation paths and prepare an executable environment by setting all the required environment variables, this is also called CK `virtual` environment.

You can check the detected software environment variables in $HOME/CK/local/env/.

## CK-enabled reproducible tuning workflows

CK-GPTune provides a number of reproducible GPTune tuning workflows with CK. We are currently offering four examples `gptune-demo`, `ScaLAPACK-PDGEQRF`, `SuperLU_DIST-PDDRIVE`, and `Hypre-IJ`. Please check out the `program` directory for the details.

The user can install (compile) and run these examples using simple command line interafaces. If there are software dependencies to compile/run, CK will detect the installation `path` and `version` of the required softwares. Defined software dependencies can be found at the meta.json file in the .cm directory of each program directory (e.g. *$HOME/CK/CK-GPTune/program/ScaLAPACK-PDGEQRF/.cm/meta.json*)


```
$ ck compile CK-GPTune:program:ScaLAPACK-PDGEQRF
```

CK-GPTune provides a command line interface to run CK-enabled GPTune workflows with the GPTune's MLA and history database features.

```
$ ck MLA gptune program:ScaLAPACK-PDGEQRF
```

The provided examples in CK-GPTune automatically creates *tmp* directory in their program directory. After finishing the run, the user may want to check *stdout* and *stderr* files. The generated history database files will be stored in the *gptune.db* directory in the *tmp* directory.

The user can also pass arguments as follows. If the argument values are not given by this command line, GPTune will use the default values defined in the program code.

```
$ ck MLA gptune --bench=ScaLAPACK-PDGEQRF --nruns=10
```

## Software detection plugins

One nice thing of CK is software detection plugins which detect the location and the version of the software. The CK community already provides many useful software detection plugs through the *ck-env* repository (*$HOME/CK/ck-env/soft*). But, CK-GPTune also contains a number of software detection plugins that are not (yet) supported by the *ck-env* repository.

The user can check out *soft* directory in CK-GPTune.

## Tested environments

We have tested CK-GPTune using standalone Linux machine, the Cori supercomputer at NERSC, and a Mac OS. Please let us know if you have any troubles with using CK-GPTune. 

## Acknowledgements

GPTune Copyright (c) 2019, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy) and the University of California, Berkeley. All rights reserved.

If you have questions about your rights to use or distribute this software, please contact Berkeley Lab's Intellectual Property Office at IPO@lbl.gov.

NOTICE. This Software was developed under funding from the U.S. Department of Energy and the U.S. Government consequently retains certain rights. As such, the U.S. Government has been granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in the Software to reproduce, distribute copies to the public, prepare derivative works, and perform publicly and display publicly, and to permit other to do so.

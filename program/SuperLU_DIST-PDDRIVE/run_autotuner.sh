#!/bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/superlu_dist/parmetis-4.0.3/install/lib/

mpirun --oversubscribe --mca pmix_server_max_wait 3600 --mca pmix_base_exchange_timeout 3600 --mca orte_abort_timeout 3600 --mca plm_rsh_no_tree_spawn true -n 1 python ../gptune_driver.py

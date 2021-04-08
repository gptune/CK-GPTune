#! /usr/bin/env python3

"""
Example of invocation of this script:

mpirun -n 1 python scalapack_MLA.py -mmax 5000 -nmax 5000 -nprocmin_pernode 1 -ntask 5 -nrun 10 -jobid 0 -tla 0

where:
    -mmax (nmax) is the maximum number of rows (columns) in a matrix
    -nprocmin_pernode is the minimum number of MPIs per node for launching the application code
    -ntask is the number of different matrix sizes that will be tuned
    -nrun is the number of calls per task 
    -jobid is optional. You can always set it to 0.
    -tla is whether TLA is used after MLA
"""

import sys
import os

from pdqrdriver import pdqrdriver
from autotune.search import *
from autotune.space import *
from autotune.problem import *
from gptune import *

import numpy as np
import argparse
import pickle
from random import *
import time
import math

''' The objective function required by GPTune. '''
# should always use this name for user-defined objective function
def objectives(point):

######################################### 
##### constants defined in TuningProblem
    nodes = point['nodes']
    cores = point['cores']
    bunit = point['bunit']	
#########################################

    m = point['m']
    n = point['n']
    mb = point['mb']*bunit
    nb = point['nb']*bunit
    p = point['p']
    npernode = 2**point['npernode']
    nproc = nodes*npernode
    nthreads = int(cores / npernode)  

    # this becomes useful when the parameters returned by TLA1 do not respect the constraints
    if(nproc == 0 or p == 0 or nproc < p):
        print('Warning: wrong parameters for objective function!!!')
        return 1e12
    q = int(nproc / p)
    nproc = p*q
    params = [('QR', m, n, nodes, cores, mb, nb, nthreads, nproc, p, q, 1., npernode)]

    print(params, ' scalapack starts ') 
    elapsedtime = pdqrdriver(params, niter=2, JOBID=JOBID)
    print(params, ' scalapack time: ', elapsedtime)

    return elapsedtime

def cst1(mb,p,m,bunit):
    return mb*bunit * p <= m
def cst2(nb,npernode,n,p,nodes,bunit):
    return nb * bunit * nodes * 2**npernode <= n * p
def cst3(npernode,p,nodes):
    return nodes * 2**npernode >= p

def main():

    global JOBID

    nprocmin_pernode = int(os.environ.get('nprocmin_pernode','1'))
    nrun = int(os.environ.get('nrun','10'))
    JOBID = int(os.environ.get('jobid','1'))

    (machine, processor, nodes, cores) = GetMachineConfiguration()
    print ("machine: " + machine + " processor: " + processor + " num_nodes: " + str(nodes) + " num_cores: " + str(cores))
    os.system("mkdir -p scalapack-driver/bin/%s; cp ./pdqrdriver scalapack-driver/bin/%s/.;" %(machine, machine))

    os.environ['MACHINE_NAME'] = machine
    os.environ['TUNER_NAME'] = 'GPTune'

    nprocmax = nodes*cores
    bunit=8     # the block size is multiple of bunit
    mmin=128
    nmin=128
    mmax=40000
    nmax=40000

    m = Integer(mmin, mmax, transform="normalize", name="m")
    n = Integer(nmin, nmax, transform="normalize", name="n")
    mb = Integer(1, 16, transform="normalize", name="mb")
    nb = Integer(1, 16, transform="normalize", name="nb")
    npernode = Integer(int(math.log2(nprocmin_pernode)), int(math.log2(cores)), transform="normalize", name="npernode")
    p = Integer(1, nprocmax, transform="normalize", name="p")
    r = Real(float("-Inf"), float("Inf"), name="r")

    IS = Space([m, n])
    PS = Space([mb, nb, npernode, p])
    OS = Space([r])
    
    constraints = {"cst1": cst1, "cst2": cst2, "cst3": cst3}
    constants={"nodes":nodes,"cores":cores,"bunit":bunit}
    print(IS, PS, OS, constraints)

    problem = TuningProblem(IS, PS, OS, objectives, constraints, None, constants=constants)
    computer = Computer(nodes=nodes, cores=cores, hosts=None)

    """ Set and validate options """
    options = Options()
    options['model_processes'] = 1
    # options['model_threads'] = 1
    options['model_restarts'] = 1
    # options['search_multitask_processes'] = 1
    # options['model_restart_processes'] = 1
    # options['model_restart_threads'] = 1
    options['distributed_memory_parallelism'] = False
    options['shared_memory_parallelism'] = False
    # options['mpi_comm'] = None
    options['model_class'] = 'Model_LCM'
    options['verbose'] = False
    options.validate(computer=computer)

    giventask = [[2000,2000],[4000,4000]]

    ntask=len(giventask)
    
    data = Data(problem)

    gt = GPTune(problem, computer=computer, data=data, options=options, driverabspath=os.path.abspath(__file__))

    """ Building MLA with the given list of tasks """
    NI = len(giventask)
    NS = nrun
    (data, model, stats) = gt.MLA(NS=NS, Igiven=giventask, NI=NI, NS1=max(NS//2, 1))
    print("stats: ", stats)

    """ Print all input and parameter samples """
    for tid in range(NI):
        print("tid: %d" % (tid))
        print("    m:%d n:%d" % (data.I[tid][0], data.I[tid][1]))
        print("    Ps ", data.P[tid])
        print("    Os ", data.O[tid].tolist())
        print('    Popt ', data.P[tid][np.argmin(data.O[tid])], 'Oopt ', min(data.O[tid])[0], 'nth ', np.argmin(data.O[tid]))
    
if __name__ == "__main__":
    main()

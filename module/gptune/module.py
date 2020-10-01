#
# Collective Knowledge (GPTune workflows)
#
#
#
#
# Developer:
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel)


#gptune_benchmarks = ["gptune-demo","scalapack","superlu_dist"]
gptune_benchmarks = ["gptune-demo","scalapack-pdqrdriver"]

# Local settings

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# autotune with gptune with history database

def crowdtune(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    ck.out('autotune with gptune with history database')
    ck.out('currently do not support history database')

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    application=i['bench']

    if application in gptune_benchmarks:
        ck.out('run target application: ' + application)

        import copy

        input_keys = list(i.keys())
        argument_keys = copy.deepcopy(input_keys)
        prescribed_keys = {'cids', 'action', 'bench', 'cid', 'out', 'module_uoa', 'xcids'}
        for prescribed_key in prescribed_keys:
            argument_keys.remove(prescribed_key)
        print (argument_keys)

        arguments = {}
        for argument_key in argument_keys:
            arguments[argument_key] = i[argument_key]
        arguments['history_db']='yes'
        #arguments = {'history_db':'yes'}
        print (arguments)

        r=ck.access({'action':'run',
                     'module_uoa':'program',
                     'data_uoa':application,
                     'env':arguments})
        if r['return']>0: return r

    else:
        ck.out('not available application: ' + application)

    return {'return':0}

##############################################################################
# autotune with gptune (default)

def autotune(i):
    """
    Input:  {
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """

    ck.out('autotune with gptune (default)')

    ck.out('')
    ck.out('Command line: ')
    ck.out('')

    import json
    cmd=json.dumps(i, indent=2)

    ck.out(cmd)

    application=i['bench']

    if application in gptune_benchmarks:
        ck.out('run target application: ' + application)
        import copy

        input_keys = list(i.keys())
        argument_keys = copy.deepcopy(input_keys)
        prescribed_keys = {'cids', 'action', 'bench', 'cid', 'out', 'module_uoa', 'xcids'}
        for prescribed_key in prescribed_keys:
            argument_keys.remove(prescribed_key)
        print (argument_keys)

        arguments = {}
        for argument_key in argument_keys:
            arguments[argument_key] = i[argument_key]
        print (arguments)

        r=ck.access({'action':'run',
                     'module_uoa':'program',
                     'data_uoa':application,
                     'env':arguments})
        if r['return']>0: return r

    else:
        ck.out('not available application: ' + application)

    return {'return':0}

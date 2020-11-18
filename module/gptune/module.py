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
gptune_benchmarks = ["gptune-demo","scalapack-pdqrdriver","hypre","superlu"]

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
# parse software dependencies from deps.json in CK-GPTune program's directory

def parse_dependencies(i):
    import json
    import os.path
    from os import path

    application = i['bench']

    r = ck.find_path_to_data({'module_uoa':'program',
        'data_uoa':application})
    path_to_entry = r['path']
    path_to_entry_meta_file = path_to_entry + "/.cm/meta.json"

    print (path_to_entry_meta_file)

    compile_deps_version_info = {}

    with open(path_to_entry_meta_file, "r") as meta_file:
        meta_data = json.load(meta_file)

        compile_deps = meta_data['compile_deps']
        compile_deps_list = list(compile_deps.keys())

        if meta_data['process_in_tmp'] == "yes":
            path_to_deps_file = path_to_entry + "/tmp/tmp-deps.json"
            if path.exists(path_to_deps_file):
                with open(path_to_deps_file) as deps_file:
                    deps_data = json.load(deps_file)

                    for dep in compile_deps_list:
                        version = deps_data[dep]['cus']['version']
                        version_split = deps_data[dep]['cus']['version_split']
                        version_info = {}
                        version_info['version'] = version
                        version_info['version_split'] = version_split
                        compile_deps_version_info[dep] = version_info

    return (compile_deps_version_info)


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
        #print (argument_keys)

        arguments = {}
        for argument_key in argument_keys:
            arguments[argument_key] = i[argument_key]
        arguments['CKGPTUNE_HISTORY_DB'] = 'yes'
        arguments['CKGPTUNE_APPLICATION_NAME'] = application

        compile_deps_version_info = parse_dependencies(i)
        arguments['CKGPTUNE_COMPILE_DEPS'] = compile_deps_version_info
        arguments['CKGPTUNE_MACHINE_NAME'] = i['machine']

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

##############################################################################
# run MLA with gptune

def MLA(i):
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


##############################################################################
# run MLA with history database

def MLA_HistoryDB(i):
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
        #print (argument_keys)

        arguments = {}
        for argument_key in argument_keys:
            arguments[argument_key] = i[argument_key]
        arguments['CKGPTUNE_HISTORY_DB'] = 'yes'
        arguments['CKGPTUNE_APPLICATION_NAME'] = application

        compile_deps_version_info = parse_dependencies(i)
        arguments['CKGPTUNE_COMPILE_DEPS'] = compile_deps_version_info
        arguments['CKGPTUNE_MACHINE_NAME'] = i['machine']

        r=ck.access({'action':'run',
                     'module_uoa':'program',
                     'data_uoa':application,
                     'env':arguments})
        if r['return']>0: return r

    else:
        ck.out('not available application: ' + application)

    return {'return':0}


##############################################################################
# run MLA with surrogate model

def MLA_LoadModel(i):
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
        #print (argument_keys)

        arguments = {}
        for argument_key in argument_keys:
            arguments[argument_key] = i[argument_key]
        arguments['CKGPTUNE_HISTORY_DB'] = 'yes'
        arguments['CKGPTUNE_APPLICATION_NAME'] = application

        compile_deps_version_info = parse_dependencies(i)
        arguments['CKGPTUNE_COMPILE_DEPS'] = compile_deps_version_info
        arguments['CKGPTUNE_MACHINE_NAME'] = i['machine']

        arguments['CKGPTUNE_LOAD_MODEL'] = 'yes'

        r=ck.access({'action':'run',
                     'module_uoa':'program',
                     'data_uoa':application,
                     'env':arguments})
        if r['return']>0: return r

    else:
        ck.out('not available application: ' + application)

    return {'return':0}

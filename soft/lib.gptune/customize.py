#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#

import os
import sys

##############################################################################

def version_cmd(i):
    path_with_init_py       = i['full_path']                            # the full_path that ends with PACKAGE_NAME/__init__.py
    path_without_init_py    = os.path.dirname( path_with_init_py )
    package_name            = os.path.basename( path_without_init_py )
    site_dir                = os.path.dirname( path_without_init_py )
    ck                      = i['ck_kernel']
    cus                     = i['customize']

    detect_version_as           = str(cus.get('detect_version_as', ''))
    detect_version_externally   = cus.get('detect_version_externally', 'no') == 'yes'
    version_variable_name       = cus.get('version_variable_name', '__version__')

    if detect_version_as!='':   # sic: otherwise version 0 cannot be suggested
        return {'return':0, 'version':detect_version_as}

    elif detect_version_externally:
        desired_python_path     = i.get('deps', {}).get('python', {}).get('dict', {}).get('env', {}).get('CK_ENV_COMPILER_PYTHON_FILE', sys.executable)

        version_cmd     = '{} -c "import sys; sys.path.insert(0,\'{}\'); import {}; print({}.{})" >$#filename#$'.format(
            desired_python_path, site_dir, package_name, package_name, version_variable_name);

        return {'return':0, 'cmd':version_cmd}

    else:
        version_recursive_import  = cus.get('version_recursive_import', 'no') == 'yes'
        version_module_name       = cus.get('version_module_name', '__init__')

        if version_recursive_import:
            sys.path.insert(0, site_dir)    # temporarily prepend site_dir to allow the potential recursive imports to work
        rx=ck.load_module_from_path({'path':path_without_init_py, 'module_code_name':version_module_name, 'skip_init':'yes'})
        if version_recursive_import:
            sys.path.pop(0)                 # restore the original module search path

        if rx['return']==0:
            loaded_package  = rx['code']
            version_string  = getattr(loaded_package, version_variable_name)
        else:
            ck.out('Failed to import package '+package_name+' : '+rx['error'])
            version_string  = ''

        return {'return':0, 'cmd':'', 'version':version_string}

##############################################################################

def dirs(i):
    hosd    = i['host_os_dict']
    macos   = hosd.get('macos','')
    #dirs    = []
    dirs    = i.get('dirs', [])

    if macos:
        python_site_packages_dir = os.path.expanduser("~") + "/Library/Python"
        if os.path.isdir( python_site_packages_dir ):
            dirs.append( python_site_packages_dir )

    return {'return':0, 'dirs':dirs}

##############################################################################

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta

              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """


    # Get variables
    ck=i['ck_kernel']

    iv=i.get('interactive','')

    cus=i.get('customize',{})

    hosd=i['host_os_dict']
    tosd=i['target_os_dict']

    winh=hosd.get('windows_base','')

    full_path               = cus.get('full_path','')
    path_lib                = os.path.dirname(full_path)
    path_build              = os.path.dirname(path_lib)

    env                     = i['env']
    env['PYTHONPATH']       = path_build + ( ';%PYTHONPATH%' if winh=='yes' else ':${PYTHONPATH}')

    # The following assumes the package has been installed (rather than detected) :
    #
    path_install            = os.path.dirname(path_build)
    path_bin                = os.path.join(path_install, 'python_deps_site', 'bin')

    if os.path.isdir(path_bin):
        env['PATH']         = path_bin + ( ';%PATH%' if winh=='yes' else ':${PATH}')

    print ("full_path: " + full_path)
    print ("path_lib: " + path_lib)
    print ("path_build: " + path_build)

    env['GPTUNEROOT']       = path_build

    gptune_lib_path         = os.path.join(path_build, 'scalapack-2.1.0/build/install/lib')

    env['LD_LIBRARY_PATH']   = gptune_lib_path + ":${LD_LIBRARY_PATH}"
    env['DYLD_LIBRARY_PATH'] = gptune_lib_path + ":${DYLD_LIBRARY_PATH}"

    gptune_python_codes     = os.path.join(path_build, 'GPTune')
    autotune_path           = os.path.join(path_build, 'autotune')
    scikit_optimize_path    = os.path.join(path_build, 'scikit-optimize')
    mpi4py_path             = os.path.join(path_build, 'mpi4py')
    scalapack_driver_path   = os.path.join(path_build, 'scalapack-driver/spt')

    env['PYTHONPATH']       = path_build + ":" + gptune_python_codes + ":" + autotune_path + ":" + scikit_optimize_path + ":" + mpi4py_path + ":" + scalapack_driver_path + ( ';%PYTHONPATH%' if winh=='yes' else ':${PYTHONPATH}')

    return {'return':0, 'bat':''}

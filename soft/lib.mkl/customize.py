#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Younghyun Cho, younghyun@berkeley.edu
#

import re

def version_cmd(i):
    import os
    import subprocess

    # Get variables
    cus = i.get('customize', {})
    full_path = cus.get('full_path','')
    path_lib = os.path.dirname(full_path)
    path_include = os.path.join(path_lib, "../include")

    output = subprocess.getstatusoutput("cat /opt/intel/compilers_and_libraries_2019.3.199/linux/mkl/include/mkl_version.h | grep __INTEL_MKL__")
    version_major = output[1].split(" ")[-1]

    output = subprocess.getstatusoutput("cat /opt/intel/compilers_and_libraries_2019.3.199/linux/mkl/include/mkl_version.h | grep __INTEL_MKL_MINOR__")
    version_minor = output[1].split(" ")[-1]

    output = subprocess.getstatusoutput("cat /opt/intel/compilers_and_libraries_2019.3.199/linux/mkl/include/mkl_version.h | grep __INTEL_MKL_UPDATE__")
    version_update = output[1].split(" ")[-1]

    return {'return':0, 'cmd': '', 'version': str(version_major)+"."+str(version_minor)+"."+str(version_update)}


##############################################################################
# setup environment setup

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

    import os

    # Get variables
    ck=i['ck_kernel']

    s = ''

    iv = i.get('interactive','')

    cus = i.get('customize', {})

    ep=cus.get('env_prefix','')

    full_path = cus.get('full_path','')
    path_lib = os.path.dirname(full_path)
    path_install = os.path.dirname(path_lib)

    print ("full_path: "+full_path)
    print ("path_lib: "+path_lib)
    print ("path_install: "+path_install)

    env = i['env']

    env[ep+'_PATH'] = full_path
    env[ep+'_DIR'] = path_lib
    env[ep+'_INCLUDE'] = os.path.join(path_lib, "../include")

    return {'return':0, 'bat':s}

#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

##############################################################################
# get version from path

import os

def version_cmd(i):

    import subprocess

    ck=i['ck_kernel']

    full_path=i['full_path']
    fp=i['full_path']
    p1=os.path.dirname(fp)
    p2=os.path.dirname(p1)
    scalapack_pc = str(p2)+"/scalapack.pc"

    output = subprocess.getstatusoutput("cat " + scalapack_pc + " | grep Version")
    version_split = output[1].split(" ")[-1]
    version_split = version_split.split("rc")[0]

    return {'return':0, 'cmd': '', 'version': str(version_split)}

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
    s=''

    iv=i.get('interactive','')

    env=i.get('env',{})
    cfg=i.get('cfg',{})
    deps=i.get('deps',{})
    tags=i.get('tags',[])
    cus=i.get('customize',{})

    target_d=i.get('target_os_dict',{})
    win=target_d.get('windows_base','')
    remote=target_d.get('remote','')
    mingw=target_d.get('mingw','')
    tbits=target_d.get('bits','')

    envp=cus.get('env_prefix','')
    pi=cus.get('path_install','')

    host_d=i.get('host_os_dict',{})
    sdirs=host_d.get('dir_sep','')

    fp=cus['full_path']
    p1=os.path.dirname(fp)
    pi=os.path.dirname(p1)

    cus['path_lib']=p1

    ep=cus['env_prefix']
    env[ep]=pi

    ################################################################
    if win=='yes':
       if remote=='yes' or mingw=='yes':
          sext='.a'
          dext='.so'
       else:
          sext='.lib'
          dext='.dll'
    else:
       sext='.a'
       dext='.so'

    r = ck.access({'action': 'lib_path_export_script', 'module_uoa': 'os', 'host_os_dict': host_d,
      'lib_path': cus.get('path_lib', '')})
    if r['return']>0: return r
    s += r['script']

    env[ep+'_LIB'] = fp
    env[ep+'_DIR'] = p1

    return {'return':0, 'bat':s}

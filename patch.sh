#/bin/bash

source ~/.bash_profile

output=$(ck  | grep 'Path to the default repo')
ck_default_path=${output##* }
additional_path="/module/soft/"
ck_module_path=${ck_default_path}${additional_path}

cp patches/soft.module.py $ck_module_path/module.py
cp patches/lib.openmpi.customize.py ../ck-env/soft/lib.openmpi/customize.py

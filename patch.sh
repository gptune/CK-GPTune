#/bin/bash

source ~/.bash_profile

output=$(ck  | grep 'Path to the default repo')
ck_default_path=${output##* }
additional_path="/module/soft/"
ck_module_path=${ck_default_path}${additional_path}

cp patch/soft_module.py $ck_module_path/module.py

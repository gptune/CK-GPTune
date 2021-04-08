#/bin/bash

output=$(python -m ck  | grep 'Path to the default repo')
ck_default_path=${output##* }
additional_path="/module/soft/"
ck_module_path=${ck_default_path}${additional_path}

cp patches/module:soft/module.py $ck_module_path/module.py
cp patches/soft:lib.openmpi/meta.json ../ck-env/soft/lib.openmpi/.cm/meta.json
cp patches/soft:lib.openmpi/customize.py ../ck-env/soft/lib.openmpi/customize.py
cp patches/soft:lib.parmetis/meta.json ../ck-env/soft/lib.parmetis/.cm/meta.json

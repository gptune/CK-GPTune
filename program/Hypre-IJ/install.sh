#!/bin/bash

rm -rf hypre

git clone https://github.com/hypre-space/hypre.git
git checkout b3a4a76a5fc965b148b55ed8e9c342666b9c3c41
cd hypre/src/
./configure

make
cp ../../../hypre-driver/src/ij.c ./test/.
make test

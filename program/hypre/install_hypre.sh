#/bin/bash

rm -rf hypre
git clone https://github.com/hypre-space/hypre.git
cd hypre/src/

./configure 
#CC=$CCC CXX=$CCCPP FC=$FTN CFLAGS="-DTIMERUSEMPI"

make
cp ../../../hypre-driver/src/ij.c ./test/.
make test

#/bin/bash

echo "MPICXX:" $MPICXX
echo "MPICC:" $MPICC
echo "MPIF90:" $MPIF90
echo "BLAS_LIB:" $BLAS_LIB
echo "LAPACK_LIB:" $LAPACK_LIB

rm -rf superlu_dist

git clone https://github.com/xiaoyeli/superlu_dist.git
cd superlu_dist
wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-4.0.3.tar.gz
tar -xf parmetis-4.0.3.tar.gz
cd parmetis-4.0.3/
mkdir -p install
make config shared=1 cc=$MPICC cxx=$MPICXX prefix=$PWD/install
make install
cd ../
export PARMETIS_INCLUDE_DIRS="$PWD/parmetis-4.0.3/metis/include;$PWD/parmetis-4.0.3/install/include"
export PARMETIS_LIBRARIES=$PWD/parmetis-4.0.3/install/lib/libparmetis.so

mkdir -p build
cd build
cmake .. \
    -DCMAKE_CXX_FLAGS="-Ofast -std=c++11 -DAdd_ -DRELEASE" \
    -DCMAKE_C_FLAGS="-std=c11 -DPRNTlevel=0 -DPROFlevel=0 -DDEBUGlevel=0" \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_CXX_COMPILER=$MPICXX \
    -DCMAKE_C_COMPILER=$MPICC \
    -DCMAKE_Fortran_COMPILER=$MPIF90 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DTPL_BLAS_LIBRARIES="$BLAS_LIB" \
    -DTPL_LAPACK_LIBRARIES="$LAPACK_LIB" \
    -DTPL_PARMETIS_INCLUDE_DIRS=$PARMETIS_INCLUDE_DIRS \
    -DTPL_PARMETIS_LIBRARIES=$PARMETIS_LIBRARIES
truncate --size -1 EXAMPLE/CMakeFiles/pddrive_spawn.dir/link.txt
echo " -lblas -lgfortran" >> EXAMPLE/CMakeFiles/pddrive_spawn.dir/link.txt
make pddrive_spawn

#! /bin/bash

git clone -b history_db https://github.com/gptune/GPTune GPTune

export GPTUNEROOT=GPTune/
cd $GPTUNEROOT
mkdir -p build
cd build

echo "MPICXX:" $MPICXX
echo "MPICC:" $MPICC
echo "MPIF90:" $MPIF90
echo "BLAS_LIB:" $BLAS_LIB
echo "LAPACK_LIB:" $LAPACK_LIB
echo "SCALAPACK_LIB: " $SCALAPACK_LIB

cmake .. \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_CXX_COMPILER=$MPICXX \
    -DCMAKE_C_COMPILER=$MPICC \
    -DCMAKE_Fortran_COMPILER=$MPIF90 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DTPL_BLAS_LIBRARIES="$BLAS_LIB" \
    -DTPL_LAPACK_LIBRARIES="$LAPACK_LIB" \
    -DTPL_SCALAPACK_LIBRARIES=$SCALAPACK_LIB
make 
#cp lib_gptuneclcm.so ../.


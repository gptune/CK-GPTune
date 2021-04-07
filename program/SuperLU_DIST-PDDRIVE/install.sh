#/bin/bash

export MPICC="$CK_ENV_LIB_MPI_BIN/mpicc"
export MPICXX="$CK_ENV_LIB_MPI_BIN/mpicxx"
export MPIF90="$CK_ENV_LIB_MPI_BIN/mpif90"
export BLAS_LIB="$CK_ENV_LIB_MKL_DIR/libmkl_gf_lp64.so;$CK_ENV_LIB_MKL_DIR/libmkl_gnu_thread.so;$CK_ENV_LIB_MKL_DIR/libmkl_core.so;-lgomp"
export LAPACK_LIB="$CK_ENV_LIB_MKL_DIR/libmkl_gf_lp64.so;$CK_ENV_LIB_MKL_DIR/libmkl_gnu_thread.so;$CK_ENV_LIB_MKL_DIR/libmkl_core.so;-lgomp"

export ParMETIS_DIR="$PWD/superlu_dist/parmetis-4.0.3/install"
export METIS_DIR=$ParMETIS_DIR
export PARMETIS_INCLUDE_DIRS="$ParMETIS_DIR/../metis/include;$ParMETIS_DIR/include"
export METIS_INCLUDE_DIRS="$ParMETIS_DIR/../metis/include"
export PARMETIS_LIBRARIES=$ParMETIS_DIR/lib/libparmetis.so
export METIS_LIBRARIES=$ParMETIS_DIR/lib/libmetis.so

git clone https://github.com/xiaoyeli/superlu_dist.git
cd superlu_dist

wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/parmetis/parmetis-4.0.3.tar.gz
tar -xf parmetis-4.0.3.tar.gz
cd parmetis-4.0.3/
cp ../../../patches/parmetis/CMakeLists.txt .
mkdir -p install
make config shared=1 cc=$MPICC cxx=$MPICXX prefix=$PWD/install
make install > make_parmetis_install.log 2>&1

cd ../
cp $PWD/parmetis-4.0.3/build/Linux-x86_64/libmetis/libmetis.so $PWD/parmetis-4.0.3/install/lib/.
cp $PWD/parmetis-4.0.3/metis/include/metis.h $PWD/parmetis-4.0.3/install/include/.
mkdir -p build
cd build
rm -rf CMakeCache.txt
rm -rf DartConfiguration.tcl
rm -rf CTestTestfile.cmake
rm -rf cmake_install.cmake
rm -rf CMakeFiles
cmake .. \
    -DCMAKE_CXX_FLAGS="-Ofast -std=c++11 -DAdd_ -DRELEASE" \
    -DCMAKE_C_FLAGS="-std=c11 -DPRNTlevel=0 -DPROFlevel=0 -DDEBUGlevel=0" \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_CXX_COMPILER=$MPICXX \
    -DCMAKE_C_COMPILER=$MPICC \
    -DCMAKE_Fortran_COMPILER=$MPIF90 \
    -DCMAKE_INSTALL_PREFIX=. \
    -DCMAKE_INSTALL_LIBDIR=./lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DTPL_BLAS_LIBRARIES="${BLAS_LIB}" \
    -DTPL_LAPACK_LIBRARIES="${LAPACK_LIB}" \
    -DTPL_PARMETIS_INCLUDE_DIRS=$PARMETIS_INCLUDE_DIRS \
    -DTPL_PARMETIS_LIBRARIES=$PARMETIS_LIBRARIES
make pddrive_spawn
make pzdrive_spawn
make install


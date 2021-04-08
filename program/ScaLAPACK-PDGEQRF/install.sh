#! /bin/bash

# Get detected software paths from CK
export MPICC="$CK_ENV_LIB_MPI_BIN/mpicc"
export MPICXX="$CK_ENV_LIB_MPI_BIN/mpicxx"
export MPIF90="$CK_ENV_LIB_MPI_BIN/mpif90"
export BLAS_LIB="$CK_ENV_LIB_MKL_DIR/libmkl_gf_lp64.so;$CK_ENV_LIB_MKL_DIR/libmkl_gnu_thread.so;$CK_ENV_LIB_MKL_DIR/libmkl_core.so;-lgomp"
export LAPACK_LIB="$CK_ENV_LIB_MKL_DIR/libmkl_gf_lp64.so;$CK_ENV_LIB_MKL_DIR/libmkl_gnu_thread.so;$CK_ENV_LIB_MKL_DIR/libmkl_core.so;-lgomp"
export SCALAPACK_LIB=$CK_ENV_LIB_SCALAPACK_LIB
export OPENMPFLAG=$CK_COMPILER_FLAG_OPENMP

# Install PDGEQRF tuning routine from GPTune
git clone https://github.com/gptune/GPTune GPTune
cd GPTune
mkdir -p build
cd build
rm -rf CMakeCache.txt
rm -rf DartConfiguration.tcl
rm -rf CTestTestfile.cmake
rm -rf cmake_install.cmake
rm -rf CMakeFiles
cmake .. \
	-DCMAKE_CXX_FLAGS="$OPENMPFLAG" \
	-DCMAKE_C_FLAGS="$OPENMPFLAG" \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_CXX_COMPILER=$MPICXX \
	-DCMAKE_C_COMPILER=$MPICC \
	-DCMAKE_Fortran_COMPILER=$MPIF90 \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DTPL_BLAS_LIBRARIES="${BLAS_LIB}" \
	-DTPL_LAPACK_LIBRARIES="${LAPACK_LIB}" \
	-DTPL_SCALAPACK_LIBRARIES="${SCALAPACK_LIB}"
make

cp pdqrdriver ../../
cd ../../
cp -r ../scalapack-driver .


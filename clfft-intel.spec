Name: clfft-intel
Version: b43cc61git  
Release: 1%{?dist}
Summary: clFFT for Intel processors using Beignet runtime on Fedora 24

License: Apache License, Version 2.0
URL: https://github.com/clMathLibraries/clFFT
Source0: https://github.com/clMathLibraries/clFFT/archive/master.zip 

BuildRequires: cmake
BuildRequires: beignet-devel
BuildRequires: fftw-devel 
BuildRequires: fftw-libs-single 
BuildRequires: fftw-libs-double
BuildRequires: boost-devel
BuildRequires: ocl-icd-devel
BuildRequires: boost-static

%description
clFFT is a library that can make use of GPUs to offload FFT subroutine libraries.
The version here is built using the Intel Beignet openCL runtime which will work on 
Intel CPUs with integrated GPUs.

%prep
rm -rf clFFT-master
unzip %{SOURCE0}

%build
cmake clFFT-master/src/ -DBUILD_TEST=off -DBUILD_CALLBACK_CLIENT=on -DBUILD_CLIENT=on \
 -DBUILD_EXAMPLES=off -DBUILD_RUNTIME=on -DBUILD_LOADLIBRARIES=on -DCMAKE_BUILD_TYPE=Debug \
 -DBOOST_LIBRARYDIR=/usr/local/lib64/
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
ctest -V %{?_smp_mflags}

%clean
rm -rf %{buildroot} 

%files
/usr/local/bin/clFFT-callback-client
/usr/local/bin/clFFT-callback-client-2.12.1
/usr/local/bin/clFFT-client
/usr/local/bin/clFFT-client-2.12.1
/usr/local/include/clAmdFft.h
/usr/local/include/clAmdFft.version.h
/usr/local/include/clFFT.h
/usr/local/include/clFFT.version.h
/usr/local/lib64/cmake/clFFT/clFFTConfig.cmake
/usr/local/lib64/cmake/clFFT/clFFTConfigVersion.cmake
/usr/local/lib64/cmake/clFFT/clFFTTargets-debug.cmake
/usr/local/lib64/cmake/clFFT/clFFTTargets.cmake
/usr/local/lib64/libStatTimer.so
/usr/local/lib64/libStatTimer.so.2
/usr/local/lib64/libStatTimer.so.2.12.1
/usr/local/lib64/libclFFT.so
/usr/local/lib64/libclFFT.so.2
/usr/local/lib64/libclFFT.so.2.12.1
/usr/local/lib64/pkgconfig/clFFT.pc

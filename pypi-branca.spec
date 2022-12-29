#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-branca
Version  : 0.6.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/bb/66/e3591bc59d0685668cf9bb451ed527b0c261cfa2afedbe72422442586ace/branca-0.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/66/e3591bc59d0685668cf9bb451ed527b0c261cfa2afedbe72422442586ace/branca-0.6.0.tar.gz
Summary  : Generate complex HTML+JS pages with Python
Group    : Development/Tools
License  : MIT
Requires: pypi-branca-python = %{version}-%{release}
Requires: pypi-branca-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jinja2)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![PyPI Package](https://img.shields.io/pypi/v/branca.svg)](https://pypi.python.org/pypi/branca)
[![Build Status](https://github.com/python-visualization/branca/actions/workflows/test_code.yml/badge.svg?branch=master)](https://github.com/python-visualization/branca/actions/workflows/test_code.yml)
[![Gitter](https://badges.gitter.im/python-visualization/folium.svg)](https://gitter.im/python-visualization/folium)

%package python
Summary: python components for the pypi-branca package.
Group: Default
Requires: pypi-branca-python3 = %{version}-%{release}

%description python
python components for the pypi-branca package.


%package python3
Summary: python3 components for the pypi-branca package.
Group: Default
Requires: python3-core
Provides: pypi(branca)
Requires: pypi(jinja2)

%description python3
python3 components for the pypi-branca package.


%prep
%setup -q -n branca-0.6.0
cd %{_builddir}/branca-0.6.0
pushd ..
cp -a branca-0.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672338490
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
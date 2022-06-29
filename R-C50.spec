#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-C50
Version  : 0.1.6
Release  : 8
URL      : https://cran.r-project.org/src/contrib/C50_0.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/C50_0.1.6.tar.gz
Summary  : C5.0 Decision Trees and Rule-Based Models
Group    : Development/Tools
License  : GPL-3.0
Requires: R-C50-lib = %{version}-%{release}
Requires: R-Cubist
Requires: R-partykit
BuildRequires : R-Cubist
BuildRequires : R-partykit
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-C50 package.
Group: Libraries

%description lib
lib components for the R-C50 package.


%prep
%setup -q -c -n C50
cd %{_builddir}/C50

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644183659

%install
export SOURCE_DATE_EPOCH=1644183659
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library C50
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library C50
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library C50
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc C50 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/C50/DESCRIPTION
/usr/lib64/R/library/C50/INDEX
/usr/lib64/R/library/C50/Meta/Rd.rds
/usr/lib64/R/library/C50/Meta/features.rds
/usr/lib64/R/library/C50/Meta/hsearch.rds
/usr/lib64/R/library/C50/Meta/links.rds
/usr/lib64/R/library/C50/Meta/nsInfo.rds
/usr/lib64/R/library/C50/Meta/package.rds
/usr/lib64/R/library/C50/Meta/vignette.rds
/usr/lib64/R/library/C50/NAMESPACE
/usr/lib64/R/library/C50/NEWS.md
/usr/lib64/R/library/C50/R/C50
/usr/lib64/R/library/C50/R/C50.rdb
/usr/lib64/R/library/C50/R/C50.rdx
/usr/lib64/R/library/C50/doc/C5.0.R
/usr/lib64/R/library/C50/doc/C5.0.Rmd
/usr/lib64/R/library/C50/doc/C5.0.html
/usr/lib64/R/library/C50/doc/Class_Probability_Calcs.R
/usr/lib64/R/library/C50/doc/Class_Probability_Calcs.Rmd
/usr/lib64/R/library/C50/doc/Class_Probability_Calcs.html
/usr/lib64/R/library/C50/doc/index.html
/usr/lib64/R/library/C50/help/AnIndex
/usr/lib64/R/library/C50/help/C50.rdb
/usr/lib64/R/library/C50/help/C50.rdx
/usr/lib64/R/library/C50/help/aliases.rds
/usr/lib64/R/library/C50/help/paths.rds
/usr/lib64/R/library/C50/html/00Index.html
/usr/lib64/R/library/C50/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/C50/libs/C50.so
/usr/lib64/R/library/C50/libs/C50.so.avx2
/usr/lib64/R/library/C50/libs/C50.so.avx512

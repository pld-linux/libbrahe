Summary:	A Heterogenous C Library of Numeric Functions
Name:		libbrahe
Version:	1.1.0
Release:	1
License:	GPL
Group:		Libraries
URL:		http://www.coyotegulch.com/products/brahe/
Source0:	http://www.coyotegulch.com/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	6b02428844db18f8c51e2857346fe132
Patch0:		%{name}-missing_libs.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brahe is where I put all sorts of useful mathematic functions that
don't seem to fit anywhere else. Among the bits and pieces here,
you'll find:
- A function, brahe_sigdig, that rounds floating-point values to a
  specific number of significant digits -- very useful in scientific and
  engineering applications.
- Several pseudorandom number generators, including the Marsenne
  Twister, various algorithms by Marsaglia, and ISAAC.
- Least common multiple and greatest common denominator functions.
- A few trigonometry functions for finding the inversions of
  hyperbolic sine, cosine, and tangent.

%package devel
Summary:	libbrahe headers and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libcoyotl libraries headers and documentation

%package static
Summary:	libbrahe static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
libbrahe static libraries

%prep
%setup -q
%patch -p0

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

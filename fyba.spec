Summary:	FYBA - library to read and write files in Norwegian geodata standard format SOSI
Summary(pl.UTF-8):	FYBA - biblioteka do odczytu i zapisu plików w norweskim formacie danych geograficznych SOSI
Name:		fyba
Version:	4.1.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/kartverket/fyba/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ab687582efdef26593796271529a10cb
Patch0:		%{name}-link.patch
URL:		https://github.com/kartverket/fyba
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenFYBA is the source code release of the FYBA library, distributed
by the National Mapping Authority of Norway (Statens kartverk) to read
and write files in the National geodata standard format SOSI. 

%description -l pl.UTF-8
OpenFYBA to mające otwarty kod źródłowy wydanie biblioteki FYBA
rozpowszechnianej przez Statens kartverk (norweską państwową
instytucję geodezyjną) w celu odczytu i zapisu plików w państwowym
formacie danych geograficznych SOSI.

%package devel
Summary:	Header files for FYBA libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek FYBA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for FYBA libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek FYBA.

%package static
Summary:	Static FYBA libraries
Summary(pl.UTF-8):	Statyczne biblioteki FYBA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FYBA libraries.

%description static -l pl.UTF-8
Statyczne biblioteki FYBA.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# keeping *.la: .pc file exists only for libfyba

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/fyba

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/en_EN
%lang(nb) %doc doc/no_NB
%attr(755,root,root) %{_libdir}/libfyba.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfyba.so.0
%attr(755,root,root) %{_libdir}/libfygm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfygm.so.0
%attr(755,root,root) %{_libdir}/libfyut.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfyut.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfyba.so
%attr(755,root,root) %{_libdir}/libfygm.so
%attr(755,root,root) %{_libdir}/libfyut.so
%{_libdir}/libfyba.la
%{_libdir}/libfygm.la
%{_libdir}/libfyut.la
%{_includedir}/fyba
%{_pkgconfigdir}/fyba.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfyba.a
%{_libdir}/libfygm.a
%{_libdir}/libfyut.a

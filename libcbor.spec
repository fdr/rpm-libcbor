Name:		libcbor
Version:	0.5.0
Release:	2%{?dist}
Summary:	A CBOR parsing library

Group:		System Environment/Libraries
License:	MIT
URL:		http://libcbor.org
Source0:	libcbor-%{version}.tar.gz

BuildRequires:	cmake, gcc, gcc-c++, python3-sphinx, python3-breathe

%description
libcbor is a C library for parsing and generating CBOR.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel contains libraries and header files for %{name}.

%prep
%setup -q

%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFFIX="/usr" ./


%build
%make_build cbor_shared
cd doc
make man


%install
%make_install 
mkdir -p %{buildroot}%{_mandir}/man1
cp doc/build/man/* %{buildroot}%{_mandir}/man1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%{_libdir}/libcbor.so.?
%{_libdir}/libcbor.so.?.?.?

%doc README.md
%{_mandir}/man1/libcbor.1.gz
%license LICENSE.md

%files devel
%{_includedir}/cbor.h
%{_includedir}/cbor/*.h
%{_includedir}/cbor/internal/*.h
%{_libdir}/libcbor.so
%{_libdir}/pkgconfig/libcbor.pc

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 19 2017 Marek Tamaskovic <mtamasko@redhat.com> 0.5.0-1
- Init package.


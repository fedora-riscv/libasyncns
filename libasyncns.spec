Name: libasyncns
Version: 0.7
Release: 1%{?dist}
Summary: Asynchronous Name Service Library
Group: System Environment/Libraries
Source0: http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
License: LGPLv2+
Url: http://0pointer.de/lennart/projects/libasyncns/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package devel
Summary: Development Files for libasyncns Client Development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development Files for libasyncns Client Development

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm -rf $RPM_BUILD_ROOT/usr/share/doc/libasyncns/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
* Tue Oct 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New release

* Fri Oct 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New release

* Sat Aug 23 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New release

* Sun Jul 27 2008 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- Initial packaging

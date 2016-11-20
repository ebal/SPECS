Name:           libsodium
Version:        1.0.11
Release:        1%{?dist}
Summary:        P(ortable|ackageable) NaCl-based crypto library
 
Group:          Development/Libraries
License:        GPLv2
URL:            http://libsodium.org
Source0:        https://github.com/jedisct1/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
 
%description
Sodium is a modern, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

It is a portable, cross-compilable, installable, packageable fork of NaCl, with a compatible API, and an extended API to improve usability even further.

Its goal is to provide all of the core operations needed to build higher-level cryptographic tools.

Sodium supports a variety of compilers and operating systems, including Windows (with MinGW or Visual Studio, x86 and x64), iOS and Android.
 
%prep
%setup -n %{name}-%{version} -q
 
%build
 
%configure --prefix=/usr
make %{?_smp_mflags}
 
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
 
%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE ChangeLog
%{_includedir}/sodium.h
%{_includedir}/sodium/*
%{_libdir}/%{name}*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Nov 20 2016 evaggelos balaskas <evaggelos _AT_ balaskas _DOT_ gr>
- *** Version 1.0.11 Stable ***

* Fri Oct 23 2015 Evaggelos Balaskas <Evaggelos _AT_ Balaskas _DOT_ GR> 
- *** Version 1.0.4 Stable ***

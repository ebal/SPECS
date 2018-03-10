Name:           libsodium
Version:        1.0.16
Release:        1%{?dist}
Summary:        P(ortable|ackageable) NaCl-based crypto library
 
Group:          Development/Libraries
License:        ISC
URL:            http://libsodium.org
Source0:        https://github.com/jedisct1/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
 
%description
Sodium is a new, easy-to-use software library for encryption, decryption, signatures, password hashing and more.

It is a portable, cross-compilable, installable, packageable fork of NaCl, with a compatible API, and an extended API to improve usability even further.

Its goal is to provide all of the core operations needed to build higher-level cryptographic tools.

Sodium supports a variety of compilers and operating systems, including Windows (with MingW or Visual Studio, x86 and x64), iOS, Android, as well as Javascript and Webassembly.
 
%prep
%setup -q


%build
%configure
make %{?_smp_mflags}

%install

%check
make check
 
%make_install

%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%doc
%{_includedir}/sodium.h
%{_includedir}/sodium/*
%{_libdir}/%{name}*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Mar 03 2018 evaggelos balaskas <evaggelos _AT_ balaskas _DOT_ gr>
- *** Version 1.0.16 Stable ***

* Sun Nov 20 2016 evaggelos balaskas <evaggelos _AT_ balaskas _DOT_ gr>
- *** Version 1.0.11 Stable ***

* Fri Oct 23 2015 Evaggelos Balaskas <Evaggelos _AT_ Balaskas _DOT_ GR> 
- *** Version 1.0.4 Stable ***

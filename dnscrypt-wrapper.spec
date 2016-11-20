Name:		dnscrypt-wrapper
Version:	v0.2.2
Release:	1%{?dist}
Summary:	dnscrypt-wrapper - A server-side dnscrypt proxy.

Group:		System Environment/Daemons
License:	GPLv2
URL:		http://dnscrypt.org/
Source0:	https://github.com/Cofyc/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	autoconf
Requires:		libevent-devel libsodium

%description
This is dnscrypt wrapper (server-side dnscrypt proxy), which helps to add dnscrypt support to any name resolver.

This software is modified from dnscrypt-proxy.

%prep
%setup -n %{name}-%{version} -q

%build
make configure

%configure --prefix=/usr
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_sbindir}
install -d -m 755  %{buildroot}/%{_sbindir}
install -p dnscrypt-wrapper %{buildroot}/%{_sbindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%doc

%changelog
* Sun Nov 20 2016 evaggelos balaskas <evaggelos _AT_ balaskas _DOT_ gr>
- *** Version 0.2.2 Stable ***

* Fri Oct 23 2015 Evaggelos Balaskas <Evaggelos _AT_ Balaskas _DOT_ GR>
- *** Version 0.1.17 Stable ***

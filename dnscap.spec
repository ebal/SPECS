Name:           dnscap
Version:        1.7.0
Release:        1%{?dist}
Summary:        network capture utility designed specifically for DNS traffic

Group:          System Environment/Daemons
License:        BSD 3
URL:            https://www.dns-oarc.net/tools/dnscap
Source0:        https://www.dns-oarc.net/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libpcap-devel ldns-devel openssl-devel bind-devel zlib-devel

%description
dnscap is a network capture utility designed specifically for DNS traffic. It produces binary data in pcap(3) and other format. This utility is similar to tcpdump(1), but has a number of features tailored to DNS transactions and protocol options. DNS-OARC uses dnscap for DITL data collections.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc CONTRIBUTORS LICENSE README.md
%{_libdir}/%{name}*
%{_mandir}/man1/dnscap.*
%{_bindir}/dnscap
%{_docdir}/dnscap/*


%changelog
* Mon Dec 18 2017 Evaggelos Balaskas <evaggelos[AT]balaskas[DOT]gr>
- *** Version 1.7.0 Stable ***

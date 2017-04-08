%define _name    Python

Name:       %{_name}27
Version:    2.7.13
Release:    1%{?dist}
Summary:    An interpreted, interactive, object-oriented programming language.

Group:      Development/Languages
License:    Python Software Foundation
URL:        https://www.python.org
Source0:    %{_name}-%{version}.tar.xz

BuildRequires: zlib-devel libxml2-devel openssl-devel

AutoReq:    no

%description
Python is an interpreted, interactive, object-oriented programming language

%prep
%setup -q -n %{_name}-%{version}


%build
%{_configure} \
    --prefix=/opt/%{_name}-%{version}
make %{?_smp_mflags}

%install
%make_install

%post
ln -sf /opt/%{_name}-%{version}/bin/python2.7 /usr/local/bin/python2

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{_name}-%{version}


%files
%doc
/opt/%{_name}-%{version}


%changelog
* Sat Apr 08 2017 ebal
- Custom RPM package for python 2.7.3


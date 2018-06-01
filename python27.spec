%define _name    Python

Name:		python
Version:	2.7.15
Release:	1%{?dist}
Summary:	An interpreted, interactive, object-oriented programming language

Group:		Development/Languages
License:	Python
URL:		https://www.python.org
Source0:	https://www.python.org/ftp/python/%{version}/%{_name}-%{version}.tgz

BuildRequires:	gcc gcc-c++
BuildRequires:	bzip2-devel glibc-devel openssl-devel zlib-devel expat-devel
BuildRequires:	sqlite-devel ncurses-devel readline-devel libxml2-devel
#Requires:	

AutoReq: no


%description
Python is a programming language that lets you work more quickly and integrate your systems more effectively.


%prep
#%setup -q
%setup -q -n Python-%{version}


%build
%{_configure} \
    --enable-shared \
    --prefix=/opt/%{_name}-%{version}

make %{?_smp_mflags}


%install

# ldconfig
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo /opt/%{_name}-%{version}/lib > %{buildroot}/etc/ld.so.conf.d/%{_name}-%{version}.conf

%make_install


%clean
rm -fr %{buildroot}


# Scriptlets
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc LICENSE README
/opt/%{_name}-%{version}
%config /etc/ld.so.conf.d/%{_name}-%{version}.conf


%changelog
* Fri Jun 01 2018 ebal
- Custom RPM package for python 2.7.15

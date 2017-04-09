%define _name dovecot
Name:           %{_name}22
Version:        2.2.28
Release:        1%{?dist}
Summary:        Secure imap and pop3 server

%define pigeonholever 0.4.17

Group:          System Environment/Daemons
License:        MIT and LGPLv2
URL:            http://www.dovecot.org
Source0:        http://www.dovecot.org/releases/2.2/%{_name}-%{version}%{?prever}.tar.gz
Source1:        http://pigeonhole.dovecot.org/releases/2.2/dovecot-2.2-pigeonhole-%{pigeonholever}.tar.gz

BuildRequires:  expat-devel libcap-devel openldap-devel openssl-devel pam-devel zlib-devel
Requires:       openssl


# Declare custom prefix 
%define _prefix /opt/dovecot-%{version}


# Filter out all files in _docdir from being scanned for requires/provides
%{?perl_default_filter}


%description
Dovecot is an IMAP server for Linux/UNIX-like systems, written with security primarily in mind. 
It also contains a small POP3 server. It supports mail in either of maildir or mbox formats.

%package pigeonhole
Requires: %{_name} = %{epoch}:%{version}-%{release}
Summary: Sieve and managesieve plug-in for dovecot
Group: System Environment/Daemons
License: MIT and LGPLv2


%description pigeonhole
This package provides sieve and managesieve plug-in for dovecot LDA.


%prep
%setup -q -D -a 1 -n %{_name}-%{version}


%build
%{_configure} \
    --prefix=%{_prefix}                \
    INSTALL_DATA="install -c -p -m644" \
    --disable-static                   \
    --disable-rpath                    \
    --with-nss                         \
    --with-shadow                      \
    --with-pam                         \
    --with-gssapi=plugin               \
    --with-zlib                        \
    --with-libcap                      \
    --with-ssl=openssl                 \
    --with-ldap                        \
    --without-docs

make %{?_smp_mflags}

# pigeonhole
pushd %{_name}-2*2-pigeonhole-%{pigeonholever}

%{_configure} \
        --prefix=%{_prefix}                \
        INSTALL_DATA="install -c -p -m644" \
        --disable-static                   \
        --with-dovecot=../                 \
        --without-unfinished-features

make %{?_smp_mflags}
popd

%install
#rm -rf $RPM_BUILD_ROOT
%make_install DESTDIR=$RPM_BUILD_ROOT

# pigeonhole
pushd %{_name}-2*2-pigeonhole-%{pigeonholever}
%make_install DESTDIR=$RPM_BUILD_ROOT
popd

# Install default dovecot configuration
mkdir -p $RPM_BUILD_ROOT%{_prefix}%{_sysconfdir}/dovecot/conf.d
# conf
install -p -m 644 %{_builddir}/%{_name}-%{version}/doc/example-config/*.conf $RPM_BUILD_ROOT%{_prefix}%{_sysconfdir}/dovecot/
install -p -m 644 %{_builddir}/%{_name}-%{version}/doc/example-config/*.conf.ext $RPM_BUILD_ROOT%{_prefix}%{_sysconfdir}/dovecot/
# conf.d
install -p -m 644 %{_builddir}/%{_name}-%{version}/doc/example-config/conf.d/*.conf $RPM_BUILD_ROOT%{_prefix}%{_sysconfdir}/dovecot/conf.d/
install -p -m 644 %{_builddir}/%{_name}-%{version}/doc/example-config/conf.d/*.conf.ext $RPM_BUILD_ROOT%{_prefix}%{_sysconfdir}/dovecot/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{_name}-%{version}

%files
%doc
/opt/dovecot-%{version}


%changelog
* Sat Apr 08 2017 ebal
- Custom RPM package for dovecot v2.2.28 and pigeonhole v0.4.17 



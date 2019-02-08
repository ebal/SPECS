%define dovecotver      2.2.36.1
%define pigeonholever   0.4.24.1

Name:           dovecot
Epoch:          1
Version:        %{dovecotver}
Release:        1%{?dist}
Summary:        Secure imap and pop3 server

Group:          System Environment/Daemons
License:        MIT and LGPLv2
URL:            http://www.dovecot.org
Source0:        http://www.dovecot.org/releases/2.2/%{name}-%{version}%{?prever}.tar.gz
Source1:        http://pigeonhole.dovecot.org/releases/2.2/dovecot-2.2-pigeonhole-%{pigeonholever}.tar.gz

BuildRequires:  libcap-devel openssl-devel openldap-devel pam-devel postgresql-devel mysql-devel sqlite-devel bzip2-devel xz-devel expat-devel
Requires:       gcc

%description
Dovecot is an IMAP server for Linux/UNIX-like systems, written with security primarily in mind.
It also contains a small POP3 server. It supports mail in either of maildir or mbox formats.

%package pigeonhole
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Sieve and managesieve plug-in for dovecot
Group: System Environment/Daemons
License: MIT and LGPLv2

%description pigeonhole
This package provides sieve and managesieve plug-in for dovecot LDA.

# Filter out all files in _docdir from being scanned for requires/provides
%{?perl_default_filter}

%prep
## %setup -q
%setup -q -D -a 1

%build
%configure                  \
    --enable-static         \
    --with-nss              \
    --with-pam              \
    --with-mysql            \
    --with-pgsql            \
    --with-sqlite           \
    --with-ssl=openssl      \
    --with-ssldir=/etc/ssl  \
    --with-gssapi           \
    --with-ldap=plugin      \
    --with-zlib             \
    --with-bzlib            \
    --with-lzma             \
    --with-libcap           \
    --with-solr             \
    --without-docs

make %{?_smp_mflags}

# pigeonhole
pushd %{name}-2*2-pigeonhole-%{pigeonholever}

%configure                         \
        --enable-static            \
        --with-dovecot=../         \
        --with-managesieve         \
        --with-ldap=yes            \
        --without-docs             \
        --without-unfinished-features

## ./configure --with-dovecot=../dovecot-2.2.36.1 --with-managesieve --with-ldap=yes --without-docs    --disable-static

make %{?_smp_mflags}

popd
# pigeonhole

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# pigeonhole
pushd %{name}-2*2-pigeonhole-%{pigeonholever}

%make_install DESTDIR=$RPM_BUILD_ROOT

popd
# pigeonhole

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%_bindir
%_sbindir
%_datadir
%_includedir
%_libexecdir
%_libdir
%doc
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
* Thu Feb 08 2019 Evaggelos Balaskas <github.com _AT_A disposable _DOT_ space>
- Custom RPM package that contains dovecot & pigeonhole/managesieve together.

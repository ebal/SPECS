# RPM Build Notes

```sh
# yum -y update
# yum -y install rpm-build
```

```sh
# cd /root/
# mkdir -pv ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
# yum -y install vim curl gcc make automake autoconf pkg-config
```

eg. 

```sh
# cd ~/rpmbuild/SPECS/

# curl -sLO https://raw.githubusercontent.com/ebal/SPECS/master/libsodium.spec
# curl -sLO https://raw.githubusercontent.com/ebal/SPECS/master/dnscrypt-wrapper.spec


# cd /root/rpmbuild/SOURCES/
# curl -sLO https://github.com/jedisct1/libsodium/releases/download/1.0.11/libsodium-1.0.11.tar.gz
# curl -sLO https://github.com/cofyc/dnscrypt-wrapper/releases/download/v0.2.2/dnscrypt-wrapper-v0.2.2.tar.bz2


# cd -
# vim libsodium.spec 
# rpmbuild --clean -ba libsodium.spec
# rpm -ivh /root/rpmbuild/RPMS/x86_64/libsodium-1.0.11-1.el7.centos.x86_64.rpm


# vim dnscrypt-wrapper.spec
# rpmbuild --clean -ba dnscrypt-wrapper.spec 
# rpm -ivh /root/rpmbuild/RPMS/x86_64/dnscrypt-wrapper-v0.2.2-1.el7.centos.x86_64.rpm 
```

## Defining Spec File Macros

### Built-in macros

#### RPM includes a host of built-in macros, including the following useful directories:

```
%_prefix /usr
%_exec_prefix %{_prefix}
%_bindir %{_exec_prefix}/bin
%_sbindir %{_exec_prefix}/sbin
%_libexecdir %{_exec_prefix}/libexec
%_datadir %{_prefix}/share
%_sysconfdir %{_prefix}/etc
%_sharedstatedir %{_prefix}/com
%_localstatedir %{_prefix}/var
%_libdir %{_exec_prefix}/lib
%_includedir %{_prefix}/include
%_oldincludedir /usr/include
%_infodir %{_prefix}/info
%_mandir %{_prefix}/man
```

#### The example directories shown above come from the standard RPM macro file, /usr/lib/rpm/macros, instead of the Red Hat-specific file, /usr/lib/rpm/redhat/macros, which holds:

```
%_prefix /usr
%_sysconfdir /etc
%_localstatedir /var
%_infodir /usr/share/info
%_mandir /usr/share/man
%_initrddir %{_sysconfdir}/rc.d/init.d
%_defaultdocdir %{_usr}/share/doc
```


Name:           tmux
Version:        2.9a
Release:        1%{?dist}
Summary:        A terminal multiplexer

Group:          Applications/System
License:        ISC
URL:            https://github.com/tmux
Source0:        https://github.com/tmux/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

# https://github.com/Bash-it/bash-it/blob/master/completion/available/bash-it.completion.bash
Source1:        bash-it.completion.bash

BuildRequires:  ncurses-devel
BuildRequires:  libevent2-devel

%description
tmux is a terminal multiplexer

%prep
%setup -q

%configure
make %{?_smp_mflags}

%install
%make_install

# bash completion
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/tmux.bash

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING
%{_bindir}/tmux
%{_mandir}/man1/tmux.1.*
%{_sysconfdir}/bash_completion.d/tmux.bash

%changelog
* Mon Aug 05 2019 Evaggelos Balaskas <evaggelos [_AT_] balaskas [_DOT_] gr>
- bump to tmux v2.9a

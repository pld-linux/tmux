# TODO:
# - vim doesn't detect filetype
#
# Conditional build:
%bcond_without	systemd		# without system integration

%define commit  e809c2ec359b0fd6151cf33929244b7a7d637119

Summary:	tmux - a terminal multiplexer
Summary(hu.UTF-8):	tmux egy terminál-sokszorozó
Summary(pl.UTF-8):	tmux - multiplekser terminali
Name:		tmux
Version:	3.5a
Release:	1
License:	ISC
Group:		Applications/Terminal
#Source0Download: https://github.com/tmux/tmux/releases
Source0:	https://github.com/tmux/tmux/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8419a3ccf6752db5dd30a664f3ca774e
Source1:	%{name}-filedetect.vim
Source2:	https://raw.githubusercontent.com/keith/tmux.vim/master/syntax/tmux.vim
# Source2-md5:	cd1169a1757b515b5c57816d339c6f72
Source3:	https://raw.githubusercontent.com/imomaliev/tmux-bash-completion/master/completions/tmux
# Source3-md5:	376dc7062c0e575ff98767747cb23554
Source4:	tmux@.service
URL:		http://tmux.github.io/
BuildRequires:	libevent-devel
BuildRequires:	libutempter-devel
BuildRequires:	ncurses-devel >= 5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
%{?with_systemd:BuildRequires:	systemd-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tmux is a terminal multiplexer: it enables a number of terminals (or
windows), each running a separate program, to be created, accessed,
and controlled from a single screen. tmux may be detached from a
screen and continue running in the background, then later reattached.

%description -l hu.UTF-8
tmux egy terminál-sokszorozó: terminálok (vagy ablakok) sokaságát
hozhatd létre, mindegyikben egy külön program fut, létrehozhatsz,
csatlakozhatsz és irányíthatod egyetlen képernyőről. tmux
lecsatlakozhat a képernyőről és folytathatja a futását a háttérben, és
később újracsatlakozhatsz.

%description -l pl.UTF-8
tmux to multiplekser terminali: pozwala na tworzenie wielu terminali
(lub okien) z osobnymi programami, dostęp do nich i sterowanie z
pojedynczego ekranu. tmux może być odłączony od ekranu i nadal działać
w tle, a następnie ponownie podłączony.

%package -n vim-syntax-tmux
Summary:	Vim syntax file to tmux config files
Summary(hu.UTF-8):	Vim syntax fájl a tmux konfigurációs fájljához
Summary(pl.UTF-8):	Plik składni Vima dla plików konfiguracyjnych tmuksa
Group:		Applications/Editors/Vim
Requires:	vim-rt

%description -n vim-syntax-tmux
Vim syntax file to tmux config files.

%description -n vim-syntax-tmux -l hu.UTF-8
Vim syntax fájl a tmux konfigurációs fájljához.

%package -n bash-completion-tmux
Summary:	Bash completion for tmux
Summary(pl.UTF-8):	Bashowe dopełnianie poleceń dla tmuksa
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-tmux
This package provides bash-completion for tmux.

%description -n bash-completion-tmux -l pl.UTF-8
Ten pakiet dostarcza bashowe dopełnianie składni dla polecenia tmux.

%prep
%setup -q

%build
[ ! -x configure ] && ./autogen.sh
# note: on Linux use plain glibc functions instead of utf8proc
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncursesw" \
	%{__enable_disable systemd}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{ftdetect,syntax}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect/tmux.vim
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -d $RPM_BUILD_ROOT%{bash_compdir}
sed -e '1s,#!/usr/bin/env bash,#!/bin/bash,' %{SOURCE3} > $RPM_BUILD_ROOT%{bash_compdir}/%{name}
install -d $RPM_BUILD_ROOT%{systemdunitdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{systemdunitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/tmux
%{_mandir}/man1/tmux.1*
%{systemdunitdir}/tmux@.service

%files -n vim-syntax-tmux
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/ftdetect/tmux.vim
%{_datadir}/vim/vimfiles/syntax/tmux.vim

%files -n bash-completion-tmux
%defattr(644,root,root,755)
%{bash_compdir}/%{name}

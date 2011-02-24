# TODO:
# - vim doesn't detect filetype
# - pass LDFLAGS (fix as-needed problem first)
Summary:	tmux is a terminal multiplexer
Summary(hu.UTF-8):	tmux egy terminál-sokszorozó
Name:		tmux
Version:	1.4
Release:	3
License:	BSD
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/tmux/%{name}-%{version}.tar.gz
# Source0-md5:	0bfc7dd9a5bab192406167589c716a21
Source1:	%{name}-filedetect.vim
Patch0:		%{name}-makefile.patch
BuildRequires:	libevent-devel
BuildRequires:	ncurses-devel
URL:		http://tmux.sourceforge.net/
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

%package -n vim-syntax-tmux
Summary:	Vim syntax file to tmux config files
Summary(hu.UTF-8):	Vim syntax fájl a tmux konfigurációs fájljához
Group:		Applications/Editors/Vim

%description -n vim-syntax-tmux
Vim syntax file to tmux config files.

%description -n vim-syntax-tmux -l hu.UTF-8
Vim syntax fájl a tmux konfigurációs fájljához.

%package -n bash-completion-tmux
Summary:	Bash completion for tmux
Group:		Applications/Shell
Requires:	bash-completion

%description -n bash-completion-tmux
This package provides bash-completion for tmux.

%prep
%setup -q
%patch0 -p1

%build
./configure
CFLAGS="%{rpmcppflags} %{rpmcflags} -I/usr/include/ncursesw" %{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/{ftdetect,syntax}
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/ftdetect/tmux.vim
install examples/tmux.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -d $RPM_BUILD_ROOT%{_datadir}/bash-completion
install examples/bash_completion_tmux.sh $RPM_BUILD_ROOT%{_datadir}/bash-completion/%{name}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
ln -s ../../%{_datadir}/bash-completion/%{name} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ NOTES TODO examples/*.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/tmux*

%files -n vim-syntax-tmux
%defattr(644,root,root,755)
%{_datadir}/vim/vimfiles/ftdetect/tmux.vim
%{_datadir}/vim/vimfiles/syntax/tmux.vim

%files -n bash-completion-tmux
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/%{name}
%{_datadir}/bash-completion/%{name}

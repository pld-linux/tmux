# TODO:
# - vim doesn't detect filetype
# - pass LDFLAGS (fix as-needed problem first)
Summary:	tmux is a terminal multiplexer
Summary(hu.UTF-8):	tmux egy terminál-sokszorozó
Name:		tmux
Version:	1.4
Release:	1
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

%prep
%setup -q
%patch0 -p1

%build
./configure
CFLAGS="%{rpmcflags} -I/usr/include/ncursesw" %{__make} \
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

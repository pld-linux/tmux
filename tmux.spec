Summary:	tmux is a terminal multiplexer
Summary(hu.UTF-8):	tmux egy terminál-sokszorozó
Name:		tmux
Version:	1.1
Release:	0.2
License:	BSD
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/tmux/%{name}-%{version}.tar.gz
# Source0-md5:	faf2fc52ac3ae63d899f6fece2c112cd
Source1:	%{name}-filedetect.vim
Patch0:		%{name}-makefile.patch
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

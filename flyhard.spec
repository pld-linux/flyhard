Summary:	Thrust clone
Summary(pl):	Klon gry Thrust
Name:		flyhard
Version:	0.3
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.markboyd.me.uk/games/flyhard/%{name}-%{version}.tar.gz
# Source0-md5:	97a94d94b3f59d5dc56fa17a02fd1663
URL:		http://www.markboyd.me.uk/games/flyhard/flyhard.html
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a game similar to Thrust - you pick things up with your ship,
carry them off, and drop them somewhere.

%description -l pl
Jest to gra podobna do gry Thrust - gracz unosi rzeczy swoim statkiem,
przesnosi je i gdzie¶ upuszcza.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

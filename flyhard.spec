Summary:	Thrust clone
Summary(pl.UTF-8):	Klon gry Thrust
Name:		flyhard
Version:	0.41
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.markboyd.me.uk/games/flyhard/%{name}-%{version}.tar.gz
# Source0-md5:	869bc989e346388b715a3a7479ab673e
Patch0:		%{name}-transform.patch
URL:		http://www.markboyd.me.uk/games/flyhard/flyhard.html
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a game similar to Thrust - you pick things up with your ship,
carry them off, and drop them somewhere.

%description -l pl.UTF-8
Jest to gra podobna do gry Thrust - gracz unosi rzeczy swoim statkiem,
przenosi je i gdzieś upuszcza.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's,\$(savedir),\$(DESTDIR)$(savedir),' src/Makefile.am

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

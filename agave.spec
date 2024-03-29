Summary:	Color scheme generator for GNOME
Summary(pl.UTF-8):	Generator schematów kolorów dla GNOME
Name:		agave
Version:	0.4.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	93097881f28dcae1eca2800a763f77c3
Patch0:		%{name}-g++.patch
Patch1:		%{name}-locale.patch
URL:		http://home.gna.org/colorscheme/
BuildRequires:	boost-devel
BuildRequires:	gconfmm-devel >= 2.12.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtkmm-devel >= 2.6.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglademm-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Have you ever been re-finishing a room in your home and found yourself
asking "What color would go well with this"? Or been working on a new
website and not been able to find colors that go well with eachother?

Try Agave. Agave is a very simple application for the GNOME desktop
that allows you to generate a variety of colorschemes from a single
starting color. It is free software licensed under the open-source GPL
License.

%description -l pl.UTF-8
Czy wykańczałeś kiedyś pokój w domu i zacząłeś zastanawiać się, jaki
kolor pasowałby najbardziej? Albo pracowałeś nad nową stroną nie mogąc
znaleźć pasujących kolorów?

Wypróbuj Agave. Jest to bardzo prosta aplikacja dla środowiska GNOME
pozwalająca generować różnorodne schematy kolorów poczynając od
jednego koloru początkowego. Jest to program wolnodostępny na licencji
GPL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
mv po/es{_ES,}.po
sed -i -e 's,-icon,,' data/%{name}.desktop.in.in


%build
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/agave
%dir %{_datadir}/agave
%dir %{_datadir}/agave/palettes
%{_datadir}/agave/palettes/*.gpl
%dir %{_datadir}/agave/pixmaps
%{_datadir}/agave/pixmaps/*.png
%dir %{_datadir}/agave/ui
%{_datadir}/agave/ui/agave.glade
%{_datadir}/agave/ui/agave.ui
%{_datadir}/agave/ui/bookmarkspopup.ui
%{_datadir}/omf/agave
%{_desktopdir}/agave.desktop
%{_iconsdir}/hicolor/*/apps/agave.*
%{_sysconfdir}/gconf/schemas/agave.schemas

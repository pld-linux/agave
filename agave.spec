Summary:	Color scheme generator for GNOME
Summary(pl.UTF-8):	Generator schematów kolorów dla GNOME
Name:		agave
Version:	0.4.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	e038138eff31a5286e1e41ac0e3b0f04
Patch0:	%{name}-locale.patch
URL:		http://home.gna.org/colorscheme/
BuildRequires:	gconfmm-devel >= 2.12.0
BuildRequires:	gtkmm-devel >= 2.6.0
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
mv po/es{_ES,}.po

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/agave/ui/agave.ui
%{_datadir}/agave/ui/bookmarkspopup.ui
%{_desktopdir}/agave.desktop
%{_iconsdir}/hicolor/48x48/apps/agave-icon.png
%{_iconsdir}/hicolor/scalable/apps/agave-icon.svg

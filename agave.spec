#
Summary:	Color scheme generator for GNOME
Name:		agave
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	88a4f89acb62eab906b26803a760d7de
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang agave

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO ChangeLog
%attr(755,root,root) %{_bindir}/agave
%{_datadir}/agave/palettes/Tango-Palette.gpl
%{_datadir}/agave/palettes/Visibone.gpl
%{_datadir}/agave/palettes/Web.gpl
%{_datadir}/agave/palettes/Ximian-Palette.gpl
%{_datadir}/agave/pixmaps/darken.png
%{_datadir}/agave/pixmaps/desaturate.png
%{_datadir}/agave/pixmaps/lighten.png
%{_datadir}/agave/pixmaps/saturate.png
%{_datadir}/agave/ui/agave.ui
%{_datadir}/agave/ui/bookmarkspopup.ui
%{_desktopdir}/agave.desktop
%{_iconsdir}/hicolor/48x48/apps/agave-icon.png
%{_iconsdir}/hicolor/scalable/apps/agave-icon.svg

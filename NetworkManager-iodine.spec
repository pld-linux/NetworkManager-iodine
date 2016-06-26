Summary:	NetworkManager VPN integration for iodine
Summary(pl.UTF-8):	Integracja NetworkManagera z iodine
Name:		NetworkManager-iodine
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-iodine/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	8753cc831435c21796035034fe16dc91
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	NetworkManager-gtk-lib >= 1.2.0
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= 2.0
Requires:	gtk+3 >= 3.0
Requires:	iodine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for iodine.

%description -l pl.UTF-8
Integracja NetworkManagera z iodine.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

# drop old gnome-shell support
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/VPN/*.name

%find_lang NetworkManager-iodine

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-iodine.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-iodine-properties.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-iodine.so
%attr(755,root,root) %{_libdir}/nm-iodine-auth-dialog
%attr(755,root,root) %{_libdir}/nm-iodine-service
%{_prefix}/lib/NetworkManager/VPN/nm-iodine-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-iodine-service.conf
%{_datadir}/appdata/network-manager-iodine.appdata.xml
%dir %{_datadir}/gnome-vpn-properties/iodine
%{_datadir}/gnome-vpn-properties/iodine/nm-iodine-dialog.ui

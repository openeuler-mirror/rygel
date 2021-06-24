Name:          rygel
Version:       0.40.1
Release:       1
Summary:       A media solution can easily share audio, video and pictures, and media player controler

License:       LGPLv2+
URL:           https://wiki.gnome.org/Projects/Rygel
Source0:       https://download.gnome.org/sources/%{name}/0.40/%{name}-%{version}.tar.xz

BuildRequires: dbus-glib-devel desktop-file-utils docbook-style-xsl gettext gobject-introspection-devel
BuildRequires: gst-editing-services-devel gstreamer1-devel gstreamer1-plugins-base-devel gtk-doc gtk3-devel
BuildRequires: gupnp-devel gupnp-av-devel gupnp-dlna-devel libgee-devel libmediaart-devel libsoup-devel
BuildRequires: libunistring-devel libuuid-devel meson sqlite-devel systemd-devel tracker-devel vala
BuildRequires: libmediaart-help libxslt

Provides:   %{name}-tracker = %{version}-%{release}
Obsoletes:  %{name}-tracker < %{version}-%{release}

%description
Rygel is a home media solution that allows you to easily share audio, video and
pictures, and control of media player on your home network. In technical terms
it is both a UPnP AV MediaServer and MediaRenderer implemented through a plug-in
mechanism. Interoperability with other devices in the market is achieved by
conformance to very strict requirements of DLNA and on the fly conversion of
media to format that client devices are capable of handling.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package_help

%prep
%setup -q

%build
%meson \
  -Dapi-docs=true \
  -Dexamples=false
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/rygel-preferences.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS TODO
%config(noreplace) %{_sysconfdir}/rygel.conf
%{_bindir}/rygel*
%{_libdir}/girepository-1.0/*
%{_libdir}/librygel-core-2.6.so.*
%{_libdir}/librygel-db-2.6.so.*
%{_libdir}/librygel-renderer-2.6.so.*
%{_libdir}/librygel-renderer-gst-2.6.so.*
%{_libdir}/librygel-ruih-2.0.so.*
%{_libdir}/librygel-server-2.6.so.*
%{_libdir}/rygel-2.6/*
%{_libexecdir}/rygel/
%{_datadir}/rygel/
%{_datadir}/applications/rygel*
%{_datadir}/dbus-1/services/org.gnome.Rygel1.service
%{_datadir}/icons/hicolor/*
%{_userunitdir}/rygel.service

%files devel
%{_includedir}/rygel-2.6
%{_libdir}/librygel-core-2.6.so
%{_libdir}/librygel-db-2.6.so
%{_libdir}/librygel-renderer-2.6.so
%{_libdir}/librygel-renderer-gst-2.6.so
%{_libdir}/librygel-ruih-2.0.so
%{_libdir}/librygel-server-2.6.so
%{_libdir}/pkgconfig/rygel*.pc
%{_datadir}/gir-1.0/*
%{_datadir}/vala/vapi/*

%files help
%doc %{_datadir}/gtk-doc/html/librygel*
%{_mandir}/man1/rygel.1*
%{_mandir}/man5/rygel.conf.5*

%changelog
* Wed Jun 23 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 0.40.1-1
- Package init with version 0.40.1

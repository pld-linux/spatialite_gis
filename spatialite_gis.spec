Summary:	Minimalistic GIS tool built on top of SpatiaLite and RasterLite
Summary(pl.UTF-8):	Minimalistyczne narzędzie GIS stworzone w oparciu o SpatiaLite i RasterLite
Name:		spatialite_gis
Version:	1.0.0c
Release:	2
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-gis-sources/%{name}-%{version}.tar.gz
# Source0-md5:	81de8d7f3e20038bd2ec721edc02dfb0
URL:		https://www.gaia-gis.it/fossil/spatialite_gis
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	libgeotiff-devel
BuildRequires:	libharu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librasterlite-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	wxGTK2-unicode-devel >= 2.8.12-4
BuildRequires:	zlib-devel
Requires:	wxGTK2-unicode >= 2.8.12-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimalistic GIS tool built on top of SpatiaLite and RasterLite.

%description -l pl.UTF-8
Minimalistyczne narzędzie GIS stworzone w oparciu o SpatiaLite i
RasterLite.

%prep
%setup -q

mkdir wx-bin
ln -sf /usr/bin/wx-gtk2-unicode-config wx-bin/wx-config

%build
# configure refers to wx-config with no option to override
PATH=$(pwd)/wx-bin:$PATH
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
sed -ne '2,$p' gnome_resource/spatialite-gis.desktop >$RPM_BUILD_ROOT%{_desktopdir}/spatialite-gis.desktop
cp -p gnome_resource/spatialite-gis.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/spatialite_gis
%{_desktopdir}/spatialite-gis.desktop
%{_pixmapsdir}/spatialite-gis.png

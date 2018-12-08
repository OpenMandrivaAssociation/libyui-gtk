%define major 8
%define libname %mklibname  yui %{major}-gtk
%define develname %mklibname yui-gtk -d

Name:		libyui-gtk
Version:	2.44.9
Release:	1
Summary:	UI abstraction library - GTK plugin
License:	LGPLv2+
Group:		System/Libraries
URL:		https://github.com/libyui/libyui-gtk
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	boost-devel
BuildRequires:	sane-devel
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen
BuildRequires:	ghostscript
BuildRequires:	graphviz

Requires:	libyui
Requires:	gtk+3.0
Requires:	gdk-pixbuf2.0
Requires:	pygtk2.0

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-gtk = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-gtk.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/Other
Requires:	libyui-devel
Requires:	%{libname} = %{EVRD}
Provides:	yui-gtk-devel = %{EVRD}

%description -n %{develname}
This package provides headers files for libyui-ncurses development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/pkgconfig/libyui-gtk.pc
%{_libdir}/cmake/libyui-gtk
%doc %{_docdir}/libyui-gtk%{major}

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -DENABLE_WERROR=0 \
    -DENABLE_DEBUG=1 \
    -DINSTALL_DOCS=yes \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -G Ninja

%ninja_build
%ninja_build docs

%install
%ninja_install -C build

find "%{buildroot}" -name "*.la" -delete

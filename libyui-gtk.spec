%define major 16
%define oldlibname %mklibname  yui 15-gtk
%define libname %mklibname  yui-gtk
%define develname %mklibname yui-gtk -d

Name:		libyui-gtk
Version:	2.52.5
Release:	3
Summary:	UI abstraction library - GTK plugin
License:	LGPLv2+
Group:		System/Libraries
URL:		https://github.com/libyui/libyui-gtk
Source0:	https://github.com/libyui/libyui-gtk/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
Patch0:		override-protection-of-YDIALOG-object.patch

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(sane-backends)
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
%rename %{oldlibname}

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
%doc COPYING.lgpl-2.1 COPYING.lgpl-3 HACKING README MAINTAINER TODO

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build

%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -DENABLE_WERROR=0 \
    -DENABLE_DEBUG=1 \
    -DINSTALL_DOCS=yes \
    -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
    -DWERROR=no \
    -G Ninja

%ninja_build


%install
%ninja_install -C build

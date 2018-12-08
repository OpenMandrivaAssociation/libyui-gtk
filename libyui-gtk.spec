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

Patch10:	https://github.com/besser82/libyui-gtk/commit/cc3ac74b1186b33bd9e6dcd532e189b5b4cb29bb.patch#/libyui-gtk-2.44.9-fix_misleading_indentation.patch
Patch11:	https://github.com/besser82/libyui-gtk/commit/5077aae7d96d607d96600a38484384ca8e5a0dee.patch#/libyui-gtk-2.44.9-fix_gtk_style_context_get_background_color.patch
Patch12:	https://github.com/besser82/libyui-gtk/commit/e48985c2384ee09fe60fd06003b013e90c94205a.patch#/libyui-gtk-2.44.9-fix_gtk_container_set_resize_mode.patch
Patch13:	https://github.com/besser82/libyui-gtk/commit/21ecc082bdf5628b91bb844e6993de4789e5d15d.patch#/libyui-gtk-2.44.9-fix_gtk_window_set_has_resize_grip.patch
Patch14:	https://github.com/besser82/libyui-gtk/commit/2c5c33d978b95bc9dd7613ddfc61810fa42c2ec8.patch#/libyui-gtk-2.44.9-fix_gtk_misc_set_alignment.patch
Patch15:	https://github.com/besser82/libyui-gtk/commit/a7b7b50c21f6e59b1325143dcbdf8555d4027804.patch#/libyui-gtk-2.44.9-fix_gtk_misc_set_padding.patch
Patch16:	https://github.com/besser82/libyui-gtk/commit/8ab57a0d462e3d65859cd56bcd1b73eacba9740d.patch#/libyui-gtk-2.44.9-fix_gtk_alignment_set_padding.patch
Patch17:	https://github.com/besser82/libyui-gtk/commit/d963977c528dc694f06ecd52a47c7f2129e1aca0.patch#/libyui-gtk-2.44.9-fix_gtk_alignment_new.patch
Patch18:	https://github.com/besser82/libyui-gtk/commit/7f6cc848f21e9f76c7247e46e934c80c339a0371.patch#/libyui-gtk-2.44.9-fix_gdk_cursor_new.patch
Patch19:	https://github.com/besser82/libyui-gtk/commit/11884a67cf26ed46e967dca9dee5e6fa32eb92b6.patch#/libyui-gtk-2.44.9-fix_gtk_widget_get_root_window.patch
Patch20:	https://github.com/besser82/libyui-gtk/commit/1191d564180b0a2ca489fdc762c302cc65a8c876.patch#/libyui-gtk-2.44.9-fix_gtk_menu_popup.patch
Patch21:	https://github.com/besser82/libyui-gtk/commit/355cbac51273f87b68e19430f591cee2c16766ed.patch#/libyui-gtk-2.44.9-fix_gtk_tree_view_set_rules_hint.patch
Patch22:	https://github.com/besser82/libyui-gtk/commit/509292d88c1cf4bf198aab2d7e5e5d075f301722.patch#/libyui-gtk-2.44.9-fix_gtk_arrow_new.patch
Patch23:	https://github.com/besser82/libyui-gtk/commit/a7eb80016ca13d33872b558cdb00eac353b3cde1.patch#/libyui-gtk-2.44.9-fix_display_get_device_manager_gdk_device_manager_get_client_pointer.patch

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

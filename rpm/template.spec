%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rtt-shape-msgs
Version:        2.10.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rtt_shape_msgs package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-rtt-geometry-msgs
Requires:       ros-noetic-rtt-roscomm
Requires:       ros-noetic-rtt-std-msgs
Requires:       ros-noetic-shape-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-rtt-geometry-msgs
BuildRequires:  ros-noetic-rtt-roscomm
BuildRequires:  ros-noetic-rtt-std-msgs
BuildRequires:  ros-noetic-shape-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Provides an rtt typekit for ROS shape_msgs messages. It allows you to use ROS
messages transparently in RTT components and applications. This package was
automatically generated by the create_rtt_msgs generator and should not be
manually modified. See the http://ros.org/wiki/shape_msgs documentation for the
documentation of the ROS messages in this typekit.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Jan 04 2021 Orocos Developers <orocos-dev@orocos.org> - 2.10.0-1
- Autogenerated by Bloom


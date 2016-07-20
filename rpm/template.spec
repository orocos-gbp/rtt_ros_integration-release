Name:           ros-indigo-rtt-tf
Version:        2.8.3
Release:        0%{?dist}
Summary:        ROS rtt_tf package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/rtt_ros_integration
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rtt
Requires:       ros-indigo-rtt-geometry-msgs
Requires:       ros-indigo-rtt-roscomm
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rtt
BuildRequires:  ros-indigo-rtt-geometry-msgs
BuildRequires:  ros-indigo-rtt-roscomm
BuildRequires:  ros-indigo-tf

%description
This package contains the components of the rtt_tf package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jul 20 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.3-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.1-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-0
- Autogenerated by Bloom


Name:           ros-indigo-rtt-visualization-msgs
Version:        2.8.6
Release:        0%{?dist}
Summary:        ROS rtt_visualization_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rtt-geometry-msgs
Requires:       ros-indigo-rtt-roscomm
Requires:       ros-indigo-rtt-std-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rtt-geometry-msgs
BuildRequires:  ros-indigo-rtt-roscomm
BuildRequires:  ros-indigo-rtt-std-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
Provides an rtt typekit for ROS visualization_msgs messages. It allows you to
use ROS messages transparently in RTT components and applications. This package
was automatically generated by the create_rtt_msgs generator and should not be
manually modified. See the http://ros.org/wiki/visualization_msgs documentation
for the documentation of the ROS messages in this typekit.

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
* Thu Nov 16 2017 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.6-0
- Autogenerated by Bloom

* Tue Mar 28 2017 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.5-0
- Autogenerated by Bloom

* Sat Nov 26 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.4-0
- Autogenerated by Bloom

* Wed Jul 20 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.3-0
- Autogenerated by Bloom

* Fri Jun 12 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.1-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.0-0
- Autogenerated by Bloom


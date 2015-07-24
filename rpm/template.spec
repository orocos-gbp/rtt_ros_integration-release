Name:           ros-jade-rtt-ros-integration
Version:        2.8.2
Release:        0%{?dist}
Summary:        ROS rtt_ros_integration package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/rtt_ros_integration
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rtt-actionlib
Requires:       ros-jade-rtt-dynamic-reconfigure
Requires:       ros-jade-rtt-ros
Requires:       ros-jade-rtt-ros-msgs
Requires:       ros-jade-rtt-rosclock
Requires:       ros-jade-rtt-roscomm
Requires:       ros-jade-rtt-rosdeployment
Requires:       ros-jade-rtt-rosnode
Requires:       ros-jade-rtt-rospack
Requires:       ros-jade-rtt-rosparam
Requires:       ros-jade-rtt-tf
BuildRequires:  ros-jade-catkin

%description
This stack contains all software necessary to build systems using both Orocos
and ROS infrastructures

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jul 24 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom


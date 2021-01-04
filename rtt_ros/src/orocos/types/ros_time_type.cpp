/*
 * (C) 2010, Steven Bellens, steven.bellens@mech.kuleuven.be
 * Department of Mechanical Engineering,
 * Katholieke Universiteit Leuven, Belgium.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the copyright holder nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include "ros_primitives_typekit_plugin.hpp"

namespace boost {
	namespace serialization {
		template<class Archive>
			void serialize( Archive & a, ros::Time & t, unsigned int) {
				using boost::serialization::make_nvp;
				a & make_nvp("sec", t.sec);
				a & make_nvp("nsec", t.nsec);
			}

		template<class Archive>
			void serialize( Archive & a, ros::Duration & t, unsigned int) {
				using boost::serialization::make_nvp;
				a & make_nvp("sec", t.sec);
				a & make_nvp("nsec", t.nsec);
			}
	}
}


namespace ros_integration{
    using namespace RTT;
    using namespace RTT::types;

    // This class works around the ROS time representation.
    class RosTimeTypeInfo : public types::StructTypeInfo<ros::Time>
    {
    public:
        RosTimeTypeInfo() : types::StructTypeInfo<ros::Time>("time") {}
    };

    // This class works around the ROS time representation.
    class RosDurationTypeInfo : public types::StructTypeInfo<ros::Duration>
    {
    public:
        RosDurationTypeInfo() : types::StructTypeInfo<ros::Duration>("duration") {}
    };

  void loadTimeTypes(){
	     RTT::types::Types()->addType( new RosTimeTypeInfo );
	     RTT::types::Types()->addType( new RosDurationTypeInfo );
  }
}

cmake_minimum_required(VERSION 2.8.3)
project(youbot_gazebo_robot)
find_package(catkin REQUIRED
   roscpp
   rospy
   std_msgs
   message_generation
)

catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...)

add_message_files(
  FILES
  e_start.msg
)

install(DIRECTORY launch/ DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch)

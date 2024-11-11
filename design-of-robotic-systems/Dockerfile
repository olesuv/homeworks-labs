# ROS melodic
FROM osrf/ros:melodic-desktop-full-bionic

# Using bash instead of sh to be able to source
ENV TERM xterm

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Update ROS packages and install Catkin
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y ros-melodic-catkin python-catkin-tools

RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
RUN mkdir -p ./catkin_ws/src  && \
    cd ./catkin_ws/  && \
    source /opt/ros/melodic/setup.bash  && \
    catkin init

# Install other libraries
RUN apt-get install -y python-scipy 

CMD ["bash"]


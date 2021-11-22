#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Email : im_caimingxue@163.com
# @github : https://github.com/caimingxue/magnetic-robot-simulation
# @notice ：
from color_tracker.utils.communication import TCP_Communication
import time

tcp_client = TCP_Communication()

def senddata2labview(x_pixel, y_pixel):

    x_world, y_world = image2world(x_pixel, y_pixel)

    mag_frequency = 2.0
    mag_direction = 90.
    mag_pitch = 90.
    mag_conical = 45.
    arm_position_x = 60.
    arm_position_y = 60.
    arm_position_z = 60.
    coil_a_angle = 45.
    coil_b_angle = 45.
    coil_c_angle = 45.


    robomag_data = [2.0, 2.0, 90.0, 90.0, 2.0, 2.0, 30.0, 60.0, 60.0, 60.0, 45.0, 45.0, 45.0]
    tcp_client.send(robomag_data)
    time.sleep(0.5)

def image2world(x_pixel, y_pixel):
    pass

# void mapToWorld(unsigned int mx, unsigned int my, double& wx, double& wy, nav_messages::OccupancyGrid& map)
# {//+0.5 为了去除边界，防止计算到地图外面，(这里map 是指像素坐标系，单位为int，
# //world 是指/map世界坐标系)
# 	wx = map.info.origin.position.x + (mx + 0.5) * map.info.resolution;
# 	wy = map.info.origin.position.y + (my + 0.5) * map.info.resolution;
#
# }
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Email : im_caimingxue@163.com
# @github : https://github.com/caimingxue/magnetic-robot-simulation
# @notice ：
from color_tracker.utils.communication import TCP_Communication
import time
import numpy as np

tcp_client = TCP_Communication()

def senddata2labview(robot_position_in_pixel):
    robot_position_in_world = image2world(robot_position_in_pixel)

    mag_strength = 4.0
    mag_frequency = 4.0
    mag_pitch = 90.
    mag_direction = 90.
    mag_conical = 50.

    target_x = robot_position_in_world[0]
    target_y = robot_position_in_world[1]
    target_z = 30.
    dist_coila_target = 60
    dist_coilb_target = 60
    dist_coilc_target = 60
    coil_a_angle = 45.
    coil_b_angle = 45.
    coil_c_angle = 45.

    robomag_data = [mag_strength, mag_frequency, mag_pitch, mag_direction, mag_conical,
                    target_x, target_y, target_z, dist_coila_target, dist_coilb_target,
                    dist_coilc_target, coil_a_angle, coil_b_angle, coil_c_angle]
    tcp_client.send(robomag_data)
    time.sleep(0.1)

def image2world(robot_position_in_pixel):
    resolution_x = 176 / 640
    resolution_y = 130 / 480

    world_x = (robot_position_in_pixel[0] - 330) * resolution_x
    world_y = -(robot_position_in_pixel[1] - 232) * resolution_y

    world_point = np.array([world_x, world_y])
    print("===============================================================", world_point)
    return world_point


# void mapToWorld(unsigned int mx, unsigned int my, double& wx, double& wy, nav_messages::OccupancyGrid& map)
# {//+0.5 为了去除边界，防止计算到地图外面，(这里map 是指像素坐标系，单位为int，
# //world 是指/map世界坐标系)
# 	wx = map.info.origin.position.x + (mx + 0.5) * map.info.resolution;
# 	wy = map.info.origin.position.y + (my + 0.5) * map.info.resolution;
#
# }
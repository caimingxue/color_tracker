#!/usr/bin/env python
# -*- coding: utf-8 -*-
  dcdfr c                       fff# @Email : im_caimingxue@163.com
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
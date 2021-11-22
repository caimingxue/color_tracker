#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : Communication.py
# @Time : 2021/11/5 11:20 上午
# @Author : Mingxue Cai
# @Email : im_caimingxue@163.com
# @github : https://github.com/caimingxue/magnetic-robot-simulation
# @notice ：

from math import *
import numpy as np
import struct
from TCP import TCPClient
from Ping import *
import time


class TCP_Communication(object):
    def __init__(self):
        self.client = TCPClient('192.168.17.130', 8080)
        # # if self.client.close():
        # # 	print(" TCP Commu. unsuccess")
        if self.client.connect():
            print(" TCP Commu. success")

    def send(self, data):
        Head = bytes.fromhex('55 AA 99 11')

        data_Byte_1 = struct.pack(">f", data[0])
        data_Byte_2 = struct.pack(">f", data[1])
        data_Byte_3 = struct.pack(">f", data[2])
        data_Byte_4 = struct.pack(">f", data[3])
        data_Byte_5 = struct.pack(">f", data[4])
        data_Byte_6 = struct.pack(">f", data[5])
        data_Byte_7 = struct.pack(">f", data[6])
        data_Byte_8 = struct.pack(">f", data[7])
        data_Byte_9 = struct.pack(">f", data[8])
        data_Byte_10 = struct.pack(">f", data[9])
        data_Byte_11 = struct.pack(">f", data[10])
        data_Byte_12 = struct.pack(">f", data[11])
        data_Byte_13 = struct.pack(">f", data[12])

        _CommandEnd = bytes.fromhex('AA BB CC DD')
        DATA = bytes()
        DATA = bytes().join([Head, data_Byte_1, data_Byte_2, data_Byte_3, data_Byte_4, data_Byte_5, data_Byte_6, data_Byte_7,
                             data_Byte_8, data_Byte_9, data_Byte_10, data_Byte_11, data_Byte_12, data_Byte_13, _CommandEnd])
        self.client.sendBytes(DATA)

def main():
    Robot = TCP_Communication()
    time.sleep(5)

    n = 0
    while n < 100:
        magData = [2.0, 2.0, 90.0, 90.0, 2.0, 2.0, 30.0, 60.0, 60.0, 60.0, 45.0, 45.0, 45.0]
        Robot.send(magData)
        time.sleep(0.5)
        n = n + 1
    Robot.client.close()

if __name__ == "__main__":
    main()

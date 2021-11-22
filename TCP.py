#!/usr/bin/env python
# coding:utf-8
import socket
import time

__author__ = "Mingxue Cai"

class TCPClient(object):
    attempts = 3
    def __init__(self, server, server_port, sock=None):
        self.host = server
        self.port = server_port
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self):

        try:
            self.sock.connect((self.host, self.port))
        except socket.error as e:
            # We show the error and tries to connect again (3 attempts)
            TCPClient.attempts -= 1
            print
            e
            while TCPClient.attempts > 0:
                self.sock.connect()
            self.sock.close()
        else:
            print ("Congratulation! Connection successful")
            return 1

    def recv(self):
        if self.sock:
            try:
                data = self.sock.recv(1024)
                # data = data.decode()  #在客户端接收到的数据是bytes字节码，要先转换为字符串
            except socket.error as e:
                print("%s" % (e))
            else:
                return data

    def send(self, msg):
        if self.sock:
            data = self.sock.sendall(msg)  #tcp_client.send(msg.encode('utf-8'))
            # if data is None:
            #     print("%s bytes of data sent" % (len(msg)))
            # else:
            #     return 0

    def sendBytes(self, msg):
        byteData = msg
        if self.sock:
            data = self.sock.sendall(byteData)
        # if data is None:
        #     print("data sent:"+str(byteData))

    def close(self):
        self.sock.close()




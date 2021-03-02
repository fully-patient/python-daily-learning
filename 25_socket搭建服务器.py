#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/24 20:47
# @Author  : he.dongdong
# @Site    : 
# @File    : 25_socket搭建服务器.py
# @Software: PyCharm


# 模拟web的流程，这里只是简单模拟客户端和服务器端的连接

# https://www.runoob.com/python/python-socket.html

# udp和tcp：
#   tcp三次握手和四次挥手：两边都需要确认
#   tcp和ip区别，osi七层(应用表示会话传输网络数据物理)，ip是网络层，tcp是传输层
# UDP：邮箱投递方式(不管在不在线)
# TCP：稳定可靠的传输协议：
#           发送应答机制(每次都确认)
#           超时重传
#           错误校验--->MD5编码
#           流量控制和阻塞管理

# socket是进程(程序)之间的通信工具

# TCP开发流程：
#       TCP服务器
#       TCP客户端

# 细节：两次阻塞，两种套接字
# osi的七层模型


# 创建服务器：
import socket

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_l = socket.gethostname()
socket_server.bind((host_l,9099))

socket_server.listen(128)
while True:
    client,address = socket_server.accept()   # 如果没有，会阻塞
    data = client.recv(1024)
    print(data.decode('utf8'))

    # 发送
    client.send('test'.encode('utf-8'))
    client.close()
else:
    socket_server.close()   # 服务器关闭


# 创建客户端：
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建 socket 对象
host_r = socket.gethostname()  # 获取本地主机名
port = 9099  # 设置端口号

s.connect((host, port))
str_a = s.recv(1024)
print(str_a.decode('utf8'))
s.close()


# web服务器原理是啥？其实就是从data入手，对请求和相应进行过滤





if __name__ == "__main__":
    pass
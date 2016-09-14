#!/usr/bin/env python
#-*-coding:utf-8-*-
# 服务端

import socket
server = socket.socket()
server.bind(('localhost',6969))
server.listen()

print("开始等电话……")
conn,addr = server.accept()
# print(conn,addr)
while True:
    print("电话来了！！！！")
    data = conn.recv(1024)
    # if str(data,encoding='utf8') == "exit":break
    print("Recv:",data)
    conn.send(data.upper())

server.close()
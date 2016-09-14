#!/usr/bin/env python
#-*-coding:utf-8-*-
# 客户端
import socket

client = socket.socket()
client.connect(('localhost',6969))
while True:
    send_date = input(">>>:")
    client.send(bytes(send_date,encoding='utf-8'))
    # if send_date == "exit":break
    data = client.recv(1024)
    print("Recv:",data)

client.close()
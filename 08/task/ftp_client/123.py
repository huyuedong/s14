#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket,os
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:continue #判断输入是否为空

    elif cmd.startswith('get'): #判断输入是否为get开头
        client.send(cmd.encode())#发送要执行的操作
        client.recv(1024)#粘包 等待确定

        filename = cmd.split()[1]
        f = open(filename, 'wb') #以要下载的文件名打开一个文件
        data = client.recv(10024)
        f.write(data)
        f.close()
        print('接收完毕')

    elif cmd.startswith('put'): #判断输入是否为put开头
        filename = cmd.split()[1]
        if os.path.isfile(filename):  # 判断本地是否存在
            client.send(cmd.encode()) #发送要执行的操作
            client.recv(1024)  # 粘包 等待确定

            f = open(filename,'rb')
            aa = f.read()
            client.send(aa)
            f.close()
            print('发送完毕')
        else:
            print('没有此文件')

    else:
        print('输入错误请重新输入')
        continue
client.close()
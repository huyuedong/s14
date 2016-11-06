#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket
import os

def put(client,cmd):
    filename = cmd.split()[1]
    if os.path.isfile(filename):
        client.send(cmd.encode())
        client.recv(1024)

        with open(filename,'rb') as f:
            data = f.read()
            client.send(data)
        print('Send the file to complete')
    else:
        print('File does not exist')

def get(client,cmd):
    client.send(cmd.encode())
    client.recv(1024)

    filename = cmd.split()[1]
    with open(filename,'wb') as f:
        data = client.recv(10024)
        f.write(data)
    print('File receiving complete')

if __name__ == '__main__':
    client = socket.socket()
    server_addr = ('localhost',9999)
    client.connect(server_addr)
    while True:
        cmd = input(">>>:").strip()
        action = cmd.split()[0]
        if len(cmd) == 0:
            continue
        else:
            if action == "put":
                put(client,cmd)
            elif action == "get":
                get(client,cmd)
            else:
                print("Input Error!")
                continue
    client.close()
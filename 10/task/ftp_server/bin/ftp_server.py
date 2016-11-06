#!/usr/bin/env python
#-*-coding:utf-8-*-

import select
import socket
import queue
import sys
import os
import time


server = socket.socket()
server.setblocking(False)

server_addr = ('localhost',9999)
print('Starting up on %s:%s' % server_addr)
server.bind(server_addr)
server.listen(999)

msg_dic = {}
inputs = [server,]
outputs = []

while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)
    for r in readable:
        if r is server:
            conn,addr = server.accept()
            print("New Connection:",addr)
            inputs.append(conn)
            msg_dic[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            if data:
                print("Received data...")
                print(data.decode())
                r.send(b'yep')
                cmd, filename = data.decode().split()
                print('Task:', cmd, filename)
                msg_dic[r].put(data)
                outputs.append(r)

    for w in writeable:
        data = msg_dic[w].get()
        cmd, filename = data.decode().split()
        if cmd == 'get':
            if os.path.isfile(filename):
                f = open(filename, 'rb')
                aa = f.read()
                w.send(aa)
                f.close()
        elif cmd == 'put':
            f = open(filename,'wb')
            time.sleep(2)
            data = w.recv(1024)
            f.write(data)
            f.close()
        outputs.remove(w)

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)

        del msg_dic[e]

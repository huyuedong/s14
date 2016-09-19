#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket
import os
import json

class ftp_client(object):
    def __init__(self):
        self.client = socket.socket()

    # 帮助提示
    def help(self):
        msg = '''
        Usage:
        1. ls（未实现）
        2. pwd（未实现）
        3. cd（未实现）
        4. get filename
        5. put filename
        '''
        print(msg)
    # 新建连接
    def connect(self,host,port):
        self.client.connect((host,port))

    # 交互处理
    def interactive(self):
        while True:
            cmd = input(">>>:").strip()
            if len(cmd) == 0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s" % cmd_str):
                func = getattr(self,"cmd_%s" % cmd_str)
                func(cmd)
            else:
                self.help()
    # 上传
    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    "action":"put",
                    "filename":filename,
                    "filesize":filesize,
                    "overridden":True
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8"))
                print("发送任务>>:",json.dumps(msg_dic).encode("utf-8"))
                server_response = self.client.recv(1024)
                with open(filename,"rb") as f:
                    for line in f:
                        self.client.send(line)
                    else:
                        print("file upload success!")
                        f.close()
            else:
                print(filename,"不存在")
    # 下载
    def cmd_get(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            msg_dic = {
                "action":"get",
                "filename":filename
            }
            self.client.send(json.dumps(msg_dic).encode("utf-8"))
            print("发送任务:",json.dumps(msg_dic).encode("utf-8"))
            server_response = self.client.recv(1024)
            self.client.send("客户端准备接收文件".encode("utf-8"))
            file_total_size = int(server_response.decode())
            received_size = 0
            f = open(filename + ".recv","wb")
            while received_size < file_total_size:
                if file_total_size - received_size > 1024:
                    size = 1024
                else:
                    size = file_total_size - received_size
                    # print("Last receive:",size)
                data = self.client.recv(size)
                received_size += len(data)
                f.write(data)
            else:
                print("File receive done!")
                f.close()
        self.client.close()


if __name__ == '__main__':
    ftp = ftp_client()
    ftp.connect("localhost",9999)
    ftp.interactive()
#!/usr/bin/env python
#-*-coding:utf-8-*-

import socketserver
import os,json

class ftp_handle(socketserver.BaseRequestHandler):

    # 上传
    def put(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["filesize"]
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename,"wb")

        self.request.send("服务端收到请求".encode("utf-8"))
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded!" % filename)
    # 下载
    def get(self,*args):
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        if os.path.isfile(filename):
            filesize = os.stat(filename).st_size
            msg_dic = {
                "filesize":filename
            }
            self.request.send(str(filesize).encode("utf-8"))
            # self.request.send(json.dumps(msg_dic).encode("utf-8"))
            self.request.recv(1024)
            f = open(filename,"rb")
            for line in f:
                self.request.send(line)
            f.close()
        print(filename,"传送完成")

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionRefusedError as e:
                print("ERROR:",e)
                break

if __name__ == '__main__':
    host,port = "localhost",9999
    server = socketserver.ThreadingTCPServer((host,port),ftp_handle)
    server.serve_forever()


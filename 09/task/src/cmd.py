#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import sys
import paramiko
import threading
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting

server_list = setting.server_list

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def run(ip,user,passwd,cmd):
    s.connect(hostname=ip,username=user,password=passwd)
    stdin,stdout,stderr = s.exec_command(cmd)
    out,err = stdout.read(),stderr.read()
    if out:
        resule = out
    else:
        resule = err
    print(resule.decode())
    s.close()

def main():
    g = []
    for group in server_list:
        print(group)
        g.append(group)
    choose_group = input("请输入机器分组：").strip()
    flag = True
    while flag:
        if choose_group in g:
            while True:
                cmd = input('请输入要执行的命令：').strip()
                for server in server_list[choose_group]:
                    ip = server_list[choose_group][server]["IP"]
                    user = server_list[choose_group][server]["user"]
                    passwd = server_list[choose_group][server]["password"]
                    port = server_list[choose_group][server]["port"]
                    t = threading.Thread(target=run,args=(ip,user,passwd,port))
                    t.start()
                    t.join()
        else:
            print("输入错误，请重新输入！")

if __name__ == '__main__':
    main()

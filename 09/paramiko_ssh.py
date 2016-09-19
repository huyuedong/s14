#!/usr/bin/env python
#-*-coding:utf-8-*-

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.92.200',port=22,username='huyd',password='hu7yue')

stdin,stdout,stderr = ssh.exec_command('df')

out,err = stdout.read(),stderr.read()
if out:print(out.decode())
else:print(err.decode())

# print(result.decode())

ssh.close()
#!/usr/bin/env python
#-*-coding:utf-8-*-
import paramiko
transport = paramiko.Transport(('192.168.92.200',22))

transport.connect(username='huyd',password='hu7yue')

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传
sftp.put('huyd','/tmp/huyd')
# 下载
# sftp.get('/tmp/huyd','huyd')
transport.close()
#!/usr/bin/env python
#-*-coding:utf-8-*-

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa_100')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.92.200',port=22,username='huyd',pkey=private_key)

stdin,stdout,stderr = ssh.exec_command('df')

result = stdout.read()
print(result.decode())

ssh.close()
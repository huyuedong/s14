#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = input("input your name:")
age = int(input("input your age:"))
job = input("input your job:")

msg = '''
Infomation of user %s:
----------------------
Name:%s
Age :%d
Job :%s
---------End----------
''' % (name,name,age,job )
print(msg)

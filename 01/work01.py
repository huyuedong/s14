#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
retry_count=0
username = input("请输入用户名:")
while retry_count < 3:
    lock_data = open('userlock','r+')
    for lock_list in lock_data.readlines():
        if username == lock_list.strip():
            sys.exit("用户:%s 已锁定!" % username)
    lock_data.close()

    user_data = open('user','r+')
    password = input("请输入密码:")
    match_flag = False
    for user_list in user_data.readlines():
        _username,_password=user_list.strip().split()
        if username == _username and password == _password:
            print("用户：%s 登录成功" % username)
            match_flag = True
            sys.exit()
    user_data.close()
    if match_flag == False:
        print("用户名或密码错误！")
        retry_count += 1

else:
    print("用户：%s 已被锁定！" % username)
    lock_data = open('userlock','a')
    lock_data.write(username+'\n')
    lock_data.close()








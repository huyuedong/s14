#!/usr/bin/env python
# -*- coding:utf-8 -*-
# account_file = 'user'
# lock_file = 'userlock'
import sys
i = 0
while i < 3:
    username = input("请输入用户名:").strip()

    lock_file = open('userlock','r+')
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        lock_line = lock_line.strip('\n')
        if username == lock_line:
            sys.exit('用户 %s 已经被锁定！' % username)

    user_file = open('user','r+')
    for user_line in user_file.readlines():
        user_line = user_line.strip().split(':')
        if user_line[0] == username:
            j = 0
            while j < 3:
                password = input("请输入密码:").strip()
                if user_line[1] == password:
                    print("用户登录成功！")
                    sys.exit()
                else:
                    print("用户名或密码错误！")
                    j += 1
            else:
                lock_file.write('\n' + username)
                sys.exit("用户 %s 达到登录次数，将被锁定" % username)
        else:
            print("用户名不存在！")
            break
lock_file.close()
user_file.close()
















# username = input("Username:").strip()
# password = input("Password:").strip()
# if len(username) != 0 and len(password) != 0:
#     lf = open(lock_file,'r')
#     for lf_line in lf.readlines():
#          lf_line = lf_line.split()
#          if username == lf_line:
#              print("User:%s is Locked!" % username)
#              lf.close()
#              break
#          else:
#              af = open(account_file,'r')
#              for af in af.readlines():
#                 af_line = af.split(':')
#                 if username == af_line[0] and password == af_line[1]:
#                     print("User:%s Login success!" % username)
#                     break



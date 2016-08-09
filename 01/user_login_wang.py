#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

username = input("Please input your name:").strip()
user_data = open('shopping_data','r+')
user_flag = False
for userline in user_data.readlines():
    userline = userline.strip().split(":")
    if userline[0] ==username and userline[2] =="lock":
        print("User:%s is Locked!" % username)
        sys.exit(1)
    elif userline[0] ==username:
        i = 0
        user_flag = True
        while i < 3:
            password = input("Please input your password:")
            if userline[1] ==password:
                print("User：%s is login sucess!" % username)
                sys.exit(0)
            else:
                print("用户名或密码错误！")
                i += 1
        else:
            with open('shopping_data','r') as f:
                userdata_file=''
                for line in f.readlines():
                    if userline[0] in line:
                        line = line.replace("active","lock")
                    userdata_file+=line
            with open('shopping_data','w') as f:
                f.write(userdata_file)

            sys.exit("密码错误次数达3次，账户已锁定！")

            # with open('shopping_data','r+') as f:
            #     d = f.read()
            #     u_old = '%s:%s:%s' % (userline[0],userline[1],userline[2])
            #     u_new = '%s:%s:%s' % (userline[0],userline[1],"lock")
            #     d.replace(u_old,u_new)
            #     f.write(d)
            #     f.close()
            #     sys.exit("密码错误次数达3次，账户已锁定！")
            #     break
if user_flag == False:
    sys.exit("用户名不存在！")





#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,getpass

username = input("Please input your name:").strip()
user_data = open('shopping_data','r+')
user_flag = False
for userline in user_data.readlines():
    userline = userline.strip().split(":")
    if userline[0] ==username and userline[2] =="lock":
        print("User:%s is Locked!" % username)
        sys.exit()
    elif userline[0] ==username:
        i = 0
        user_flag = True
        while i < 3:
            password = getpass.getpass("Please input your password:")
            if userline[1] ==password:
                print("User：%s is login sucessful!" % username)
                sys.exit()
            else:
                print("Incorrect username or password.")
                i += 1
        else:
            with open('shopping_data','r+') as f:
                new_line = ''
                for line in f.readlines():
                    if userline[0] in line:
                        line = line.replace("active","lock")
                    new_line += line
            with open('shopping_data','w') as f:
                f.write(new_line)
            sys.exit("You tried too many times,account will be locked")
if user_flag == False:
    sys.exit("User:%s does not exist" % username)





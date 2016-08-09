#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

def login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    with open("user","r+") as userdata:
        for userline in userdata.readlines():
            userline = userline.strip().split(":")
            print(userline)

login()
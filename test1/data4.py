#!/usr/bin/env python
# -*- coding:utf-8 -*-
user = "huyd"
passwd = "huyd"

for i in range(3):
    username = input("Please input your name:")
    password = input("Please input your password:")

    if user == username and passwd == password:
        print("Welcome Login")
        break
    else:
        print("Invalid Username or password!")

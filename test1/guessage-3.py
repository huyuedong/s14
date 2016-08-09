#!/usr/bin/env python
# -*- coding:utf-8 -*-

my_age = 22
counter = 0
while counter < 3:
    user_input = int(input("Please enter a guess my age:"))
    if user_input > my_age:
        print("Think smaller!")
    elif user_input < my_age:
        print("Think bigger!")
    else:
        print("Congratulations,you got it!")
        break
    counter += 1
else:
    print("猜这么多次都不对，笨蛋！")

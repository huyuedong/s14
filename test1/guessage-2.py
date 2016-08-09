#!/usr/bin/env python
# -*- coding:utf-8 -*-

my_age = 22
counter = 0
#for i in range(10):
while True:
    if counter < 3:
        user_input = int(input("Please enter a guess my age:"))
        if user_input > my_age:
            print("Think smaller!")
        elif user_input < my_age:
            print("Think bigger!")
        else:
            print("Congratulations,you got it!")
            break
    else:
        continue_confirm = input("Do you want to continue?(y/n):")
        if continue_confirm == 'y':
            counter = 0
            continue
        else:
            break
    counter += 1
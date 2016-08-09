#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
name = input("Your Name:")
age = input("Your Name:")
job = input("Your Name:")
print("Your Name:",name)
'''
age = 22
counter = 0
for i in range(10):
    print('-----> counter:',counter)
    if counter < 3:
        guess_num = int(input("Please input your guess number:"))
        if guess_num == age:
            print("Ture!")
            break
        elif guess_num < age:
            print("Think biger!")
        else:
            print("Think smaller!")
    else:
        continue_confirm = input("Do you want to continue?(y/n):")
        if continue_confirm == 'y':
            counter = 0
            continue
        else:
            break
    counter +=1

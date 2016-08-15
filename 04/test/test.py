#!/usr/bin/env python
#-*-coding:utf-8-*-
import time

# def timer(func):
#     def deco():
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("The func run time is %s" % (stop_time-start_time))
#     return deco
#
# # def timer(func):
# #     start_time = time.time()
# #     func()
# #     stop_time = time.time()
# #     print("The function run time is %s" % (stop_time-start_time))
# #     return func
#
#
#
#
# #
# @timer
# def f1():
#     print("This is function F1")
#     time.sleep(1)
#     # return "done"
#
#
# f1()

def login(func):
    def deco(*args,**kwargs):
        print("[装饰器]正在验证登录：")
        res = func(*args,**kwargs)
        return res     # 此处应该将被装饰函数的返回值return
    return deco

@login
def wel(*args,**kwargs):
    print("Welcome {} to login the page!".format(*args,**kwargs))
    return "sucessful"     # 被装饰的函数有返回值

wel = wel("huyd")
print(wel)




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

# def login(func):
#     def deco(*args,**kwargs):
#         print("[装饰器]正在验证登录：")
#         res = func(*args,**kwargs)
#         return res     # 此处应该将被装饰函数的返回值return
#     return deco
#
# @login
# def wel(*args,**kwargs):
#     print("Welcome {} to login the page!".format(*args,**kwargs))
#     return "sucessful"     # 被装饰的函数有返回值
#
# wel = wel("huyd")
# print(wel)

import json
data = {'k1':123,'k2':'Hello'}

# json.dumps 将数据通过特殊的形式转换为所有程序语言都认识的字符串
j_str = json.dumps(data)
print(type(j_str),j_str)
# json.loads 将字典形式的字符串转换为字典格式
j_dict = json.loads(j_str)
print(type(j_dict),j_dict)
# json.dump 将数据通过特殊的形式转换为所有程序都认识的字符串，并写入文件
with open('result.json','w') as f:
    json.dump(data,f)

import pickle
# pickle.dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(type(p_str),p_str)

# pickle.dump 将数据通过特殊的形式转换为只有Python语言认识的字符串，并写入文件
with open('result.pk','w') as f:
    pickle.dump(data,f)
































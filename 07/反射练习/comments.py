#!/usr/bin/env python
#-*-coding:utf-8-*-
# 利用字符串的形式去对象（默认）中操作（寻找）成员
# getattr()   # 获取它的成员（属性）

class Web(object):

    def home(self):
        print("家目录")

    def index(self):
        print("主页面")

    def login(self):
        print("登录页面")
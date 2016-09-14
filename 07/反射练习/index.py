#!/usr/bin/env python
#-*-coding:utf-8-*-

class Web(object):

    def home(self):
        print("家目录")

    def index(self):
        print("主页面")

    def login(self):
        print("登录页面")

def run():
    w1 = Web()
    inp = input("请输入您要访问的URL：").strip()

    if hasattr(w1,inp):
        func = getattr(w1,inp)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()

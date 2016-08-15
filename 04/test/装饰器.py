#!/usr/bin/env python
#-*-coding:utf-8-*-

def deco_fun1():
    print("装饰器功能1")

def deco_fun2():
    print("装饰器功能2")

def deco(deco_fun):
    def outer(main_fun):
        def inner():
            deco_fun()
            main_fun()
        return inner
    return outer

@deco(deco_fun1)
def index():
    print("我是主程序")

index()
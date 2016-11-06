#!/usr/bin/env python
#-*-coding:utf-8-*-
import gevent

def bar():
    print("111111")
    gevent.sleep(1)
    print("222222")

def func1():
    print("333333")
    gevent.sleep(2)
    print("444444")

def func2():
    print("555555")
    gevent.sleep(0)
    print("666666")

gevent.joinall([
    gevent.spawn(bar),
    gevent.spawn(func1),
    gevent.spawn(func2),
])
#!/usr/bin/env python
#-*-coding:utf-8-*-
# 协程
from greenlet import greenlet

def test1():
    print("111111")
    gr2.switch()
    print("222222")
    gr2.switch()
    print("done")

def test2():
    print("333333")
    gr1.switch()
    print("444444")
    gr1.switch()

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
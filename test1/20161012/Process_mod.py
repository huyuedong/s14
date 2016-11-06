#!/usr/bin/env python
#-*-coding:utf-8-*-
from multiprocessing import Process
from multiprocessing import Array

def Foo(i,temp):
    temp[0] += 100
    for item in temp:
        print(i,'----->',item)

if __name__ == '__main__':
    temp = Array('i', [11, 22, 33, 44])
    for i in range(2):
        p = Process(target=Foo, args=(i,temp))
        p.start()
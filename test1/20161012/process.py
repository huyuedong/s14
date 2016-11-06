#!/usr/bin/env python
#-*-coding:utf-8-*-
from multiprocessing import Process

def foo(i):
    print("This is Process ",i)

if __name__ == '__main__':
    for i in range(5):
        p = Process(target=foo,args=(i,))
        p.start()
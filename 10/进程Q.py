#!/usr/bin/env python
#-*-coding:utf-8-*-
import queue,threading,multiprocessing
from multiprocessing import Queue,Process

def f(qq):
    qq.put([42,None,'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
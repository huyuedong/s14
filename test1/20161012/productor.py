#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import queue
import threading

q = queue.Queue(10)
def productor(i):
    while True:
        q.put("厨师 %s 做的包子！"%i)
        time.sleep(2)

def consumer(k):
    while True:
        print("顾客 %s 吃了一个 %s"%(k,q.get()))
        time.sleep(1)

for i in range(3):
    t = threading.Thread(target=productor,args=(i,))
    t.start()

for k in range(10):
    v = threading.Thread(target=consumer,args=(k,))
    v.start()
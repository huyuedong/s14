#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
import threading

def addNum():
    global num
    print('--get num:',num)
    time.sleep(1)
    lock.acquire()
    num -=1
    lock.release()

num = 100
thread_list = []
lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:
    t.join()

print('final num:',num)



#!/usr/bin/env python
#-*-coding:utf-8-*-

import threading

def func(e,i):
    print(i)
    e.wait()
    print(i+100)

event = threading.Event()
for i in range(10):
    t = threading.Thread(target=func,args=(event,i))
    t.start()

event.clear()
inp = input(">>>")
if inp == "1":
    event.set()
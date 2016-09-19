#!/usr/bin/env python
#-*-coding:utf-8-*-
import threading
import time

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count > 5 and count <= 10:
            event.clear() # 清空标志位变成红灯
            print("\033[41;1m红灯\033[0m")
        elif count > 10:
            event.set()   # 变成绿灯
            count = 0
        else:
            print("\033[42;1m绿灯\033[0m")
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print("%s is running......" % name)
            time.sleep(1)
        else:
            print("%s 遇到红灯  waiting......" % name)
            event.wait()
            print("\033[42;1m%s 绿灯亮了，Let's go!!\033[0m"% name)

light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()
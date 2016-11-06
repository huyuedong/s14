#!/usr/bin/env python
#-*-coding:utf-8-*-
import time
from threading import Timer

def hello():
    print("hello world")
    print(stop_time - start_time)

start_time = time.time()
t = Timer(1,hello)
t.start()
stop_time = time.time()

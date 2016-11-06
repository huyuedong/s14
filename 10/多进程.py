#!/usr/bin/env python
#-*-coding:utf-8-*-
import multiprocessing
import threading
import time

def mod_threading():
    print(threading.get_ident())

def run(name):
    time.sleep(2)
    print("Hello %s" % name)
    t = threading.Thread(target=mod_threading,)
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('Dave %s' % i,))
        p.start()
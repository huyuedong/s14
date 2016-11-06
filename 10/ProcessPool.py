#!/usr/bin/env python
#-*-coding:utf-8-*-
#回调
from multiprocessing import Process,Pool,freeze_support
import time,os

def Foo(i):
    time.sleep(2)
    print("In Process",os.getpid())
    return i + 100

def Bar(arg):
    print("--->exec done:",arg,os.getpid())

if __name__ == '__main__':
    pool = Pool(processes=3)
    print("主进程",os.getpid())
    for i in range(12):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)
    print("end")
    pool.close()
    pool.join()
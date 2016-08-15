#!/usr/bin/env python
#-*-coding:utf-8-*-
import time

def timmer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("The fucntion run time is %s" % (stop_time-start_time))
    return deco


@timmer
def test1():
    time.sleep(2)
    print("in the test1")
@timmer
def test2(name,age):
    time.sleep(2)
    print("my name is %s ,i am %s years old" % (name,age))

test1()
test2("huyd",155)

# 列表生成式
# 迭代器￥生成器


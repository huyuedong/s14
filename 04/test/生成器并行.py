#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
def consumer(name):
    print("%s准备吃包子啦" % name)
    while True:
        baozi = yield
        print("[%s]包子来了，被[%s]吃了！" % (baozi,name))

c = consumer("shaolin")
c.__next__()
c.send("jidan")

# def producer(name):
#     c1 = consumer("A1")
#     c2 = consumer("A2")
#     c1.__next__()
#     c2.__next__()
#     print("开始做包子啦！")
#     for i in range(10):
#         time.sleep(1)
#         print("做了一个包子，分了一半。")
#         c1.send(i)
#         c2.send(i)
#
# producer("Shaolin")
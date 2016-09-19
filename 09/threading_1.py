#!/usr/bin/env python
#-*-coding:utf-8-*-

import threading
import time

'''
def run(n):
    print("task:",n)
    time.sleep(2)

t1 = threading.Thread(target=run,args=("T1",))
t2 = threading.Thread(target=run,args=("T2",))

t1.start()
t2.start()
'''

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("RUNING Task:",self.n)
        time.sleep(2)

# t1 = MyThread("T1")
# t2 = MyThread("T2")
# t1.start()
# t2.start()

start_time = time.time()
t_objs = []

for i in range(50):
    t = MyThread("T-%s" % i)
    t.setDaemon(True)
    t.start()
    t_objs.append(t)

# for t in t_objs:
#     t.join()

print("----All threads has finished----")
print("cost:",time.time() - start_time)


















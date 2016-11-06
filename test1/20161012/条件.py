#!/usr/bin/env python
#-*-coding:utf-8-*-
import threading

# def condition():
#     ret = False
#     r = input(">>>:")
#     if r == "yes":
#         ret = True
#     return ret
#
# def func(conn,i):
#     print(i)
#     conn.acquire()
#     conn.wait_for(condition)
#     print(i+100)
#     conn.release()
#
# c = threading.Condition()
# for i in range(10):
#     t = threading.Thread(target=func,args=(c,i))
#     t.start()
def run(n):
    con.acquire()
    con.wait()
    print("run the thread:%s" %n)
    con.release()

if __name__ == '__main__':
    con = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=run,args=(i,))
        t.start()

    while True:
        inp = input(">>>:")
        if inp == "q":
            break
        con.acquire()
        con.notify(int(inp))
        con.release()
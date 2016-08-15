#!/usr/bin/env python
#-*-coding:utf-8-*-

#day4for上节课回顾:
# 0、变量
# 1、函数、作用域
# 2、位置变量、指定变量
# 3、递归、高阶函数

# 1、set集合
list_1 = set([1,2,3,4,5])
list_2 = set([5,6,7,8,9])
list_3 = set([1,2,3])
'''
# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集(合并两个列表，并去重)
print(list_1.union(list_2))
print(list_1 | list_2)
# 差集
print(list_1.difference(list_2))
print(list_1 - list_2)
# 对称差集(取出两个列表中互不相同的部分)
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
# 子集
print(list_3.issubset(list_1))
# 父集
print(list_1.issuperset(list_3))
# 是否有交集
print(list_3.isdisjoint(list_1))
## 增删改差
'''
# 2、文件操作
'''
# 实时刷新
f = open("data","a",encoding="utf-8")
import sys,time
a = 0
for i in range(100):
    a += 1
    a = str(a)
    sys.stdout.write(a)
    sys.stdout.flush()
    time.sleep(0.3)
    a = int(a)
f.close()
'''
'''
# high bige loop
count = 0
with open("data","r+",encoding="utf-8") as f:
    for line in f:
        if count == 9:
            print("------我是分割线------")
            count += 1
            continue
        print(line)
        count += 1
'''
'''
# 文件修改
f = open("data","r",encoding="utf-8")
f_new = open("data.tmp","w",encoding="utf-8")
print(f.readlines())
for line in f:
    if "昨日当我年少轻狂" in line:
        line = line.replace("昨日当我年少轻狂","昨日当Alex年少轻狂")
    f_new.write(line)

f.close()
f_new.close()
'''
'''
# 函数
import time
def logger_test():
    time_format='%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("a.txt","a+") as f:
        f.write('time %s end action...\n' % time_current)

def test1():
    print("This is Test1")
    logger_test()

def test2():
    print("This is Test2")
    logger_test()

def test3():
    print("This is Test3")
    logger_test()

test1()
test2()
test3()
'''
# def test(x,y):
#     print(x,y)
#
# test(6,7)

# def test1(name,age,*args,**kwargs):
#     print(name,age,args,kwargs)
# test1("shaolin",99,balance=88,monry=77)

# School = "Oldboy edu."
#
# def change_name(name):
#     global School       # don't use
#     School = "Beidaqingniao"
#     print("before change:",name,School)
#     name = "JACK"
#     print("after change:",name,School)
#
# change_name("huyd")
# print(School)

# def calc(n):
#     print(n)
#     if int(n/2) > 0:
#         return calc (int(n/2))
#     print("+++++",n)
# calc(10)

#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
print(sys.getdefaultencoding())

msg = "周杰伦"
msg_gb2312 = msg.decode("utf-8").encode("gb2312")
gb2312_to_gbk = msg_gb2312.decode("gbk").encode("gbk")

print(msg)
print(msg_gb2312)
print(gb2312_to_gbk)



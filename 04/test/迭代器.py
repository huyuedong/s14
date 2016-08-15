#!/usr/bin/env python
#-*-coding:utf-8-*-

gen = iter([1,2,3])

# 取值方法一：
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
# print(gen.__next__())    #再取值就会报错

# 取值方法二：
for i in gen:
    print(i)


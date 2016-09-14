#!/usr/bin/env python
#-*-coding:utf-8-*-

try:
    a = [1,2]
    a[0]
    b = {"a":"b"}
    b["a"]
    # open("aaa")
except IndexError as e:
    print("列表错误",e)
except KeyError as e:
    print("没有这个key",e)
except Exception as e:
    print("未知错误",e)
else:
    print("没有错误")
finally:
    print("不管有没有错，我都执行")
    print("---------------------")

class huydError(Exception):
    def __init__(self,msg):
        self.msg = msg
try:
    raise huydError('我的自定义错误')
except huydError as e:
    print(e)
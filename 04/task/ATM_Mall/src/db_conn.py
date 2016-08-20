#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

'''
数据库读写模块
'''
import json,pickle

# 读取用户数据库
def read_db(arg):
    with open(arg,'r') as f:
        return json.load(f)

# 写入用户数据库
def write_db(file=None,data=None):
    with open(file,'w') as f:
        return json.dump(data,f)



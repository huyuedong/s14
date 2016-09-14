#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
读写数据文件接口
'''
import pickle

# 读取存档文件
def read(db_path):
    with open(db_path,"rb") as f:
        return pickle.load(f)

# 写入存档文件
def write(db_path,db_info):
    with open(db_path,"ab") as f:
        pickle.dump(db_info,f)
    return True
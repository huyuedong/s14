#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
处理数据文件接口
'''
import sys,os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from conf import settings

def file_handle(conn_params,file_name):
    db_path = os.path.join(conn_params['path'],file_name)
    return db_path

def handle(conn_params,file_name):
    if conn_params['engine'] == 'file':
        return file_handle(conn_params,file_name)
    else:
        pass
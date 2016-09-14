#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
数据库操作模块
'''
import json,os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import db_conn
from conf import settings

def read(card_id):
    '''
    读取数据中的用户基本信息
    :param card_id: 用户卡号
    :param user_type: 用户类型 ADMIN or USER
    :return: 用户基本信息
    '''
    db_path = db_conn.db_conn(settings.USER)
    db_file = '%s' % os.path.join(db_path,str(card_id),'base_info.json')
    with open(db_file,'r') as f:
        base_info = json.load(f)
        return base_info

def write(db_data):
    '''
    将更新过的信息写入数据文件中
    :param card_id: 用户卡号
    :param user_type: 用户类型 ADMIN or USER
    :return: base_info
    '''
    db_path = db_conn.db_conn(settings.user_type)
    db_file = '%s' % os.path.join(db_path,str(db_data['id']),'base_info.json')
    with open(db_file,'w') as f:
        return json.dump(db_data,f)






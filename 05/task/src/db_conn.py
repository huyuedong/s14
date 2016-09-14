#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
数据库连接模块
'''

def file_db_conn(user_type):
    '''
    获取本地文件类型数据路径
    :param conn_option: settings文件中的用户类型（USER_DATABASE or ADMIN_DATABASE）
    :return: 不同用户类型的db路径
    '''
    print("FileDB Path:",user_type)
    db_path = user_type['path']
    return db_path

def db_conn(user_type):
    '''
    根据不同的数据类型来判断连接方式，便于后续拓展其他连接方式。
    :param user_type: USER or ADMIN
    :return: 连接方式
    '''
    if user_type['engine'] == 'file':
        return file_db_conn(user_type)

#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
from src import db_conn


def login(arg):
    def wrapper(func):
        def inner(*args):
            while True:
                if arg == 1:
                    card_id = input("请输入银行卡号：").strip()
                    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
                    db =db_conn.read_db(user_info_file)
                    password = input("请输入密码：").strip()
                    if os.path.exists(user_info_file):
                        if password == db['password']:
                            print("登录成功！")
                            func(*args)
                        else:
                            print("密码错误！")
                    else:
                        print("该账号不存在！")
                elif arg == 2:
                    admin_info_file = os.path.join(settings.ADMIN_INFO_DIR,'base_info.json')
                    db = db_conn.read_db(admin_info_file)
                    user = input("请输入管理员账户名：")
                    passwd = input("请输入管理员密码：")
                    if user == db['username'] and passwd == db['password']:
                        print("管理员admin登录成功！")
                        func()
                    else:
                        print("用户名或密码错误！")
                else:
                    print("ERROR！接口调用参数异常！")
        return inner
    return wrapper

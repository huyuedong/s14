#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,json,shutil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
from src import atm_login

# 新建用户
def create_user():
    print("功能：新建用户>>>")
    card_id = input("请输入新用户卡号（4位数字）:").strip()
    if card_id.isdigit():
        pass
    else:
        print("ERROR! Must enter the Numbers!")
        exit(1)
    os.makedirs(os.path.join(settings.USER_INFO_DIR,card_id,'record'))

    base_info = {'username':'lily',
                 'card_id':card_id,
                 'password':'123',
                 "credit":15000,         # 信用卡额度
                 'balance':15000,        # 本月可用余额
                 'saving':0,             # 储蓄金额
                 'enroll_date':"2016-01-01",
                 'expire_date':"2026-01-01",
                 'status':0,
                 "debt":[],              # 欠款记录，如：[{'date':"2016-08-08","total":80000,"balance":8000}]
                }
    json.dump(base_info,open(os.path.join(settings.USER_INFO_DIR,card_id,'base_info.json'),'w'))
    print("用户账号：[%s]创建成功。" % card_id)

def remove_user():
    '''
    删除用户模块
    :return:
    '''
    print("功能：删除用户>>>")
    card_id = input("请输入您要删除的账户：").strip()
    user_info_path = os.path.join(settings.USER_INFO_DIR,str(card_id))
    while user_info_path:
        shutil.rmtree(user_info_path)
    else:
        print("您要删除的用户不存在")

def quit():
    '''
    退出模块
    :return: exit(0)
    '''
    exit(0)

@atm_login.login(2)
def main_body():
    menu = '''
    1.创建账户
    2.删除账户
    Q.退出
    '''
    print(menu)
    menu_dic = {
        '1':create_user,
        '2':remove_user,
        'q':quit,
        'Q':quit
    }
    while True:
        user_choose = input("请选择：").strip()
        if user_choose in menu_dic:
            menu_dic[user_choose]()
        else:
            print("您选择的功能不存在")












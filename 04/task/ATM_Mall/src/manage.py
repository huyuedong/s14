#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
from src import atm_login

# 新建用户
def create_user():
    print("功能：新建用户>>>")
    card_id = input("请输入新用户卡号（4位数字）:")
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

def main_body():
    loop_flag = True
    while loop_flag:
        print("1.新建用户")
        user_choose = input("请选择：").strip()
        if user_choose == '1':
            create_user()
        elif user_choose == 'q':
            exit(0)












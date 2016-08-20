#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from src import db_conn
from src import atm_login

# 查询接口
def query_info(card_id):
    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
    db =db_conn.read_db(user_info_file)
    print("功能：查询额度>>>")
    print("您的总额度为：%s，本月可用额度：%s，存款余额：%s" % (db['credit'],db['balance'],db['saving']))

# 提现接口
def get_money(card_id):
    print("功能：提现>>>")
    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
    db =db_conn.read_db(user_info_file)
    num = float(input("请输入提现金额："))
    if db['saving'] >= num:
        db['saving'] -= num
        db_conn.write_db(file=user_info_file,data=db)
        print("您本次从储蓄金中提现：[%s] 不收手续费。" % num)
    else:
        tmp = num - db['saving']
        if db['balance'] >= (tmp + tmp * 0.05):
            db['saving'] = 0
            db['balance'] -= tmp
            db['balance'] -= tmp * 0.05
            db_conn.write_db(file=user_info_file,data=db)
            print("您本次提现[%s]，其中透支[%s]，透支部分收取利息[%s]" % (num,tmp,tmp*0.05))
        else:
            print("账户余额不足，无法提现！")

# 还款接口
def repay(card_id):
    print("功能：还款>>>")
    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
    db =db_conn.read_db(user_info_file)
    num = float(input("请输入还款金额："))
    tmp = db['credit'] - db['balance']
    if tmp == 0:
        db['saving'] += num
        db_conn.write_db(file=user_info_file,data=db)
        print("您本次存入储蓄金：[%s]" % num)
    else:
        if num <= tmp:
            db['balance'] += num
            db_conn.write_db(file=user_info_file,data=db)
            print("您本次还款：[%s]" % num)
        else:
            money = num - tmp
            db['balance'] = db['credit']
            db['saving'] += money
            db_conn.write_db(file=user_info_file,data=db)
            print("您本次还款：[%s]，其中存入储蓄金[%s]" % (num,money))

# @atm_login.login(1)
def main_body():
    card_id = input("请输入用户卡号：")
    loop_flag = True
    while loop_flag:
        user_choose = input("1.查询\n2.提现\n3.还款").strip()
        if user_choose == '1':
            query_info(card_id)
        elif user_choose == '2':
            get_money(card_id)
        elif user_choose == '3':
            repay(card_id)
        elif user_choose.upper() == "B":
            break
        elif user_choose.upper() == "Q":
            loop_flag = False
            break
        else:
            print("输入有误！")


# def main():
#     id = input("请输入卡号：")
# 	main_body(id)

if __name__ == "__main__":
	main_body()

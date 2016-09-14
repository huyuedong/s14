#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from conf import settings
from src import db_conn
from src import atm_login


def query_info(card_id):
    '''
    查询接口
    :param card_id:
    :return:
    '''
    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
    db =db_conn.read_db(user_info_file)
    print("功能：查询额度>>>")
    print("您的总额度为：%s，本月可用额度：%s，存款余额：%s" % (db['credit'],db['balance'],db['saving']))

def get_money(card_id):
    '''
    提现接口
    :param card_id:用户账号
    :return:
    '''
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
        if db['balance'] >= (tmp + tmp * settings.interest):
            db['saving'] = 0
            db['balance'] -= tmp
            db['balance'] -= tmp * settings.interest
            db_conn.write_db(file=user_info_file,data=db)
            print("您本次提现[%s]，其中透支[%s]，透支部分收取利息[%s]" % (num,tmp,tmp*settings.interest))
        else:
            print("账户余额不足，无法提现！")

def repay(card_id):
    '''
    还款接口
    :param card_id:用户账号
    :return:
    '''
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

def transfer(card_id):
    '''
    转账接口
    :param card_id:
    :return:
    '''
    print("功能：转账>>>")
    user_info_file = os.path.join(settings.USER_INFO_DIR,str(card_id),'base_info.json')
    db =db_conn.read_db(user_info_file)
    receiver_card_id = int(input("请输入收款人的账号："))
    transfer_money = float(input("您目前储蓄账户余额为[%s]，请输入要转账的金额：" % db['saving']))
    receiver_user_info_file = os.path.join(settings.USER_INFO_DIR,str(receiver_card_id),'base_info.json')
    receiver_db =db_conn.read_db(receiver_user_info_file)
    if transfer_money > db['saving']:
        print("余额不足，无法完成本次转账")
    else:
        db['saving'] -= transfer_money
        db_conn.write_db(file=user_info_file,data=db)
        tmp = receiver_db['credit'] - receiver_db['balance']
        if tmp == 0:
            receiver_db['saving'] += transfer_money
            db_conn.write_db(file=receiver_user_info_file,data=receiver_db)
            print("转入对方储蓄账户[%s]" % transfer_money)
        else:
            if tmp >= transfer_money:
                receiver_db['balance'] += transfer_money
                db_conn.write_db(file=receiver_user_info_file,data=receiver_db)
                print("转入对方信用账户[%s]" % transfer_money)
            else:
                money = transfer_money - tmp
                receiver_db['balance'] += tmp
                receiver_db['saving'] += money
                db_conn.write_db(file=receiver_user_info_file,data=receiver_db)
                print("转入对方信用账户[%s],储蓄账户[%s]" % (tmp,money))
        print("成功给账户[%s]转账[%s]" % (receiver_card_id,transfer_money))


@atm_login.login(1)
def main_body(card_id):
    menu = '''
    ---功能列表---
    1.查询
    2.提现
    3.还款
    4.转账
    5.账单（敬请期待）
    q.退出
    '''
    menu_dic = {
        '1':query_info,
        '2':get_money,
        '3':repay,
        '4':transfer,
    }
    while True:
        print(menu)
        user_choose = input("请选择:").strip()
        if user_choose in menu_dic:
            menu_dic[user_choose](card_id)
        else:
            if user_choose == 'q':
                exit(0)
            else:
                print("你选择的功能不存在")

if __name__ == "__main__":
	main_body()

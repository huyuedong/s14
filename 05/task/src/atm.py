#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
import db_handle
import deal

def account_info():
    pass

def repay(acc_data):
    '''
    还款模块
    :param account_data:
    :return:
    '''
    account_data = db_handle.read(acc_data['id'])
    curren_balance = '''------余额信息------
    额度：%s
    余额：%s''' % (account_data['credit'],account_data['balance'])
    print(curren_balance)
    back_flag = True
    while back_flag:
        repay_num = input('请输入还款金额：').strip()
        if len(repay_num) > 0 and repay_num.isdigit():
            print('ddd 00')
            new_balance = deal.deal_calc(account_data,'repay',repay_num)
            if new_balance:
                print("还款后余额为：%s" % new_balance['balance'])
        else:
            print("负数怎么存？")
        if repay_num == 'b':
            back_flag = False

def withdraw():
    pass

def transfer():
    pass

def pay_check():
    pass

def logout():
    pass

def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款(功能已实现)
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    user_data = int(input("请输入账号："))
    interactive(user_data)


if __name__ == '__main__':
    run()
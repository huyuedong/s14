#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
交易计算
'''
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
import db_handle

def deal_calc(account_data,tran_type,num):
    '''

    :param account_data:
    :param tran_type:
    :param num:
    :param user_type:
    :return:
    '''
    num = float(num)
    if tran_type in settings.TRANSACTION_TYPE:
        interest = num * settings.TRANSACTION_TYPE[tran_type]['interest']
        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + num + interest
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - num - interest
            if new_balance < 0:
                print('交易失败，余额%s不够支付该笔交易。' % old_balance)
                return
            account_data['balance'] = new_balance
            db_handle.write(account_data)
            return account_data
    else:
        print("交易类型不存在！")
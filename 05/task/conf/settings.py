#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# USER_INFO_DIR = "{}\\db".format(BASE_PATH)
# USER_INFO_DIR = os.path.join(BASE_PATH,"db")
# ADMIN_INFO_DIR = os.path.join(BASE_PATH,"db","admin_data")

USER = {
    'engine':'file',
    'name':'accounts',
    'path':'%s' % os.path.join(BASE_PATH,"db","user_data")
}

ADMIN = {
    'engine':'file',
    'name':'accounts',
    'path':'%s' % os.path.join(BASE_PATH,"db","admin_data")
}

TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}
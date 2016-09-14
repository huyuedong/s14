#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import atm
from src import manage

def main():
    menu = '''
    -----ATM机-----
    1.个人用户登录
    2.管理后台登录
    Q.退出
    '''
    print(menu)
    menu_dic = {
        '1':atm.main_body,
        '2':manage.main_body,
    }
    while True:
        user_choose = input("请选择：").strip()
        if user_choose in menu_dic:
            menu_dic[user_choose]()
        elif user_choose == 'q':
            exit(0)
        else:
            print("您选择的功能不存在！")

if __name__ == "__main__":
	main()


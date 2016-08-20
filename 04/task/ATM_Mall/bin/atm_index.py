#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import atm
from src import manage

def main():
    while True:
        print(">>>欢迎使用ATM机<<<")
        choose = input("1.用户登录\n2.后台管理\n3.Q：退出").strip()
        if choose == "1":
            atm.main_body()
        elif choose == '2':
            manage.main_body()
        elif choose == 'q':
            exit(0)
        else:
            print("输入错误！")


if __name__ == "__main__":
	main()


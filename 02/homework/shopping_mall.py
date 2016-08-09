#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

user_type = ["个人用户","商家用户"]
shopping_cart = []
product_list = []
print("\033[31m欢迎登陆京西商城\033[0m")
while True:
    for key,user_list in enumerate(user_type,1):
        print("%s.%s" % (key,user_list))
    user_choose = input("请您选择入口信息：")
    if user_choose == "1":      # 进入个人入口
        user_flag = False
        while True:
            username = input("请输入您的用户名：").strip()
            with open("user_data",'r+') as userdata:      # 打开用户数据文件
                for userline in userdata.readlines():
                    userline = userline.strip().split(":")
                    if userline[0] == "u" and userline[1] == username:
                        if userline[3] == "lock":           # 判断是否被锁定
                            print("\033[31m用户:%s 已被锁定!\033[0m" % username)
                            sys.exit(1)
                        elif userline[1] == username:
                            user_flag = True
                            i = 0
                            while i < 3:
                                password = input("请输入您的密码：")
                                if userline[2] == password:              # 判断密码是否正确
                                    balance = int(userline[4])
                                    print("登录成功,您的账户余额为：%s" % balance)
                                    with open("shopping_data","r+") as shopping_list:          #打开商品数据文件
                                        for key,item in enumerate(shopping_list,1):
                                            item = item.strip().split(":")
                                            product_list.append(item)
                                            print("%s.%s" % (key,item))
                                        while True:                         # 进入购物车循环
                                            user_choose1 = input("请选择您要购买的商品(输入q退出并结算)：")
                                            if user_choose1.isdigit():
                                                user_choose1 = int(user_choose1)
                                                if user_choose1 <= int(key) and user_choose1 > 0:
                                                    p_item = product_list[user_choose1 - 1]
                                                    if int(p_item[1]) <= balance:
                                                        shopping_cart.append(p_item)
                                                        balance -= int(p_item[1])
                                                        print("商品：%s已加入购物车，您的余额为：%s" % (p_item,balance))
                                                    else:
                                                        print("余额不足，买不起！")
                                                else:
                                                    print("您选择的商品编号：%s不存在！" % user_choose1)
                                            elif user_choose1 == "q":          # 退出并修改该用户数据文件中的账户余额
                                                with open("user_data","r+") as f:
                                                    new_str = ''
                                                    for line in f.readlines():
                                                        line = line.strip().split(":")
                                                        str = "%s:%s:%s:%s:%s\n" % (line[0],line[1],line[2],line[3],line[4])
                                                        if username in line:
                                                            line[4] = balance
                                                            str = "%s:%s:%s:%s:%s\n" % (line[0],line[1],line[2],line[3],line[4])
                                                        new_str += str
                                                with open("user_data","w") as new_f:
                                                    new_f.write(new_str)
                                                print("======购物清单======")
                                                for item_list in shopping_cart:
                                                    print(item_list)
                                                print("您的余额为：%s" % balance)
                                                sys.exit()
                                else:
                                    print("用户名或密码错误！")
                                    i += 1
                            else:
                                with open("user_data","r+") as user_line:
                                    new_line = ''
                                    for line in user_line.readlines():
                                        if username in line:
                                            line = line.replace("active","lock")
                                        new_line += line
                                with open("user_data","w") as f:
                                    f.write(new_line)
                                    print("密码输入错误3次，你的账户%s已锁定！" % username)
                                    sys.exit(1)
            if user_flag == False:
                print("用户名不存在！")
    if user_choose == "2":         # 进入商家入口
        user_flag = False
        while True:
            username = input("请输入您的用户名：").strip()
            with open("user_data",'r+') as userdata:         # 打开用户数据文件
                for userline in userdata.readlines():
                    userline = userline.strip().split(":")
                    if userline[0] == "g" and userline[1] == username:
                        if userline[3] == "lock":
                            print("用户:%s 已被锁定!" % username)
                            sys.exit(1)
                        elif userline[1] == username:
                            user_flag = True
                            i = 0
                            while i < 3:
                                password = input("请输入您的密码：")
                                if userline[2] == password:
                                    balance = int(userline[4])
                                    print("尊敬的用户：%s您好，欢迎登陆商家管理后台！" % username)
                                    menu = ["查看商品列表","修改商品价格","添加商品信息"]
                                    while True:
                                        with open("shopping_data","r+") as shopping_list:
                                            print("======功能列表======")
                                            for key,item in enumerate(menu,1):
                                                print("%s.%s" % (key,item))
                                            user_choose2 = input("请选择您需要的功能（输入q退出）：")
                                            if user_choose2 == "1":             # 查看商品列表功能
                                                print("======商品列表======")
                                                for key,item in enumerate(shopping_list,1):
                                                    item = item.strip().split(":")
                                                    product_list.append(item)
                                                    print("%s.%s" % (key,item))
                                            elif user_choose2 == "2":                 # 修改价格功能
                                                for key,item in enumerate(shopping_list,1):
                                                    item = item.strip().split(":")
                                                    product_list.append(item)
                                                    print("%s.%s" % (key,item))
                                                user_choose3 = input("请选择您要修改价格的商品：").strip()
                                                new_price = input("请输入您想修改的价格：").strip()
                                                if user_choose3.isdigit() and new_price.isdigit():
                                                    user_choose3 = int(user_choose3)
                                                    new_price = int(new_price)
                                                    if user_choose3 <= int(key) and user_choose3 > 0:
                                                        with open("shopping_data","r+") as f:
                                                            new_str = ''
                                                            for line in f.readlines():
                                                                line = line.strip().split(":")
                                                                str = "%s:%s\n" % (line[0],line[1])
                                                                if product_list[user_choose3 - 1][0] in line:
                                                                    line[1] = new_price
                                                                    str = "%s:%s\n" % (line[0],line[1])
                                                                new_str += str
                                                        with open("shopping_data","w") as new_f:
                                                            new_f.write(new_str)
                                                        print("商品：%s价格已修改为：%s" % (product_list[user_choose3 - 1],new_price))
                                            elif user_choose2 == "3":        # 添加商品功能
                                                add_flag = True
                                                while add_flag:
                                                    new_item = input("请输入您要添加的商品名：")
                                                    new_price = input("请输入该商品的价格：")
                                                    if new_price.isdigit():
                                                        new_price = int(new_price)
                                                        if new_price > 0:
                                                            new_str = "%s:%s\n" % (new_item,new_price)
                                                            with open("shopping_data","a") as f:
                                                                f.write(new_str)
                                                            print("商品：%s添加成功，价格为：%s" % (new_item,new_price))
                                                            user_choose4 = input("请问是否继续添加商品？（y/n）")
                                                            if user_choose4 == "y":
                                                                add_flag = True
                                                            elif user_choose4 == "n":
                                                                add_flag = False
                                                            else:
                                                                print("输入有误！")
                                                        else:
                                                            print("价格必须大于零！")
                                                    else:
                                                        print("价格仅支持输入数字！")
                                            elif user_choose2 == "q":
                                                print("退出成功。")
                                                sys.exit(0)
                                            else:
                                                print("您的输入有误，请重新输入！")
                                else:
                                    print("用户名或密码错误！")
                                    i += 1
                            else:
                                with open("user_data","r+") as user_line:
                                    new_line = ''
                                    for line in user_line.readlines():
                                        if username in line:
                                            line = line.replace("active","lock")
                                        new_line += line
                                with open("user_data","w") as f:
                                    f.write(new_line)
                                    print("密码输入错误3次，你的账户%s已锁定！" % username)
                                    sys.exit(1)
            if user_flag == False:
                print("用户名不存在！")
    else:
        print("输入有误，请重新输入：")
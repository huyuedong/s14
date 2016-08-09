#!/usr/bin/env python
#-*-coding:utf-8-*-
product_list = [
    ["iphone4s",1000],
    ["iphone5s",2000],
    ["iphone6s",3000],
    ["iphoneSE",4000],
    ["iphone7s",5000]
]
shoping_list = []
salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    while 1:
        for num,item in enumerate(product_list,1):
            print("%s.%s" % (num,item))
        user_chooise = input("你想买啥？选：")
        if user_chooise.isdigit():
            user_chooise = int(user_chooise)
            if user_chooise <= len(product_list) and user_chooise >=0:
                p_item = product_list[user_chooise-1]
                if salary >= p_item[1]:
                    shoping_list.append(p_item)
                    salary -= p_item[1]
                    print("Add %s to shoping cart,your current balance is %s" % (p_item[0],salary))
                else:
                    print("余额不足！")
            else:
                print("商品序号：%s不存在" % user_chooise)
        elif user_chooise == "q":
            print("------Shoping list------")
            for item in shoping_list:
                print(item)
            print("Your current balance is %s" % salary)
            quit()

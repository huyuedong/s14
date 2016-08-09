#!/usr/bin/env python
#-*-coding:utf-8-*-
product_list = [
    ["iPhone6s",5888],
    ["iPhone7",6888],
    ["Macbook Pro",12888],
    ["Macbook Air",7888],
    ["Apple Watch",2888],
    ["iPad",3888]
]
msg='''
 +------------------------+
 + Welcome to Apple Store +
 +------------------------+
'''
shoping_list = []
print(msg)
salary = input("Please input your salary:")
if salary.isdigit():
        salary = int(salary)
        while 1:
            for key,item in enumerate(product_list):
                print("%s.%s" % (key,item))
            user_choice = input("What are you want to buy?")
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice <= len(product_list) and user_choice >= 0:
                    p_item = product_list[user_choice]
                    if p_item[1] <= salary:
                        shoping_list.append(p_item)
                        salary -= p_item[1]
                        print("Add %s in shopping cart,your current balance is %s" % (p_item,salary))
                    else:
                        print("余额不足！！")
                else:
                    print("你选择的商品编号：%s 不存在" % user_choice)
            elif user_choice =="q":
                print("------Shoping List------")
                for item in shoping_list:
                    print(item)
                print("Your current balance is %s" % salary)
                exit()




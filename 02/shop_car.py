#!/usr/bin/env python
#-*-coding:utf-8-*-

msg = '''
----------Shopping Car----------
'''
product_list = [
    ["Mac",12000],
    ["iPhone",6888],
    ["bike",800],
    ["coffee",33],
]
shoping_list = []
salary = input("input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choise = input("What are you want to buy?")
        if user_choise.isdigit():
            user_choise = int(user_choise)
            if user_choise < len(product_list) and user_choise >= 0:
                p_item = product_list[user_choise]
                if p_item[1] <= salary:
                    shoping_list.append(p_item)
                    salary -= p_item[1]
                    print("Add %s in shoping catt,your current balance is %s" %(p_item[0],salary))
                else:
                    print("余额不足！！！")
            else:
                print("你选的商品序号：%s 不存在" % user_choise)
        elif user_choise == 'q':
            print("---shoping list---")
            for item in shoping_list:
                print(item)
            print("Your current balance is %s" % salary)
            exit()






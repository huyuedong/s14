#!/usr/bin/env python
#-*-coding:utf-8-*-

def layer():
    print("++++++++++++++++ 一级菜单 ++++++++++++++++")
    for index,key in enumerate(layer_menu.keys(),1):
        print(index,key)
        menu_key[str(key)] = key
    choose = input('请选择一级菜单！退出输入"q",返回请输入"b":')
    if choose == "q":
        quit()
    elif choose == "b":
        print('目前为一级菜单，无法返回，请重新输入')
        return
    elif menu_key.get(choose):
        layer2(menu_key[choose])
    else:
        print('\n输入有误，请重新输入！')

def layer1(choose1):
    while True:
        print("++++++++++++++++ 一级菜单 ++++++++++++++++")
        for index,key in enumerate(layer_menu[choose1].keys(),1):
            print(index,key)
            menu_key[str(index)] = key
        choose2 = input('请选择二级菜单！退出输入"q",返回请输入"b":')
        if choose2 == 'q':
            quit()
        elif choose2 == 'b':
            layer1()
        elif menu_key.get(choose2,0):
            layer2(choose2,menu_key[choose2])
        else:
            print('输入有误，请重新输入！')

def layer2(choose1,choose2):
    while True:
        print("++++++++++++++++ 一级菜单 ++++++++++++++++")
        for index,key in enumerate(layer_menu[choose1][choose2],1):
            print(index,key)
            menu_key[str(index)] = key
        choose3 = input('请选择三级菜单！退出输入"q",返回请输入"b":')
        if choose3 == 'q':
            quit()
        elif choose3 == 'b':
            layer1(choose1)
        else:
            print('输入有误，请重新输入！')

if __name__ == '__main__':
    layer_menu ={'中国':{'山东':['济南','临沂','青岛'],
                      '河北':['石家庄','秦皇岛']
                     },
             '美国':{'洛杉矶':['奥兰治县','河滨县','洛杉矶县'],
                      '纽约':['曼哈顿区','皇后区','布鲁克林区']
                     }
             }
    menu_key = {}
    while True:
        layer()









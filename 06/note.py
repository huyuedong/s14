#!/usr/bin/env python
#-*-coding:utf-8-*-

# 1.面向对象
# 把一个类变成一个具体对象的过程叫实例化

class Role(object):
    n = "我是类变量1"
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        self.name = name     # 实例变量
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def shot(self):
        print("shotting......")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self,gun_name):
        print("just bought %s" % gun_name)

    def show_status(self):
        print("name:%s  life_value:%s" % (self.name,self.__life_value))

    def __del__(self):
        '''
        析构函数
        :return:
        '''
        print("游戏结束")

# print(Role.n)
r1 = Role("huyd","police","AK47")
# r1.n = "我是类变量2"
# print(r1.n,r1.name)
r2 = Role("Alex","terrorist","B51")
# Role.n = "我是类变量3"
# print(r2.n,r2.name)

r1.show_status()
# print(r1.show_status())

# r1.shot()
# r1.got_shot()
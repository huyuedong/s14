#!/usr/bin/env python
#-*-coding:utf-8-*-

# class Prople   经典类(py2默认深度优先、py3经典类和新式类都是广度优先）
class People(object):    # 新式类（py2默认广度优先）
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eatting......" % self.name)

    def sleep(self):
        print("%s is sleeping......" % self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s is make friends with %s" % (self.name,obj.name))

class man(People,Relation):
    def __init__(self,name,age,money):
        # People.__init__(self,name,age)   # 继承构造方法01
        super(man,self).__init__(name,age)   # 继承构造方法02
        self.money = money
        print("%s 一出生就有%s钱" % (self.name,self.money))

    def piao(self):
        print("%s is piaoing......" % self.name)

    def sleep(self):
        People.sleep(self)
        print("man is sleeping")

class women(People,Relation):
    def shopping(self):
        print("%s is shopping......" % self.name)

m1 = man("shaolin",22,10)     # 实例化
w1 = women("sunli",33)
# m1.piao()
# w1.shopping()
# m1.sleep()

m1.make_friends(w1)
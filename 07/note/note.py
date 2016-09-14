#!/usr/bin/env python
#-*-coding:utf-8-*-

# 静态方法
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     @staticmethod
#     def eat(self):
#         print("%s is eating" % self.name)

# d1 = Dog("herry")  # 报错
# d1.eat(d1)  # 调用方法1
# 方法2： 在eat方法中去掉self参数，但这也意味着，在eat中不能通过self.调用实例中的其它变量了

# 类方法 @classmethod   ------   类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量

# 属性方法-----------属性方法的作用就是通过@property把一个方法变成一个静态属性
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print("%s is eating" % self.name)
#
# d2 = Dog("Jack Ma")
# d2.eat    # 不加（）才能正常调用

# 属性方法eg
# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print("%s is eating" % self.name)
#
#     @eat.setter
#     def eat(self,food):
#         print("set to food:",food)
#         self.__food = food
#
#     @eat.deleter
#     def eat(self):
#         del self.__food
#         print("删完了")
#
# d2 = Dog("刘德华")
# d2.eat
# d2.eat = "包子"
# del d2.eat

# 航班例子（属性方法）
# class Flight(object):
#     def __init__(self,name):
#         self.flight_name = name
#
#
#     def checking_status(self):
#         print("checking flight %s status " % self.flight_name)
#         return  0
#
#     @property
#     def flight_status(self):
#         status = self.checking_status()
#         if status == 0 :
#             print("flight got canceled...")
#         elif status == 1 :
#             print("flight is arrived...")
#         elif status == 2:
#             print("flight has departured already...")
#         else:
#             print("cannot confirm the flight status...,please check later")
#
#
# f = Flight("CA980")
# f.flight_status




class Flight(object):
    def __init__(self,name):
        self.flight_name = name

    def checking_status(self):
        print("checking flight %s status " % self.flight_name)
        return  1

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("flight got canceled...")
        elif status == 1 :
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter #修改
    def flight_status(self,status):
        status_dic = {
            0 : "canceled",
            1 :"arrived",
            2 : "departured"
        }
        print("\033[31;1mHas changed the flight status to \033[0m",status_dic.get(status) )

    @flight_status.deleter  #删除
    def flight_status(self):
        print("status got removed...")

f = Flight("CA980")
f.flight_status
f.flight_status =  0 #触发@flight_status.setter
del f.flight_status #触发@flight_status.deleter






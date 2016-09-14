#!/usr/bin/env python
#-*-coding:utf-8-*-

class People(object):   # 创建一个类：People
    def __init__(self,name,age):    # 父类的构造方法，实例化时自动执行。
        self.name = name
        self.age = age

    def show_info(self):   # 父类的方法
        print("%s is %s years old." % (self.name,self.age))

class Teacher(People):   # 创建一个类：Teacher，继承People类。
    def __init__(self,name,age,course):
        # People.__init__(self,name,age)   # 不推荐这么写
        super(Teacher,self).__init__(name,age)   # 推荐写法，在子类的构造方法里只出现子类的类名
        self.course = course

    def show_course(self):   # 定义一个方法
        print("Teacher:%s is teaching %s" % (self.name,self.course))   # 继承了父类的name属性

Jack = Teacher("Jack",33,"Python")   # 实例化一个老师：Jack
Jack.show_info()   # 调用父类的方法 output>> Jack is 33 years old.
Jack.show_course()   # 调用本类的方法 output>> Teacher:Jack is teaching Python


# 多继承

class D(object):
    def bar(self):
        print ('D.bar')

class C(D):
    def bar(self):
        print ('C.bar')

class B(D):
    def bar(self):
        print ('B.bar')

class A(B, C):
    def bar(self):
        print ('A.bar')

a = A()
a.bar()

# 多态

class F1:
    pass


class S1(F1):

    def show(self):
        print ('S1.show')


class S2(F1):

    def show(self):
        print ('S2.show')

def Func(obj):
    print (obj.show())

s1_obj = S1()
Func(s1_obj)

s2_obj = S2()
Func(s2_obj)

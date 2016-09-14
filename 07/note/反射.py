#!/usr/bin/env python
#-*-coding:utf-8-*-

def bulk(self):
    print("%s is bulk......" % self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s" % (self.name,food) )

d1 = Dog("shaolin")
choose = input(">>>:")
if hasattr(d1,choose):
    delattr(d1,choose)
    foo = getattr(d1,choose)
    foo("xxx")
else:
    # setattr(d1,choose,bulk)
    # d1.talk(d1)
    # val = getattr(d1,choose)
    # val(d1)
    setattr(d1,choose,22)
    foo = getattr(d1,choose)
    print(foo)
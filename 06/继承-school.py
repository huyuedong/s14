#!/usr/bin/env python
#-*-coding:utf-8-*-

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
    def enroll(self,stu_obj):
        print("为学员%s办理注册手续" % (stu_obj.name))
    def hire(self,staff_obj):
        print("雇佣新员工：%s" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("%s is talking......." % self.name)

    def teach(self):
        print("%s is teaching course [%s]" % (self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print('''
        ---info of Student:%s---
        Name:%s
        Age:%s
        Sex:%s
        Stu_id;%s
        Grade:%s
        ''' % (self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tution for $%s" % (self.name,amount))

School = School("清华大学","北京")

t1 = Teacher("刘德华",44,"Man",5000,"Music")
t2 = Teacher("邵林",22,"Man",4000,"武术")

s1 = Student("胡越东",22,"man",1001,"Python")
s2 = Student("学生2",22,"man",1002,"Python3")

t1.tell()
School.enroll(s1)
School.hire(t2)


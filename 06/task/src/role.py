#!/usr/bin/env python
#-*-coding:utf-8-*-

# 定义一个学校类
class School(object):
    def __init__(self,school_name,addr):
        self.school_name = school_name
        self.addr = addr

    # 创建班级方法
    def Create_grade(self):
        print("\033[32m【班级创建成功】\n班级：%s  课程：%s  校区：%s\033[0m" % (self.grade_name,self.course_name,self.addr))

    # 创建讲师方法
    def Create_teacher(self):
        print("\033[32m【讲师信息创建成功】\n姓名：%s\n课程：%s\n学校：%s\n校区：%s\033[0m" % (self.name,self.course_name,self.school_name,self.school_name))

    # 创建课程方法
    def Create_course(self,course_obj):
        pass

# 定义一个班级类
class Grade(School):
    def __init__(self,school_name,addr,course_name,grade_name):
        super(Grade,self).__init__(school_name,addr)
        self.course_name = course_name
        self.grade_name = grade_name

# 定义一个课程类
class Course(School):
    def __init__(self,school_name,addr,course_name,cycle,tuition):
        super(Course,self).__init__(school_name,addr)
        self.course_name = course_name
        self.cycle = cycle
        self.tuition = tuition

# 定义一个学校成员类
class SchoolMember(object):
    def __init__(self,name):
        self.name = name

# 定义一个讲师类
class Teacher(SchoolMember,School):
    def __init__(self,name,school_name,addr,course_name):
        # super(Teacher,self).__init__(name,school_name,addr) 这样写不对？
        SchoolMember.__init__(self,name)
        School.__init__(self,school_name,addr)
        self.course_name = course_name

    # 查看班级方法
    def Show_grade(self):
        pass

    # 查看学生列表方法
    def Show_student(self):
        pass

# 定义一个学生类
class Student(SchoolMember):
    def __init__(self,name,tuition,grade,report):
        super(Student,self).__init__(name)
        self.tuition = tuition
        self.grade = grade
        self.report = report

    # 注册方法(创建学员)
    def Register(self):
        pass

    # 学员报名缴费方法
    def Pay(self):
        pass

    # 选择班级方法
    def Choose_grade(self):
        pass





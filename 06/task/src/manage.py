#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,sys,time
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

import role
import db_handle
import db_save
from conf import settings

school1 = role.School("蓝翔技校","北京校区")
school2 = role.School("蓝翔技校","上海校区")
course1 = role.Course("蓝翔技校","北京","Linux","1年","12800")
course2 = role.Course("蓝翔技校","北京","Python","1年","16800")
course3 = role.Course("蓝翔技校","上海","Go","2年","18800")
school_dic = {"北京校区":{"school_name":"蓝翔技校","addr":"北京校区"},
              "上海校区":{"school_name":"蓝翔技校","addr":"上海校区"}
              }
course_dic = {"Linux":{"school_name":"蓝翔技校","addr":"北京","course_name":"Linux","cycle":"1年","tuition":"12800"},
              "Python":{"school_name":"蓝翔技校","addr":"北京","course_name":"Python","cycle":"1年","tuition":"16800"},
              "Go":{"school_name":"蓝翔技校","addr":"上海","course_name":"Go","cycle":"2年","tuition":"18800"}
              }
grade_dic = {}
teacher_dic = {}

# 学校视图
def School():
    menu = '''
    \033[46m【学校管理系统】\033[0m
    1.新建班级
    2.新建讲师
    3.新建课程
    '''
    menu_dic = {
        "1":{"option":"新建班级","action":role.School.Create_grade},
        "2":{"option":"新建讲师","action":role.School.Create_teacher},
        "3":{"option":"新建课程","action":role.School.Create_course},
    }
    while True:
        print(menu)
        user_choose = input(">>>:")
        if user_choose == "1":
            print("\033[46m--------------------新建班级页面--------------------\033[0m")
            menu1 = "\033[34m学校名称：%s\t校区地址：1.%s 2.%s\033[0m" % (school1.school_name,school1.addr,school2.addr)
            print(menu1)
            flag = True
            while flag:
                school_option = input("请选择校区：").strip()
                if school_option == "1":
                    school_name = school1.school_name
                    addr = school1.addr
                    flag1 = True
                    while flag1:
                        print("\033[34m课程名称：1.%s 2.%s\033[0m" % (course1.course_name,course2.course_name))
                        course_option = input("请选择课程：").strip()
                        if course_option == "1":
                            course_name = course1.course_name
                            flag1 = False
                        elif course_option == "2":
                            course_name = course2.course_name
                            flag1 = False
                        else:
                            print("该校区没有您选择的课程选项，请重新选择。")
                    flag = False
                elif school_option == "2":
                    school_name = school2.school_name
                    addr = school2.addr
                    course_name = course3.course_name
                    flag = False
                else:
                    print("您选择的校区不存在")
            grade_name = input("班级名称:").strip()
            g1 = role.Grade(school_name,addr,course_name,grade_name)
            grade_dic[g1.grade_name] = {"school_name":g1.school_name,"addr":g1.addr,"course_name":g1.course_name,"grade_name":g1.grade_name}
            menu_dic[user_choose]["action"](g1)
            data_save(grade_dic)
            flag = False
        elif user_choose == "2":
            print("---新建讲师页面---")
            name = input("请输入姓名：").strip()
            flag2 = False
            while not flag2:
                print("1.Linux  2.Python  3.Go")
                course_option = input("请选择课程：")
                if course_option == "1":
                    school_name = course_dic["Linux"]["school_name"]
                    addr = course_dic["Linux"]["addr"]
                    course_name = "Linux"
                    flag2 = True
                elif course_option == "2":
                    school_name = course_dic["Python"]["school_name"]
                    addr = course_dic["Python"]["addr"]
                    course_name = "Python"
                    flag2 = True
                elif course_option == "3":
                    school_name = course_dic["Go"]["school_name"]
                    addr = course_dic["Go"]["addr"]
                    course_name = "Go"
                    flag2 = True
                else:
                    print("没有该选项啊，哥！")
        elif user_choose == "3":
            print("不要意思，新建课程功能我也没写完，哭......")
            flag = False
        else:
            print("选项不存在")
            flag = True

            t1 = role.Teacher(name,school_name,addr,course_name)
            teacher_dic[t1.name] = {"name":t1.name,"school_name":t1.school_name,"addr":t1.addr,"course_name":t1.course_name}
            menu_dic[user_choose]["action"](t1)
            data_save(teacher_dic)

def Teacher():
    print("不好意思哈，讲师管理系统我还没写完......")

def Student():
    print("不好意思哈，学生管理系统我还没写完......")

# 存档方法
def data_save(data):
    file_name = time.strftime('%Y%m%d_%H%M%S', time.gmtime(time.time()))
    db_path = db_handle.handle(settings.DATABASE, file_name)
    db_save.write(db_path,data)
    print("已存档：%s" % data)


def run():
    menu = '''
    \033[46m山东蓝翔高级技工学校管理系统\033[0m
    1.学校    2.讲师     3.学生
    '''
    menu_dic = {
        "1":School,
        "2":Teacher,
        "3":Student
    }
    while True:
        print(menu)
        menu_option = input("请选择您要进入的系统：").strip()
        if menu_option in menu_dic:
            menu_dic[menu_option]()
        else:
            print("\033[31m选项不存在\033[0m")



#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
#    -.-    coding: utf-8    -.-
# by sandler
import sys
welcome = '''
    ******************************************************************
    *                                                                *
    *                    \033[31m欢迎进入地区信息浏览系统\033[0m                    *
    *                                                                *
    ******************************************************************
                                                      \033[31m退出请按Q\033[0m
'''
index_dic = {
    "天津":{
        "和平区":["小白楼","劝业场","体育馆"],
        "河西区":["挂甲寺","桃园","大营门"]
    },
    "北京":{
        "海淀区":["中关村","五道口","上地"],
        "朝阳区":["安贞","国贸","管庄"]
    },
    "河北":{
        "保定":["徐水区","竞秀区","满城区"],
        "石家庄":["新华区","长安区","裕华区"]
    }
}
print(welcome)

for i in index_dic:
    print(i)    #打印第一层菜单
print ("-------------------------------------------------")
for i in range(3):
    shi_input = input("请输入你要查看的地区名字,按q退出: ")
    if shi_input == "q":    #判断用户输入是否为“q”，
        sys.exit(0) #用户输入“q”退出
    if shi_input in index_dic:
        qu_name = index_dic[shi_input]
        jd_name = qu_name.keys()
        while True:
            for i in jd_name:   #遍历列表，取出地区名字
                print (i)   #打印第二层菜单
            qu_input = input("请输入你要查看的区名字，按b返回，按q退出: ")
            if qu_name == "q":
                sys.exit(0)
            if qu_input in jd_name: #判断用户输入是否在列表中
                shi_name = index_dic[shi_input][qu_input]
                for i in shi_name:
                    print (i)   #打印第三层菜单

            if qu_input not in jd_name: #判断输入是否在列表中
                print ("您输入的信息有误，请重新输入: ")
                continue
            back_or_quit = input("已到最后，按b:Back是返回上一级菜单;按q:Exit是退出整个程序: ")
            if back_or_quit == "q":
                sys.exit(0)
                break
            if back_or_quit == "b":
                continue
            print ("您输入的信息有误，请重新输入: ")
else:
    print ("3次输入错误，程序退出")

多级菜单
#!/usr/bin/env python
#-*-coding:utf-8-*-
import pymysql

conn = pymysql.connect(host="192.168.92.201",port=3306,user='root',passwd='123456',db='test')
cursor = conn.cursor()

test = cursor.execute("select * from class")

show = cursor.fetchall()
print(show)
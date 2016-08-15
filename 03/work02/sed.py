#!/usr/bin/env python
#-*-coding:utf-8-*-
import os

def sed(old,new):
    with open('data','r',encoding="utf-8") as f_read, open('data.temp','w',encoding="utf-8") as f_write:
        for line in f_read:
            if old in line:
                line = line.replace(old,new)
            f_write.write(line)
    os.replace('data.temp','data')
    print("\033[31m[%s]\033[0m已成功替换成\033[31m[%s]\033[0m" %(old,new))

if __name__ == "__main__":
    old = input("输入你想替换的内容：")
    new = input("输入你想把\033[31m[%s]\033[0m替换成什么内容：" % old)
    sed(old,new)
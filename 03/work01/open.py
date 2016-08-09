#!/usr/bin/env python
#-*-coding:utf-8-*-
import json,os

def fetch(backend):
    backend_title = 'backend %s' % backend
    record_list = []
    with open('haproxy.conf','r') as f:
        flag = False
        for line in f:
            line = line.strip()
            if line == backend_title:
                flag = True
                continue
            if flag and line.startswith('backend'):
                flag = False
                break
            if flag and line:
                record_list.append(line)
                for i in record_list:
                    print(i)
                    exit()
    # return record_list

if __name__ == '__main__':
    print('1.获取；2.添加；3.删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    if num == '1':
        fetch(data)
    else:
        pass

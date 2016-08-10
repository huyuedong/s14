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
    return record_list

def add(dict_info):
    backend = dict_info.get("backend")
    backend_title = "backend %s" % backend
    record_list = fetch(backend)
    current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'],dict_info['record']['server'],dict_info['record']['weight'],dict_info['record']['maxconn'])
    if not record_list:
        record_list.append(backend_title)
        record_list.append(current_record)
        with open('haproxy.conf') as read_file,open('haproxy.new','w') as write_file:
            flag = False
            for line in read_file:
                write_file.write(line)
            for i in record_list:
                if i.startswith('backend'):
                    write_file.write(i+'\n')
                else:
                    write_file.write("%s%s\n" % (8*" ",i))
    else:
        record_list.insert(0,backend_title)
        if current_record not in record_list:
            record_list.append(current_record)

        with open('haproxy.conf') as read_file,open('haproxy.new','w') as write_file:
            flag = False
            has_write = False
            for line in read_file:
                line_strip = line.strip()
                if line_strip == backend_title:
                    flag = True
                    continue
                if flag and line_strip.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(line)
                else:
                    if not has_write:
                        for i in record_list:
                            if i.startswith('backend'):
                                write_file.write(i+'\n')
                            else:
                                write_file.write("%s%s\n" % (8*" ", i))
                    has_write = True
    os.rename('haproxy.conf','haproxy.conf.bak')
    os.rename('haproxy.new','haproxy.conf')



if __name__ == '__main__':
    print('1.获取；2.添加；3.删除')
    num = input('请输入序号：')
    data = input('请输入内容：')
    if num == '1':
        record_list = fetch(data)
        for i in record_list:
            print(i)
            exit()
    else:
        dict_data = json.loads(data)
        add(dict_data)

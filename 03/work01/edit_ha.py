#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,json

def get(backend):
    result = []
    with open('haproxy.conf','r') as f:
        flag = False
        for line in f:
            if line.strip().startswith("backend") and line.strip() == "backend %s" % backend:
                flag = True
                continue
            if flag == True and line.strip().startswith("backend"):
                flag = False
                break
            if flag == True and line.strip():
                result.append(line.strip())
    return result

def add(backend,record):
    record_list = get(backend)
    # backend 不存在时：
    if not record_list:
        with open('haproxy.conf','r') as f_read, open('haproxy.new','w') as f_write:
            for line in f_read:
                f_write.write(line)
            f_write.write("\nbackend %s\n" % backend)
            f_write.write(" " * 8 + '%s \n' % record)
    else:
        # backend 存在时:
        if record in record_list:
            # record 已经存在
            pass
        else:
            # record 不存在
            record_list.append(record)
            with open('haproxy.conf','r') as f_read, open('haproxy.new','w') as f_write:
                flag = False
                for line in f_read:
                    if line.strip().startswith('backend') and line.strip() == "backend %s" % backend:
                        flag = True
                        f_write.write(line)
                        for i in record_list:
                            f_write.write(" "*8 + '%s\n' % i)
                        continue
                    if flag and line.strip().startswith("backend"):
                        flag = False
                    if flag:
                        pass
                    else:
                        f_write.write(line)
    os.replace('haproxy.new','haproxy.conf')

def remove(backend,record):
    record_list = get(backend)
    if record_list:
        pass
    else:
        print("您要删除的记录不存在！")
        exit()


if __name__ == "__main__":
    while True:
        print("HAProxy配置菜单：\n1.查找\n2.添加\n3.删除")
        user_choose = input("请输入您要操作的序号：")
        if user_choose == "1":
            data = input("请输入域名（eg:www.oldboy.org）：")
            a = get(data)
            str = a[0],"\n",a[1]
            print(str)
        elif user_choose == "2":
            data = input("请输入要添加的内容：")
            dic_data = json.loads(data)
            backend = dic_data.get("backend")
            record = "server %s %s weight %s maxconn %s" % (dic_data["record"]["server"],
                                                            dic_data["record"]["server"],
                                                            dic_data["record"]["weight"],
                                                            dic_data["record"]["maxconn"])
            add(backend,record)
        elif user_choose == "3":
            data = input("请输入要删除的内容：")
            dic_data = json.loads(data)
            backend = dic_data.get("backend")
            record = "server %s %s weight %s maxconn %s" % (dic_data["record"]["server"],
                                                            dic_data["record"]["server"],
                                                            dic_data["record"]["weight"],
                                                            dic_data["record"]["maxconn"])
            remove(backend,record)
        else:
            print("输入有误,请重新输入！")

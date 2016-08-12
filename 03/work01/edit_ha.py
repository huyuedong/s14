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
            f_write.write('%s%s\n' % (" " * 8,record))
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
                            f_write.write('%s%s\n' % (" "*8,i))
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
    backend_title = "backend %s" % backend
    if record_list:
        if record not in record_list:
            print("\033[31m你输入的内容不存在。\033[0m")
            return
        else:
            record_list.remove(record)
        with open('haproxy.conf','r') as f_read, open('haproxy.new','w') as f_write:
            flag = False
            for line in f_read:
                if line.strip() == backend_title:
                    f_write.write(line)
                    flag = True
                    continue
                if flag == True and line.startswith("backend"):
                    flag = False
                if flag == True:
                    for new_line in record_list:
                        new_record = "%s%s\n" % (" "*8,new_line)
                        f_write.write(new_record)
                else:
                    f_write.write(line)
    else:
        print("\033[31m您要删除的记录不存在！\033[0m")
        return
    os.replace('haproxy.new','haproxy.conf')


if __name__ == "__main__":
    while True:
        print("\033[47mHAProxy配置菜单：\033[0m\n1.查找\n2.添加\n3.删除\nq.退出")
        user_choose = input("\033[31m请输入您要操作的序号：\033[0m")
        if user_choose == "1":
            data = input("\033[31m请输入域名（eg:www.oldboy.org）：\033[0m")
            a = get(data)
            print(a)
        elif user_choose == "2":
            data = input("\033[31m请输入要添加的内容：\033[0m")
            dic_data = json.loads(data)
            backend = dic_data.get("backend")
            record = "server %s %s weight %s maxconn %s" % (dic_data["record"]["server"],
                                                            dic_data["record"]["server"],
                                                            dic_data["record"]["weight"],
                                                            dic_data["record"]["maxconn"])
            add(backend,record)
        elif user_choose == "3":
            data = input("\033[31m请输入要删除的内容：\033[0m")
            dic_data = json.loads(data)
            backend = dic_data["backend"]
            record = "server %s %s weight %s maxconn %s" % (dic_data["record"]["server"],
                                                            dic_data["record"]["server"],
                                                            dic_data["record"]["weight"],
                                                            dic_data["record"]["maxconn"])
            remove(backend,record)
        elif user_choose == "q":
            quit()
        else:
            print("\033[31m输入有误,请重新输入！\033[0m")

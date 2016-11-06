#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

server_list = {
    'group1':{
        "server1":{"IP":"192.168.92.100","user":"huyd","password":"hu7yue","port":22},
        "server2":{"IP":"192.168.92.101","user":"root","password":"xxxxxx","port":22}
    },
    'group2':{
        "server1":{"IP":"192.168.92.103","user":"huyd","password":"hu7yue","port":22},
        "server2":{"IP":"192.168.92.104","user":"root","password":"xxxxxx","port":22}
    }
}


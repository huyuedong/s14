#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import cmd
from conf import setting

if __name__ == '__main__':
    # cmd.main()
    server = setting.server_list
    print(server["group1"][""])
#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

# 数据存放设置
DATABASE = {
    'engine':'file',
    'path':'%s' % os.path.join(BASE_PATH,"db")
}

# INFO = {
#     "School":{"name":"蓝翔技校",
#                "addr":("北京","山东")},
#     "Teacher":{"1":{"name":"苍井井","age":18,"sex":"F"},
#                 "2":{"name":"唐僧","age":99,"sex":"M","course":"挖掘机"}
#     }
# }

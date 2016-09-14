#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用户信息目录
USER_INFO_DIR = os.path.join(BASE_PATH,"db")

# 管理员信息目录
ADMIN_INFO_DIR = os.path.join(BASE_PATH,"db","admin")

# 利息设置
interest = 0.05


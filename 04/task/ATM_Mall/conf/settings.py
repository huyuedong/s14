#!/usr/bin/env python
#-*-coding:utf-8-*-
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# USER_INFO_DIR = "{}\\db".format(BASE_PATH)
USER_INFO_DIR = os.path.join(BASE_PATH,"db")
ADMIN_INFO_DIR = os.path.join(BASE_PATH,"db","admin")

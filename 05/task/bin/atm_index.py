#!/usr/bin/env python
#-*-coding:utf-8-*-

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings
from src import atm

if __name__ == '__main__':
    atm.run()
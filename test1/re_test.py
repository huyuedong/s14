#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/python
#coding:utf-8
import re
demo_str='''/dev/xvda1     ext4       20G  7.6G   11G  41% /
devtmpfs       devtmpfs  489M     0  489M   0% /dev
tmpfs          tmpfs     497M     0  497M   0% /dev/shm
tmpfs          tmpfs     497M   51M  447M  11% /run
tmpfs          tmpfs     497M     0  497M   0% /sys/fs/cgroup
'''
pattern=re.compile('(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+(.*?)\s+')
items=re.findall(pattern, demo_str)
for item in items:
    print item

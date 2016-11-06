#!/usr/bin/env python
#-*-coding:utf-8-*-
from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all()   # 把当前所有IO操作打上标记

def f(url):
    print("GET:%s" % url)
    resp = request.urlopen(url)
    data = resp.read()
    # with open("a.html","wb") as d:
    #     d.write(data)
    print('%d bytes received from %s' % (len(data),url))

# urls = [
#     'https://www.python.org/',
#     'http://www.heika.com/',
#     'https://github.com/'
# ]

# start_time = time.time()
# for url in urls:
#     f(url)
# print("同步cost时间：",time.time() - start_time)

async_start_time = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'http://www.heika.com/'),
    gevent.spawn(f,'https://github.com/'),
])
print("异步cost时间：",time.time() - async_start_time)
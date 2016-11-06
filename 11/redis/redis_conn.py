#!/usr/bin/env python
#-*-coding:utf-8-*-
import redis

# r = redis.Redis(host='192.168.92.201',port=6379)
# r.set('name','hxxxxxxx')
# print(r.get('name'))

pool = redis.ConnectionPool(host='192.168.92.201', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print (r.get('foo'))
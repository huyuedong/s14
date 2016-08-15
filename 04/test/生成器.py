#!/usr/bin/env python
#-*-coding:utf-8-*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1
    return "----done----"

f = fib(10)

# for i in f:
#     print(i)

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

while True:
    try:
        x = next(f)
        print('g:',x)
    except StopAsyncIteration as e:
        print("Generator return value:",e.value)
        break









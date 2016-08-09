#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
age = [123]
name.extend(age)
name.insert(-1,"huyuedong")
name2 = name[4:15]
name2.reverse()
name2.sort()
print(name)
name[-2] = "(Leader)huyuedong"
print (name[::2])
counter = name.index(3,4)
print(counter)


name = ["Jack","Lily","Lucy","James",1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
a = name.count(3)
b = name.count(4)

for i in range(name.count(a+b)):
    ele_index = name.index(3,4)
    name.pop(ele_index)
print(name)


for i in range(name.count(3)):
    counter = name.index(3)
    name[counter] = 33333333
    print(counter)


username = input("User:")
if username.strip() == 'huyd':
    print("Welcome")
'''
'''
name = "alex,huyd,james"
name2 = name.split(",")
print("|".join(name2))

username = "david hu"
print(' ' in username)
print(username.capitalize())

msg = "Hello,My name is {name},is's {age} years old!"
#msg2 = msg.format(name='David',age=12)
#print(msg2)

msg2 = "name{0},age{1}"
print(msg2.format('Alex',33))     #字符串格式化2
'''

name = "David"
age = "22"

print (name.center(40,'-'))  #字符串总长度为40，居中显示，不够的地方以“-”填充
print (name.find('i'))       #找到返回索引，找不到返回-1
print (age.isdigit())        #判断是否为数字
print (age.isalnum())        #判断是否为阿拉伯数字，懵逼。
print (name.endswith('vid')) #判断是否以vid结尾。
print (name.startswith("Da"))  #判断是否以Da开头。
print (name.upper())         #将name全部转为大写字母。
print (name.lower())         #将name全部转为小写字母。



list = ['David','huyd','huyd','James','Lily']
list2 = [1,2,3]
list.insert(0,"huyd")
print(list)











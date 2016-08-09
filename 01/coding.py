#!/usr/bin/env python
#-*-coding:utf-8-*-

### 字符串格式化 ###
name = input("Username:")
age = input("Age:")
job = input("Job:")
salary = input("Salary:")

info1='''
----------Info1 Of %s-----------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,age,job,salary)

info2='''
---------info2 of {_name}----------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)

info3='''
-----------info3 of {0}-------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print(info1,info2,info3)

### 初识模块 ###
#getpass

### 用户名密码登录 ###

### 猜大小 ###
age_of_shaolin = 30
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_shaolin:
        print("Yes! You got it!")
        break
    elif guess_age > age_of_shaolin:
        print("Think little!")
    else:
        print("Think bigger!")
    count += 1
    if count == 3:
        countinue_confirm = input("Do you want to continue?(*/n)")
        if countinue_confirm != "n":
            count = 0
        else:
            break
# else:
#     print("You have tried too many times!fuck off!")

###







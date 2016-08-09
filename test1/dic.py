#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
dics = {"jay":100,"huyd":99,"james":98}
print (dics["james"])
print ("huyd" in dics)
'''
dic1 = {
        2:{
            "test":123456
        }
}
dic2 = {
    1:{
        "huyd":120,"james":190,"lebron":200
    },
    2:{
        "liuyifei":111,"jay":199,"test":999
    }
}

#print(dic2)
#print(dic2[1]["huyd"])         #获取元素

#dic2[1]["huyd"] = 66666666     #修改元素
#dic2[1]["qq"] = 1111111        #添加元素，和修改一样，如果要修改的元素不存在则添加。
#del dic2[1]["james"]          #删除元素
#dic2[1].pop("huyd")            #删除元素
#print(dic2[1])                  #获取元素，如果key不存在会报错。
#print(dic2.get(2))              #获取元素
#dic2.update(dic1)               #使用dic1里面的元素更新dic2
#print(dic2.items())             #将字典转换为列表，大数据时不建议用。
#print(dic2.values())            #打印该字典中所有的values
#print(dic2.keys())              #打印该字典中所有的keys
#print(1 in dic2)               #判断是否包含该key或元素
#print(dic2[1].setdefault("huydd",3333333))   #取一个值，如果不存在，就设置一个默认的k v值
#print(dic2.fromkeys([1,2,3,4,5,6],'yyyyy'))  #大坑
#print(dic2)
#print(dic2.popitem())        #随机删除，不要用。

for k,v in dic2.items():     #效率低
    print(k,v)

for key in dic2:              #效率高
    print(key,dic2[key])

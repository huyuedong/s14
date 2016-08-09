#!/usr/bin/env python
#-*-coding:utf-8-*-
# 模块初识
import sys,os,copy
# print("sys.path-->",sys.path)
# print("sys.argv-->",sys.argv)

# print("os.system-->",os.system('dir'))
# cmd_res = os.system('dir')
# print('cmd_res-->',cmd_res)

# cmd_res = os.popen('dir').read()
# print(cmd_res)

# os.mkdir('aa')
# os.makedirs('bb/cc')

# 自定义模块

# pyc是什么

# 数据类型初识
'''
数字
a,b = 10,100
a << 1 = 20    # a*2
a >> 1 = 5     # a/2

# 三元运算
result = 值1 if 条件 else 值2
如果条件为真：result = 值1
如果条件为假：result = 值2
eg:
a,b = 1,2
c = a if a > b else b
print(c)


# bytes类型
name = '刘德华'
bytes_a = name.encode(encoding='utf-8'   # str to bytes
str_a = bytes_a.decode(encoding='utf-8') # bytes to str

# 列表
names = ["zhangyang",'xiangpeng','shaolin','liudehua']
print (names)
print (names[0:2])    #切片：顾头不顾尾
print (names[-1])     #切片：取出最后一个
print (names[-2:])    #切片：取出最后两个
print (names[:])      #切片：取出所有
names.append("jay")   #追加
names.insert(1,"Huyd")#指定位置插入
names[2] = "xiugai"   #修改
names.count("chenronghua")
names2 = [1,2,3,4]
names.extend(names2)  # 合并
name.copy()    #浅复制，引用
name.deepcopy()#深复制，重新生成一块内存
# 循环
names1 = ["zhangyang",'xiangpeng','shaolin',['aaa','bbb'],'liudehua']
for i in names1[::2]:
    print(i)
'''
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
info['stu1104'] = "Cang Jingkong"
info['stu1101'] = "武藤兰"
# 删除
# info.pop('stu1104')
# del info['stu1101']
# info.popitem()
# 查找
# if "stu1103" in info:
#     print("Yes")
# else:
#     print("No!")

# print(info.get('stu1104'))  #获取，不存在返回None
# print(info['stu1104'])  #同上，但是不存在会报错
# print(info)

#多级字典嵌套及操作
# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# av_catalog["大陆"]["1024"][1] += ",爬虫"
# print(av_catalog["大陆"]["1024"])
# print(info)
# info.setdefault("stu1105","James")
# print(info)

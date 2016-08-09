#!/usr/bin/env python
#-*-coding:utf-8-*-
#!/usr/bin/env python
#-*-coding:utf-8-*-

#coding:utf-8
layer_menu ={'中国':{'山东':['济南','临沂','青岛'],
                      '河北':['石家庄','秦皇岛','沧州'],
                      '北京':['朝阳区','海淀区','丰台区']
                     },
             '美国':{'洛杉矶':['奥兰治县','河滨县','洛杉矶县'],
                      '纽约':['曼哈顿区','皇后区','布鲁克林区'],
                     },
             '日本':{'东京':['千代田区','中央区','港区'],
                      '大阪':['都岛区','福岛区','此花区']
                    }
             }
'''
定义一个list 来存储选择的菜单
0 ： 选择的一级菜单
1 : 选择的二级菜单
2 : 选择的三级菜单
最开始,一个都没选择,所以3个值都是空的
'''
choice = ['','','']
try:
    while True:
        '''如果1级菜单没选择的时候,0肯定是空的.所以这时候把1级菜单的东西显示出来'''
        if choice[0] == '':
            for i in layer_menu:
                print(i)
        elif choice[1] =='':
            for i in layer_menu[choice[0]]:
                print(i)
        elif choice[2] =='':
            for i in layer_menu[choice[0]][choice[1]]:
                print(i)
        print('f:返回一级菜单，b:返回二级菜单，其他(q)：退出')
        choice_input = input('请输入要进入的菜单：')

        if choice_input == 'f':
            choice[0] =''
            choice[1] =''
            choice[2] =''
        elif choice_input == 'b':
            choice[1] =''
            choice[2] =''
        else:
            choice[choice.index('')] = choice_input
except:
    pass



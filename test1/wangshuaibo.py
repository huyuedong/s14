# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# #coding:utf-8
# import os
# user_file='%s/user.txt' % (os.path.dirname(__file__))
# def ShopCar(user,gold,shop_car):
# 	buy_flag=True
# 	while buy_flag:
# 		shop_index=0
# 		shop_car_index=0
# 		shop_list=[u'香蕉',u'橘子',u'苹果',u'iPhone']
# 		shop_price=['1','2','5','3000']
# 		print u'''
# 	--------------------------------------------
# 	商品列表
# 	物品编号	物品名称	物品价格
# 	'''
# 		while shop_index <len(shop_list):
# 			print u'\t%s\t\t%s\t\t%s'%(shop_index,shop_list[shop_index],shop_price[shop_index])
# 			shop_index=shop_index+1
# 		print u"""
# 	顾客:%s\t现金:%s
# 	输入要购买商品的编号或者输入00退出,输入9XX可以从购物车中删除
# 		""" %(user,gold)
# 		buy_shop_index=input('\tInput:')
# 		print u"""
# 	已购物清单
# 		"""
# 		try:
# 			if buy_shop_index=='00':
# 				exit()
# 			elif buy_shop_index>=900:
# 				del shop_car[(buy_shop_index-900)]
# 				gold=gold+int(shop_price[(buy_shop_index-900)])
# 				print u'\t%s已经删除' % shop_list[(buy_shop_index-900)]
# 				continue
# 			if gold < int(shop_price[buy_shop_index]):
# 				print u'\t买不起%s' % shop_list[buy_shop_index]
# 				continue
# 			shop_car.append(shop_list[buy_shop_index])
# 			gold=gold-int(shop_price[buy_shop_index])
# 		#for i in shop_car:
# 		#	print '\t\t%s' % i.index()
# 		finally:
# 			while shop_car_index <len(shop_car):
# 				print u'\t%s\t%s'%(shop_car_index,shop_car[shop_car_index])
# 				shop_car_index+=1
# def menu(user):
# 	print u'''
# 	--------------------------------------------
# 	欢迎 %s
# 	1.购物车程序
# 	输入要进入的程序编号,其他输入退出程序
# 	''' % user
# 	choice_menu=input('Input:')
# 	if choice_menu ==1:
# 		ShopCar(user)
# 	else:
# 		exit()
# def Login(user,passwd):
# 	f_user.seek(0,0);
# 	for user_line in f_user.readlines():
# 		u=user_line.strip().split(':')
# 		if u[0]==user and u[1]==passwd:
# 			return True
# 			exit()
# 	return False
# def Lock(user,retry):
# 	f_user.seek(0,0);
# 	user_retry_num=0
# 	u_str=''
# 	for user_line in f_user.readlines():
# 		u=user_line.strip().split(':')
# 		if retry:
# 			if u[0]==user:
# 				if  int(u[2])<3:
# 					u_str='%s%s:%s:%s\n' %(u_str,u[0],u[1],(int(u[2])+1))
# 				else:
# 					u_str='%s%s:%s:%s\n' %(u_str,u[0],u[1],u[2])
# 				user_retry_num=int(u[2])
# 			else:
# 				u_str='%s%s:%s:%s\n' %(u_str,u[0],u[1],u[2])
# 		else:
# 			if u[0]==user and int(u[2])>=3:
# 				return True
# 				exit()
# 	if retry:
# 		f=file(user_file,'wb')
# 		f.write(u_str)
# 		f.close()
# 		return 3-user_retry_num
# 	else:
# 		return False
# def CheckUser(user):
# 	f_user.seek(0,0);
# 	for user_line in f_user.readlines():
# 		u=user_line.strip().split(':')
# 		if u[0]==user:
# 			return True
# 			exit()
# 	return False
# def main():
# 	user=raw_input('Login UserName:')
# 	if CheckUser(user) ==False:
# 		print u'用户%s 不存在' % user
# 		exit()
# 	if Lock(user,False):
# 		print u'用户%s 被锁定' % user
# 		exit()
# 	passwd=raw_input('Login Password:')
# 	if Login(user,passwd):
# 		print u'登陆成功'
# 		ShopCar('admin',10,[])
# 		menu(user)
# 	else:
# 		print u'用户%s密码不对,还有%s次机会 ' % (user,Lock(user,True))
# 		main()
# if __name__=='__main__':
# 	f_user=file(user_file,'r')
# 	main()
# 	f_user.close()
# 购物车小程序
## 作者介绍
- Author:huyuedong
- Day02 Blog:http://www.cnblogs.com/huyuedong/p/5722478.html

## 功能介绍：
- 个人用户：验证用户名密码后可购买商品。
- 商家用户：验证用户名密码后可以：1.查看商品列表。2.修改商品价格


## 环境依赖：
- Python3.0+

## 目录结构：

```python
shopping_mall.py   # 主程序文件
shopping_data      # 商品数据文件 [商品名称:价格]
user_data          # 用户数据文件 [用户类型:用户名:密码:是否锁定:余额]
```

## 运行说明：
- 把shopping_mall.py、shopping_data、user_data三个文件放到同一目录下运行即可。
- 个人用户默认用户名：test 密码：test
- 商家用户默认用户名：admin 密码：admin

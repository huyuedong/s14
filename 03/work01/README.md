# 修改HAProxy配置文件
## 作者介绍
- Author:huyuedong
- Day03-Blog:http://www.cnblogs.com/huyuedong/p/5747651.html

## 功能介绍：
- 查询配置：输入域名即可显示相关backend配置
- 添加配置：输入字典格式的字符串即可添加相应的backend配置
- 删除配置：输入字典格式的字符串即可删除相应的backend配置

## 环境依赖：
- Python3.0+

## 目录结构：
- edit_ha.py为主程序文件。
- haproxy.conf为HAProxy的配置文件。


## 运行说明：

> 把edit_ha.py和haproxy.conf放在同一个目录运行。

1. 查询。如：输入 www.baidu.com 即可显示该域名下的backend。
2. 添加。如：输入下列字符串即可添加配置

```
{"backend":"www.qq.com","record":{"server":"100.1.7.99","weight":20,"maxconn":3000}}
```

3.删除。如：输入下列字符串即可删除配置

```
{"backend":"www.baidu.com","record":{"server":"100.1.7.93","weight":20,"maxconn":3000}}
```


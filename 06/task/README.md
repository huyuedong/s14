# 选课系统小程序

## 作者介绍
- Author:huyuedong
- Day06-Blog:http://www.cnblogs.com/huyuedong/articles/5815165.html

## 功能介绍
1. 学校管理系统：新建课程、新建班级、新建讲师
2. 讲师管理系统（未完成）：管理班级、选择班级、查看学员列表、修改学员成绩
3. 学员管理系统（未完成）：注册、缴费、选择班级

## 运行说明
- Python环境：3.0+
- 起始程序：运行src目录下面main.py

## 目录说明
homework06
├── bin 
│   └── __init__.py
├── conf 
── settings.py 配置文件
├── db 数据文件目录
│   ├── 20160901_074059  数据文件（pickle）
│   └── __init__.py
├── __init__.py
  ── README.md
└── src 核心程序目录
    ├── db_handle.py 处理数据文件接口
    ├── db_save.py  读写数据文件接口
    ├── __init__.py
    ├── main.py 程序入口
    ├── manage.py  主逻辑程序
    └── role.py  主程序
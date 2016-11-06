#!/usr/bin/env python
#-*-coding:utf-8-*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://root:123456@192.168.92.201/test?charset=utf8",
                       encoding='utf-8',echo=True)

Base = declarative_base()  # 生成ORM基类

class User(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine) #创建表结构

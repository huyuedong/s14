#!/usr/bin/env python
#-*-coding:utf-8-*-

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy import ForeignKey

engine = create_engine("mysql+pymysql://root:123456@192.168.92.201/test?charset=utf8",
                       encoding='utf-8',echo=True)

Base = declarative_base()  # 生成ORM基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))

    user = relationship("User", backref="addresses")

    def __repr__(self):
        return "<Address(enail_address='%s')>" % self.email_address

# Base.metadata.create_all(engine)  #创建表结构
Session_class = sessionmaker(bind=engine)
session = Session_class()

# session.add(User(name='Jack',password='123'))
# session.add(Address(email_address="xxx@jd.com",user_id='2'))
obj = session.query(User).filter(User.name=='David').all()[0]
print(obj.addresses)

# obj.addresses = [Address(email_address='David@jd.com'),
#                  Address(email_address='David@xxx.com')]
# print(obj.addresses)
# for i in obj.addresses:
#     print(i)
# addr_obj = session.query(Address).first()
# print(addr_obj.user.name)

# print(session.query(Address).all())

session.commit()
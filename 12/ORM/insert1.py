#!/usr/bin/env python
#-*-coding:utf-8-*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql://root:123456@192.168.92.201/test?charset=utf8",encoding='utf-8',echo=True)

Base = declarative_base()  # 生成ORM基类

class User(Base):
    __tablename__='users'  # 表名
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',password='%s')>" % (self.name,self.password)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

user_obj = User(name="Jack",password="dave008")
# print("+++++++++ obj.name ++++++++++",user_obj.name,user_obj.id)
# my_user = Session.query(User).filter_by(name="David").first()
# my_user = Session.query(User.name.label('name_label')).all()
# my_user = Session.query(User).filter(User.name.like("Da%")).count()
my_user = Session.query(User).order_by(User.id)[0:1]
# my_user = Session.query(User).filter(User.name=="David").update({'password':123})    # 修改
print("++++++",my_user,"++++++",type(my_user))
# Session.add(user_obj)
# Session.commit()

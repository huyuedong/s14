#!/usr/bin/env python
#-*-coding:utf-8-*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.92.201/huydb",
                       encoding='utf-8',echo=False)

Base = declarative_base()

class User(Base):
    __tablename__='ORM_USER'
    id = Column(INTEGER,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" % (self.id,self.name)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()
# user_obj = User(name='David',password='123456')
# user_obj2 = User(name='Jack',password='666666')
# print(user_obj.name,user_obj.id)
# Session.add(user_obj)
# Session.add(user_obj2)
# print(user_obj.name,user_obj.id)
my_user = Session.query(User).filter_by(name='David').update({"password":"0000000"})
# my_user.update({"name":"one step"})
# print(my_user.id,my_user.name,my_user.password)
Session.commit()
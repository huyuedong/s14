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

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer, ForeignKey("new_address.id"))
    shipping_address_id = Column(Integer, ForeignKey("new_address.id"))

    billing_address = relationship("Address",foreign_keys=[billing_address_id])
    shipping_address = relationship("Address",foreign_keys=[shipping_address_id])

class Address(Base):
    __tablename__ = 'new_address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

# Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
session = Session_class()

addr1 = Address(street="fengtai",city="beijing",state="china")
addr2 = Address(street="haidian",city="beijing",state="china")
addr3 = Address(street="fangshan",city="beijing",state="china")

c1 = Customer(name="user1",billing_address_id="2",shipping_address_id="3")
c2 = Customer(name="user2",billing_address_id="1",shipping_address_id="3")
c3 = Customer(name="user3",billing_address_id="3",shipping_address_id="3")

session.add_all([addr1,addr2,addr3,c1,c2,c3])
session.commit()
#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
import orm_b1
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine,String,Integer

Session_class = sessionmaker(bind=engine)
session = Session_class()

addr1 = Address(street="fengtai",city="beijing",state="china")
addr2 = Address(street="haidian",city="beijing",state="china")
addr3 = Address(street="fangshan",city="beijing",state="china")

c1 = Customer(name="user1",billing_address_id="2",shipping_address_id="3")
c1 = Customer(name="user2",billing_address_id="1",shipping_address_id="3")
c1 = Customer(name="user3",billing_address_id="3",shipping_address_id="3")
# session.commit()


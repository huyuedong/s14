#!/usr/bin/env python
#-*-coding:utf-8-*-
import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey,engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import settings

Conn = create_engine(settings.ConnMySQL,echo=True)

Base = declarative_base()

user_m2m_bindhost = Table('user_m2m_bindhost',Base.metadata,
                      Column('bastionuser_id',Integer,ForeignKey('bastion_user.id')),
                      Column('host_id',Integer,ForeignKey('host_group.id')),
                      )

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    ip = Column(String(64),unique=True)    # IP唯一
    hostname = Column(String(64))
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostGroup(Base):
    __tablename__ = 'hostgroup'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    bind_hosts = relationship("BindHost",secondary="bindhost_m2m_hostgroup",backref="host_group")

class BastionUser(Base):
    __tablename__ = 'bastion_user'
    id = Column(Integer,primary_key=True)
    username = Column(String(32))
    passowrd = Column(String(128))

    bind_hosts = relationship("BindHosst", secondary='user_m2m_bindhost',backref='bastion_user')

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    username = Column(String(32))
    password = Column(String(128))



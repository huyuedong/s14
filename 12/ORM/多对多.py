#!/usr/bin/env python
#-*-coding:utf-8-*-
from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey,engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@192.168.92.201/test?charset=utf8",
                       encoding='utf-8',echo=True)

Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

# Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
s = Session_class()

# 插入数据
b1 = Book(name="book1",pub_date="2016-05-08")
b2 = Book(name="book2",pub_date="2017-06-08")
b3 = Book(name="book3",pub_date="2018-07-08")
b4 = Book(name="book4",pub_date="2019-08-08")
b5 = Book(name="book5",pub_date="2020-08-08")

a1 = Author(name="Alex")
a2 = Author(name="Jack")
a3 = Author(name="Rain")
a4 = Author(name="David")

b1.authors = [a1,a2]
b2.authors = [a1,a2,a3]
b5.authors = [a4]

s.add_all([b1,b2,b3,b4,b5,a1,a2,a3,a4])
s.commit()
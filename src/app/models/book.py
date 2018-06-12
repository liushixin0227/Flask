#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 16:58
# @Author  : LiuShixin
# @Site    : 
# @File    : book.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未知')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    page = Column(Integer)
    pubdata = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

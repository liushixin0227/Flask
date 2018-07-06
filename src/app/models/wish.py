#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/07/01 22:02
# @Author  : LiuShixin
# @Site    : 
# @File    : wish.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from src.app.models.base import Base


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)
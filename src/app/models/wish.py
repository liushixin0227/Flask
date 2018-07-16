#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/07/01 22:02
# @Author  : LiuShixin
# @Site    : 
# @File    : wish.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, func, desc
from sqlalchemy.orm import relationship

from src.app.models.base import Base, db
from src.app.spider.FishBook import FishBook


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_gift_count(cls, isbn_list):
        from src.app.models.gift import Gift

        gidt_count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        gift_count_dict = [{'count': w[0], 'isbn': w[1]} for w in gidt_count_list]
        return gift_count_dict

    @classmethod
    def get_user_wishs(cls, uid):
        wishs = Wish.query.filter_by(launched=False, uid=uid).order_by(
            desc(Wish.create_time)).all()
        return wishs

    @property
    def book(self):
        fishbook = FishBook()
        fishbook.search_by_isbn(self.isbn)
        return fishbook.first

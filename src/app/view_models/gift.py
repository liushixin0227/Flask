#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/07/03 17:37
# @Author  : LiuShixin
# @Site    : 
# @File    : gift.py
# @Software: PyCharm
from collections import namedtuple

from src.app.view_models.book import BookViewModle


class MyGifts:
    def __init__(self, gift_of_mine, wish_count_list):
        self.gifts = []
        self.__gift_of_mine = gift_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        gifts = []
        for gift in self.__gift_of_mine:
            my_gift = self.__matching(gift)
            gifts.append(my_gift)
        return gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModle(gift.book),
            'id': gift.id
        }
        return r

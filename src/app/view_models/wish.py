#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 0010 13:21
# @Author  : Liushixin
# @Site    : 
# @File    : wish.py
# @Software: PyCharm
from src.app.view_models.book import BookViewModle


class MyWishs:
    def __init__(self, wish_of_mine, gift_count_list):
        self.wishs = []
        self.__wish_of_mine = wish_of_mine
        self.__gift_count_list = gift_count_list
        self.wishs = self.__parse()

    def __parse(self):
        wishs = []
        for wish in self.__wish_of_mine:
            my_wish = self.__matching(wish)
            wishs.append(my_wish)
        return wishs

    def __matching(self, wish):
        count = 0
        for gift_count in self.__gift_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['count']
        r = {
            'wishes_count': count,
            'book': BookViewModle(wish.book),
            'id': wish.id
        }
        return r

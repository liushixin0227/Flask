#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 13:11
# @Author  : Aries
# @Site    : 
# @File    : FishBook.py
# @Software: PyCharm

from src.app.libs.get_http import Http
from flask import current_app


class FishBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.__class__.isbn_url.format(isbn)
        result = Http.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        url = self.__class__.keyword_url.format(keyword, current_app.config['PRO_PAGE'],
                                                self.__class__.calcurlate_start(page))
        result = Http.get(url)
        self.__fill_collection(result)

    @classmethod
    def calcurlate_start(self, page):
        return (page - 1) * current_app.config['PRO_PAGE']

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

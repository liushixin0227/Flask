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

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PRO_PAGE'], cls.calcurlate_start(page))
        result = Http.get(url)
        return result

    @staticmethod
    def calcurlate_start(page):
        return (page - 1) * current_app.config['PRO_PAGE']
